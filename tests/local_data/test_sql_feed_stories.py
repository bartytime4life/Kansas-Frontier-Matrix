"""Story bundles: the builder contract, the export and the feed, on small fixture databases. Never the real store."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import sqlite3
import tempfile
from types import ModuleType
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from tools.local_data import sql_feed_stories as stories, sql_feeds as core
from tools.local_data import stories as kit
from tools.local_data.stories import climate_stripes, iron_horse

BASE = "CREATE TABLE kfm_sql_sources (file_id INTEGER PRIMARY KEY, source_id TEXT, source_path TEXT, sha256 TEXT UNIQUE, source_bytes INTEGER, source_url TEXT, receipt_json TEXT, imported_rows INTEGER DEFAULT 0, state TEXT)"
ATACK = ("CREATE TABLE kfm_atack_railroads (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, fid_rr1826 INTEGER, track REAL, "
         "vx_count INTEGER, gauge REAL, rrname TEXT, in_op_by INTEGER, exact_date INTEGER, fidall INTEGER, edited INTEGER, miles REAL, "
         "fid_1900st INTEGER, statenam TEXT, geometry_geojson TEXT, min_lon REAL, min_lat REAL, max_lon REAL, max_lat REAL, "
         "PRIMARY KEY(file_id,row_number))")
CLIMATE = """
CREATE TABLE kfm_climdiv_monthly (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, area_type TEXT NOT NULL, area_code TEXT NOT NULL,
  element TEXT NOT NULL, year INTEGER NOT NULL, month INTEGER NOT NULL, value REAL, missing_token TEXT, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
CREATE TABLE kfm_climdiv_normals (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, area_type TEXT NOT NULL, area_code TEXT NOT NULL,
  element TEXT NOT NULL, period_code TEXT NOT NULL, period TEXT, month INTEGER NOT NULL, value REAL, missing_token TEXT, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
"""
NOW = datetime(2026, 11, 4, 12, 0, tzinfo=timezone.utc)
LATER = datetime(2026, 11, 5, 12, 0, tzinfo=timezone.utc)


def line(*points) -> str:
    return json.dumps({"type": "MultiLineString", "coordinates": [[list(a), list(b)] for a, b in zip(points, points[1:])]})


def atack_rows(db) -> None:
    db.execute(ATACK)
    rows = [
        (56.5, "Platte County", 1861, 2.5, "Missouri", line((-94.9, 39.8), (-94.8, 39.7))),
        (0.0, "", 1872, 10.0, "Kansas", line((-97.0, 38.0), (-96.9, 38.0), (-96.8, 38.0), (-96.7, 38.1))),
        (0.0, "", 1872, 5.0, "Kansas", line((-96.7, 38.1), (-96.6, 38.2))),
        (0.0, "", 1889, 3.0, "Kansas", line((-99.0, 39.0), (-98.9, 39.0))),
        (0.0, None, 1889, None, None, line((-99.0, 37.0), (-98.9, 37.0))),
    ]
    for index, (gauge, name, year, miles, state, geometry) in enumerate(rows, 1):
        db.execute("INSERT INTO kfm_atack_railroads (file_id,row_number,gauge,rrname,in_op_by,exact_date,miles,statenam,geometry_geojson) "
                   "VALUES (1,?,?,?,?,0,?,?,?)", (index, gauge, name, year, miles, state, geometry))


def climate_rows(db) -> None:
    db.executescript(CLIMATE)
    row = 0

    def add(area_type, area, element, year, month, value):
        nonlocal row
        row += 1
        db.execute("INSERT INTO kfm_climdiv_monthly VALUES (1,?,?,?,?,?,?,?,NULL)", (row, area_type, area, element, year, month, value))
    for area_type, area in (("state", "20"), ("division", "1401")):
        for year in (1895, 1896):
            for month in range(1, 13):
                add(area_type, area, "tmpc", year, month, 50.0 + month / 10)
                add(area_type, area, "pcpn", year, month, 1.25)
                add(area_type, area, "pdsi", year, month, -1.5)
                add(area_type, area, "tmax", year, month, 99.0)   # not used by the story
        add(area_type, area, "tmpc", 1897, 1, 40.0)
        add(area_type, area, "tmpc", 1897, 2, None)
    add("county", "20001", "tmpc", 1895, 1, 1.0)                  # counties stay out of the bundle
    for number, area in enumerate(("20", "1401"), 1):
        for month in range(1, 13):
            for element, value in (("tmpc", 49.0), ("pcpn", 1.0)):
                for period_code, period in (("0031", "1901-2000"), ("0010", "1991-2020")):
                    db.execute("INSERT INTO kfm_climdiv_normals VALUES (2,?,?,?,?,?,?,?,?,NULL)",
                               (number * 10000 + month * 100 + (1 if element == "tmpc" else 2) * 10 + (1 if period_code == "0031" else 2),
                                "state" if area == "20" else "division", area, element, period_code, period, month, value))


def seed_source(db) -> None:
    db.execute("INSERT INTO kfm_sql_sources (source_id) VALUES ('x')")


def make_db(path: Path, *fill) -> Path:
    db = sqlite3.connect(path)
    db.execute(BASE)
    for step in fill:
        step(db)
    db.commit()
    db.close()
    return path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fake_module(story_id="fake-story", build=lambda db: {"value": 1}, **story) -> ModuleType:
    module = ModuleType(f"tools.local_data.stories.{story_id.replace('-', '_')}")
    module.STORY = {"id": story_id, "version": 1, "db": "observations", "tables": ["kfm_sql_sources"],
                    "sources": [{"name": "n", "license": "l", "url": "u", "citation": "c"}], **story}
    module.build = build
    return module


class Case(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.tmp = Path(directory.name)

    def context(self, db: Path, **fields) -> core.Context:
        return core.Context(root=self.tmp / "store", db_path=db, now=lambda: NOW, log=lambda line: None, floor=0, **fields)


class Helpers(unittest.TestCase):
    def test_rounded_and_scaled_keep_nulls(self):
        self.assertIsNone(kit.rounded(None))
        self.assertEqual(kit.rounded(2.0), 2)
        self.assertEqual(kit.rounded(2.456, 2), 2.46)
        self.assertEqual(kit.scaled([1.25, None, -0.5], 100), [125, None, -50])

    def test_simplify_keeps_ends_and_real_bends(self):
        straight = [(0.0, 0.0), (1.0, 0.0001), (2.0, 0.0)]
        self.assertEqual(kit.simplify(straight, 0.01), [(0.0, 0.0), (2.0, 0.0)])
        bent = [(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)]
        self.assertEqual(kit.simplify(bent, 0.01), bent)
        self.assertEqual(kit.simplify([(1.0, 1.0)], 0.1), [(1.0, 1.0)])

    def test_grid_path_is_deltas_and_drops_repeats(self):
        self.assertEqual(kit.grid_path([(-102.0, 37.0), (-102.0, 37.0), (-101.999, 37.002)], (-103.0, 36.0), 0.001), [1000, 1000, 1, 2])

    def test_geojson_lines(self):
        self.assertEqual(kit.geojson_lines('{"type":"LineString","coordinates":[[1,2],[3,4,9]]}'), [[(1.0, 2.0), (3.0, 4.0)]])
        with self.assertRaises(ValueError):
            kit.geojson_lines('{"type":"Point","coordinates":[1,2]}')

    def test_has_rows_refuses_unsafe_names(self):
        db = sqlite3.connect(":memory:")
        db.execute("CREATE TABLE t (a)")
        self.assertFalse(kit.has_rows(db, "t"))
        db.execute("INSERT INTO t VALUES (1)")
        self.assertTrue(kit.has_rows(db, "t"))
        self.assertFalse(kit.has_rows(db, "absent"))
        with self.assertRaises(ValueError):
            kit.has_rows(db, "t; DROP TABLE t")


class Contract(unittest.TestCase):
    def test_every_builder_meets_the_contract(self):
        modules = stories.builders()
        self.assertEqual([m.STORY["id"] for m in modules], ["climate-stripes", "iron-horse"])

    def test_bad_stories_are_named(self):
        for module in (ModuleType("tools.local_data.stories.nothing"), fake_module(version=None), fake_module(db="elsewhere"), fake_module(tables=[]),
                       fake_module(sources=[{"name": "only a name"}])):
            with self.assertRaises(core.FeedError):
                stories.validate_story(module)
        mismatched = fake_module()
        mismatched.__name__ = "tools.local_data.stories.other_name"
        with self.assertRaises(core.FeedError):
            stories.validate_story(mismatched)


class IronHorse(Case):
    def build(self, name="obs.sqlite"):
        db = stories.read_only(make_db(self.tmp / name, atack_rows))
        self.addCleanup(db.close)
        return iron_horse.build(db)

    def test_miles_stay_with_the_state_the_file_tags(self):
        data = self.build()
        self.assertEqual(data["_observed"], {"from": 1861, "to": 1889})
        self.assertEqual(data["years"], [1861, 1872, 1889])
        by_year = {row["year"]: row for row in data["milesByYear"]}
        self.assertEqual(by_year[1861]["kansas"], 0)
        self.assertEqual(by_year[1861]["neighbours"], 2.5)
        self.assertEqual(by_year[1872]["kansas"], 15)
        self.assertEqual(by_year[1872]["kansasTotal"], 15)
        self.assertEqual(by_year[1889]["kansasTotal"], 18)
        self.assertEqual(by_year[1889]["neighboursTotal"], 2.5)
        self.assertEqual(data["firstKansasYear"], 1872)

    def test_touching_pieces_join_and_each_keeps_its_miles(self):
        data = self.build()
        kansas = data["states"].index("Kansas")
        in_1872 = [entry for entry in data["lines"] if data["years"][entry[0]] == 1872 and entry[1] == kansas]
        self.assertEqual(len(in_1872), 1, "the two 1872 rows meet end to end")
        self.assertEqual(in_1872[0][4], 15)
        self.assertEqual(in_1872[0][5][:2], [6000, 2000], "grid units from the origin")

    def test_limits_count_what_the_rows_hold(self):
        data = self.build()
        self.assertEqual(data["counts"], {"segments": 5, "dated": 0, "gauged": 1, "named": 1, "standardGauge": 1})
        text = " ".join(data["limits"])
        self.assertIn("5 of 5 segments carry no exact date", text)
        self.assertIn("names are recorded for 1 of 5", text)
        self.assertIn("gauge for 1", text)
        self.assertIn("no abandonment", text)
        self.assertIn("1861", text)

    def test_the_same_rows_build_the_same_bytes(self):
        first = self.build()
        self.assertEqual(stories.serialize(first), stories.serialize(self.build("again.sqlite")))

    def test_no_rows_is_nothing_to_show(self):
        db = stories.read_only(make_db(self.tmp / "empty.sqlite", lambda d: d.execute(ATACK)))
        self.addCleanup(db.close)
        self.assertIsNone(iron_horse.build(db))


class ClimateStripes(Case):
    def build(self):
        db = stories.read_only(make_db(self.tmp / "obs.sqlite", climate_rows))
        self.addCleanup(db.close)
        return climate_stripes.build(db)

    def test_shape_scale_and_gaps(self):
        data = self.build()
        self.assertEqual(data["years"], [1895, 1896, 1897])
        self.assertEqual(data["latest"], {"year": 1897, "month": 1})
        self.assertEqual(data["_observed"], {"from": "1895-01", "to": "1897-01"}, "a trailing NULL month is not observed")
        state = data["values"]["tmpc"]["20"]
        self.assertEqual(len(state), 36)
        self.assertEqual(state[0], 501)
        self.assertEqual(state[24], 400)
        self.assertIsNone(state[25], "NULL stays NULL")
        self.assertEqual(data["values"]["pcpn"]["1401"][0], 125)
        self.assertEqual(data["values"]["pdsi"]["20"][0], -150)
        self.assertEqual(len(data["values"]["tmpc"]["1409"]), 36)
        self.assertTrue(all(v is None for v in data["values"]["tmpc"]["1409"]), "a division with no rows is empty, not invented")
        self.assertNotIn("tmax", data["values"])
        self.assertNotIn("20001", data["values"]["tmpc"])

    def test_baselines_and_limits(self):
        data = self.build()
        self.assertEqual(data["baselines"], ["1901-2000", "1991-2020"])
        self.assertEqual(data["normals"]["1901-2000"]["tmpc"]["20"], [490] * 12)
        self.assertEqual(data["normals"]["1991-2020"]["pcpn"]["1401"], [100] * 12)
        self.assertNotIn("pdsi", data["normals"]["1901-2000"])
        text = " ".join(data["limits"])
        self.assertIn("1897 runs through month 1 of 12", text)
        self.assertIn("no", text)
        self.assertIn("revises", text)


class Export(Case):
    def test_writes_bundles_and_leaves_the_database_alone(self):
        path = make_db(self.tmp / "obs.sqlite", atack_rows, climate_rows)
        before = digest(path)
        result = stories.export(stories.Paths(path), self.tmp / "out", now=NOW)
        self.assertEqual(digest(path), before)
        self.assertEqual(sorted(p.name for p in self.tmp.glob("obs*")), ["obs.sqlite"], "no journal or WAL files appear")
        self.assertEqual({k: v["state"] for k, v in result.items()}, {"climate-stripes": "ready", "iron-horse": "ready"})
        bundle = json.loads((self.tmp / "out" / "iron-horse.json").read_text())
        self.assertEqual(bundle["format"], "kfm-story-bundle-v1")
        self.assertEqual(bundle["story"], "iron-horse")
        self.assertEqual(bundle["built_at"], "2026-11-04T12:00:00Z")
        self.assertEqual(bundle["observed"], {"from": 1861, "to": 1889})
        self.assertNotIn("_observed", bundle["data"])
        self.assertTrue(bundle["sources"][0]["citation"])
        self.assertEqual(sorted(p.name for p in (self.tmp / "out").iterdir()), ["climate-stripes.json", "iron-horse.json"])

    def test_one_story_and_a_waiting_story(self):
        path = make_db(self.tmp / "obs.sqlite", atack_rows)
        out = self.tmp / "out"
        result = stories.export(stories.Paths(path), out, "climate-stripes", now=NOW)
        self.assertEqual(result["climate-stripes"]["state"], "waiting")
        self.assertEqual(result["climate-stripes"]["missing"], ["kfm_climdiv_monthly", "kfm_climdiv_normals"])
        self.assertEqual(list(out.iterdir()), [])
        with self.assertRaises(core.FeedError):
            stories.export(stories.Paths(path), out, "no-such-story")

    def test_read_only_connection_cannot_write(self):
        path = make_db(self.tmp / "obs.sqlite")
        db = stories.read_only(path)
        self.addCleanup(db.close)
        with self.assertRaises(sqlite3.OperationalError):
            db.execute("CREATE TABLE nope (a)")

    def test_cli(self):
        path = make_db(self.tmp / "obs.sqlite", atack_rows)
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(stories.main(["list", "--db", str(path)]), 0)
        listing = json.loads(out.getvalue())
        self.assertEqual(listing["iron-horse"]["state"], "ready")
        self.assertEqual(listing["climate-stripes"]["state"], "waiting")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(stories.main(["export", "--db", str(path), "--out", str(self.tmp / "o"), "--story", "iron-horse"]), 0)
        self.assertTrue((self.tmp / "o" / "iron-horse.json").is_file())


class Feed(Case):
    def rows(self, path: Path) -> dict:
        db = sqlite3.connect(path)
        try:
            return {row[0]: row[1:] for row in db.execute("SELECT story_id, version, built_at, sha256, bytes, bundle_json FROM kfm_story_bundles")}
        finally:
            db.close()

    def test_builds_and_reports_the_waiting(self):
        path = make_db(self.tmp / "obs.sqlite", atack_rows)
        result = stories.story_bundles(self.context(path))
        self.assertEqual(result["built"], ["iron-horse"])
        self.assertEqual(result["waiting"]["climate-stripes"]["missing"], ["kfm_climdiv_monthly", "kfm_climdiv_normals"])
        row = self.rows(path)["iron-horse"]
        self.assertEqual(row[0], 1)
        self.assertEqual(row[1], "2026-11-04T12:00:00Z")
        self.assertEqual(row[3], len(row[4].encode()))
        self.assertEqual(json.loads(row[4])["story"], "iron-horse")

    def test_writes_only_when_content_changes(self):
        path = make_db(self.tmp / "obs.sqlite", atack_rows)
        stories.story_bundles(self.context(path))
        first = self.rows(path)["iron-horse"]
        context = self.context(path)
        context.now = lambda: LATER
        result = stories.story_bundles(context)
        self.assertEqual(result["unchanged"], ["iron-horse"])
        self.assertEqual(result["built"], [])
        self.assertEqual(self.rows(path)["iron-horse"], first, "built_at stays with the content")
        db = sqlite3.connect(path)
        db.execute("UPDATE kfm_atack_railroads SET miles=99 WHERE row_number=1")
        db.commit()
        db.close()
        self.assertEqual(stories.story_bundles(context)["built"], ["iron-horse"])
        second = self.rows(path)["iron-horse"]
        self.assertNotEqual(second[2], first[2])
        self.assertEqual(second[1], "2026-11-05T12:00:00Z")

    def test_tables_gone_keeps_the_old_bundle(self):
        path = make_db(self.tmp / "obs.sqlite", atack_rows)
        stories.story_bundles(self.context(path))
        db = sqlite3.connect(path)
        db.execute("DROP TABLE kfm_atack_railroads")
        db.commit()
        db.close()
        result = stories.story_bundles(self.context(path))
        self.assertIn("iron-horse", result["waiting"])
        self.assertIn("iron-horse", self.rows(path))

    def test_writes_under_the_pipeline_lock(self):
        path = make_db(self.tmp / "obs.sqlite", atack_rows)
        seen = []
        real = core.pipeline_lock

        def spy(ctx, *args, **kwargs):
            seen.append(ctx)
            return real(ctx, *args, **kwargs)
        lock = self.tmp / "pipeline.lock"
        with patch.object(core, "pipeline_lock", spy):
            stories.story_bundles(self.context(path, lock=lock))
        self.assertTrue(seen)
        self.assertTrue(lock.exists())

    def test_oversized_bundle_fails_alone_and_the_rest_still_write(self):
        path = make_db(self.tmp / "obs.sqlite", seed_source)
        big = fake_module("big-story", lambda db: {"blob": "x" * (kit.MAX_BUNDLE_BYTES + 1)})
        small = fake_module("small-story", lambda db: {"value": 1, "_observed": {"from": 1, "to": 2}})
        with patch.object(stories, "builders", lambda: [big, small]):
            with self.assertRaisesRegex(core.FeedError, "STORY_BUILD_FAILED big-story"):
                stories.story_bundles(self.context(path))
        rows = self.rows(path)
        self.assertEqual(sorted(rows), ["small-story"])
        self.assertEqual(json.loads(rows["small-story"][4])["observed"], {"from": 1, "to": 2})

    def test_builder_returning_none_waits(self):
        path = make_db(self.tmp / "obs.sqlite", seed_source)
        with patch.object(stories, "builders", lambda: [fake_module("empty-story", lambda db: None)]):
            result = stories.story_bundles(self.context(path))
        self.assertIn("empty-story", result["waiting"])
        self.assertEqual(self.rows(path), {})


class BulkStories(Case):
    def setUp(self):
        super().setUp()
        self.obs = make_db(self.tmp / "obs.sqlite", lambda d: (d.execute("CREATE TABLE kfm_o (a)"), d.execute("INSERT INTO kfm_o VALUES (5)")))
        (self.tmp / "bulk").mkdir()
        self.bulk = make_db(self.tmp / "bulk" / "bulk.sqlite", lambda d: (d.execute("CREATE TABLE kfm_b (a)"), d.execute("INSERT INTO kfm_b VALUES (7)")))

    def test_bulk_story_reads_the_bulk_database_only_when_it_exists(self):
        story = fake_module("bulk-story", lambda db: {"value": db.execute("SELECT a FROM kfm_b").fetchone()[0]}, db="bulk", tables=["kfm_b"])
        with patch.object(stories, "builders", lambda: [story]):
            result = stories.export(stories.Paths(self.obs), self.tmp / "o", now=NOW)
            self.assertEqual(result["bulk-story"]["reason"], "bulk database not available")
            before = digest(self.bulk)
            result = stories.export(stories.Paths(self.obs, self.bulk), self.tmp / "o", now=NOW)
            self.assertEqual(result["bulk-story"]["state"], "ready")
            self.assertEqual(digest(self.bulk), before)
            self.assertEqual(json.loads((self.tmp / "o" / "bulk-story.json").read_text())["data"]["value"], 7)
            context = self.context(self.obs, bulk_db=self.bulk)
            self.assertEqual(stories.story_bundles(context)["built"], ["bulk-story"])

    def test_story_spanning_both_databases(self):
        story = fake_module("both-story", lambda db: {"value": db.execute("SELECT a FROM other.kfm_o").fetchone()[0]}, db="bulk", tables=["kfm_b"], other_tables=["kfm_o"])
        with patch.object(stories, "builders", lambda: [story]):
            result = stories.export(stories.Paths(self.obs, self.bulk), self.tmp / "o", now=NOW)
            self.assertEqual(result["both-story"]["state"], "ready")
            self.assertEqual(json.loads((self.tmp / "o" / "both-story.json").read_text())["data"]["value"], 5)
        absent = fake_module("gap-story", lambda db: {}, db="bulk", tables=["kfm_b"], other_tables=["kfm_absent"])
        with patch.object(stories, "builders", lambda: [absent]):
            result = stories.export(stories.Paths(self.obs, self.bulk), self.tmp / "o", now=NOW)
            self.assertEqual(result["gap-story"]["missing"], ["other.kfm_absent"])


if __name__ == "__main__":
    unittest.main()
