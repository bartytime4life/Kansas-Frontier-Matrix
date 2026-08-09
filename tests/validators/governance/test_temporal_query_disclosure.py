from __future__ import annotations

import ast
import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/temporal_query_disclosure.schema.json"
BUILDER_PATH = REPO_ROOT / "tools/generators/temporal_query_disclosure/build.py"
VALIDATOR_PATH = REPO_ROOT / "tools/validators/governance/validate_temporal_query_disclosure.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


BUILDER = load_module("test_temporal_query_disclosure_builder", BUILDER_PATH)
VALIDATOR = load_module("test_temporal_query_disclosure_validator", VALIDATOR_PATH)


class TemporalQueryDisclosureTests(unittest.TestCase):
    def current(self):
        return BUILDER.build_disclosure(
            query_run_ref="kfm:query-run:" + "a" * 64,
            temporal_query_type="CURRENT_STATE",
            time_basis="VALID_TIME",
            evaluated_at="2026-08-08T20:00:00Z",
            requested_as_of=None,
            valid_start=None,
            valid_end=None,
            transaction_cutoff=None,
            snapshot_refs=["kfm:temporal-snapshot:" + "b" * 64],
            evidence_refs=["kfm:evidence-ref:" + "c" * 64],
        )

    def test_schema_is_draft_2020_12_valid(self):
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_builder_is_deterministic_and_has_fixed_explanation(self):
        first = self.current()
        second = self.current()
        self.assertEqual(first, second)
        self.assertEqual(first["public_explanation_code"], "CURRENT_STATE_AT_EVALUATION")
        self.assertNotIn("summary", first)

    def test_current_state_validates(self):
        result = VALIDATOR.validate_disclosure(self.current())
        self.assertEqual(result.outcome, "PASS", result.findings)

    def test_query_class_semantics_do_not_collapse(self):
        prior = BUILDER.build_disclosure(
            query_run_ref="kfm:query-run:" + "a" * 64,
            temporal_query_type="PRIOR_STATE",
            time_basis="VALID_TIME",
            evaluated_at="2026-08-08T20:00:00Z",
            requested_as_of="2020-01-01T00:00:00Z",
            valid_start=None,
            valid_end=None,
            transaction_cutoff=None,
            snapshot_refs=["kfm:temporal-snapshot:" + "b" * 64],
            evidence_refs=["kfm:evidence-ref:" + "c" * 64],
        )
        self.assertNotEqual(prior["disclosure_id"], self.current()["disclosure_id"])
        self.assertEqual(VALIDATOR.validate_disclosure(prior).outcome, "PASS")

    def test_fixture_suite_has_exact_polarity(self):
        ok, report = VALIDATOR.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 12)
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_identity_tampering_is_denied(self):
        value = self.current()
        value["disclosure_id"] = "kfm:temporal-query-disclosure:" + "0" * 64
        result = VALIDATOR.validate_disclosure(value)
        self.assertIn("DISCLOSURE_ID_MISMATCH", {finding.code for finding in result.findings})

    def test_sources_have_no_network_database_or_write_surface(self):
        imports = set()
        attributes = set()
        for path in (BUILDER_PATH, VALIDATOR_PATH):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(alias.name.split(".")[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module.split(".")[0])
                elif isinstance(node, ast.Attribute):
                    attributes.add(node.attr)
        self.assertTrue({"socket", "requests", "urllib3", "httpx", "sqlite3", "psycopg", "duckdb"}.isdisjoint(imports))
        self.assertTrue({"write_text", "write_bytes", "unlink", "rename"}.isdisjoint(attributes))

    def test_fixture_cli_is_deterministic(self):
        env = dict(os.environ)
        env["PYTHONHASHSEED"] = "0"
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=REPO_ROOT, env=env, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=REPO_ROOT, env=env, check=False, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        json.loads(first.stdout)


if __name__ == "__main__":
    unittest.main()
