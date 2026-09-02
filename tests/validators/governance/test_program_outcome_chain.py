from __future__ import annotations

import ast
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/governance/validate_program_outcome_chain.py"
)
IMPLEMENTATION_PATHS = [
    VALIDATOR_PATH,
    REPO_ROOT
    / "tools/validators/governance/program_outcome_chain_model.py",
    REPO_ROOT
    / "tools/validators/governance/program_outcome_chain_semantics.py",
    REPO_ROOT
    / "tools/validators/governance/program_outcome_chain_io.py",
]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/program_outcome_chain.schema.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_module("test_program_outcome_chain_validator", VALIDATOR_PATH)


class ProgramOutcomeChainTests(unittest.TestCase):
    def test_schema_is_draft_2020_12_valid(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_fixture_suite_has_exact_polarity(self) -> None:
        ok, report = VALIDATOR.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 13)
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_valid_partial_and_full_chains_pass(self) -> None:
        document = VALIDATOR._load_fixture_document()
        by_id = {case["case_id"]: case for case in document["cases"]}
        for case_id in ("valid-application-chain", "valid-full-chain"):
            candidate = VALIDATOR.materialize_case(document, by_id[case_id])
            result = VALIDATOR.validate_payload(candidate)
            self.assertEqual(result.outcome, "PASS", result.findings)

    def test_payment_does_not_imply_project(self) -> None:
        document = VALIDATOR._load_fixture_document()
        case = next(
            item
            for item in document["cases"]
            if item["case_id"] == "payment-before-project"
        )
        result = VALIDATOR.validate_payload(
            VALIDATOR.materialize_case(document, case)
        )
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            "REQUIRED_PREDECESSOR_MISSING",
            {finding.code for finding in result.findings},
        )

    def test_observation_does_not_imply_completion_or_causation(self) -> None:
        document = VALIDATOR._load_fixture_document()
        case = next(
            item
            for item in document["cases"]
            if item["case_id"] == "outcome-without-completion"
        )
        result = VALIDATOR.validate_payload(
            VALIDATOR.materialize_case(document, case)
        )
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            "REQUIRED_PREDECESSOR_MISSING",
            {finding.code for finding in result.findings},
        )

    def test_identity_tampering_is_error(self) -> None:
        document = VALIDATOR._load_fixture_document()
        case = next(
            item
            for item in document["cases"]
            if item["case_id"] == "tampered-spec-hash"
        )
        result = VALIDATOR.validate_payload(
            VALIDATOR.materialize_case(document, case)
        )
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"SPEC_HASH_MISMATCH"},
        )

    def test_invalid_json_returns_value_free_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "candidate.json"
            path.write_text('{"secret":"DO_NOT_ECHO",', encoding="utf-8")
            first = VALIDATOR.validate_file(path)
            second = VALIDATOR.validate_file(path)
        self.assertEqual(first, second)
        self.assertEqual(first.outcome, "ERROR")
        self.assertEqual(
            [(finding.code, finding.path) for finding in first.findings],
            [("JSON_INVALID", "/")],
        )
        self.assertNotIn("DO_NOT_ECHO", repr(first))

    def test_fixture_cli_is_deterministic(self) -> None:
        environment = dict(os.environ)
        environment["PYTHONHASHSEED"] = "0"
        environment["KFM_NO_NETWORK"] = "1"
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(
            command,
            cwd=REPO_ROOT,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
        )
        second = subprocess.run(
            command,
            cwd=REPO_ROOT,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(first.stdout, second.stdout)
        json.loads(first.stdout)

    def test_validator_has_no_network_or_write_surface(self) -> None:
        imports: set[str] = set()
        attributes: set[str] = set()
        for path in IMPLEMENTATION_PATHS:
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(
                        alias.name.split(".")[0]
                        for alias in node.names
                    )
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module.split(".")[0])
                elif isinstance(node, ast.Attribute):
                    attributes.add(node.attr)
        self.assertTrue(
            {"socket", "requests", "urllib3", "httpx", "subprocess"}.isdisjoint(
                imports
            )
        )
        self.assertTrue(
            {
                "write_text",
                "write_bytes",
                "unlink",
                "rename",
                "mkdir",
            }.isdisjoint(attributes)
        )


if __name__ == "__main__":
    unittest.main()
