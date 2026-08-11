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
MODULE_PATH = ROOT / "tools/validators/map/validate_renderer_binding_assessment.py"
SPEC = importlib.util.spec_from_file_location("validate_renderer_binding_assessment", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RendererBindingAssessmentTests(unittest.TestCase):
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
        self.assertEqual(outcomes, {"REVIEW_REQUIRED", "ABSTAIN", "DENY", "ERROR"})

    def test_coherent_bindings_require_review_without_authority(self) -> None:
        for name in (
            "review_required_published_released_carrier",
            "review_required_candidate_governed_api",
        ):
            candidate = self._candidate(name)
            result = MODULE.validate_candidate(candidate)
            self.assertEqual(result.outcome, "REVIEW_REQUIRED")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertEqual(candidate["renderer"]["binding_state"], "CANDIDATE_INACTIVE")

    def test_unknown_or_unresolved_declarations_abstain(self) -> None:
        expected = {
            "abstain_renderer_family_unknown": ["RENDERER_FAMILY_UNKNOWN"],
            "abstain_peer_browser_policy_unresolved": ["RENDERER_POLICY_UNRESOLVED"],
            "abstain_runtime_surface_unknown": ["RUNTIME_SURFACE_UNKNOWN"],
            "abstain_binding_state_unknown": ["BINDING_STATE_UNKNOWN"],
            "abstain_delivery_input_unknown": ["DELIVERY_INPUT_UNKNOWN"],
            "abstain_evidence_support_unresolved": ["EVIDENCE_SUPPORT_UNRESOLVED"],
            "abstain_policy_support_unresolved": ["POLICY_SUPPORT_UNRESOLVED"],
            "abstain_review_support_unresolved": ["REVIEW_SUPPORT_UNRESOLVED"],
            "abstain_sensitivity_unknown": ["SENSITIVITY_STATE_UNKNOWN"],
            "abstain_rights_unknown": ["RIGHTS_STATE_UNKNOWN"],
            "abstain_release_state_unknown": ["RELEASE_STATE_UNKNOWN"],
            "abstain_interaction_context_unknown": ["INTERACTION_CONTEXT_UNKNOWN"],
            "abstain_evidence_resolution_unresolved": ["EVIDENCE_RESOLUTION_UNRESOLVED"],
            "abstain_review_pending": ["REVIEW_PENDING"],
            "abstain_review_unknown": ["REVIEW_UNKNOWN"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "ABSTAIN")
            self.assertEqual(result.codes, codes)

    def test_renderer_delivery_and_reference_bypasses_are_denied(self) -> None:
        expected = {
            "deny_headless_renderer_on_browser_surface": [
                "BROWSER_RENDERER_FAMILY_INCOHERENT"
            ],
            "deny_active_binding": ["ACTIVE_BINDING_DENIED"],
            "deny_raw_input": ["INTERNAL_INPUT_CLASS_DENIED"],
            "deny_work_input": ["INTERNAL_INPUT_CLASS_DENIED"],
            "deny_quarantine_input": ["INTERNAL_INPUT_CLASS_DENIED"],
            "deny_internal_store_input": ["INTERNAL_INPUT_CLASS_DENIED"],
            "deny_direct_store_access": ["DIRECT_STORE_ACCESS_DENIED"],
            "deny_query_text": ["QUERY_TEXT_DENIED"],
            "deny_mutable_published_locator": ["IMMUTABLE_LOCATOR_REQUIRED"],
            "deny_layer_reference_role_collapse": ["LAYER_REFERENCE_ROLE_COLLAPSE"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_public_trust_closure_fails_closed(self) -> None:
        expected = {
            "deny_restricted_sensitivity": ["RESTRICTED_SENSITIVITY_DENIED"],
            "deny_restricted_rights": ["RESTRICTED_RIGHTS_DENIED"],
            "deny_withdrawn_release": ["WITHDRAWN_RELEASE_DENIED"],
            "deny_published_without_evidence_closure": [
                "PUBLISHED_TRUST_CLOSURE_REQUIRED"
            ],
            "deny_published_without_promotion": ["PUBLISHED_PROMOTION_REQUIRED"],
            "deny_published_without_release_manifest": ["PUBLISHED_RELEASE_REQUIRED"],
            "deny_published_without_rollback": ["PUBLISHED_ROLLBACK_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_interaction_authority_bypasses_are_denied(self) -> None:
        expected = {
            "deny_feature_properties_only_context": ["FEATURE_PROPERTIES_CONTEXT_DENIED"],
            "deny_feature_properties_as_authority": [
                "FEATURE_PROPERTIES_AUTHORITY_DENIED"
            ],
            "deny_client_policy_authority": ["CLIENT_POLICY_AUTHORITY_DENIED"],
            "deny_hidden_feature_inference": ["HIDDEN_FEATURE_INFERENCE_DENIED"],
            "deny_direct_internal_lookup": ["DIRECT_INTERNAL_LOOKUP_DENIED"],
            "deny_direct_store_reference": ["DIRECT_STORE_REFERENCE_DENIED"],
            "deny_embedded_query_reference": ["EMBEDDED_QUERY_DENIED"],
            "deny_noncanonical_policy_refs": ["REFERENCES_NOT_CANONICAL"],
            "deny_complete_review_without_record": ["REVIEW_RECORD_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_and_assessment_id_bind_declared_semantics(self) -> None:
        candidate = self._candidate("review_required_published_released_carrier")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        self.assertEqual(candidate["assessment_id"], MODULE.compute_assessment_id(candidate))
        changed = copy.deepcopy(candidate)
        changed["delivery"]["delivery_ref"] = "kfm://released-carrier/map/synthetic-soil/v2"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))
        self.assertNotEqual(candidate["assessment_id"], MODULE.compute_assessment_id(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("review_required_published_released_carrier")
        candidate["renderer"]["adapter_ref"] = "kfm://adapter/invalid\ud800"
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
