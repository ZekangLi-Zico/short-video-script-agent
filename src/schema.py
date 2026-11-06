"""Shared structured action schema and strict boundary validation."""

import hashlib
import json
import math


def obj(properties):
    return {"type": "object", "properties": properties,
            "required": list(properties), "additionalProperties": False}


TEXT = {"type": "string"}
BLOCK_SCHEMA = obj({"text": TEXT, "source_id": TEXT, "fact_id": TEXT,
                    "channel": {"type": "string", "enum": ["voice", "screen", "both"]},
                    "beat": {"type": "integer", "minimum": 1, "maximum": 8},
                    "display_seconds": {"type": "number", "minimum": 0, "maximum": 300}})
SHOT_SCHEMA = obj({"purpose": TEXT, "visual": TEXT, "hold_seconds": {"type": "number"},
                   "blocks": {"type": "array", "items": BLOCK_SCHEMA, "minItems":1, "maxItems":8}})
SCRIPT_SCHEMA = obj({"format_version": {"type": "integer", "enum": [2]}, "title": TEXT, "shots": {"type": "array", "items": SHOT_SCHEMA, "minItems":1, "maxItems":8},
                     "editor_notes": TEXT})
ACTION_SCHEMA = obj({
    "action": {"type": "string", "enum": ["search_materials", "write_script", "estimate_duration", "check_rules", "check_requirements", "finish"]},
    "reason": TEXT,
    "query": TEXT,
    "script": {"anyOf": [SCRIPT_SCHEMA, {"type": "null"}]},
    "status": {"type": "string", "enum": ["running", "completed", "needs_input", "blocked"]},
    "message": TEXT,
})

STAGING_SCHEMA = obj({'beat': {'type':'integer','minimum':1,'maximum':8},
    'action': TEXT, 'camera': TEXT, 'sound': TEXT,
    'min_seconds': {'type':'number','minimum':0,'maximum':300}})
STAGED_BLOCK_SCHEMA = obj({**BLOCK_SCHEMA['properties'], 'speaker': TEXT})
STAGED_SHOT_SCHEMA = obj({**SHOT_SCHEMA['properties'],
    'staging': {'type':'array','items':STAGING_SCHEMA,'minItems':1,'maxItems':8},
    'blocks': {'type':'array','items':STAGED_BLOCK_SCHEMA,'minItems':0,'maxItems':8}})
STAGED_SCRIPT_SCHEMA = obj({**SCRIPT_SCHEMA['properties'],
    'format_version': {'type':'integer','enum':[3]},
    'shots': {'type':'array','items':STAGED_SHOT_SCHEMA,'minItems':1,'maxItems':8}})
STAGED_ACTION_SCHEMA = obj({**ACTION_SCHEMA['properties'],
    'script': {'anyOf':[STAGED_SCRIPT_SCHEMA,{'type':'null'}]}})


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     allow_nan=False).encode("utf-8")).hexdigest()


def number(value, minimum, maximum):
    return (type(value) in (int, float) and math.isfinite(value)
            and minimum <= value <= maximum)


def validate_script(script):
    if not isinstance(script, dict):
        raise ValueError('script 必须为对象')
    v3 = type(script.get('format_version')) is int and script['format_version'] == 3
    v2 = type(script.get('format_version')) is int and script['format_version'] in (2, 3)
    keys = {"title", "shots", "editor_notes", "format_version"} if v2 else None
    if (v2 and set(script) != keys) or (not v2 and set(script) not in ({"title", "shots"}, {"title", "shots", "editor_notes"})):
        raise ValueError("script 必须包含 title、shots；可选 editor_notes")
    # Legacy drafts stay valid; the real-model schema asks new drafts to supply
    # an empty string when no editorial explanation is needed.
    if 'editor_notes' in script and (not isinstance(script['editor_notes'], str) or len(script['editor_notes']) > 2000):
        raise ValueError('editor_notes 必须是0至2000字符的字符串')
    if not isinstance(script["title"], str) or not 1 <= len(script["title"]) <= 120:
        raise ValueError("title 长度应为 1–120")
    if not isinstance(script["shots"], list) or not 1 <= len(script["shots"]) <= 8:
        raise ValueError("shots 数量应为 1–8")
    for shot in script["shots"]:
        shot_keys = {"visual", "hold_seconds", "blocks"} | ({'purpose'} if v2 else set()) | ({'staging'} if v3 else set())
        if not isinstance(shot, dict) or set(shot) != shot_keys:
            raise ValueError("分镜字段错误")
        if v2 and (not isinstance(shot['purpose'], str) or not 1 <= len(shot['purpose'].strip()) <= 200):
            raise ValueError('purpose 应明确本镜内容目的，1–200字符')
        if not isinstance(shot["visual"], str) or not 1 <= len(shot["visual"]) <= 200:
            raise ValueError("visual 不能为空或过长")
        if not number(shot["hold_seconds"], 0, 300):
            raise ValueError("hold_seconds 应为 0–300 的有限数值")
        if not isinstance(shot["blocks"], list) or not (0 if v3 else 1) <= len(shot["blocks"]) <= 8:
            raise ValueError("每个分镜应包含 1–8 个文案块")
        for block in shot["blocks"]:
            block_keys = {"text", "source_id", "fact_id"} | ({'channel', 'beat', 'display_seconds'} if v2 else set()) | ({'speaker'} if v3 else set())
            if not isinstance(block, dict) or set(block) != block_keys:
                raise ValueError("文案块字段错误")
            if any(not isinstance(block[k], str) for k in ('text', 'source_id', 'fact_id')):
                raise ValueError("文案块各字段必须为字符串")
            if v2:
                if not isinstance(block['channel'],str) or block['channel'] not in {'voice','screen','both'}:
                    raise ValueError('channel 应为 voice/screen/both')
                if type(block['beat']) is not int or not 1 <= block['beat'] <= 8:
                    raise ValueError('beat 应为1–8整数')
                if not number(block['display_seconds'],0,300) or (block['channel']=='voice' and block['display_seconds']!=0):
                    raise ValueError('display_seconds 应为0–300秒；纯旁白填0')
            if not 1 <= len(block["text"]) <= 500:
                raise ValueError("text 长度应为 1–500")
            if v3:
                speaker = block['speaker']
                if (not isinstance(speaker,str) or len(speaker)>60
                        or (block['channel']=='screen' and speaker!='')
                        or (block['channel']!='screen' and not speaker.strip())):
                    raise ValueError('有声内容须标明说话者或旁白；屏幕文字speaker填空')
        if v3:
            stages=shot['staging']
            if not isinstance(stages,list) or not 1<=len(stages)<=8:
                raise ValueError('每镜staging须包含1–8个动作段')
            seen=set()
            for stage in stages:
                if not isinstance(stage,dict) or set(stage)!=set(STAGING_SCHEMA['properties']):
                    raise ValueError('动作段字段错误')
                beat=stage['beat']
                if type(beat) is not int or not 1<=beat<=8 or beat in seen:
                    raise ValueError('动作段beat须为不重复的1–8整数')
                seen.add(beat)
                for key,limit in [('action',240),('camera',100),('sound',100)]:
                    if not isinstance(stage[key],str) or len(stage[key])>limit or (key=='action' and not stage[key].strip()):
                        raise ValueError('动作须具体非空；动作/镜头/现场声超出长度限制')
                if not number(stage['min_seconds'],0,300):
                    raise ValueError('动作min_seconds须为0–300的有限数值')
                if not any(b['beat']==beat for b in shot['blocks']) and stage['min_seconds']<=0:
                    raise ValueError('无对白或屏幕文字的动作段须安排正数时长')
            if any(b['beat'] not in seen for b in shot['blocks']):
                raise ValueError('每段文案须有对应beat的动作安排')


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
        raise ValueError("target_seconds 必须是 1–300 的有限数值")
    if request.get("initial_script") is not None:
        validate_script(request["initial_script"])
    if request.get('expression_mode', 'strict') not in ('strict', 'creative'):
        raise ValueError('expression_mode 必须为 strict 或 creative')
    if request.get('duration_mode', 'max') not in ('max', 'target'):
        raise ValueError('duration_mode 必须为 max 或 target')
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
