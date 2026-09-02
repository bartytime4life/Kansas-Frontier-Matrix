from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
import unittest
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/ui/validate_evidence_drawer_payload.py"
SPEC = importlib.util.spec_from_file_location("validate_evidence_drawer_payload", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class EvidenceDrawerPayloadValidatorTests(unittest.TestCase):
    def test_fixture_matrix_has_exact_polarity(self) -> None:
        self.assertEqual(0, MODULE.run_fixtures())

    def test_schema_is_closed_and_pins_explorer_profile(self) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            "kfm.explorer.evidence-drawer.public-safe.v1",
            schema["properties"]["profile"]["const"],
        )
        self.assertIn("history", schema["properties"])
        self.assertEqual(
            ["ANSWER", "ABSTAIN", "DENY", "ERROR"],
            schema["properties"]["outcome"]["enum"],
        )

    def test_corrected_answer_requires_acyclic_bound_history(self) -> None:
        missing = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "invalid/corrected-answer-without-history.json"
        )
        cycle = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "invalid/correction-cycle.json"
        )
        self.assertIn("CORRECTION_HISTORY_REQUIRED", {item.code for item in missing})
        self.assertIn("CORRECTION_CYCLE", {item.code for item in cycle})

    def test_multi_hop_correction_chain_terminates_in_current_support(self) -> None:
        findings = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "valid/answer-corrected-chain.json"
        )
        self.assertEqual((), findings)

    def test_every_outcome_requires_superseded_correction_prior_history(self) -> None:
        valid = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "valid/answer-corrected.json"
        )
        invalid = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT
            / "invalid/abstain-correction-without-superseded-history.json"
        )

        self.assertEqual((), valid)
        self.assertEqual(
            {"CORRECTION_PRIOR_NOT_SUPERSEDED"},
            {item.code for item in invalid},
        )

    def test_correction_history_cannot_claim_no_correction(self) -> None:
        payload = json.loads(
            (MODULE.FIXTURES_ROOT / "valid/abstain-stale.json").read_text(encoding="utf-8")
        )
        corrected = json.loads(
            (MODULE.FIXTURES_ROOT / "valid/answer-corrected.json").read_text(encoding="utf-8")
        )
        payload["history"] = corrected["history"]

        findings = MODULE._semantic_findings(payload)
        self.assertEqual(
            {"CORRECTION_STATE_REQUIRED"},
            {item.code for item in findings},
        )

        payload["trust_state"]["correction"] = "CORRECTED"
        self.assertEqual([], MODULE._semantic_findings(payload))

    def test_negative_state_reason_must_match(self) -> None:
        findings = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "invalid/negative-state-reason-mismatch.json"
        )
        self.assertIn(
            "NEGATIVE_STATE_REASON_MISMATCH",
            {item.code for item in findings},
        )

    def test_revoked_abstention_requires_bound_non_current_history(self) -> None:
        valid_path = MODULE.FIXTURES_ROOT / "valid/abstain-revoked.json"
        missing_path = (
            MODULE.FIXTURES_ROOT
            / "invalid/abstain-revoked-without-history.json"
        )

        self.assertEqual((), MODULE.validate_payload(valid_path))
        self.assertIn(
            "NEGATIVE_HISTORY_REQUIRED",
            {item.code for item in MODULE.validate_payload(missing_path)},
        )

        payload = json.loads(valid_path.read_text(encoding="utf-8"))
        self.assertEqual("REVOKED_EVIDENCE", payload["reason_code"])
        self.assertEqual([], payload["evidence_refs"])
        self.assertEqual([], payload["citations"])
        revoked = payload["history"]["negative_outcomes"]
        self.assertEqual(1, len(revoked))
        self.assertEqual("REVOKED", revoked[0]["state"])
        self.assertEqual("REVOKED_EVIDENCE", revoked[0]["reason_code"])
        self.assertTrue(revoked[0]["visible_in_runtime"])
        self.assertFalse(revoked[0]["resolvable_as_current"])

    def test_answer_history_must_be_a_complete_correction_chain(self) -> None:
        findings = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "invalid/answer-unbound-history.json"
        )
        self.assertIn("ANSWER_HISTORY_UNBOUND", {item.code for item in findings})

    def test_denied_projection_cannot_expose_history(self) -> None:
        findings = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "invalid/deny-history-leak.json"
        )
        self.assertIn("DENY_HISTORY_LEAK", {item.code for item in findings})

    def test_validator_is_deterministic_and_no_network(self) -> None:
        path = MODULE.FIXTURES_ROOT / "valid/answer-corrected.json"
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "getaddrinfo", side_effect=AssertionError("dns denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("socket denied")):
            self.assertEqual(MODULE.validate_payload(path), MODULE.validate_payload(path))

    def test_cli_fixture_mode(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr + completed.stdout)
        self.assertIn("EVIDENCE_DRAWER_FIXTURES_VALID", completed.stdout)

    def test_typescript_adapter_tracks_schema_profile_and_history(self) -> None:
        source = (
            REPO_ROOT / "apps/explorer-web/src/adapters/GovernedClient.ts"
        ).read_text(encoding="utf-8")
        self.assertIn("kfm.explorer.evidence-drawer.public-safe.v1", source)
        self.assertIn("SUPERSEDED_EVIDENCE", source)
        self.assertIn("correctionPriorRefs", source)
        self.assertIn("correctionsContainCycle", source)
        self.assertIn("resolvable_as_current", source)


if __name__ == "__main__":
    unittest.main()
