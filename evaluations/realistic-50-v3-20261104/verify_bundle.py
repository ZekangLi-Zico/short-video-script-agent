"""Verify this evidence bundle's hashes without model calls or application imports."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'checksums.json').read_text(encoding='utf-8'))
errors = []
for name, expected in manifest['sha256'].items():
    path = (root / name).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        errors.append(f'missing/invalid: {name}')
    elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        errors.append(f'changed: {name}')
print(json.dumps({'files_checked':len(manifest['sha256']), 'errors':errors},ensure_ascii=False))
raise SystemExit(bool(errors))
