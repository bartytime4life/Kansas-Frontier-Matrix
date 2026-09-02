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
MODULE_PATH = ROOT / "tools/validators/data/validate_map_scale_generalization_disclosure.py"
SPEC = importlib.util.spec_from_file_location("validate_map_scale_generalization_disclosure", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class MapScaleGeneralizationDisclosureTests(unittest.TestCase):
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
        for name in ("pass_zoom_simplification", "pass_scale_denominator_aggregation", "pass_internal_no_generalization"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_profiles_abstain(self) -> None:
        for name in ("abstain_unresolved_validity", "abstain_unresolved_method", "abstain_unknown_precision", "abstain_incomplete_disclosure", "abstain_unresolved_evidence"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_range_basis_and_generalization_obligations_fail_closed(self) -> None:
        expected = {
            "deny_inverted_zoom_range": ["VALIDITY_RANGE_INVERTED"],
            "deny_basis_field_mismatch": ["VALIDITY_BASIS_FIELDS_INCOHERENT"],
            "deny_generalized_without_receipt": ["GENERALIZATION_RECEIPT_REQUIRED"],
            "deny_generalized_without_caveat": ["GENERALIZATION_CAVEAT_REQUIRED"],
            "deny_generalized_without_review": ["GENERALIZATION_REVIEW_REFERENCE_REQUIRED"],
            "deny_noncanonical_arrays": ["ARRAY_NOT_CANONICAL"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_binds_scale_and_method(self) -> None:
        candidate = self._candidate("pass_zoom_simplification")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["validity_context"]["maximum_zoom"] = 13
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_zoom_simplification")
        candidate["generalization"]["method_description"] = "invalid \ud800 text"
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
