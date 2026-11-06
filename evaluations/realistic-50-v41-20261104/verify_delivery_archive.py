"""Verify a completed local submission snapshot. Does not call models."""
import hashlib
import json
import zipfile
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parents[1]
name = "小影科技笔试_第4题_v4.1_50次复测提交包"
path = ROOT / (name + ".zip")
prefix = "short-video-script-agent/"
sha = lambda b: hashlib.sha256(b).hexdigest()
with zipfile.ZipFile(path) as z:
    assert z.testzip() is None, "ZIP CRC failed"
    load = lambda p: json.loads(z.read(prefix + p).decode("utf-8-sig"))
    m = load("DELIVERY.json")
    for p, expected in m["files_sha256"].items():
        assert sha(z.read(prefix + p)) == expected, p
    base = "evaluations/realistic-50-v41-20261104/"
    freeze, result = load(base + "baseline.json"), load(base + "results.json")
    for p, expected in freeze["source_sha256"].items():
        assert sha(z.read(prefix + p)) == expected, "tested source changed: " + p
    assert sha(z.read(prefix + base + "cases.json")) == freeze["cases_sha256"]
    assert z.read(prefix + base + "cases.json") == z.read(prefix + "evaluations/realistic-50-v4-20261104/cases.json")
    assert result["archived"] == 50 and result["actual_model_responses"] == 317 and not result["errors"]
    for r in result["runs"]:
        for filename in ("page.png", "brief.json", "ui-input.json", "output.json", "script.md", "trace.jsonl",
                         "manifest.json", "checkpoint.json", "run.json", "review.json", "audit.json"):
            assert z.getinfo(prefix + base + "runs/" + r["folder"] + "/" + filename).file_size > 0
out = {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path.read_bytes()),
       "files_checked": len(m["files_sha256"]), "zip_crc_ok": True, "all_file_hashes_ok": True,
       "tested_source_files_unchanged": len(freeze["source_sha256"]), "paired_input_bytes_identical": True,
       "complete_real_experiments": 50, "model_responses": 317,
       "note": "Local snapshot; not a final Git commit or submitted exam. Historical root ZIPs are preserved in the workspace, not nested in this archive."}
(ROOT / (name + "_校验.json")).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, ensure_ascii=False))
