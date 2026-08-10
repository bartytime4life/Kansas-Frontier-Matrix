from __future__ import annotations

import ast
import copy
import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/governance/validate_atlas_card_delta_assessment.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/atlas_card_delta_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/atlas_card_delta_assessment/cases.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_module("test_atlas_card_delta_validator", VALIDATOR_PATH)


class AtlasCardDeltaAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.suite = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    def test_schema_is_draft_2020_12_valid(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_fixture_suite_has_exact_finite_outcomes(self) -> None:
        ok, report = VALIDATOR.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 10)
        self.assertEqual(
            {case["actual_outcome"] for case in report["cases"]},
            {"PASS", "ABSTAIN", "DENY", "ERROR"},
        )

    def test_snapshot_collections_must_be_sorted(self) -> None:
        candidate = copy.deepcopy(self.suite["cases"][0]["candidate"])
        candidate["after"]["evidence_refs"].reverse()
        result = VALIDATOR.evaluate_candidate(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn("COLLECTION_NOT_SORTED_UNIQUE", {item.code for item in result.findings})

    def test_added_and_removed_references_are_derived(self) -> None:
        candidate = copy.deepcopy(self.suite["cases"][0]["candidate"])
        candidate["declared_delta"]["evidence_refs_added"] = []
        result = VALIDATOR.evaluate_candidate(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn("DELTA_EVIDENCE_ADDED_MISMATCH", {item.code for item in result.findings})

    def test_validator_has_no_network_or_write_surface(self) -> None:
        tree = ast.parse(VALIDATOR_PATH.read_text(encoding="utf-8"))
        imports: set[str] = set()
        attributes: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])
            elif isinstance(node, ast.Attribute):
                attributes.add(node.attr)
        self.assertTrue({"httpx", "requests", "socket", "subprocess", "urllib3"}.isdisjoint(imports))
        self.assertTrue({"rename", "replace", "unlink", "write_bytes", "write_text"}.isdisjoint(attributes))

    def test_fixture_cli_is_deterministic(self) -> None:
        environment = dict(os.environ)
        environment["PYTHONHASHSEED"] = "0"
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(first.stdout, second.stdout)
        json.loads(first.stdout)


if __name__ == "__main__":
    unittest.main()
