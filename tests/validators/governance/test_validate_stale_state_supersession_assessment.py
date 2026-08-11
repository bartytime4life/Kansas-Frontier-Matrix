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
MODULE_PATH = ROOT / "tools/validators/governance/validate_stale_state_supersession_assessment.py"
SPEC = importlib.util.spec_from_file_location(
    "validate_stale_state_supersession_assessment", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class StaleStateSupersessionAssessmentTests(unittest.TestCase):
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

    def test_coherent_candidates_require_review_without_authority(self) -> None:
        for name in (
            "review_required_coherent_published_supersession",
            "review_required_ai_receipt_new_cross_reference",
        ):
            candidate = self._candidate(name)
            result = MODULE.validate_candidate(candidate)
            self.assertEqual(result.outcome, "REVIEW_REQUIRED")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertEqual(candidate["limitations"][0], "ASSESSMENT_ONLY")

    def test_unknown_or_unresolved_declarations_abstain(self) -> None:
        expected = {
            "abstain_marker_unknown": ["MARKER_UNKNOWN"],
            "abstain_source_basis_unresolved": ["SOURCE_BASIS_UNRESOLVED"],
            "abstain_lineage_unknown": ["LINEAGE_UNKNOWN"],
            "abstain_subject_state_unknown": ["SUBJECT_STATE_UNKNOWN"],
            "abstain_review_pending": ["REVIEW_PENDING"],
            "abstain_review_unknown": ["REVIEW_UNKNOWN"],
            "abstain_action_held": ["ACTION_HELD"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "ABSTAIN")
            self.assertEqual(result.codes, codes)

    def test_lineage_history_and_ai_receipt_bypasses_are_denied(self) -> None:
        expected = {
            "deny_missing_successor": ["SUCCESSOR_REQUIRED"],
            "deny_self_referential_successor": ["LINEAGE_SELF_REFERENCE"],
            "deny_prior_artifact_not_retained": ["PRIOR_ARTIFACT_NOT_RETAINED"],
            "deny_silent_rebind": ["SILENT_REBIND_DENIED"],
            "deny_ai_receipt_retroactive_supersession": [
                "AI_RECEIPT_RETROACTIVE_SUPERSESSION_DENIED"
            ],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_stale_signal_temporal_and_action_coherence_fail_closed(self) -> None:
        expected = {
            "deny_state_marker_contradiction": ["STATE_MARKER_CONTRADICTION"],
            "deny_missing_detection_time": ["MARKER_DETECTED_AT_REQUIRED"],
            "deny_detection_after_evaluation": ["DETECTED_AFTER_EVALUATION"],
            "deny_action_lineage_mismatch": ["ACTION_LINEAGE_INCOHERENT"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_correction_public_and_adr_closure_fail_closed(self) -> None:
        expected = {
            "deny_incorrect_without_correction": ["INCORRECT_WITHOUT_CORRECTION"],
            "deny_published_without_rollback": ["PUBLISHED_ROLLBACK_REQUIRED"],
            "deny_published_without_affected_surfaces": ["PUBLISHED_SURFACES_REQUIRED"],
            "deny_schema_supersession_without_adr": ["ADR_REFERENCE_REQUIRED"],
            "deny_policy_supersession_without_adr": ["ADR_REFERENCE_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_reference_query_store_and_review_bypasses_are_denied(self) -> None:
        expected = {
            "deny_noncanonical_basis_refs": ["REFERENCES_NOT_CANONICAL"],
            "deny_direct_store_reference": ["DIRECT_STORE_REFERENCE_DENIED"],
            "deny_embedded_query": ["EMBEDDED_QUERY_DENIED"],
            "deny_complete_review_without_record": ["REVIEW_RECORD_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_and_assessment_id_bind_declared_semantics(self) -> None:
        candidate = self._candidate("review_required_coherent_published_supersession")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        self.assertEqual(candidate["assessment_id"], MODULE.compute_assessment_id(candidate))
        changed = copy.deepcopy(candidate)
        changed["stale_evaluation"]["marker"] = "RIGHTS_STATUS_CHANGED"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))
        self.assertNotEqual(candidate["assessment_id"], MODULE.compute_assessment_id(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("review_required_coherent_published_supersession")
        candidate["subject"]["object_ref"] = "kfm://evidence/invalid\ud800"
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
