import unittest

from tests.subprocess_utils import assert_python_ok


class DocsTruthLabelsTests(unittest.TestCase):
    def test_validate_docs_truth_labels(self):
        assert_python_ok(self, ["tools/validate_docs_truth_labels.py"])
