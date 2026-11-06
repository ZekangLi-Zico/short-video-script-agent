"""Compare saved paired experiments; no execution or semantic grading."""
import csv,json
from collections import Counter
from pathlib import Path
B=Path(__file__).resolve().parent;OLD=B.parent/'realistic-50-v4-20261104'
load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
old=load(OLD/'results.json');new=load(B/'results.json')
oldrows={r['case']:r for r in old['runs']};newrows={r['case']:r for r in new['runs']}
def trace(folder):
 p=folder/'trace.jsonl'
 return [json.loads(s) for s in p.read_text(encoding='utf-8').splitlines()] if p.exists() else None
def reviews(t):return None if t is None else sum(x['action']=='check_requirements' for x in t)
rows=[]
for key,n in sorted(newrows.items()):
 o=oldrows[key];ot=trace(OLD/'runs'/key);nt=trace(B/'runs'/n['folder'])
 rows.append({'case':key,'name':n['name'],'before_status':o['status'],'after_status':n['status'],'before_steps':o['steps'],'after_steps':n['steps'],'before_responses':o['responses'],'before_response_lower_bound':o.get('response_lower_bound'),'after_responses':n['responses'],'before_reviews':reviews(ot),'after_reviews':reviews(nt),'before_seconds':o['seconds'],'after_seconds':n['seconds'],'before_complete_record':ot is not None,'after_complete_record':True,'after_folder':n['folder']})
paired=[r for r in rows if r['before_responses'] is not None]
summary={'paired_cases':len(rows),'before_statuses':dict(Counter(r['before_status'] for r in rows)),'after_statuses':dict(Counter(r['after_status'] for r in rows)),'transitions':dict(Counter(r['before_status']+' -> '+r['after_status'] for r in rows)),'before_complete_records':sum(r['before_complete_record'] for r in rows),'after_complete_records':sum(r['after_complete_record'] for r in rows),'after_responses':sum(r['after_responses'] for r in rows),'exact_comparable_subset':{'cases':len(paired),'before_responses':sum(r['before_responses'] for r in paired),'after_responses':sum(r['after_responses'] for r in paired),'before_reviews':sum(r['before_reviews'] for r in paired),'after_reviews':sum(r['after_reviews'] for r in paired)},'note':'Same predefined briefs, single stochastic runs; not blinded, randomized or a causal estimate. Baseline is v4 before editorial-note separation; all available paired records used. Semantic assessment is recorded separately.','rows':rows}
(B/'comparison.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if rows:
 with (B/'前后对照.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(json.dumps({k:v for k,v in summary.items() if k!='rows'},ensure_ascii=False))
