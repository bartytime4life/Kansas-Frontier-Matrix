from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / 'tools/validators/validate_validator_assurance_report.py'
SCHEMA_PATH = REPO_ROOT / 'schemas/contracts/v1/validation/validator_assurance_report.schema.json'
FIXTURE_ROOT = REPO_ROOT / 'fixtures/contracts/v1/validation/validator_assurance_report'

SPEC = importlib.util.spec_from_file_location("validator_under_test", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ValidatorAssuranceReportTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED")
        self.assertFalse(schema["additionalProperties"])

    def test_all_valid_fixtures_pass(self) -> None:
        paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertEqual(len(paths), 4)
        for path in paths:
            with self.subTest(path=path.name):
                self.assertTrue(MODULE.validate_record(path).ok)

    def test_invalid_fixtures_match_exact_reviewed_codes(self) -> None:
        invalid_root = FIXTURE_ROOT / "invalid"
        manifest = json.loads(
            (invalid_root / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        paths = sorted(invalid_root.glob("invalid_*.json"))
        self.assertEqual(len(paths), 9)
        self.assertEqual(set(manifest), {path.name for path in paths})
        for path in paths:
            with self.subTest(path=path.name):
                result = MODULE.validate_record(path)
                actual = sorted({finding.code for finding in result.findings})
                self.assertFalse(result.ok)
                self.assertEqual(actual, sorted(manifest[path.name]))

    def test_fixture_cli_replays_exact_profile(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT, check=False, capture_output=True, text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertNotIn("FIXTURE_POLARITY_ERROR", completed.stdout + completed.stderr)
        self.assertEqual(completed.stdout.count('"outcome":"PASS"'), 4)
        self.assertEqual(completed.stdout.count('"outcome":"FAIL"'), 9)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"ValidatorAssuranceReport","object_type":"ValidatorAssuranceReport"}',
                encoding="utf-8",
            )
            result = MODULE.validate_record(path)
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_DUPLICATE_KEY"})

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_NONFINITE_NUMBER"})

    def test_missing_file_is_error(self) -> None:
        result = MODULE.validate_record(REPO_ROOT / "does-not-exist.json")
        self.assertTrue(result.error)
        self.assertEqual({finding.code for finding in result.findings}, {"FILE_NOT_FOUND"})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        candidate = json.loads(
            (FIXTURE_ROOT / "valid/valid_pass_all_killed.json").read_text(encoding="utf-8")
        )
        untrusted_value = "UNTRUSTED_VALUE_DO_NOT_ECHO"
        candidate["untrusted_negative_canary"] = untrusted_value
        candidate["spec_hash"] = MODULE._canonical_spec_hash(candidate)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            result = MODULE.validate_record(path)
            report = MODULE._serialize(path, result)
        self.assertNotIn(untrusted_value, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_replay_is_deterministic(self) -> None:
        path = FIXTURE_ROOT / "valid/valid_pass_all_killed.json"
        first = MODULE._serialize(path, MODULE.validate_record(path))
        second = MODULE._serialize(path, MODULE.validate_record(path))
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
