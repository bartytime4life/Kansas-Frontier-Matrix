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
MODULE_PATH = ROOT / "tools/validators/evidence/validate_correlation_claim_boundary_assessment.py"
SPEC = importlib.util.spec_from_file_location("correlation_claim_boundary_assessment_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CorrelationClaimBoundaryAssessmentTests(unittest.TestCase):
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
        self.assertEqual(len(results), 31)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_cases_cover_registered_method_vocabulary(self) -> None:
        names = ("pass_association_pearson", "pass_association_spearman", "pass_association_kendall", "pass_association_other_registered")
        candidates = [self._candidate(name) for name in names]
        self.assertEqual({item["statistic"]["method"]["kind"] for item in candidates}, {"PEARSON_R", "SPEARMAN_RHO", "KENDALL_TAU", "OTHER_REGISTERED"})
        self.assertTrue(all(MODULE.validate_candidate(item).outcome == "PASS" for item in candidates))

    def test_resolved_association_does_not_grant_authority(self) -> None:
        candidate = self._candidate("pass_association_pearson")
        self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
        self.assertEqual(candidate["statistic"]["statistic_role"], "RELATIONSHIP_EVIDENCE")
        self.assertTrue(all(value is False for value in candidate["authority_claims"].values()))

    def test_unresolved_bindings_and_ambiguous_wording_abstain(self) -> None:
        names = (
            "abstain_analytic_disclosure_unresolved",
            "abstain_condition_relation_unresolved",
            "abstain_method_registry_unresolved",
            "abstain_uncertainty_unresolved",
            "abstain_wording_ambiguous",
        )
        self.assertTrue(all(MODULE.validate_candidate(self._candidate(name)).outcome == "ABSTAIN" for name in names))

    def test_stronger_roles_never_pass_locally(self) -> None:
        names = (
            "abstain_contribution_without_design",
            "abstain_exposure_design_unresolved",
            "abstain_contribution_design_review",
            "abstain_cause_stronger_design_review",
            "abstain_cause_design_unresolved",
        )
        self.assertTrue(all(MODULE.validate_candidate(self._candidate(name)).outcome == "ABSTAIN" for name in names))

    def test_unsupported_causal_wording_denies(self) -> None:
        expected = {
            "deny_cause_without_design": ["CAUSAL_WORDING_UNSUPPORTED"],
            "deny_cause_observational_design": ["CAUSAL_WORDING_UNSUPPORTED"],
            "deny_association_with_causal_wording": ["CAUSAL_WORDING_UNSUPPORTED"],
            "deny_required_caveat_missing": ["REQUIRED_CAVEAT_MISSING"],
            "deny_public_review_record_missing": ["REVIEW_RECORD_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_replays_and_binds_claim_role(self) -> None:
        candidate = self._candidate("pass_association_pearson")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["claim"]["requested_role"] = "CAUSE"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
