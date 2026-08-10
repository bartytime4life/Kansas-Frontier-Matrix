from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.source import validate_source_activation_portfolio_assessment as validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/source/source_activation_portfolio_assessment.schema.json"
VALIDATOR_PATH = ROOT / "tools/validators/source/validate_source_activation_portfolio_assessment.py"
SOURCE_MAP_PATH = ROOT / "docs/intake/exploratory/source-activation-portfolio-assessment-source-map.md"


class SourceActivationPortfolioAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_exact_fixture_suite(self) -> None:
        self.assertEqual(0, validator.run_fixtures())

    def test_fixture_outcomes_cover_finite_states(self) -> None:
        statuses: set[str] = set()
        portfolio_states: set[str] = set()
        for case in self.manifest["cases"]:
            result = validator.validate_payload(validator.materialize_case(self.manifest, case))
            statuses.add(result.outcome)
            if result.portfolio_outcome is not None:
                portfolio_states.add(result.portfolio_outcome)
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, statuses)
        self.assertEqual({"READY_FOR_REVIEW", "CONDITIONAL", "HOLD", "ERROR"}, portfolio_states)

    def test_identity_is_deterministic_and_sensitive(self) -> None:
        case = self.manifest["cases"][0]
        first = validator.materialize_case(self.manifest, case)
        second = validator.materialize_case(self.manifest, case)
        self.assertEqual(first["portfolio_id"], second["portfolio_id"])
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        changed = copy.deepcopy(first)
        changed["evaluated_at"] = "2026-08-10T06:00:00Z"
        digest, identifier = validator.canonical_identity(changed)
        self.assertNotEqual(first["spec_hash"], digest)
        self.assertNotEqual(first["portfolio_id"], identifier)

    def test_parser_rejects_duplicate_keys_and_nonfinite_numbers(self) -> None:
        samples = [
            ('{"a":1,"a":2}', "SOURCE_PORTFOLIO_JSON_DUPLICATE_KEY"),
            ('{"a":NaN}', "SOURCE_PORTFOLIO_JSON_NONFINITE_NUMBER"),
        ]
        with tempfile.TemporaryDirectory() as directory:
            for index, (content, expected_code) in enumerate(samples):
                with self.subTest(expected_code=expected_code):
                    path = Path(directory) / f"sample-{index}.json"
                    path.write_text(content, encoding="utf-8")
                    value, findings = validator._read(path)
                    self.assertIsNone(value)
                    self.assertEqual(expected_code, findings[0].code)

    def test_parser_rejects_symlink_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            value, findings = validator._read(link)
            self.assertIsNone(value)
            self.assertEqual("SOURCE_PORTFOLIO_INPUT_SYMLINK_DENIED", findings[0].code)

    def test_hold_cannot_be_overridden_by_ready_candidate(self) -> None:
        payload = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        result = validator.validate_payload(payload)
        self.assertEqual("ABSTAIN", result.outcome)
        self.assertEqual("HOLD", result.portfolio_outcome)
        self.assertEqual(["kfm:fixture:source:beta-denied"], payload["portfolio_decision"]["held_source_ids"])

    def test_every_authority_effect_is_false(self) -> None:
        for case in self.manifest["cases"][:4]:
            payload = validator.materialize_case(self.manifest, case)
            self.assertTrue(all(value is False for value in payload["permissions"].values()))
            for candidate in payload["candidates"]:
                self.assertTrue(all(value is False for value in candidate["governance"].values()))

    def test_fixtures_are_synthetic_and_contain_no_network_locator(self) -> None:
        text = json.dumps(self.manifest["base"], sort_keys=True)
        self.assertNotIn("http://", text)
        self.assertNotIn("https://", text)
        for candidate in self.manifest["base"]["candidates"]:
            self.assertTrue(candidate["source_id"].startswith("kfm:fixture:source:"))

    def test_validator_has_no_network_or_process_client_import(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        for forbidden in ("import requests", "import urllib", "import socket", "subprocess", "httpx", "aiohttp"):
            self.assertNotIn(forbidden, source)

    def test_source_map_preserves_traceability_and_boundaries(self) -> None:
        source = SOURCE_MAP_PATH.read_text(encoding="utf-8")
        for marker in (
            "Comprehensive Research and Verification Report",
            "SourceActivationDecision",
            "VerificationConvergencePlan",
            "No source is contacted",
        ):
            self.assertIn(marker, source)

    def test_serialized_result_declares_non_effects(self) -> None:
        result = validator.validate_payload(validator.materialize_case(self.manifest, self.manifest["cases"][0]))
        serialized = json.loads(validator.serialize(None, result))
        self.assertEqual("NONE", serialized["authority"])
        self.assertIn("no_activation", serialized["non_effects"])
        self.assertIn("no_review_scheduling", serialized["non_effects"])
        self.assertIn("no_publication", serialized["non_effects"])


if __name__ == "__main__":
    unittest.main()
