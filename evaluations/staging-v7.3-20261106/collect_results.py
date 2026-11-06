"""Read saved webpage outputs and compare structure; never grade with expected answers."""
import json
from datetime import datetime
from pathlib import Path
from scripts.verify_evidence import verify_run

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
IDS={'hallway':'30769563136641ea8660d4a3c6cc355f','chess':'e728b9dabc21453387bb89c4e55f4fe7'}

def read(p): return json.loads(p.read_text(encoding='utf-8'))

def metrics(run_id):
    p=ROOT/'outputs/web'/run_id
    r=read(p/'output.json');s=r['script'];m=r['metadata']
    diagnostics=[read(d) for d in (p/'diagnostics').glob('*.json')]
    blocks=[b for shot in s['shots'] for b in shot['blocks']]
    return dict(web_run_id=run_id,status=r['status'],version=m['app_version'],format_version=s.get('format_version',1),
                elapsed_seconds=round((datetime.fromisoformat(m['finished_at'])-datetime.fromisoformat(m['started_at'])).total_seconds(),2),
                estimated_video_seconds=r['duration']['total_seconds'],shots=len(s['shots']),
                staged_segments=sum(len(shot.get('staging',[])) for shot in s['shots']),
                silent_action_segments=sum(not any(b['beat']==stage['beat'] for b in shot['blocks'])
                                           for shot in s['shots'] for stage in shot.get('staging',[])),
                voice_blocks=sum(b.get('channel') in ('voice','both') for b in blocks),
                voice_blocks_with_speaker=sum(b.get('channel') in ('voice','both') and bool(b.get('speaker')) for b in blocks),
                model_responses=m['model_responses'],attempts=len(diagnostics),
                timeouts=sum(d.get('error_code')=='codex_timeout' for d in diagnostics),
                checks={k:bool(r.get(k,{}).get('ok') and r.get(k,{}).get('passed')) for k in ('duration','rules_check','requirements_check')},
                data_hash=m['data_hash'])

if __name__=='__main__':
    results=[]
    for case in read(OUT/'cases.json'):
        rid=IDS[case['name']];after=metrics(rid)
        before=metrics(case['previous_run_id']) if case['previous_run_id'] else None
        results.append(dict(case=case['name'],before=before,after=after,
                            input_matches_frozen=read(ROOT/'outputs/web'/rid/'input.json')==case['request'],
                            data_matches_previous=(before['data_hash']==after['data_hash']) if before else None,
                            evidence_errors=verify_run(ROOT/'outputs/web'/rid)))
    (OUT/'live-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(results,ensure_ascii=False,indent=2))
