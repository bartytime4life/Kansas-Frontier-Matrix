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
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_classification_release.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/classification_release.schema.json"

spec = importlib.util.spec_from_file_location(
    "validate_classification_release",
    VALIDATOR_PATH,
)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class ClassificationReleaseTests(unittest.TestCase):
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
            self.assertEqual(result.outcome, raw_case["expected_outcome"])
            self.assertEqual(
                [finding.code for finding in result.findings],
                raw_case["expected_findings"],
            )
        self.assertEqual(observed, {"PASS": 4, "DENY": 3, "ERROR": 1})

    def test_all_four_lineage_states_are_positive(self) -> None:
        states = set()
        for raw_case, candidate in self.cases:
            if raw_case["expected_outcome"] != "PASS":
                continue
            states.add(candidate["lineage"]["state"])
            self.assertTrue(validator.validate_payload(candidate).ok)
        self.assertEqual(
            states,
            {"CURRENT", "CORRECTED", "SUPERSEDED", "CONFLICTED"},
        )

    def test_identity_is_stable_across_mapping_key_order(self) -> None:
        candidate = self.by_name["valid_current"][1]
        reordered = {
            key: candidate[key] for key in reversed(list(candidate.keys()))
        }
        self.assertEqual(
            validator.canonical_spec_hash(reordered),
            candidate["spec_hash"],
        )
        self.assertEqual(
            validator.expected_release_id(reordered),
            candidate["classification_release_id"],
        )

    def test_role_and_support_are_classification_only(self) -> None:
        candidate = self.by_name["valid_current"][1]
        self.assertEqual(candidate["source_role"], "CLASSIFICATION")
        self.assertEqual(
            candidate["support_type"],
            "DERIVED_CLASSIFICATION",
        )

    def test_unknown_member_is_denied_by_closed_schema(self) -> None:
        candidate = dict(self.by_name["valid_current"][1])
        candidate["unexpected"] = True
        result = validator.validate_payload(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            [finding.code for finding in result.findings],
            ["SCHEMA_INVALID"],
        )

    def test_duplicate_json_key_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"profile":"a","profile":"b"}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            result.findings,
            (validator.Finding("JSON_DUPLICATE_KEY", "/"),),
        )

    def test_nonfinite_number_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":Infinity}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            result.findings,
            (validator.Finding("JSON_NONFINITE_NUMBER", "/"),),
        )

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
        self.assertEqual(
            result.findings,
            (validator.Finding("INPUT_SYMLINK_DENIED", "/"),),
        )

    def test_oversized_input_is_rejected_before_parsing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "large.json"
            path.write_bytes(b" " * (validator.MAX_FILE_BYTES + 1))
            result = validator.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            result.findings,
            (validator.Finding("FILE_TOO_LARGE", "/"),),
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

    def test_cli_emits_bounded_value_free_pass(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.json"
            path.write_text(
                json.dumps(self.by_name["valid_current"][1]),
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
        self.assertNotIn("kfm://source/usdm", completed.stdout)
        self.assertNotIn("usdm:2026-08-04", completed.stdout)

    def test_cli_uses_finite_exit_code_for_deny(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "deny.json"
            path.write_text(
                json.dumps(self.by_name["source_role_collapse"][1]),
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), str(path)],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 1, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "DENY")
        self.assertEqual(
            [finding["code"] for finding in payload["findings"]],
            ["SOURCE_ROLE_COLLAPSE"],
        )

    def test_fixture_cli_replays_every_case(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        rows = [
            json.loads(line)
            for line in completed.stdout.splitlines()
            if line.strip()
        ]
        self.assertEqual(len(rows), 8)
        self.assertEqual(
            {row["outcome"] for row in rows},
            {"PASS", "DENY", "ERROR"},
        )


if __name__ == "__main__":
    unittest.main()
