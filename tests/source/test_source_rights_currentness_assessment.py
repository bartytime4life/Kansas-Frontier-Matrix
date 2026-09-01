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
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/validators/source/validate_source_rights_currentness_assessment.py"
SCHEMA = ROOT / "schemas/contracts/v1/source/source_rights_currentness_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_rights_currentness_assessment/cases.json"
SPEC = importlib.util.spec_from_file_location("validate_source_rights_currentness_assessment", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _decode(value: str) -> str:
    return value.replace("~1", "/").replace("~0", "~")


def _replace(document: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [_decode(part) for part in pointer[1:].split("/")]
    target: Any = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


class SourceRightsCurrentnessAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(FIXTURES.read_text(encoding="utf-8"))
        cls.cases = {case["case_id"]: case for case in cls.manifest["cases"]}

    def materialize(self, case_id: str) -> dict[str, Any]:
        case = self.cases[case_id]
        document = copy.deepcopy(self.manifest["bases"][case["base"]])
        for mutation in case.get("mutations", []):
            _replace(document, mutation["path"], mutation.get("value"))
        document["result"] = copy.deepcopy(case.get("result_override", MODULE.recompute_result(document)))
        spec_hash, assessment_id = MODULE.canonical_identity(document)
        document["spec_hash"] = case.get("spec_hash_override", spec_hash)
        document["assessment_id"] = case.get("assessment_id_override", assessment_id)
        return document

    def result(self, case_id: str) -> Any:
        return MODULE.validate_payload(self.materialize(case_id))

    def test_schema_is_draft_2020_12_valid(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_fixture_manifest_has_exact_polarity(self) -> None:
        outcomes = [case["expected_outcome"] for case in self.manifest["cases"]]
        self.assertEqual(outcomes.count("PASS"), 2)
        self.assertEqual(outcomes.count("ABSTAIN"), 1)
        self.assertEqual(outcomes.count("ERROR"), 1)
        self.assertEqual(outcomes.count("DENY"), 11)

    def test_all_fixture_cases_match_exactly(self) -> None:
        for case in self.manifest["cases"]:
            with self.subTest(case_id=case["case_id"]):
                result = self.result(case["case_id"])
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(actual, case["expected_findings"])

    def test_identity_is_deterministic(self) -> None:
        first = self.materialize("current-open")
        second = self.materialize("current-open")
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        self.assertEqual(first["assessment_id"], second["assessment_id"])

    def test_fixture_manifest_is_flora_anchored(self) -> None:
        document = self.materialize("current-open")
        self.assertTrue(document["source_id"].startswith("flora."))
        self.assertTrue(document["source_descriptor_ref"].startswith("kfm://source/flora."))

    def test_governance_non_effects_are_false(self) -> None:
        document = self.materialize("current-open")
        self.assertEqual("FIXTURE_ONLY", document["governance"]["execution_mode"])
        self.assertFalse(any(value for key, value in document["governance"].items() if key != "execution_mode"))

    def test_validator_has_no_network_client_import(self) -> None:
        source = Path(MODULE.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "socket."):
            self.assertNotIn(token, source)

    def test_no_network_is_used(self) -> None:
        original = socket.socket

        def denied(*_args: Any, **_kwargs: Any) -> Any:
            raise AssertionError("network denied")

        socket.socket = denied
        try:
            for case_id in self.cases:
                self.result(case_id)
        finally:
            socket.socket = original

    def test_findings_do_not_echo_document_values(self) -> None:
        document = self.materialize("unknown-rights")
        document["source_id"] = "flora.private-value"
        result = MODULE.validate_payload(document)
        serialized = MODULE.serialize(None, result)
        self.assertIn("RIGHTS_NOT_VERIFIED", serialized)
        self.assertNotIn("private-value", serialized)

    def test_cli_validates_fixtures_without_credentials(self) -> None:
        env = os.environ.copy()
        env["KFM_NO_NETWORK"] = "1"
        env.pop("GITHUB_TOKEN", None)
        env.pop("KFM_GITHUB_READ_TOKEN", None)
        completed = subprocess.run(
            [sys.executable, str(TOOL), "--fixtures"],
            cwd=ROOT,
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_invalid_json_cli_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text("{", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(TOOL), str(path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(2, completed.returncode)
        self.assertIn('"outcome":"ERROR"', completed.stdout)


if __name__ == "__main__":
    unittest.main()
