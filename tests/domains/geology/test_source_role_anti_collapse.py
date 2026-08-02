#!/usr/bin/env python3
"""Deterministic tests for the synthetic Geology resource-class profile."""

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
from tools.validators.domains.geology.validate_resource_class_distinction import (  # noqa: E402
    FIXTURE_RESOURCE_RULES,
    FORBIDDEN_LOCATION_ALIASES,
    MAX_ASSUMPTION_REFS,
    MAX_EVIDENCE_REFS,
    MAX_LIMITATIONS,
    PROFILE_ID,
    Finding,
    main,
    validate_candidate,
    validate_file,
)


FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/geology/resource_class"
VALID_FIXTURE_DIR = FIXTURE_ROOT / "valid"
INVALID_FIXTURE_DIR = FIXTURE_ROOT / "invalid"

VALID_FIXTURE_NAMES = (
    "mineral_occurrence.json",
    "resource_deposit.json",
    "resource_estimate.json",
)
INVALID_FIXTURE_NAMES = (
    "estimate_as_observation.json",
    "estimate_as_reserve.json",
    "estimate_missing_classification.json",
    "modeled_potential_as_deposit.json",
    "occurrence_as_deposit.json",
    "permit_as_deposit.json",
    "precise_resource_location.json",
    "production_as_deposit.json",
)


def _valid_fixture(name: str = "mineral_occurrence.json") -> Path:
    return VALID_FIXTURE_DIR / name


def _invalid_fixture(name: str) -> Path:
    return INVALID_FIXTURE_DIR / name


def _sidecar_for(fixture: Path) -> Path:
    return fixture.with_suffix(".expected_error.txt")


def _load_candidate(name: str = "mineral_occurrence.json") -> dict[str, object]:
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


class GeologyResourceClassFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        denied = RuntimeError(
            "network access is forbidden in Geology resource-class tests"
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

    def test_every_frozen_resource_character_has_one_valid_case(self) -> None:
        observed: set[str] = set()
        for name in VALID_FIXTURE_NAMES:
            candidate = json.loads(_valid_fixture(name).read_text(encoding="utf-8"))
            self.assertEqual(candidate["profile_id"], PROFILE_ID)
            observed.add(candidate["resource_character"])
        self.assertEqual(observed, set(FIXTURE_RESOURCE_RULES))

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

    def test_pairing_mismatch_fails_closed(self) -> None:
        candidate = _load_candidate()
        candidate["object_family"] = "ResourceDeposit"
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("OBJECT_FAMILY_INVALID", "$.object_family")],
        )

    def test_missing_unknown_and_multiple_character_states_fail_closed(self) -> None:
        cases = (
            (
                lambda candidate: candidate.pop("resource_character"),
                Finding("RESOURCE_CHARACTER_MISSING", "$.resource_character"),
            ),
            (
                lambda candidate: candidate.update(
                    resource_character="UNREVIEWED_CHARACTER"
                ),
                Finding("RESOURCE_CHARACTER_UNKNOWN", "$.resource_character"),
            ),
            (
                lambda candidate: candidate.update(
                    resource_character=[
                        "MINERAL_OCCURRENCE",
                        "RESOURCE_DEPOSIT",
                    ]
                ),
                Finding("RESOURCE_CHARACTER_MULTIPLE", "$.resource_character"),
            ),
        )
        for mutate, expected in cases:
            candidate = _load_candidate()
            mutate(candidate)
            self.assertEqual(validate_candidate(candidate), [expected])

    def test_reference_count_boundaries_are_bounded(self) -> None:
        candidate = _load_candidate()
        candidate["evidence_refs"] = [
            f"fixture://evidence/geology/boundary/{index}"
            for index in range(MAX_EVIDENCE_REFS)
        ]
        self.assertEqual(validate_candidate(candidate), [])
        candidate["evidence_refs"].append(  # type: ignore[union-attr]
            "fixture://evidence/geology/boundary/exceeded"
        )
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("EVIDENCE_REF_COUNT_EXCEEDED", "$.evidence_refs")],
        )

        estimate = _load_candidate("resource_estimate.json")
        claim = estimate["claim"]
        self.assertIsInstance(claim, dict)
        claim["assumption_refs"] = [
            f"fixture://assumptions/geology/boundary/{index}"
            for index in range(MAX_ASSUMPTION_REFS + 1)
        ]
        self.assertEqual(
            validate_candidate(estimate),
            [
                Finding(
                    "ESTIMATE_ASSUMPTION_REF_COUNT_EXCEEDED",
                    "$.claim.assumption_refs",
                )
            ],
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

    def test_estimate_date_rejects_impossible_calendar_values(self) -> None:
        candidate = _load_candidate("resource_estimate.json")
        claim = candidate["claim"]
        self.assertIsInstance(claim, dict)
        claim["estimate_date"] = "2026-02-30"
        self.assertEqual(
            validate_candidate(candidate),
            [Finding("ESTIMATE_DATE_INVALID", "$.claim.estimate_date")],
        )

    def test_non_estimate_records_cannot_carry_estimate_support(self) -> None:
        candidate = _load_candidate()
        claim = candidate["claim"]
        self.assertIsInstance(claim, dict)
        claim["classification_scheme_ref"] = (
            "fixture://classification/geology/not-applicable"
        )
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding(
                    "ESTIMATE_SUPPORT_NOT_ALLOWED",
                    "$.claim.classification_scheme_ref",
                )
            ],
        )

    def test_every_precise_location_alias_is_denied_without_values(self) -> None:
        for alias in sorted(FORBIDDEN_LOCATION_ALIASES):
            candidate = _load_candidate("resource_deposit.json")
            spatial_support = candidate["spatial_support"]
            self.assertIsInstance(spatial_support, dict)
            spatial_support[alias.upper()] = "SENSITIVE_SENTINEL"
            findings = validate_candidate(candidate)
            self.assertIn(
                Finding(
                    "SENSITIVE_RESOURCE_LOCATION_DENIED",
                    f"$.spatial_support.{alias.upper()}",
                ),
                findings,
            )
            serialized = "\n".join(f"{item.code}\t{item.path}" for item in findings)
            self.assertNotIn("SENSITIVE_SENTINEL", serialized)

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
                main([str(_invalid_fixture("precise_resource_location.json"))]),
                1,
            )
            self.assertEqual(main([]), 2)
        output = stdout.getvalue()
        self.assertIn('"status":"PASS"', output)
        self.assertIn('"status":"FAIL"', output)
        self.assertNotIn("SYNTHETIC_PRECISE_RESOURCE_SENTINEL", output)
        self.assertIn("at least one fixture file is required", stderr.getvalue())

    def test_validation_never_attempts_network_access(self) -> None:
        for name in VALID_FIXTURE_NAMES:
            self.assertEqual(validate_file(_valid_fixture(name)), [])
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
