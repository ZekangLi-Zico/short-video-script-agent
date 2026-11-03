"""Shared structured action schema and strict boundary validation."""

import hashlib
import json
import math


def obj(properties):
    return {"type": "object", "properties": properties,
            "required": list(properties), "additionalProperties": False}


TEXT = {"type": "string"}
BLOCK_SCHEMA = obj({"text": TEXT, "source_id": TEXT, "fact_id": TEXT})
SHOT_SCHEMA = obj({"visual": TEXT, "hold_seconds": {"type": "number"},
                   "blocks": {"type": "array", "items": BLOCK_SCHEMA}})
SCRIPT_SCHEMA = obj({"title": TEXT, "shots": {"type": "array", "items": SHOT_SCHEMA}})
ACTION_SCHEMA = obj({
    "action": {"type": "string", "enum": ["search_materials", "write_script", "estimate_duration", "check_rules", "finish"]},
    "reason": TEXT,
    "query": TEXT,
    "script": {"anyOf": [SCRIPT_SCHEMA, {"type": "null"}]},
    "status": {"type": "string", "enum": ["running", "completed", "needs_input", "blocked"]},
    "message": TEXT,
})


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     allow_nan=False).encode("utf-8")).hexdigest()


def number(value, minimum, maximum):
    return (type(value) in (int, float) and math.isfinite(value)
            and minimum <= value <= maximum)


def validate_script(script):
    if not isinstance(script, dict) or set(script) != {"title", "shots"}:
        raise ValueError("script 必须包含且只包含 title、shots")
    if not isinstance(script["title"], str) or not 1 <= len(script["title"]) <= 120:
        raise ValueError("title 长度应为 1–120")
    if not isinstance(script["shots"], list) or not 1 <= len(script["shots"]) <= 8:
        raise ValueError("shots 数量应为 1–8")
    for shot in script["shots"]:
        if not isinstance(shot, dict) or set(shot) != {"visual", "hold_seconds", "blocks"}:
            raise ValueError("分镜字段错误")
        if not isinstance(shot["visual"], str) or not 1 <= len(shot["visual"]) <= 200:
            raise ValueError("visual 不能为空或过长")
        if not number(shot["hold_seconds"], 0, 300):
            raise ValueError("hold_seconds 应为 0–300 的有限数值")
        if not isinstance(shot["blocks"], list) or not 1 <= len(shot["blocks"]) <= 8:
            raise ValueError("每个分镜应包含 1–8 个文案块")
        for block in shot["blocks"]:
            if not isinstance(block, dict) or set(block) != {"text", "source_id", "fact_id"}:
                raise ValueError("文案块字段错误")
            if any(not isinstance(v, str) for v in block.values()):
                raise ValueError("文案块各字段必须为字符串")
            if not 1 <= len(block["text"]) <= 500:
                raise ValueError("text 长度应为 1–500")


def validate_request(request):
    if not isinstance(request, dict):
        raise ValueError("输入必须是 JSON 对象")
    required = ("topic", "audience", "platform", "style", "product_id", "target_seconds")
    missing = [k for k in required if k not in request or request[k] is None or request[k] == ""]
    for key in required[:-1]:
        if key not in missing and (not isinstance(request[key], str) or not request[key].strip()
                                   or len(request[key]) > 500):
            raise ValueError(f"{key} 必须是 1–500 字符的非空字符串")
    if "target_seconds" not in missing and not number(request["target_seconds"], 1, 300):
        raise ValueError("target_seconds 必须是 1–300 的有限数值，表示时长上限")
    if request.get("initial_script") is not None:
        validate_script(request["initial_script"])
    return missing


def validate_action(action):
    if not isinstance(action, dict) or set(action) != set(ACTION_SCHEMA["properties"]):
        raise ValueError("动作应符合提供的 JSON schema")
    for key in ("action", "reason", "query", "status", "message"):
        if not isinstance(action[key], str) or len(action[key]) > 2000:
            raise ValueError(f"非法动作字段: {key}")
    if not action["reason"].strip():
        raise ValueError("必须给出简短、可观察的动作依据")
    if action["action"] not in ACTION_SCHEMA["properties"]["action"]["enum"]:
        raise ValueError("未知动作")
    if action["status"] not in ACTION_SCHEMA["properties"]["status"]["enum"]:
        raise ValueError("未知状态")
    if action["script"] is not None:
        validate_script(action["script"])
    if action["action"] == "write_script" and action["script"] is None:
        raise ValueError("write_script 必须提供 script")
