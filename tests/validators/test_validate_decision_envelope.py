from __future__ import annotations

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
VALIDATOR = ROOT / "tools/validators/validate_decision_envelope.py"
SCHEMA = ROOT / "schemas/contracts/v1/runtime/decision_envelope.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/runtime/decision_envelope"
MANIFEST = FIXTURES / "expected_findings_manifest.json"

SPEC = importlib.util.spec_from_file_location("validate_decision_envelope", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class DecisionEnvelopeValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.cases = cls.manifest["cases"]
        cls.schema_validator = Draft202012Validator(
            cls.schema,
            format_checker=FormatChecker(),
        )

    def _path(self, case: dict[str, object]) -> Path:
        return FIXTURES / str(case["path"])

    def test_schema_is_closed_and_names_validator(self) -> None:
        Draft202012Validator.check_schema(self.schema)
        self.assertFalse(self.schema["additionalProperties"])
        self.assertEqual(
            self.schema["x-kfm"]["validator"],
            "tools/validators/validate_decision_envelope.py",
        )

    def test_manifest_has_reviewed_polarity(self) -> None:
        kinds = {case["case_kind"] for case in self.cases}
        self.assertEqual(kinds, {"VALID", "SCHEMA_NEGATIVE", "SEMANTIC_NEGATIVE"})
        self.assertEqual(len(self.cases), 15)

    def test_exact_manifest_outcomes_and_findings(self) -> None:
        for case in self.cases:
            result = MODULE.validate(self._path(case))
            self.assertEqual(result.outcome, case["expected_outcome"], case["case_id"])
            self.assertEqual(
                sorted({finding.code for finding in result.findings}),
                sorted(case["expected_findings"]),
                case["case_id"],
            )

    def test_schema_and_semantic_negative_boundary(self) -> None:
        for case in self.cases:
            errors = list(self.schema_validator.iter_errors(
                json.loads(self._path(case).read_text(encoding="utf-8"))
            ))
            if case["case_kind"] == "SCHEMA_NEGATIVE":
                self.assertTrue(errors, case["case_id"])
            elif case["case_kind"] == "SEMANTIC_NEGATIVE":
                self.assertFalse(errors, case["case_id"])

    def test_valid_legacy_fixtures_remain_accepted(self) -> None:
        valid = [case for case in self.cases if case["case_kind"] == "VALID"]
        self.assertEqual(len(valid), 2)
        for case in valid:
            self.assertTrue(MODULE.validate(self._path(case)).ok, case["case_id"])

    def test_alias_mismatch_is_semantic_not_schema_failure(self) -> None:
        case = next(case for case in self.cases if case["case_id"] == "semantic-alias-mismatch")
        result = MODULE.validate(self._path(case))
        self.assertEqual({item.code for item in result.findings}, {"OUTCOME_ALIAS_MISMATCH"})

    def test_internal_reference_is_denied_without_value_echo(self) -> None:
        case = next(case for case in self.cases if case["case_id"] == "semantic-internal-ref")
        path = self._path(case)
        result = MODULE.validate(path)
        rendered = json.dumps(
            [{"code": finding.code, "field": finding.field, "detail": finding.detail}
             for finding in result.findings]
        )
        self.assertIn("INTERNAL_REFERENCE_DENIED", rendered)
        self.assertNotIn("internal:evidence:secret", rendered)

    def test_duplicate_key_and_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            nonfinite = Path(directory) / "nonfinite.json"
            duplicate.write_text('{"decision_id":"a","decision_id":"b"}', encoding="utf-8")
            nonfinite.write_text('{"decision_id":"a","value":NaN}', encoding="utf-8")
            self.assertEqual(
                {item.code for item in MODULE.validate(duplicate).findings},
                {"JSON_DUPLICATE_KEY"},
            )
            self.assertEqual(
                {item.code for item in MODULE.validate(nonfinite).findings},
                {"JSON_NONFINITE_NUMBER"},
            )

    def test_symlink_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            link = Path(directory) / "link.json"
            target.write_text("{}", encoding="utf-8")
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            self.assertEqual(
                {item.code for item in MODULE.validate(link).findings},
                {"INPUT_SYMLINK_DENIED"},
            )

    def test_no_network_replay_and_cli_fixture_mode(self) -> None:
        with mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network access attempted"),
        ), mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network access attempted"),
        ):
            first = [
                (case["case_id"], MODULE.validate(self._path(case)))
                for case in self.cases
            ]
            second = [
                (case["case_id"], MODULE.validate(self._path(case)))
                for case in self.cases
            ]
        self.assertEqual(first, second)

        completed = subprocess.run(
            [sys.executable, str(VALIDATOR), "--fixtures"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("DECISION_ENVELOPE_FIXTURES_VALID cases=15", completed.stdout)
        self.assertNotIn("DECISION_ENVELOPE_FIXTURE_MISMATCH case=", completed.stdout)

    def test_cli_exit_codes_are_finite(self) -> None:
        valid = FIXTURES / "valid/valid_1.json"
        invalid = FIXTURES / "semantic_invalid/semantic_invalid_alias_mismatch.json"
        for path, expected in ((valid, 0), (invalid, 1), (ROOT / "missing.json", 2)):
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR), str(path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(completed.returncode, expected, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
