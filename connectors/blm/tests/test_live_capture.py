"""Offline acceptance checks for complete, unreleased BLM capture."""
from collections import deque
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import sys
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for path in (HERE, ROOT / "connectors/blm/src", ROOT / "packages/connectors-core/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from blm import live_capture, plss_cadnsdi  # noqa: E402
from connectors_core.transport import TransportResponse  # noqa: E402
import test_plss_cadnsdi as fixtures  # noqa: E402


class Clock:
    def __init__(self):
        self.wall = datetime(2026, 9, 30, 12, tzinfo=timezone.utc)
        self.elapsed = 0.0

    def now(self):
        return self.wall + timedelta(seconds=self.elapsed)

    def monotonic(self):
        return self.elapsed

    def sleep(self, seconds):
        self.elapsed += seconds


class Transport:
    def __init__(self, clock, bodies):
        self.clock, self.bodies, self.calls = clock, deque(bodies), []

    def send(self, request, *, timeout_seconds, max_response_bytes, allow_redirects):
        self.calls.append(request.url)
        self.clock.elapsed += 0.1
        body = self.bodies.popleft()
        return TransportResponse(200, {"Content-Type": "application/geo+json",
                                       "Content-Length": str(len(body))}, (body,))


def section(object_id: int):
    value = fixtures.feature(object_id, FRSTDIVID=f"KS060001S0010W0SN{object_id:03d}",
                             STATEABBR=...)
    return value


class LiveCaptureTests(unittest.TestCase):
    def run_capture(self, bodies):
        with TemporaryDirectory() as directory:
            clock = Clock()
            transport = Transport(clock, bodies)
            result = live_capture.capture("first_division", Path(directory) / "capture",
                                          transport=transport, clock=clock)
            manifest = json.loads((result.directory / "manifest.json").read_text())
            files = sorted(item.name for item in result.directory.iterdir())
            return manifest, files, transport.calls

    def test_complete_section_capture_preserves_bytes_and_counts(self):
        page = fixtures.body([section(1), section(2)])
        manifest, files, urls = self.run_capture([b'{"count":2}', page, b'{"count":2}'])
        self.assertEqual((manifest["state"], manifest["feature_count"], manifest["count_after"]),
                         ("COMPLETE_CANDIDATE", 2, 2))
        self.assertEqual(manifest["source_admission"], "PENDING")
        self.assertEqual(manifest["release_state"], "UNRELEASED")
        self.assertEqual(files, ["count-after.json", "count-before.json", "manifest.json",
                                 "page-0000.geojson"])
        self.assertEqual(urls[0], plss_cadnsdi.count_url("first_division"))
        self.assertEqual(manifest["pages"][0]["sha256"], live_capture._digest(page))

    def test_changed_count_and_arcgis_http_200_error_hold_candidate(self):
        page = fixtures.body([section(1)])
        changed, _, _ = self.run_capture([b'{"count":1}', page, b'{"count":2}'])
        self.assertEqual((changed["state"], changed["reason_code"]),
                         ("INCOMPLETE", "COUNT_CHANGED"))
        errored, files, _ = self.run_capture([b'{"error":{"code":400}}'])
        self.assertEqual(errored["state"], "INCOMPLETE")
        self.assertIn("count-before.json", files)
        self.assertEqual(errored["feature_count"], 0)

    def test_out_of_scope_section_is_quarantined(self):
        item = section(1)
        item["properties"]["PLSSID"] = "OK170001N0010W0"
        held, _, _ = self.run_capture([b'{"count":1}', fixtures.body([item])])
        self.assertEqual(held["state"], "INCOMPLETE")
        self.assertEqual(held["reason_code"], "STATE_SCOPE")


if __name__ == "__main__":
    unittest.main()
