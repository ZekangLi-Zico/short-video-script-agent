import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
sys.path.insert(0,str(ROOT))
from scripts.verify_evidence import verify_run
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=json.loads((ROOT/'archives/v5-before-v6-20261105/baseline.json').read_text(encoding='utf8'))
files=[p for folder in ('src','web','tests','scripts','data') for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc']
manifest={'frozen_at':datetime.now(timezone.utc).isoformat(),'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'preserved_sha256':old['preserved_sha256'],'cases_sha256':sha(B/'cases.json'),'archive_sha256':old['archive_sha256'],'reasoning_effort':'medium','max_steps':12,'timeout_per_attempt_seconds':180,'max_timeout_recoveries_per_run':1}
with (B/'baseline.json').open('x',encoding='utf8') as f:json.dump(manifest,f,ensure_ascii=False,indent=2)
legacy={p.parent.name:verify_run(p.parent) for p in (B.parent/'realistic-50-v5-20261104/runs').glob('*/input.json')}
(B/'legacy-replay.json').write_text(json.dumps(legacy,ensure_ascii=False,indent=2),encoding='utf8')
assert len(legacy)==50 and not any(legacy.values())
print(json.dumps({'source_files':len(files),'historical_files':len(old['preserved_sha256']),'legacy_replayed':len(legacy)}))
