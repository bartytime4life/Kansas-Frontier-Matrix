import subprocess
import sys
import unittest
from typing import Sequence


def run_python(args: Sequence[str], timeout_seconds: float = 30.0) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
    )


def assert_python_ok(
    testcase: unittest.TestCase,
    args: Sequence[str],
    timeout_seconds: float = 30.0,
) -> None:
    try:
        result = run_python(args, timeout_seconds=timeout_seconds)
    except subprocess.TimeoutExpired as exc:
        testcase.fail(f"python subprocess timed out after {timeout_seconds}s for args={list(args)}: {exc}")
        return
    testcase.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
