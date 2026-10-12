"""Download integrity, selection budgets, and hostile archive boundaries."""
from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch
from urllib.request import Request

from tools.local_data import github_baseline as baseline


class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.parent = Path(self.temporary.name)
        self.destination = self.parent / "baseline"
        self.manifest_path = self.parent / "baseline-manifest.json"
        self.payloads = {}
        self.manifest = {"schema_version": 1, "release_tag": "curated-data-20261008",
                         "snapshot_utc": "2026-10-08T23:00:00Z", "status": baseline.STATUS,
                         "storage_cap_bytes": baseline.STORAGE_CAP, "datasets": [], "exclusions": ["backups"]}
        self.add_dataset("maps", [("maps/provider.csv", b"year,value\n2024,12\n")])

    def add_dataset(self, identifier, members):
        stream = io.BytesIO()
        files = size = 0
        with tarfile.open(fileobj=stream, mode="w:gz") as archive:
            for name, value in members:
                if isinstance(value, tarfile.TarInfo):
                    info = value
                    info.name = name
                    archive.addfile(info)
                else:
                    info = tarfile.TarInfo(name)
                    info.size = len(value)
                    archive.addfile(info, io.BytesIO(value))
                    files += 1
                    size += len(value)
        content = stream.getvalue()
        name = identifier + ".tar.gz"
        self.payloads[name] = content
        row = {"id": identifier, "title": identifier, "description": "Dated public source context",
               "source_urls": ["https://example.org/provider"], "license": "Public domain source",
               "files": files, "bytes": size, "install_subdir": identifier,
               "assets": [{"name": name, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest(),
                           "url": baseline.asset_url(self.manifest["release_tag"], name)}]}
        self.manifest["datasets"].append(row)
        self.save()
        return row

    def save(self):
        self.manifest_path.write_text(json.dumps(self.manifest))

    def fake_fetch(self, asset, destination):
        content = self.payloads[asset["name"]]
        self.assertEqual(len(content), asset["bytes"])
        self.assertEqual(hashlib.sha256(content).hexdigest(), asset["sha256"])
        destination.write_bytes(content)

    def download(self):
        self.save()
        value, digest = baseline.load_manifest(self.manifest_path)
        with patch.object(baseline, "fetch_asset", side_effect=self.fake_fetch):
            return baseline.download(value, digest, value["datasets"], self.destination, baseline.STORAGE_CAP)

    def test_plan_defaults_to_offline_read_only_and_lists_sizes_and_provenance(self):
        output = io.StringIO()
        with patch.object(baseline, "fetch_asset", side_effect=AssertionError("network")), contextlib.redirect_stdout(output):
            code = baseline.main(["--manifest", str(self.manifest_path)])
        self.assertEqual(code, 0)
        result = json.loads(output.getvalue())
        self.assertFalse(result["network"])
        self.assertFalse(result["writes"])
        self.assertEqual(result["expanded_bytes"], len(b"year,value\n2024,12\n"))
        self.assertIn("source_urls", result["datasets"][0])
        self.assertFalse(self.destination.exists())

    def test_download_requires_selection_and_budget_before_network(self):
        for extra in ([], ["--all"], ["--dataset", "unknown", "--max-bytes", "100000"]):
            with self.subTest(extra=extra), patch.object(baseline, "fetch_asset", side_effect=AssertionError("network")), contextlib.redirect_stderr(io.StringIO()):
                code = baseline.main(["download", "--manifest", str(self.manifest_path), "--directory", str(self.destination), *extra])
                self.assertEqual(code, 1)
                self.assertFalse(self.destination.exists())

    def test_budget_rejection_has_no_network_or_directory_effects(self):
        with patch.object(baseline, "fetch_asset", side_effect=AssertionError("network")):
            with self.assertRaisesRegex(baseline.BaselineError, "max-bytes"):
                baseline.download(self.manifest, "abc", self.manifest["datasets"], self.destination, 1)
        self.assertFalse(self.destination.exists())

    def test_success_extracts_selected_bytes_and_receipt_without_activation(self):
        result = self.download()
        self.assertEqual((self.destination / "maps/provider.csv").read_bytes(), b"year,value\n2024,12\n")
        self.assertFalse((self.destination / ".baseline-incomplete").exists())
        self.assertFalse(result["activation"])
        self.assertFalse(result["source_admission"])
        self.assertEqual(result["files"], 1)
        self.assertEqual(json.loads((self.destination / "baseline-install-receipt.json").read_text())["status"], baseline.STATUS)
        self.assertEqual(self.destination.stat().st_mode & 0o777, 0o700)

    def test_existing_directory_and_symlink_are_preserved_before_download(self):
        self.destination.mkdir()
        marker = self.destination / "mine"
        marker.write_text("preserved")
        with patch.object(baseline, "fetch_asset", side_effect=AssertionError("network")):
            with self.assertRaisesRegex(baseline.BaselineError, "already exists"):
                baseline.download(self.manifest, "abc", self.manifest["datasets"], self.destination, baseline.STORAGE_CAP)
        self.assertEqual(marker.read_text(), "preserved")
        link = self.parent / "linked"
        link.symlink_to(self.destination, target_is_directory=True)
        with self.assertRaises(OSError):
            with baseline.parent_directory(link / "new"):
                self.fail("followed a symlink")

    def test_manifest_rejects_arbitrary_urls_and_overlapping_destinations(self):
        for url in ("https://example.org/payload", "https://github.com/other/repo/releases/download/x/maps.tar.gz",
                    baseline.asset_url(self.manifest["release_tag"], "maps.tar.gz") + "?redirect=1"):
            altered = copy.deepcopy(self.manifest)
            altered["datasets"][0]["assets"][0]["url"] = url
            with self.subTest(url=url), self.assertRaisesRegex(baseline.BaselineError, "Asset URL"):
                baseline.validate_manifest(altered)
        duplicate = copy.deepcopy(self.manifest["datasets"][0])
        duplicate["id"] = "nested"
        duplicate["install_subdir"] = "maps/subdir"
        self.manifest["datasets"].append(duplicate)
        with self.assertRaisesRegex(baseline.BaselineError, "Overlapping"):
            baseline.validate_manifest(self.manifest)

    def test_redirects_allow_only_release_cdn(self):
        handler = baseline.ReleaseRedirects()
        request = Request(self.manifest["datasets"][0]["assets"][0]["url"])
        for url in ("http://release-assets.githubusercontent.com/file", "https://127.0.0.1/file",
                    "https://release-assets.githubusercontent.com.evil.test/file", "https://user@release-assets.githubusercontent.com/file"):
            with self.subTest(url=url), self.assertRaises(baseline.BaselineError):
                handler.redirect_request(request, None, 302, "Found", {}, url)
        redirected = handler.redirect_request(request, None, 302, "Found", {}, "https://release-assets.githubusercontent.com/file?signature=example")
        self.assertTrue(redirected.full_url.startswith("https://release-assets.githubusercontent.com/"))

    def test_archive_traversal_absolute_paths_links_and_duplicates_are_rejected_before_output(self):
        link = tarfile.TarInfo("ignored")
        link.type = tarfile.SYMTYPE
        link.linkname = "/etc/passwd"
        cases = [
            [("maps/../escape", b"x")], [("/maps/absolute", b"x")],
            [("maps\\escape", b"x")], [("other/data", b"x")],
            [("maps/link", link), ("maps/valid", b"x")],
            [("maps/duplicate", b"x"), ("maps/duplicate", b"y")],
            [("maps/directory/child", b"x"), ("maps/directory", b"y")],
            [("maps/file", b"x"), ("maps/file/child", b"y")],
        ]
        for members in cases:
            with self.subTest(members=members):
                self.manifest["datasets"] = []
                self.add_dataset("maps", members)
                with self.assertRaises(baseline.BaselineError):
                    self.download()
                self.assertFalse(self.destination.exists())

    def test_archive_expansion_and_file_count_mismatch_rejected_before_output(self):
        for field, change in (("bytes", 1), ("files", 2)):
            original = self.manifest["datasets"][0][field]
            self.manifest["datasets"][0][field] = change
            with self.subTest(field=field), self.assertRaises(baseline.BaselineError):
                self.download()
            self.assertFalse(self.destination.exists())
            self.manifest["datasets"][0][field] = original

    def test_network_size_and_digest_mismatch_rejected(self):
        class Response(io.BytesIO):
            status = 200
            headers = {}
        asset = self.manifest["datasets"][0]["assets"][0]
        original = self.payloads[asset["name"]]
        for content in (original[:-1], original + b"extra", bytes(len(original))):
            response = Response(content)
            with tempfile.TemporaryDirectory(dir=self.parent) as directory:
                with patch.object(baseline, "build_opener") as opener:
                    opener.return_value.open.return_value = response
                    with self.assertRaisesRegex(baseline.BaselineError, "(bytes|mismatch)"):
                        baseline.fetch_asset(asset, Path(directory) / "payload")

    def reassembly_fixture(self):
        self.manifest["datasets"] = []
        row = self.add_dataset("imagery", [("imagery/image.tif.part000", b"abcdef"), ("imagery/image.tif.part001", b"ghij")])
        row["reassemble"] = [{"path": "imagery/image.tif", "bytes": 10,
                              "sha256": hashlib.sha256(b"abcdefghij").hexdigest(),
                              "parts": ["imagery/image.tif.part000", "imagery/image.tif.part001"]}]
        return row

    def test_split_file_reassembles_exact_bytes_then_removes_only_parts(self):
        self.reassembly_fixture()
        result = self.download()
        self.assertEqual((self.destination / "imagery/image.tif").read_bytes(), b"abcdefghij")
        self.assertFalse((self.destination / "imagery/image.tif.part000").exists())
        self.assertEqual(result["files"], 2)
        self.assertEqual(result["installed_files"], 1)

    def test_failed_join_keeps_parts_and_marks_incomplete_install(self):
        row = self.reassembly_fixture()
        row["reassemble"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(baseline.BaselineError, "Reassembly size or SHA-256"):
            self.download()
        self.assertTrue((self.destination / ".baseline-incomplete").exists())
        self.assertEqual((self.destination / "imagery/image.tif.part000").read_bytes(), b"abcdef")
        self.assertFalse((self.destination / "baseline-install-receipt.json").exists())

    def test_join_budget_includes_extra_output_and_reused_parts_are_rejected(self):
        row = self.reassembly_fixture()
        result = baseline.plan(self.manifest, [row])
        self.assertEqual(result["reassembly_temporary_bytes"], 10)
        self.assertGreaterEqual(result["minimum_free_bytes"], result["download_bytes"] + 20)
        row["reassemble"][0]["parts"][1] = row["reassemble"][0]["parts"][0]
        with self.assertRaisesRegex(baseline.BaselineError, "reused"):
            baseline.validate_manifest(self.manifest)


if __name__ == "__main__":
    unittest.main()
