"""Deterministic tests for the fixture-only MukeyProperties profile."""
from __future__ import annotations

import copy
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.domains.soil.mukey_properties.validate_mukey_properties import (
    FIXTURE_ROOT,
    Finding,
    compute_content_spec_hash,
    validate_candidate,
    validate_file,
    validate_fixture_tree,
)


def _load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _restamp(candidate: dict[str, object]) -> None:
    candidate["content_spec_hash"] = compute_content_spec_hash(candidate)


class MukeyPropertiesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.single = _load(FIXTURE_ROOT / "valid/single_component.json")
        cls.multi = _load(FIXTURE_ROOT / "valid/multi_component.json")

    def test_fixture_matrix_has_exact_polarity(self) -> None:
        self.assertEqual(validate_fixture_tree(), ())

    def test_valid_metrics_are_recomputed(self) -> None:
        self.assertTrue(validate_candidate(copy.deepcopy(self.single)).ok)
        self.assertTrue(validate_candidate(copy.deepcopy(self.multi)).ok)
        derived = self.multi["derived"]
        self.assertAlmostEqual(34.6, derived["root_zone_clay_pct"], places=6)
        self.assertAlmostEqual(3.82, derived["root_zone_ksat_um_s"], places=6)
        self.assertAlmostEqual(
            0.156,
            derived["root_zone_available_water_capacity_fraction"],
            places=6,
        )
        self.assertAlmostEqual(3.2, derived["surface_organic_matter_pct"], places=6)

    def test_component_closure_fails_closed(self) -> None:
        result = validate_file(FIXTURE_ROOT / "invalid/component_closure.json")
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(Finding("COMPONENT_PERCENT_CLOSURE", "/components"), result.findings)

    def test_horizon_gap_and_overlap_are_distinct(self) -> None:
        gap_candidate = copy.deepcopy(self.single)
        gap_candidate["components"][0]["horizons"][0]["bottom_cm"] = 40
        _restamp(gap_candidate)
        gap = validate_candidate(gap_candidate)

        overlap_candidate = copy.deepcopy(self.single)
        overlap_candidate["components"][0]["horizons"][0]["bottom_cm"] = 60
        _restamp(overlap_candidate)
        overlap = validate_candidate(overlap_candidate)

        self.assertIn("HORIZON_GAP", {finding.code for finding in gap.findings})
        self.assertIn("HORIZON_OVERLAP", {finding.code for finding in overlap.findings})

    def test_declared_metric_must_match_recomputation(self) -> None:
        candidate = copy.deepcopy(self.single)
        candidate["derived"]["root_zone_clay_pct"] = 26.0
        _restamp(candidate)
        result = validate_candidate(candidate)
        self.assertIn("DERIVED_METRIC_MISMATCH", {finding.code for finding in result.findings})

    def test_content_hash_is_exact_and_non_self_referential(self) -> None:
        candidate = copy.deepcopy(self.single)
        self.assertEqual(candidate["content_spec_hash"], compute_content_spec_hash(candidate))
        candidate["derived"]["root_zone_clay_pct"] = 25.5
        result = validate_candidate(candidate)
        self.assertIn("CONTENT_HASH_MISMATCH", {finding.code for finding in result.findings})

    def test_hydric_current_requires_criteria_reference(self) -> None:
        candidate = copy.deepcopy(self.single)
        candidate["hydric"]["status"] = "CURRENT"
        candidate["hydric"]["criteria_ref"] = None
        _restamp(candidate)
        result = validate_candidate(candidate)
        self.assertIn("HYDRIC_CRITERIA_REQUIRED", {finding.code for finding in result.findings})

    def test_physical_ranges_fail_closed(self) -> None:
        candidate = copy.deepcopy(self.single)
        candidate["components"][0]["horizons"][0]["clay_total_pct"] = 110.0
        _restamp(candidate)
        result = validate_candidate(candidate)
        self.assertIn("PHYSICAL_RANGE_INVALID", {finding.code for finding in result.findings})

    def test_incomplete_root_zone_abstains(self) -> None:
        candidate = copy.deepcopy(self.single)
        candidate["components"][0]["horizons"][-1]["bottom_cm"] = 80
        _restamp(candidate)
        result = validate_candidate(candidate)
        codes = {finding.code for finding in result.findings}
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertIn("ROOT_ZONE_INCOMPLEDE", codes)
        self.assertIn("CRITICAL_PROPERTY_MISSING", codes)

    def test_source_family_role_pair_is_enforced(self) -> None:
        candidate = copy.deepcopy(self.single)
        candidate["source"]["source_role"] = "official_static_survey"
        _restamp(candidate)
        result = validate_candidate(candidate)
        self.assertIn("SOURCE_ROLE_MISMATCH", {finding.code for finding in result.findings})

    def test_component_and_horizon_identity_must_be_unique(self) -> None:
        candidate = copy.deepcopy(self.multi)
        candidate["components"][1]["cokey"] = candidate["components"][0]["cokey"]
        candidate["components"][1]["horizons"][0]["chkey"] = (
            candidate["components"][0]["horizons"][0]["chkey"]
        )
        _restamp(candidate)
        result = validate_candidate(candidate)
        codes = {finding.code for finding in result.findings}
        self.assertIn("DUPLICATE_COKEY", codes)
        self.assertIn("DUPLICATE_CHKEY", codes)

    def test_duplicate_keys_are_safe_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"profile":"a","profile":"b"}', encoding="utf-8")
            result = validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn(Finding("JSON_DUPLICATE_KEY", "/"), result.findings)

    def test_validation_is_deterministic_and_no_network(self) -> None:
        path = FIXTURE_ROOT / "valid/multi_component.json"
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "getaddrinfo", side_effect=AssertionError("dns denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("socket denied")):
            first = validate_file(path)
            second = validate_file(path)
        self.assertEqual(first, second)
        self.assertEqual(first.findings, tuple(sorted(first.findings)))

    def test_input_is_not_mutated(self) -> None:
        candidate = copy.deepcopy(self.multi)
        snapshot = copy.deepcopy(candidate)
        validate_candidate(candidate)
        self.assertEqual(candidate, snapshot)


if __name__ == "__main__":
    unittest.main()
