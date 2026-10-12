from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_recommendation_decision_authority_assessment.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/recommendation_decision_authority_assessment.schema.json"

spec = importlib.util.spec_from_file_location(
    "validate_recommendation_decision_authority_assessment",
    VALIDATOR_PATH,
)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class RecommendationDecisionAuthorityAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = validator.load_fixture_cases()
        cls.by_name = {
            raw_case["name"]: (raw_case, candidate)
            for raw_case, candidate in cls.cases
        }

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        observed = {"PASS": 0, "DENY": 0, "ERROR": 0}
        for raw_case, candidate in self.cases:
            result = validator.validate_payload(candidate)
            observed[result.outcome] += 1
            self.assertEqual(result.outcome, raw_case["expected_outcome"], raw_case["name"])
            self.assertEqual(
                [finding.code for finding in result.findings],
                raw_case["expected_findings"],
                raw_case["name"],
            )
        self.assertEqual(observed, {"PASS": 7, "DENY": 11, "ERROR": 1})

    def test_identity_is_stable_across_mapping_order(self) -> None:
        candidate = self.by_name["valid_adopted_as_recommended"][1]
        reordered = {key: candidate[key] for key in reversed(list(candidate.keys()))}
        self.assertEqual(validator.canonical_spec_hash(reordered), candidate["spec_hash"])
        self.assertEqual(validator.expected_assessment_id(reordered), candidate["assessment_id"])

    def test_recommendation_without_decision_remains_valid_and_advisory(self) -> None:
        candidate = self.by_name["valid_no_decision"][1]
        self.assertEqual(candidate["recommendation"]["state"], "ISSUED")
        self.assertEqual(candidate["decision"]["state"], "NO_DECISION_RECORDED")
        self.assertEqual(candidate["linkage"]["disposition"], "NO_DECISION")
        self.assertEqual(candidate["effects"], validator.FALSE_EFFECTS)
        self.assertTrue(validator.validate_payload(candidate).ok)

    def test_adoption_with_changes_requires_explicit_comparison(self) -> None:
        valid = self.by_name["valid_adopted_with_changes"][1]
        invalid = self.by_name["changes_without_comparison"][1]
        self.assertIsNotNone(valid["linkage"]["comparison_digest"])
        self.assertTrue(validator.validate_payload(valid).ok)
        self.assertEqual(
            [finding.code for finding in validator.validate_payload(invalid).findings],
            ["CHANGE_COMPARISON_REQUIRED"],
        )

    def test_decision_implementation_and_outcome_links_do_not_collapse(self) -> None:
        candidate = self.by_name["valid_downstream_references_remain_non_effects"][1]
        self.assertTrue(candidate["decision"]["decision_ref"])
        self.assertTrue(candidate["linkage"]["implementation_refs"])
        self.assertTrue(candidate["linkage"]["outcome_observation_refs"])
        self.assertFalse(candidate["effects"]["implementation_started"])
        self.assertFalse(candidate["effects"]["outcome_measured"])
        self.assertTrue(validator.validate_payload(candidate).ok)

    def test_outcome_without_implementation_fails_closed(self) -> None:
        result = validator.validate_payload(self.by_name["outcome_without_implementation"][1])
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            [finding.code for finding in result.findings],
            ["OUTCOME_WITHOUT_IMPLEMENTATION"],
        )

    def test_duplicate_json_key_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"profile":"a","profile":"b"}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings, (validator.Finding("JSON_DUPLICATE_KEY", "/"),))

    def test_nonfinite_json_number_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings, (validator.Finding("JSON_NONFINITE_NUMBER", "/"),))

    def test_symlink_input_is_denied(self) -> None:
        if not hasattr(os, "symlink"):
            self.skipTest("symbolic links are unavailable")
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            result = validator.validate_file(link)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings, (validator.Finding("INPUT_SYMLINK_DENIED", "/"),))

    def test_validator_has_no_network_policy_or_workflow_client_import(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        forbidden = (
            "import requests",
            "import httpx",
            "import aiohttp",
            "import socket",
            "from urllib",
            "urlopen(",
            "googleapiclient",
            "subprocess.Popen",
        )
        self.assertFalse(any(token in source for token in forbidden))

    def test_cli_pass_is_value_free_and_authority_free(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.json"
            path.write_text(
                json.dumps(self.by_name["valid_adopted_as_recommended"][1]),
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), str(path)],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["findings"], [])
        self.assertEqual(set(payload["authority"].values()), {False})
        self.assertNotIn("synthetic-planning-board", completed.stdout)
        self.assertNotIn("2026-08-01T18:00:00Z", completed.stdout)

    def test_fixture_cli_replays_every_case(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        rows = [json.loads(line) for line in completed.stdout.splitlines() if line.strip()]
        self.assertEqual(len(rows), 19)
        self.assertEqual({row["outcome"] for row in rows}, {"PASS", "DENY", "ERROR"})


if __name__ == "__main__":
    unittest.main()
