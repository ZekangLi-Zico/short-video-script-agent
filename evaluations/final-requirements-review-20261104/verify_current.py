"""Read-only requirements evidence audit; writes only this review's report."""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parents[1]
sys.path.insert(0, str(ROOT))
from scripts.verify_evidence import verify_run

load = lambda p: json.loads(p.read_text(encoding="utf-8-sig"))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
campaign = ROOT / "evaluations/realistic-50-v41-20261104"
baseline = load(campaign / "baseline.json")
source_changed = [p for p, h in baseline["source_sha256"].items() if sha(ROOT / p) != h]
required = ["README.md", "requirements.txt", ".env.example", "src/agent.py", "src/cli.py",
    "data/materials.json", "data/brand_rules.json", "docs/01-requirements.md", "docs/02-solution.md",
    "docs/03-evaluation.md", "docs/04-ai-usage.md", "docs/05-retrospective.md"]
missing_files = [p for p in required if not (ROOT / p).is_file()]
rows, errors = [], []
for parent in (ROOT / "evaluations/final-polish-20261104/runs", campaign / "runs"):
    for p in sorted(parent.glob("*/manifest.json")):
        d, m = p.parent, load(p)
        output = load(d / "output.json")
        trace = [json.loads(line) for line in (d / "trace.jsonl").read_text(encoding="utf-8").splitlines()]
        issues = verify_run(d)
        diagnostic_count = 0
        for t in trace:
            for key in ("model", "review_model"):
                if key in t:
                    diag = load(d / "diagnostics" / (t[key]["call_id"] + ".json"))
                    diagnostic_count += bool(diag["response_received"])
                    if diag["metadata"] != t[key] or not diag["response_received"]:
                        issues.append("diagnostic mismatch")
        if diagnostic_count != m["model_responses"]: issues.append("response count mismatch")
        rows.append({"directory": d.relative_to(ROOT).as_posix(), "status": output["status"],
            "steps": m["steps"], "responses": m["model_responses"], "fault_injection": m.get("fault_injection"),
            "path": [t["action"] for t in trace], "errors": issues})
        errors += [{"directory": d.relative_to(ROOT).as_posix(), "error": e} for e in issues]
archive_check = load(ROOT / "小影科技笔试_第4题_v4.1_50次复测提交包_校验.json")
archive_match = sha(ROOT / archive_check["file"]) == archive_check["sha256"]
tests = load(B / "tests/summary.json")
remotes = subprocess.check_output(["git", "remote", "-v"], cwd=ROOT, text=True).strip()
report = {"checked_at": datetime.now(timezone.utc).isoformat(),
    "source_files_checked": len(baseline["source_sha256"]), "source_changed": source_changed,
    "missing_required_files": missing_files, "saved_runs_verified": len(rows),
    "saved_real_model_responses": sum(r["responses"] for r in rows),
    "fresh_automated_tests": tests, "archive_sha256_matches": archive_match,
    "git_remotes": remotes, "evidence_errors": errors, "rows": rows,
    "scope": "Fresh local tests plus read-only saved evidence verification. No new real-model experiments, application changes, Git commit, push, or exam submission."}
(B / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in report.items() if k != "rows"}, ensure_ascii=False))
raise SystemExit(bool(source_changed or missing_files or errors or not archive_match or not tests["passed"]))
