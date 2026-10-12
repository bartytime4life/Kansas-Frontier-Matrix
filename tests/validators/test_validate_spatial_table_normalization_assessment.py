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

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/data/validate_spatial_table_normalization_assessment.py"
SPEC = importlib.util.spec_from_file_location("validate_spatial_table_normalization_assessment", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SpatialTableNormalizationAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.cases = {entry["name"]: entry for entry in cls.manifest["cases"]}

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self.cases[name])

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), len(self.cases))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_canonical_and_derivative_pass_profiles_remain_non_authoritative(self) -> None:
        for name in ("pass_canonical_third_normal_form", "pass_canonical_boyce_codd", "pass_intentional_release_derivative"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_profiles_abstain(self) -> None:
        for name in ("abstain_unresolved_schema", "abstain_incomplete_assessment", "abstain_unassessed_form", "abstain_incomplete_release_derivative"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_incomplete_release_derivative_abstains_without_completeness_denials(self) -> None:
        result = MODULE.validate_candidate(self._candidate("abstain_incomplete_release_derivative"))
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertEqual(result.codes, ["ASSESSMENT_INCOMPLETE", "NORMAL_FORM_UNASSESSED"])

    def test_field_dependency_form_and_derivative_invariants_fail_closed(self) -> None:
        expected = {
            "deny_entity_key_unknown": ["FIELD_REFERENCE_UNKNOWN"],
            "deny_relationship_field_arity_mismatch": ["RELATIONSHIP_FIELD_ARITY_MISMATCH"],
            "deny_dependency_field_unknown": ["FIELD_REFERENCE_UNKNOWN"],
            "deny_dependency_field_overlap": ["DEPENDENCY_FIELD_OVERLAP"],
            "deny_canonical_partial_dependency": ["CANONICAL_NORMALIZATION_ANOMALY"],
            "deny_canonical_form_insufficient": ["CANONICAL_NORMAL_FORM_INSUFFICIENT"],
            "deny_anomaly_disclosure_mismatch": ["ANOMALY_DISCLOSURE_MISMATCH"],
            "deny_derivative_source_missing": ["DERIVATIVE_SOURCE_BINDING_REQUIRED"],
            "deny_derivative_wrong_form": ["DERIVATIVE_DECLARATION_REQUIRED", "DERIVATIVE_FORM_REQUIRED", "DERIVATIVE_SOURCE_BINDING_REQUIRED"],
            "deny_review_reference_missing": ["REVIEW_REFERENCE_REQUIRED"],
            "deny_noncanonical_field_inventory": ["ARRAY_NOT_CANONICAL"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_relationship_field_arity_mismatch_denies(self) -> None:
        result = MODULE.validate_candidate(self._candidate("deny_relationship_field_arity_mismatch"))
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(result.codes, ["RELATIONSHIP_FIELD_ARITY_MISMATCH"])

    def test_profile_hash_binds_dependency_semantics(self) -> None:
        candidate = self._candidate("pass_canonical_third_normal_form")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["dependencies"][0]["kind"] = "TRANSITIVE"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_canonical_third_normal_form")
        candidate["dependencies"][0]["rationale"] = "invalid \ud800 text"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["JSON_UNPAIRED_SURROGATE"])
        with self.assertRaises(MODULE.UnpairedSurrogateError):
            MODULE.compute_profile_hash(candidate)

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            _, findings = MODULE.load_json_object(duplicate)
            self.assertEqual([item.code for item in findings], ["JSON_DUPLICATE_KEY"])
            nonfinite = Path(directory) / "nonfinite.json"
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            _, findings = MODULE.load_json_object(nonfinite)
            self.assertEqual([item.code for item in findings], ["JSON_NONFINITE_NUMBER"])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
