import subprocess
import unittest


class DocsTruthLabelsTests(unittest.TestCase):
    def test_docs_truth_labels(self):
        self.assertEqual(subprocess.run(["python", "tools/validate_docs_truth_labels.py"]).returncode, 0)
