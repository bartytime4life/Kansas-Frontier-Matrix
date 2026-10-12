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
MODULE_PATH = ROOT / "tools/validators/validate_recursive_traversal_safety_assessment.py"
SPEC = importlib.util.spec_from_file_location("recursive_traversal_safety_assessment_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RecursiveTraversalSafetyAssessmentTests(unittest.TestCase):
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
        self.assertFalse(schema["x-kfm"]["sql_text_allowed"])
        self.assertFalse(schema["x-kfm"]["database_execution"])
        self.assertNotIn("sql", schema["properties"])
        self.assertNotIn("connection", schema["properties"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 25)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_cases_preserve_guards_receipt_fields_and_no_authority(self) -> None:
        for name in (
            "pass_not_run_declaration",
            "pass_complete_observation",
            "pass_cycle_stopped_and_reported",
            "pass_synthetic_dialect_parity",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertTrue(all(value is False for value in candidate["authority_claims"].values()))
        complete = self._candidate("pass_complete_observation")
        self.assertIn("recursion_depth", complete["observation"])
        self.assertIn("cycle_detected", complete["observation"])
        self.assertIsNotNone(complete["observation"]["receipt_ref"])

    def test_unresolved_and_truncated_declarations_abstain(self) -> None:
        for name in (
            "abstain_assessment_incomplete",
            "abstain_query_definition_unresolved",
            "abstain_termination_predicate_unresolved",
            "abstain_dialect_parity_unresolved",
            "abstain_depth_limit_reached",
            "abstain_cycle_policy",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_cycle_depth_and_parity_guards_fail_closed(self) -> None:
        expected = {
            "deny_cycle_strategy_none": ["CYCLE_STRATEGY_REQUIRED"],
            "deny_cycle_ignore": ["CYCLE_IGNORE_DENIED"],
            "deny_silent_partial_depth_limit": ["SILENT_PARTIAL_DENIED"],
            "deny_cycle_identity_outside_traversal_identity": ["CYCLE_IDENTITY_OUTSIDE_TRAVERSAL_IDENTITY"],
            "deny_synthetic_parity_fixture_missing": ["PARITY_FIXTURE_MISSING"],
            "deny_dialect_parity_mismatch": ["DIALECT_PARITY_MISMATCH"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_observation_bounds_state_timestamp_and_identity_fail_closed(self) -> None:
        expected = {
            "deny_not_run_observation_present": ["NOT_RUN_OBSERVATION_PRESENT"],
            "deny_executed_observation_incomplete": ["EXECUTED_OBSERVATION_INCOMPLETE", "OBSERVATION_STATE_MISMATCH"],
            "deny_observed_depth_exceeds_cap": ["DEPTH_CAP_EXCEEDED"],
            "deny_observed_nodes_exceed_cap": ["NODE_CAP_EXCEEDED"],
            "deny_complete_observation_cycle_flag": ["OBSERVATION_STATE_MISMATCH"],
            "deny_non_utc_timestamp": ["UTC_TIMESTAMP_REQUIRED"],
            "deny_profile_hash_tamper": ["PROFILE_SPEC_HASH_MISMATCH"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_replays_and_binds_guard_semantics(self) -> None:
        candidate = self._candidate("pass_not_run_declaration")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["guard_profile"]["max_depth"] = 31
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
