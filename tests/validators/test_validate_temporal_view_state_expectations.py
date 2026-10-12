"""Exact temporal schema expectations shared with generic schema discovery."""

import json
from pathlib import Path
import tempfile
import unittest

from tools.validators.validate_temporal_view_state import Finding, _expected_matches


class TemporalSchemaExpectationTests(unittest.TestCase):
    def matches(self, text, findings):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.expected_error.txt"
            path.write_text(text, encoding="utf-8")
            return _expected_matches(path, findings)

    def test_structured_expectation_requires_exact_schema_field_and_keyword(self):
        expected = '{"kind":"schema","field":"/","keyword":"additionalProperties"}'
        self.assertTrue(self.matches(expected, [Finding("SCHEMA_INVALID", "/", "additionalProperties")]))
        for findings in (
            [],
            [Finding("SCHEMA_INVALID", "/selection", "additionalProperties")],
            [Finding("SCHEMA_INVALID", "/", "required")],
            [Finding("SCHEMA_INVALID", "/", "additionalproperties")],
            [Finding("OTHER", "/", "additionalProperties")],
        ):
            with self.subTest(findings=findings):
                self.assertFalse(self.matches(expected, findings))

    def test_malformed_or_unsupported_structured_expectations_fail_closed(self):
        findings = [Finding("SCHEMA_INVALID", "/", "additionalProperties")]
        valid = {"kind": "schema", "field": "/", "keyword": "additionalProperties"}
        invalid = [
            "", "{", "{}",
            '{"kind":"other","kind":"schema","field":"/","keyword":"additionalProperties"}',
            json.dumps({**valid, "contains": "private_token"}),
            json.dumps({**valid, "extra": True}),
            json.dumps({**valid, "kind": "semantic"}),
            json.dumps({**valid, "field": ""}),
            json.dumps({**valid, "field": 0}),
            json.dumps({**valid, "keyword": ""}),
            json.dumps({**valid, "keyword": []}),
        ]
        for text in invalid:
            with self.subTest(text=text):
                self.assertFalse(self.matches(text, findings))

    def test_existing_plaintext_expectations_still_require_every_line(self):
        findings = [Finding("SCHEMA_INVALID", "/display/mode", "enum")]
        self.assertTrue(self.matches("enum\n", findings))
        self.assertTrue(self.matches("schema_invalid\nenum\n", findings))
        self.assertFalse(self.matches("enum\nrequired\n", findings))
        self.assertFalse(self.matches("enum\n", []))


if __name__ == "__main__":
    unittest.main()
