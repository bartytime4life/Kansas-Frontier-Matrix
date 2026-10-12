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
VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/validate_conditions_source_role_readiness_matrix.py"
)
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/common/conditions_source_role_readiness_matrix.schema.json"
)


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


matrix = _load_module("conditions_source_role_matrix_validator", VALIDATOR_PATH)
classification = _load_module(
    "conditions_matrix_classification_validator",
    REPO_ROOT / "tools/validators/validate_classification_release.py",
)
forecast = _load_module(
    "conditions_matrix_forecast_validator",
    REPO_ROOT / "tools/validators/validate_forecast_product.py",
)
soil = _load_module(
    "conditions_matrix_soil_validator",
    REPO_ROOT
    / "tools/validators/domains/soil/validate_domain_observation.py",
)


class ConditionsSourceRoleReadinessMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = matrix.load_fixture_cases()
        cls.by_name = {
            raw_case["name"]: (raw_case, candidate)
            for raw_case, candidate in cls.cases
        }
        cls.valid = cls.by_name["valid_partial_readiness"][1]

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        observed = {"PASS": 0, "DENY": 0, "ERROR": 0}
        for raw_case, candidate in self.cases:
            result = matrix.validate_payload(candidate)
            observed[result.outcome] += 1
            self.assertEqual(result.outcome, raw_case["expected_outcome"], raw_case["name"])
            self.assertEqual(
                [finding.code for finding in result.findings],
                raw_case["expected_findings"],
                raw_case["name"],
            )
        self.assertEqual(observed, {"PASS": 1, "DENY": 10, "ERROR": 1})

    def test_role_set_is_complete_canonical_and_partially_ready(self) -> None:
        bindings = self.valid["bindings"]
        self.assertEqual(
            [binding["role"] for binding in bindings],
            list(matrix.ROLE_ORDER),
        )
        self.assertEqual(
            {binding["role"] for binding in bindings if binding["readiness"] == "BOUND"},
            {"CLASSIFICATION", "FORECAST", "OBSERVATION"},
        )
        self.assertEqual(
            {binding["role"] for binding in bindings if binding["readiness"] == "HOLD"},
            {"AGGREGATE", "MODEL", "SURVEY"},
        )
        self.assertEqual(self.valid["matrix_outcome"], "PARTIAL_READY")

    def test_bound_paths_exist_and_holds_have_no_binding(self) -> None:
        for binding in self.valid["bindings"]:
            if binding["readiness"] == "BOUND":
                for field in matrix.PATH_FIELDS:
                    self.assertTrue((REPO_ROOT / binding[field]).is_file())
                self.assertEqual(binding["reason_codes"], [])
            else:
                for field in matrix.PATH_FIELDS + matrix.MAPPING_FIELDS:
                    self.assertIsNone(binding[field])
                self.assertTrue(binding["reason_codes"])

    def test_selected_profile_fixtures_pass_their_own_validators(self) -> None:
        classification_candidate = next(
            candidate
            for raw_case, candidate in classification.load_fixture_cases()
            if raw_case["name"] == "valid_current"
        )
        forecast_candidate = next(
            candidate
            for raw_case, candidate in forecast.load_fixture_cases()
            if raw_case["name"] == "valid_model_current"
        )
        soil_cases = json.loads(
            (
                REPO_ROOT
                / "fixtures/domains/soil/domain_observation/cases.json"
            ).read_text(encoding="utf-8")
        )["cases"]
        observation_candidate = next(
            case["candidate"] for case in soil_cases if case["name"] == "valid_station"
        )

        self.assertTrue(classification.validate_payload(classification_candidate).ok)
        self.assertTrue(forecast.validate_payload(forecast_candidate).ok)
        soil_outcome, soil_findings = soil.evaluate(observation_candidate)
        self.assertEqual((soil_outcome, soil_findings), ("PASS", []))

    def test_selected_profiles_fail_closed_under_cross_substitution(self) -> None:
        classification_candidate = next(
            candidate
            for raw_case, candidate in classification.load_fixture_cases()
            if raw_case["name"] == "valid_current"
        )
        forecast_candidate = next(
            candidate
            for raw_case, candidate in forecast.load_fixture_cases()
            if raw_case["name"] == "valid_model_current"
        )
        self.assertNotEqual(
            classification.validate_payload(forecast_candidate).outcome,
            "PASS",
        )
        self.assertNotEqual(
            forecast.validate_payload(classification_candidate).outcome,
            "PASS",
        )

    def test_condition_relation_vocabulary_matches_bound_common_pairs(self) -> None:
        relation = json.loads(
            (
                REPO_ROOT
                / "fixtures/contracts/v1/common/condition_relation/valid/observation_classification_answer.json"
            ).read_text(encoding="utf-8")
        )
        relation_pairs = {
            (endpoint["source_role"], endpoint["support_type"])
            for endpoint in (relation["left"], relation["right"])
        }
        bound_pairs = {
            (binding["common_source_role"], binding["common_support_type"])
            for binding in self.valid["bindings"]
            if binding["role"] in {"CLASSIFICATION", "OBSERVATION"}
        }
        self.assertEqual(bound_pairs, relation_pairs)

    def test_identity_is_stable_across_mapping_key_order(self) -> None:
        reordered = {key: self.valid[key] for key in reversed(list(self.valid))}
        self.assertEqual(matrix.canonical_spec_hash(reordered), self.valid["spec_hash"])
        self.assertEqual(matrix.expected_matrix_id(reordered), self.valid["matrix_id"])

    def test_duplicate_json_key_and_symlink_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"profile":"a","profile":"b"}', encoding="utf-8")
            duplicate_result = matrix.validate_file(duplicate)
            self.assertEqual(duplicate_result.outcome, "ERROR")
            self.assertEqual(
                duplicate_result.findings,
                (matrix.Finding("JSON_DUPLICATE_KEY", "/"),),
            )

            if hasattr(os, "symlink"):
                target = Path(directory) / "target.json"
                target.write_text("{}", encoding="utf-8")
                link = Path(directory) / "link.json"
                link.symlink_to(target)
                link_result = matrix.validate_file(link)
                self.assertEqual(link_result.outcome, "ERROR")
                self.assertEqual(
                    link_result.findings,
                    (matrix.Finding("INPUT_SYMLINK_DENIED", "/"),),
                )

    def test_validator_has_no_network_client_import(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        forbidden = (
            "import requests",
            "import httpx",
            "import aiohttp",
            "import socket",
            "from urllib",
            "urlopen(",
        )
        self.assertFalse(any(token in source for token in forbidden))

    def test_cli_pass_is_bounded_and_value_free(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.json"
            path.write_text(json.dumps(self.valid), encoding="utf-8")
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
        self.assertNotIn("direct_observation_measurement", completed.stdout)
        self.assertNotIn("station_soil_moisture", completed.stdout)

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
        self.assertEqual(len(rows), 12)
        self.assertEqual({row["outcome"] for row in rows}, {"PASS", "DENY", "ERROR"})


if __name__ == "__main__":
    unittest.main()
