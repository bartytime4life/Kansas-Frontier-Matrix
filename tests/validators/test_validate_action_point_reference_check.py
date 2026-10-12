from __future__ import annotations

import ast
import copy
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


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_action_point_reference_check.py"
BUILDER_PATH = REPO_ROOT / "tools/generators/action_point_reference_check/build_action_point_reference_check.py"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/validation/action_point_reference_check/cases.json"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/validation/action_point_reference_check.schema.json"
VALIDATOR = load_module("test_action_point_validator", VALIDATOR_PATH)
BUILDER = load_module("test_action_point_builder", BUILDER_PATH)


class ActionPointReferenceCheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.suite = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.documents = {case["case_id"]: BUILDER.build_case(case) for case in cls.suite["cases"]}

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_fixture_polarity(self) -> None:
        ok, report = VALIDATOR.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 8)

    def test_only_exact_preserved_pre_action_literal_matches(self) -> None:
        self.assertEqual(self.documents["valid-match"]["report"]["outcome"], "MATCH")
        self.assertEqual(self.documents["valid-mismatch"]["report"]["outcome"], "MISMATCH")
        self.assertEqual(self.documents["valid-blocked-abbreviation"]["report"]["outcome"], "BLOCKED")
        self.assertEqual(self.documents["valid-blocked-late-dereference"]["report"]["outcome"], "BLOCKED")
        self.assertEqual(self.documents["valid-unclassifiable"]["report"]["outcome"], "UNCLASSIFIABLE")

    def test_report_and_identity_drift_fail_closed(self) -> None:
        report = VALIDATOR.validate_document(self.documents["invalid-report-drift"])
        self.assertEqual({finding.code for finding in report.findings}, {"REPORT_MISMATCH"})
        identity = VALIDATOR.validate_document(self.documents["invalid-spec-hash"])
        self.assertEqual({finding.code for finding in identity.findings}, {"CHECK_ID_MISMATCH", "SPEC_HASH_MISMATCH"})

    def test_line_number_only_pointer_is_not_admitted(self) -> None:
        result = VALIDATOR.validate_document(self.documents["invalid-line-number-only"])
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual({finding.code for finding in result.findings}, {"SCHEMA_INVALID"})

    def test_builder_and_validator_have_no_network_or_write_surface(self) -> None:
        imports: set[str] = set()
        attributes: set[str] = set()
        for path in (BUILDER_PATH, VALIDATOR_PATH):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(alias.name.split(".")[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module.split(".")[0])
                elif isinstance(node, ast.Attribute):
                    attributes.add(node.attr)
        self.assertTrue({"socket", "requests", "urllib", "httpx", "subprocess"}.isdisjoint(imports))
        self.assertTrue({"write_text", "write_bytes", "unlink", "rename", "replace"}.isdisjoint(attributes))

    def test_symlink_candidate_is_rejected(self) -> None:
        if not hasattr(os, "symlink"):
            self.skipTest("symlink support unavailable")
        with tempfile.TemporaryDirectory() as temporary:
            candidate = Path(temporary) / "candidate.json"
            try:
                candidate.symlink_to(FIXTURE_PATH)
            except OSError:
                self.skipTest("symlink creation unavailable")
            result = VALIDATOR.validate_file(candidate)
        self.assertEqual(result.outcome, "ERROR")

    def test_clis_are_deterministic(self) -> None:
        environment = dict(os.environ)
        environment["PYTHONHASHSEED"] = "0"
        commands = [
            [sys.executable, str(BUILDER_PATH), "--case", "valid-match"],
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
        ]
        for command in commands:
            first = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
            second = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(first.stdout, second.stdout)
            json.loads(first.stdout)


if __name__ == "__main__":
    unittest.main()
