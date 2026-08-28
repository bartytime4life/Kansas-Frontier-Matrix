#!/usr/bin/env python3
"""Deterministic tests for the synthetic Hydrology flow profile."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(REPO_ROOT))

from tools.validators.domains.hydrology.validate_public_safe_flow_fixture import (  # noqa: E402
    FORBIDDEN_LOCATION_ALIASES,
    MAX_FIXTURE_BYTES,
    Finding,
    main,
    validate_candidate,
    validate_file,
)


FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/hydrology/public_safe_flow"
VALID_FIXTURE = FIXTURE_ROOT / "valid/public_safe_flow.json"
INVALID_FIXTURE = (
    FIXTURE_ROOT / "invalid/role_location_time_governance_collapse.json"
)
EXPECTED_ERROR = INVALID_FIXTURE.with_suffix(".expected_error.txt")


def _load_candidate() -> dict[str, object]:
    return json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))


def _load_expected() -> list[Finding]:
    findings: list[Finding] = []
    for line in EXPECTED_ERROR.read_text(encoding="utf-8").splitlines():
        code, separator, path = line.partition("\t")
        if not separator:
            raise AssertionError(f"malformed expected-error sidecar: {line!r}")
        findings.append(Finding(code, path))
    return findings


class HydrologyFlowFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        denied = RuntimeError("network access is forbidden in Hydrology tests")
        for patcher in (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
            mock.patch.object(socket, "create_connection", side_effect=denied),
            mock.patch.object(socket, "getaddrinfo", side_effect=denied),
            mock.patch.object(urllib.request, "urlopen", side_effect=denied),
        ):
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_fixture_inventory_is_explicit_and_polarized(self) -> None:
        self.assertEqual(list((FIXTURE_ROOT / "valid").glob("*.json")), [VALID_FIXTURE])
        self.assertEqual(
            list((FIXTURE_ROOT / "invalid").glob("*.json")), [INVALID_FIXTURE]
        )
        self.assertEqual(validate_file(VALID_FIXTURE), [])
        expected = _load_expected()
        self.assertEqual(expected, sorted(expected))
        self.assertEqual(validate_file(INVALID_FIXTURE), expected)

    def test_measurement_boundaries_and_boolean_separation(self) -> None:
        for value in (0, 1_000_000_000):
            candidate = _load_candidate()
            candidate["measurement"]["value"] = value  # type: ignore[index]
            self.assertEqual(validate_candidate(candidate), [])
        for value in (-1, 1_000_000_001, True, False, float("nan"), float("inf")):
            candidate = _load_candidate()
            candidate["measurement"]["value"] = value  # type: ignore[index]
            self.assertIn(
                Finding("MEASUREMENT_VALUE_OUT_OF_RANGE", "$.measurement.value"),
                validate_candidate(candidate),
            )

    def test_no_data_must_be_the_boolean_false(self) -> None:
        for value in (0, "false", None, True):
            candidate = _load_candidate()
            candidate["measurement"]["no_data"] = value  # type: ignore[index]
            self.assertIn(
                Finding("NO_DATA_STATE_INVALID", "$.measurement.no_data"),
                validate_candidate(candidate),
            )

    def test_temporal_axes_remain_valid_and_ordered(self) -> None:
        candidate = _load_candidate()
        candidate["temporal_scope"] = {
            "observed_at": "2026-08-02T12:00:00Z",
            "retrieved_at": "2026-08-02T11:59:59Z",
        }
        self.assertIn(
            Finding("TEMPORAL_ORDER_INVALID", "$.temporal_scope"),
            validate_candidate(candidate),
        )
        candidate["temporal_scope"] = {
            "observed_at": "2026-08-02T12:00:00+00:00",
            "retrieved_at": "2026-08-02T12:05:00Z",
        }
        self.assertIn(
            Finding("OBSERVED_TIME_INVALID", "$.temporal_scope.observed_at"),
            validate_candidate(candidate),
        )

    def test_precise_location_aliases_are_forbidden(self) -> None:
        for alias in sorted(FORBIDDEN_LOCATION_ALIASES):
            candidate = _load_candidate()
            candidate["spatial_support"][alias.upper()] = "protected"  # type: ignore[index]
            self.assertIn(
                Finding(
                    "PRECISE_LOCATION_FIELD_FORBIDDEN",
                    f"$.spatial_support.{alias.upper()}",
                ),
                validate_candidate(candidate),
            )

    def test_closed_shapes_and_deterministic_findings(self) -> None:
        candidate = _load_candidate()
        candidate["warning_state"] = "official"
        candidate["measurement"]["forecast"] = True  # type: ignore[index]
        expected = [
            Finding("UNDECLARED_MEASUREMENT_FIELD", "$.measurement.forecast"),
            Finding("UNDECLARED_TOP_LEVEL_FIELD", "$.warning_state"),
        ]
        self.assertEqual(validate_candidate(candidate), expected)
        reordered = dict(reversed(list(copy.deepcopy(candidate).items())))
        self.assertEqual(validate_candidate(reordered), expected)

    def test_parser_rejects_duplicate_nonfinite_and_nonobject_json(self) -> None:
        cases = (
            b'{"record_id":"a","record_id":"b"}',
            b'{"measurement":{"value":Infinity}}',
            b"[]",
        )
        expected = (
            [Finding("FIXTURE_JSON_INVALID", "$")],
            [Finding("FIXTURE_JSON_INVALID", "$")],
            [Finding("CANDIDATE_NOT_OBJECT", "$")],
        )
        with tempfile.TemporaryDirectory() as directory:
            for index, (content, wanted) in enumerate(zip(cases, expected, strict=True)):
                path = Path(directory) / f"case-{index}.json"
                path.write_bytes(content)
                self.assertEqual(validate_file(path), wanted)

    def test_file_size_is_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "large.json"
            path.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(validate_file(path), [Finding("FIXTURE_TOO_LARGE", "$")])

    def test_cli_exit_status_and_output_do_not_echo_candidate_values(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            self.assertEqual(main([str(VALID_FIXTURE)]), 0)
            self.assertEqual(main([str(INVALID_FIXTURE)]), 1)
            self.assertEqual(main([]), 2)
        output = stdout.getvalue()
        self.assertIn('"status":"PASS"', output)
        self.assertIn('"status":"FAIL"', output)
        self.assertNotIn("synthetic-forbidden-location", output)
        self.assertIn("at least one fixture file is required", stderr.getvalue())

    def test_network_guard_is_active(self) -> None:
        with self.assertRaises(RuntimeError):
            socket.create_connection(("example.invalid", 443))
        with self.assertRaises(RuntimeError):
            urllib.request.urlopen("https://example.invalid")


if __name__ == "__main__":
    unittest.main()
