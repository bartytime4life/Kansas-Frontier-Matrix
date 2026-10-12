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
MODULE_PATH = (
    ROOT / "tools/validators/evidence/validate_hyperparameter_tuning_receipt.py"
)
SPEC = importlib.util.spec_from_file_location(
    "hyperparameter_tuning_receipt_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class HyperparameterTuningReceiptTests(unittest.TestCase):
    """Prove the tuning declaration matrix and no-effect boundary."""

    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 31)
        self.assertTrue(all(item["ok"] for item in results))

    def test_supported_search_methods_pass_without_authority(self) -> None:
        for name in (
            "pass_grid_search",
            "pass_random_search",
            "pass_bayesian_optimization",
            "pass_successive_halving",
            "pass_manual",
            "pass_custom",
            "pass_public_claim_support",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertIsNone(candidate["disclosure"]["release_manifest_ref"])

    def test_unresolved_inputs_and_reproducibility_abstain(self) -> None:
        for name in (
            "abstain_incomplete",
            "abstain_method_unresolved",
            "abstain_model_card_unresolved",
            "abstain_evaluation_report_unresolved",
            "abstain_determinism_unknown",
            "abstain_nondeterministic",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "ABSTAIN",
            )

    def test_search_and_selection_contradictions_deny(self) -> None:
        expected = {
            "deny_random_seed_missing": ["RANDOM_SEED_REQUIRED"],
            "deny_custom_definition_missing": [
                "CUSTOM_METHOD_DEFINITION_REQUIRED"
            ],
            "deny_selected_parameter_missing": [
                "SELECTED_PARAMETER_SET_MISMATCH"
            ],
            "deny_selected_value_kind": ["SELECTED_VALUE_KIND_MISMATCH"],
            "deny_search_space_order": ["SEARCH_SPACE_NOT_CANONICAL"],
            "deny_selected_values_order": ["SELECTED_VALUES_NOT_CANONICAL"],
        }
        for name, codes in expected.items():
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).codes,
                codes,
            )

    def test_trial_and_domain_accounting_fail_closed(self) -> None:
        for name in (
            "deny_trial_accounting",
            "deny_no_completed_trial",
            "deny_discrete_count_missing",
            "deny_fixed_count_invalid",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "DENY",
            )

    def test_public_candidate_requires_summary_evidence_review_and_generalization(
        self,
    ) -> None:
        for name in (
            "deny_public_summary_missing",
            "deny_public_evidence_missing",
            "deny_public_review_missing",
            "deny_public_generalization_missing",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "DENY",
            )

    def test_hash_binds_search_and_selection_semantics(self) -> None:
        candidate = self._candidate("pass_grid_search")
        profile_hash = MODULE.compute_profile_hash(candidate)
        self.assertEqual(candidate["profile_spec_hash"], profile_hash)
        self.assertEqual(
            candidate["receipt_ref"],
            MODULE.expected_receipt_ref(profile_hash),
        )
        changed = copy.deepcopy(candidate)
        changed["selection"]["selected_values"][0]["canonical_value"] = "0.10"
        self.assertNotEqual(profile_hash, MODULE.compute_profile_hash(changed))
        self.assertNotIn("training_rows", candidate)
        self.assertNotIn("trial_payloads", candidate["search"])
        self.assertNotIn("metric_value", candidate["objective"])

    def test_identity_authority_and_error_cases_are_finite(self) -> None:
        for name in (
            "deny_profile_hash_mismatch",
            "deny_receipt_ref_mismatch",
            "deny_authority_overclaim",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "DENY",
            )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("error_tuning")).outcome,
            "ERROR",
        )
        surrogate = self._candidate("pass_grid_search")
        surrogate["selection"]["selected_values"][0]["canonical_value"] = "\ud800"
        self.assertEqual(
            MODULE.validate_candidate(surrogate).codes,
            ["CANONICALIZATION_FAILED"],
        )

    def test_input_hardening_rejects_duplicate_nonfinite_and_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            link.symlink_to(target)
            self.assertEqual(MODULE.load_json_object(duplicate)[1][0].code, "JSON_DUPLICATE_KEY")
            self.assertEqual(
                MODULE.load_json_object(nonfinite)[1][0].code,
                "JSON_NONFINITE_NUMBER",
            )
            self.assertEqual(MODULE.load_json_object(link)[1][0].code, "INPUT_SYMLINK_DENIED")

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network denied"),
        ), mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network denied"),
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
