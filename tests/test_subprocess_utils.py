import unittest

from tests.subprocess_utils import assert_python_ok, run_python


class SubprocessUtilsTests(unittest.TestCase):
    def test_run_python_success(self):
        result = run_python(["-c", "print('ok')"])
        self.assertEqual(result.returncode, 0)
        self.assertIn("ok", result.stdout)

    def test_assert_python_ok_success(self):
        assert_python_ok(self, ["-c", "print('ok')"])

    def test_assert_python_ok_timeout_surfaces_assertion(self):
        with self.assertRaises(AssertionError):
            assert_python_ok(self, ["-c", "import time; time.sleep(0.2)"], timeout_seconds=0.01)
