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
MODULE_PATH = ROOT / "tools/validators/evidence/validate_choropleth_classification_disclosure.py"
SPEC = importlib.util.spec_from_file_location(
    "choropleth_classification_disclosure_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ChoroplethClassificationDisclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 20)
        self.assertTrue(all(item["ok"] for item in results))

    def test_complete_profiles_pass_without_authority(self) -> None:
        for name in (
            "pass_public_equal_interval",
            "pass_internal_quantile",
            "pass_exploratory_standardized_range",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_incomplete_and_unresolved_profiles_abstain(self) -> None:
        for name in (
            "abstain_incomplete_classification",
            "abstain_unknown_classification",
            "abstain_method_definition_unresolved",
            "abstain_geography_version_unresolved",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_break_and_range_invariants_fail_closed(self) -> None:
        expected = {
            "deny_break_count_mismatch": ["BREAK_COUNT_MISMATCH"],
            "deny_unordered_breaks": ["BREAKS_NOT_STRICTLY_INCREASING"],
            "deny_value_range_break_mismatch": ["VALUE_RANGE_BREAK_MISMATCH"],
            "deny_invalid_value_range": ["VALUE_RANGE_INVALID"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_method_and_treatment_references_fail_closed(self) -> None:
        for name in (
            "deny_manual_rationale_missing",
            "deny_custom_range_reference_missing",
            "deny_imputation_reference_missing",
            "deny_outlier_reference_missing",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_public_candidates_require_review_facing_disclosure(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_public_legend_missing")).codes,
            ["PUBLIC_LEGEND_REFERENCE_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_public_review_missing")).codes,
            ["PUBLIC_REVIEW_REFERENCE_REQUIRED"],
        )

    def test_profile_hash_binds_classification_semantics(self) -> None:
        candidate = self._candidate("pass_public_equal_interval")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["classification"]["break_values"] = ["0", "10", "30", "60", "80", "100"]
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_profile_does_not_carry_values_or_rendered_output(self) -> None:
        candidate = self._candidate("pass_public_equal_interval")
        self.assertNotIn("source_values", candidate)
        self.assertNotIn("rendered_legend", candidate)
        self.assertNotIn("color_ramp", candidate["classification"])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
