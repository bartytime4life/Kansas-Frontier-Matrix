from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest.mock import MagicMock, patch

from jsonschema import Draft202012Validator

from tools.validators.source import validate_source_rights_currentness_assessment as validator

ROOT = Path(__file__).resolve().parents[2]


class SourceRightsCurrentnessInputTests(unittest.TestCase):
    def read_bytes(self, payload: bytes) -> tuple[dict | None, tuple[validator.Finding, ...]]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "assessment.json"
            path.write_bytes(payload)
            return validator._read(path)

    def assert_finding(self, payload: bytes, code: str) -> None:
        self.assertEqual((None, (validator.Finding(code, "/"),)), self.read_bytes(payload))

    def test_exact_byte_limit_is_readable(self) -> None:
        payload = b"{}" + b" " * (validator.MAX_BYTES - 2)
        self.assertEqual(({}, ()), self.read_bytes(payload))

    def test_one_byte_over_limit_is_rejected(self) -> None:
        self.assert_finding(b"{}" + b" " * (validator.MAX_BYTES - 1), "RIGHTS_INPUT_TOO_LARGE")

    def test_read_budget_does_not_trust_small_metadata(self) -> None:
        # A deterministic stream stand-in, not a race or a live-system test.
        path = MagicMock(spec=Path)
        path.is_symlink.return_value = False
        path.is_file.return_value = True
        path.stat.return_value.st_size = 2
        payload = b"{}" + b" " * validator.MAX_BYTES
        path.read_text.return_value = payload.decode("utf-8")
        stream = MagicMock(wraps=io.BytesIO(payload))
        path.open.return_value.__enter__.return_value = stream
        self.assertEqual(
            (None, (validator.Finding("RIGHTS_INPUT_TOO_LARGE", "/"),)),
            validator._read(path),
        )
        path.open.assert_called_once_with("rb")
        stream.read.assert_called_once_with(validator.MAX_BYTES + 1)
        path.read_text.assert_not_called()
        path.open.return_value.__exit__.assert_called_once()

    def test_multibyte_utf8_uses_byte_not_character_budget(self) -> None:
        payload = '{"label":"é"}'.encode("utf-8")
        with patch.object(validator, "MAX_BYTES", len(payload)):
            self.assertEqual(({"label": "é"}, ()), self.read_bytes(payload))
            self.assert_finding(payload + b" ", "RIGHTS_INPUT_TOO_LARGE")

    def test_invalid_utf8_is_json_invalid(self) -> None:
        self.assert_finding(b'{"label":"\xff"}', "RIGHTS_JSON_INVALID")

    def test_malformed_json_is_invalid(self) -> None:
        for payload in (b"", b"{", b"{}{}", b"\xef\xbb\xbf{}"):
            with self.subTest(payload=payload):
                self.assert_finding(payload, "RIGHTS_JSON_INVALID")

    def test_duplicate_keys_keep_specific_finding(self) -> None:
        self.assert_finding(b'{"x":1,"x":2}', "RIGHTS_JSON_DUPLICATE_KEY")

    def test_nonfinite_numbers_keep_specific_finding(self) -> None:
        for number in (b"NaN", b"Infinity", b"-Infinity", b"1e999", b"-1e999"):
            with self.subTest(number=number):
                self.assert_finding(b'{"x":' + number + b"}", "RIGHTS_JSON_NONFINITE_NUMBER")

    def test_non_object_roots_are_rejected(self) -> None:
        for payload in (b"[]", b"null", b"true", b"1", b'"text"'):
            with self.subTest(payload=payload):
                self.assert_finding(payload, "RIGHTS_ROOT_NOT_OBJECT")

    def test_integer_digit_limit_is_json_invalid(self) -> None:
        previous_limit = sys.get_int_max_str_digits()
        try:
            sys.set_int_max_str_digits(640)
            self.assert_finding(b'{"x":' + b"9" * 641 + b"}", "RIGHTS_JSON_INVALID")
        finally:
            sys.set_int_max_str_digits(previous_limit)

    def test_parser_recursion_limit_is_json_invalid(self) -> None:
        with patch.object(validator.json, "loads", side_effect=RecursionError):
            self.assert_finding(b"{}", "RIGHTS_JSON_INVALID")

    def test_unreadable_file_is_json_invalid(self) -> None:
        path = MagicMock(spec=Path)
        path.is_symlink.return_value = False
        path.is_file.return_value = True
        path.stat.return_value.st_size = 2
        path.open.side_effect = OSError
        self.assertEqual(
            (None, (validator.Finding("RIGHTS_JSON_INVALID", "/"),)),
            validator._read(path),
        )

    def test_symlinks_are_denied_before_read(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_bytes(b"{}")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            with patch.object(Path, "open", side_effect=AssertionError("must not read")):
                self.assertEqual(
                    (None, (validator.Finding("RIGHTS_INPUT_SYMLINK_DENIED", "/"),)),
                    validator._read(link),
                )

    def test_directory_and_missing_file_are_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for path in (Path(directory), Path(directory) / "missing.json"):
                with self.subTest(path=path.name):
                    self.assertEqual(
                        (None, (validator.Finding("RIGHTS_INPUT_NOT_FILE", "/"),)),
                        validator._read(path),
                    )

    def test_cli_errors_have_finite_shape_without_payload_echo(self) -> None:
        cases = (
            (b'{"secret_marker":', "RIGHTS_JSON_INVALID"),
            (b'{"secret_marker":1,"secret_marker":2}', "RIGHTS_JSON_DUPLICATE_KEY"),
            (b'{"secret_marker":NaN}', "RIGHTS_JSON_NONFINITE_NUMBER"),
            (b" " * (validator.MAX_BYTES + 1), "RIGHTS_INPUT_TOO_LARGE"),
            (b'{"secret_marker":' + b"9" * 641 + b"}", "RIGHTS_JSON_INVALID"),
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            for payload, code in cases:
                with self.subTest(code=code, size=len(payload)):
                    path.write_bytes(payload)
                    completed = subprocess.run(
                        [sys.executable, "-X", "int_max_str_digits=640", str(Path(validator.__file__)), str(path)],
                        cwd=ROOT, check=False, capture_output=True, text=True,
                    )
                    self.assertEqual(2, completed.returncode)
                    self.assertEqual("", completed.stderr)
                    self.assertNotIn("secret_marker", completed.stdout)
                    expected = {
                        "authority": "NONE",
                        "execution_mode": "FIXTURE_ONLY",
                        "file": path.as_posix(),
                        "findings": [{"code": code, "path": "/"}],
                        "non_effects": [
                            "no_network", "no_source_activation", "no_fetch",
                            "no_raw_write", "no_promotion", "no_release", "no_publication",
                        ],
                        "outcome": "ERROR",
                    }
                    self.assertEqual(expected, json.loads(completed.stdout))


class SourceRightsCurrentnessAssessmentTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_cases(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_is_non_vacuous(self) -> None:
        manifest = validator.load_fixtures()
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, set(outcomes))
        self.assertGreaterEqual(outcomes["DENY"], 8)

    def test_identity_is_deterministic(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(json.loads(json.dumps(document)))
        self.assertEqual(first, second)

    def test_governance_non_effects_are_false(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        self.assertEqual("FIXTURE_ONLY", document["governance"]["execution_mode"])
        self.assertFalse(any(value for key, value in document["governance"].items() if key != "execution_mode"))

    def test_validator_has_no_network_client_import(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "socket."):
            self.assertNotIn(token, source)

    def test_fixture_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(Path(validator.__file__)), "--fixtures"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_invalid_json_cli_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text("{", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(2, completed.returncode)
        self.assertIn('"outcome":"ERROR"', completed.stdout)


if __name__ == "__main__":
    unittest.main()
