from __future__ import annotations

import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES
from tools.validators.validate_evidence_custody_handoff import (
    FIXTURES_ROOT,
    SCHEMA_PATH,
    canonical_digest,
    canonical_handoff_id,
    canonical_spec_hash,
    main as validate_main,
    validate_handoff_file,
)


class EvidenceCustodyHandoffTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_files = sorted((FIXTURES_ROOT / "valid").glob("valid_*.json"))
        self.semantic_files = sorted((FIXTURES_ROOT / "semantic_invalid").glob("semantic_invalid_*.json"))
        self.schema_files = sorted((FIXTURES_ROOT / "invalid").glob("invalid_*.json"))

    def test_schema_is_closed_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])

    def test_valid_fixtures_pass_with_deterministic_identity(self) -> None:
        self.assertEqual(len(self.valid_files), 3)
        for path in self.valid_files:
            with self.subTest(path=path.name):
                self.assertEqual(validate_handoff_file(path), [])
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(payload["sender"]["manifest_digest"], canonical_digest(payload["items"]))
                self.assertEqual(payload["receiver"]["reconciliation_digest"], canonical_digest(payload["receiver_dispositions"]))
                self.assertEqual(payload["handoff_id"], canonical_handoff_id(payload))
                self.assertEqual(payload["spec_hash"], canonical_spec_hash(payload))

    def test_semantic_invalid_fixtures_match_manifest_exactly(self) -> None:
        expected = json.loads((FIXTURES_ROOT / "semantic_invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual({path.name for path in self.semantic_files}, set(expected))
        for path in self.semantic_files:
            with self.subTest(path=path.name):
                actual = sorted({finding.code for finding in validate_handoff_file(path)})
                self.assertEqual(actual, sorted(expected[path.name]))

    def test_schema_invalid_lane_is_distinct_and_non_vacuous(self) -> None:
        expected = json.loads((FIXTURES_ROOT / "invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual({path.name for path in self.schema_files}, set(expected))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for path in self.schema_files:
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(list(validator.iter_errors(payload)))
            self.assertEqual(sorted({finding.code for finding in validate_handoff_file(path)}), sorted(expected[path.name]))
        for path in self.semantic_files:
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(list(validator.iter_errors(payload)), [])

    def test_closed_mixed_fixture_partitions_every_item_once(self) -> None:
        payload = json.loads((FIXTURES_ROOT / "valid/valid_closed_mixed_dispositions.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["summary"], {"sent": 4, "accepted": 2, "rejected": 1, "duplicate": 1, "unresolved": 0, "accounted": 4, "closure_status": "CLOSED"})
        self.assertEqual({item["item_id"] for item in payload["items"]}, {entry["item_id"] for entry in payload["receiver_dispositions"]})

    def test_unknown_posture_remains_open_in_quarantine(self) -> None:
        payload = json.loads((FIXTURES_ROOT / "valid/valid_open_unresolved_quarantine.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["receiver"]["lifecycle_stage"], "QUARANTINE")
        self.assertEqual(payload["summary"]["closure_status"], "OPEN")
        self.assertEqual(payload["summary"]["unresolved"], 1)

    def test_all_duplicate_fixture_proves_idempotent_accounting(self) -> None:
        payload = json.loads((FIXTURES_ROOT / "valid/valid_closed_all_duplicates.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["summary"]["accepted"], 0)
        self.assertEqual(payload["summary"]["duplicate"], payload["summary"]["sent"])
        self.assertTrue(all(entry["existing_item_ref"] for entry in payload["receiver_dispositions"]))

    def test_duplicate_keys_and_oversize_inputs_fail_before_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text('{"schema_version":"1.0.0","schema_version":"1.0.0"}', encoding="utf-8")
            self.assertEqual(validate_handoff_file(duplicate)[0].code, "FIXTURE_JSON_INVALID")
            oversized = Path(temp_dir) / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(validate_handoff_file(oversized)[0].code, "FIXTURE_TOO_LARGE")

    def test_cli_fixture_and_single_file_polarity(self) -> None:
        self.assertEqual(validate_main(["--fixtures"]), 0)
        self.assertEqual(validate_main([str(self.valid_files[0])]), 0)
        self.assertEqual(validate_main([str(self.semantic_files[0])]), 1)
        self.assertEqual(validate_main([]), 2)

    def test_validator_has_no_network_dependency(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            for path in [*self.valid_files, *self.semantic_files, *self.schema_files]:
                validate_handoff_file(path)


if __name__ == "__main__":
    unittest.main()
