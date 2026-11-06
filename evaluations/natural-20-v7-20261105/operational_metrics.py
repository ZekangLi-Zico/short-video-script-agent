"""Observable latency/title/attempt metrics from saved artifacts; no quality inference."""
import json,statistics
from collections import Counter,defaultdict
from datetime import datetime
from pathlib import Path
B=Path(__file__).resolve().parent;OLD=B.parent/'realistic-50-v6-20261105'
load=lambda p:json.loads(p.read_text(encoding='utf8'))
seconds=lambda d:round((datetime.fromisoformat(d['finished_at'])-datetime.fromisoformat(d['started_at'])).total_seconds(),2)
def distribution(values):
    v=sorted(values)
    return {'n':len(v),'median':round(statistics.median(v),2),'p90':v[max(0,__import__('math').ceil(len(v)*.9)-1)],'max':max(v)} if v else None
def metrics(base):
    rows=[];calls=[];by_action=defaultdict(list);titles=[]
    for d in sorted((base/'runs').glob('V[0-9][0-9]')):
        if d.name not in {c['id'] for c in load(B/'cases.json')} or not (d/'capture.json').exists():continue
        o=load(d/'output.json');m=load(d/'manifest.json');trace=[json.loads(line) for line in (d/'trace.jsonl').read_text(encoding='utf8').splitlines()]
        diags={p.stem:load(p) for p in (d/'diagnostics').glob('*.json')}
        for t in trace:
            for key in ('model','review_model'):
                if key not in t:continue
                meta=t[key];diag=diags[meta['call_id']];kind='review' if key=='review_model' else t['action']
                row={'case':d.name,'call_id':meta['call_id'],'action':kind,'seconds':seconds(diag),
                     'reasoning_effort':meta.get('reasoning_effort','inherited (not recorded)'),
                     'input_tokens':meta.get('usage',{}).get('input_tokens',0),
                     'output_tokens':meta.get('usage',{}).get('output_tokens',0),
                     'recovered_attempts':meta.get('recovered_attempts',[])}
                calls.append(row);by_action[kind].append(row['seconds'])
        failures=[{'call_id':key,'error_code':v.get('error_code'),'seconds':seconds(v)} for key,v in diags.items() if not v.get('response_received')]
        title=(o.get('script') or {}).get('title')
        if title:titles.append({'case':d.name,'title':title})
        rows.append({'case':d.name,'status':o['status'],'seconds':seconds(m),'responses':m['model_responses'],
                     'attempts':len(diags),'failed_attempts':failures,'title':title,
                     'bundled_local_checks':sum(len(t.get('preflight_checks',[])) for t in trace),
                     'invalid_actions':sum(t['action']=='invalid_model_action' for t in trace),
                     'review_responses':sum('review_model' in t for t in trace)})
    return {'tasks':distribution([r['seconds'] for r in rows]),'responses':len(calls),
            'attempts':sum(r['attempts'] for r in rows),'failed_attempts':sum(len(r['failed_attempts']) for r in rows),
            'recovered_calls':sum(bool(c['recovered_attempts']) for c in calls),
            'invalid_actions':sum(r['invalid_actions'] for r in rows),
            'call_seconds_by_action':{k:distribution(v) for k,v in by_action.items()},
            'input_tokens':sum(c['input_tokens'] for c in calls),'output_tokens':sum(c['output_tokens'] for c in calls),
            'titles':titles,'rows':rows,'calls':calls}
result={'old':metrics(OLD),'new':metrics(B),'note':'Same frozen briefs, both four-page concurrency; different time windows and model service conditions. Counts are not billing amounts; title specificity requires reading.'}
(B/'operational-metrics.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:{n:v for n,v in x.items() if n not in {'rows','calls','titles'}} for k,x in result.items() if k!='note'},ensure_ascii=False))
