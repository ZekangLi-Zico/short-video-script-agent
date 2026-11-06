"""Bounded model -> action -> observation loop with evidence-bound completion."""

import copy
import time
from datetime import datetime, timezone
from .version import APP_VERSION

from .schema import fingerprint, validate_action, validate_request
from .requirements import review_observation, bound_duration_check
from .revisions import revision_summary, failed_feedback


class ModelError(RuntimeError):
    """Sanitized backend error, safe to include in an artifact."""


def model_failure_message(error, phase):
    code = str(error).split(';', 1)[0]
    cause = {'codex_timeout':'等待超时', 'codex_model_at_capacity':'服务暂时繁忙',
             'codex_stream_disconnected':'连接中断', 'codex_authentication_failed':'鉴权失败',
             'codex_rate_limited':'请求受到限流'}.get(code, '调用失败')
    return f'模型{phase}{cause}，任务未完成；已有草稿和执行记录已保留，可稍后重试。'


class Agent:
    def __init__(self, model, tools, max_steps=12, on_event=None, cancel_event=None):
        if type(max_steps) is not int or not 1 <= max_steps <= 50:
            raise ValueError("max_steps 应为 1–50 的整数")
        self.model, self.tools, self.max_steps = model, tools, max_steps
        self.on_event, self.cancel_event = on_event, cancel_event

    def run(self, request):
        started = datetime.now(timezone.utc).isoformat()
        state = {"request": copy.deepcopy(request), "script": None, "retrieved": {},
                 "duration": None, "rules_check": None, "requirements_check": None,
                 "history": [], "max_steps": self.max_steps, "rules_retrieved_ids":None}

        def emit(kind, step, checkpoint=None):
            if self.on_event:
                self.on_event(copy.deepcopy({"kind": kind, "step": step, "script": state["script"],
                                             "duration": state["duration"], "rules_check": state["rules_check"],
                                             "requirements_check": state["requirements_check"],
                                             "trace": state["history"],
                                             "snapshot": checkpoint if checkpoint is not None else result('in_progress', '任务执行中，尚未完成。')}))

        def record(entry):
            state["history"].append(entry)
            emit("step", entry["step"])

        def result(status, message):
            return {"status": status, "message": message, "script": state["script"],
                    "duration": state["duration"], "rules_check": state["rules_check"],
                    "requirements_check": state["requirements_check"],
                    "sources": list(state["retrieved"].values()), "trace": state["history"],
                    "metadata": {"app_version": APP_VERSION, "started_at": started, "finished_at": datetime.now(timezone.utc).isoformat(),
                                 "provider": self.model.name, "evidence_kind": self.model.evidence_kind,
                                 "data_hash": self.tools.data_hash, "max_steps": self.max_steps,
                                 "tool_contracts": {"search_materials": self.tools.search_contract},
                                 "steps": len(state["history"]), "synthetic_data": self.tools.synthetic_data,
                                 "completion_policy": "facts_duration_requirements_v6",
                                 "requirements_review_context": "current_rules_and_duration_v2",
                                 "script_format": "staged_storyboard_v3; legacy_v1_v2_readable",
                                 "model_responses": sum(("model" in item) + ("review_model" in item)
                                                        for item in state["history"])}}
        try:
            missing = validate_request(request)
        except ValueError as exc:
            return result("invalid_input", str(exc))
        if missing:
            return result("needs_input", "请补充关键字段：" + "、".join(missing))
        state["script"] = copy.deepcopy(request.get("initial_script"))
        if hasattr(self.model,'cancel_event'):
            self.model.cancel_event = self.cancel_event
        for step in range(1, self.max_steps + 1):
            if self.cancel_event and self.cancel_event.is_set():
                return result("cancelled", "已停止后续步骤，保留已有草稿和执行记录。")
            emit("thinking", step)
            step_checkpoint = result('in_progress', '任务执行中，尚未完成。')
            if hasattr(self.model,'on_retry'):
                self.model.on_retry = lambda failure: emit('retrying_review' if failure.get('phase') == 'review'
                                                           else 'retrying_decision',step,step_checkpoint)
            tick = time.monotonic()
            try:
                action, meta = self.model.decide(copy.deepcopy(state), copy.deepcopy(self.tools.rules))
            except ModelError as exc:
                record({"step": step, "action": "model_error", "arguments": {},
                                         "decision_basis": "模型不可用，不能继续决策",
                                         "observation": {"ok": False, "error": str(exc)}})
                return result("blocked", model_failure_message(exc, '决策'))
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
            review_meta = {}
            preflight = []
            if name == "search_materials":
                args = {"query": action["query"], "product_id": request["product_id"]}
                observation = self.tools.call(name, args)
                if observation["ok"]:
                    for material in observation["materials"]:
                        state["retrieved"][material["id"]] = material
            elif name == "write_script":
                args = {"script": copy.deepcopy(action["script"])}
                revision = revision_summary(state['script'], action['script'], failed_feedback(state))
                state["script"] = copy.deepcopy(action["script"])
                state["duration"] = state["rules_check"] = state["requirements_check"] = None
                observation = {"ok": True, "script_hash": fingerprint(state["script"]),
                               "revision": revision,
                               "message": "已更新草稿，必须对本稿重新运行时长、规则与需求检查"}
            elif name in {"estimate_duration", "check_rules", "check_requirements"}:
                if state["script"] is None:
                    observation = {"ok": False, "error": "no_script", "message": "请先生成草稿"}
                else:
                    args = {"script": copy.deepcopy(state["script"])}
                    if name == "estimate_duration":
                        args["target_seconds"] = request["target_seconds"]
                        if 'duration_mode' in request:
                            args['duration_mode'] = request['duration_mode']
                        observation = self.tools.call(name, args)
                        state["duration"] = observation
                    elif name == "check_rules":
                        args["retrieved_ids"] = sorted(state["retrieved"])
                        if 'expression_mode' in request:
                            args['expression_mode'] = request['expression_mode']
                        observation = self.tools.call(name, args)
                        state["rules_check"] = observation
                        state['rules_retrieved_ids'] = sorted(state['retrieved'])
                    else:
                        # A model-selected review action can bundle cheap local
                        # checks; its real observations remain independently replayable.
                        emit('checking',step)
                        current = fingerprint(state['script'])
                        for tool, key, extra in (
                            ('estimate_duration','duration',{'target_seconds':request['target_seconds'], **({'duration_mode':request['duration_mode']} if 'duration_mode' in request else {})}),
                            ('check_rules','rules_check',{'retrieved_ids':sorted(state['retrieved']), **({'expression_mode':request['expression_mode']} if 'expression_mode' in request else {})})):
                            checked = state[key]
                            valid = checked and checked.get('ok') and checked.get('script_hash') == current
                            if key == 'duration':
                                valid = valid and bound_duration_check(checked,request,state['script']) is not None
                            else:
                                valid = valid and state['rules_retrieved_ids'] == sorted(state['retrieved'])
                            if not valid:
                                tool_args = {'script':copy.deepcopy(state['script']), **extra}
                                state[key] = self.tools.call(tool,tool_args)
                                if key == 'rules_check': state['rules_retrieved_ids'] = sorted(state['retrieved'])
                                preflight.append({'action':tool,'arguments':tool_args,'observation':copy.deepcopy(state[key])})
                        args['request'] = copy.deepcopy(request)
                        checked = state['rules_check']
                        args['rules_check'] = copy.deepcopy(checked) if checked and checked.get('script_hash') == fingerprint(state['script']) else None
                        args['duration_check'] = bound_duration_check(state['duration'], request, state['script'])
                        try:
                            if not all(c and c.get('ok') and c.get('passed') for c in (state['duration'],state['rules_check'])):
                                raise ValueError('local_checks_failed')
                            emit('reviewing',step,step_checkpoint)
                            if self.cancel_event and self.cancel_event.is_set():
                                raise ValueError('review_cancelled')
                            review, review_model = self.model.review(copy.deepcopy(request), copy.deepcopy(state['script']), copy.deepcopy(args['rules_check']), copy.deepcopy(args['duration_check']))
                            review_meta = {'review_model': review_model}
                            if self.cancel_event and self.cancel_event.is_set():
                                observation = {'ok': False, 'error': 'review_cancelled'}
                            else:
                                observation = review_observation(review, request, state['script'], args['rules_check'])
                        except ModelError as exc:
                            observation = {'ok': False, 'error': 'requirements_review_failed', 'message': str(exc)}
                            # The adapter already applied its bounded recovery.
                            # Do not spend another decision call asking a failed provider what to do.
                            finish = ('cancelled', '已停止后续步骤，保留已有草稿和执行记录。') if (
                                self.cancel_event and self.cancel_event.is_set()) else (
                                'blocked', model_failure_message(exc, '需求审核'))
                        except ValueError as exc:
                            error = str(exc) if str(exc) in {'local_checks_failed','review_cancelled'} else 'requirements_review_failed'
                            message = '时长或规则检查发现需要处理的内容，先根据检查结果修订或补查。' if error=='local_checks_failed' else str(exc)
                            observation = {'ok': False, 'error': error, 'message': message}
                        state['requirements_check'] = observation
            else:
                args = {"status": action["status"], "message": action["message"]}
                if action["status"] == "completed":
                    current = fingerprint(state["script"]) if state["script"] else None
                    checks = [state["duration"], state["rules_check"], state['requirements_check']]
                    passed = current and all(c and c.get("ok") and c.get("passed")
                                             and c.get("script_hash") == current for c in checks)
                    passed = passed and state['requirements_check'].get('request_hash') == fingerprint(request)
                    if passed:
                        observation = {"ok": True, "status": "completed", "script_hash": current}
                        explanation = action["message"].strip()
                        checked_note = "当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。"
                        finish = ("completed", (explanation + "\n\n" if explanation else "") + checked_note)
                    else:
                        observation = {"ok": False, "error": "completion_gate_rejected",
                                       "message": "只有当前稿件的时长、规则和需求检查均通过，才能完成；遗漏需求时修订或说明缺口。"}
                elif action["status"] in {"needs_input", "blocked"} and action["message"].strip():
                    observation = {"ok": True, "status": action["status"]}
                    finish = (action["status"], action["message"])
                else:
                    observation = {"ok": False, "error": "invalid_finish_status"}
            record({"step": step, "action": name, "arguments": args,
                                     "decision_basis": action["reason"], "observation": observation,
                                     **({'preflight_checks':preflight} if preflight else {}),
                                     "model": meta, **review_meta, "elapsed_ms": round((time.monotonic() - tick) * 1000)})
            if finish:
                return result(*finish)
        return result("step_limit", "达到最大决策步数，任务未完成；保留草稿和已执行检查，不声明成功。")
