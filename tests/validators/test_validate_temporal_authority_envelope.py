"""Deterministic no-network tests for TemporalAuthorityEnvelope validation."""

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

from tools.validators.validate_temporal_authority_envelope import (
    FIXTURE_ROOT,
    MAX_FILE_BYTES,
    MAX_SCHEMA_FINDINGS,
    main,
    validate_envelope,
)

ROOT = Path(__file__).resolve().parents[2]
VALID = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
INVALID = sorted((FIXTURE_ROOT / "invalid").glob("*.json"))
SEMANTIC_INVALID = sorted((FIXTURE_ROOT / "semantic_invalid").glob("*.json"))
OBSERVED = FIXTURE_ROOT / "valid" / "valid_1_observed_condition.json"
REGULATORY = FIXTURE_ROOT / "valid" / "valid_2_future_effective_regulatory.json"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("TemporalAuthorityEnvelope validation attempted network access")


class TemporalAuthorityEnvelopeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.path = self.root / "envelope.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _fixture(self, path: Path = OBSERVED) -> dict[str, object]:
        return json.loads(path.read_text(encoding="utf-8"))

    def _write(self, payload: dict[str, object]) -> Path:
        self.path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return self.path

    def assertCode(self, path: Path, code: str) -> None:
        result = validate_envelope(path)
        self.assertIn(code, {finding.code for finding in result.findings})

    def test_all_valid_fixtures_pass(self) -> None:
        self.assertEqual(len(VALID), 4)
        for path in VALID:
            with self.subTest(path=path.name):
                result = validate_envelope(path)
                self.assertTrue(result.ok, result.findings)

    def test_schema_and_semantic_negative_fixtures_match_sidecars(self) -> None:
        self.assertEqual(len(INVALID), 7)
        self.assertEqual(len(SEMANTIC_INVALID), 7)
        for path in (*INVALID, *SEMANTIC_INVALID):
            with self.subTest(path=path.name):
                expected = {
                    line.strip()
                    for line in path.with_suffix(".expected_findings.txt")
                    .read_text(encoding="utf-8")
                    .splitlines()
                    if line.strip()
                }
                result = validate_envelope(path)
                actual = {finding.code for finding in result.findings}
                self.assertFalse(result.ok)
                self.assertEqual(actual, expected)

    def test_future_effective_regulatory_record_is_not_rejected(self) -> None:
        result = validate_envelope(REGULATORY)
        self.assertTrue(result.ok, result.findings)

    def test_source_role_reference_must_bind_to_declared_descriptor(self) -> None:
        payload = self._fixture()
        payload["source"]["source_role_ref"] = "src:synthetic:other-feed#/source_role"
        self.assertCode(self._write(payload), "SOURCE_ROLE_REF_UNBOUND")

    def test_timezone_naive_time_is_rejected_even_if_format_checker_drifts(self) -> None:
        payload = self._fixture()
        payload["time"]["retrieved_at"] = "2026-08-03T12:05:00"
        self.assertCode(self._write(payload), "TEMPORAL_TIMEZONE_REQUIRED")

    def test_temporal_and_lineage_semantics_fail_closed(self) -> None:
        cases = (
            (
                lambda value: value["time"].update(
                    valid_from="2026-08-04T00:00:00Z",
                    valid_to="2026-08-03T00:00:00Z",
                ),
                "TEMPORAL_ORDER_INVALID",
            ),
            (
                lambda value: value["time"].update(
                    observed_at="2026-08-03T12:10:00Z"
                ),
                "SOURCE_TIME_AFTER_RETRIEVAL",
            ),
            (
                lambda value: value["identity"].update(
                    revision_id=value["identity"]["object_id"]
                ),
                "REVISION_ID_COLLAPSE",
            ),
            (
                lambda value: value["lineage"].update(
                    supersedes=[value["identity"]["revision_id"]]
                ),
                "SELF_LINEAGE_REFERENCE",
            ),
        )
        for mutate, code in cases:
            with self.subTest(code=code):
                payload = self._fixture()
                mutate(payload)
                self.assertCode(self._write(payload), code)

    def test_duplicate_keys_nonfinite_numbers_and_nesting_are_rejected(self) -> None:
        text = OBSERVED.read_text(encoding="utf-8")
        duplicate = text.replace(
            '  "schema_version": "1.0.0",',
            '  "schema_version": "1.0.0",\n  "schema_version": "1.0.0",',
            1,
        )
        self.path.write_text(duplicate, encoding="utf-8")
        self.assertCode(self.path, "DUPLICATE_KEY")

        self.path.write_text('{"value": NaN}\n', encoding="utf-8")
        self.assertCode(self.path, "NONFINITE_NUMBER")

        nested = "[" * 100 + "0" + "]" * 100
        self.path.write_text('{"nested":' + nested + "}\n", encoding="utf-8")
        self.assertCode(self.path, "JSON_COMPLEXITY_LIMIT")

    def test_schema_diagnostics_are_bounded(self) -> None:
        payload = self._fixture()
        payload["lineage"]["supersedes"] = [0 for _ in range(MAX_SCHEMA_FINDINGS + 50)]
        result = validate_envelope(self._write(payload))
        self.assertIn(
            "SCHEMA_FINDINGS_TRUNCATED",
            {finding.code for finding in result.findings},
        )
        self.assertLessEqual(len(result.findings), MAX_SCHEMA_FINDINGS + 1)

    def test_oversized_and_symbolic_link_inputs_fail_closed(self) -> None:
        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (MAX_FILE_BYTES + 1))
        self.assertCode(oversized, "FILE_TOO_LARGE")

        target = self._write(self._fixture())
        linked = self.root / "linked.json"
        linked.symlink_to(target)
        self.assertCode(linked, "UNSAFE_FILE")

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO inputs require POSIX")
    def test_fifo_input_fails_without_blocking(self) -> None:
        fifo = self.root / "envelope.fifo"
        os.mkfifo(fifo)
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools/validators/validate_temporal_authority_envelope.py"),
                str(fifo),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("UNSAFE_FILE", completed.stdout)

    def test_validation_performs_no_network_io(self) -> None:
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            result = validate_envelope(OBSERVED)
        self.assertTrue(result.ok, result.findings)

    def test_cli_output_is_deterministic_and_does_not_echo_values(self) -> None:
        payload = self._fixture()
        secret_marker = "synthetic-sensitive-marker"
        payload["source"]["authority_scope"] = secret_marker
        payload["governance"]["public_use_allowed"] = True
        path = self._write(payload)
        outputs = []
        for _ in range(2):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                code = main([str(path)])
            self.assertEqual(code, 1)
            outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(secret_marker, outputs[0])

    def test_fixture_cli_passes(self) -> None:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(["--fixtures"])
        self.assertEqual(code, 0, stream.getvalue())
        self.assertNotIn("FIXTURE_POLARITY_ERROR", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
