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
MODULE_PATH = ROOT / "tools/validators/governance/validate_responsibility_layer_impact_assessment.py"
SPEC = importlib.util.spec_from_file_location(
    "validate_responsibility_layer_impact_assessment", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ResponsibilityLayerImpactAssessmentTests(unittest.TestCase):
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

    def test_pass_is_local_coherence_without_authority(self) -> None:
        for name in (
            "pass_declared_public_surface_chain",
            "pass_single_operations_layer",
        ):
            candidate = self._candidate(name)
            result = MODULE.validate_candidate(candidate)
            self.assertEqual(result.outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertEqual(candidate["limitations"][0], "ASSESSMENT_ONLY")

    def test_unresolved_review_or_seam_abstains(self) -> None:
        expected = {
            "abstain_review_pending": ["REVIEW_PENDING"],
            "abstain_review_unknown": ["REVIEW_UNKNOWN"],
            "abstain_unresolved_seam": ["SEAM_UNRESOLVED"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "ABSTAIN")
            self.assertEqual(result.codes, codes)

    def test_artifact_ownership_and_layer_coverage_fail_closed(self) -> None:
        expected = {
            "deny_owner_path_mismatch": ["OWNING_ROOT_PATH_MISMATCH"],
            "deny_noncanonical_artifacts": ["ARTIFACTS_NOT_CANONICAL"],
            "deny_noncanonical_related_layers": ["RELATED_LAYERS_NOT_CANONICAL"],
            "deny_layer_impact_coverage_mismatch": ["LAYER_IMPACT_COVERAGE_MISMATCH"],
            "deny_impact_kind_mismatch": ["IMPACT_KIND_INCOHERENT"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_public_surface_policy_and_release_closure_fail_closed(self) -> None:
        expected = {
            "deny_public_surface_without_evidence_closure": [
                "PUBLIC_SURFACE_CLOSURE_INCOMPLETE"
            ],
            "deny_release_without_rollback": ["RELEASE_ROLLBACK_REFERENCE_REQUIRED"],
            "deny_policy_without_decision_reference": [
                "POLICY_DECISION_REFERENCE_REQUIRED"
            ],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_cross_layer_seams_fail_closed(self) -> None:
        expected = {
            "deny_seam_uses_undeclared_layer": [
                "LAYER_GRAPH_DISCONNECTED",
                "SEAM_LAYER_NOT_DECLARED",
            ],
            "deny_self_referential_seam": [
                "LAYER_GRAPH_DISCONNECTED",
                "SEAM_SELF_REFERENCE",
            ],
            "deny_disconnected_layer_graph": ["LAYER_GRAPH_DISCONNECTED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_direct_store_query_and_review_bypasses_are_denied(self) -> None:
        expected = {
            "deny_complete_review_without_record": ["REVIEW_RECORD_REQUIRED"],
            "deny_direct_store_reference": ["DIRECT_STORE_REFERENCE_DENIED"],
            "deny_embedded_query_marker": ["EMBEDDED_QUERY_DENIED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_and_assessment_id_bind_declared_semantics(self) -> None:
        candidate = self._candidate("pass_declared_public_surface_chain")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        self.assertEqual(candidate["assessment_id"], MODULE.compute_assessment_id(candidate))
        changed = copy.deepcopy(candidate)
        changed["layer_impacts"][0]["validation_refs"] = [
            "kfm://validation/synthetic/api-contract-v2"
        ]
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))
        self.assertNotEqual(candidate["assessment_id"], MODULE.compute_assessment_id(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_declared_public_surface_chain")
        candidate["change_ref"] = "kfm://change/invalid\ud800"
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
