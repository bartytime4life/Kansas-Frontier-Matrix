from __future__ import annotations

import copy
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.validate_review_record import (
    FIXTURES_ROOT,
    result_payload,
    validate_packet_file,
    validate_packet_document,
)


ROOT = Path(__file__).resolve().parents[2]
VALID_FIXTURE = FIXTURES_ROOT / "valid/pass__complete_candidate.json"
CLI = ROOT / "tools/validators/validate_review_record.py"


def load_valid() -> dict[str, object]:
    return json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))


class ReviewRecordFixtureProfileTests(unittest.TestCase):
    def test_exact_positive_and_negative_fixture_outcomes(self) -> None:
        expected = {
            "pass__complete_candidate.json": ("PASS", set()),
            "abstain__review_authority_missing.json": (
                "ABSTAIN",
                {"RR_AUTHORITY_MISSING"},
            ),
            "abstain__review_obligations_open.json": (
                "ABSTAIN",
                {"RR_OBLIGATIONS_OPEN"},
            ),
            "deny__review_authority_expired.json": (
                "DENY",
                {"RR_AUTHORITY_NOT_CURRENT"},
            ),
            "deny__review_artifact_hash_unbound.json": (
                "DENY",
                {"RR_ARTIFACT_HASH_UNBOUND"},
            ),
            "deny__review_missing.json": (
                "DENY",
                {"RR_DECISION_NOT_APPROVED"},
            ),
            "deny__review_scope_mismatch.json": (
                "DENY",
                {"RR_SCOPE_MISMATCH"},
            ),
            "deny__review_self.json": ("DENY", {"RR_SELF_REVIEW"}),
            "deny__review_spec_hash_unbound.json": (
                "DENY",
                {"RR_SPEC_HASH_UNBOUND"},
            ),
            "deny__review_stale.json": ("DENY", {"RR_REVIEW_STALE"}),
            "deny__review_superseded.json": (
                "DENY",
                {"RR_REVIEW_SUPERSEDED"},
            ),
        }
        files = [VALID_FIXTURE]
        files.extend(sorted((FIXTURES_ROOT / "invalid").glob("*review*.json")))
        self.assertEqual({path.name for path in files}, set(expected))
        for path in files:
            with self.subTest(path=path.name):
                findings = validate_packet_file(path)
                payload = result_payload(path, findings)
                self.assertEqual(payload["status"], expected[path.name][0])
                self.assertEqual(
                    {finding.code for finding in findings}, expected[path.name][1]
                )

    def test_fixture_validation_uses_no_network(self) -> None:
        with mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network access is forbidden"),
        ):
            self.assertEqual(validate_packet_file(VALID_FIXTURE), [])

    def test_result_is_value_free_and_never_emits_governed_state(self) -> None:
        path = FIXTURES_ROOT / "invalid/deny__review_scope_mismatch.json"
        payload_text = json.dumps(result_payload(path, validate_packet_file(path)))
        self.assertNotIn("release.other_gate", payload_text)
        for forbidden in ("APPROVED", "PROMOTED", "RELEASED", "PUBLISHED"):
            self.assertNotIn(forbidden, payload_text)
        self.assertFalse(json.loads(payload_text)["authoritative"])

    def test_actor_ids_are_canonical_before_separation_comparison(self) -> None:
        candidate = load_valid()
        review = copy.deepcopy(candidate["review"])
        assert isinstance(review, dict)
        reviewer_identity = review["reviewer_identity"]
        authority = review["authority"]
        assert isinstance(reviewer_identity, dict)
        assert isinstance(authority, dict)
        reviewer_identity["id"] = " actor:synthetic-author"
        authority["assigned_to"] = " actor:synthetic-author"
        candidate["review"] = review
        findings = validate_packet_document(candidate)
        self.assertEqual(
            {finding.code for finding in findings},
            {"RR_AUTHORITY_INVALID", "RR_IDENTITY_INVALID"},
        )

    def test_identity_must_exist_by_review_time(self) -> None:
        candidate = load_valid()
        review = copy.deepcopy(candidate["review"])
        assert isinstance(review, dict)
        reviewer_identity = review["reviewer_identity"]
        assert isinstance(reviewer_identity, dict)
        reviewer_identity["issued_at"] = "2026-04-14T00:00:00Z"
        candidate["review"] = review
        findings = validate_packet_document(candidate)
        self.assertEqual(
            {finding.code for finding in findings}, {"RR_IDENTITY_NOT_CURRENT"}
        )

    def test_review_timestamps_require_canonical_utc_seconds(self) -> None:
        for value in (
            "2026-4-13T00:30:00Z",
            "2026-04-13t00:30:00Z",
            "2026-04-13T00:30:00z",
        ):
            candidate = load_valid()
            review = copy.deepcopy(candidate["review"])
            assert isinstance(review, dict)
            record = review["record"]
            assert isinstance(record, dict)
            record["reviewed_at"] = value
            candidate["review"] = review
            with self.subTest(value=value):
                self.assertIn(
                    "RR_RECORD_INVALID",
                    {finding.code for finding in validate_packet_document(candidate)},
                )

    def test_result_does_not_echo_caller_controlled_path(self) -> None:
        payload = result_payload(Path("DO-NOT-ECHO") / "DO-NOT-ECHO.json", [])
        self.assertEqual(payload["file"], "external-input")
        self.assertNotIn("DO-NOT-ECHO", json.dumps(payload))

    def test_supersession_marker_must_be_explicit(self) -> None:
        candidate = load_valid()
        review = copy.deepcopy(candidate["review"])
        assert isinstance(review, dict)
        review.pop("superseded_by_review_id")
        candidate["review"] = review
        self.assertEqual(
            {finding.code for finding in validate_packet_document(candidate)},
            {"RR_RECORD_INVALID"},
        )

    def test_declared_expiry_instants_are_exclusive(self) -> None:
        cases = (
            ("authority", "expires_at", "RR_AUTHORITY_NOT_CURRENT"),
            ("review", "valid_until", "RR_REVIEW_STALE"),
        )
        for target, field, expected_code in cases:
            candidate = load_valid()
            review = copy.deepcopy(candidate["review"])
            assert isinstance(review, dict)
            if target == "authority":
                authority = review["authority"]
                assert isinstance(authority, dict)
                authority[field] = candidate["gate_evaluated_at"]
            else:
                review[field] = candidate["gate_evaluated_at"]
            candidate["review"] = review
            with self.subTest(target=target):
                self.assertIn(
                    expected_code,
                    {finding.code for finding in validate_packet_document(candidate)},
                )

    def test_symlink_loop_is_finite_error_with_redacted_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "DO-NOT-ECHO.json"
            path.symlink_to(path.name)
            result = subprocess.run(
                [sys.executable, str(CLI), str(path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(result.returncode, 2, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["file"], "external-input")
        self.assertEqual(payload["status"], "ERROR")
        self.assertEqual(
            {finding["code"] for finding in payload["findings"]},
            {"FIXTURE_JSON_INVALID"},
        )
        self.assertNotIn("DO-NOT-ECHO", result.stdout)

    def test_cli_is_deterministic_with_finite_exit_codes(self) -> None:
        cases = (
            (VALID_FIXTURE, 0, "PASS"),
            (
                FIXTURES_ROOT / "invalid/abstain__review_authority_missing.json",
                1,
                "ABSTAIN",
            ),
            (FIXTURES_ROOT / "invalid/deny__review_self.json", 1, "DENY"),
        )
        for path, expected_code, expected_status in cases:
            with self.subTest(path=path.name):
                command = [sys.executable, str(CLI), str(path)]
                first = subprocess.run(
                    command,
                    cwd=ROOT,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                second = subprocess.run(
                    command,
                    cwd=ROOT,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(first.returncode, expected_code, first.stderr)
                self.assertEqual(first.stdout, second.stdout)
                self.assertEqual(json.loads(first.stdout)["status"], expected_status)


if __name__ == "__main__":
    unittest.main()
