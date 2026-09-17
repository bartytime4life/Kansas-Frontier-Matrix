"""Behavioral checks for offline quarantine capture and safe retry."""

from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.local_data import manage
from tools.local_data.file_io import capture_file


class LocalDataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "store"
        self.downloads = self.base / "downloads"
        self.downloads.mkdir()
        self.manifest_path = self.base / "manifest.json"
        self.manifest = {"schema_version": "1", "items": [self.item("map.geojson", b'{"type":"FeatureCollection","features":[]}', "maps")]}
        self.save()

    def item(self, name, payload, dataset="maps", source="provider", version="v1"):
        path = self.downloads / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        return {"source_id": source, "dataset_id": dataset, "domain": "geology", "version": version, "relative_path": name, "source_uri": "https://example.org/data/" + name, "media_type": "application/octet-stream", "rights": {"license_id": None, "redistribution": "unknown"}, "sensitivity": "unknown", "sha256": hashlib.sha256(payload).hexdigest(), "size_bytes": len(payload), "captured_at": "2026-09-17T00:00:00Z"}

    def save(self):
        self.manifest_path.write_bytes(manage.canonical(self.manifest))

    def run_tool(self, command, *options):
        argv = [command, "--root", str(self.root)]
        if command != "init":
            argv += ["--manifest", str(self.manifest_path)]
        if command in {"plan", "sync"}:
            argv += ["--downloads", str(self.downloads)]
        argv += list(options)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = manage.main(argv)
        return code, json.loads(output.getvalue())

    def init(self):
        self.assertEqual(self.run_tool("init")[0], 0)

    def sync(self):
        self.init()
        code, result = self.run_tool("sync")
        self.assertEqual(code, 0, result)
        return result

    def test_init_private_layout_and_idempotence(self):
        self.init()
        self.assertEqual({p.name for p in (self.root / "data").iterdir()}, set(manage.LANES))
        if os.name == "posix":
            self.assertEqual(self.root.stat().st_mode & 0o777, 0o700)
        self.assertEqual(self.run_tool("init")[1]["outcome"], "NOOP")

    def test_plan_before_init_is_read_only_and_deterministic(self):
        first = self.run_tool("plan")
        self.assertEqual(first[0], 0, first)
        self.assertFalse(self.root.exists())
        self.assertEqual(first, self.run_tool("plan"))
        self.assertFalse(first[1]["writes"])

    def test_describe_outputs_valid_manifest_for_one_explicit_file(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = manage.main(["describe", "--downloads", str(self.downloads), "--file", "map.geojson", "--source-id", "provider", "--dataset-id", "maps", "--domain", "geology", "--version", "v1", "--source-uri", "https://example.org/maps", "--captured-at", "2026-09-17T00:00:00Z"])
        self.assertEqual(code, 0)
        described = json.loads(output.getvalue())
        from jsonschema import Draft202012Validator, FormatChecker
        schema = json.loads((manage.REPO_ROOT / "schemas/contracts/v1/source/local_data_manifest.schema.json").read_text())
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(described)
        self.assertEqual(described["items"][0]["sha256"], self.manifest["items"][0]["sha256"])
        self.assertEqual(described["items"][0]["rights"], {"license_id": None, "redistribution": "unknown"})
        self.assertEqual(described["items"][0]["sensitivity"], "unknown")
        self.assertFalse(self.root.exists())

    def test_sync_opaque_formats_and_schema_bound_receipts(self):
        self.manifest["items"].append(self.item("pictures/image.jpg", b"not decoded image bytes", "pictures", "photographer"))
        self.save()
        result = self.sync()
        self.assertEqual(result["captured_objects"], 2)
        self.assertEqual(result["lifecycle"], "QUARANTINE")
        from jsonschema import Draft202012Validator, FormatChecker
        schema = json.loads((manage.REPO_ROOT / "schemas/contracts/v1/source/ingest_receipt.schema.json").read_text())
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for item in self.manifest["items"]:
            self.assertEqual(manage.payload_path(self.root, item).read_bytes(), (self.downloads / item["relative_path"]).read_bytes())
            receipt = manage.receipt_path(self.root, item["source_id"], result["run_id"])
            validator.validate(json.loads(receipt.read_bytes()))
        for lane in set(manage.LANES) - {"quarantine", "receipts"}:
            self.assertEqual(list((self.root / "data" / lane).iterdir()), [])
        self.assertEqual(self.run_tool("verify")[1]["outcome"], "VERIFIED")

    def test_repeated_sync_skips_verified_bytes_even_after_download_removed(self):
        self.sync()
        (self.downloads / "map.geojson").unlink()
        with patch.object(manage, "capture_file", side_effect=AssertionError("must not recopy")):
            code, result = self.run_tool("sync")
        self.assertEqual(code, 0, result)
        self.assertEqual((result["outcome"], result["captured_objects"], result["reused_objects"]), ("NOOP", 0, 1))

    def test_new_version_retains_prior_payload_and_old_verification(self):
        self.sync()
        old = copy.deepcopy(self.manifest)
        old_path = manage.payload_path(self.root, old["items"][0])
        self.manifest["items"] = [self.item("map.geojson", b"new version", version="v2")]
        self.save()
        self.assertEqual(self.run_tool("sync")[0], 0)
        self.assertTrue(old_path.is_file())
        self.manifest = old
        self.save()
        self.assertEqual(self.run_tool("verify")[0], 0)

    def test_same_revision_cannot_change_bytes(self):
        self.sync()
        self.manifest["items"] = [self.item("map.geojson", b"changed bytes")]
        self.save()
        code, result = self.run_tool("sync")
        self.assertEqual(code, 1)
        self.assertEqual(result["code"], "CAPTURE_VERSION_CONFLICT_USE_NEW_VERSION")
        self.assertFalse(manage.payload_path(self.root, self.manifest["items"][0]).exists())

    def test_missing_receipt_and_snapshot_are_recreated_without_recopy(self):
        result = self.sync()
        receipt = manage.receipt_path(self.root, "provider", result["run_id"])
        snapshot = manage.manifest_path(self.root, "provider", result["run_id"])
        receipt.unlink()
        snapshot.unlink()
        self.assertEqual(self.run_tool("verify")[0], 1)
        with patch.object(manage, "capture_file", side_effect=AssertionError("must not recopy")):
            self.assertEqual(self.run_tool("sync")[0], 0)
        self.assertTrue(receipt.is_file())
        self.assertTrue(snapshot.is_file())
        self.assertEqual(self.run_tool("verify")[0], 0)

    def test_restored_multiple_source_store_verifies_from_preserved_full_manifest(self):
        self.manifest["items"].append(self.item("photo.jpg", b"image", "pictures", "photographer"))
        self.save()
        result = self.sync()
        restored = self.base / "restored"
        shutil.copytree(self.root, restored)
        self.root = restored
        self.manifest_path = manage.full_manifest_path(restored, result["run_id"])
        self.assertEqual(self.run_tool("verify")[0], 0)

    def test_interrupted_batch_preserves_verified_objects_and_retry_completes(self):
        self.manifest["items"].append(self.item("second.bin", b"second file", "second"))
        self.save()
        self.init()
        calls = 0
        original = manage.capture_file
        def fail_second(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated disk failure")
            return original(*args, **kwargs)
        with patch.object(manage, "capture_file", side_effect=fail_second):
            self.assertEqual(self.run_tool("sync")[0], 1)
        self.assertTrue(manage.payload_path(self.root, self.manifest["items"][0]).is_file())
        run = manage.run_id(self.manifest)
        receipt = manage.receipt_path(self.root, "provider", run)
        self.assertFalse(receipt.exists())
        attempts = list((receipt.parent / "attempts").glob("*.json"))
        self.assertEqual(len(attempts), 1)
        self.assertEqual(json.loads(attempts[0].read_bytes())["outcome"], "PARTIAL")
        code, result = self.run_tool("sync")
        self.assertEqual(code, 0, result)
        self.assertEqual((result["captured_objects"], result["reused_objects"]), (1, 1))
        self.assertTrue(attempts[0].exists())
        self.assertEqual(self.run_tool("verify")[0], 0)

    def test_corrupt_destination_is_reported_without_repair(self):
        self.sync()
        target = manage.payload_path(self.root, self.manifest["items"][0])
        corrupt = b"X" * target.stat().st_size
        target.write_bytes(corrupt)
        for command in ("plan", "sync", "verify"):
            code, result = self.run_tool(command)
            self.assertEqual(code, 1)
            self.assertEqual(result["code"], "STORED_PAYLOAD_CORRUPT")
            self.assertEqual(target.read_bytes(), corrupt)

    def test_corrupt_success_receipt_fails_without_overwrite(self):
        result = self.sync()
        path = manage.receipt_path(self.root, "provider", result["run_id"])
        path.write_bytes(b"{}")
        self.assertEqual(self.run_tool("sync")[1]["code"], "RECEIPT_INVALID")
        self.assertEqual(path.read_bytes(), b"{}")

    def test_wrong_input_digest_cannot_create_accepted_payload(self):
        self.init()
        self.manifest["items"][0]["sha256"] = "a" * 64
        self.save()
        self.assertEqual(self.run_tool("sync")[1]["code"], "INPUT_CHECKSUM_MISMATCH")
        self.assertEqual(list((self.root / "data/quarantine").iterdir()), [])

    def test_inputs_changing_between_preflight_and_capture_are_refused(self):
        self.init()
        original = manage.capture_file
        def change_input(source, *args, **kwargs):
            source.write_bytes(b"X" * source.stat().st_size)
            return original(source, *args, **kwargs)
        with patch.object(manage, "capture_file", side_effect=change_input):
            self.assertEqual(self.run_tool("sync")[0], 1)
        self.assertFalse(manage.payload_path(self.root, self.manifest["items"][0]).exists())
        self.assertEqual(list(self.root.rglob(".capture-*")), [])

    @unittest.skipUnless(hasattr(os, "symlink"), "requires symlinks")
    def test_input_symlink_and_ancestor_symlink_are_denied(self):
        original = self.downloads / "map.geojson"
        moved = self.base / "original"
        original.rename(moved)
        original.symlink_to(moved)
        self.assertEqual(self.run_tool("plan")[0], 1)
        original.unlink()
        directory = self.base / "outside"
        directory.mkdir()
        (directory / "map.geojson").write_bytes(moved.read_bytes())
        (self.downloads / "linked").symlink_to(directory, target_is_directory=True)
        self.manifest["items"][0]["relative_path"] = "linked/map.geojson"
        self.save()
        self.assertEqual(self.run_tool("plan")[1]["code"], "DIRECTORY_SYMLINK_OR_SPECIAL")

    @unittest.skipUnless(hasattr(os, "symlink"), "requires symlinks")
    def test_destination_ancestor_symlink_is_denied_without_outside_writes(self):
        self.init()
        outside = self.base / "outside"
        outside.mkdir()
        (self.root / "data/quarantine/provider").symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.run_tool("sync")[1]["code"], "DIRECTORY_SYMLINK_OR_SPECIAL")
        self.assertEqual(list(outside.iterdir()), [])

    def test_path_traversal_and_windows_paths_are_denied(self):
        for value in ("../secret", "/absolute", "a//b", "a/./b", "C:\\file", "foo:stream", "NUL", "foo/COM1.txt", "a."):
            with self.subTest(value=value):
                self.manifest["items"][0]["relative_path"] = value
                self.save()
                self.assertEqual(self.run_tool("plan")[1]["code"], "RELATIVE_PATH_UNSAFE")

    def test_duplicate_keys_nonfinite_unknown_and_empty_input_fail(self):
        for content in (b'{"schema_version":"1","schema_version":"1","items":[]}', b'{"schema_version":"1","items":NaN}', b'{"schema_version":"1","items":[],"extra":true}', b'{"schema_version":"1","items":[]}'):
            with self.subTest(content=content):
                self.manifest_path.write_bytes(content)
                self.assertEqual(self.run_tool("plan")[0], 1)
                self.assertFalse(self.root.exists())

    def test_item_file_batch_limits_and_bool_byte_count_fail(self):
        for flag in ("--max-file-bytes", "--max-total-bytes"):
            self.assertEqual(self.run_tool("plan", flag, "1")[0], 1)
        self.assertEqual(self.run_tool("plan", "--max-items", "1001")[1]["code"], "LIMIT_CONFIGURATION_INVALID")
        self.manifest["items"][0]["size_bytes"] = True
        self.save()
        self.assertEqual(self.run_tool("plan")[1]["code"], "FILE_BYTE_LIMIT")

    def test_low_disk_preflight_creates_no_capture(self):
        self.init()
        usage = type("Usage", (), {"free": 0})()
        with patch.object(manage.shutil, "disk_usage", return_value=usage):
            self.assertEqual(self.run_tool("sync")[1]["code"], "DISK_CAPACITY_INSUFFICIENT")
        self.assertEqual(list((self.root / "data/quarantine").iterdir()), [])

    def test_existing_lock_prevents_mutation_and_is_not_removed(self):
        self.init()
        lock = self.root / ".local-data.lock"
        lock.write_bytes(b"another writer")
        self.assertEqual(self.run_tool("sync")[1]["code"], "STORE_LOCKED")
        self.assertEqual(lock.read_bytes(), b"another writer")

    def test_root_inside_or_ancestor_of_repo_is_denied(self):
        for root in (manage.REPO_ROOT / "data/local", manage.REPO_ROOT.parent, Path("/")):
            with self.subTest(root=root), self.assertRaisesRegex(ValueError, "ROOT_MUST_BE_SEPARATE"):
                manage.external_root(str(root))

    def test_capture_commit_never_overwrites_existing_destination(self):
        item = self.manifest["items"][0]
        destination = self.base / "occupied"
        destination.write_bytes(b"preserved")
        with self.assertRaises(FileExistsError):
            capture_file(self.downloads / item["relative_path"], destination, sha256=item["sha256"], size_bytes=item["size_bytes"], max_bytes=1000)
        self.assertEqual(destination.read_bytes(), b"preserved")


if __name__ == "__main__":
    unittest.main()
