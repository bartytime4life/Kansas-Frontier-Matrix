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

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/map/validate_cartographic_communication_risk_assessment.py"
SPEC = importlib.util.spec_from_file_location("validate_cartographic_communication_risk_assessment", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CartographicCommunicationRiskAssessmentTests(unittest.TestCase):
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
            "pass_all_axes_acceptable",
            "pass_mitigated_scale",
            "pass_classification_not_applicable",
            "pass_high_consequence_reviewed",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_declarations_abstain(self) -> None:
        expected = {
            "abstain_selection_unresolved": ["SELECTION_RISK_UNRESOLVED"],
            "abstain_support_unresolved": ["SUPPORTING_ASSESSMENT_UNRESOLVED"],
            "abstain_review_pending": ["REVIEW_PENDING"],
            "abstain_consequence_unresolved": ["CONSEQUENCE_UNRESOLVED"],
            "abstain_review_unknown": ["REVIEW_UNKNOWN"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_misleading_axis_fails_closed(self) -> None:
        result = MODULE.validate_candidate(self._candidate("deny_selection_misleading"))
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(result.codes, ["SELECTION_RISK_MISLEADING"])

    def test_mitigation_references_are_state_bound(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_mitigation_without_reference")).codes,
            ["MITIGATION_REFERENCE_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_reference_without_mitigation")).codes,
            ["MITIGATION_REFERENCE_PROHIBITED"],
        )

    def test_supporting_assessment_bindings_fail_closed(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_not_applicable_with_binding")).codes,
            ["SUPPORTING_ASSESSMENT_BINDING_PROHIBITED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_resolved_without_digest")).codes,
            ["SUPPORTING_ASSESSMENT_BINDING_REQUIRED"],
        )

    def test_review_records_and_timestamps_are_canonical(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_noncanonical_review_refs")).codes,
            ["ARRAY_NOT_CANONICAL"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_non_utc_observed_at")).codes,
            ["OBSERVED_AT_NOT_UTC"],
        )

    def test_profile_hash_binds_review_axes(self) -> None:
        candidate = self._candidate("pass_all_axes_acceptable")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["risk_review"]["axes"][0]["state"] = "MISLEADING"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_all_axes_acceptable")
        candidate["risk_review"]["communication_summary"] = "invalid \ud800 text"
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
