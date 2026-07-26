"""Bounded, deterministic, no-network Soil fixture validation tests.

This slice validates only synthetic in-memory candidates. It does not fetch source
material, establish soil truth, construct proof objects, promote lifecycle data,
or authorize release/publication.
"""

from __future__ import annotations

import copy
import json
import socket
import unittest
import urllib.request
from unittest.mock import patch


ALLOWED_TOP_LEVEL = {
    "record_id",
    "support_type",
    "source_descriptor_ref",
    "evidence_refs",
    "spatial_support",
    "depth_interval_cm",
    "measurement",
    "governance",
}
ALLOWED_SUPPORT_TYPES = {
    "static_survey",
    "station_observation",
    "satellite_grid",
    "modeled_derivative",
}
FORBIDDEN_LOCATION_KEYS = {
    "lat",
    "latitude",
    "lon",
    "lng",
    "longitude",
    "x",
    "y",
    "bbox",
    "centroid",
    "easting",
    "northing",
}


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("Soil fixture validation attempted network access")


def _base_candidate() -> dict:
    return {
        "record_id": "soil-fixture-0001",
        "support_type": "station_observation",
        "source_descriptor_ref": "source:synthetic-soil-station",
        "evidence_refs": ["evidence:synthetic-soil-reading"],
        "spatial_support": {
            "kind": "generalized_county",
            "county_fips": "99999",
        },
        "depth_interval_cm": {"top": 10, "bottom": 20},
        "measurement": {
            "property": "volumetric_water_content",
            "value": 0.24,
            "unit": "m3/m3",
        },
        "governance": {
            "rights_state": "fixture_only",
            "sensitivity_state": "public_safe_fixture",
            "review_state": "fixture_only",
            "release_state": "not_released",
            "promotion_eligible": False,
            "rollback_state": "fixture_only",
        },
    }


def validate_candidate(candidate: object) -> tuple[str, ...]:
    findings: list[str] = []

    if not isinstance(candidate, dict):
        return ("CANDIDATE_NOT_OBJECT",)

    for key in candidate:
        if key not in ALLOWED_TOP_LEVEL:
            findings.append(f"UNDECLARED_TOP_LEVEL_FIELD:{key}")

    support_type = candidate.get("support_type")
    if support_type not in ALLOWED_SUPPORT_TYPES:
        findings.append("SUPPORT_TYPE_INVALID")

    source_ref = candidate.get("source_descriptor_ref")
    if not isinstance(source_ref, str) or not source_ref.strip():
        findings.append("SOURCE_DESCRIPTOR_REF_MISSING")

    evidence_refs = candidate.get("evidence_refs")
    if not (
        isinstance(evidence_refs, list)
        and evidence_refs
        and all(isinstance(item, str) and item.strip() for item in evidence_refs)
    ):
        findings.append("EVIDENCE_REF_MISSING")

    spatial_support = candidate.get("spatial_support")
    if not isinstance(spatial_support, dict):
        findings.append("SPATIAL_SUPPORT_INVALID")
    else:
        for key in spatial_support:
            if str(key).casefold() in FORBIDDEN_LOCATION_KEYS:
                findings.append(f"PRECISE_LOCATION_FIELD_FORBIDDEN:{key}")
        if spatial_support.get("kind") != "generalized_county":
            findings.append("SPATIAL_SUPPORT_NOT_PUBLIC_SAFE")
        county_fips = spatial_support.get("county_fips")
        if not (
            isinstance(county_fips, str)
            and len(county_fips) == 5
            and county_fips.isdigit()
        ):
            findings.append("COUNTY_FIPS_INVALID")

    depth = candidate.get("depth_interval_cm")
    if not isinstance(depth, dict):
        findings.append("DEPTH_INTERVAL_INVALID")
    else:
        top = depth.get("top")
        bottom = depth.get("bottom")
        if not isinstance(top, (int, float)) or not isinstance(bottom, (int, float)):
            findings.append("DEPTH_INTERVAL_NON_NUMERIC")
        elif top < 0 or bottom <= top:
            findings.append("DEPTH_INTERVAL_INVALID")

    measurement = candidate.get("measurement")
    if not isinstance(measurement, dict):
        findings.append("MEASUREMENT_INVALID")
    else:
        value = measurement.get("value")
        if not isinstance(value, (int, float)) or not 0 <= value <= 1:
            findings.append("MEASUREMENT_VALUE_OUT_OF_RANGE")
        if measurement.get("unit") != "m3/m3":
            findings.append("MEASUREMENT_UNIT_INVALID")
        if measurement.get("property") != "volumetric_water_content":
            findings.append("MEASUREMENT_PROPERTY_INVALID")

    governance = candidate.get("governance")
    required_governance = {
        "rights_state": "fixture_only",
        "sensitivity_state": "public_safe_fixture",
        "review_state": "fixture_only",
        "release_state": "not_released",
        "promotion_eligible": False,
        "rollback_state": "fixture_only",
    }
    if not isinstance(governance, dict):
        findings.append("GOVERNANCE_INVALID")
    else:
        for key, expected in required_governance.items():
            if governance.get(key) != expected:
                findings.append(f"GOVERNANCE_STATE_INVALID:{key}")

    return tuple(sorted(set(findings)))


class SoilPublicSafeFixtureValidationTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_synthetic_public_safe_candidate_passes_without_network(self):
        self.assertEqual(validate_candidate(_base_candidate()), ())

    def test_support_types_cannot_be_collapsed_or_omitted(self):
        for support_type in sorted(ALLOWED_SUPPORT_TYPES):
            with self.subTest(support_type=support_type):
                candidate = _base_candidate()
                candidate["support_type"] = support_type
                self.assertEqual(validate_candidate(candidate), ())

        for invalid in (None, "", "soil", "authoritative_surface", ["static_survey"]):
            with self.subTest(invalid=invalid):
                candidate = _base_candidate()
                candidate["support_type"] = invalid
                self.assertIn("SUPPORT_TYPE_INVALID", validate_candidate(candidate))

    def test_missing_source_and_evidence_refs_fail_closed(self):
        candidate = _base_candidate()
        candidate["source_descriptor_ref"] = ""
        candidate["evidence_refs"] = []
        findings = validate_candidate(candidate)
        self.assertIn("SOURCE_DESCRIPTOR_REF_MISSING", findings)
        self.assertIn("EVIDENCE_REF_MISSING", findings)

    def test_depth_interval_and_units_are_bounded(self):
        cases = (
            ({"top": 20, "bottom": 10}, "DEPTH_INTERVAL_INVALID"),
            ({"top": -1, "bottom": 10}, "DEPTH_INTERVAL_INVALID"),
            ({"top": "10", "bottom": 20}, "DEPTH_INTERVAL_NON_NUMERIC"),
        )
        for depth, expected in cases:
            with self.subTest(depth=depth):
                candidate = _base_candidate()
                candidate["depth_interval_cm"] = depth
                self.assertIn(expected, validate_candidate(candidate))

        candidate = _base_candidate()
        candidate["measurement"]["unit"] = "%"
        candidate["measurement"]["value"] = 24
        findings = validate_candidate(candidate)
        self.assertIn("MEASUREMENT_UNIT_INVALID", findings)
        self.assertIn("MEASUREMENT_VALUE_OUT_OF_RANGE", findings)

    def test_exact_or_aliased_location_fields_fail_closed(self):
        for alias in sorted(FORBIDDEN_LOCATION_KEYS):
            with self.subTest(alias=alias):
                candidate = _base_candidate()
                candidate["spatial_support"][alias] = "synthetic-only"
                self.assertIn(
                    f"PRECISE_LOCATION_FIELD_FORBIDDEN:{alias}",
                    validate_candidate(candidate),
                )

    def test_non_public_governance_states_are_rejected(self):
        candidate = _base_candidate()
        candidate["governance"].update(
            {
                "rights_state": "unknown",
                "sensitivity_state": "unreviewed",
                "review_state": "pending",
                "release_state": "published",
                "promotion_eligible": True,
                "rollback_state": "missing",
            }
        )
        findings = validate_candidate(candidate)
        for key in (
            "rights_state",
            "sensitivity_state",
            "review_state",
            "release_state",
            "promotion_eligible",
            "rollback_state",
        ):
            self.assertIn(f"GOVERNANCE_STATE_INVALID:{key}", findings)

    def test_undeclared_fields_are_rejected(self):
        candidate = _base_candidate()
        candidate["generated_claim"] = "synthetic"
        self.assertIn(
            "UNDECLARED_TOP_LEVEL_FIELD:generated_claim",
            validate_candidate(candidate),
        )

    def test_round_trip_json_does_not_change_validation(self):
        candidate = _base_candidate()
        round_tripped = json.loads(json.dumps(candidate, sort_keys=True))
        self.assertEqual(validate_candidate(round_tripped), ())


if __name__ == "__main__":
    unittest.main()
