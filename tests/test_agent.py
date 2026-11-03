import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.evaluate import check_case, scenarios
from src.agent import Agent, ModelError
from src.mock import MockModel, action, example_script
from src.reporting import save_run
from src.schema import fingerprint
from src.tools import ToolBox, ROOT, read_json


class SequenceModel:
    name = "test_sequence"
    evidence_kind = "test_stub"

    def __init__(self, actions):
        self.actions = iter(actions)

    def decide(self, state, rules):
        return next(self.actions), {"provider": "test_sequence"}


class AgentTests(unittest.TestCase):
    def setUp(self):
        self.request = read_json(ROOT / "examples/inputs/normal.json")

    def test_all_acceptance_scenarios_offline(self):
        for name, request, failures, expected in scenarios():
            with self.subTest(case=name):
                result = Agent(MockModel(), ToolBox(failures=failures)).run(request)
                self.assertEqual(check_case(name, result, expected), [])
                self.assertEqual(result["metadata"]["evidence_kind"], "offline_mock_not_model_evidence")

    def test_cannot_finish_without_checks(self):
        model = SequenceModel([action("finish", "试图提前完成", status="completed")])
        result = Agent(model, ToolBox(), max_steps=1).run(self.request)
        self.assertEqual(result["status"], "step_limit")
        self.assertEqual(result["trace"][0]["observation"]["error"], "completion_gate_rejected")

    def test_revision_invalidates_both_checks(self):
        script = example_script()
        changed = copy.deepcopy(script)
        changed["shots"][0]["hold_seconds"] = 100
        actions = [action("search_materials", "查资料", query="字幕"), action("write_script", "生成", script=script),
                   action("estimate_duration", "估时"), action("check_rules", "查规则"),
                   action("write_script", "修改", script=changed), action("finish", "用旧结果完成", status="completed")]
        result = Agent(SequenceModel(actions), ToolBox(), max_steps=6).run(self.request)
        self.assertEqual(result["status"], "step_limit")
        self.assertIsNone(result["duration"])
        self.assertIsNone(result["rules_check"])

    def test_failed_check_cannot_be_reported_as_completed(self):
        actions = [action("search_materials", "检索", query="字幕"), action("write_script", "生成", script=example_script()),
                   action("estimate_duration", "估时"), action("check_rules", "检查"),
                   action("finish", "尝试完成", status="completed")]
        result = Agent(SequenceModel(actions), ToolBox(failures={"check_rules": -1}), max_steps=5).run(self.request)
        self.assertEqual(result["status"], "step_limit")
        self.assertFalse(result["rules_check"]["ok"])

    def test_unknown_action_is_observation_and_bounded(self):
        result = Agent(SequenceModel([action("publish", "未知动作")]), ToolBox(), max_steps=1).run(self.request)
        self.assertEqual(result["status"], "step_limit")
        self.assertEqual(result["trace"][0]["action"], "invalid_model_action")

    def test_missing_field_never_calls_model(self):
        del self.request["audience"]
        result = Agent(SequenceModel([]), ToolBox()).run(self.request)
        self.assertEqual(result["status"], "needs_input")
        self.assertIn("audience", result["message"])
        self.assertEqual(result["trace"], [])

    def test_invalid_target_values(self):
        for target in [0, -1, True, "30", float("nan"), float("inf"), 301]:
            with self.subTest(target=target):
                result = Agent(SequenceModel([]), ToolBox()).run({**self.request, "target_seconds": target})
                self.assertEqual(result["status"], "invalid_input")

    def test_model_error_is_not_offline_fallback(self):
        class Unavailable(SequenceModel):
            def decide(self, state, rules):
                raise ModelError("test_timeout")
        result = Agent(Unavailable([]), ToolBox()).run(self.request)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["trace"][0]["action"], "model_error")
        self.assertEqual(result["metadata"]["provider"], "test_sequence")

    def test_request_target_is_bound_by_host(self):
        self.request["target_seconds"] = 1
        result = Agent(MockModel(), ToolBox()).run(self.request)
        self.assertNotEqual(result["status"], "completed")
        self.assertEqual(result["duration"]["target_seconds"], 1)

    def test_valid_completion_and_saved_artifacts(self):
        tools = ToolBox()
        result = Agent(MockModel(), tools).run(self.request)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["duration"]["script_hash"], fingerprint(result["script"]))
        self.assertEqual(result["rules_check"]["script_hash"], fingerprint(result["script"]))
        scratch = ROOT / ".runtime/tests"
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as folder:
            self.assertTrue(Path(folder).resolve().is_relative_to(scratch.resolve()))
            save_run(folder, self.request, result, tools)
            for file in ("input.json", "output.json", "trace.jsonl", "script.md", "data_snapshot.json", "manifest.json"):
                self.assertTrue((Path(folder) / file).exists())
            stored = json.loads((Path(folder) / "output.json").read_text(encoding="utf-8"))
            self.assertEqual(stored["script"], result["script"])

    def test_no_mutation_of_input_or_materials(self):
        self.request["initial_script"] = example_script(long=True)
        before = copy.deepcopy(self.request)
        Agent(MockModel(), ToolBox()).run(self.request)
        self.assertEqual(self.request, before)

    def test_step_limit_is_validated(self):
        for value in [0, 51, True, 1.5]:
            with self.assertRaises(ValueError):
                Agent(MockModel(), ToolBox(), max_steps=value)


if __name__ == "__main__":
    unittest.main()
