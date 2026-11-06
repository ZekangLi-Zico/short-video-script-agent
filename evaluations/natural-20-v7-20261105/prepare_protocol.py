"""Freeze existing real briefs before writing v7; do not synthesize expected outputs."""
import hashlib,json,shutil
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
OLD=B.parent/'realistic-50-v6-20261105'
ids=['V01','V02','V03','V05','V06','V09','V11','V14','V15','V16','V17','V19','V21','V22','V25','V28','V29','V36','V45','V47']
source=json.loads((OLD/'cases.json').read_text(encoding='utf8'))
cases=[next(c for c in source if c['id']==i) for i in ids]
with (B/'cases.json').open('x',encoding='utf8') as f:json.dump(cases,f,ensure_ascii=False,indent=2)
protocol={'frozen_at':datetime.now(timezone.utc).isoformat(),'baseline':OLD.name,'cases':20,'unique_briefs':20,
 'cases_sha256':hashlib.sha256((B/'cases.json').read_bytes()).hexdigest(),'submission':'browser UI only','provider':'codex real model','concurrency':4,'fault':'none',
 'selection':'Existing v6 briefs selected for varied spoken use: ordinary shops, nonprofit, travel, teaching, English, bilingual, one silent screen, old-draft preservation. No inputs edited and no desired wording supplied.',
 'assessment':'Read the whole audible copy before viewing audit verdicts. Judge complete spoken sentences, clear referents, cross-shot meaning and scene relation, then factual and hard-constraint fidelity. Record exact problematic words and needed edit; do not score by forbidden-word counts.',
 'readiness':['可直接试配音','需局部改写','需整体重写','静音稿不适用','未成稿'],
 'limits':'Developer AI text read-through, not independent human blind evaluation, recorded voice or TTS. Preserve every attempt; no post-hoc replacement reruns.'}
(B/'protocol.json').write_text(json.dumps(protocol,ensure_ascii=False,indent=2),encoding='utf8')
shutil.copytree(ROOT/'outputs/web/efcc96a70bf4485db882c7cc6aba2722',B/'reported-example-v3')
print({'cases':len(cases),'sha256':protocol['cases_sha256']})
