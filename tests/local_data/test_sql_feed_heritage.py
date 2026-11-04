"""SQL feed for the Library of Congress's Kansas holdings, without network access."""
from datetime import datetime, timezone
import gzip
import json
import unittest
from unittest.mock import patch
import urllib.parse

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_heritage as heritage, sql_feeds as core

PHOTOS, MAPS = "https://www.loc.gov/photos/", "https://www.loc.gov/maps/"
HABS = heritage.LOC_BUCKETS["habs"][0]
CHRONAM = heritage.CHRONAM


def at(*args):
    return lambda: datetime(*args, 15, 0, tzinfo=timezone.utc)


def item(number, kind="photo", **more):
    return {"id": f"http://www.loc.gov/item/{kind}{number}/", "title": f"{kind} {number}", "date": "1943-01-01", "dates": ["1943"], "index": number,
            "location": ["kansas", "ellis"], "subject": ["wheat", "farms"], "contributor": ["delano, jack"], "description": ["A view"],
            "image_url": ["https://tile.loc.gov/a.jpg"], "online_format": ["image"], "url": f"https://www.loc.gov/item/{kind}{number}/",
            "partof": ["farm security administration"], "original_format": ["photo, print, drawing"], "shelf_id": f"LC-{number}", "timestamp": "2024-01-01T00:00:00Z",
            "item": {"rights_information": "No known restrictions.", "medium": ["1 negative"]}, **more}


def issue(lccn, day, pages=4):
    return {"id": f"http://www.loc.gov/item/{lccn}/1894-01-{day:02d}/ed-1/", "title": f"Paper, January {day}", "date": f"1894-01-{day:02d}", "dates": [f"1894-01-{day:02d}"],
            "index": day, "number_lccn": [lccn], "shelf_id": f"{lccn}, 1894-01-{day:02d}, Edition 1", "timestamp": "2023-08-08T13:08:26Z",
            "segments": [{"count": pages, "link": f"{CHRONAM}?c=1000&dl=issue&fa=segmentof:{lccn}/&fo=json&st=gallery", "url": f"https://www.loc.gov/resource/{lccn}/"}],
            "item": {"medium": f"{pages} pages"}}


def title(lccn, count, first="1894-01-01", last="1894-01-31"):
    return {"id": f"http://www.loc.gov/item/{lccn}/", "title": f"Paper {lccn} (Topeka, Kan.) 1890-1900", "number_lccn": [lccn], "number_issue_count": [str(count)],
            "number_first_issue": [f"http://www.loc.gov/item/{lccn}/{first}/ed-1/"], "number_last_issue": [f"http://www.loc.gov/item/{lccn}/{last}/ed-1/"],
            "location_str": "Topeka, Kansas", "date": "1890", "publication_frequency": ["daily"], "location_state": ["kansas"], "url": f"https://www.loc.gov/item/{lccn}/",
            "number_source_modified": ["2026-04-13t21:30:13"]}


class FakeLoc:
    """loc.gov search pages: a query's results by c and sp, a larger c falling back to 25, and what a test wants to go wrong."""

    def __init__(self):
        self.photos, self.maps, self.habs = [item(1), item(2), item(3)], [item(1, "map")], [item(1, "habs", segments=[{"count": 7, "link": f"{HABS}?c=1000&fo=json", "url": "x"}])]
        self.titles = [title("sn1", 3), title("sn2", 1)]
        self.issues = {"sn1": [issue("sn1", d) for d in (1, 2, 3)], "sn2": [issue("sn2", 1, pages=8)]}
        self.fail, self.calls, self.limit = None, [], 1000

    def __call__(self, url):
        self.calls.append(url)
        if self.fail:
            outcome = self.fail(url)
            if isinstance(outcome, bytes):
                return outcome
            if outcome:
                raise core.FeedError(f"{outcome} {url}")
        endpoint, query = url.split("?", 1)
        params = dict(urllib.parse.parse_qsl(query))
        if endpoint == PHOTOS:
            found = self.photos
        elif endpoint == MAPS:
            found = self.maps
        elif endpoint == HABS:
            found = self.habs
        elif params.get("dl") == "title":
            found = self.titles
        else:
            found = self.issues[params["fa"].rsplit(":", 1)[1]]
        size, page = int(params["c"]), int(params["sp"])
        if size > self.limit:
            size = 25
        start = (page - 1) * size
        following = f"{endpoint}?sp={page + 1}" if start + size < len(found) else None
        return json.dumps({"pagination": {"of": len(found), "perpage": size, "current": page, "next": following}, "results": found[start:start + size]}).encode()


class LocCase(FeedCase):
    def setUp(self):
        super().setUp()
        self.ctx.pause = 0
        self.loc = FakeLoc()
        self.web.routes = {"https://www.loc.gov/": self.loc}


class BackfillTests(LocCase):
    def test_buckets_titles_and_issues_load_with_their_own_rights(self):
        result = heritage.loc_kansas(self.ctx)
        self.assertEqual((result["rows"], result["pending_segments"], result["pages"]), (11, 0, 6))
        self.assertEqual(self.q("SELECT bucket, COUNT(*) FROM kfm_loc_items GROUP BY 1 ORDER BY 1"), [("habs", 1), ("map", 1), ("newspaper", 4), ("photo", 3)])
        self.assertEqual(self.q("SELECT rights, medium, segments, shelf_id, date FROM kfm_loc_items WHERE id LIKE '%photo1/'"),
                         [("No known restrictions.", "1 negative", None, "LC-1", "1943-01-01")])
        self.assertEqual(self.q("SELECT rights, medium, segments, lccn FROM kfm_loc_items WHERE bucket='newspaper' AND lccn='sn2'"), [(None, "8 pages", 8, "sn2")])
        self.assertEqual(self.q("SELECT lccn, issue_count, first_issue, last_issue, place FROM kfm_loc_newspaper_titles ORDER BY lccn"),
                         [("sn1", 3, "1894-01-01", "1894-01-31", "Topeka, Kansas"), ("sn2", 1, "1894-01-01", "1894-01-31", "Topeka, Kansas")])
        self.assertEqual({k for (k,) in self.q("SELECT json_extract(receipt_json,'$.key') FROM kfm_sql_sources")},
                         {"newspaper-titles", "photo", "map", "habs", "newspaper/sn1", "newspaper/sn2"})

    def test_urls_ask_for_the_largest_page_results_and_paging_only(self):
        heritage.loc_kansas(self.ctx)
        self.assertIn("https://www.loc.gov/photos/?fa=location_state:kansas&fo=json&c=1000&sp=1&at=results,pagination", self.loc.calls)
        self.assertIn(f"{HABS}?fa=location:kansas&fo=json&c=1000&sp=1&at=results,pagination", self.loc.calls)
        self.assertIn(f"{CHRONAM}?fa=location_state:kansas&dl=title&fo=json&c=1000&sp=1&at=results,pagination", self.loc.calls)
        self.assertIn(f"{CHRONAM}?fa=location_state:kansas|number_lccn:sn1&dl=issue&fo=json&c=1000&sp=1&at=results,pagination", self.loc.calls)

    def test_the_kept_copy_is_canonical_and_cited(self):
        heritage.loc_kansas(self.ctx)
        path, receipt = self.q("SELECT source_path, receipt_json FROM kfm_sql_sources WHERE json_extract(receipt_json,'$.key')='habs'")[0]
        self.assertRegex(path, r"sql-feeds/loc-kansas/habs-[0-9a-f]{12}\.jsonl\.gz$")
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            kept = json.loads(handle.readline())
        self.assertNotIn("index", kept)
        self.assertEqual(kept["subject"], ["farms", "wheat"])
        self.assertEqual(kept["segments"][0]["link"], f"{HABS}?fo=json")
        receipt = json.loads(receipt)
        self.assertEqual((receipt["records"], receipt["terms"]), (1, heritage.LOC_TERMS))
        self.assertIn("Library of Congress", receipt["citation"])
        self.assertIn("rights", receipt["license"])

    def test_a_rerun_makes_no_requests(self):
        heritage.loc_kansas(self.ctx)
        self.ctx.now = at(2026, 11, 5)
        calls = len(self.loc.calls)
        result = heritage.loc_kansas(self.ctx)
        self.assertEqual((result["pages"], len(self.loc.calls)), (0, calls))

    def test_the_budget_stops_starting_segments_and_the_next_run_carries_on(self):
        first = heritage.loc_kansas(self.ctx, max_pages=2)
        self.assertEqual(first["pages"], 2)
        self.assertGreater(first["pending_segments"], 0)
        second = heritage.loc_kansas(self.ctx, max_pages=50)
        self.assertEqual(second["pending_segments"], 0)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_loc_items"), [(9,)])

    def test_a_segment_larger_than_the_budget_still_loads_when_it_comes_first(self):
        self.loc.issues["sn1"] = [issue("sn1", d) for d in (1, 2)]
        self.loc.titles = [title("sn1", 5000)]
        with patch.object(heritage, "LOC_BUCKETS", {}), patch.object(heritage, "LOC_PAGE_SIZES", (1,)):
            self.loc.limit = 1
            self.ctx.now = at(2026, 11, 4)
            heritage.loc_kansas(self.ctx, max_pages=1)     # the title list alone
            result = heritage.loc_kansas(self.ctx, max_pages=1)
        self.assertEqual(result["pages"], 2)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_loc_items"), [(2,)])


class StopTests(LocCase):
    def test_a_429_a_403_or_an_html_page_stops_at_once_and_keeps_finished_segments(self):
        outcomes = {"HTTP_429": "HTTP_429", "HTTP_403": "HTTP_403", "html": b"<html>Just a moment...</html>"}
        for name, outcome in outcomes.items():
            with self.subTest(name):
                self.loc.fail = lambda url, outcome=outcome: outcome if url.startswith(MAPS) else None
                self.loc.calls.clear()
                with self.assertRaisesRegex(core.FeedError, "^LOC_RATE_LIMITED"):
                    heritage.loc_kansas(self.ctx)
                self.assertEqual(len([u for u in self.loc.calls if u.startswith(MAPS)]), 1)
                self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_loc_items WHERE bucket='photo'"), [(3,)])
        self.loc.fail = None
        heritage.loc_kansas(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_loc_items"), [(9,)])

    def test_a_page_size_the_api_did_not_honour_stops_the_run(self):
        self.loc.limit = 500
        with self.assertRaisesRegex(core.FeedError, "^LOC_PAGE_SIZE_CHANGED"):
            heritage.loc_kansas(self.ctx)

    def test_a_result_seen_twice_or_a_short_query_is_shifted(self):
        self.loc.photos = [item(1), item(1)]
        with self.assertRaisesRegex(core.FeedError, "^LOC_RESULTS_SHIFTED"):
            heritage.loc_kansas(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_loc_items"), [(0,)])

    def test_a_failed_page_is_tried_again_then_smaller_continuing_at_the_same_offset(self):
        self.loc.photos = [item(i) for i in range(1, 1201)]
        tries = {"n": 0}

        def fail(url):
            if url.startswith(PHOTOS) and "c=1000" in url and "sp=2" in url:
                return "HTTP_503"
            if url.startswith(PHOTOS) and "c=500" in url and "sp=3" in url and tries["n"] == 0:
                tries["n"] = 1
                return "FETCH_FAILED"
            return None
        self.loc.fail = fail
        heritage.loc_kansas(self.ctx, max_pages=100)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_loc_items WHERE bucket='photo'"), [(1200,)])
        asked = [u for u in self.loc.calls if u.startswith(PHOTOS)]
        self.assertEqual([("c=1000" in u, u.split("sp=")[1].split("&")[0]) for u in asked], [(True, "1"), (True, "2"), (True, "2"), (False, "3"), (False, "3")])

    def test_a_segment_that_fails_at_every_size_waits_while_the_others_load(self):
        self.loc.fail = lambda url: "HTTP_503" if url.startswith(PHOTOS) else None
        with self.assertRaisesRegex(core.FeedError, "^LOC_UNAVAILABLE photo$"):
            heritage.loc_kansas(self.ctx)
        self.assertEqual(self.q("SELECT bucket, COUNT(*) FROM kfm_loc_items GROUP BY 1 ORDER BY 1"), [("habs", 1), ("map", 1), ("newspaper", 4)])
        self.loc.fail = None
        heritage.loc_kansas(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_loc_items WHERE bucket='photo'"), [(3,)])

    def test_a_second_failing_segment_ends_the_run(self):
        self.loc.fail = lambda url: "HTTP_503" if "titles" not in url and "dl=title" not in url else None
        with self.assertRaisesRegex(core.FeedError, "^LOC_UNAVAILABLE photo,map$"):
            heritage.loc_kansas(self.ctx)
        self.assertEqual([u for u in self.loc.calls if u.startswith(HABS) or "dl=issue" in u], [])


class RevisionTests(LocCase):
    def test_after_28_days_an_identical_answer_in_another_order_is_unchanged(self):
        heritage.loc_kansas(self.ctx)
        self.loc.photos = [{**item(3, index=99), "subject": ["farms", "wheat"]}, item(1, index=7), item(2)]
        self.ctx.now = at(2026, 12, 2)
        result = heritage.loc_kansas(self.ctx)
        self.assertEqual(result["loaded"], [])
        self.assertEqual(sorted(result["unchanged"]), ["habs", "map", "photo"])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='superseded'"), [(0,)])

    def test_a_changed_bucket_replaces_its_rows(self):
        heritage.loc_kansas(self.ctx)
        self.loc.photos = [item(1), item(4)]
        self.ctx.now = at(2026, 12, 2)
        heritage.loc_kansas(self.ctx)
        self.assertEqual({i for (i,) in self.q("SELECT id FROM kfm_loc_items WHERE bucket='photo'")},
                         {"http://www.loc.gov/item/photo1/", "http://www.loc.gov/item/photo4/"})
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='superseded'"), [(1,)])

    def test_a_title_is_pulled_again_when_its_listing_changes_and_every_182_days(self):
        heritage.loc_kansas(self.ctx)
        self.loc.titles = [title("sn1", 4), title("sn2", 1)]
        self.loc.issues["sn1"].append(issue("sn1", 4))
        self.loc.calls.clear()
        self.ctx.now = at(2026, 11, 12)
        heritage.loc_kansas(self.ctx)
        self.assertEqual([u for u in self.loc.calls if "dl=issue" in u and "sn2" in u], [])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_loc_items WHERE lccn='sn1'"), [(4,)])
        self.ctx.now = at(2027, 5, 11)
        self.loc.calls.clear()
        heritage.loc_kansas(self.ctx)
        self.assertTrue([u for u in self.loc.calls if "dl=issue" in u and "sn2" in u])

    def test_a_title_modified_date_alone_does_not_pull_it_again(self):
        heritage.loc_kansas(self.ctx)
        self.loc.titles = [{**title("sn1", 3), "number_source_modified": ["2026-11-10t00:00:00"]}, title("sn2", 1)]
        self.loc.calls.clear()
        self.ctx.now = at(2026, 11, 12)
        heritage.loc_kansas(self.ctx)
        self.assertEqual([u for u in self.loc.calls if "dl=issue" in u], [])

    def test_a_title_gone_from_the_list_keeps_its_rows_and_stops_after_the_others(self):
        heritage.loc_kansas(self.ctx)
        self.loc.titles = [title("sn2", 2)]
        self.loc.issues["sn2"].append(issue("sn2", 2))
        self.ctx.now = at(2026, 11, 12)
        with self.assertRaisesRegex(core.FeedError, "^LOC_TITLE_UNLISTED sn1$"):
            heritage.loc_kansas(self.ctx)
        self.assertEqual(self.q("SELECT lccn, COUNT(*) FROM kfm_loc_items WHERE bucket='newspaper' GROUP BY 1 ORDER BY 1"), [("sn1", 3), ("sn2", 2)])


if __name__ == "__main__":
    unittest.main()
