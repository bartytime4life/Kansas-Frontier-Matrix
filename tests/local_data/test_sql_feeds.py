"""SQL feeds: additive, resumable loads from new source data, without network access."""
from datetime import date, datetime, timezone
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sqlite3
import struct
import tarfile
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from tests.local_data import test_intake as fixtures
from tools.local_data import intake, intake_route, sql_feed_prism as prism, sql_feed_sources as feeds, sql_feeds as core, sql_snapshot as snapshot
from tools.local_data.manage import init_store

BASE_SCHEMA = """
CREATE TABLE kfm_sql_sources (file_id INTEGER PRIMARY KEY, source_id TEXT NOT NULL, source_path TEXT NOT NULL,
  sha256 TEXT NOT NULL UNIQUE, source_bytes INTEGER NOT NULL, source_url TEXT NOT NULL, receipt_json TEXT NOT NULL,
  imported_rows INTEGER NOT NULL DEFAULT 0, state TEXT NOT NULL);
CREATE TABLE kfm_sql_build (name TEXT PRIMARY KEY, value TEXT NOT NULL) WITHOUT ROWID;
CREATE TABLE kfm_environmental_features (source_id TEXT NOT NULL, feature_sha256 TEXT NOT NULL, feature_id TEXT,
  feature_json TEXT NOT NULL, PRIMARY KEY(source_id,feature_sha256)) WITHOUT ROWID;
CREATE TABLE kfm_environmental_capture_features (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, source_id TEXT NOT NULL,
  feature_sha256 TEXT NOT NULL, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE TABLE kfm_wind_stations (station_id TEXT PRIMARY KEY, metadata_json TEXT NOT NULL) WITHOUT ROWID;
CREATE TABLE kfm_wind_daily (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, station_id TEXT NOT NULL, observation_day TEXT NOT NULL,
  average_knots TEXT, maximum_knots TEXT, gust_knots TEXT, PRIMARY KEY(file_id,station_id,observation_day,row_number)) WITHOUT ROWID;
CREATE TABLE kfm_wind_observations (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, station_id TEXT NOT NULL, observed_at_utc TEXT NOT NULL,
  direction_degrees TEXT, speed_knots TEXT, gust_knots TEXT, peak_gust_knots TEXT, peak_direction_degrees TEXT, peak_wind_time TEXT,
  PRIMARY KEY(file_id,station_id,observed_at_utc,row_number)) WITHOUT ROWID;
CREATE TABLE kfm_ghcnd_stations (station_id TEXT PRIMARY KEY, name TEXT NOT NULL, latitude REAL, longitude REAL, elevation_m REAL,
  metadata_json TEXT NOT NULL) WITHOUT ROWID;
CREATE TABLE kfm_storm_event_details (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "event_id" TEXT, "state_fips" TEXT, "year" TEXT,
  "event_type" TEXT, PRIMARY KEY(event_id)) WITHOUT ROWID;
CREATE TABLE kfm_storm_event_locations (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "event_id" TEXT, "location_index" TEXT,
  PRIMARY KEY(event_id,location_index)) WITHOUT ROWID;
CREATE TABLE kfm_storm_event_fatalities (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "fatality_id" TEXT, "event_id" TEXT,
  PRIMARY KEY(fatality_id)) WITHOUT ROWID;
CREATE TABLE kfm_asos_fivemin (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, wban TEXT NOT NULL, icao TEXT NOT NULL,
  local_time TEXT NOT NULL, utc_ddhhmm TEXT, wind_direction TEXT, wind_knots INTEGER, gust_knots INTEGER, visibility_sm TEXT,
  temperature_c INTEGER, dewpoint_c INTEGER, altimeter_inhg REAL, raw_line TEXT NOT NULL, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE TABLE kfm_prism_grids (grid_id INTEGER PRIMARY KEY, source_path TEXT NOT NULL UNIQUE, unit TEXT NOT NULL, source_sha256 TEXT NOT NULL,
  source_bytes INTEGER, raster_path TEXT NOT NULL, processed_at TEXT, county_rows INTEGER NOT NULL DEFAULT 0, state TEXT NOT NULL);
CREATE TABLE kfm_prism_county_stats (grid_id INTEGER NOT NULL, county_geoid TEXT NOT NULL, county_name TEXT NOT NULL, mean REAL,
  minimum REAL, maximum REAL, valid_pixels INTEGER NOT NULL, quality_flag TEXT NOT NULL, PRIMARY KEY(grid_id,county_geoid)) WITHOUT ROWID;
"""


class FakeWeb:
    """URL prefix -> bytes (or None for 404). Records every request."""

    def __init__(self, routes):
        self.routes, self.calls = routes, []

    def __call__(self, url, *, limit, timeout=120, missing_ok=False, attempts=3):
        self.calls.append(url)
        for prefix, body in self.routes.items():
            if url.startswith(prefix):
                body = body(url) if callable(body) else body
                if body is None:
                    if missing_ok:
                        return None
                    raise core.FeedError("HTTP_404 " + url)
                return core.Fetched(url, body, "Sun, 01 Nov 2026 00:00:00 GMT")
        if missing_ok:
            return None
        raise core.FeedError("HTTP_404 " + url)


class FeedCase(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "store"
        self.root.mkdir(mode=0o700)
        out = self.root / "data/work/sql"
        out.mkdir(parents=True)
        self.db_path = out / "observations.sqlite"
        db = sqlite3.connect(self.db_path)
        db.executescript(BASE_SCHEMA)
        db.close()
        self.web = FakeWeb({})
        self.logs = []
        self.ctx = core.Context(root=self.root, db_path=self.db_path, lock=self.root / "pipeline.lock", fetch=self.web,
                                now=lambda: datetime(2026, 11, 4, 15, 0, tzinfo=timezone.utc), log=self.logs.append, floor=0)

    def tearDown(self):
        self.temp.cleanup()

    def q(self, sql, *args):
        db = sqlite3.connect(self.db_path)
        try:
            return db.execute(sql, args).fetchall()
        finally:
            db.close()


class CoreTests(FeedCase):
    def test_raw_objects_are_immutable_and_record_the_discarded_original(self):
        path, digest = core.store_raw(self.ctx, "demo", "a/b.txt", b"kansas", url="https://x/full", original=b"kansas and more")
        receipt = core.receipt_for(self.ctx, path)
        self.assertEqual((receipt["sha256"], receipt["original"]["bytes"], receipt["original"]["kept"]), (digest, 15, False))
        self.assertEqual(oct(path.stat().st_mode & 0o777), "0o600")
        self.assertEqual(core.store_raw(self.ctx, "demo", "a/b.txt", b"kansas", url="u")[1], digest)
        with self.assertRaisesRegex(core.FeedError, "RAW_OBJECT_CHANGED"):
            core.store_raw(self.ctx, "demo", "a/b.txt", b"changed", url="u")
        with self.assertRaisesRegex(core.FeedError, "RAW_NAME_UNSAFE"):
            core.store_raw(self.ctx, "demo", "../escape", b"x", url="u")

    def test_a_source_loads_once_and_a_failed_load_leaves_nothing(self):
        db = core.open_db(self.ctx)
        path, digest = core.store_raw(self.ctx, "demo", "x.txt", b"x", url="u")
        file_id = core.begin_source(db, self.ctx, "demo", path, digest, "u", {})
        db.execute("ROLLBACK")
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        file_id = core.begin_source(db, self.ctx, "demo", path, digest, "u", {})
        core.finish_source(db, file_id, 3)
        self.assertIsNone(core.begin_source(db, self.ctx, "demo", path, digest, "u", {}))
        self.assertEqual(self.q("SELECT imported_rows, state FROM kfm_sql_sources"), [(3, "complete")])
        db.close()

    def test_the_pipeline_lock_is_reentrant_within_a_run(self):
        with core.pipeline_lock(self.ctx):
            with core.pipeline_lock(self.ctx):
                self.assertEqual(self.ctx.lock_depth, 2)
        self.assertEqual(self.ctx.lock_depth, 0)

    def test_status_reports_feed_state(self):
        db = core.open_db(self.ctx)
        core.set_state(db, self.ctx, "demo", {"through": "2026-11-03"})
        db.close()
        self.assertEqual(core.status(self.ctx)["feeds"]["demo"]["through"], "2026-11-03")


class SnapshotTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.dest = Path(self.temp.name) / "backup/sql-snapshots"
        self.dest.parent.mkdir()
        self.hour = 8

    def take(self, **options):
        self.hour += 1
        self.ctx.now = lambda hour=self.hour: datetime(2026, 11, 2, hour, 30, tzinfo=timezone.utc)
        return snapshot.snapshot(self.ctx, self.dest, device_check=False, floor_fraction=0, **options)

    def add_source(self, name):
        db = core.open_db(self.ctx)
        path, digest = core.store_raw(self.ctx, "demo", name, name.encode(), url="u")
        core.finish_source(db, core.begin_source(db, self.ctx, "demo", path, digest, "u", {}), 7)
        db.close()

    def test_a_nightly_copy_is_verified_and_only_the_newest_two_are_kept(self):
        self.add_source("a.txt")
        first = self.take()
        self.assertEqual((first["state"], first["source_files"], first["source_rows"], first["pruned"]), ("verified", 1, 7, []))
        copy = self.dest / first["snapshot"]
        self.assertTrue(copy.name.endswith(first["sha256"][:12] + ".sqlite"))
        self.assertEqual(hashlib.sha256(copy.read_bytes()).hexdigest(), first["sha256"])
        self.assertEqual(oct(copy.stat().st_mode & 0o777), "0o600")
        with sqlite3.connect(f"file:{copy}?mode=ro", uri=True) as db:
            self.assertEqual(db.execute("PRAGMA journal_mode").fetchone()[0], "delete")
        self.assertEqual(self.take()["state"], "unchanged", "an unchanged database is not copied twice")
        self.add_source("b.txt")
        second = self.take()
        self.add_source("c.txt")
        third = self.take()
        self.assertEqual(third["pruned"], [first["snapshot"]])
        self.assertEqual(sorted(p.name for p in self.dest.glob("*.sqlite")), [second["snapshot"], third["snapshot"]])
        self.assertEqual(len(list((self.dest / "receipts").glob("*.json"))), 3, "a pruned copy's receipt stays")
        self.assertEqual(snapshot.check(self.ctx, self.dest)["snapshot"], third["snapshot"])

    def test_a_failed_copy_deletes_nothing_and_leaves_no_partial(self):
        self.add_source("a.txt")
        first = self.take()
        (self.dest / "observations-20261102T000000Z.sqlite.partial").write_bytes(b"interrupted")
        (self.dest / "observations-20261102T000000Z.sqlite.partial-journal").write_bytes(b"interrupted")
        with self.assertRaisesRegex(core.FeedError, "SNAPSHOT_SPACE_FLOOR"):
            self.hour += 1
            snapshot.snapshot(self.ctx, self.dest, device_check=False, floor_fraction=1.0)
        self.assertEqual([p.name for p in self.dest.iterdir() if p.is_file()], [first["snapshot"]])
        with self.assertRaisesRegex(core.FeedError, "SNAPSHOT_SAME_DEVICE"):
            snapshot.snapshot(self.ctx, self.dest)
        with self.assertRaisesRegex(core.FeedError, "SNAPSHOT_DESTINATION_MISSING"):
            snapshot.snapshot(self.ctx, Path(self.temp.name) / "unmounted/KFM-pipeline-backup/sql-snapshots", device_check=False)
        with self.assertRaisesRegex(core.FeedError, "SNAPSHOT_KEEP_INVALID"):
            self.take(keep=0)

    def test_the_restore_check_rereads_the_newest_copy(self):
        with self.assertRaisesRegex(core.FeedError, "SNAPSHOT_MISSING"):
            snapshot.check(self.ctx, self.dest)
        self.add_source("a.txt")
        copy = self.dest / self.take()["snapshot"]
        result = snapshot.check(self.ctx, self.dest)
        self.assertEqual((result["state"], result["integrity_check"]), ("verified", "ok"))
        with open(copy, "r+b") as handle:
            handle.seek(200)
            handle.write(b"\xff")
        with self.assertRaisesRegex(core.FeedError, "SNAPSHOT_DIGEST_MISMATCH"):
            snapshot.check(self.ctx, self.dest)

    def test_the_command_takes_the_lock_unless_the_caller_holds_it(self):
        self.add_source("a.txt")
        out = io.StringIO()
        args = ["--root", str(self.root), "--db", str(self.db_path), "--lock", str(self.ctx.lock), "snapshot", "--dest", str(self.dest)]
        with patch("sys.stdout", out):
            self.assertEqual(core.main(args), 1)
        self.assertIn('"reason": "SNAPSHOT_SAME_DEVICE"', out.getvalue())
        taken = []
        real = core.pipeline_lock
        with patch.object(core, "pipeline_lock", lambda ctx: (taken.append(1), real(ctx))[1]):
            self.take()
            self.assertEqual(len(taken), 1)
            self.add_source("b.txt")
            taken.clear()
            self.assertEqual(self.take(lock_held=True)["state"], "verified")
            self.assertEqual(taken, [], "the backup's own lock covers a held run")


class CaptureTests(FeedCase):
    def capture(self, source, features, *, receipt_bytes=None):
        body = json.dumps({"type": "FeatureCollection", "features": features}).encode()
        digest = hashlib.sha256(body).hexdigest()
        payload = self.root / f"data/quarantine/{source}/objects/sha256/{digest}/payload"
        payload.parent.mkdir(parents=True, exist_ok=True)
        payload.write_bytes(body)
        receipts = self.root / "data/receipts/ingest/pc-pipeline"
        receipts.mkdir(parents=True, exist_ok=True)
        (receipts / f"{digest}.json").write_text(json.dumps({"sourceId": source, "sha256": digest, "byteLength": receipt_bytes or len(body),
                                                            "featureCount": len(features), "sourceUrl": f"https://{source}.example/api"}))
        return digest

    def test_new_captures_are_reviewed_by_policy_then_loaded_once(self):
        init_store(self.root)
        budget = fixtures.budget(github_limit_bytes=10**12, reserved_for_code_and_interface_bytes=10**11, committed=[])
        feature = {"type": "Feature", "id": "q1", "geometry": {"type": "Point", "coordinates": [-98, 38]}, "properties": {"mag": "2.7"}}
        self.capture("usgs-earthquakes", [feature])
        bad = self.capture("nws-alerts", [], receipt_bytes=1)
        intake.analyze(self.root, budget=budget)
        with patch.object(intake_route, "load_budget", return_value=budget):
            first = feeds.captures(self.ctx)
            second = feeds.captures(self.ctx)
        self.assertEqual((first["reviewed"], first["held"], first["files_loaded"]), (1, 1, 1))
        self.assertEqual(first["held_reasons"], ["missing matching provenance receipt"])
        self.assertEqual((second["reviewed"], second["files_loaded"]), (0, 0))
        self.assertEqual(self.q("SELECT source_id, feature_id FROM kfm_environmental_features"), [("usgs-earthquakes", "q1")])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE sha256=?", bad), [(0,)])
        reviewed = [i for i in intake.list_items(self.root)["items"] if i["status"] == "reviewed"] if hasattr(intake, "list_items") else None
        if reviewed is not None:
            self.assertEqual(len(reviewed), 1)


class WindTests(FeedCase):
    def test_wind_catches_up_readings_and_summaries_then_backfills_a_year(self):
        db = sqlite3.connect(self.db_path)
        db.executemany("INSERT INTO kfm_wind_stations VALUES (?,?)", [("ICT", "{}"), ("DDC", "{}")])
        db.commit()
        db.close()
        obs = lambda url: (b"station,valid,drct,sknt,gust,peak_wind_gust,peak_wind_drct,peak_wind_time\n"
                           + (b"ICT,2003-01-01 00:53,180.00,12.00,M,M,M,M\n" if "year1=2003" in url else b"ICT,2026-11-01 00:53,180.00,12.00,M,M,M,M\n"))
        daily = b"station,day,avg_wind_speed_kts,max_wind_speed_kts,max_wind_gust_kts,network\nICT,2026-09-24,6.1,16.0,None,KS_ASOS\n"
        self.web.routes = {feeds.IEM + "asos.py": obs, feeds.IEM + "daily.py": daily}
        result = feeds.iem_wind(self.ctx)
        self.assertEqual((result["observation_rows"], result["daily_rows"], result["backfill_year"]), (2, 1, 2003))
        self.assertEqual((result["obs_through"], result["daily_through"]), ("2026-11-03", "2026-11-03"))
        backfill = [u for u in self.web.calls if "year1=2003" in u]
        self.assertTrue(backfill and "station=DDC" in backfill[0] and "report_type=3" in backfill[0])
        self.assertEqual(self.q("SELECT station_id, observation_day, gust_knots FROM kfm_wind_daily"), [("ICT", "2026-09-24", "None")])
        # Next run: nothing new, and the backfill moves on a year (an identical answer is not loaded twice).
        again = feeds.iem_wind(self.ctx)
        self.assertEqual((again["observation_rows"], again["daily_rows"], again["backfill_year"]), (0, 0, 2004))


class GhcndTests(FeedCase):
    def station_line(self, sid, state):
        return f"{sid} {37.65:8.4f} {-97.43:9.4f} {407.2:6.1f} {state} {'TEST':30s}"

    def diff(self, rows):
        out = io.BytesIO()
        with tarfile.open(fileobj=out, mode="w:gz") as tar:
            for action, lines in rows.items():
                body = "".join(l + "\n" for l in lines).encode()
                info = tarfile.TarInfo(f"superghcnd_diff/{action}.csv")
                info.size = len(body)
                tar.addfile(info, io.BytesIO(body))
        return out.getvalue()

    def test_daily_update_files_become_a_kansas_revision_overlay(self):
        stations = "\n".join([self.station_line("USW00003928", "KS"), self.station_line("USW00094728", "NY")]).encode()
        listing = b'<a href="superghcnd_diff_20261005_to_20261006.tar.gz"></a><a href="superghcnd_diff_20261006_to_20261007.tar.gz"></a>'
        diff = self.diff({"insert": ["USW00003928,20261006,TMAX,256,,,W,2400", "USW00094728,20261006,TMAX,200,,,W,"],
                          "update": ["USW00003928,20261001,PRCP,10,,,W,2400"], "delete": ["USW00003928,20260930,SNOW,0,,,W,"]})
        self.web.routes = {feeds.GHCN + "ghcnd-stations.txt": stations, feeds.GHCN + "superghcnd/superghcnd_diff_": diff, feeds.GHCN + "superghcnd/": listing}
        result = feeds.ghcnd(self.ctx)
        self.assertEqual((result["files"], result["kansas_rows"], result["applied_through"]), (1, 3, "20261007"))
        self.assertEqual(self.q("SELECT station_id FROM kfm_ghcnd_stations"), [("USW00003928",)])
        self.assertEqual(self.q("SELECT action, observation_day, element, raw_value FROM kfm_ghcnd_daily_revisions ORDER BY action"),
                         [("delete", 20260930, "SNOW", 0), ("insert", 20261006, "TMAX", 256), ("update", 20261001, "PRCP", 10)])
        receipt = json.loads(next((self.root / "data/receipts/ingest/sql-feeds/ghcnd/diffs").rglob("*.json")).read_text())
        self.assertEqual((receipt["kansas_rows"], receipt["original"]["kept"]), (3, False))
        self.assertEqual(feeds.ghcnd(self.ctx)["files"], 0)


class StormTests(FeedCase):
    def gz_csv(self, rows):
        return gzip.compress("".join(",".join(r) + "\n" for r in rows).encode())

    def test_a_newer_ncei_file_replaces_that_years_kansas_rows(self):
        db = sqlite3.connect(self.db_path)
        db.execute("INSERT INTO kfm_sql_sources VALUES (1,'noaa-storm-events-details','x/StormEvents_details-ftp_v1.0_d2026_c20260918.csv.gz','a',1,'u','{}',1,'complete')")
        db.execute("INSERT INTO kfm_storm_event_details VALUES (1,1,'900','20','2026','Hail')")
        db.commit()
        db.close()
        listing = "".join(f'<a href="StormEvents_{k}-ftp_v1.0_d2026_c20261026.csv.gz">' for k in feeds.STORM_KINDS).encode()
        files = {"details": [["EVENT_ID", "STATE_FIPS", "YEAR", "EVENT_TYPE"], ["900", "20", "2026", "Hail"], ["901", "20", "2026", "Tornado"], ["902", "31", "2026", "Hail"]],
                 "locations": [["EVENT_ID", "LOCATION_INDEX"], ["901", "1"], ["902", "1"]],
                 "fatalities": [["FATALITY_ID", "EVENT_ID", "EVENT_YEARMONTH"], ["5", "902", "202605"], ["6", "901", "202605"]]}
        routes = {feeds.STORM + f"StormEvents_{k}": self.gz_csv(v) for k, v in files.items()}
        self.web.routes = {**routes, feeds.STORM: listing}
        result = feeds.storm_events(self.ctx)
        self.assertEqual(result["years"], ["2026"])
        self.assertEqual(self.q("SELECT event_id, event_type FROM kfm_storm_event_details ORDER BY event_id"), [("900", "Hail"), ("901", "Tornado")])
        self.assertEqual(self.q("SELECT event_id FROM kfm_storm_event_locations"), [("901",)])
        # A column NCEI added at the end is added to the table; only the Kansas event's fatality is kept.
        self.assertEqual(self.q("SELECT fatality_id, event_yearmonth FROM kfm_storm_event_fatalities"), [("6", "202605")])
        self.assertEqual(self.q("SELECT state FROM kfm_sql_sources WHERE file_id=1"), [("superseded",)])
        self.assertEqual(feeds.storm_events(self.ctx)["years"], [])
        # NCEI re-publishes with no Kansas change: the date is recorded and the year stops being due.
        newer = listing.replace(b"c20261026", b"c20261101")
        self.web.routes = {**{k.replace("c20261026", "c20261101"): v for k, v in routes.items()}, **routes, feeds.STORM: newer}
        self.assertEqual(feeds.storm_events(self.ctx)["years"], ["2026"])
        self.assertEqual(self.q("SELECT event_id FROM kfm_storm_event_details ORDER BY event_id"), [("900",), ("901",)])
        self.assertEqual(feeds.storm_events(self.ctx)["years"], [])


class AsosTests(FeedCase):
    LINE = "03928KICT ICT2001010100000101/01/01 00:00:31  5-MIN KICT 010600Z 27004KT 10SM CLR 03/M01 A2989 210 54 -1100 270/04 RMK AO2"

    def test_one_backfill_year_per_run_with_the_same_decoding(self):
        self.web.routes = {feeds.ASOS + "6401-2001/64010KICT200101.dat": self.LINE.encode() + b"\n",
                           feeds.ASOS + "6401-2001/": None, feeds.ASOS: b'<a href="6401-2001/">6401-2001/</a>'}
        result = feeds.asos_fivemin(self.ctx)
        self.assertEqual((result["year"], result["files"], result["missing"], result["rows"]), (2001, 1, 59, 1))
        self.assertEqual(self.q("SELECT icao, wind_direction, wind_knots, temperature_c, dewpoint_c, altimeter_inhg FROM kfm_asos_fivemin"),
                         [("KICT", "270", 4, 3, -1, 29.89)])
        self.assertIn("NCEI has no 6401-2002", feeds.asos_fivemin(self.ctx)["note"])


def _gp(polygons):
    def le(fmt, *v):
        return struct.pack("<" + fmt, *v)
    body = le("BI", 1, 6) + le("I", len(polygons))
    for rings in polygons:
        body += le("BI", 1, 3) + le("I", len(rings))
        for ring in rings:
            body += le("I", len(ring)) + b"".join(le("dd", *p) for p in ring)
    return b"GP\x00\x01" + le("I", 4269) + body


def _bil_zip(values, nrows, ncols, x0, y0, d):
    hdr = (f"BYTEORDER I\nLAYOUT BIL\nNROWS {nrows}\nNCOLS {ncols}\nNBANDS 1\nNBITS 32\nPIXELTYPE FLOAT\n"
           f"ULXMAP {x0}\nULYMAP {y0}\nXDIM {d}\nYDIM {d}\nNODATA -9999\n")
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w") as z:
        z.writestr("prism_ppt_us_25m_20261103.bil", struct.pack(f"<{len(values)}f", *values))
        z.writestr("prism_ppt_us_25m_20261103.hdr", hdr)
        z.writestr("prism_ppt_us_25m_20261103.info.txt", "Version: early\n")
    return out.getvalue()


class PrismTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.ctx.tiger = self.root / "tiger.gpkg"
        db = sqlite3.connect(self.ctx.tiger)
        db.execute("CREATE TABLE us_county (fid INTEGER PRIMARY KEY, GEOID TEXT, NAME TEXT, geom BLOB)")
        square = lambda w, s, e, n: [[(w, s), (e, s), (e, n), (w, n), (w, s)]]
        db.execute("INSERT INTO us_county VALUES (1,'20001','West',?)", (_gp([square(-101.9, 37.1, -99.9, 39.1)]),))
        # Two parts, one with a hole: only cells between the outer ring and the hole count.
        db.execute("INSERT INTO us_county VALUES (2,'20003','East',?)", (_gp([square(-97.9, 37.1, -95.9, 39.1) + [list(reversed(square(-97.1, 37.9, -96.6, 38.4)[0]))],
                                                                               square(-95.4, 37.1, -94.9, 37.6)]),))
        db.commit()
        db.close()

    def test_due_targets_follow_new_week_and_month_checks(self):
        state = {"daily_through": "2026-11-01", "daily_checks": {"20261027": ["new"], "20260930": ["new", "week"]},
                 "monthly_through": "2026-09", "annual_checks": {"2025": ["new"]}}
        targets = prism.due_targets(state, date(2026, 11, 4))
        self.assertEqual(targets, [("daily", "20261102", "new"), ("daily", "20261103", "new"), ("daily", "20260930", "month"),
                                   ("daily", "20261027", "week"), ("monthly", "202610", "new"), ("annual", "2025", "revision")])
        marked = prism._mark(state, "daily", "20260930", "month", date(2026, 11, 4))
        self.assertNotIn("20260930", marked["daily_checks"])

    def test_an_incomplete_target_is_retried_and_an_incomplete_revision_stays_due(self):
        grid = _bil_zip([1.0] * (14 * 24), 14, 24, -104.75, 41.75, 0.5)
        self.web.routes = {"https://services.nacse.org/prism/data/get/us/4km/ppt/20261103": grid,
                           "https://services.nacse.org/prism/data/get/us/4km/ppt/": None}
        self.ctx.pause = 0
        db = core.open_db(self.ctx)
        core.set_state(db, self.ctx, "prism", {"daily_through": "2026-11-01", "monthly_through": "2026-10",
                                               "annual_checks": {"2025": ["new", "revision"]}, "daily_checks": {"20261027": ["new"]}})
        db.close()
        with patch.object(prism, "VARIABLES", ("ppt",)):
            result = prism.prism(self.ctx, resolutions=("4km",))
        self.assertEqual((result["grids_loaded"], result["unavailable"], result["daily_through"]), (1, 2, "2026-11-03"))
        db = core.open_db(self.ctx)
        state = core.get_state(db, "prism")
        db.close()
        # November 2 was not posted yet: it is kept for retry though November 3 moved the watermark on.
        self.assertEqual(list(state["retry"]), ["daily|20261102"])
        self.assertEqual(state["daily_checks"]["20261027"], ["new"])
        self.assertEqual(prism.due_targets(state, date(2026, 11, 4))[:2], [("daily", "20261102", "new"), ("daily", "20261027", "week")])

    def test_the_kept_clip_is_byte_identical_for_the_same_grid(self):
        parsed = prism.read_bil(_bil_zip([2.0] * (14 * 24), 14, 24, -104.75, 41.75, 0.5))
        self.assertEqual(prism._clip_tar(parsed, "x"), prism._clip_tar(parsed, "x"))

    def test_grids_become_kansas_county_rows_and_revisions_are_new_versions(self):
        d, x0, y0, ncols, nrows = 0.5, -104.75, 41.75, 24, 14
        values = [float(c) if not (r == 7 and c == 10) else -9999.0 for r in range(nrows) for c in range(ncols)]
        first, revised = _bil_zip(values, nrows, ncols, x0, y0, d), _bil_zip([v + 1 if v != -9999.0 else v for v in values], nrows, ncols, x0, y0, d)
        calls = {"n": 0}

        def grid(url):
            calls["n"] += 1
            return first if calls["n"] <= 1 else revised
        self.web.routes = {"https://services.nacse.org/prism/data/get/us/4km/ppt/20261103": grid}
        self.ctx.pause = 0
        with patch.object(prism, "VARIABLES", ("ppt",)), patch.object(prism, "due_targets", return_value=[("daily", "20261103", "new")]):
            result = prism.prism(self.ctx, resolutions=("4km",))
            self.assertEqual((result["downloads"], result["grids_loaded"]), (1, 1))
            stats = dict((g, (n, round(m, 3), c)) for g, n, m, c in self.q("SELECT county_geoid, county_name, mean, valid_pixels FROM kfm_prism_county_stats"))
            # West: centers at -101.75..-100.25 by 37.25..38.75 -> 4x4 cells, columns 6..9 (values 6..9).
            self.assertEqual(stats["20001"], ("West", 7.5, 16))
            # East: 4x4 minus the hole's 1 center (-96.75, 38.25), plus the second part's 1 cell; column 10 nodata is outside.
            east = self.q("SELECT valid_pixels FROM kfm_prism_county_stats WHERE county_geoid='20003'")[0][0]
            self.assertEqual(east, 16)
            self.assertEqual(prism.prism(self.ctx, resolutions=("4km",))["grids_loaded"], 1)
            self.assertEqual(prism.prism(self.ctx, resolutions=("4km",))["unchanged"], 1)
        paths = [p for (p,) in self.q("SELECT source_path FROM kfm_prism_grids ORDER BY grid_id")]
        self.assertEqual(paths[0], "time_series/us/an/4km/ppt/daily/2026/prism_ppt_us_25m_20261103.zip")
        self.assertRegex(paths[1], r"_20261103\.zip#sha256=[0-9a-f]{12}$")
        kept = next((self.root / "data/raw/sql-feeds/prism").rglob("*.tar.gz"))
        with tarfile.open(kept) as tar:
            self.assertIn("Version: early", tar.extractfile([m for m in tar.getmembers() if m.name.endswith(".info.txt")][0]).read().decode())
        self.assertLess(kept.stat().st_size, len(first))


class NwmCursorTests(FeedCase):
    def test_missing_days_advance_and_save_the_cursor(self):
        from tools.local_data import sql_feed_nwm as nwm

        self.ctx.nwm_gpkg = self.root / "nwm.gpkg"
        db = sqlite3.connect(self.ctx.nwm_gpkg)
        db.execute("CREATE TABLE nwm_v30_flowlines (fid INTEGER PRIMARY KEY, feature_id TEXT)")
        db.execute("INSERT INTO nwm_v30_flowlines VALUES (1, '744183')")
        db.commit()
        db.close()
        self.web.routes = {}
        first = nwm.nwm(self.ctx)
        self.assertEqual((first["runs"], first["next_day"], len(first["missing_days"])), (0, "2026-10-15", 7))
        second = nwm.nwm(self.ctx)
        self.assertEqual(second["next_day"], "2026-10-22")
        self.assertFalse(any("nwm.20261008" in url for url in self.web.calls[7:]))


@unittest.skipUnless(importlib.util.find_spec("netCDF4") and importlib.util.find_spec("numpy"), "NWM reader environment not installed")
class NwmTests(FeedCase):
    def test_kansas_rows_keep_the_archived_shape(self):
        import netCDF4
        from tools.local_data import sql_feed_nwm as nwm

        path = self.root / "channel.nc"
        with netCDF4.Dataset(path, "w") as ds:
            ds.model_output_type = "channel_rt"
            ds.createDimension("feature_id", 3)
            ds.createDimension("time", 1)
            ds.createDimension("reference_time", 1)
            ds.createVariable("feature_id", "i8", ("feature_id",))[:] = [1, 2, 3]
            ds.createVariable("time", "i4", ("time",))[:] = [29875680]
            ds.createVariable("reference_time", "i4", ("reference_time",))[:] = [29875500]
            for name in nwm.VARIABLES:
                var = ds.createVariable(name, "i4", ("feature_id",), fill_value=-999900)
                var.scale_factor, var.add_offset, var.valid_range = 0.01, 0.0, [0, 5000000]
                var.set_auto_maskandscale(False)
                var[:] = [3, -999900, 7]
        data = nwm.extract(path, [1, 2])
        rows = list(nwm.rows_for(data, "2026-10-31T12:00:00Z"))
        self.assertEqual([r[0] for r in rows], [1, 2])
        self.assertEqual(rows[0][5:8], (0.029999999329447746, 3, "valid"))
        self.assertEqual(rows[1][5:8], (None, -999900, "missing"))


if __name__ == "__main__":
    unittest.main()
