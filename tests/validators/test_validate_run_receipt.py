from __future__ import annotations

import contextlib
import copy
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from tools.validators._common.jsonschema_runner import load_validator
from tools.validators.validate_run_receipt import (
    MAX_FILE_BYTES,
    MAX_SCHEMA_FINDINGS,
    SCHEMA_PATH,
    _expected_rejection_matches,
    main,
    validate_receipt,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "fixtures/contracts/v1/runtime/run_receipt"
VALID_304 = FIXTURES / "valid/valid_2_http_304_no_op.json"
VALID_MATERIALIZE = FIXTURES / "valid/valid_3_http_200_materialize.json"
VALID_DRIFT = FIXTURES / "valid/valid_4_http_200_validator_drift.json"


class RunReceiptValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.receipt_path = self.root / "receipt.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    @staticmethod
    def _fixture(path: Path) -> dict[str, object]:
        return json.loads(path.read_text(encoding="utf-8"))

    def _write(self, payload: dict[str, object]) -> Path:
        self.receipt_path.write_text(
            json.dumps(payload, indent=2) + "\n", encoding="utf-8"
        )
        return self.receipt_path

    def _mutated(self, fixture: Path, mutate) -> Path:
        payload = copy.deepcopy(self._fixture(fixture))
        mutate(payload)
        return self._write(payload)

    def assertFinding(self, path: Path, code: str) -> None:
        result = validate_receipt(path)
        self.assertIn(code, {finding.code for finding in result.findings})

    def test_generic_and_smart_sync_positive_fixtures_pass(self) -> None:
        paths = [
            FIXTURES / "valid/valid_1.json",
            FIXTURES / "valid/valid_2.json",
            VALID_304,
            VALID_MATERIALIZE,
            VALID_DRIFT,
        ]
        for path in paths:
            with self.subTest(path=path.name):
                result = validate_receipt(path)
                self.assertTrue(result.ok, result.findings)

    def test_http_200_decision_must_match_content_digest(self) -> None:
        unchanged = self._mutated(
            VALID_MATERIALIZE,
            lambda value: value["smart_sync"].update(
                content_digest=value["smart_sync"]["prior_content_digest"]
            ),
        )
        self.assertFinding(unchanged, "UNCHANGED_MATERIALIZATION")

        changed = self._mutated(
            VALID_DRIFT,
            lambda value: value["smart_sync"].update(
                content_digest="sha256:" + ("4" * 64)
            ),
        )
        self.assertFinding(changed, "CHANGED_CONTENT_NO_OP")

    def test_source_url_rejects_unsafe_components_without_echoing_values(self) -> None:
        unsafe_urls = (
            "https://example.invalid/data?token=synthetic-secret",
            "https://user:password@example.invalid/data",
            "https://example.invalid/data#fragment",
            "https://[::1",
            "https://example.invalid:99999/data",
            "https://example.invalid/data\n",
            "https://example.invalid/data\x00",
            "https://example.invalid/data\ufeff",
            "https://example.invalid/data\u202e",
            "https://example.invalid/a\ud800b",
            "https://example.invalid/%GG",
            "https://example.invalid\\evil",
        )
        for source_url in unsafe_urls:
            with self.subTest(source_url=repr(source_url)):
                path = self._mutated(
                    VALID_304,
                    lambda value, source_url=source_url: value["smart_sync"].update(
                        source_url=source_url
                    ),
                )
                self.assertFinding(path, "UNSAFE_SOURCE_URL")

        valid_escape = self._mutated(
            VALID_304,
            lambda value: value["smart_sync"].update(
                source_url="https://example.invalid/a%20b"
            ),
        )
        self.assertTrue(validate_receipt(valid_escape).ok)

        secret = "synthetic-secret-value"
        path = self._mutated(
            VALID_304,
            lambda value: value["smart_sync"].update(
                source_url=f"https://example.invalid/data?token={secret}"
            ),
        )
        outputs = []
        for _ in range(2):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                self.assertEqual(main([str(path)]), 1)
            outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertIn("UNSAFE_SOURCE_URL", outputs[0])
        self.assertNotIn(secret, outputs[0])

    def test_etag_and_http_date_grammar_and_304_consistency(self) -> None:
        unquoted = self._mutated(
            VALID_304,
            lambda value: value["smart_sync"]["http_validators"]["request"].update(
                etag="unquoted-etag"
            ),
        )
        self.assertFinding(unquoted, "INVALID_ETAG")

        for etag in ('"a b"', '"a\tb"', '"a\x00b"', '"a\x7fb"', '"snowman-☃"'):
            with self.subTest(etag=repr(etag)):
                path = self._mutated(
                    VALID_304,
                    lambda value, etag=etag: value["smart_sync"]["http_validators"][
                        "request"
                    ].update(etag=etag),
                )
                self.assertFinding(path, "INVALID_ETAG")

        for date_value in (
            "not-an-http-date",
            "Mon, 03 Aug 2026 11:00:00 +0000",
            "Tue, 03 Aug 2026 11:00:00 GMT",
        ):
            with self.subTest(date_value=date_value):
                path = self._mutated(
                    VALID_304,
                    lambda value, date_value=date_value: value["smart_sync"][
                        "http_validators"
                    ]["request"].update(last_modified=date_value),
                )
                self.assertFinding(path, "INVALID_HTTP_DATE")

        mismatch = self._mutated(
            VALID_304,
            lambda value: value["smart_sync"]["http_validators"]["response"].update(
                etag='"different"'
            ),
        )
        self.assertFinding(mismatch, "NOT_MODIFIED_VALIDATOR_MISMATCH")

        def last_modified_only(value):
            request = value["smart_sync"]["http_validators"]["request"]
            response = value["smart_sync"]["http_validators"]["response"]
            request.clear()
            response.clear()
            request["last_modified"] = "Mon, 03 Aug 2026 12:00:00 GMT"
            response["last_modified"] = "Mon, 03 Aug 2026 13:00:00 GMT"

        self.assertFinding(
            self._mutated(VALID_304, last_modified_only),
            "NOT_MODIFIED_VALIDATOR_MISMATCH",
        )

    def test_identity_and_profile_bindings_fail_closed(self) -> None:
        cases = (
            (
                VALID_304,
                lambda value: value["smart_sync"].update(
                    prior_run_receipt_ref=value["run_id"]
                ),
                "SELF_PRIOR_RECEIPT",
            ),
            (
                VALID_304,
                lambda value: value["smart_sync"].update(
                    prior_content_digest="sha256:" + ("0" * 64)
                ),
                "PLACEHOLDER_DIGEST",
            ),
            (
                FIXTURES / "valid/valid_1.json",
                lambda value: value.update(spec_hash="sha256:" + ("0" * 64)),
                "PLACEHOLDER_DIGEST",
            ),
        )
        for fixture, mutate, code in cases:
            with self.subTest(fixture=fixture.name, code=code):
                self.assertFinding(self._mutated(fixture, mutate), code)

        payload = self._fixture(FIXTURES / "valid/valid_1.json")
        payload["stage"] = "smart_sync"
        self.assertFinding(self._write(payload), "SCHEMA")

        for mutate in (
            lambda value: value.update(inputs=[" \t"]),
            lambda value: value.update(outputs=[" \t"]),
            lambda value: value.update(code_ref=" \t"),
            lambda value: value["smart_sync"].update(prior_run_receipt_ref=" \t"),
        ):
            with self.subTest(mutate=mutate):
                self.assertFinding(self._mutated(VALID_MATERIALIZE, mutate), "SCHEMA")

    def test_parser_budgets_duplicate_keys_and_file_types_fail_closed(self) -> None:
        duplicate = VALID_304.read_text(encoding="utf-8").replace(
            '  "run_id": "run:smart-sync:synthetic-304",',
            '  "run_id": "run:smart-sync:synthetic-304",\n'
            '  "run_id": "run:smart-sync:duplicate",',
            1,
        )
        self.receipt_path.write_text(duplicate, encoding="utf-8")
        self.assertFinding(self.receipt_path, "DUPLICATE_KEY")

        nonfinite = VALID_304.read_text(encoding="utf-8").replace(
            '"http_status": 304', '"http_status": NaN', 1
        )
        self.receipt_path.write_text(nonfinite, encoding="utf-8")
        self.assertFinding(self.receipt_path, "NONFINITE_NUMBER")

        nested = "[" * 1500 + "0" + "]" * 1500
        self.receipt_path.write_text('{"nested":' + nested + "}\n", encoding="utf-8")
        self.assertFinding(self.receipt_path, "JSON_COMPLEXITY_LIMIT")

        payload = self._fixture(FIXTURES / "valid/valid_1.json")
        payload["inputs"] = [{} for _ in range(MAX_SCHEMA_FINDINGS + 50)]
        result = validate_receipt(self._write(payload))
        self.assertIn(
            "SCHEMA_FINDINGS_TRUNCATED",
            {finding.code for finding in result.findings},
        )
        self.assertLessEqual(len(result.findings), MAX_SCHEMA_FINDINGS + 1)

        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (MAX_FILE_BYTES + 1))
        self.assertFinding(oversized, "FILE_TOO_LARGE")

        target = self._write(self._fixture(VALID_304))
        linked = self.root / "linked.json"
        linked.symlink_to(target)
        self.assertFinding(linked, "UNSAFE_FILE")

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO inputs require POSIX")
    def test_fifo_input_fails_without_blocking(self) -> None:
        fifo = self.root / "receipt.fifo"
        os.mkfifo(fifo)
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools/validators/validate_run_receipt.py"),
                str(fifo),
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("UNSAFE_FILE", completed.stdout)

    def test_validation_performs_no_network_io(self) -> None:
        with mock.patch("socket.socket", side_effect=AssertionError("network attempted")):
            result = validate_receipt(VALID_304)
        self.assertTrue(result.ok, result.findings)

    def test_fixture_mode_and_sidecar_polarity(self) -> None:
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            exit_code = main(["--fixtures"])
        self.assertEqual(exit_code, 0)
        self.assertIn("smart-sync status=304 decision=no_op", stdout.getvalue())
        self.assertIn("EXPECTED_FAIL", stdout.getvalue())

        validator = load_validator(SCHEMA_PATH)
        for path in sorted((FIXTURES / "invalid").glob("*.json")):
            with self.subTest(path=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                result = validate_receipt(path)
                self.assertTrue(
                    _expected_rejection_matches(path, payload, result, validator)
                )

    def test_sidecar_matching_is_literal_exact_and_bounded(self) -> None:
        path = self.root / "invalid.json"
        payload = self._fixture(FIXTURES / "invalid/invalid_1.json")
        path.write_text(json.dumps(payload), encoding="utf-8")
        path.with_suffix(".expected_error.txt").write_text("(\n", encoding="utf-8")
        result = validate_receipt(path)
        validator = load_validator(SCHEMA_PATH)
        self.assertFalse(
            _expected_rejection_matches(path, payload, result, validator)
        )

        crossed = self._fixture(FIXTURES / "valid/valid_1.json")
        crossed["run_id"] = "BAD"
        del crossed["code_ref"]
        path.write_text(json.dumps(crossed), encoding="utf-8")
        path.with_suffix(".expected_error.txt").write_text(
            '{"kind":"schema","field":"/","keyword":"required",'
            '"contains":"run_id"}\n',
            encoding="utf-8",
        )
        self.assertFalse(
            _expected_rejection_matches(
                path, crossed, validate_receipt(path), validator
            )
        )

        seen = 0

        def many_errors(_payload):
            nonlocal seen
            for _ in range(MAX_SCHEMA_FINDINGS + 50):
                seen += 1
                yield SimpleNamespace(
                    absolute_path=(),
                    validator="required",
                    message="'run_id' is a required property",
                )

        path.write_text(json.dumps(payload), encoding="utf-8")
        path.with_suffix(".expected_error.txt").write_text(
            '{"kind":"schema","field":"/","keyword":"required",'
            '"contains":"run_id"}\n',
            encoding="utf-8",
        )
        bounded_validator = SimpleNamespace(iter_errors=many_errors)
        self.assertTrue(
            _expected_rejection_matches(
                path, payload, validate_receipt(path), bounded_validator
            )
        )
        self.assertEqual(seen, MAX_SCHEMA_FINDINGS + 1)


if __name__ == "__main__":
    unittest.main()
