"""Create a reviewable workspace snapshot; never imply it is a Git commit."""
import argparse
import hashlib
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    parser.add_argument('--version',default='quality-v3-workspace')
    parser.add_argument('--include-root-archives',action='store_true',help='Include preserved ZIPs referenced by the v4 baseline')
    args=parser.parse_args()
    output=Path(args.output).resolve()
    if output.exists(): parser.error('Refuse replacing archive')
    files=[]
    for folder in ('src','web','tests','scripts','data','docs','examples','evaluations','outputs','archives'):
        files += [p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts
                  and p.suffix not in {'.pyc','.pyo'} and p.name != '.env']
    files += [ROOT/n for n in ('README.md','PRODUCT.md','DESIGN.md','requirements.txt','.env.example','.gitignore','run.ps1','启动网页.cmd')]
    if args.include_root_archives:
        files += [p for p in ROOT.glob('*.zip') if p.resolve()!=output]
        files += list(ROOT.glob('*_校验.json'))
    hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    manifest={'version':args.version,'created_at':datetime.now(timezone.utc).isoformat(),
              'git_base_commit':commit,'uncommitted_changes':True,
              'note':'Local workspace snapshot; not uploaded or exam-submitted. Baseline commit does not identify final content.',
              'file_count':len(hashes),'files_sha256':hashes}
    with zipfile.ZipFile(output,'x',zipfile.ZIP_DEFLATED) as z:
        for p in files: z.write(p,'short-video-script-agent/'+p.relative_to(ROOT).as_posix())
        z.writestr('short-video-script-agent/DELIVERY.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'archive':str(output),'bytes':output.stat().st_size,'file_count':len(hashes),
                      'sha256':hashlib.sha256(output.read_bytes()).hexdigest()},ensure_ascii=False))


if __name__=='__main__':main()
