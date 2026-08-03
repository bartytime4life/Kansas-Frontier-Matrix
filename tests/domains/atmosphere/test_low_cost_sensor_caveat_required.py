#!/usr/bin/env python3
"""Deterministic tests for the synthetic low-cost-sensor calibration profile."""

from __future__ import annotations

import contextlib
import copy
import hashlib
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

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    MAX_FIXTURE_BYTES,
)
from tools.validators.domains.atmosphere.validate_low_cost_sensor_caveats import (  # noqa: E402
    FORBIDDEN_LOCATION_ALIASES,
    EXPECTED_IDENTITY_FIELDS,
    MAX_EVIDENCE_REFS,
    PROFILE_ID,
    Finding,
    main,
    validate_candidate,
    validate_file,
)


FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/atmosphere/low_cost_sensor_calibration"
VALID_FIXTURE_DIR = FIXTURE_ROOT / "valid"
INVALID_FIXTURE_DIR = FIXTURE_ROOT / "invalid"

VALID_FIXTURE_NAMES = (
    "caveated_context.json",
    "corrected_with_lineage.json",
)
INVALID_FIXTURE_NAMES = (
    "metric_driven_promotion.json",
    "missing_caveat.json",
    "missing_bound_model_evidence.json",
    "missing_confidence_limitations_rollback.json",
    "missing_correction_identity.json",
    "missing_evaluation_bounds.json",
    "missing_meteorology_inputs.json",
    "missing_reference_collocation.json",
    "modeled_output_as_raw.json",
    "peer_consensus_reference.json",
    "precise_site_exposure.json",
    "raw_corrected_pair_collapsed.json",
    "real_county_exposure.json",
    "reference_grade_overclaim.json",
    "unbounded_transfer_claim.json",
    "unknown_transferability_drift.json",
)


def _valid_fixture(name: str = "caveated_context.json") -> Path:
    return VALID_FIXTURE_DIR / name


def _invalid_fixture(name: str) -> Path:
    return INVALID_FIXTURE_DIR / name


def _sidecar_for(fixture: Path) -> Path:
    return fixture.with_suffix(".expected_error.txt")


def _load_candidate(name: str = "caveated_context.json") -> dict[str, object]:
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


class AtmosphereLowCostSensorCalibrationTests(unittest.TestCase):
    def setUp(self) -> None:
        denied = RuntimeError(
            "network access is forbidden in low-cost-sensor calibration tests"
        )
        self.network_mocks: list[mock.Mock] = []
        for patcher in (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
            mock.patch.object(socket.socket, "connect_ex", side_effect=denied),
            mock.patch.object(socket, "create_connection", side_effect=denied),
            mock.patch.object(socket, "getaddrinfo", side_effect=denied),
            mock.patch.object(urllib.request, "urlopen", side_effect=denied),
        ):
            self.network_mocks.append(patcher.start())
            self.addCleanup(patcher.stop)

    def test_valid_fixture_inventory_is_explicit_and_positive(self) -> None:
        expected = {_valid_fixture(name) for name in VALID_FIXTURE_NAMES}
        self.assertEqual(set(VALID_FIXTURE_DIR.glob("*.json")), expected)
        for fixture in sorted(expected):
            with self.subTest(fixture=fixture.name):
                self.assertEqual(validate_file(fixture), [])

    def test_both_frozen_calibration_states_have_positive_controls(self) -> None:
        observed = {
            _load_candidate(name)["calibration"]["status"]  # type: ignore[index]
            for name in VALID_FIXTURE_NAMES
        }
        self.assertEqual(
            observed,
            {"UNCORRECTED_CONTEXT_ONLY", "CORRECTED_WITH_LINEAGE"},
        )
        for name in VALID_FIXTURE_NAMES:
            self.assertEqual(_load_candidate(name)["profile_id"], PROFILE_ID)

    def test_identity_digests_pin_exact_fixture_references(self) -> None:
        candidate = _load_candidate("corrected_with_lineage.json")
        calibration = candidate["calibration"]
        self.assertIsInstance(calibration, dict)
        for reference_field, (
            expected_reference,
            digest_field,
            expected_digest,
        ) in EXPECTED_IDENTITY_FIELDS.items():
            with self.subTest(reference_field=reference_field):
                self.assertEqual(calibration[reference_field], expected_reference)
                self.assertEqual(calibration[digest_field], expected_digest)
                self.assertEqual(
                    expected_digest,
                    "sha256:"
                    + hashlib.sha256(expected_reference.encode("utf-8")).hexdigest(),
                )

    def test_invalid_fixture_inventory_and_sidecars_are_explicit(self) -> None:
        expected = {_invalid_fixture(name) for name in INVALID_FIXTURE_NAMES}
        self.assertEqual(set(INVALID_FIXTURE_DIR.glob("*.json")), expected)
        self.assertEqual(
            set(INVALID_FIXTURE_DIR.glob("*.expected_error.txt")),
            {_sidecar_for(fixture) for fixture in expected},
        )

    def test_invalid_findings_match_exact_sorted_sidecars(self) -> None:
        for name in INVALID_FIXTURE_NAMES:
            fixture = _invalid_fixture(name)
            expected = _load_expected_findings(_sidecar_for(fixture))
            with self.subTest(fixture=name):
                self.assertTrue(expected)
                self.assertEqual(expected, tuple(sorted(expected)))
                self.assertEqual(tuple(validate_file(fixture)), expected)

    def test_missing_confidence_and_limitations_fail_closed(self) -> None:
        candidate = _load_candidate()
        assessment = candidate["assessment"]
        self.assertIsInstance(assessment, dict)
        assessment.pop("confidence_state")
        candidate.pop("limitations")
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding("CONFIDENCE_STATE_INVALID", "$.assessment.confidence_state"),
                Finding("LIMITATIONS_INVALID", "$.limitations"),
            ],
        )

    def test_character_role_source_and_profile_fail_closed(self) -> None:
        candidate = _load_candidate()
        candidate["profile_id"] = "unreviewed-profile"
        candidate["knowledge_character"] = "OBSERVED_SENSOR"
        candidate["source_role"] = "regulatory"
        candidate["source_descriptor_ref"] = ""
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding("KNOWLEDGE_CHARACTER_INVALID", "$.knowledge_character"),
                Finding("PROFILE_ID_INVALID", "$.profile_id"),
                Finding("SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref"),
                Finding("SOURCE_ROLE_INVALID", "$.source_role"),
            ],
        )

    def test_external_refs_and_real_county_fail_closed(self) -> None:
        candidate = _load_candidate()
        candidate["source_descriptor_ref"] = "https://example.invalid/private-site"
        candidate["evidence_refs"] = ["https://example.invalid/evidence"]
        spatial_support = candidate["spatial_support"]
        self.assertIsInstance(spatial_support, dict)
        spatial_support["county_fips"] = "20053"
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding("COUNTY_FIPS_INVALID", "$.spatial_support.county_fips"),
                Finding("EVIDENCE_REF_NOT_FIXTURE_LOCAL", "$.evidence_refs[0]"),
                Finding("EVIDENCE_REF_SET_INVALID", "$.evidence_refs"),
                Finding("RAW_EVIDENCE_REF_UNBOUND", "$.calibration.raw_evidence_ref"),
                Finding("SOURCE_DESCRIPTOR_REF_INVALID", "$.source_descriptor_ref"),
            ],
        )

    def test_reference_inventory_and_count_are_bounded(self) -> None:
        candidate = _load_candidate()
        candidate["evidence_refs"].append(  # type: ignore[union-attr]
            "fixture://evidence/atmosphere/unexpected"
        )
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("EVIDENCE_REF_SET_INVALID", "$.evidence_refs")],
        )
        candidate = _load_candidate()
        candidate["evidence_refs"].extend(  # type: ignore[union-attr]
            f"fixture://evidence/atmosphere/boundary/{index}"
            for index in range(MAX_EVIDENCE_REFS)
        )
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding("EVIDENCE_REF_COUNT_EXCEEDED", "$.evidence_refs"),
                Finding("EVIDENCE_REF_SET_INVALID", "$.evidence_refs"),
            ],
        )

    def test_reference_collocation_time_order_fails_closed(self) -> None:
        candidate = _load_candidate("corrected_with_lineage.json")
        calibration = candidate["calibration"]
        self.assertIsInstance(calibration, dict)
        collocation = calibration["reference_collocation"]
        self.assertIsInstance(collocation, dict)
        collocation["period_start"] = collocation["period_end"]
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding(
                    "REFERENCE_COLLOCATION_TIME_ORDER_INVALID",
                    "$.calibration.reference_collocation",
                )
            ],
        )

    def test_every_precise_location_alias_is_denied_without_values(self) -> None:
        for alias in sorted(FORBIDDEN_LOCATION_ALIASES):
            candidate = _load_candidate()
            spatial_support = candidate["spatial_support"]
            self.assertIsInstance(spatial_support, dict)
            spatial_support[alias.upper()] = "SENSITIVE_SENTINEL"
            findings = validate_candidate(candidate)
            self.assertIn(
                Finding(
                    "PRECISE_SITE_EXPOSURE_DENIED",
                    f"$.spatial_support.{alias.upper()}",
                ),
                findings,
            )

    def test_closed_shapes_and_deterministic_finding_order(self) -> None:
        candidate = _load_candidate()
        candidate["zeta"] = "synthetic-zeta"
        candidate["alpha"] = "synthetic-alpha"
        calibration = candidate["calibration"]
        self.assertIsInstance(calibration, dict)
        calibration["unsupported"] = "synthetic"
        expected = [
            Finding("UNDECLARED_CALIBRATION_FIELD", "$.calibration.unsupported"),
            Finding("UNDECLARED_TOP_LEVEL_FIELD", "$.alpha"),
            Finding("UNDECLARED_TOP_LEVEL_FIELD", "$.zeta"),
        ]
        self.assertEqual(validate_candidate(candidate), expected)
        reordered = dict(reversed(list(copy.deepcopy(candidate).items())))
        self.assertEqual(validate_candidate(reordered), expected)

    def test_parser_rejects_duplicate_nonfinite_and_nonobject_json(self) -> None:
        cases = (
            b'{"fixture_id":"first","fixture_id":"second"}',
            b'{"calibration":{"value":NaN}}',
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

    def test_cli_exit_codes_and_output_do_not_echo_candidate_values(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            self.assertEqual(main([str(_valid_fixture())]), 0)
            self.assertEqual(
                main([str(_invalid_fixture("reference_grade_overclaim.json"))]), 1
            )
            self.assertEqual(main([]), 2)
        output = stdout.getvalue()
        self.assertIn('"status":"PASS"', output)
        self.assertIn('"status":"FAIL"', output)
        self.assertNotIn("fixture://source/atmosphere/low-cost-sensor", output)
        self.assertIn("at least one fixture file is required", stderr.getvalue())

    def test_validation_never_attempts_network_access(self) -> None:
        for name in VALID_FIXTURE_NAMES:
            self.assertEqual(validate_file(_valid_fixture(name)), [])
        for name in INVALID_FIXTURE_NAMES:
            self.assertTrue(validate_file(_invalid_fixture(name)))
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
