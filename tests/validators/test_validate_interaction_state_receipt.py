from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/source/validate_interaction_state_receipt.py"
SPEC = importlib.util.spec_from_file_location("interaction_state_receipt_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class InteractionStateReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        self.assertEqual(len(MODULE.validate_fixture_manifest()), 16)

    def test_success_failure_and_blocked_receipts_remain_distinct(self) -> None:
        for name, outcome in (("pass_captured_form_with_redaction", "CAPTURED"), ("pass_failed_script_receipt", "FAILED"), ("pass_blocked_redirect_receipt", "BLOCKED"), ("pass_composite_capture", "CAPTURED")):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertEqual(candidate["result"]["outcome"], outcome)
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_sensitive_classes_have_no_value_fields(self) -> None:
        candidate = self._candidate("pass_captured_form_with_redaction")
        serialized = json.dumps(candidate, sort_keys=True)
        for forbidden in ("cookie_values", "headers", "hidden_values", "query_string", "token_values", "url"):
            self.assertNotIn(forbidden, serialized.lower())
        self.assertFalse(candidate["redaction"]["retained_sensitive_values"])

    def test_step_result_redaction_and_obligation_conflicts_deny(self) -> None:
        for name in ("deny_step_index_gap", "deny_state_chain_mismatch", "deny_form_action_missing", "deny_sensitive_coverage_mismatch", "deny_sensitive_redaction_receipt_missing", "deny_capture_handoff_obligation_missing", "deny_capture_result_incoherent", "deny_terminal_step_not_last"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_identity_binds_interaction_trace(self) -> None:
        candidate = self._candidate("pass_captured_form_with_redaction")
        expected_hash, expected_id = MODULE.canonical_identity(candidate)
        self.assertEqual((candidate["receipt_spec_hash"], candidate["receipt_id"]), (expected_hash, expected_id))
        changed = copy.deepcopy(candidate)
        changed["interaction"]["steps"][1]["target_ref"] = "kfm:interaction-target:synthetic-form:changed"
        self.assertNotEqual(expected_hash, MODULE.canonical_identity(changed)[0])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
