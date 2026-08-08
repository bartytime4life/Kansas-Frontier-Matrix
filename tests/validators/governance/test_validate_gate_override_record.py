"""Deterministic no-network tests for gate override record candidates."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.governance.gate_override_record_core import (
    SCHEMA_PATH,
    refresh_identity,
    validate_document,
)
from tools.validators.governance.validate_gate_override_record import (
    load_fixture_cases,
    main,
    run_fixture_suite,
    validate_file,
)


def _deny_network(*_args, **_kwargs):
    raise AssertionError("network access attempted")


class GateOverrideRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases, findings = load_fixture_cases()
        assert not findings, findings
        cls.by_id = {case["case_id"]: case for case in cls.cases}

    def document(self, case_id: str) -> dict[str, object]:
        return copy.deepcopy(self.by_id[case_id]["document"])

    def test_schema_is_closed_fixture_only_and_no_authority(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual("PROPOSED_INACTIVE", schema["properties"]["status"]["const"])
        self.assertEqual("FIXTURE_ONLY", schema["properties"]["execution_mode"]["const"])
        claims = schema["$defs"]["claims"]
        self.assertFalse(claims["additionalProperties"])
        self.assertTrue(all(item["const"] is False for item in claims["properties"].values()))
        self.assertFalse(schema["$defs"]["attestation"]["properties"]["production_signature_verified"]["const"])

    def test_exact_fixture_outcomes_and_findings(self) -> None:
        self.assertEqual(14, len(self.cases))
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                result = validate_document(case["document"])
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_runner_reports_finite_no_authority_boundary(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(
            {"PASS": 1, "HOLD": 3, "DENY": 7, "ERROR": 3},
            payload["counts"],
        )
        self.assertEqual("NONE", payload["authority"])
        self.assertIn("no_gate_bypass", payload["non_effects"])
        self.assertIn(
            "no_promotion_release_deployment_or_publication",
            payload["non_effects"],
        )

    def test_actor_separation_support_and_temporal_rules(self) -> None:
        expectations = {
            "hold_missing_policy_decision": ("HOLD", "OVERRIDE_SUPPORT_INCOMPLETE"),
            "deny_self_approval": ("DENY", "OVERRIDE_SELF_APPROVAL_DENIED"),
            "deny_signer_approver_mismatch": ("DENY", "OVERRIDE_SIGNER_APPROVER_MISMATCH"),
            "error_expires_before_valid": ("ERROR", "OVERRIDE_VALIDITY_INTERVAL_INVALID"),
            "error_remediation_due_before_created": ("ERROR", "OVERRIDE_REMEDIATION_DUE_INVALID"),
        }
        for case_id, (outcome, code) in expectations.items():
            with self.subTest(case=case_id):
                result = validate_document(self.document(case_id))
                self.assertEqual(outcome, result.outcome)
                self.assertIn(code, {finding.code for finding in result.findings})

    def test_identity_and_fixture_attestation_are_deterministic(self) -> None:
        first = self.document("valid_complete_candidate")
        second = copy.deepcopy(first)
        refresh_identity(first)
        refresh_identity(second)
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        self.assertEqual(first["override_id"], second["override_id"])
        self.assertEqual(first["attestation"], second["attestation"])
        self.assertEqual("PASS", validate_document(first).outcome)

    def test_no_network_deterministic_non_echoing_output(self) -> None:
        candidate = self.document("valid_complete_candidate")
        with mock.patch.object(socket.socket, "connect", _deny_network), mock.patch.object(
            socket, "create_connection", _deny_network
        ), mock.patch.object(urllib.request, "urlopen", _deny_network):
            self.assertEqual("PASS", validate_document(candidate).outcome)
        marker = "sensitive-marker-must-not-echo"
        candidate["rationale"]["summary"] = marker
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            outputs = []
            for _ in range(2):
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    self.assertEqual(1, main([str(path)]))
                outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(marker, outputs[0])

    def test_bounded_loader_and_finite_cli_codes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "candidate.json"
            values = [
                (self.document("valid_complete_candidate"), 0),
                (self.document("deny_self_approval"), 1),
                (self.document("hold_missing_evidence_support"), 3),
            ]
            for value, code in values:
                path.write_text(json.dumps(value), encoding="utf-8")
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(code, main([str(path)]))
            path.write_text("{not-json}\n", encoding="utf-8")
            self.assertEqual("ERROR", validate_file(path).outcome)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(2, main([str(path)]))
            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * 1_000_001)
            self.assertEqual("ERROR", validate_file(oversized).outcome)

    def test_multi_file_cli_uses_highest_severity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            hold = root / "hold.json"
            deny = root / "deny.json"
            error = root / "error.json"
            hold.write_text(json.dumps(self.document("hold_missing_review_support")), encoding="utf-8")
            deny.write_text(json.dumps(self.document("deny_self_approval")), encoding="utf-8")
            error.write_text("{not-json}\n", encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(1, main([str(hold), str(deny)]))
                self.assertEqual(2, main([str(deny), str(error)]))


if __name__ == "__main__":
    unittest.main()
