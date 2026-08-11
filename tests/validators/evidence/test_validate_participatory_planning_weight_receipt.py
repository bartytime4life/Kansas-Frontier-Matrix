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
MODULE_PATH = ROOT / "tools/validators/evidence/validate_participatory_planning_weight_receipt.py"
SPEC = importlib.util.spec_from_file_location("participatory_planning_weight_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ParticipatoryPlanningWeightReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(entry for entry in self.manifest["cases"] if entry["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_valid_closed_draft_2020_12(self) -> None:
        schema = MODULE._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 23)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_complete_profiles_pass(self) -> None:
        for name in (
            "pass_separate_group_weights_with_dissent",
            "pass_criteria_review_without_sensitivity_run",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "PASS")

    def test_unresolved_profiles_abstain(self) -> None:
        for name in (
            "abstain_consent_incomplete",
            "abstain_facilitation_incomplete",
            "abstain_evidence_unresolved",
            "abstain_dissent_unknown",
            "abstain_sensitivity_analysis_incomplete",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_weights_and_group_identity_fail_closed(self) -> None:
        expected = {
            "deny_weight_sum_invalid": ["WEIGHT_SUM_INVALID"],
            "deny_weight_criteria_mismatch": ["WEIGHT_CRITERIA_MISMATCH"],
            "deny_criteria_not_canonical": ["CRITERIA_NOT_CANONICAL"],
            "deny_duplicate_group_ref": ["DUPLICATE_STAKEHOLDER_GROUP_REF"],
            "deny_groups_not_canonical": ["STAKEHOLDER_GROUPS_NOT_CANONICAL"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_deliberation_and_governance_overclaims_fail_closed(self) -> None:
        expected = {
            "deny_dissent_summary_required": ["DISSENT_SUMMARY_REQUIRED"],
            "deny_dissent_summary_unexpected": ["DISSENT_SUMMARY_UNEXPECTED"],
            "deny_false_consensus_claim": ["CONSENSUS_CLAIM_DENIED"],
            "deny_conflict_summary_required": ["CONFLICT_SUMMARY_REQUIRED"],
            "deny_group_comparison_hidden": ["GROUP_COMPARISON_DISCLOSURE_REQUIRED"],
            "deny_review_overclaim": ["REVIEW_STATE_OVERCLAIM"],
            "deny_release_overclaim": ["RELEASE_STATE_OVERCLAIM"],
            "deny_policy_outcome_overclaim": ["POLICY_OUTCOME_OVERCLAIM"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_replays_and_binds_semantics(self) -> None:
        candidate = self._candidate("pass_separate_group_weights_with_dissent")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["stakeholder_weight_sets"][0]["weights"][0]["basis_points"] = 5999
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
