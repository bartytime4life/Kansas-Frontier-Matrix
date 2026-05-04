import shlex
import subprocess
import sys
import tempfile
import unittest

from tests.subprocess_utils import assert_python_ok, build_python_cmd, format_python_args, run_python


class SubprocessUtilsTests(unittest.TestCase):
    def test_build_python_cmd_prefixes_interpreter(self):
        cmd = build_python_cmd(["-c", "print('ok')"])
        self.assertEqual(cmd[0], sys.executable)
        self.assertEqual(cmd[1:], ["-c", "print('ok')"])

    def test_build_python_cmd_without_args(self):
        self.assertEqual(build_python_cmd([]), [sys.executable])

    def test_format_python_args_includes_interpreter(self):
        rendered = format_python_args(["-c", "print('ok')"])
        self.assertTrue(rendered.startswith(sys.executable))
        self.assertIn("-c", rendered)
        self.assertIn("print", rendered)

    def test_format_python_args_matches_built_command(self):
        args = ["-c", "print('ok')"]
        self.assertEqual(shlex.split(format_python_args(args)), build_python_cmd(args))

    def test_format_python_args_without_extra_args(self):
        rendered = format_python_args([])
        self.assertEqual(shlex.split(rendered), [sys.executable])

    def test_format_python_args_round_trips_with_shlex_split(self):
        args = ["-c", "print('hello world')"]
        rendered = format_python_args(args)
        self.assertEqual(shlex.split(rendered)[1:], args)

    def test_format_python_args_handles_spaces(self):
        rendered = format_python_args(["-c", "print('hello world')"])
        self.assertIn("hello world", rendered)
        self.assertIn("'", rendered)

    def test_run_python_success(self):
        result = run_python(["-c", "print('ok')"])
        self.assertEqual(result.returncode, 0)
        self.assertIn("ok", result.stdout)

    def test_run_python_honors_cwd(self):
        with tempfile.TemporaryDirectory() as td:
            result = run_python(["-c", "import os; print(os.getcwd())"], cwd=td)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), td)

    def test_run_python_timeout_raises(self):
        with self.assertRaises(subprocess.TimeoutExpired):
            run_python(["-c", "import time; time.sleep(0.2)"], timeout_seconds=0.01)

    def test_assert_python_ok_success(self):
        assert_python_ok(self, ["-c", "print('ok')"])

    def test_assert_python_ok_honors_cwd(self):
        with tempfile.TemporaryDirectory() as td:
            assert_python_ok(self, ["-c", "import os; print(os.getcwd())"], cwd=td)

    def test_assert_python_ok_timeout_surfaces_assertion(self):
        with self.assertRaises(AssertionError):
            assert_python_ok(self, ["-c", "import time; time.sleep(0.2)"], timeout_seconds=0.01)

    def test_assert_python_ok_timeout_message_includes_context(self):
        with self.assertRaises(AssertionError) as ctx:
            assert_python_ok(self, ["-c", "import time; time.sleep(0.2)"], timeout_seconds=0.01)
        msg = str(ctx.exception)
        self.assertIn("timed out", msg)
        self.assertIn("0.01s", msg)
        self.assertIn("cmd=", msg)

    def test_assert_python_ok_timeout_message_includes_interpreter_path(self):
        with self.assertRaises(AssertionError) as ctx:
            assert_python_ok(self, ["-c", "import time; time.sleep(0.2)"], timeout_seconds=0.01)
        self.assertIn(sys.executable, str(ctx.exception))

    def test_assert_python_ok_nonzero_exit_surfaces_assertion(self):
        with self.assertRaises(AssertionError):
            assert_python_ok(self, ["-c", "import sys; print('boom'); sys.exit(3)"])

    def test_assert_python_ok_nonzero_message_includes_context(self):
        with self.assertRaises(AssertionError) as ctx:
            assert_python_ok(self, ["-c", "import sys; print('boom'); sys.exit(3)"])
        msg = str(ctx.exception)
        self.assertIn("rc=3", msg)
        self.assertIn("boom", msg)
        self.assertIn("cmd=", msg)
        self.assertIn("stdout:", msg)
        self.assertIn("stderr:", msg)
