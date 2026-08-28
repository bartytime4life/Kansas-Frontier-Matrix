"""Deterministic no-network tests for SourceArtifact validation and local storage."""

from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import os
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

from tools.source_artifacts.content_addressed_store import object_path, store, verify
from tools.validators.validate_source_artifact import (
    FIXTURE_ROOT,
    MAX_METADATA_BYTES,
    SCHEMA_PATH,
    load_fixture_cases,
    main,
    materialize_case,
    validate_artifact,
)

CORPUS = load_fixture_cases()
VALID_CASES = CORPUS["valid"]
INVALID_CASES = CORPUS["invalid"]
SEMANTIC_CASES = CORPUS["semantic_invalid"]


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("SourceArtifact validation attempted network access")


def _case(name: str) -> dict[str, object]:
    for lane in (VALID_CASES, INVALID_CASES, SEMANTIC_CASES):
        for item in lane:
            if item["name"] == name:
                return copy.deepcopy(item)
    raise KeyError(name)


class SourceArtifactTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.metadata_path = self.root / "artifact.json"
        self.payload_path = self.root / "payload.bin"
        self.api_case = _case("valid_fetched_api")
        self.api_metadata, self.api_payload = materialize_case(self.api_case, self.root)
        assert self.api_payload is not None

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _write_metadata(self, metadata: dict[str, object]) -> Path:
        self.metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return self.metadata_path

    def assertCode(self, path: Path, code: str, payload: Path | None = None) -> None:
        result = validate_artifact(path, payload)
        self.assertIn(code, {finding.code for finding in result.findings})

    def test_three_valid_profiles_bind_exact_payload_bytes(self) -> None:
        self.assertEqual(len(VALID_CASES), 3)
        for case in VALID_CASES:
            with self.subTest(case=case["name"]), tempfile.TemporaryDirectory() as temporary:
                metadata, payload = materialize_case(case, Path(temporary))
                self.assertIsNotNone(payload)
                result = validate_artifact(metadata, payload)
                self.assertTrue(result.ok, result.findings)

    def test_schema_and_semantic_negative_cases_match_exact_codes(self) -> None:
        self.assertEqual(len(INVALID_CASES), 3)
        self.assertEqual(len(SEMANTIC_CASES), 8)
        for case in (*INVALID_CASES, *SEMANTIC_CASES):
            with self.subTest(case=case["name"]), tempfile.TemporaryDirectory() as temporary:
                metadata, _ = materialize_case(case, Path(temporary))
                result = validate_artifact(metadata)
                self.assertFalse(result.ok)
                self.assertEqual({finding.code for finding in result.findings}, set(case["expected_codes"]))

    def test_semantic_negative_cases_remain_schema_valid(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for case in SEMANTIC_CASES:
            with self.subTest(case=case["name"]):
                self.assertEqual(list(validator.iter_errors(case["metadata"])), [])

    def test_identity_and_storage_refs_are_digest_derived(self) -> None:
        metadata = copy.deepcopy(self.api_case["metadata"])
        metadata["artifact_id"] = "source-artifact:sha256:" + ("a" * 64)
        metadata["immutable_storage_ref"] = "cas:sha256:" + ("b" * 64)
        result = validate_artifact(self._write_metadata(metadata))
        self.assertEqual({finding.code for finding in result.findings}, {"ARTIFACT_ID_MISMATCH", "STORAGE_REF_MISMATCH"})

    def test_payload_digest_and_length_mismatch_fail_closed(self) -> None:
        self.payload_path.write_bytes(b"different synthetic bytes\n")
        result = validate_artifact(self.api_metadata, self.payload_path)
        self.assertEqual({finding.code for finding in result.findings}, {"PAYLOAD_DIGEST_MISMATCH", "PAYLOAD_LENGTH_MISMATCH"})

    def test_safe_locator_posture_rejects_credentials_query_fragment_and_control(self) -> None:
        cases = (
            "https://user:pass@example.invalid/official/records/1",
            "https://example.invalid/official/records/1?token=synthetic",
            "https://example.invalid/official/records/1#fragment",
            "https://example.invalid/official/records/1\\escape",
            "https://example.invalid/official/records/1%0aheader",
        )
        for value in cases:
            with self.subTest(value=value):
                metadata = copy.deepcopy(self.api_case["metadata"])
                metadata["source_locator"]["value"] = value
                kind = metadata["source_locator"]["kind"]
                metadata["source_locator"]["locator_digest"] = "sha256:" + hashlib.sha256(f"{kind}\n{value}".encode()).hexdigest()
                self.assertCode(self._write_metadata(metadata), "LOCATOR_UNSAFE")

    def test_temporal_rules_require_source_and_rights_not_after_retrieval(self) -> None:
        metadata = copy.deepcopy(self.api_case["metadata"])
        metadata["source_reported_at"] = "2026-08-04T08:00:01Z"
        metadata["rights_snapshot"]["captured_at"] = "2026-08-04T08:00:02Z"
        result = validate_artifact(self._write_metadata(metadata))
        self.assertEqual({finding.code for finding in result.findings}, {"RIGHTS_TIME_AFTER_RETRIEVAL", "SOURCE_TIME_AFTER_RETRIEVAL"})

    def test_conflict_and_supersession_lineage_are_fail_closed(self) -> None:
        metadata = copy.deepcopy(_case("valid_source_conflict_gis")["metadata"])
        metadata["lineage"]["conflict_group_ref"] = None
        self.assertCode(self._write_metadata(metadata), "CONFLICT_GROUP_REQUIRED")
        metadata = copy.deepcopy(self.api_case["metadata"])
        metadata["lineage"]["supersedes_artifact_ref"] = metadata["artifact_id"]
        metadata["lineage"]["correction_refs"] = ["correction:synthetic-001"]
        self.assertCode(self._write_metadata(metadata), "SELF_SUPERSESSION")
        metadata = copy.deepcopy(self.api_case["metadata"])
        metadata["lineage"]["supersedes_artifact_ref"] = "source-artifact:sha256:" + ("c" * 64)
        self.assertCode(self._write_metadata(metadata), "SUPERSESSION_CORRECTION_REQUIRED")

    def test_duplicate_nonfinite_complex_and_unsafe_inputs_fail_closed(self) -> None:
        text = self.api_metadata.read_text(encoding="utf-8")
        duplicate = text.replace('  "schema_version": "1.0.0",', '  "schema_version": "1.0.0",\n  "schema_version": "1.0.0",', 1)
        self.metadata_path.write_text(duplicate, encoding="utf-8")
        self.assertCode(self.metadata_path, "DUPLICATE_KEY")
        self.metadata_path.write_text('{"value": NaN}\n', encoding="utf-8")
        self.assertCode(self.metadata_path, "NONFINITE_NUMBER")
        nested = "[" * 100 + "0" + "]" * 100
        self.metadata_path.write_text('{"nested":' + nested + "}\n", encoding="utf-8")
        self.assertCode(self.metadata_path, "JSON_COMPLEXITY_LIMIT")
        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (MAX_METADATA_BYTES + 1))
        self.assertCode(oversized, "FILE_TOO_LARGE")
        linked = self.root / "linked.json"
        linked.symlink_to(self.api_metadata)
        self.assertCode(linked, "UNSAFE_FILE")
        if hasattr(os, "mkfifo"):
            fifo = self.root / "artifact.fifo"
            os.mkfifo(fifo)
            self.assertCode(fifo, "UNSAFE_FILE")

    def test_validation_performs_no_network_io(self) -> None:
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            result = validate_artifact(self.api_metadata, self.api_payload)
        self.assertTrue(result.ok, result.findings)

    def test_cli_output_is_deterministic_and_does_not_echo_candidate_values(self) -> None:
        metadata = copy.deepcopy(self.api_case["metadata"])
        secret_marker = "synthetic-sensitive-reference-marker"
        metadata["source_descriptor_ref"] = secret_marker
        metadata["governance"]["public_use_allowed"] = True
        path = self._write_metadata(metadata)
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

    def test_content_addressed_store_is_deterministic_and_detects_tampering(self) -> None:
        store_root = self.root / "store"
        first = store(self.api_metadata, self.api_payload, store_root)
        second = store(self.api_metadata, self.api_payload, store_root)
        self.assertEqual(first, second)
        self.assertEqual(first, object_path(store_root, self.api_case["metadata"]))
        self.assertEqual(verify(self.api_metadata, store_root), first)
        first.write_bytes(b"tampered\n")
        with self.assertRaisesRegex(ValueError, "do not match"):
            verify(self.api_metadata, store_root)


if __name__ == "__main__":
    unittest.main()
