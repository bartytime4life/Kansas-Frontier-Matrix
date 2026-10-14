"""Synthetic, offline NCEI Access transport/product boundary regressions."""
import copy
import io
import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "packages/connectors-core/src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from connectors.noaa.src.noaa import ncei_access as api

NOW = "2026-10-14T00:00:00Z"


def query(dataset="daily-summaries", **kwargs):
    window = {} if api.PRODUCTS[dataset].period in ("normal-month", "normal-year") else {"start": "2024-01-01", "end": "2024-01-02"}
    return api.Query(dataset, **({"stations": ("USW00003928",)} | window | kwargs))


def row(q):
    product = api.PRODUCTS[q.dataset]
    value = {"STATION": "USW00003928", "NAME": "SYNTHETIC STATION, KS US",
             "LATITUDE": "37.6", "LONGITUDE": "-97.4", "ELEVATION": "401.7"}
    period = {"day": "2024-01-01", "month": "2024-01", "year": "2024",
              "normal-day": "01-01", "normal-month": "01", "normal-year": None}[product.period]
    if period:
        value["DATE"] = period
    for element in q.parameters()["dataTypes"].split(","):
        value[element] = "1.0"
        if product.baseline:
            value.update({"meas_flag_" + element: " ", "comp_flag_" + element: "P", "years_" + element: "28"})
        else:
            value[element + "_ATTRIBUTES"] = ",,W,2400"
    return value


def raw(q):
    return json.dumps([row(q)]).encode()


def fake_capture(q):
    return api.capture(q, fetcher=lambda request: (raw(request), {
        "url": request.url(), "status": 200, "retrieved_at": NOW,
        "content_type": "application/json;charset=utf-8"}))


class Response(io.BytesIO):
    status = 200
    def __init__(self, q, body=None, headers=None, url=None):
        super().__init__(raw(q) if body is None else body)
        self.headers = {"Content-Type": "application/json"} | (headers or {})
        self.url = q.url() if url is None else url
    def geturl(self):
        return self.url


class Opener:
    def __init__(self, response=None, error=None):
        self.response, self.error, self.calls = response, error, []
    def open(self, request, timeout):
        self.calls.append((request, timeout))
        if self.error:
            raise self.error
        return self.response


class NceiAccessTests(unittest.TestCase):
    def test_all_profiles_preserve_native_bytes_flags_and_distinct_roles(self):
        for dataset, product in api.PRODUCTS.items():
            with self.subTest(dataset=dataset):
                q = query(dataset)
                acquired = fake_capture(q)
                self.assertEqual(acquired.raw, raw(q))
                self.assertEqual(acquired.manifest["source_role"], product.role)
                self.assertEqual(acquired.manifest["baseline_period"], product.baseline)
                self.assertEqual(api.verify_capture(acquired)["row_count"], 1)
                self.assertFalse(acquired.manifest["source_admitted"])
                self.assertEqual(acquired.manifest["release_state"], "UNRELEASED")

    def test_plan_is_deterministic_fixed_host_and_retains_quality_options(self):
        q = query()
        with patch.object(api, "build_opener", side_effect=AssertionError("network")):
            first = q.plan()
        self.assertEqual(first, q.plan())
        self.assertIsNone(first["expected_bytes"])
        self.assertFalse(first["network"])
        self.assertTrue(q.url().startswith(api.ENDPOINT + "?"))
        self.assertEqual(q.parameters()["bbox"], api.KANSAS_BBOX)
        for key in ("includeAttributes", "includeStationLocation", "includeStationName"):
            self.assertEqual(q.parameters()[key], "true")

    def test_invalid_request_rejected_before_transport(self):
        cases = [api.Query("https://evil.example"), query(stations=()),
                 query(stations=("USW00003928&url=http://127.0.0.1",)),
                 query(stations=("USW00003928", "USW00003928")),
                 query(elements=()), query(elements=("PRCP", "PRCP")),
                 query(elements=("TEMP",)), query(units="kelvin"),
                 query(start="2024-02-31"), query(start="2025-01-01"),
                 query(end="2025-01-01"), query(max_bytes=True), query(max_bytes=api.MAX_BYTES + 1),
                 query("normals-monthly-1991-2020", start="2024-01-01"),
                 query("normals-daily-1991-2020", end="2025-01-01")]
        for q in cases:
            with self.subTest(query=q), self.assertRaises(ValueError):
                api.fetch(q, opener=Opener(error=AssertionError("network")))

    def test_missing_dates_rejected_and_normal_days_are_cyclic(self):
        with self.assertRaises(ValueError):
            api.Query("daily-summaries").plan()
        q = query("normals-daily-1991-2020", start="2000-01-01", end="2000-12-31")
        item = row(q) | {"DATE": "02-29"}
        self.assertEqual(api.inspect_response(json.dumps([item]).encode(), q)["row_count"], 1)
        self.assertEqual(q.plan()["baseline_period"], "1991-2020")

    def test_response_identity_date_and_field_drift_fail_closed(self):
        q = query()
        for changes in ({"STATION": "USW00013985"}, {"NAME": "X, MO US"},
                        {"LATITUDE": "80"}, {"LONGITUDE": "NaN"},
                        {"DATE": "2024-01-03"}, {"DATE": "2024-02-31"},
                        {"unreviewed": "field"}, {"PRCP": "NaN"}, {"PRCP": 1.0},
                        {"NAME": "X\n, KS US"}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                api.inspect_response(json.dumps([row(q) | changes]).encode(), q)
        item = row(q)
        del item["PRCP_ATTRIBUTES"]
        with self.assertRaises(ValueError):
            api.inspect_response(json.dumps([item]).encode(), q)

    def test_normal_flag_loss_and_annual_date_drift_fail_closed(self):
        q = query("normals-monthly-1991-2020")
        item = row(q)
        del item["years_MLY-PRCP-NORMAL"]
        with self.assertRaises(ValueError):
            api.inspect_response(json.dumps([item]).encode(), q)
        q = query("normals-annualseasonal-1991-2020")
        with self.assertRaises(ValueError):
            api.inspect_response(json.dumps([row(q) | {"DATE": "2024"}]).encode(), q)

    def test_empty_missing_and_flagged_are_never_certified_complete(self):
        q = query()
        empty = api.inspect_response(b"[]", q)
        self.assertEqual(empty["outcome"], "EMPTY")
        self.assertEqual(empty["missing_station_ids"], list(q.stations))
        item = row(q) | {"PRCP": "", "TMAX_ATTRIBUTES": ",Q,W"}
        del item["SNOW"]
        result = api.inspect_response(json.dumps([item]).encode(), q)
        self.assertIn("SNOW", result["elements_absent_in_some_rows"])
        self.assertFalse(result["coverage_certified"])
        self.assertFalse(result["normalization_performed"])

    def test_json_shape_duplicates_and_byte_row_bounds(self):
        q = query()
        for payload in (b"{}", b'{"errorCode":400}', b'[NaN]', b'[null]', b'[{"STATION":"x","STATION":"y"}]',
                        json.dumps([row(q), row(q)]).encode()):
            with self.subTest(payload=payload[:50]), self.assertRaises(ValueError):
                api.inspect_response(payload, q)
        with self.assertRaises(ValueError):
            api.inspect_response(raw(q), query(max_bytes=2))
        with patch.object(api, "MAX_ROWS", 1), self.assertRaises(ValueError):
            api.inspect_response(json.dumps([row(q), row(q)]).encode(), q)

    def test_successful_transport_is_bounded_one_request_no_token(self):
        q = query()
        opener = Opener(Response(q))
        with patch.dict(os.environ, {"KFM_NO_NETWORK": "0"}):
            body, meta = api.fetch(q, opener=opener, clock=lambda: NOW)
        self.assertEqual(body, raw(q))
        self.assertEqual(meta["retrieved_at"], NOW)
        self.assertEqual(len(opener.calls), 1)
        request, timeout = opener.calls[0]
        self.assertEqual(timeout, 15)
        self.assertEqual(request.full_url, q.url())
        self.assertNotIn("Authorization", request.headers)
        self.assertEqual(request.headers["Accept-encoding"], "identity")

    def test_network_disable_prevents_effects(self):
        opener = Opener(error=AssertionError("network"))
        with patch.dict(os.environ, {"KFM_NO_NETWORK": "1"}), self.assertRaisesRegex(ValueError, "NETWORK_DISABLED"):
            api.fetch(query(), opener=opener)
        self.assertEqual(opener.calls, [])

    def test_redirect_media_encoding_size_and_deadline_rejected(self):
        q = query()
        cases = [Response(q, url="http://127.0.0.1"), Response(q, headers={"Content-Type": "text/html"}),
                 Response(q, headers={"Content-Encoding": "gzip"}),
                 Response(q, headers={"Content-Length": str(q.max_bytes + 1)}),
                 Response(q, headers={"Content-Length": "bad"}),
                 Response(q, headers={"Content-Length": "1"}), Response(q, body=b"")]
        for response in cases:
            with self.subTest(headers=response.headers), patch.dict(os.environ, {"KFM_NO_NETWORK": "0"}), self.assertRaises(ValueError):
                api.fetch(q, opener=Opener(response))
        q = query(max_bytes=2)
        with patch.dict(os.environ, {"KFM_NO_NETWORK": "0"}), self.assertRaisesRegex(ValueError, "RESPONSE_BYTE_LIMIT"):
            api.fetch(q, opener=Opener(Response(q, body=b"123")))
        times = iter([0, 0, 61])
        with patch.dict(os.environ, {"KFM_NO_NETWORK": "0"}), self.assertRaisesRegex(ValueError, "RESPONSE_DEADLINE"):
            api.fetch(query(), opener=Opener(Response(query())), monotonic=lambda: next(times))

    def test_http_and_network_errors_are_finite_without_body_leakage_or_retry(self):
        q = query()
        for code in (400, 404, 429, 500, 503, 302):
            error = HTTPError(q.url(), code, "SECRET", {}, io.BytesIO(b"SECRET"))
            opener = Opener(error=error)
            with patch.dict(os.environ, {"KFM_NO_NETWORK": "0"}), self.assertRaises(ValueError) as context:
                api.fetch(q, opener=opener)
            self.assertNotIn("SECRET", str(context.exception))
            self.assertEqual(len(opener.calls), 1)
        with patch.dict(os.environ, {"KFM_NO_NETWORK": "0"}), self.assertRaisesRegex(ValueError, "PROVIDER_UNAVAILABLE"):
            api.fetch(q, opener=Opener(error=URLError("SECRET")))
        self.assertIsNone(api.NoRedirect().redirect_request(None, None, 302, "x", {}, "http://127.0.0.1"))

    def test_capture_identity_and_every_manifest_boundary_are_rebuilt(self):
        acquired = fake_capture(query())
        for field, value in (("source_role", "aggregate"), ("source_admitted", True),
                             ("published", True), ("url", "https://evil.example"),
                             ("max_bytes", True), ("capture_id", "sha256:" + "0" * 64)):
            manifest = copy.deepcopy(acquired.manifest)
            manifest[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                api.verify_capture(api.Capture(manifest, acquired.raw))
        with self.assertRaises(ValueError):
            api.verify_capture(api.Capture(acquired.manifest, acquired.raw + b" "))


if __name__ == "__main__":
    unittest.main()
