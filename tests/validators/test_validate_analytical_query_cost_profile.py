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

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/validate_analytical_query_cost_profile.py"
SPEC = importlib.util.spec_from_file_location("validate_analytical_query_cost_profile", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AnalyticalQueryCostProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.cases = {entry["name"]: entry for entry in cls.manifest["cases"]}

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self.cases[name])

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), len(self.cases))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_profiles_remain_non_authoritative(self) -> None:
        for name in (
            "pass_measured_resource_budget",
            "pass_billing_profile_reference",
            "pass_public_candidate_with_review",
            "pass_no_index_assumption",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertFalse(candidate["plan_capture"]["raw_plan_stored"])
            self.assertFalse(candidate["plan_capture"]["raw_sql_stored"])

    def test_unresolved_profiles_abstain(self) -> None:
        for name in (
            "abstain_unresolved_engine",
            "abstain_unresolved_input_scope",
            "abstain_plan_not_captured",
            "abstain_unresolved_indexes",
            "abstain_unresolved_cost_posture",
            "abstain_not_run",
            "abstain_unknown_disclosure",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_resource_and_result_drift_fail_closed(self) -> None:
        expected = {
            "deny_input_estimate_exceeds_budget": ["INPUT_ESTIMATE_EXCEEDS_BUDGET"],
            "deny_observation_incomplete": ["OBSERVATION_INCOMPLETE"],
            "deny_budget_exceeded": ["BUDGET_EXCEEDED"],
            "deny_budget_result_drift": ["BUDGET_RESULT_MISMATCH"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_plan_index_billing_and_public_obligations_fail_closed(self) -> None:
        expected = {
            "deny_plan_capture_incoherent": ["PLAN_CAPTURE_INCOHERENT"],
            "deny_index_state_incoherent": ["INDEX_STATE_INCOHERENT"],
            "deny_billing_profile_missing": ["BILLING_PROFILE_REQUIRED"],
            "deny_public_without_review": ["PUBLIC_DISCLOSURE_REVIEW_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_binds_budget_and_observation(self) -> None:
        candidate = self._candidate("pass_measured_resource_budget")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["budget"]["max_duration_ms"] = 851
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_recorded_execution_error_is_finite_error(self) -> None:
        result = MODULE.validate_candidate(self._candidate("error_recorded_execution"))
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["OBSERVATION_RECORDED_ERROR"])

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_measured_resource_budget")
        candidate["disclosure"]["summary"] = "invalid \ud800 text"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["JSON_UNPAIRED_SURROGATE"])
        with self.assertRaises(MODULE.UnpairedSurrogateError):
            MODULE.compute_profile_hash(candidate)

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            _, findings = MODULE.load_json_object(duplicate)
            self.assertEqual([item.code for item in findings], ["JSON_DUPLICATE_KEY"])
            nonfinite = Path(directory) / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            _, findings = MODULE.load_json_object(nonfinite)
            self.assertEqual([item.code for item in findings], ["JSON_NONFINITE_NUMBER"])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
