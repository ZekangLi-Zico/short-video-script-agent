"""Package the completed paired evidence, without overwriting earlier deliveries."""
import hashlib
import json
import zipfile
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parents[1]
load = lambda p: json.loads(p.read_text(encoding="utf-8-sig"))
sha = lambda b: hashlib.sha256(b).hexdigest()
result = load(B / "results.json")
assert result["archived"] == 50 and not result["errors"]
assert result["old_files_checked"] == 3481
assert not result["source_changed"] and not result["old_files_changed"]
for r in result["runs"]:
    assert (B / "runs" / r["folder"] / "review.json").is_file()
for name in ("README.md", "复盘报告.md", "逐条复盘.csv", "comparison.json", "前后对照.csv"):
    assert (B / name).is_file(), name

files = {}
for folder in (B, B.parent / "realistic-50-v3-20261104", B.parent / "finite-v4-20261104"):
    for p in sorted(folder.rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
            files[p.relative_to(ROOT).as_posix()] = p.read_bytes()
files["docs/11-v4-real50-comparison.md"] = (ROOT / "docs/11-v4-real50-comparison.md").read_bytes()
files["docs/10-finite-v4-report.md"] = (ROOT / "docs/10-finite-v4-report.md").read_bytes()
for doc in ("README.md", "docs/03-evaluation.md", "docs/06-submission.md"):
    files["updated-submission-docs/" + doc] = (ROOT / doc).read_bytes()
files["verify_bundle.py"] = (B / "verify_bundle.py").read_bytes()
files["README.md"] = ("# v4 修复后 50 次真实模型网页实验：证据补充包\n\n"
    "这是实验与对比材料，不是另一套应用版本。可运行项目使用此前的 `小影科技笔试_第4题_v4有限修复版.zip`；本轮应用源码没有变化。`updated-submission-docs/`是对应路径的最新提交说明，复制回完整项目后链接才完整。\n\n"
    "- [本轮复盘报告](evaluations/realistic-50-v4-20261104/复盘报告.md)\n"
    "- [逐条评阅](evaluations/realistic-50-v4-20261104/逐条复盘.csv)\n"
    "- [前后逐例对照](evaluations/realistic-50-v4-20261104/前后对照.csv)\n"
    "- [修复前原始记录](evaluations/realistic-50-v3-20261104/README.md)\n"
    "- [提交用简明说明](docs/11-v4-real50-comparison.md)\n\n"
    "此前专项修复与受控故障证据另附于 `evaluations/finite-v4-20261104/`，不计入本轮50次自然需求实验。\n\n"
    "解压后在本目录运行 `python verify_bundle.py`，核对本包所有文件哈希。该检查只验证文件完整性，不调用模型，不评定语义正确性。\n\n"
    "本包保留两轮实验的原始记录，包括失败；未收入所有其他历史ZIP和后台输出目录。因此 `audit_campaign.py --full` 需要原项目完整工作区；不要把本包自校验与3481项历史工作区核验混为一谈。\n"
).encode("utf-8")
manifest = {"kind": "paired_real_model_web_evidence_supplement", "application_changed": False,
            "planned_cases": 50, "unique_inputs": 49, "actual_model_responses": result["actual_model_responses"],
            "files_sha256": {name: sha(data) for name, data in sorted(files.items())}}
name = "小影科技笔试_v4_50次真实模型对比实验"
target = ROOT / (name + ".zip")
assert not target.exists(), "Refuse to overwrite an existing delivery"
with zipfile.ZipFile(target, "x", compression=zipfile.ZIP_DEFLATED) as z:
    for path, data in sorted(files.items()):
        z.writestr("v4-real50-evidence/" + path, data)
    z.writestr("v4-real50-evidence/DELIVERY.json", json.dumps(manifest, ensure_ascii=False, indent=2))
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    for path, expected in manifest["files_sha256"].items():
        assert sha(z.read("v4-real50-evidence/" + path)) == expected, path
check = {"file": target.name, "sha256": sha(target.read_bytes()), "bytes": target.stat().st_size,
         "files_checked": len(files), "zip_crc_ok": True, "all_file_hashes_ok": True}
(ROOT / (name + "_校验.json")).write_text(json.dumps(check, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(check, ensure_ascii=False))
