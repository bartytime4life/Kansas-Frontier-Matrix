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
MODULE_PATH = ROOT / "tools/validators/evidence/validate_model_selection_rationale_assessment.py"
SPEC = importlib.util.spec_from_file_location("model_selection_rationale_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ModelSelectionRationaleAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Draft202012Validator.check_schema(
            json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        )
        cls.cases = {entry["name"]: entry for entry in MANIFEST["cases"]}

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(MANIFEST, self.cases[name])

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 27)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_coherent_classification_regression_and_clustering_pass(self) -> None:
        for name in (
            "pass_classification_tree_over_linear_baseline",
            "pass_regression_linear_over_tree_baseline",
            "pass_clustering_with_clustering_baseline",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_finite_outcomes_are_covered(self) -> None:
        outcomes = {
            MODULE.validate_candidate(self._candidate(name)).outcome
            for name in self.cases
        }
        self.assertEqual(outcomes, {"PASS", "ABSTAIN", "DENY", "ERROR"})

    def test_unresolved_problem_selection_review_and_sensitivity_abstain(self) -> None:
        for name in (
            "abstain_problem_unresolved",
            "abstain_selection_unresolved",
            "abstain_review_pending",
            "abstain_sensitive_data_unknown",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "ABSTAIN",
            )

    def test_selection_requires_comparable_eligible_evaluated_candidates(self) -> None:
        expected = {
            "deny_selected_candidate_unknown": ["SELECTED_CANDIDATE_UNKNOWN"],
            "deny_selected_candidate_ineligible": ["SELECTED_CANDIDATE_INELIGIBLE"],
            "deny_eligible_evaluation_missing": ["ELIGIBLE_EVALUATION_REQUIRED"],
            "deny_baseline_same_as_selected": ["BASELINE_MUST_DIFFER"],
            "deny_candidates_not_canonical": ["CANDIDATES_NOT_CANONICAL"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_selection_links_problem_data_and_nonperformance_reasons(self) -> None:
        expected = {
            "deny_problem_fit_missing": ["PROBLEM_FIT_REFERENCE_REQUIRED"],
            "deny_data_fit_missing": ["DATA_FIT_REFERENCE_REQUIRED"],
            "deny_performance_only_selection": ["PERFORMANCE_ONLY_SELECTION_DENIED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_interpretability_consequence_sensitivity_and_claim_boundaries_fail_closed(self) -> None:
        expected = {
            "deny_high_consequence_policy_missing": ["HIGH_CONSEQUENCE_POLICY_REFERENCE_REQUIRED"],
            "deny_high_interpretability_opaque_selection": ["INTERPRETABILITY_METHOD_REQUIRED"],
            "deny_sensitive_data_policy_missing": ["SENSITIVE_DATA_POLICY_REFERENCE_REQUIRED"],
            "deny_causal_claim": ["CAUSAL_OR_REGULATORY_AUTHORITY_DENIED"],
            "deny_task_model_family_mismatch": ["TASK_MODEL_FAMILY_INCOHERENT"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_carries_no_numeric_performance_threshold(self) -> None:
        candidate = self._candidate("pass_classification_tree_over_linear_baseline")
        serialized = json.dumps(candidate, sort_keys=True)
        self.assertNotIn("accuracy_threshold", serialized)
        self.assertNotIn("loss_threshold", serialized)
        self.assertNotIn("candidate_score", serialized)

    def test_profile_hash_and_assessment_id_bind_selection_semantics(self) -> None:
        candidate = self._candidate("pass_classification_tree_over_linear_baseline")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        self.assertEqual(candidate["assessment_id"], MODULE.compute_assessment_id(candidate))
        changed = copy.deepcopy(candidate)
        changed["selection"]["selected_candidate_id"] = "LINEAR_BASELINE"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))
        self.assertNotEqual(candidate["assessment_id"], MODULE.compute_assessment_id(changed))

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            _, findings = MODULE.load_json_object(duplicate)
            self.assertEqual([item.code for item in findings], ["JSON_DUPLICATE_KEY"])
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            _, findings = MODULE.load_json_object(nonfinite)
            self.assertEqual([item.code for item in findings], ["JSON_NONFINITE_NUMBER"])

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_classification_tree_over_linear_baseline")
        candidate["subject_ref"] = "kfm://model-assisted-layer/invalid\ud800"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["JSON_UNPAIRED_SURROGATE"])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
