"""Print original brief and actual unreviewed output; never generate inputs."""
import json,sys
from pathlib import Path
B=Path(__file__).resolve().parent
load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
for p in sorted((B/'runs').glob('*/capture.json')):
 d=p.parent
 if (d/'review.json').exists() or (sys.argv[1:] and d.name not in sys.argv[1:]):continue
 cap=load(p)
 if not cap['responses']:continue
 print('\nCASE',d.name)
 print('BRIEF',json.dumps(load(d/'brief.json')['request'],ensure_ascii=False))
 x=load(d/'output.json');print('RESULT',x['status'],x['message'])
 print('SCRIPT',json.dumps(x.get('script'),ensure_ascii=False))
 print('TIMING',json.dumps(x.get('duration'),ensure_ascii=False))
 for line in (d/'trace.jsonl').read_text(encoding='utf-8').splitlines():
  t=json.loads(line);o=t['observation']
  if o.get('ok') is False or o.get('passed') is False:
   print('FAILED OBSERVATION',t['step'],t['action'],json.dumps(o,ensure_ascii=False))
 print('PACING',json.dumps((x.get('requirements_check') or {}).get('pacing'),ensure_ascii=False))
