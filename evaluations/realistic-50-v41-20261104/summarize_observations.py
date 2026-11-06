"""Summarize archived evidence only; no model calls or automatic semantic verdicts."""
import json
from collections import Counter
from pathlib import Path

B = Path(__file__).resolve().parent
load = lambda p: json.loads(p.read_text(encoding="utf-8-sig"))
rows, diagnostics, actions, reviews = [], [], Counter(), []
for d in sorted((B / "runs").glob("*")):
    if not (d / "capture.json").exists():
        continue
    cap, manifest = load(d / "capture.json"), load(d / "manifest.json")
    trace = [json.loads(s) for s in (d / "trace.jsonl").read_text(encoding="utf-8").splitlines()]
    actions.update(t["action"] for t in trace)
    for p in sorted((d / "diagnostics").glob("*.json")):
        x = load(p)
        diagnostics.append({"case": d.name, "call_id": x.get("call_id"),
            "response_received": x.get("response_received"), "exit_code": x.get("exit_code"),
            "error_type": x.get("error_type"), "cleanup_error_type": x.get("cleanup_error_type"),
            "cleanup_deferred": "cleanup_deferred" in x.get("metadata", {}).get("warnings", []),
            "warnings": x.get("metadata", {}).get("warnings", [])})
    if (d / "review.json").exists():
        reviews.append(load(d / "review.json"))
    rows.append({"case": d.name, "started_at": manifest["started_at"],
        "finished_at": manifest["finished_at"], "actions": [t["action"] for t in trace],
        "status": cap["status"], "responses": cap["responses"]})
out = {"archived": len(rows), "reviewed": len(reviews), "actions": dict(actions),
    "diagnostic_count": len(diagnostics),
    "successful_responses": sum(bool(x["response_received"]) for x in diagnostics),
    "diagnostic_warnings": [x for x in diagnostics if not x["response_received"] or x["error_type"] or x["cleanup_error_type"]],
    "review_assessments": dict(Counter(x["assessment"] for x in reviews)),
    "stale_editorial_note_cases": [x["case"] for x in reviews if x.get("editorial_note_staleness")],
    "observed_hard_requirement_violation_cases": [x["case"] for x in reviews if x.get("hard_requirement_violation_observed")],
    "first_started_at": min((x["started_at"] for x in rows), default=None),
    "last_finished_at": max((x["finished_at"] for x in rows), default=None), "rows": rows}
(B / "observations.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "rows"}, ensure_ascii=False))
