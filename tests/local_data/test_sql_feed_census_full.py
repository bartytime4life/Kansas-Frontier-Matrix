"""The full Census feeds: every table into the bulk database, in short transactions, without network access."""
from datetime import datetime, timezone
import fcntl
import gzip
import json
import os
import re
import sqlite3
import unittest
from unittest.mock import patch
import zipfile

from tests.local_data.test_sql_feed_census import (ACS, DHC_FIELDS, DHC_GEO, GEOS, KANSAS, LEAD, PL_GEO, SHELLS, VALUES, acs_table,
                                                   dec_segment, dhc_zip, listing, xlsx, zipped)
from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_census as census, sql_feeds as core, sql_snapshot

RECOVERED_SELECTION = "753a2c663a66adb5"   # the bulk database's census-decennial row, 2026-11-03
REAL_PAUSE = census.FULL_CHUNK_PAUSE       # read here, because FullCase sets it to 0
PL3_FIELDS = xlsx({
    "2020 P.L. Segment 1 Definitions": [["TABLE NUMBER AND CONTENTS", "DATA DICTIONARY REFERENCE NAME", "SEGMENT", "MAX SIZE", "DATA TYPE", "NOTES"],
                                        *LEAD, ["Total:", "P0010001", "01", "9", "N", "P1. RACE [3]"],
                                        ["Population of one race:", "P0010002", "01", "9", "N", "Universe: Total population"],
                                        ["White alone", "P0010003", "01", "9", "N", ""]],
    "2020 P.L. Segment 2 Definitions": [["TABLE NUMBER AND CONTENTS", "DATA DICTIONARY REFERENCE NAME", "DATA SEGMENT", "MAX SIZE", "DATA TYPE", "NOTES"],
                                        *LEAD, ["Total:", "H0010001", "02", "9", "N", "H1. OCCUPANCY STATUS [3]"],
                                        ["Occupied", "H0010002", "02", "9", "N", "Universe: Housing units"],
                                        ["Vacant", "H0010003", "02", "9", "N", ""]],
    "2020 P.L. Segment 3 Definitions": [["TABLE NUMBER AND CONTENTS", "DATA DICTIONARY REFERENCE NAME", "DATA SEGMENT", "MAX SIZE", "DATA TYPE", "NOTES"],
                                        *LEAD, ["Total:", "P0050001", "03", "9", "N", "P5. GROUP QUARTERS [2]"],
                                        ["Institutionalized", "P0050002", "03", "9", "N", "Universe: In group quarters"]],
})
PL_ROWS, DHC_ROWS = 3 * 3 + 3 * 3 + 3 * 2, 4 * 4 + 4 * 4 + 4 * 2   # kept geographies times cells, per segment


def pl3_zip(extra=0):
    rows = lambda seg, cells: [(f"{n:07d}", [n * seg + c + extra for c in range(cells)]) for n in range(1, 5)]
    return zipped({"ks000012020.pl": dec_segment("PLST", 1, rows(1, 3)), "ks000022020.pl": dec_segment("PLST", 2, rows(2, 3)),
                   "ks000032020.pl": dec_segment("PLST", 3, rows(3, 2)), "ksgeo2020.pl": "\n".join(PL_GEO) + "\n"})


class FullCase(FeedCase):
    """FeedCase with a bulk database beside observations.sqlite, chunks of a few rows and no waiting."""

    def setUp(self):
        super().setUp()
        self.bulk_path = self.root / "bulk-sql/kfm-bulk.sqlite"
        self.bulk = core.Context(root=self.root, db_path=self.bulk_path, bulk_db=self.bulk_path, lock=self.ctx.lock, fetch=self.web,
                                 now=self.ctx.now, log=self.logs.append, floor=0)
        core.init_bulk(self.bulk)
        for name, value in (("FULL_CHUNK_PAUSE", 0), ("FULL_REQUEST_SPACING", 0), ("FULL_BATCH_ROWS", 2)):
            patcher = patch.object(census, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def b(self, sql, *args):
        db = sqlite3.connect(self.bulk_path)
        try:
            return db.execute(sql, args).fetchall()
        finally:
            db.close()

    def assert_clean_load(self, table):
        """Every source's rows are numbered 1..n with nothing missing or repeated, and match its recorded count."""
        for file_id, rows in self.b("SELECT file_id, imported_rows FROM kfm_sql_sources WHERE state='complete'"):
            count, low, high = self.b(f"SELECT COUNT(*), MIN(row_number), MAX(row_number) FROM {table} WHERE file_id=?", file_id)[0]
            if count:
                self.assertEqual((count, low, high), (rows, 1, rows))
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='loading'"), [(0,)])


class DecennialCase(FullCase):
    def setUp(self):
        super().setUp()
        self.serve()

    def serve(self, pl=None, dhc=None):
        (pl_url, pl_layout, _), (dhc_url, dhc_layout, _) = census.DEC_SOURCES["pl"], census.DEC_SOURCES["dhc"]
        self.web.routes = {pl_url: pl or pl3_zip(), pl_layout: PL3_FIELDS, dhc_url: dhc or dhc_zip(), dhc_layout: DHC_FIELDS}

    def values(self):
        return self.b("SELECT product, vintage, table_id, geoid, variable, value FROM kfm_census_decennial_values "
                      "ORDER BY product, geoid, variable")

    def assert_no_duplicates(self):
        self.assertEqual(self.b("SELECT product, geoid, variable, COUNT(*) FROM kfm_census_decennial_values "
                                "GROUP BY 1, 2, 3 HAVING COUNT(*) > 1"), [])
        self.assert_clean_load("kfm_census_decennial_values")


class DecennialFullTests(DecennialCase):
    def test_it_refuses_any_database_but_the_bulk_one(self):
        for ctx in (self.ctx, core.Context(root=self.root, db_path=self.db_path, bulk_db=self.bulk_path, lock=self.ctx.lock, fetch=self.web)):
            with self.assertRaisesRegex(core.FeedError, "BULK_DATABASE_REQUIRED"):
                census.census_decennial_full(ctx)
            with self.assertRaisesRegex(core.FeedError, "BULK_DATABASE_REQUIRED"):
                census.census_acs_full(ctx)
        self.assertEqual(self.q("SELECT name FROM sqlite_master WHERE name LIKE 'kfm_census%' OR name='kfm_feed_state'"), [])
        self.assertEqual(self.web.calls, [])

    def test_every_table_and_the_blocks_of_both_products_load(self):
        result = census.census_decennial_full(self.bulk)
        self.assertEqual((result["complete"], result["pending"], result["rows"]), (["pl", "dhc"], [], PL_ROWS + DHC_ROWS))
        self.assertEqual(self.b("SELECT product, COUNT(*) FROM kfm_census_decennial_values GROUP BY 1 ORDER BY 1"),
                         [("dhc", DHC_ROWS), ("pl", PL_ROWS)])
        # A block is summary level 750 in the PL and 100 in the DHC; both carry cell values. Voting districts and components stay out.
        self.assertEqual(self.b("SELECT product, COUNT(DISTINCT geoid) FROM kfm_census_decennial_values WHERE geoid LIKE '7500000%' "
                                "OR geoid LIKE '1000000%' GROUP BY 1 ORDER BY 1"), [("dhc", 1), ("pl", 1)])
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_census_decennial_values WHERE geoid LIKE '7000000%' OR geoid LIKE '0400001%'"), [(0,)])
        # Iterations the curated feed leaves out are here: every table of the workbook.
        self.assertEqual(self.b("SELECT DISTINCT table_id FROM kfm_census_decennial_values WHERE product='dhc' ORDER BY 1"),
                         [("P1",), ("P12",), ("P12A",), ("P12J",), ("P13",), ("PCT12A",)])
        self.assertEqual(self.b("SELECT value FROM kfm_census_decennial_values WHERE geoid='1000000US200019526001000' AND variable='P0130001'"),
                         [(".",)])
        self.assertEqual(self.b("SELECT source_id, json_extract(receipt_json,'$.key') FROM kfm_sql_sources WHERE source_id LIKE '%segment' ORDER BY 2"),
                         [("census-dhc2020-segment", f"dhc2020/segment-{s:02d}") for s in (1, 2, 3)]
                         + [("census-pl2020-segment", f"pl2020/segment-{s:02d}") for s in (1, 2, 3)])
        self.assert_no_duplicates()
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])

    def test_a_rerun_makes_no_request_until_the_yearly_recheck(self):
        census.census_decennial_full(self.bulk)
        self.web.calls.clear()
        again = census.census_decennial_full(self.bulk)
        self.assertEqual((again["rows"], again["segments"], self.web.calls), (0, [], []))

    def seed_the_recovered_state(self):
        """What the interrupted original load left: PL labels, geography and two segments, with its state row."""
        zip_bytes = self.web.routes[census.DEC_SOURCES["pl"][0]]
        levels, zip_url, stem = census.DEC_FULL_LEVELS["pl"], census.DEC_SOURCES["pl"][0], "pl2020"
        fields = census._pl_fields(census._xlsx(PL3_FIELDS, "fields"))
        tables = {name: table for _, table, name, *_ in fields}
        db = core.open_db(self.bulk)
        db.executescript(census.DEC_SCHEMA)
        work = core.temp_path(self.bulk, "seed.gz")
        archive = core.temp_path(self.bulk, "seed.zip")
        archive.write_bytes(zip_bytes)
        with zipfile.ZipFile(archive) as z:
            kept, geo = census._dec_geo_cut(z, "pl", b"PLST", work, levels=levels, geography_only=())
            path, digest = core.store_raw(self.bulk, "census-decennial", f"{stem}/kansas-ksgeo2020.pl-{core.file_sha256(work)[:12]}.txt.gz", work,
                                          url=zip_url, original=archive, extra={"key": f"{stem}/geo", "kansas_rows": kept})
            core.load_version(db, self.bulk, source_id="census-pl2020-geo", key=f"{stem}/geo", path=path, digest=digest, url=zip_url,
                              table="kfm_census_decennial_geographies", rows=census._dec_geo_rows("pl")(path), width=len(census.DEC_GEO_COLUMNS) + 2)
            for seg in (1, 2):
                names = [name for s, _, name, *_ in fields if s == seg]
                member, key = f"ks{seg:05d}2020.pl", f"{stem}/segment-{seg:02d}"
                kept = census._dec_segment_cut(z, member, b"PLST", seg, names, list(range(len(names))), {g.encode() for g in geo}, work)
                path, digest = core.store_raw(self.bulk, "census-decennial", f"{stem}/kansas-{member}-{core.file_sha256(work)[:12]}.txt.gz", work,
                                              url=zip_url, original=archive, extra={"key": key, "member": member, "kansas_rows": kept})
                core.load_version(db, self.bulk, source_id="census-pl2020-segment", key=key, path=path, digest=digest, url=zip_url,
                                  table="kfm_census_decennial_values", rows=census._dec_value_rows("pl", geo, tables)(path), width=6)
        core.set_state(db, self.bulk, "census-decennial", {"pl": {
            "complete": False, "last_modified": "Thu, 12 Aug 2021 17:18:47 GMT", "segments_done": [1, 2], "selection": RECOVERED_SELECTION,
            "zip_sha256": core.file_sha256(archive)}})
        archive.unlink()
        db.close()

    def test_it_continues_from_the_recovered_state_and_rows(self):
        self.assertEqual(census._dec_full_signature("pl"), RECOVERED_SELECTION)
        self.seed_the_recovered_state()
        before = self.b("SELECT file_id, sha256, imported_rows FROM kfm_sql_sources WHERE source_id='census-pl2020-segment' ORDER BY 1")
        self.assertEqual([rows for _, _, rows in before], [9, 9])
        result = census.census_decennial_full(self.bulk)
        self.assertEqual(result["segments"][0], "pl2020/segment-03")
        self.assertEqual(result["rows"], 3 * 2 + DHC_ROWS)
        self.assertEqual(self.b("SELECT file_id, sha256, imported_rows FROM kfm_sql_sources WHERE source_id='census-pl2020-segment' AND "
                                "json_extract(receipt_json,'$.key')<>'pl2020/segment-03' ORDER BY 1"), before)
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_census_decennial_values WHERE product='pl'"), [(PL_ROWS,)])
        state = json.loads(self.b("SELECT state_json FROM kfm_feed_state WHERE feed='census-decennial'")[0][0])
        self.assertEqual((state["pl"]["complete"], state["pl"]["segments_done"], state["pl"]["selection"]), (True, [1, 2, 3], RECOVERED_SELECTION))
        self.assert_no_duplicates()

    def reference(self):
        """The values an uninterrupted load gives, from a second bulk database."""
        path = self.root / "bulk-reference/kfm-bulk.sqlite"
        ctx = core.Context(root=self.root, db_path=path, bulk_db=path, fetch=self.web, now=self.ctx.now, log=self.logs.append, floor=0)
        core.init_bulk(ctx)
        census.census_decennial_full(ctx)
        db = sqlite3.connect(path)
        try:
            return db.execute("SELECT product, vintage, table_id, geoid, variable, value FROM kfm_census_decennial_values "
                              "ORDER BY product, geoid, variable").fetchall()
        finally:
            db.close()

    def test_an_interrupted_load_resumes_with_no_duplicate_or_lost_row(self):
        expected = self.reference()
        self.assertEqual(len(expected), PL_ROWS + DHC_ROWS)
        real, calls = census._num, []

        def failing(value):
            calls.append(value)
            if len(calls) == 15:
                raise RuntimeError("disk went away")
            return real(value)
        with patch.object(census, "_num", failing), self.assertRaisesRegex(RuntimeError, "disk went away"):
            census.census_decennial_full(self.bulk, chunk_rows=4)
        # What committed stays, numbered from 1; the source is not complete and its segment is not recorded as done.
        loading = self.b("SELECT file_id, imported_rows FROM kfm_sql_sources WHERE state='loading'")
        self.assertEqual(len(loading), 1)
        self.assertEqual(loading[0][1], 0)
        partial = self.b("SELECT COUNT(*), MAX(row_number) FROM kfm_census_decennial_values WHERE file_id=?", loading[0][0])[0]
        self.assertTrue(0 < partial[0] < 9 and partial[0] == partial[1] and partial[0] % 4 == 0, partial)
        state = json.loads(self.b("SELECT state_json FROM kfm_feed_state WHERE feed='census-decennial'")[0][0])
        self.assertLess(len(state["pl"]["segments_done"]), 3)
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])
        again = census.census_decennial_full(self.bulk, chunk_rows=4)
        self.assertEqual(again["complete"], ["pl", "dhc"])
        self.assertEqual(self.values(), expected)
        self.assert_no_duplicates()

    def test_a_killed_process_resumes_with_no_duplicate_or_lost_row(self):
        expected = self.reference()
        pid = os.fork()
        if pid == 0:   # no cleanup or rollback runs: this is SIGKILL or a power cut with a transaction open
            try:
                real, calls = census._num, []

                def dying(value):
                    calls.append(value)
                    if len(calls) == 23:
                        os._exit(9)
                    return real(value)
                census._num = dying
                census.census_decennial_full(self.bulk, chunk_rows=4)
            finally:
                os._exit(1)
        self.assertEqual(os.waitstatus_to_exitcode(os.waitpid(pid, 0)[1]), 9)
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='loading'"), [(1,)])
        partial = self.b("SELECT COUNT(*) FROM kfm_census_decennial_values")[0][0]
        self.assertTrue(0 < partial < PL_ROWS + DHC_ROWS, partial)
        for leftover in (self.root / "tmp-sql-feeds").iterdir():   # a killed process cannot clean up; the next one's pid differs
            leftover.unlink()
        self.assertEqual(census.census_decennial_full(self.bulk, chunk_rows=4)["complete"], ["pl", "dhc"])
        self.assertEqual(self.values(), expected)
        self.assert_no_duplicates()

    def test_the_lock_is_free_between_chunks_and_held_during_them(self):
        def lock_is_free() -> bool:
            with open(self.bulk.lock, "a") as other:
                try:
                    fcntl.flock(other, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError:
                    return False
                fcntl.flock(other, fcntl.LOCK_UN)
                return True
        gaps, during, sizes, last = [], [], [], {"rows": 0}
        real_gap, real_num = census._between_chunks, census._num

        def gap(db, pause):
            gaps.append(lock_is_free())
            rows = db.execute("SELECT COUNT(*) FROM kfm_census_decennial_values").fetchone()[0]
            sizes.append(rows - last["rows"])
            last["rows"] = rows
            real_gap(db, pause)

        def num(value):
            during.append(lock_is_free())
            return real_num(value)
        with patch.object(census, "_between_chunks", gap), patch.object(census, "_num", num):
            result = census.census_decennial_full(self.bulk, chunk_rows=4)
        self.assertEqual(result["rows"], PL_ROWS + DHC_ROWS)
        self.assertGreater(result["transactions"], (PL_ROWS + DHC_ROWS) // 6)
        self.assertTrue(all(gaps) and len(gaps) == result["transactions"], gaps)
        self.assertFalse(any(during))
        self.assertLessEqual(max(sizes), 5)   # chunk_rows 4, in batches of 2: never more than one batch over
        self.assert_no_duplicates()

    def test_each_gap_outlasts_a_waiters_poll_when_more_of_the_file_is_coming(self):
        # flock is not fair, and pipeline_lock's waiters look every 5 seconds: taking it straight back would starve them.
        pauses = []
        self.assertGreater(REAL_PAUSE, 5)
        with patch.object(census, "FULL_CHUNK_PAUSE", REAL_PAUSE), patch.object(census.time, "sleep", pauses.append):
            census.census_decennial_full(self.bulk, chunk_rows=4)
        self.assertTrue(pauses)
        self.assertTrue(all(p > 5 for p in pauses), pauses)

    def test_a_chunk_ends_when_its_time_is_up_however_few_rows_it_has(self):
        with patch.object(census, "FULL_CHUNK_SECONDS", 0):
            result = census.census_decennial_full(self.bulk)
        # Each transaction ends at once; the rows still arrive, and in order.
        self.assertEqual(result["rows"], PL_ROWS + DHC_ROWS)
        self.assertGreater(result["transactions"], 30)
        self.assert_no_duplicates()

    def test_a_run_stops_at_its_budget_and_the_next_one_resumes_without_reloading(self):
        first = census.census_decennial_full(self.bulk, run_rows=15, chunk_rows=2)   # labels 8, geography 3, then part of segment 1
        self.assertEqual((first["complete"], first["partial"], first["pending"]), ([], ["pl2020/segment-01"], ["pl", "dhc"]))
        self.assertEqual(first["rows"], 4)
        self.assertEqual(self.b("SELECT COUNT(*), MAX(row_number) FROM kfm_census_decennial_values"), [(4, 4)])
        self.assertEqual(self.b("SELECT imported_rows, state FROM kfm_sql_sources WHERE source_id='census-pl2020-segment'"), [(0, "loading")])
        second = census.census_decennial_full(self.bulk)
        self.assertEqual(second["complete"], ["pl", "dhc"])
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_census_decennial_values"), [(PL_ROWS + DHC_ROWS,)])
        self.assert_no_duplicates()

    def test_a_source_with_a_row_missing_is_never_recorded_complete(self):
        census.census_decennial_full(self.bulk, run_rows=15, chunk_rows=2)
        db = sqlite3.connect(self.bulk_path)
        db.execute("DELETE FROM kfm_census_decennial_values WHERE row_number=1")
        db.commit()
        db.close()
        with self.assertRaisesRegex(core.FeedError, "FULL_LOAD_COUNT_MISMATCH pl2020/segment-01 8 9"):
            census.census_decennial_full(self.bulk)
        self.assertEqual(self.b("SELECT imported_rows, state FROM kfm_sql_sources WHERE source_id='census-pl2020-segment'"), [(0, "loading")])

    def test_a_run_out_of_time_starts_no_new_work(self):
        result = census.census_decennial_full(self.bulk, run_seconds=0)
        self.assertEqual((result["rows"], result["pending"], self.web.calls), (0, ["pl", "dhc"], []))

    def test_the_verified_snapshot_works_during_a_partial_load_and_counts_only_complete_sources(self):
        census.census_decennial_full(self.bulk, run_rows=5, chunk_rows=2)
        complete = self.b("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='complete'")[0][0]
        result = sql_snapshot.snapshot(self.bulk, self.root / "snapshots", device_check=False, floor_fraction=0)
        self.assertEqual((result["state"], result["source_files"]), ("verified", complete))
        self.assertEqual(core.status(self.bulk)["source_files"], complete)
        self.assertEqual(census.census_decennial_full(self.bulk)["complete"], ["pl", "dhc"])
        self.assert_no_duplicates()

    def test_a_republished_zip_replaces_only_what_changed_and_a_partial_version_is_abandoned(self):
        census.census_decennial_full(self.bulk)
        self.bulk.now = lambda: datetime(2027, 11, 6, 15, 0, tzinfo=timezone.utc)
        self.serve(pl=pl3_zip(extra=1000))
        first = census.census_decennial_full(self.bulk, run_rows=6, chunk_rows=2)
        self.assertEqual(first["partial"], ["pl2020/segment-01"])
        self.assertEqual(self.b("SELECT state FROM kfm_sql_sources WHERE source_id='census-pl2020-segment' AND "
                                "json_extract(receipt_json,'$.key')='pl2020/segment-01' ORDER BY file_id"), [("superseded",), ("loading",)])
        # Before the partial version finishes the provider publishes again: it is abandoned too.
        self.serve(pl=pl3_zip(extra=2000))
        result = census.census_decennial_full(self.bulk)
        self.assertEqual((result["complete"], result["unchanged"]), (["pl", "dhc"], ["dhc"]))
        self.assertEqual(self.b("SELECT state, COUNT(*) FROM kfm_sql_sources WHERE source_id='census-pl2020-segment' GROUP BY 1 ORDER BY 1"),
                         [("complete", 3), ("superseded", 4)])
        self.assertEqual(self.b("SELECT COUNT(*), MIN(value) >= 2000 FROM kfm_census_decennial_values WHERE product='pl'"), [(PL_ROWS, 1)])
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_census_decennial_values WHERE file_id IN "
                                "(SELECT file_id FROM kfm_sql_sources WHERE state='superseded')"), [(0,)])
        self.assert_no_duplicates()

    def test_a_crash_while_removing_the_old_version_resumes_the_removal(self):
        census.census_decennial_full(self.bulk)
        self.bulk.now = lambda: datetime(2027, 11, 6, 15, 0, tzinfo=timezone.utc)
        self.serve(pl=pl3_zip(extra=1000))
        real, gaps = census._between_chunks, []

        def crash(db, pause):
            gaps.append(1)
            if db.execute("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='superseded'").fetchone()[0] and len(gaps) == 1:
                raise RuntimeError("power cut")
            real(db, pause)
        with patch.object(census, "_between_chunks", crash), self.assertRaisesRegex(RuntimeError, "power cut"):
            census.census_decennial_full(self.bulk, chunk_rows=2)
        self.assertEqual(self.b("SELECT state, COUNT(*) FROM kfm_sql_sources WHERE source_id='census-pl2020-segment' GROUP BY 1 ORDER BY 1"),
                         [("complete", 2), ("loading", 1), ("superseded", 1)])
        left = self.b("SELECT COUNT(*) FROM kfm_census_decennial_values WHERE file_id IN (SELECT file_id FROM kfm_sql_sources WHERE state='superseded')")
        self.assertTrue(0 < left[0][0] < 9, left)
        census.census_decennial_full(self.bulk)
        self.assertEqual(self.b("SELECT COUNT(*), MIN(value) >= 1000 FROM kfm_census_decennial_values WHERE product='pl'"), [(PL_ROWS, 1)])
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_census_decennial_values WHERE file_id IN "
                                "(SELECT file_id FROM kfm_sql_sources WHERE state='superseded')"), [(0,)])
        self.assert_no_duplicates()

    def test_the_curated_feed_and_its_database_are_untouched(self):
        curated = census.census_decennial(self.ctx)
        rows = self.q("SELECT COUNT(*) FROM kfm_census_decennial_values")
        states = self.q("SELECT state_json FROM kfm_feed_state WHERE feed='census-decennial'")
        sources = self.q("SELECT COUNT(*) FROM kfm_sql_sources")
        full = census.census_decennial_full(self.bulk)
        self.assertEqual((self.q("SELECT COUNT(*) FROM kfm_census_decennial_values"), self.q("SELECT state_json FROM kfm_feed_state WHERE feed='census-decennial'"),
                          self.q("SELECT COUNT(*) FROM kfm_sql_sources")), (rows, states, sources))
        self.assertEqual(full["rows"], PL_ROWS + DHC_ROWS)
        self.assertGreater(full["rows"], curated["rows"])
        self.web.calls.clear()
        self.assertEqual(census.census_decennial(self.ctx)["segments"], [])
        self.assertEqual(self.web.calls, [])
        self.assertNotEqual(self.b("SELECT state_json FROM kfm_feed_state WHERE feed='census-decennial'"), states)


class AcsFullTests(FullCase):
    TABLES = ("B01003", "B19013", "B25003")

    def setUp(self):
        super().setUp()
        self.listed = {t: "2026-01-29 07:30" for t in (*self.TABLES, "B992705")}
        self.files = {t: acs_table(t) for t in self.TABLES}
        self.files["B992705"] = acs_table("B992705", [[10, 3, 7], [20, 6, 14], [30, 9, 21], [40, 1, 39], [50, 2, 48], [60, 5, 55]],
                                          header="GEO_ID|B992705_E001|B992705_E002|B992705_E003")
        self.serve()

    def routes(self, vintage, bom=b""):
        """One release's files. Each release's Kansas numbers differ, as they do in fact; 2024 is the fixture as written."""
        base, serve = census.ACS.format(vintage=vintage), lambda body: re.sub(rb"(?m)^(0400000US20\|)-?\d+", rb"\g<1>%d" % vintage, body)
        return {
            base + f"documentation/Geos{vintage}5YR.txt": bom + GEOS.replace("Allen County", f"Allen County {vintage}").encode(),
            base + f"documentation/ACS{vintage}5YR_Table_Shells.txt": bom + SHELLS.replace("in 2024", f"in {vintage}").encode(),
            base + "documentation/": listing({f"Geos{vintage}5YR.txt": "2026-01-22 07:15", f"ACS{vintage}5YR_Table_Shells.txt": "2026-01-22 07:15"}),
            **{base + f"data/5YRData/acsdt5y{vintage}-{t.lower()}.dat": body if vintage == 2024 else serve(body) for t, body in self.files.items()},
            base + "data/5YRData/": listing({"5YRData.zip": "2026-01-29 07:30",
                                             **{f"acsdt5y{vintage}-{t.lower()}.dat": when for t, when in self.listed.items()}}),
        }

    def serve(self):
        self.web.routes = self.routes(2024)

    def run_acs(self, **options):
        return census.census_acs_full(self.bulk, **{"vintages": (2024,), **options})

    def test_every_listed_table_loads_including_those_with_estimates_alone(self):
        result = self.run_acs()
        self.assertEqual((result["tables_loaded"], result["pending"], result["rows"]), (4, 0, 15 + 9))
        self.assertEqual(result["tables"], [f"acs5/2024/{t}" for t in ("B01003", "B19013", "B25003", "B992705")])
        self.assertEqual(self.b("SELECT geo_id, variable, estimate, margin_of_error FROM kfm_census_acs_values WHERE table_id='B992705' AND "
                                "geo_id='0500000US20001' ORDER BY variable"),
                         [("0500000US20001", "B992705_001", 30, None), ("0500000US20001", "B992705_002", 9, None),
                          ("0500000US20001", "B992705_003", 21, None)])
        self.assertEqual({g for (g,) in self.b("SELECT DISTINCT geo_id FROM kfm_census_acs_values")}, KANSAS)
        self.assertEqual(self.b("SELECT estimate, margin_of_error FROM kfm_census_acs_values WHERE variable='B19013_001' AND geo_id='860Z200US66002'"),
                         [(-666666666, -222222222)])
        kept = next((self.root / "data/raw/sql-feeds/census-acs/acs5/2024").glob("kansas-acsdt5y2024-b992705-*.dat.gz"))
        self.assertEqual(gzip.decompress(kept.read_bytes()).decode().splitlines()[0], "GEO_ID|B992705_E001|B992705_E002|B992705_E003")
        self.assert_clean_load("kfm_census_acs_values")
        self.assertEqual(self.q("SELECT name FROM sqlite_master WHERE name='kfm_census_acs_values'"), [])
        self.assertEqual(self.b("SELECT feed FROM kfm_feed_state"), [("census-acs",)])

    def test_the_curated_feed_still_stops_on_a_header_without_margins(self):
        with self.assertRaisesRegex(core.FeedError, "ACS_COLUMNS_CHANGED acsdt5y2024-b992705.dat"):
            census.census_acs(self.ctx, tables=("B992705",))

    def test_any_other_header_stops_the_full_feed_too(self):
        self.files["B25003"] = acs_table("B25003", header="GEO_ID|B25003_E001|B25003_M001|B25003_E002|B25003_X002|B25003_E003|B25003_M003")
        self.serve()
        with self.assertRaisesRegex(core.FeedError, "ACS_COLUMNS_CHANGED acsdt5y2024-b25003.dat"):
            self.run_acs()

    def test_all_four_releases_load_newest_first_with_their_byte_order_marks(self):
        self.web.routes = {**self.routes(2024), **self.routes(2023, b"\xef\xbb\xbf"), **self.routes(2022, b"\xef\xbb\xbf"),
                           **self.routes(2021, b"\xef\xbb\xbf")}
        result = census.census_acs_full(self.bulk, vintages=(*census.ACS_FULL_VINTAGES, 2025))
        self.assertEqual(census.ACS_FULL_VINTAGES, (2024, 2023, 2022, 2021))
        self.assertEqual((result["unpublished"], result["pending"], result["rows"]), ([2025], 0, 4 * 24))
        self.assertEqual(self.b("SELECT vintage, COUNT(*) FROM kfm_census_acs_geographies GROUP BY 1 ORDER BY 1"), [(v, 3) for v in (2021, 2022, 2023, 2024)])
        self.assertEqual(self.b("SELECT DISTINCT vintage FROM kfm_census_acs_values ORDER BY 1"), [(2021,), (2022,), (2023,), (2024,)])
        self.assert_clean_load("kfm_census_acs_values")
        self.web.calls.clear()
        self.assertEqual(census.census_acs_full(self.bulk)["tables_loaded"], 0)
        self.assertFalse([u for u in self.web.calls if u.endswith((".dat", ".txt"))])

    def test_no_table_is_cut_before_every_geography_has_loaded(self):
        first = self.run_acs(run_rows=1, chunk_rows=1)
        self.assertEqual((first["pending_vintages"], first["tables_loaded"]), ([2024], 0))
        self.assertFalse([u for u in self.web.calls if u.endswith(".dat")])
        self.assertEqual(self.b("SELECT state FROM kfm_sql_sources"), [("loading",)])
        result = self.run_acs()
        self.assertEqual(result["rows"], 24)
        self.assertEqual({g for (g,) in self.b("SELECT DISTINCT geo_id FROM kfm_census_acs_values")}, KANSAS)

    def test_a_table_interrupted_part_way_resumes_with_no_duplicate_or_lost_row(self):
        real, calls = census._num, []

        def failing(value):
            calls.append(value)
            if len(calls) == 9:
                raise RuntimeError("disk went away")
            return real(value)
        with patch.object(census, "_num", failing), self.assertRaisesRegex(RuntimeError, "disk went away"):
            self.run_acs(chunk_rows=2)
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='loading'"), [(1,)])
        partial = self.b("SELECT COUNT(*) FROM kfm_census_acs_values")[0][0]
        self.assertGreater(partial, 0)
        result = self.run_acs(chunk_rows=2)
        self.assertEqual((result["pending"], self.b("SELECT COUNT(*) FROM kfm_census_acs_values")[0][0]), (0, 24))
        self.assertEqual(self.b("SELECT geo_id, variable, COUNT(*) FROM kfm_census_acs_values GROUP BY 1, 2 HAVING COUNT(*) > 1"), [])
        self.assert_clean_load("kfm_census_acs_values")

    def test_a_republished_table_replaces_its_rows_and_a_rerun_reads_only_the_listings(self):
        self.run_acs()
        changed = [list(v) for v in VALUES["B19013"]]
        changed[2] = [61000, 4400]
        self.listed.update(B19013="2026-03-30 15:30", B01003="2026-03-30 15:30")
        self.files["B19013"] = acs_table("B19013", changed)
        self.serve()
        result = self.run_acs()
        self.assertEqual((result["tables"], result["unchanged"]), (["acs5/2024/B19013"], ["acs5/2024/B01003"]))
        self.assertEqual(self.b("SELECT estimate, margin_of_error FROM kfm_census_acs_values WHERE geo_id='0500000US20001' AND table_id='B19013'"),
                         [(61000, 4400)])
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_census_acs_values"), [(24,)])
        self.web.calls.clear()
        self.assertEqual(self.run_acs()["tables"], [])
        self.assertEqual(self.web.calls, [ACS + "documentation/", ACS + "data/5YRData/"])

    def test_a_table_the_firewall_rejects_is_reported_and_holds_nothing_back(self):
        # www2.census.gov answers these with 200 and this page, as for 2023's B19053 and 2024's B18101F on 2026-11-03.
        page = (b"<html><head><title>Request Rejected</title></head><body>The requested URL was rejected. "
                b"Please consult with your administrator.<br><br>Your support ID is: 1</body></html>")
        self.files["B19013"] = page
        self.serve()
        result = self.run_acs()
        self.assertEqual((result["rejected"], result["tables_loaded"], result["pending"]), (["acs5/2024/B19013"], 3, 1))
        self.assertEqual(self.b("SELECT COUNT(*) FROM kfm_census_acs_values WHERE table_id='B19013'"), [(0,)])
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])
        self.files["B19013"] = acs_table("B19013")
        self.serve()
        again = self.run_acs()
        self.assertEqual((again["rejected"], again["tables"], again["pending"]), ([], ["acs5/2024/B19013"], 0))

    def test_a_table_identical_in_two_releases_is_reported_and_holds_nothing_back(self):
        routes = {**self.routes(2024), **self.routes(2023)}
        routes[census.ACS.format(vintage=2023) + "data/5YRData/acsdt5y2023-b01003.dat"] = self.files["B01003"]
        self.web.routes = routes
        result = census.census_acs_full(self.bulk, vintages=(2024, 2023))
        self.assertEqual((result["shared"], result["tables_loaded"], result["pending"]), (["acs5/2023/B01003"], 7, 1))

    def test_national_file_requests_are_spaced(self):
        sleeps = []
        with patch.object(census, "FULL_REQUEST_SPACING", 2), patch.object(census.time, "sleep", sleeps.append):
            self.run_acs()
        waits = [s for s in sleeps if s]   # the chunk pause is 0 here
        self.assertEqual(len(waits), 3)    # four tables, none before the first
        self.assertTrue(all(0 < s <= 2 for s in waits), waits)


if __name__ == "__main__":
    unittest.main()
