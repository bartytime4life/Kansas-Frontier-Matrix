"""EPA AirData air-quality feed against a fake provider."""
import csv
from datetime import datetime, timedelta, timezone
import gzip
import io
import unittest
from unittest.mock import patch
import zipfile

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_air as air, sql_feeds as core


def zipped(name, header, rows):
    text = io.StringIO()
    csv.writer(text, quoting=csv.QUOTE_ALL, lineterminator="\n").writerows([header, *rows])
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(name.replace(".zip", ".csv"), text.getvalue())
    return out.getvalue()


def daily(state, county, site, code, day, mean, aqi="19", duration="24 HOUR"):
    return [state, county, site, code, "1", "37.775303", "-100.03544", "WGS84", "PM2.5 - Local Conditions", duration, "PM25 24-hour 2024",
            day, "Micrograms/cubic meter (LC)", "None", "24", "100.0", mean, "20.6", "6", aqi, "638", "Teledyne T640X",
            "", "Dodge City Community College", "Kansas" if state == "20" else "Iowa", "Ford", "Dodge City", "Dodge City, KS", "2025-03-17"]


def site(state, county, number):
    return [state, county, number, "38.9349", "-95.2309", "WGS84", "250", "RESIDENTIAL", "SUBURBAN", "1990-01-01", "", "", "", "", "", "", "", "-6",
            "Kansas Department Of Health And Environment", "Haskell", "155 Indian Ave", "66046", "Kansas", "Douglas", "Lawrence", "Lawrence, KS", "", "2026-07-13"]


def monitor(state, county, number):
    return [state, county, number, "44201", "Ozone", "1", "38.9349", "-95.2309", "WGS84", "1990", "2026-06-30", "SLAMS", "", "Kansas Department Of Health And Environment",
            "", "", "", "POPULATION EXPOSURE", "087", "INSTRUMENTAL", "NEIGHBORHOOD", "500 M TO 4KM", "Y", "Y", "Haskell", "155 Indian Ave",
            "Kansas", "Douglas", "Lawrence", "Lawrence, KS", "", "2026-07-13"]


class AirTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.created = "2026-06-25"
        self.files = {
            "daily_88101_2026.zip": [daily("20", "057", "0002", "88101", "2026-01-01", "7.9", aqi="", duration="1 HOUR"),
                                     daily("20", "057", "0002", "88101", "2026-01-02", "6.1"), daily("19", "153", "0030", "88101", "2026-01-01", "9.0"),
                                     daily("CC", "010", "0001", "88101", "2026-01-01", "3.0")],
            "daily_88101_2025.zip": [daily("20", "173", "0010", "88101", "2025-07-04", "12.5"), daily("19", "153", "0030", "88101", "2025-07-04", "9.0"),
                                     daily("19", "153", "0030", "88101", "2025-07-05", "9.0") + ["stray"]],   # another state's bad row is skipped
            "daily_42602_2019.zip": [daily("20", "209", "0021", "42602", "2019-03-01", "11.0")],
            "daily_aqi_by_county_2026.zip": [["Kansas", "Chase", "20", "017", "2026-01-01", "14", "Good", "PM2.5", "20-017-0001", "1"],
                                             ["Iowa", "Polk", "19", "153", "2026-01-01", "30", "Good", "PM2.5", "19-153-0030", "2"]],
        }
        self.extra = {"daily_88502_1980.zip": "0", "hourly_88101_2026.zip": "9", "annual_conc_by_monitor_2026.zip": "9"}
        self.lists = {"aqs_sites.zip": [site("20", "045", "9991"), site("19", "153", "0030")],
                      "aqs_monitors.zip": [monitor("20", "045", "9991"), monitor("31", "055", "0019")]}
        self.web.routes = {air.AIRDATA + "file_list.csv": lambda url: self.file_list(),
                           **{air.AIRDATA + name: (lambda url, name=name: self.zip_for(name)) for name in [*self.files, *self.lists, *self.extra]}}

    def file_list(self):
        lines = ["Filename,Rows,Size,Created"]
        lines += [f"{name},{len(rows)},1,{self.created}" for name, rows in self.files.items()]
        lines += [f"{name},{rows},1,{self.created}" for name, rows in self.extra.items()]
        return ("\n".join(lines) + "\n").encode()

    def zip_for(self, name):
        if name in self.lists:
            return zipped(name, air.SITES_HEADER if "sites" in name else air.MONITORS_HEADER, self.lists[name])
        return zipped(name, air.AQI_HEADER if "aqi" in name else air.DAILY_HEADER, self.files.get(name, []))

    def downloads(self):
        return [url.rsplit("/", 1)[1] for url in self.web.calls if url.endswith(".zip")]

    def temp_files(self):
        folder = self.root / "tmp-sql-feeds"
        return list(folder.iterdir()) if folder.exists() else []

    def test_a_first_run_loads_kansas_rows_and_a_rerun_reads_only_the_list(self):
        result = air.air_quality(self.ctx)
        self.assertEqual((result["files"], result["rows"], result["lists"], result["empty"], result["pending"]), (4, 5, 2, 1, 0))
        self.assertNotIn("daily_88502_1980.zip", self.downloads(), "a file EPA lists with 0 rows is not downloaded")
        self.assertFalse(any(name.startswith(("hourly", "annual")) for name in self.downloads()))
        self.assertEqual(self.q("SELECT county_code, site_num, date_local, arithmetic_mean, aqi, poc, latitude FROM kfm_aqs_daily ORDER BY 1, 3"),
                         [("057", "0002", "2026-01-01", 7.9, None, 1, 37.775303), ("057", "0002", "2026-01-02", 6.1, 19, 1, 37.775303),
                          ("173", "0010", "2025-07-04", 12.5, 19, 1, 37.775303), ("209", "0021", "2019-03-01", 11.0, 19, 1, 37.775303)])
        self.assertEqual(self.q("SELECT county_name, date, aqi, defining_site FROM kfm_aqs_daily_aqi_county"), [("Chase", "2026-01-01", 14, "20-017-0001")])
        self.assertEqual(self.q("SELECT state_code, site_number, owning_agency FROM kfm_aqs_sites"),
                         [("20", "9991", "Kansas Department Of Health And Environment")])
        self.assertEqual(self.q("SELECT site_number, parameter_code FROM kfm_aqs_monitors"), [("9991", "44201")])
        kept = next((self.root / "data/raw/sql-feeds/air-quality/daily_88101").glob("2026-kansas-*.csv.gz"))
        receipt = core.receipt_for(self.ctx, kept)
        self.assertEqual((receipt["key"], receipt["kansas_rows"], receipt["created"], receipt["original"]["bytes"]),
                         ("daily_88101/2026", 2, "2026-06-25", len(self.zip_for("daily_88101_2026.zip"))))
        self.assertEqual(gzip.decompress(kept.read_bytes()).decode().count("\n"), 3)
        self.assertEqual(self.temp_files(), [])
        calls = len(self.web.calls)
        again = air.air_quality(self.ctx)
        self.assertEqual((again["files"], again["rows"], again["lists"]), (0, 0, 0))
        self.assertEqual(self.web.calls[calls:], [air.AIRDATA + "file_list.csv"])

    def test_a_regenerated_file_replaces_recent_years_and_older_years_wait_a_year(self):
        air.air_quality(self.ctx)
        raw = sorted((self.root / "data/raw/sql-feeds/air-quality").rglob("*.gz"))
        self.created = "2026-12-15"
        self.ctx.now = lambda: datetime(2026, 12, 20, 12, tzinfo=timezone.utc)
        self.files["daily_88101_2026.zip"].append(daily("20", "057", "0002", "88101", "2026-07-01", "8.8"))
        self.files["daily_88101_2025.zip"].append(daily("19", "153", "0030", "88101", "2025-07-05", "9.1"))   # not Kansas
        self.lists["aqs_monitors.zip"] = [monitor("20", "045", "9991")[:-1] + ["2026-12-14"]]
        downloaded = len(self.downloads())
        result = air.air_quality(self.ctx)
        self.assertEqual((result["files"], result["rows"], result["unchanged"], result["lists"]), (1, 3, 2, 1))
        self.assertEqual(self.downloads()[downloaded:], ["aqs_sites.zip", "aqs_monitors.zip", "daily_88101_2026.zip", "daily_aqi_by_county_2026.zip",
                                                         "daily_88101_2025.zip"], "an older year waits a year for its re-check")
        self.assertEqual(self.q("SELECT COUNT(*), COUNT(DISTINCT file_id) FROM kfm_aqs_daily WHERE parameter_code='88101' AND date_local LIKE '2026%'"), [(3, 1)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources WHERE source_id='epa-aqs-daily' GROUP BY 1"), [("complete", 3), ("superseded", 1)])
        self.assertEqual(self.q("SELECT extraction_date FROM kfm_aqs_monitors"), [("2026-12-14",)])
        self.assertEqual(len(list((self.root / "data/raw/sql-feeds/air-quality").rglob("*.gz"))), len(raw) + 2, "unchanged cuts keep no second copy")
        self.ctx.now = lambda: datetime(2027, 12, 21, 12, tzinfo=timezone.utc)
        downloaded = len(self.downloads())
        later = air.air_quality(self.ctx)
        self.assertEqual(self.downloads()[downloaded:], ["daily_42602_2019.zip"])
        self.assertEqual((later["unchanged"], later["empty"]), (1, 1))

    def test_a_capped_run_leaves_the_rest_pending(self):
        first = air.air_quality(self.ctx, max_files=3)
        self.assertEqual((first["lists"], first["files"], first["pending"]), (2, 1, 3))
        self.assertEqual(self.downloads()[2:], ["daily_88101_2026.zip"], "the newest year comes first")
        second = air.air_quality(self.ctx, max_files=3)
        self.assertEqual((second["files"], second["pending"]), (3, 0))

    def test_a_changed_header_stops_the_feed_and_leaves_no_temp_file(self):
        self.web.routes[air.AIRDATA + "daily_88101_2026.zip"] = lambda url: zipped("daily_88101_2026.zip", air.DAILY_HEADER[:-1] + ["Last Change"],
                                                                                 self.files["daily_88101_2026.zip"])
        with self.assertRaisesRegex(core.FeedError, "AQS_COLUMNS_CHANGED daily_88101_2026.zip"):
            air.air_quality(self.ctx)
        self.assertEqual(self.temp_files(), [])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_aqs_daily"), [(0,)])
        self.web.routes[air.AIRDATA + "daily_88101_2026.zip"] = lambda url: zipped("daily_88101_2026.zip", air.DAILY_HEADER,
                                                                                 [daily("20", "057", "0002", "88101", "2026-01-01", "7.9")[:-1]])
        with self.assertRaisesRegex(core.FeedError, "AQS_ROW_SHAPE daily_88101_2026.zip 1"):
            air.air_quality(self.ctx)
        self.web.routes[air.AIRDATA + "file_list.csv"] = b"Filename,Rows,Size (KB),Created\n"
        with self.assertRaisesRegex(core.FeedError, "AQS_FILE_LIST_CHANGED"):
            air.air_quality(self.ctx)

    def test_a_failure_part_way_keeps_only_whole_files(self):
        self.web.routes[air.AIRDATA + "daily_88101_2025.zip"] = None
        with self.assertRaisesRegex(core.FeedError, "HTTP_404"):
            air.air_quality(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_aqs_daily"), [(2,)])
        state = self.q("SELECT state_json FROM kfm_feed_state WHERE feed='air-quality'")[0][0]
        self.assertIn("daily_88101/2026", state)
        self.assertNotIn("daily_88101/2025", state)
        self.assertEqual(self.temp_files(), [])
        self.web.routes[air.AIRDATA + "daily_88101_2025.zip"] = lambda url: self.zip_for("daily_88101_2025.zip")
        with patch.object(core, "finish_source", side_effect=core.FeedError("DISK_FULL")):
            with self.assertRaisesRegex(core.FeedError, "DISK_FULL"):
                air.air_quality(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_aqs_daily WHERE date_local LIKE '2025%'"), [(0,)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE state!='complete'"), [(0,)])
        self.assertEqual(self.temp_files(), [])
        self.assertEqual(air.air_quality(self.ctx)["files"], 2)

    def test_a_kansas_cut_that_becomes_empty_retires_the_loaded_version(self):
        air.air_quality(self.ctx)
        self.created = "2026-12-15"
        self.ctx.now = lambda: datetime(2026, 12, 20, 12, tzinfo=timezone.utc)
        self.files["daily_aqi_by_county_2026.zip"] = self.files["daily_aqi_by_county_2026.zip"][1:]
        result = air.air_quality(self.ctx)
        self.assertEqual((result["empty"], result["unchanged"]), (1, 2))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_aqs_daily_aqi_county"), [(0,)])
        self.assertEqual(self.q("SELECT state FROM kfm_sql_sources WHERE source_id='epa-aqs-daily-aqi-county'"), [("superseded",)])
        self.assertIn('"daily_aqi_by_county/2026":{"created":"2026-12-15"', self.q("SELECT state_json FROM kfm_feed_state")[0][0])

    def test_due_order(self):
        files = {("88101", 2026): (1, "2026-12-15"), ("88101", 2010): (1, "2026-12-15"), ("44201", 2026): (1, "2026-06-25"),
                 ("44201", 2025): (1, "2026-12-15"), ("42101", 1999): (1, "2026-12-15")}
        state = {"files": {"daily_88101/2026": {"created": "2026-06-25", "fetched": "2026-07-01"},
                           "daily_88101/2010": {"created": "2026-06-25", "fetched": "2025-12-01"},
                           "daily_44201/2026": {"created": "2026-06-25", "fetched": "2026-07-01"}}}
        today = datetime(2026, 12, 20).date()
        self.assertEqual(air.due_files(files, state, today), [("88101", 2026), ("44201", 2025), ("42101", 1999), ("88101", 2010)])
        self.assertEqual(air.due_files(files, state, today - timedelta(days=60))[-1:], [("42101", 1999)])


if __name__ == "__main__":
    unittest.main()
