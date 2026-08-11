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
MODULE_PATH = ROOT / "tools/validators/validate_aggregate_null_semantics_disclosure.py"
SPEC = importlib.util.spec_from_file_location("validate_aggregate_null_semantics_disclosure", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AggregateNullSemanticsDisclosureTests(unittest.TestCase):
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
        names = (
            "pass_average_excludes_null",
            "pass_row_count_composes_population",
            "pass_distinct_count_composes_population",
            "pass_sum_with_imputation_receipt",
            "pass_ungrouped_minimum",
        )
        for name in names:
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_profiles_abstain(self) -> None:
        names = (
            "abstain_unresolved_aggregate",
            "abstain_unresolved_missingness",
            "abstain_unresolved_query",
            "abstain_unresolved_group_null",
            "abstain_incomplete_disclosure",
        )
        for name in names:
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_aggregate_kind_fields_fail_closed(self) -> None:
        expected = {
            "deny_row_count_with_value_field": ["AGGREGATE_KIND_FIELDS_INCOHERENT"],
            "deny_average_without_value_field": ["AGGREGATE_KIND_FIELDS_INCOHERENT"],
            "deny_average_zero_for_empty_input": ["EMPTY_INPUT_RESULT_INCOHERENT"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_count_population_composition_is_not_duplicated(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_count_without_population_disclosure")).codes,
            ["COUNT_POPULATION_DISCLOSURE_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_noncount_with_population_disclosure")).codes,
            ["COUNT_POPULATION_DISCLOSURE_PROHIBITED"],
        )

    def test_imputation_and_grouping_declarations_fail_closed(self) -> None:
        expected = {
            "deny_imputed_without_receipt": ["IMPUTATION_RECEIPT_REQUIRED"],
            "deny_receipt_without_imputation": ["IMPUTATION_RECEIPT_PROHIBITED"],
            "deny_ungrouped_with_group_behavior": ["GROUP_NULL_SEMANTICS_INCOHERENT"],
            "deny_grouped_as_not_grouped": ["GROUP_NULL_SEMANTICS_INCOHERENT"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_public_disclosure_obligations_fail_closed(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_public_without_disclosure")).codes,
            [
                "DISCLOSURE_SUMMARY_REQUIRED",
                "PUBLIC_DISCLOSURE_REVIEW_REQUIRED",
                "PUBLIC_DISCLOSURE_SURFACE_REQUIRED",
            ],
        )

    def test_profile_hash_binds_null_semantics(self) -> None:
        candidate = self._candidate("pass_average_excludes_null")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["semantics"]["input_null_handling"] = "ERROR"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_average_excludes_null")
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
