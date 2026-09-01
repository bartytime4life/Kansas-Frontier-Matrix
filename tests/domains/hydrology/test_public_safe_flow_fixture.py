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
    ALLOWED_PROVISIONAL_STATUSES,
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

    def test_source_role_must_remain_observed(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(candidate["source_role"], "observed")
        self.assertEqual(validate_candidate(candidate), [])

        for role in ("modeled", "forecast", "regulatory", "aggregate", "synthetic", None):
            candidate = _load_candidate()
            candidate["source_role"] = role
            self.assertIn(
                Finding("SOURCE_ROLE_INVALID", "$.source_role"),
                validate_candidate(candidate),
            )

        candidate = _load_candidate()
        candidate.pop("source_role")
        self.assertIn(
            Finding("SOURCE_ROLE_INVALID", "$.source_role"),
            validate_candidate(candidate),
        )

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
            "aggregation_window": "instant",
            "observed_at": "2026-08-02T12:00:00Z",
            "retrieved_at": "2026-08-02T11:59:59Z",
        }
        self.assertIn(
            Finding("TEMPORAL_ORDER_INVALID", "$.temporal_scope"),
            validate_candidate(candidate),
        )
        candidate["temporal_scope"] = {
            "aggregation_window": "instant",
            "observed_at": "2026-08-02T12:00:00+00:00",
            "retrieved_at": "2026-08-02T12:05:00Z",
        }
        self.assertIn(
            Finding("OBSERVED_TIME_INVALID", "$.temporal_scope.observed_at"),
            validate_candidate(candidate),
        )

    def test_aggregation_window_must_be_instant(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(candidate["temporal_scope"]["aggregation_window"], "instant")  # type: ignore[index]
        self.assertEqual(validate_candidate(candidate), [])
        expected = Finding(
            "AGGREGATION_WINDOW_INVALID", "$.temporal_scope.aggregation_window"
        )
        for value in ("daily_mean", "period_statistic", "forecast", "", None, 60):
            mutated = copy.deepcopy(candidate)
            mutated["temporal_scope"]["aggregation_window"] = value  # type: ignore[index]
            self.assertIn(expected, validate_candidate(mutated))
        mutated = copy.deepcopy(candidate)
        mutated["temporal_scope"].pop("aggregation_window")  # type: ignore[index]
        self.assertIn(expected, validate_candidate(mutated))

    def test_canonical_whole_second_utc_is_required(self) -> None:
        observed_values = (
            "2026-08-02T12:00:00.000Z",
            "2026-08-02 12:00:00Z",
            "2026-W31-7T12:00:00Z",
            "20260802T120000Z",
            "2026-08-02T12:00Z",
            "2026-08-02T12:00:60Z",
        )
        for value in observed_values:
            candidate = copy.deepcopy(_load_candidate())
            candidate["temporal_scope"]["observed_at"] = value  # type: ignore[index]
            self.assertIn(
                Finding("OBSERVED_TIME_INVALID", "$.temporal_scope.observed_at"),
                validate_candidate(candidate),
            )

        retrieved_values = (
            "2026-08-02T12:05:00.000Z",
            "2026-08-02 12:05:00Z",
            "2026-W31-7T12:05:00Z",
            "20260802T120500Z",
            "2026-08-02T12:05Z",
            "2026-08-02T12:05:60Z",
        )
        for value in retrieved_values:
            candidate = copy.deepcopy(_load_candidate())
            candidate["temporal_scope"]["retrieved_at"] = value  # type: ignore[index]
            self.assertIn(
                Finding("RETRIEVAL_TIME_INVALID", "$.temporal_scope.retrieved_at"),
                validate_candidate(candidate),
            )
        self.assertEqual(validate_candidate(_load_candidate()), [])

    def test_provisional_status_is_preserved_and_bounded(self) -> None:
        candidate = _load_candidate()
        measurement = candidate["measurement"]
        self.assertEqual(measurement["qualifier"], "synthetic")  # type: ignore[index]
        self.assertEqual(measurement["provisional_status"], "provisional")  # type: ignore[index]
        self.assertEqual(validate_candidate(candidate), [])

        missing = Finding(
            "PROVISIONAL_STATUS_MISSING",
            "$.measurement.provisional_status",
        )
        for value in ("", "   ", None, 0, False):
            mutated = copy.deepcopy(candidate)
            mutated["measurement"]["provisional_status"] = value  # type: ignore[index]
            self.assertIn(missing, validate_candidate(mutated))
        mutated = copy.deepcopy(candidate)
        mutated["measurement"].pop("provisional_status")  # type: ignore[index]
        self.assertIn(missing, validate_candidate(mutated))

        for status in ALLOWED_PROVISIONAL_STATUSES:
            mutated = copy.deepcopy(candidate)
            mutated["measurement"]["provisional_status"] = status  # type: ignore[index]
            self.assertEqual(validate_candidate(mutated), [], status)

        invalid = Finding(
            "PROVISIONAL_STATUS_INVALID",
            "$.measurement.provisional_status",
        )
        for status in ("unknown", "approved/final", "PROVISIONAL", "ice-affected"):
            mutated = copy.deepcopy(candidate)
            mutated["measurement"]["provisional_status"] = status  # type: ignore[index]
            self.assertIn(invalid, validate_candidate(mutated), status)

    def test_source_status_is_not_inferred_from_qualifier(self) -> None:
        candidate = copy.deepcopy(_load_candidate())
        candidate["measurement"]["qualifier"] = "synthetic"  # type: ignore[index]
        candidate["measurement"].pop("provisional_status")  # type: ignore[index]
        findings = validate_candidate(candidate)
        self.assertIn(
            Finding("PROVISIONAL_STATUS_MISSING", "$.measurement.provisional_status"),
            findings,
        )
        self.assertNotIn(Finding("QUALIFIER_INVALID", "$.measurement.qualifier"), findings)

    def test_fixture_reference_profile_is_synthetic_and_generalized(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(validate_candidate(candidate), [])
        cases = (
            (
                "source_descriptor_ref",
                "https://example.invalid/live-source",
                Finding("SOURCE_DESCRIPTOR_REF_NOT_FIXTURE", "$.source_descriptor_ref"),
            ),
            (
                "gauge_site_ref",
                "fixture://hydrology/gauge/exact/06800000",
                Finding(
                    "GAUGE_SITE_REF_NOT_GENERALIZED_FIXTURE",
                    "$.gauge_site_ref",
                ),
            ),
        )
        for field, value, expected in cases:
            mutated = copy.deepcopy(candidate)
            mutated[field] = value
            self.assertIn(expected, validate_candidate(mutated))

        mutated = copy.deepcopy(candidate)
        mutated["evidence_refs"] = ["https://example.invalid/live-evidence"]
        self.assertIn(
            Finding("EVIDENCE_REF_NOT_FIXTURE", "$.evidence_refs"),
            validate_candidate(mutated),
        )

    def test_missing_references_keep_missing_findings(self) -> None:
        candidate = _load_candidate()
        candidate["source_descriptor_ref"] = ""
        candidate["gauge_site_ref"] = ""
        candidate["evidence_refs"] = []
        findings = validate_candidate(candidate)
        self.assertIn(
            Finding("SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref"),
            findings,
        )
        self.assertIn(Finding("GAUGE_SITE_REF_MISSING", "$.gauge_site_ref"), findings)
        self.assertIn(Finding("EVIDENCE_REF_MISSING", "$.evidence_refs"), findings)
        self.assertNotIn(
            Finding("SOURCE_DESCRIPTOR_REF_NOT_FIXTURE", "$.source_descriptor_ref"),
            findings,
        )
        self.assertNotIn(
            Finding(
                "GAUGE_SITE_REF_NOT_GENERALIZED_FIXTURE",
                "$.gauge_site_ref",
            ),
            findings,
        )
        self.assertNotIn(Finding("EVIDENCE_REF_NOT_FIXTURE", "$.evidence_refs"), findings)

    def test_unit_transform_provenance_is_explicitly_no_transform(self) -> None:
        candidate = _load_candidate()
        measurement = candidate["measurement"]  # type: ignore[index]
        self.assertEqual(measurement["unit"], "ft3/s")  # type: ignore[index]
        self.assertIsNone(measurement["unit_transform_ref"])  # type: ignore[index]
        self.assertEqual(validate_candidate(candidate), [])

        missing = copy.deepcopy(candidate)
        missing["measurement"].pop("unit_transform_ref")  # type: ignore[index]
        self.assertIn(
            Finding("UNIT_TRANSFORM_REF_MISSING", "$.measurement.unit_transform_ref"),
            validate_candidate(missing),
        )

        expected = Finding(
            "UNIT_TRANSFORM_REF_UNSUPPORTED", "$.measurement.unit_transform_ref"
        )
        for value in (
            "fixture://transforms/hydrology/unverified-normalization",
            "",
            False,
            0,
            {},
            [],
        ):
            mutated = copy.deepcopy(candidate)
            mutated["measurement"]["unit_transform_ref"] = value  # type: ignore[index]
            self.assertIn(expected, validate_candidate(mutated))

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
