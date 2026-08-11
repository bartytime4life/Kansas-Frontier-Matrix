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
MODULE_PATH = ROOT / "tools/validators/release/validate_api_developer_experience_readiness_assessment.py"
SPEC = importlib.util.spec_from_file_location("api_dx_readiness_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ApiDeveloperExperienceReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        case = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, case)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 28)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_all_finite_outcomes_are_covered(self) -> None:
        self.assertEqual(
            {"PASS", "ABSTAIN", "DENY", "ERROR"},
            {item["outcome"] for item in MODULE.validate_fixture_manifest()},
        )

    def test_pass_remains_declarative_and_non_authoritative(self) -> None:
        for name in ("pass_public_candidate", "pass_internal_candidate"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertFalse(candidate["prototype_validation"]["runtime_behavior_claimed"])

    def test_negative_outcome_examples_are_required(self) -> None:
        for name in (
            "deny_outcome_example_missing",
            "deny_citation_duty_undisclosed",
            "deny_policy_semantics_undisclosed",
            "deny_failure_mode_missing",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_prototypes_cannot_claim_runtime_behavior(self) -> None:
        for name in (
            "deny_prototype_fixture_missing",
            "deny_consumer_validation_missing",
            "deny_prototype_receipt_missing",
            "deny_runtime_behavior_claim",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_profile_hash_binds_readiness_declarations(self) -> None:
        candidate = self._candidate("pass_public_candidate")
        original = MODULE.compute_profile_hash(candidate)
        changed = copy.deepcopy(candidate)
        changed["onboarding"]["getting_started_ref"] = "fixture:api-doc:different-getting-started"
        self.assertNotEqual(original, MODULE.compute_profile_hash(changed))

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
