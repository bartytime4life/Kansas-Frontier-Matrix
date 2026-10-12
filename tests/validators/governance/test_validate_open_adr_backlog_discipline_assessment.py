from __future__ import annotations

import copy
import importlib.util
import json
import os
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
TOOL = ROOT / "tools/validators/governance/validate_open_adr_backlog_discipline_assessment.py"
SCHEMA = ROOT / "schemas/contracts/v1/governance/open_adr_backlog_discipline_assessment.schema.json"
SPEC = importlib.util.spec_from_file_location("open_adr_backlog_validator", TOOL)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class OpenAdrBacklogDisciplineAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads(MODULE.VALID_FIXTURE.read_text(encoding="utf-8"))
        cls.cases = json.loads(MODULE.CASES.read_text(encoding="utf-8"))

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA.read_text(encoding="utf-8")))

    def test_valid_fixture_passes_without_authority(self) -> None:
        result = MODULE.validate_candidate(self.base)
        self.assertEqual(result, MODULE.Result("PASS", ()))
        self.assertFalse(any(self.base["effects"].values()))

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_matrix()
        self.assertEqual(len(results), len(self.cases))
        self.assertTrue(all(result["suite_match"] for result in results), results)

    def test_finite_outcomes_are_covered(self) -> None:
        outcomes = {result["outcome"] for result in MODULE.validate_fixture_matrix()}
        self.assertEqual(outcomes, {"PASS", "ABSTAIN", "DENY", "ERROR"})

    def test_identity_binds_declared_semantics(self) -> None:
        self.assertEqual(self.base["assessment_id"], MODULE.expected_id(self.base))
        changed = copy.deepcopy(self.base)
        changed["entries"][0]["decision_class"] = "REVIEW_DUTY"
        self.assertNotEqual(self.base["assessment_id"], MODULE.expected_id(changed))

    def test_supersession_cycle_is_denied(self) -> None:
        case = next(case for case in self.cases if case["name"] == "deny_supersession_cycle")
        result = MODULE.validate_candidate(MODULE.materialize_case(self.base, case))
        self.assertEqual(
            result,
            MODULE.Result(
                "DENY",
                (
                    MODULE.Finding("SUPERSESSION_CYCLE", "/entries/0/superseded_by"),
                    MODULE.Finding("SUPERSESSION_CYCLE", "/entries/1/superseded_by"),
                ),
            ),
        )

    def test_evaluation_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_matrix()
            second = MODULE.validate_fixture_matrix()
        self.assertEqual(first, second)

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            _, findings = MODULE.read_json_object(duplicate)
            self.assertEqual(findings, (MODULE.Finding("JSON_DUPLICATE_KEY", "/"),))
            nonfinite = Path(directory) / "nonfinite.json"
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            _, findings = MODULE.read_json_object(nonfinite)
            self.assertEqual(findings, (MODULE.Finding("JSON_NONFINITE_NUMBER", "/"),))

    def test_diagnostics_do_not_echo_declared_values(self) -> None:
        case = next(case for case in self.cases if case["name"] == "deny_resolved_without_adr")
        result = MODULE.validate_candidate(MODULE.materialize_case(self.base, case))
        serialized = MODULE.serialize(None, result)
        self.assertIn("RESOLUTION_ADR_REQUIRED", serialized)
        self.assertNotIn("fixture-resolution-record-03", serialized)

    def test_cli_valid_fixture(self) -> None:
        environment = os.environ.copy()
        environment["KFM_NO_NETWORK"] = "1"
        completed = subprocess.run(
            [sys.executable, str(TOOL), str(MODULE.VALID_FIXTURE)],
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn('"outcome":"PASS"', completed.stdout)

    def test_fixture_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(TOOL), "--fixtures"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)


if __name__ == "__main__":
    unittest.main()
