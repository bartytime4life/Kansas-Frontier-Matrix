import unittest

from tests.subprocess_utils import assert_python_ok, run_python


class FixtureValidationTests(unittest.TestCase):
    def test_validate_fixtures(self):
        assert_python_ok(self, ["tools/validate_fixtures.py"])

    def test_invalid_answer_fixture_is_missing_citations(self):
        result = run_python(
            [
                "-c",
                "import json;from pathlib import Path;o=json.loads(Path('fixtures/invalid/focus_answer_without_citation.json').read_text());print('ok' if o.get('outcome')=='ANSWER' and 'citations' not in o else 'bad')",
            ]
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        self.assertIn("ok", result.stdout)
