from __future__ import annotations

import copy
import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/validate_policy_transform_receipt.py"
SCHEMA = ROOT / "schemas/contracts/v1/receipts/policy_transform_receipt.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/receipts/policy_transform_receipt"

SPEC = importlib.util.spec_from_file_location("validate_policy_transform_receipt", VALIDATOR)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PolicyTransformReceiptTests(unittest.TestCase):
    def _load(self, relative: str) -> dict[str, object]:
        return json.loads((FIXTURES / relative).read_text(encoding="utf-8"))

    def test_schema_is_closed_and_inactive(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["effects"], "NONE")

    def test_valid_records_pass(self) -> None:
        paths = sorted((FIXTURES / "valid").glob("valid_*.json"))
        self.assertEqual(len(paths), 3)
        for path in paths:
            with self.subTest(path=path.name):
                self.assertTrue(MODULE.validate_record(path).ok)

    def test_manifest_has_exact_polarity(self) -> None:
        manifest = self._load("expected_findings_manifest.json")
        self.assertEqual(len(manifest["cases"]), 16)
        for case in manifest["cases"]:
            path = FIXTURES / case["record"]
            result = MODULE.validate_record(path)
            outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
            self.assertEqual(outcome, case["expected_outcome"], case["case_id"])
            self.assertEqual(sorted({item.code for item in result.findings}), case["expected_findings"], case["case_id"])

    def test_schema_and_semantic_negative_names_do_not_collide(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        schema_invalid = sorted((FIXTURES / "invalid").glob("invalid_*.json"))
        semantic_invalid = sorted((FIXTURES / "invalid").glob("semantic_invalid_*.json"))
        self.assertEqual(len(schema_invalid), 4)
        self.assertEqual(len(semantic_invalid), 9)
        for path in schema_invalid:
            self.assertTrue(list(validator.iter_errors(json.loads(path.read_text(encoding="utf-8")))), path.name)
        for path in semantic_invalid:
            self.assertFalse(list(validator.iter_errors(json.loads(path.read_text(encoding="utf-8")))), path.name)

    def test_operation_derivation_preserves_all_dimensions(self) -> None:
        source = json.loads((ROOT / "fixtures/contracts/v1/policy/policy_transform_plan_simulation/valid/valid_stronger_suppress.json").read_text(encoding="utf-8"))
        names = [item["operation"] for item in MODULE.derive_operations(source["plan"])]
        self.assertEqual(names, ["GENERALIZE_GEOMETRY", "FUZZ_DATE", "SUPPRESS_GEOMETRY", "SUPPRESS_RECORD", "APPLY_EMBARGO"])

    def test_receipt_identity_reproduces_valid_fixture(self) -> None:
        candidate = self._load("valid/valid_combined.json")
        self.assertEqual(MODULE.compute_receipt_spec_hash(candidate), candidate["spec_hash"])
        self.assertEqual(MODULE.compute_receipt_id(candidate), candidate["receipt_id"])

    def test_duplicate_json_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"object_type":"a","object_type":"b"}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertTrue(result.error)
        self.assertEqual({item.code for item in result.findings}, {"JSON_DUPLICATE_KEY"})

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nan.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertTrue(result.error)
        self.assertEqual({item.code for item in result.findings}, {"JSON_NONFINITE_NUMBER"})

    def test_missing_file_is_error(self) -> None:
        result = MODULE.validate_record(ROOT / "not-present.json")
        self.assertTrue(result.error)
        self.assertEqual({item.code for item in result.findings}, {"FILE_NOT_FOUND"})

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_symlink_input_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            real = Path(directory) / "real.json"
            real.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            try:
                link.symlink_to(real)
            except OSError:
                self.skipTest("symlink creation unavailable")
            result = MODULE.validate_record(link)
        self.assertTrue(result.error)
        self.assertEqual({item.code for item in result.findings}, {"INPUT_SYMLINK_DENIED"})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        candidate = self._load("valid/valid_generalize.json")
        untrusted = "UNTRUSTED_VALUE_DO_NOT_ECHO"
        candidate["source_simulation"]["simulation_id"] = untrusted
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            report = MODULE._serialize(path, MODULE.validate_record(path))
        self.assertNotIn(untrusted, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_fixture_suite_is_no_network_and_deterministic(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            ok, first = MODULE.validate_fixture_suite()
            second_ok, second = MODULE.validate_fixture_suite()
        self.assertTrue(ok)
        self.assertTrue(second_ok)
        self.assertEqual(first, second)
        completed = subprocess.run([sys.executable, str(VALIDATOR), "--fixtures"], cwd=ROOT, check=False, capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 16)
        self.assertNotIn('"suite_match":false', completed.stdout)


if __name__ == "__main__":
    unittest.main()
