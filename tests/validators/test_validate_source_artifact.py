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

from tools.source_artifacts import content_addressed_store as cas
from tools.source_artifacts.content_addressed_store import object_path, store, verify
from tools.validators import validate_source_artifact as artifact_validator
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

    def test_store_keeps_validated_payload_when_source_changes(self) -> None:
        original = self.api_payload.read_bytes()
        ensure_safe_root = cas._ensure_safe_root
        for mutation in ("replace", "grow", "remove", "symlink"):
            with self.subTest(mutation=mutation):
                # Restore a regular source before each capture.
                self.api_payload.unlink(missing_ok=True)
                self.api_payload.write_bytes(original)
                store_root = self.root / f"store-{mutation}"

                def mutate_source(path: Path) -> None:
                    ensure_safe_root(path)
                    self.api_payload.unlink()
                    if mutation == "replace":
                        self.api_payload.write_bytes(b"x" * len(original))
                    elif mutation == "grow":
                        self.api_payload.write_bytes(original + b"unvalidated suffix")
                    elif mutation == "symlink":
                        replacement = self.root / "unvalidated-payload.bin"
                        replacement.write_bytes(b"unvalidated symlink bytes")
                        self.api_payload.symlink_to(replacement)

                with mock.patch.object(cas, "_ensure_safe_root", side_effect=mutate_source):
                    destination = store(self.api_metadata, self.api_payload, store_root)
                self.assertEqual(destination.read_bytes(), original)
                self.assertEqual(verify(self.api_metadata, store_root), destination)

    def test_store_keeps_metadata_identity_captured_by_strict_reader(self) -> None:
        original = self.api_payload.read_bytes()
        read_json_object = artifact_validator.read_json_object
        replacement = copy.deepcopy(self.api_case["metadata"])
        replacement_digest = "sha256:" + hashlib.sha256(b"replacement").hexdigest()
        replacement["content_digest"] = replacement_digest
        replacement["artifact_id"] = f"source-artifact:{replacement_digest}"
        replacement["immutable_storage_ref"] = f"cas:{replacement_digest}"
        replacement["byte_length"] = len(b"replacement")

        def mutate_metadata(path: Path):
            captured = read_json_object(path)
            path.write_text(json.dumps(replacement), encoding="utf-8")
            return captured

        store_root = self.root / "store"
        with mock.patch.object(artifact_validator, "read_json_object", side_effect=mutate_metadata):
            destination = store(self.api_metadata, self.api_payload, store_root)
        self.assertEqual(destination, object_path(store_root, self.api_case["metadata"]))
        self.assertEqual(destination.read_bytes(), original)
        self.assertFalse(object_path(store_root, replacement).exists())

    def test_store_never_reopens_validated_input_paths(self) -> None:
        read_bytes, read_text = Path.read_bytes, Path.read_text

        def reject_payload_reopen(path: Path):
            if path == self.api_payload:
                raise AssertionError("payload reopened after bounded validation")
            return read_bytes(path)

        def reject_metadata_reopen(path: Path, *args, **kwargs):
            if path == self.api_metadata:
                raise AssertionError("metadata reopened after strict validation")
            return read_text(path, *args, **kwargs)

        with (
            mock.patch.object(Path, "read_bytes", reject_payload_reopen),
            mock.patch.object(Path, "read_text", reject_metadata_reopen),
        ):
            destination = store(self.api_metadata, self.api_payload, self.root / "store")
        self.assertEqual(destination.read_bytes(), self.api_case["payload_text"].encode())

    def test_store_rejects_invalid_payload_before_creating_root(self) -> None:
        self.api_payload.write_bytes(b"unvalidated bytes")
        store_root = self.root / "store"
        with self.assertRaisesRegex(ValueError, "metadata/payload pair failed SourceArtifact validation"):
            store(self.api_metadata, self.api_payload, store_root)
        self.assertFalse(store_root.exists())

    def test_store_rejects_duplicate_metadata_before_creating_root(self) -> None:
        text = self.api_metadata.read_text(encoding="utf-8")
        self.api_metadata.write_text(text.replace("{", '{"schema_version":"1.0.0",', 1), encoding="utf-8")
        store_root = self.root / "store"
        with self.assertRaisesRegex(ValueError, "metadata/payload pair failed SourceArtifact validation"):
            store(self.api_metadata, self.api_payload, store_root)
        self.assertFalse(store_root.exists())

    def test_store_rejects_unreadable_unsafe_and_over_budget_payloads(self) -> None:
        original = self.api_payload.read_bytes()
        for kind in ("missing", "symlink", "over-budget"):
            with self.subTest(kind=kind):
                candidate = self.root / f"{kind}.bin"
                if kind == "symlink":
                    candidate.symlink_to(self.api_payload)
                elif kind == "over-budget":
                    candidate.write_bytes(original)
                store_root = self.root / f"store-{kind}"
                with mock.patch.object(artifact_validator, "MAX_PAYLOAD_BYTES", len(original) - 1):
                    with self.assertRaisesRegex(ValueError, "metadata/payload pair failed SourceArtifact validation"):
                        store(self.api_metadata, candidate, store_root)
                self.assertFalse(store_root.exists())

    def test_store_preserves_empty_payload_schema_rejection(self) -> None:
        metadata = copy.deepcopy(self.api_case["metadata"])
        digest = "sha256:" + hashlib.sha256(b"").hexdigest()
        metadata.update(content_digest=digest, artifact_id=f"source-artifact:{digest}",
                        immutable_storage_ref=f"cas:{digest}", byte_length=0)
        self.api_payload.write_bytes(b"")
        metadata_path = self._write_metadata(metadata)
        store_root = self.root / "store"
        with self.assertRaisesRegex(ValueError, "metadata/payload pair failed SourceArtifact validation"):
            store(metadata_path, self.api_payload, store_root)
        self.assertFalse(store_root.exists())

    def test_store_refuses_to_overwrite_existing_corrupt_object(self) -> None:
        store_root = self.root / "store"
        destination = store(self.api_metadata, self.api_payload, store_root)
        destination.write_bytes(b"existing corrupt bytes")
        with self.assertRaisesRegex(ValueError, "existing object bytes do not match digest identity"):
            store(self.api_metadata, self.api_payload, store_root)
        self.assertEqual(destination.read_bytes(), b"existing corrupt bytes")
        self.assertEqual(list(store_root.rglob("*.tmp-*")), [])

    def _containment_layout(self, name: str, level: str) -> tuple[Path, Path, Path]:
        base = self.root / name
        base.mkdir()
        store_root = base / "store"
        destination = object_path(store_root, self.api_case["metadata"])
        components = {
            "root": store_root,
            "algorithm": store_root / "sha256",
            "first-shard": destination.parent.parent,
            "second-shard": destination.parent,
        }
        if level == "ancestor":
            link = base / "root-link"
            store_root = link / "missing" / "store"
        else:
            link = components[level]
        link.parent.mkdir(parents=True, exist_ok=True)
        return store_root, link, base / "outside"

    def test_store_rejects_static_directory_symlinks_before_outside_mutation(self) -> None:
        for level in ("ancestor", "root", "algorithm", "first-shard", "second-shard"):
            with self.subTest(level=level):
                store_root, link, outside = self._containment_layout(f"linked-{level}", level)
                outside.mkdir()
                (outside / "sentinel").write_bytes(b"unchanged")
                link.symlink_to(outside, target_is_directory=True)
                with self.assertRaisesRegex(ValueError, "store"):
                    store(self.api_metadata, self.api_payload, store_root)
                self.assertEqual(sorted(p.relative_to(outside).as_posix() for p in outside.rglob("*")), ["sentinel"])
                self.assertEqual((outside / "sentinel").read_bytes(), b"unchanged")
                self.assertTrue(link.is_symlink())

    def test_store_rejects_dangling_directory_symlinks(self) -> None:
        for level in ("ancestor", "root", "algorithm", "first-shard", "second-shard"):
            with self.subTest(level=level):
                store_root, link, outside = self._containment_layout(f"dangling-{level}", level)
                link.symlink_to(outside, target_is_directory=True)
                with self.assertRaisesRegex(ValueError, "store"):
                    store(self.api_metadata, self.api_payload, store_root)
                self.assertTrue(link.is_symlink())
                self.assertFalse(outside.exists())

    def test_verify_rejects_static_directory_symlinks_before_payload_read(self) -> None:
        for level in ("ancestor", "root", "algorithm", "first-shard", "second-shard"):
            with self.subTest(level=level):
                store_root, link, outside = self._containment_layout(f"verify-{level}", level)
                destination = object_path(store_root, self.api_case["metadata"])
                external_object = outside / destination.relative_to(link)
                external_object.parent.mkdir(parents=True)
                external_object.write_bytes(self.api_payload.read_bytes())
                link.symlink_to(outside, target_is_directory=True)
                with mock.patch.object(Path, "read_bytes", side_effect=AssertionError("unsafe object read")):
                    with self.assertRaisesRegex(ValueError, "store"):
                        verify(self.api_metadata, store_root)
                self.assertEqual(external_object.read_bytes(), self.api_payload.read_bytes())

    def test_store_rejects_non_directory_components(self) -> None:
        for level in ("ancestor", "root", "algorithm", "first-shard", "second-shard"):
            with self.subTest(level=level):
                store_root, component, _ = self._containment_layout(f"file-{level}", level)
                component.write_bytes(b"not a directory")
                with self.assertRaisesRegex(ValueError, "store"):
                    store(self.api_metadata, self.api_payload, store_root)
                self.assertEqual(component.read_bytes(), b"not a directory")

    def test_store_refuses_dangling_object_symlink_without_replacing_it(self) -> None:
        store_root = self.root / "store"
        destination = object_path(store_root, self.api_case["metadata"])
        destination.parent.mkdir(parents=True)
        outside = self.root / "missing-outside-object"
        destination.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "unsafe"):
            store(self.api_metadata, self.api_payload, store_root)
        self.assertTrue(destination.is_symlink())
        self.assertFalse(outside.exists())
        self.assertEqual(list(store_root.rglob("*.tmp-*")), [])

    def test_object_identity_rejects_noncanonical_digest_before_directory_access(self) -> None:
        invalid_digests = (
            "sha256:" + "/" + "a" * 63,
            "sha256:" + "../" + "a" * 61,
            "sha256:" + "\\" + "a" * 63,
            "sha256:" + "A" * 64,
            "sha256:" + "g" * 64,
            "sha256:" + "a" * 63 + "\n",
            "sha256:" + "a" * 63,
            "sha256:" + "a" * 65,
        )
        for value in invalid_digests:
            with self.subTest(digest=value):
                metadata = copy.deepcopy(self.api_case["metadata"])
                metadata["content_digest"] = value
                path = self._write_metadata(metadata)
                with self.assertRaisesRegex(ValueError, "sha256 identity"):
                    object_path(self.root / "store", metadata)
                with mock.patch.object(Path, "lstat", side_effect=AssertionError("invalid identity reached filesystem")):
                    with self.assertRaisesRegex(ValueError, "sha256 identity"):
                        verify(path, self.root / "store")

    def test_store_cli_reports_finite_failure_for_symlink_escape(self) -> None:
        for command in ("store", "verify"):
            with self.subTest(command=command):
                store_root, link, outside = self._containment_layout(f"cli-{command}", "algorithm")
                destination = object_path(store_root, self.api_case["metadata"])
                external_object = outside / destination.relative_to(link)
                external_object.parent.mkdir(parents=True)
                external_object.write_bytes(self.api_payload.read_bytes())
                link.symlink_to(outside, target_is_directory=True)
                args = [command, str(self.api_metadata)]
                if command == "store":
                    args.append(str(self.api_payload))
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    code = cas.main([*args, str(store_root)])
                self.assertEqual(code, 1)
                result = json.loads(stream.getvalue())
                self.assertEqual(result["outcome"], "FAIL")
                self.assertNotIn("object_path", result)
                self.assertNotIn(str(outside), stream.getvalue())

    def test_verify_missing_store_is_read_only(self) -> None:
        store_root = self.root / "missing" / "store"
        with mock.patch.object(Path, "mkdir", side_effect=AssertionError("verify created directories")):
            with self.assertRaisesRegex(ValueError, "store|missing"):
                verify(self.api_metadata, store_root)
        self.assertFalse(store_root.parent.exists())

    def test_safe_nested_relative_store_roundtrip_remains_no_network(self) -> None:
        previous = Path.cwd()
        try:
            os.chdir(self.root)
            store_root = Path("relative") / "nested" / "store"
            with (
                mock.patch.object(socket.socket, "connect", _unexpected_network),
                mock.patch.object(socket, "create_connection", _unexpected_network),
                mock.patch.object(urllib.request, "urlopen", _unexpected_network),
            ):
                first = store(self.api_metadata, self.api_payload, store_root)
                self.assertFalse(first.is_absolute())
                self.assertEqual(store(self.api_metadata, self.api_payload, store_root), first)
                self.assertEqual(verify(self.api_metadata, store_root), first)
                self.assertEqual(first.read_bytes(), self.api_payload.read_bytes())
                self.assertEqual(list(store_root.rglob("*.tmp-*")), [])
        finally:
            os.chdir(previous)

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
