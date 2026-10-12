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
MODULE_PATH = ROOT / "tools/validators/evidence/validate_planning_proxy_uncertainty_assessment.py"
SPEC = importlib.util.spec_from_file_location("planning_proxy_uncertainty_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PlanningProxyUncertaintyAssessmentTests(unittest.TestCase):
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
        self.assertEqual(len(results), 15)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_complete_profiles_pass(self) -> None:
        for name in ("pass_data_poor_proxy_disclosed", "pass_sufficient_without_proxy"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "PASS")

    def test_unresolved_profiles_abstain(self) -> None:
        for name in (
            "abstain_unresolved_evidence",
            "abstain_incomplete_assessment",
            "abstain_unknown_proxy_fitness",
            "abstain_unknown_uncertainty",
            "abstain_decision_support_high_uncertainty",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_proxy_and_disclosure_fail_closed(self) -> None:
        expected = {
            "deny_data_poor_without_proxy": ["PROXY_REQUIRED_FOR_DATA_POOR"],
            "deny_proxy_uncertainty_hidden": ["UNCERTAINTY_DISCLOSURE_REQUIRED"],
            "deny_limited_without_limitation": ["PROXY_LIMITATION_REQUIRED"],
            "deny_primary_proxy_overconfidence": ["PRIMARY_PROXY_OVERCONFIDENCE"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_quantification_completeness_and_order_fail_closed(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_quantified_without_method")).codes,
            ["UNCERTAINTY_METHOD_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_complete_with_known_gap")).codes,
            ["COMPLETENESS_CLAIM_INCOHERENT"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_noncanonical_proxy_ids")).codes,
            ["PROXIES_NOT_CANONICAL"],
        )

    def test_profile_hash_replays_and_binds_semantics(self) -> None:
        candidate = self._candidate("pass_data_poor_proxy_disclosed")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["assessment"]["scope_statement"] = "A materially different synthetic planning scope."
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
