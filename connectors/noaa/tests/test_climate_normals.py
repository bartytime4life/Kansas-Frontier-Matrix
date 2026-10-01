"""Synthetic, no-network conformance for NOAA monthly-normal intake."""
from __future__ import annotations

import csv
from hashlib import sha256
from io import StringIO
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "connectors/noaa/src"))

from noaa.climate_normals import (INVENTORY_KEY, NormalsError, object_url,
                                  parse_inventory, parse_station, station_key)  # noqa: E402
from noaa.climate_normals_capture import Capture, canonical_bytes, capture  # noqa: E402
from pipelines.domains.atmosphere.noaa_normals import normalize_capture, project_station_points  # noqa: E402


def inventory_line(station_id="USC00140010", state="KS"):
    return f"{station_id:<11} {38.9267:8.4f} {-97.2128:9.4f} {361.8:6.1f} {state} {'ABILENE':<30}".ljust(85)


INVENTORY = (inventory_line() + "\n" + inventory_line("USC00240010", "MO") + "\n").encode()
FIELDS = ["STATION", "DATE", "LATITUDE", "LONGITUDE", "NAME", "month",
          "MLY-TAVG-NORMAL", "meas_flag_MLY-TAVG-NORMAL", "comp_flag_MLY-TAVG-NORMAL",
          "years_MLY-TAVG-NORMAL", "MLY-PRCP-NORMAL", "meas_flag_MLY-PRCP-NORMAL",
          "comp_flag_MLY-PRCP-NORMAL", "years_MLY-PRCP-NORMAL"]


def station_csv(*, missing=False, provisional=False):
    out = StringIO()
    writer = csv.DictWriter(out, fieldnames=FIELDS)
    writer.writeheader()
    for month in range(1, 13):
        writer.writerow({"STATION": "USC00140010", "DATE": f"{month:02d}",
                         "LATITUDE": "38.9267", "LONGITUDE": "-97.2128",
                         "NAME": "ABILENE, KS US", "month": f"{month:02d}",
                         "MLY-TAVG-NORMAL": "-9999" if missing and month == 2 else "32.5",
                         "meas_flag_MLY-TAVG-NORMAL": "",
                         "comp_flag_MLY-TAVG-NORMAL": "" if missing and month == 2 else "S",
                         "years_MLY-TAVG-NORMAL": "" if missing and month == 2 else "27",
                         "MLY-PRCP-NORMAL": "0.86", "meas_flag_MLY-PRCP-NORMAL": "",
                         "comp_flag_MLY-PRCP-NORMAL": "P" if provisional else "S",
                         "years_MLY-PRCP-NORMAL": "20" if provisional else "27"})
    return out.getvalue().encode()


class NormalTests(unittest.TestCase):
    def test_kansas_inventory_and_url_scope(self):
        stations = parse_inventory(INVENTORY)
        self.assertEqual([s["station_id"] for s in stations], ["USC00140010"])
        self.assertEqual(object_url(station_key("USC00140010")),
                         "https://noaa-normals-pds.s3.amazonaws.com/normals-monthly/1991-2020/access/USC00140010.csv")
        for invalid in ("../evil", "USC00140010?x", "USC00140010/"):
            with self.assertRaises(NormalsError):
                station_key(invalid)

    def test_values_flags_and_missing_are_preserved(self):
        station = parse_inventory(INVENTORY)[0]
        item = parse_station(station_csv(missing=True, provisional=True), station)
        self.assertEqual(item["months"][0]["temperature_f"]["value"], "32.5")
        self.assertEqual(item["months"][1]["temperature_f"]["value"], None)
        self.assertEqual(item["months"][0]["precipitation_in"]["completeness_flag"], "P")
        self.assertEqual(item["months"][0]["precipitation_in"]["years"], 20)

    def test_wrong_station_month_and_location_rejected(self):
        station = parse_inventory(INVENTORY)[0]
        for old, new in ((b"USC00140010", b"USC00140011"),
                         (b"ABILENE, KS US", b"ABILENE, MO US"),
                         (b"38.9267", b"35.9267")):
            with self.assertRaises(NormalsError):
                parse_station(station_csv().replace(old, new), station)
        with self.assertRaises(NormalsError):
            parse_station(station_csv().replace(b",02,", b",03,", 1), station)

    def test_capture_replay_is_deterministic_and_partial_is_held(self):
        raw = station_csv()
        def fake(key, limit):
            if key == INVENTORY_KEY:
                return INVENTORY, {"retrieved_at": "2026-10-01T00:00:00Z", "status": 200}
            return raw, {"retrieved_at": "2026-10-01T00:00:01Z", "status": 200}
        acquired = capture(fetcher=fake)
        first = normalize_capture(acquired.manifest, acquired.objects)
        second = normalize_capture(acquired.manifest, acquired.objects)
        self.assertEqual(first["candidate_id"], second["candidate_id"])
        self.assertEqual(first["station_count"], 1)
        self.assertEqual(first["release_state"], "UNRELEASED")
        damaged = dict(acquired.objects)
        damaged["sha256:" + sha256(raw).hexdigest()] = b"changed"
        with self.assertRaises(ValueError):
            normalize_capture(acquired.manifest, damaged)
        partial = dict(acquired.manifest, complete=False, failed_station_ids=["USC00140010"])
        with self.assertRaises(ValueError):
            normalize_capture(partial, acquired.objects)

    def test_review_map_is_station_points_only_and_unreleased(self):
        def fake(key, limit):
            raw = INVENTORY if key == INVENTORY_KEY else station_csv(missing=True)
            return raw, {"retrieved_at": "2026-10-01T00:00:00Z", "status": 200}
        acquired = capture(fetcher=fake)
        candidate = normalize_capture(acquired.manifest, acquired.objects)
        january = project_station_points(candidate, month=1, variable="temperature_f")
        self.assertEqual(len(january["features"]), 1)
        self.assertEqual(january["features"][0]["geometry"]["type"], "Point")
        self.assertEqual(january["features"][0]["properties"]["value"], 32.5)
        self.assertEqual(january["features"][0]["properties"]["completeness_flag"], "S")
        self.assertEqual(january["release_state"], "UNRELEASED")
        february = project_station_points(candidate, month=2, variable="temperature_f")
        self.assertEqual(february["features"], [])
        for month, variable in ((0, "temperature_f"), (13, "temperature_f"), (1, "unknown")):
            with self.assertRaises(ValueError):
                project_station_points(candidate, month=month, variable=variable)

    def test_provider_failure_cannot_form_complete_candidate(self):
        def fake(key, limit):
            if key == INVENTORY_KEY:
                return INVENTORY, {"retrieved_at": "2026-10-01T00:00:00Z", "status": 200}
            raise NormalsError("PROVIDER_UNAVAILABLE")
        acquired = capture(fetcher=fake)
        self.assertFalse(acquired.manifest["complete"])
        self.assertEqual(acquired.manifest["failed_station_ids"], ["USC00140010"])
        with self.assertRaises(ValueError):
            normalize_capture(acquired.manifest, acquired.objects)


if __name__ == "__main__":
    unittest.main()
