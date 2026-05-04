import subprocess
import sys
import unittest


class DocsTruthLabelsTests(unittest.TestCase):
    def test_docs_truth_labels(self):
        self.assertEqual(subprocess.run([sys.executable, "tools/validate_docs_truth_labels.py"]).returncode, 0)
