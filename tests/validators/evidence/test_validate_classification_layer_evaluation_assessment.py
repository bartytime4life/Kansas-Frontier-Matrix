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
MODULE_PATH = ROOT / "tools/validators/evidence/validate_classification_layer_evaluation_assessment.py"
SPEC = importlib.util.spec_from_file_location("classification_layer_evaluation_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ClassificationLayerEvaluationAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 23)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_confusion_matrix_arithmetic_passes_without_authority(self) -> None:
        candidate = self._candidate("pass_public_confusion_matrix")
        self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
        self.assertFalse(any(candidate["authority_claims"].values()))

    def test_comparable_evaluation_is_reference_only(self) -> None:
        candidate = self._candidate("pass_public_comparable_evaluation")
        self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
        self.assertIsNone(candidate["evaluation"]["confusion_matrix"])
        self.assertTrue(candidate["evaluation"]["comparable_evaluation_refs"])

    def test_weak_and_unsupervised_public_use_abstain(self) -> None:
        for name in ("abstain_public_weakly_supervised", "abstain_public_unsupervised"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_tampered_counts_and_metrics_fail_closed(self) -> None:
        for name in (
            "deny_sample_count_mismatch",
            "deny_correct_count_mismatch",
            "deny_overall_accuracy_mismatch",
            "deny_class_metric_mismatch",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_profile_defines_no_scientific_threshold(self) -> None:
        candidate = self._candidate("pass_public_confusion_matrix")
        self.assertNotIn("accuracy_threshold", candidate)
        self.assertNotIn("minimum_class_support", candidate)
        self.assertIn("NO_SCIENTIFIC_THRESHOLD", candidate["limitations"])

    def test_profile_hash_binds_matrix_semantics(self) -> None:
        candidate = self._candidate("pass_public_confusion_matrix")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["evaluation"]["confusion_matrix"]["rows"][0]["predictions"][0]["count"] += 1
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
