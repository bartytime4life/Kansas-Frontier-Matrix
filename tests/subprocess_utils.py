import shlex
import subprocess
import sys
import unittest
from pathlib import Path
from typing import Sequence

PythonArgs = Sequence[str]


def build_python_cmd(args: PythonArgs) -> list[str]:
    """Build the Python command argv used by subprocess helpers."""
    return [sys.executable, *args]


def format_python_args(args: PythonArgs) -> str:
    """Render the python command used by subprocess helpers."""
    return shlex.join(build_python_cmd(args))


def run_python(
    args: PythonArgs,
    timeout_seconds: float = 30.0,
    cwd: str | Path | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run a Python subprocess with captured output and timeout."""
    return subprocess.run(
        build_python_cmd(args),
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
        cwd=cwd,
    )


def assert_python_ok(
    testcase: unittest.TestCase,
    args: PythonArgs,
    timeout_seconds: float = 30.0,
    cwd: str | Path | None = None,
) -> None:
    """Assert that a Python subprocess succeeds, otherwise fail with rich context."""
    cmd = format_python_args(args)
    try:
        result = run_python(args, timeout_seconds=timeout_seconds, cwd=cwd)
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
