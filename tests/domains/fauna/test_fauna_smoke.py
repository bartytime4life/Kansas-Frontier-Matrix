"""Bounded, deterministic, no-network Fauna fixture validation tests."""

from __future__ import annotations

import copy
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.domains.fauna.validate_public_safe_fixture import (
    MAX_FIXTURE_BYTES,
    MAX_JSON_INTEGER_DIGITS,
    main,
    validate_candidate,
    validate_file,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "fixtures" / "domains" / "fauna"
VALID_FIXTURE = FIXTURE_ROOT / "valid" / "non_sensitive_occurrence.json"
ENCODED_FIXTURE = FIXTURE_ROOT / "invalid" / "encoded_location_clue.json"
LOCATION_ALIASES = (
    "lat",
    "lon",
    "lng",
    "x",
    "y",
    "bbox",
    "centroid",
    "easting",
    "northing",
)
INVALID_FIXTURES = {
    FIXTURE_ROOT / "invalid" / "missing_source_descriptor.json": {
        ("SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref")
    },
    FIXTURE_ROOT / "invalid" / "over_precise_sensitive.json": {
        (
            "PRECISE_LOCATION_FIELD_FORBIDDEN",
            "$.spatial_support.latitude",
        ),
        (
            "PRECISE_LOCATION_FIELD_FORBIDDEN",
            "$.spatial_support.longitude",
        ),
        ("SENSITIVITY_NOT_PUBLIC_SAFE", "$.sensitivity_state"),
        ("SPATIAL_SUPPORT_NOT_PUBLIC_SAFE", "$.spatial_support.kind"),
        ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.latitude"),
        ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.longitude"),
    },
    FIXTURE_ROOT / "invalid" / "unresolved_taxonomy.json": {
        ("TAXONOMY_UNRESOLVED", "$.taxonomy_state")
    },
    FIXTURE_ROOT / "invalid" / "unresolved_governance.json": {
        ("CORRECTION_STATE_NOT_FIXTURE_ONLY", "$.governance.correction_state"),
        ("EVIDENCE_REF_MISSING", "$.evidence_refs"),
        ("EVIDENCE_STATE_UNRESOLVED", "$.governance.evidence_state"),
        (
            "GEOPRIVACY_STATE_UNRESOLVED",
            "$.governance.geoprivacy_state",
        ),
        ("POLICY_STATE_UNRESOLVED", "$.governance.policy_state"),
        ("REVIEW_STATE_NOT_FIXTURE_ONLY", "$.governance.review_state"),
        ("RIGHTS_STATE_UNRESOLVED", "$.rights_state"),
        ("ROLLBACK_STATE_NOT_FIXTURE_ONLY", "$.governance.rollback_state"),
    },
    ENCODED_FIXTURE: {
        ("COORDINATE_PATTERN_FORBIDDEN", "$.public_caveats.1"),
        ("LIVE_URL_FORBIDDEN", "$.public_caveats.0"),
        (
            "PRECISE_LOCATION_FIELD_FORBIDDEN",
            "$.spatial_support.centroid",
        ),
        ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.centroid"),
    },
}


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("Fauna fixture validation attempted network access")


class FaunaPublicSafeFixtureValidationTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_synthetic_public_safe_fixture_passes_without_network(self):
        findings = validate_file(VALID_FIXTURE)
        self.assertEqual(findings, ())

    def test_accepted_fixture_inventory_is_explicit(self):
        self.assertEqual(
            set((FIXTURE_ROOT / "valid").glob("*.json")),
            {VALID_FIXTURE},
        )
        self.assertEqual(
            set((FIXTURE_ROOT / "invalid").glob("*.json")),
            set(INVALID_FIXTURES),
        )

    def test_fail_closed_fixtures_return_expected_findings(self):
        for fixture_path, expected_findings in INVALID_FIXTURES.items():
            with self.subTest(fixture=fixture_path.name):
                findings = validate_file(fixture_path)
                actual_findings = {
                    (finding.code, finding.path) for finding in findings
                }
                self.assertEqual(
                    actual_findings,
                    expected_findings,
                    f"{fixture_path.name}: {sorted(actual_findings)}",
                )

        output = io.StringIO()
        with redirect_stdout(output):
            return_code = main([str(ENCODED_FIXTURE)])

        self.assertEqual(return_code, 1)
        self.assertNotIn("Synthetic out-of-range pair", output.getvalue())
        self.assertNotIn("999999", output.getvalue())

    def test_location_aliases_and_numeric_values_fail_closed(self):
        base_payload = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))

        for alias in LOCATION_ALIASES:
            with self.subTest(alias=alias):
                payload = copy.deepcopy(base_payload)
                payload["spatial_support"][alias] = "SYNTHETIC-ONLY"
                actual = {
                    (finding.code, finding.path)
                    for finding in validate_candidate(payload)
                }
                path = f"$.spatial_support.{alias}"
                self.assertIn(
                    ("PRECISE_LOCATION_FIELD_FORBIDDEN", path),
                    actual,
                )
                self.assertIn(
                    ("UNDECLARED_SPATIAL_FIELD", path),
                    actual,
                )

        payload = copy.deepcopy(base_payload)
        payload["spatial_support"]["x"] = 999.0
        actual = {
            (finding.code, finding.path)
            for finding in validate_candidate(payload)
        }
        self.assertIn(
            ("PRECISE_LOCATION_FIELD_FORBIDDEN", "$.spatial_support.x"),
            actual,
        )
        self.assertIn(
            ("LOCATION_NUMERIC_VALUE_FORBIDDEN", "$.spatial_support.x"),
            actual,
        )

        oversized_integer = copy.deepcopy(base_payload)
        oversized_integer["spatial_support"]["x"] = "OVERSIZED_INTEGER"
        with tempfile.TemporaryDirectory() as temp_directory:
            invalid_path = Path(temp_directory) / "oversized-integer.json"
            invalid_path.write_text(
                json.dumps(oversized_integer).replace(
                    '"OVERSIZED_INTEGER"',
                    "9" * (MAX_JSON_INTEGER_DIGITS + 1),
                ),
                encoding="utf-8",
            )
            invalid_findings = {
                (finding.code, finding.path)
                for finding in validate_file(invalid_path)
            }

            bounded_path = Path(temp_directory) / "bounded-integer.json"
            bounded_path.write_text(
                json.dumps(oversized_integer).replace(
                    '"OVERSIZED_INTEGER"',
                    "9" * MAX_JSON_INTEGER_DIGITS,
                ),
                encoding="utf-8",
            )
            bounded_findings = {
                (finding.code, finding.path)
                for finding in validate_file(bounded_path)
            }

            too_large_path = Path(temp_directory) / "too-large.json"
            too_large_path.write_text(
                " " * (MAX_FIXTURE_BYTES + 1),
                encoding="utf-8",
            )
            too_large_findings = {
                (finding.code, finding.path)
                for finding in validate_file(too_large_path)
            }

        self.assertEqual(invalid_findings, {("FIXTURE_JSON_INVALID", "$")})
        self.assertIn(
            ("LOCATION_NUMERIC_VALUE_FORBIDDEN", "$.spatial_support.x"),
            bounded_findings,
        )
        self.assertEqual(too_large_findings, {("FIXTURE_TOO_LARGE", "$")})
        self.assertIn(
            ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.x"),
            actual,
        )

        payload = copy.deepcopy(base_payload)
        payload[1] = "synthetic"
        payload["extra_mixed"] = "synthetic"
        payload["spatial_support"][2] = "synthetic"
        payload["spatial_support"]["extra_mixed"] = "synthetic"
        payload["governance"][3] = "synthetic"
        payload["governance"]["extra_mixed"] = "synthetic"
        mixed_key_findings = {
            (finding.code, finding.path)
            for finding in validate_candidate(payload)
        }
        self.assertIn(("UNDECLARED_TOP_LEVEL_FIELD", "$.1"), mixed_key_findings)
        self.assertIn(
            ("UNDECLARED_TOP_LEVEL_FIELD", "$.extra_mixed"),
            mixed_key_findings,
        )
        self.assertIn(
            ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.2"),
            mixed_key_findings,
        )
        self.assertIn(
            ("UNDECLARED_SPATIAL_FIELD", "$.spatial_support.extra_mixed"),
            mixed_key_findings,
        )
        self.assertIn(
            ("UNDECLARED_GOVERNANCE_FIELD", "$.governance.3"),
            mixed_key_findings,
        )
        self.assertIn(
            ("UNDECLARED_GOVERNANCE_FIELD", "$.governance.extra_mixed"),
            mixed_key_findings,
        )

        payload = copy.deepcopy(base_payload)
        payload["spatial_support"]["x"] = 10**400
        actual = {
            (finding.code, finding.path)
            for finding in validate_candidate(payload)
        }
        self.assertIn(
            ("PRECISE_LOCATION_FIELD_FORBIDDEN", "$.spatial_support.x"),
            actual,
        )
        self.assertIn(
            ("LOCATION_NUMERIC_VALUE_FORBIDDEN", "$.spatial_support.x"),
            actual,
        )

    def test_public_caveats_reject_malformed_and_encoded_content(self):
        base_payload = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        malformed_cases = (
            (
                "null",
                None,
                ("PUBLIC_CAVEATS_INVALID", "$.public_caveats"),
            ),
            (
                "object",
                {"note": "synthetic"},
                ("PUBLIC_CAVEATS_INVALID", "$.public_caveats"),
            ),
            (
                "number",
                999,
                ("PUBLIC_CAVEATS_INVALID", "$.public_caveats"),
            ),
            (
                "string",
                "synthetic",
                ("PUBLIC_CAVEATS_INVALID", "$.public_caveats"),
            ),
            (
                "empty",
                [],
                ("PUBLIC_CAVEATS_INVALID", "$.public_caveats"),
            ),
            (
                "nested",
                [["synthetic"]],
                ("PUBLIC_CAVEAT_INVALID", "$.public_caveats.0"),
            ),
            (
                "unbounded",
                ["x" * 513],
                ("PUBLIC_CAVEAT_TOO_LONG", "$.public_caveats.0"),
            ),
            (
                "too-many",
                ["synthetic"] * 17,
                ("PUBLIC_CAVEATS_TOO_MANY", "$.public_caveats"),
            ),
        )

        for case, caveats, expected in malformed_cases:
            with self.subTest(case=case):
                payload = copy.deepcopy(base_payload)
                payload["public_caveats"] = caveats
                malformed = {
                    (finding.code, finding.path)
                    for finding in validate_candidate(payload)
                }
                self.assertIn(expected, malformed)

        deeply_nested = "synthetic"
        for _ in range(1_100):
            deeply_nested = [deeply_nested]
        payload = copy.deepcopy(base_payload)
        payload["public_caveats"] = [deeply_nested]
        nested_findings = {
            (finding.code, finding.path)
            for finding in validate_candidate(payload)
        }
        self.assertEqual(
            {code for code, _path in nested_findings},
            {"DOCUMENT_DEPTH_EXCEEDED"},
        )

        cyclic = []
        cyclic.append(cyclic)
        payload = copy.deepcopy(base_payload)
        payload["public_caveats"] = cyclic
        cyclic_findings = {
            (finding.code, finding.path)
            for finding in validate_candidate(payload)
        }
        self.assertEqual(
            cyclic_findings,
            {("DOCUMENT_CYCLE_FORBIDDEN", "$.public_caveats.0")},
        )

        payload = copy.deepcopy(base_payload)
        payload["public_caveats"] = ["synthetic"] * 4_097
        bounded_findings = {
            (finding.code, finding.path)
            for finding in validate_candidate(payload)
        }
        self.assertEqual(
            bounded_findings,
            {("DOCUMENT_NODE_LIMIT_EXCEEDED", "$")},
        )

        shared = {"note": "synthetic"}
        payload = copy.deepcopy(base_payload)
        payload["extra_a"] = shared
        payload["extra_b"] = shared
        shared_findings = {
            (finding.code, finding.path)
            for finding in validate_candidate(payload)
        }
        self.assertNotIn(
            "DOCUMENT_CYCLE_FORBIDDEN",
            {code for code, _path in shared_findings},
        )

        payload = copy.deepcopy(base_payload)
        payload["public_caveats"] = [
            "  HTTPS://",
            "  //",
            "  WWW.",
            "Synthetic embedded scheme-relative marker //",
            "Synthetic split marker https:/ /",
            "H T T P S : / / synthetic marker",
            "Synthetic format marker https:/\u200b/",
            "Synthetic control\x00marker",
            "Synthetic out-of-range pair 999999, -999999",
            "Synthetic whitespace pair 999999 -999999",
            "Synthetic exponent pair 9e9; -9e9",
            "Synthetic slash pair 999999/-999999",
        ]
        encoded = {
            (finding.code, finding.path)
            for finding in validate_candidate(payload)
        }
        self.assertIn(
            ("LIVE_URL_FORBIDDEN", "$.public_caveats.0"),
            encoded,
        )
        self.assertIn(
            ("LIVE_URL_FORBIDDEN", "$.public_caveats.1"),
            encoded,
        )
        self.assertIn(
            ("LIVE_URL_FORBIDDEN", "$.public_caveats.2"),
            encoded,
        )
        self.assertIn(
            ("LIVE_URL_FORBIDDEN", "$.public_caveats.3"),
            encoded,
        )
        self.assertIn(
            ("LIVE_URL_FORBIDDEN", "$.public_caveats.4"),
            encoded,
        )
        self.assertIn(
            ("LIVE_URL_FORBIDDEN", "$.public_caveats.5"),
            encoded,
        )
        self.assertIn(
            ("LIVE_URL_FORBIDDEN", "$.public_caveats.6"),
            encoded,
        )
        self.assertIn(
            ("CONTROL_CHARACTER_FORBIDDEN", "$.public_caveats.7"),
            encoded,
        )
        for index in range(8, 12):
            self.assertIn(
                ("COORDINATE_PATTERN_FORBIDDEN", f"$.public_caveats.{index}"),
                encoded,
            )

    def test_fixture_corpus_contains_no_live_target_or_plausible_coordinate(self):
        for fixture_path in (VALID_FIXTURE, *INVALID_FIXTURES):
            with self.subTest(fixture=fixture_path.name):
                payload = json.loads(fixture_path.read_text(encoding="utf-8"))
                serialized = json.dumps(payload, sort_keys=True).casefold()
                self.assertNotIn("http://", serialized)
                self.assertNotIn("https://", serialized)
                self.assertNotIn("www.", serialized)

                for value in _walk_values(payload):
                    if isinstance(value, (int, float)) and not isinstance(
                        value, bool
                    ):
                        self.assertGreater(
                            abs(float(value)),
                            180.0,
                            f"{fixture_path.name} contains plausible coordinate",
                        )

    def test_cli_emits_stable_pass_envelope_for_accepted_fixture(self):
        output = io.StringIO()
        with redirect_stdout(output):
            return_code = main([str(VALID_FIXTURE)])

        self.assertEqual(return_code, 0)
        envelope = json.loads(output.getvalue())
        self.assertEqual(envelope["findings"], [])
        self.assertEqual(envelope["outcome"], "PASS")
        self.assertEqual(
            envelope["scope"], "synthetic-public-safe-fixture-only"
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
