"""Bounded model -> action -> observation loop with evidence-bound completion."""

import copy
import time
from datetime import datetime, timezone

from .schema import fingerprint, validate_action, validate_request


class ModelError(RuntimeError):
    """Sanitized backend error, safe to include in an artifact."""


class Agent:
    def __init__(self, model, tools, max_steps=12, on_event=None, cancel_event=None):
        if type(max_steps) is not int or not 1 <= max_steps <= 50:
            raise ValueError("max_steps 应为 1–50 的整数")
        self.model, self.tools, self.max_steps = model, tools, max_steps
        self.on_event, self.cancel_event = on_event, cancel_event

    def run(self, request):
        started = datetime.now(timezone.utc).isoformat()
        state = {"request": copy.deepcopy(request), "script": None, "retrieved": {},
                 "duration": None, "rules_check": None, "history": [], "max_steps": self.max_steps}

        def emit(kind, step):
            if self.on_event:
                self.on_event(copy.deepcopy({"kind": kind, "step": step, "script": state["script"],
                                             "duration": state["duration"], "rules_check": state["rules_check"],
                                             "trace": state["history"]}))

        def record(entry):
            state["history"].append(entry)
            emit("step", entry["step"])

        def result(status, message):
            return {"status": status, "message": message, "script": state["script"],
                    "duration": state["duration"], "rules_check": state["rules_check"],
                    "sources": list(state["retrieved"].values()), "trace": state["history"],
                    "metadata": {"started_at": started, "finished_at": datetime.now(timezone.utc).isoformat(),
                                 "provider": self.model.name, "evidence_kind": self.model.evidence_kind,
                                 "data_hash": self.tools.data_hash, "max_steps": self.max_steps,
                                 "steps": len(state["history"]), "synthetic_data": self.tools.synthetic_data,
                                 "model_responses": sum("model" in item for item in state["history"])}}
        try:
            missing = validate_request(request)
        except ValueError as exc:
            return result("invalid_input", str(exc))
        if missing:
            return result("needs_input", "请补充关键字段：" + "、".join(missing))
        state["script"] = copy.deepcopy(request.get("initial_script"))
        for step in range(1, self.max_steps + 1):
            if self.cancel_event and self.cancel_event.is_set():
                return result("cancelled", "已停止后续步骤，保留已有草稿和执行记录。")
            emit("thinking", step)
            tick = time.monotonic()
            try:
                action, meta = self.model.decide(copy.deepcopy(state), copy.deepcopy(self.tools.rules))
            except ModelError as exc:
                record({"step": step, "action": "model_error", "arguments": {},
                                         "decision_basis": "模型不可用，不能继续决策",
                                         "observation": {"ok": False, "error": str(exc)}})
                return result("blocked", "模型调用失败，未完成；见执行记录。")
            if self.cancel_event and self.cancel_event.is_set():
                return result("cancelled", "当前模型调用已返回，已停止执行后续动作。")
            try:
                validate_action(action)
            except ValueError as exc:
                record({"step": step, "action": "invalid_model_action", "arguments": {},
                                         "decision_basis": "结构校验失败，反馈模型调整",
                                         "observation": {"ok": False, "error": str(exc)}, "model": meta})
                continue
            name = action["action"]
            args = {}
            finish = None
            if name == "search_materials":
                args = {"query": action["query"], "product_id": request["product_id"]}
                observation = self.tools.call(name, args)
                if observation["ok"]:
                    for material in observation["materials"]:
                        state["retrieved"][material["id"]] = material
            elif name == "write_script":
                args = {"script": copy.deepcopy(action["script"])}
                state["script"] = copy.deepcopy(action["script"])
                state["duration"] = state["rules_check"] = None
                observation = {"ok": True, "script_hash": fingerprint(state["script"]),
                               "message": "已更新草稿，必须对本稿重新运行时长与规则检查"}
            elif name in {"estimate_duration", "check_rules"}:
                if state["script"] is None:
                    observation = {"ok": False, "error": "no_script", "message": "请先生成草稿"}
                else:
                    args = {"script": copy.deepcopy(state["script"])}
                    if name == "estimate_duration":
                        args["target_seconds"] = request["target_seconds"]
                        observation = self.tools.call(name, args)
                        state["duration"] = observation
                    else:
                        args["retrieved_ids"] = sorted(state["retrieved"])
                        observation = self.tools.call(name, args)
                        state["rules_check"] = observation
            else:
                args = {"status": action["status"], "message": action["message"]}
                if action["status"] == "completed":
                    current = fingerprint(state["script"]) if state["script"] else None
                    checks = [state["duration"], state["rules_check"]]
                    passed = current and all(c and c.get("ok") and c.get("passed")
                                             and c.get("script_hash") == current for c in checks)
                    if passed:
                        observation = {"ok": True, "status": "completed", "script_hash": current}
                        finish = ("completed", "脚本已通过来源、规则与预计时长检查；仍为可编辑脚本，未生成或发布视频。")
                    else:
                        observation = {"ok": False, "error": "completion_gate_rejected",
                                       "message": "只有当前稿件的时长和规则检查均通过，才能完成"}
                elif action["status"] in {"needs_input", "blocked"} and action["message"].strip():
                    observation = {"ok": True, "status": action["status"]}
                    finish = (action["status"], action["message"])
                else:
                    observation = {"ok": False, "error": "invalid_finish_status"}
            record({"step": step, "action": name, "arguments": args,
                                     "decision_basis": action["reason"], "observation": observation,
                                     "model": meta, "elapsed_ms": round((time.monotonic() - tick) * 1000)})
            if finish:
                return result(*finish)
        return result("step_limit", "达到最大决策步数，任务未完成；保留草稿和已执行检查，不声明成功。")
