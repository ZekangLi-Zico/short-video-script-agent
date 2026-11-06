"""Reproduce observed symptoms from immutable real-model records, not synthetic claims."""
import argparse,json,statistics
from collections import defaultdict
from datetime import datetime
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
p=argparse.ArgumentParser();p.add_argument('--campaign',default='realistic-50-v5-20261104');p.add_argument('--check',action='store_true');args=p.parse_args()
C=B.parent/args.campaign;load=lambda p:json.loads(p.read_text(encoding='utf8'))
generic=set(load(ROOT/'data/brand_rules.json')['allowed_titles']);titles=[];fail=[];latency=defaultdict(list);tokens=defaultdict(list);wall=[]
for d in sorted((C/'runs').glob('V*')):
    if not (d/'capture.json').exists():continue
    out=load(d/'output.json');m=load(d/'manifest.json')
    if (out.get('script') or {}).get('title') in generic:titles.append(d.name)
    wall.append((datetime.fromisoformat(m['finished_at'])-datetime.fromisoformat(m['started_at'])).total_seconds())
    trace=[json.loads(x) for x in (d/'trace.jsonl').read_text(encoding='utf8').splitlines()]
    call_actions={t[k]['call_id']:('review' if k=='review_model' else t['action']) for t in trace for k in ('model','review_model') if t.get(k)}
    for q in (d/'diagnostics').glob('*.json'):
        x=load(q);kind=call_actions.get(x['call_id'],'failed');elapsed=(datetime.fromisoformat(x['finished_at'])-datetime.fromisoformat(x['started_at'])).total_seconds()
        latency[kind].append(elapsed)
        u=x.get('metadata',{}).get('usage',{})
        if u.get('input_tokens'):tokens[kind].append(u['input_tokens'])
        if not x.get('response_received'):fail.append({'case':d.name,'call':x['call_id'],'error':x.get('error_code'),'seconds':round(elapsed,1)})
result={'campaign':args.campaign,'runs':len(wall),'generic_title_cases':titles,'failed_calls':fail,'median_task_seconds':round(statistics.median(wall),1),'calls_by_action':{k:{'calls':len(v),'median_seconds':round(statistics.median(v),1),'max_seconds':round(max(v),1),'median_input_tokens':statistics.median(tokens[k]) if tokens[k] else None} for k,v in latency.items()}}
(B/(args.campaign+'-diagnosis.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False))
if args.check:raise SystemExit(int(len(titles)>=10 or len(fail)>=2 or statistics.median(wall)>=300))
