"""Offline checks for the Kansas-only, unreleased DASC candidate capture."""
from collections import deque
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
for path in (ROOT, ROOT / "packages/connectors-core/src", ROOT / "connectors/kansas"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import dasc_geoportal as dasc  # noqa: E402
from connectors_core.transport import TransportRequest, TransportResponse  # noqa: E402
from connectors_core.bounded_curl import BoundedCurlTransport  # noqa: E402


def encoded(value):
    return json.dumps(value, separators=(",", ":")).encode("utf-8")


def item(modified=10):
    return encoded({"id": dasc.ITEM_ID, "access": "public", "url": dasc.SERVICE,
                    "owner": "jkastens_KU", "modified": modified, "licenseInfo": "Acknowledge KBS"})


def layer(revision=20):
    return encoded({"name": "WBDHU12", "objectIdField": "FID", "geometryType": "esriGeometryPolygon",
                    "maxRecordCount": 2000, "advancedQueryCapabilities": {"supportsPagination": True,
                    "supportsOrderBy": True}, "editingInfo": {"dataLastEditDate": revision},
                    "fields": [{"name": name, "type": "esriFieldTypeOID" if name == "FID"
                                else "esriFieldTypeString"} for name in dasc.FIELDS]})


def feature(oid=1, huc="110400040101", states="KS,CO"):
    return {"type": "Feature", "properties": {"FID": oid, "huc12": huc, "states": states,
             "name": "Test watershed", "tohuc": None, "hutype": "S", "humod": "NM"},
            "geometry": {"type": "Polygon", "coordinates": [[[-102.0, 39.0], [-101.0, 39.0],
                [-101.0, 40.1], [-102.0, 39.0]]]}}


def page(features):
    return encoded({"type": "FeatureCollection", "features": features,
                    "properties": {"exceededTransferLimit": False}})


class Clock:
    def __init__(self):
        self.elapsed = 0.0

    def now(self):
        return datetime(2026, 10, 1, tzinfo=timezone.utc) + timedelta(seconds=self.elapsed)

    def monotonic(self):
        return self.elapsed

    def sleep(self, seconds):
        self.elapsed += seconds


class Transport:
    def __init__(self, bodies, clock):
        self.bodies, self.clock, self.urls = deque(bodies), clock, []

    def send(self, request, *, timeout_seconds, max_response_bytes, allow_redirects):
        self.urls.append(request.url)
        self.clock.elapsed += 0.1
        body = self.bodies.popleft()
        return TransportResponse(200, {"Content-Type": "application/json",
                                       "Content-Length": str(len(body))}, (body,), request.url)


class DascCaptureTests(unittest.TestCase):
    def run_capture(self, *, item_bodies=None, service_bodies=None):
        clock = Clock()
        item_transport = Transport(item_bodies or [item(), item()], clock)
        service_transport = Transport(service_bodies or [layer(), b'{"count":1}',
            page([feature()]), b'{"count":1}', layer()], clock)
        with TemporaryDirectory() as temporary:
            destination = Path(temporary) / "capture"
            manifest = dasc.capture(destination, item_transport=item_transport,
                                    service_transport=service_transport, clock=clock)
            names = sorted(path.name for path in destination.iterdir())
            on_disk = json.loads((destination / "manifest.json").read_text())
            return manifest, on_disk, names, service_transport.urls

    def test_complete_capture_preserves_source_bytes_and_unreleased_state(self):
        manifest, on_disk, names, urls = self.run_capture()
        self.assertEqual(manifest, on_disk)
        self.assertEqual((manifest["state"], manifest["feature_count"], manifest["count_after"]),
                         ("COMPLETE_CANDIDATE", 1, 1))
        self.assertEqual((manifest["source_admission"], manifest["release_state"]),
                         ("NOT_ADMITTED", "UNRELEASED"))
        self.assertIn("page-0000.geojson", names)
        self.assertEqual(urls[1], dasc.count_url())
        self.assertIn("states+LIKE+%27%25KS%25%27", urls[2])
        self.assertEqual(len(manifest["objects"]), 7)
        self.assertEqual(manifest["objects"][3]["url"], urls[2])

    def test_http_200_error_and_non_kansas_feature_fail_closed(self):
        errored, _, names, _ = self.run_capture(service_bodies=[layer(), b'{"error":{"code":400}}'])
        self.assertEqual((errored["state"], errored["reason_code"]), ("INCOMPLETE", "SERVICE_ERROR"))
        self.assertIn("count-before.json", names)
        outside, _, _, _ = self.run_capture(service_bodies=[layer(), b'{"count":1}',
            page([feature(states="CO")])])
        self.assertEqual((outside["state"], outside["reason_code"]), ("INCOMPLETE", "STATE_SCOPE"))

    def test_count_and_source_revision_drift_hold_capture(self):
        changed, _, _, _ = self.run_capture(service_bodies=[layer(), b'{"count":1}',
            page([feature()]), b'{"count":2}', layer()])
        self.assertEqual((changed["state"], changed["reason_code"]), ("INCOMPLETE", "COUNT_CHANGED"))
        revised, _, _, _ = self.run_capture(item_bodies=[item(), item(modified=11)])
        self.assertEqual((revised["state"], revised["reason_code"]),
                         ("INCOMPLETE", "SOURCE_REVISION_CHANGED"))

    def test_duplicate_ids_bad_geometry_and_missing_terms_rejected(self):
        self.assertRaises(dasc.CaptureError, dasc.parse_page, page([feature(), feature()]),
                          expected=2, previous_id=-1, seen_hucs=set())
        broken = feature()
        broken["geometry"]["coordinates"][0][-1] = [-99, 39]
        with self.assertRaisesRegex(dasc.CaptureError, "RING_OPEN"):
            dasc.parse_page(page([broken]), expected=1, previous_id=-1, seen_hucs=set())
        with self.assertRaisesRegex(dasc.CaptureError, "ITEM_IDENTITY"):
            dasc.parse_item(encoded({"id": dasc.ITEM_ID, "access": "public", "url": dasc.SERVICE,
                                     "owner": "x", "modified": 10, "licenseInfo": ""}))

    def test_unquoted_arcgis_etag_is_ignored_without_changing_body(self):
        body = b'{"count":1}'
        response = TransportResponse(200, {"Content-Type": "application/json",
            "Content-Length": str(len(body)), "ETag": "sd15856_-366898795"}, (body,), dasc.count_url())
        with patch.object(BoundedCurlTransport, "send", return_value=response):
            observed = dasc.ServiceTransport().send(dasc.count_url(), timeout_seconds=5,
                max_response_bytes=100, allow_redirects=False)
        self.assertEqual(observed.body_chunks, (body,))
        self.assertNotIn("etag", observed.headers)

    def test_item_and_service_hosts_are_separate(self):
        with self.assertRaises(ValueError):
            dasc.SERVICE_PROFILE.validate_request(TransportRequest("GET", dasc.ITEM + "?f=json"))
        with self.assertRaises(ValueError):
            dasc.ITEM_PROFILE.validate_request(TransportRequest("GET", dasc.count_url()))


if __name__ == "__main__":
    unittest.main()
