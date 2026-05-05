import unittest
from pathlib import Path

from tests.subprocess_utils import assert_python_ok
from tools.check_schema_home import collect_violations


class SchemaHomeTests(unittest.TestCase):
    def test_checker_passes_repository(self):
        assert_python_ok(self, ["tools/check_schema_home.py"])

    def test_pass_fixture_with_documented_exemption(self):
        root = Path("fixtures/policy/schema_home/pass")
        self.assertEqual(collect_violations(root), [])

    def test_fail_fixture_without_documented_exemption(self):
        root = Path("fixtures/policy/schema_home/fail")
        violations = collect_violations(root)
        self.assertTrue(any("schema outside canonical home" in v for v in violations))


if __name__ == "__main__":
    unittest.main()
