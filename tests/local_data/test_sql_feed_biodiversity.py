"""SQL feed for GBIF occurrences in Kansas, without network access."""
from collections import Counter
from datetime import datetime, timezone
import gzip
import json
import sqlite3
import unittest
from unittest.mock import patch
import urllib.parse

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_biodiversity as bio, sql_feeds as core

KANSAS, MISSOURI = "USA.17_1", "USA.26_1"
CC_BY = "http://creativecommons.org/licenses/by/4.0/legalcode"
CC0 = "http://creativecommons.org/publicdomain/zero/1.0/legalcode"


def at(*args):
    return lambda: datetime(*args, 15, 0, tzinfo=timezone.utc)


def record(key, dataset="ds-big", year=2020, month=5, day=1, lat=38.5, lon=-98.0, state="Kansas", level1=KANSAS, county="USA.17.1_1", family=9,
           license=CC_BY, basis="HUMAN_OBSERVATION", interpreted="2026-10-01T00:00:00.000+00:00", **more):
    found = {"key": key, "gbifID": str(key), "datasetKey": dataset, "publishingOrgKey": "org-1", "license": license, "basisOfRecord": basis,
             "countryCode": "US", "stateProvince": state, "scientificName": f"Species {key}", "familyKey": family, "occurrenceID": f"occ-{key}",
             "issues": ["B_ISSUE", "A_ISSUE"], "lastInterpreted": interpreted, "lastCrawled": interpreted, "crawlId": 7,
             "classifications": {"checklist": {"usage": {"key": "x"}}}, "extensions": {"media": [1, 2, 3]}, "http://unknown.org/status": "x", **more}
    for name, value in (("year", year), ("month", month), ("day", day), ("decimalLatitude", lat), ("decimalLongitude", lon)):
        if value is not None:
            found[name] = value
    if level1:
        found["gadm"] = {"level0": {"gid": "USA", "name": "United States"}, "level1": {"gid": level1, "name": "State"},
                         **({"level2": {"gid": county, "name": "County"}} if county else {})}
    return found


def dataset(key, license=CC_BY):
    return {"key": key, "title": f"Title of {key}", "doi": f"10.0/{key}", "license": license, "publishingOrganizationKey": "org-1", "type": "OCCURRENCE",
            "homepage": "https://example.org/", "pubDate": "2026-01-01", "modified": "2026-02-01",
            "citation": {"text": f"Author (2026). {key}. https://doi.org/10.0/{key} accessed via GBIF.org on 2026-11-04."}, "description": "long text"}


class FakeGbif:
    """The occurrence search API, as far as the feed uses it: filters ANDed across params and ORed within one, facets, the window."""

    FIELDS = {"gadmGid": lambda r: (r.get("gadm") or {}).get("level1", {}).get("gid"), "gadmLevel1Gid": lambda r: (r.get("gadm") or {}).get("level1", {}).get("gid"),
              "gadmLevel2Gid": lambda r: (r.get("gadm") or {}).get("level2", {}).get("gid"), "country": lambda r: r.get("countryCode")}

    def __init__(self, records, window):
        self.records, self.window, self.datasets, self.fail, self.search_calls, self.shift_count = list(records), window, {}, None, [], 0
        self.farthest = 0

    def _value(self, param, r):
        return self.FIELDS[param](r) if param in self.FIELDS else r.get(param)

    def _matches(self, r, params):
        for param, values in params.items():
            if param in ("limit", "offset", "facet", "facetLimit"):
                continue
            if param == "hasCoordinate":
                if ("decimalLatitude" in r) != (values[0] == "true"):
                    return False
            elif param in ("decimalLatitude", "decimalLongitude"):
                low, high = values[0].split(",")
                if param not in r or not float(low) <= r[param] <= float(high):
                    return False
            elif param == "lastInterpreted":
                if r["lastInterpreted"][:10] < values[0].split(",")[0]:
                    return False
            elif str(self._value(param, r)) not in values:
                return False
        return True

    def search(self, url):
        if self.fail and self.fail(url):
            raise core.FeedError(f"{self.fail.reason} {url}")
        params = urllib.parse.parse_qs(url.split("?", 1)[1])
        self.search_calls.append(url)
        found = sorted((r for r in self.records if self._matches(r, params)), key=lambda r: r["key"])
        offset, limit = int(params.get("offset", ["0"])[0]), int(params.get("limit", ["20"])[0])
        self.farthest = max(self.farthest, offset + limit)
        answer = {"offset": offset, "limit": limit, "count": len(found) + self.shift_count if found else 0, "results": found[offset:offset + limit],
                  "endOfRecords": offset + limit >= len(found), "facets": []}
        if "facet" in params:
            name = params["facet"][0]
            counts = Counter(str(self._value(name, r)) for r in found if self._value(name, r) is not None)
            answer["facets"] = [{"field": name.upper(), "counts": [{"name": k, "count": v} for k, v in counts.most_common()]}]
        return json.dumps(answer).encode()

    def dataset(self, url):
        key = url.rsplit("/", 1)[1]
        return json.dumps(self.datasets[key]).encode() if key in self.datasets else None


def failing(reason, when):
    def check(url):
        return when(url)
    check.reason = reason
    return check


def fixture():
    big = [record(i, day=1 + i % 3, county=f"USA.17.{1 + i % 2}_1") for i in range(100, 106)] + [record(i, year=2021) for i in (106, 107)]
    small = [record(200, dataset="ds-small", license=CC0, year=1890, month=None, day=None, typeStatus=["HOLOTYPE", "PARATYPE"], locality="Fort Riley",
                    media=[{"type": "StillImage"}, {"type": "StillImage"}], verbatimDepth="3 m", recordedBy="A. Collector"),
             record(201, dataset="ds-small", license=CC0, year=None, month=None, day=None, county="USA.17.2_1")]
    fossils = [record(300 + i, dataset="ds-fossil", year=None, month=None, day=None, basis="FOSSIL_SPECIMEN", county=f"USA.17.{1 + i % 2}_1") for i in range(5)]
    named = [record(400, dataset="ds-small", lat=None, lon=None, level1=None, license=CC0),                     # no coordinates
             record(401, dataset="ds-small", lat=None, lon=None, level1=None, state="Ks", license=CC0),
             record(402, dataset="ds-small", lat=45.0, lon=-98.0, level1="USA.42_1", county=None, license=CC0),  # north of the box
             record(403, dataset="ds-small", lat=38.5, lon=-94.6, level1=MISSOURI, county=None, license=CC0),    # the Missouri side
             record(404, dataset="ds-small", lat=38.5, lon=-98.0, level1=None, license=CC0)]                     # no GADM state: unreachable
    others = [record(500, dataset="ds-other", state="Nebraska", lat=41.0, level1="USA.28_1", county=None)]
    return big + small + fossils + named + others


class GbifCase(FeedCase):
    def setUp(self):
        super().setUp()
        for name, value in (("GBIF_WINDOW", 4), ("GBIF_PAGE", 2)):
            patcher = patch.object(bio, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        bulk = self.root / "bulk-sql/kfm-bulk.sqlite"
        self.ctx.db_path, self.ctx.bulk_db, self.ctx.pause = bulk, bulk, 0
        core.init_bulk(self.ctx)
        self.api = FakeGbif(fixture(), 4)
        self.api.datasets = {k: dataset(k, CC0 if k == "ds-small" else CC_BY) for k in ("ds-big", "ds-small", "ds-fossil")}
        self.web.routes = {bio.GBIF_SEARCH: self.api.search, "https://api.gbif.org/v1/dataset/": self.api.dataset}

    def bq(self, sql, *args):
        db = sqlite3.connect(self.ctx.db_path)
        try:
            return db.execute(sql, args).fetchall()
        finally:
            db.close()

    def ids(self):
        return [i for (i,) in self.bq("SELECT gbif_id FROM kfm_gbif_occurrences ORDER BY gbif_id")]

    ALL = sorted([*range(100, 108), 200, 201, *range(300, 305), 400, 401, 402, 403])

    def backfill(self):
        return bio.gbif(self.ctx, max_requests=2000)


class BackfillTests(GbifCase):
    def test_it_refuses_observations_sqlite(self):
        with self.assertRaisesRegex(core.FeedError, "BULK_DATABASE_REQUIRED"):
            bio.gbif(core.Context(root=self.root, db_path=self.db_path, fetch=self.web, lock=self.ctx.lock, log=self.logs.append))
        self.assertEqual(self.q("SELECT name FROM sqlite_master WHERE name='kfm_gbif_occurrences'"), [])

    def test_every_kansas_record_loads_once_and_nothing_else(self):
        result = self.backfill()
        self.assertEqual(self.ids(), self.ALL)
        self.assertEqual((result["rows"], result["segments_pending"], result["nodes_open"]), (len(self.ALL), 0, 0))
        self.assertLessEqual(self.api.farthest, 4)   # never past the window
        self.assertEqual(result["gap_rows"], 1)      # record 404: inside the box with no GADM state
        self.assertEqual(result["backfill_done"], "2026-11-04")
        self.assertEqual(core.get_state(sqlite3.connect(self.ctx.db_path), "gbif")["last_stop"], None)

    def test_licence_dataset_and_citation_are_kept_per_record(self):
        self.backfill()
        self.assertEqual(self.bq("SELECT license, dataset_key, publishing_org_key FROM kfm_gbif_occurrences WHERE gbif_id=200"), [(CC0, "ds-small", "org-1")])
        self.assertEqual(self.bq("SELECT license, COUNT(*) FROM kfm_gbif_occurrences GROUP BY 1 ORDER BY 1"), [(CC_BY, 13), (CC0, 6)])
        self.assertEqual(self.bq("SELECT dataset_key, doi, license, citation FROM kfm_gbif_datasets WHERE dataset_key='ds-small'"),
                         [("ds-small", "10.0/ds-small", CC0, "Author (2026). ds-small. https://doi.org/10.0/ds-small")])
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_gbif_datasets"), [(3,)])
        receipt = json.loads(self.bq("SELECT receipt_json FROM kfm_sql_sources WHERE source_id=? AND receipt_json LIKE '%segment/gadm/datasetKey-ds-small%'", bio.GBIF_SOURCE)[0][0])
        self.assertEqual(receipt["licenses"], {CC0: 2})
        self.assertEqual(receipt["datasets"], {"ds-small": 2})
        self.assertEqual((receipt["terms"], receipt["records"], receipt["reported_count"]), (bio.GBIF_TERMS, 2, 2))
        self.assertIn("kfm_gbif_datasets", receipt["citation"])

    def test_a_record_becomes_columns_extra_and_keeps_nothing_volatile(self):
        self.backfill()
        row = self.bq("""SELECT gbif_id, typeof(gbif_id), occurrence_id, year, month, decimal_latitude, type_status, locality, media_count, issues_json, extra_json, recorded_by,
                         gadm_level1_gid, gadm_level2_gid FROM kfm_gbif_occurrences WHERE gbif_id=200""")[0]
        self.assertEqual(row, (200, "integer", "occ-200", 1890, None, 38.5, '["HOLOTYPE","PARATYPE"]', "Fort Riley", 2, '["A_ISSUE","B_ISSUE"]', '{"verbatimDepth":"3 m"}',
                               "A. Collector", KANSAS, "USA.17.1_1"))
        kept = bio.kept_record(record(1, year=2020))
        for gone in ("lastInterpreted", "lastCrawled", "crawlId", "key", "classifications", "extensions"):
            self.assertNotIn(gone, kept)
        self.assertNotIn("http://unknown.org/status", kept.get("extra", {}))

    def test_the_tree_splits_on_complete_dimensions_so_records_without_a_year_are_reached(self):
        self.backfill()
        nodes = dict(self.bq("SELECT key, split_dimension FROM kfm_gbif_segments WHERE kind='split'"))
        self.assertEqual(nodes["gadm"], "datasetKey")
        self.assertEqual(nodes["gadm/datasetKey-ds-big"], "year")
        self.assertEqual(nodes["gadm/datasetKey-ds-big/year-2020"], "day")     # one month does not divide it
        self.assertEqual(nodes["gadm/datasetKey-ds-fossil"], "gadmLevel2Gid")  # no year, month or day to split on
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_gbif_occurrences WHERE dataset_key='ds-fossil'"), [(5,)])
        self.assertEqual(self.bq("SELECT SUM(gap_rows) FROM kfm_gbif_segments WHERE key LIKE 'gadm%'"), [(0,)])

    def test_kept_copies_are_jsonl_named_by_tree_path_and_one_key_per_leaf(self):
        self.backfill()
        path, key = self.bq("SELECT source_path, json_extract(receipt_json,'$.key') FROM kfm_sql_sources WHERE receipt_json LIKE '%segment/gadm/datasetKey-ds-small%'")[0]
        self.assertEqual(key, "segment/gadm/datasetKey-ds-small")
        self.assertRegex(path, r"data/raw/sql-feeds/gbif/segments/gadm/datasetKey-ds-small-[0-9a-f]{12}\.jsonl\.gz$")
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            lines = [json.loads(line) for line in handle]
        self.assertEqual(lines[0], {"segment": key})
        self.assertEqual([line["gbifID"] for line in lines[1:]], [200, 201])

    def test_a_node_nothing_can_divide_keeps_its_first_window_and_says_so(self):
        self.api.records = [record(i, dataset="ds-big", county="USA.17.1_1") for i in range(1, 8)]
        self.backfill()
        self.assertEqual(self.bq("SELECT key, note, gap_rows, planned_rows, loaded_rows FROM kfm_gbif_segments WHERE note='truncated'"),
                         [("gadm", "truncated", 3, 7, 4)])
        self.assertEqual(len(self.ids()), 4)
        receipt = json.loads(self.bq("SELECT receipt_json FROM kfm_sql_sources WHERE source_id=?", bio.GBIF_SOURCE)[0][0])
        self.assertTrue(receipt["truncated"])

    def test_a_dimension_with_a_gap_is_used_only_when_none_is_complete(self):
        self.api.records = [record(i, dataset="ds-big", county="USA.17.1_1", year=2000 + i % 2, day=1) for i in range(1, 7)] + [record(9, dataset="ds-big", year=None, month=None, day=None)]
        self.backfill()
        self.assertEqual(self.bq("SELECT key, split_dimension, gap_rows FROM kfm_gbif_segments WHERE gap_rows > 0"), [("gadm", "year", 1)])
        self.assertEqual(self.ids(), [1, 2, 3, 4, 5, 6])


class ResumeTests(GbifCase):
    def test_the_budget_stops_between_leaves_and_the_next_run_carries_on(self):
        first = bio.gbif(self.ctx, max_requests=12)
        self.assertEqual(first["requests"], 12)
        self.assertGreater(first["segments_pending"] + first["nodes_open"], 0)
        self.assertIsNone(first["backfill_done"])
        for _ in range(20):
            again = bio.gbif(self.ctx, max_requests=12)
            if again["backfill_done"]:
                break
        self.assertEqual(self.ids(), self.ALL)
        self.assertLessEqual(max(Counter(self.ids()).values()), 1)

    def test_a_429_stops_with_a_fixed_reason_and_keeps_every_finished_segment(self):
        calls = {"n": 0}
        def after_ten(url):
            calls["n"] += 1
            return calls["n"] > 10
        self.api.fail = failing("HTTP_429", after_ten)
        with self.assertRaisesRegex(core.FeedError, r"^GBIF_RATE_LIMITED$"):
            self.backfill()
        before = self.ids()
        self.assertEqual(self.bq("SELECT state FROM kfm_sql_sources WHERE state!='complete'"), [])
        state = json.loads(self.bq("SELECT state_json FROM kfm_feed_state WHERE feed='gbif'")[0][0])
        self.assertEqual(state["last_stop"], "GBIF_RATE_LIMITED")
        self.assertEqual(calls["n"], 11)   # stopped at once
        self.api.fail = None
        self.backfill()
        self.assertEqual(self.ids(), self.ALL)
        self.assertTrue(set(before) <= set(self.ids()))

    def test_a_503_or_connection_failure_or_html_answer_is_gbif_unavailable(self):
        for reason in ("HTTP_503", "FETCH_FAILED"):
            self.api.fail = failing(reason, lambda url: True)
            with self.assertRaisesRegex(core.FeedError, r"^GBIF_UNAVAILABLE$"):
                self.backfill()
        self.api.fail = None
        self.web.routes[bio.GBIF_SEARCH] = b"<html>Backend fetch failed</html>"
        with self.assertRaisesRegex(core.FeedError, r"^GBIF_UNAVAILABLE$"):
            self.backfill()

    def test_an_outage_in_the_middle_of_a_leaf_leaves_none_of_that_leaf(self):
        self.api.records.append(record(108, year=2021))   # three records, so two pages
        self.api.fail = failing("HTTP_503", lambda url: "year=2021" in url and "offset=2" in url)
        with self.assertRaisesRegex(core.FeedError, "GBIF_UNAVAILABLE"):
            self.backfill()
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_gbif_occurrences WHERE year=2021"), [(0,)])
        self.api.fail = None
        self.backfill()
        self.assertEqual(self.ids(), sorted([*self.ALL, 108]))

    def test_a_leaf_that_moved_while_paged_waits_and_is_loaded_flagged_at_the_third_try(self):
        self.api.records = [record(1, dataset="ds-big"), record(2, dataset="ds-big")]
        self.api.shift_count = 1   # the count says 3, the pages hold 2
        first = self.backfill()
        self.assertEqual((first["shifted"], self.ids()), (1, []))
        self.assertEqual(self.backfill()["shifted"], 1)
        third = self.backfill()
        self.assertEqual((third["shifted"], third["rows"], self.ids()), (0, 2, [1, 2]))
        self.assertEqual(self.bq("SELECT note FROM kfm_gbif_segments WHERE note IS NOT NULL"), [("shifted",)])


class RefreshTests(GbifCase):
    def test_nothing_is_due_until_the_refresh_days_pass(self):
        self.backfill()
        self.ctx.now = at(2026, 11, 5)
        calls = len(self.web.calls)
        result = bio.gbif(self.ctx)
        self.assertEqual((result["requests"], len(self.web.calls)), (0, calls))

    def test_after_28_days_unchanged_leaves_are_checked_with_one_small_request(self):
        self.backfill()
        rows = self.bq("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='complete'")
        self.ctx.now = at(2026, 12, 2)
        self.api.search_calls.clear()
        result = bio.gbif(self.ctx, max_requests=2000)
        self.assertEqual(result["rows"], 0)
        self.assertGreater(result["segments_checked"], 0)
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='complete'"), rows)
        self.assertFalse([u for u in self.api.search_calls if "limit=2" in u and "offset" in u])   # no pages fetched
        self.assertTrue([u for u in self.api.search_calls if "lastInterpreted=2026-11-04,*" in u])

    def test_a_reinterpreted_leaf_with_the_same_records_is_not_loaded_again(self):
        self.backfill()
        for r in self.api.records:
            r["lastInterpreted"] = "2026-11-20T00:00:00.000+00:00"
            r["crawlId"] = 8
        self.ctx.now = at(2026, 12, 2)
        result = bio.gbif(self.ctx, max_requests=2000)
        self.assertEqual(result["rows"], 0)
        self.assertGreater(result["segments_unchanged"], 0)
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='superseded'"), [(0,)])

    def test_a_revised_record_replaces_its_leaf(self):
        self.backfill()
        for r in self.api.records:
            if r["key"] == 200:
                r.update(scientificName="Species renamed", lastInterpreted="2026-11-20T00:00:00.000+00:00")
        self.ctx.now = at(2026, 12, 2)
        result = bio.gbif(self.ctx, max_requests=2000)
        self.assertEqual(result["segments_loaded"], 1)
        self.assertEqual(self.bq("SELECT scientific_name FROM kfm_gbif_occurrences WHERE gbif_id=200"), [("Species renamed",)])
        self.assertEqual(self.ids(), self.ALL)
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='superseded'"), [(1,)])

    def test_a_new_dataset_joins_and_a_vanished_one_is_retired_with_its_rows(self):
        self.backfill()
        self.api.records = [r for r in self.api.records if r["datasetKey"] != "ds-fossil"] + [record(600, dataset="ds-new", year=2026)]
        self.api.datasets["ds-new"] = dataset("ds-new")
        self.ctx.now = at(2026, 12, 2)
        result = bio.gbif(self.ctx, max_requests=2000)
        self.assertGreater(result["retired"], 0)
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_gbif_occurrences WHERE dataset_key='ds-fossil'"), [(0,)])
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_gbif_occurrences WHERE gbif_id=600"), [(1,)])
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_gbif_segments WHERE key LIKE '%ds-fossil%'"), [(0,)])
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_gbif_datasets WHERE dataset_key='ds-new'"), [(1,)])

    def test_a_leaf_grown_past_the_window_is_split_and_its_records_return(self):
        self.backfill()
        self.api.records += [record(700 + i, dataset="ds-small", year=2025, county="USA.17.3_1", license=CC0) for i in range(4)]
        self.ctx.now = at(2026, 12, 2)
        result = bio.gbif(self.ctx, max_requests=2000)
        self.assertEqual(self.bq("SELECT kind, split_dimension FROM kfm_gbif_segments WHERE key='gadm/datasetKey-ds-small'")[0][0], "split")
        self.assertEqual(self.ids(), sorted([*self.ALL, 700, 701, 702, 703]))
        self.assertEqual(result["segments_pending"], 0)

    def test_a_truncated_leaf_stays_loaded_through_a_refresh_of_its_parent(self):
        self.api.records = [record(i, dataset="ds-big") for i in range(1, 8)] + [record(20, dataset="ds-small")]
        self.backfill()
        self.assertEqual(self.bq("SELECT key, gap_rows FROM kfm_gbif_segments WHERE note='truncated'"), [("gadm/datasetKey-ds-big", 3)])
        self.ctx.now = at(2026, 12, 2)
        result = bio.gbif(self.ctx, max_requests=2000)
        self.assertEqual((result["retired"], result["reopened"], len(self.ids())), (0, 0, 5))
        self.assertEqual(self.bq("SELECT kind, note FROM kfm_gbif_segments WHERE key='gadm/datasetKey-ds-big'"), [("leaf", "truncated")])

    def test_old_years_wait_a_year_and_dataset_records_half_a_year(self):
        self.backfill()
        self.ctx.now = at(2026, 12, 2)
        bio.gbif(self.ctx, max_requests=2000)
        old = "gadm/datasetKey-ds-big/year-2020"
        self.assertEqual(self.bq("SELECT checked_on FROM kfm_gbif_segments WHERE key=?", old), [("2026-11-04",)])
        self.assertEqual(self.bq("SELECT fetched_on FROM kfm_gbif_dataset_queue WHERE dataset_key='ds-big'"), [("2026-11-04",)])
        self.ctx.now = at(2027, 6, 1)
        bio.gbif(self.ctx, max_requests=2000)
        self.assertEqual(self.bq("SELECT fetched_on FROM kfm_gbif_dataset_queue WHERE dataset_key='ds-big'"), [("2027-06-01",)])
        self.assertEqual(self.bq("SELECT checked_on FROM kfm_gbif_segments WHERE key=?", old), [("2026-11-04",)])
        self.ctx.now = at(2027, 11, 5)
        bio.gbif(self.ctx, max_requests=2000)
        self.assertEqual(self.bq("SELECT checked_on FROM kfm_gbif_segments WHERE key=?", old), [("2027-11-05",)])


class DatasetRecordTests(GbifCase):
    def test_a_dataset_gone_from_the_registry_is_noted_and_its_rows_stay(self):
        del self.api.datasets["ds-small"]
        self.backfill()
        self.assertEqual(self.bq("SELECT note FROM kfm_gbif_dataset_queue WHERE dataset_key='ds-small'"), [("missing",)])
        self.assertEqual(self.bq("SELECT COUNT(*) FROM kfm_gbif_occurrences WHERE dataset_key='ds-small'"), [(6,)])

    def test_dataset_requests_take_at_most_a_fifth_of_the_budget(self):
        self.api.records = [record(i, dataset=f"ds-{i:02d}") for i in range(30)]
        self.api.datasets = {f"ds-{i:02d}": dataset(f"ds-{i:02d}") for i in range(30)}
        result = bio.gbif(self.ctx, max_requests=20)
        self.assertEqual(result["datasets"], 4)
        self.assertEqual(result["datasets_pending"], 26)


if __name__ == "__main__":
    unittest.main()
