"""Check current evidence/doc links and optionally ZIP member hashes."""
import argparse,hashlib,json,re,subprocess,zipfile
from pathlib import Path
from urllib.parse import unquote
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--zip');args=p.parse_args();errors=[]
a=load(B/'results.json');s=load(B/'summary.json');t=load(B/'development-tests/review-fixed/summary.json')
assert a['archived']==20 and not a['errors'] and t['tests_run']==133 and t['passed']
assert len(list((B/'runs').glob('*/review.json')))==20
for name,digest in load(B/'baseline.json')['source_sha256'].items():
 if sha(ROOT/name)!=digest:errors.append('Frozen file changed: '+name)
docs=[ROOT/'README.md',B/'README.md',B/'复盘报告.md',ROOT/'examples/v7-live/evaluation.md']
docs += [q for q in (ROOT/'docs').glob('*.md') if q.name[:2] in ['01','02','03','04','05','06','07','13','17']]
for q in docs:
 for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',q.read_text(encoding='utf8')):
  if link.startswith(('http:','https:','#','mailto:')):continue
  dest=unquote(link.strip('<>').split('#')[0])
  if not (q.parent/dest).exists():errors.append(f'Broken link {q.relative_to(ROOT)} -> {dest}')
copies=0
for q in (ROOT/'examples/v7-live').glob('V*/**/*'):
 if q.is_file():
  if sha(q)!=sha(B/'runs'/q.relative_to(ROOT/'examples/v7-live')):errors.append('Example copy differs: '+str(q))
  copies+=1
report={'cases':20,'tests':133,'source_files':47,'preserved_historical_files':a['old_files_checked'],
        'readiness':s['new_readiness'],'example_files_checked':copies,'documents_checked':len(docs),
        'git_remote_names':subprocess.check_output(['git','remote'],cwd=ROOT,text=True).splitlines(),'errors':errors}
if args.zip:
 archive=(ROOT/args.zip).resolve()
 with zipfile.ZipFile(archive) as z:
  bad=z.testzip()
  if bad:errors.append('ZIP CRC error: '+bad)
  m=json.loads(z.read('short-video-script-agent/DELIVERY.json'))
  for name,digest in m['files_sha256'].items():
   if hashlib.sha256(z.read('short-video-script-agent/'+name)).hexdigest()!=digest:errors.append('ZIP hash mismatch: '+name)
   if name.startswith(('src/','tests/','scripts/','web/','data/')) and sha(ROOT/name)!=digest:errors.append('ZIP source differs: '+name)
  for name in z.namelist():
   if any(part in {'.env','.runtime','.codex','.git'} for part in Path(name).parts):errors.append('Excluded private/runtime path included: '+name)
 report.update(archive=archive.name,bytes=archive.stat().st_size,sha256=sha(archive),file_count=m['file_count'],crc_ok=not bad)
 (ROOT/(archive.stem+'_校验.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
else:(B/'delivery-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False));raise SystemExit(bool(errors))
