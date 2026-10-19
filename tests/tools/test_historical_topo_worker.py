"""RAW capture stays incomplete on a failed provider stream; staging is verified end to end."""
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

SOURCE = Path(__file__).resolve().parents[2] / "tools/historical_topo_worker.py"
spec = importlib.util.spec_from_file_location("kfm_historical_topo_worker", SOURCE)
worker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(worker)


class WorkerCaptureTests(unittest.TestCase):
    def test_capture_receipt_and_deduplicated_rerun(self):
        original = worker.stream_geotiff
        calls = []
        try:
            def stream(_item, emit):
                calls.append(1)
                emit(b"original GeoTIFF")
                return {"geotiff": {"bytes": 16, "sha256": "example"}}
            worker.stream_geotiff = stream
            with TemporaryDirectory() as directory:
                raw = Path(directory)
                receipt = worker.capture_raw({"scanId": 122705}, raw, 122705)
                self.assertEqual((raw / "122705.tif").read_bytes(), b"original GeoTIFF")
                self.assertEqual(json.loads(receipt.read_text())["geotiff"]["bytes"], 16)
                self.assertEqual(worker.capture_raw({"scanId": 122705}, raw, 122705), receipt)
                self.assertEqual(len(calls), 1)
        finally:
            worker.stream_geotiff = original

    def test_failed_stream_leaves_no_original_or_receipt(self):
        original = worker.stream_geotiff
        try:
            def fail(_item, emit):
                emit(b"partial")
                raise ValueError("incomplete provider response")
            worker.stream_geotiff = fail
            with TemporaryDirectory() as directory:
                raw = Path(directory)
                with self.assertRaisesRegex(ValueError, "incomplete"):
                    worker.capture_raw({"scanId": 122705}, raw, 122705)
                self.assertEqual(list(raw.iterdir()), [])
        finally:
            worker.stream_geotiff = original

    def test_stale_partials_from_a_killed_worker_are_replaced(self):
        with TemporaryDirectory() as directory, patch.object(worker, "stream_geotiff", stream_ok):
            raw = Path(directory)
            (raw / "7.tif.part").write_bytes(b"stale")
            (raw / "7.capture.json.part").write_text("{")
            worker.capture_raw({"scanId": 7}, raw, 7)
            self.assertEqual(sorted(p.name for p in raw.iterdir()), ["7.capture.json", "7.tif"])
            self.assertEqual((raw / "7.tif").read_bytes(), TIFF)

    def test_a_concurrent_capture_is_refused_without_touching_its_partial(self):
        with TemporaryDirectory() as directory, patch.object(worker, "stream_geotiff", stream_ok):
            raw = Path(directory)
            with worker.capture_lock(raw):
                (raw / "7.tif.part").write_bytes(b"in progress")
                with self.assertRaisesRegex(ValueError, "another worker"):
                    worker.capture_raw({"scanId": 7}, raw, 7)
                self.assertEqual((raw / "7.tif.part").read_bytes(), b"in progress")

    def test_inconsistent_raw_state_fails_closed(self):
        with TemporaryDirectory() as directory, patch.object(worker, "stream_geotiff", stream_ok):
            raw = Path(directory)
            (raw / "7.tif").write_bytes(TIFF)
            with self.assertRaisesRegex(ValueError, "without its capture receipt"):
                worker.capture_raw({"scanId": 7}, raw, 7)
            (raw / "7.tif").unlink()
            (raw / "7.capture.json").write_text("{}")
            with self.assertRaisesRegex(ValueError, "without its original"):
                worker.capture_raw({"scanId": 7}, raw, 7)


TIFF = b"original GeoTIFF"
TOKEN = "t" * 32
SITE = worker.SITE_ORIGIN
ITEM = {"version": 1, "state": "KS", "scanId": 7, "id": "s7", "name": "Abilene", "year": 1893, "scale": 125000}


def stream_ok(_item, emit):
    emit(TIFF)
    return {"geotiff": {"bytes": len(TIFF), "sha256": hashlib.sha256(TIFF).hexdigest()}}


class Response(io.BytesIO):
    def __init__(self, body, status=200, content_type="application/json"):
        super().__init__(body if isinstance(body, bytes) else json.dumps(body).encode())
        self.status, self.headers = status, {"Content-Type": content_type}


class Opener:
    """Replays scripted responses (or raises scripted errors) and records each request."""
    def __init__(self, *script):
        self.script, self.requests = list(script), []

    def open(self, request, timeout):
        self.requests.append(request)
        step = self.script.pop(0)
        if isinstance(step, BaseException):
            raise step
        return step(request) if callable(step) else step


def confirm(request):
    return Response({"staged": True, "sha256": request.get_header("X-kfm-sha256")}, status=201)


def http_error(code):
    return HTTPError("https://example.invalid", code, "error", {}, None)


class StageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.tile = Path(self.temporary.name) / "tile.png"
        self.tile.write_bytes(b"\x89PNG tile")
        sleep = patch.object(worker.time, "sleep")
        self.sleeps = sleep.start()
        self.addCleanup(sleep.stop)
        self.addCleanup(self.temporary.cleanup)

    def stage(self, *script, address="9/1/2"):
        opener = Opener(*script)
        with patch.object(worker, "OPENER", opener):
            worker.stage(SITE, TOKEN, 7, "a" * 24, address, self.tile)
        return opener

    def test_put_carries_digest_identity_and_bypass_header(self):
        with patch.dict(os.environ, {"KFM_SITES_BYPASS_TOKEN": "bypass"}):
            request = self.stage(confirm).requests[0]
        self.assertEqual(request.get_method(), "PUT")
        self.assertEqual(request.full_url, f"{SITE}/api/historical-topo/stage?scan=7&package={'a' * 24}&address=9%2F1%2F2")
        self.assertEqual(request.get_header("X-kfm-sha256"), hashlib.sha256(b"\x89PNG tile").hexdigest())
        self.assertEqual(request.get_header("Content-type"), "image/png")
        self.assertEqual(request.get_header("Oai-sites-authorization"), "Bearer bypass")
        manifest = self.stage(confirm, address="manifest").requests[0]
        self.assertEqual(manifest.get_header("Content-type"), "application/json")

    def test_transient_failures_are_retried_with_backoff(self):
        opener = self.stage(http_error(503), URLError("reset"), confirm)
        self.assertEqual(len(opener.requests), 3)
        self.assertEqual([c.args for c in self.sleeps.call_args_list], [(1,), (2,)])
        self.assertEqual(len(self.stage(ConnectionResetError(), confirm).requests), 2)

    def test_permanent_or_exhausted_failures_stop(self):
        with self.assertRaisesRegex(ValueError, "staging failed"):
            self.stage(http_error(403))
        self.sleeps.assert_not_called()
        with self.assertRaisesRegex(ValueError, "staging failed"):
            self.stage(TimeoutError(), TimeoutError(), TimeoutError())
        self.assertEqual(self.sleeps.call_count, 2)

    def test_unconfirmed_staging_is_refused(self):
        for body in ({"staged": False, "sha256": "x"}, {"staged": True, "sha256": "0" * 64}, ["staged"]):
            with self.subTest(body=body), self.assertRaisesRegex(ValueError, "did not confirm"):
                self.stage(Response(body))


class QueueTests(unittest.TestCase):
    def fetch(self, response):
        with patch.object(worker, "OPENER", Opener(response)):
            return worker.request_json(f"{SITE}/api/historical-topo/queue", TOKEN)

    def test_queue_response_is_bounded_and_typed(self):
        self.assertEqual(self.fetch(Response({"requests": []})), {"requests": []})
        with self.assertRaisesRegex(ValueError, "unexpected response"):
            self.fetch(Response(b"<html>", content_type="text/html"))
        with self.assertRaisesRegex(ValueError, "byte limit"):
            self.fetch(Response(b" " * 500_001))
        headers = worker.headers(TOKEN)
        self.assertEqual(headers["Authorization"], f"Bearer {TOKEN}")


class RunTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        base = Path(self.temporary.name)
        self.raw, self.packages = base / "raw", base / "packages"
        self.request = base / "request.json"
        self.request.write_text(json.dumps(ITEM))
        self.package = hashlib.sha256(TIFF).hexdigest()[:24]
        self.transforms = 0
        stream = patch.object(worker, "stream_geotiff", stream_ok)
        stream.start()
        self.addCleanup(stream.stop)
        transform = patch.object(worker.subprocess, "run", side_effect=self.transform)
        transform.start()
        self.addCleanup(transform.stop)
        self.addCleanup(self.temporary.cleanup)

    def transform(self, command, check):
        self.transforms += 1
        folder = self.packages / f"7-{self.package}"
        (folder / "tiles/9/1").mkdir(parents=True)
        tile = b"\x89PNG tile"
        (folder / "tiles/9/1/2.png").write_bytes(tile)
        manifest = {"packageId": self.package, "sheet": {"scanId": 7},
                    "tiles": {"9/1/2": {"bytes": len(tile), "sha256": hashlib.sha256(tile).hexdigest()}}}
        (folder / "manifest.json").write_text(json.dumps(manifest))

    def run_worker(self, *, dry_run=False, token=TOKEN, request=True, opener=None):
        with patch.object(worker, "OPENER", opener or Opener()), patch("builtins.print") as printed:
            worker.run(SITE, self.raw, self.packages, token, dry_run, self.request if request else None)
        return " ".join(str(c.args[0]) for c in printed.call_args_list)

    def test_dry_run_captures_and_prepares_without_upload(self):
        self.assertIn("Prepared 1 tiles for scan 7; no upload", self.run_worker(dry_run=True, token=""))
        self.assertEqual(sorted(p.name for p in self.raw.iterdir()), ["7.capture.json", "7.request.json", "7.tif"])
        self.run_worker(dry_run=True, token="")
        self.assertEqual(self.transforms, 1, "an existing package is reused")

    def test_full_run_stages_every_tile_then_the_manifest(self):
        opener = Opener(confirm, confirm)
        self.assertIn("Staged 1 tiles for scan 7; owner review", self.run_worker(opener=opener))
        self.assertEqual([r.full_url.rsplit("address=", 1)[1] for r in opener.requests], ["9%2F1%2F2", "manifest"])

    def test_queue_from_the_site_and_empty_queue(self):
        opener = Opener(Response({"requests": []}))
        self.assertIn("No pending", self.run_worker(request=False, opener=opener))
        self.assertEqual(opener.requests[0].full_url, f"{SITE}/api/historical-topo/queue")
        for queue in ({"requests": "x"}, ["requests"]):
            with self.subTest(queue=queue), self.assertRaisesRegex(ValueError, "changed shape"):
                self.run_worker(request=False, opener=Opener(Response(queue)))

    def test_origin_token_and_request_identity_are_checked_before_capture(self):
        with self.assertRaisesRegex(ValueError, "exact HTTPS"):
            worker.run(SITE + ".evil", self.raw, self.packages, TOKEN, False, self.request)
        with self.assertRaisesRegex(ValueError, "not configured"):
            self.run_worker(token="short")
        for change in ({"state": "MO"}, {"scanId": "7"}, {"scanId": True}, {"scanId": 0}, {"scanId": -7}, {"scanId": 10**11}):
            with self.subTest(change=change):
                self.request.write_text(json.dumps({**ITEM, **change}))
                with self.assertRaisesRegex(ValueError, "invalid Kansas request"):
                    self.run_worker(dry_run=True)
        self.request.write_text(json.dumps(["not an object"]))
        with self.assertRaisesRegex(ValueError, "invalid Kansas request"):
            self.run_worker(dry_run=True)
        self.assertFalse(self.raw.exists(), "nothing is written for a rejected request")

    def test_changed_identity_mismatched_package_and_tampered_tile_fail_closed(self):
        self.run_worker(dry_run=True)
        self.request.write_text(json.dumps({**ITEM, "name": "Salina"}))
        with self.assertRaisesRegex(ValueError, "identity changed"):
            self.run_worker(dry_run=True)
        self.request.write_text(json.dumps(ITEM))
        manifest_file = self.packages / f"7-{self.package}/manifest.json"
        manifest = json.loads(manifest_file.read_text())
        manifest_file.write_text(json.dumps({**manifest, "sheet": {"scanId": 8}}))
        with self.assertRaisesRegex(ValueError, "does not match the queued sheet"):
            self.run_worker(dry_run=True)
        manifest_file.write_text(json.dumps(manifest))
        (self.packages / f"7-{self.package}/tiles/9/1/2.png").write_bytes(b"\x89PNG tampered")
        opener = Opener()
        with self.assertRaisesRegex(ValueError, "local tile digest failed: 9/1/2"):
            self.run_worker(opener=opener)
        self.assertEqual(opener.requests, [], "nothing is uploaded once a tile fails")

    def test_main_reads_the_token_from_the_environment(self):
        argv = ["worker", "--site", SITE + "/", "--raw", str(self.raw), "--packages", str(self.packages), "--request", str(self.request), "--dry-run"]
        with patch.object(worker.sys, "argv", argv), patch.dict(os.environ, {"KFM_HISTORICAL_WORKER_TOKEN": ""}), \
                patch.object(worker, "run") as run:
            worker.main()
        run.assert_called_once_with(SITE, self.raw, self.packages, "", True, self.request)


if __name__ == "__main__":
    unittest.main()
