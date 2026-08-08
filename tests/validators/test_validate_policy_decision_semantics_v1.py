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

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT / "tools/validators/policy/validate_policy_decision_semantics_v1.py"
)
VALID_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/policy/policy_decision_semantics_v1/valid_answer.json"
)

SPEC = importlib.util.spec_from_file_location(
    "validate_policy_decision_semantics_v1", VALIDATOR_PATH
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PolicyDecisionSemanticsV1Tests(unittest.TestCase):
    def _valid(self) -> dict[str, object]:
        return json.loads(VALID_PATH.read_text(encoding="utf-8"))

    def test_valid_answer_passes(self) -> None:
        self.assertTrue(MODULE.validate_record(VALID_PATH).ok)

    def test_reason_and_obligation_registry_binding(self) -> None:
        unknown_reason = self._valid()
        unknown_reason["reasons"] = ["UNKNOWN_REASON"]
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(unknown_reason).findings},
            {"REASON_CODE_UNKNOWN"},
        )

        wrong_outcome = self._valid()
        wrong_outcome["outcome"] = "DENY"
        wrong_outcome["obligations"] = []
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(wrong_outcome).findings},
            {"REASON_OUTCOME_MISMATCH"},
        )

        wrong_family = self._valid()
        wrong_family["policy_family"] = "consent"
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(wrong_family).findings},
            {"OBLIGATION_FAMILY_MISMATCH", "REASON_FAMILY_MISMATCH"},
        )

    def test_negative_outcomes_require_reasons_and_deny_obligations(self) -> None:
        negative = self._valid()
        negative["outcome"] = "DENY"
        negative["reasons"] = []
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(negative).findings},
            {
                "NEGATIVE_OBLIGATIONS_DENIED",
                "NEGATIVE_REASON_REQUIRED",
                "OBLIGATION_OUTCOME_MISMATCH",
            },
        )

    def test_answer_with_obligation_reason_requires_obligation(self) -> None:
        candidate = self._valid()
        candidate["obligations"] = []
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(candidate).findings},
            {"ANSWER_OBLIGATION_REQUIRED"},
        )

    def test_code_arrays_are_canonical(self) -> None:
        candidate = self._valid()
        candidate["obligations"] = ["GENERALIZE_GEOMETRY", "ATTACH_CITATIONS"]
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(candidate).findings},
            {"OBLIGATIONS_NOT_CANONICAL"},
        )

    def test_cli_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.serialize(VALID_PATH, MODULE.validate_record(VALID_PATH))
            second = MODULE.serialize(VALID_PATH, MODULE.validate_record(VALID_PATH))
        self.assertEqual(first, second)

        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), str(VALID_PATH)],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
