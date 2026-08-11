from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/governance/validate_aggregate_boundary_assessment.py"
SPEC = importlib.util.spec_from_file_location("validate_aggregate_boundary_assessment", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AggregateBoundaryAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.cases = {entry["name"]: entry for entry in cls.manifest["cases"]}

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self.cases[name])

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(
            json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        )

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), len(self.cases))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_finite_outcomes_are_covered(self) -> None:
        outcomes = {
            MODULE.validate_candidate(self._candidate(name)).outcome
            for name in self.cases
        }
        self.assertEqual(outcomes, {"PASS", "ABSTAIN", "DENY", "ERROR"})

    def test_valid_profiles_remain_declarations_without_authority(self) -> None:
        for name in (
            "pass_declared_repository_and_factory",
            "pass_repository_and_factory_not_required",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertEqual(
                candidate["declaration"]["external_evidence"]["relationship"],
                "REFERENCE_ONLY",
            )

    def test_unresolved_postures_abstain(self) -> None:
        expected = {
            "abstain_boundary_unresolved": ["AGGREGATE_BOUNDARY_UNRESOLVED"],
            "abstain_register_unresolved": ["OBJECT_FAMILY_BINDING_UNRESOLVED"],
            "abstain_not_registered": ["OBJECT_FAMILY_NOT_REGISTERED"],
            "abstain_identity_assessment_unresolved": ["IDENTITY_ASSESSMENT_UNRESOLVED"],
            "abstain_invariant_coverage_incomplete": ["INVARIANT_COVERAGE_INCOMPLETE"],
            "abstain_repository_unresolved": ["REPOSITORY_PROFILE_UNRESOLVED"],
            "abstain_factory_unresolved": ["FACTORY_PROFILE_UNRESOLVED"],
            "abstain_review_pending": ["REVIEW_PENDING"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "ABSTAIN")
            self.assertEqual(result.codes, codes)

    def test_root_and_identity_invariants_fail_closed(self) -> None:
        expected = {
            "deny_multiple_roots": ["AGGREGATE_ROOT_CARDINALITY"],
            "deny_root_declaration_mismatch": ["AGGREGATE_ROOT_DECLARATION_MISMATCH"],
            "deny_aggregate_family_root_mismatch": ["AGGREGATE_FAMILY_ROOT_MISMATCH"],
            "deny_root_identity_value_object": ["AGGREGATE_ROOT_IDENTITY_INCOHERENT"],
            "deny_resolved_register_binding_missing_digest": ["OBJECT_FAMILY_BINDING_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_external_and_internal_reference_rules_fail_closed(self) -> None:
        expected = {
            "deny_external_reference_to_internal_member": ["EXTERNAL_REFERENCE_BOUNDARY_VIOLATION"],
            "deny_external_reference_from_member": ["EXTERNAL_REFERENCE_BOUNDARY_VIOLATION"],
            "deny_external_reference_policy": ["EXTERNAL_REFERENCE_POLICY_INCOHERENT"],
            "deny_internal_reference_outside_boundary": ["INTERNAL_REFERENCE_SCOPE_INCOHERENT"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_repository_and_factory_profiles_fail_closed(self) -> None:
        expected = {
            "deny_repository_internal_fragment": ["REPOSITORY_AGGREGATE_SCOPE_INCOHERENT"],
            "deny_repository_exposes_internal_member": ["REPOSITORY_AGGREGATE_SCOPE_INCOHERENT"],
            "deny_factory_internal_fragment": ["FACTORY_AGGREGATE_SCOPE_INCOHERENT"],
            "deny_factory_without_invariant_enforcement": ["FACTORY_AGGREGATE_SCOPE_INCOHERENT"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_consistency_and_evidence_boundaries_fail_closed(self) -> None:
        expected = {
            "deny_eventual_internal_consistency": ["CONSISTENCY_BOUNDARY_INCOHERENT"],
            "deny_evidence_bundle_owned_member": ["EVIDENCE_REFERENCE_BOUNDARY_INCOHERENT"],
            "deny_direct_store_reference": ["DIRECT_STORE_REFERENCE_DENIED"],
            "deny_embedded_query_marker": ["EMBEDDED_QUERY_DENIED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_canonical_order_and_review_evidence_are_required(self) -> None:
        expected = {
            "deny_noncanonical_invariant_refs": ["ARRAY_NOT_CANONICAL"],
            "deny_noncanonical_members": ["MEMBERS_NOT_CANONICAL"],
            "deny_noncanonical_reference_edges": ["REFERENCE_EDGES_NOT_CANONICAL"],
            "deny_complete_review_without_record": ["REVIEW_RECORD_REQUIRED"],
            "deny_complete_review_without_rationale": ["RATIONALE_SUMMARY_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_and_assessment_id_bind_boundary_semantics(self) -> None:
        candidate = self._candidate("pass_declared_repository_and_factory")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        self.assertEqual(candidate["assessment_id"], MODULE.compute_assessment_id(candidate))
        changed = copy.deepcopy(candidate)
        changed["declaration"]["invariant_coverage"] = "INCOMPLETE"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))
        self.assertNotEqual(candidate["assessment_id"], MODULE.compute_assessment_id(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_declared_repository_and_factory")
        candidate["declaration"]["rationale_summary"] = "invalid \ud800 text"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["JSON_UNPAIRED_SURROGATE"])
        with self.assertRaises(MODULE.UnpairedSurrogateError):
            MODULE.compute_profile_hash(candidate)

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            _, findings = MODULE.load_json_object(duplicate)
            self.assertEqual([item.code for item in findings], ["JSON_DUPLICATE_KEY"])
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            _, findings = MODULE.load_json_object(nonfinite)
            self.assertEqual([item.code for item in findings], ["JSON_NONFINITE_NUMBER"])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
