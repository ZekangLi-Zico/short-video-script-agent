"""Run unittest and save verifiable test evidence in examples/test-results/."""

import io
import json
import platform
import sys
import unittest
from datetime import datetime, timezone

from src.tools import ROOT


def main():
    stream = io.StringIO()
    started = datetime.now(timezone.utc).isoformat()
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    text = stream.getvalue()
    sys.stdout.write(text)
    directory = ROOT / "examples/test-results"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "unittest.txt").write_text(text, encoding="utf-8")
    report = {"started_at": started, "finished_at": datetime.now(timezone.utc).isoformat(),
              "python": platform.python_version(), "platform": platform.system(),
              "tests_run": result.testsRun, "failures": len(result.failures),
              "errors": len(result.errors), "skipped": len(result.skipped), "passed": result.wasSuccessful(),
              "scope": "Offline unit, integration and adapter-contract tests; not a real API benchmark."}
    (directory / "summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
