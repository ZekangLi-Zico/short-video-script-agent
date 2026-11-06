"""Deterministic offline stub. This is NOT evidence of model reasoning."""

from .tools import read_json, ROOT
from .expression import extended_review, expression_slots


def action(name, reason, query="", script=None, status="running", message=""):
    return {"action": name, "reason": reason, "query": query, "script": script, "status": status, "message": message}


def example_script(long=False, bad_claim=False):
    rules = read_json(ROOT / "data/brand_rules.json")
    return {"title": rules["allowed_titles"][0], "shots": [
        {"visual": rules["visuals"][0], "hold_seconds": 19 if long else 0,
         "blocks": [{"text": rules["creative_copy"][0], "source_id": "", "fact_id": ""}]},
        {"visual": rules["visuals"][2], "hold_seconds": 19 if long else 0,
         "blocks": [{"text": "效率提升80%。" if bad_claim else "剪影练习版支持为视频添加字幕。",
                     "source_id": "P01", "fact_id": "P01.F1"}]}]}


class MockModel:
    name = "mock"
    evidence_kind = "offline_mock_not_model_evidence"

    def review(self, request, script, rules_check=None, duration_check=None):
        report = {'items': [{'field': field, 'requirement': request[field], 'verdict': 'met',
                           'evidence': '固定离线桩返回；仅验证接线，不证明语义符合。'}
                          for field in ('topic', 'audience', 'platform', 'style')],
                'summary': '固定离线需求检查，不证明真实语义判断。'}
        if extended_review(request):
            slots = expression_slots(script) if request.get('expression_mode') == 'creative' else []
            report.update(expressions=[{**s, 'verdict':'plain_expression', 'references':[],
                                        'evidence':'固定离线桩，不证明语义事实正确'} for s in slots],
                          pacing={'verdict':'met','evidence':'固定离线桩，不证明节奏合适'})
        return report, {'provider': 'mock', 'warning': 'offline stub'}

    def decide(self, state, rules):
        history = state["history"]
        last = history[-1] if history else None
        if last and not last["observation"].get("ok", False):
            failures = sum(not e["observation"].get("ok", False) for e in history)
            if failures >= 2:
                response = action("finish", "离线桩：连续工具错误", status="blocked", message="工具失败，未完成。")
            else:
                response = action(last["action"], "离线桩：一次重试", query=state["request"]["topic"])
        elif not state["retrieved"]:
            searches = [h for h in history if h["action"] == "search_materials"]
            if len(searches) >= 2:
                response = action("finish", "离线桩：两次检索无资料", status="needs_input", message="未找到素材，请提供产品资料。")
            else:
                query = state["request"]["topic"] if not searches else "字幕"
                response = action("search_materials", "离线桩：检索或改写查询", query=query)
        elif state["script"] is None:
            source = next(iter(state["retrieved"].values()))
            fact = source["facts"][0]
            script = {"title": rules["allowed_titles"][0], "shots": [
                {"visual": rules["visuals"][2], "hold_seconds": 0,
                 "blocks": [{"text": fact["text"], "source_id": source["id"], "fact_id": fact["id"]}]}]}
            response = action("write_script", "离线桩：按检索事实组装脚本", script=script)
        elif state["duration"] is None:
            response = action("estimate_duration", "离线桩：检查当前稿时长")
        elif not state["duration"].get("passed"):
            if any(h["action"] == "write_script" for h in history):
                response = action("finish", "离线桩：最短事实脚本仍超时", status="blocked", message="无法在时长上限内保留事实，请增加时长。")
            else:
                source = next(iter(state["retrieved"].values()))
                fact = source["facts"][0]
                script = {"title": rules["allowed_titles"][0], "shots": [
                    {"visual": rules["visuals"][2], "hold_seconds": 0,
                     "blocks": [{"text": fact["text"], "source_id": source["id"], "fact_id": fact["id"]}]}]}
                response = action("write_script", "离线桩：删减超时稿", script=script)
        elif state["rules_check"] is None:
            response = action("check_rules", "离线桩：检查当前稿事实与规则")
        elif not state["rules_check"].get("passed"):
            source = next(iter(state["retrieved"].values()))
            fact = source["facts"][0]
            script = {"title": rules["allowed_titles"][0], "shots": [
                {"visual": rules["visuals"][2], "hold_seconds": 0,
                 "blocks": [{"text": fact["text"], "source_id": source["id"], "fact_id": fact["id"]}]}]}
            response = action("write_script", "离线桩：删除无依据宣传", script=script)
        elif state.get('requirements_check') is None:
            response = action('check_requirements', '离线桩：检查需求接线')
        elif not state['requirements_check'].get('passed'):
            response = action('finish', '离线桩：需求未满足', status='needs_input', message='当前稿未满足需求，请补充资料。')
        else:
            response = action("finish", "离线桩：检查通过", status="completed")
        return response, {"provider": "mock", "warning": "固定离线桩；不证明真实模型决策效果"}
