"""Verify the local deliverable and (optionally) each archive member."""
import argparse,hashlib,json,re,subprocess,zipfile
from pathlib import Path
from urllib.parse import unquote
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--zip');args=p.parse_args();errors=[]
audit=load(B/'results.json');summary=load(B/'summary.json');tests=load(B/'development-tests/final/summary.json')
assert audit['archived']==50 and not audit['errors'] and tests['tests_run']==118 and tests['passed']
assert len(list((B/'runs').glob('*/review.json')))==50
for name,digest in load(B/'tested-source.json')['files'].items():
    if sha(ROOT/name)!=digest:errors.append('Frozen file changed: '+name)
docs=[ROOT/'README.md',B/'README.md',B/'复盘报告.md',ROOT/'examples/v5-live/evaluation.md']
docs += [q for q in (ROOT/'docs').glob('*.md') if q.name[:2] in ['01','02','03','04','05','06','07','13','15']]
for q in docs:
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',q.read_text(encoding='utf8')):
        if link.startswith(('http:','https:','#','mailto:')):continue
        dest=unquote(link.strip('<>').split('#')[0])
        if not (q.parent/dest).exists():errors.append(f'Broken link {q.relative_to(ROOT)} -> {dest}')
copies=0
for q in (ROOT/'examples/v5-live').glob('V*/*'):
    if q.is_file():
        if sha(q)!=sha(B/'runs'/q.parent.name/q.name):errors.append('Example copy differs: '+str(q))
        copies+=1
report={'cases':50,'tests':118,'source_files':43,'preserved_historical_files':audit['old_files_checked'],
        'quality_assessments':summary['quality_assessments'],'example_files_checked':copies,'documents_checked':len(docs),
        'git_remote_names':subprocess.check_output(['git','remote'],cwd=ROOT,text=True).splitlines(),'errors':errors}
if args.zip:
    archive=(ROOT/args.zip).resolve()
    with zipfile.ZipFile(archive) as z:
        bad=z.testzip()
        if bad:errors.append('ZIP CRC error: '+bad)
        manifest=json.loads(z.read('short-video-script-agent/DELIVERY.json'))
        for name,digest in manifest['files_sha256'].items():
            if hashlib.sha256(z.read('short-video-script-agent/'+name)).hexdigest()!=digest:errors.append('ZIP hash mismatch: '+name)
            if name.startswith(('src/','tests/','scripts/','web/','data/')) and sha(ROOT/name)!=digest:errors.append('ZIP source differs: '+name)
        for name in z.namelist():
            if any(part in {'.env','.runtime','.codex','.git'} for part in Path(name).parts):errors.append('Excluded private/runtime path included: '+name)
    report.update(archive=archive.name,bytes=archive.stat().st_size,sha256=sha(archive),file_count=manifest['file_count'],crc_ok=not bad)
    (ROOT/(archive.stem+'_校验.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
else:
    (B/'delivery-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False));raise SystemExit(bool(errors))
