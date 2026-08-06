#!/usr/bin/env python3
"""Tests for the fixture-only historical place-name resolver."""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_historical_place_resolution.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/domains/settlements-infrastructure/historical_place_resolution"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/settlements-infrastructure/historical_place_resolution.schema.json"

spec = importlib.util.spec_from_file_location("historical_place_validator", VALIDATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("validator module could not be loaded")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class HistoricalPlaceResolutionTests(unittest.TestCase):
    def load(self, relative: str) -> dict:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def codes(self, candidate: dict) -> set[str]:
        return {finding.code for finding in module.validate_candidate(candidate)}

    def refresh(self, candidate: dict) -> dict:
        candidate["derived"] = module.derive(candidate)
        candidate["governance"]["review_state"] = candidate["derived"]["disposition"]
        candidate["spec_hash"] = module.candidate_spec_hash(candidate)
        return candidate

    def test_schema_is_draft_2020_12_and_closed(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])
        self.assertIn("derived", schema["required"])
        self.assertIn("spec_hash", schema["required"])

    def test_valid_fixture_polarity(self) -> None:
        expected = {
            "variant_resolved.json": ("high", "candidate_review"),
            "post_office_resolved.json": ("high", "candidate_review"),
            "rail_stop_hold.json": ("medium", "hold_for_review"),
            "ambiguous_hold.json": ("medium", "hold_for_review"),
            "out_of_time_abstain.json": ("low", "abstain"),
        }
        for name, result in expected.items():
            with self.subTest(name=name):
                candidate = self.load(f"valid/{name}")
                self.assertEqual(module.validate_candidate(candidate), [])
                derived = candidate["derived"]
                self.assertEqual((derived["confidence"], derived["disposition"]), result)
                self.assertEqual(candidate["spec_hash"], module.candidate_spec_hash(candidate))

    def test_invalid_fixture_expected_codes(self) -> None:
        for path in sorted((FIXTURE_ROOT / "invalid").glob("*.json")):
            with self.subTest(path=path.name):
                candidate = json.loads(path.read_text(encoding="utf-8"))
                expected = path.with_suffix(".expected_error.txt").read_text(encoding="utf-8").strip()
                self.assertIn(expected, self.codes(candidate))

    def test_name_matching_normalizes_case_whitespace_and_diacritics(self) -> None:
        candidate = self.load("valid/variant_resolved.json")
        candidate["query"]["name"] = "  CÉDAR   JUNCTION  "
        self.refresh(candidate)
        self.assertEqual(module.validate_candidate(candidate), [])
        self.assertEqual(candidate["derived"]["confidence"], "high")

    def test_place_id_uses_only_canonical_name_ahcb_and_gnis(self) -> None:
        candidate = self.load("valid/variant_resolved.json")
        before = candidate["derived"]["place_id"]
        candidate["candidates"][0]["source_support"][2]["scan_ids"]["fixture_record"] = "changed"
        self.refresh(candidate)
        self.assertEqual(candidate["derived"]["place_id"], before)
        self.assertEqual(module.validate_candidate(candidate), [])

    def test_rail_stop_is_never_auto_resolved(self) -> None:
        candidate = self.load("valid/rail_stop_hold.json")
        self.assertEqual(module.candidate_rank(candidate["query"], candidate["candidates"][0]), 1)
        self.assertEqual(candidate["derived"]["reason_codes"], ["RAIL_STOP_REQUIRES_REVIEW"])

    def test_forbidden_precision_and_person_fields_fail_closed(self) -> None:
        candidate = self.load("valid/variant_resolved.json")
        candidate["candidates"][0]["coordinates"] = [-100.0, 38.0]
        candidate["candidates"][0]["living_person"] = True
        candidate["spec_hash"] = module.candidate_spec_hash(candidate)
        codes = self.codes(candidate)
        self.assertIn("FORBIDDEN_SENSITIVE_OR_PRECISE_FIELD", codes)

    def test_fixture_runner(self) -> None:
        self.assertEqual(module.run_fixtures(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
