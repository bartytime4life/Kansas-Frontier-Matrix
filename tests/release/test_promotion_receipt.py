from __future__ import annotations

import ast
import json
from pathlib import Path
import subprocess
import sys
import unittest

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/release/validate_promotion_receipt.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/promotion_receipt.schema.json"
FIXTURES = REPO_ROOT / "fixtures/release/promotion_receipt"

sys.path.insert(0, str(REPO_ROOT))
from tools.validators.release.validate_promotion_receipt import (  # noqa: E402
    canonical_digest,
    derived_status,
    validate_path,
)


class PromotionReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.schema_validator = Draft202012Validator(
            cls.schema, format_checker=FormatChecker()
        )

    def test_schema_metadata_and_gate_order_are_pinned(self) -> None:
        self.assertEqual("PROPOSED", self.schema["x-kfm"]["status"])
        self.assertEqual(
            "contracts/release/promotion_receipt.md",
            self.schema["x-kfm"]["contract_doc"],
        )
        expected = list("ABCDEFG")
        actual = [
            item["$ref"].rsplit("_", 1)[-1].upper()
            for item in self.schema["properties"]["gates"]["prefixItems"]
        ]
        self.assertEqual(expected, actual)
        self.assertFalse(self.schema["additionalProperties"])

    def test_valid_fixtures_pass_schema_and_semantics(self) -> None:
        paths = sorted((FIXTURES / "valid").glob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path.name):
                value = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual([], list(self.schema_validator.iter_errors(value)))
                self.assertEqual((), validate_path(path))
                self.assertEqual(value["integrity"]["receipt_digest"], canonical_digest(value))

    def test_invalid_fixtures_expose_expected_codes(self) -> None:
        paths = sorted((FIXTURES / "invalid").glob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            expected = path.with_suffix(".expected_code.txt").read_text(
                encoding="utf-8"
            ).strip()
            with self.subTest(path=path.name, expected=expected):
                self.assertIn(expected, validate_path(path))

    def test_status_precedence_is_fail_closed(self) -> None:
        self.assertEqual("PASS", derived_status(["PASS"] * 7))
        self.assertEqual("ABSTAIN", derived_status(["PASS"] * 6 + ["ABSTAIN"]))
        self.assertEqual("DENY", derived_status(["PASS", "ABSTAIN", "DENY"]))
        self.assertEqual("ERROR", derived_status(["PASS", "DENY", "ERROR"]))

    def test_cli_fixture_mode_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True)
        second = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True)
        self.assertEqual(0, first.returncode, first.stderr or first.stdout)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn("PROMOTION_RECEIPT_FIXTURES_VALID", first.stdout)

    def test_validator_imports_no_network_or_process_client(self) -> None:
        tree = ast.parse(VALIDATOR_PATH.read_text(encoding="utf-8"))
        roots: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                roots.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                roots.add(node.module.split(".", 1)[0])
        self.assertTrue(
            roots.isdisjoint(
                {"http", "requests", "socket", "subprocess", "urllib", "aiohttp"}
            ),
            roots,
        )


if __name__ == "__main__":
    unittest.main()
