"""Local business tools. No model decisions or automatic retries here."""

import copy
import json
import math
import re
from pathlib import Path

from .schema import fingerprint, number, validate_script

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"非法数值 {value}")))


def speech_units(text):
    """Each Han character / Latin word / number token is one speech unit."""
    return len(re.findall(r"[\u3400-\u9fff]|[A-Za-z]+(?:'[A-Za-z]+)?|\d+(?:\.\d+)?", text))


class ToolBox:
    def __init__(self, materials=None, rules=None, failures=None, synthetic_data=None):
        self.synthetic_data = (materials is None) if synthetic_data is None else bool(synthetic_data)
        self.materials = copy.deepcopy(materials if materials is not None else read_json(ROOT / "data/materials.json")["materials"])
        self.rules = copy.deepcopy(rules if rules is not None else read_json(ROOT / "data/brand_rules.json"))
        self._validate_data()
        self.failures = dict(failures or {})
        self.initial_failures = dict(self.failures)
        self.data_hash = fingerprint({"materials": self.materials, "rules": self.rules})

    def _validate_data(self):
        if not isinstance(self.materials, list):
            raise ValueError("materials 必须是数组")
        ids, fact_ids = set(), set()
        for material in self.materials:
            if not isinstance(material, dict):
                raise ValueError("素材必须是对象")
            for key in ("id", "product_id", "title", "version"):
                if not isinstance(material.get(key), str) or not material[key].strip():
                    raise ValueError(f"素材缺少非空字段 {key}")
            if material["id"] in ids:
                raise ValueError("素材 ID 必须唯一")
            ids.add(material["id"])
            if not isinstance(material.get("keywords"), list) or any(not isinstance(k, str) or not k for k in material["keywords"]):
                raise ValueError("keywords 必须是非空字符串数组")
            if not isinstance(material.get("facts"), list) or not material["facts"]:
                raise ValueError("每条素材至少包含一条事实")
            for fact in material["facts"]:
                if not isinstance(fact, dict) or any(not isinstance(fact.get(k), str) or not fact[k].strip() for k in ("id", "text")):
                    raise ValueError("事实必须包含非空 id 与 text")
                if fact["id"] in fact_ids:
                    raise ValueError("事实 ID 必须唯一")
                fact_ids.add(fact["id"])
        for key in ("allowed_titles", "creative_copy", "visuals", "forbidden_phrases"):
            value = self.rules.get(key)
            if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
                raise ValueError(f"品牌规则 {key} 必须为字符串数组")
        if not number(self.rules.get("speech_units_per_second"), 0.1, 20):
            raise ValueError("语速参数应为正的有限数值")
        for key in ("shot_pause_seconds", "min_shot_seconds"):
            if not number(self.rules.get(key), 0, 60):
                raise ValueError(f"非法时长规则：{key}")

    def call(self, name, args):
        if name not in {"search_materials", "estimate_duration", "check_rules"}:
            return {"ok": False, "error": "unknown_tool"}
        remaining = self.failures.get(name, 0)
        if remaining:
            if remaining > 0:
                self.failures[name] -= 1
            return {"ok": False, "error": "injected_tool_failure", "retryable": True,
                    "message": "测试环境注入的工具故障；未伪造成功结果"}
        try:
            return {"ok": True, **getattr(self, name)(**args)}
        except (ValueError, TypeError, KeyError) as exc:
            return {"ok": False, "error": "invalid_tool_arguments", "message": str(exc)}

    def search_materials(self, query, product_id):
        if not isinstance(query, str) or not 1 <= len(query.strip()) <= 200:
            raise ValueError("query 必须为 1–200 字符")
        q = query.strip().casefold()
        terms = re.findall(r"[a-z0-9]+|[\u3400-\u9fff]+", q)
        ranked = []
        for item in self.materials:
            if item["product_id"] != product_id:
                continue
            haystack = " ".join([item["title"], *item["keywords"], *(f["text"] for f in item["facts"])]).casefold()
            score = sum(2 for word in item["keywords"] if word.casefold() in q)
            score += sum(1 for term in terms if term in haystack)
            if score:
                ranked.append((score, item))
        ranked.sort(key=lambda entry: (-entry[0], entry[1]["id"]))
        return {"query": query, "product_id": product_id, "materials": [copy.deepcopy(item) for _, item in ranked[:5]],
                "count": len(ranked[:5])}

    def estimate_duration(self, script, target_seconds):
        validate_script(script)
        shots = []
        for index, shot in enumerate(script["shots"], 1):
            text = "".join(block["text"] for block in shot["blocks"])
            units = speech_units(text)
            seconds = max(self.rules["min_shot_seconds"], shot["hold_seconds"],
                          units / self.rules["speech_units_per_second"] + self.rules["shot_pause_seconds"])
            shots.append({"shot": index, "speech_units": units, "estimated_seconds": math.ceil(seconds * 10) / 10})
        total = round(sum(shot["estimated_seconds"] for shot in shots), 1)
        return {"script_hash": fingerprint(script), "shots": shots, "total_seconds": total,
                "target_seconds": target_seconds, "passed": total <= target_seconds,
                "method": "max(旁白单位数/语速+停顿, 画面停留, 最短镜头); 按镜头向上取整到0.1秒",
                "is_estimate": True}

    def check_rules(self, script, retrieved_ids):
        validate_script(script)
        issues, citations = [], []
        allowed = {item["id"]: item for item in self.materials if item["id"] in retrieved_ids}
        if script["title"] not in self.rules["allowed_titles"]:
            issues.append({"code": "unapproved_title", "location": "title"})
        for i, shot in enumerate(script["shots"], 1):
            if shot["visual"] not in self.rules["visuals"]:
                issues.append({"code": "unapproved_visual", "location": f"shot:{i}"})
            for j, block in enumerate(shot["blocks"], 1):
                where = f"shot:{i}/block:{j}"
                source = allowed.get(block["source_id"])
                if not block["source_id"] and not block["fact_id"]:
                    if block["text"] not in self.rules["creative_copy"]:
                        issues.append({"code": "unapproved_copy", "location": where, "text": block["text"]})
                elif source is None:
                    issues.append({"code": "source_not_retrieved", "location": where, "source_id": block["source_id"]})
                else:
                    fact = next((f for f in source["facts"] if f["id"] == block["fact_id"]), None)
                    if fact is None or block["text"] != fact["text"]:
                        issues.append({"code": "unsupported_claim", "location": where, "text": block["text"]})
                    else:
                        citations.append({"location": where, "source_id": source["id"], "fact_id": fact["id"],
                                          "quote": fact["text"], "version": source["version"]})
        if not citations:
            issues.append({"code": "no_supported_product_fact", "location": "script"})
        all_text = json.dumps(script, ensure_ascii=False)
        for phrase in self.rules["forbidden_phrases"]:
            if phrase in all_text:
                issues.append({"code": "brand_rule_violation", "phrase": phrase})
        return {"script_hash": fingerprint(script), "passed": not issues, "issues": issues,
                "citations": citations, "rules_version": self.rules["version"]}
