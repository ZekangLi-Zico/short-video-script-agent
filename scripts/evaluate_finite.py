"""Explicit real-Codex regression runs; controlled faults are never hidden."""
import argparse
import contextlib
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from src.providers import CodexModel
from src.recording import run_recorded, recover_run
from src.tools import ROOT, ToolBox, read_json
from scripts.verify_evidence import verify_run

SOURCE_CASES = ROOT/'evaluations/realistic-50-v3-20261104/cases.json'
CASES = {'V26':'none','V27':'none','V28':'none','V29':'none','V46':'none',
         'cleanup_lock':'cleanup_lock_once','runtime_exception':'exception_after_draft',
         'process_exit':'process_exit_after_draft'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',required=True,choices=CASES)
    parser.add_argument('--output',required=True)
    parser.add_argument('--recover',action='store_true')
    args=parser.parse_args()
    directory=Path(args.output)
    if args.recover:
        assert args.case=='process_exit'
        recover_run(directory)
    else:
        if directory.exists():parser.error('Refuse replacing an existing experiment')
        original=next(c for c in read_json(SOURCE_CASES) if c['id']==(args.case if args.case.startswith('V') else 'V01'))
        request=original['request']
        directory.mkdir(parents=True)
        annotation={'case':args.case,'source_case':original['id'],'request_unchanged':True,
                    'injection':CASES[args.case], 'provider':'codex',
                    'started_at':datetime.now(timezone.utc).isoformat(),
                    'note':'Actual model responses; faults, if any, are controlled host experiments, not naturally observed failures.'}
        annotation['source_sha256']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for name in ('src','web','data') for p in (ROOT/name).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
        (directory/'experiment.json').write_text(json.dumps(annotation,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        injection_log=[]
        def progress(event):
            if CASES[args.case] in {'exception_after_draft','process_exit_after_draft'} and event['kind']=='step' and event['script']:
                # run_recorded has flushed the checkpoint before this callback.
                (directory/'injection-observed.json').write_text(json.dumps({'injection':CASES[args.case],
                    'after_step':event['step'],'checkpoint_sha256':hashlib.sha256((directory/'checkpoint.json').read_bytes()).hexdigest()})+'\n',encoding='utf-8')
                if CASES[args.case]=='process_exit_after_draft':os._exit(86)
                raise RuntimeError('controlled runtime interruption after a real-model draft')
        cleanup=tempfile.TemporaryDirectory.cleanup
        def locked_once(workspace):
            if not injection_log:
                injection_log.append({'injection':'cleanup_lock_once','directory_name':Path(workspace.name).name})
                # Detach then fail inside the real cleanup path, like Windows rmtree.
                with patch.object(tempfile.TemporaryDirectory,'_rmtree',side_effect=PermissionError(32,'controlled cleanup lock')):
                    return cleanup(workspace)
            return cleanup(workspace)
        context=patch.object(tempfile.TemporaryDirectory,'cleanup',locked_once) if CASES[args.case]=='cleanup_lock_once' else contextlib.nullcontext()
        with context:
            result=run_recorded(directory,request,CodexModel(),ToolBox(),on_event=progress)
        if injection_log:
            (directory/'injection-observed.json').write_text(json.dumps(injection_log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    output=read_json(directory/'output.json')
    errors=verify_run(directory)
    metadata=output['metadata']
    review_calls=[json.loads(line) for line in (directory/'trace.jsonl').read_text(encoding='utf-8').splitlines() if json.loads(line)['action']=='check_requirements']
    summary={'case':args.case,'status':output['status'],'model_responses':metadata['model_responses'],
             'provider':metadata['provider'],'steps':metadata['steps'],
             'seconds':(output.get('duration') or {}).get('total_seconds'),
             'review_calls':len(review_calls),
             'review_has_current_duration':all(t['arguments'].get('duration_check') is not None for t in review_calls) if review_calls else None,
             'replay_errors':errors,'message':output['message']}
    (directory/'evaluation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))
    return 0 if metadata['provider']=='codex' and metadata['model_responses']>0 and not errors else 2


if __name__=='__main__':raise SystemExit(main())
