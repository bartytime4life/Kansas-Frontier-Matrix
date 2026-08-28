"""Deterministic no-network tests for ReplaySafeEffectLedgerCandidate."""
from __future__ import annotations

import contextlib
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from tools.validators.runtime.replay_safe_effect_ledger_fixture_expectations import (
    evaluate_fixture_expectation,
)
from tools.validators.runtime.validate_replay_safe_effect_ledger import (
    FIXTURE_ROOT,
    MANIFEST_PATH,
    main,
    run_fixture_suite,
    validate_file,
    validate_file_staged,
)

VALID = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
SCHEMA_INVALID = sorted((FIXTURE_ROOT / "schema_invalid").glob("*.json"))
SEMANTIC_INVALID = sorted((FIXTURE_ROOT / "semantic_invalid").glob("*.json"))
EXECUTED = FIXTURE_ROOT / "valid" / "executed_once.json"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("replay-safe ledger validation attempted network access")


class ReplaySafeEffectLedgerTests(unittest.TestCase):
    def test_fixture_lanes_are_nonempty_and_valid_cases_pass(self) -> None:
        self.assertEqual(len(VALID), 5)
        self.assertEqual(len(SCHEMA_INVALID), 1)
        self.assertEqual(len(SEMANTIC_INVALID), 9)
        for path in VALID:
            with self.subTest(path=path.name):
                staged = validate_file_staged(path)
                self.assertEqual(staged.validation_stage, "SEMANTIC")
                self.assertEqual(staged.result.outcome, "PASS", staged.result.findings)

    def test_manifest_binds_exact_stage_outcomes_and_findings(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema_version"], "1.1.0")
        self.assertEqual(len(manifest["cases"]), 15)
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                staged = validate_file_staged(FIXTURE_ROOT / case["file"])
                result = staged.result
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                mismatches = evaluate_fixture_expectation(
                    case,
                    validation_stage=staged.validation_stage,
                    outcome=result.outcome,
                    findings=actual,
                )
                self.assertEqual(mismatches, ())

    def test_semantic_fixture_schema_regression_cannot_mask_coverage(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        case = next(
            item
            for item in manifest["cases"]
            if item["case_id"]
            == "semantic-invalid-compensation-without-completion"
        )
        candidate = json.loads(
            (FIXTURE_ROOT / case["file"]).read_text(encoding="utf-8")
        )
        candidate["event"]["payload_digest"] = "sha256:" + ("1" * 61)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "schema-regressed-semantic-negative.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            staged = validate_file_staged(path)
        actual = [
            {"code": finding.code, "path": finding.path}
            for finding in staged.result.findings
        ]
        mismatches = evaluate_fixture_expectation(
            case,
            validation_stage=staged.validation_stage,
            outcome=staged.result.outcome,
            findings=actual,
        )
        self.assertEqual(staged.validation_stage, "SCHEMA")
        self.assertIn(
            "VALIDATION_STAGE_MISMATCH",
            {item.code for item in mismatches},
        )
        self.assertNotEqual(mismatches, ())

    def test_negative_fixture_families_remain_distinct(self) -> None:
        schema = validate_file_staged(SCHEMA_INVALID[0])
        self.assertEqual(schema.validation_stage, "SCHEMA")
        self.assertEqual(schema.result.outcome, "ERROR")
        for path in SEMANTIC_INVALID:
            with self.subTest(path=path.name):
                staged = validate_file_staged(path)
                result = staged.result
                self.assertEqual(staged.validation_stage, "SEMANTIC")
                self.assertEqual(result.outcome, "DENY")
                self.assertNotIn(
                    "SCHEMA_INVALID",
                    {item.code for item in result.findings},
                )

    def test_duplicate_delivery_requires_one_suppression_bound_to_that_delivery(self) -> None:
        for filename in (
            "duplicate_unsuppressed.json",
            "duplicate_suppression_misbound.json",
        ):
            with self.subTest(filename=filename):
                result = validate_file(
                    FIXTURE_ROOT / "semantic_invalid" / filename
                )
                self.assertEqual(
                    [(item.code, item.path) for item in result.findings],
                    [("DUPLICATE_SUPPRESSION_INCOMPLETE", "/ledger_entries")],
                )

    def test_ledger_entry_cannot_precede_its_referenced_delivery(self) -> None:
        result = validate_file(
            FIXTURE_ROOT / "semantic_invalid" / "entry_before_delivery.json"
        )
        self.assertEqual(
            [(item.code, item.path) for item in result.findings],
            [("LEDGER_ENTRY_BEFORE_DELIVERY", "/ledger_entries/2/recorded_at")],
        )

    def test_compensation_requires_one_prior_completed_effect(self) -> None:
        result = validate_file(
            FIXTURE_ROOT
            / "semantic_invalid"
            / "compensation_without_completion.json"
        )
        self.assertEqual(
            [(item.code, item.path) for item in result.findings],
            [("COMPENSATION_WITHOUT_COMPLETION", "/ledger_entries")],
        )

    def test_reservation_snapshot_is_derived_from_ledger_transitions(self) -> None:
        valid = validate_file(
            FIXTURE_ROOT / "valid" / "completed_then_released.json"
        )
        self.assertEqual(valid.outcome, "PASS", valid.findings)
        invalid = validate_file(
            FIXTURE_ROOT
            / "semantic_invalid"
            / "reservation_state_unrecorded.json"
        )
        self.assertEqual(
            [(item.code, item.path) for item in invalid.findings],
            [("RESERVATION_STATE_MISMATCH", "/reservation/state")],
        )

    def test_reservation_timestamps_are_causal_and_ledger_bound(self) -> None:
        result = validate_file(
            FIXTURE_ROOT
            / "semantic_invalid"
            / "reservation_time_inverted.json"
        )
        self.assertEqual(
            [(item.code, item.path) for item in result.findings],
            [("RESERVATION_TIME_INVALID", "/reservation")],
        )

    def test_duplicate_keys_and_nonfinite_numbers_fail_closed(self) -> None:
        text = EXECUTED.read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(
                text.replace(
                    '  "schema_version": "1.0.0",',
                    '  "schema_version": "1.0.0",\n  "schema_version": "1.0.0",',
                    1,
                ),
                encoding="utf-8",
            )
            staged = validate_file_staged(path)
            self.assertEqual(staged.validation_stage, "PARSE")
            self.assertEqual(staged.result.findings[0].code, "DUPLICATE_KEY")
            path.write_text('{"value": NaN}\n', encoding="utf-8")
            staged = validate_file_staged(path)
            self.assertEqual(staged.validation_stage, "PARSE")
            self.assertEqual(staged.result.findings[0].code, "NONFINITE_NUMBER")

    def test_validation_performs_no_network_io(self) -> None:
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            result = validate_file(EXECUTED)
        self.assertEqual(result.outcome, "PASS", result.findings)

    def test_cli_is_deterministic_and_does_not_echo_candidate_values(self) -> None:
        candidate = json.loads(EXECUTED.read_text(encoding="utf-8"))
        subject_marker = "kfm://fixture/subject/redaction-marker"
        candidate["event"]["subject_ref"] = subject_marker
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            outputs = []
            for _ in range(2):
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    self.assertEqual(main([str(path)]), 1)
                outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(subject_marker, outputs[0])
        self.assertIn("EVENT_ID_MISMATCH", outputs[0])
        self.assertIn('"validation_stage": "SEMANTIC"', outputs[0])

    def test_fixture_runner_is_explicitly_non_authoritative(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 15)
        self.assertEqual(
            payload["stage_counts"],
            {"PARSE": 0, "SCHEMA": 1, "SEMANTIC": 14},
        )
        self.assertEqual(payload["authority"], "NONE")
        self.assertEqual(payload["execution_mode"], "FIXTURE_ONLY")
        self.assertEqual(payload["network_access"], "NONE")


if __name__ == "__main__":
    unittest.main()
