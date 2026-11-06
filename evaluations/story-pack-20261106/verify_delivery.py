"""Read-only preservation, bundle and live-run checks; writes a new audit report."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
baseline=ROOT/'archives/v7-before-story-pack-20261106-011637'
history=json.loads((baseline/'history-manifest.json').read_text(encoding='utf-8'))
changed=[]
for entry in history:
    path=ROOT/entry['path']
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=entry['sha256']:
        changed.append(entry['path'])
packdir=ROOT/'data/packs/city-drama'
pack=json.loads((packdir/'materials.json').read_text(encoding='utf-8'))
bundle_errors=[]
with zipfile.ZipFile(packdir/'city-drama-materials.zip') as z:
    if z.testzip(): bundle_errors.append('CRC failed')
    for name in z.namelist():
        if z.read(name)!=(packdir/name).read_bytes():bundle_errors.append(name)
    for s in pack['sources'].values():
        if s['file'] not in z.namelist(): bundle_errors.append('missing '+s['file'])
report={'history_files_checked':len(history),'changed_or_missing_history':changed,
        'cards':len(pack['materials']),'facts':sum(len(m['facts']) for m in pack['materials']),
        'bundle_errors':bundle_errors,'sources':len(pack['sources'])}
(OUT/'preservation-and-bundle.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
raise SystemExit(bool(changed or bundle_errors))
