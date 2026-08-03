"""Bounded, deterministic, no-network Flora fixture validation tests."""

from __future__ import annotations

import copy
import io
import json
import socket
import sys
import tempfile
import unittest
import urllib.request
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES  # noqa: E402
from tools.validators.domains.flora.validate_public_safe_fixture import (
    MAX_CAVEAT_ITEMS,
    MAX_EVIDENCE_REFS,
    SCOPE,
    main,
    validate_candidate,
    validate_file,
)  # noqa: E402


FIXTURE_ROOT = REPO_ROOT / "fixtures" / "domains" / "flora"
VALID_FIXTURE = FIXTURE_ROOT / "valid" / "non_sensitive_occurrence.json"
ENCODED_FIXTURE = FIXTURE_ROOT / "invalid" / "encoded_location_clue.json"
LOCATION_ALIASES = (
    "lat",
    "latitude",
    "lon",
    "lng",
    "x",
    "y",
    "bbox",
    "centroid",
    "easting",
    "northing",
    "exact-location",
    "occurrence coordinates",
    "decimalLatitude",
    "decimalLongitude",
    "verbatimCoordinates",
)
INVALID_FIXTURES = {
    FIXTURE_ROOT / "invalid" / "missing_source_descriptor.json": {
        ("SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref"),
    },
    FIXTURE_ROOT / "invalid" / "over_precise_sensitive.json": {
        ("PRECISE_LOCATION_FIELD_FORBIDDEN", "$.spatial_support.latitude"),
        ("PRECISE_LOCATION_FIELD_FORBIDDEN", "$.spatial_support.longitude"),
        ("SENSITIVITY_NOT_PUBLIC_SAFE", "$.sensitivity_state"),
        ("SPATIAL_SUPPORT_NOT_PUBLIC_SAFE", "$.spatial_support.kind"),
        ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.latitude"),
        ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.longitude"),
    },
    FIXTURE_ROOT / "invalid" / "unresolved_taxonomy.json": {
        ("TAXONOMY_UNRESOLVED", "$.taxonomy_state"),
    },
    FIXTURE_ROOT / "invalid" / "unresolved_governance.json": {
        ("CORRECTION_STATE_NOT_FIXTURE_ONLY", "$.governance.correction_state"),
        ("EVIDENCE_REF_MISSING", "$.evidence_refs"),
        ("EVIDENCE_STATE_UNRESOLVED", "$.governance.evidence_state"),
        ("GEOPRIVACY_STATE_UNRESOLVED", "$.governance.geoprivacy_state"),
        ("POLICY_STATE_UNRESOLVED", "$.governance.policy_state"),
        ("REVIEW_STATE_NOT_FIXTURE_ONLY", "$.governance.review_state"),
        ("RIGHTS_STATE_UNRESOLVED", "$.rights_state"),
        ("ROLLBACK_STATE_NOT_FIXTURE_ONLY", "$.governance.rollback_state"),
    },
    ENCODED_FIXTURE: {
        ("COORDINATE_PATTERN_FORBIDDEN", "$.public_caveats.1"),
        ("LIVE_URL_FORBIDDEN", "$.public_caveats.0"),
        ("PRECISE_LOCATION_FIELD_FORBIDDEN", "$.spatial_support.centroid"),
        ("PUBLIC_CAVEAT_NOT_PROFILE_TOKEN", "$.public_caveats.0"),
        ("PUBLIC_CAVEAT_NOT_PROFILE_TOKEN", "$.public_caveats.1"),
        ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.centroid"),
    },
}


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("Flora fixture validation attempted network access")


def _finding_pairs(findings):
    return {(finding.code, finding.path) for finding in findings}


def _base_payload():
    return json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))


class FloraPublicSafeFixtureValidationTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_synthetic_withheld_fixture_passes_without_network(self):
        self.assertEqual(validate_file(VALID_FIXTURE), [])

    def test_accepted_fixture_inventory_is_explicit(self):
        self.assertEqual(
            set((FIXTURE_ROOT / "valid").glob("*.json")),
            {VALID_FIXTURE},
        )
        self.assertEqual(
            set((FIXTURE_ROOT / "invalid").glob("*.json")),
            set(INVALID_FIXTURES),
        )

    def test_fail_closed_fixtures_return_exact_findings(self):
        for fixture_path, expected_findings in INVALID_FIXTURES.items():
            with self.subTest(fixture=fixture_path.name):
                self.assertEqual(
                    _finding_pairs(validate_file(fixture_path)),
                    expected_findings,
                )

    def test_sensitive_failure_output_never_echoes_candidate_values(self):
        output = io.StringIO()
        with redirect_stdout(output):
            return_code = main([str(ENCODED_FIXTURE)])
        self.assertEqual(return_code, 1)
        self.assertNotIn("Synthetic out-of-range pair", output.getvalue())
        self.assertNotIn("999999", output.getvalue())
        self.assertNotIn("SYNTHETIC-ONLY", output.getvalue())

    def test_location_aliases_and_numeric_location_values_fail_closed(self):
        base_payload = _base_payload()
        for alias in LOCATION_ALIASES:
            with self.subTest(alias=alias):
                payload = copy.deepcopy(base_payload)
                payload["spatial_support"][alias] = "SYNTHETIC-ONLY"
                findings = _finding_pairs(validate_candidate(payload))
                normalized_alias = {
                    "exact-location": "exact_location",
                    "occurrence coordinates": "occurrence_coordinates",
                    "decimalLatitude": "decimal_latitude",
                    "decimalLongitude": "decimal_longitude",
                    "verbatimCoordinates": "verbatim_coordinates",
                }.get(alias, alias)
                path = f"$.spatial_support.{normalized_alias}"
                self.assertIn(("PRECISE_LOCATION_FIELD_FORBIDDEN", path), findings)
                self.assertIn(("UNDECLARED_SPATIAL_FIELD", path), findings)

        payload = copy.deepcopy(base_payload)
        payload["spatial_support"]["x"] = 999.0
        findings = _finding_pairs(validate_candidate(payload))
        self.assertIn(
            ("LOCATION_NUMERIC_VALUE_FORBIDDEN", "$.spatial_support.x"),
            findings,
        )

    def test_recursive_location_fields_fail_closed(self):
        payload = _base_payload()
        payload["extra"] = {"nested": {"exact_location": {"clue": 999}}}
        findings = _finding_pairs(validate_candidate(payload))
        self.assertIn(("UNDECLARED_TOP_LEVEL_FIELD", "$.field_0"), findings)
        location_paths = {
            path
            for code, path in findings
            if code == "PRECISE_LOCATION_FIELD_FORBIDDEN"
        }
        self.assertEqual(len(location_paths), 1)
        location_path = location_paths.pop()
        self.assertTrue(location_path.endswith(".exact_location"))
        self.assertIn(
            ("LOCATION_NUMERIC_VALUE_FORBIDDEN", location_path),
            findings,
        )

    def test_encoded_urls_coordinates_and_control_characters_fail_closed(self):
        payload = _base_payload()
        payload["public_caveats"] = [
            "H T T P S : / / synthetic marker",
            "Synthetic pair 999999, -999999",
            "Synthetic control\x00marker",
        ]
        findings = _finding_pairs(validate_candidate(payload))
        self.assertIn(("LIVE_URL_FORBIDDEN", "$.public_caveats.0"), findings)
        self.assertIn(
            ("COORDINATE_PATTERN_FORBIDDEN", "$.public_caveats.1"),
            findings,
        )
        self.assertIn(
            ("CONTROL_CHARACTER_FORBIDDEN", "$.public_caveats.2"),
            findings,
        )

    def test_closed_shapes_reject_undeclared_fields_deterministically(self):
        payload = _base_payload()
        payload["extra"] = "synthetic"
        payload["spatial_support"]["extra"] = "synthetic"
        payload["governance"]["extra"] = "synthetic"
        first = validate_candidate(payload)
        second = validate_candidate(copy.deepcopy(payload))
        self.assertEqual(first, second)
        self.assertEqual(first, sorted(first))
        self.assertIn(
            ("UNDECLARED_TOP_LEVEL_FIELD", "$.field_0"),
            _finding_pairs(first),
        )
        self.assertIn(
            ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.field_0"),
            _finding_pairs(first),
        )
        self.assertIn(
            ("UNDECLARED_GOVERNANCE_FIELD", "$.governance.field_0"),
            _finding_pairs(first),
        )

    def test_unknown_key_and_value_are_redacted_from_cli_findings(self):
        payload = _base_payload()
        sensitive_key = "38.8977,-77.0365"
        sensitive_value = "dqcjqcp84c6e"
        payload[sensitive_key] = sensitive_value

        with tempfile.TemporaryDirectory() as temp_directory:
            path = Path(temp_directory) / "candidate.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            output = io.StringIO()
            with redirect_stdout(output):
                return_code = main([str(path)])

        self.assertEqual(return_code, 1)
        self.assertNotIn(sensitive_key, output.getvalue())
        self.assertNotIn(sensitive_value, output.getvalue())
        self.assertIn("field_", output.getvalue())

    def test_profile_strings_are_exact_and_canonical(self):
        mutations = (
            ("fixture_id", "fixture:flora:valid:dqcjqcp84c6e"),
            ("source_descriptor_ref", "fixture:source:flora:dqcjqcp84c6e"),
            ("taxon_ref", "fixture:taxon:flora:dqcjqcp84c6e"),
        )
        for field, value in mutations:
            with self.subTest(field=field):
                payload = _base_payload()
                payload[field] = value
                self.assertIn(
                    ("STRING_VALUE_NOT_PROFILE_TOKEN", f"$.{field}"),
                    _finding_pairs(validate_candidate(payload)),
                )

        payload = _base_payload()
        payload["evidence_refs"][0] = "fixture:evidence:flora:dqcjqcp84c6e"
        self.assertIn(
            ("STRING_VALUE_NOT_PROFILE_TOKEN", "$.evidence_refs.0"),
            _finding_pairs(validate_candidate(payload)),
        )

        payload = _base_payload()
        payload["spatial_support"]["label"] = "synthetic-area-dqcjqcp84c6e"
        self.assertIn(
            ("STRING_VALUE_NOT_PROFILE_TOKEN", "$.spatial_support.label"),
            _finding_pairs(validate_candidate(payload)),
        )

        for field in ("fixture_id", "source_descriptor_ref", "taxon_ref"):
            with self.subTest(canonical_field=field):
                payload = _base_payload()
                payload[field] = f" {payload[field]} "
                self.assertIn(
                    ("STRING_VALUE_NOT_PROFILE_TOKEN", f"$.{field}"),
                    _finding_pairs(validate_candidate(payload)),
                )

    def test_public_caveats_accept_only_fixed_profile_tokens(self):
        leak_channels = (
            ["38.500000", "-98.500000"],
            ["latitude 38.500000", "longitude -98.500000"],
            ["decimalLatitude=38.500000", "decimalLongitude=-98.500000"],
            ["38°53′52.9″N 77°02′11.6″W"],
            ["1600 Pennsylvania Avenue NW, Washington, DC 20500"],
            ["dqcjqcp84c6e"],
            ["ｈｔｔｐｓ：／／example.invalid"],
            ["MzguODk3NywtNzcuMDM2NQ=="],
        )
        for caveats in leak_channels:
            with self.subTest(caveats=caveats):
                payload = _base_payload()
                payload["public_caveats"] = caveats
                findings = _finding_pairs(validate_candidate(payload))
                for index in range(len(caveats)):
                    self.assertIn(
                        (
                            "PUBLIC_CAVEAT_NOT_PROFILE_TOKEN",
                            f"$.public_caveats.{index}",
                        ),
                        findings,
                    )

    def test_only_synthetic_source_role_is_accepted(self):
        for source_role in ("observed", "aggregate", "candidate", "modeled"):
            with self.subTest(source_role=source_role):
                payload = _base_payload()
                payload["source_role"] = source_role
                self.assertIn(
                    ("SOURCE_ROLE_NOT_SYNTHETIC", "$.source_role"),
                    _finding_pairs(validate_candidate(payload)),
                )

    def test_release_and_promotion_claims_fail_closed(self):
        payload = _base_payload()
        payload["governance"]["release_state"] = "released"
        payload["governance"]["promotion_state"] = "eligible"
        findings = _finding_pairs(validate_candidate(payload))
        self.assertIn(
            ("RELEASE_STATE_NOT_HELD", "$.governance.release_state"),
            findings,
        )
        self.assertIn(
            ("PROMOTION_STATE_NOT_HELD", "$.governance.promotion_state"),
            findings,
        )

    def test_evidence_references_are_unique_and_bounded(self):
        payload = _base_payload()
        payload["evidence_refs"] = [
            "fixture:evidence:flora:duplicate",
            "fixture:evidence:flora:duplicate",
        ]
        self.assertIn(
            ("EVIDENCE_REF_DUPLICATE", "$.evidence_refs.1"),
            _finding_pairs(validate_candidate(payload)),
        )

        payload["evidence_refs"] = [
            f"fixture:evidence:flora:item-{index}"
            for index in range(MAX_EVIDENCE_REFS + 1)
        ]
        self.assertIn(
            ("EVIDENCE_REFS_TOO_MANY", "$.evidence_refs"),
            _finding_pairs(validate_candidate(payload)),
        )

    def test_public_caveats_are_typed_and_bounded(self):
        malformed_cases = (
            None,
            {},
            "synthetic",
            [],
        )
        for caveats in malformed_cases:
            with self.subTest(caveats=repr(caveats)):
                payload = _base_payload()
                payload["public_caveats"] = caveats
                self.assertIn(
                    ("PUBLIC_CAVEATS_INVALID", "$.public_caveats"),
                    _finding_pairs(validate_candidate(payload)),
                )

        payload = _base_payload()
        payload["public_caveats"] = ["synthetic"] * (MAX_CAVEAT_ITEMS + 1)
        self.assertIn(
            ("PUBLIC_CAVEATS_TOO_MANY", "$.public_caveats"),
            _finding_pairs(validate_candidate(payload)),
        )

    def test_parser_rejects_duplicate_nonfinite_nonobject_and_invalid_utf8(self):
        cases = {
            "duplicate.json": (
                b'{"fixture_id":"one","fixture_id":"two"}',
                {("FIXTURE_JSON_INVALID", "$")},
            ),
            "nonfinite.json": (
                b'{"value":NaN}',
                {("FIXTURE_JSON_INVALID", "$")},
            ),
            "nonobject.json": (b"[]", {("DOCUMENT_NOT_OBJECT", "$")}),
            "invalid-utf8.json": (b"\xff", {("FIXTURE_JSON_INVALID", "$")}),
        }
        with tempfile.TemporaryDirectory() as temp_directory:
            for filename, (content, expected) in cases.items():
                with self.subTest(filename=filename):
                    path = Path(temp_directory) / filename
                    path.write_bytes(content)
                    self.assertEqual(_finding_pairs(validate_file(path)), expected)

    def test_parser_rejects_oversize_depth_and_node_exhaustion(self):
        with tempfile.TemporaryDirectory() as temp_directory:
            temp_root = Path(temp_directory)
            oversized = temp_root / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(
                _finding_pairs(validate_file(oversized)),
                {("FIXTURE_TOO_LARGE", "$")},
            )

            nested: object = "synthetic"
            for _ in range(70):
                nested = [nested]
            too_deep = temp_root / "too-deep.json"
            too_deep.write_text(json.dumps(nested), encoding="utf-8")
            self.assertEqual(
                _finding_pairs(validate_file(too_deep)),
                {("FIXTURE_JSON_INVALID", "$")},
            )

            too_many = temp_root / "too-many.json"
            too_many.write_text(json.dumps([None] * 4_100), encoding="utf-8")
            self.assertEqual(
                _finding_pairs(validate_file(too_many)),
                {("FIXTURE_JSON_INVALID", "$")},
            )

    def test_cli_exit_codes_and_stable_pass_envelope(self):
        output = io.StringIO()
        with redirect_stdout(output):
            return_code = main([str(VALID_FIXTURE)])
        self.assertEqual(return_code, 0)
        envelope = json.loads(output.getvalue())
        self.assertEqual(envelope["findings"], [])
        self.assertEqual(envelope["status"], "PASS")
        self.assertEqual(envelope["scope"], SCOPE)

        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(main([str(ENCODED_FIXTURE)]), 1)

        error = io.StringIO()
        with redirect_stderr(error):
            self.assertEqual(main([]), 2)
        self.assertIn("at least one fixture file is required", error.getvalue())

    def test_fixture_corpus_contains_no_live_target_or_plausible_number(self):
        for fixture_path in (VALID_FIXTURE, *INVALID_FIXTURES):
            with self.subTest(fixture=fixture_path.name):
                payload = json.loads(fixture_path.read_text(encoding="utf-8"))
                serialized = json.dumps(payload, sort_keys=True).casefold()
                self.assertNotIn("http://", serialized)
                self.assertNotIn("https://", serialized)
                self.assertNotIn("www.", serialized)
                for value in _walk_values(payload):
                    if isinstance(value, (int, float)) and not isinstance(value, bool):
                        self.assertGreater(
                            abs(float(value)),
                            180.0,
                            f"{fixture_path.name} contains a plausible coordinate",
                        )


def _walk_values(value):
    pending = [value]
    while pending:
        parent = pending.pop()
        if isinstance(parent, dict):
            children = list(parent.values())
        elif isinstance(parent, list):
            children = list(parent)
        else:
            continue
        for child in children:
            yield child
        pending.extend(children)


if __name__ == "__main__":
    unittest.main()
