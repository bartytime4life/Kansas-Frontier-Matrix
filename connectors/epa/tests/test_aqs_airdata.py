"""Deterministic synthetic tests; no EPA access, monitor review, or rights claim."""
import csv
from decimal import Decimal
import importlib.util
import io
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch
import zipfile

PATH = Path(__file__).resolve().parents[1] / "src/epa/aqs_airdata.py"
SPEC = importlib.util.spec_from_file_location("kfm_epa_aqs_airdata_tested", PATH)
aq = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = aq
SPEC.loader.exec_module(aq)
NOW = "2026-09-28T12:00:00Z"
URL = aq.daily_url("88101", 2023)
MEMBER = "daily_88101_2023.csv"
HEADER = list(aq.REQUIRED_COLUMNS)


def row(**overrides):
    # Synthetic values only: not a real monitor, site, or observation.
    base = {"State Code": "20", "County Code": "999", "Site Num": "9001",
            "Parameter Code": "88101", "POC": "1", "Latitude": "38.500000",
            "Longitude": "-98.250000", "Datum": "WGS84",
            "Parameter Name": "PM2.5 - Local Conditions", "Sample Duration": "24 HOUR",
            "Pollutant Standard": "PM25 24-hour 2012", "Date Local": "2023-06-01",
            "Units of Measure": "Micrograms/cubic meter (LC)", "Event Type": "No Events",
            "Observation Count": "1", "Observation Percent": "100.0",
            "Arithmetic Mean": "7.30", "1st Max Value": "7.3", "1st Max Hour": "0",
            "AQI": "30", "Method Code": "000", "Method Name": "Synthetic method",
            "Local Site Name": "Synthetic site", "Address": "Synthetic address",
            "State Name": "Kansas", "County Name": "Synthetic", "City Name": "Synthetic",
            "CBSA Name": "", "Date of Last Change": "2024-01-01"}
    base.update(overrides)
    return base


def csv_bytes(rows, header=HEADER):
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, quoting=csv.QUOTE_ALL, lineterminator="\n")
    writer.writerow(header)
    for item in rows:
        writer.writerow([item.get(column, "") for column in header]
                        if isinstance(item, dict) else item)
    return buffer.getvalue().encode("utf-8")


def archive(rows=None, *, member=MEMBER, data=None, extra=(), header=HEADER):
    payload = csv_bytes([row()] if rows is None else rows, header) if data is None else data
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as out:
        out.writestr(member, payload)
        for name, content in extra:
            out.writestr(name, content)
    return buffer.getvalue()


def parse(body=None, url=URL, **kwargs):
    return aq.parse_daily_file(archive() if body is None else body, status=200,
                               source_url=url, retrieved_at=NOW, **kwargs)


def rejected(test, code, body=None, **kwargs):
    with test.assertRaises(aq.AqsInputError) as ctx:
        parse(body, **kwargs)
    test.assertEqual(ctx.exception.args[0], code)


class PlannerTests(unittest.TestCase):
    def test_canonical_url_round_trips(self):
        self.assertEqual(URL, "https://aqs.epa.gov/aqsweb/airdata/daily_88101_2023.zip")
        self.assertEqual(aq.daily_file(URL), aq.DailyFile("88101", 2023, "daily_88101_2023.zip"))
        self.assertEqual(aq.daily_file(URL).member_name, MEMBER)

    def test_bounded_planning(self):
        for parameter, year, code in (("88101", 1979, "INTEGER_BOUND"),
                                      ("88101", True, "INTEGER_BOUND"),
                                      ("12345", 2023, "PARAMETER_SCOPE"),
                                      (88101, 2023, "PARAMETER_SCOPE")):
            with self.subTest(parameter=parameter, year=year), \
                    self.assertRaises(aq.AqsInputError) as ctx:
                aq.daily_url(parameter, year)
            self.assertEqual(ctx.exception.args[0], code)

    def test_only_canonical_urls(self):
        for url, code in ((URL + "?x=1", "SOURCE_URL"),
                          (URL.replace("https://", "http://"), "SOURCE_URL"),
                          (URL.replace("aqs.epa.gov", "evil.example"), "SOURCE_URL"),
                          (URL.replace("daily_", "hourly_"), "SOURCE_URL"),
                          (URL.replace("88101", "12345"), "PARAMETER_SCOPE"),
                          (URL.replace("2023", "1970"), "INTEGER_BOUND"),
                          (None, "SOURCE_URL")):
            with self.subTest(url=url), self.assertRaises(aq.AqsInputError) as ctx:
                aq.daily_file(url)
            self.assertEqual(ctx.exception.args[0], code)


class ParseTests(unittest.TestCase):
    def test_kansas_rows_are_exact_and_other_states_skipped(self):
        other = row(**{"State Code": "19", "County Code": "abc"})
        result = parse(archive([row(), other, row(**{"Date Local": "2023-06-02"})]))
        self.assertEqual((result.rows_total, len(result.records)), (3, 2))
        record = result.records[0]
        self.assertEqual((record.site_id, record.poc, record.date_local, record.route),
                         ("20-999-9001", 1, "2023-06-01", "RAW_CANDIDATE"))
        self.assertEqual(str(record.arithmetic_mean), "7.30")
        self.assertEqual(record.observation_percent, Decimal("100.0"))
        self.assertEqual((record.aqi, record.first_max_hour, record.observation_count),
                         (30, 0, 1))
        self.assertEqual(str(record.latitude), "38.500000")
        self.assertEqual(json.loads(record.raw_record_json)["Arithmetic Mean"], "7.30")
        self.assertEqual((result.scope, result.coverage, record.admission),
                         ("STATE_CODE_20_ROWS", "NOT_ESTABLISHED", "NOT_ADMITTED"))
        self.assertEqual(result.member_bytes, len(csv_bytes([row(), other,
                                                             row(**{"Date Local": "2023-06-02"})])))

    def test_flags_and_quarantine(self):
        cases = ((row(**{"Event Type": "Events Included"}), ("EVENTS_INCLUDED",),
                  "RAW_CANDIDATE"),
                 (row(**{"Event Type": "Events Excluded"}), ("EVENTS_EXCLUDED",),
                  "RAW_CANDIDATE"),
                 (row(**{"Event Type": "Concurred Events Excluded"}),
                  ("CONCURRED_EVENTS_EXCLUDED",), "RAW_CANDIDATE"),
                 (row(**{"Event Type": "None"}), (), "RAW_CANDIDATE"),
                 (row(**{"Event Type": "Included"}), ("EVENTS_INCLUDED",), "RAW_CANDIDATE"),
                 (row(**{"Event Type": "Excluded"}), ("EVENTS_EXCLUDED",), "RAW_CANDIDATE"),
                 (row(**{"Event Type": "Concurred"}), ("CONCURRED_EVENTS_EXCLUDED",),
                  "RAW_CANDIDATE"),
                 (row(**{"Event Type": "events included"}), ("EVENT_TYPE_UNRECOGNIZED",),
                  "QUARANTINE_CANDIDATE"),
                 (row(AQI=""), ("AQI_NOT_REPORTED",), "RAW_CANDIDATE"),
                 (row(**{"Event Type": "Other"}), ("EVENT_TYPE_UNRECOGNIZED",),
                  "QUARANTINE_CANDIDATE"),
                 (row(**{"Arithmetic Mean": "1e3"}), ("NUMBER_UNPARSEABLE",),
                  "QUARANTINE_CANDIDATE"),
                 (row(**{"1st Max Hour": "24"}), ("NUMBER_UNPARSEABLE",),
                  "QUARANTINE_CANDIDATE"),
                 (row(AQI="-1"), ("NUMBER_UNPARSEABLE",), "QUARANTINE_CANDIDATE"),
                 (row(Latitude="98.0"), ("COORDINATE_UNPARSEABLE",), "QUARANTINE_CANDIDATE"),
                 (row(Longitude=""), ("COORDINATE_UNPARSEABLE",), "QUARANTINE_CANDIDATE"))
        for item, reasons, route in cases:
            with self.subTest(reasons=reasons, item=item["Event Type"]):
                (record,) = parse(archive([item])).records
                self.assertEqual((record.reasons, record.route), (reasons, route))
        (bad,) = parse(archive([row(**{"Arithmetic Mean": "x"})])).records
        self.assertIsNone(bad.arithmetic_mean)
        (blank,) = parse(archive([row(AQI="")])).records
        self.assertIsNone(blank.aqi)

    def test_negative_and_zero_values_stay_verbatim(self):
        (record,) = parse(archive([row(**{"Arithmetic Mean": "-0.4",
                                          "1st Max Value": "0.0"})])).records
        self.assertEqual((str(record.arithmetic_mean), str(record.first_max_value)),
                         ("-0.4", "0.0"))

    def test_same_day_distinct_standards_and_events_are_distinct_rows(self):
        rows = [row(), row(**{"Pollutant Standard": "PM25 Annual 2012"}),
                row(**{"Event Type": "Events Included"}), row(POC="2")]
        self.assertEqual(len(parse(archive(rows)).records), 4)
        rejected(self, "DUPLICATE_RECORD", archive([row(), row()]))

    def test_structural_rejections(self):
        cases = (
            ("SCHEMA_DRIFT", archive(header=HEADER[:-1])),
            ("DUPLICATE_COLUMN", archive(header=HEADER + ["AQI"])),
            ("HEADER_MISSING", archive(data=b"")),
            ("ROW_WIDTH", archive(data=csv_bytes([["20", "999"]]))),
            ("PARAMETER_MISMATCH", archive([row(**{"Parameter Code": "44201",
                                                   "State Code": "19"})])),
            ("ROW_OUTSIDE_DATA_YEAR", archive([row(**{"Date Local": "2022-12-31"})])),
            ("DATE_FORMAT", archive([row(**{"Date Local": "2023-02-30"})])),
            ("SITE_IDENTITY", archive([row(**{"County Code": "99"})])),
            ("POC_FORMAT", archive([row(POC="0")])),
            ("ROW_IDENTITY", archive([row(**{"Sample Duration": ""})])),
            ("ENCODING", archive(data=csv_bytes([row()]) + b"\xff\xfe")),
            ("CSV_STRUCTURE", archive(data=csv_bytes([]) + b'"unterminated\n')),
        )
        for code, body in cases:
            with self.subTest(code=code):
                rejected(self, code, body)

    def test_archive_rejections(self):
        # zipfile will not write an encrypted member; set the flag bit in both headers.
        encrypted = bytearray(archive())
        encrypted[6] |= 0x1
        encrypted[encrypted.rindex(b"PK\x01\x02") + 8] |= 0x1
        corrupt = bytearray(archive())
        corrupt[60] ^= 0xFF
        cases = (
            ("NOT_ZIP", b"not a zip"),
            ("ZIP_MEMBERS", archive(extra=(("README.txt", b"x"),))),
            ("ZIP_MEMBER_NAME", archive(member="daily_44201_2023.csv")),
            ("ZIP_MEMBER_NAME", archive(member="../" + MEMBER)),
            ("ZIP_ENCRYPTED", bytes(encrypted)),
            ("ZIP_CORRUPT", bytes(corrupt)),
            ("ZIP_CORRUPT", archive()[:40]),
        )
        for code, body in cases:
            with self.subTest(code=code):
                rejected(self, code, body)

    def test_decompression_is_bounded(self):
        filler = [row(**{"State Code": "19"})] * 20_000
        bomb = archive(filler)
        rejected(self, "COMPRESSION_RATIO", bomb)
        rejected(self, "DECOMPRESSED_BOUND", archive([row()]), max_member_bytes=100)

    def test_row_bounds(self):
        rows = [row(**{"Date Local": f"2023-06-0{day}"}) for day in range(1, 4)]
        rejected(self, "ROW_BOUND", archive(rows), max_rows_total=2)
        rejected(self, "KANSAS_ROW_BOUND", archive(rows), max_rows=2)

    def test_response_rejections(self):
        for kwargs, code in (({"status": 404}, "HTTP_STATUS"),
                             ({"retrieved_at": "yesterday"}, "UTC_TIME"),
                             ({"body": b"x" * 11, "max_bytes": 10}, "RESPONSE_BOUND")):
            args = {"body": archive(), "status": 200, "source_url": URL, "retrieved_at": NOW}
            args.update(kwargs)
            with self.subTest(code=code), self.assertRaises(aq.AqsInputError) as ctx:
                aq.parse_daily_file(**args)
            self.assertEqual(ctx.exception.args[0], code)

    def test_empty_kansas_selection_is_not_absence(self):
        result = parse(archive([row(**{"State Code": "19"})]))
        self.assertEqual((result.rows_total, result.records, result.coverage),
                         (1, (), "NOT_ESTABLISHED"))


class NoNetworkTests(unittest.TestCase):
    def test_parsing_opens_no_socket(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            parse()


if __name__ == "__main__":
    unittest.main()
