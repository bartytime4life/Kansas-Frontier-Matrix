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

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/validate_elapsed_time_unit_disclosure.py"
SPEC = importlib.util.spec_from_file_location("elapsed_time_unit_disclosure_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ElapsedTimeUnitDisclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(entry for entry in self.manifest["cases"] if entry["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_valid_closed_value_free_and_inactive(self) -> None:
        schema = MODULE._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertFalse(schema["x-kfm"]["network"])
        self.assertFalse(schema["x-kfm"]["timestamp_values_allowed"])
        self.assertFalse(schema["x-kfm"]["elapsed_values_allowed"])
        self.assertFalse(schema["x-kfm"]["sql_text_allowed"])
        self.assertNotIn("elapsed_value", schema["properties"])
        self.assertNotIn("sql", schema["properties"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 31)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_cases_cover_exact_fixed_calendar_and_internal_profiles(self) -> None:
        for name in (
            "pass_seconds_to_hours",
            "pass_hours_to_minutes",
            "pass_identity_units",
            "pass_synthetic_engine_parity",
            "pass_calendar_month_identity",
            "pass_internal_disclosure_candidate",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertTrue(all(value is False for value in candidate["authority_claims"].values()))
        conversion = self._candidate("pass_seconds_to_hours")["conversion"]
        self.assertEqual((conversion["conversion_numerator"], conversion["conversion_denominator"]), (1, 3600))

    def test_unresolved_declarations_abstain(self) -> None:
        for name in (
            "abstain_assessment_incomplete",
            "abstain_query_run_unresolved",
            "abstain_timezone_assumption_unresolved",
            "abstain_engine_profile_unresolved",
            "abstain_engine_parity_unresolved",
            "abstain_boundary_profile_unresolved",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_unit_calendar_boundary_sign_and_null_rules_fail_closed(self) -> None:
        expected = {
            "deny_unit_conversion_mismatch": ["UNIT_CONVERSION_MISMATCH"],
            "deny_conversion_fraction_not_reduced": ["CONVERSION_FRACTION_NOT_REDUCED"],
            "deny_calendar_cross_unit_conversion": ["CALENDAR_UNIT_CONVERSION_DENIED"],
            "deny_calendar_unit_instant_semantics": ["CALENDAR_UNIT_BOUNDARY_SEMANTICS_REQUIRED"],
            "deny_boundary_profile_unexpected": ["BOUNDARY_PROFILE_UNEXPECTED"],
            "deny_boundary_profile_missing": ["BOUNDARY_PROFILE_REQUIRED"],
            "deny_absolute_value_direction_loss": ["ABSOLUTE_VALUE_DIRECTION_LOSS"],
            "deny_null_interval_drop": ["NULL_INTERVAL_DROP_DENIED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_parity_public_timestamp_rounding_and_identity_rules_fail_closed(self) -> None:
        expected = {
            "deny_engine_parity_mismatch": ["ENGINE_PARITY_MISMATCH"],
            "deny_synthetic_parity_fixture_missing": ["PARITY_FIXTURE_MISSING"],
            "deny_single_engine_parity_fixture_unexpected": ["PARITY_FIXTURE_UNEXPECTED"],
            "deny_public_disclosure_incomplete": ["PUBLIC_DISCLOSURE_INCOMPLETE"],
            "deny_public_candidate_references_missing": ["PUBLIC_CANDIDATE_REFERENCE_MISSING"],
            "deny_timestamp_field_collision": ["TIMESTAMP_FIELD_COLLISION"],
            "deny_rounding_declaration_mismatch": ["ROUNDING_DECLARATION_MISMATCH"],
            "deny_non_utc_timestamp": ["UTC_TIMESTAMP_REQUIRED"],
            "deny_profile_hash_tamper": ["PROFILE_SPEC_HASH_MISMATCH"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_replays_and_binds_conversion_semantics(self) -> None:
        candidate = self._candidate("pass_seconds_to_hours")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["conversion"]["conversion_denominator"] = 60
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_input_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            link.symlink_to(target)
            self.assertEqual(MODULE.load_json_object(duplicate)[1][0].code, "JSON_DUPLICATE_KEY")
            self.assertEqual(MODULE.load_json_object(nonfinite)[1][0].code, "JSON_NONFINITE_NUMBER")
            self.assertEqual(MODULE.load_json_object(link)[1][0].code, "INPUT_SYMLINK_DENIED")

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
