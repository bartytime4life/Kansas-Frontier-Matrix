"""No-network proof of the finite RuntimeResponseEnvelope shape boundary.

These tests prove schema, compatibility alias, fixture polarity, and bounded
precision-disclosure semantics only. They do not resolve evidence, evaluate
policy, authorize an answer, or establish release/publication state.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
import unittest

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CANONICAL_SCHEMA_PATH = REPOSITORY_ROOT / "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"
FOCUS_ALIAS_PATH = REPOSITORY_ROOT / "schemas/contracts/v1/focus/runtime_response_envelope.schema.json"
FIXTURE_ROOT = REPOSITORY_ROOT / "fixtures/contracts/v1/runtime/runtime_response_envelope"
VALIDATOR_PATH = REPOSITORY_ROOT / "tools/validators/validate_runtime_response_envelope.py"
EXPECTED_OUTCOMES = ("ANSWER", "ABSTAIN", "DENY", "ERROR")

SPEC = importlib.util.spec_from_file_location("runtime_response_validator_proof", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
runtime_validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = runtime_validator
SPEC.loader.exec_module(runtime_validator)


def _load_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected a JSON object: {path}")
    return value


class FiniteRuntimeEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = _load_json(CANONICAL_SCHEMA_PATH)
        cls.focus_alias = _load_json(FOCUS_ALIAS_PATH)
        cls.validator = runtime_validator._validator()

    def test_canonical_schema_is_closed_to_four_outcomes(self) -> None:
        self.assertEqual(self.schema["properties"]["outcome"]["enum"], list(EXPECTED_OUTCOMES))
        self.assertIs(self.schema["additionalProperties"], False)
        self.assertEqual(len(self.schema["required"]), 10)
        self.assertIn("precision_actually_used", self.schema["properties"])
        self.assertTrue(self.schema["allOf"])

    def test_focus_path_is_a_compatibility_alias_not_a_second_shape(self) -> None:
        self.assertEqual(self.focus_alias["$ref"], self.schema["$id"])
        self.assertEqual(
            self.focus_alias["x-kfm"]["canonical_schema"],
            CANONICAL_SCHEMA_PATH.relative_to(REPOSITORY_ROOT).as_posix(),
        )
        self.assertEqual(self.focus_alias["x-kfm"]["role"], "compatibility-alias")
        self.assertNotIn("properties", self.focus_alias)

    def test_valid_fixtures_cover_outcomes_and_disclose_answer_precision(self) -> None:
        paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        fixtures = [_load_json(path) for path in paths]
        self.assertEqual({item["outcome"] for item in fixtures}, set(EXPECTED_OUTCOMES))
        self.assertEqual(len({item["id"] for item in fixtures}), len(fixtures))
        for path, value in zip(paths, fixtures):
            self.assertEqual(runtime_validator.validate_path(path, self.validator), [], path)
            if value["outcome"] == "ANSWER":
                self.assertIn("precision_actually_used", value)
                self.assertTrue(value["evidence_refs"])
            else:
                self.assertNotIn("precision_actually_used", value)

    def test_existing_invalid_fixtures_remain_rejected(self) -> None:
        paths = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
        findings = {path.name: runtime_validator.validate_path(path, self.validator) for path in paths}
        self.assertTrue(all(value for value in findings.values()), findings)
        self.assertEqual(set(findings), {"invalid_1.json", "invalid_2.json", "invalid_3.json", "invalid_4.json"})


if __name__ == "__main__":
    unittest.main()
