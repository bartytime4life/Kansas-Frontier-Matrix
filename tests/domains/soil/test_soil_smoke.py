#!/usr/bin/env python3
"""Frozen, standard-library smoke checks for Soil public-safe fixtures."""

from __future__ import annotations

import contextlib
import copy
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


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.domains.soil.validate_public_safe_fixture import (  # noqa: E402
    ALLOWED_SUPPORT_TYPES,
    FORBIDDEN_LOCATION_ALIASES,
    MAX_DOCUMENT_DEPTH,
    MAX_DOCUMENT_NODES,
    MAX_FIXTURE_BYTES,
    MAX_JSON_INTEGER_DIGITS,
    Finding,
    main,
    validate_candidate,
    validate_file,
)


VALIDATOR = (
    REPO_ROOT
    / "tools"
    / "validators"
    / "domains"
    / "soil"
    / "validate_public_safe_fixture.py"
)
VALID_FIXTURE_DIR = REPO_ROOT / "fixtures" / "domains" / "soil" / "valid"
INVALID_FIXTURE_DIR = REPO_ROOT / "fixtures" / "domains" / "soil" / "invalid"

VALID_FIXTURE_NAMES = (
    "public_safe_observation.json",
)
INVALID_FIXTURE_NAMES = (
    "boolean_numeric_misuse.json",
    "candidate_not_object.json",
    "invalid_container_shapes.json",
    "invalid_depth_and_measurement.json",
    "invalid_governance.json",
    "invalid_support_and_spatial.json",
    "missing_references.json",
    "undeclared_fields.json",
)


def _valid_fixture(name: str = VALID_FIXTURE_NAMES[0]) -> Path:
    return VALID_FIXTURE_DIR / name


def _invalid_fixture(name: str) -> Path:
    return INVALID_FIXTURE_DIR / name


def _sidecar_for(fixture: Path) -> Path:
    return fixture.with_suffix(".expected_error.txt")


def _load_candidate() -> dict[str, object]:
    return json.loads(_valid_fixture().read_text(encoding="utf-8"))


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


class SoilPublicSafeFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        network_block = RuntimeError("network access is forbidden in Soil smoke tests")
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
        discovered = set(VALID_FIXTURE_DIR.glob("*.json"))
        self.assertEqual(discovered, accepted)

        for fixture in sorted(accepted):
            with self.subTest(fixture=fixture.name):
                self.assertEqual(validate_file(fixture), [])
                decoded = json.loads(fixture.read_text(encoding="utf-8"))
                self.assertEqual(validate_candidate(decoded), [])

    def test_invalid_fixture_inventory_and_sidecars_are_explicit(self) -> None:
        accepted = {_invalid_fixture(name) for name in INVALID_FIXTURE_NAMES}
        discovered = set(INVALID_FIXTURE_DIR.glob("*.json"))
        self.assertEqual(discovered, accepted)

        accepted_sidecars = {_sidecar_for(fixture) for fixture in accepted}
        discovered_sidecars = set(INVALID_FIXTURE_DIR.glob("*.expected_error.txt"))
        self.assertEqual(discovered_sidecars, accepted_sidecars)

    def test_invalid_fixture_findings_match_exact_sidecars(self) -> None:
        for name in INVALID_FIXTURE_NAMES:
            fixture = _invalid_fixture(name)
            expected = _load_expected_findings(_sidecar_for(fixture))
            with self.subTest(fixture=name):
                self.assertTrue(expected)
                self.assertEqual(expected, tuple(sorted(expected)))
                self.assertEqual(tuple(validate_file(fixture)), expected)

    def test_frozen_support_type_profile_is_enforced(self) -> None:
        for support_type in sorted(ALLOWED_SUPPORT_TYPES):
            candidate = _load_candidate()
            candidate["support_type"] = support_type
            with self.subTest(support_type=support_type):
                self.assertEqual(validate_candidate(candidate), [])

        invalid_support_types = (None, "", "soil", ["static_survey"], {})
        for support_type in invalid_support_types:
            candidate = _load_candidate()
            candidate["support_type"] = support_type
            with self.subTest(invalid_support_type=repr(support_type)):
                self.assertIn(
                    Finding("SUPPORT_TYPE_INVALID", "$.support_type"),
                    validate_candidate(candidate),
                )

    def test_every_precise_location_alias_is_rejected_case_insensitively(self) -> None:
        for alias in sorted(FORBIDDEN_LOCATION_ALIASES):
            candidate = _load_candidate()
            spatial_support = candidate["spatial_support"]
            self.assertIsInstance(spatial_support, dict)
            asserted_spatial_support = spatial_support
            asserted_spatial_support[alias.upper()] = "synthetic-location-value"
            findings = validate_candidate(candidate)
            path = f"$.spatial_support.{alias.upper()}"
            with self.subTest(alias=alias):
                self.assertIn(
                    Finding("PRECISE_LOCATION_FIELD_FORBIDDEN", path), findings
                )
                self.assertIn(
                    Finding("UNDECLARED_SPATIAL_SUPPORT_FIELD", path), findings
                )

    def test_booleans_and_non_finite_values_are_not_numeric_measurements(self) -> None:
        rejected_values = (True, False, float("nan"), float("inf"), float("-inf"))
        for rejected in rejected_values:
            candidate = _load_candidate()
            depth_interval = candidate["depth_interval_cm"]
            measurement = candidate["measurement"]
            self.assertIsInstance(depth_interval, dict)
            self.assertIsInstance(measurement, dict)
            depth_interval["top"] = rejected
            measurement["value"] = rejected
            findings = validate_candidate(candidate)
            with self.subTest(value=repr(rejected)):
                self.assertIn(
                    Finding("DEPTH_INTERVAL_NON_NUMERIC", "$.depth_interval_cm"),
                    findings,
                )
                self.assertIn(
                    Finding(
                        "MEASUREMENT_VALUE_OUT_OF_RANGE", "$.measurement.value"
                    ),
                    findings,
                )

    def test_governance_false_is_not_interchangeable_with_numeric_zero(self) -> None:
        candidate = _load_candidate()
        governance = candidate["governance"]
        self.assertIsInstance(governance, dict)
        governance["promotion_eligible"] = 0
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding(
                    "GOVERNANCE_STATE_INVALID",
                    "$.governance.promotion_eligible",
                )
            ],
        )

    def test_all_nested_objects_are_closed(self) -> None:
        candidate = _load_candidate()
        additions = (
            (candidate, "generated_claim", "UNDECLARED_TOP_LEVEL_FIELD", "$"),
            (
                candidate["spatial_support"],
                "soil_series",
                "UNDECLARED_SPATIAL_SUPPORT_FIELD",
                "$.spatial_support",
            ),
            (
                candidate["depth_interval_cm"],
                "datum",
                "UNDECLARED_DEPTH_INTERVAL_FIELD",
                "$.depth_interval_cm",
            ),
            (
                candidate["measurement"],
                "method",
                "UNDECLARED_MEASUREMENT_FIELD",
                "$.measurement",
            ),
            (
                candidate["governance"],
                "approval_state",
                "UNDECLARED_GOVERNANCE_FIELD",
                "$.governance",
            ),
        )
        expected: list[Finding] = []
        for target, field, code, parent_path in additions:
            self.assertIsInstance(target, dict)
            target[field] = "synthetic-undeclared-value"
            expected.append(Finding(code, f"{parent_path}.{field}"))
        self.assertEqual(validate_candidate(candidate), sorted(expected))

    def test_findings_are_unique_sorted_and_insertion_order_independent(self) -> None:
        candidate = _load_candidate()
        candidate["zeta"] = "synthetic-zeta"
        candidate["alpha"] = "synthetic-alpha"
        spatial_support = candidate["spatial_support"]
        self.assertIsInstance(spatial_support, dict)
        spatial_support["longitude"] = "synthetic-longitude"
        first = validate_candidate(candidate)

        reordered = copy.deepcopy(candidate)
        reordered = dict(reversed(list(reordered.items())))
        spatial = reordered["spatial_support"]
        self.assertIsInstance(spatial, dict)
        reordered["spatial_support"] = dict(reversed(list(spatial.items())))
        second = validate_candidate(reordered)

        self.assertEqual(first, sorted(set(first)))
        self.assertEqual(second, first)

    def test_loader_rejects_malformed_duplicate_and_unbounded_json(self) -> None:
        invalid_documents = {
            "malformed.json": "{not-json",
            "duplicate.json": '{"record_id":"first","record_id":"second"}',
            "nan.json": '{"measurement":{"value":NaN}}',
            "infinite.json": '{"measurement":{"value":1e999}}',
            "oversized_integer.json": (
                '{"measurement":{"value":'
                + ("9" * (MAX_JSON_INTEGER_DIGITS + 1))
                + "}}"
            ),
            "document_too_deep.json": (
                ("[" * (MAX_DOCUMENT_DEPTH + 1))
                + "0"
                + ("]" * (MAX_DOCUMENT_DEPTH + 1))
            ),
            "document_has_too_many_nodes.json": (
                "[" + ",".join("0" for _ in range(MAX_DOCUMENT_NODES)) + "]"
            ),
            "deeply_nested.json": ("[" * 1_100) + "0" + ("]" * 1_100),
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            for filename, raw_document in invalid_documents.items():
                fixture = temp_path / filename
                fixture.write_text(raw_document, encoding="utf-8")
                with self.subTest(filename=filename):
                    self.assertEqual(
                        validate_file(fixture),
                        [Finding("FIXTURE_JSON_INVALID", "$")],
                    )

            invalid_utf8 = temp_path / "invalid_utf8.json"
            invalid_utf8.write_bytes(b"\xff\xfe")
            self.assertEqual(
                validate_file(invalid_utf8),
                [Finding("FIXTURE_JSON_INVALID", "$")],
            )

    def test_loader_rejects_files_over_the_size_bound_before_decoding(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = Path(temp_dir) / "oversized.json"
            fixture.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(
                validate_file(fixture),
                [Finding("FIXTURE_TOO_LARGE", "$")],
            )

    @unittest.skipUnless(hasattr(os, "mkfifo"), "named pipes require POSIX")
    def test_loader_rejects_non_regular_input_without_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = Path(temp_dir) / "fixture-pipe.json"
            os.mkfifo(fixture)
            self.assertEqual(
                validate_file(fixture),
                [Finding("FIXTURE_JSON_INVALID", "$")],
            )

    def test_validation_never_attempts_network_access(self) -> None:
        self.assertEqual(validate_file(_valid_fixture()), [])
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()

    def test_main_contract_is_sorted_and_never_echoes_candidate_values(self) -> None:
        sentinel = "CANDIDATE_VALUE_MUST_NOT_BE_ECHOED"
        candidate = _load_candidate()
        measurement = candidate["measurement"]
        self.assertIsInstance(measurement, dict)
        measurement["value"] = sentinel

        with tempfile.TemporaryDirectory() as temp_dir:
            invalid_fixture = Path(temp_dir) / "candidate.json"
            invalid_fixture.write_text(json.dumps(candidate), encoding="utf-8")
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                exit_code = main([str(invalid_fixture), str(_valid_fixture())])

        self.assertEqual(exit_code, 1)
        self.assertNotIn(sentinel, stdout.getvalue())
        self.assertNotIn(sentinel, stderr.getvalue())
        envelopes = [json.loads(line) for line in stdout.getvalue().splitlines()]
        self.assertEqual(
            [envelope["file"] for envelope in envelopes],
            sorted(envelope["file"] for envelope in envelopes),
        )
        self.assertEqual({envelope["status"] for envelope in envelopes}, {"PASS", "FAIL"})
        for envelope in envelopes:
            self.assertEqual(envelope["scope"], "soil-public-safe-fixture")
            self.assertEqual(
                envelope["findings"],
                sorted(envelope["findings"], key=lambda item: (item["code"], item["path"])),
            )

    def test_main_without_files_returns_usage_exit_code_two(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            exit_code = main([])
        self.assertEqual(exit_code, 2)
        self.assertEqual(stdout.getvalue(), "")
        self.assertTrue(stderr.getvalue())

    def test_executable_cli_exit_codes_are_zero_one_and_two(self) -> None:
        commands = (
            (0, [str(_valid_fixture())]),
            (1, [str(_invalid_fixture("missing_references.json"))]),
            (2, []),
        )
        for expected_exit, arguments in commands:
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR), *arguments],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            with self.subTest(expected_exit=expected_exit):
                self.assertEqual(completed.returncode, expected_exit)
                if arguments:
                    for line in completed.stdout.splitlines():
                        json.loads(line)


if __name__ == "__main__":
    unittest.main(verbosity=2)
