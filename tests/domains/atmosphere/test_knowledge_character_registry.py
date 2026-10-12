#!/usr/bin/env python3
"""Deterministic tests for the synthetic Atmosphere anti-collapse profile."""

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

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    MAX_FIXTURE_BYTES,
)
from tools.validators.domains.atmosphere.validate_knowledge_character import (  # noqa: E402
    FIXTURE_CHARACTER_RULES,
    FORBIDDEN_LOCATION_ALIASES,
    MAX_EVIDENCE_REFS,
    MAX_LIMITATIONS,
    PROFILE_ID,
    Finding,
    main,
    validate_candidate,
    validate_file,
)


FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/atmosphere/knowledge_character"
VALID_FIXTURE_DIR = FIXTURE_ROOT / "valid"
INVALID_FIXTURE_DIR = FIXTURE_ROOT / "invalid"

VALID_FIXTURE_NAMES = (
    "advisory_context.json",
    "aqi_report.json",
    "model_field.json",
    "observed_sensor.json",
    "remote_sensing_aod.json",
    "site_context.json",
)
INVALID_FIXTURE_NAMES = (
    "advisory_as_life_safety.json",
    "aod_as_pm25.json",
    "aqi_as_concentration.json",
    "model_as_observation.json",
    "precise_site_exposure.json",
)


def _valid_fixture(name: str = "observed_sensor.json") -> Path:
    return VALID_FIXTURE_DIR / name


def _invalid_fixture(name: str) -> Path:
    return INVALID_FIXTURE_DIR / name


def _sidecar_for(fixture: Path) -> Path:
    return fixture.with_suffix(".expected_error.txt")


def _load_candidate(name: str = "observed_sensor.json") -> dict[str, object]:
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


class AtmosphereKnowledgeCharacterFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        denied = RuntimeError(
            "network access is forbidden in Atmosphere knowledge-character tests"
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

    def test_every_frozen_fixture_character_has_one_valid_case(self) -> None:
        observed: set[str] = set()
        for name in VALID_FIXTURE_NAMES:
            candidate = json.loads(_valid_fixture(name).read_text(encoding="utf-8"))
            self.assertEqual(candidate["profile_id"], PROFILE_ID)
            observed.add(candidate["knowledge_character"])
        self.assertEqual(observed, set(FIXTURE_CHARACTER_RULES))

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

    def test_character_pairing_mismatch_fails_closed(self) -> None:
        candidate = _load_candidate()
        claim = candidate["claim"]
        self.assertIsInstance(claim, dict)
        claim["unit"] = "ppm"
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("CLAIM_UNIT_INVALID", "$.claim.unit")],
        )

    def test_missing_unknown_and_multiple_character_states_fail_closed(self) -> None:
        cases = (
            (
                lambda candidate: candidate.pop("knowledge_character"),
                Finding("KNOWLEDGE_CHARACTER_MISSING", "$.knowledge_character"),
            ),
            (
                lambda candidate: candidate.update(
                    knowledge_character="UNREVIEWED_CHARACTER"
                ),
                Finding("KNOWLEDGE_CHARACTER_UNKNOWN", "$.knowledge_character"),
            ),
            (
                lambda candidate: candidate.update(
                    knowledge_character=[
                        "OBSERVED_SENSOR",
                        "ATMOSPHERIC_MODEL_FIELD",
                    ]
                ),
                Finding("KNOWLEDGE_CHARACTER_MULTIPLE", "$.knowledge_character"),
            ),
        )
        for mutate, expected in cases:
            candidate = _load_candidate()
            mutate(candidate)
            self.assertEqual(validate_candidate(candidate), [expected])

    def test_reference_count_boundary_is_bounded(self) -> None:
        candidate = _load_candidate()
        candidate["evidence_refs"] = [
            f"fixture://evidence/atmosphere/boundary/{index}"
            for index in range(MAX_EVIDENCE_REFS)
        ]
        self.assertEqual(validate_candidate(candidate), [])

        candidate["evidence_refs"].append(  # type: ignore[union-attr]
            "fixture://evidence/atmosphere/boundary/exceeded"
        )
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("EVIDENCE_REF_COUNT_EXCEEDED", "$.evidence_refs")],
        )

    def test_limitation_count_is_bounded_before_set_comparison(self) -> None:
        candidate = _load_candidate()
        candidate["limitations"] = [
            f"synthetic-limit-{index}" for index in range(MAX_LIMITATIONS + 1)
        ]
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("LIMITATION_COUNT_EXCEEDED", "$.limitations")],
        )

    def test_every_precise_location_alias_is_denied_without_values(self) -> None:
        for alias in sorted(FORBIDDEN_LOCATION_ALIASES):
            candidate = _load_candidate("site_context.json")
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
        claim = candidate["claim"]
        self.assertIsInstance(claim, dict)
        claim["unsupported"] = "synthetic"
        expected = [
            Finding("UNDECLARED_CLAIM_FIELD", "$.claim.unsupported"),
            Finding("UNDECLARED_TOP_LEVEL_FIELD", "$.alpha"),
            Finding("UNDECLARED_TOP_LEVEL_FIELD", "$.zeta"),
        ]
        self.assertEqual(validate_candidate(candidate), expected)
        reordered = dict(reversed(list(copy.deepcopy(candidate).items())))
        self.assertEqual(validate_candidate(reordered), expected)

    def test_parser_rejects_duplicate_nonfinite_and_nonobject_json(self) -> None:
        cases = (
            b'{"fixture_id":"first","fixture_id":"second"}',
            b'{"claim":{"value":NaN}}',
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
                main([str(_invalid_fixture("precise_site_exposure.json"))]), 1
            )
            self.assertEqual(main([]), 2)
        output = stdout.getvalue()
        self.assertIn('"status":"PASS"', output)
        self.assertIn('"status":"FAIL"', output)
        self.assertNotIn("SYNTHETIC_PRECISE_SITE_SENTINEL", output)
        self.assertIn("at least one fixture file is required", stderr.getvalue())

    def test_validation_never_attempts_network_access(self) -> None:
        for name in VALID_FIXTURE_NAMES:
            self.assertEqual(validate_file(_valid_fixture(name)), [])
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
