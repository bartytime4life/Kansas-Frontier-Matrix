"""Deny-suite runner outcome mapping; never treats an empty suite as a pass."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "kfm_deny_test_runner", ROOT / "tools" / "qa" / "deny_test_runner.py")
assert SPEC and SPEC.loader
TOOL = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = TOOL
SPEC.loader.exec_module(TOOL)
SUITE = TOOL.Suite("synthetic", ("-c", "pass"), ("tools/qa/deny_test_runner.py",))


def _run(returncode: int, stdout: str) -> dict[str, object]:
    completed = subprocess.CompletedProcess([], returncode, stdout, "")
    with patch.object(TOOL.subprocess, "run", return_value=completed):
        return TOOL.run_suite(SUITE, timeout=5)


def test_suite_ids_are_unique_and_paths_exist() -> None:
    ids = [suite.suite_id for suite in TOOL.SUITES]
    assert len(ids) == len(set(ids))
    for suite in TOOL.SUITES:
        assert all((ROOT / path).exists() for path in suite.required_paths), suite.suite_id


def test_outcomes() -> None:
    assert _run(0, "7 passed in 0.1s")["status"] == "PASS"
    assert _run(1, "1 failed")["status"] == "FAIL"
    assert _run(0, "no tests ran in 0.01s")["status"] == "EMPTY"
    assert _run(0, "Ran 0 tests in 0.000s\n\nOK")["status"] == "EMPTY"


def test_missing_paths_fail_before_execution() -> None:
    suite = TOOL.Suite("gone", ("-c", "pass"), ("tests/does/not/exist.py",))
    with patch.object(TOOL.subprocess, "run") as run:
        result = TOOL.run_suite(suite, timeout=5)
    run.assert_not_called()
    assert result == {"suite": "gone", "status": "MISSING",
                      "missing_paths": ["tests/does/not/exist.py"]}


def test_timeout() -> None:
    with patch.object(TOOL.subprocess, "run",
                      side_effect=subprocess.TimeoutExpired("x", 5)):
        assert TOOL.run_suite(SUITE, timeout=5)["status"] == "TIMEOUT"


def test_main_exit_code_follows_suite_status(capsys) -> None:
    with patch.object(TOOL, "run_suite", return_value={"suite": "s", "status": "EMPTY"}):
        assert TOOL.main([]) == 1
    with patch.object(TOOL, "run_suite", return_value={"suite": "s", "status": "PASS"}):
        assert TOOL.main([]) == 0
    capsys.readouterr()
