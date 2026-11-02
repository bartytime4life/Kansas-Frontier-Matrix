"""SQL feeds for Kansas earthquakes, tornadoes, NWS warnings and CDC PLACES, without network access."""
from datetime import datetime, timezone
import json
import sqlite3
import unittest
import urllib.parse
from unittest.mock import patch

from tests.local_data.test_sql_feeds import FeedCase, _gp
from tools.local_data import sql_feed_hazards as hz, sql_feeds as core


def at(*args):
    return lambda: datetime(*args, 15, 0, tzinfo=timezone.utc)


def square(w, s, e, n):
    return [(w, s), (e, s), (e, n), (w, n), (w, s)]


# --- Earthquakes -----------------------------------------------------------------------------------

def quake(time, lat, lon, eid, updated, mag="2.6", place="5 km E of Palco, Kansas", depth="5"):
    return (f'{time},{lat},{lon},{depth},{mag},mb_lg,34,73,0.476,0.51,us,{eid},{updated},"{place}",earthquake,'
            f'3.76,1.993,0.077,44,reviewed,us,us')


OLD = ('1867-04-24T20:22:00.000Z,38.98,-96.12,,5.2,mfa,,,,,official,official18670424202200000,2026-07-31T23:50:11.080Z,'
       '"Between Manhattan and Topeka, Kansas",earthquake,,,,,reviewed,official,official')
A = quake("2015-03-01T10:00:00.000Z", "38.0", "-100.5", "us10001", "2015-04-01T00:00:00.000Z")
B = quake("2015-06-01T12:00:00.000Z", "38.6", "-96.5", "us10002", "2015-07-01T00:00:00.000Z")
HOLE = quake("2015-08-01T12:00:00.000Z", "38.1", "-96.85", "us10003", "2015-09-01T00:00:00.000Z")
SLIVER = quake("2024-01-09T20:46:44.670Z", "36.995", "-97.8", "ok2024abcd", "2024-02-01T00:00:00.000Z", place="9 km S of Bluff City, Kansas")


def box(*events, header=None):
    return ((header or ",".join(hz.QUAKE_HEADER)) + "\n" + "".join(e + "\n" for e in events)).encode()


class EarthquakeTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.ctx.tiger = self.root / "tiger.gpkg"
        db = sqlite3.connect(self.ctx.tiger)
        db.execute("CREATE TABLE us_county (fid INTEGER PRIMARY KEY, GEOID TEXT, NAME TEXT, geom BLOB)")
        db.execute("INSERT INTO us_county VALUES (1,'20001','West',?)", (_gp([[square(-101.9, 37.1, -99.9, 39.1)]]),))
        db.execute("INSERT INTO us_county VALUES (2,'20003','East',?)", (_gp([[square(-97.9, 37.1, -95.9, 39.1),
                                                                               list(reversed(square(-97.1, 37.9, -96.6, 38.4)))]]),))
        db.execute("INSERT INTO us_county VALUES (3,'40071','Kay',?)", (_gp([[square(-98.5, 36.0, -96.5, 37.0)]]),))
        db.commit()
        db.close()
        self.full, self.probe = box(OLD, A, B, HOLE, SLIVER), box()
        self.web.routes = {hz.COMCAT: lambda url: self.probe if "updatedafter=" in url else self.full}

    def box_calls(self):
        return [u for u in self.web.calls if u == hz.COMCAT]

    def test_the_box_loads_by_year_and_events_outside_kansas_are_kept_flagged(self):
        result = hz.earthquakes(self.ctx)
        self.assertEqual((result["years_loaded"], result["rows"], result["events"]), (3, 5, 5))
        self.assertEqual(self.q("SELECT id, county_geoid, in_kansas FROM kfm_usgs_earthquakes ORDER BY time"),
                         [("official18670424202200000", "20003", 1), ("us10001", "20001", 1), ("us10002", "20003", 1),
                          ("us10003", None, 0), ("ok2024abcd", None, 0)])
        self.assertEqual(self.q("SELECT depth, nst, mag, typeof(latitude) FROM kfm_usgs_earthquakes WHERE id LIKE 'official%'"), [(None, None, 5.2, "real")])
        self.assertEqual(self.q("SELECT json_extract(receipt_json,'$.key'), imported_rows FROM kfm_sql_sources ORDER BY 1"),
                         [("year/1867", 1), ("year/2015", 3), ("year/2024", 1)])
        receipt = json.loads(self.q("SELECT receipt_json FROM kfm_sql_sources WHERE receipt_json LIKE '%year/2015%'")[0][0])
        self.assertEqual((receipt["events"], receipt["original"]["bytes"]), (3, len(self.full)))
        with self.assertRaisesRegex(core.FeedError, "TIGER_GEOPACKAGE_REQUIRED"):
            hz.earthquakes(core.Context(root=self.root, db_path=self.db_path))

    def test_a_rerun_only_probes_and_a_revision_or_deletion_reloads_the_whole_box(self):
        hz.earthquakes(self.ctx)
        # Next day: the probe sees only an event already loaded, so the box is not fetched again.
        self.ctx.now, self.probe = at(2026, 11, 5), box(OLD)
        again = hz.earthquakes(self.ctx)
        self.assertEqual((again["changed_events"], again["rows"], len(self.box_calls())), (0, 0, 1))
        self.assertIn("updatedafter=2026-07-29T23:50:11", self.web.calls[-1])
        # ComCat revised a 2015 event: only 2015 is replaced.
        revised = quake("2015-03-01T10:00:00.000Z", "38.0", "-100.5", "us10001", "2026-11-05T01:00:00.000Z", mag="2.8")
        self.probe, self.full = box(revised), box(OLD, revised, B, HOLE, SLIVER)
        result = hz.earthquakes(self.ctx)
        self.assertEqual((result["changed_events"], result["years_loaded"], result["years_unchanged"], result["rows"]), (1, 1, 2, 3))
        self.assertEqual(self.q("SELECT mag FROM kfm_usgs_earthquakes WHERE id='us10001'"), [(2.8,)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources GROUP BY state"), [("complete", 3), ("superseded", 1)])
        # A month later the whole box is checked even without a probe hit; ComCat deleted the 1867 event.
        self.ctx.now, self.probe, self.full = at(2026, 12, 6), box(), box(revised, B, HOLE, SLIVER)
        result = hz.earthquakes(self.ctx)
        self.assertEqual((result["years_removed"], result["years_unchanged"]), (1, 2))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usgs_earthquakes WHERE id LIKE 'official%'"), [(0,)])

    def test_a_header_change_stops_before_anything_is_kept(self):
        self.full = box(A, header=",".join(hz.QUAKE_HEADER).replace("magType", "mag_type"))
        with self.assertRaisesRegex(core.FeedError, "COMCAT_COLUMNS_CHANGED"):
            hz.earthquakes(self.ctx)
        self.full = box(A.replace(",38.0,", ",north,"))
        with self.assertRaisesRegex(core.FeedError, "NOT_A_NUMBER"):
            hz.earthquakes(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertFalse((self.root / "data/raw/sql-feeds/earthquakes").exists())

    def test_a_failure_part_way_through_a_year_leaves_none_of_its_rows(self):
        real, calls = hz.county_at, []

        def failing(*args):
            calls.append(1)
            if len(calls) == 3:
                raise core.FeedError("TEST_INTERRUPTED")
            return real(*args)
        with patch.object(hz, "county_at", failing), self.assertRaisesRegex(core.FeedError, "TEST_INTERRUPTED"):
            hz.earthquakes(self.ctx)
        self.assertEqual(self.q("SELECT substr(time,1,4), COUNT(*) FROM kfm_usgs_earthquakes GROUP BY 1"), [("1867", 1)])
        self.assertEqual(self.q("SELECT json_extract(receipt_json,'$.key') FROM kfm_sql_sources"), [("year/1867",)])
        result = hz.earthquakes(self.ctx)
        self.assertEqual((result["years_loaded"], result["years_unchanged"], result["rows"]), (2, 1, 4))


# --- Tornadoes -------------------------------------------------------------------------------------

TORNADO_ROWS = [
    "192,1950,10,01,1950-10-01,21:00:00,3,OK,40,23,1,0,0,4.0,0.0,36.73,-102.52,36.88,-102.3,15.8,10,1,1,1,25,0,0,0,0,,",
    # Udall, 1955: touched down in Oklahoma; the whole-track row and the OK segment are Oklahoma's, the KS segment is kept.
    "227,1955,05,25,1955-05-25,21:45:00,3,OK,40,30,5,0,0,5.0,0.0,36.85,-97.5,37.45,-96.75,60.0,1320,2,0,1,71,0,0,0,0,,",
    "227,1955,05,25,1955-05-25,21:45:00,3,OK,40,30,5,0,0,5.0,0.0,36.85,-97.5,37.0,-97.25,11.6,1320,2,1,2,71,0,0,0,0,,",
    "227,1955,05,25,1955-05-25,22:15:00,3,KS,20,13,5,273,80,5.0,0.0,37.0,-97.25,37.45,-96.75,48.4,1320,2,1,2,191,35,0,0,0,,",
    "144,1953,05,10,1953-05-10,03:00:00,3,KS,20,4,2,0,0,4.0,0.0,37.0,-97.6,37.38,-97.12,37.5,10,1,1,1,191,135,15,173,0,,",
    "144,1953,05,10,1953-05-10,03:00:00,3,KS,20,4,2,0,0,4.0,0.0,37.0,-97.6,37.38,-97.12,37.5,10,1,0,-9,79,0,0,0,0,,",
    "2505181930-01,2025,05,18,2025-05-18,19:30:00,3,KS,20,0,1,0,0,25000,0,38.8312,-98.0104,38.8405,-97.9917,1.2400,100,1,1,1,169,0,0,0,0,2025-05-18,19:34:00",
    "2505182005-01,2025,05,18,2025-05-18,20:05:00,3,NE,31,0,0,0,0,0,0,40.1,-97.6,40.11,-97.59,0.5000,25,1,1,1,169,0,0,0,0,2025-05-18,20:06:00",
]


def spc_page(*stems):
    return "".join(f'<a href="data/{s}.csv">{s}</a> <a href="data/{s.replace("all", "actual")}.csv">x</a>\n' for s in stems).encode()


def spc_file(rows, header=None):
    return ((header or ",".join(hz.TORNADO_HEADER)) + "\n" + "".join(r + "\n" for r in rows)).encode("latin-1")


class TornadoTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.page, self.files = spc_page("1950-2024_all_tornadoes", "1950-2025_all_tornadoes"), {}
        self.web.routes = {hz.SPC + "data/": lambda url: self.files.get(url.rsplit("/", 1)[1]), hz.SPC: lambda url: self.page}

    def test_the_newest_all_file_is_cut_to_kansas_rows_and_a_newer_one_replaces_it(self):
        self.files["1950-2025_all_tornadoes.csv"] = spc_file(TORNADO_ROWS)
        result = hz.tornadoes(self.ctx)
        self.assertEqual((result["file"], result["state"], result["rows"]), ("data/1950-2025_all_tornadoes.csv", "loaded", 4))
        self.assertEqual(self.q("SELECT om, st, ns, sn, sg, fat FROM kfm_spc_tornadoes ORDER BY row_number"),
                         [("227", "KS", "2", "1", "2", "80"), ("144", "KS", "1", "1", "1", "0"), ("144", "KS", "1", "0", "-9", "0"),
                          ("2505181930-01", "KS", "1", "1", "1", "0")])
        self.assertFalse(any("2024_all" in u or "actual" in u for u in self.web.calls))
        # Same day: the page is read, the file is not fetched again; after 28 days an identical file is not reloaded.
        self.assertEqual(hz.tornadoes(self.ctx)["state"], "not_due")
        self.ctx.now = at(2026, 12, 3)
        self.assertEqual(hz.tornadoes(self.ctx)["state"], "unchanged")
        self.assertEqual(sum(1 for u in self.web.calls if u.endswith("2025_all_tornadoes.csv")), 2)
        # SPC adds 2026 under a new name, reprocessing a past row: the Kansas cut is replaced.
        self.page = spc_page("1950-2025_all_tornadoes", "1950-2026_all_tornadoes")
        self.files["1950-2026_all_tornadoes.csv"] = spc_file([r.replace(",273,80,", ",273,81,") for r in TORNADO_ROWS])
        result = hz.tornadoes(self.ctx)
        self.assertEqual((result["state"], result["superseded"], result["rows"]), ("loaded", 1, 4))
        self.assertEqual(self.q("SELECT fat FROM kfm_spc_tornadoes WHERE om='227'"), [("81",)])
        self.assertEqual(self.q("SELECT state FROM kfm_sql_sources ORDER BY file_id"), [("superseded",), ("complete",)])

    def test_a_header_change_or_a_missing_link_stops_the_feed(self):
        self.files["1950-2025_all_tornadoes.csv"] = spc_file(TORNADO_ROWS, header=",".join(hz.TORNADO_HEADER[:-2]))
        with self.assertRaisesRegex(core.FeedError, "SPC_TORNADO_COLUMNS_CHANGED"):
            hz.tornadoes(self.ctx)
        self.page = b"<html>moved</html>"
        with self.assertRaisesRegex(core.FeedError, "SPC_TORNADO_FILE_NOT_LISTED"):
            hz.tornadoes(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_spc_tornadoes"), [(0,)])

    def test_a_failure_part_way_leaves_no_partial_cut(self):
        self.files["1950-2025_all_tornadoes.csv"] = spc_file(TORNADO_ROWS)
        real = hz.read_csv

        def failing(*args, **kwargs):
            for n, row in enumerate(real(*args, **kwargs)):
                if n == 2:
                    raise core.FeedError("TEST_INTERRUPTED")
                yield row
        with patch.object(hz, "read_csv", failing), self.assertRaisesRegex(core.FeedError, "TEST_INTERRUPTED"):
            hz.tornadoes(self.ctx)
        self.assertEqual(self.q("SELECT (SELECT COUNT(*) FROM kfm_spc_tornadoes), (SELECT COUNT(*) FROM kfm_sql_sources)"), [(0, 0)])
        self.assertEqual(hz.tornadoes(self.ctx)["rows"], 4)


# --- NWS warnings ----------------------------------------------------------------------------------

def vtec_event(year, eventid, wfo="ICT", phenomena="SV", locations="Sedgwick [KS], Butler [KS], Harvey [KS]"):
    return {"ph_name": "Severe Thunderstorm", "sig_name": "Warning", "phenomena": phenomena, "significance": "W", "eventid": eventid,
            "hvtec_nwsli": None, "area": 1480.0, "locations": locations, "issue": f"{year}-05-16T11:40:00Z",
            "product_issue": f"{year}-05-16T11:40:00Z", "expire": f"{year}-05-16T12:30:00Z", "init_expire": f"{year}-05-16T12:30:00Z",
            "uri": f"/vtec/?year={year}&wfo=K{wfo}&phenomena={phenomena}&significance=W&eventid={eventid:04d}", "wfo": wfo}


class WarningTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.events = {2023: [vtec_event(2023, 1)], 2024: [], 2025: [vtec_event(2025, 2), vtec_event(2025, 1, wfo="TOP")],
                       2026: [vtec_event(2026, 7)], 2027: [vtec_event(2027, 1)]}
        self.web.routes = {hz.VTEC.split("?")[0]: self.answer}
        self.first = patch.object(hz, "VTEC_FIRST", 2023)
        self.first.start()
        self.addCleanup(self.first.stop)

    def answer(self, url):
        year = int(urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)["year"][0])
        events = self.events[year]
        if callable(events):
            return events()
        return json.dumps({"state": "KS", "year": year, "events": events}).encode()

    def years(self):
        return [int(urllib.parse.parse_qs(urllib.parse.urlsplit(u).query)["year"][0]) for u in self.web.calls]

    def test_the_current_year_every_run_a_capped_backfill_then_one_older_year_in_rotation(self):
        first = hz.nws_warnings(self.ctx, max_backfill=2)
        self.assertEqual((first["loaded"], first["empty"], first["backfill_next"], first["revisited"]), ([2026, 2023], [2024], 2025, None))
        self.assertEqual(self.years(), [2026, 2023, 2024])
        self.assertEqual(self.q("SELECT year, wfo, eventid, locations FROM kfm_iem_vtec_events ORDER BY year"),
                         [(2023, "ICT", 1, "Butler [KS], Harvey [KS], Sedgwick [KS]"), (2026, "ICT", 7, "Butler [KS], Harvey [KS], Sedgwick [KS]")])
        # IEM's location order changes between requests: the year is still unchanged.
        self.events[2026] = [vtec_event(2026, 7, locations="Harvey [KS], Sedgwick [KS], Butler [KS]")]
        second = hz.nws_warnings(self.ctx, max_backfill=2)
        self.assertEqual((second["unchanged"], second["loaded"], second["backfill_next"]), ([2026], [2025], 2026))
        self.assertEqual(self.q("SELECT wfo FROM kfm_iem_vtec_events WHERE year=2025 ORDER BY row_number"), [("ICT",), ("TOP",)])
        third = hz.nws_warnings(self.ctx, max_backfill=2)
        self.assertEqual((third["unchanged"], third["revisited"]), ([2026, 2023], 2023))
        # A new event this year replaces the year's rows; the rotation moves on.
        self.events[2026].append(vtec_event(2026, 8))
        fourth = hz.nws_warnings(self.ctx, max_backfill=2)
        self.assertEqual((fourth["loaded"], fourth["empty"], fourth["revisited"]), ([2026], [2024], 2024))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_iem_vtec_events WHERE year=2026"), [(2,)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='superseded'"), [(1,)])
        # In January the previous year is fetched again too.
        self.ctx.now = at(2027, 1, 10)
        self.web.calls.clear()
        self.assertEqual(hz.nws_warnings(self.ctx, max_backfill=2)["loaded"], [2027])
        self.assertEqual(self.years()[:2], [2027, 2026])

    def test_field_changes_and_an_emptied_year_stop_the_feed(self):
        hz.nws_warnings(self.ctx, max_backfill=0)
        self.events[2026] = [{**vtec_event(2026, 7), "fcster": "X"}]
        with self.assertRaisesRegex(core.FeedError, "IEM_VTEC_FIELDS_CHANGED 2026"):
            hz.nws_warnings(self.ctx, max_backfill=0)
        self.events[2026] = []
        with self.assertRaisesRegex(core.FeedError, "IEM_VTEC_YEAR_EMPTIED 2026"):
            hz.nws_warnings(self.ctx, max_backfill=0)
        self.events[2026] = lambda: json.dumps({"state": "NE", "year": 2026, "events": []}).encode()
        with self.assertRaisesRegex(core.FeedError, "IEM_VTEC_RESPONSE_SHAPE"):
            hz.nws_warnings(self.ctx, max_backfill=0)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_iem_vtec_events"), [(1,)])

    def test_a_failure_part_way_keeps_the_years_done_and_resumes(self):
        self.events[2024] = lambda: (_ for _ in ()).throw(core.FeedError("HTTP_503 test"))
        with self.assertRaisesRegex(core.FeedError, "HTTP_503"):
            hz.nws_warnings(self.ctx, max_backfill=3)
        self.assertEqual(self.q("SELECT year FROM kfm_iem_vtec_events ORDER BY year"), [(2023,), (2026,)])
        db = core.open_db(self.ctx)
        self.assertEqual(core.get_state(db, "nws-warnings"), {"backfill_next": 2024})
        db.close()
        self.events[2024] = []
        result = hz.nws_warnings(self.ctx, max_backfill=3)
        self.assertEqual((result["unchanged"], result["empty"], result["loaded"], result["backfill_next"]), ([2026], [2024], [2025], 2026))


# --- CDC PLACES ------------------------------------------------------------------------------------

def county_row(fips, name, measure="ARTHRITIS", value="29.8", state="KS"):
    return [ "2023", state, "Kansas" if state == "KS" else "Nebraska", name, "BRFSS", "Health Outcomes", "Arthritis among adults", "%",
            "Crude prevalence", value, "", "", "26.3", "33.2", "12412", "9628", fips, "HLTHOUT", measure, "CrdPrv", "Arthritis",
            "POINT (-95.3017112327545 37.8857027458086)"]


def tract_row(tract, value="31.0", state="KS"):
    return ["2023", state, "Kansas", "Allen", tract[:5], tract, "BRFSS", "Health Outcomes", "Arthritis among adults", "%", "Crude prevalence",
            value, "", "", "27.0", "35.1", "2154", "1702", "POINT (-95.39 37.92)", tract, "HLTHOUT", "ARTHRITIS", "CrdPrv", "Arthritis"]


class PlacesTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.release, self.updated = {"swc5-untb": "2025", "cwsq-ngmh": "2025"}, {"swc5-untb": 1764844506, "cwsq-ngmh": 1765560443}
        self.rows = {"swc5-untb": [county_row("20001", "Allen"), county_row("31001", "Adams", state="NE"), county_row("20003", "Anderson"),
                                   county_row("20005", "Atchison")],
                     "cwsq-ngmh": [tract_row("20001952600"), tract_row("20001952700"), tract_row("20001952800")]}
        self.headers = {"swc5-untb": hz.PLACES_COLUMNS["county"], "cwsq-ngmh": hz.PLACES_COLUMNS["tract"]}
        self.ignore_filter = False
        self.web.routes = {"https://data.cdc.gov/api/views/": self.view, "https://data.cdc.gov/resource/": self.soda}
        page = patch.object(hz, "PLACES_PAGE", 2)
        page.start()
        self.addCleanup(page.stop)

    def view(self, url):
        dataset = url.rsplit("/", 1)[1][:-5]
        level = "County Data" if dataset == "swc5-untb" else "Census Tract Data"
        return json.dumps({"id": dataset, "name": f"PLACES: Local Data for Better Health, {level}, {self.release[dataset]} release",
                           "rowsUpdatedAt": self.updated[dataset]}).encode()

    def soda(self, url):
        parts = urllib.parse.urlsplit(url)
        dataset, fmt = parts.path.rsplit("/", 1)[1].split(".")
        params = {k: urllib.parse.unquote(v) for k, v in (p.split("=", 1) for p in parts.query.split("&"))}
        self.assertEqual(params["$where"], "stateabbr='KS'")
        rows = [r for r in self.rows[dataset] if self.ignore_filter or r[1] == "KS"]
        if fmt == "json":
            return json.dumps([{"count": str(len(rows))}]).encode()
        offset, limit = int(params["$offset"]), int(params["$limit"])
        return hz.csv_bytes([self.headers[dataset], *rows[offset:offset + limit]])

    def test_kansas_rows_load_per_release_and_a_new_release_is_kept_beside_the_old(self):
        result = hz.cdc_places(self.ctx)
        self.assertEqual((result["county"], result["tract"], result["rows"]), ("loaded 2025", "loaded 2025", 6))
        self.assertEqual(self.q("SELECT release, locationid, data_value, totalpopulation FROM kfm_cdc_places_county ORDER BY row_number"),
                         [("2025", "20001", 29.8, 12412), ("2025", "20003", 29.8, 12412), ("2025", "20005", 29.8, 12412)])
        self.assertEqual(self.q("SELECT countyfips, COUNT(*) FROM kfm_cdc_places_tract GROUP BY 1"), [("20001", 3)])
        self.assertTrue(any("%24offset=" in u or "$offset=2" in u for u in self.web.calls))
        # Checked every 28 days; an unchanged release costs only the metadata request.
        self.web.calls.clear()
        self.assertEqual(hz.cdc_places(self.ctx)["state"], "not_due")
        self.assertEqual(self.web.calls, [])
        self.ctx.now = at(2026, 12, 3)
        self.assertEqual(hz.cdc_places(self.ctx), {"rows": 0, "county": "unchanged 2025", "tract": "unchanged 2025"})
        self.assertTrue(all("/api/views/" in u for u in self.web.calls))
        # CDC refills the same id with the 2026 release: loaded as a new key, the 2025 release stays.
        self.ctx.now, self.release["swc5-untb"], self.updated["swc5-untb"] = at(2027, 1, 5), "2026", 1790000000
        self.rows["swc5-untb"] = [county_row("20001", "Allen", value="30.1")]
        self.assertEqual(hz.cdc_places(self.ctx)["county"], "loaded 2026")
        self.assertEqual(self.q("SELECT release, COUNT(*) FROM kfm_cdc_places_county GROUP BY 1"), [("2025", 3), ("2026", 1)])
        # A correction within the 2026 release replaces that release only.
        self.ctx.now, self.updated["swc5-untb"] = at(2027, 2, 5), 1790500000
        self.rows["swc5-untb"] = [county_row("20001", "Allen", value="30.2")]
        self.assertEqual(hz.cdc_places(self.ctx)["county"], "loaded 2026")
        self.assertEqual(self.q("SELECT release, data_value FROM kfm_cdc_places_county WHERE release='2026'"), [("2026", 30.2)])
        self.assertEqual(self.q("SELECT json_extract(receipt_json,'$.key'), state FROM kfm_sql_sources WHERE source_id='cdc-places-county' ORDER BY file_id"),
                         [("swc5-untb/2025", "complete"), ("swc5-untb/2026", "superseded"), ("swc5-untb/2026", "complete")])

    def test_header_name_and_count_changes_stop_without_loading(self):
        self.headers["swc5-untb"] = [c for c in hz.PLACES_COLUMNS["county"] if c != "totalpop18plus"]
        with self.assertRaisesRegex(core.FeedError, "CDC_PLACES_COLUMNS_CHANGED swc5-untb"):
            hz.cdc_places(self.ctx)
        self.headers["swc5-untb"] = hz.PLACES_COLUMNS["county"]
        self.ignore_filter = True
        with self.assertRaisesRegex(core.FeedError, "CDC_PLACES_EXTRACT_MISMATCH"):
            hz.cdc_places(self.ctx)
        self.ignore_filter = False
        self.release["swc5-untb"] = "archived"
        with self.assertRaisesRegex(core.FeedError, "CDC_PLACES_DATASET_CHANGED"):
            hz.cdc_places(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])

    def test_a_failure_part_way_leaves_the_county_release_and_no_partial_tract_rows(self):
        self.rows["cwsq-ngmh"][2][11] = "n/a"
        with self.assertRaisesRegex(core.FeedError, "NOT_A_NUMBER"):
            hz.cdc_places(self.ctx)
        self.assertEqual(self.q("SELECT (SELECT COUNT(*) FROM kfm_cdc_places_county), (SELECT COUNT(*) FROM kfm_cdc_places_tract)"), [(3, 0)])
        self.rows["cwsq-ngmh"][2][11] = "31.5"
        self.assertEqual(hz.cdc_places(self.ctx), {"rows": 3, "county": "unchanged 2025", "tract": "loaded 2025"})


class SharedTests(FeedCase):
    def test_names_numbers_and_tables(self):
        self.assertEqual([hz.snake(n) for n in ("magType", "horizontalError", "amountPaidOnIncreasedCostOfComplianceClaim", "id")],
                         ["mag_type", "horizontal_error", "amount_paid_on_increased_cost_of_compliance_claim", "id"])
        self.assertEqual([hz.number(v) for v in ("5", "-0.25", "", "1e3")], [5, -0.25, None, 1000.0])
        self.assertIn("PRIMARY KEY(file_id, row_number)", hz.QUAKE_DDL)


if __name__ == "__main__":
    unittest.main()
