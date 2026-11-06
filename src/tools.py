"""Local business tools. No model decisions or automatic retries here."""

import copy
import json
import math
import re
from pathlib import Path

from .schema import fingerprint, number, validate_script
from .expression import expression_slots
from .timing import estimate_tracks

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"非法数值 {value}")))


def speech_units(text):
    """Each Han character / Latin word / number token is one speech unit."""
    return len(re.findall(r"[\u3400-\u9fff]|[A-Za-z]+(?:'[A-Za-z]+)?|\d+(?:\.\d+)?", text))


class ToolBox:
    search_contract = 'id_first_v2'

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
        # The dossier exposes card IDs so a model can deliberately fetch a scene
        # without common character names pushing it out of the top five.
        requested = set(re.findall(r'[a-z0-9]+(?:-[a-z0-9]+)*', q))
        exact = [m for m in self.materials if m['product_id'] == product_id and m['id'].casefold() in requested]
        if exact:
            return {'query':query, 'product_id':product_id, 'materials':copy.deepcopy(exact[:5]), 'count':len(exact[:5])}
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

    def estimate_duration(self, script, target_seconds, duration_mode='max'):
        validate_script(script)
        if duration_mode not in {'max', 'target'} or not number(target_seconds, 1, 300):
            raise ValueError('非法时长模式或目标秒数')
        shots = []
        for index, shot in enumerate(script["shots"], 1):
            if script.get('format_version') in (2, 3):
                shots.append({'shot':index, **estimate_tracks(shot,self.rules)})
                continue
            text = "".join(block["text"] for block in shot["blocks"])
            units = speech_units(text)
            seconds = max(self.rules["min_shot_seconds"], shot["hold_seconds"],
                          units / self.rules["speech_units_per_second"] + self.rules["shot_pause_seconds"])
            shots.append({"shot": index, "speech_units": units, "estimated_seconds": math.ceil(seconds * 10) / 10})
        total = round(sum(shot["estimated_seconds"] for shot in shots), 1)
        result = {"script_hash": fingerprint(script), "shots": shots, "total_seconds": total,
                "target_seconds": target_seconds, "passed": total <= target_seconds,
                "method": "max(旁白单位数/语速+停顿, 画面停留, 最短镜头); 按镜头向上取整到0.1秒",
                "is_estimate": True}
        if script.get('format_version') in (2, 3):
            result['method']='声画节拍v2：同拍max(旁白,全部屏幕文字阅读,展示停留)，不同拍相加；镜头取累计与最低停留较大者；中文4字/秒（资料配置），英文2.5词/秒'
        if duration_mode == 'target':
            minimum = round(target_seconds * 0.9, 4)
            result.update(duration_mode='target', min_seconds=minimum, max_seconds=target_seconds,
                          passed=minimum <= total <= target_seconds,
                          issue='too_short' if total < minimum else 'too_long' if total > target_seconds else None)
        if script.get('format_version') == 3:
            result['method']='动作与声画v3：每段max(声音,屏幕文字阅读,展示停留,动作最低时长)，各段相加；再取镜头最低停留较大者。说话者和动作说明不计入朗读。'
        return result

    def check_rules(self, script, retrieved_ids, expression_mode='strict'):
        validate_script(script)
        if expression_mode not in {'strict', 'creative'}:
            raise ValueError('非法表达模式')
        issues, citations = [], []
        if script.get('format_version') == 3 and expression_mode == 'strict':
            issues.append({'code':'staging_requires_creative_mode','location':'script'})
        allowed = {item["id"]: item for item in self.materials if item["id"] in retrieved_ids}
        if expression_mode == 'strict' and script["title"] not in self.rules["allowed_titles"]:
            issues.append({"code": "unapproved_title", "location": "title"})
        for i, shot in enumerate(script["shots"], 1):
            if expression_mode == 'strict' and shot["visual"] not in self.rules["visuals"]:
                issues.append({"code": "unapproved_visual", "location": f"shot:{i}"})
            for j, block in enumerate(shot["blocks"], 1):
                where = f"shot:{i}/block:{j}"
                source = allowed.get(block["source_id"])
                if not block["source_id"] and not block["fact_id"]:
                    if expression_mode == 'strict' and block["text"] not in self.rules["creative_copy"]:
                        issues.append({"code": "unapproved_copy", "location": where, "text": block["text"]})
                elif source is None:
                    issues.append({"code": "source_not_retrieved", "location": where, "source_id": block["source_id"]})
                else:
                    fact = next((f for f in source["facts"] if f["id"] == block["fact_id"]), None)
                    paraphrase = script.get('format_version') in (2, 3) and expression_mode == 'creative'
                    if fact is None or (not paraphrase and block["text"] != fact["text"]):
                        issues.append({"code": "unsupported_claim", "location": where, "text": block["text"]})
                    else:
                        citations.append({"location": where, "source_id": source["id"], "fact_id": fact["id"],
                                          "quote": fact["text"], "version": source["version"]})
                        if script.get('format_version') in (2, 3):
                            citations[-1].update(text=block['text'], requires_semantic_review=paraphrase)
        if not citations:
            issues.append({"code": "no_supported_product_fact", "location": "script"})
        # Editorial notes can quote a rejected claim to explain its removal.
        # They are not video copy; every actual title/shot/block remains checked.
        all_text = json.dumps({'title': script['title'], 'shots': script['shots']}, ensure_ascii=False)
        if script.get('format_version') in (2, 3):
            all_text = '\n'.join([script['title'], *[s['visual'] for s in script['shots']],
                                  *[b['text'] for s in script['shots'] for b in s['blocks']]])
        if script.get('format_version') == 3:
            all_text='\n'.join(slot['text'] for slot in expression_slots(script))
        for phrase in self.rules["forbidden_phrases"]:
            if phrase in all_text:
                issues.append({"code": "brand_rule_violation", "phrase": phrase})
        result = {"script_hash": fingerprint(script), "passed": not issues, "issues": issues,
                  "citations": citations, "rules_version": self.rules["version"]}
        if self.rules.get('material_kind') == 'narrative':
            result['material_kind'] = 'narrative'
        if expression_mode == 'creative':
            result.update(requires_expression_review=True, expression_slots=expression_slots(script),
                          available_facts=[{'source_id': m['id'], 'fact_id': f['id'], 'quote': f['text'], 'version': m['version']}
                                           for m in allowed.values() for f in m['facts']],
                          scope='exact_quote_and_brand_checks_only; expression semantics require independent model review')
            if script.get('format_version') in (2, 3):
                result['scope']='source_identity_and_brand_checks; every public claim requires semantic entailment review'
        return result
