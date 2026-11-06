import io
import json
import os
import subprocess
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import Mock, patch

from src.agent import ModelError
from src.mock import action
from src.providers import APIModel, CodexModel, parse_action, run_cli
from src.tools import ToolBox
from src.requirements import REVIEW_SCHEMA


STATE = {"request": {"topic": "字幕"}, "script": None, "retrieved": {}, "duration": None,
         "rules_check": None, "history": [], "max_steps": 12}
ACTION = action("search_materials", "需要来源证据", query="字幕")


class FakeOpener:
    def __init__(self, response):
        self.response, self.requests = response, []

    def open(self, request, timeout):
        self.requests.append(request)
        return io.BytesIO(json.dumps(self.response).encode("utf-8"))


class ProviderTests(unittest.TestCase):
    def test_review_uses_separate_schema_and_original_request_without_writer_history(self):
        report = {'items': [], 'summary': 'contract fixture'}
        opener = FakeOpener({'output': [{'type': 'message', 'content': [{'type': 'output_text', 'text': json.dumps(report)}]}]})
        with patch.dict(os.environ, {'MODEL_API_KEY': 'test-only', 'MODEL_NAME': 'test-model', 'MODEL_API_STYLE': 'responses'}, clear=True):
            with patch('urllib.request.build_opener', return_value=opener):
                actual, _ = APIModel().review({'topic': '校园采访'}, {'title': '当前稿', 'shots': []}, {'ok': True, 'citations': []})
        self.assertEqual(actual, report)
        body = json.loads(opener.requests[0].data)
        self.assertEqual(body['text']['format']['schema'], REVIEW_SCHEMA)
        payload = json.loads(body['input'][1]['content'])
        self.assertEqual(set(payload), {'request', 'script', 'listening_copy', 'rules_check', 'duration_check'})
        self.assertEqual(payload['request']['topic'], '校园采访')
        self.assertEqual(payload['rules_check'], {'ok': True, 'citations': []})

    def test_responses_adapter_sends_observation_and_schema(self):
        response = {"id": "test-response", "model": "test-model", "output": [
            {"type": "reasoning", "summary": []},
            {"type": "message", "content": [{"type": "output_text", "text": json.dumps(ACTION)}]}]}
        opener = FakeOpener(response)
        with patch.dict(os.environ, {"MODEL_API_KEY": "test-only", "MODEL_NAME": "test-model", "MODEL_API_STYLE": "responses"}, clear=True):
            with patch("urllib.request.build_opener", return_value=opener):
                result, meta = APIModel().decide(STATE, ToolBox().rules)
        self.assertEqual(result, ACTION)
        body = json.loads(opener.requests[0].data)
        self.assertTrue(body["text"]["format"]["strict"])
        self.assertIn("remaining_steps", body["input"][1]["content"])
        self.assertNotIn("test-only", json.dumps(meta))

    def test_chat_compatible_adapter(self):
        opener = FakeOpener({"choices": [{"message": {"content": json.dumps(ACTION)}}]})
        with patch.dict(os.environ, {"MODEL_API_KEY": "test-only", "MODEL_NAME": "test-model", "MODEL_API_STYLE": "chat"}, clear=True):
            with patch("urllib.request.build_opener", return_value=opener):
                result, _ = APIModel().decide(STATE, ToolBox().rules)
        self.assertEqual(result, ACTION)
        self.assertTrue(opener.requests[0].full_url.endswith("/chat/completions"))

    def test_http_error_does_not_echo_provider_body_or_key(self):
        with patch.dict(os.environ, {"MODEL_API_KEY": "test-secret", "MODEL_NAME": "test-model"}, clear=True):
            opener = Mock()
            opener.open.side_effect = urllib.error.HTTPError("https://example.invalid", 401, "test-secret", {}, None)
            with patch("urllib.request.build_opener", return_value=opener):
                with self.assertRaisesRegex(ModelError, "^api_http_401$"):
                    APIModel().decide(STATE, ToolBox().rules)

    def test_bad_api_configuration_is_rejected(self):
        for url in ["http://remote.example/v1", "https://user:password@example.invalid", "https://example.invalid?key=x"]:
            with self.subTest(url=url), patch.dict(os.environ, {"MODEL_API_KEY": "test", "MODEL_NAME": "test", "MODEL_BASE_URL": url}, clear=True):
                with self.assertRaises(ValueError):
                    APIModel()

    def test_missing_credentials_have_no_fallback(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError):
                APIModel()

    def test_codex_adapter_uses_json_and_keeps_reasoning_out_of_metadata(self):
        def fake_run(command, **kwargs):
            output = Path(command[command.index("--output-last-message") + 1])
            output.write_text(json.dumps(ACTION), encoding="utf-8")
            self.assertIn("--ephemeral", command)
            self.assertIn("read-only", command)
            self.assertNotIn("shell", kwargs)
            self.assertIn("STATE_JSON", kwargs["input"])
            return subprocess.CompletedProcess(command, 0, stdout='{"type":"turn.completed","usage":{"input_tokens":123}}\n', stderr="")
        with patch.dict(os.environ, {"CODEX_BIN": "test-codex.exe"}):
            with patch("src.providers.run_cli", side_effect=fake_run):
                result, meta = CodexModel().decide(STATE, ToolBox().rules)
        self.assertEqual(result, ACTION)
        self.assertEqual(meta["usage"]["input_tokens"], 123)

    def test_codex_unexpected_tools_are_rejected(self):
        def fake_run(command, **kwargs):
            Path(command[command.index("--output-last-message") + 1]).write_text(json.dumps(ACTION), encoding="utf-8")
            return subprocess.CompletedProcess(command, 0, stdout='{"type":"item.completed","item":{"type":"command_execution"}}\n', stderr="")
        with patch.dict(os.environ, {"CODEX_BIN": "test-codex.exe"}):
            with patch("src.providers.run_cli", side_effect=fake_run):
                with self.assertRaisesRegex(ModelError, "codex_unexpected_external_tool_use"):
                    CodexModel().decide(STATE, ToolBox().rules)

    def test_codex_timeout_is_explicit(self):
        with patch.dict(os.environ, {"CODEX_BIN": "test-codex.exe"}):
            with patch("src.providers.run_cli", side_effect=subprocess.TimeoutExpired("codex", 1)):
                with self.assertRaisesRegex(ModelError, "codex_timeout"):
                    CodexModel().decide(STATE, ToolBox().rules)

    def test_json_markdown_or_text_is_not_silently_accepted(self):
        for text in ["```json\n{}\n```", "I completed the task"]:
            with self.assertRaises(ModelError):
                parse_action(text)

    def test_timeout_terminates_only_the_created_process_tree(self):
        process = Mock()
        process.pid = 123456789
        process.communicate.side_effect = [subprocess.TimeoutExpired("test", 1), ("", "")]
        with patch("subprocess.Popen", return_value=process), patch("subprocess.run") as terminate:
            if os.name == "nt":
                with self.assertRaises(subprocess.TimeoutExpired):
                    run_cli(["test"], input="", timeout=1, cwd=".")
                self.assertEqual(terminate.call_args.args[0], ["taskkill", "/PID", "123456789", "/T", "/F"])
            else:
                with patch("os.killpg") as kill:
                    with self.assertRaises(subprocess.TimeoutExpired):
                        run_cli(["test"], input="", timeout=1, cwd=".")
                    self.assertEqual(kill.call_args.args[0], 123456789)


if __name__ == "__main__":
    unittest.main()
