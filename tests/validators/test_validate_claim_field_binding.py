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
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_claim_field_binding.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/claim_field_binding.schema.json"

spec = importlib.util.spec_from_file_location("validate_claim_field_binding", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class ClaimFieldBindingTests(unittest.TestCase):
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
        self.assertEqual(observed, {"PASS": 4, "DENY": 9, "ERROR": 1})

    def test_identity_is_stable_across_mapping_order(self) -> None:
        candidate = self.by_name["valid_exact_current"][1]
        reordered = {
            key: candidate[key]
            for key in reversed(list(candidate.keys()))
        }
        self.assertEqual(
            validator.canonical_spec_hash(reordered),
            candidate["spec_hash"],
        )
        self.assertEqual(
            validator.expected_binding_id(reordered),
            candidate["claim_field_binding_id"],
        )

    def test_transform_requires_reference_receipt_and_determinism(self) -> None:
        for name, code in (
            ("transform_receipt_missing", "TRANSFORM_RECEIPT_REQUIRED"),
            ("nondeterministic_transform", "NONDETERMINISTIC_TRANSFORM_DENIED"),
        ):
            result = validator.validate_payload(self.by_name[name][1])
            self.assertEqual(result.outcome, "DENY")
            self.assertEqual([finding.code for finding in result.findings], [code])

    def test_context_only_support_cannot_claim_high_confidence(self) -> None:
        result = validator.validate_payload(
            self.by_name["context_confidence_overclaim"][1]
        )
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            [finding.code for finding in result.findings],
            ["CONTEXT_CONFIDENCE_OVERCLAIM"],
        )

    def test_release_public_and_effect_overclaims_are_separate(self) -> None:
        expected = {
            "release_overclaim": "RELEASE_OVERCLAIM",
            "public_use_overclaim": "PUBLIC_USE_OVERCLAIM",
            "effect_overclaim": "EFFECT_OVERCLAIM",
        }
        for name, code in expected.items():
            result = validator.validate_payload(self.by_name[name][1])
            self.assertEqual(result.outcome, "DENY")
            self.assertEqual([finding.code for finding in result.findings], [code])

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

    def test_nonfinite_json_number_is_operational_error(self) -> None:
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

    def test_cli_pass_is_value_free_and_all_authority_flags_are_false(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.json"
            path.write_text(
                json.dumps(self.by_name["valid_exact_current"][1]),
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
        self.assertNotIn("synthetic-condition-record", completed.stdout)
        self.assertNotIn("/record/value", completed.stdout)

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
        self.assertEqual(len(rows), 14)
        self.assertEqual(
            {row["outcome"] for row in rows},
            {"PASS", "DENY", "ERROR"},
        )


if __name__ == "__main__":
    unittest.main()
