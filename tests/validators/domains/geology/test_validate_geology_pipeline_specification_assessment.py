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
MODULE_PATH = ROOT / "tools/validators/validate_geology_pipeline_specification_assessment.py"
SPEC = importlib.util.spec_from_file_location("geology_pipeline_specification_assessment_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class GeologyPipelineSpecificationAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        case = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, case)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 30)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_all_finite_outcomes_are_covered(self) -> None:
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, {item["outcome"] for item in MODULE.validate_fixture_manifest()})

    def test_pass_is_inactive_non_authoritative_and_geometry_free(self) -> None:
        banned_keys = {"coordinates", "geometry", "latitude", "longitude", "site_location"}
        for name in ("pass_bedrock_units", "pass_borehole_controlled", "pass_well_log_controlled", "pass_cross_section_interpreted", "pass_mineral_occurrence"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertEqual(candidate["source_bindings"]["source_activation_state"], "INACTIVE")
            self.assertEqual(candidate["lifecycle"]["execution_mode"], "FIXTURE_ONLY")
            self.assertFalse(candidate["lifecycle"]["network_access"])
            self.assertFalse(candidate["lifecycle"]["source_material_access"])
            self.assertFalse(any(candidate["authority_claims"].values()))
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

    def test_identity_binds_source_role_and_spatial_scope(self) -> None:
        candidate = self._candidate("pass_bedrock_units")
        original = MODULE.compute_identity(candidate)
        changed = copy.deepcopy(candidate)
        changed["source_bindings"]["source_roles"] = ["AUTHORITATIVE_MAP", "SYNTHETIC_FIXTURE"]
        self.assertNotEqual(original, MODULE.compute_identity(changed))
        changed = copy.deepcopy(candidate)
        changed["spatial_temporal"]["map_scale_denominator"] = 50000
        self.assertNotEqual(original, MODULE.compute_identity(changed))

    def test_profile_specific_boundaries_fail_closed(self) -> None:
        names = (
            "deny_bedrock_wrong_role",
            "deny_bedrock_point_support",
            "deny_borehole_public_posture",
            "deny_borehole_missing_depth",
            "deny_well_log_missing_vertical_datum",
            "deny_cross_section_observation_only",
            "deny_mineral_resource_class_collapse",
        )
        for name in names:
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_no_profile_can_upgrade_run_or_carrier_to_truth(self) -> None:
        for base in ("bedrock", "borehole", "well_log", "cross_section", "mineral_occurrence"):
            candidate = MODULE._resolve_base(MANIFEST, base)
            assertions = set(candidate["domain_semantics"]["anti_collapse_assertions"])
            self.assertIn("SUCCESSFUL_RUN_NOT_EVIDENCE_OR_RELEASE", assertions)
            self.assertFalse(candidate["authority_claims"]["geologic_truth_authority"])
            self.assertFalse(candidate["authority_claims"]["resource_classification_authority"])

    def test_unresolved_rights_or_sensitivity_abstains(self) -> None:
        for name in ("abstain_rights_unresolved", "abstain_sensitivity_unresolved"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_duplicate_and_nonfinite_json_fail_safely(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            nonfinite = Path(directory) / "nonfinite.json"
            duplicate.write_text('{"value":1,"value":2}', encoding="utf-8")
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            self.assertEqual(["JSON_DUPLICATE_KEY"], [item.code for item in MODULE.load_json_object(duplicate)[1]])
            self.assertEqual(["JSON_NONFINITE_NUMBER"], [item.code for item in MODULE.load_json_object(nonfinite)[1]])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
