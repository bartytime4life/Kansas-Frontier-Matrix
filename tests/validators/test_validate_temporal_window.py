"""Focused no-network tests for the KFM TemporalWindow validator."""

from __future__ import annotations

import contextlib
import io
import json
import os
import socket
import subprocess
import sys
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from tools.validators.validate_temporal_window import (
    MAX_FILE_BYTES,
    FIXTURE_ROOT,
    main,
    run_fixture_profile,
    validate_file,
)


ROOT = Path(__file__).resolve().parents[2]
VALID_UTC = FIXTURE_ROOT / "valid/valid_1.json"
VALID_EQUAL_OFFSETS = FIXTURE_ROOT / "valid/valid_2.json"
REVERSED = (
    FIXTURE_ROOT
    / "semantic_invalid/invalid_1_reversed_interval.json"
)


class TemporalWindowValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.candidate_path = self.root / "candidate.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _fixture(self, path: Path) -> dict[str, object]:
        return json.loads(path.read_text(encoding="utf-8"))

    def _write(self, payload: object) -> Path:
        self.candidate_path.write_text(
            json.dumps(payload, indent=2) + "\n",
            encoding="utf-8",
        )
        return self.candidate_path

    def _finding_codes(self, path: Path) -> set[str]:
        return {finding.code for finding in validate_file(path).findings}

    def test_valid_fixtures_pass(self) -> None:
        for path in (VALID_UTC, VALID_EQUAL_OFFSETS):
            with self.subTest(path=path.name):
                result = validate_file(path)
                self.assertTrue(result.ok, result.findings)

    def test_schema_invalid_fixtures_fail_for_reviewed_constraints(self) -> None:
        expected = {
            "invalid_1_missing_time_kind.json": "SCHEMA_INVALID",
            "invalid_2_unknown_time_kind.json": "SCHEMA_INVALID",
            "invalid_3_extra_property.json": "SCHEMA_INVALID",
        }
        for name, code in expected.items():
            with self.subTest(name=name):
                self.assertIn(
                    code,
                    self._finding_codes(FIXTURE_ROOT / "invalid" / name),
                )

    def test_reversed_interval_fails_semantic_ordering(self) -> None:
        self.assertIn("TEMPORAL_ORDER_INVALID", self._finding_codes(REVERSED))

    def test_equal_instants_with_different_offsets_pass(self) -> None:
        result = validate_file(VALID_EQUAL_OFFSETS)
        self.assertTrue(result.ok, result.findings)

    def test_duplicate_json_member_is_rejected(self) -> None:
        self.candidate_path.write_text(
            '{"start":"2026-08-03T12:00:00Z",'
            '"start":"2026-08-03T13:00:00Z",'
            '"end":"2026-08-03T14:00:00Z",'
            '"time_kind":"observed"}\n',
            encoding="utf-8",
        )
        self.assertIn("DUPLICATE_KEY", self._finding_codes(self.candidate_path))

    def test_root_type_and_nonfinite_numbers_fail_closed(self) -> None:
        self._write([])
        self.assertIn("ROOT_TYPE", self._finding_codes(self.candidate_path))

        self.candidate_path.write_text(
            '{"start":"2026-08-03T12:00:00Z",'
            '"end":"2026-08-03T13:00:00Z",'
            '"time_kind":"observed","unexpected":NaN}\n',
            encoding="utf-8",
        )
        self.assertIn(
            "NONFINITE_NUMBER",
            self._finding_codes(self.candidate_path),
        )

    def test_oversized_and_symlink_inputs_fail_closed(self) -> None:
        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (MAX_FILE_BYTES + 1))
        self.assertIn("FILE_TOO_LARGE", self._finding_codes(oversized))

        target = self._write(self._fixture(VALID_UTC))
        linked = self.root / "linked.json"
        linked.symlink_to(target)
        self.assertIn("UNSAFE_FILE", self._finding_codes(linked))

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO inputs require POSIX")
    def test_fifo_input_fails_without_blocking(self) -> None:
        fifo = self.root / "candidate.fifo"
        os.mkfifo(fifo)
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools/validators/validate_temporal_window.py"),
                str(fifo),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("UNSAFE_FILE", completed.stdout)

    def test_validation_performs_no_network_io(self) -> None:
        def unexpected_network(*_args, **_kwargs):
            raise AssertionError("TemporalWindow validation attempted network access")

        with (
            mock.patch.object(socket.socket, "connect", unexpected_network),
            mock.patch.object(socket, "create_connection", unexpected_network),
            mock.patch.object(urllib.request, "urlopen", unexpected_network),
        ):
            self.assertTrue(validate_file(VALID_UTC).ok)
            self.assertEqual(run_fixture_profile(), 0)

    def test_cli_output_is_deterministic_and_does_not_echo_values(self) -> None:
        payload = self._fixture(VALID_UTC)
        payload["end"] = "1999-12-31T23:59:59Z"
        path = self._write(payload)

        outputs: list[str] = []
        for _ in range(2):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                return_code = main([str(path)])
            self.assertEqual(return_code, 1)
            outputs.append(stream.getvalue())

        self.assertEqual(outputs[0], outputs[1])
        self.assertIn("TEMPORAL_ORDER_INVALID", outputs[0])
        self.assertNotIn("1999-12-31", outputs[0])

    def test_fixture_profile_is_non_vacuous_and_polarity_safe(self) -> None:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            return_code = run_fixture_profile()
        self.assertEqual(return_code, 0)
        output = stream.getvalue()
        self.assertEqual(output.count('"outcome":"PASS"'), 2)
        self.assertEqual(output.count('"outcome":"EXPECTED_REJECTION"'), 5)

    def test_fixture_expected_error_mismatch_fails_profile(self) -> None:
        expected_path = (
            FIXTURE_ROOT
            / "semantic_invalid/invalid_1_reversed_interval.expected_error.txt"
        )
        original = expected_path.read_text(encoding="utf-8")
        try:
            expected_path.write_text("nonexistent_code\n", encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(run_fixture_profile(), 1)
        finally:
            expected_path.write_text(original, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
