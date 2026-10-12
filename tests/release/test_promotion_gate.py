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

from tools.validators.promotion_gate.validate_promotion_gate import (
    FIXTURES_ROOT,
    result_payload,
    validate_candidate_file,
    validate_document,
)


ROOT = Path(__file__).resolve().parents[2]
VALID_FIXTURE = FIXTURES_ROOT / "valid/pass__complete_candidate.json"
ROOT_CLI = ROOT / "tools/validators/validate_promotion_gate.py"


def load_valid() -> dict[str, object]:
    return json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))


def finding_codes(candidate: object) -> set[str]:
    return {finding.code for finding in validate_document(candidate)}


class PromotionGateTests(unittest.TestCase):
    def test_complete_candidate_is_only_approve_ready(self) -> None:
        findings = validate_candidate_file(VALID_FIXTURE)
        self.assertEqual(findings, [])
        payload = result_payload(VALID_FIXTURE, findings)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["readiness"], "APPROVE_READY")
        self.assertEqual(
            payload["gates"],
            [{"gate": gate, "status": "PASS"} for gate in "ABCDEFG"],
        )
        payload_text = json.dumps(payload)
        for forbidden in ("APPROVED", "PROMOTED", "RELEASED", "PUBLISHED"):
            self.assertNotIn(forbidden, payload_text)

    def test_repository_fixture_matrix_has_exact_outcomes(self) -> None:
        expected = {
            "abstain__missing_evidence_ref.json": (
                "ABSTAIN",
                {"PG_F_EVIDENCE_REF_MISSING"},
            ),
            "abstain__review_authority_missing.json": (
                "ABSTAIN",
                {"PG_G_REVIEW_AUTHORITY_MISSING"},
            ),
            "abstain__review_obligations_open.json": (
                "ABSTAIN",
                {"PG_G_REVIEW_OBLIGATIONS_OPEN"},
            ),
            "deny__artifact_set_mismatch.json": (
                "DENY",
                {"PG_B_ARTIFACT_SET_MISMATCH"},
            ),
            "deny__invalid_geometry.json": (
                "DENY",
                {"PG_C_GEOMETRY_INVALID"},
            ),
            "deny__missing_candidate_id.json": (
                "DENY",
                {
                    "PG_A_CANDIDATE_ID_MISSING",
                    "PG_G_REVIEW_CONTEXT_INVALID",
                },
            ),
            "deny__review_missing.json": (
                "DENY",
                {"PG_G_REVIEW_NOT_APPROVED"},
            ),
            "deny__review_artifact_hash_unbound.json": (
                "DENY",
                {"PG_G_REVIEW_ARTIFACT_HASH_UNBOUND"},
            ),
            "deny__review_authority_expired.json": (
                "DENY",
                {"PG_G_REVIEW_AUTHORITY_NOT_CURRENT"},
            ),
            "deny__review_scope_mismatch.json": (
                "DENY",
                {"PG_G_REVIEW_SCOPE_MISMATCH"},
            ),
            "deny__review_self.json": (
                "DENY",
                {"PG_G_SEPARATION_OF_DUTIES_INVALID"},
            ),
            "deny__review_spec_hash_unbound.json": (
                "DENY",
                {"PG_G_REVIEW_SPEC_HASH_UNBOUND"},
            ),
            "deny__review_stale.json": (
                "DENY",
                {"PG_G_REVIEW_STALE"},
            ),
            "deny__review_superseded.json": (
                "DENY",
                {"PG_G_REVIEW_SUPERSEDED"},
            ),
            "deny__unknown_policy_label.json": (
                "DENY",
                {"PG_E_POLICY_LABEL_UNKNOWN"},
            ),
            "error__malformed_json.json": (
                "ERROR",
                {"FIXTURE_JSON_INVALID"},
            ),
            "error__policy_evaluation.json": (
                "ERROR",
                {"PG_E_POLICY_EVALUATION_ERROR"},
            ),
            "pass__complete_candidate.json": ("PASS", set()),
        }
        files = sorted(FIXTURES_ROOT.glob("*/*.json"))
        self.assertEqual({path.name for path in files}, set(expected))
        for path in files:
            with self.subTest(path=path.name):
                findings = validate_candidate_file(path)
                payload = result_payload(path, findings)
                self.assertEqual(payload["status"], expected[path.name][0])
                self.assertEqual(
                    {finding.code for finding in findings}, expected[path.name][1]
                )

    def test_ai_mediation_requires_separate_receipt(self) -> None:
        candidate = load_valid()
        candidate["ai_mediation"] = {"used": True, "receipt_ref": None}
        self.assertEqual(finding_codes(candidate), {"PG_F_AI_RECEIPT_MISSING"})

    def test_supersession_without_correction_link_abstains(self) -> None:
        candidate = load_valid()
        candidate["correction"] = {"supersedes_prior": True, "notice_ref": None}
        findings = validate_document(candidate)
        self.assertEqual(
            {finding.code for finding in findings},
            {"PG_G_CORRECTION_LINK_MISSING"},
        )
        self.assertEqual(result_payload("candidate.json", findings)["status"], "ABSTAIN")

    def test_author_cannot_be_the_recorded_reviewer(self) -> None:
        candidate = load_valid()
        review = copy.deepcopy(candidate["review"])
        assert isinstance(review, dict)
        reviewer_identity = review["reviewer_identity"]
        authority = review["authority"]
        assert isinstance(reviewer_identity, dict)
        assert isinstance(authority, dict)
        reviewer_identity["id"] = candidate["candidate_author"]
        authority["assigned_to"] = candidate["candidate_author"]
        candidate["review"] = review
        self.assertEqual(
            finding_codes(candidate), {"PG_G_SEPARATION_OF_DUTIES_INVALID"}
        )

    def test_actor_padding_cannot_bypass_separation(self) -> None:
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
        self.assertEqual(
            finding_codes(candidate),
            {"PG_G_REVIEW_AUTHORITY_INVALID", "PG_G_REVIEW_INVALID"},
        )

    def test_identity_issued_after_review_is_denied(self) -> None:
        candidate = load_valid()
        review = copy.deepcopy(candidate["review"])
        assert isinstance(review, dict)
        reviewer_identity = review["reviewer_identity"]
        assert isinstance(reviewer_identity, dict)
        reviewer_identity["issued_at"] = "2026-04-14T00:00:00Z"
        candidate["review"] = review
        self.assertEqual(
            finding_codes(candidate), {"PG_G_REVIEW_IDENTITY_NOT_CURRENT"}
        )

    def test_outcome_precedence_remains_error_deny_abstain_pass(self) -> None:
        candidate = load_valid()
        candidate["evidence_refs"] = []
        review = copy.deepcopy(candidate["review"])
        assert isinstance(review, dict)
        review["authority"] = None
        candidate["review"] = review
        findings = validate_document(candidate)
        self.assertEqual(result_payload("candidate.json", findings)["status"], "ABSTAIN")

        reviewer_identity = review["reviewer_identity"]
        assert isinstance(reviewer_identity, dict)
        reviewer_identity["id"] = candidate["candidate_author"]
        candidate["review"] = review
        findings = validate_document(candidate)
        self.assertEqual(result_payload("candidate.json", findings)["status"], "DENY")

        policy_context = copy.deepcopy(candidate["policy_context"])
        assert isinstance(policy_context, dict)
        policy_context["evaluation"] = "ERROR"
        candidate["policy_context"] = policy_context
        findings = validate_document(candidate)
        self.assertEqual(result_payload("candidate.json", findings)["status"], "ERROR")

    def test_equal_temporal_boundary_is_valid(self) -> None:
        candidate = load_valid()
        candidate["temporal"] = {
            "start": "2026-04-13T00:00:00Z",
            "end": "2026-04-13T00:00:00Z",
        }
        self.assertEqual(validate_document(candidate), [])

    def test_impossible_utc_timestamp_is_denied(self) -> None:
        candidate = load_valid()
        candidate["temporal"] = {
            "start": "2026-02-30T00:00:00Z",
            "end": "2026-04-13T00:00:00Z",
        }
        self.assertEqual(finding_codes(candidate), {"PG_D_TEMPORAL_INVALID"})

    def test_timestamp_spelling_must_be_canonical_utc_seconds(self) -> None:
        for value in (
            "2026-4-13T01:00:00Z",
            "2026-04-13t01:00:00Z",
            "2026-04-13T01:00:00z",
        ):
            candidate = load_valid()
            candidate["gate_evaluated_at"] = value
            with self.subTest(value=value):
                self.assertEqual(
                    finding_codes(candidate),
                    {
                        "PG_D_GATE_EVALUATED_AT_INVALID",
                        "PG_G_REVIEW_CONTEXT_INVALID",
                    },
                )

    def test_gate_g_cannot_pass_when_review_context_is_unavailable(self) -> None:
        candidate = load_valid()
        candidate["candidate_id"] = ""
        findings = validate_document(candidate)
        payload = result_payload("candidate.json", findings)
        self.assertEqual(
            {finding.code for finding in findings},
            {"PG_A_CANDIDATE_ID_MISSING", "PG_G_REVIEW_CONTEXT_INVALID"},
        )
        self.assertEqual(payload["gates"][-1], {"gate": "G", "status": "DENY"})

    def test_result_does_not_echo_caller_controlled_path(self) -> None:
        payload = result_payload(
            Path("DO-NOT-ECHO") / "DO-NOT-ECHO.json",
            [],
        )
        self.assertEqual(payload["file"], "external-input")
        self.assertNotIn("DO-NOT-ECHO", json.dumps(payload))

    def test_gate_g_declared_expiry_instants_are_exclusive(self) -> None:
        cases = (
            ("authority", "expires_at", "PG_G_REVIEW_AUTHORITY_NOT_CURRENT"),
            ("review", "valid_until", "PG_G_REVIEW_STALE"),
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
                self.assertIn(expected_code, finding_codes(candidate))

    def test_symlink_loop_is_finite_error_with_redacted_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "DO-NOT-ECHO.json"
            path.symlink_to(path.name)
            result = subprocess.run(
                [sys.executable, str(ROOT_CLI), str(path)],
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

    def test_duplicate_json_keys_fail_as_error_without_echoing_values(self) -> None:
        sentinel = "DO-NOT-ECHO-SYNTHETIC-SENTINEL"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(
                '{"candidate_id":"first","candidate_id":"'
                + sentinel
                + '"}',
                encoding="utf-8",
            )
            findings = validate_candidate_file(path)
            payload_text = json.dumps(result_payload(path, findings), sort_keys=True)
        self.assertEqual({finding.code for finding in findings}, {"FIXTURE_JSON_INVALID"})
        self.assertNotIn(sentinel, payload_text)

    def test_unknown_field_is_gate_local_without_echoing_untrusted_key(self) -> None:
        sentinel = "DO-NOT-ECHO-UNKNOWN-FIELD-SENTINEL"
        candidate = load_valid()
        review = copy.deepcopy(candidate["review"])
        assert isinstance(review, dict)
        review[sentinel] = "synthetic-value"
        candidate["review"] = review
        findings = validate_document(candidate)
        payload_text = json.dumps(
            result_payload("candidate.json", findings), sort_keys=True
        )
        self.assertEqual(
            {finding.code for finding in findings}, {"PG_G_UNDECLARED_FIELD"}
        )
        self.assertNotIn(sentinel, payload_text)

    def test_validation_uses_no_network(self) -> None:
        with mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network access is forbidden"),
        ):
            self.assertEqual(validate_candidate_file(VALID_FIXTURE), [])

    def test_cli_exit_codes_and_deterministic_json(self) -> None:
        cases = (
            (VALID_FIXTURE, 0, "PASS"),
            (
                FIXTURES_ROOT / "invalid/deny__artifact_set_mismatch.json",
                1,
                "DENY",
            ),
            (FIXTURES_ROOT / "invalid/error__malformed_json.json", 2, "ERROR"),
        )
        for path, expected_code, expected_status in cases:
            with self.subTest(path=path.name):
                command = [sys.executable, str(ROOT_CLI), str(path)]
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
