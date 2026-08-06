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

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/governance/validate_query_run_record.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/query_run_record"
FIXTURE_PATHS = (
    FIXTURE_ROOT / "valid_cases.json",
    FIXTURE_ROOT / "schema_invalid_cases.json",
    FIXTURE_ROOT / "semantic_identity_cases.json",
    FIXTURE_ROOT / "semantic_resolution_cases.json",
)
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/query_run_record.schema.json"

spec = importlib.util.spec_from_file_location("validate_query_run_record", VALIDATOR_PATH)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class QueryRunRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = []
        for fixture_path in FIXTURE_PATHS:
            cls.cases.extend(
                json.loads(fixture_path.read_text(encoding="utf-8"))["cases"]
            )
        cls.by_id = {case["case_id"]: case for case in cls.cases}

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_valid_case_matrix_passes(self) -> None:
        valid = [case for case in self.cases if case["case_id"].startswith("valid-")]
        self.assertEqual(len(valid), 3)
        for case in valid:
            with self.subTest(case_id=case["case_id"]):
                result = module.validate_document(case["record"])
                self.assertEqual(result.outcome, "PASS")
                self.assertEqual(result.findings, ())

    def test_exact_fixture_matrix(self) -> None:
        ok, report = module.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(len(report["cases"]), 11)
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_hashes_and_query_run_identity_reproduce(self) -> None:
        document = self.by_id["valid-answer"]["record"]
        expected = module._expected_hashes(document)
        self.assertEqual(
            document["hashes"],
            {"canonicalization": "RFC8785-JCS", "algorithm": "SHA-256", **expected},
        )
        self.assertEqual(
            document["query_run_id"],
            module._expected_query_run_id(expected["run_hash"]),
        )

    def test_finite_outcomes_follow_evidence_precedence(self) -> None:
        matrix = {
            "valid-answer": "ANSWER",
            "valid-abstain": "ABSTAIN",
            "valid-deny": "DENY",
        }
        for case_id, outcome in matrix.items():
            self.assertEqual(self.by_id[case_id]["record"]["outcome"], outcome)

    def test_raw_query_and_public_authority_fail_closed(self) -> None:
        for case_id in ("invalid-raw-query", "invalid-public-use"):
            result = module.validate_document(self.by_id[case_id]["record"])
            self.assertEqual(result.outcome, "DENY")
            self.assertIn("SCHEMA_INVALID", {finding.code for finding in result.findings})

    def test_symlink_input_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.json"
            source.write_text(
                json.dumps(self.by_id["valid-answer"]["record"]),
                encoding="utf-8",
            )
            target = Path(directory) / "candidate.json"
            try:
                target.symlink_to(source)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks are unavailable")
            result = module.validate_file(target)
            self.assertEqual(result.outcome, "ERROR")
            self.assertEqual(
                {finding.code for finding in result.findings},
                {"QUERY_RUN_JSON_INVALID"},
            )

    def test_cli_is_deterministic_and_does_not_echo_untrusted_value(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text(
                json.dumps(self.by_id["invalid-raw-query"]["record"]),
                encoding="utf-8",
            )
            command = [sys.executable, str(VALIDATOR_PATH), str(path)]
            env = {**os.environ, "PYTHONHASHSEED": "0", "KFM_NO_NETWORK": "1"}
            first = subprocess.run(
                command, cwd=REPO_ROOT, env=env, text=True, capture_output=True, check=False
            )
            second = subprocess.run(
                command, cwd=REPO_ROOT, env=env, text=True, capture_output=True, check=False
            )
            self.assertEqual(first.returncode, 1)
            self.assertEqual(first.stdout, second.stdout)
            self.assertNotIn("SECRET_MARKER_NEVER_ECHO", first.stdout + first.stderr)

    def test_validator_has_no_network_or_mutation_client(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8").lower()
        for token in ("requests", "urllib.request", "httpx", "socket", "subprocess", "git ", "github"):
            self.assertNotIn(token, source)

    def test_cli_fixture_suite_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            env={**os.environ, "PYTHONHASHSEED": "0", "KFM_NO_NETWORK": "1"},
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        report = json.loads(completed.stdout)
        self.assertTrue(report["ok"])


if __name__ == "__main__":
    unittest.main()
