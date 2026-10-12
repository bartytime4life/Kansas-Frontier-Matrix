"""No-network tests for the ConditionalDecisionClosure candidate."""

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

from tools.validators.policy.validate_conditional_decision_closure import (
    FIXTURES,
    MANIFEST,
    main,
    run_fixtures,
    validate,
)

VALID = sorted((FIXTURES / "valid").glob("*.json"))
SCHEMA_INVALID = sorted((FIXTURES / "schema_invalid").glob("*.json"))
SEMANTIC_INVALID = sorted((FIXTURES / "semantic_invalid").glob("*.json"))
SATISFIED = FIXTURES / "valid" / "satisfied.json"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("conditional decision closure attempted network access")


class ConditionalDecisionClosureTests(unittest.TestCase):
    def test_fixture_lanes_are_nonempty_and_valid_cases_pass(self) -> None:
        self.assertEqual(len(VALID), 4)
        self.assertEqual(len(SCHEMA_INVALID), 1)
        self.assertEqual(len(SEMANTIC_INVALID), 5)
        for path in VALID:
            with self.subTest(path=path.name):
                result = validate(path)
                self.assertEqual(result.outcome, "PASS", result.findings)

    def test_manifest_binds_exact_outcomes_and_findings(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["cases"]), 10)
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validate(FIXTURES / case["file"])
                actual = [
                    {"code": item.code, "path": item.path}
                    for item in result.findings
                ]
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(actual, case["expected_findings"])

    def test_open_expired_and_violated_obligations_hold(self) -> None:
        for filename in ("open_hold.json", "expired_violated_hold.json"):
            candidate = json.loads((FIXTURES / "valid" / filename).read_text())
            self.assertEqual(candidate["result"]["outcome"], "HOLD")
            self.assertTrue(candidate["result"]["blocking_obligation_ids"])
            self.assertEqual(validate(FIXTURES / "valid" / filename).outcome, "PASS")

    def test_missing_closure_evidence_and_waiver_authority_deny(self) -> None:
        expected = {
            "satisfied_missing_evidence.json": "CLOSURE_EVIDENCE_MISSING",
            "waiver_missing_authority.json": "WAIVER_AUTHORITY_MISSING",
        }
        for filename, code in expected.items():
            with self.subTest(filename=filename):
                result = validate(FIXTURES / "semantic_invalid" / filename)
                self.assertEqual(result.outcome, "DENY")
                self.assertEqual([item.code for item in result.findings], [code])

    def test_duplicate_keys_and_nonfinite_numbers_fail_closed(self) -> None:
        text = SATISFIED.read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(
                text.replace(
                    '  "object_type": "ConditionalDecisionClosure",',
                    '  "object_type": "ConditionalDecisionClosure",\n'
                    '  "object_type": "ConditionalDecisionClosure",',
                    1,
                ),
                encoding="utf-8",
            )
            self.assertEqual(validate(path).findings[0].code, "JSON_DUPLICATE_KEY")
            path.write_text('{"value": NaN}\n', encoding="utf-8")
            self.assertEqual(validate(path).findings[0].code, "JSON_NONFINITE_NUMBER")

    def test_validation_performs_no_network_io(self) -> None:
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            result = validate(SATISFIED)
        self.assertEqual(result.outcome, "PASS", result.findings)

    def test_cli_is_deterministic_and_does_not_echo_candidate_values(self) -> None:
        candidate = json.loads(SATISFIED.read_text(encoding="utf-8"))
        subject_marker = "kfm://fixture/subject/redaction-marker"
        candidate["subject_ref"] = subject_marker
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
        self.assertIn("SPEC_HASH_MISMATCH", outputs[0])

    def test_fixture_runner_has_no_authority(self) -> None:
        ok, payload = run_fixtures()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 10)
        self.assertEqual(payload["authority"], "NONE")
        self.assertEqual(payload["execution_mode"], "FIXTURE_ONLY")
        self.assertEqual(payload["network_access"], "NONE")


if __name__ == "__main__":
    unittest.main()
