"""Deterministic no-network tests for the corrected web-delta profile fixtures."""

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

from jsonschema import Draft202012Validator

from tools.validators.replay_web_delta_profile_fixtures import (
    CORRECTION_PATH,
    load_effective_cases,
    run_fixture_suite,
)
from tools.validators.validate_web_delta_profile import (
    MAX_FILE_BYTES,
    SCHEMA_PATH,
    main as validate_main,
    validate_document,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[2]


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("web delta validation attempted network access")


class WebDeltaProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = load_effective_cases()
        cls.by_id = {case["case_id"]: case for case in cls.cases}

    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.path = self.root / "candidate.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _document(self, case_id: str) -> dict[str, object]:
        return copy.deepcopy(self.by_id[case_id]["document"])

    def _write(self, value: object) -> Path:
        self.path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        return self.path

    def test_profile_schema_is_valid_and_closed(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["properties"]["web.profile"]["const"], "kfm.web_delta.v1")

    def test_correction_manifest_is_bounded_and_append_only(self) -> None:
        correction = json.loads(CORRECTION_PATH.read_text(encoding="utf-8"))
        self.assertEqual(correction["status"], "CORRECTION")
        self.assertEqual(
            {item["case_id"] for item in correction["corrections"]},
            {"valid_http_304_heartbeat", "invalid_heartbeat_carries_new_content"},
        )
        self.assertIn("no_source_activation", correction["non_effects"])
        self.assertIn("no_publication", correction["non_effects"])

    def test_effective_fixture_matrix_has_exact_polarity(self) -> None:
        self.assertEqual(len(self.cases), 17)
        self.assertEqual(sum(case["expected_outcome"] == "PASS" for case in self.cases), 6)
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                result = validate_document(case["document"])
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                diagnostics = {
                    "actual_findings": actual,
                    "actual_event_id": result.event_id,
                    "actual_payload_spec_hash": result.payload_spec_hash,
                    "stored_event_id": case["document"]["event_id"],
                    "stored_payload_spec_hash": case["document"]["payload"]["payload_spec_hash"],
                }
                self.assertEqual(result.outcome, case["expected_outcome"], diagnostics)
                self.assertEqual(actual, case["expected_findings"], diagnostics)

    def test_replay_runner_passes_without_authority(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 17)
        self.assertEqual(payload["corrections_applied"], 2)
        self.assertEqual(payload["authority"], "NONE")
        self.assertIn("no_raw_or_lifecycle_write", payload["non_effects"])

    def test_license_modes_fail_closed(self) -> None:
        denied = validate_document(self._document("invalid_contentful_unknown_license"))
        self.assertEqual(denied.outcome, "DENY")
        self.assertIn(
            "CONTENTFUL_LICENSE_NOT_PERMITTED",
            {finding.code for finding in denied.findings},
        )
        for case_id in (
            "valid_metadata_only_restrictive",
            "valid_metadata_only_ambiguous",
            "valid_metadata_only_unknown",
        ):
            candidate = self._document(case_id)
            attributes = candidate["payload"]["attributes"]
            self.assertEqual(attributes["web.payload_mode"], "metadata_only")
            self.assertIsNone(attributes["web.canonical_new_digest"])
            self.assertIsNone(attributes["web.diff_digest"])
            self.assertEqual(candidate["routing"]["disposition"], "PROPOSE_QUARANTINE")
            self.assertEqual(validate_document(candidate).outcome, "PASS")

    def test_http_304_is_no_action_and_identity_valid(self) -> None:
        candidate = self._document("valid_http_304_heartbeat")
        result = validate_document(candidate)
        self.assertEqual(
            result.outcome,
            "PASS",
            {
                "findings": result.findings,
                "actual_event_id": result.event_id,
                "actual_payload_spec_hash": result.payload_spec_hash,
                "stored_event_id": candidate["event_id"],
                "stored_payload_spec_hash": candidate["payload"]["payload_spec_hash"],
            },
        )
        self.assertEqual(candidate["routing"]["disposition"], "NO_ACTION")
        self.assertIsNone(candidate["payload"]["attributes"]["web.raw_digest"])

    def test_base_envelope_integrity_remains_a_hard_dependency(self) -> None:
        candidate = self._document("valid_contentful_created_permissive")
        candidate["event_id"] = "kfm:source-event:sha256:" + "f" * 64
        result = validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn("EVENT_ID_MISMATCH", {finding.code for finding in result.findings})

    def test_bounded_file_reader_rejects_unsafe_inputs(self) -> None:
        valid = self._document("valid_contentful_created_permissive")
        text = json.dumps(valid, indent=2)
        duplicate = text.replace(
            '  "schema_version": "1.0.0",',
            '  "schema_version": "1.0.0",\n  "schema_version": "1.0.0",',
            1,
        )
        self.path.write_text(duplicate, encoding="utf-8")
        self.assertIn("DUPLICATE_KEY", {f.code for f in validate_file(self.path).findings})

        self.path.write_text('{"value": NaN}\n', encoding="utf-8")
        self.assertIn("NONFINITE_NUMBER", {f.code for f in validate_file(self.path).findings})

        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (MAX_FILE_BYTES + 1))
        self.assertIn("FILE_TOO_LARGE", {f.code for f in validate_file(oversized).findings})

        target = self._write(valid)
        linked = self.root / "linked.json"
        linked.symlink_to(target)
        self.assertIn("UNSAFE_FILE", {f.code for f in validate_file(linked).findings})

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO inputs require POSIX")
    def test_fifo_input_fails_without_blocking(self) -> None:
        fifo = self.root / "candidate.fifo"
        os.mkfifo(fifo)
        completed = subprocess.run(
            [sys.executable, "-m", "tools.validators.validate_web_delta_profile", str(fifo)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("UNSAFE_FILE", completed.stdout)

    def test_validation_is_no_network_and_diagnostics_do_not_echo_values(self) -> None:
        candidate = self._document("valid_contentful_created_permissive")
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            self.assertEqual(validate_document(candidate).outcome, "PASS")

        marker = "synthetic-source-marker-that-must-not-echo"
        candidate["payload"]["attributes"]["web.canonical_url"] = marker
        path = self._write(candidate)
        outputs: list[str] = []
        for _ in range(2):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                code = validate_main([str(path)])
            self.assertEqual(code, 1)
            outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(marker, outputs[0])
        self.assertIn("PAYLOAD_SPEC_HASH_MISMATCH", outputs[0])


if __name__ == "__main__":
    unittest.main()
