"""Replay saved deterministic tool observations against their data snapshots."""

import json
from pathlib import Path

from src.schema import fingerprint
from src.tools import ROOT, ToolBox, read_json


def verify_run(directory):
    directory = Path(directory)
    request = read_json(directory / "input.json")
    output = read_json(directory / "output.json")
    manifest = read_json(directory / "manifest.json")
    snapshot = read_json(directory / "data_snapshot.json")
    trace = [json.loads(line) for line in (directory / "trace.jsonl").read_text(encoding="utf-8").splitlines()]
    tools = ToolBox(snapshot["materials"], snapshot["rules"], manifest["fault_injection"])
    errors = []
    if tools.data_hash != manifest["data_hash"]:
        errors.append("data_hash 不一致")
    script, retrieved, duration, rules_check = request.get("initial_script"), {}, None, None
    for index, entry in enumerate(trace, 1):
        if entry["step"] != index:
            errors.append("步骤不连续")
        name, args = entry["action"], entry["arguments"]
        if name == "write_script":
            script = args["script"]
            duration = rules_check = None
            if entry["observation"].get("script_hash") != fingerprint(script):
                errors.append(f"step {index}: 写稿哈希不一致")
        elif name in {"search_materials", "estimate_duration", "check_rules"}:
            if script is None and name != "search_materials":
                continue
            if name == "search_materials":
                expected_args = {"query": args["query"], "product_id": request["product_id"]}
            elif name == "estimate_duration":
                expected_args = {"script": script, "target_seconds": request["target_seconds"]}
            else:
                expected_args = {"script": script, "retrieved_ids": sorted(retrieved)}
            if args != expected_args:
                errors.append(f"step {index}: 宿主绑定参数不一致")
            actual = tools.call(name, expected_args)
            if actual != entry["observation"]:
                errors.append(f"step {index}: 工具返回不能由当前快照复算")
            if name == "search_materials" and actual["ok"]:
                retrieved.update({m["id"]: m for m in actual["materials"]})
            elif name == "estimate_duration":
                duration = actual
            elif name == "check_rules":
                rules_check = actual
    if output["script"] != script or output["duration"] != duration or output["rules_check"] != rules_check:
        errors.append("最终输出与 Trace 重放状态不一致")
    if output["status"] == "completed":
        if not all(c and c.get("ok") and c.get("passed") and c.get("script_hash") == fingerprint(script)
                   for c in (duration, rules_check)):
            errors.append("完成状态缺少有效检查")
        if not trace or trace[-1]["observation"].get("status") != "completed":
            errors.append("完成状态缺少结束动作")
    return errors


def main():
    rows = []
    for group in ("mock", "live"):
        for input_file in sorted((ROOT / "examples" / group).glob("*/input.json")):
            errors = verify_run(input_file.parent)
            rows.append({"run": input_file.parent.relative_to(ROOT).as_posix(), "passed": not errors, "errors": errors})
    report = {"scope": "Replay of local tools and saved state only; does not rerun or authenticate the remote model.",
              "runs_checked": len(rows), "passed": bool(rows) and all(r["passed"] for r in rows), "runs": rows}
    (ROOT / "examples/evidence-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
