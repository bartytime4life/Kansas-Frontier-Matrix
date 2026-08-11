"""Deterministic no-network tests for SourceEvent admission candidates."""

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

from tools.validators.validate_source_event_admission import (
    EVENT_FIXTURE_ROOT,
    FIXTURE_ROOT,
    MANIFEST_PATH,
    MAX_FILE_BYTES,
    PREFILTER_SCHEMA_PATH,
    RECEIPT_SCHEMA_PATH,
    _expected_fixture_signature,
    _expected_prefilter_id,
    _expected_prefilter_spec_hash,
    _expected_receipt_id,
    _expected_receipt_spec_hash,
    main,
    run_fixture_suite,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[2]
VALID_PREFILTER = FIXTURE_ROOT / "valid" / "valid_prefilter_material_change.json"
VALID_RECEIPT = FIXTURE_ROOT / "valid" / "valid_receipt_allow_fixture.json"
EVENT = EVENT_FIXTURE_ROOT / "valid_admission_candidate.json"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("SourceEvent admission validation attempted network access")


class SourceEventAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.path = self.root / "candidate.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _write(self, payload: object) -> Path:
        self.path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return self.path

    def test_schemas_are_valid_draft_2020_12(self) -> None:
        prefilter_schema = json.loads(PREFILTER_SCHEMA_PATH.read_text(encoding="utf-8"))
        receipt_schema = json.loads(RECEIPT_SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(prefilter_schema)
        Draft202012Validator.check_schema(receipt_schema)
        self.assertEqual(prefilter_schema["x-kfm"]["status"], "PROPOSED")
        self.assertEqual(receipt_schema["x-kfm"]["status"], "PROPOSED")
        self.assertFalse(prefilter_schema["additionalProperties"])
        self.assertFalse(receipt_schema["additionalProperties"])

    def test_fixture_manifest_matches_exact_outcomes_and_findings(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["cases"]), 13)
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertTrue(all(item["matches_manifest"] for item in payload["reports"]))

    def test_valid_identity_and_fixture_signature_are_deterministic(self) -> None:
        prefilter = json.loads(VALID_PREFILTER.read_text(encoding="utf-8"))
        receipt = json.loads(VALID_RECEIPT.read_text(encoding="utf-8"))
        self.assertEqual(prefilter["prefilter_id"], _expected_prefilter_id(prefilter))
        self.assertEqual(prefilter["spec_hash"], _expected_prefilter_spec_hash(prefilter))
        self.assertEqual(receipt["receipt_id"], _expected_receipt_id(receipt))
        self.assertEqual(receipt["spec_hash"], _expected_receipt_spec_hash(receipt))
        self.assertEqual(
            receipt["signature"]["signature_value"],
            _expected_fixture_signature(receipt),
        )
        self.assertFalse(receipt["signature"]["production_signature_claimed"])

    def test_validation_performs_no_network_io(self) -> None:
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            result = validate_file(
                VALID_RECEIPT,
                event_path=EVENT,
                prefilter_path=VALID_PREFILTER,
            )
        self.assertEqual(result.outcome, "PASS", result.findings)

    def test_duplicate_nonfinite_oversized_and_symlink_inputs_fail_closed(self) -> None:
        self.path.write_text(
            '{"object_type":"SourceEventPrefilterOutputCandidate",'
            '"object_type":"SourceEventPrefilterOutputCandidate"}\n',
            encoding="utf-8",
        )
        self.assertIn(
            "DUPLICATE_KEY",
            {item.code for item in validate_file(self.path).findings},
        )

        self.path.write_text('{"value":NaN}\n', encoding="utf-8")
        self.assertIn(
            "NONFINITE_NUMBER",
            {item.code for item in validate_file(self.path).findings},
        )

        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (MAX_FILE_BYTES + 1))
        self.assertIn(
            "FILE_TOO_LARGE",
            {item.code for item in validate_file(oversized).findings},
        )

        linked = self.root / "linked.json"
        linked.symlink_to(VALID_PREFILTER)
        self.assertIn(
            "UNSAFE_FILE",
            {item.code for item in validate_file(linked).findings},
        )

    def test_diagnostics_are_deterministic_and_do_not_echo_values(self) -> None:
        candidate = json.loads(VALID_PREFILTER.read_text(encoding="utf-8"))
        sentinel_value = "UNIQUE-PREFILTER-SENTINEL-DO-NOT-ECHO"
        candidate["reason_codes"] = [sentinel_value]
        path = self._write(candidate)

        outputs: list[str] = []
        for _ in range(2):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                code = main([str(path), "--event", str(EVENT)])
            self.assertEqual(code, 1)
            outputs.append(stream.getvalue())

        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(sentinel_value, outputs[0])
        self.assertIn("SCHEMA_INVALID", outputs[0])

    def test_receipt_cannot_claim_operational_or_public_authority(self) -> None:
        receipt = json.loads(VALID_RECEIPT.read_text(encoding="utf-8"))
        self.assertEqual(receipt["claims"]["operational_effect"], "NONE_FIXTURE_ONLY")
        for field in (
            "raw_write_allowed",
            "raw_write_performed",
            "work_write_performed",
            "quarantine_write_performed",
            "authority_created",
            "evidence_created",
            "proof_created",
            "policy_authority_created",
            "review_approved",
            "promoted",
            "released",
            "published",
            "network_access_performed",
        ):
            self.assertFalse(receipt["claims"][field])

    def test_fixture_cli_passes_and_reports_no_authority(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools/validators/validate_source_event_admission.py"),
                "--fixtures",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 13)
        self.assertEqual(payload["authority"], "NONE")
        self.assertIn("no_raw_or_lifecycle_write", payload["non_effects"])


if __name__ == "__main__":
    unittest.main()
