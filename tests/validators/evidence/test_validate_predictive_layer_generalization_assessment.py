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
MODULE_PATH = ROOT / "tools/validators/evidence/validate_predictive_layer_generalization_assessment.py"
SPEC = importlib.util.spec_from_file_location("predictive_layer_generalization_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class PredictiveLayerGeneralizationAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 18)
        self.assertTrue(all(item["ok"] for item in results))

    def test_supported_public_profile_passes_without_authority(self) -> None:
        candidate = self._candidate("pass_public_supported_kfold")
        self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
        self.assertFalse(any(candidate["authority_claims"].values()))

    def test_internal_and_exploratory_profiles_can_record_adverse_labels(self) -> None:
        for name in ("pass_internal_limited_holdout", "pass_exploratory_detected_not_supported"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "PASS")

    def test_incomplete_unresolved_and_limited_public_profiles_abstain(self) -> None:
        for name in (
            "abstain_incomplete_evaluation",
            "abstain_unknown_evaluation",
            "abstain_model_card_unresolved",
            "abstain_public_risk_and_limited",
            "abstain_cross_validation_not_performed",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_public_adverse_labels_fail_closed(self) -> None:
        result = MODULE.validate_candidate(self._candidate("deny_public_overfit_not_supported"))
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(result.codes, ["PUBLIC_GENERALIZATION_DENIED", "PUBLIC_OVERFITTING_DENIED"])

    def test_profile_carries_no_numeric_scientific_threshold(self) -> None:
        candidate = self._candidate("pass_public_supported_kfold")
        self.assertNotIn("accuracy_threshold", candidate)
        self.assertNotIn("abstention_threshold", candidate)

    def test_profile_hash_binds_generalization_semantics(self) -> None:
        candidate = self._candidate("pass_public_supported_kfold")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["evaluation"]["generalization_label"] = "LIMITED"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
