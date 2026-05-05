import tempfile
import unittest
from pathlib import Path

from tests.subprocess_utils import assert_python_ok
from tools.check_directory_rules import collect_violations


class DirectoryRulesTests(unittest.TestCase):
    def test_check_directory_rules(self):
        assert_python_ok(self, ["tools/check_directory_rules.py"])

    def test_documented_transitional_root_is_allowed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "ui").mkdir()
            (root / "ui" / "README.md").write_text("status: legacy transitional root")
            self.assertEqual(collect_violations(root), [])

    def test_undocumented_transitional_root_is_forbidden(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "web").mkdir()
            violations = collect_violations(root)
            self.assertTrue(any("transitional root missing documented status" in v for v in violations))

    def test_domain_root_is_forbidden(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "hydrology").mkdir()
            violations = collect_violations(root)
            self.assertIn("forbidden domain root directory: hydrology/", violations)


if __name__ == "__main__":
    unittest.main()
