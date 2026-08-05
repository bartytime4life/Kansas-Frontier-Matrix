"""Deterministic tests for the inactive Soil support-type profile."""
from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools.validators.domains.soil.support_type.validate_support_type_profile import (
    FIXTURE_ROOT,
    PROFILE_PATH,
    Finding,
    validate_candidate,
    validate_file,
    validate_fixture_tree,
)


def _load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _digest(label: str) -> str:
    return "sha256:" + hashlib.sha256(label.encode("utf-8")).hexdigest()


class SoilSupportTypeProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profile = _load(PROFILE_PATH)
        cls.base_candidate = _load(
            FIXTURE_ROOT / "valid/station_soil_moisture.json"
        )

    def test_every_declared_support_type_accepts_a_minimal_candidate(self) -> None:
        rules = self.profile["support_types"]
        self.assertEqual(len(rules), 8)
        for index, rule in enumerate(rules):
            candidate = copy.deepcopy(self.base_candidate)
            candidate["candidate_id"] = (
                f"soil-support-candidate:generated-{index:04d}"
            )
            candidate["content_spec_hash"] = _digest(rule["support_type"])
            candidate["support_type"] = rule["support_type"]
            candidate["source_family"] = rule["source_families"][0]
            candidate["source_role"] = rule["source_roles"][0]
            candidate["spatial_support"] = rule["spatial_support"][0]
            candidate["claim_kind"] = rule["claim_kinds"][0]
            candidate["source_refs"] = [
                f"source:{candidate['source_family']}"
            ]
            candidate["evidence_refs"] = [
                f"evidence:synthetic-{index:04d}"
            ]
            with self.subTest(support_type=rule["support_type"]):
                result = validate_candidate(candidate, self.profile)
                self.assertTrue(result.ok, result.findings)
                self.assertEqual(result.outcome, "PASS")

    def test_fixture_tree_has_positive_and_negative_polarity(self) -> None:
        self.assertEqual(validate_fixture_tree(), ())

    def test_station_cannot_masquerade_as_satellite_grid(self) -> None:
        path = FIXTURE_ROOT / "invalid/station_as_satellite_grid.json"
        result = validate_file(path)
        codes = {finding.code for finding in result.findings}
        self.assertEqual(result.outcome, "DENY")
        self.assertIn("CLAIM_KIND_NOT_ALLOWED", codes)
        self.assertIn("FORBIDDEN_CLAIM_KIND", codes)

    def test_satellite_grid_cannot_masquerade_as_station(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        candidate["candidate_id"] = (
            "soil-support-candidate:generated-satellite-collapse"
        )
        candidate["support_type"] = "satellite_soil_moisture_grid"
        candidate["source_family"] = "nasa_smap"
        candidate["source_role"] = "satellite_grid_measurement"
        candidate["spatial_support"] = "satellite_grid_cell"
        candidate["claim_kind"] = "current_station_condition"
        result = validate_candidate(candidate, self.profile)
        codes = {finding.code for finding in result.findings}
        self.assertIn("CLAIM_KIND_NOT_ALLOWED", codes)
        self.assertIn("FORBIDDEN_CLAIM_KIND", codes)

    def test_profile_digest_binding_is_required(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        candidate["profile_spec_hash"] = _digest("wrong-profile")
        result = validate_candidate(candidate, self.profile)
        self.assertIn(
            Finding("PROFILE_HASH_BINDING_MISMATCH", "/profile_spec_hash"),
            result.findings,
        )

    def test_public_use_request_fails_closed(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        candidate["public_use_requested"] = True
        result = validate_candidate(candidate, self.profile)
        codes = {finding.code for finding in result.findings}
        self.assertIn("CANDIDATE_SCHEMA_INVALID", codes)
        self.assertIn("PUBLIC_USE_DENIED", codes)

    def test_reference_order_is_deterministic(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        candidate["source_refs"] = ["source:z", "source:a"]
        result = validate_candidate(candidate, self.profile)
        self.assertIn(
            Finding("REFS_NOT_CANONICAL", "/source_refs"),
            result.findings,
        )

    def test_input_is_not_mutated(self) -> None:
        candidate = copy.deepcopy(self.base_candidate)
        snapshot = copy.deepcopy(candidate)
        result = validate_candidate(candidate, self.profile)
        self.assertTrue(result.ok)
        self.assertEqual(candidate, snapshot)

    def test_duplicate_json_keys_are_rejected_safely(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"SoilSupportTypeCandidate",'
                '"object_type":"duplicate"}',
                encoding="utf-8",
            )
            result = validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn(Finding("JSON_DUPLICATE_KEY", "/"), result.findings)

    def test_findings_are_sorted_and_repeatable(self) -> None:
        path = FIXTURE_ROOT / "invalid/station_as_satellite_grid.json"
        first = validate_file(path)
        second = validate_file(path)
        self.assertEqual(first, second)
        self.assertEqual(first.findings, tuple(sorted(first.findings)))


if __name__ == "__main__":
    unittest.main()
