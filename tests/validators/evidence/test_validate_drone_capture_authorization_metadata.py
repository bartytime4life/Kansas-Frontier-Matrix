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

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/evidence/validate_drone_capture_authorization_metadata.py"
SPEC = importlib.util.spec_from_file_location("drone_capture_authorization_metadata_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class DroneCaptureAuthorizationMetadataTests(unittest.TestCase):
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
        self.assertEqual(
            {"PASS", "ABSTAIN", "DENY", "ERROR"},
            {item["outcome"] for item in MODULE.validate_fixture_manifest()},
        )

    def test_pass_is_non_authoritative_and_coordinate_free(self) -> None:
        for name in ("pass_complete_restricted", "pass_withheld_area"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
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
            self.assertTrue({"coordinates", "latitude", "longitude"}.isdisjoint(keys))

    def test_identity_binds_authorization_parameters(self) -> None:
        candidate = self._candidate("pass_complete_restricted")
        original = MODULE.compute_identity(candidate)
        changed = copy.deepcopy(candidate)
        changed["authorization"]["valid_until"] = "2026-06-01T14:59:00Z"
        self.assertNotEqual(original, MODULE.compute_identity(changed))

    def test_temporal_and_altitude_contradictions_fail_closed(self) -> None:
        for name in (
            "deny_capture_window_invalid",
            "deny_authorization_window_invalid",
            "deny_capture_outside_declared_authorization_window",
            "deny_observed_altitude_exceeds_declared_ceiling",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_unresolved_inputs_abstain_without_permission_claim(self) -> None:
        for name in (
            "abstain_authorization_evidence_incomplete",
            "abstain_operating_area_match_unresolved",
            "abstain_altitude_unresolved",
            "abstain_airspace_review_incomplete",
            "abstain_handoff_review_pending",
        ):
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
