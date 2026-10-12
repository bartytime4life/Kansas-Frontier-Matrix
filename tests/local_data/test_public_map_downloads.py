"""Deterministic transfer-boundary checks; no external downloads."""
import copy
import hashlib
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from tools.local_data.manage import init_store
from tools.local_data import public_map_downloads as downloads


URL = "https://www.kgs.ku.edu/General/Geology/test.pdf"
PAYLOAD = b"%PDF-1.7\nsynthetic source bytes\n"


def catalog(expected=len(PAYLOAD)):
    return {"schema": "kfm-public-map-catalog/v1", "generatedAt": "2026-10-08T00:00:00Z", "sourceUrls": [], "records": [{
        "id": "test-map", "sourceId": "synthetic", "title": "Synthetic map", "rights": {"status": "held"},
        "crs": None, "spatialAccuracy": None,
        "assets": [{"id": "test-pdf", "kind": "download", "availability": "verified", "format": "PDF",
                    "url": URL, "expectedBytes": expected}],
    }], "coverage": [{"sourceId": "synthetic", "state": "seed", "recordCount": 1, "discoveredCount": 0,
                       "seedReferenceCount": 1, "expectedCount": None, "reason": "Synthetic reference"}]}


class Response(io.BytesIO):
    def __init__(self, payload=PAYLOAD, *, length=True, url=URL, encoding=None):
        super().__init__(payload)
        self.status = 200
        self.url = url
        self.headers = {}
        if length:
            self.headers["Content-Length"] = str(len(payload))
        if encoding:
            self.headers["Content-Encoding"] = encoding

    def geturl(self):
        return self.url


class DownloadTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "store"
        init_store(self.root)
        self.seed = patch.object(downloads.public_map_catalog, "load_seed", side_effect=catalog)
        self.seed.start()
        self.manager = downloads.PublicMapDownloads(self.root)

    def tearDown(self):
        self.manager.close()
        self.seed.stop()
        self.temp.cleanup()

    def start(self, identifier="a" * 32, maximum=1024):
        with patch.object(downloads.threading, "Thread"):
            return self.manager.start({"requestId": identifier, "assetId": "test-pdf", "maxBytes": maximum})

    def run_job(self, response=None):
        job = self.start()
        with patch.object(downloads, "request_asset", return_value=response or Response()):
            self.manager.run(job["id"])
        return self.manager.jobs[job["id"]]

    def receipt(self, job):
        return json.loads((self.manager.receipts / (job["id"] + ".json")).read_bytes())

    def test_streamed_original_has_stored_hash_and_separate_unreviewed_receipt(self):
        job = self.run_job()
        self.assertEqual(job["state"], "downloaded")
        self.assertEqual((Path(job["destination"]) / "test.pdf").read_bytes(), PAYLOAD)
        self.assertEqual(job["sha256"], hashlib.sha256(PAYLOAD).hexdigest())
        self.assertFalse(job["mapReady"])
        self.assertIsNone(self.manager.health()["active"])
        receipt = self.receipt(job)
        self.assertEqual(receipt["admission"], "NOT_ADMITTED")
        self.assertEqual(receipt["review"], "UNREVIEWED")
        self.assertEqual(receipt["release"], "NOT_RELEASED")
        self.assertFalse(receipt["providerChecksumVerified"])
        self.assertEqual(receipt["files"][0]["sha256"], job["sha256"])
        self.assertEqual(json.loads((Path(job["destination"]) / "source.json").read_bytes())["record"]["rights"]["status"], "held")

    def test_card_summary_checks_presence_and_survives_recent_history_window(self):
        job = self.run_job()
        payload = Path(job["destination"]) / "test.pdf"
        def state():
            return next(row["state"] for row in self.manager.health()["assetStates"] if row["assetId"] == "test-pdf")
        self.assertEqual(state(), "downloaded")
        before = (self.manager.receipts / (job["id"] + ".json")).read_bytes()
        for i in range(120):
            identifier = f"{i:032x}"
            self.manager.jobs[identifier] = {**job, "id": identifier, "assetId": f"other-{i}", "state": "cancelled", "bytes": 0}
        self.assertNotIn(job["id"], [row["id"] for row in self.manager.health()["jobs"]])
        self.assertEqual(state(), "downloaded")
        # A failed retry does not hide an existing complete capture.
        self.manager.jobs["b" * 32] = {**job, "id": "b" * 32, "state": "failed", "bytes": 0}
        self.assertEqual(state(), "downloaded")
        payload.write_bytes(b"short")
        self.assertEqual(state(), "missing")
        payload.unlink()
        self.assertEqual(state(), "missing")
        payload.symlink_to(Path(job["destination"]) / "source.json")
        self.assertEqual(state(), "missing")
        self.assertEqual((self.manager.receipts / (job["id"] + ".json")).read_bytes(), before)

    def test_card_summary_does_not_confuse_reissued_publisher_files_with_prior_copies(self):
        job = self.run_job()
        self.manager._catalog["records"][0]["assets"][0]["url"] = URL.replace("test.pdf", "reissued.pdf")
        self.assertEqual(self.manager.health()["assetStates"][0]["state"], "outdated")
        self.manager._catalog["records"][0]["assets"][0]["url"] = URL
        self.assertEqual(self.manager.health()["assetStates"][0]["state"], "downloaded")
        self.manager._catalog["records"][0]["assets"][0]["expectedBytes"] = len(PAYLOAD) + 1
        self.assertEqual(self.manager.health()["assetStates"][0]["state"], "outdated")

    def test_card_summary_tracks_queue_and_partial_without_promoting_them(self):
        job = self.start()
        self.assertEqual(self.manager.health()["assetStates"], [{"assetId": "test-pdf", "state": "queued"}])
        self.manager.update(job["id"], state="downloading")
        self.assertEqual(self.manager.health()["assetStates"][0]["state"], "downloading")
        self.manager.update(job["id"], state="cancelled", bytes=12)
        self.assertEqual(self.manager.health()["assetStates"][0]["state"], "partial")
        self.manager.update(job["id"], bytes=0)
        self.assertEqual(self.manager.health()["assetStates"][0]["state"], "cancelled")

    def test_starts_are_idempotent_and_single_concurrency_without_ee_configuration(self):
        first = self.start()
        self.assertEqual(self.manager.start({"requestId": first["id"], "assetId": "test-pdf", "maxBytes": 1024}), first)
        with self.assertRaisesRegex(ValueError, "REQUEST_ID_CONFLICT"):
            self.manager.start({"requestId": first["id"], "assetId": "test-pdf", "maxBytes": 2048})
        with self.assertRaisesRegex(ValueError, "DOWNLOAD_ALREADY_RUNNING"):
            self.start("b" * 32)
        self.assertNotIn("configured", self.manager.health())

    def test_provider_checksum_uses_pinned_metadata_without_claiming_verification(self):
        checksum = {"algorithm": "MD5", "value": "1" * 32}
        self.manager._catalog["records"][0]["assets"][0]["providerChecksum"] = copy.deepcopy(checksum)
        job = self.start()
        self.manager._catalog["records"][0]["assets"][0]["providerChecksum"]["value"] = "2" * 32
        with patch.object(downloads, "request_asset", return_value=Response()):
            self.manager.run(job["id"])
        receipt = self.receipt(job)
        self.assertEqual(receipt["providerChecksum"], checksum)
        self.assertFalse(receipt["providerChecksumVerified"])
        self.assertEqual(receipt["files"][0]["sha256"], hashlib.sha256(PAYLOAD).hexdigest())

    def test_invalid_bounds_ids_extra_urls_and_unverified_assets_are_rejected_before_io(self):
        good = {"requestId": "a" * 32, "assetId": "test-pdf", "maxBytes": 1024}
        for changes in ({"maxBytes": True}, {"maxBytes": 0}, {"maxBytes": downloads.MAX_BYTES + 1},
                        {"requestId": "../escape"}, {"assetId": "../escape"}, {"url": URL}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.manager.start({**good, **changes})
        for changes in ({"kind": "service"}, {"kind": "request"}, {"availability": "unverified"},
                        {"url": "https://localhost/test.pdf"}, {"format": "HTML"}):
            self.manager._catalog = catalog()
            self.manager._catalog["records"][0]["assets"][0].update(changes)
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.manager.start(good)
        self.assertEqual(self.manager.jobs, {})

    def test_source_changed_length_and_encoding_are_rejected(self):
        for response, reason in [(Response(PAYLOAD + b"x"), "ASSET_SIZE_CHANGED"),
                                 (Response(encoding="gzip"), "ASSET_CONTENT_ENCODING_REJECTED"),
                                 (Response(url="https://other.example/a.pdf"), "ASSET_REDIRECT_DENIED")]:
            with self.subTest(reason=reason):
                identifier = str(len(self.manager.jobs) + 1) * 32
                job = self.start(identifier)
                with patch.object(downloads, "request_asset", return_value=response):
                    self.manager.run(job["id"])
                self.assertEqual(self.manager.jobs[job["id"]]["reason"], reason)
                self.assertFalse((Path(job["destination"]) / "test.pdf").exists())

    def test_non_map_and_truncated_body_fail_with_partial_receipt(self):
        bad = Response(b"<html>denied</html>")
        bad.headers["Content-Length"] = str(len(PAYLOAD))
        job = self.run_job(bad)
        self.assertEqual(job["reason"], "ASSET_FORMAT_MISMATCH")
        self.assertEqual(self.receipt(job)["job"]["state"], "failed")
        truncated = Response(PAYLOAD[:10])
        truncated.headers["Content-Length"] = str(len(PAYLOAD))
        next_job = self.start("b" * 32)
        with patch.object(downloads, "request_asset", return_value=truncated):
            self.manager.run(next_job["id"])
        actual = self.manager.jobs[next_job["id"]]
        self.assertEqual(actual["reason"], "ASSET_TRUNCATED_OR_SIZE_CHANGED")
        self.assertEqual(actual["bytes"], 10)
        self.assertTrue((Path(actual["destination"]) / "test.pdf.part").is_file())

    def test_unknown_length_is_bounded_without_writing_over_limit(self):
        self.manager._catalog = catalog(expected=None)
        job = self.start(maximum=10)
        with patch.object(downloads, "request_asset", return_value=Response(length=False)):
            self.manager.run(job["id"])
        actual = self.manager.jobs[job["id"]]
        self.assertEqual(actual["reason"], "ASSET_EXCEEDS_SELECTED_LIMIT")
        self.assertLessEqual(actual["bytes"], 10)

    def test_cancellation_preserves_partial_bytes_and_never_promotes_them(self):
        job = self.start()
        response = Response()
        original_read = response.read

        def cancel_after_read(size):
            value = original_read(min(size, 8))
            self.manager.cancel_event.set()
            return value

        response.read = cancel_after_read
        with patch.object(downloads, "request_asset", return_value=response):
            self.manager.run(job["id"])
        actual = self.manager.jobs[job["id"]]
        self.assertEqual(actual["state"], "cancelled")
        self.assertEqual((Path(job["destination"]) / "test.pdf.part").read_bytes(), PAYLOAD[:8])
        self.assertFalse((Path(job["destination"]) / "test.pdf").exists())
        self.assertEqual(self.receipt(actual)["files"][0]["sha256"], hashlib.sha256(PAYLOAD[:8]).hexdigest())

    def test_restart_records_interruption_and_preserves_receipt_on_repeated_restart(self):
        job = self.start()
        part = Path(job["destination"]) / "test.pdf.part"
        part.write_bytes(PAYLOAD[:10])
        restored = downloads.PublicMapDownloads(self.root)
        self.assertEqual(restored.jobs[job["id"]]["state"], "interrupted")
        self.assertEqual(restored.jobs[job["id"]]["bytes"], 10)
        receipt = (restored.receipts / (job["id"] + ".json")).read_bytes()
        downloads.PublicMapDownloads(self.root)
        self.assertEqual((restored.receipts / (job["id"] + ".json")).read_bytes(), receipt)
        self.assertEqual(part.read_bytes(), PAYLOAD[:10])

    def test_restart_repairs_receipt_gap_after_terminal_state_was_saved(self):
        for index, state in enumerate(["downloaded", "cancelled", "failed", "interrupted"], 1):
            job = self.start(str(index) * 32)
            name = "test.pdf" if state == "downloaded" else "test.pdf.part"
            (Path(job["destination"]) / name).write_bytes(PAYLOAD)
            self.manager.update(job["id"], state=state, bytes=len(PAYLOAD), sha256=hashlib.sha256(PAYLOAD).hexdigest())
            self.manager.active = None
        restored = downloads.PublicMapDownloads(self.root)
        for job in restored.jobs.values():
            self.assertTrue((restored.receipts / (job["id"] + ".json")).is_file())
            self.assertEqual(self.receipt(job)["job"]["state"], job["state"])

    def test_receipt_recovery_rejects_changed_bytes_after_downloaded_state(self):
        job = self.start()
        (Path(job["destination"]) / "test.pdf").write_bytes(PAYLOAD + b"changed")
        self.manager.update(job["id"], state="downloaded", bytes=len(PAYLOAD), sha256=hashlib.sha256(PAYLOAD).hexdigest())
        restored = downloads.PublicMapDownloads(self.root)
        actual = restored.jobs[job["id"]]
        self.assertEqual(actual["state"], "failed")
        self.assertEqual(actual["reason"], "STORED_BYTES_CHANGED")
        self.assertFalse(self.receipt(actual)["files"][0]["complete"])

    def test_source_metadata_and_thread_start_failures_do_not_leave_queued_jobs(self):
        original_write = downloads.write_new

        def fail_source(path, content):
            if path.name == "source.json":
                raise OSError("synthetic disk failure")
            original_write(path, content)

        with patch.object(downloads, "write_new", side_effect=fail_source), self.assertRaisesRegex(ValueError, "PUBLIC_MAP_START_FAILED"):
            self.start()
        failed = self.manager.jobs["a" * 32]
        self.assertEqual(failed["state"], "failed")
        self.assertEqual(self.receipt(failed)["job"]["state"], "failed")
        with patch.object(downloads.threading, "Thread") as thread:
            thread.return_value.start.side_effect = RuntimeError("synthetic thread failure")
            with self.assertRaisesRegex(ValueError, "PUBLIC_MAP_START_FAILED"):
                self.manager.start({"requestId": "b" * 32, "assetId": "test-pdf", "maxBytes": 1024})
        self.assertIsNone(self.manager.active)
        self.assertEqual(self.manager.jobs["b" * 32]["state"], "failed")

    def test_existing_raw_path_and_symlink_are_not_overwritten(self):
        parent = self.manager.raw / "test-map"
        parent.mkdir(mode=0o700)
        elsewhere = self.root / "elsewhere"
        elsewhere.mkdir()
        (parent / ("a" * 32)).symlink_to(elsewhere, target_is_directory=True)
        with self.assertRaises(FileExistsError):
            self.start()
        self.assertEqual(list(elsewhere.iterdir()), [])

    def test_free_space_reserve_checked_before_job_and_during_stream(self):
        with patch.object(downloads.shutil, "disk_usage", return_value=SimpleNamespace(free=0)):
            with self.assertRaisesRegex(ValueError, "INSUFFICIENT_FREE_SPACE"):
                self.start()
        job = self.start()
        with patch.object(downloads, "request_asset", return_value=Response()), \
             patch.object(downloads.shutil, "disk_usage", return_value=SimpleNamespace(free=downloads.RESERVE_BYTES)):
            self.manager.run(job["id"])
        self.assertEqual(self.manager.jobs[job["id"]]["reason"], "DISK_SPACE_LOW")

    def test_bad_redirect_is_rejected_before_follow(self):
        with self.assertRaisesRegex(ValueError, "REDIRECT_DENIED"):
            downloads.NoRedirect().redirect_request(None, None, 302, "", {}, "http://127.0.0.1/private")
        for url in ["http://www.kgs.ku.edu/General/Geology/a.pdf", "https://www.kgs.ku.edu.evil/General/Geology/a.pdf",
                    "https://www.kgs.ku.edu/General/Geology/../a.pdf", "https://www.kgs.ku.edu/General/Geology/%2e%2e/a.pdf",
                    "https://www.kgs.ku.edu:443/General/Geology/a.pdf", "https://www.kgs.ku.edu/General/Geology/a.pdf?token=x"]:
            with self.subTest(url=url), self.assertRaises(ValueError):
                downloads.validate_url(url)

    def test_nmmr_scene_rule_is_allowlisted_without_promoting_unverified_links(self):
        for url in ["https://mmr.osmre.gov/images/00004200_web.jpg", "https://mmr.osmre.gov/images/100004201_web.jpg"]:
            self.assertEqual(downloads.validate_url(url), url)
        for url in ["https://mmr.osmre.gov/images/arbitrary.jpg", "https://mmr.osmre.gov/images/00004200.tif",
                    "https://mmr.osmre.gov/Request", "https://mmr.osmre.gov/images/00004200_web.jpg?download=1"]:
            with self.subTest(url=url), self.assertRaises(ValueError):
                downloads.validate_url(url)
        asset = self.manager._catalog["records"][0]["assets"][0]
        asset.update(url="https://mmr.osmre.gov/images/00004200_web.jpg", format="JPEG", availability="unverified")
        with self.assertRaisesRegex(ValueError, "ASSET_NOT_VERIFIED_DOWNLOAD"):
            self.start()

    def test_sciencebase_allows_only_four_pinned_query_urls_and_original_names(self):
        for url, filename in downloads.SCIENCEBASE_FILES.items():
            self.assertEqual(downloads.validate_url(url), url)
            for changed in (url + "&allowOpen=true", url + "#x", url.replace("%2F", "/"),
                            url.replace("?f=", "?other="), url.replace("sciencebase.gov", "sciencebase.gov.evil"),
                            url.replace("__disk__", "__disk__00"), url.replace("https:", "http:")):
                with self.subTest(url=changed), self.assertRaises(ValueError):
                    downloads.validate_url(changed)
            payload = b"PK\x03\x04synthetic archive bytes"
            self.manager._catalog = catalog(expected=len(payload))
            self.manager._catalog["records"][0]["assets"][0].update(url=url, format="ZIP")
            job = self.start(str(len(self.manager.jobs) + 1) * 32)
            with patch.object(downloads, "request_asset", return_value=Response(payload, url=url)):
                self.manager.run(job["id"])
            self.assertEqual(self.manager.jobs[job["id"]]["state"], "downloaded")
            self.assertEqual((Path(job["destination"]) / filename).read_bytes(), payload)

    def test_catalog_refresh_is_bounded_and_keeps_prior_on_discovery_failure(self):
        previous = self.manager.catalog()
        with patch.object(downloads.public_map_catalog, "discover_catalog", side_effect=ValueError("UPSTREAM_UNAVAILABLE")):
            self.manager._refresh()
        self.assertEqual(self.manager.catalog(), previous)
        self.assertEqual(self.manager.health()["refresh"], {"state": "failed", "reason": "UPSTREAM_UNAVAILABLE"})
        changed = copy.deepcopy(previous)
        changed["coverage"][0].update(state="partial", reason="bounded")
        with patch.object(downloads.public_map_catalog, "discover_catalog", return_value=changed):
            self.manager._refresh()
        self.assertEqual(self.manager.catalog(), changed)
        restored = downloads.PublicMapDownloads(self.root)
        self.assertEqual(restored.catalog(), changed)

    def test_cngm_allows_only_four_exact_publisher_queries_and_safe_local_names(self):
        self.assertEqual(len(downloads.NGMDB_FILES), 4)
        for url, filename in downloads.NGMDB_FILES.items():
            self.assertEqual(downloads.validate_url(url), url)
            for changed in (url + "&download=1", url + "#x", url.replace("id=", "file="),
                            url.replace("pid=118545", "pid=118546"), url.replace("https:", "http:"),
                            url.replace("ngmdb.usgs.gov", "ngmdb.usgs.gov.evil"),
                            url.replace("?id=", "?pid=118545&id=").replace("&pid=118545", "")):
                with self.subTest(url=changed), self.assertRaises(ValueError):
                    downloads.validate_url(changed)
            payload = b"PK\x03\x04synthetic national archive bytes"
            self.manager._catalog = catalog(expected=len(payload))
            self.manager._catalog["records"][0]["assets"][0].update(url=url, format="ZIP")
            job = self.start(str(len(self.manager.jobs) + 1) * 32)
            with patch.object(downloads, "request_asset", return_value=Response(payload, url=url)):
                self.manager.run(job["id"])
            self.assertEqual(self.manager.jobs[job["id"]]["state"], "downloaded")
            self.assertEqual((Path(job["destination"]) / filename).read_bytes(), payload)

    def test_saved_catalog_gets_new_curated_assets_without_new_discovery_claim(self):
        saved = catalog()
        saved["records"][0]["assets"] = []
        (self.manager.work / "catalog.json").write_text(json.dumps(saved))
        restored = downloads.PublicMapDownloads(self.root)
        merged = restored.catalog()
        self.assertEqual(merged["records"][0]["assets"], catalog()["records"][0]["assets"])
        self.assertEqual(merged["generatedAt"], saved["generatedAt"])
        self.assertFalse(merged["seedAugmentation"]["discoveryRefreshed"])

    def test_stream_exceeds_candidate_buffer_cap_without_unbounded_reads(self):
        size = 33 * 1024 * 1024
        self.manager._catalog = catalog(expected=size)

        class LargeResponse:
            status = 200
            headers = {"Content-Length": str(size)}

            def __init__(self):
                self.remaining = size
                self.maximum_read = 0

            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

            def geturl(self):
                return URL

            def read(self, bound):
                self.maximum_read = max(self.maximum_read, bound)
                count = min(bound, self.remaining)
                first = self.remaining == size
                self.remaining -= count
                return (b"%PDF-1.7" + b"x" * (count - 8)) if first else b"x" * count

        response = LargeResponse()
        job = self.start(maximum=size)
        with patch.object(downloads, "request_asset", return_value=response):
            self.manager.run(job["id"])
        self.assertEqual(self.manager.jobs[job["id"]]["state"], "downloaded")
        self.assertEqual(self.manager.jobs[job["id"]]["bytes"], size)
        self.assertLessEqual(response.maximum_read, downloads.CHUNK_BYTES)
        self.assertEqual((Path(job["destination"]) / "test.pdf").stat().st_size, size)


class StormEventsDownloadTests(unittest.TestCase):
    """A discovered Storm Events year downloads through the same bounded transfer."""

    def setUp(self):
        from tools.local_data import public_map_catalog
        self.name = "StormEvents_details-ftp_v1.0_d2024_c20250401.csv.gz"
        self.payload = b"\x1f\x8b\x08\x00" + b"synthetic gzip member" * 8
        record = public_map_catalog.storm_events_record(2024, {"details": self.name}, "2026-10-09")
        seed = catalog()
        seed["records"].append(record)
        seed["coverage"].append({"sourceId": record["sourceId"], "state": "complete", "recordCount": 1, "discoveredCount": 1,
                                 "seedReferenceCount": 0, "expectedCount": 1, "reason": "Synthetic listing"})
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "store"
        init_store(self.root)
        self.seed = patch.object(downloads.public_map_catalog, "load_seed", return_value=seed)
        self.seed.start()
        self.manager = downloads.PublicMapDownloads(self.root)
        self.url = record["assets"][0]["url"]

    def tearDown(self):
        self.manager.close()
        self.seed.stop()
        self.temp.cleanup()

    def run_storm(self, payload):
        with patch.object(downloads.threading, "Thread"):
            job = self.manager.start({"requestId": "b" * 32, "assetId": "publisher-noaa-storm-events-2024-details", "maxBytes": 4096})
        with patch.object(downloads, "request_asset", return_value=Response(payload, url=self.url)):
            self.manager.run(job["id"])
        return self.manager.jobs[job["id"]]

    def test_gzip_original_is_stored_under_its_ncei_name(self):
        job = self.run_storm(self.payload)
        self.assertEqual(job["state"], "downloaded")
        self.assertEqual((Path(job["destination"]) / self.name).read_bytes(), self.payload)
        self.assertEqual(job["sha256"], hashlib.sha256(self.payload).hexdigest())

    def test_html_error_page_in_place_of_gzip_fails_closed(self):
        job = self.run_storm(b"<!DOCTYPE html><title>Not Found</title>")
        self.assertEqual((job["state"], job["reason"]), ("failed", "ASSET_FORMAT_MISMATCH"))


class QueueTests(unittest.TestCase):
    """Several verified files download one after another without an idle gap."""

    def setUp(self):
        from tools.local_data import public_map_catalog
        seed = catalog()
        for year in (2022, 2023, 2024):
            record = public_map_catalog.storm_events_record(year, {"details": f"StormEvents_details-ftp_v1.0_d{year}_c20250401.csv.gz"}, "2026-10-09")
            seed["records"].append(record)
        seed["coverage"].append({"sourceId": "publisher-noaa-storm-events", "state": "complete", "recordCount": 3, "discoveredCount": 3,
                                 "seedReferenceCount": 0, "expectedCount": 3, "reason": "Synthetic listing"})
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "store"
        init_store(self.root)
        self.seed = patch.object(downloads.public_map_catalog, "load_seed", return_value=seed)
        self.seed.start()
        self.threads = patch.object(downloads.threading, "Thread")
        self.threads.start()
        self.manager = downloads.PublicMapDownloads(self.root)
        self.assets = [f"publisher-noaa-storm-events-{year}-details" for year in (2022, 2023, 2024)]

    def tearDown(self):
        self.threads.stop()
        self.manager.close()
        self.seed.stop()
        self.temp.cleanup()

    def enqueue(self, assets=None, maximum=4096, request="c" * 32):
        return self.manager.enqueue({"requestId": request, "assetIds": self.assets if assets is None else assets, "maxBytes": maximum})

    def finish_active(self):
        active = self.manager.active
        url = downloads.public_map_catalog.STORM_EVENTS + json.loads((Path(self.manager.jobs[active]["destination"]) / "source.json").read_text())["asset"]["title"]
        with patch.object(downloads, "request_asset", return_value=Response(b"\x1f\x8b\x08\x00 gzip", url=url)):
            self.manager.run(active)
        return active

    def test_files_run_in_order_and_the_queue_is_reported_as_a_count(self):
        summary = self.enqueue()
        self.assertEqual((summary["jobs"], summary["queued"]), (3, 2))
        health = self.manager.health()
        self.assertEqual(health["queued"], 2)
        self.assertEqual([job["id"] for job in health["jobs"]], [self.manager.active])
        finished = [self.finish_active(), self.finish_active(), self.finish_active()]
        self.assertEqual([self.manager.jobs[i]["assetId"] for i in finished], self.assets)
        self.assertTrue(all(self.manager.jobs[i]["state"] == "downloaded" for i in finished))
        self.assertIsNone(self.manager.active)
        self.assertEqual(self.manager.health()["queued"], 0)

    def test_a_retried_queue_request_is_idempotent_and_blocks_other_starts(self):
        first = self.enqueue()
        self.assertEqual(self.enqueue(), first)
        with self.assertRaisesRegex(ValueError, "REQUEST_ID_CONFLICT"):
            self.enqueue(maximum=8192)
        with self.assertRaisesRegex(ValueError, "DOWNLOAD_ALREADY_RUNNING"):
            self.manager.start({"requestId": "d" * 32, "assetId": "test-pdf", "maxBytes": 1024})
        with self.assertRaisesRegex(ValueError, "DOWNLOAD_ALREADY_RUNNING"):
            self.enqueue(request="e" * 32)

    def test_jobs_from_a_record_with_several_files_name_their_file(self):
        from tools.local_data import public_map_catalog
        seed = downloads.public_map_catalog.load_seed()
        seed["records"].append(public_map_catalog.storm_events_record(2021, {kind: f"StormEvents_{kind}-ftp_v1.0_d2021_c20250401.csv.gz" for kind in ("details", "fatalities")}, "2026-10-09"))
        self.manager._catalog = seed
        self.enqueue(assets=["publisher-noaa-storm-events-2021-details", "publisher-noaa-storm-events-2021-fatalities"])
        titles = sorted(job["title"] for job in self.manager.jobs.values())
        self.assertEqual(titles, ["Storm Events 2021 · national CSV files including Kansas · StormEvents_details-ftp_v1.0_d2021_c20250401.csv.gz",
                                  "Storm Events 2021 · national CSV files including Kansas · StormEvents_fatalities-ftp_v1.0_d2021_c20250401.csv.gz"])

    def test_a_record_with_one_file_and_a_service_keeps_its_title(self):
        seed = downloads.public_map_catalog.load_seed()
        record = copy.deepcopy(next(r for r in seed["records"] if r["id"] == "publisher-noaa-storm-events-2022"))
        record["id"] = "map-with-service"
        record["assets"][0]["id"] = "map-with-service-file"
        record["assets"].append({"id": "map-with-service-wms", "title": "WMS", "kind": "service", "availability": "verified",
                                 "format": "WMS", "url": "https://example.invalid/wms", "expectedBytes": None})
        seed["records"].append(record)
        self.manager._catalog = seed
        with patch.object(downloads, "validate_url"):
            job = self.manager.start({"requestId": "f" * 32, "assetId": "map-with-service-file", "maxBytes": 4096})
        self.assertEqual(job["title"], record["title"])

    def test_an_identical_retry_after_a_restart_returns_the_same_queue(self):
        assets = list(reversed(self.assets))
        first = self.enqueue(assets=assets)
        self.manager.close()
        self.manager = downloads.PublicMapDownloads(self.root)
        retried = self.enqueue(assets=assets)
        self.assertEqual((retried["batchId"], retried["jobs"]), (first["batchId"], 3))
        with self.assertRaisesRegex(ValueError, "REQUEST_ID_CONFLICT"):
            self.enqueue(assets=self.assets)

    def test_the_idle_status_window_holds_one_hundred_jobs(self):
        for index in range(101):
            identifier = f"{index:032x}"
            self.manager.jobs[identifier] = {"id": identifier, "assetId": f"test-{index}", "state": "cancelled", "bytes": 0}
        self.assertIsNone(self.manager.active)
        self.assertEqual(len(self.manager.health()["jobs"]), 100)

    def test_a_request_id_names_one_exact_ordered_selection(self):
        self.enqueue()
        for changed in (self.assets[:2], list(reversed(self.assets)), [self.assets[0]]):
            with self.assertRaisesRegex(ValueError, "REQUEST_ID_CONFLICT"):
                self.enqueue(assets=changed)
        self.assertEqual(sum(bool(job.get("batchId")) for job in self.manager.jobs.values()), 3)

    def test_the_queue_reserves_disk_space_for_every_file(self):
        usage = SimpleNamespace(free=downloads.RESERVE_BYTES + 2 * 4096)
        with patch.object(downloads.shutil, "disk_usage", return_value=usage):
            with self.assertRaisesRegex(ValueError, "INSUFFICIENT_FREE_SPACE_FOR_LIMIT"):
                self.enqueue()
            self.assertEqual(self.manager.jobs, {})
            self.enqueue(assets=self.assets[:2])

    def test_the_running_job_stays_listed_after_a_long_queue_is_cancelled(self):
        from tools.local_data import public_map_catalog
        seed = downloads.public_map_catalog.load_seed()
        seed["records"] = [r for r in seed["records"] if r["sourceId"] != "publisher-noaa-storm-events"]
        kinds = ("details", "fatalities", "locations")
        for year in range(1950, 2025):
            seed["records"].append(public_map_catalog.storm_events_record(
                year, {kind: f"StormEvents_{kind}-ftp_v1.0_d{year}_c20250401.csv.gz" for kind in kinds}, "2026-10-09"))
        self.manager._catalog = seed
        self.enqueue(assets=[f"publisher-noaa-storm-events-{year}-{kind}" for year in range(1950, 2025) for kind in kinds])
        running = self.manager.active
        self.manager.cancel_queue()
        health = self.manager.health()
        self.assertEqual(len(health["jobs"]), 100)
        self.assertEqual(health["jobs"][-1]["id"], running)
        self.assertEqual(health["queued"], 0)

    def test_cancelling_the_queue_stops_waiting_files_with_receipts(self):
        self.enqueue()
        running = self.manager.active
        result = self.manager.cancel_queue()
        self.assertEqual(result, {"cancelledQueued": 2, "cancelling": running})
        self.assertTrue(self.manager.cancel_event.is_set())
        waiting = [job for job in self.manager.jobs.values() if job["id"] != running and job.get("batchId")]
        self.assertTrue(all(job["state"] == "cancelled" for job in waiting))
        self.assertTrue(all((self.manager.receipts / (job["id"] + ".json")).exists() for job in waiting))

    def test_one_invalid_file_rejects_the_whole_selection_before_any_job(self):
        for assets in ([*self.assets, "unknown-asset"], [self.assets[0], self.assets[0]], []):
            with self.assertRaises(ValueError):
                self.enqueue(assets=assets)
        self.assertEqual((self.manager.jobs, self.manager.queue, self.manager.active), ({}, [], None))


if __name__ == "__main__":
    unittest.main()

def test_public_climate_downloads_are_exact_pinned_files_and_do_not_require_google():
    import pytest
    from tools.local_data import public_map_downloads as download, public_map_catalog as catalog
    rows=[r for r in catalog.load_seed()['records'] if r['sourceId'].startswith('publisher-')]
    assert len(rows)==64
    assert len(download.PUBLISHER_FILES)==64
    for row in rows:
        a=row['assets'][0]
        assert download.validate_url(a['url'])==a['url']
        assert a['expectedBytes']>0 and a['availability']=='verified'
        assert row['rights']['status']=='public-domain'
        assert 'not clipped' in row['description']
        with pytest.raises(ValueError): download.validate_url(a['url']+'?redirect=https://evil.example')
    with pytest.raises(ValueError): download.validate_url('https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2099_30m_cdls.zip')


def test_storm_events_files_are_admitted_only_by_exact_ncei_name_and_gzip_signature():
    import pytest
    from tools.local_data import public_map_downloads as download
    base = "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/"
    url = base + "StormEvents_fatalities-ftp_v1.0_d2024_c20250401.csv.gz"
    assert download.validate_url(url) == url
    for denied in (base + "Storm-Data-Bulk-csv-Format.pdf", base + "legacy/StormEvents_details-ftp_v1.0_d1999_c20250401.csv.gz",
                   url + "?x=1", base + "StormEvents_details-ftp_v1.0_d2024_c20250401.csv",
                   "https://www.ncei.noaa.gov/pub/data/other/StormEvents_details-ftp_v1.0_d2024_c20250401.csv.gz"):
        with pytest.raises(ValueError):
            download.validate_url(denied)
    download._magic("GZIP", b"\x1f\x8b\x08\x00\x00\x00\x00\x00")
    with pytest.raises(ValueError, match="ASSET_FORMAT_MISMATCH"):
        download._magic("GZIP", b"<!DOCTYP")
