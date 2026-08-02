#!/usr/bin/env python3
"""Deterministic tests for the synthetic station soil-moisture profile."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import subprocess
import sys
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.domains.soil.moisture.validate_soil_moisture import (  # noqa: E402
    MAX_READINGS,
    Finding,
    main,
    reading_dedupe_key,
    validate_candidate,
    validate_file,
)


VALIDATOR = (
    REPO_ROOT
    / "tools"
    / "validators"
    / "domains"
    / "soil"
    / "moisture"
    / "validate_soil_moisture.py"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures" / "domains" / "soil" / "soil_moisture"
VALID_FIXTURE_DIR = FIXTURE_ROOT / "valid"
INVALID_FIXTURE_DIR = FIXTURE_ROOT / "invalid"

VALID_FIXTURE_NAMES = (
    "boundary_values.json",
    "station_series.json",
)
INVALID_FIXTURE_NAMES = (
    "duplicate_reading.json",
    "invalid_measurement_time.json",
    "invalid_shapes.json",
    "invalid_source_profile.json",
    "missing_identity.json",
    "unsafe_spatial_support.json",
)


def _valid_fixture(name: str = "station_series.json") -> Path:
    return VALID_FIXTURE_DIR / name


def _invalid_fixture(name: str) -> Path:
    return INVALID_FIXTURE_DIR / name


def _sidecar_for(fixture: Path) -> Path:
    return fixture.with_suffix(".expected_error.txt")


def _load_candidate(name: str = "station_series.json") -> dict[str, object]:
    return json.loads(_valid_fixture(name).read_text(encoding="utf-8"))


def _load_expected_findings(sidecar: Path) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    for line_number, raw_line in enumerate(
        sidecar.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw_line:
            continue
        code, separator, path = raw_line.partition("\t")
        if not separator or not code or not path:
            raise AssertionError(
                f"malformed expected-error sidecar line {line_number}: {sidecar}"
            )
        findings.append(Finding(code=code, path=path))
    return tuple(findings)


class SoilMoistureFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        network_block = RuntimeError("network access is forbidden in soil-moisture tests")
        self.network_mocks: list[mock.Mock] = []
        patchers = (
            mock.patch.object(socket.socket, "connect", side_effect=network_block),
            mock.patch.object(socket.socket, "connect_ex", side_effect=network_block),
            mock.patch.object(socket, "create_connection", side_effect=network_block),
            mock.patch.object(socket, "getaddrinfo", side_effect=network_block),
            mock.patch.object(urllib.request, "urlopen", side_effect=network_block),
        )
        for patcher in patchers:
            self.network_mocks.append(patcher.start())
            self.addCleanup(patcher.stop)

    def test_valid_fixture_inventory_is_explicit_and_positive(self) -> None:
        accepted = {_valid_fixture(name) for name in VALID_FIXTURE_NAMES}
        self.assertEqual(set(VALID_FIXTURE_DIR.glob("*.json")), accepted)
        for fixture in sorted(accepted):
            with self.subTest(fixture=fixture.name):
                self.assertEqual(validate_file(fixture), [])

    def test_invalid_fixture_inventory_and_sidecars_are_explicit(self) -> None:
        accepted = {_invalid_fixture(name) for name in INVALID_FIXTURE_NAMES}
        self.assertEqual(set(INVALID_FIXTURE_DIR.glob("*.json")), accepted)
        self.assertEqual(
            set(INVALID_FIXTURE_DIR.glob("*.expected_error.txt")),
            {_sidecar_for(fixture) for fixture in accepted},
        )

    def test_invalid_findings_match_exact_sorted_sidecars(self) -> None:
        for name in INVALID_FIXTURE_NAMES:
            fixture = _invalid_fixture(name)
            expected = _load_expected_findings(_sidecar_for(fixture))
            with self.subTest(fixture=name):
                self.assertTrue(expected)
                self.assertEqual(expected, tuple(sorted(expected)))
                self.assertEqual(tuple(validate_file(fixture)), expected)

    def test_dedupe_identity_excludes_value_and_qc_but_includes_depth(self) -> None:
        candidate = _load_candidate()
        readings = candidate["readings"]
        self.assertIsInstance(readings, list)
        first = readings[0]
        self.assertIsInstance(first, dict)
        key = reading_dedupe_key(first)
        self.assertIsNotNone(key)

        same_identity = copy.deepcopy(first)
        same_identity["value"] = 0.99
        same_identity["qc_flags"] = ["synthetic-revised"]
        self.assertEqual(reading_dedupe_key(same_identity), key)

        different_depth = copy.deepcopy(first)
        different_depth["depth_cm"] = 30
        self.assertNotEqual(reading_dedupe_key(different_depth), key)

    def test_numeric_boundaries_accept_zero_and_one_but_reject_booleans(self) -> None:
        self.assertEqual(validate_file(_valid_fixture("boundary_values.json")), [])

        candidate = _load_candidate("boundary_values.json")
        readings = candidate["readings"]
        self.assertIsInstance(readings, list)
        first = readings[0]
        self.assertIsInstance(first, dict)
        first["depth_cm"] = True
        first["value"] = False
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding("DEPTH_CM_INVALID", "$.readings[0].depth_cm"),
                Finding("VALUE_OUT_OF_RANGE", "$.readings[0].value"),
            ],
        )

    def test_timestamp_requires_canonical_z_and_source_timezone(self) -> None:
        candidate = _load_candidate()
        readings = candidate["readings"]
        self.assertIsInstance(readings, list)
        first = readings[0]
        self.assertIsInstance(first, dict)
        first["timestamp_iso"] = "2026-04-15T14:00:00+00:00"
        first["source_timezone"] = ""
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding("SOURCE_TIMEZONE_MISSING", "$.readings[0].source_timezone"),
                Finding(
                    "TIMESTAMP_NOT_CANONICAL_UTC",
                    "$.readings[0].timestamp_iso",
                ),
            ],
        )

    def test_all_zero_spec_hash_is_rejected_as_a_placeholder(self) -> None:
        candidate = _load_candidate()
        candidate["spec_hash"] = "sha256:" + ("0" * 64)
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("SPEC_HASH_PLACEHOLDER", "$.spec_hash")],
        )

    def test_reading_count_is_bounded_before_per_reading_work(self) -> None:
        candidate = _load_candidate()
        readings = candidate["readings"]
        self.assertIsInstance(readings, list)
        candidate["readings"] = [copy.deepcopy(readings[0])] * (MAX_READINGS + 1)
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("READING_COUNT_EXCEEDED", "$.readings")],
        )

    def test_findings_are_sorted_and_insertion_order_independent(self) -> None:
        candidate = _load_candidate()
        candidate["zeta"] = "synthetic-zeta"
        candidate["alpha"] = "synthetic-alpha"
        first = validate_candidate(candidate)

        reordered = dict(reversed(list(copy.deepcopy(candidate).items())))
        second = validate_candidate(reordered)
        self.assertEqual(first, sorted(set(first)))
        self.assertEqual(second, first)

    def test_validation_never_attempts_network_access(self) -> None:
        self.assertEqual(validate_file(_valid_fixture()), [])
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()

    def test_loader_rejects_duplicate_keys_without_echoing_values(self) -> None:
        sentinel = "SOIL_MOISTURE_SENTINEL_MUST_NOT_LEAK"
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = Path(temp_dir) / "duplicate.json"
            fixture.write_text(
                '{"record_id":"' + sentinel + '","record_id":"duplicate"}',
                encoding="utf-8",
            )
            self.assertEqual(validate_file(fixture), [Finding("FIXTURE_JSON_INVALID", "$")])

            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                exit_code = main([str(fixture)])
            self.assertEqual(exit_code, 1)
            self.assertNotIn(sentinel, stdout.getvalue())
            self.assertNotIn(sentinel, stderr.getvalue())

    def test_cli_exit_codes_and_machine_readable_non_echoing_output(self) -> None:
        cases = (
            (0, [str(_valid_fixture())]),
            (1, [str(_invalid_fixture("missing_identity.json"))]),
            (2, []),
        )
        for expected_exit, arguments in cases:
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR), *arguments],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            with self.subTest(expected_exit=expected_exit):
                self.assertEqual(completed.returncode, expected_exit)
                for line in completed.stdout.splitlines():
                    payload = json.loads(line)
                    self.assertEqual(payload["scope"], "soil-moisture-station-fixture")
                    self.assertIn(payload["status"], {"PASS", "FAIL"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
