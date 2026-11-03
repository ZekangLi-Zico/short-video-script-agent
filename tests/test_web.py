import copy
import http.client
import json
import tempfile
import threading
import time
import unittest
from pathlib import Path

from src.agent import Agent
from src.mock import MockModel, action
from src.tools import ROOT, ToolBox, read_json
from src.web import BusyError, RunManager, make_server


def wait_finished(manager, run_id):
    deadline = time.monotonic() + 3
    while time.monotonic() < deadline:
        job = manager.get(run_id)
        if job["state"] != "running":
            return job
        time.sleep(0.01)
    raise AssertionError("test job timed out")


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.request = read_json(ROOT / "examples/inputs/normal.json")

    def test_progress_exposes_actual_steps_without_mutating_core_state(self):
        events = []
        def observer(event):
            events.append(copy.deepcopy(event))
            event["trace"].clear()
            if event["script"]:
                event["script"]["title"] = "must not leak into core"
        result = Agent(MockModel(), ToolBox(), on_event=observer).run(self.request)
        self.assertEqual(result["status"], "completed")
        self.assertEqual([e["step"] for e in events if e["kind"] == "step"], [1, 2, 3, 4, 5])
        self.assertEqual(len(result["trace"]), 5)
        self.assertNotEqual(result["script"]["title"], "must not leak into core")

    def test_cancel_before_model_never_calls_model(self):
        stop = threading.Event()
        stop.set()
        result = Agent(MockModel(), ToolBox(), cancel_event=stop).run(self.request)
        self.assertEqual(result["status"], "cancelled")
        self.assertEqual(result["trace"], [])

    def test_cancel_after_model_prevents_tool_execution(self):
        stop = threading.Event()
        class CancelModel(MockModel):
            def decide(self, state, rules):
                stop.set()
                return action("search_materials", "test", query="字幕"), {}
        result = Agent(CancelModel(), ToolBox(), cancel_event=stop).run(self.request)
        self.assertEqual(result["status"], "cancelled")
        self.assertEqual(result["sources"], [])


class WebTests(unittest.TestCase):
    def setUp(self):
        scratch = ROOT / ".runtime/tests"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=scratch)
        self.assertTrue(Path(self.temp.name).resolve().is_relative_to(scratch.resolve()))
        self.manager = RunManager(self.temp.name, lambda provider, timeout: MockModel())
        self.server = make_server(0, self.manager)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.port = self.server.server_port
        status, data, _ = self.http("GET", "/api/config")
        self.assertEqual(status, 200)
        self.token = json.loads(data)["token"]
        self.request = read_json(ROOT / "examples/inputs/normal.json")

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)
        self.temp.cleanup()

    def http(self, method, path, data=None, headers=None):
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=3)
        payload = json.dumps(data).encode() if data is not None else None
        merged = {"Content-Type": "application/json"}
        merged.update(headers or {})
        connection.request(method, path, body=payload, headers=merged)
        response = connection.getresponse()
        result = (response.status, response.read(), dict(response.getheaders()))
        connection.close()
        return result

    def test_http_run_download_and_saved_evidence(self):
        status, raw, _ = self.http("POST", "/api/runs", {"provider": "mock", "request": self.request}, {"X-Local-Token": self.token})
        self.assertEqual(status, 202)
        run_id = json.loads(raw)["id"]
        job = wait_finished(self.manager, run_id)
        self.assertEqual(job["result"]["status"], "completed")
        self.assertTrue(job["saved"])
        status, data, headers = self.http("GET", f"/api/runs/{run_id}/download/script.md")
        self.assertEqual(status, 200)
        self.assertIn("短视频脚本运行结果", data.decode())
        self.assertIn("attachment", headers["Content-Disposition"])
        self.assertTrue((Path(self.temp.name) / run_id / "trace.jsonl").exists())

    def test_missing_field_is_a_testable_business_result(self):
        del self.request["target_seconds"]
        run_id = self.manager.start({"provider": "mock", "request": self.request})
        self.assertEqual(wait_finished(self.manager, run_id)["result"]["status"], "needs_input")

    def test_fault_injection_returns_real_failure(self):
        run_id = self.manager.start({"provider": "mock", "request": self.request, "failures": {"search_materials": -1}})
        job = wait_finished(self.manager, run_id)
        self.assertEqual(job["result"]["status"], "blocked")
        self.assertIn("injected_tool_failure", json.dumps(job["trace"]))

    def test_no_csrf_token_and_foreign_origin_are_rejected(self):
        payload = {"provider": "mock", "request": self.request}
        self.assertEqual(self.http("POST", "/api/runs", payload)[0], 403)
        self.assertEqual(self.http("POST", "/api/runs", payload, {"X-Local-Token": self.token, "Origin": "https://example.invalid"})[0], 403)

    def test_invalid_input_and_faults_are_400(self):
        for body in [{"provider": "shell", "request": self.request}, {"request": {**self.request, "target_seconds": -1}}, {"request": self.request, "failures": {"delete": 1}}]:
            self.assertEqual(self.http("POST", "/api/runs", body, {"X-Local-Token": self.token})[0], 400)

    def test_host_and_path_are_not_arbitrary_file_access(self):
        self.assertEqual(self.http("GET", "/api/config", headers={"Host": "attacker.invalid"})[0], 403)
        self.assertEqual(self.http("GET", "/../.env")[0], 404)
        self.assertEqual(self.http("GET", "/api/runs/" + "0" * 32 + "/download/../../.env")[0], 404)

    def test_page_and_static_assets_have_correct_types(self):
        status, html, _ = self.http("GET", "/")
        self.assertEqual(status, 200)
        self.assertIn("脚本试验台", html.decode())
        status, _, headers = self.http("GET", "/app.js")
        self.assertEqual(status, 200)
        self.assertIn("javascript", headers["Content-Type"])

    def test_setup_error_is_visible_not_fake_completion(self):
        def unavailable(provider, timeout):
            raise ValueError("测试：模型未配置")
        self.manager.model_factory = unavailable
        run_id = self.manager.start({"provider": "api", "request": self.request})
        job = wait_finished(self.manager, run_id)
        self.assertEqual(job["state"], "error")
        self.assertFalse(job["saved"])
        self.assertIn("模型未配置", job["error"])

    def test_restart_restores_saved_runs_without_running_models(self):
        run_id = self.manager.start({"provider": "mock", "request": self.request})
        job = wait_finished(self.manager, run_id)
        def must_not_call(provider, timeout):
            raise AssertionError("restoring history must not run a model")
        restored = RunManager(self.temp.name, must_not_call)
        self.assertEqual(restored.get(run_id)["result"], job["result"])
        self.assertIsNone(restored.active_id)
        self.assertTrue(restored.get(run_id)["saved"])

    def test_only_one_active_run_and_cooperative_stop(self):
        entered, release = threading.Event(), threading.Event()
        class BlockingModel(MockModel):
            def decide(self, state, rules):
                entered.set()
                release.wait(2)
                return action("search_materials", "test", query="字幕"), {}
        self.manager.model_factory = lambda provider, timeout: BlockingModel()
        run_id = self.manager.start({"provider": "mock", "request": self.request})
        self.assertTrue(entered.wait(1))
        with self.assertRaises(BusyError):
            self.manager.start({"provider": "mock", "request": self.request})
        self.assertTrue(self.manager.cancel(run_id))
        release.set()
        self.assertEqual(wait_finished(self.manager, run_id)["result"]["status"], "cancelled")


if __name__ == "__main__":
    unittest.main()
