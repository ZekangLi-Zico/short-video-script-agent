"""Audit v4 evidence and preserved history without invoking any model."""
import argparse
import hashlib
import json
from datetime import datetime,timezone
from pathlib import Path
from scripts.verify_evidence import verify_run
from src.tools import ROOT,read_json


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--require-complete',action='store_true')
    args=parser.parse_args()
    base=ROOT/'evaluations/finite-v4-20261104'
    baseline=read_json(base/'baseline.json')
    final_source=read_json(base/'tested-source-final.json')
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    changed=[name for name,digest in baseline['preserved_sha256'].items() if not (ROOT/name).is_file() or sha(ROOT/name)!=digest]
    source_changed=[name for name,digest in final_source.items() if sha(ROOT/name)!=digest]
    rows=[]
    original={c['id']:c for c in read_json(ROOT/'evaluations/realistic-50-v3-20261104/cases.json')}
    for group in ('live','live-final','web'):
        for file in sorted((base/group).glob('*/output.json')):
            folder=file.parent; output=read_json(file); manifest=read_json(folder/'manifest.json')
            experiment=read_json(folder/'experiment.json')
            expected=original[experiment['source_case']]['request']
            errors=verify_run(folder)
            if read_json(folder/'input.json')!=expected:errors.append('input changed')
            if manifest['provider']!='codex' or manifest['evidence_kind']!='real_model' or manifest['model_responses']<=0:
                errors.append('not evidence of an actual Codex response')
            if group in {'live-final','web'} and experiment.get('source_sha256')!=final_source:
                errors.append('source mismatch')
            if read_json(folder/'run.json')['state']!='finished':errors.append('final save marker missing')
            trace=[json.loads(line) for line in (folder/'trace.jsonl').read_text(encoding='utf-8').splitlines()]
            for step in trace:
                for key in ('model','review_model'):
                    if key in step:
                        call_id=step[key]['call_id']
                        diagnostic=read_json(folder/'diagnostics'/(call_id+'.json'))
                        if not diagnostic['response_received'] or diagnostic['metadata']!=step[key]:
                            errors.append('diagnostic does not match recorded model response')
            rows.append({'group':group,'case':folder.name,'source_case':experiment['source_case'],
                         'injection':experiment['injection'],'status':output['status'],
                         'steps':manifest['steps'],'model_responses':manifest['model_responses'],
                         'seconds':(output.get('duration') or {}).get('total_seconds'),
                         'review_calls':sum(t['action']=='check_requirements' for t in trace),
                         'errors':errors,'path':folder.relative_to(ROOT).as_posix()})
    required={'V26','V27','V28','V29','V46','cleanup_lock','runtime_exception','process_exit'}
    missing=sorted(required-{r['case'] for r in rows if r['group']=='live-final'})
    if not any(r['group']=='web' for r in rows):missing.append('web/V01')
    report={'verified_at':datetime.now(timezone.utc).isoformat(),'old_files_checked':len(baseline['preserved_sha256']),
            'old_files_changed':changed,'final_source_changed':source_changed,
            'backup_source_zip_verified':sha(ROOT/baseline['source_archive'])==baseline['source_zip_sha256'],
            'runs':rows,'missing_final_runs':missing,
            'note':'Saved-record and hash audit only; no model calls, no semantic correctness guarantee.'}
    (base/'audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='runs'},ensure_ascii=False))
    print(json.dumps(rows,ensure_ascii=False))
    return int(bool(changed or source_changed or any(r['errors'] for r in rows) or not report['backup_source_zip_verified'] or (args.require_complete and missing)))


if __name__=='__main__':raise SystemExit(main())
