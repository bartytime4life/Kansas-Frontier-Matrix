from __future__ import annotations

import ast
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/governance/validate_dependency_origin_policy.py"
POLICY_PATH = REPO_ROOT / "policy/supply_chain/dependency_origin_policy.v1.json"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/dependency_origin_policy.schema.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_module("test_dependency_origin_policy_validator", VALIDATOR_PATH)


class DependencyOriginPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))

    def test_schema_is_draft_2020_12_valid(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_policy_is_closed_and_semantically_ordered(self) -> None:
        result = VALIDATOR.validate_policy(self.policy)
        self.assertEqual(result.outcome, "PASS", result.findings)

    def test_fixture_suite_has_exact_polarity(self) -> None:
        ok, report = VALIDATOR.run_fixture_suite(self.policy)
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 9)
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_minimal_repository_scan_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "apps/example").mkdir(parents=True)
            (root / "packages/ui").mkdir(parents=True)
            (root / "package.json").write_text(
                json.dumps({"name": "root", "private": True, "packageManager": "pnpm@11.17.0", "dependencies": {"external": "1.0.0"}}),
                encoding="utf-8",
            )
            (root / "apps/example/package.json").write_text(
                json.dumps({"name": "example", "dependencies": {"@kfm/ui": "workspace:*"}}),
                encoding="utf-8",
            )
            (root / "packages/ui/package.json").write_text(json.dumps({"name": "@kfm/ui", "version": "0.0.0"}), encoding="utf-8")
            (root / "pnpm-lock.yaml").write_text(
                textwrap.dedent("""\
                lockfileVersion: '9.0'
                importers: {}
                packages:
                  external@1.0.0:
                    resolution:
                      integrity: sha512-synthetic
                """),
                encoding="utf-8",
            )
            (root / "pyproject.toml").write_text(
                textwrap.dedent("""\
                [project]
                name = "fixture"
                version = "0.0.0"
                dependencies = ["jsonschema>=4,<5"]

                [project.optional-dependencies]
                test = ["pytest>=9,<10"]
                """),
                encoding="utf-8",
            )
            result = VALIDATOR.validate_repository(root, self.policy)
        self.assertEqual(result.outcome, "PASS", result.findings)

    def test_minimal_repository_scan_denies_internal_registry_escape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "apps/example").mkdir(parents=True)
            (root / "package.json").write_text(json.dumps({"name": "root", "private": True, "packageManager": "pnpm@11.17.0"}), encoding="utf-8")
            (root / "apps/example/package.json").write_text(json.dumps({"name": "example", "dependencies": {"@kfm/private": "^1.0.0"}}), encoding="utf-8")
            (root / "pnpm-lock.yaml").write_text("lockfileVersion: '9.0'\npackages: {}\n", encoding="utf-8")
            (root / "pyproject.toml").write_text('[project]\nname="fixture"\nversion="0.0.0"\ndependencies=[]\n', encoding="utf-8")
            result = VALIDATOR.validate_repository(root, self.policy)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn("INTERNAL_PACKAGE_NOT_WORKSPACE_BOUND", {finding.code for finding in result.findings})

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
        self.assertTrue({"socket", "requests", "urllib3", "httpx", "subprocess"}.isdisjoint(imports))
        self.assertTrue({"write_bytes", "unlink", "rename", "replace"}.isdisjoint(attributes))

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
