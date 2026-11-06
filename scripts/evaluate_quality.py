"""Append-only execution of pre-frozen briefs; no expected output/status inference."""
import argparse
import concurrent.futures
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--cases',required=True)
    parser.add_argument('--output',required=True)
    parser.add_argument('--code-root',default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument('--provider',choices=['codex','mock','api'],default='codex')
    parser.add_argument('--case',action='append')
    parser.add_argument('--legacy',action='store_true')
    parser.add_argument('--workers',type=int,choices=[1,2],default=1)
    args=parser.parse_args()
    root=Path(args.code_root).resolve()
    sys.path.insert(0,str(root))
    from src.agent import Agent
    from src.cli import make_model
    from src.reporting import save_run
    from src.tools import ToolBox
    cases_path=Path(args.cases).resolve()
    freeze=json.loads(cases_path.with_name('freeze.json').read_text('utf-8'))
    digest=hashlib.sha256(cases_path.read_bytes()).hexdigest()
    if digest != freeze['cases_sha256']: parser.error('Frozen briefs changed')
    cases=json.loads(cases_path.read_text('utf-8'))
    if set(args.case or [])-{c['id'] for c in cases}: parser.error('Unknown case')
    cases=[c for c in cases if not args.case or c['id'] in args.case]
    output=Path(args.output).resolve()
    output.mkdir(parents=True,exist_ok=True)
    for c in cases:
        if (output/c['id']).exists(): parser.error('Refuse overwrite: '+c['id'])
    hashes={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for folder in ('src','data','web') for p in (root/folder).rglob('*')
            if p.is_file() and '__pycache__' not in p.parts}
    def run(case):
        directory=output/case['id']; directory.mkdir(exist_ok=False)
        request=dict(case['request'])
        if args.legacy:
            request.pop('expression_mode',None); request.pop('duration_mode',None)
        dump(directory/'attempt.json',{'case_id':case['id'],'started_at':datetime.now(timezone.utc).isoformat(),
            'frozen_cases_sha256':digest,'code_root':str(root),'source_hashes':hashes,'legacy':args.legacy,
            'entry':'CLI through Agent.run; not a browser test','workers':args.workers})
        dump(directory/'request-started.json',request)
        tools=ToolBox(failures=case.get('faults',{}))
        model=make_model(args.provider,180)
        result=Agent(model,tools,max_steps=12).run(request)
        save_run(directory,request,result,tools)
        row={'id':case['id'],'status':result['status'],'steps':result['metadata']['steps'],
             'model_responses':result['metadata'].get('model_responses'),
             'duration':(result.get('duration') or {}).get('total_seconds'),
             'path':[t['action'] for t in result['trace']], 'message':result['message']}
        dump(directory/'result-summary.json',row)
        print(json.dumps(row,ensure_ascii=False),flush=True)
        return row
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures={executor.submit(run,c):c for c in cases}
        for future in concurrent.futures.as_completed(futures):
            c=futures[future]
            try: future.result()
            except Exception as exc:
                # Retain the interrupted attempt; do not recast it as a business outcome.
                dump(output/c['id']/'runner-error.json',{'type':type(exc).__name__,
                     'error':'runner failed; no business acceptance conclusion'})
                print(json.dumps({'id':c['id'],'runner_error':type(exc).__name__}),flush=True)


if __name__=='__main__': main()
