import subprocess
import sys
import unittest
from typing import Sequence


def run_python(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        check=False,
        capture_output=True,
        text=True,
    )


def assert_python_ok(testcase: unittest.TestCase, args: Sequence[str]) -> None:
    result = run_python(args)
    testcase.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
