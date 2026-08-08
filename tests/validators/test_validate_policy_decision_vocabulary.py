from __future__ import annotations

import copy
import importlib.util
import json
import socket
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT / "tools/validators/policy/validate_policy_decision_vocabulary.py"
)
SCHEMA_PATH = (
    REPO_ROOT / "schemas/contracts/v1/policy/policy_decision_vocabulary.schema.json"
)
REGISTRY_PATH = REPO_ROOT / "policy/decision/vocabulary.v1.json"

SPEC = importlib.util.spec_from_file_location(
    "validate_policy_decision_vocabulary", VALIDATOR_PATH
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PolicyDecisionVocabularyTests(unittest.TestCase):
    def _registry(self) -> dict[str, object]:
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    def test_schema_is_closed_and_inactive(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["execution_mode"], "FIXTURE_ONLY")

    def test_registry_passes(self) -> None:
        self.assertTrue(MODULE.validate_record(REGISTRY_PATH).ok)

    def test_code_sets_are_sorted_unique_and_disjoint(self) -> None:
        registry = self._registry()
        reasons = [item["code"] for item in registry["reason_codes"]]
        obligations = [item["code"] for item in registry["obligation_codes"]]
        self.assertEqual(reasons, sorted(set(reasons)))
        self.assertEqual(obligations, sorted(set(obligations)))
        self.assertFalse(set(reasons).intersection(obligations))

    def test_semantic_negative_polarity(self) -> None:
        registry = self._registry()

        unsorted = copy.deepcopy(registry)
        unsorted["reason_codes"][0], unsorted["reason_codes"][1] = (
            unsorted["reason_codes"][1],
            unsorted["reason_codes"][0],
        )
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(unsorted).findings},
            {"REASON_CODES_NOT_CANONICAL"},
        )

        collision = copy.deepcopy(registry)
        collision["obligation_codes"].append({
            "code": "RIGHTS_UNKNOWN",
            "applicable_outcomes": ["ANSWER"],
            "policy_families": ["access"],
            "description": "Synthetic namespace collision.",
        })
        collision["obligation_codes"].sort(key=lambda item: item["code"])
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(collision).findings},
            {"CODE_NAMESPACE_COLLISION"},
        )

        wrong_outcome = copy.deepcopy(registry)
        wrong_outcome["obligation_codes"][0]["applicable_outcomes"] = ["ABSTAIN"]
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(wrong_outcome).findings},
            {"OBLIGATION_OUTCOME_UNSUPPORTED"},
        )

        overclaim = copy.deepcopy(registry)
        overclaim["governance"]["policy_evaluation"] = True
        self.assertIn(
            "SCHEMA_INVALID",
            {item.code for item in MODULE.validate_payload(overclaim).findings},
        )

    def test_cli_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.serialize(
                REGISTRY_PATH, MODULE.validate_record(REGISTRY_PATH)
            )
            second = MODULE.serialize(
                REGISTRY_PATH, MODULE.validate_record(REGISTRY_PATH)
            )
        self.assertEqual(first, second)

        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--registry"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 1)

    def test_governance_flags_deny_authority(self) -> None:
        self.assertTrue(
            all(value is False for value in self._registry()["governance"].values())
        )


if __name__ == "__main__":
    unittest.main()
