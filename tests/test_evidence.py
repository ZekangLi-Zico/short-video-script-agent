import tempfile
import unittest
from pathlib import Path

from scripts.verify_evidence import verify_run
from src.agent import Agent
from src.mock import MockModel
from src.reporting import save_run
from src.tools import ToolBox, ROOT, read_json


class EvidenceTests(unittest.TestCase):
    def test_replay_accepts_real_tool_outputs_and_detects_tampering(self):
        scratch = ROOT / ".runtime/tests"
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as folder:
            self.assertTrue(Path(folder).resolve().is_relative_to(scratch.resolve()))
            tools = ToolBox()
            request = read_json(ROOT / "examples/inputs/normal.json")
            result = Agent(MockModel(), tools).run(request)
            save_run(folder, request, result, tools)
            self.assertEqual(verify_run(folder), [])
            result["trace"][2]["observation"]["total_seconds"] = 0
            save_run(folder, request, result, tools)
            self.assertTrue(verify_run(folder))


if __name__ == "__main__":
    unittest.main()
