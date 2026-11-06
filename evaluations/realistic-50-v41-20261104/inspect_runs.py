"""Print current saved briefs and output for human/assistant review; no grading."""
import argparse,json
from pathlib import Path
B=Path(__file__).resolve().parent
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
a=argparse.ArgumentParser();a.add_argument('ids',nargs='*');args=a.parse_args()
for d in sorted((B/'runs').glob('*')):
 if not (d/'capture.json').exists() or (args.ids and d.name not in args.ids):continue
 if not args.ids and (d/'review.json').exists():continue
 c=load(d/'brief.json');o=load(d/'output.json');m=load(d/'manifest.json');ts=[json.loads(s) for s in (d/'trace.jsonl').read_text(encoding='utf-8').splitlines()]
 print(json.dumps({'case':d.name,'request':c['request'],'status':o['status'],'steps':m['steps'],'responses':m['model_responses'],'duration':o.get('duration'),'script':o.get('script'),'message':o['message'],'path':[(t['step'],t['action'],t['observation'].get('passed'),t['observation'].get('error')) for t in ts],'failed_reviews':[t['observation'] for t in ts if t['action']=='check_requirements' and not t['observation'].get('passed')]},ensure_ascii=False))
