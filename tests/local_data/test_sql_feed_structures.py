"""SQL feeds for Kansas airports, obstacles, dams, mines, grade crossings and rail lines, without network access."""
import csv
from datetime import datetime, timezone
import gzip
import io
import json
import sqlite3
import unittest
import urllib.parse
import zipfile

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_structures as st, sql_feeds as core


def at(*args):
    return lambda: datetime(*args, 15, 0, tzinfo=timezone.utc)


def zipped(members: dict) -> bytes:
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w") as archive:
        for name, body in members.items():
            archive.writestr(name, body)
    return out.getvalue()


def lines(rows, delimiter=",", ending="\r\n") -> bytes:
    out = io.StringIO()
    csv.writer(out, delimiter=delimiter, lineterminator=ending).writerows(rows)
    return out.getvalue().encode()


def params(url: str) -> dict:
    return {k: v[0] for k, v in urllib.parse.parse_qs(urllib.parse.urlsplit(url).query).items()}


def unavailable(url):
    raise core.FeedError("HTTP_503 " + url)


class SharedTests(FeedCase):
    def test_ddl_names_bbox_and_dof_fields(self):
        self.assertEqual(st.ddl("t", ["a", "b", "c"], {"a": "INTEGER", "b": ""}, [("a", "c")]),
                         'CREATE TABLE IF NOT EXISTS t (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, "a" INTEGER, "b", "c" TEXT, '
                         'PRIMARY KEY(file_id, row_number));\nCREATE INDEX IF NOT EXISTS t_a_c ON t("a", "c");\n')
        self.assertEqual([st.column_name(h) for h in ("NID ID", "Is Associated Structure?", "Max Discharge (Cubic Ft/Second)",
                                                      "Non-USACE Dam with USACE Flood Control Storage Authority (Section 7, Flood Control Act of 1944)")],
                         ["nid_id", "is_associated_structure", "max_discharge_cubic_ft_second",
                          "non_usace_dam_with_usace_flood_control_storage_authority_section_7_flood_control_act_of_1944"])
        self.assertEqual(st.bbox({"type": "MultiPolygon", "coordinates": [[[[-97, 38], [-96, 38], [-96, 39], [-97, 38]]], [[[-99, 37.5], [-98, 37.5], [-98, 37.9], [-99, 37.5]]]]}),
                         (-99, 37.5, -96, 39))
        self.assertEqual(st.point(-97.0, 38.5), '{"coordinates":[-97.0,38.5],"type":"Point"}')
        self.assertIsNone(st.point(None, 38.5))
        row = st.dof_values(DOF_TOWER)
        self.assertEqual(row[:7], ("20-000296", "20", "000296", "O", "US", "KS", "ELKHART"))
        self.assertEqual(row[16:19], (1, 345, 3976))
        self.assertEqual((row[23], row[26], row[27], row[28]), ("2013ACE02350OE", 36.9944444, -101.9056889, '{"coordinates":[-101.9056889,36.9944444],"type":"Point"}'))
        self.assertEqual(st.dof_values(DOF_POLE)[23], "")
        with self.assertRaisesRegex(core.FeedError, "DOF_LINE_SHORT"):
            st.dof_values(DOF_TOWER[:100])
        # Every table keeps the framework's (file_id, row_number) key; NARN attribute columns are untyped, OBJECTID an INTEGER.
        self.assertIn('"objectid" INTEGER, "fraarcid", "frfranode",', st.NARN_DDL)
        self.assertEqual(len(st.FRA_COLUMNS), 263)
        self.assertEqual(len(st.NID_COLUMNS), 83)


# --- Airports --------------------------------------------------------------------------------------

APRA_XML = '<?xml version="1.0"?><productSet><status code="200"/><edition editionDate="{date}" editionName="CURRENT"><product productName="NASR" url="x"/></edition></productSet>'


def nasr_row(stem, **values):
    row = [""] * len(st.NASR_COLUMNS[stem])
    for column, value in {"eff_date": "2026/10/29", "site_type_code": "A", "state_code": "KS", "country_code": "US", **values}.items():
        row[st.NASR_COLUMNS[stem].index(column)] = value
    return row


def nasr_member(stem, rows, header=None):
    return lines([header or [c.upper() for c in st.NASR_COLUMNS[stem]], *rows])


class AirportTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.edition, self.members = "10/29/2026", {}
        self.members["APT_BASE.csv"] = nasr_member("APT_BASE", [
            nasr_row("APT_BASE", site_no="06460.", arpt_id="K78", city="ABILENE", county_name="DICKINSON", lat_decimal="38.90405555", long_decimal="-97.23586111"),
            nasr_row("APT_BASE", site_no="01074.06", arpt_id="95KS", city="MAPLE HILL", county_name="WABAUNSEE", lat_decimal="39.02616111", long_decimal="-96.01504166"),
            nasr_row("APT_BASE", site_no="18045.", arpt_id="OMA", city="OMAHA", state_code="NE", lat_decimal="41.3", long_decimal="-95.9")])
        self.members["APT_RWY.csv"] = nasr_member("APT_RWY", [nasr_row("APT_RWY", site_no="06460.", arpt_id="K78", rwy_id="18/36", rwy_len="4100")])
        self.members["APT_RWY_END.csv"] = nasr_member("APT_RWY_END", [
            nasr_row("APT_RWY_END", site_no="06460.", arpt_id="K78", rwy_id="18/36", rwy_end_id="18", lat_decimal="38.9", long_decimal="-97.2"),
            nasr_row("APT_RWY_END", site_no="06460.", arpt_id="K78", rwy_id="18/36", rwy_end_id="36", lat_decimal="", long_decimal="")])
        self.members["APT_ATT.csv"] = nasr_member("APT_ATT", [nasr_row("APT_ATT", site_no="06460.", arpt_id="K78", sked_seq_no="1", month="ALL")]) + b"\r\n"
        # A remark line the FAA malformed (a stray delimiter) is still Kansas, so it is kept and loaded as malformed_line.
        self.members["APT_RMK.csv"] = (nasr_member("APT_RMK", [nasr_row("APT_RMK", site_no="06460.", arpt_id="K78", remark="OWNER REQUESTS CHARTING.")])
                                       + b'"2026/10/29","06460.","A","KS","K78","ABILENE","US","A110-1","AIRPORT","GENERAL_REMARK","",1,"BAD","EXTRA"\r\n')
        self.members["APT_CON.csv"] = nasr_member("APT_CON", [nasr_row("APT_CON", site_no="06460.", arpt_id="K78", title="MANAGER", name="A. PERSON")])
        self.members["APT_ARS.csv"] = nasr_member("APT_ARS", [nasr_row("APT_ARS", site_no="06979.", arpt_id="IAB", rwy_id="01L/19R", rwy_end_id="01L", arrest_device_code="BAK-12B")])
        self.posted = True
        self.web.routes = {st.APRA: lambda url: APRA_XML.format(date=self.edition).encode(),
                           "https://nfdc.faa.gov/webContent/28DaySub/extra/": lambda url: zipped(self.members) if self.posted else None}

    def zip_calls(self):
        return [u for u in self.web.calls if "28DaySub" in u]

    def test_the_current_edition_is_cut_to_kansas_per_member_and_fetched_once(self):
        result = st.airports(self.ctx)
        self.assertEqual((result["edition"], result["rows"], result["loaded"]), ("2026-10-29", 10, list(st.NASR_FILES)))
        self.assertEqual(self.zip_calls(), ["https://nfdc.faa.gov/webContent/28DaySub/extra/29_Oct_2026_APT_CSV.zip"])
        self.assertEqual(self.q("SELECT arpt_id, lat_decimal, typeof(lat_deg), geometry_geojson, malformed_line FROM kfm_nasr_airports ORDER BY row_number"),
                         [("K78", 38.90405555, "text", '{"coordinates":[-97.23586111,38.90405555],"type":"Point"}', None),
                          ("95KS", 39.02616111, "text", '{"coordinates":[-96.01504166,39.02616111],"type":"Point"}', None)])
        self.assertEqual(self.q("SELECT rwy_end_id, lat_decimal, geometry_geojson FROM kfm_nasr_runway_ends ORDER BY row_number"),
                         [("18", 38.9, '{"coordinates":[-97.2,38.9],"type":"Point"}'), ("36", None, None)])
        self.assertEqual(self.q("SELECT arpt_id, remark, malformed_line FROM kfm_nasr_remarks ORDER BY row_number"),
                         [("K78", "OWNER REQUESTS CHARTING.", None),
                          (None, None, '"2026/10/29","06460.","A","KS","K78","ABILENE","US","A110-1","AIRPORT","GENERAL_REMARK","",1,"BAD","EXTRA"')])
        self.assertEqual(self.q("SELECT arrest_device_code FROM kfm_nasr_arresting_systems"), [("BAK-12B",)])
        sources = self.q("SELECT source_id, json_extract(receipt_json,'$.key'), imported_rows, source_path FROM kfm_sql_sources ORDER BY file_id")
        self.assertEqual([s[:3] for s in sources], [("faa-nasr-kansas", k, n) for k, n in zip(st.NASR_FILES, (2, 1, 2, 1, 2, 1, 1))])
        self.assertRegex(sources[0][3], r"/data/raw/sql-feeds/airports/APT_BASE/APT_BASE-2026-10-29-KS-[0-9a-f]{12}\.csv\.gz$")
        receipt = json.loads(self.q("SELECT receipt_json FROM kfm_sql_sources WHERE json_extract(receipt_json,'$.key')='APT_RMK'")[0][0])
        archive = zipped(self.members)
        self.assertEqual({k: receipt[k] for k in ("archive", "citation", "dropped_lines", "edition", "key", "license", "malformed_lines", "rows", "terms")},
                         {"archive": {"bytes": len(archive), "sha256": core.sha256(archive)}, "citation": st.NASR_CITATION, "dropped_lines": 0,
                          "edition": "2026-10-29", "key": "APT_RMK", "license": st.PUBLIC_DOMAIN, "malformed_lines": 1, "rows": 2, "terms": st.NASR_TERMS})
        self.assertNotIn("original", receipt)
        self.assertEqual(json.loads(self.q("SELECT receipt_json FROM kfm_sql_sources WHERE json_extract(receipt_json,'$.key')='APT_ATT'")[0][0])["dropped_lines"], 1)
        # The kept copy is the FAA's own lines: header and Kansas lines, CRLF as published.
        kept = gzip.decompress(next((self.root / "data/raw/sql-feeds/airports/APT_BASE").glob("*.csv.gz")).read_bytes())
        self.assertEqual(kept.count(b"\r\n"), 3)
        self.assertNotIn(b"OMAHA", kept)
        self.assertEqual(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='airports'"), [('{"edition":"2026-10-29"}',)])
        # The same edition costs one APRA request and no download.
        self.assertEqual(st.airports(self.ctx), {"state": "not_due", "edition": "2026-10-29"})
        self.assertEqual(len(self.zip_calls()), 1)
        # The next edition: a changed member replaces its rows, the unchanged members are recognized by their bytes.
        self.ctx.now, self.edition = at(2026, 11, 27), "11/26/2026"
        self.members["APT_RWY.csv"] = nasr_member("APT_RWY", [nasr_row("APT_RWY", site_no="06460.", arpt_id="K78", rwy_id="18/36", rwy_len="4200")])
        result = st.airports(self.ctx)
        self.assertEqual((result["loaded"], len(result["unchanged"])), (["APT_RWY"], 6))
        self.assertEqual(self.zip_calls()[-1], "https://nfdc.faa.gov/webContent/28DaySub/extra/26_Nov_2026_APT_CSV.zip")
        self.assertEqual(self.q("SELECT rwy_len FROM kfm_nasr_runways"), [("4200",)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources GROUP BY state"), [("complete", 7), ("superseded", 1)])
        self.assertEqual(core.get_state(core.open_db(self.ctx), "airports"), {"edition": "2026-11-26"})

    def test_an_unposted_edition_is_retried_and_a_member_problem_is_reported_after_the_others(self):
        self.posted = False
        self.assertEqual(st.airports(self.ctx), {"state": "not_posted", "edition": "2026-10-29"})
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_feed_state"), [(0,)])
        self.posted = True
        self.members["APT_ARS.csv"] = nasr_member("APT_ARS", [], header=["EFF_DATE", "SITE_NO"])
        with self.assertRaisesRegex(core.FeedError, "NASR_FILES_FAILED APT_ARS: NASR_COLUMNS_CHANGED"):
            st.airports(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='complete'"), [(6,)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_feed_state"), [(0,)], "the edition is not recorded until every member loaded")
        del self.members["APT_ARS.csv"]
        with self.assertRaisesRegex(core.FeedError, "NASR_MEMBER_MISSING APT_ARS.csv"):
            st.airports(self.ctx)
        self.members["APT_ARS.csv"] = nasr_member("APT_ARS", [nasr_row("APT_ARS", site_no="06979.", arpt_id="IAB", rwy_end_id="01L", arrest_device_code="BAK-12B")])
        result = st.airports(self.ctx)
        self.assertEqual((result["loaded"], len(result["unchanged"])), (["APT_ARS"], 6))
        self.assertEqual(st.airports(self.ctx)["state"], "not_due")
        self.web.routes[st.APRA] = b"<html>moved</html>"
        with self.assertRaisesRegex(core.FeedError, "NASR_EDITION_UNREADABLE"):
            st.airports(self.ctx)

    def test_a_missing_apra_service_falls_back_to_the_28_day_cycle_calendar(self):
        # APRA's nasr/chart query answered 404 from 2026-11-03; the clock is 2026-11-04, inside the 2026-10-29 cycle.
        self.web.routes[st.APRA] = None
        result = st.airports(self.ctx)
        self.assertEqual((result["edition"], result["loaded"]), ("2026-10-29", list(st.NASR_FILES)))
        self.assertEqual(st.airports(self.ctx)["state"], "not_due")
        # The next cycle begins 28 days later; its zip is not posted yet, so the feed waits without failing.
        self.ctx.now = lambda: datetime(2026, 11, 26, 15, 0, tzinfo=timezone.utc)
        self.posted = False
        self.assertEqual(st.airports(self.ctx), {"state": "not_posted", "edition": "2026-11-26"})
        self.assertEqual(self.zip_calls()[-1], "https://nfdc.faa.gov/webContent/28DaySub/extra/26_Nov_2026_APT_CSV.zip")


# --- Obstacles -------------------------------------------------------------------------------------

DOF_HEAD = ["  CURRENCY DATE = 10/28/26",
            "                                     LATITUDE    LONGITUDE     OBSTACLE            AGL  AMSL LT ACC MAR FAA       ACTION",
            "OAS#      V CO ST CITY             DEG MIN SEC  DEG MIN SEC   TYPE                 HT    HT    H V IND STUDY            JDATE",
            "-" * 127]
DOF_TOWER = "20-000296 O US KS ELKHART          36 59 40.00N 101 54 20.48W TOWER              1 00345 03976 D 4 D N 2013ACE02350OE C 2014078 "
DOF_POLE = "20-022333 O US KS ELKHART          36 59 45.82N 101 52 51.61W POLE               1 00004 03620 U 1 A U                C 2020121 "
DOF_OKLAHOMA = "40-000484 O US OK ROLLA            36 59 47.00N 101 30 50.00W TOWER              1 00199 03500 N 4 D M                C 2014152 "


def dof(*rows, head=DOF_HEAD, currency="10/28/26"):
    head = [head[0].replace("10/28/26", currency), *head[1:]]
    return zipped({"DOF.DAT": "".join(l + "\r\n" for l in [*head, *rows])})


class ObstacleTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.zip = dof(DOF_TOWER, DOF_POLE, DOF_OKLAHOMA)
        self.web.routes = {st.DOF_ZIP: lambda url: self.zip}

    def test_the_national_file_is_cut_on_state_ks_and_rechecked_every_28_days(self):
        result = st.obstacles(self.ctx)
        self.assertEqual((result["state"], result["rows"], result["currency_date"], result["obstacles"]), ("loaded", 2, "10/28/26", 2))
        self.assertEqual(self.q("SELECT oas_number, obstacle_number, city, obstacle_type, quantity, agl_height_ft, amsl_height_ft, faa_study_number, "
                                "latitude, longitude, geometry_geojson FROM kfm_faa_obstacles ORDER BY row_number"),
                         [("20-000296", "000296", "ELKHART", "TOWER", 1, 345, 3976, "2013ACE02350OE", 36.9944444, -101.9056889,
                           '{"coordinates":[-101.9056889,36.9944444],"type":"Point"}'),
                          ("20-022333", "022333", "ELKHART", "POLE", 1, 4, 3620, "", 36.9960611, -101.8810028,
                           '{"coordinates":[-101.8810028,36.9960611],"type":"Point"}')])
        source = self.q("SELECT source_id, source_path, receipt_json FROM kfm_sql_sources")[0]
        self.assertEqual(source[0], "faa-dof-kansas")
        self.assertRegex(source[1], r"/obstacles/dof-KS-[0-9a-f]{12}\.dat\.gz$")
        receipt = json.loads(source[2])
        self.assertEqual({k: receipt[k] for k in ("citation", "currency_date", "kansas_test", "key", "license", "rows", "terms")},
                         {"citation": st.DOF_CITATION, "currency_date": "10/28/26", "kansas_test": "state KS (columns 16-17)", "key": "KS",
                          "license": st.PUBLIC_DOMAIN, "rows": 2, "terms": st.DOF_TERMS})
        self.assertEqual((receipt["original"]["bytes"], receipt["original"]["kept"], receipt["last_modified"]), (len(self.zip), False, "Sun, 01 Nov 2026 00:00:00 GMT"))
        kept = gzip.decompress(next((self.root / "data/raw/sql-feeds/obstacles").glob("*.dat.gz")).read_bytes()).decode()
        self.assertEqual(kept, "".join(l + "\r\n" for l in [*DOF_HEAD, DOF_TOWER, DOF_POLE]))
        self.assertEqual(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='obstacles'"), [('{"currency_date":"10/28/26","fetched":"2026-11-04"}',)])
        self.assertEqual(st.obstacles(self.ctx)["state"], "not_due")
        self.assertEqual(len(self.web.calls), 1)
        self.ctx.now = at(2026, 12, 3)
        self.assertEqual(st.obstacles(self.ctx)["state"], "unchanged")
        self.ctx.now, self.zip = at(2027, 1, 1), dof(DOF_TOWER, DOF_OKLAHOMA, currency="12/30/26")
        result = st.obstacles(self.ctx)
        self.assertEqual((result["state"], result["superseded"], result["currency_date"]), ("loaded", 1, "12/30/26"))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_faa_obstacles"), [(1,)])

    def test_a_changed_layout_stops_before_anything_is_kept(self):
        self.zip = dof(DOF_TOWER, head=["  EFFECTIVE 10/28/26", *DOF_HEAD[1:]])
        with self.assertRaisesRegex(core.FeedError, "DOF_FORMAT_CHANGED"):
            st.obstacles(self.ctx)
        self.zip = dof(DOF_TOWER.replace("00345", "003A5"))
        with self.assertRaisesRegex(core.FeedError, "DOF_NOT_A_NUMBER"):
            st.obstacles(self.ctx)
        self.zip = dof(DOF_OKLAHOMA)
        with self.assertRaisesRegex(core.FeedError, "DOF_NO_KANSAS_ROWS"):
            st.obstacles(self.ctx)
        self.zip = zipped({"README.txt": "no data"})
        with self.assertRaisesRegex(core.FeedError, "DOF_MEMBER_MISSING"):
            st.obstacles(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertFalse((self.root / "data/raw/sql-feeds/obstacles").exists())


# --- Dams ------------------------------------------------------------------------------------------

NID_HEADER = ("Dam Name,Other Names,Former Names,NID ID,Other Structure ID,Federal ID,Owner Names,Owner Types,Primary Owner Type,Number of Associated "
              "Structures,Is Associated Structure?,Designer Names,Non-Federal Dam on Federal Property,Primary Purpose,Purposes,Source Agency,State or "
              "Federal Agency ID,Latitude,Longitude,State,County,City,Distance to Nearest City (Miles),River or Stream Name,Congressional District,State "
              "Regulated Dam,State Jurisdictional Dam,State Regulatory Agency,State Permitting Authority,State Inspection Authority,State Enforcement "
              "Authority,Federally Regulated Dam,Federal Agency Owners,Federal Agency Involvement Funding,Federal Agency Involvement Design,Federal Agency "
              "Involvement Construction,Federal Agency Involvement Regulatory,Federal Agency Involvement Inspection,Federal Agency Involvement Operation,"
              "Federal Agency Involvement Other,Built Under the Authority of the Secretary of Agriculture,NRCS Watershed Dam Authorization,Primary Dam Type,"
              "Dam Types,Core Types,Foundation,Dam Height (Ft),Hydraulic Height (Ft),Structural Height (Ft),NID Height (Ft),NID Height Category,Dam Length "
              "(Ft),Volume (Cubic Yards),Year Completed,Year Completed Category,Years Modified,NID Storage (Acre-Ft),Max Storage (Acre-Ft),Normal Storage "
              "(Acre-Ft),Surface Area (Acres),Drainage Area (Sq Miles),Max Discharge (Cubic Ft/Second),Spillway Type,Spillway Width (Ft),Number of Locks,"
              "Length of Locks (ft),Lock Width (Ft),Length of Secondary Lock (Ft),Secondary Lock Width (Ft),Outlet Gate Type,Data Last Updated,Last "
              "Inspection Date,Inspection Frequency,Hazard Potential Classification,EAP Prepared,EAP Last Revision Date,Website URL,Operational Status,"
              "Operational Status Date,Inundation Maps Added to NID?,American Indian/Alaska Native/Native Hawaiian,Has Photo?,\"Non-USACE Dam with USACE "
              "Flood Control Storage Authority (Section 7, Flood Control Act of 1944)\"")


def dam(name, nid_id, lat, lon, state="Kansas", county="Morris", year="1964"):
    row = [""] * 83
    for column, value in (("dam_name", name), ("nid_id", nid_id), ("latitude", lat), ("longitude", lon), ("state", state), ("county", county),
                          ("year_completed", year), ("owner_names", "USACE - Tulsa District"), ("congressional_district", "Kansas, Congressional District 02")):
        row[st.NID_COLUMNS.index(column)] = value
    return row


def nid_csv(rows, header=NID_HEADER):
    return "﻿".encode() + (header + "\n").encode() + lines(rows, ending="\n")


class DamTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.rows = [dam("Elk City Dam", "KS00002", "37.2772000000001", "-95.78786", county="Montgomery"), dam("Council Grove Dam", "KS00001", "38.6805614250001", "-96.502653113"),
                     dam("Unlocated Dam", "KS00003", "", "")]
        self.web.routes = {st.NID_URL: lambda url: nid_csv(self.rows)}

    def test_kansas_dams_load_sorted_by_nid_id_and_are_rechecked_weekly(self):
        result = st.dams(self.ctx)
        self.assertEqual((result["state"], result["rows"], result["records"]), ("loaded", 3, 3))
        self.assertEqual(self.q("SELECT nid_id, dam_name, latitude, typeof(year_completed), congressional_district, geometry_geojson FROM kfm_nid_dams ORDER BY row_number"),
                         [("KS00001", "Council Grove Dam", 38.6805614250001, "text", "Kansas, Congressional District 02", '{"coordinates":[-96.502653113,38.6805614250001],"type":"Point"}'),
                          ("KS00002", "Elk City Dam", 37.2772000000001, "text", "Kansas, Congressional District 02", '{"coordinates":[-95.78786,37.2772000000001],"type":"Point"}'),
                          ("KS00003", "Unlocated Dam", None, "text", "Kansas, Congressional District 02", None)])
        source = self.q("SELECT source_id, source_path, receipt_json FROM kfm_sql_sources")[0]
        self.assertEqual(source[0], "usace-nid-kansas")
        self.assertRegex(source[1], r"/dams/nid-dams-KS-[0-9a-f]{12}\.csv\.gz$")
        receipt = json.loads(source[2])
        self.assertEqual({k: receipt[k] for k in ("citation", "key", "license", "rows", "terms", "etag", "last_modified")},
                         {"citation": st.NID_CITATION, "key": "KS", "license": st.PUBLIC_DOMAIN, "rows": 3, "terms": st.NID_TERMS, "etag": None, "last_modified": None})
        self.assertEqual(receipt["original"]["bytes"], len(nid_csv(self.rows)))
        kept = gzip.decompress(next((self.root / "data/raw/sql-feeds/dams").glob("*.csv.gz")).read_bytes())
        self.assertTrue(kept.startswith(b"Dam Name,"), "no BOM, the title row as published")
        self.assertEqual(kept.split(b"\n")[1].split(b",")[3], b"KS00001")
        self.assertEqual(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='dams'"), [('{"fetched":"2026-11-04","records":3}',)])
        self.assertEqual(st.dams(self.ctx)["state"], "not_due")
        # A week later the same dams in another order are the same version.
        self.ctx.now, self.rows = at(2026, 11, 12), list(reversed(self.rows))
        self.assertEqual(st.dams(self.ctx)["state"], "unchanged")
        self.ctx.now = at(2026, 11, 20)
        self.rows[0][st.NID_COLUMNS.index("year_completed")] = "1965"
        self.assertEqual(st.dams(self.ctx)["superseded"], 1)
        self.assertEqual(self.q("SELECT year_completed FROM kfm_nid_dams WHERE nid_id='KS00003'"), [("1965",)])

    def test_other_states_and_header_changes_stop_without_loading(self):
        self.rows.append(dam("Keystone Dam", "OK00001", "36.15", "-96.25", state="Oklahoma"))
        with self.assertRaisesRegex(core.FeedError, "NID_NOT_KANSAS"):
            st.dams(self.ctx)
        self.rows = [dam("Bad Dam", "KS00009", "north", "-96")]
        with self.assertRaisesRegex(core.FeedError, "NOT_A_NUMBER"):
            st.dams(self.ctx)
        self.web.routes[st.NID_URL] = nid_csv([dam("x", "KS00001", "38", "-96")], header=NID_HEADER.replace("NID ID", "NID Identifier"))
        with self.assertRaisesRegex(core.FeedError, "NID_COLUMNS_CHANGED"):
            st.dams(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertFalse((self.root / "data/raw/sql-feeds/dams").exists())


# --- Mines -----------------------------------------------------------------------------------------

def mrds_site(dep_id, name, lat, lon, state="Kansas", county="Riley"):
    row = [""] * len(st.MRDS_COLUMNS)
    for column, value in (("dep_id", dep_id), ("site_name", name), ("latitude", lat), ("longitude", lon), ("state", state), ("county", county),
                          ("commod3", "Titanium, Metal, Garnet"), ("url", f"https://mrdata.usgs.gov/mrds/show-mrds.php?dep_id={dep_id}")):
        row[st.MRDS_COLUMNS.index(column)] = value
    return row


GML_HEAD = ('<?xml version=\'1.0\' encoding="UTF-8" ?>\n<wfs:FeatureCollection xmlns:ms="http://mapserver.gis.umn.edu/mapserver" '
            'xmlns:wfs="http://www.opengis.net/wfs" xmlns:gml="http://www.opengis.net/gml">\n<gml:boundedBy><gml:Box srsName="EPSG:4326">'
            '<gml:coordinates>-98,39 -95,40</gml:coordinates></gml:Box></gml:boundedBy>\n')


def gml_feature(layer, fid, geometry, **properties):
    props = {"state": "KS", "county": "Atchison", "ftr_type": "Adit", "ftr_name": "", "topo_name": "Atchison East", "topo_date": "1984",
             "topo_scale": "24000", "compiledby": "USGS", "remarks": "", "gda_id": "5969740", "scanid": "513005",
             "url": f"https://mrdata.usgs.gov/usmin/show-usmin.php?type={layer[:-1]}&amp;id={fid}", **properties}
    body = "".join(f"<ms:{k}>{v}</ms:{k}>" for k, v in props.items())
    return (f'<gml:featureMember><ms:{layer} fid="{layer}.{fid}"><gml:boundedBy><gml:Box srsName="EPSG:4326"><gml:coordinates>-98,39 -95,40'
            f'</gml:coordinates></gml:Box></gml:boundedBy><ms:geometry>{geometry}</ms:geometry>{body}</ms:{layer}></gml:featureMember>\n')


def gml_point(lon, lat):
    return f'<gml:Point srsName="EPSG:4326"><gml:coordinates>{lon},{lat}</gml:coordinates></gml:Point>'


def gml_polygon(outer, *holes):
    ring = lambda points: "<gml:LinearRing><gml:coordinates>" + " ".join(f"{x},{y}" for x, y in points) + " </gml:coordinates></gml:LinearRing>"
    return ('<gml:Polygon srsName="EPSG:4326"><gml:outerBoundaryIs>' + ring(outer) + "</gml:outerBoundaryIs>"
            + "".join("<gml:innerBoundaryIs>" + ring(h) + "</gml:innerBoundaryIs>" for h in holes) + "</gml:Polygon>")


def gml(*features):
    return (GML_HEAD + "".join(features) + "</wfs:FeatureCollection>\n").encode()


def msha_mine(mine_id, name, state="KS", lon="-95.5", lat="38.1", county="Lincoln"):
    row = [""] * len(st.MSHA_COLUMNS)
    for column, value in (("mine_id", mine_id), ("current_mine_name", name), ("state", state), ("longitude", lon), ("latitude", lat),
                          ("fips_cnty_nm", county), ("days_per_week", "5"), ("directions_to_mine", "from Lincoln, KS travel 1.1 miles south on KS-14")):
        row[st.MSHA_COLUMNS.index(column)] = value
    return row


class MineTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.mrds = [mrds_site("10121108", "Mille Brothers Constr Sand Pit", "39.33311", "-101.81047", county="Sherman"),
                     mrds_site("10068349", "Stockdale Kimberlite Deposit", "39.33336", "-96.66698"), mrds_site("10000001", "Joplin Field", "37.1", "-94.5", state="Missouri"),
                     ["10000002", "short row"]]
        self.usmin = {"points": gml(gml_feature("points", 148351, gml_point(-95.113054, 39.537076), ftr_azimut="316", dir="nw"),
                                    gml_feature("points", 148350, gml_point(-95.115471, 39.53514), ftr_azimut="5", dir="n")),
                      "polygons": gml(gml_feature("polygons", 28871, gml_polygon([(-95.0785, 39.6353), (-95.0763, 39.6353), (-95.0763, 39.6364), (-95.0785, 39.6353)],
                                                                                  [(-95.078, 39.6355), (-95.077, 39.6355), (-95.077, 39.636), (-95.078, 39.6355)]),
                                                  ftr_type="Borrow Pit", county="Doniphan"))}
        self.msha = [msha_mine("0203501", "Portable Crusher No. 4", lon="-111.739722", lat="33.465833"), msha_mine("0504581", "Screening Oper", lon="", lat=""),
                     msha_mine("2300001", "Missouri Quarry", state="MO")]
        self.msha_extra = b'"0203502"|"Broken Line"|"M"|"Surface"|"Intermittent"|"07/31/2026"|"0138763"|"X"|"0155455"|"Rango Inc."|"KS"|"14"\r\n\r\n'
        self.web.routes = {st.MRDS_ZIP: lambda url: zipped({"mrds.csv": lines([st.MRDS_COLUMNS, *self.mrds], ending="\n")}),
                           "https://mrdata.usgs.gov/services/wfs/usmin": lambda url: self.usmin[params(url)["typename"]],
                           st.MSHA_ZIP: lambda url: zipped({"Mines.txt": lines([st.MSHA_HEADER, *self.msha], delimiter="|") + self.msha_extra})}

    def test_three_sources_load_on_their_own_schedules(self):
        result = st.mines(self.ctx)
        self.assertEqual((result["mrds"]["rows"], result["usmin"], result["msha"]["rows"]), (2, {"rows": 3, "points": "loaded", "polygons": "loaded"}, 3))
        self.assertEqual(self.q("SELECT dep_id, site_name, latitude, commod3, geometry_geojson FROM kfm_mrds_sites ORDER BY row_number"),
                         [("10121108", "Mille Brothers Constr Sand Pit", 39.33311, "Titanium, Metal, Garnet", '{"coordinates":[-101.81047,39.33311],"type":"Point"}'),
                          ("10068349", "Stockdale Kimberlite Deposit", 39.33336, "Titanium, Metal, Garnet", '{"coordinates":[-96.66698,39.33336],"type":"Point"}')])
        self.assertEqual(self.q("SELECT layer, fid, ftr_type, ftr_azimut, dir, url, min_lon, min_lat, max_lon, max_lat FROM kfm_usmin_features ORDER BY file_id, row_number"),
                         [("points", 148350, "Adit", "5", "n", "https://mrdata.usgs.gov/usmin/show-usmin.php?type=point&id=148350", -95.115471, 39.53514, -95.115471, 39.53514),
                          ("points", 148351, "Adit", "316", "nw", "https://mrdata.usgs.gov/usmin/show-usmin.php?type=point&id=148351", -95.113054, 39.537076, -95.113054, 39.537076),
                          ("polygons", 28871, "Borrow Pit", None, None, "https://mrdata.usgs.gov/usmin/show-usmin.php?type=polygon&id=28871", -95.0785, 39.6353, -95.0763, 39.6364)])
        polygon = json.loads(self.q("SELECT geometry_geojson FROM kfm_usmin_features WHERE layer='polygons'")[0][0])
        self.assertEqual((polygon["type"], len(polygon["coordinates"]), polygon["coordinates"][1][0]), ("Polygon", 2, [-95.078, 39.6355]))
        self.assertEqual(self.q("SELECT mine_id, current_mine_name, days_per_week, longitude, geometry_geojson, malformed_line FROM kfm_msha_mines ORDER BY row_number"),
                         [("0203501", "Portable Crusher No. 4", "5", -111.739722, '{"coordinates":[-111.739722,33.465833],"type":"Point"}', None),
                          ("0504581", "Screening Oper", "5", None, None, None),
                          (None, None, None, None, None, '"0203502"|"Broken Line"|"M"|"Surface"|"Intermittent"|"07/31/2026"|"0138763"|"X"|"0155455"|"Rango Inc."|"KS"|"14"')])
        sources = self.q("SELECT source_id, json_extract(receipt_json,'$.key'), imported_rows, source_path, receipt_json FROM kfm_sql_sources ORDER BY file_id")
        self.assertEqual([s[:3] for s in sources], [("usgs-mrds-kansas", "mrds", 2), ("usgs-usmin-kansas", "usmin/points", 2),
                                                    ("usgs-usmin-kansas", "usmin/polygons", 1), ("msha-mines-kansas", "msha", 3)])
        self.assertRegex(sources[0][3], r"/mines/mrds/mrds-KS-[0-9a-f]{12}\.csv\.gz$")
        self.assertRegex(sources[1][3], r"/mines/usmin/usmin-points-KS-[0-9a-f]{12}\.jsonl\.gz$")
        self.assertRegex(sources[3][3], r"/mines/msha/mines-KS-[0-9a-f]{12}\.txt\.gz$")
        mrds, usmin, msha = (json.loads(sources[i][4]) for i in (0, 1, 3))
        self.assertEqual((mrds["dropped_rows"], mrds["citation"], mrds["terms"], mrds["original"]["kept"], mrds["last_modified"]),
                         (1, st.MRDS_CITATION, st.MRDS_TERMS, False, "Sun, 01 Nov 2026 00:00:00 GMT"))
        self.assertEqual({k: usmin[k] for k in ("filter", "layer", "license", "rows", "terms", "etag", "citation")},
                         {"filter": "state = 'KS'", "layer": "points", "license": st.PUBLIC_DOMAIN, "rows": 2, "terms": st.USMIN_TERMS, "etag": None, "citation": st.USMIN_CITATION})
        self.assertEqual(usmin["original"]["bytes"], len(self.usmin["points"]))
        self.assertEqual((msha["dropped_lines"], msha["malformed_lines"], msha["rows"], msha["citation"], msha["terms"]), (1, 1, 3, st.MSHA_CITATION, st.MSHA_TERMS))
        # Kept forms: USMIN features canonical and sorted by fid; MSHA lines as published.
        kept = gzip.decompress(next((self.root / "data/raw/sql-feeds/mines/usmin").glob("usmin-points-*")).read_bytes()).decode().splitlines()
        self.assertTrue(kept[0].startswith('{"fid":148350,"geometry":{"coordinates":[-95.115471,39.53514],"type":"Point"},"properties":{"compiledby":"USGS",'))
        kept = gzip.decompress(next((self.root / "data/raw/sql-feeds/mines/msha").glob("*.txt.gz")).read_bytes())
        self.assertEqual((kept.count(b"\r\n"), kept.count(b"Missouri")), (4, 0))
        self.assertEqual(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='mines'"), [('{"mrds":"2026-11-04","msha":"2026-11-04","usmin":"2026-11-04"}',)])
        # A week later only MSHA is due; after 91 days USMIN too; MRDS waits 182 days.
        self.ctx.now, self.web.calls = at(2026, 11, 12), []
        self.assertEqual(st.mines(self.ctx), {"mrds": "not_due", "usmin": "not_due", "msha": {"state": "unchanged", "rows": 0, "superseded": 0}})
        self.assertEqual(self.web.calls, [st.MSHA_ZIP])
        self.ctx.now = at(2027, 2, 5)
        self.usmin["points"] = gml(gml_feature("points", 148350, gml_point(-95.115471, 39.53514), ftr_azimut="5", dir="n"))
        result = st.mines(self.ctx)
        self.assertEqual((result["mrds"], result["usmin"]["points"], result["usmin"]["polygons"]), ("not_due", "loaded", "unchanged"))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usmin_features WHERE layer='points'"), [(1,)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources GROUP BY state"), [("complete", 4), ("superseded", 1)])

    def test_a_failing_source_is_reported_after_the_others_and_retried_next_run(self):
        self.web.routes["https://mrdata.usgs.gov/services/wfs/usmin"] = unavailable
        with self.assertRaisesRegex(core.FeedError, "MINES_SOURCES_FAILED usmin: HTTP_503"):
            st.mines(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_mrds_sites"), [(2,)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_msha_mines"), [(3,)])
        self.assertEqual(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='mines'"), [('{"mrds":"2026-11-04","msha":"2026-11-04"}',)])
        self.web.routes["https://mrdata.usgs.gov/services/wfs/usmin"] = lambda url: self.usmin[params(url)["typename"]]
        self.assertEqual(st.mines(self.ctx)["usmin"]["rows"], 3)
        # Field, Kansas and layout changes; a rate limit names the source.
        self.usmin["points"] = gml(gml_feature("points", 1, gml_point(-95.1, 39.5), state="MO"))
        self.ctx.now = at(2027, 3, 1)
        with self.assertRaisesRegex(core.FeedError, "USMIN_NOT_KANSAS points"):
            st.mines(self.ctx)
        self.usmin["points"] = gml(gml_feature("points", 1, gml_point(-95.1, 39.5), newfield="x"))
        with self.assertRaisesRegex(core.FeedError, "USMIN_FIELDS_CHANGED points"):
            st.mines(self.ctx)
        self.usmin["points"] = b'<?xml version="1.0"?><ServiceExceptionReport><ServiceException>bad</ServiceException></ServiceExceptionReport>'
        with self.assertRaisesRegex(core.FeedError, "USMIN_RESPONSE_SHAPE points ServiceExceptionReport"):
            st.mines(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usmin_features WHERE layer='points'"), [(2,)])
        self.ctx.now = at(2027, 6, 1)
        self.web.routes[st.MSHA_ZIP] = lambda url: (_ for _ in ()).throw(core.FeedError("HTTP_429 " + url))
        self.web.routes[st.MRDS_ZIP] = zipped({"mrds.csv": lines([st.MRDS_COLUMNS[:-1], ["x"] * 45], ending="\n")})
        with self.assertRaisesRegex(core.FeedError, "MINES_SOURCES_FAILED mrds: MRDS_COLUMNS_CHANGED; .*msha: MSHA_RATE_LIMITED"):
            st.mines(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_mrds_sites"), [(2,)])


# --- Grade crossings -------------------------------------------------------------------------------

def crossing(crossingid, lat, lon, statecode="20", railroad="UP"):
    row = [""] * len(st.FRA_COLUMNS)
    for column, value in (("crossingid", crossingid), ("latitude", lat), ("longitude", lon), ("statecode", statecode), ("railroadcode", railroad),
                          ("countycode", "20035"), ("revisiondate", "1980-01-01T00:00:00.000"), ("railroadnarrative", "two\nlines")):
        row[st.FRA_COLUMNS.index(column)] = value
    return row


class CrossingTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.rows = [crossing("435313T", "37.2248190", "-97.0389250"), crossing("009063K", "", "", railroad="ATSF"), crossing("435312L", "37.2", "-97.1")]
        self.view = {"id": "m2f8-22s6", "name": "Crossing Inventory Data (Form 71) - Current", "rowsUpdatedAt": 1793622164, "license": {"name": "Public Domain"}}
        self.count = None
        self.web.routes = {"https://data.transportation.gov/api/views/": lambda url: json.dumps(self.view).encode(),
                           "https://data.transportation.gov/resource/": self.soda}

    def soda(self, url):
        query = params(url)
        self.assertEqual(query["$where"], "statecode='20'")
        if url.split("?")[0].endswith(".json"):
            return json.dumps([{"count": str(self.count if self.count is not None else len(self.rows))}]).encode()
        offset, limit = int(query["$offset"]), int(query["$limit"])
        return st.csv_bytes([st.FRA_COLUMNS, *self.rows[offset:offset + limit]])

    def test_kansas_crossings_are_paged_counted_and_rechecked_every_28_days(self):
        result = st.grade_crossings(self.ctx, page_size=2)
        self.assertEqual((result["state"], result["rows"], result["records"]), ("loaded", 3, 3))
        self.assertEqual(self.q("SELECT crossingid, railroadcode, countycode, latitude, railroadnarrative, geometry_geojson FROM kfm_fra_crossings ORDER BY row_number"),
                         [("435313T", "UP", "20035", 37.224819, "two\nlines", '{"coordinates":[-97.038925,37.224819],"type":"Point"}'),
                          ("009063K", "ATSF", "20035", None, "two\nlines", None), ("435312L", "UP", "20035", 37.2, "two\nlines", '{"coordinates":[-97.1,37.2],"type":"Point"}')])
        self.assertEqual([u for u in self.web.calls if ".csv" in u],
                         ["https://data.transportation.gov/resource/m2f8-22s6.csv?$where=statecode%3D%2720%27&$order=%3Aid&$limit=2&$offset=0",
                          "https://data.transportation.gov/resource/m2f8-22s6.csv?$where=statecode%3D%2720%27&$order=%3Aid&$limit=2&$offset=2"])
        source = self.q("SELECT source_id, source_path, source_url, receipt_json FROM kfm_sql_sources")[0]
        self.assertEqual((source[0], source[2]), ("fra-crossings-kansas", self.web.calls[2]))
        self.assertRegex(source[1], r"/grade-crossings/fra-crossings-KS-[0-9a-f]{12}\.csv\.gz$")
        receipt = json.loads(source[3])
        self.assertEqual({k: receipt[k] for k in ("citation", "dataset", "key", "license", "rows", "rows_updated_at", "terms", "where", "etag")},
                         {"citation": "Federal Railroad Administration, Crossing Inventory Data (Form 71) - Current", "dataset": "m2f8-22s6", "key": "KS",
                          "license": "Public Domain (dataset license)", "rows": 3, "rows_updated_at": 1793622164,
                          "terms": "https://data.transportation.gov/api/views/m2f8-22s6.json", "where": "statecode='20'", "etag": None})
        self.assertNotIn("original", receipt)
        self.assertEqual(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='grade-crossings'"), [('{"fetched":"2026-11-04","records":3}',)])
        self.web.calls.clear()
        self.assertEqual(st.grade_crossings(self.ctx)["state"], "not_due")
        self.assertEqual(self.web.calls, [])
        self.ctx.now = at(2026, 12, 3)
        self.assertEqual(st.grade_crossings(self.ctx, page_size=2)["state"], "unchanged")
        self.ctx.now, self.rows = at(2027, 1, 1), self.rows[:2]
        self.assertEqual(st.grade_crossings(self.ctx, page_size=2)["superseded"], 1)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_fra_crossings"), [(2,)])

    def test_count_header_dataset_and_state_checks_stop_without_loading(self):
        self.count = 5
        with self.assertRaisesRegex(core.FeedError, "FRA_CROSSINGS_EXTRACT_MISMATCH 3 of 5"):
            st.grade_crossings(self.ctx, page_size=2)
        self.count = None
        self.rows.append(crossing("1", "40.1", "-96.1", statecode="31"))
        with self.assertRaisesRegex(core.FeedError, "FRA_CROSSINGS_NOT_KANSAS"):
            st.grade_crossings(self.ctx, page_size=2)
        self.rows = [crossing("1", "north", "-96.1")]
        with self.assertRaisesRegex(core.FeedError, "NOT_A_NUMBER"):
            st.grade_crossings(self.ctx)
        self.web.routes["https://data.transportation.gov/resource/"] = lambda url: (json.dumps([{"count": "1"}]).encode() if ".json?" in url
                                                                                   else st.csv_bytes([st.FRA_COLUMNS[:-1], ["x"] * 262]))
        with self.assertRaisesRegex(core.FeedError, "FRA_CROSSINGS_COLUMNS_CHANGED"):
            st.grade_crossings(self.ctx)
        self.view["name"] = "Something else"
        with self.assertRaisesRegex(core.FeedError, "FRA_CROSSINGS_DATASET_CHANGED"):
            st.grade_crossings(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertFalse((self.root / "data/raw/sql-feeds/grade-crossings").exists())


# --- Rail lines ------------------------------------------------------------------------------------

def segment(objectid, coordinates, stateab="KS", **values):
    properties = {name: None for name in st.NARN_PROPERTIES.values()}
    properties.update({"OBJECTID": objectid, "FRAARCID": 345000 + objectid, "FRFRANODE": 368748, "TOFRANODE": 368755, "STFIPS": "20", "CNTYFIPS": "133",
                       "STCNTYFIPS": "20133", "STATEAB": stateab, "COUNTRY": "US", "FRADISTRCT": 6, "RROWNER1": "SKOL", "SUBDIV": "CHANUTE", "TRACKS": 0,
                       "NET": "O", "MILES": 0.15973083461493143, "KM": 0.2570623744272811, "TIMEZONE": "C", "Shape__Length": 0.002524075961748751, **values})
    return {"type": "Feature", "id": objectid, "geometry": {"type": "LineString", "coordinates": coordinates}, "properties": properties}


class RailLineTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.features = [segment(39560, [[-94.61, 39.09], [-94.6, 39.1]]), segment(39558, [[-95.4646065192218, 37.6971087508275], [-95.46, 37.7]]),
                         segment(39559, [[-94.68, 39.1], [-94.67, 39.11]], RROWNER1="UP")]
        self.count = None
        self.web.routes = {st.NARN_LAYER + "/query?": self.query}

    def query(self, url):
        query = params(url)
        self.assertEqual((query["where"], query.get("outSR", "4326")), ("STATEAB='KS'", "4326"))
        if query.get("returnCountOnly") == "true":
            return json.dumps({"count": self.count if self.count is not None else len(self.features)}).encode()
        offset, limit = int(query["resultOffset"]), int(query["resultRecordCount"])
        features = sorted(self.features, key=lambda f: f["id"])[offset:offset + limit]
        return json.dumps({"type": "FeatureCollection", "features": features, "properties": {"exceededTransferLimit": offset + limit < len(self.features)}}).encode()

    def test_kansas_segments_are_paged_sorted_and_kept_with_the_services_value_types(self):
        result = st.rail_lines(self.ctx, page_size=2)
        self.assertEqual(result, {"rows": 3, "KS": "loaded"})
        self.assertEqual(self.q("SELECT objectid, fraarcid, typeof(fraarcid), stfips, rrowner1, rrowner2, tracks, miles, shape_length, min_lon, max_lat "
                                "FROM kfm_narn_rail_lines ORDER BY row_number"),
                         [(39558, 384558, "integer", "20", "SKOL", None, 0, 0.15973083461493143, 0.002524075961748751, -95.4646065192218, 37.7),
                          (39559, 384559, "integer", "20", "UP", None, 0, 0.15973083461493143, 0.002524075961748751, -94.68, 39.11),
                          (39560, 384560, "integer", "20", "SKOL", None, 0, 0.15973083461493143, 0.002524075961748751, -94.61, 39.1)])
        self.assertEqual(self.q("SELECT geometry_geojson FROM kfm_narn_rail_lines WHERE objectid=39558"),
                         [('{"coordinates":[[-95.4646065192218,37.6971087508275],[-95.46,37.7]],"type":"LineString"}',)])
        pages = [u for u in self.web.calls if "f=geojson" in u]
        self.assertEqual(pages[0], st.NARN_LAYER + "/query?where=STATEAB%3D%27KS%27&outFields=%2A&outSR=4326&orderByFields=OBJECTID&resultOffset=0&resultRecordCount=2&f=geojson")
        self.assertEqual(len(pages), 2)
        source = self.q("SELECT source_id, source_path, source_url, receipt_json FROM kfm_sql_sources")[0]
        self.assertEqual((source[0], source[2]), ("bts-narn-rail-lines-kansas", pages[0]))
        self.assertRegex(source[1], r"/rail-lines/KS/rail-lines-KS-KS-[0-9a-f]{12}\.jsonl\.gz$")
        receipt = json.loads(source[3])
        self.assertEqual({k: receipt[k] for k in ("citation", "kansas_test", "key", "layer", "license", "rows", "terms", "where", "last_modified")},
                         {"citation": st.NARN_CITATION, "kansas_test": "STATEAB='KS'", "key": "KS", "layer": "KS", "license": st.NARN_LICENSE, "rows": 3,
                          "terms": st.NARN_LAYER, "where": "STATEAB='KS'", "last_modified": None})
        kept = gzip.decompress(next((self.root / "data/raw/sql-feeds/rail-lines/KS").glob("*.jsonl.gz")).read_bytes()).decode().splitlines()
        self.assertEqual([json.loads(l)["properties"]["OBJECTID"] for l in kept], [39558, 39559, 39560])
        self.assertTrue(kept[0].startswith('{"geometry":{"coordinates":[[-95.4646065192218,37.6971087508275],[-95.46,37.7]],"type":"LineString"},"properties":{"BRANCH":null,'))
        self.assertTrue(kept[0].endswith(',"type":"Feature"}'))
        self.assertNotIn('"id"', kept[0])
        self.assertEqual(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='rail-lines'"), [('{"KS":"2026-11-04"}',)])
        self.web.calls.clear()
        self.assertEqual(st.rail_lines(self.ctx), {"rows": 0, "KS": "not_due"})
        self.assertEqual(self.web.calls, [])
        self.ctx.now = at(2026, 12, 3)
        self.assertEqual(st.rail_lines(self.ctx, page_size=2)["KS"], "unchanged")
        self.ctx.now, self.features[0]["properties"]["TRACKS"] = at(2027, 1, 1), 2
        self.assertEqual(st.rail_lines(self.ctx, page_size=2)["KS"], "loaded")
        self.assertEqual(self.q("SELECT tracks FROM kfm_narn_rail_lines WHERE objectid=39560"), [(2,)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources GROUP BY state"), [("complete", 1), ("superseded", 1)])

    def test_field_state_and_count_changes_stop_without_loading(self):
        self.count = 4
        with self.assertRaisesRegex(core.FeedError, "NARN_EXTRACT_MISMATCH 3 of 4"):
            st.rail_lines(self.ctx)
        self.count = None
        self.features.append(segment(1, [[-96, 40.1], [-96, 40.2]], stateab="NE"))
        with self.assertRaisesRegex(core.FeedError, "NARN_NOT_KANSAS 1"):
            st.rail_lines(self.ctx)
        del self.features[-1]["properties"]["SUBDIV"]
        with self.assertRaisesRegex(core.FeedError, "NARN_FIELDS_CHANGED"):
            st.rail_lines(self.ctx)
        self.web.routes[st.NARN_LAYER + "/query?"] = b'{"error": {"code": 400}}'
        with self.assertRaisesRegex(core.FeedError, "NARN_RESPONSE_SHAPE count"):
            st.rail_lines(self.ctx)
        self.web.routes[st.NARN_LAYER + "/query?"] = lambda url: (_ for _ in ()).throw(core.FeedError("HTTP_429 " + url))
        with self.assertRaisesRegex(core.FeedError, "NARN_RATE_LIMITED"):
            st.rail_lines(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertFalse((self.root / "data/raw/sql-feeds/rail-lines").exists())


if __name__ == "__main__":
    unittest.main()
