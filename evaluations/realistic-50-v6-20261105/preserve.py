import hashlib,json,zipfile
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];B=Path(__file__).resolve().parent
A=ROOT/'archives/v5-before-v6-20261105'
assert not A.exists()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=[]
for folder in ('src','web','tests','scripts','data','docs','examples'):
    source += [p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.pyo'}]
source += [ROOT/n for n in ('README.md','PRODUCT.md','DESIGN.md','requirements.txt','.env.example','.gitignore','run.ps1','启动网页.cmd')]
old=[]
for folder in ('evaluations','examples','outputs','archives'):
    old += [p for p in (ROOT/folder).rglob('*') if p.is_file() and not p.is_relative_to(B) and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.pyo'}]
old += list(ROOT.glob('*.zip'))+list(ROOT.glob('*_校验.json'))
manifest={'created_at':datetime.now(timezone.utc).isoformat(),'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in source},'preserved_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in old}}
A.mkdir(parents=True)
with zipfile.ZipFile(A/'source.zip','x',zipfile.ZIP_DEFLATED) as z:
    for p in source:z.write(p,p.relative_to(ROOT).as_posix())
manifest['archive_sha256']=sha(A/'source.zip')
(A/'baseline.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
cases=ROOT/'evaluations/realistic-50-v5-20261104/cases.json'
(B/'cases.json').write_bytes(cases.read_bytes())
(B/'protocol.json').write_text(json.dumps({'frozen_at':datetime.now(timezone.utc).isoformat(),'baseline':'realistic-50-v5-20261104','cases':50,'unique_briefs':49,'cases_sha256':sha(cases),'submission':'browser UI only','provider':'codex real model','concurrency':4,'fault':'none','rule':'Inputs unchanged, no expected answers passed to model. Preserve every attempt. Count received-model failures, no replacement rerun. Freeze code after development.'},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'source_files':len(source),'preserved_files':len(old),'archive_sha256':manifest['archive_sha256']},ensure_ascii=False))
