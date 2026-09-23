"""Deterministic synthetic tests; no provider access or operational accuracy claim."""
from dataclasses import FrozenInstanceError
import importlib.util
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

PATH = Path(__file__).resolve().parents[1] / "src/usgs/earthquake.py"
SPEC = importlib.util.spec_from_file_location("kfm_usgs_earthquake_tested", PATH)
eq = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = eq
SPEC.loader.exec_module(eq)
NOW = "2026-09-22T18:00:00Z"


def event(identifier="synthetic1", time=-1000):
    return {"type": "Feature", "id": identifier,
            "geometry": {"type": "Point", "coordinates": [-98, 38, -0.4]},
            "properties": {"time": time, "updated": 1000, "mag": 0,
                           "magType": "ml", "type": "earthquake", "status": "automatic",
                           "ids": f",{identifier},", "unknown_field": {"retained": True}}}


def document(events=None):
    features = [event()] if events is None else events
    return {"type": "FeatureCollection", "metadata": {"status": 200,
            "count": len(features), "generated": 2000}, "features": features}


def parse(payload=None, **kwargs):
    body = json.dumps(document() if payload is None else payload).encode()
    return eq.parse_snapshot(body, status=200, source_url=eq.live_url(),
                             retrieved_at=NOW, **kwargs)


class RequestTests(unittest.TestCase):
    def test_all_twenty_fixed_feeds(self):
        for period in ("hour", "day", "week", "month"):
            for level in ("all", "1.0", "2.5", "4.5", "significant"):
                with self.subTest(period=period, level=level):
                    self.assertEqual(eq._request_kind(eq.live_url(period, level)), ("summary", None))

    def test_unknown_feed_and_url_injection(self):
        for value in ("year", "../../query", "day?url=private", "https://example.org"):
            with self.subTest(value=value), self.assertRaises(eq.EarthquakeInputError):
                eq.live_url(value)

    def test_history_explicit_bounds_no_default_magnitude_floor(self):
        plans = eq.history_windows("1969-12-01T00:00:00Z", "1970-02-01T00:00:00Z")
        self.assertEqual(len(plans), 2)
        self.assertEqual(plans[0].end_exclusive, plans[1].start)
        params = parse_qs(urlsplit(plans[0].query_url).query)
        self.assertEqual(params["nodata"], ["204"])
        self.assertEqual(params["offset"], ["1"])
        self.assertEqual(params["eventtype"], ["earthquake"])
        self.assertNotIn("minmagnitude", params)
        self.assertEqual(params["starttime"], [plans[0].start])
        count_params = parse_qs(urlsplit(plans[0].count_url).query)
        self.assertNotIn("limit", count_params)
        self.assertEqual(count_params["endtime"], [plans[0].end_exclusive])

    def test_short_final_window_and_timezone_normalization(self):
        plans = eq.history_windows("2020-02-28T00:00:00-06:00", "2020-03-02T06:00:00Z", window_days=2)
        self.assertEqual(len(plans), 2)
        self.assertEqual(plans[0].start, "2020-02-28T06:00:00.000Z")
        self.assertEqual(plans[1].end_exclusive, "2020-03-02T06:00:00.000Z")

    def test_time_validation(self):
        for start, end in (("2020-01-01", NOW), (NOW, NOW), (NOW, "1900-01-01T00:00:00Z"),
                           ("2020-02-30T00:00:00Z", NOW), ("2020-01-01T00:00:00.000001Z", NOW)):
            with self.subTest(start=start, end=end), self.assertRaises(eq.EarthquakeInputError):
                eq.history_windows(start, end)

    def test_caps_and_nonfinite_parameters(self):
        for name, values in {"limit": (0, 20001, True, 2.5), "window_days": (0, 32, True),
                             "max_windows": (0, 2401, True)}.items():
            for value in values:
                with self.subTest(name=name, value=value), self.assertRaises(eq.EarthquakeInputError):
                    eq.history_windows("2000-01-01T00:00:00Z", NOW, **{name: value})
        with self.assertRaisesRegex(eq.EarthquakeInputError, "WINDOW_CAPACITY"):
            eq.history_windows("1800-01-01T00:00:00Z", NOW, max_windows=1)

    def test_bad_bbox(self):
        for bounds in ((0, 0, 0, 1), (-181, 0, 1, 1), (-1, 0, 1, 91),
                       (float("nan"), 0, 1, 1), (-1, 0, True, 1), (1, 2), None):
            with self.subTest(bounds=bounds), self.assertRaises(eq.EarthquakeInputError):
                eq.history_windows("2020-01-01T00:00:00Z", NOW, bounds=bounds)


class SnapshotTests(unittest.TestCase):
    def test_negative_epoch_zero_magnitude_negative_depth_and_unknown_fields(self):
        snapshot = parse()
        record = snapshot.events[0]
        self.assertEqual((record.origin_ms, record.magnitude, record.depth_km), (-1000, 0.0, -0.4))
        self.assertTrue(json.loads(record.raw_feature_json)["properties"]["unknown_field"]["retained"])
        self.assertEqual((snapshot.coverage, snapshot.admission), ("NOT_ESTABLISHED", "NOT_ADMITTED"))
        self.assertEqual(snapshot.generated_ms, 2000)
        self.assertEqual(snapshot.retrieved_at, "2026-09-22T18:00:00.000Z")

    def test_null_optional_values_not_zero(self):
        data = document()
        data["features"][0]["properties"].update(mag=None, magType=None, updated=None, status=None)
        data["features"][0]["geometry"]["coordinates"][2] = None
        record = parse(data).events[0]
        self.assertIsNone(record.magnitude)
        self.assertIsNone(record.depth_km)
        self.assertIsNone(record.updated_ms)
        self.assertIsNone(record.review_status)

    def test_missing_required_origin_is_not_epoch_zero(self):
        data = document()
        del data["features"][0]["properties"]["time"]
        with self.assertRaises(eq.EarthquakeInputError):
            parse(data)

    def test_snapshot_and_events_are_immutable(self):
        snapshot = parse()
        with self.assertRaises(FrozenInstanceError):
            snapshot.events = ()
        with self.assertRaises(FrozenInstanceError):
            snapshot.events[0].magnitude = 4

    def test_retrieval_does_not_change_feature_version_hash(self):
        first = parse()
        second = eq.parse_snapshot(json.dumps(document()).encode(), status=200,
                 source_url=eq.live_url(), retrieved_at="2026-09-23T00:00:00Z")
        self.assertEqual(first.body_sha256, second.body_sha256)
        self.assertEqual(first.events[0].feature_sha256, second.events[0].feature_sha256)
        self.assertNotEqual(first.retrieved_at, second.retrieved_at)
        data = document()
        data["features"][0]["properties"]["updated"] = 2001
        self.assertNotEqual(first.events[0].feature_sha256, parse(data).events[0].feature_sha256)

    def test_raw_digest_detects_body_whitespace_change(self):
        source = document()
        other = eq.parse_snapshot(json.dumps(source, indent=2).encode(), status=200,
                                  source_url=eq.live_url(), retrieved_at=NOW)
        self.assertNotEqual(parse(source).body_sha256, other.body_sha256)
        self.assertEqual(parse(source).events[0].feature_sha256, other.events[0].feature_sha256)

    def test_204_is_query_only_with_empty_body(self):
        url = eq.history_windows("2020-01-01T00:00:00Z", "2020-01-02T00:00:00Z")[0].query_url
        result = eq.parse_snapshot(b"", status=204, source_url=url, retrieved_at=NOW)
        self.assertEqual(result.events, ())
        self.assertIsNone(result.generated_ms)
        for source_url, body in ((eq.live_url(), b""), (url, b"{}")):
            with self.subTest(source=source_url), self.assertRaises(eq.EarthquakeInputError):
                eq.parse_snapshot(body, status=204, source_url=source_url, retrieved_at=NOW)

    def test_other_statuses_do_not_become_empty(self):
        for status in (201, 206, 301, 304, 400, 404, 409, 429, 500, 503, True):
            with self.subTest(status=status), self.assertRaises(eq.EarthquakeInputError):
                eq.parse_snapshot(b"", status=status, source_url=eq.live_url(), retrieved_at=NOW)

    def test_untrusted_source_urls_rejected(self):
        base = eq.history_windows("2020-01-01T00:00:00Z", "2020-01-02T00:00:00Z")[0].query_url
        for url in ("http://earthquake.usgs.gov/", eq.live_url()+"#x", eq.live_url()+"?callback=x",
                    eq.live_url().replace("earthquake.usgs.gov", "earthquake.usgs.gov.evil"),
                    eq.live_url().replace("earthquake.usgs.gov", "a@earthquake.usgs.gov"),
                    base+"&callback=x", base+"&limit=1", base.replace("nodata=204", "nodata=404"),
                    "\n"+eq.live_url(), base.replace("limit=1000", "limit=20001")):
            with self.subTest(url=url), self.assertRaises(eq.EarthquakeInputError):
                eq.parse_snapshot(b"", status=204, source_url=url, retrieved_at=NOW)

    def test_invalid_json_and_duplicate_keys(self):
        for body in (b"", b"<html>error</html>", b"\xff", b'{"a":1,"a":2}',
                     b'{"a":NaN}', b'{"a":Infinity}', b'['*1500+b']'*1500):
            with self.subTest(body=body[:20]), self.assertRaises(eq.EarthquakeInputError):
                eq.parse_snapshot(body, status=200, source_url=eq.live_url(), retrieved_at=NOW)

    def test_collection_validation(self):
        for data in ([], None, {"type": "Feature"}, {"type": "FeatureCollection", "features": []}):
            with self.subTest(data=data), self.assertRaises(eq.EarthquakeInputError):
                eq.parse_snapshot(json.dumps(data).encode(), status=200, source_url=eq.live_url(), retrieved_at=NOW)
        for field, value in (("count", 2), ("count", True), ("status", 500), ("generated", True)):
            data = document()
            data["metadata"][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(eq.EarthquakeInputError):
                parse(data)

    def test_duplicate_primary_or_alias_is_not_double_counted(self):
        for second in (event(), event("synthetic2")):
            second["properties"]["ids"] = ",synthetic1,"
            with self.assertRaisesRegex(eq.EarthquakeInputError, "IDENTITY_CONFLICT"):
                parse(document([event(), second]))

    def test_invalid_geometry_and_scalars(self):
        for coords in ([-98, 38], [-181, 38, 0], [-98, 91, 0], [True, 38, 0], [-98, 38, "0"]):
            data = document()
            data["features"][0]["geometry"]["coordinates"] = coords
            with self.subTest(coords=coords), self.assertRaises(eq.EarthquakeInputError):
                parse(data)
        for key, value in (("mag", "0"), ("time", True), ("time", 10**30), ("ids", ",bad id,")):
            data = document()
            data["features"][0]["properties"][key] = value
            with self.subTest(key=key), self.assertRaises(eq.EarthquakeInputError):
                parse(data)

    def test_byte_and_event_caps(self):
        for kwargs in ({"max_bytes": 1}, {"max_bytes": 0}, {"max_bytes": True},
                       {"max_bytes": 16*1024*1024+1}, {"max_events": 0}):
            with self.subTest(kwargs=kwargs), self.assertRaises(eq.EarthquakeInputError):
                parse(**kwargs)
        with self.assertRaises(eq.EarthquakeInputError):
            parse(document([event("one"), event("two")]), max_events=1)

    def test_limit_is_not_completeness(self):
        url = eq.history_windows("2020-01-01T00:00:00Z", "2020-01-02T00:00:00Z", limit=1)[0].query_url
        snap = eq.parse_snapshot(json.dumps(document()).encode(), status=200, source_url=url, retrieved_at=NOW)
        self.assertTrue(snap.query_limit_reached)
        self.assertEqual(snap.coverage, "NOT_ESTABLISHED")
        with self.assertRaisesRegex(eq.EarthquakeInputError, "QUERY_LIMIT_EXCEEDED"):
            eq.parse_snapshot(json.dumps(document([event("one"), event("two")])).encode(),
                              status=200, source_url=url, retrieved_at=NOW)

    def test_half_open_scope_preserves_original_and_event_types(self):
        first, at_boundary, blast, outside = event("old", -1000), event("edge", 0), event("blast", -500), event("outside", -500)
        blast["properties"]["type"] = "quarry blast"
        outside["geometry"]["coordinates"][0] = -120
        snapshot = parse(document([first, at_boundary, blast, outside]))
        selected = eq.select_earthquakes(snapshot, start="1969-12-31T23:59:59Z", end="1970-01-01T00:00:00Z")
        self.assertEqual([item.event_id for item in selected], ["old"])
        self.assertEqual(len(snapshot.events), 4)

    def test_nonempty_empty_nonempty_no_retained_state(self):
        first = parse()
        empty = parse(document([]))
        last = parse()
        self.assertEqual(empty.events, ())
        self.assertEqual(first.events, last.events)

    def test_import_and_helpers_make_no_network_calls(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            name = "kfm_usgs_earthquake_no_network"
            spec = importlib.util.spec_from_file_location(name, PATH)
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            try:
                spec.loader.exec_module(module)
                module.history_windows("2020-01-01T00:00:00Z", "2020-01-02T00:00:00Z")
                module.parse_snapshot(json.dumps(document()).encode(), status=200,
                                      source_url=module.live_url(), retrieved_at=NOW)
            finally:
                del sys.modules[name]


if __name__ == "__main__":
    unittest.main()
