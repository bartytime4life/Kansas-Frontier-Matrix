"""Deterministic synthetic tests; no provider access, finalization, or sensitivity claim."""
import csv
from dataclasses import FrozenInstanceError, replace
import gzip
import importlib.util
import io
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "src/noaa/storm_events.py"
SPEC = importlib.util.spec_from_file_location("kfm_noaa_storm_events_tested", PATH)
se = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = se
SPEC.loader.exec_module(se)
NOW = "2026-09-26T12:00:00Z"
URL = se.details_url(2020, "20260915")
COLUMNS = (*se.REQUIRED_COLUMNS, "DATA_SOURCE")


def row(event_id=1, **overrides):
    # Synthetic values only: no real event, place, casualty, or narrative.
    base = {"BEGIN_YEARMONTH": "202005", "BEGIN_DAY": "1", "BEGIN_TIME": "1530",
            "END_YEARMONTH": "202005", "END_DAY": "1", "END_TIME": "1545",
            "EPISODE_ID": "100", "EVENT_ID": str(event_id), "STATE": "KANSAS",
            "STATE_FIPS": "20", "EVENT_TYPE": "Hail", "CZ_TYPE": "C", "CZ_FIPS": "1",
            "CZ_NAME": "SYNTHETIC", "CZ_TIMEZONE": "CST-6", "INJURIES_DIRECT": "0",
            "INJURIES_INDIRECT": "0", "DEATHS_DIRECT": "0", "DEATHS_INDIRECT": "0",
            "DAMAGE_PROPERTY": "10.00K", "DAMAGE_CROPS": "0.00K", "MAGNITUDE": "1.75",
            "MAGNITUDE_TYPE": "", "TOR_F_SCALE": "", "BEGIN_LAT": "38.5",
            "BEGIN_LON": "-98.5", "END_LAT": "38.5", "END_LON": "-98.4",
            "EPISODE_NARRATIVE": "Synthetic episode text.",
            "EVENT_NARRATIVE": "Synthetic event text, with a comma.", "DATA_SOURCE": "CSV"}
    base.update(overrides)
    return base


def gz(rows, columns=COLUMNS):
    text = io.StringIO(newline="")
    writer = csv.writer(text, lineterminator="\n")
    writer.writerow(columns)
    for item in rows:
        writer.writerow([item.get(column, "") for column in columns])
    return gzip.compress(text.getvalue().encode("utf-8"), mtime=0)


def parse(rows=None, url=URL, **kwargs):
    return se.parse_details_file(gz([row()] if rows is None else rows), status=200,
                                 source_url=url, retrieved_at=NOW, **kwargs)


class VintageTests(unittest.TestCase):
    def test_url_and_vintage(self):
        self.assertTrue(URL.endswith("StormEvents_details-ftp_v1.0_d2020_c20260915.csv.gz"))
        vintage = se.file_vintage(URL)
        self.assertEqual((vintage.data_year, vintage.created), (2020, "20260915"))

    def test_rejected_urls(self):
        for bad in (URL.replace("https://", "http://"), URL.replace("details", "fatalities"),
                    URL.replace("c20260915", "c20261399"), se.details_url(2020, "20190101"),
                    URL + "?x=1", URL.replace("www.ncei", "evil.ncei")):
            with self.subTest(bad=bad), self.assertRaises(se.StormEventsInputError):
                se.file_vintage(bad)
        for args in ((1949, "20200101"), (2020, "2020-01-01")):
            with self.subTest(args=args), self.assertRaises(se.StormEventsInputError):
                se.details_url(*args)


class DamageTests(unittest.TestCase):
    def test_exact_parsing(self):
        self.assertEqual(se.parse_damage("10.00K"), 10_000)
        self.assertEqual(se.parse_damage("1.5M"), 1_500_000)
        self.assertEqual(se.parse_damage("2B"), 2_000_000_000)
        self.assertEqual(se.parse_damage("0.00K"), 0)
        self.assertEqual(se.parse_damage("250"), 250)
        self.assertIsNone(se.parse_damage(""))
        for bad in ("1.2345K", "K", "10X", "-5K", "1e3"):
            with self.subTest(bad=bad), self.assertRaises(se.StormEventsInputError):
                se.parse_damage(bad)


class ParseTests(unittest.TestCase):
    def test_clean_row(self):
        (event,) = parse().events
        self.assertEqual(event.route, "RAW_CANDIDATE")
        self.assertEqual((event.begin_local, event.begin_utc),
                         ("2020-05-01T15:30", "2020-05-01T21:30Z"))
        self.assertEqual((event.damage_property_usd, event.damage_crops_usd), (10_000, 0))
        self.assertEqual(event.damage_property_source, "10.00K")
        self.assertEqual(event.magnitude_source, "1.75")
        self.assertEqual((event.narrative_sensitivity_flag, event.finalized_state,
                          event.admission), ("unreviewed", "NOT_DETERMINED", "NOT_ADMITTED"))
        self.assertIn("with a comma", event.raw_record_json)
        self.assertIn('"DATA_SOURCE":"CSV"', event.raw_record_json)
        with self.assertRaises(FrozenInstanceError):
            event.narrative_sensitivity_flag = "cleared"

    def test_flags_that_do_not_quarantine(self):
        (event,) = parse([row(EPISODE_ID="", EVENT_TYPE="THUNDERSTORM WINDS",
                              CZ_TIMEZONE="CST", BEGIN_LAT="", BEGIN_LON="",
                              DAMAGE_PROPERTY="")]).events
        self.assertEqual(event.route, "RAW_CANDIDATE")
        self.assertEqual(event.reasons, ("EPISODE_ID_ABSENT", "EVENT_TYPE_OUTSIDE_DIRECTIVE",
                                         "UTC_OFFSET_UNKNOWN", "ZONE_OR_COUNTY_SUPPORT_ONLY"))
        self.assertIsNone(event.begin_utc)
        self.assertIsNone(event.damage_property_usd)

    def test_unreadable_values_quarantine_with_source_kept(self):
        cases = {"DAMAGE_UNPARSEABLE": {"DAMAGE_CROPS": "lots"},
                 "CASUALTY_UNPARSEABLE": {"DEATHS_DIRECT": "-1"},
                 "END_BEFORE_BEGIN": {"END_TIME": "1400"}}
        for reason, overrides in cases.items():
            with self.subTest(reason=reason):
                (event,) = parse([row(**overrides)]).events
                self.assertEqual(event.route, "QUARANTINE_CANDIDATE")
                self.assertIn(reason, event.reasons)
        (event,) = parse([row(DAMAGE_CROPS="lots")]).events
        self.assertEqual(event.damage_crops_source, "lots")

    def test_structural_failures_reject_file(self):
        missing = tuple(c for c in COLUMNS if c != "EVENT_NARRATIVE")
        cases = {
            "duplicate event": gz([row(1), row(1)]),
            "schema drift": gz([row()], columns=missing),
            "duplicate column": gz([row()], columns=(*COLUMNS, "EVENT_ID")),
            "wrong year": gz([row(BEGIN_YEARMONTH="201912")]),
            "bad identity": gz([row(EVENT_ID="abc")]),
            "half coordinate": gz([row(BEGIN_LAT="")]),
            "bad latitude": gz([row(BEGIN_LAT="91")]),
            "bad time": gz([row(BEGIN_TIME="2575")]),
            "short row": gzip.compress((",".join(COLUMNS) + "\n1,2\n").encode()),
            "not gzip": b"BEGIN_YEARMONTH\n",
            "corrupt gzip": gz([row()])[:-8],
        }
        for name, body in cases.items():
            with self.subTest(name=name), self.assertRaises(se.StormEventsInputError):
                se.parse_details_file(body, status=200, source_url=URL, retrieved_at=NOW)
        with self.assertRaises(se.StormEventsInputError):
            parse([row(1), row(2)], max_rows=1)
        with self.assertRaises(se.StormEventsInputError):
            parse(max_bytes=100)
        bomb = gz([row(EVENT_NARRATIVE="x" * 200_000)])
        self.assertLess(len(bomb), 2_000)
        with self.assertRaises(se.StormEventsInputError) as caught:
            se.parse_details_file(bomb, status=200, source_url=URL, retrieved_at=NOW,
                                  max_bytes=10_000)
        self.assertEqual(str(caught.exception), "DECOMPRESSED_BOUND")
        with self.assertRaises(se.StormEventsInputError):
            se.parse_details_file(gz([row()]), status=404, source_url=URL, retrieved_at=NOW)

    def test_errors_do_not_echo_payload(self):
        secret = "123 PRIVATE ROAD"
        with self.assertRaises(se.StormEventsInputError) as caught:
            parse([row(EVENT_ID=secret)])
        self.assertNotIn(secret, str(caught.exception))

    def test_select_state(self):
        parsed = parse([row(1), row(2, STATE_FIPS="40", STATE="OKLAHOMA")])
        self.assertEqual([e.event_id for e in se.select_state(parsed)], [1])
        self.assertEqual(parsed.coverage, "NOT_ESTABLISHED")


class VintageDeltaTests(unittest.TestCase):
    def test_corrections_are_named_not_merged(self):
        older = parse([row(1), row(2), row(3)])
        newer = parse([row(1), row(2, DAMAGE_PROPERTY="20.00K"), row(4)],
                      url=se.details_url(2020, "20261001"))
        delta = se.compare_vintages(older, newer)
        self.assertEqual((delta.added, delta.removed, delta.changed, delta.unchanged),
                         ((4,), (3,), (2,), 1))

    def test_vintage_order_and_year_enforced(self):
        older = parse()
        with self.assertRaises(se.StormEventsInputError):
            se.compare_vintages(older, older)
        other_year = replace(older, vintage=se.FileVintage(2021, "20270101", "x"))
        with self.assertRaises(se.StormEventsInputError):
            se.compare_vintages(older, other_year)


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            se.select_state(parse())


if __name__ == "__main__":
    unittest.main()
