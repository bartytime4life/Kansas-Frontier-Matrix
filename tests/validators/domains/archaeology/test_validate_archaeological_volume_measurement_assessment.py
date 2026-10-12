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

ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = ROOT / "tools/validators/domains/archaeology/validate_archaeological_volume_measurement_assessment.py"
SPEC = importlib.util.spec_from_file_location(
    "archaeological_volume_measurement_assessment_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ArchaeologicalVolumeMeasurementAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        case = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, case)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 26)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_all_finite_outcomes_are_covered(self) -> None:
        self.assertEqual(
            {"PASS", "ABSTAIN", "DENY", "ERROR"},
            {item["outcome"] for item in MODULE.validate_fixture_manifest()},
        )

    def test_pass_is_non_authoritative_coordinate_free_and_separate(self) -> None:
        banned_keys = {"coordinates", "geometry", "latitude", "longitude", "site_location"}
        for name in ("pass_internal_ct_derived", "pass_public_mesh_derived"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertTrue(candidate["assessment_id"].startswith(MODULE.IDENTITY_PREFIX))
            self.assertNotIn(candidate["assessment_id"], candidate["source_documentation"]["input_asset_refs"])
            keys: set[str] = set()

            def collect_keys(value: object) -> None:
                if isinstance(value, dict):
                    keys.update(str(key).lower() for key in value)
                    for item in value.values():
                        collect_keys(item)
                elif isinstance(value, list):
                    for item in value:
                        collect_keys(item)

            collect_keys(candidate)
            self.assertTrue(banned_keys.isdisjoint(keys))

    def test_identity_binds_measurement_and_uncertainty(self) -> None:
        candidate = self._candidate("pass_internal_ct_derived")
        original = MODULE.compute_identity(candidate)
        changed = copy.deepcopy(candidate)
        changed["measurement"]["value"] = 12.5
        self.assertNotEqual(original, MODULE.compute_identity(changed))
        changed = copy.deepcopy(candidate)
        changed["uncertainty"]["upper_bound"] = 13.1
        self.assertNotEqual(original, MODULE.compute_identity(changed))

    def test_method_specific_sources_fail_closed(self) -> None:
        for name in (
            "deny_ct_without_volumetric_input",
            "deny_mesh_without_visual_input",
            "deny_visual_input_undeclared",
            "deny_volumetric_input_undeclared",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_uncertainty_contradictions_fail_closed(self) -> None:
        for name in (
            "deny_quantified_profile_missing",
            "deny_uncertainty_interval_inverted",
            "deny_value_outside_interval",
            "deny_qualitative_statement_missing",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_public_candidate_requires_safety_and_reversible_closure(self) -> None:
        for name in ("deny_public_sensitivity_unresolved", "deny_public_rollback_missing"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_duplicate_and_nonfinite_json_fail_safely(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            nonfinite = Path(directory) / "nonfinite.json"
            duplicate.write_text('{"value":1,"value":2}', encoding="utf-8")
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            self.assertEqual(
                ["JSON_DUPLICATE_KEY"],
                [item.code for item in MODULE.load_json_object(duplicate)[1]],
            )
            self.assertEqual(
                ["JSON_NONFINITE_NUMBER"],
                [item.code for item in MODULE.load_json_object(nonfinite)[1]],
            )

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
