"""Deterministic no-network tests for SourceActivationDecision validation."""

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

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators.validate_source_activation_decision import (
    FIXTURE_ROOT,
    MAX_FILE_BYTES,
    MAX_SCHEMA_FINDINGS,
    SCHEMA_PATH,
    _expected_codes,
    main,
    validate_decision,
)


ROOT = Path(__file__).resolve().parents[2]
VALID = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
INVALID = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
SEMANTIC_INVALID = sorted((FIXTURE_ROOT / "semantic_invalid").glob("invalid_*.json"))
FIXTURE_ADMIT = FIXTURE_ROOT / "valid" / "valid_1_fixture_only_admit.json"
LIVE_CAPTURE = FIXTURE_ROOT / "valid" / "valid_2_live_raw_capture.json"
QUARANTINE = FIXTURE_ROOT / "valid" / "valid_4_quarantine_unknown_rights.json"
HOLD = FIXTURE_ROOT / "valid" / "valid_5_hold_permission_review.json"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("SourceActivationDecision validation attempted network access")


class SourceActivationDecisionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.path = self.root / "activation-decision.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _fixture(self, path: Path = FIXTURE_ADMIT) -> dict[str, object]:
        return json.loads(path.read_text(encoding="utf-8"))

    def _write(self, payload: dict[str, object]) -> Path:
        self.path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return self.path

    def _mutated(self, fixture: Path, mutate) -> Path:
        payload = copy.deepcopy(self._fixture(fixture))
        mutate(payload)
        return self._write(payload)

    def assertCode(self, path: Path, code: str) -> None:
        result = validate_decision(path)
        self.assertIn(code, {finding.code for finding in result.findings})

    def test_all_six_finite_route_profiles_pass(self) -> None:
        self.assertEqual(len(VALID), 6)
        observed_routes = set()
        for path in VALID:
            with self.subTest(path=path.name):
                result = validate_decision(path)
                self.assertTrue(result.ok, result.findings)
                observed_routes.add(result.route)
        self.assertEqual(
            observed_routes,
            {"ADMIT_TO_RAW", "QUARANTINE", "HOLD", "DENY_INTAKE", "ERROR"},
        )

    def test_schema_and_semantic_negative_fixtures_match_exact_sidecars(self) -> None:
        self.assertEqual(len(INVALID), 4)
        self.assertEqual(len(SEMANTIC_INVALID), 8)
        for path in (*INVALID, *SEMANTIC_INVALID):
            with self.subTest(path=path.name):
                expected = set(_expected_codes(path))
                result = validate_decision(path)
                actual = {finding.code for finding in result.findings}
                self.assertFalse(result.ok)
                self.assertEqual(actual, expected)

    def test_semantic_negative_fixtures_remain_schema_valid(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for path in SEMANTIC_INVALID:
            with self.subTest(path=path.name):
                errors = list(
                    validator.iter_errors(json.loads(path.read_text(encoding="utf-8")))
                )
                self.assertEqual(errors, [])

    def test_descriptor_and_source_role_references_are_exactly_bound(self) -> None:
        self.assertCode(
            self._mutated(
                FIXTURE_ADMIT,
                lambda value: value.update(
                    source_descriptor_ref=(
                        "source-descriptor:src:synthetic:other-source:1.0.0"
                    ),
                    source_role_ref=(
                        "source-descriptor:src:synthetic:other-source:"
                        "1.0.0#/source_role"
                    ),
                ),
            ),
            "SOURCE_DESCRIPTOR_REF_UNBOUND",
        )
        self.assertCode(
            self._mutated(
                FIXTURE_ADMIT,
                lambda value: value.update(
                    source_role_ref=(
                        "source-descriptor:src:synthetic:other-source:"
                        "1.0.0#/source_role"
                    )
                ),
            ),
            "SOURCE_ROLE_REF_UNBOUND",
        )

    def test_all_zero_descriptor_and_spec_hashes_are_rejected(self) -> None:
        cases = (
            lambda value: value.update(
                source_descriptor_digest="sha256:" + ("0" * 64)
            ),
            lambda value: value["governance"].update(
                spec_hash="sha256:" + ("0" * 64)
            ),
        )
        for mutate in cases:
            with self.subTest(mutate=mutate):
                self.assertCode(
                    self._mutated(FIXTURE_ADMIT, mutate),
                    "PLACEHOLDER_DIGEST",
                )

    def test_admit_route_fails_closed_for_rights_access_and_descriptor_review(self) -> None:
        cases = (
            (
                lambda value: value["context"].update(rights_status="unknown"),
                "ADMIT_RIGHTS_BLOCKED",
            ),
            (
                lambda value: value["context"].update(access_posture="closed"),
                "ADMIT_ACCESS_BLOCKED",
            ),
            (
                lambda value: value["context"].update(
                    descriptor_review_state="needs_review"
                ),
                "ADMIT_DESCRIPTOR_REVIEW_REQUIRED",
            ),
            (
                lambda value: value["decision"].update(policy_decision_refs=[]),
                "ADMIT_POLICY_REFERENCE_REQUIRED",
            ),
        )
        for mutate, code in cases:
            with self.subTest(code=code):
                self.assertCode(self._mutated(FIXTURE_ADMIT, mutate), code)

    def test_raw_capture_requires_active_registry_review_and_ingest_receipt(self) -> None:
        cases = (
            (
                lambda value: value["decision"].update(
                    activation_state="live_candidate"
                ),
                "RAW_CAPTURE_REQUIRES_LIVE_ACTIVE",
            ),
            (
                lambda value: value["decision"].update(
                    review_state="pending",
                    review_refs=[],
                ),
                "RAW_CAPTURE_REQUIRES_APPROVED_REVIEW",
            ),
            (
                lambda value: value["context"].update(registry_state="proposed"),
                "RAW_CAPTURE_REQUIRES_ACTIVE_REGISTRY",
            ),
            (
                lambda value: value["decision"].update(
                    obligations=[
                        item
                        for item in value["decision"]["obligations"]
                        if item != "require_ingest_receipt"
                    ]
                ),
                "RAW_CAPTURE_RECEIPT_OBLIGATION_MISSING",
            ),
        )
        for mutate, code in cases:
            with self.subTest(code=code):
                self.assertCode(self._mutated(LIVE_CAPTURE, mutate), code)

    def test_quarantine_and_hold_routes_require_governed_obligations(self) -> None:
        self.assertCode(
            self._mutated(
                QUARANTINE,
                lambda value: value["decision"].update(
                    obligations=[
                        item
                        for item in value["decision"]["obligations"]
                        if item != "open_quarantine_case"
                    ]
                ),
            ),
            "QUARANTINE_OBLIGATION_MISSING",
        )
        self.assertCode(
            self._mutated(
                HOLD,
                lambda value: value["decision"].update(
                    obligations=[
                        item
                        for item in value["decision"]["obligations"]
                        if item != "set_hold_expiry"
                    ]
                ),
            ),
            "HOLD_EXPIRY_OBLIGATION_MISSING",
        )

    def test_time_order_and_timezone_fail_closed(self) -> None:
        cases = (
            (
                lambda value: value["timing"].update(
                    effective_at="2026-08-02T12:00:00Z"
                ),
                "EFFECTIVE_TIME_INVALID",
            ),
            (
                lambda value: value["timing"].update(
                    expires_at="2026-08-03T11:59:59Z"
                ),
                "EXPIRY_TIME_INVALID",
            ),
            (
                lambda value: value["timing"].update(
                    created_at="2026-08-03T12:00:00"
                ),
                "TEMPORAL_TIMEZONE_REQUIRED",
            ),
            (
                lambda value: value["timing"].update(
                    hold_expires_at="2026-08-02T12:00:00Z"
                ),
                "HOLD_EXPIRY_INVALID",
            ),
        )
        fixtures = (FIXTURE_ADMIT, LIVE_CAPTURE, FIXTURE_ADMIT, HOLD)
        for fixture, (mutate, code) in zip(fixtures, cases, strict=True):
            with self.subTest(code=code):
                self.assertCode(self._mutated(fixture, mutate), code)

    def test_lineage_self_reference_and_direction_conflict_are_rejected(self) -> None:
        def self_reference(value):
            value["lineage"]["supersedes"] = value["activation_decision_id"]

        self.assertCode(
            self._mutated(FIXTURE_ADMIT, self_reference),
            "SELF_LINEAGE_REFERENCE",
        )

        def conflict(value):
            value["lineage"]["supersedes"] = (
                "activation:synthetic-prior-source:20260701"
            )
            value["lineage"]["superseded_by"] = (
                "activation:synthetic-prior-source:20260701"
            )

        self.assertCode(
            self._mutated(FIXTURE_ADMIT, conflict),
            "LINEAGE_DIRECTION_CONFLICT",
        )

    def test_duplicate_keys_nonfinite_numbers_and_excessive_nesting_fail_closed(self) -> None:
        text = FIXTURE_ADMIT.read_text(encoding="utf-8")
        duplicate = text.replace(
            '  "schema_version": "1.0.0",',
            '  "schema_version": "1.0.0",\n'
            '  "schema_version": "1.0.0",',
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
        payload["decision"]["review_refs"] = [
            index for index in range(MAX_SCHEMA_FINDINGS + 50)
        ]
        result = validate_decision(self._write(payload))
        codes = {finding.code for finding in result.findings}
        self.assertIn("SCHEMA_FINDINGS_TRUNCATED", codes)
        self.assertLessEqual(len(result.findings), MAX_SCHEMA_FINDINGS + 1)

    def test_oversized_symlink_and_fifo_inputs_fail_closed(self) -> None:
        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (MAX_FILE_BYTES + 1))
        self.assertCode(oversized, "FILE_TOO_LARGE")

        target = self._write(self._fixture())
        linked = self.root / "linked.json"
        linked.symlink_to(target)
        self.assertCode(linked, "UNSAFE_FILE")

        if hasattr(os, "mkfifo"):
            fifo = self.root / "decision.fifo"
            os.mkfifo(fifo)
            self.assertCode(fifo, "UNSAFE_FILE")

    def test_validation_performs_no_network_io(self) -> None:
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            result = validate_decision(FIXTURE_ADMIT)
        self.assertTrue(result.ok, result.findings)

    def test_cli_output_is_deterministic_and_does_not_echo_values(self) -> None:
        payload = self._fixture()
        secret_marker = "synthetic-sensitive-authority-marker"
        payload["decision"]["decision_authority_ref"] = secret_marker
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
