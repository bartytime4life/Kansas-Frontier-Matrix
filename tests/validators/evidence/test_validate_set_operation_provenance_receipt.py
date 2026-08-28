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

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/evidence/validate_set_operation_provenance_receipt.py"
SPEC = importlib.util.spec_from_file_location("set_operation_provenance_receipt_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class SetOperationProvenanceReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 21)
        self.assertTrue(all(item["ok"] for item in results))

    def test_complete_operator_profiles_pass_without_authority(self) -> None:
        for name in (
            "pass_union_all",
            "pass_union_distinct",
            "pass_intersect",
            "pass_except",
            "pass_symmetric_difference",
            "pass_custom",
            "pass_public_support",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_incomplete_and_unresolved_profiles_abstain(self) -> None:
        for name in (
            "abstain_incomplete",
            "abstain_query_plan_unresolved",
            "abstain_input_unresolved",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_count_invariants_fail_closed(self) -> None:
        expected = {
            "deny_union_all_count_mismatch": ["UNION_ALL_COUNT_MISMATCH"],
            "deny_intersect_count_bound": ["INTERSECT_COUNT_BOUND_EXCEEDED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_ordered_except_and_duplicate_policy_fail_closed(self) -> None:
        for name in (
            "deny_except_roles",
            "deny_duplicate_policy",
            "deny_input_order",
            "deny_output_input_ref_collision",
            "deny_custom_rationale_missing",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_public_candidate_requires_evidence_and_review_disclosure(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_public_evidence_missing")).codes,
            ["PUBLIC_EVIDENCE_REFERENCE_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("pass_public_support")).outcome,
            "PASS",
        )

    def test_profile_hash_binds_operator_semantics(self) -> None:
        candidate = self._candidate("pass_union_all")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["operator"]["operation_type"] = "UNION_DISTINCT"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_profile_does_not_carry_records_or_query_text(self) -> None:
        candidate = self._candidate("pass_union_all")
        self.assertNotIn("records", candidate)
        self.assertNotIn("executed_query", candidate)
        self.assertNotIn("query_text", candidate["evidence"])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
