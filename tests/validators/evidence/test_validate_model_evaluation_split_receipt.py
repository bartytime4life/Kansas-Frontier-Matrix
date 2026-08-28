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
MODULE_PATH = (
    ROOT / "tools/validators/evidence/validate_model_evaluation_split_receipt.py"
)
SPEC = importlib.util.spec_from_file_location(
    "model_evaluation_split_receipt_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ModelEvaluationSplitReceiptTests(unittest.TestCase):
    """Prove the split matrix, leakage posture, and no-effect boundary."""

    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 34)
        self.assertTrue(all(item["ok"] for item in results))

    def test_supported_split_profiles_pass_without_authority(self) -> None:
        for name in (
            "pass_random_holdout",
            "pass_stratified_holdout",
            "pass_group_holdout",
            "pass_spatial_block",
            "pass_temporal_block",
            "pass_spatiotemporal_block",
            "pass_k_fold",
            "pass_public_explanation_support",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertIsNone(candidate["disclosure"]["release_manifest_ref"])

    def test_incomplete_and_unresolved_profiles_abstain(self) -> None:
        for name in (
            "abstain_incomplete",
            "abstain_model_card_unresolved",
            "abstain_split_method_unresolved",
            "abstain_partition_unresolved",
            "abstain_leakage_check_unresolved",
            "abstain_evaluation_receipt_unresolved",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "ABSTAIN",
            )

    def test_partition_accounting_and_order_fail_closed(self) -> None:
        expected = {
            "deny_partition_count_mismatch": ["PARTITION_COUNT_MISMATCH"],
            "deny_partition_reference_duplicate": [
                "PARTITION_REFERENCE_DUPLICATE"
            ],
            "deny_partition_order": ["PARTITION_ORDER_INVALID"],
        }
        for name, codes in expected.items():
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).codes,
                codes,
            )

    def test_seed_stratification_and_group_rules_fail_closed(self) -> None:
        expected = {
            "deny_random_seed_missing": ["RANDOM_SEED_REQUIRED"],
            "deny_stratification_fields_missing": [
                "STRATIFICATION_FIELDS_REQUIRED"
            ],
            "deny_class_distribution_missing": [
                "CLASS_DISTRIBUTION_REFERENCE_REQUIRED"
            ],
            "deny_grouping_fields_missing": ["GROUPING_FIELDS_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).codes,
                codes,
            )

    def test_spatial_and_temporal_holdout_scope_fail_closed(self) -> None:
        for name in (
            "deny_spatial_holdout_incomplete",
            "deny_temporal_holdout_incomplete",
        ):
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "DENY")
            self.assertGreaterEqual(len(result.codes), 3)

    def test_leakage_checks_require_passing_evidence(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(
                self._candidate("deny_leakage_check_failed")
            ).codes,
            ["LEAKAGE_CHECK_FAILED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(
                self._candidate("deny_leakage_check_evidence_missing")
            ).codes,
            ["LEAKAGE_CHECK_EVIDENCE_REQUIRED"],
        )

    def test_public_candidate_requires_scope_evidence_review_and_generalization(
        self,
    ) -> None:
        for name in (
            "deny_public_holdout_note_missing",
            "deny_public_evidence_missing",
            "deny_public_review_missing",
            "deny_public_generalization_missing",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "DENY",
            )

    def test_hash_and_receipt_identity_bind_partition_semantics(self) -> None:
        candidate = self._candidate("pass_random_holdout")
        profile_hash = MODULE.compute_profile_hash(candidate)
        self.assertEqual(candidate["profile_spec_hash"], profile_hash)
        self.assertEqual(
            candidate["receipt_ref"],
            MODULE.expected_receipt_ref(profile_hash),
        )
        changed = copy.deepcopy(candidate)
        changed["partitions"][0]["count"] = 79
        self.assertNotEqual(profile_hash, MODULE.compute_profile_hash(changed))
        self.assertNotIn("training_rows", candidate)
        self.assertNotIn("record_ids", candidate["partitions"][0])
        self.assertNotIn("labels", candidate["partitions"][0])
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("error_evaluation")).outcome,
            "ERROR",
        )

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
