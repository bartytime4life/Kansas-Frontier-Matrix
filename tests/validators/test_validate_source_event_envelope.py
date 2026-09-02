"""Deterministic no-network tests for SourceEventEnvelopeCandidate validation."""

from __future__ import annotations

import contextlib
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

from tools.validators.validate_source_event_envelope import (
    FIXTURE_ROOT,
    MANIFEST_PATH,
    MAX_FILE_BYTES,
    main,
    run_fixture_suite,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[2]
VALID = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
INVALID = sorted((FIXTURE_ROOT / "invalid").glob("*.json"))
SEMANTIC_INVALID = sorted((FIXTURE_ROOT / "semantic_invalid").glob("*.json"))
ADMISSION = FIXTURE_ROOT / "valid" / "valid_admission_candidate.json"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("SourceEventEnvelope validation attempted network access")


class SourceEventEnvelopeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.path = self.root / "event.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _fixture(self) -> dict[str, object]:
        return json.loads(ADMISSION.read_text(encoding="utf-8"))

    def _write(self, payload: object) -> Path:
        self.path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return self.path

    def assertCode(self, path: Path, code: str) -> None:
        result = validate_file(path)
        self.assertIn(code, {finding.code for finding in result.findings})

    def test_fixture_lanes_are_nonempty_and_valid_cases_pass(self) -> None:
        self.assertEqual(len(VALID), 4)
        self.assertEqual(len(INVALID), 4)
        self.assertEqual(len(SEMANTIC_INVALID), 13)
        for path in VALID:
            with self.subTest(path=path.name):
                result = validate_file(path)
                self.assertEqual(result.outcome, "PASS", result.findings)

    def test_fixture_manifest_matches_exact_outcomes_and_findings(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["cases"]), 21)
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validate_file(FIXTURE_ROOT / case["file"])
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(actual, case["expected_findings"])

    def test_schema_invalid_and_semantic_invalid_lanes_remain_distinct(self) -> None:
        for path in INVALID:
            with self.subTest(path=path.name):
                result = validate_file(path)
                self.assertFalse(result.outcome == "PASS")
                self.assertEqual(
                    {finding.code for finding in result.findings},
                    {"SCHEMA_INVALID"},
                )
        for path in SEMANTIC_INVALID:
            with self.subTest(path=path.name):
                result = validate_file(path)
                self.assertEqual(result.outcome, "DENY")
                self.assertNotIn(
                    "SCHEMA_INVALID",
                    {finding.code for finding in result.findings},
                )

    def test_duplicate_keys_nonfinite_numbers_and_nesting_fail_closed(self) -> None:
        text = ADMISSION.read_text(encoding="utf-8")
        duplicate = text.replace(
            '  "schema_version": "1.0.0",',
            '  "schema_version": "1.0.0",\n  "schema_version": "1.0.0",',
            1,
        )
        self.path.write_text(duplicate, encoding="utf-8")
        self.assertCode(self.path, "DUPLICATE_KEY")

        self.path.write_text('{"value": NaN}\n', encoding="utf-8")
        self.assertCode(self.path, "NONFINITE_NUMBER")

        nested = "[" * 100 + "0" + "]" * 100
        self.path.write_text('{"nested":' + nested + "}\n", encoding="utf-8")
        self.assertCode(self.path, "JSON_COMPLEXITY_LIMIT")

    def test_oversized_and_symbolic_link_inputs_fail_closed(self) -> None:
        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (MAX_FILE_BYTES + 1))
        self.assertCode(oversized, "FILE_TOO_LARGE")

        target = self._write(self._fixture())
        linked = self.root / "linked.json"
        linked.symlink_to(target)
        self.assertCode(linked, "UNSAFE_FILE")

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO inputs require POSIX")
    def test_fifo_input_fails_without_blocking(self) -> None:
        fifo = self.root / "event.fifo"
        os.mkfifo(fifo)
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools/validators/validate_source_event_envelope.py"),
                str(fifo),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("UNSAFE_FILE", completed.stdout)

    def test_validation_performs_no_network_io(self) -> None:
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            result = validate_file(ADMISSION)
        self.assertEqual(result.outcome, "PASS", result.findings)

    def test_cli_output_is_deterministic_and_does_not_echo_candidate_values(self) -> None:
        payload = self._fixture()
        secret_marker = "synthetic-private-source-marker"
        payload["subject"]["subject_ref"] = secret_marker
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
        self.assertIn("EVENT_ID_MISMATCH", outputs[0])

    def test_fixture_cli_passes(self) -> None:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(["--fixtures"])
        self.assertEqual(code, 0, stream.getvalue())
        payload = json.loads(stream.getvalue())
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 21)
        self.assertEqual(payload["authority"], "NONE")

    def test_source_role_and_routing_rules_fail_closed(self) -> None:
        cases = {
            "SOURCE_ROLE_REF_UNBOUND": (
                FIXTURE_ROOT
                / "semantic_invalid"
                / "semantic_invalid_source_role.json"
            ),
            "ADMISSION_GOVERNANCE_INCOMPLETE": (
                FIXTURE_ROOT
                / "semantic_invalid"
                / "semantic_invalid_unknown_rights_admission.json"
            ),
            "MANUAL_REPLAY_ROUTING_INVALID": (
                FIXTURE_ROOT
                / "semantic_invalid"
                / "semantic_invalid_manual_replay_routing.json"
            ),
        }
        for code, path in cases.items():
            with self.subTest(code=code):
                self.assertCode(path, code)

    def test_deterministic_identity_and_payload_hash_are_reported(self) -> None:
        result = validate_file(ADMISSION)
        self.assertEqual(result.outcome, "PASS")
        self.assertIsNotNone(result.event_id)
        self.assertTrue(result.event_id.startswith("kfm:source-event:sha256:"))
        self.assertIsNotNone(result.payload_spec_hash)
        self.assertTrue(result.payload_spec_hash.startswith("sha256:"))

    def test_fixture_runner_has_no_side_effect_authority(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["authority"], "NONE")
        self.assertEqual(payload["execution_mode"], "FIXTURE_ONLY")
        self.assertIn("no_source_activation", payload["non_effects"])
        self.assertIn("no_raw_or_lifecycle_write", payload["non_effects"])
        self.assertIn(
            "no_promotion_release_deployment_or_publication",
            payload["non_effects"],
        )


if __name__ == "__main__":
    unittest.main()
