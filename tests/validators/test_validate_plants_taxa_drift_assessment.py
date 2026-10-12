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
MODULE_PATH = ROOT / "tools/validators/source/validate_plants_taxa_drift_assessment.py"
SPEC = importlib.util.spec_from_file_location(
    "validate_plants_taxa_drift_assessment", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PlantsTaxaDriftAssessmentTests(unittest.TestCase):
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

    def test_pass_is_fixture_coherence_without_authority(self) -> None:
        for name in (
            "pass_nonsensitive_change_candidate",
            "pass_sensitive_withheld_candidate",
            "pass_no_material_change_without_work_record",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertFalse(candidate["sensitivity"]["occurrence_join_performed"])
            self.assertFalse(candidate["sensitivity"]["exact_locations_present"])
            self.assertEqual(candidate["output"]["publication_state"], "NOT_PUBLISHED")

    def test_unchanged_fixture_emits_no_work_record(self) -> None:
        candidate = self._candidate("pass_no_material_change_without_work_record")
        self.assertEqual(candidate["materiality"], "NO_MATERIAL_CHANGE")
        self.assertEqual(candidate["output"]["posture"], "NO_WORK_RECORD")
        self.assertIsNone(candidate["output"]["candidate_ref"])
        self.assertEqual(candidate["set_delta"]["added_taxon_refs"], [])
        self.assertEqual(candidate["set_delta"]["removed_taxon_refs"], [])

    def test_unresolved_taxonomy_sensitivity_materiality_or_review_abstains(self) -> None:
        expected = {
            "abstain_taxonomy_version_drift": ["TAXONOMY_VERSION_DRIFT"],
            "abstain_unknown_sensitivity_intersection": [
                "SENSITIVITY_INTERSECTION_UNKNOWN"
            ],
            "abstain_materiality_unresolved": ["MATERIALITY_UNRESOLVED"],
            "abstain_review_pending": ["REVIEW_PENDING"],
            "abstain_review_unknown": ["REVIEW_UNKNOWN"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "ABSTAIN")
            self.assertEqual(result.codes, codes)

    def test_set_delta_and_rename_invariants_fail_closed(self) -> None:
        expected = {
            "deny_noncanonical_added_taxa": ["ADDED_TAXA_NOT_CANONICAL"],
            "deny_noncanonical_removed_taxa": ["REMOVED_TAXA_NOT_CANONICAL"],
            "deny_added_removed_overlap": ["DELTA_SET_OVERLAP"],
            "deny_rename_source_not_removed": ["RENAME_SOURCE_NOT_REMOVED"],
            "deny_rename_target_not_added": ["RENAME_TARGET_NOT_ADDED"],
            "deny_self_referential_rename": [
                "RENAME_SELF_REFERENCE",
                "RENAME_TARGET_NOT_ADDED",
            ],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_materiality_and_snapshot_invariants_fail_closed(self) -> None:
        expected = {
            "deny_delta_with_identical_snapshot_digest": [
                "DELTA_WITH_IDENTICAL_SNAPSHOT_DIGEST"
            ],
            "deny_no_material_change_with_delta": ["NO_MATERIAL_CHANGE_WITH_DELTA"],
            "deny_change_candidate_without_delta": ["CHANGE_CANDIDATE_WITHOUT_DELTA"],
            "deny_current_snapshot_not_newer": ["CURRENT_SNAPSHOT_NOT_NEWER"],
            "deny_snapshot_reference_reuse": ["SNAPSHOT_REFERENCE_REUSED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_sensitive_join_and_location_boundaries_fail_closed(self) -> None:
        expected = {
            "deny_occurrence_join": ["OCCURRENCE_JOIN_DENIED"],
            "deny_exact_locations": ["EXACT_LOCATION_DENIED"],
            "deny_sensitive_detail_not_withheld": ["SENSITIVE_DETAIL_NOT_WITHHELD"],
            "deny_sensitive_without_policy_reference": [
                "SENSITIVITY_POLICY_REFERENCE_REQUIRED"
            ],
            "deny_change_without_sensitivity_review": ["CHANGE_REVIEW_REQUIRED"],
            "deny_sensitive_without_review": [
                "CHANGE_REVIEW_REQUIRED",
                "SENSITIVITY_REVIEW_REQUIRED",
            ],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_attestations_review_and_store_bypasses_fail_closed(self) -> None:
        expected = {
            "deny_missing_source_snapshot_attestations": [
                "SOURCE_SNAPSHOT_ATTESTATIONS_INCOMPLETE"
            ],
            "deny_missing_taxonomy_version_attestation": [
                "TAXONOMY_VERSION_ATTESTATION_REQUIRED"
            ],
            "deny_complete_review_without_record": ["REVIEW_RECORD_REQUIRED"],
            "deny_direct_store_reference": ["DIRECT_STORE_REFERENCE_DENIED"],
            "deny_embedded_query_marker": ["EMBEDDED_QUERY_DENIED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_and_assessment_id_bind_declared_semantics(self) -> None:
        candidate = self._candidate("pass_nonsensitive_change_candidate")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        self.assertEqual(candidate["assessment_id"], MODULE.compute_assessment_id(candidate))
        changed = copy.deepcopy(candidate)
        changed["sensitivity"]["public_detail_mode"] = "WITHHELD"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))
        self.assertNotEqual(candidate["assessment_id"], MODULE.compute_assessment_id(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_nonsensitive_change_candidate")
        candidate["source_bindings"]["watcher_registry_ref"] = "kfm://registry/invalid\ud800"
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
