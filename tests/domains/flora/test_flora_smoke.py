#!/usr/bin/env python3
"""Deterministic, no-network checks for the Flora public-safe fixture slice."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import os
import re
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

from tools.validators.domains.flora.validate_public_safe_fixture import (  # noqa: E402
    FORBIDDEN_LOCATION_ALIASES,
    FORBIDDEN_TRANSFORM_ALIASES,
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
    / "flora"
    / "validate_public_safe_fixture.py"
)
VALID_FIXTURE_DIR = REPO_ROOT / "fixtures" / "domains" / "flora" / "valid"
INVALID_FIXTURE_DIR = REPO_ROOT / "fixtures" / "domains" / "flora" / "invalid"

VALID_FIXTURE_NAMES = ("public_safe_occurrence.json",)
INVALID_FIXTURE_NAMES = (
    "candidate_not_object.json",
    "missing_public_controls.json",
    "missing_references.json",
    "role_and_taxonomy_collapse.json",
    "undeclared_external_transform.json",
    "unsafe_location_and_sensitivity.json",
)

_COORDINATE_PAIR_RE = re.compile(
    r"(?<![0-9])[-+]?[0-9]{1,3}(?:\.[0-9]+)?\s*,\s*"
    r"[-+]?[0-9]{1,3}(?:\.[0-9]+)?(?![0-9])"
)


def _valid_fixture() -> Path:
    return VALID_FIXTURE_DIR / VALID_FIXTURE_NAMES[0]


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


class FloraPublicSafeFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        network_block = RuntimeError(
            "network access is forbidden in Flora public-safe fixture tests"
        )
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
        accepted = {_valid_fixture()}
        discovered = set(VALID_FIXTURE_DIR.glob("*.json"))
        self.assertEqual(discovered, accepted)

        for fixture in sorted(accepted):
            with self.subTest(fixture=fixture.name):
                self.assertEqual(validate_file(fixture), [])
                decoded = json.loads(fixture.read_text(encoding="utf-8"))
                self.assertEqual(validate_candidate(decoded), [])

    def test_valid_fixture_contains_no_location_or_external_reference(self) -> None:
        raw_text = _valid_fixture().read_text(encoding="utf-8")
        self.assertNotRegex(raw_text, r"(?i)https?://|ftp://|www\.")
        self.assertIsNone(_COORDINATE_PAIR_RE.search(raw_text))
        decoded = json.loads(raw_text)
        self.assertNotIn("geometry", decoded)
        self.assertNotIn("coordinates", decoded)
        self.assertEqual(decoded["governance"]["release_state"], "not_released")
        self.assertIs(decoded["governance"]["promotion_eligible"], False)

    def test_invalid_inventory_and_sidecars_are_explicit(self) -> None:
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

    def test_source_role_taxonomy_rights_and_governance_are_frozen(self) -> None:
        mutations = (
            ("source_role", "modeled_distribution", "SOURCE_ROLE_INVALID"),
            ("taxon_concept_state", "unresolved", "TAXON_CONCEPT_STATE_INVALID"),
            ("rights_state", "unknown", "RIGHTS_STATE_INVALID"),
        )
        for field, value, code in mutations:
            candidate = _load_candidate()
            candidate[field] = value
            with self.subTest(field=field):
                self.assertIn(Finding(code, f"$.{field}"), validate_candidate(candidate))

        candidate = _load_candidate()
        governance = candidate["governance"]
        self.assertIsInstance(governance, dict)
        governance["promotion_eligible"] = True
        governance["release_state"] = "released"
        findings = validate_candidate(candidate)
        self.assertIn(
            Finding("GOVERNANCE_STATE_INVALID", "$.governance.promotion_eligible"),
            findings,
        )
        self.assertIn(
            Finding("GOVERNANCE_STATE_INVALID", "$.governance.release_state"),
            findings,
        )

    def test_boolean_fields_do_not_accept_numeric_zero(self) -> None:
        candidate = _load_candidate()
        sensitivity = candidate["sensitivity"]
        governance = candidate["governance"]
        self.assertIsInstance(sensitivity, dict)
        self.assertIsInstance(governance, dict)
        sensitivity["exact_location_present"] = 0
        governance["promotion_eligible"] = 0
        findings = validate_candidate(candidate)
        self.assertIn(
            Finding(
                "SENSITIVITY_STATE_INVALID",
                "$.sensitivity.exact_location_present",
            ),
            findings,
        )
        self.assertIn(
            Finding(
                "GOVERNANCE_STATE_INVALID",
                "$.governance.promotion_eligible",
            ),
            findings,
        )
        self.assertIn(
            Finding("NUMERIC_VALUE_FORBIDDEN", "$.sensitivity.exact_location_present"),
            findings,
        )
        self.assertIn(
            Finding("NUMERIC_VALUE_FORBIDDEN", "$.governance.promotion_eligible"),
            findings,
        )

    def test_every_location_alias_is_rejected_case_insensitively(self) -> None:
        for alias in sorted(FORBIDDEN_LOCATION_ALIASES):
            candidate = _load_candidate()
            spatial_support = candidate["spatial_support"]
            self.assertIsInstance(spatial_support, dict)
            key = alias.upper()
            spatial_support[key] = "synthetic-sensitive-value"
            with self.subTest(alias=alias):
                self.assertIn(
                    Finding(
                        "SENSITIVE_LOCATION_FIELD_FORBIDDEN",
                        f"$.spatial_support.{key}",
                    ),
                    validate_candidate(candidate),
                )

    def test_every_transform_secret_alias_is_rejected(self) -> None:
        for alias in sorted(FORBIDDEN_TRANSFORM_ALIASES):
            candidate = _load_candidate()
            sensitivity = candidate["sensitivity"]
            self.assertIsInstance(sensitivity, dict)
            sensitivity[alias] = "synthetic-secret"
            with self.subTest(alias=alias):
                self.assertIn(
                    Finding(
                        "TRANSFORM_SECRET_FIELD_FORBIDDEN",
                        f"$.sensitivity.{alias}",
                    ),
                    validate_candidate(candidate),
                )

    def test_all_nested_objects_are_closed(self) -> None:
        candidate = _load_candidate()
        additions = (
            (candidate, "generated_claim", "UNDECLARED_TOP_LEVEL_FIELD", "$"),
            (
                candidate["spatial_support"],
                "county_name",
                "UNDECLARED_SPATIAL_SUPPORT_FIELD",
                "$.spatial_support",
            ),
            (
                candidate["sensitivity"],
                "audience_tier",
                "UNDECLARED_SENSITIVITY_FIELD",
                "$.sensitivity",
            ),
            (
                candidate["public_representation"],
                "map_layer",
                "UNDECLARED_PUBLIC_REPRESENTATION_FIELD",
                "$.public_representation",
            ),
            (
                candidate["governance"],
                "approval_actor",
                "UNDECLARED_GOVERNANCE_FIELD",
                "$.governance",
            ),
        )
        expected: list[Finding] = []
        for target, field, code, parent_path in additions:
            self.assertIsInstance(target, dict)
            target[field] = "synthetic-undeclared-value"
            expected.append(Finding(code, f"{parent_path}.{field}"))
        findings = validate_candidate(candidate)
        for finding in expected:
            self.assertIn(finding, findings)

    def test_container_shape_errors_fail_closed(self) -> None:
        mutations = (
            ("spatial_support", [], "SPATIAL_SUPPORT_INVALID"),
            ("sensitivity", [], "SENSITIVITY_STATE_INVALID"),
            ("public_representation", [], "PUBLIC_REPRESENTATION_INVALID"),
            ("governance", [], "GOVERNANCE_STATE_INVALID"),
            ("public_caveats", {}, "PUBLIC_CAVEATS_INVALID"),
        )
        for field, replacement, code in mutations:
            candidate = _load_candidate()
            candidate[field] = replacement
            with self.subTest(field=field):
                self.assertIn(Finding(code, f"$.{field}"), validate_candidate(candidate))

    def test_findings_are_unique_sorted_and_order_independent(self) -> None:
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
            "nan.json": '{"value":NaN}',
            "infinite.json": '{"value":1e999}',
            "oversized_integer.json": '{"value":' + ("9" * (MAX_JSON_INTEGER_DIGITS + 1)) + "}",
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

    def test_loader_rejects_oversized_and_non_regular_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = Path(temp_dir) / "oversized.json"
            fixture.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(
                validate_file(fixture),
                [Finding("FIXTURE_TOO_LARGE", "$")],
            )

        if hasattr(os, "mkfifo"):
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

    def test_cli_is_sorted_machine_readable_and_does_not_echo_values(self) -> None:
        sentinel = "CANDIDATE_VALUE_MUST_NOT_BE_ECHOED"
        candidate = _load_candidate()
        candidate["taxon_ref"] = sentinel

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
        self.assertEqual(
            {envelope["status"] for envelope in envelopes}, {"PASS", "FAIL"}
        )
        for envelope in envelopes:
            self.assertEqual(envelope["scope"], "flora-public-safe-fixture")
            self.assertEqual(
                envelope["findings"],
                sorted(
                    envelope["findings"],
                    key=lambda item: (item["code"], item["path"]),
                ),
            )

    def test_cli_exit_codes_are_zero_one_and_two(self) -> None:
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
