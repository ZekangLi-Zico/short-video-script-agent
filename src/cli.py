"""Usage: python -m src.cli --provider mock --input examples/inputs/normal.json"""

import argparse
import json
import sys

from .agent import Agent
from .mock import MockModel
from .providers import APIModel, CodexModel
from .reporting import save_run
from .tools import ToolBox, read_json


def make_model(provider, timeout=180):
    if provider == "mock":
        return MockModel()
    if provider == "codex":
        return CodexModel(timeout=timeout)
    return APIModel(timeout=timeout)


def main(argv=None):
    parser = argparse.ArgumentParser(description="第4题：有来源、可检查修订的短视频脚本 Agent")
    parser.add_argument("--provider", required=True, choices=["mock", "codex", "api"])
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="outputs/latest")
    parser.add_argument("--max-steps", type=int, default=12)
    parser.add_argument("--timeout", type=int, default=180, help="每次模型调用的超时秒数")
    parser.add_argument("--materials", help="自定义素材 JSON；结构同 data/materials.json")
    parser.add_argument("--fail-tool", choices=["search_materials", "estimate_duration", "check_rules"])
    parser.add_argument("--fail-count", type=int, default=1, help="注入次数；-1 表示持续失败")
    args = parser.parse_args(argv)
    try:
        if not 1 <= args.timeout <= 600 or args.fail_count < -1:
            raise ValueError("timeout 应为 1–600，fail-count 应 >= -1")
        request = read_json(args.input)
        model = make_model(args.provider, args.timeout)
        failures = {args.fail_tool: args.fail_count} if args.fail_tool else {}
        material_file = read_json(args.materials) if args.materials else None
        materials = material_file["materials"] if material_file is not None else None
        tools = ToolBox(materials=materials, failures=failures,
                        synthetic_data=material_file.get("synthetic", False) if material_file is not None else True)
        result = Agent(model, tools, max_steps=args.max_steps).run(request)
        save_run(args.output, request, result, tools)
    except (ValueError, OSError, KeyError) as exc:
        print(f"运行或保存失败：{exc}", file=sys.stderr)
        return 2
    print(json.dumps({"status": result["status"], "evidence_kind": result["metadata"]["evidence_kind"],
                      "output": args.output, "message": result["message"]}, ensure_ascii=False))
    return 0 if result["status"] == "completed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
