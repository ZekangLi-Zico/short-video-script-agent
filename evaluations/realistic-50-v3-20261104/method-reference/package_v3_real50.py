import hashlib
import json
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B = ROOT/'evaluations/realistic-50-v3-20261104'
load = lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha = lambda b:hashlib.sha256(b).hexdigest()
validation = load(B/'validation.json')
assert validation['archived_experiments'] == 50
assert (B/'复盘报告.md').is_file() and (B/'最终页面.jpg').is_file()
for name in ('audit_v3_real50.py','finalize_v3_real50.py','package_v3_real50.py'):
    target = B/'method-reference'/name
    target.parent.mkdir(exist_ok=True)
    assert not target.exists()
    shutil.copyfile(ROOT/'.runtime'/name,target)
files = sorted(p for p in B.rglob('*') if p.is_file() and p.name != 'checksums.json')
manifest = {'created_at':datetime.now(timezone.utc).isoformat(),
            'scope':'All bundle files except checksums.json itself',
            'sha256':{p.relative_to(B).as_posix():sha(p.read_bytes()) for p in files}}
with (B/'checksums.json').open('x',encoding='utf-8') as f:
    json.dump(manifest,f,ensure_ascii=False,indent=2);f.write('\n')
destination = ROOT/'小影科技笔试_v3_50次真实模型实验.zip'
assert not destination.exists()
with zipfile.ZipFile(destination,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(B.rglob('*')):
        if p.is_file():z.write(p,B.name+'/'+p.relative_to(B).as_posix())
with zipfile.ZipFile(destination) as z:
    assert z.testzip() is None
    for name,expected in manifest['sha256'].items():
        assert sha(z.read(B.name+'/'+name)) == expected,name
    assert sha(z.read(B.name+'/checksums.json')) == sha((B/'checksums.json').read_bytes())
    entries = len(z.infolist())
report = {'zip':destination.name,'sha256':sha(destination.read_bytes()),
          'bytes':destination.stat().st_size,'entries':entries,
          'hashed_evidence_files':len(manifest['sha256']),
          'crc_and_all_hashes_verified':True,
          'original_v3_release_unchanged':validation['v3_release_zip_sha256'],
          'verified_at':datetime.now(timezone.utc).isoformat()}
with (ROOT/'小影科技笔试_v3_50次真实模型实验_校验.json').open('x',encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps(report,ensure_ascii=False))
