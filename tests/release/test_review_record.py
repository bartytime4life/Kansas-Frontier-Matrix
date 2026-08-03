from __future__ import annotations

import json
import socket
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.validate_review_record import (
    FIXTURES_ROOT,
    result_payload,
    validate_packet_file,
)


ROOT = Path(__file__).resolve().parents[2]
VALID_FIXTURE = FIXTURES_ROOT / "valid/pass__complete_candidate.json"
CLI = ROOT / "tools/validators/validate_review_record.py"


class ReviewRecordFixtureProfileTests(unittest.TestCase):
    def test_exact_positive_and_negative_fixture_outcomes(self) -> None:
        expected = {
            "pass__complete_candidate.json": ("PASS", set()),
            "abstain__review_authority_missing.json": (
                "ABSTAIN",
                {"RR_AUTHORITY_MISSING"},
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
