"""Deterministic synthetic tests; no NRCS access, station review, or rights claim."""
from decimal import Decimal
import importlib.util
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "src/nrcs/scan_awdb.py"
SPEC = importlib.util.spec_from_file_location("kfm_nrcs_scan_awdb_tested", PATH)
sa = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = sa
SPEC.loader.exec_module(sa)
NOW = "2026-09-27T12:00:00Z"
STATIONS = ("99901",)
ELEMENTS = ("SMS:-2", "STO:-2")
URL = sa.data_url(STATIONS, ELEMENTS, duration="DAILY", begin_date="2023-06-01",
                  end_date="2023-06-03")
TRIPLET = "99901:KS:SCAN"
# Request with one depth-free element, for series that state no depth.
LOOSE_URL = sa.data_url(STATIONS, ("SMS:-2", "STO"), duration="DAILY",
                        begin_date="2023-06-01", end_date="2023-06-03")


def element(code="SMS", depth=-2, values=None, **header):
    # Synthetic values only: not a real station, sensor, or observation.
    base = {"elementCode": code, "ordinal": 1, "heightDepth": depth, "durationName": "DAILY",
            "storedUnitCode": "pct"}
    base.update(header)
    base = {k: v for k, v in base.items() if v is not ...}
    if values is None:
        values = [{"date": "2023-06-01", "value": 25.4, "qcFlag": "V", "qaFlag": "P"},
                  {"date": "2023-06-02", "qcFlag": "M"}]
    return {"stationElement": base, "values": values}


def body(elements=None, triplet=TRIPLET, raw=None):
    payload = [{"stationTriplet": triplet,
                "data": [element(), element("STO", values=[{"date": "2023-06-01", "value": 20.5}])]
                if elements is None
                else elements}]
    return (json.dumps(payload) if raw is None else raw).encode()


def parse(payload=None, url=URL, **kwargs):
    return sa.parse_data(body() if payload is None else payload, status=200, source_url=url,
                         retrieved_at=NOW, **kwargs)


class PlannerTests(unittest.TestCase):
    def test_canonical_url_round_trips(self):
        self.assertTrue(URL.startswith("https://wcc.sc.egov.usda.gov/awdbRestApi/services/v1/data?"))
        self.assertIn("stationTriplets=99901%3AKS%3ASCAN", URL)
        request = sa.parse_request(URL)
        self.assertEqual((request.station_ids, request.elements, request.duration),
                         (STATIONS, ELEMENTS, "DAILY"))

    def test_bounded_planning(self):
        cases = {
            "STATION": (((), ELEMENTS), (("0123",), ELEMENTS), (("1", "1"), ELEMENTS),
                        (tuple(str(i) for i in range(1, 12)), ELEMENTS)),
            "ELEMENT": ((STATIONS, ()), (STATIONS, ("sms",)), (STATIONS, ("SMS:-2", "SMS:-2"))),
        }
        for code, arguments in cases.items():
            for stations, elements in arguments:
                with self.subTest(stations=stations, elements=elements), \
                        self.assertRaises(sa.ScanInputError) as ctx:
                    sa.data_url(stations, elements, duration="DAILY", begin_date="2023-06-01",
                                end_date="2023-06-02")
                self.assertEqual(str(ctx.exception), code)
        for kwargs, code in (({"duration": "MONTHLY"}, "DURATION"),
                             ({"end_date": "2024-06-02"}, "DATE_RANGE"),
                             ({"duration": "HOURLY", "end_date": "2023-07-15"}, "DATE_RANGE"),
                             ({"begin_date": "2023-06-05"}, "DATE_RANGE"),
                             ({"begin_date": "2023-02-30"}, "DATE_FORMAT"),
                             ({"begin_date": "1979-12-31"}, "DATE_RANGE")):
            merged = {"duration": "DAILY", "begin_date": "2023-06-01",
                      "end_date": "2023-06-02", **kwargs}
            with self.subTest(kwargs=kwargs), self.assertRaises(sa.ScanInputError) as ctx:
                sa.data_url(STATIONS, ELEMENTS, **merged)
            self.assertEqual(str(ctx.exception), code)

    def test_non_canonical_urls_are_refused(self):
        base = URL.split("?")[0] + "?"
        cases = {
            "SOURCE_URL": (URL.replace("wcc.sc.egov.usda.gov", "example.org"), URL + "#x",
                           URL + "&extra=1", URL.replace("https:", "http:"),
                           base + "duration=DAILY&stationTriplets=99901%3AKS%3ASCAN"
                                  "&elements=SMS%3A-2&beginDate=2023-06-01&endDate=2023-06-02"),
            "STATION_SCOPE": (URL.replace("KS%3ASCAN", "KS%3ATSCAN"),
                              URL.replace("KS%3ASCAN", "NE%3ASCAN")),
            "SOURCE_URL_SCOPE": (URL.replace("%3A", ":"),),
        }
        for code, urls in cases.items():
            for url in urls:
                with self.subTest(url=url), self.assertRaises(sa.ScanInputError) as ctx:
                    sa.parse_request(url)
                self.assertEqual(str(ctx.exception), code)


class ParserTests(unittest.TestCase):
    def test_values_and_flags_are_source_faithful(self):
        candidate = parse()
        series = candidate.series[0]
        self.assertEqual((series.station_triplet, series.element_code, series.ordinal,
                          series.height_depth_raw, series.duration, series.stored_unit),
                         (TRIPLET, "SMS", 1, "-2", "DAILY", "pct"))
        present, missing = series.values
        self.assertEqual((present.raw, present.value, present.qc_flag, present.qa_flag),
                         ("25.4", Decimal("25.4"), "V", "P"))
        self.assertEqual((missing.value, missing.missing, missing.reasons),
                         (None, True, ("VALUE_MISSING",)))
        self.assertEqual((candidate.coverage, candidate.admission),
                         ("NOT_ESTABLISHED", "NOT_ADMITTED"))
        self.assertTrue(series.element_sha256.startswith("sha256:"))

    def test_numbers_never_pass_through_float(self):
        values = parse(body([element(values=[
            {"date": "2023-06-01", "value": 0.1234567890123456789},
            {"date": "2023-06-02", "value": 25.40}, {"date": "2023-06-03", "value": 7}])]),
            url=sa.data_url(STATIONS, ("SMS:-2",), duration="DAILY",
                            begin_date="2023-06-01", end_date="2023-06-03")).series[0].values
        # json.dumps writes the float 0.1234567890123456789 as its shortest repr, so feed
        # the exact token through raw JSON instead.
        exact = parse(body(raw='[{"stationTriplet": "99901:KS:SCAN", "data": [{"stationElement":'
                           ' {"elementCode": "SMS", "ordinal": 1, "heightDepth": -2.0,'
                           ' "durationName": "DAILY"}, "values": [{"date": "2023-06-01",'
                           ' "value": 0.1234567890123456789}, {"date": "2023-06-02",'
                           ' "value": 25.40}, {"date": "2023-06-03", "value": 2.5e-3}]}]}]'),
                      url=sa.data_url(STATIONS, ("SMS:-2",), duration="DAILY",
                                      begin_date="2023-06-01", end_date="2023-06-03"))
        series = exact.series[0]
        self.assertEqual([(v.raw, v.value) for v in series.values],
                         [("0.1234567890123456789", Decimal("0.1234567890123456789")),
                          ("25.40", Decimal("25.40")), ("2.5e-3", Decimal("0.0025"))])
        self.assertIs(type(series.values[0].value), Decimal)
        self.assertEqual(series.height_depth_raw, "-2.0")
        self.assertIn('"heightDepth":"-2.0"', series.raw_element_json)
        self.assertEqual(values[2].raw, "7")

    def test_integer_tokens_are_kept_including_negative_zero(self):
        raw = ('[{"stationTriplet": "99901:KS:SCAN", "data": [{"stationElement":'
               ' {"elementCode": "SMS", "ordinal": 1, "heightDepth": -2,'
               ' "durationName": "DAILY"}, "values": [{"date": "2023-06-01", "value": -0},'
               ' {"date": "2023-06-02", "value": 12}]}, {"stationElement":'
               ' {"elementCode": "STO", "ordinal": 1, "heightDepth": -0,'
               ' "durationName": "DAILY"}, "values": []}]}]')
        url = sa.data_url(STATIONS, ("SMS:-2", "STO"), duration="DAILY",
                          begin_date="2023-06-01", end_date="2023-06-03")
        sms, sto = parse(body(raw=raw), url=url).series
        self.assertEqual([(v.raw, str(v.value)) for v in sms.values],
                         [("-0", "-0"), ("12", "12")])
        self.assertIs(type(sms.ordinal), int)
        self.assertEqual(sto.height_depth_raw, "-0")
        self.assertIn('"heightDepth":"-0"', sto.raw_element_json)
        self.assertIn('"heightDepth":-2', sms.raw_element_json)

    def test_pathologically_nested_headers_are_a_bounded_rejection(self):
        # Deep enough to exceed the explicit bound on every supported Python version.
        nested = '{"a":' * 700 + "1" + "}" * 700
        raw = ('[{"stationTriplet": "99901:KS:SCAN", "data": [{"stationElement":'
               ' {"elementCode": "SMS", "heightDepth": -2, "durationName": "DAILY",'
               ' "extra": ' + nested + '}, "values": []}]}]')
        with self.assertRaises(sa.ScanInputError) as ctx:
            parse(body(raw=raw))
        self.assertEqual(str(ctx.exception), "NESTING_DEPTH")

    def test_pathologically_nested_values_are_a_bounded_rejection(self):
        # Deep enough to exceed the explicit bound on every supported Python version.
        nested = '{"a":' * 700 + "1" + "}" * 700
        raw = ('[{"stationTriplet": "99901:KS:SCAN", "data": [{"stationElement":'
               ' {"elementCode": "SMS", "heightDepth": -2, "durationName": "DAILY"},'
               ' "values": [{"date": "2023-06-01", "value": ' + nested + '}]}]}]')
        with self.assertRaises(sa.ScanInputError) as ctx:
            parse(body(raw=raw))
        self.assertEqual(str(ctx.exception), "NESTING_DEPTH")

    def test_modest_excess_nesting_is_rejected_by_the_explicit_bound(self):
        nested = '{"a":' * 25 + "1" + "}" * 25
        raw = ('[{"stationTriplet": "99901:KS:SCAN", "data": [{"stationElement":'
               ' {"elementCode": "SMS", "heightDepth": -2, "durationName": "DAILY",'
               ' "extra": ' + nested + '}, "values": []}]}]')
        with self.assertRaises(sa.ScanInputError) as ctx:
            parse(body(raw=raw))
        self.assertEqual(str(ctx.exception), "NESTING_DEPTH")
        self.assertEqual(sa.MAX_NESTING, 16)

    def test_numbers_outside_decimal_range_reject_as_invalid_json(self):
        for token in ("1e" + "9" * 100, "1" * 5000):
            raw = ('[{"stationTriplet": "99901:KS:SCAN", "data": [{"stationElement":'
                   ' {"elementCode": "SMS", "durationName": "DAILY"}, "values":'
                   ' [{"date": "2023-06-01", "value": ' + token + '}]}]}]')
            with self.subTest(token=token[:12]), self.assertRaises(sa.ScanInputError) as ctx:
                parse(body(raw=raw))
            self.assertEqual(str(ctx.exception), "INVALID_JSON")

    def test_value_level_quarantine_and_series_flags(self):
        candidate = parse(body([element(values=[{"date": "2023-06-01", "value": "25.4"}]),
                                element("STO", depth=None, values=[])]), url=LOOSE_URL)
        series = candidate.series
        self.assertEqual(series[0].values[0].route, "QUARANTINE_CANDIDATE")
        self.assertEqual(series[0].values[0].reasons, ("VALUE_NOT_NUMERIC",))
        self.assertEqual(series[1].reasons, ("EMPTY_SERIES_NOT_ABSENCE", "DEPTH_NOT_STATED"))
        self.assertEqual(candidate.unreturned, ())

    def test_unreturned_requested_series_are_listed_not_filled(self):
        self.assertEqual(parse(body([element()])).unreturned, (f"{TRIPLET}|STO:-2",))
        self.assertEqual(parse(body(raw="[]")).unreturned,
                         (f"{TRIPLET}|SMS:-2", f"{TRIPLET}|STO:-2"))

    def test_series_must_match_requested_depth_and_ordinal(self):
        ordinal_url = sa.data_url(STATIONS, ("SMS:-2:1",), duration="DAILY",
                                  begin_date="2023-06-01", end_date="2023-06-03")
        self.assertEqual(parse(body([element()]), url=ordinal_url).series[0].ordinal, 1)
        for url, header in ((URL, {"depth": -8}), (URL, {"depth": None}),
                            (ordinal_url, {"ordinal": 2})):
            with self.subTest(header=header), self.assertRaises(sa.ScanInputError) as ctx:
                parse(body([element(**header)]), url=url)
            self.assertEqual(str(ctx.exception), "ELEMENT_NOT_REQUESTED")

    def test_value_dates_follow_the_duration_layout(self):
        for stamp in ("2023-06-01garbage", "2023-06-01 01:00", "2023-6-1", "2023-06-01T00:00"):
            with self.subTest(stamp=stamp), self.assertRaises(sa.ScanInputError) as ctx:
                parse(body([element(values=[{"date": stamp, "value": 1}])]))
            self.assertEqual(str(ctx.exception), "VALUE_DATE")
        hourly = sa.data_url(STATIONS, ("SMS:-2",), duration="HOURLY",
                             begin_date="2023-06-01", end_date="2023-06-01")
        values = parse(body([element(durationName="HOURLY", values=[
            {"date": "2023-06-01 01:00", "value": 1}])]), url=hourly).series[0].values
        self.assertEqual(values[0].date, "2023-06-01 01:00")
        with self.assertRaises(sa.ScanInputError):
            parse(body([element(durationName="HOURLY", values=[
                {"date": "2023-06-01", "value": 1}])]), url=hourly)

    def test_scope_and_shape_drift_reject_whole_response(self):
        cases = {
            "STATION_NOT_REQUESTED": body(triplet="99902:KS:SCAN"),
            "ELEMENT_NOT_REQUESTED": body([element("PREC")]),
            "DURATION_MISMATCH": body([element(durationName="HOURLY")]),
            "VALUE_DATE": body([element(values=[{"date": "2023-06-04", "value": 1}])]),
            "DUPLICATE_VALUE_DATE": body([element(values=[{"date": "2023-06-01", "value": 1},
                                                          {"date": "2023-06-01", "value": 2}])]),
            "ELEMENT_SHAPE": body([element(ordinal="1")]),
            "FLAG_SHAPE": body([element(values=[{"date": "2023-06-01", "qcFlag": 3}])]),
            "RESPONSE_SHAPE": body(raw='{"stationTriplet": "x"}'),
            "STATION_SHAPE": body(raw='[{"stationTriplet": "99901:KS:SCAN"}]'),
            "DUPLICATE_STATION": body(raw=json.dumps([{"stationTriplet": TRIPLET, "data": []}] * 2)),
            "DUPLICATE_SERIES": body([element(), element()]),
            "INVALID_JSON": body(raw='[{"stationTriplet": "99901:KS:SCAN", "data": NaN}]'),
            "VALUE_SHAPE": body([element(values=[{"value": 1}])]),
        }
        for code, payload in cases.items():
            with self.subTest(code=code), self.assertRaises(sa.ScanInputError) as ctx:
                parse(payload)
            self.assertEqual(str(ctx.exception), code)
        for kwargs, code in (({"status": 404}, "HTTP_STATUS"),
                             ({"retrieved_at": "yesterday"}, "UTC_TIME")):
            merged = {"status": 200, "source_url": URL, "retrieved_at": NOW, **kwargs}
            with self.subTest(code=code), self.assertRaises(sa.ScanInputError) as ctx:
                sa.parse_data(body(), **merged)
            self.assertEqual(str(ctx.exception), code)
        with self.assertRaises(sa.ScanInputError):
            parse(max_values=1)

    def test_malformed_values_never_escape_as_other_errors(self):
        for value in ({"date": 5}, {"date": "2023-13-01"}, [], "x", {"date": "2023-06-01",
                                                                   "value": {"n": 1}}):
            with self.subTest(value=value):
                try:
                    parse(body([element(values=[value])]))
                except sa.ScanInputError:
                    pass


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            parse()


if __name__ == "__main__":
    unittest.main()
