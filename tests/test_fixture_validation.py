import subprocess
import sys
import unittest


class FixtureValidationTests(unittest.TestCase):
    def test_validate_fixtures(self):
        self.assertEqual(subprocess.run([sys.executable, "tools/validate_fixtures.py"]).returncode, 0)

    def test_invalid_answer_fixture_is_missing_citations(self):
        result = subprocess.run([sys.executable, "-c", "import json;from pathlib import Path;o=json.loads(Path('fixtures/invalid/focus_answer_without_citation.json').read_text());print('ok' if o.get('outcome')=='ANSWER' and 'citations' not in o else 'bad')"], capture_output=True, text=True)
        self.assertIn("ok", result.stdout)
