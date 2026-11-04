"""SQL feeds for Kansas texts and registers: Internet Archive full text, the LOC newspaper directory and FCC towers."""
from datetime import datetime, timedelta, timezone
import gzip
import hashlib
import io
import json
import sqlite3
import unittest
from unittest.mock import patch
import urllib.parse
import zipfile

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_texts as texts, sql_feeds as core

START = datetime(2026, 11, 4, 15, 0, tzinfo=timezone.utc)

# --- Towers ------------------------------------------------------------------------------------------

# The tables as they stand in observations.sqlite (sqlite_master.sql, copied from the recovered schema).
ASR_SCHEMA = {
    "kfm_asr_entities": 'CREATE TABLE kfm_asr_entities (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "record_type" TEXT, "content_indicator" TEXT, "file_number" TEXT, "registration_number" TEXT, "unique_system_identifier" TEXT, "entity_type" TEXT, "entity_type_code" TEXT, "entity_type_other" TEXT, "licensee_id" TEXT, "entity_name" TEXT, "first_name" TEXT, "mi" TEXT, "last_name" TEXT, "suffix" TEXT, "phone" TEXT, "fax_number" TEXT, "internet_address" TEXT, "street_address" TEXT, "street_address2" TEXT, "po_box" TEXT, "city" TEXT, "state" TEXT, "zip_code" TEXT, "attention" TEXT, "frn" TEXT, PRIMARY KEY(file_id, row_number))',
    "kfm_asr_entities_entity_name": 'CREATE INDEX kfm_asr_entities_entity_name ON kfm_asr_entities("entity_name")',
    "kfm_asr_entities_registration_number": 'CREATE INDEX kfm_asr_entities_registration_number ON kfm_asr_entities("registration_number")',
    "kfm_asr_history": 'CREATE TABLE kfm_asr_history (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "record_type" TEXT, "content_indicator" TEXT, "file_number" TEXT, "registration_number" TEXT, "unique_system_identifier" TEXT, "date" TEXT, "description" TEXT, PRIMARY KEY(file_id, row_number))',
    "kfm_asr_history_registration_number": 'CREATE INDEX kfm_asr_history_registration_number ON kfm_asr_history("registration_number")',
    "kfm_asr_locations": 'CREATE TABLE kfm_asr_locations (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "record_type" TEXT, "content_indicator" TEXT, "file_number" TEXT, "registration_number" TEXT, "unique_system_identifier" TEXT, "coordinate_type" TEXT, "latitude_degrees" TEXT, "latitude_minutes" TEXT, "latitude_seconds" TEXT, "latitude_direction" TEXT, "latitude_total_seconds" TEXT, "longitude_degrees" TEXT, "longitude_minutes" TEXT, "longitude_seconds" TEXT, "longitude_direction" TEXT, "longitude_total_seconds" TEXT, "array_tower_position" TEXT, "array_total_tower" TEXT, "latitude" REAL, "longitude" REAL, "geometry_geojson" TEXT, PRIMARY KEY(file_id, row_number))',
    "kfm_asr_locations_registration_number": 'CREATE INDEX kfm_asr_locations_registration_number ON kfm_asr_locations("registration_number")',
    "kfm_asr_registrations": 'CREATE TABLE kfm_asr_registrations (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "record_type" TEXT, "content_indicator" TEXT, "file_number" TEXT, "registration_number" TEXT, "unique_system_identifier" TEXT, "application_purpose" TEXT, "previous_purpose" TEXT, "input_source_code" TEXT, "status_code" TEXT, "date_entered" TEXT, "date_received" TEXT, "date_issued" TEXT, "date_constructed" TEXT, "date_dismantled" TEXT, "date_action" TEXT, "archive_flag_code" TEXT, "version" TEXT, "signature_first_name" TEXT, "signature_middle_initial" TEXT, "signature_last_name" TEXT, "signature_suffix" TEXT, "signature_title" TEXT, "invalid_signature" TEXT, "structure_street_address" TEXT, "structure_city" TEXT, "structure_state_code" TEXT, "county_code" TEXT, "zip_code" TEXT, "height_of_structure" REAL, "ground_elevation" REAL, "overall_height_above_ground" REAL, "overall_height_amsl" REAL, "structure_type" TEXT, "date_faa_determination_issued" TEXT, "faa_study_number" TEXT, "faa_circular_number" TEXT, "specification_option" TEXT, "painting_and_lighting" TEXT, "mark_light_code" TEXT, "mark_light_other" TEXT, "faa_emi_flag" TEXT, "nepa_flag" TEXT, "date_signed" TEXT, "assignor_signature_last_name" TEXT, "assignor_signature_first_name" TEXT, "assignor_signature_middle_initial" TEXT, "assignor_signature_suffix" TEXT, "assignor_signature_title" TEXT, "assignor_signature_date" TEXT, PRIMARY KEY(file_id, row_number))',
    "kfm_asr_registrations_county_code": 'CREATE INDEX kfm_asr_registrations_county_code ON kfm_asr_registrations("county_code")',
    "kfm_asr_registrations_registration_number": 'CREATE INDEX kfm_asr_registrations_registration_number ON kfm_asr_registrations("registration_number")',
    "kfm_asr_registrations_structure_city": 'CREATE INDEX kfm_asr_registrations_structure_city ON kfm_asr_registrations("structure_city")',
    "kfm_asr_remarks": 'CREATE TABLE kfm_asr_remarks (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "record_type" TEXT, "content_indicator" TEXT, "file_number" TEXT, "registration_number" TEXT, "unique_system_identifier" TEXT, "remark_type" TEXT, "date_keyed" TEXT, "sequence_number" TEXT, "remark_text" TEXT, PRIMARY KEY(file_id, row_number))',
    "kfm_asr_remarks_registration_number": 'CREATE INDEX kfm_asr_remarks_registration_number ON kfm_asr_remarks("registration_number")',
    "kfm_asr_special_conditions": 'CREATE TABLE kfm_asr_special_conditions (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "record_type" TEXT, "content_indicator" TEXT, "file_number" TEXT, "registration_number" TEXT, "unique_system_identifier" TEXT, "date_keyed" TEXT, "sequence_number" TEXT, "special_condition_text" TEXT, PRIMARY KEY(file_id, row_number))',
    "kfm_asr_special_conditions_registration_number": 'CREATE INDEX kfm_asr_special_conditions_registration_number ON kfm_asr_special_conditions("registration_number")',
}
FIRST_ROUTE, SECOND_ROUTE = texts.ASR_ROUTES[0], texts.ASR_ROUTES[1]


def ra(usi: str, reg: str, state: str = "KS", city: str = "RUSSELL", height: str = "122.2") -> str:
    return (f"RA|REG|A1|{reg}|{usi}|NT|MD|I|C|09/11/2026|09/11/2026|09/11/2026|10/10/1996||09/11/2026|C||Aiko||Sogabe||Specialist|Y|4547 184th Blvd|{city}|{state}|20167|67665|"
            f"{height}|562.0|131.1|693.1|GTOWER|06/09/2025|2025-ACE-1192-OE|70/7460-1J|1|4, 8, 13|7|||N|09/11/2026||||||\r\n")


def co(usi: str, reg: str, kind: str = "T") -> str:
    return f"CO|REG|A1|{reg}|{usi}|{kind}|39|11|17.5|N|141077.5|95|19|40.1|W|343180.1||\r\n"


def en(usi: str, reg: str) -> str:
    return f"EN|REG|A1|{reg}|{usi}|O|E||L1|Prairie Towers LLC|||||8005551212||x@example.org|1 Main|||Topeka|KS|66601|Attn|0001\r\n"


def asr_zip(ra_lines=None, others=None, counts=None) -> bytes:
    members = {"RA": ra_lines if ra_lines is not None else [ra("11", "1000"), ra("22", "2000", state="NE")],
               "CO": [co("11", "1000"), co("11", "1000", "A"), co("22", "2000")],
               "EN": [en("11", "1000"), en("22", "2000")],
               "HS": ["HS|REG|A1|1000|11|07/30/1999|Registered\r\n", "HS|REG|A2|2000|22|07/30/1999|Elsewhere\r\n"],
               "RE": ["RE|REG|A1|1000|11|FCC|01/13/2017|14|A remark | with a pipe\nand a second line\r\n"],
               "SC": ["SC|REG|A1|1000|11|12/04/2014|1|Lighting condition.\n"], **(others or {})}
    listed = {m: sum(line.count("\n") for line in lines) for m, lines in members.items()}
    listed.update(counts or {})
    head = "File Creation Date: Sun Nov  1 06:22:48 EST 2026\r\n"
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w") as z:
        for member, lines in members.items():
            z.writestr(f"{member}.dat", "".join(lines))
        z.writestr("counts", head + "".join(f"   {n} /home/pubacc/scripts/towweekzipdata/{m}.dat\r\n" for m, n in listed.items()) + "   9 total\r\n")
    return out.getvalue()


class TowerTests(FeedCase):
    def test_tables_match_the_ones_already_in_the_database(self):
        db = sqlite3.connect(":memory:")
        db.executescript(texts.ASR_DDL)
        self.assertEqual(dict(db.execute("SELECT name, sql FROM sqlite_master WHERE name LIKE 'kfm_asr%' AND sql IS NOT NULL").fetchall()), ASR_SCHEMA)

    def test_only_the_web_routes_fcc_documents_are_tried(self):
        for route in texts.ASR_ROUTES:
            parts = urllib.parse.urlsplit(route)
            self.assertEqual(parts.scheme, "https")
            self.assertTrue(parts.hostname.endswith(".fcc.gov"), route)

    def test_loads_kansas_registrations_and_their_records_from_the_first_route(self):
        self.web.routes = {FIRST_ROUTE: asr_zip()}
        result = texts.towers(self.ctx)
        self.assertEqual((result["state"], result["route"], result["registrations"]), ("loaded", FIRST_ROUTE, 1))
        self.assertEqual(self.web.calls, [FIRST_ROUTE])
        self.assertEqual(self.q("SELECT registration_number, structure_city, county_code, height_of_structure, structure_state_code FROM kfm_asr_registrations"),
                         [("1000", "RUSSELL", "20167", 122.2, "KS")])
        self.assertEqual(self.q("SELECT registration_number, coordinate_type, latitude, longitude, geometry_geojson FROM kfm_asr_locations WHERE coordinate_type='T'"),
                         [("1000", "T", 39.1881944, -95.3278056, '{"coordinates":[-95.3278056,39.1881944],"type":"Point"}')])
        self.assertEqual(self.q("SELECT count(*) FROM kfm_asr_locations"), [(2,)])
        self.assertEqual(self.q("SELECT entity_name, po_box FROM kfm_asr_entities"), [("Prairie Towers LLC", None)])
        self.assertEqual(self.q("SELECT description FROM kfm_asr_history"), [("Registered",)])
        self.assertEqual(self.q("SELECT remark_text FROM kfm_asr_remarks"), [("A remark | with a pipe\nand a second line",)])
        self.assertEqual(self.q("SELECT special_condition_text FROM kfm_asr_special_conditions"), [("Lighting condition.",)])
        sources = self.q("SELECT source_id, json_extract(receipt_json,'$.key'), json_extract(receipt_json,'$.license'), json_extract(receipt_json,'$.original.bytes'), "
                         "json_extract(receipt_json,'$.kansas_records'), json_extract(receipt_json,'$.file_creation_date'), source_url FROM kfm_sql_sources WHERE source_id='fcc-asr-ra'")
        self.assertEqual(sources[0][:2], ("fcc-asr-ra", "RA"))
        self.assertIn("public domain", sources[0][2])
        self.assertEqual((sources[0][3], sources[0][4], sources[0][5], sources[0][6]), (len(self.web.routes[FIRST_ROUTE]), 1, "Sun Nov  1 06:22:48 EST 2026", FIRST_ROUTE))
        kept = list((self.root / "data/raw/sql-feeds/towers").glob("RA-KS-*.dat.gz"))
        self.assertEqual(len(kept), 1)
        self.assertEqual(gzip.open(kept[0], "rt", newline="").read(), ra("11", "1000"))

    def test_only_rechecked_after_seven_days_and_a_changed_cut_replaces_only_its_member(self):
        self.web.routes = {FIRST_ROUTE: asr_zip()}
        texts.towers(self.ctx)
        self.assertEqual(texts.towers(self.ctx)["state"], "not_due")
        self.assertEqual(len(self.web.calls), 1)
        self.ctx.now = lambda: START + timedelta(days=7)
        self.web.routes = {FIRST_ROUTE: asr_zip([ra("11", "1000", height="150.0"), ra("22", "2000", state="NE")])}
        result = texts.towers(self.ctx)
        self.assertEqual(result["members"], {"RA": "loaded", "CO": "unchanged", "EN": "unchanged", "HS": "unchanged", "RE": "unchanged", "SC": "unchanged"})
        self.assertEqual(self.q("SELECT height_of_structure FROM kfm_asr_registrations"), [(150.0,)])
        self.assertEqual(self.q("SELECT state, count(*) FROM kfm_sql_sources WHERE source_id='fcc-asr-ra' GROUP BY state"), [("complete", 1), ("superseded", 1)])
        self.ctx.now = lambda: START + timedelta(days=14)
        self.web.routes = {FIRST_ROUTE: asr_zip([ra("11", "1000", height="150.0"), ra("22", "2000", state="NE")])}
        self.assertEqual(texts.towers(self.ctx)["state"], "unchanged")

    def test_every_route_refused_records_fcc_blocked_and_tries_nothing_clever(self):
        calls = []

        def fetch(url, *, limit, timeout=120, missing_ok=False, attempts=3):
            calls.append((url, limit))
            raise core.FeedError(f"HTTP_403 {url}")

        self.ctx.fetch = fetch
        with self.assertRaisesRegex(core.FeedError, r"^FCC_BLOCKED .*HTTP_403"):
            texts.towers(self.ctx)
        self.assertEqual([url for url, _ in calls], list(texts.ASR_ROUTES))
        state = json.loads(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='towers'")[0][0])
        self.assertEqual((state["blocked"], state["routes"][SECOND_ROUTE]), ("FCC_BLOCKED", "HTTP_403"))
        self.assertEqual(self.q("SELECT count(*) FROM kfm_sql_sources"), [(0,)])
        self.assertEqual(texts.towers(self.ctx), {"state": "not_due", "blocked": "FCC_BLOCKED", "registrations": None})
        self.assertEqual(len(calls), len(texts.ASR_ROUTES))
        self.ctx.now = lambda: START + timedelta(days=7)
        self.ctx.fetch = self.web
        self.web.routes = {SECOND_ROUTE: asr_zip()}
        self.assertEqual(texts.towers(self.ctx)["route"], SECOND_ROUTE)
        state = json.loads(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='towers'")[0][0])
        self.assertIsNone(state["blocked"])
        self.assertNotIn("routes", state)

    def test_a_block_page_with_status_200_is_not_a_zip(self):
        self.web.routes = {route: b"<HTML><H1>Access Denied</H1></HTML>" for route in texts.ASR_ROUTES}
        with self.assertRaisesRegex(core.FeedError, "^FCC_BLOCKED .*NOT_A_ZIP"):
            texts.towers(self.ctx)
        self.assertFalse(list((self.root / "tmp-sql-feeds").glob("*")))

    def test_routes_that_only_failed_to_connect_are_unavailable_not_blocked(self):
        def fetch(url, *, limit, timeout=120, missing_ok=False, attempts=3):
            raise core.FeedError(f"FETCH_FAILED {url}: <urlopen error timed out>")

        self.ctx.fetch = fetch
        with self.assertRaisesRegex(core.FeedError, "^FCC_UNAVAILABLE"):
            texts.towers(self.ctx)

    def test_counts_file_and_field_widths_are_checked(self):
        self.web.routes = {FIRST_ROUTE: asr_zip(counts={"HS": 99})}
        with self.assertRaisesRegex(core.FeedError, "ASR_COUNTS_MISMATCH HS 2 lines, counts says 99"):
            texts.towers(self.ctx)
        self.web.routes = {FIRST_ROUTE: asr_zip(others={"HS": ["HS|REG|A1|1000|11|07/30/1999\r\n"]})}
        with self.assertRaisesRegex(core.FeedError, "ASR_COLUMNS_CHANGED HS"):
            texts.towers(self.ctx)
        self.assertEqual(self.q("SELECT count(*) FROM kfm_sql_sources"), [(0,)])

    def test_no_kansas_registrations_stops_and_a_member_left_empty_is_retired(self):
        self.web.routes = {FIRST_ROUTE: asr_zip([ra("22", "2000", state="NE")])}
        with self.assertRaisesRegex(core.FeedError, "ASR_KANSAS_EMPTY"):
            texts.towers(self.ctx)
        self.web.routes = {FIRST_ROUTE: asr_zip()}
        texts.towers(self.ctx)
        self.ctx.now = lambda: START + timedelta(days=7)
        self.web.routes = {FIRST_ROUTE: asr_zip(others={"SC": []})}
        self.assertEqual(texts.towers(self.ctx)["members"]["SC"], "empty")
        self.assertEqual(self.q("SELECT count(*) FROM kfm_asr_special_conditions"), [(0,)])

    def test_degrees_handle_blanks_and_total_seconds(self):
        self.assertEqual(texts._degrees("39", "30", ".0", "N", ""), 39.5)
        self.assertEqual(texts._degrees("", "", "", "W", "343180.1"), -95.3278056)
        self.assertIsNone(texts._degrees("", "", "", "", ""))


# --- Newspaper directory -----------------------------------------------------------------------------

BASE = "https://www.loc.gov/collections/directory-of-us-newspapers-in-american-libraries/"


def title(number: int) -> dict:
    lccn = f"sn{85000000 + number}"
    return {"id": f"http://www.loc.gov/item/{lccn}/", "url": f"https://www.loc.gov/item/{lccn}/", "title": f"The Prairie News {number}", "date": "1897",
            "dates": ["[1897 TO 1899]"], "number_lccn": [lccn], "location_city": ["abbyville"], "location_county": ["reno"], "location_state": ["kansas"],
            "publication_frequency": ["weekly"], "digitized": False, "language": ["english"], "subject": ["reno"], "description": ["Weekly"],
            "number_succeeding_items": ["sn1"], "number_oclc": ["1"], "number_institution": ["kansas state hist soc"], "number_source_modified": ["2026-04-13t21:30:13"],
            "timestamp": "2026-05-26T23:05:50.058Z", "item": {"created_published": ["Abbyville, Kan. : Phillips, 1897-"]}}


class FakeDirectory:
    """loc.gov's paged answer for a list of titles; fail maps (c, sp) to a list of errors raised on successive asks."""

    def __init__(self, count: int, fail=None):
        self.titles, self.fail, self.asked = [title(n) for n in range(count)], fail or {}, []

    def __call__(self, url):
        query = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))
        size, page = int(query["c"]), int(query["sp"])
        self.asked.append((size, page))
        errors = self.fail.get((size, page))
        if errors:
            error = errors.pop(0)
            if isinstance(error, bytes):
                return error
            raise core.FeedError(f"{error} {url}")
        start, total = size * (page - 1), len(self.titles)
        if start >= total:
            raise core.FeedError(f"HTTP_404 {url}")
        results = self.titles[start:start + size]
        answer = {"pagination": {"current": page, "from": start + 1, "to": start + len(results), "of": total, "perpage": size,
                                 "next": f"{BASE}?sp={page + 1}" if start + size < total else None},
                  "results": [{**t, "index": start + i + 1} for i, t in enumerate(results)]}
        return json.dumps(answer).encode()


class DirectoryTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.ctx.pause = 0

    def run_with(self, directory, **options):
        self.web.routes = {BASE: directory}
        return texts.newspaper_directory(self.ctx, **options)

    def test_reads_every_page_and_keeps_a_sorted_copy_without_positions(self):
        directory = FakeDirectory(230)
        result = self.run_with(directory)
        self.assertEqual((result["state"], result["rows"], result["titles"], result["pages"]), ("loaded", 230, 230, 3))
        self.assertEqual(directory.asked, [(100, 1), (100, 2), (100, 3)])
        row = self.q("SELECT lccn, title, start_year, end_year, city, county, publication_frequency, created_published, digitized, json_extract(record_json,'$.index') "
                     "FROM kfm_loc_newspaper_directory WHERE lccn='sn85000007'")
        self.assertEqual(row, [("sn85000007", "The Prairie News 7", 1897, 1899, "abbyville", "reno", "weekly", "Abbyville, Kan. : Phillips, 1897-", 0, None)])
        self.assertEqual(self.q("SELECT json_extract(receipt_json,'$.key'), json_extract(receipt_json,'$.titles'), imported_rows FROM kfm_sql_sources"), [("directory", 230, 230)])
        kept = list((self.root / "data/raw/sql-feeds/newspaper-directory").glob("loc-newspaper-directory-kansas-*.jsonl.gz"))
        lines = [json.loads(line) for line in gzip.open(kept[0], "rt")]
        self.assertEqual([t["id"] for t in lines], sorted(t["id"] for t in lines))
        self.assertFalse((self.root / "tmp-sql-feeds/newspaper-directory-spool.jsonl").exists())

    def test_requests_are_at_least_six_seconds_apart(self):
        waits = []
        with patch.object(texts, "_pause", lambda ctx, seconds: waits.append(seconds)):
            self.run_with(FakeDirectory(230))
        self.assertEqual(len(waits), 3)
        self.assertGreaterEqual(min(waits), 6.0)

    def test_not_due_for_28_days_and_a_changed_directory_replaces_the_old_one(self):
        self.run_with(FakeDirectory(150))
        calls = len(self.web.calls)
        self.assertEqual(self.run_with(FakeDirectory(150))["state"], "not_due")
        self.assertEqual(len(self.web.calls), calls)
        self.ctx.now = lambda: START + timedelta(days=28)
        self.assertEqual(self.run_with(FakeDirectory(150))["state"], "unchanged")
        self.ctx.now = lambda: START + timedelta(days=56)
        self.assertEqual(self.run_with(FakeDirectory(160))["rows"], 160)
        self.assertEqual(self.q("SELECT count(*) FROM kfm_loc_newspaper_directory"), [(160,)])

    def test_a_temporary_404_on_a_page_is_retried(self):
        directory = FakeDirectory(230, {(100, 2): ["HTTP_404"]})
        result = self.run_with(directory)
        self.assertEqual(result["rows"], 230)
        self.assertEqual(directory.asked, [(100, 1), (100, 2), (100, 2), (100, 3)])

    def test_a_page_that_keeps_failing_is_read_in_smaller_pages_from_the_same_offset(self):
        directory = FakeDirectory(230, {(100, 2): ["HTTP_404", "HTTP_500"]})
        result = self.run_with(directory)
        self.assertEqual((result["rows"], result["titles"]), (230, 230))
        self.assertEqual(directory.asked, [(100, 1), (100, 2), (100, 2), (25, 5), (25, 6), (25, 7), (25, 8), (100, 3)])

    def test_broken_json_and_a_cloudflare_error_are_temporary_too(self):
        directory = FakeDirectory(230, {(100, 1): [b'{"pagination": {"cur'], (100, 2): ["HTTP_520"], (100, 3): ["FETCH_FAILED"]})
        self.assertEqual(self.run_with(directory)["rows"], 230)
        self.assertEqual(directory.asked, [(100, 1), (100, 1), (100, 2), (100, 2), (100, 3), (100, 3)])
        self.assertEqual(sum(line["event"] == "loc_page_retry" for line in self.logs), 3)

    def test_years_ignore_loc_placeholders(self):
        years = texts._directory_years
        self.assertEqual(years({"dates": ["[1897 TO 1899]"]}), (1897, 1899))
        self.assertEqual(years({"dates": ["[2001 TO 9999]"], "date": "2001"}), (2001, None))
        self.assertEqual(years({"dates": ["[1000 TO 1924]"], "date": "1???"}), (None, 1924))
        self.assertEqual(years({"dates": ["[1936 TO 2023]", "[1936 TO 9999]"]}), (1936, 2023))
        self.assertEqual(years({"dates": None, "date": "1854", "title": "The Kansas Herald of Freedom (Wakarusa, Kan. Territory) 1854-1860"}), (1854, 1860))
        self.assertEqual(years({"dates": None, "date": "1897", "title": "The Indian Leader (Lawrence, Kan.) 1897-????"}), (1897, None))
        self.assertEqual(years({"date": "18??", "title": "Recorder 18??-1899"}), (None, 1899))
        self.assertEqual(years({"dates": ["[1911 TO 2099]"]}), (1911, None))
        self.assertEqual(years({}), (None, None))

    def test_a_failed_run_resumes_without_asking_for_finished_pages_again(self):
        broken = {(100, 2): ["HTTP_404", "HTTP_404"], (25, 5): ["HTTP_404"]}
        directory = FakeDirectory(230, broken)
        with self.assertRaisesRegex(core.FeedError, "LOC_PAGE_FAILED HTTP_404"):
            self.run_with(directory)
        state = json.loads(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='newspaper-directory'")[0][0])
        self.assertEqual((state["spool"]["offset"], state["spool"]["of"]), (100, 230))
        self.assertEqual(self.q("SELECT count(*) FROM kfm_sql_sources"), [(0,)])
        directory = FakeDirectory(230)
        self.assertEqual(self.run_with(directory)["rows"], 230)
        self.assertEqual(directory.asked, [(100, 2), (100, 3)])

    def test_a_run_interrupted_after_writing_a_page_ignores_the_unrecorded_part(self):
        with self.assertRaises(core.FeedError):
            self.run_with(FakeDirectory(230, {(100, 2): ["HTTP_404", "HTTP_404"], (25, 5): ["HTTP_404"]}))
        with open(self.root / "tmp-sql-feeds/newspaper-directory-spool.jsonl", "ab") as out:
            out.write(b'{"half written')
        self.assertEqual(self.run_with(FakeDirectory(230))["rows"], 230)

    def test_a_stale_spool_is_not_continued(self):
        with self.assertRaises(core.FeedError):
            self.run_with(FakeDirectory(230, {(100, 2): ["HTTP_404", "HTTP_404"], (25, 5): ["HTTP_404"]}))
        self.ctx.now = lambda: START + timedelta(days=7)
        directory = FakeDirectory(230)
        self.run_with(directory)
        self.assertEqual(directory.asked[0], (100, 1))

    def test_running_out_of_time_is_partial_and_the_next_run_finishes(self):
        result = self.run_with(FakeDirectory(230), max_seconds=-1)
        self.assertEqual((result["state"], result["offset"], result["pages"]), ("partial", 100, 1))
        directory = FakeDirectory(230)
        self.assertEqual(self.run_with(directory)["rows"], 230)
        self.assertEqual(directory.asked, [(100, 2), (100, 3)])

    def test_a_block_stops_at_once(self):
        for error in ("HTTP_429", "HTTP_403", b"<html>challenge</html>"):
            directory = FakeDirectory(230, {(100, 1): [error]})
            with self.assertRaisesRegex(core.FeedError, "LOC_RATE_LIMITED"):
                self.run_with(directory)
            self.assertEqual(directory.asked, [(100, 1)])

    def test_a_list_that_moved_is_dropped_and_read_again_next_run(self):
        directory = FakeDirectory(230)
        directory.titles[150] = directory.titles[50]
        with self.assertRaisesRegex(core.FeedError, "LOC_RESULTS_SHIFTED 229 distinct"):
            self.run_with(directory)
        self.assertFalse((self.root / "tmp-sql-feeds/newspaper-directory-spool.jsonl").exists())
        self.assertEqual(self.run_with(FakeDirectory(230))["rows"], 230)

    def test_a_total_that_changes_part_way_is_refused(self):
        directory = FakeDirectory(230)
        original = directory.__call__

        def moved(url):
            answer = json.loads(original(url))
            if answer["pagination"]["current"] == 2:
                answer["pagination"]["of"] = 231
            return json.dumps(answer).encode()

        with self.assertRaisesRegex(core.FeedError, "LOC_RESULTS_SHIFTED"):
            self.run_with(moved)

    def test_a_silently_changed_page_size_is_refused(self):
        def small(url):
            return json.dumps({"pagination": {"from": 1, "to": 25, "of": 230, "perpage": 25}, "results": [title(n) for n in range(25)]}).encode()

        with self.assertRaisesRegex(core.FeedError, "LOC_PAGE_SIZE_CHANGED"):
            self.run_with(small)

    def test_a_much_smaller_directory_is_refused(self):
        self.run_with(FakeDirectory(200))
        self.ctx.now = lambda: START + timedelta(days=28)
        with self.assertRaisesRegex(core.FeedError, "LOC_DIRECTORY_SHRANK 200 to 100"):
            self.run_with(FakeDirectory(100))
        self.assertEqual(self.q("SELECT count(*) FROM kfm_loc_newspaper_directory"), [(200,)])


# --- Archive texts -----------------------------------------------------------------------------------

class RegistryTests(unittest.TestCase):
    def test_the_lines_for_the_integrator_resolve_to_documented_feeds(self):
        lines = {"archive-texts": "archive_texts", "newspaper-directory": "newspaper_directory", "towers": "towers"}
        with patch.dict(core.FEEDS, {feed: f"tools.local_data.sql_feed_texts:{name}" for feed, name in lines.items()}):
            for feed, name in lines.items():
                function = core.resolve(feed)
                self.assertIs(function, getattr(texts, name))
                self.assertGreater(len(function.__doc__), 100)


SCRAPE, METADATA, FILES = texts.IA_SCRAPE, "https://archive.org/metadata/", "https://archive.org/download/"


def book(identifier: str, year=1883, subject=("Kansas--History",), title_text="History of Kansas", **more) -> dict:
    return {"identifier": identifier, "title": title_text, "year": year, "date": f"{year}-01-01T00:00:00Z" if year else None, "subject": list(subject),
            "collection": ["americana"], "format": ["DjVuTXT", "Text PDF"], "oai_updatedate": ["2026-05-08T17:42:06Z"], "imagecount": 300,
            "item_size": 9000, **more}


def md5(text: bytes) -> str:
    return hashlib.md5(text, usedforsecurity=False).hexdigest()


class FakeArchive:
    """IA's Scrape, metadata and download answers. texts maps identifier to {file name: bytes}; errors maps a URL's start to a FeedError code."""

    def __init__(self, items, files=None):
        self.items, self.files, self.errors, self.page = list(items), dict(files or {}), {}, 2

    def _check(self, url):
        for start, code in self.errors.items():
            if url.startswith(start):
                raise core.FeedError(f"{code} {url}")

    def scrape(self, url):
        self._check(url)
        query = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))
        start = int(query.get("cursor", 0))
        items = self.items[start:start + self.page]
        answer = {"items": items, "count": len(items), "total": len(self.items)}
        if start + self.page < len(self.items):
            answer["cursor"] = str(start + self.page)
        return json.dumps(answer).encode()

    def metadata(self, url):
        self._check(url)
        identifier = url[len(METADATA):].split("/")[0]
        if identifier not in self.files:
            return b"{}"
        listed = [{"name": name, "format": "DjVuTXT", "size": str(len(body)), "md5": md5(body)} for name, body in self.files[identifier].items()]
        return json.dumps({"result": [{"name": "x.pdf", "format": "Text PDF", "size": "9", "md5": "0"}, *listed]}).encode()

    def download(self, url):
        self._check(url)
        identifier, name = url[len(FILES):].split("/", 1)
        return self.files[identifier].get(urllib.parse.unquote(name))

    def routes(self):
        return {SCRAPE: self.scrape, METADATA: self.metadata, FILES: self.download}


class ArchiveCase(FeedCase):
    def setUp(self):
        super().setUp()
        self.target = self.root / "bulk-sql/kfm-bulk.sqlite"
        self.bulk = core.Context(root=self.root, db_path=self.target, bulk_db=self.target, lock=self.root / "pipeline.lock", fetch=self.web,
                                 now=lambda: START, log=self.logs.append, floor=0)
        self.bulk.pause = 0
        core.init_bulk(self.bulk)

    def b(self, sql, *args):
        db = sqlite3.connect(self.target)
        try:
            return db.execute(sql, args).fetchall()
        finally:
            db.close()

    def state(self):
        return json.loads(self.b("SELECT state_json FROM kfm_feed_state WHERE feed='archive-texts'")[0][0])

    def run_feed(self, archive, **options):
        self.web.routes = archive.routes()
        return texts.archive_texts(self.bulk, **options)


class MirrorFallbackTests(ArchiveCase):
    HOST = "https://ia800500.us.archive.org/1/items/"

    def archive(self):
        archive = FakeArchive([book("a")], {"a": {"a_djvu.txt": b"text of a"}})
        routes = archive.routes()
        served = routes[METADATA]
        def metadata(url):
            if url == METADATA + "a":
                archive.checked = True
                return json.dumps({"d1": "ia800500.us.archive.org", "d2": "ia600500.us.archive.org", "dir": "/1/items/a"}).encode()
            return served(url)
        routes[METADATA] = metadata
        routes[self.HOST] = b"text of a"
        archive.routes = lambda: routes
        return archive

    def test_a_mirror_500_reads_the_file_from_the_items_own_server(self):
        archive = self.archive()
        archive.errors[FILES] = "HTTP_500"
        result = self.run_feed(archive)
        self.assertEqual((result["loaded"], result["failed"]), (1, 0))
        self.assertIn(self.HOST + "a/a_djvu.txt", self.web.calls)

    def test_a_refusal_is_not_retried_on_another_server(self):
        archive = self.archive()
        archive.errors[FILES] = "HTTP_403"
        self.run_feed(archive)
        self.assertFalse(any(url.startswith(self.HOST) for url in self.web.calls))

    def test_hosts_outside_archive_org_are_ignored(self):
        self.assertIsNone(texts.IA_HOST.fullmatch("ia800500.evil.example"))
        self.assertIsNone(texts.IA_HOST.fullmatch("archive.org.evil.example"))
        self.assertIsNotNone(texts.IA_HOST.fullmatch("ia800500.us.archive.org"))


class PublicDomainTests(unittest.TestCase):
    def basis(self, **item):
        return texts.pd_basis({"identifier": "x", "format": ["DjVuTXT"], **item}, 1930)

    def test_date_cut_is_inclusive(self):
        self.assertEqual(self.basis(year=1930), "date")
        self.assertIsNone(self.basis(year=1931))
        self.assertEqual(self.basis(date="1883-01-01T00:00:00Z"), "date")
        self.assertIsNone(self.basis())

    def test_explicit_statements(self):
        self.assertEqual(self.basis(year=1950, licenseurl="https://creativecommons.org/publicdomain/zero/1.0/"), "license")
        self.assertEqual(self.basis(licenseurl="http://creativecommons.org/publicdomain/mark/1.0/"), "license")
        self.assertEqual(self.basis(licenseurl="https://www.usa.gov/government-works"), "license")
        self.assertIsNone(self.basis(licenseurl="http://creativecommons.org/licenses/by-nc-nd/3.0/"))
        self.assertEqual(self.basis(**{"possible-copyright-status": "NOT_IN_COPYRIGHT"}), "rights")
        self.assertEqual(self.basis(rights="The contributing institution believes that this item is not in copyright."), "rights")
        self.assertEqual(self.basis(**{"possible-copyright-status": "The Library of Congress is unaware of any copyright restrictions for this item."}), "rights")

    def test_a_copyright_claim_overrides_date_and_statement(self):
        self.assertIsNone(self.basis(year=1920, rights="Copyright is held by Park University, Parkville, Mo."))
        self.assertIsNone(self.basis(year=1920, **{"possible-copyright-status": "In copyright. Digitized with the permission of the rights holder."}))
        self.assertIsNone(self.basis(rights="Public domain source text; modern edition (c) editor."))

    def test_restricted_or_textless_items_are_never_eligible(self):
        self.assertIsNone(self.basis(year=1900, **{"access-restricted-item": "true"}))
        self.assertIsNone(self.basis(year=1900, collection=["printdisabled"]))
        self.assertIsNone(texts.pd_basis({"identifier": "x", "year": 1900, "format": ["Text PDF"]}, 1930))

    def test_queue_ranks(self):
        self.assertEqual(texts.queue_rank({"subject": ["Kansas--History"], "title": "Annals"}), 0)
        self.assertEqual(texts.queue_rank({"subject": ["Nebraska"], "title": "Kansas annals"}), 1)
        self.assertEqual(texts.queue_rank({"subject": "Kansas City (Mo.)", "title": "Annals"}), 1)
        self.assertEqual(texts.queue_rank({"subject": ["Kansas"], "title": "The Kansas City Star"}), 2)


class ArchiveTextTests(ArchiveCase):
    def test_refuses_a_context_without_the_bulk_database(self):
        with self.assertRaisesRegex(core.FeedError, "BULK_DATABASE_REQUIRED"):
            texts.archive_texts(self.ctx)

    def test_loads_listing_and_public_domain_text_with_a_searchable_index(self):
        body = "\n".join(f"Line {i} of the settlement of Kansas territory" for i in range(8000)).encode()
        archive = FakeArchive([book("andreas", 1883), book("newer", 1990, rights="In copyright"), book("nodate", None)], {"andreas": {"andreas_djvu.txt": body}})
        result = self.run_feed(archive)
        self.assertEqual((result["listing"], result["loaded"], result["pending"], result["stopped"]), ("loaded", 1, 0, None))
        self.assertEqual(self.b("SELECT identifier, year, pd_basis, queue_rank, has_text, imagecount FROM kfm_ia_items ORDER BY identifier"),
                         [("andreas", 1883, "date", 0, 1, 300), ("newer", 1990, None, 0, 1, 300), ("nodate", None, None, 0, 1, 300)])
        parts = self.b("SELECT part, char_count, file_name FROM kfm_ia_texts ORDER BY part")
        self.assertGreater(len(parts), 2)
        self.assertLessEqual(max(p[1] for p in parts), texts.IA_PART_CHARS)
        joined = "".join(t for (t,) in self.b("SELECT text FROM kfm_ia_texts ORDER BY part"))
        self.assertEqual(joined.encode(), body)
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_texts_fts WHERE kfm_ia_texts_fts MATCH 'settlement'"), [(len(parts),)])
        self.assertEqual(self.b("SELECT status, oai_updatedate FROM kfm_ia_text_status"), [("loaded", '["2026-05-08T17:42:06Z"]')])
        key, license, digest = self.b("SELECT json_extract(receipt_json,'$.key'), json_extract(receipt_json,'$.license'), json_extract(receipt_json,'$.md5') "
                                      "FROM kfm_sql_sources WHERE source_id=?", texts.IA_TEXT_SOURCE)[0]
        self.assertEqual((key, digest), ("text/andreas/andreas_djvu.txt", md5(body)))
        self.assertIn("public domain (date", license)
        kept = list((self.root / "data/raw/sql-feeds/archive-texts/texts/an/andreas").glob("andreas_djvu-*.txt.gz"))
        self.assertEqual(gzip.decompress(kept[0].read_bytes()), body)
        self.assertEqual(self.state()["pd_cutoff_year"], 1930)
        self.assertFalse([p for p in (self.root / "tmp-sql-feeds").glob("*ia-text*")])

    def test_parts_cut_at_line_ends_and_lose_nothing(self):
        text = "".join(f"line {i}\n" for i in range(60000))
        parts = list(texts.ia_parts(io.StringIO(text), 1000))
        self.assertEqual("".join(parts), text)
        self.assertTrue(all(len(p) <= 1000 and p.endswith("\n") for p in parts))
        self.assertEqual(list(texts.ia_parts(io.StringIO("x" * 2500), 1000)), ["x" * 1000, "x" * 1000, "x" * 500])
        self.assertEqual(list(texts.ia_parts(io.StringIO(""), 1000)), [])
        self.assertEqual(list(texts.ia_parts(io.StringIO("a\x00b"), 1000)), ["ab"])

    def test_a_budget_stops_the_run_and_the_next_run_continues_without_repeating_work(self):
        items = [book(f"b{i}", 1880 + i) for i in range(5)]
        archive = FakeArchive(items, {f"b{i}": {f"b{i}_djvu.txt": f"text {i}".encode()} for i in range(5)})
        result = self.run_feed(archive, max_items=2)
        self.assertEqual((result["loaded"], result["pending"], result["stopped"]), (2, 3, "budget"))
        self.assertEqual(self.b("SELECT identifier FROM kfm_ia_text_status ORDER BY identifier"), [("b0",), ("b1",)])
        self.web.calls.clear()
        result = self.run_feed(archive, max_items=2)
        self.assertEqual((result["listing"], result["loaded"], result["pending"]), ("not_due", 2, 1))
        self.assertFalse([u for u in self.web.calls if "b0" in u or "b1" in u or u.startswith(SCRAPE)])
        self.assertEqual(self.run_feed(archive)["loaded"], 1)
        self.assertEqual(self.run_feed(archive)["pending"], 0)

    def test_requests_and_bytes_budgets_hold(self):
        items = [book(f"b{i}", 1880 + i) for i in range(4)]
        archive = FakeArchive(items, {f"b{i}": {f"b{i}_djvu.txt": b"x" * 1000 + str(i).encode()} for i in range(4)})
        result = self.run_feed(archive, max_bytes=1500)      # the listing (2 pages), then b0; b1 would pass the bytes
        self.assertEqual((result["loaded"], result["stopped"], result["bytes"]), (1, "budget", 1001))
        self.assertEqual(result["requests"], 5)
        result = self.run_feed(archive, max_requests=2)      # b1 fits: metadata and text; b2 would pass the requests
        self.assertEqual((result["loaded"], result["stopped"], result["requests"]), (1, "budget", 2))
        result = self.run_feed(archive, max_seconds=-1)
        self.assertEqual((result["loaded"], result["requests"], result["stopped"]), (0, 0, "budget"))

    def test_order_is_kansas_subject_then_title_then_kansas_city_oldest_first(self):
        items = [book("kc", 1880, title_text="The Kansas City Star"), book("title", 1880, subject=["Nebraska"], title_text="Kansas annals"),
                 book("young", 1920), book("old", 1860)]
        archive = FakeArchive(items, {i["identifier"]: {f"{i['identifier']}_djvu.txt": i["identifier"].encode()} for i in items})
        self.run_feed(archive)
        order = [u[len(FILES):].split("/")[0] for u in self.web.calls if u.startswith(FILES)]
        self.assertEqual(order, ["old", "young", "title", "kc"])

    def test_rate_limit_stops_at_once_and_keeps_what_loaded(self):
        items = [book(f"b{i}", 1880 + i) for i in range(3)]
        archive = FakeArchive(items, {f"b{i}": {f"b{i}_djvu.txt": f"text {i}".encode()} for i in range(3)})
        archive.errors = {FILES + "b1/": "HTTP_503"}
        with self.assertRaisesRegex(core.FeedError, "IA_RATE_LIMITED HTTP_503"):
            self.run_feed(archive)
        self.assertEqual(self.b("SELECT identifier FROM kfm_ia_text_status"), [("b0",)])
        self.assertTrue(self.state()["stopped"].startswith("IA_RATE_LIMITED"))
        self.assertFalse([u for u in self.web.calls if "b2" in u])
        archive.errors = {METADATA + "b1/": "HTTP_429"}
        with self.assertRaisesRegex(core.FeedError, "IA_RATE_LIMITED HTTP_429"):
            self.run_feed(archive)
        archive.errors = {}
        self.assertEqual(self.run_feed(archive)["loaded"], 2)
        self.assertIsNone(self.state()["stopped"])

    def test_a_503_is_not_retried_by_the_download_itself(self):
        calls = []

        def download(url, dest, *, limit, timeout=600, attempts=3, missing_ok=False):
            calls.append(attempts)
            dest.write_bytes(b"text")
            return core.Fetched(url, b"")

        self.bulk.fetch = core.http_fetch
        with patch.object(core, "http_download", download):
            run = texts._IARun(self.bulk, 1, 1, 1, 1)
            run.download("https://archive.org/download/a/b", self.root / "probe", 4)
        self.assertEqual(calls, [1])

    def test_listing_refused_or_limited_keeps_the_loaded_listing(self):
        archive = FakeArchive([book("a"), book("b"), book("c")], {"a": {"a_djvu.txt": b"text a"}, "b": {"b_djvu.txt": b"text b"}, "c": {"c_djvu.txt": b"text c"}})
        self.run_feed(archive)
        self.bulk.now = lambda: START + timedelta(days=28)
        archive.errors = {SCRAPE: "HTTP_429"}
        with self.assertRaisesRegex(core.FeedError, "IA_RATE_LIMITED"):
            self.run_feed(archive)
        archive.errors = {SCRAPE: "HTTP_403"}
        with self.assertRaisesRegex(core.FeedError, "IA_BLOCKED"):
            self.run_feed(archive)
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_items"), [(3,)])
        archive.errors, archive.items = {}, archive.items[:2]
        with self.assertRaisesRegex(core.FeedError, "IA_LISTING_SHRANK 3 to 2"):
            self.run_feed(archive)
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_texts"), [(3,)])

    def test_a_listing_that_does_not_add_up_is_refused(self):
        archive = FakeArchive([book("a"), book("b"), book("a"), book("c")])
        with self.assertRaisesRegex(core.FeedError, "IA_RESULTS_SHIFTED 3 of 4"):
            self.run_feed(archive)

    def test_a_missing_file_or_item_is_recorded_and_the_run_goes_on(self):
        items = [book("gone"), book("nofile", 1884), book("good", 1885), book("empty", 1886)]
        archive = FakeArchive(items, {"nofile": {}, "good": {"good_djvu.txt": b"good text"}, "empty": {"empty_djvu.txt": b""}})
        archive.files["missingfile"] = {}
        self.assertEqual(self.run_feed(archive)["loaded"], 1)
        self.assertEqual(self.b("SELECT identifier, status FROM kfm_ia_text_status ORDER BY identifier"),
                         [("empty", "empty"), ("gone", "missing"), ("good", "loaded"), ("nofile", "no_text")])

    def test_404_on_the_text_file_is_recorded_as_missing(self):
        archive = FakeArchive([book("a"), book("b", 1884)], {"a": {"a_djvu.txt": b"text"}, "b": {"b_djvu.txt": b"more"}})
        archive.errors = {FILES + "a/": "HTTP_404"}
        self.assertEqual(self.run_feed(archive)["loaded"], 1)
        self.assertEqual(self.b("SELECT identifier, status, detail IS NOT NULL FROM kfm_ia_text_status ORDER BY identifier"), [("a", "missing", 1), ("b", "loaded", 0)])
        archive.errors = {}
        self.assertEqual(self.run_feed(archive)["pending"], 0)   # not asked again until 182 days on, or until the item changes
        self.bulk.now = lambda: START + timedelta(days=182)
        self.assertEqual(self.run_feed(archive)["loaded"], 1)

    def test_an_unsafe_identifier_is_never_requested_or_kept(self):
        archive = FakeArchive([book("../escape")], {"../escape": {"x_djvu.txt": b"text"}})
        result = self.run_feed(archive)
        self.assertEqual((result["without_text"], result["requests"]), (1, 1))     # the listing only
        self.assertEqual(self.b("SELECT status FROM kfm_ia_text_status"), [("bad_identifier",)])

    def test_a_private_file_is_not_requested(self):
        archive = FakeArchive([book("a")], {"a": {"a_djvu.txt": b"text"}})
        archive.metadata = lambda url: json.dumps({"result": [{"name": "a_djvu.txt", "format": "DjVuTXT", "size": "4", "md5": "x", "private": "true"}]}).encode()
        self.run_feed(archive)
        self.assertFalse([u for u in self.web.calls if u.startswith(FILES)])
        self.assertEqual(self.b("SELECT status FROM kfm_ia_text_status"), [("restricted",)])

    def test_md5_mismatch_is_a_failure_of_that_file_only(self):
        archive = FakeArchive([book("a"), book("b", 1884)], {"a": {"a_djvu.txt": b"text"}, "b": {"b_djvu.txt": b"more"}})
        listed = archive.metadata

        def wrong(url):
            answer = json.loads(listed(url))
            if "/a/" in url:
                answer["result"][1]["md5"] = "0" * 32
            return json.dumps(answer).encode()

        archive.metadata = wrong
        result = self.run_feed(archive)
        self.assertEqual((result["loaded"], result["failed"]), (1, 1))
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_texts WHERE identifier='a'"), [(0,)])
        archive.metadata = listed
        self.assertEqual(self.run_feed(archive)["pending"], 0)      # failed items wait 7 days
        self.bulk.now = lambda: START + timedelta(days=7)
        self.assertEqual(self.run_feed(archive)["loaded"], 1)

    def test_repeated_failures_or_refusals_stop_the_run(self):
        items = [book(f"b{i}", 1880 + i) for i in range(8)]
        files = {f"b{i}": {f"b{i}_djvu.txt": f"text {i}".encode()} for i in range(8)}
        archive = FakeArchive(items, files)
        archive.errors = {FILES: "FETCH_FAILED"}
        with self.assertRaisesRegex(core.FeedError, "IA_UNAVAILABLE"):
            self.run_feed(archive)
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_text_status WHERE status='failed'"), [(texts.IA_STOP_FAILURES,)])
        archive.errors = {FILES: "HTTP_403"}
        with self.assertRaisesRegex(core.FeedError, "IA_BLOCKED"):
            self.run_feed(archive)
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_text_status WHERE status='forbidden'"), [(texts.IA_STOP_FORBIDDEN,)])
        self.assertTrue(self.state()["stopped"].startswith("IA_BLOCKED"))

    def test_identical_bytes_on_two_items_load_once(self):
        archive = FakeArchive([book("twin1"), book("twin2", 1884)], {"twin1": {"twin1_djvu.txt": b"same text"}, "twin2": {"twin2_djvu.txt": b"same text"}})
        result = self.run_feed(archive)
        self.assertEqual((result["loaded"], result["without_text"]), (1, 1))
        self.assertEqual(self.b("SELECT identifier, status FROM kfm_ia_text_status ORDER BY identifier"), [("twin1", "loaded"), ("twin2", "duplicate")])
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_texts"), [(1,)])

    def test_a_revised_item_replaces_its_text_and_an_unchanged_md5_is_not_downloaded(self):
        archive = FakeArchive([book("a")], {"a": {"a_djvu.txt": b"wheat harvest"}})
        self.run_feed(archive)
        self.bulk.now = lambda: START + timedelta(days=28)
        archive.items = [book("a", oai_updatedate=["2026-12-01T00:00:00Z"])]
        self.web.calls.clear()
        result = self.run_feed(archive)
        self.assertEqual((result["listing"], result["unchanged"], result["loaded"]), ("loaded", 1, 0))
        self.assertFalse([u for u in self.web.calls if u.startswith(FILES)])
        self.bulk.now = lambda: START + timedelta(days=56)
        archive.items = [book("a", oai_updatedate=["2027-01-01T00:00:00Z"])]
        archive.files["a"] = {"a_djvu.txt": b"corn harvest"}
        self.assertEqual(self.run_feed(archive)["loaded"], 1)
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_texts_fts WHERE kfm_ia_texts_fts MATCH 'wheat'"), [(0,)])
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_texts_fts WHERE kfm_ia_texts_fts MATCH 'corn'"), [(1,)])
        self.assertEqual(self.b("SELECT state, count(*) FROM kfm_sql_sources WHERE source_id=? GROUP BY state", texts.IA_TEXT_SOURCE), [("complete", 1), ("superseded", 1)])

    def test_a_half_done_item_skips_the_file_it_has_and_a_dropped_file_is_retired(self):
        archive = FakeArchive([book("a")], {"a": {"a1_djvu.txt": b"first volume", "a2_djvu.txt": b"second volume"}})
        with patch.object(texts, "_ia_set_status"):
            archive.errors = {FILES + "a/a2": "HTTP_429"}
            with self.assertRaisesRegex(core.FeedError, "IA_RATE_LIMITED"):
                self.run_feed(archive)
        self.assertEqual(self.b("SELECT file_name FROM kfm_ia_texts"), [("a1_djvu.txt",)])
        archive.errors = {}
        self.web.calls.clear()
        result = self.run_feed(archive)
        self.assertEqual(result["rows"], 1)
        self.assertEqual([u for u in self.web.calls if u.startswith(FILES)], [FILES + "a/a2_djvu.txt"])
        self.bulk.now = lambda: START + timedelta(days=28)
        archive.items = [book("a", oai_updatedate=["2027-01-01T00:00:00Z"])]
        archive.files["a"] = {"a2_djvu.txt": b"second volume"}
        self.run_feed(archive)
        self.assertEqual(self.b("SELECT file_name FROM kfm_ia_texts"), [("a2_djvu.txt",)])

    def test_an_item_that_stops_qualifying_or_leaves_is_retired(self):
        archive = FakeArchive([book(f"b{i}", 1880 + i) for i in range(12)],
                              {f"b{i}": {f"b{i}_djvu.txt": f"unique text {i}".encode()} for i in range(12)})
        self.run_feed(archive)
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_texts"), [(12,)])
        self.bulk.now = lambda: START + timedelta(days=28)
        archive.items = [*archive.items[:10], book("b10", 1890, rights="In copyright."), book("newcomer", 1900)]
        archive.files["newcomer"] = {"newcomer_djvu.txt": b"newcomer text"}
        result = self.run_feed(archive)
        self.assertEqual((result["retired"], result["loaded"]), (2, 1))
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_texts WHERE identifier IN ('b10','b11')"), [(0,)])
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_text_status WHERE identifier IN ('b10','b11')"), [(0,)])
        self.assertEqual(self.b("SELECT count(*) FROM kfm_ia_texts_fts WHERE kfm_ia_texts_fts MATCH '\"text 11\"'"), [(0,)])

    def test_a_new_year_moves_the_cut_and_reloads_the_listing(self):
        archive = FakeArchive([book("a", 1931)], {"a": {"a_djvu.txt": b"text of 1931"}})
        self.assertEqual(self.run_feed(archive)["loaded"], 0)
        self.bulk.now = lambda: datetime(2027, 1, 2, 15, 0, tzinfo=timezone.utc)
        result = self.run_feed(archive)
        self.assertEqual((result["listing"], result["loaded"]), ("loaded", 1))
        self.assertEqual(self.b("SELECT pd_basis FROM kfm_ia_items"), [("date",)])

    def test_requests_are_at_least_a_second_apart(self):
        waits = []
        archive = FakeArchive([book("a")], {"a": {"a_djvu.txt": b"text"}})
        with patch.object(texts, "_pause", lambda ctx, seconds: waits.append(seconds)):
            self.run_feed(archive)
        self.assertEqual(len(waits), 3)
        self.assertGreaterEqual(min(waits), 1.0)

    def test_a_rerun_with_nothing_due_asks_nothing(self):
        archive = FakeArchive([book("a")], {"a": {"a_djvu.txt": b"text"}})
        self.run_feed(archive)
        self.web.calls.clear()
        result = self.run_feed(archive)
        self.assertEqual((self.web.calls, result["pending"], result["listing"]), ([], 0, "not_due"))


if __name__ == "__main__":
    unittest.main()
