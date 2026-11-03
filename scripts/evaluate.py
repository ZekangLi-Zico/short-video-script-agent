"""Run acceptance scenarios and preserve actual outputs, never fabricated traces."""

import argparse
import copy
import json
from pathlib import Path

from src.agent import Agent
from src.cli import make_model
from src.mock import example_script
from src.reporting import save_run
from src.tools import ToolBox, ROOT, read_json


def scenarios():
    base = read_json(ROOT / "examples/inputs/normal.json")
    missing = copy.deepcopy(base)
    del missing["target_seconds"]
    no_material = {**base, "product_id": "product-without-materials"}
    return [
        ("normal", base, {}, {"completed"}),
        ("missing_information", missing, {}, {"needs_input"}),
        ("no_material", no_material, {}, {"needs_input", "blocked"}),
        ("tool_failure", base, {"search_materials": -1}, {"blocked", "step_limit"}),
        ("recoverable_failure", base, {"search_materials": 1}, {"completed"}),
        ("over_duration", {**base, "initial_script": example_script(long=True)}, {}, {"completed"}),
        ("rule_revision", {**base, "initial_script": example_script(bad_claim=True)}, {}, {"completed"}),
        ("impossible_duration", {**base, "target_seconds": 1}, {}, {"blocked", "needs_input", "step_limit"}),
    ]


def check_case(name, result, expected):
    problems = []
    trace = result["trace"]
    if result["status"] not in expected:
        problems.append(f"status={result['status']}, expected one of {sorted(expected)}")
    if result["status"] == "completed":
        if not all((result[k] or {}).get("passed") for k in ("duration", "rules_check")):
            problems.append("完成状态未同时通过两项检查")
    if name == "over_duration" and result["status"] == "completed":
        rejected = [i for i, t in enumerate(trace) if t["action"] == "estimate_duration"
                    and t["observation"].get("ok") and not t["observation"].get("passed")]
        if not rejected or not any(t["action"] == "write_script" for t in trace[rejected[0]+1:]):
            problems.append("缺少先观察超时结果、再修订的证据")
    if name == "rule_revision" and result["status"] == "completed":
        rejected = [i for i, t in enumerate(trace) if t["action"] == "check_rules"
                    and t["observation"].get("ok") and not t["observation"].get("passed")]
        if not rejected or not any(t["action"] == "write_script" for t in trace[rejected[0]+1:]):
            problems.append("缺少先观察规则风险、再修订的证据")
    if name in {"recoverable_failure", "tool_failure"}:
        if not any(t["observation"].get("error") == "injected_tool_failure" for t in trace):
            problems.append("没有实际触发注入故障")
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=["mock", "codex", "api"], required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--case", action="append", help="只运行指定场景，可重复")
    parser.add_argument("--timeout", type=int, default=180)
    args = parser.parse_args(argv)
    model = make_model(args.provider, args.timeout)
    rows = []
    available = scenarios()
    unknown = set(args.case or []) - {entry[0] for entry in available}
    if unknown:
        parser.error("未知场景：" + ", ".join(sorted(unknown)))
    for name, request, failures, expected in available:
        if args.case and name not in args.case:
            continue
        tools = ToolBox(failures=failures)
        result = Agent(model, tools).run(copy.deepcopy(request))
        directory = Path(args.output) / name
        save_run(directory, request, result, tools)
        errors = check_case(name, result, expected)
        row = {"case": name, "expected_status": sorted(expected), "actual_status": result["status"],
               "passed": not errors, "errors": errors, "steps": result["metadata"]["steps"],
               "evidence_kind": result["metadata"]["evidence_kind"],
               "path": " -> ".join(t["action"] for t in result["trace"]), "artifacts": str(directory)}
        rows.append(row)
        print(json.dumps(row, ensure_ascii=False), flush=True)
    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=True)
    current_rows = rows
    previous_file = root / "evaluation.json"
    if args.case and previous_file.exists():
        by_case = {row["case"]: row for row in read_json(previous_file)}
        by_case.update({row["case"]: row for row in rows})
        rows = [by_case[name] for name, *_ in available if name in by_case]
    (root / "evaluation.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# 实际验收结果", "", f"模型入口：{args.provider}。Mock 不证明真实模型决策效果。", "",
             "| 场景 | 状态 | 验收 | 步数 |", "|---|---|---|---|"]
    lines += [f"| [{r['case']}]({r['case']}/script.md) | {r['actual_status']} | {'通过' if r['passed'] else '失败'} | {r['steps']} |" for r in rows]
    (root / "evaluation.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0 if current_rows and all(r["passed"] for r in current_rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
