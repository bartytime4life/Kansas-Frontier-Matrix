#!/usr/bin/env python3
"""Deterministic no-network tests for the BriefingSignal intake boundary."""
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

from jsonschema import Draft202012Validator

from tools.validators.governance.validate_briefing_signal import (
    Finding,
    compute_event_cluster_id,
    compute_issue_idempotency_key,
    compute_signal_digest,
    compute_signal_id,
    main,
    validate_candidate,
    validate_file,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/briefing_signal"
VALID_FIXTURES = {
    FIXTURE_ROOT / "valid/valid_1.json",
    FIXTURE_ROOT / "valid/valid_duplicate_followup.json",
}
INVALID_FIXTURES = {
    FIXTURE_ROOT / "invalid/invalid_public_use.json": {
        ("BRIEFING_SIGNAL_SCHEMA_INVALID", "$.next_action.repository_mutation_allowed"),
        ("BRIEFING_SIGNAL_SCHEMA_INVALID", "$.permissions.publication"),
        ("BRIEFING_SIGNAL_SCHEMA_INVALID", "$.public_use_allowed"),
        ("CONSEQUENTIAL_PERMISSION_FORBIDDEN", "$.permissions.publication"),
        ("PUBLIC_USE_MUST_REMAIN_FALSE", "$.public_use_allowed"),
        ("REPOSITORY_MUTATION_PERMISSION_FORBIDDEN", "$.next_action.repository_mutation_allowed"),
    },
    FIXTURE_ROOT / "invalid/invalid_missing_evidence.json": {
        ("BRIEFING_SIGNAL_SCHEMA_INVALID", "$.claims.0.evidence_refs"),
        ("CONFIRMED_CLAIM_WITHOUT_EVIDENCE", "$.claims.0.evidence_refs"),
    },
    FIXTURE_ROOT / "invalid/invalid_inline_geometry.json": {
        ("BRIEFING_SIGNAL_SCHEMA_INVALID", "$.candidate_payload.attributes"),
        ("INLINE_GEOMETRY_FORBIDDEN", "$.candidate_payload.attributes.coordinates"),
    },
    FIXTURE_ROOT / "invalid/invalid_duplicate_issue_create.json": {
        ("DUPLICATE_CANNOT_OPEN_ISSUE", "$.next_action.disposition"),
    },
}
EXAMPLE_ROOT = REPO_ROOT / "examples/briefing_integration"
EXAMPLES = {
    EXAMPLE_ROOT / "hays_water_local_consult_2026_07_29.json",
    EXAMPLE_ROOT / "gmd_action_plan_inventory_2026_07_29.json",
}
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/briefing_signal.schema.json"


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("BriefingSignal validation attempted network access")


class BriefingSignalTests(unittest.TestCase):
    def setUp(self):
        self.network_mocks = []
        for patcher in (
            patch.object(socket.socket, "connect", side_effect=_unexpected_network),
            patch.object(socket.socket, "connect_ex", side_effect=_unexpected_network),
            patch.object(socket, "create_connection", side_effect=_unexpected_network),
            patch.object(socket, "getaddrinfo", side_effect=_unexpected_network),
            patch.object(urllib.request, "urlopen", side_effect=_unexpected_network),
        ):
            self.network_mocks.append(patcher.start())
            self.addCleanup(patcher.stop)

    def test_schema_is_closed_and_valid(self):
        schema = _load(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["$defs"]["claim"]["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["profile_version"], "1.1.0")

    def test_valid_fixture_inventory_and_examples_pass(self):
        self.assertEqual(set((FIXTURE_ROOT / "valid").glob("*.json")), VALID_FIXTURES)
        self.assertEqual(set(EXAMPLE_ROOT.glob("*.json")), EXAMPLES)
        for path in sorted(VALID_FIXTURES | EXAMPLES):
            with self.subTest(path=path.name):
                self.assertEqual(validate_file(path), ())

    def test_invalid_fixtures_produce_exact_stable_findings(self):
        self.assertEqual(set((FIXTURE_ROOT / "invalid").glob("*.json")), set(INVALID_FIXTURES))
        for path, expected in INVALID_FIXTURES.items():
            with self.subTest(path=path.name):
                findings = validate_file(path)
                self.assertEqual(
                    {(finding.code, finding.path) for finding in findings}, expected
                )
                self.assertEqual(tuple(findings), tuple(sorted(findings)))

    def test_declared_identity_reproduces_for_all_valid_inputs(self):
        for path in sorted(VALID_FIXTURES | EXAMPLES):
            candidate = _load(path)
            with self.subTest(path=path.name):
                self.assertEqual(candidate["identity"]["signal_digest"], compute_signal_digest(candidate))
                self.assertEqual(candidate["signal_id"], compute_signal_id(candidate))
                self.assertEqual(candidate["event_cluster_id"], compute_event_cluster_id(candidate))
                self.assertEqual(
                    candidate["next_action"]["idempotency_key"],
                    compute_issue_idempotency_key(candidate),
                )

    def test_object_and_unordered_array_reordering_is_identity_stable(self):
        candidate = _load(FIXTURE_ROOT / "valid/valid_1.json")
        expected = compute_signal_digest(candidate)
        reordered = dict(reversed(list(copy.deepcopy(candidate).items())))
        reordered["domains"] = list(reversed(reordered["domains"]))
        reordered["claims"] = list(reversed(reordered["claims"]))
        reordered["official_source_candidates"] = list(
            reversed(reordered["official_source_candidates"])
        )
        self.assertEqual(compute_signal_digest(reordered), expected)

    def test_substantive_headline_change_changes_signal_not_cluster(self):
        candidate = _load(FIXTURE_ROOT / "valid/valid_1.json")
        changed = copy.deepcopy(candidate)
        changed["headline"] = "A materially revised orientation headline"
        self.assertNotEqual(compute_signal_id(changed), candidate["signal_id"])
        self.assertEqual(compute_event_cluster_id(changed), candidate["event_cluster_id"])

    def test_identity_token_drift_and_digest_tampering_fail(self):
        candidate = _load(FIXTURE_ROOT / "valid/valid_1.json")
        candidate["identity"]["primary_authority_id"] = "Fixture Authority"
        candidate["identity"]["signal_digest"] = "sha256:" + "0" * 64
        findings = validate_candidate(candidate)
        self.assertIn(
            Finding("IDENTITY_TOKEN_NOT_NORMALIZED", "$.identity.primary_authority_id"),
            findings,
        )
        self.assertIn(Finding("SIGNAL_DIGEST_MISMATCH", "$.identity.signal_digest"), findings)
        self.assertIn(Finding("EVENT_CLUSTER_ID_MISMATCH", "$.event_cluster_id"), findings)

    def test_examples_remain_non_authoritative_and_issue_idempotent(self):
        for path in sorted(EXAMPLES):
            payload = _load(path)
            with self.subTest(path=path.name):
                self.assertFalse(payload["public_use_allowed"])
                self.assertFalse(payload["next_action"]["repository_mutation_allowed"])
                self.assertTrue(all(value is False for value in payload["permissions"].values()))
                self.assertEqual(payload["status"], "DUPLICATE")
                self.assertEqual(payload["deduplication"]["status"], "DUPLICATE")
                self.assertEqual(payload["deduplication"]["matched_issue_ids"], [1647])
                self.assertEqual(payload["next_action"]["disposition"], "UPDATE_EXISTING_ISSUE")

    def test_hays_candidate_does_not_claim_the_meeting_occurred(self):
        payload = _load(EXAMPLE_ROOT / "hays_water_local_consult_2026_07_29.json")
        attributes = payload["candidate_payload"]["attributes"]
        self.assertEqual(payload["candidate_payload"]["candidate_state"], "STATUS_UNCONFIRMED")
        self.assertEqual(attributes["observed_event_state"], "status_unconfirmed")
        self.assertIsNone(attributes["venue_geometry_ref"])
        self.assertIsNone(attributes["regional_scope_ref"])

    def test_gmd_inventory_does_not_infer_approval_or_non_submission(self):
        payload = _load(EXAMPLE_ROOT / "gmd_action_plan_inventory_2026_07_29.json")
        records = payload["candidate_payload"]["attributes"]["records"]
        self.assertEqual(len(records), 5)
        for record in records:
            self.assertEqual(record["approval_status"], "UNKNOWN")
            self.assertEqual(record["implementation_status"], "UNKNOWN")
            self.assertIsNone(record["district_geometry_ref"])
            self.assertIsNone(record["priority_area_geometry_ref"])
        gmd1 = next(record for record in records if record["district_id"] == "ks-gmd-1")
        self.assertEqual(gmd1["action_plan_index_state"], "NOT_LISTED_ON_AUTHORITY_INDEX")
        self.assertEqual(gmd1["submission_status"], "UNKNOWN")

    def test_parser_rejects_duplicate_nonfinite_and_nonobject_json(self):
        cases = (
            (b'{"signal_id":"a","signal_id":"b"}', Finding("BRIEFING_SIGNAL_JSON_INVALID", "$")),
            (b'{"score":NaN}', Finding("BRIEFING_SIGNAL_JSON_INVALID", "$")),
            (b"[]", Finding("DOCUMENT_NOT_OBJECT", "$")),
        )
        with tempfile.TemporaryDirectory() as directory:
            for index, (content, expected) in enumerate(cases):
                path = Path(directory) / f"case-{index}.json"
                path.write_bytes(content)
                with self.subTest(index=index):
                    self.assertEqual(validate_file(path), (expected,))

    def test_cli_output_is_deterministic_and_value_free(self):
        fixture = FIXTURE_ROOT / "invalid/invalid_public_use.json"
        outputs = []
        for _ in range(2):
            stream = io.StringIO()
            with redirect_stdout(stream):
                return_code = main([str(fixture)])
            self.assertEqual(return_code, 1)
            outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn("Synthetic governance event signal", outputs[0])
        self.assertIn('"authority_created":false', outputs[0])

    def test_validation_never_attempts_network_access(self):
        for path in sorted(VALID_FIXTURES | EXAMPLES | set(INVALID_FIXTURES)):
            validate_file(path)
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
