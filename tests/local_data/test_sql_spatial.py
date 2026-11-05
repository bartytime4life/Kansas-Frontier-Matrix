"""Spatial sidecars: an R-tree per geometry table, kept in step with the files each table holds."""
import json
import sqlite3

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feeds as core, sql_spatial as spatial

POINT = '{"type":"Point","coordinates":[-97.3,37.6]}'
LINE = '{"type":"LineString","coordinates":[[-100.1,38.2],[-99.9,38.4]]}'
MULTI = '{"type":"MultiPolygon","coordinates":[[[[-95.5,39.0],[-95.4,39.0],[-95.4,39.1],[-95.5,39.0]]],[[[-95.2,39.2],[-95.1,39.2],[-95.1,39.3],[-95.2,39.2]]]]}'
COLLECTION = '{"type":"GeometryCollection","geometries":[{"type":"Point","coordinates":[-98.0,38.0]},{"type":"Point","coordinates":[-97.9,38.1]}]}'
SCHEMA = """
CREATE TABLE kfm_demo_sites (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, name TEXT, geometry_geojson TEXT, PRIMARY KEY(file_id,row_number));
CREATE TABLE kfm_demo_boxes (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, name TEXT, geometry_geojson TEXT,
  min_lon REAL, min_lat REAL, max_lon REAL, max_lat REAL, PRIMARY KEY(file_id,row_number));
CREATE TABLE kfm_demo_plain (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, value TEXT, PRIMARY KEY(file_id,row_number));
CREATE TABLE kfm_feed_state (feed TEXT PRIMARY KEY, state_json TEXT NOT NULL, updated_at TEXT NOT NULL) WITHOUT ROWID;
"""


class SpatialCase(FeedCase):
    def setUp(self):
        super().setUp()
        db = sqlite3.connect(self.db_path)
        db.executescript(SCHEMA)
        db.executemany("INSERT INTO kfm_demo_sites VALUES (?,?,?,?)", [
            (1, 1, "Wichita", POINT), (1, 2, "Trail", LINE), (1, 3, "Parks", MULTI), (1, 4, "Pair", COLLECTION),
            (1, 5, "No geometry", None), (1, 6, "Bad JSON", "{not json"), (1, 7, "Empty", '{"type":"Point","coordinates":[]}'),
            (1, 8, "Off the planet", '{"type":"Point","coordinates":[-190,95]}'), (2, 1, "Dodge City", '{"type":"Point","coordinates":[-100.0,37.8]}')])
        db.executemany("INSERT INTO kfm_demo_boxes VALUES (?,?,?,?,?,?,?,?)", [
            (3, 1, "Boxed", None, -96.0, 38.0, -95.9, 38.1), (3, 2, "Geometry only", POINT, None, None, None, None),
            (3, 3, "Nothing", None, None, None, None, None), (3, 4, "Inverted box", None, -95.0, 38.0, -96.0, 38.1)])
        db.execute("INSERT INTO kfm_demo_plain VALUES (1,1,'x')")
        db.commit()
        db.close()

    def connect(self):
        db = sqlite3.connect(self.db_path, isolation_level=None)
        self.addCleanup(db.close)
        return db

    def within(self, db, table, west, south, east, north):
        return sorted(row[0] for row in db.execute(
            f"SELECT id FROM {table}_rtree WHERE min_lon<=? AND max_lon>=? AND min_lat<=? AND max_lat>=?", (east, west, north, south)))


class BuildTests(SpatialCase):
    def test_geometry_tables_are_found_by_their_columns_only(self):
        db = self.connect()
        self.assertEqual(spatial.geometry_tables(db), {"kfm_demo_boxes": {"bbox": True, "geometry": True}, "kfm_demo_sites": {"bbox": False, "geometry": True}})

    def test_bounding_boxes_cover_every_geometry_type_and_refuse_the_unusable(self):
        self.assertEqual(spatial.bbox_of(POINT), (-97.3, 37.6, -97.3, 37.6))
        self.assertEqual(spatial.bbox_of(LINE), (-100.1, 38.2, -99.9, 38.4))
        self.assertEqual(spatial.bbox_of(MULTI), (-95.5, 39.0, -95.1, 39.3))
        self.assertEqual(spatial.bbox_of(COLLECTION), (-98.0, 38.0, -97.9, 38.1))
        for bad in (None, "", "{not json", "[]", '{"type":"Point","coordinates":[]}', '{"type":"Point","coordinates":[-190,95]}',
                    '{"type":"Point","coordinates":["x","y"]}', '{"type":"Point","coordinates":[NaN,1]}'):
            self.assertIsNone(spatial.bbox_of(bad), bad)

    def test_build_fills_both_kinds_of_table_and_answers_a_bounding_box(self):
        db = self.connect()
        results = {r["table"]: r for r in spatial.refresh(self.ctx, db)}
        self.assertEqual((results["kfm_demo_sites"]["entries"], results["kfm_demo_sites"]["skipped"], results["kfm_demo_sites"]["files"]), (5, 4, 2))
        # The boxed row through its columns, the geometry-only row through its GeoJSON; nothing for the empty or inverted rows.
        self.assertEqual((results["kfm_demo_boxes"]["entries"], results["kfm_demo_boxes"]["skipped"]), (2, 2))
        self.assertEqual(self.within(db, "kfm_demo_sites", -97.5, 37.5, -97.0, 38.0), [spatial.key(1, 1)])
        self.assertEqual(self.within(db, "kfm_demo_sites", -101, 37, -99, 39), [spatial.key(1, 2), spatial.key(2, 1)])
        self.assertEqual(self.within(db, "kfm_demo_boxes", -97.5, 37.5, -95.5, 38.5), [spatial.key(3, 1), spatial.key(3, 2)])
        self.assertEqual([r["table"] for r in self.logs if r["event"] == "spatial_index"], ["kfm_demo_boxes", "kfm_demo_sites"])
        self.assertEqual({r["table"]: r["state"] for r in spatial.check(db)}, {"kfm_demo_boxes": "current", "kfm_demo_sites": "current"})
        # The join back to the table through the stable key.
        rows = db.execute("SELECT s.name FROM kfm_demo_sites_rtree r JOIN kfm_demo_sites s ON s.file_id = r.id >> 32 AND s.row_number = r.id & 4294967295 "
                          "WHERE r.min_lon<=-97.0 AND r.max_lon>=-97.5 AND r.min_lat<=38.0 AND r.max_lat>=37.5").fetchall()
        self.assertEqual(rows, [("Wichita",)])

    def test_a_replaced_file_drops_its_entries_and_a_new_file_adds_its_own(self):
        db = self.connect()
        spatial.refresh(self.ctx, db)
        self.assertEqual({r["table"]: r["state"] for r in spatial.check(db)}["kfm_demo_sites"], "current")
        # The feed supersedes file 2 with file 9 (as load_version does) and the sidecar is stale until refreshed.
        db.execute("DELETE FROM kfm_demo_sites WHERE file_id=2")
        db.execute("INSERT INTO kfm_demo_sites VALUES (9,1,'Dodge City moved','{\"type\":\"Point\",\"coordinates\":[-100.5,37.7]}')")
        self.assertEqual({r["table"]: r["state"] for r in spatial.check(db)}["kfm_demo_sites"], "stale")
        self.assertEqual(self.within(db, "kfm_demo_sites", -101, 37, -99, 39), [spatial.key(1, 2), spatial.key(2, 1)])
        result = [r for r in spatial.refresh(self.ctx, db, ["kfm_demo_sites"]) if r["table"] == "kfm_demo_sites"][0]
        self.assertEqual((result["added"], result["removed"], result["entries"]), (1, 1, 5))
        self.assertEqual(self.within(db, "kfm_demo_sites", -101, 37, -99, 39), [spatial.key(1, 2), spatial.key(9, 1)])
        self.assertEqual({r["table"]: r["state"] for r in spatial.check(db)}["kfm_demo_sites"], "current")
        state = json.loads(db.execute("SELECT file_ids_json FROM kfm_spatial_index WHERE table_name='kfm_demo_sites'").fetchone()[0])
        self.assertEqual(state, [1, 9])

    def test_a_sidecar_without_a_record_is_rebuilt_from_nothing(self):
        db = self.connect()
        db.execute("CREATE VIRTUAL TABLE kfm_demo_sites_rtree USING rtree(id, min_lon, max_lon, min_lat, max_lat)")
        db.execute("INSERT INTO kfm_demo_sites_rtree VALUES (12345, 0, 1, 0, 1)")
        self.assertEqual({r["table"]: r["state"] for r in spatial.check(db)}["kfm_demo_sites"], "missing")
        spatial.refresh(self.ctx, db, ["kfm_demo_sites"])
        self.assertEqual(db.execute("SELECT COUNT(*) FROM kfm_demo_sites_rtree WHERE id=12345").fetchone()[0], 0)
        self.assertEqual(db.execute("SELECT COUNT(*) FROM kfm_demo_sites_rtree").fetchone()[0], 5)

    def test_rows_beyond_the_key_space_and_unknown_tables_are_refused_or_skipped(self):
        db = self.connect()
        db.execute("INSERT INTO kfm_demo_sites VALUES (1, 4294967296, 'Too far', ?)", (POINT,))
        result = [r for r in spatial.refresh(self.ctx, db, ["kfm_demo_sites"])][0]
        self.assertEqual(result["entries"], 5)
        with self.assertRaisesRegex(core.FeedError, "SPATIAL_TABLE_UNKNOWN kfm_demo_plain"):
            spatial.refresh(self.ctx, db, ["kfm_demo_plain"])

    def test_the_feed_runner_refreshes_sidecars_after_a_feed_and_notes_a_failure(self):
        spatial.refresh_after_feed(self.ctx, "demo")
        self.assertEqual([r["table"] for r in self.logs if r["event"] == "spatial_index"], ["kfm_demo_boxes", "kfm_demo_sites"])
        # A directory where the database should be: the connection fails, the feed's own result stands.
        broken = core.Context(root=self.root, db_path=self.root, log=self.logs.append, now=self.ctx.now)
        spatial.refresh_after_feed(broken, "demo")
        self.assertEqual(self.logs[-1]["event"], "spatial_index_failed")
        self.assertEqual(self.logs[-1]["feed"], "demo")

    def test_the_spatial_subcommand_builds_then_checks_and_reports_stale_with_exit_one(self):
        argv = ["--root", str(self.root), "--db", str(self.db_path), "--lock", str(self.root / "pipeline.lock")]
        self.assertEqual(core.main([*argv, "spatial", "check"]), 1)
        self.assertEqual(core.main([*argv, "spatial", "build"]), 0)
        self.assertEqual(core.main([*argv, "spatial", "check"]), 0)
        self.assertEqual(core.main([*argv, "spatial", "check", "--table", "kfm_demo_sites"]), 0)
        self.assertEqual(core.main([*argv, "spatial", "check", "--table", "kfm_demo_plain"]), 1)
        db = self.connect()
        db.execute("INSERT INTO kfm_demo_sites VALUES (7,1,'Later',?)", (POINT,))
        self.assertEqual(core.main([*argv, "spatial", "check"]), 1)
        self.assertEqual(core.main([*argv, "spatial", "build", "--table", "kfm_demo_sites"]), 0)
        self.assertEqual(core.main([*argv, "spatial", "check"]), 0)
