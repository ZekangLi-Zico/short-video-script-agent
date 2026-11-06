"""Replay saved deterministic tool observations against their data snapshots."""

import json
import argparse
from datetime import datetime, timezone
from pathlib import Path

from src.schema import fingerprint
from src.tools import ROOT, ToolBox, read_json
from src.requirements import review_observation, bound_duration_check
from src.expression import extended_review
from src.revisions import revision_summary, failed_feedback
from scripts.replay_compat import replay_tools, search_contract


def verify_run(directory):
    directory = Path(directory)
    request = read_json(directory / "input.json")
    output = read_json(directory / "output.json")
    manifest = read_json(directory / "manifest.json")
    snapshot = read_json(directory / "data_snapshot.json")
    trace = [json.loads(line) for line in (directory / "trace.jsonl").read_text(encoding="utf-8").splitlines()]
    try:
        tools = replay_tools(snapshot, manifest)
    except ValueError as exc:
        return [str(exc)]
    errors = []
    if manifest.get('app_version') != output.get('metadata',{}).get('app_version'):
        errors.append('manifest与output应用版本不一致')
    if manifest.get('tool_contracts') != output.get('metadata',{}).get('tool_contracts'):
        errors.append('manifest与output工具契约不一致')
    if tools.data_hash != manifest["data_hash"]:
        errors.append("data_hash 不一致")
    script, retrieved, duration, rules_check = request.get("initial_script"), {}, None, None
    requirements_check = None
    for index, entry in enumerate(trace, 1):
        if entry["step"] != index:
            errors.append("步骤不连续")
        name, args = entry["action"], entry["arguments"]
        for check in entry.get('preflight_checks',[]):
            if name != 'check_requirements' or not script:
                errors.append(f'step {index}: 预检查不属于当前审核动作'); continue
            tool = check['action']
            if tool == 'estimate_duration':
                expected = {'script':script,'target_seconds':request['target_seconds']}
                if 'duration_mode' in request: expected['duration_mode']=request['duration_mode']
            elif tool == 'check_rules':
                expected = {'script':script,'retrieved_ids':sorted(retrieved)}
                if 'expression_mode' in request: expected['expression_mode']=request['expression_mode']
            else:
                errors.append(f'step {index}: 未知预检查'); continue
            actual = tools.call(tool,expected)
            if check['arguments'] != expected or check['observation'] != actual:
                errors.append(f'step {index}: 预检查参数或结果无法复算')
            if tool == 'estimate_duration': duration = actual
            else: rules_check = actual
        if name == "write_script":
            if 'revision' in entry['observation']:
                expected_revision = revision_summary(script, args['script'], failed_feedback({
                    'duration':duration, 'rules_check':rules_check, 'requirements_check':requirements_check}))
                if expected_revision != entry['observation']['revision']:
                    errors.append(f'step {index}: 修订差异无法复算')
            script = args["script"]
            duration = rules_check = requirements_check = None
            if entry["observation"].get("script_hash") != fingerprint(script):
                errors.append(f"step {index}: 写稿哈希不一致")
        elif name == 'check_requirements':
            if script is None:
                continue
            expected_review_args = {'script': script, 'request': request}
            if manifest.get('requirements_review_context') in {'current_rules_check_v1', 'current_rules_and_duration_v2'}:
                expected_review_args['rules_check'] = rules_check if rules_check and rules_check.get('script_hash') == fingerprint(script) else None
            if manifest.get('requirements_review_context') == 'current_rules_and_duration_v2':
                expected_review_args['duration_check'] = bound_duration_check(duration, request, script)
            if args != expected_review_args:
                errors.append(f'step {index}: 需求检查参数未绑定当前稿和原始需求')
            requirements_check = entry['observation']
            if requirements_check.get('ok'):
                try:
                    reviewed = {k: requirements_check[k] for k in ('items', 'summary')}
                    if extended_review(request):
                        reviewed.update({k:requirements_check[k] for k in ('expressions','pacing')})
                    if review_observation(reviewed, request, script, args.get('rules_check')) != requirements_check:
                        errors.append(f'step {index}: 需求检查哈希或状态不一致')
                except (KeyError, ValueError):
                    errors.append(f'step {index}: 需求检查结构无效')
        elif name in {"search_materials", "estimate_duration", "check_rules"}:
            if script is None and name != "search_materials":
                continue
            if name == "search_materials":
                expected_args = {"query": args["query"], "product_id": request["product_id"]}
            elif name == "estimate_duration":
                expected_args = {"script": script, "target_seconds": request["target_seconds"]}
                if 'duration_mode' in request: expected_args['duration_mode'] = request['duration_mode']
            else:
                expected_args = {"script": script, "retrieved_ids": sorted(retrieved)}
                if 'expression_mode' in request: expected_args['expression_mode'] = request['expression_mode']
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
    if output.get('requirements_check') != requirements_check:
        errors.append('最终需求检查与 Trace 不一致')
    if output["status"] == "completed":
        if output.get('metadata', {}).get('completion_policy') in {'facts_duration_requirements_v2','facts_duration_requirements_v3','facts_duration_requirements_v4','facts_duration_requirements_v5','facts_duration_requirements_v6'}:
            if not (requirements_check and requirements_check.get('ok') and requirements_check.get('passed')
                    and requirements_check.get('script_hash') == fingerprint(script)
                    and requirements_check.get('request_hash') == fingerprint(request)):
                errors.append('完成状态缺少当前需求检查')
        if not all(c and c.get("ok") and c.get("passed") and c.get("script_hash") == fingerprint(script)
                   for c in (duration, rules_check)):
            errors.append("完成状态缺少有效检查")
        if not trace or trace[-1]["observation"].get("status") != "completed":
            errors.append("完成状态缺少结束动作")
    return errors


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',action='append',help='复算指定运行目录；可以重复')
    parser.add_argument('--group',choices=['current','historical','all'],default='all')
    parser.add_argument('--output',help='新验证报告路径；默认写outputs/evidence-audit下的时间戳文件')
    args=parser.parse_args(argv)
    directories=[Path(p) for p in args.run] if args.run else []
    if not args.run:
        groups=(['current'] if args.group=='current' else ['mock','live'] if args.group=='historical' else ['current','mock','live'])
        directories=[p.parent for group in groups for p in sorted((ROOT/'examples'/group).glob('*/input.json'))]
    rows = []
    for directory in directories:
        row={'run':directory.relative_to(ROOT).as_posix() if directory.is_absolute() and directory.is_relative_to(ROOT) else directory.as_posix()}
        try:
            manifest=read_json(directory/'manifest.json')
            row['app_version']=manifest.get('app_version','legacy_unversioned')
            row['search_contract'],row['contract_source']=search_contract(manifest)
            errors=verify_run(directory)
        except (OSError,ValueError,KeyError,TypeError) as exc:
            errors=[f'无法复算记录：{type(exc).__name__}: {exc}']
        rows.append({**row,'passed':not errors,'errors':errors})
    report = {"scope": "Replay of local tools and saved state only; does not rerun or authenticate the remote model.",
              "runs_checked": len(rows), "passed": bool(rows) and all(r["passed"] for r in rows), "runs": rows}
    destination=Path(args.output) if args.output else ROOT/'outputs/evidence-audit'/('audit-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')
    destination.parent.mkdir(parents=True,exist_ok=True)
    report['report_path']=str(destination)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
