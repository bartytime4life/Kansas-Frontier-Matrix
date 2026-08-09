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

from tools.validators.runtime.validate_replay_safe_effect_ledger import (
    FIXTURE_ROOT,
    MANIFEST_PATH,
    main,
    run_fixture_suite,
    validate_file,
)

VALID = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
SCHEMA_INVALID = sorted((FIXTURE_ROOT / "schema_invalid").glob("*.json"))
SEMANTIC_INVALID = sorted((FIXTURE_ROOT / "semantic_invalid").glob("*.json"))
EXECUTED = FIXTURE_ROOT / "valid" / "executed_once.json"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("replay-safe ledger validation attempted network access")


class ReplaySafeEffectLedgerTests(unittest.TestCase):
    def test_fixture_lanes_are_nonempty_and_valid_cases_pass(self) -> None:
        self.assertEqual(len(VALID), 4)
        self.assertEqual(len(SCHEMA_INVALID), 1)
        self.assertEqual(len(SEMANTIC_INVALID), 4)
        for path in VALID:
            with self.subTest(path=path.name):
                result = validate_file(path)
                self.assertEqual(result.outcome, "PASS", result.findings)

    def test_manifest_binds_exact_outcomes_and_findings(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["cases"]), 9)
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validate_file(FIXTURE_ROOT / case["file"])
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(actual, case["expected_findings"])

    def test_negative_fixture_families_remain_distinct(self) -> None:
        self.assertEqual(validate_file(SCHEMA_INVALID[0]).outcome, "ERROR")
        for path in SEMANTIC_INVALID:
            with self.subTest(path=path.name):
                result = validate_file(path)
                self.assertEqual(result.outcome, "DENY")
                self.assertNotIn("SCHEMA_INVALID", {item.code for item in result.findings})

    def test_duplicate_delivery_requires_recorded_suppression(self) -> None:
        result = validate_file(FIXTURE_ROOT / "semantic_invalid" / "duplicate_unsuppressed.json")
        self.assertEqual(
            [(item.code, item.path) for item in result.findings],
            [("DUPLICATE_SUPPRESSION_INCOMPLETE", "/ledger_entries")],
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
            self.assertEqual(validate_file(path).findings[0].code, "DUPLICATE_KEY")
            path.write_text('{"value": NaN}\n', encoding="utf-8")
            self.assertEqual(validate_file(path).findings[0].code, "NONFINITE_NUMBER")

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
        sentinel = "synthetic-sensitive-subject-marker"
        candidate["event"]["subject_ref"] = sentinel
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
        self.assertNotIn(sentinel, outputs[0])
        self.assertIn("EVENT_ID_MISMATCH", outputs[0])

    def test_fixture_runner_is_explicitly_non_authoritative(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 9)
        self.assertEqual(payload["authority"], "NONE")
        self.assertEqual(payload["execution_mode"], "FIXTURE_ONLY")
        self.assertEqual(payload["network_access"], "NONE")


if __name__ == "__main__":
    unittest.main()
