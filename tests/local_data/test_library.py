"""Metadata-only, bounded, nonblocking local library and HTTP contract tests."""
import io
import json
import os
from email.message import Message
from pathlib import Path
import tempfile
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from tools.local_data.earth_engine_downloads import handler, PORT
from tools.local_data.library import LocalLibrary, LibraryScanError, ScanLimits, scan_library
from tools.local_data.manage import init_store


class ScanTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "store"
        init_store(self.root)

    def tearDown(self): self.temporary.cleanup()

    def put(self, relative, value=b"data"):
        target = self.root / "data" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(value)
        return target

    def test_counts_all_four_lanes_without_payload_reads_or_private_names(self):
        self.put("raw/Weather/very-private-filename.bin", b"abc")
        self.put("raw/Weather/nested/other.bin", b"defgh")
        self.put("work/Review/context.json", b"{}")
        self.put("quarantine/Weather/payload", b"1234")
        self.put("processed/top-level.csv", b"12345")
        for excluded in ["work/earth-engine-downloads/credentials.json", "raw/Weather/.hidden/secret", "work/Review/runtime/token", "raw/Weather/credentials.json", "work/Review/.venv/package", "work/Review/node_modules/package"]:
            self.put(excluded, b"SECRET")
        with patch.object(Path, "read_bytes", side_effect=AssertionError("Payload read")), patch("builtins.open", side_effect=AssertionError("Payload read")):
            result = scan_library(self.root)
        self.assertEqual(result["totalFiles"], 5)
        self.assertEqual(result["totalBytes"], 19)
        self.assertEqual(len(result["entries"]), 4)
        self.assertEqual({row["lane"] for row in result["entries"]}, {"raw", "work", "quarantine", "processed"})
        self.assertNotIn("private-filename", json.dumps(result))
        self.assertNotIn(str(self.root), json.dumps(result))
        self.assertNotIn("SECRET", json.dumps(result))

    def test_symlink_directories_files_and_special_files_are_never_followed(self):
        outside = Path(self.temporary.name) / "outside"; outside.mkdir(); (outside / "secret").write_bytes(b"secret")
        link = self.root / "data/raw/linked"
        for target in [outside, outside / "secret"]:
            link.symlink_to(target)
            with self.assertRaisesRegex(LibraryScanError, "UNSAFE"): scan_library(self.root)
            link.unlink()
        os.mkfifo(link)
        with self.assertRaisesRegex(LibraryScanError, "UNSAFE"): scan_library(self.root)

    def test_symlink_root_ancestor_is_denied(self):
        link = Path(self.temporary.name) / "alias"; link.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(OSError): scan_library(link)

    def test_count_depth_collection_and_elapsed_limits_reject_partial_totals(self):
        self.put("raw/A/nested/payload")
        self.put("raw/B/payload")
        for limits in [ScanLimits(entries=1), ScanLimits(collections=1), ScanLimits(depth=0)]:
            with self.subTest(limits=limits), self.assertRaisesRegex(LibraryScanError, "LIMIT"):
                scan_library(self.root, limits=limits)
        with self.assertRaisesRegex(LibraryScanError, "LIMIT"):
            scan_library(self.root, limits=ScanLimits(seconds=1), clock=iter([0, 2]).__next__)

    def test_progress_is_reported_during_scan_without_exposing_file_names(self):
        for i in range(260): self.put(f"raw/Weather/{i:04}.bin", b"x")
        counts = []; scan_library(self.root, counts.append)
        self.assertGreater(len(counts), 2)
        self.assertGreater(counts[0], 0)
        self.assertLess(counts[0], 260)
        self.assertEqual(counts[-1], 260)

    def test_directory_changed_during_scan_never_reports_complete(self):
        for i in range(130): self.put(f"raw/Weather/{i:04}.bin", b"x")
        def progress(count):
            if count and not (self.root / "data/raw/Weather/added").exists(): self.put("raw/Weather/added")
        with self.assertRaisesRegex(LibraryScanError, "CHANGED"):
            scan_library(self.root, progress)


class BackgroundTests(unittest.TestCase):
    def test_first_get_is_nonblocking_refresh_coalesces_and_progress_is_observable(self):
        entered, release = threading.Event(), threading.Event(); calls = []
        def scan(_root, progress):
            calls.append(1); progress(7); entered.set(); release.wait(2)
            return {"entries": [], "totalFiles": 7, "totalBytes": 70}
        library = LocalLibrary(Path("/unused"), scan=scan)
        self.assertEqual(library.snapshot()["state"], "idle")
        self.assertEqual(library.snapshot(start=True)["state"], "scanning")
        self.assertTrue(entered.wait(1))
        try:
            for _ in range(5): self.assertEqual(library.refresh()["state"], "scanning")
            self.assertEqual(library.snapshot()["scannedFiles"], 7)
            self.assertEqual(calls, [1])
            self.assertIsNone(library.snapshot()["generatedAt"])
        finally: release.set(); library.thread.join(2)
        complete = library.snapshot(start=True)
        self.assertEqual(complete["state"], "complete")
        self.assertEqual(complete["totalBytes"], 70)
        self.assertIsNotNone(complete["generatedAt"])
        self.assertEqual(calls, [1], "polling cannot launch another completed scan")

    def test_previous_complete_snapshot_is_retained_during_refresh_and_failure(self):
        entry = {"id": "a" * 64, "label": "Weather", "lane": "raw", "files": 2, "bytes": 20, "role": "stored-candidate"}
        def complete(_root, progress):
            progress(2); return {"entries": [entry], "totalFiles": 2, "totalBytes": 20}
        library = LocalLibrary(Path("/unused"), scan=complete)
        library.refresh(); library.thread.join(2); old = library.snapshot()
        entered, release = threading.Event(), threading.Event()
        def failure(_root, progress):
            progress(1); entered.set(); release.wait(2); raise PermissionError("/secret/path")
        library.scan = failure; library.refresh(); self.assertTrue(entered.wait(1))
        try:
            during = library.snapshot()
            self.assertEqual(during["entries"], old["entries"])
            self.assertEqual(during["generatedAt"], old["generatedAt"])
        finally: release.set(); library.thread.join(2)
        failed = library.snapshot()
        self.assertEqual(failed["state"], "failed")
        self.assertEqual(failed["error"], "LIBRARY_SCAN_FAILED")
        self.assertNotIn("secret", json.dumps(failed))
        self.assertEqual(failed["totalBytes"], 20)
        failed["entries"][0]["bytes"] = 0
        self.assertEqual(library.snapshot()["entries"][0]["bytes"], 20, "callers cannot mutate the stored snapshot")


class HandlerTests(unittest.TestCase):
    def test_library_get_and_refresh_obey_exact_host_origin_session_and_empty_body(self):
        library = SimpleNamespace(snapshot=Mock(return_value={"state": "scanning"}), refresh=Mock(return_value={"state": "scanning"}))
        manager = SimpleNamespace(token="session", library=library, health=Mock(return_value={"idle": True}))
        Handler = handler(manager)
        def request(path, method="GET", overrides=None, value=None):
            body = json.dumps(value if value is not None else {}).encode()
            headers = {"Host": f"127.0.0.1:{PORT}", "Origin": "http://127.0.0.1:4173", "X-KFM-Session": "session",
                       "Content-Type": "application/json", "Content-Length": str(len(body)), **(overrides or {})}
            h = Handler.__new__(Handler); h.path = path; h.headers = Message()
            for key, v in headers.items(): h.headers[key] = v
            h.rfile = io.BytesIO(body); h.wfile = io.BytesIO(); h.connection = SimpleNamespace(settimeout=Mock())
            result = {}; h.send_response = lambda code: result.update(code=code); h.send_header = lambda *_: None; h.end_headers = lambda: None
            getattr(h, "do_" + method)(); return result["code"]
        for headers in [{"Host": "localhost:8769"}, {"Origin": "https://other.example"}]:
            self.assertEqual(request("/library", overrides=headers), 403)
        library.snapshot.assert_not_called()
        self.assertEqual(request("/library"), 200); library.snapshot.assert_called_once_with(start=True)
        self.assertEqual(request("/library?extra=true"), 404)
        self.assertEqual(request("/library/refresh", "POST", {"X-KFM-Session": "wrong"}), 403)
        self.assertEqual(request("/library/refresh", "POST", value={"root": "/outside"}), 400)
        library.refresh.assert_not_called()
        self.assertEqual(request("/library/refresh", "POST"), 200); library.refresh.assert_called_once_with()
        self.assertEqual(request("/status"), 200); manager.health.assert_called_once_with()


if __name__ == "__main__": unittest.main()

class PeriodLibraryTests(unittest.TestCase):
    setUp = ScanTests.setUp
    tearDown = ScanTests.tearDown
    put = ScanTests.put
    def test_earth_engine_periods_are_separate_without_payload_or_empty_download_claims(self):
        self.put('raw/earth-engine/ee-cdl/2024/job-a/tile.tif', b'1234')
        self.put('raw/earth-engine/ee-cdl/2024/job-b/tile.tif', b'12')
        self.put('raw/earth-engine/ee-cdl/2023/job-c/tile.tif', b'abc')
        (self.root/'data/raw/earth-engine/ee-3dep/fixed/empty').mkdir(parents=True)
        result=scan_library(self.root)
        self.assertEqual(result['totalFiles'],3)
        self.assertEqual(len(result['entries']),2)
        years={entry['period']:entry for entry in result['entries']}
        self.assertEqual(years['2024']['files'],2)
        self.assertEqual(years['2024']['bytes'],6)
        self.assertEqual(years['2023']['dataset'],'ee-cdl')
