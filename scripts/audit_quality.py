"""Audit preserved files and v3 run evidence without rewriting older artifacts."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from src.tools import ROOT, read_json
from scripts.verify_evidence import verify_run


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    campaign=ROOT/'evaluations/quality-v3-20261104'
    freeze=read_json(campaign/'freeze.json')
    changed=[]
    for rel, digest in freeze['preserved_files'].items():
        p=ROOT/rel
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest: changed.append(rel)
    cases_unchanged=hashlib.sha256((campaign/'cases.json').read_bytes()).hexdigest()==freeze['cases_sha256']
    rows=[]
    groups=[ROOT/'examples/mock',ROOT/'examples/live',ROOT/'examples/repairs',
            ROOT/'evaluations/realistic-50-20261103/runs',campaign]
    for group in groups:
        for file in sorted(group.rglob('output.json')):
            directory=file.parent
            if not all((directory/n).is_file() for n in ('input.json','manifest.json','trace.jsonl','data_snapshot.json')): continue
            try: errors=verify_run(directory)
            except Exception as exc: errors=['replay_exception:'+type(exc).__name__]
            rows.append({'run':directory.relative_to(ROOT).as_posix(),'passed':not errors,'errors':errors})
    # Frozen correspondence only applies to the planned CLI campaign; UI variants are documented separately.
    cases={c['id']:c for c in read_json(campaign/'cases.json')}
    for group in ('live-v3-attempt1','live-v2-comparison'):
        for file in sorted((campaign/group).glob('*/input.json')):
            expected=dict(cases[file.parent.name]['request'])
            if group=='live-v2-comparison':
                expected.pop('expression_mode',None); expected.pop('duration_mode',None)
            if read_json(file)!=expected: changed.append(file.relative_to(ROOT).as_posix()+': case mismatch')
    result={'checked_at':datetime.now(timezone.utc).isoformat(),'preserved_files_checked':len(freeze['preserved_files']),
            'preserved_changed':changed,'frozen_cases_unchanged':cases_unchanged,
            'runs_checked':len(rows),'runs_passed':sum(r['passed'] for r in rows),'runs':rows,
            'passed':not changed and cases_unchanged and all(r['passed'] for r in rows),
            'scope':'File integrity, deterministic replay, review structure/hash and revision diff consistency; not semantic truth or remote model authentication.'}
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists(): parser.error('Refuse replacing an audit; select a new output')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='runs'},ensure_ascii=False))
    if not result['passed']:
        print(json.dumps([r for r in rows if not r['passed']],ensure_ascii=False))
    return 0 if result['passed'] else 1


if __name__=='__main__': raise SystemExit(main())
