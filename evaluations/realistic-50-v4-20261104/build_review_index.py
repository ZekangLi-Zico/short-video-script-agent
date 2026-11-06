"""Assemble already-written per-case reviews; never infer a verdict from status."""
import csv
import json
from pathlib import Path

B = Path(__file__).resolve().parent
load = lambda p: json.loads(p.read_text(encoding="utf-8-sig"))
results = load(B / "results.json")
comparisons = {r["case"]: r for r in load(B / "comparison.json")["rows"]}
rows = []
for r in results["runs"]:
    review = load(B / "runs" / r["folder"] / "review.json")
    old = comparisons[r["case"]]
    rows.append({
        "case": r["case"], "name": r["name"],
        "before_status": old["before_status"], "after_status": r["status"],
        "steps": r["steps"], "responses": r["responses"],
        "estimated_seconds": r["seconds"], "assessment": review["assessment"],
        "note": review["note"], "folder": "runs/" + r["folder"],
        "reviewer": review["reviewer"],
    })
assert len(rows) == 50, "Only publish the complete campaign review"
with (B / "逐条复盘.csv").open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(json.dumps({"reviewed": len(rows)}, ensure_ascii=False))
