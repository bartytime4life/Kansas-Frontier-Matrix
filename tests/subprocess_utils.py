import shlex
import subprocess
import sys
import unittest
from typing import Sequence


def format_python_args(args: Sequence[str]) -> str:
    return shlex.join([sys.executable, *args])


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
    cmd = format_python_args(args)
    try:
        result = run_python(args, timeout_seconds=timeout_seconds)
    except subprocess.TimeoutExpired as exc:
        testcase.fail(f"python subprocess timed out after {timeout_seconds}s for cmd={cmd}: {exc}")
        return

    if result.returncode != 0:
        testcase.fail(
            "python subprocess failed"
            f" (rc={result.returncode}, cmd={cmd}):\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
