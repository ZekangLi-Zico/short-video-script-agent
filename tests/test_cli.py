import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.cli import main
from src.tools import ROOT, read_json


class CLITests(unittest.TestCase):
    def test_success_exit_and_actual_files(self):
        scratch = ROOT / ".runtime/tests"
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as folder, contextlib.redirect_stdout(io.StringIO()) as stdout:
            self.assertTrue(Path(folder).resolve().is_relative_to(scratch.resolve()))
            code = main(["--provider", "mock", "--input", str(ROOT / "examples/inputs/normal.json"), "--output", folder])
            self.assertEqual(code, 0)
            self.assertEqual(read_json(Path(folder) / "output.json")["status"], "completed")
            self.assertIn("offline_mock_not_model_evidence", stdout.getvalue())

    def test_save_failure_never_prints_success(self):
        with patch("src.cli.save_run", side_effect=OSError("test-disk-full")):
            with contextlib.redirect_stdout(io.StringIO()) as stdout, contextlib.redirect_stderr(io.StringIO()) as stderr:
                code = main(["--provider", "mock", "--input", str(ROOT / "examples/inputs/normal.json")])
        self.assertEqual(code, 2)
        self.assertNotIn("completed", stdout.getvalue())
        self.assertIn("test-disk-full", stderr.getvalue())

    def test_step_limit_cli_exit_is_nonzero(self):
        scratch = ROOT / ".runtime/tests"
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as folder, contextlib.redirect_stdout(io.StringIO()):
            self.assertTrue(Path(folder).resolve().is_relative_to(scratch.resolve()))
            code = main(["--provider", "mock", "--input", str(ROOT / "examples/inputs/normal.json"),
                         "--output", folder, "--max-steps", "1"])
            self.assertEqual(code, 2)
            self.assertEqual(read_json(Path(folder) / "output.json")["status"], "step_limit")


if __name__ == "__main__":
    unittest.main()
