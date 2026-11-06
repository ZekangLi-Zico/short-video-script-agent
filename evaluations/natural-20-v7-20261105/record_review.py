"""Store the developer's actual read-through; no automatic fluency inference."""
import argparse,json
from datetime import datetime,timezone
from pathlib import Path
B=Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument('case');p.add_argument('readiness');p.add_argument('comparison');p.add_argument('note');p.add_argument('--remaining',default='')
a=p.parse_args()
old=next(r for r in json.loads((B/'baseline-readthrough.json').read_text(encoding='utf8'))['rows'] if r['case']==a.case)
d=B/'runs'/a.case
assert (d/'capture.json').exists()
assert a.readiness in ['可直接试配音','需局部改写','需整体重写','静音稿不适用','未成稿']
assert a.comparison in ['改善','相当','退步','静音单列']
record={'case':a.case,'reviewed_at':datetime.now(timezone.utc).isoformat(),'old':old,'readiness':a.readiness,'comparison':a.comparison,'note':a.note,'remaining':a.remaining,'method':'开发助手逐条阅读实际文案及对应需求，非独立人类盲评或实际配音。'}
with (d/'review.json').open('x',encoding='utf8') as f:json.dump(record,f,ensure_ascii=False,indent=2)
print(a.case,a.readiness,a.comparison)
