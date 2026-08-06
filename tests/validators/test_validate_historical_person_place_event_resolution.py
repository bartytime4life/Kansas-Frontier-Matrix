#!/usr/bin/env python3
"""Tests for the fixture-only historical person-place-event resolver."""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_historical_person_place_event_resolution.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution.schema.json"

spec = importlib.util.spec_from_file_location("historical_resolution_validator", VALIDATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("validator module could not be loaded")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class HistoricalResolutionTests(unittest.TestCase):
    def load(self, relative: str) -> dict:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def codes(self, candidate: dict) -> set[str]:
        return {finding.code for finding in module.validate_candidate(candidate)}

    def test_schema_is_draft_2020_12_and_closed(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])
        self.assertIn("spec_hash", schema["required"])
        self.assertIn("negative_evidence", schema["required"])

    def test_valid_fixture_polarity(self) -> None:
        expected = {
            "high_anchor.json": (7, "high", "candidate_review"),
            "conflict_hold.json": (4, "medium", "hold_for_review"),
            "weak_abstain.json": (0, "low", "abstain"),
        }
        for name, result in expected.items():
            with self.subTest(name=name):
                candidate = self.load(f"valid/{name}")
                self.assertEqual(module.validate_candidate(candidate), [])
                self.assertEqual((candidate["score"], candidate["confidence"], candidate["disposition"]), result)
                self.assertEqual(candidate["spec_hash"], module.candidate_spec_hash(candidate))

    def test_invalid_fixture_expected_codes(self) -> None:
        for path in sorted((FIXTURE_ROOT / "invalid").glob("*.json")):
            with self.subTest(path=path.name):
                candidate = json.loads(path.read_text(encoding="utf-8"))
                expected = path.with_suffix(".expected_error.txt").read_text(encoding="utf-8").strip()
                self.assertIn(expected, self.codes(candidate))

    def test_confidence_and_disposition_are_derived(self) -> None:
        candidate = self.load("valid/high_anchor.json")
        candidate["confidence"] = "medium"
        candidate["disposition"] = "hold_for_review"
        candidate["governance"]["review_state"] = "hold_for_review"
        candidate["spec_hash"] = module.candidate_spec_hash(candidate)
        codes = self.codes(candidate)
        self.assertIn("CONFIDENCE_MISMATCH", codes)
        self.assertIn("DISPOSITION_MISMATCH", codes)

    def test_snac_alone_is_corroborative_not_primary_score(self) -> None:
        candidate = self.load("valid/weak_abstain.json")
        self.assertEqual(module.authority_points(candidate), 0)
        self.assertEqual(candidate["person"]["primary_authority"], "local")

    def test_private_and_dna_fields_fail_closed(self) -> None:
        candidate = self.load("valid/high_anchor.json")
        candidate["person"]["raw_genotype"] = "denied"
        candidate["person"]["parcel_id"] = "denied"
        candidate["spec_hash"] = module.candidate_spec_hash(candidate)
        codes = self.codes(candidate)
        self.assertIn("RAW_DNA_FIELD_DENIED", codes)
        self.assertIn("PRIVATE_OR_PRECISE_FIELD_DENIED", codes)

    def test_fixture_runner(self) -> None:
        self.assertEqual(module.run_fixtures(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
