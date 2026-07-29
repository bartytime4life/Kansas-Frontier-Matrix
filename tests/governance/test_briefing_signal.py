"""Deterministic no-network tests for the BriefingSignal intake boundary."""

from __future__ import annotations

import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.governance.validate_briefing_signal import main, validate_file


REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_ROOT = REPO_ROOT / "fixtures" / "contracts" / "v1" / "governance" / "briefing_signal"
VALID_FIXTURE = FIXTURE_ROOT / "valid" / "valid_1.json"
INVALID_FIXTURES = {
    FIXTURE_ROOT / "invalid" / "invalid_public_use.json": {
        ("BRIEFING_SIGNAL_SCHEMA_INVALID", "$.next_action.repository_mutation_allowed"),
        ("BRIEFING_SIGNAL_SCHEMA_INVALID", "$.permissions.publication"),
        ("BRIEFING_SIGNAL_SCHEMA_INVALID", "$.public_use_allowed"),
        ("CONSEQUENTIAL_PERMISSION_FORBIDDEN", "$.permissions.publication"),
        (
            "REPOSITORY_MUTATION_PERMISSION_FORBIDDEN",
            "$.next_action.repository_mutation_allowed",
        ),
        ("PUBLIC_USE_MUST_REMAIN_FALSE", "$.public_use_allowed"),
    },
    FIXTURE_ROOT / "invalid" / "invalid_missing_evidence.json": {
        ("BRIEFING_SIGNAL_SCHEMA_INVALID", "$.claims.0.evidence_refs"),
        ("CONFIRMED_CLAIM_WITHOUT_EVIDENCE", "$.claims.0.evidence_refs"),
    },
    FIXTURE_ROOT / "invalid" / "invalid_inline_geometry.json": {
        (
            "INLINE_GEOMETRY_FORBIDDEN",
            "$.candidate_payload.attributes.coordinates",
        ),
    },
}
EXAMPLE_ROOT = REPO_ROOT / "examples" / "briefing_integration"
EXAMPLES = {
    EXAMPLE_ROOT / "hays_water_local_consult_2026_07_29.json",
    EXAMPLE_ROOT / "gmd_action_plan_inventory_2026_07_29.json",
}


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("BriefingSignal validation attempted network access")


class BriefingSignalTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_valid_fixture_passes(self):
        self.assertEqual(validate_file(VALID_FIXTURE), ())

    def test_invalid_fixtures_produce_stable_findings(self):
        for fixture_path, expected_findings in INVALID_FIXTURES.items():
            with self.subTest(fixture=fixture_path.name):
                findings = validate_file(fixture_path)
                actual = {(finding.code, finding.path) for finding in findings}
                self.assertEqual(actual, expected_findings)

    def test_real_source_examples_remain_non_authoritative(self):
        self.assertEqual(set(EXAMPLE_ROOT.glob("*.json")), EXAMPLES)
        for example_path in EXAMPLES:
            with self.subTest(example=example_path.name):
                self.assertEqual(validate_file(example_path), ())
                payload = json.loads(example_path.read_text(encoding="utf-8"))
                self.assertFalse(payload["public_use_allowed"])
                self.assertFalse(
                    payload["next_action"]["repository_mutation_allowed"]
                )
                self.assertTrue(
                    all(value is False for value in payload["permissions"].values())
                )

    def test_hays_candidate_does_not_claim_the_meeting_occurred(self):
        payload = json.loads(
            (EXAMPLE_ROOT / "hays_water_local_consult_2026_07_29.json").read_text(
                encoding="utf-8"
            )
        )
        attributes = payload["candidate_payload"]["attributes"]
        self.assertEqual(payload["candidate_payload"]["candidate_state"], "STATUS_UNCONFIRMED")
        self.assertEqual(attributes["observed_event_state"], "status_unconfirmed")
        self.assertIsNone(attributes["venue_geometry_ref"])
        self.assertIsNone(attributes["regional_scope_ref"])

    def test_gmd_inventory_does_not_infer_approval_or_non_submission(self):
        payload = json.loads(
            (EXAMPLE_ROOT / "gmd_action_plan_inventory_2026_07_29.json").read_text(
                encoding="utf-8"
            )
        )
        records = payload["candidate_payload"]["attributes"]["records"]
        self.assertEqual(len(records), 5)
        for record in records:
            self.assertIn(record["approval_status"], {"UNKNOWN"})
            self.assertIn(record["implementation_status"], {"UNKNOWN"})
            self.assertIsNone(record["district_geometry_ref"])
            self.assertIsNone(record["priority_area_geometry_ref"])
        gmd1 = next(record for record in records if record["district_id"] == "ks-gmd-1")
        self.assertEqual(gmd1["action_plan_index_state"], "NOT_LISTED_ON_AUTHORITY_INDEX")
        self.assertEqual(gmd1["submission_status"], "UNKNOWN")

    def test_cli_output_is_deterministic_and_does_not_echo_claim_text(self):
        fixture = FIXTURE_ROOT / "invalid" / "invalid_public_use.json"
        outputs = []
        for _ in range(2):
            stream = io.StringIO()
            with redirect_stdout(stream):
                return_code = main([str(fixture)])
            self.assertEqual(return_code, 1)
            outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn("Synthetic governance event signal", outputs[0])


if __name__ == "__main__":
    unittest.main()
