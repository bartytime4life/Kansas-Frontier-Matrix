"""Deny-suite runner outcome mapping; never treats an empty suite as a pass."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch
import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "kfm_deny_test_runner", ROOT / "tools" / "qa" / "deny_test_runner.py")
assert SPEC and SPEC.loader
TOOL = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = TOOL
SPEC.loader.exec_module(TOOL)
SUITE = TOOL.Suite("synthetic", ("-c", "pass"), ("tools/qa/deny_test_runner.py",))


def _run(returncode: int, stdout: str, *, suite=SUITE, stderr="") -> dict[str, object]:
    completed = subprocess.CompletedProcess([], returncode, stdout, stderr)
    with patch.object(TOOL.subprocess, "run", return_value=completed):
        return TOOL.run_suite(suite, timeout=5)


def test_suite_ids_are_unique_and_paths_exist() -> None:
    ids = [suite.suite_id for suite in TOOL.SUITES]
    assert len(ids) == len(set(ids))
    for suite in TOOL.SUITES:
        assert all((ROOT / path).exists() for path in suite.required_paths), suite.suite_id
        assert suite.result_format in {"pytest", "unittest", "evidence-fixtures"}


def test_outcomes() -> None:
    assert _run(0, "7 passed in 0.1s")["status"] == "PASS"
    assert _run(1, "1 failed")["status"] == "FAIL"
    assert _run(0, "no tests ran in 0.01s")["status"] == "EMPTY"
    suite = TOOL.Suite("unit", (), (), result_format="unittest")
    assert _run(0, "Ran 0 tests in 0.000s\n\nOK", suite=suite)["status"] == "EMPTY"


@pytest.mark.parametrize("output", [
    "1 skipped in 0.01s",
    "3 deselected in 0.01s",
    "2 xfailed in 0.01s",
    "1 xpassed in 0.01s",
])
def test_no_passing_pytest_case_cannot_report_pass(output: str) -> None:
    assert _run(0, output)["status"] == "EMPTY"


@pytest.mark.parametrize("output", ["", "Everything looks fine", "1 passed\noutput suppressed"])
def test_zero_exit_without_runner_evidence_cannot_report_pass(output: str) -> None:
    assert _run(0, output)["status"] == "UNVERIFIED"


@pytest.mark.parametrize("output,passed", [
    ("3 passed, 2 skipped in 0.11s", 3),
    ("==== 1 passed, 1 warning in 60.01s (0:01:00) ====", 1),
    ("1 passed, 3 subtests passed in 0.01s", 1),
    ("1 passed, 2 xfailed, 1 deselected in 0.01s", 1),
])
def test_pytest_summary_counts_only_passing_cases(output: str, passed: int) -> None:
    result = _run(0, output)
    assert result["status"] == "PASS"
    assert result["passing_cases"] == passed


@pytest.mark.parametrize("output", [
    "0 passed, 1 failed in 0.1s", "1 passed, 1 error in 0.1s",
    "1 passed, 1 passed in 0.1s", "1 passed, unknown=1 in 0.1s",
])
def test_inconsistent_or_unknown_pytest_summary_is_unverified(output: str) -> None:
    assert _run(0, output)["status"] == "UNVERIFIED"


@pytest.mark.parametrize("total,annotation,passed", [
    (1, "skipped=1", 0), (2, "expected failures=2", 0),
    (2, "skipped=1, expected failures=1", 0),
    (3, "skipped=1, expected failures=1", 1), (2, "skipped=1", 1),
])
def test_unittest_excludes_skipped_and_expected_failures(total: int, annotation: str, passed: int) -> None:
    suite = TOOL.Suite("unit", (), (), result_format="unittest")
    result = _run(0, "", suite=suite, stderr=f"Ran {total} tests in 0.001s\n\nOK ({annotation})\n")
    assert result["status"] == ("PASS" if passed else "EMPTY")
    assert result["passing_cases"] == passed


@pytest.mark.parametrize("output", [
    "OK", "Ran 1 test in 0.01s\nOK (skipped=2)",
    "Ran 1 test in 0.01s\nOK (skipped=0, skipped=0)",
])
def test_unittest_requires_consistent_counted_summary(output: str) -> None:
    suite = TOOL.Suite("unit", (), (), result_format="unittest")
    assert _run(0, output, suite=suite)["status"] == "UNVERIFIED"


@pytest.mark.parametrize("output,status,passed", [
    ("SUMMARY DENIED=2 ERROR=7 RESOLVED=0 UNRESOLVED=10 FAILED=0", "PASS", 19),
    ("SUMMARY DENIED=0 ERROR=0 RESOLVED=0 UNRESOLVED=0 FAILED=0", "EMPTY", 0),
    ("SUMMARY DENIED=2 ERROR=7 RESOLVED=1 UNRESOLVED=10 FAILED=0", "UNVERIFIED", None),
    ("SUMMARY DENIED=2 ERROR=7 RESOLVED=0 UNRESOLVED=10 FAILED=1", "UNVERIFIED", None),
    ("PASS everything", "UNVERIFIED", None),
])
def test_negative_fixture_summary_requires_verified_negative_cases(output: str, status: str, passed: int | None) -> None:
    suite = TOOL.Suite("fixtures", (), (), result_format="evidence-fixtures")
    result = _run(0, output, suite=suite)
    assert result["status"] == status
    assert result["passing_cases"] == passed


@pytest.mark.parametrize("runner", ["pytest", "unittest"])
@pytest.mark.parametrize("with_pass", [False, True])
def test_real_runners_do_not_accept_all_skipped_suites(tmp_path: Path, monkeypatch, runner: str, with_pass: bool) -> None:
    if runner == "pytest":
        code = "import pytest\n@pytest.mark.skip(reason='synthetic skip')\ndef test_skip(): pass\n"
        if with_pass:
            code += "def test_pass(): assert 2 + 2 == 4\n"
        argv = ("-m", "pytest", "-q", "-p", "no:cacheprovider", "test_cases.py")
    else:
        code = "import unittest\nclass Cases(unittest.TestCase):\n @unittest.skip('synthetic skip')\n def test_skip(self): pass\n"
        if with_pass:
            code += " def test_pass(self): self.assertEqual(2 + 2, 4)\n"
        argv = ("-m", "unittest", "-v", "test_cases")
    (tmp_path / "test_cases.py").write_text(code)
    monkeypatch.setattr(TOOL, "ROOT", tmp_path)
    monkeypatch.delenv("PYTEST_ADDOPTS", raising=False)
    suite = TOOL.Suite("real-" + runner, argv, ("test_cases.py",), result_format=runner)
    result = TOOL.run_suite(suite, timeout=20)
    assert result["status"] == ("PASS" if with_pass else "EMPTY"), result
    assert result["passing_cases"] == int(with_pass)


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


@pytest.mark.parametrize("status", ["EMPTY", "UNVERIFIED", "FAIL", "MISSING", "TIMEOUT"])
def test_main_exit_code_follows_suite_status(capsys, status: str) -> None:
    with patch.object(TOOL, "run_suite", return_value={"suite": "s", "status": status}):
        assert TOOL.main([]) == 1
    with patch.object(TOOL, "run_suite", return_value={"suite": "s", "status": "PASS"}):
        assert TOOL.main([]) == 0
    capsys.readouterr()
