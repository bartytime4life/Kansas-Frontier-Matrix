"""Deterministic synthetic tests; no provider access, station review, or admission claim."""
from dataclasses import FrozenInstanceError
from decimal import Decimal
import importlib.util
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "src/noaa/uscrn_hourly.py"
SPEC = importlib.util.spec_from_file_location("kfm_noaa_uscrn_hourly_tested", PATH)
us = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = us
SPEC.loader.exec_module(us)
NOW = "2026-09-27T12:00:00Z"
URL = us.hourly_url(2023, "KS_Synthetic_1_N")


def line(hour=1, date="20230601", **overrides):
    # Synthetic values only: not a real station, observation, or location.
    values = {"WBANNO": "99999", "UTC_DATE": date, "UTC_TIME": f"{hour:02d}00",
              "LST_DATE": date, "LST_TIME": f"{hour:02d}00", "CRX_VN": "2.623",
              "LONGITUDE": "-98.00", "LATITUDE": "39.00", "T_CALC": "21.4",
              "T_HR_AVG": "21.9", "T_MAX": "22.5", "T_MIN": "21.3", "P_CALC": "0.0",
              "SOLARAD": "450", "SOLARAD_FLAG": "0", "SOLARAD_MAX": "610",
              "SOLARAD_MAX_FLAG": "0", "SOLARAD_MIN": "300", "SOLARAD_MIN_FLAG": "0",
              "SUR_TEMP_TYPE": "C", "SUR_TEMP": "30.1", "SUR_TEMP_FLAG": "0",
              "SUR_TEMP_MAX": "33.0", "SUR_TEMP_MAX_FLAG": "0", "SUR_TEMP_MIN": "27.2",
              "SUR_TEMP_MIN_FLAG": "0", "RH_HR_AVG": "55", "RH_HR_AVG_FLAG": "0",
              **{f"SOIL_MOISTURE_{d}": "0.250" for d in (5, 10, 20, 50, 100)},
              **{f"SOIL_TEMP_{d}": "18.5" for d in (5, 10, 20, 50, 100)}}
    values.update(overrides)
    return " ".join(values[c.name] for c in us.PROFILE)


def parse(lines=None, url=URL, **kwargs):
    body = "\n".join([line()] if lines is None else lines).encode() + b"\n"
    return us.parse_station_year(body, status=200, source_url=url, retrieved_at=NOW, **kwargs)


def measurement(record, name):
    return next(m for m in record.measurements if m.variable == name)


class UrlTests(unittest.TestCase):
    def test_url_and_station(self):
        self.assertTrue(URL.endswith("/hourly02/2023/CRNH0203-2023-KS_Synthetic_1_N.txt"))
        station = us.station_file(URL)
        self.assertEqual((station.year, station.state, station.station),
                         (2023, "KS", "KS_Synthetic_1_N"))
        for bad in (URL.replace("/2023/", "/2022/"), URL.replace("https", "http"),
                    URL.replace("CRNH0203", "CRND0103"), URL + "?x"):
            with self.subTest(bad=bad), self.assertRaises(us.UscrnInputError):
                us.station_file(bad)
        for args in ((1999, "KS_A"), (2023, "ks_a"), (2023, "KS/../x")):
            with self.subTest(args=args), self.assertRaises(us.UscrnInputError):
                us.hourly_url(*args)

    def test_profile_is_38_columns(self):
        self.assertEqual(len(us.PROFILE), 38)
        self.assertEqual(len({c.name for c in us.PROFILE}), 38)


class ParseTests(unittest.TestCase):
    def test_clean_record(self):
        candidate = parse()
        (record,) = candidate.records
        self.assertEqual((record.interval_start_utc, record.interval_end_utc),
                         ("2023-06-01T00:00:00Z", "2023-06-01T01:00:00Z"))
        self.assertEqual(record.route, "RAW_CANDIDATE")
        self.assertEqual(record.surface_temperature_type, "CORRECTED")
        t_calc = measurement(record, "T_CALC")
        self.assertEqual((t_calc.value, t_calc.raw, t_calc.derivation),
                         (Decimal("21.4"), "21.4", "calculated_last_5_min"))
        soil = measurement(record, "SOIL_MOISTURE_20")
        self.assertEqual((soil.depth_cm, soil.unit), (20, "m3/m3"))
        self.assertEqual(measurement(record, "SOLARAD").qc_status, "GOOD")
        self.assertEqual((candidate.wban, candidate.profile_id, candidate.admission),
                         ("99999", "uscrn-hourly02-v1", "NOT_ADMITTED"))
        with self.assertRaises(FrozenInstanceError):
            record.route = "PUBLISHED"

    def test_missing_sentinels_never_become_zero(self):
        (record,) = parse([line(T_HR_AVG="-9999.0", SOIL_MOISTURE_5="-99.000",
                                SOIL_TEMP_100="-9999.0", P_CALC="-9999.0")]).records
        for name in ("T_HR_AVG", "SOIL_MOISTURE_5", "SOIL_TEMP_100", "P_CALC"):
            with self.subTest(name=name):
                item = measurement(record, name)
                self.assertTrue(item.missing)
                self.assertIsNone(item.value)
        self.assertEqual(measurement(record, "SOIL_MOISTURE_5").raw, "-99.000")
        # -99.000 is only a sentinel for soil moisture, not for temperatures.
        (cold,) = parse([line(T_MIN="-9.9")]).records
        self.assertEqual(measurement(cold, "T_MIN").value, Decimal("-9.9"))

    def test_qc_flags_preserved_and_unknown_quarantines(self):
        (flagged,) = parse([line(SOLARAD_FLAG="3")]).records
        item = measurement(flagged, "SOLARAD")
        self.assertEqual((item.value, item.qc_flag_raw, item.qc_status),
                         (Decimal("450"), "3", "FAILED_QC_CHECK"))
        self.assertEqual(flagged.route, "RAW_CANDIDATE")
        (unknown,) = parse([line(RH_HR_AVG_FLAG="7")]).records
        self.assertEqual((unknown.route, unknown.reasons),
                         ("QUARANTINE_CANDIDATE", ("QUALITY_UNKNOWN",)))
        (surface,) = parse([line(SUR_TEMP_TYPE="Z")]).records
        self.assertIn("SURFACE_TEMPERATURE_TYPE_UNKNOWN", surface.reasons)

    def test_gaps_counted_not_filled(self):
        candidate = parse([line(1), line(2), line(5)])
        self.assertEqual(len(candidate.records), 3)
        self.assertEqual(candidate.missing_hours, 2)
        self.assertEqual(candidate.coverage, "NOT_ESTABLISHED")

    def test_midnight_forms(self):
        (late,) = parse([line(24)]).records
        (early,) = parse([line(0, date="20230602")]).records
        self.assertEqual(late.interval_end_utc, early.interval_end_utc)
        with self.assertRaises(us.UscrnInputError):
            parse([line(24), line(0, date="20230602")])

    def test_structural_failures_reject_file(self):
        cases = {
            "SCHEMA_DRIFT": [line() + " 1.0"],
            "TIME_ORDER": [line(2), line(1)],
            "MIXED_STATIONS": [line(1), line(2, WBANNO="99998")],
            "RECORD_OUTSIDE_FILE_YEAR": [line(1, date="20220601")],
            "VALUE_FORMAT": [line(T_MAX="warm")],
            "TIME_FORMAT": [line(UTC_TIME="0130")],
            "STATION_ID": [line(WBANNO="ABCDE")],
            "COORDINATE_RANGE": [line(LATITUDE="95.0")],
            "EMPTY_FILE": [],
        }
        for code, lines in cases.items():
            with self.subTest(code=code), self.assertRaises(us.UscrnInputError) as caught:
                parse(lines)
            self.assertEqual(str(caught.exception), code)
        # Numeric but impossible calendar dates are bounded diagnostics, not ValueError leaks.
        for date in ("20231301", "20230229", "20230431", "20230000"):
            with self.subTest(date=date), self.assertRaises(us.UscrnInputError) as caught:
                parse([line(1, date=date)])
            self.assertEqual(str(caught.exception), "TIME_FORMAT")
        with self.assertRaises(us.UscrnInputError):
            parse([line(1), line(2)], max_records=1)
        with self.assertRaises(us.UscrnInputError):
            us.parse_station_year("é".encode(), status=200, source_url=URL, retrieved_at=NOW)


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            parse()


if __name__ == "__main__":
    unittest.main()
