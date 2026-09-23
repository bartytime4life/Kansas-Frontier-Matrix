"""Synthetic history orchestration tests. No socket, provider, or storage use."""
import dataclasses
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import unittest
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from usgs.earthquake_history import HistoryResponse, acquire_history

START = "1969-12-31T00:00:00Z"
END = "1970-01-01T00:00:00Z"
STAMP = "2026-09-22T00:00:00Z"


def feature(identifier="test-a", when=-1000, **props):
    return {"type": "Feature", "id": identifier,
            "geometry": {"type": "Point", "coordinates": [-98, 38, -0.5]},
            "properties": {"type": "earthquake", "time": when, "updated": 1,
                           "mag": 0, "magType": "ml", "status": "reviewed", **props}}


def epoch(text):
    return int(datetime.fromisoformat(text.replace("Z", "+00:00")).timestamp() * 1000)


class Reader:
    def __init__(self, events=(), mutate=None):
        self.events = list(events)
        self.calls = []
        self.mutate = mutate

    def __call__(self, request):
        self.calls.append(request)
        url = urlsplit(request.url)
        query = parse_qs(url.query)
        a, b = epoch(query["starttime"][0]), epoch(query["endtime"][0])
        selected = [f for f in self.events if a <= f["properties"]["time"] <= b]
        selected.sort(key=lambda f: f["properties"]["time"])
        if url.path.endswith("count"):
            response = HistoryResponse(request.url, 200, "text/plain", STAMP,
                                       str(len(selected)).encode())
        else:
            offset, limit = int(query["offset"][0]), int(query["limit"][0])
            page = selected[offset - 1:offset - 1 + limit]
            body = json.dumps({"type": "FeatureCollection", "metadata": {
                "status": 200, "count": len(page), "generated": 100}, "features": page}).encode()
            response = HistoryResponse(request.url, 200, "application/json", STAMP, body)
        return self.mutate(request, response, len(self.calls)) if self.mutate else response


class HistoryTests(unittest.TestCase):
    def run_reader(self, reader, **options):
        return acquire_history(START, END, reader, clock=lambda: 0, **options)

    def assert_held(self, reader, reason, **options):
        result = self.run_reader(reader, **options)
        self.assertEqual((result.outcome, result.reason, result.events), ("HELD", reason, ()))
        self.assertEqual(result.admission, "NOT_ADMITTED")
        return result

    def test_complete_two_pages_twice_preserves_values(self):
        reader = Reader([feature("a", -2000), feature("b", -1000, mag=-1)])
        result = self.run_reader(reader, page_size=1)
        self.assertEqual(result.outcome, "TWO_PASS_MATCH")
        self.assertEqual(result.requests_attempted, 8)
        self.assertEqual(result.passes_completed, 2)
        self.assertEqual([e.magnitude for e in result.events], [0, -1])
        self.assertEqual(result.events[0].depth_km, -0.5)
        self.assertEqual(result.coverage, "NOT_ESTABLISHED")
        self.assertTrue(all(not request.allow_redirects for request in reader.calls))
        self.assertTrue(all("format=text" in r.url for r in reader.calls if "/count?" in r.url))
        self.assertTrue(all("nodata=204" in r.url for r in reader.calls if "/query?" in r.url))

    def test_exact_page_limit_is_not_automatically_rejected(self):
        self.assertEqual(self.run_reader(Reader([feature()]), page_size=1).outcome, "TWO_PASS_MATCH")

    def test_empty_requires_query_not_just_count(self):
        reader = Reader()
        result = self.run_reader(reader)
        self.assertEqual(result.outcome, "TWO_PASS_MATCH")
        self.assertEqual(len(reader.calls), 6)
        self.assertEqual(result.events, ())

    def test_query_204_empty_is_valid(self):
        reader = Reader(mutate=lambda q, r, n: dataclasses.replace(r, status=204, body=b"", media_type="") if "/query?" in q.url else r)
        self.assertEqual(self.run_reader(reader).outcome, "TWO_PASS_MATCH")

    def test_count_204_is_not_zero(self):
        self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, status=204, body=b"")), "UPSTREAM_HTTP")

    def test_query_204_with_body_fails(self):
        self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, status=204) if "/query?" in q.url else r), "UPSTREAM_HTTP")

    def test_half_open_final_boundary_is_not_owned(self):
        result = self.run_reader(Reader([feature("inside", -1), feature("next", 0)]))
        self.assertEqual([e.event_id for e in result.events], ["inside"])

    def test_adjacent_window_boundary_owned_once(self):
        result = acquire_history("1969-12-01T00:00:00Z", "1970-02-01T00:00:00Z",
                                 Reader([feature("edge", 0)]), clock=lambda: 0)
        self.assertEqual(result.outcome, "TWO_PASS_MATCH")
        self.assertEqual([e.event_id for e in result.events], ["edge"])

    def test_capture_exact_bytes(self):
        result = self.run_reader(Reader([feature()]))
        for capture in result.captures:
            self.assertEqual(capture.body_sha256, "sha256:" + hashlib.sha256(capture.response.body).hexdigest())
            self.assertNotIn('"FeatureCollection"', repr(capture))

    def test_media_failure_keeps_failed_capture(self):
        result = self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, media_type="text/html")), "MEDIA_TYPE")
        self.assertEqual(len(result.captures), 1)

    def test_redirect_and_final_url_changes_fail(self):
        for changes in ({"status": 302}, {"final_url": "https://invalid.example/"}):
            with self.subTest(changes=changes):
                self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, **changes)), "REDIRECT_DENIED")

    def test_http_failures_never_become_empty(self):
        for status in (401, 403, 404, 429, 500, 503):
            with self.subTest(status=status):
                self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, status=status)), "UPSTREAM_HTTP")

    def test_bad_count(self):
        for body in (b"-1", b"true", b"1.0", b"NaN", b"01", b"{}", b"", b"1000000000000"):
            with self.subTest(body=body):
                self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, body=body)), "COUNT_SHAPE")

    def test_changing_count_holds(self):
        self.assert_held(Reader([feature()], mutate=lambda q, r, n: dataclasses.replace(r, body=b"2") if n == 3 else r), "COUNT_CHANGED")

    def test_short_page_holds_even_if_count_unchanged(self):
        def mutate(q, r, n):
            if "/query?" not in q.url:
                return r
            data = json.loads(r.body)
            data["features"] = []
            data["metadata"]["count"] = 0
            return dataclasses.replace(r, body=json.dumps(data).encode())
        self.assert_held(Reader([feature()], mutate), "PAGE_COUNT_CHANGED")

    def test_revisions_between_passes_hold(self):
        def mutate(q, r, n):
            if n == 5:
                data = json.loads(r.body)
                data["features"][0]["properties"]["mag"] = 2
                return dataclasses.replace(r, body=json.dumps(data).encode())
            return r
        result = self.assert_held(Reader([feature()], mutate), "CATALOG_CHANGED")
        self.assertEqual(result.passes_completed, 2)

    def test_cross_page_identity_conflict(self):
        self.assert_held(Reader([feature("a", -2000), feature("a", -1000)]), "PAGE_IDENTITY_CONFLICT", page_size=1)

    def test_cross_page_alias_conflict(self):
        self.assert_held(Reader([feature("a", -2000, ids=",a,shared,"), feature("b", -1000, ids=",b,shared,")]), "PAGE_IDENTITY_CONFLICT", page_size=1)

    def test_invalid_query_membership(self):
        for mutate_feature in (lambda f: f["properties"].update(type="quarry blast"),
                               lambda f: f["geometry"].update(coordinates=[10, 20, 1]),
                               lambda f: f["properties"].update(time=1)):
            def mutate(q, r, n):
                if "/query?" in q.url:
                    data = json.loads(r.body)
                    mutate_feature(data["features"][0])
                    return dataclasses.replace(r, body=json.dumps(data).encode())
                return r
            self.assert_held(Reader([feature()], mutate), "QUERY_MEMBERSHIP")

    def test_invalid_page_json(self):
        self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, body=b"{") if "/query?" in q.url else r), "PAGE_INVALID")

    def test_request_budget(self):
        result = self.assert_held(Reader([feature("a", -2000), feature("b", -1000)]), "REQUEST_BUDGET", page_size=1, max_requests=6)
        self.assertEqual(result.requests_attempted, 6)

    def test_byte_budget(self):
        self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, body=b"x" * 129)), "BYTE_BUDGET")

    def test_transport_error_sanitized(self):
        def bad(_):
            raise RuntimeError("secret=do-not-expose")
        result = self.assert_held(bad, "TRANSPORT_ERROR")
        self.assertNotIn("secret", repr(result))

    def test_deadline_observed_after_callback(self):
        ticks = [0]
        def mutate(q, r, n):
            ticks[0] = 121
            return r
        result = acquire_history(START, END, Reader(mutate=mutate), clock=lambda: ticks[0])
        self.assertEqual(result.reason, "DEADLINE_EXCEEDED")
        self.assertEqual(len(result.captures), 1)

    def test_cancellation_prevents_transport(self):
        reader = Reader()
        result = acquire_history(START, END, reader, cancelled=lambda: True)
        self.assertEqual(result.reason, "CANCELLED")
        self.assertEqual(reader.calls, [])

    def test_invalid_clock(self):
        ticks = iter((10, 9))
        result = acquire_history(START, END, Reader(), clock=lambda: next(ticks))
        self.assertEqual(result.reason, "CLOCK_INVALID")

    def test_bad_retrieval_time(self):
        self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, retrieved_at="2026-09-22")), "RETRIEVAL_TIME")

    def test_retrieval_order(self):
        self.assert_held(Reader(mutate=lambda q, r, n: dataclasses.replace(r, retrieved_at="2020-01-01T00:00:00Z") if n == 2 else r), "RETRIEVAL_ORDER")

    def test_saturation_is_finite(self):
        reader = Reader([feature("a", -1), feature("b", -1)])
        result = acquire_history("1969-12-31T23:59:59.998Z", "1970-01-01T00:00:00Z",
                                 reader, max_events=1, clock=lambda: 0)
        self.assertEqual(result.reason, "SATURATED_INTERVAL")
        self.assertLess(result.requests_attempted, 10)

    def test_configuration_rejects_before_reader(self):
        for options in ({"page_size": True}, {"max_requests": 5}, {"max_events": 0},
                        {"max_bytes": 0}, {"deadline_seconds": float("nan")},
                        {"bounds": (-98, 38, -99, 37)}):
            reader = Reader()
            with self.subTest(options=options), self.assertRaises(ValueError):
                self.run_reader(reader, **options)
            self.assertEqual(reader.calls, [])

    def test_global_event_budget_not_evaded_by_windows(self):
        result = acquire_history("1969-12-01T00:00:00Z", "1970-02-01T00:00:00Z",
                                 Reader([feature("a", -1000), feature("b", 1000)]),
                                 max_events=1, clock=lambda: 0)
        self.assertEqual(result.reason, "EVENT_BUDGET")


if __name__ == "__main__":
    unittest.main()
