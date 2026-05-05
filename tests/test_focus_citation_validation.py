import unittest

from tests.subprocess_utils import assert_python_ok


class FocusCitationValidationTests(unittest.TestCase):
    def test_validate_focus_citations(self):
        assert_python_ok(self, ["tools/validate_focus_citations.py"])


if __name__ == "__main__":
    unittest.main()
