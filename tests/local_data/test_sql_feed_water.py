"""SQL feeds for Kansas water (USGS daily values, peaks, field measurements; Water Quality Portal), without network access."""
import csv
from datetime import datetime, timezone
import gzip
import io
import json
import urllib.parse
from unittest.mock import patch
import zipfile

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_water as w, sql_feeds as core

DAILY_HEADER = ["x", "y", "time_series_id", "monitoring_location_id", "parameter_code", "statistic_id", "time", "value", "unit_of_measure",
                "approval_status", "qualifier", "last_modified"]
META_HEADER = ("x,y,monitoring_location_id,agency_code,agency_name,monitoring_location_number,monitoring_location_name,district_code,country_code,"
               "country_name,state_code,state_name,county_code,county_name,minor_civil_division_code,site_type_code,site_type,hydrologic_unit_code,"
               "basin_code,altitude,altitude_accuracy,altitude_method_code,altitude_method_name,vertical_datum,vertical_datum_name,"
               "horizontal_positional_accuracy_code,horizontal_positional_accuracy,horizontal_position_method_code,horizontal_position_method_name,"
               "original_horizontal_datum,original_horizontal_datum_name,drainage_area,contributing_drainage_area,time_zone_abbreviation,"
               "uses_daylight_savings,construction_date,aquifer_code,national_aquifer_code,aquifer_type_code,well_constructed_depth,"
               "hole_constructed_depth,depth_source_code,id,unit_of_measure,parameter_name,parameter_code,statistic_id,last_modified,begin,end,"
               "data_type,computation_identifier,thresholds,sublocation_identifier,primary,web_description,parameter_description,"
               "parent_time_series_id,data_gap_interval,reading_type").split(",")
PEAK_HEADER = ["x", "y", "time_series_id", "monitoring_location_id", "parameter_code", "unit_of_measure", "value", "last_modified", "time",
               "water_year", "year", "month", "day", "time_of_day", "peak_since", "qualifier"]
GW_HEADER = ["x", "y", "field_measurements_series_id", "reading_type", "field_visit_id", "parameter_code", "monitoring_location_id",
             "observing_procedure_code", "observing_procedure", "value", "unit_of_measure", "time", "qualifier", "vertical_datum", "approval_status",
             "measuring_agency", "last_modified", "control_condition", "measurement_rated", "year", "month", "day", "time_of_day",
             "sublocation_identifier"]
DESOTO, SEDGWICK = "USGS-06892350", "USGS-07144100"
Q_DESOTO, H_SEDGWICK, PEAK_DESOTO = "7d898ff87de840fa928562c5b9a5a2bd", "d6cc5e7798b04045964a595f7256317a", "0f3e0aa1a0a94b4f8a6c1e5f2b7d9c11"


def qs(url):
    return {k: v[0] for k, v in urllib.parse.parse_qs(urllib.parse.urlsplit(url).query).items()}


def table(header, rows) -> bytes:
    out = io.StringIO()
    csv.writer(out, lineterminator="\n").writerows([header, *rows])
    return out.getvalue().encode()


def ogc(header, rows) -> bytes:
    """An OGC API CSV answer: a query with no rows is an empty body, without a header (as the real API answers)."""
    return table(header, rows) if rows else b""


def meta_row(site, series, parameter, statistic, data_type, name, x, y):
    row = dict.fromkeys(META_HEADER, "")
    row.update(x=x, y=y, monitoring_location_id=site, agency_code="USGS", agency_name="U.S. Geological Survey", monitoring_location_number=site[5:],
               monitoring_location_name=name, district_code="20", country_code="US", state_code="20", state_name="Kansas", county_code="103",
               county_name="Leavenworth County", site_type_code="ST", site_type="Stream", hydrologic_unit_code="10270104", drainage_area="59756",
               id=series, unit_of_measure="ft^3/s", parameter_code=parameter, statistic_id=statistic, data_type=data_type,
               begin="1917-07-08 06:00:00+00:00", end="2026-10-31 05:00:00+00:00", primary="Primary", thresholds="[]",
               last_modified="2026-11-02 06:49:13.637742+00:00")
    return [row[c] for c in META_HEADER]


METADATA = table(META_HEADER, [
    meta_row(DESOTO, Q_DESOTO, "00060", "00003", "Daily values", "KANSAS R AT DESOTO, KS", "-94.9646893327574", "38.9833375194952"),
    meta_row(SEDGWICK, H_SEDGWICK, "00065", "00003", "Daily values", "L ARKANSAS R NR SEDGWICK, KS", "-97.4244863910926", "37.8830673894379"),
    meta_row(DESOTO, PEAK_DESOTO, "00060", "", "Peaks", "KANSAS R AT DESOTO, KS", "-94.9646893327574", "38.9833375194952")])


def value(series, site, day, val, approval="Approved", qualifier="", modified="2025-03-11 04:57:51.423987+00:00", parameter="00060"):
    return ["", "", series, site, parameter, "00003", day, val, "ft^3/s", approval, qualifier, modified]


class DailyTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.ctx.pause = 0
        self.records = {Q_DESOTO: [value(Q_DESOTO, DESOTO, "1917-07-08", "2240"), value(Q_DESOTO, DESOTO, "1917-07-09", "2100", qualifier="ESTIMATED"),
                                   value(Q_DESOTO, DESOTO, "2026-11-03", "3120", approval="Provisional", modified="2026-11-04 05:00:00.000000+00:00")],
                        H_SEDGWICK: [value(H_SEDGWICK, SEDGWICK, "2026-11-03", "3.10", approval="Provisional", qualifier="ICE", parameter="00065")]}
        self.modified = []   # rows the statewide last_modified query can return
        self.web.routes = {w.OGC + "combined-metadata/items?": self.metadata, w.OGC + "daily/items?": self.daily}

    def metadata(self, url):
        q = qs(url)
        self.assertEqual((q["state_code"], q["data_type"], q["f"]), ("20", "Daily values,Peaks", "csv"))
        return METADATA

    def daily(self, url):
        q = qs(url)
        if "time_series_id" in q:
            first, last = q["time"].split("/")
            return ogc(DAILY_HEADER, [r for r in self.records[q["time_series_id"]] if first <= r[6] <= last][:w.PAGE])
        self.assertEqual(q["state_code"], "20")
        lo, hi = (datetime.strptime(t, w.STAMP).replace(tzinfo=timezone.utc) for t in q["last_modified"].split("/"))
        first, _, last = q.get("time", "../..").partition("/")
        rows = [r for r in self.modified if lo <= datetime.fromisoformat(r[11]) <= hi
                and (first in ("..", "") or r[6] >= first) and (last in ("..", "") or r[6] <= last)]
        # The API pages rows in record-UUID order, which is unrelated to time.
        return ogc(DAILY_HEADER, sorted(rows, key=lambda r: core.sha256((r[2] + r[6]).encode()))[:w.PAGE])

    def values(self):
        return self.q("SELECT time_series_id, time, value, approval_status, qualifier FROM kfm_usgs_daily_values ORDER BY 1, 2")

    def test_records_backfill_at_the_cap_then_modifications_revise_without_duplicates(self):
        first = w.usgs_daily(self.ctx, max_records=1)
        self.assertEqual((first["metadata"]["series"], first["metadata"]["sites"], first["metadata"]["site_rows"]), ("loaded", "loaded", 1 + 1))
        self.assertEqual((first["records"], first["record_rows"], first["backfill_pending"]), (1, 3, 1))
        self.assertEqual(self.q("SELECT site_no, name, longitude, county_code FROM kfm_usgs_sites ORDER BY site_no"),
                         [("06892350", "KANSAS R AT DESOTO, KS", -94.9646893327574, "103"),
                          ("07144100", "L ARKANSAS R NR SEDGWICK, KS", -97.4244863910926, "103")])
        self.assertEqual(self.q("SELECT data_type, COUNT(*) FROM kfm_usgs_series GROUP BY 1 ORDER BY 1"), [("Daily values", 2), ("Peaks", 1)])
        self.assertTrue(all(qs(u).get("state_code") == "20" or qs(u).get("time_series_id") in self.records for u in self.web.calls))
        self.assertEqual({qs(u)["time"] for u in self.web.calls if "time_series_id=" in u}, {"1800-01-01/2026-11-05"})
        # Next run: USGS approved yesterday's value and added a day; the second series' record is backfilled.
        self.modified = [value(Q_DESOTO, DESOTO, "2026-11-03", "3100", modified="2026-11-04 12:00:00.000000+00:00"),
                         value(Q_DESOTO, DESOTO, "2026-11-04", "3050", approval="Provisional", modified="2026-11-04 12:00:00.000000+00:00")]
        second = w.usgs_daily(self.ctx, max_records=1)
        self.assertEqual((second["metadata"], second["modified_files"], second["modified_rows"], second["records"], second["backfill_pending"]),
                         (None, 1, 2, 1, 0))
        self.assertEqual(self.values(), [(Q_DESOTO, "1917-07-08", "2240", "Approved", None), (Q_DESOTO, "1917-07-09", "2100", "Approved", "ESTIMATED"),
                                         (Q_DESOTO, "2026-11-03", "3100", "Approved", None), (Q_DESOTO, "2026-11-04", "3050", "Provisional", None),
                                         (H_SEDGWICK, "2026-11-03", "3.10", "Provisional", "ICE")])
        window = qs([u for u in self.web.calls if "&last_modified=" in u][0])["last_modified"]
        self.assertEqual(window, "2026-11-03T15:00:00.000000Z/2026-11-04T15:00:00.000000Z", "a day of overlap with the last window")
        # A rerun: the same modifications and unchanged records load nothing new.
        third = w.usgs_daily(self.ctx)
        self.assertEqual((third["modified_files"], third["records"], third["records_unchanged"]), (0, 2, 2))
        self.assertEqual(len(self.values()), 5)

    def test_a_record_a_modification_window_already_loaded_still_counts_as_read(self):
        w.usgs_daily(self.ctx, max_records=1)   # metadata, then DeSoto's record
        row = value(H_SEDGWICK, SEDGWICK, "2026-11-03", "3.10", approval="Provisional", qualifier="ICE", parameter="00065",
                    modified="2026-11-04 05:00:00.000000+00:00")
        self.records[H_SEDGWICK], self.modified = [row], [row]
        # The window brings Sedgwick's only value, so its full record is the same bytes and registers no source.
        second = w.usgs_daily(self.ctx, max_records=1)
        self.assertEqual((second["modified_files"], second["records"], second["records_unchanged"]), (1, 1, 1))
        third = w.usgs_daily(self.ctx, max_records=1)
        self.assertEqual((third["backfill_pending"], third["records_unchanged"]), (0, 1))
        state = json.loads(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='usgs-daily'")[0][0])
        self.assertIn("rotation_after", state, "the backfill ended, so the third run rotates instead of reading Sedgwick again")
        self.assertEqual((state.get("records_read"), state["rotation_after"]), ([H_SEDGWICK], min(Q_DESOTO, H_SEDGWICK)))

    def test_a_reread_record_replaces_its_series_and_drops_days_usgs_removed(self):
        w.usgs_daily(self.ctx)
        self.records[Q_DESOTO] = [value(Q_DESOTO, DESOTO, "1917-07-08", "2240"),
                                  value(Q_DESOTO, DESOTO, "2026-11-03", "3100", modified="2026-11-05 05:00:00.000000+00:00")]
        result = w.usgs_daily(self.ctx)
        self.assertEqual((result["records"], result["rows_dropped"], result["records_unchanged"]), (2, 1, 1))
        self.assertEqual([r[:3] for r in self.values() if r[0] == Q_DESOTO], [(Q_DESOTO, "1917-07-08", "2240"), (Q_DESOTO, "2026-11-03", "3100")])
        states = self.q("SELECT state FROM kfm_sql_sources WHERE source_id='usgs-daily-record' AND receipt_json LIKE ? ORDER BY file_id", f"%{Q_DESOTO}%")
        self.assertEqual(states, [("superseded",), ("complete",)])

    def test_a_full_modification_page_is_cut_and_carried_to_the_next_run(self):
        w.usgs_daily(self.ctx)
        self.modified = [value(Q_DESOTO, DESOTO, f"2026-10-{d:02d}", str(d), modified=f"2026-11-04 0{d % 9}:00:00.000000+00:00") for d in range(1, 11)]
        self.modified += [value(H_SEDGWICK, SEDGWICK, f"2026-10-{d:02d}", str(d), parameter="00065", modified="2026-11-04 09:30:00.000000+00:00")
                          for d in range(1, 6)]
        for row in self.modified:   # USGS's records hold what it modified: a record read again agrees
            self.records[row[2]].append(row)
        with patch.object(w, "PAGE", 3):
            partial = w.usgs_daily(self.ctx, max_modified_requests=3)
            self.assertGreater(partial["modified_pending"], 0)
            db = core.open_db(self.ctx)
            self.assertEqual(core.get_state(db, "usgs-daily")["modified_through"], "2026-11-04T15:00:00.000000Z", "not moved while windows wait")
            db.close()
            for _ in range(20):
                if not w.usgs_daily(self.ctx, max_modified_requests=3)["modified_pending"]:
                    break
        windows = [qs(u) for u in self.web.calls if "&last_modified=" in u]
        self.assertTrue(any("time" in q for q in windows), "the five values modified at one instant were cut by day")
        self.assertGreater(len({q["last_modified"] for q in windows}), 4, "the window was cut at its quartiles")
        got = {(t, d): v for t, d, v, _, _ in self.values()}
        self.assertTrue(all(got[(r[2], r[6])] == r[7] for r in self.modified), "every modified value arrived, the one-instant group cut by day")
        self.assertEqual(len(got), len({(t, d) for t, d, *_ in self.values()}))

    def test_a_changed_header_or_rate_limit_stops_the_feed(self):
        broken = table([c for c in META_HEADER if c != "parameter_code"], [])
        self.web.routes[w.OGC + "combined-metadata/items?"] = broken
        with self.assertRaisesRegex(core.FeedError, "USGS_METADATA_COLUMNS_CHANGED missing parameter_code"):
            w.usgs_daily(self.ctx)
        self.web.routes[w.OGC + "combined-metadata/items?"] = self.metadata
        self.records[Q_DESOTO] = [r[:10] + r[11:] for r in self.records[Q_DESOTO]]
        self.web.routes[w.OGC + "daily/items?"] = lambda url: table([c for c in DAILY_HEADER if c != "qualifier"], self.records[Q_DESOTO])
        with self.assertRaisesRegex(core.FeedError, "USGS_DAILY_COLUMNS_CHANGED missing qualifier"):
            w.usgs_daily(self.ctx)

        def limited(url):
            raise core.FeedError("HTTP_429 " + url)
        self.web.routes[w.OGC + "daily/items?"] = limited
        with self.assertRaisesRegex(core.FeedError, "USGS_RATE_LIMITED"):
            w.usgs_daily(self.ctx)

    def test_a_failure_part_way_leaves_no_rows(self):
        with patch.object(core, "finish_source", side_effect=RuntimeError("disk")), self.assertRaises(RuntimeError):
            w.usgs_daily(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usgs_daily_values"), [(0,)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE source_id LIKE 'usgs-daily%'"), [(0,)])
        self.assertEqual(w.usgs_daily(self.ctx)["record_rows"], 4, "the next run loads the records")


class PeaksTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.ctx.pause = 0
        self.rows = [["-94.96", "38.98", PEAK_DESOTO, DESOTO, "00060", "ft^3/s", "510000", "2026-05-01 20:12:19+00:00", "1951-07-13", "1951", "1951", "7", "13",
                      "", "1844", "HISTORIC"],
                     ["-94.96", "38.98", PEAK_DESOTO, DESOTO, "00060", "ft^3/s", "0.00", "2026-05-01 20:12:19+00:00", "1963-01-01", "1963", "1963", "", "",
                      "", "", "MONTHUNKNOWN"]]
        self.web.routes = {w.OGC + "peaks/items?": self.peaks}

    def peaks(self, url):
        q = qs(url)
        self.assertEqual((q["state_code"], q["time"]), ("20", f"1800-01-01/{self.ctx.now().date()}"))
        return ogc(PEAK_HEADER, self.rows)

    def test_statewide_peaks_load_monthly_and_a_changed_answer_replaces_the_last(self):
        first = w.usgs_peaks(self.ctx)
        self.assertEqual((first["state"], first["rows"], first["sites"]), ("loaded", 2, 1))
        self.assertEqual(self.q("SELECT water_year, typeof(water_year), month, peak_since, qualifier, longitude FROM kfm_usgs_peaks ORDER BY row_number"),
                         [(1951, "integer", "7", "1844", "HISTORIC", -94.96), (1963, "integer", None, None, "MONTHUNKNOWN", -94.96)])
        self.assertEqual(w.usgs_peaks(self.ctx)["state"], "not_due")
        self.ctx.now = lambda: datetime(2026, 12, 5, 15, 0, tzinfo=timezone.utc)
        self.assertEqual(w.usgs_peaks(self.ctx)["state"], "unchanged")
        self.ctx.now = lambda: datetime(2027, 1, 5, 15, 0, tzinfo=timezone.utc)
        self.rows.append(["-94.96", "38.98", PEAK_DESOTO, DESOTO, "00060", "ft^3/s", "61200", "2026-12-20 10:00:00+00:00", "2026-06-01", "2026", "2026",
                          "6", "1", "", "", ""])
        self.assertEqual({k: v for k, v in w.usgs_peaks(self.ctx).items() if k in ("state", "rows", "superseded")},
                         {"state": "loaded", "rows": 3, "superseded": 1})
        self.assertEqual(self.q("SELECT COUNT(*), COUNT(DISTINCT file_id) FROM kfm_usgs_peaks"), [(3, 1)])
        receipt = json.loads(next((self.root / "data/receipts/ingest/sql-feeds/usgs-peaks").rglob("*.json")).read_text())
        self.assertEqual(receipt["key"], "peaks/kansas")

    def test_a_changed_header_stops_and_a_failed_load_leaves_nothing(self):
        self.web.routes[w.OGC + "peaks/items?"] = table([c for c in PEAK_HEADER if c != "water_year"], [])
        with self.assertRaisesRegex(core.FeedError, "USGS_PEAKS_COLUMNS_CHANGED"):
            w.usgs_peaks(self.ctx)
        self.web.routes[w.OGC + "peaks/items?"] = self.peaks
        with patch.object(core, "finish_source", side_effect=RuntimeError("disk")), self.assertRaises(RuntimeError):
            w.usgs_peaks(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usgs_peaks"), [(0,)])
        self.assertEqual(w.usgs_peaks(self.ctx)["state"], "loaded", "a failed run is not marked checked")


def gw(year, parameter, reading_type="ReferencePrimary", val="868.60", site="USGS-390519095445301", visit="f63f7a8f", modified="2026-10-24 09:34:13+00:00"):
    return ["-95.748", "39.088", f"{site}-{parameter}", reading_type, visit, parameter, site, "S", "GW level, steel tape", val, "ft", f"{year}-01-30",
            "Static", "NAVD88", "Approved", "", modified, "", "", str(year), "1", "30", "", ""]


class GroundwaterTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.ctx.pause = 0
        self.years = {2023: [gw(2023, "72019", val="41.20"), gw(2023, "62611"), gw(2023, "00060", "Discharge", "12.0", "USGS-06892350"),
                             gw(2023, "00065", "MeanGageHeight", "3.1", "USGS-06892350"), gw(2023, "62614", val="1072.4", site="USGS-06857050")],
                      2025: [gw(2025, "72019", val="44.75")], 2026: [gw(2026, "72019", val="45.10")]}
        self.modified = []
        self.web.routes = {w.OGC + "field-measurements/items?": self.measurements}

    def measurements(self, url):
        q = qs(url)
        self.assertEqual(q["state_code"], "20")
        if "last_modified" in q:
            return ogc(["x", "y", "time", "last_modified"], [["", "", t, "2026-11-04 10:00:00+00:00"] for t in self.modified])
        first, last = q["time"].split("/")
        rows = [r for rows in self.years.values() for r in rows if first <= r[11] <= last]
        return ogc(GW_HEADER, rows[:w.PAGE])

    def test_years_backfill_at_the_cap_and_changed_years_are_fetched_again(self):
        with patch.object(w, "GW_FIRST_YEAR", 2023):
            first = w.usgs_groundwater(self.ctx, max_years=2)
            self.assertEqual((first["years"], first["rows"], first["next_year"], first["backfill_pending"]), ([2023, 2024], 5, 2025, 2))
            self.assertEqual(self.q("SELECT kind, parameter_code FROM kfm_usgs_field_measurements ORDER BY row_number"),
                             [("groundwater_level", "72019"), ("groundwater_level", "62611"), ("discharge", "00060"), ("gage_height", "00065"),
                              ("other", "62614")])
            self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE receipt_json LIKE '%year/2024%'"), [(0,)], "an empty year is only state")
            # USGS revises a 2023 reading: the probe names 2023, which is fetched again before the backfill goes on.
            self.years[2023][0][9], self.modified = "41.25", ["2023-01-30"]
            second = w.usgs_groundwater(self.ctx, max_years=3)
            self.assertEqual((second["changed_years"], second["years"], second["next_year"]), ([2023], [2023, 2025, 2026], 2027))
            self.assertEqual(self.q("SELECT value FROM kfm_usgs_field_measurements WHERE parameter_code='72019' ORDER BY time"),
                             [("41.25",), ("44.75",), ("45.10",)])
            self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources WHERE source_id='usgs-field-measurements' GROUP BY 1 ORDER BY 1"),
                             [("complete", 3), ("superseded", 1)])
            self.modified = []
            third = w.usgs_groundwater(self.ctx)
            self.assertEqual((third["years"], third["rows"]), ([], 0), "a rerun with nothing changed fetches nothing")

    def test_a_year_that_fills_a_page_is_fetched_in_halves(self):
        self.years[2023] += [gw(2023, "72019", val=str(n), visit=f"v{n}") for n in range(4)]
        for row in self.years[2023][-4:]:
            row[11] = "2023-08-30"
        with patch.object(w, "GW_FIRST_YEAR", 2023), patch.object(w, "PAGE", 6):
            result = w.usgs_groundwater(self.ctx, max_years=1)
        self.assertEqual(result["rows"], 9)
        receipt = json.loads(next((self.root / "data/receipts/ingest/sql-feeds/usgs-groundwater").rglob("*.json")).read_text())
        self.assertEqual((receipt["rows"], receipt["requests"]), (9, 3))   # the full page, then its two halves

    def test_a_changed_header_stops_and_a_failed_load_leaves_nothing(self):
        self.web.routes[w.OGC + "field-measurements/items?"] = table([c for c in GW_HEADER if c != "field_visit_id"], [])
        with patch.object(w, "GW_FIRST_YEAR", 2023), self.assertRaisesRegex(core.FeedError, "USGS_GW_COLUMNS_CHANGED missing field_visit_id"):
            w.usgs_groundwater(self.ctx)
        self.web.routes[w.OGC + "field-measurements/items?"] = self.measurements
        with patch.object(w, "GW_FIRST_YEAR", 2023), patch.object(core, "finish_source", side_effect=RuntimeError("disk")), \
                self.assertRaises(RuntimeError):
            w.usgs_groundwater(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usgs_field_measurements"), [(0,)])


WQP_HEADER = ("OrganizationIdentifier,OrganizationFormalName,ActivityIdentifier,ActivityTypeCode,ActivityMediaName,ActivityMediaSubdivisionName,"
              "ActivityStartDate,ActivityStartTime/Time,ActivityStartTime/TimeZoneCode,ActivityEndDate,ActivityEndTime/Time,ActivityEndTime/TimeZoneCode,"
              "ActivityDepthHeightMeasure/MeasureValue,ActivityDepthHeightMeasure/MeasureUnitCode,ActivityDepthAltitudeReferencePointText,"
              "ActivityTopDepthHeightMeasure/MeasureValue,ActivityTopDepthHeightMeasure/MeasureUnitCode,ActivityBottomDepthHeightMeasure/MeasureValue,"
              "ActivityBottomDepthHeightMeasure/MeasureUnitCode,ProjectIdentifier,ActivityConductingOrganizationText,MonitoringLocationIdentifier,"
              "ActivityCommentText,SampleAquifer,HydrologicCondition,HydrologicEvent,SampleCollectionMethod/MethodIdentifier,"
              "SampleCollectionMethod/MethodIdentifierContext,SampleCollectionMethod/MethodName,SampleCollectionEquipmentName,"
              "ResultDetectionConditionText,CharacteristicName,ResultSampleFractionText,ResultMeasureValue,ResultMeasure/MeasureUnitCode,"
              "MeasureQualifierCode,ResultStatusIdentifier,StatisticalBaseCode,ResultValueTypeName,ResultWeightBasisText,ResultTimeBasisText,"
              "ResultTemperatureBasisText,ResultParticleSizeBasisText,PrecisionValue,ResultCommentText,USGSPCode,ResultDepthHeightMeasure/MeasureValue,"
              "ResultDepthHeightMeasure/MeasureUnitCode,ResultDepthAltitudeReferencePointText,SubjectTaxonomicName,SampleTissueAnatomyName,"
              "ResultAnalyticalMethod/MethodIdentifier,ResultAnalyticalMethod/MethodIdentifierContext,ResultAnalyticalMethod/MethodName,"
              "MethodDescriptionText,LaboratoryName,AnalysisStartDate,ResultLaboratoryCommentText,DetectionQuantitationLimitTypeName,"
              "DetectionQuantitationLimitMeasure/MeasureValue,DetectionQuantitationLimitMeasure/MeasureUnitCode,PreparationStartDate,ProviderName").split(",")
STATION_HEADER = [p for p, _ in w.WQP_STATION_COLUMNS]


def wqp(day, characteristic, val, *, org="USGS-KS", site="USGS-07144100", detection="", limit="", comment=""):
    row = dict.fromkeys(WQP_HEADER, "")
    row.update({"OrganizationIdentifier": org, "ActivityIdentifier": f"nwisks.01.{day}", "ActivityTypeCode": "Sample-Routine", "ActivityMediaName": "Water",
                "ActivityStartDate": day, "ActivityStartTime/Time": "12:20:00", "ActivityStartTime/TimeZoneCode": "CST", "MonitoringLocationIdentifier": site,
                "ActivityCommentText": comment, "CharacteristicName": characteristic, "ResultSampleFractionText": "Dissolved", "ResultMeasureValue": val,
                "ResultMeasure/MeasureUnitCode": "mg/l", "ResultStatusIdentifier": "Accepted", "ResultValueTypeName": "Actual", "USGSPCode": "00631",
                "ResultDetectionConditionText": detection, "DetectionQuantitationLimitTypeName": "Lower Reporting Limit" if limit else "",
                "DetectionQuantitationLimitMeasure/MeasureValue": limit, "DetectionQuantitationLimitMeasure/MeasureUnitCode": "mg/l" if limit else "",
                "ProviderName": "NWIS"})
    return [row[c] for c in WQP_HEADER]


def zipped(name, header, rows) -> bytes:
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(name, table(header, rows))
    return out.getvalue()


class WaterQualityTests(FeedCase):
    def setUp(self):
        super().setUp()
        station = dict.fromkeys(STATION_HEADER, "")
        station.update({"OrganizationIdentifier": "USGS-KS", "MonitoringLocationIdentifier": "USGS-07144100",
                        "MonitoringLocationName": "L ARKANSAS R NR SEDGWICK, KS",
                        "MonitoringLocationDescriptionText": "Contact the Kansas WSC", "LatitudeMeasure": "37.8830674", "LongitudeMeasure": "-97.4244864",
                        "StateCode": "20", "CountyCode": "173", "ProviderName": "NWIS"})
        self.stations = [[station[c] for c in STATION_HEADER]]
        self.years = {2024: [wqp("2024-01-17", "Nitrate", "1.2"), wqp("2024-01-17", "Atrazine", "", detection="Not Detected", limit="0.007",
                                                                       comment="Kansas chain of custody samples, Attn: H. Example")],
                      2025: [], 2026: [wqp("2026-05-02", "Phosphorus", "0.31", org="21KAN001_WQX", site="21KAN001_WQX-SC273")]}
        self.web.routes = {w.WQP + "Station/search?": self.station_zip, w.WQP + "Result/search?": self.result_zip}

    def station_zip(self, url):
        self.assertIn("statecode=US%3A20", url)
        return zipped("station.csv", STATION_HEADER, self.stations)

    def result_zip(self, url):
        q = qs(url)
        self.assertEqual((q["statecode"], q["zip"], q["mimeType"]), ("US:20", "yes", "csv"))
        year = int(q["startDateLo"][-4:])
        self.assertEqual((q["startDateLo"], q["startDateHi"]), (f"01-01-{year}", f"12-31-{year}"))
        return zipped("result.csv", WQP_HEADER, self.years[year])

    def test_years_backfill_oldest_first_and_recent_years_are_refreshed(self):
        with patch.object(w, "WQP_FIRST_YEAR", 2024):
            first = w.water_quality(self.ctx, max_years=2)
            self.assertEqual((first["stations"], first["years"], first["rows"], first["next_year"]), ("loaded", [2024, 2025], 2, 2026))
            self.assertEqual(self.q("SELECT characteristic_name, result_measure_value, result_detection_condition_text, detection_quantitation_limit_value, "
                                    "activity_comment_text FROM kfm_wqp_results ORDER BY row_number"),
                             [("Nitrate", "1.2", None, None, None),
                              ("Atrazine", None, "Not Detected", "0.007", "Kansas chain of custody samples, Attn: H. Example")])
            self.assertEqual(self.q("SELECT monitoring_location_name, monitoring_location_description_text, latitude FROM kfm_wqp_stations"),
                             [("L ARKANSAS R NR SEDGWICK, KS", "Contact the Kansas WSC", 37.8830674)])
            kept = next((self.root / "data/raw/sql-feeds/water-quality/results/2024").glob("*.csv.gz"))
            self.assertEqual(gzip.decompress(kept.read_bytes()), table(WQP_HEADER, self.years[2024]), "the kept copy is the provider's CSV")
            receipt = core.receipt_for(self.ctx, kept)
            download = zipped("result.csv", WQP_HEADER, self.years[2024])
            self.assertEqual((receipt["key"], receipt["rows"], receipt["original"]),
                             ("results/2024", 2, {"sha256": core.sha256(download), "bytes": len(download), "kept": False}))
            self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE receipt_json LIKE '%results/2025%'"), [(0,)], "an empty year is only state")
            self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [], "temp files are removed")
            # The backfill finishes; nothing is due again the same day.
            second = w.water_quality(self.ctx)
            self.assertEqual((second["stations"], second["years"], second["backfill_pending"]), (None, [2026], 0))
            self.assertEqual(w.water_quality(self.ctx)["years"], [])
            # Eight days on, the current and previous years are due; 2024 (two years back) waits for its month.
            self.ctx.now = lambda: datetime(2026, 11, 12, 15, 0, tzinfo=timezone.utc)
            self.years[2026].append(wqp("2026-06-11", "Phosphorus", "0.12", org="21KAN001_WQX", site="21KAN001_WQX-SC273"))
            third = w.water_quality(self.ctx)
            self.assertEqual((third["years"], third["loaded"], third["unchanged"]), ([2026, 2025], 1, 0))
            self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_wqp_results WHERE activity_start_date LIKE '2026%'"), [(2,)])
            self.assertEqual(self.q("SELECT state FROM kfm_sql_sources WHERE receipt_json LIKE '%results/2026%' ORDER BY file_id"),
                             [("superseded",), ("complete",)])
            # A week later 2026 is due again but unchanged: no second kept copy of the same bytes.
            self.ctx.now = lambda: datetime(2026, 11, 20, 15, 0, tzinfo=timezone.utc)
            copies = sorted((self.root / "data/raw/sql-feeds/water-quality/results/2026").glob("*.csv.gz"))
            self.assertEqual(w.water_quality(self.ctx)["unchanged"], 1)   # 2025 is empty, so only 2026 compares
            self.assertEqual(sorted((self.root / "data/raw/sql-feeds/water-quality/results/2026").glob("*.csv.gz")), copies)
            self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [], "temp files are removed")

    def test_a_run_stops_at_its_row_budget(self):
        with patch.object(w, "WQP_FIRST_YEAR", 2024):
            self.assertEqual(w.water_quality(self.ctx, row_budget=1)["years"], [2024])

    def test_a_changed_header_or_damaged_archive_stops_and_a_failed_load_leaves_nothing(self):
        self.web.routes[w.WQP + "Station/search?"] = zipped("station.csv", [c for c in STATION_HEADER if c != "MonitoringLocationName"], [])
        with self.assertRaisesRegex(core.FeedError, "WQP_COLUMNS_CHANGED stations missing MonitoringLocationName"):
            w.water_quality(self.ctx)
        self.web.routes[w.WQP + "Station/search?"] = self.station_zip
        self.web.routes[w.WQP + "Result/search?"] = lambda url: self.result_zip(url)[:-30]
        with patch.object(w, "WQP_FIRST_YEAR", 2024), self.assertRaisesRegex(core.FeedError, "WQP_ARCHIVE_DAMAGED results/2024"):
            w.water_quality(self.ctx)
        self.web.routes[w.WQP + "Result/search?"] = self.result_zip
        with patch.object(w, "WQP_FIRST_YEAR", 2024), patch.object(core, "load_version", side_effect=RuntimeError("disk")), \
                self.assertRaises(RuntimeError):
            w.water_quality(self.ctx)
        real = core.finish_source
        with patch.object(w, "WQP_FIRST_YEAR", 2024), patch.object(core, "finish_source", side_effect=RuntimeError("disk")), \
                self.assertRaises(RuntimeError):
            w.water_quality(self.ctx)
        self.assertIs(core.finish_source, real)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_wqp_results"), [(0,)])
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [], "temp files are removed on failure")


if __name__ == "__main__":
    import unittest

    unittest.main()
