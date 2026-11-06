"""Read saved speech before judging; never call a model or assign scores."""
import json,sys
from pathlib import Path
B=Path(__file__).resolve().parent
sys.path.insert(0,str(B.parents[1]))
from src.listening import listening_copy
load=lambda p:json.loads(p.read_text(encoding='utf8'))
cases={c['id']:c for c in load(B/'cases.json')}
for case in sys.argv[1:]:
 print('\n###',case,cases[case]['name'])
 print('需求',json.dumps(cases[case]['request'],ensure_ascii=False))
 for label,base in [('旧v6',B.parent/'realistic-50-v6-20261105'),('新v7',B)]:
  d=base/'runs'/case
  if not (d/'output.json').exists():continue
  o=load(d/'output.json');s=o.get('script');m=load(d/'manifest.json')
  print(label,'连读文案',json.dumps(listening_copy(s),ensure_ascii=False))
  if s:
   print('标题',s['title'])
   for i,shot in enumerate(s['shots'],1):
    print(i,shot['visual'])
    for b in shot['blocks']:
     if b.get('channel')=='screen':print('屏幕',b['text'])
  print('状态',o['status'],'秒',(o.get('duration') or {}).get('total_seconds'),'调用',m['model_responses'])
  trace=[json.loads(l) for l in (d/'trace.jsonl').read_text(encoding='utf8').splitlines()]
  print('动作',' → '.join(t['action'] for t in trace))
  for t in trace:
   obs=t['observation']
   if obs.get('passed') is False or obs.get('ok') is False:print('失败观察',t['action'],json.dumps(obs,ensure_ascii=False)[:1400])
