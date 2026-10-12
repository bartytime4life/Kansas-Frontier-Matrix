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

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/validate_spatial_model_family_assessment.py"
SPEC = importlib.util.spec_from_file_location("spatial_model_family_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class SpatialModelFamilyAssessmentTests(unittest.TestCase):
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
        self.assertEqual(len(results), 20)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_each_base_family_and_decomposed_composite_pass(self) -> None:
        for name in (
            "pass_position_family",
            "pass_network_family",
            "pass_field_family",
            "pass_transformation_family",
            "pass_decomposed_composite",
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

    def test_base_families_cannot_share_one_generic_rubric(self) -> None:
        expected = {
            "deny_family_characteristics_mismatch": ["FAMILY_CHARACTERISTICS_INCOHERENT"],
            "deny_family_evidence_missing": ["FAMILY_EVIDENCE_REQUIRED"],
            "deny_cross_family_evidence": ["CROSS_FAMILY_EVIDENCE_UNDECLARED"],
            "deny_base_family_components": ["BASE_FAMILY_COMPONENTS_DENIED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_composites_retain_components_and_partition_uncertainty(self) -> None:
        underdecomposed = MODULE.validate_candidate(
            self._candidate("deny_composite_underdecomposed")
        )
        self.assertEqual(underdecomposed.outcome, "DENY")
        self.assertEqual(
            underdecomposed.codes,
            [
                "COMPOSITE_COMPONENTS_REQUIRED",
                "COMPOSITE_FAMILIES_REQUIRED",
                "COMPOSITE_UNCERTAINTY_PARTITION_REQUIRED",
            ],
        )
        flattened = MODULE.validate_candidate(
            self._candidate("deny_composite_uncertainty_flattened")
        )
        self.assertEqual(flattened.codes, ["COMPOSITE_UNCERTAINTY_PARTITION_REQUIRED"])

    def test_profile_hash_and_assessment_id_bind_semantics(self) -> None:
        candidate = self._candidate("pass_field_family")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        self.assertEqual(candidate["assessment_id"], MODULE.compute_assessment_id(candidate))
        changed = copy.deepcopy(candidate)
        changed["family_evidence"]["field_support_refs"] = [
            "kfm://support/synthetic/changed/v2"
        ]
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
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            _, findings = MODULE.load_json_object(nonfinite)
            self.assertEqual([item.code for item in findings], ["JSON_NONFINITE_NUMBER"])

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_position_family")
        candidate["subject_ref"] = "kfm://feature/invalid\ud800"
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
