"""OpenFEMA SQL feed: Kansas extracts paged by key, replaced when FEMA refreshes, without network access."""
from datetime import datetime, timezone
import json
import unittest
import urllib.parse
from unittest.mock import patch

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_fema as fe, sql_feeds as core

DS = {d.name: d for d in fe.DATASETS}
DDS, CLAIMS = DS["DisasterDeclarationsSummaries"], DS["NfipClaims"]


def at(*args):
    return lambda: datetime(*args, 15, 0, tzinfo=timezone.utc)


def declaration(uid, county, state="KS", area="Trego (County)", title="COVID-19 PANDEMIC"):
    return {"femaDeclarationString": f"DR-4504-{state}", "disasterNumber": 4504, "state": state, "declarationType": "DR",
            "declarationDate": "2020-03-29T00:00:00.000Z", "fyDeclared": 2020, "incidentType": "Biological", "declarationTitle": title,
            "ihProgramDeclared": True, "iaProgramDeclared": False, "paProgramDeclared": True, "hmProgramDeclared": True,
            "incidentBeginDate": "2020-01-20T00:00:00.000Z", "incidentEndDate": "2023-05-11T00:00:00.000Z", "disasterCloseoutDate": None,
            "tribalRequest": False, "fipsStateCode": "20" if state == "KS" else "31", "fipsCountyCode": county, "placeCode": "99" + county,
            "designatedArea": area, "declarationRequestNumber": "20101", "declarationRequestDate": "2020-03-26T00:00:00.000Z",
            "lastIAFilingDate": None, "incidentId": "2020030901", "region": 7, "designatedIncidentTypes": None,
            "lastRefresh": "2026-10-05T11:26:24.661Z", "hash": "ad575ca107cf978d9041456e8275a0723c2f5653", "id": uid}


def claim(cid, county="20043", state="KS", paid=1250.5):
    return {"id": cid, "asOfDate": "2026-09-08T00:00:00.000Z", "dateOfLoss": "2011-06-28T00:00:00.000Z", "yearOfLoss": 2011, "state": state,
            "reportedCity": "Currently Unavailable", "reportedZipCode": "66024", "countyCode": county, "censusGeoid": (county or "") + "0201001",
            "latitude": 39.8, "longitude": -95.1, "nfipCommunityNumberCurrent": "200078", "floodEvent": None, "causeOfDamage": "4",
            "amountPaidOnBuildingClaim": paid, "amountPaidOnContentsClaim": 0.0, "amountPaidOnIncreasedCostOfComplianceClaim": 0.0,
            "buildingDamageAmount": 1800, "contentsDamageAmount": None}


UUIDS = ["000dafac-f1e9-40f2-bb56-e88d2c24b7f9", "1a7e0c55-1111-4c2e-9d0e-2b6f0e8f5a10", "5c9e2a01-2222-4f5b-8a3d-7c1e9b0d4e21",
         "9bac603d-7ab9-4a45-9839-92cee009da67", "fe8d8a3a-7fcb-4a3e-9e2c-1b1c0f2b6b1a"]


class FakeFema:
    """OpenFEMA's dataset list and paged, filtered, key-ordered dataset endpoints."""

    def __init__(self):
        self.data = {"DisasterDeclarationsSummaries": [declaration(UUIDS[3], "195"), declaration(UUIDS[0], "097", area="Kiowa (County)"),
                                                       declaration(UUIDS[1], "000", area="Statewide"), declaration(UUIDS[2], "055", state="NE"),
                                                       declaration(UUIDS[4], "015", area="Butler (County)")],
                     "NfipClaims": [claim(5449304), claim(5449301, county=None), claim(6000000, state="MO", county="29095")]}
        self.listing = {"DisasterDeclarationsSummaries": {"version": 2, "accrualPeriodicity": "R/PT20M", "lastDataSetRefresh": "2026-11-04T14:47:50Z"},
                        "NfipClaims": {"version": 3, "accrualPeriodicity": "R/P1M", "lastDataSetRefresh": "2026-09-09T16:23:10Z"}}
        self.ignore_filter, self.shift, self.fail_after = False, 0, None

    def __call__(self, url):
        if url == fe.LISTING:
            return json.dumps({"metadata": {}, "OpenFemaDataSets": [{"name": n, **m} for n, m in self.listing.items()]}).encode()
        parts = urllib.parse.urlsplit(url)
        name = parts.path.rsplit("/", 1)[1]
        query = {k: urllib.parse.unquote(v) for k, v in (p.split("=", 1) for p in parts.query.split("&"))}
        ds, where = DS[name], query["$filter"]
        records = sorted((r for r in self.data[name] if self.ignore_filter or ds.is_kansas(r)), key=lambda r: r[ds.key])
        count = len(records) + self.shift
        if where != ds.kansas:
            prefix = f"({ds.kansas}) and {ds.key} gt "
            assert where.startswith(prefix) and "$inlinecount" not in query, url
            last = where[len(prefix):]
            records = [r for r in records if r[ds.key] > (int(last) if last.isdigit() else last.strip("'"))]
            if self.fail_after is not None:
                raise core.FeedError("HTTP_503 " + url)
        assert query["$orderby"] == ds.key
        return json.dumps({"metadata": {"count": count if "$inlinecount" in query else 0}, name: records[:int(query["$top"])]}).encode()


class FemaTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.fake = FakeFema()
        self.web.routes = {fe.API: self.fake}
        page = patch.object(fe, "PAGE", 2)
        page.start()
        self.addCleanup(page.stop)

    def run_feed(self, datasets=(DDS, CLAIMS)):
        return fe.fema(self.ctx, datasets=datasets)

    def temp_files(self):
        return list((self.root / "tmp-sql-feeds").glob("*")) if (self.root / "tmp-sql-feeds").exists() else []

    def test_kansas_records_are_paged_by_key_and_kept_whole(self):
        result = self.run_feed()
        self.assertEqual((result["DisasterDeclarationsSummaries"], result["NfipClaims"], result["rows"]), ("loaded 4", "loaded 2", 6))
        self.assertEqual(self.q("SELECT id, county_geoid, designated_area FROM kfm_fema_disaster_declarations ORDER BY row_number"),
                         [(UUIDS[0], "20097", "Kiowa (County)"), (UUIDS[1], None, "Statewide"), (UUIDS[3], "20195", "Trego (County)"),
                          (UUIDS[4], "20015", "Butler (County)")])
        self.assertEqual(self.q("SELECT id, county_geoid, amount_paid_on_building_claim, typeof(id) FROM kfm_fema_nfip_claims ORDER BY id"),
                         [(5449301, None, 1250.5, "integer"), (5449304, "20043", 1250.5, "integer")])
        record = json.loads(self.q("SELECT record_json FROM kfm_fema_nfip_claims WHERE id=5449304")[0][0])
        self.assertEqual(record, claim(5449304))
        dds_pages = [u for u in self.web.calls if "/v2/DisasterDeclarationsSummaries" in u]
        self.assertEqual(len(dds_pages), 3)
        self.assertIn("$inlinecount=allpages", dds_pages[0])
        self.assertIn(urllib.parse.quote(f"(state eq 'KS') and id gt '{UUIDS[1]}'", safe=""), dds_pages[1])
        receipt = json.loads(self.q("SELECT receipt_json FROM kfm_sql_sources WHERE source_id='openfema-NfipClaims'")[0][0])
        self.assertEqual((receipt["key"], receipt["records"], receipt["version"], receipt["dataset_refresh"]),
                         ("NfipClaims", 2, "v3", "2026-09-09T16:23:10Z"))
        self.assertEqual(self.temp_files(), [])

    def test_a_rerun_waits_for_a_refresh_and_an_identical_extract_is_not_loaded_again(self):
        self.run_feed()
        self.web.calls.clear()
        self.assertEqual(self.run_feed()["DisasterDeclarationsSummaries"], "not_due")
        self.assertEqual(self.web.calls, [fe.LISTING])
        # FEMA refreshed every 20 minutes; the next day's extract has the same Kansas records.
        self.ctx.now, self.fake.listing["DisasterDeclarationsSummaries"]["lastDataSetRefresh"] = at(2026, 11, 5), "2026-11-05T14:47:50Z"
        result = self.run_feed()
        self.assertEqual((result["DisasterDeclarationsSummaries"], result["NfipClaims"], result["rows"]), ("unchanged 4", "not_due", 0))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(2,)])

    def test_a_changed_extract_replaces_the_old_one_and_a_return_to_it_is_reinstated(self):
        self.run_feed()
        original = self.fake.data["DisasterDeclarationsSummaries"]
        changed = [*original[:-1], declaration(UUIDS[4], "015", area="Butler (County)", title="SEVERE STORMS")]
        for day, records, state in ((5, changed, "loaded"), (6, original, "reinstated")):
            self.ctx.now = at(2026, 11, day)
            self.fake.data["DisasterDeclarationsSummaries"] = records
            self.fake.listing["DisasterDeclarationsSummaries"]["lastDataSetRefresh"] = f"2026-11-{day:02d}T14:47:50Z"
            self.assertEqual(self.run_feed()["DisasterDeclarationsSummaries"], f"{state} 4")
            self.assertEqual(self.q("SELECT COUNT(*), COUNT(DISTINCT file_id) FROM kfm_fema_disaster_declarations"), [(4, 1)])
        self.assertEqual(self.q("SELECT declaration_title FROM kfm_fema_disaster_declarations WHERE id=?", UUIDS[4]), [("COVID-19 PANDEMIC",)])
        self.assertEqual(self.q("SELECT file_id, state FROM kfm_sql_sources WHERE source_id LIKE '%Declarations%' ORDER BY file_id"),
                         [(1, "complete"), (3, "superseded")])

    def test_the_cadence_follows_the_datasets_periodicity(self):
        self.assertEqual([fe.gap_days(p) for p in ("R/PT20M", "R/P1D", "R/P1W", "R/P1M", "R/P3M", "R/P1Y", "irregular", None)],
                         [1, 1, 6, 25, 75, 330, 1, 1])
        self.run_feed()
        self.fake.listing["NfipClaims"]["lastDataSetRefresh"] = "2026-11-10T16:23:10Z"
        self.fake.data["NfipClaims"].append(claim(7000000, county="20045"))
        self.ctx.now = at(2026, 11, 20)
        self.assertEqual(self.run_feed()["NfipClaims"], "not_due")
        self.ctx.now = at(2026, 11, 29)
        self.assertEqual(self.run_feed()["NfipClaims"], "loaded 3")

    def test_changed_fields_and_unexpected_extracts_stop_without_loading(self):
        del self.fake.data["NfipClaims"][0]["countyCode"]
        with self.assertRaisesRegex(core.FeedError, "FEMA_COLUMNS_CHANGED NfipClaims"):
            self.run_feed((CLAIMS,))
        self.fake.data["NfipClaims"][0]["countyCode"] = "20043"
        self.fake.ignore_filter = True
        with self.assertRaisesRegex(core.FeedError, "FEMA_NOT_KANSAS NfipClaims 6000000"):
            self.run_feed((CLAIMS,))
        self.fake.ignore_filter, self.fake.shift = False, 1
        with self.assertRaisesRegex(core.FeedError, "FEMA_EXTRACT_SHIFTED NfipClaims 2 of 3"):
            self.run_feed((CLAIMS,))
        self.fake.shift = 0
        with patch.object(fe, "MAX_RECORDS", 1), self.assertRaisesRegex(core.FeedError, "FEMA_EXTRACT_TOO_LARGE"):
            self.run_feed((CLAIMS,))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertEqual(self.temp_files(), [])

    def test_a_failure_part_way_leaves_no_rows_and_no_temp_file(self):
        self.fake.fail_after = 1
        with self.assertRaisesRegex(core.FeedError, "HTTP_503"):
            self.run_feed((DDS,))
        self.fake.fail_after = None
        real = fe.rows

        def failing(path, ds):
            for n, row in enumerate(real(path, ds)):
                if n == 2:
                    raise core.FeedError("TEST_INTERRUPTED")
                yield row
        with patch.object(fe, "rows", failing), self.assertRaisesRegex(core.FeedError, "TEST_INTERRUPTED"):
            self.run_feed((DDS,))
        self.assertEqual(self.q("SELECT (SELECT COUNT(*) FROM kfm_fema_disaster_declarations), (SELECT COUNT(*) FROM kfm_sql_sources)"), [(0, 0)])
        self.assertEqual(self.temp_files(), [])
        self.assertEqual(self.run_feed((DDS,))["DisasterDeclarationsSummaries"], "loaded 4")

    def test_a_retired_dataset_stops_the_run_after_the_others_and_a_planned_one_is_reported(self):
        self.fake.listing["DisasterDeclarationsSummaries"]["depDate"] = "2027-03-01T00:00:00.000Z"
        self.fake.listing["NfipClaims"]["version"] = 4
        with self.assertRaisesRegex(core.FeedError, "^FEMA_DATASET_RETIRED NfipClaims/v3$"):
            self.run_feed()
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_fema_disaster_declarations"), [(4,)])
        self.ctx.now, self.fake.listing["NfipClaims"]["version"] = at(2026, 11, 5), 3
        self.assertEqual(self.run_feed()["retiring"], {"DisasterDeclarationsSummaries": "2027-03-01T00:00:00.000Z"})
        # FEMA serving no Kansas records where there were some is not taken as a deletion.
        self.ctx.now, self.fake.data["NfipClaims"] = at(2026, 12, 5), []
        self.fake.listing["NfipClaims"]["lastDataSetRefresh"] = "2026-12-01T00:00:00Z"
        with self.assertRaisesRegex(core.FeedError, "FEMA_KANSAS_EMPTY NfipClaims"):
            self.run_feed()
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_fema_nfip_claims"), [(2,)])


if __name__ == "__main__":
    unittest.main()
