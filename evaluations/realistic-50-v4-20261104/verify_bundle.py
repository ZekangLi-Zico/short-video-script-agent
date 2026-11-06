"""Verify a portable evidence supplement. No network or model calls."""
import hashlib
import json
from pathlib import Path

B = Path(__file__).resolve().parent
# This file is copied to the bundle root when packaged.
manifest = json.loads((B / "DELIVERY.json").read_text(encoding="utf-8"))
errors = []
for name, expected in manifest["files_sha256"].items():
    p = (B / name).resolve()
    if not p.is_relative_to(B.resolve()) or not p.is_file():
        errors.append(name + ": missing or outside bundle")
    elif hashlib.sha256(p.read_bytes()).hexdigest() != expected:
        errors.append(name + ": hash mismatch")
print(json.dumps({"checked": len(manifest["files_sha256"]), "errors": errors}, ensure_ascii=False))
raise SystemExit(bool(errors))
