"""Compute observable paired changes; no automatic creative-quality verdict."""
import csv,json,re
from collections import Counter
from pathlib import Path
B=Path(__file__).resolve().parent;OLD=B.parent/'realistic-50-v41-20261104'
load=lambda p:json.loads(p.read_text(encoding='utf8'))
rows=[]
for c in load(B/'cases.json'):
    d=B/'runs'/c['id']
    if not (d/'capture.json').exists():continue
    old=load(OLD/'runs'/c['id']/'output.json');new=load(d/'output.json')
    def metric(o):
        script=o.get('script') or {}; blocks=[b for s in script.get('shots',[]) for b in s['blocks']]
        citations=(o.get('rules_check') or {}).get('citations',[])
        return dict(status=o['status'],responses=o['metadata']['model_responses'],steps=o['metadata']['steps'],
            seconds=(o.get('duration') or {}).get('total_seconds'),shots=len(script.get('shots',[])),format=script.get('format_version',1),
            rewritten_citations=sum(c.get('text',c['quote'])!=c['quote'] for c in citations),
            english_fact_blocks=sum(bool(b['source_id'] and re.search('[A-Za-z]',b['text']) and not re.search('[\u3400-\u9fff]',b['text'])) for b in blocks),
            stale_notes=bool(re.search('待估时|待重新检查|尚待.*核验',script.get('editor_notes',''))))
    a,z=metric(old),metric(new)
    rows.append({'case':c['id'],'name':c['name'],**{'old_'+k:v for k,v in a.items()},**{'new_'+k:v for k,v in z.items()}})
summary={'paired':len(rows),'old_statuses':dict(Counter(r['old_status'] for r in rows)),
         'new_statuses':dict(Counter(r['new_status'] for r in rows)),
         'old_responses':sum(r['old_responses'] for r in rows),'new_responses':sum(r['new_responses'] for r in rows),
         'status_changes':[dict(case=r['case'],old=r['old_status'],new=r['new_status']) for r in rows if r['old_status']!=r['new_status']],
         'rewritten_citations':sum(r['new_rewritten_citations'] for r in rows),
         'english_fact_cases':[r['case'] for r in rows if r['new_english_fact_blocks']],
         'stale_note_cases':[r['case'] for r in rows if r['new_stale_notes']],
         'runs':rows}
(B/'comparison.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
if rows:
    with (B/'前后对照.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(json.dumps({k:v for k,v in summary.items() if k!='runs'},ensure_ascii=False))
