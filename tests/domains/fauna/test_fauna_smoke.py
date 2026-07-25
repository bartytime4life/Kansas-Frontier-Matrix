"""Bounded, deterministic, no-network Fauna fixture validation tests."""

from __future__ import annotations

import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.domains.fauna.validate_public_safe_fixture import (
    main,
    validate_file,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "fixtures" / "domains" / "fauna"
VALID_FIXTURE = FIXTURE_ROOT / "valid" / "non_sensitive_occurrence.json"
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

    def test_fixture_corpus_contains_no_live_urls_or_numeric_coordinates(self):
        for fixture_path in (VALID_FIXTURE, *INVALID_FIXTURES):
            with self.subTest(fixture=fixture_path.name):
                payload = json.loads(fixture_path.read_text(encoding="utf-8"))
                serialized = json.dumps(payload, sort_keys=True).lower()
                self.assertNotIn("http://", serialized)
                self.assertNotIn("https://", serialized)

                spatial_support = payload["spatial_support"]
                for field in ("latitude", "longitude", "coordinates"):
                    value = spatial_support.get(field)
                    self.assertFalse(
                        isinstance(value, (int, float, list)),
                        f"{fixture_path.name} contains numeric {field}",
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


if __name__ == "__main__":
    unittest.main()
