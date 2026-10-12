from __future__ import annotations

import json
import socket
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES
from tools.validators.validate_occurrence_retrieval_snapshot import (
    FIXTURES_ROOT,
    SCHEMA_PATH,
    canonical_query_hash,
    canonical_spec_hash,
    main as validate_main,
    validate_document,
    validate_snapshot_file,
)


class OccurrenceRetrievalSnapshotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_files = sorted((FIXTURES_ROOT / "valid").glob("valid_*.json"))
        self.semantic_files = sorted((FIXTURES_ROOT / "semantic_invalid").glob("semantic_invalid_*.json"))
        self.schema_files = sorted((FIXTURES_ROOT / "schema_invalid").glob("invalid_*.json"))

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_valid_fixtures_pass_with_canonical_identity(self) -> None:
        self.assertEqual(len(self.valid_files), 3)
        for path in self.valid_files:
            with self.subTest(path=path.name):
                self.assertEqual(validate_snapshot_file(path), [])
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(payload["query_snapshot"]["query_hash"], canonical_query_hash(payload["query_snapshot"]))
                self.assertEqual(payload["spec_hash"], canonical_spec_hash(payload))
                self.assertEqual(payload["revision"], len(payload["transfer"]["state_history"]))

    def test_semantic_invalid_fixtures_match_manifest_exactly(self) -> None:
        expected = json.loads(
            (FIXTURES_ROOT / "semantic_invalid/expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual({path.name for path in self.semantic_files}, set(expected))
        for path in self.semantic_files:
            with self.subTest(path=path.name):
                actual = sorted({finding.code for finding in validate_snapshot_file(path)})
                self.assertEqual(actual, sorted(expected[path.name]))

    def test_schema_invalid_lane_is_distinct_and_non_vacuous(self) -> None:
        expected = json.loads(
            (FIXTURES_ROOT / "schema_invalid/expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual({path.name for path in self.schema_files}, set(expected))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema)
        for path in self.schema_files:
            with self.subTest(path=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertTrue(list(validator.iter_errors(payload)))
                actual = sorted({finding.code for finding in validate_snapshot_file(path)})
                self.assertEqual(actual, sorted(expected[path.name]))
        for path in self.semantic_files:
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(list(validator.iter_errors(payload)), [])

    def test_sampling_support_distinguishes_non_detection_from_absence(self) -> None:
        ebird = json.loads((FIXTURES_ROOT / "valid/valid_ebird_complete_checklist_succeeded.json").read_text(encoding="utf-8"))
        gbif = json.loads((FIXTURES_ROOT / "valid/valid_gbif_async_succeeded.json").read_text(encoding="utf-8"))
        self.assertTrue(ebird["sampling_support"]["non_detection_supported"])
        self.assertFalse(ebird["sampling_support"]["absence_claim_supported"])
        self.assertEqual(ebird["result_semantics"]["non_detection_scope"], "CHECKLIST_EVENT_ONLY")
        self.assertFalse(gbif["sampling_support"]["non_detection_supported"])
        self.assertFalse(gbif["sampling_support"]["absence_claim_supported"])

    def test_transfer_failure_and_zero_records_never_become_absence(self) -> None:
        zero = json.loads((FIXTURES_ROOT / "valid/valid_gbif_async_succeeded.json").read_text(encoding="utf-8"))
        zero["transfer"]["record_count"] = 0
        zero["transfer"]["result_interpretation"] = "zero_records_no_claim"
        zero["spec_hash"] = canonical_spec_hash(zero)
        self.assertEqual(validate_document(zero), [])

        failed = deepcopy(zero)
        failed["transfer"]["state_history"].append({"state": "FAILED", "occurred_at": "2026-04-30T12:04:00Z"})
        failed["transfer"]["current_state"] = "FAILED"
        failed["transfer"]["result_artifact_refs"] = []
        failed["transfer"]["citation_refs"] = []
        failed["transfer"]["record_count"] = None
        failed["transfer"]["result_interpretation"] = "not_evaluated"
        failed["transfer"]["failure_reason_code"] = "SYNTHETIC_TRANSFER_FAILED"
        failed["revision"] = len(failed["transfer"]["state_history"])
        failed["snapshot_id"] = f"{failed['retrieval_id']}/revision/{failed['revision']}"
        failed["previous_snapshot_ref"] = f"{failed['retrieval_id']}/revision/{failed['revision'] - 1}"
        failed["spec_hash"] = canonical_spec_hash(failed)
        codes = {finding.code for finding in validate_document(failed)}
        self.assertEqual(codes, {"OCCURRENCE_RETRIEVAL_TRANSFER_TRANSITION_INVALID"})

    def test_duplicate_keys_and_oversize_inputs_fail_before_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text('{"schema_version":"x","schema_version":"x"}', encoding="utf-8")
            self.assertEqual(validate_snapshot_file(duplicate)[0].code, "FIXTURE_JSON_INVALID")
            oversized = Path(temp_dir) / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(validate_snapshot_file(oversized)[0].code, "FIXTURE_TOO_LARGE")

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
                validate_snapshot_file(path)


if __name__ == "__main__":
    unittest.main()
