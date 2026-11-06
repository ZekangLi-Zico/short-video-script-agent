"""Read-only local delivery checks, without exposing possible credential text."""
import hashlib
import json
import re
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parents[1]
load = lambda p: json.loads(p.read_text(encoding="utf-8-sig"))
r, o, c = load(B / "results.json"), load(B / "observations.json"), load(B / "comparison.json")
assert r["archived"] == o["reviewed"] == c["paired_cases"] == 50
assert not r["errors"] and r["old_files_checked"] == 5820
assert r["actual_model_responses"] == o["successful_responses"] == 317
assert r["statuses"] == {"completed": 36, "needs_input": 14}
files = []
for folder in ("src", "web", "tests", "scripts", "data", "docs", "examples", "evaluations", "outputs", "archives"):
    files += [p for p in (ROOT / folder).rglob("*") if p.is_file() and "__pycache__" not in p.parts
              and p.suffix not in {".pyc", ".pyo"} and p.name != ".env"]
forbidden = [str(p.relative_to(ROOT)) for p in files if p.name.lower() in
             {"auth.json", "credentials", "credentials.json", ".env.local", "id_rsa", "id_ed25519"}]
patterns = [re.compile(r"\bsk-[A-Za-z0-9_-]{30,}\b"), re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
            re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")]
suspects = []
for p in files:
    if p.suffix.lower() in {".json", ".jsonl", ".md", ".txt", ".py", ".js", ".html", ".csv"}:
        text = p.read_text(encoding="utf-8-sig", errors="replace")
        if any(x.search(text) for x in patterns): suspects.append(str(p.relative_to(ROOT)))
links = []
docs = [ROOT / "README.md", ROOT / "docs/14-v41-real50-comparison.md", B / "README.md", B / "复盘报告.md"]
for p in docs:
    for href in re.findall(r"\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
        if "://" in href or href.startswith("#"): continue
        if not (p.parent / href.split("#", 1)[0]).exists(): links.append({"file": str(p.relative_to(ROOT)), "link": href})
out = {"files_considered": len(files), "forbidden_filename_matches": forbidden,
       "credential_pattern_file_matches": suspects, "broken_report_links": links,
       "complete_real_campaign": True,
       "scope": "Limited filename/pattern inspection; auth/runtime directories excluded. Not a comprehensive secret scan."}
(B / "delivery-preflight.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, ensure_ascii=False))
raise SystemExit(bool(forbidden or suspects or links))
