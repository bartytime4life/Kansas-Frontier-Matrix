"""Climate SQL feeds (nClimDiv, U.S. Drought Monitor) against fake providers."""
from datetime import date, datetime, timedelta, timezone
import gzip
import json
import unittest
import urllib.parse
from unittest.mock import patch

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_climate as climate, sql_feeds as core

MONTHS = ["1.54", "0.99", "3.30", "8.09", "5.12", "5.96", "4.34", "2.05", "4.87", "1.10", "0.80", "0.75"]


def line(prefix: str, tokens) -> str:
    return prefix + "".join(f"{t:>7}" for t in tokens) + "   \n"


def pcpncy(oct_2026="-9.99", tail=""):
    return (line("13001011895", MONTHS)                                      # Iowa
            + line("14001012025", MONTHS) + line("14001012026", MONTHS[:9] + [oct_2026, "-9.99", "-9.99"])
            + line("14209012025", MONTHS) + line("14209012026", MONTHS[:9] + [oct_2026, "-9.99", "-9.99"]) + tail
            + line("20001012025", ["9.99"] * 12)).encode()                    # NCEI 20 is Michigan


def tmpcdv(sep_2026="77.30"):
    return (line("1401022026", ["31.60", "43.70", "52.80", "59.40", "64.70", "75.00", "80.80", "80.90", sep_2026, "-99.90", "-99.90", "-99.90"])
            + line("1501022026", ["40.00"] * 12)).encode()


def pdsist(dec_2025="-1.21"):
    return (line("0130051895", ["0.78"] * 12) + line("0140052025", ["0.60"] * 11 + [dec_2025])
            + line("1050052025", ["2.00"] * 12)).encode()


NORMALS = (line("0140020010", ["29.90", "34.50", "43.60", "53.40", "63.70", "74.10", "79.00", "77.50", "68.80", "56.30", "42.60", "32.20"])
           + line("0140020032", ["28.00"] * 12) + line("1100020010", ["33.00"] * 12)).encode()
COUNTY_MAP = (b"This file matches each county to a climate division.\n\nPOSTAL_FIPS_ID NCDC_FIPS_ID CLIMDIV_ID\n"
              b"01033 01033 0101\n20001 14001 1401\n20209 14209 1409\n26001 20001 2001\n")


def listing(release="20261006"):
    names = [f"climdiv-{c}-v1.0.0-{release}" for c in ("pcpncy", "tmpcdv", "pdsist", "norm-tmpcst", "sp60dv")]
    return "".join(f'<a href="{n}">{n}</a>' for n in names + ["climdiv-prcp-inv-v1.0.0-" + release, "county-readme.txt"]).encode()


class ClimdivTests(FeedCase):
    def serve(self, release="20261006", **files):
        bodies = {"pcpncy": pcpncy(), "tmpcdv": tmpcdv(), "pdsist": pdsist(), "norm-tmpcst": NORMALS, **files}
        self.web.routes = {climate.CLIMDIV + "county-to-climdivs.txt": COUNTY_MAP,
                           **{climate.CLIMDIV + f"climdiv-{code}-v1.0.0-{release}": body for code, body in bodies.items()},
                           climate.CLIMDIV: listing(release)}

    def raw_files(self):
        return sorted(p.name for p in (self.root / "data/raw/sql-feeds/climdiv").rglob("*.gz"))

    def test_a_release_is_loaded_as_kansas_long_form_rows_once(self):
        self.serve()
        result = climate.climdiv(self.ctx)
        self.assertEqual((result["files"], result["rows"], result["county_map_rows"], result["skipped"]), (4, 48 + 12 + 12 + 24, 2, ["sp60dv"]))
        self.assertEqual(self.q("SELECT area_code, COUNT(*), MIN(value), MAX(value) FROM kfm_climdiv_monthly WHERE element='pcpn' GROUP BY 1"),
                         [("20001", 24, 0.75, 8.09), ("20209", 24, 0.75, 8.09)], "Iowa and Michigan (NCEI 20) are left out")
        self.assertEqual(self.q("SELECT year, month, value, missing_token FROM kfm_climdiv_monthly WHERE area_code='20209' AND year=2026 AND month>=9"),
                         [(2026, 9, 4.87, None), (2026, 10, None, "-9.99"), (2026, 11, None, "-9.99"), (2026, 12, None, "-9.99")])
        self.assertEqual(self.q("SELECT area_type, area_code, element, COUNT(*), SUM(value IS NULL) FROM kfm_climdiv_monthly WHERE element!='pcpn' GROUP BY 1,2,3"),
                         [("division", "1401", "tmpc", 12, 3), ("state", "20", "pdsi", 12, 0)])
        self.assertEqual(self.q("SELECT period_code, period, month, value FROM kfm_climdiv_normals WHERE month=7 ORDER BY period_code"),
                         [("0010", "1991-2020", 7, 79.0), ("0032", "1895-2020", 7, 28.0)])
        self.assertEqual(self.q("SELECT postal_fips_id, ncdc_fips_id, climdiv_id FROM kfm_climdiv_county_divisions"),
                         [("20001", "14001", "1401"), ("20209", "14209", "1409")])
        kept = next((self.root / "data/raw/sql-feeds/climdiv/20261006").glob("climdiv-pcpncy-*.txt.gz"))
        receipt = core.receipt_for(self.ctx, kept)
        self.assertEqual((receipt["key"], receipt["kansas_lines"], receipt["original"]["bytes"]), ("pcpncy", 4, len(pcpncy())))
        self.assertTrue(gzip.decompress(kept.read_bytes()).decode().startswith("14001012025"))
        # A rerun reads only the listing.
        calls = len(self.web.calls)
        self.assertEqual(climate.climdiv(self.ctx)["files"], 0)
        self.assertEqual(self.web.calls[calls:], [climate.CLIMDIV])

    def test_a_newer_release_replaces_the_one_loaded_and_skips_an_unchanged_file(self):
        self.serve()
        climate.climdiv(self.ctx)
        before = self.raw_files()
        self.serve("20261106", pcpncy=pcpncy(oct_2026="2.22"), tmpcdv=tmpcdv("77.40"), pdsist=pdsist("-1.30"))
        result = climate.climdiv(self.ctx)
        self.assertEqual((result["files"], result["unchanged"], result["release"]), (3, 1, "20261106"))
        self.assertEqual(self.q("SELECT COUNT(*), COUNT(DISTINCT file_id) FROM kfm_climdiv_monthly WHERE element='pcpn'"), [(48, 1)])
        self.assertEqual(self.q("SELECT value FROM kfm_climdiv_monthly WHERE area_code='20001' AND year=2026 AND month=10"), [(2.22,)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources WHERE source_id='noaa-climdiv' GROUP BY 1"),
                         [("complete", 3), ("superseded", 3)])
        self.assertEqual(len(self.raw_files()), len(before) + 3, "an unchanged Kansas cut keeps no second raw copy")
        state = self.q("SELECT json_extract(state_json,'$.releases') FROM kfm_feed_state WHERE feed='climdiv'")[0][0]
        self.assertEqual(set(json.loads(state).values()), {"20261106"})

    def test_a_capped_run_leaves_the_rest_pending(self):
        self.serve()
        first = climate.climdiv(self.ctx, max_files=2)
        self.assertEqual((first["files"], first["pending"]), (2, 2))
        second = climate.climdiv(self.ctx, max_files=2)
        self.assertEqual((second["files"], second["pending"]), (2, 0))
        self.assertEqual(self.q("SELECT COUNT(DISTINCT element) FROM kfm_climdiv_monthly"), [(3,)])

    def test_a_changed_format_stops_the_feed_and_a_failed_load_leaves_the_old_release(self):
        self.serve()
        climate.climdiv(self.ctx)
        # The last Kansas line is one column short: the rows inserted before it are rolled back.
        self.serve("20261106", pcpncy=pcpncy(oct_2026="2.22", tail="14209012027  1.00\n"))
        with self.assertRaisesRegex(core.FeedError, "CLIMDIV_FORMAT_CHANGED climdiv-pcpncy-v1.0.0-20261106 5"):
            climate.climdiv(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*), MAX(value IS NULL) FROM kfm_climdiv_monthly WHERE area_code='20001' AND year=2026 AND month=10"), [(1, 1)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources WHERE json_extract(receipt_json,'$.key')='pcpncy' GROUP BY 1"), [("complete", 1)])
        self.assertIn('"pcpncy":"20261006"', self.q("SELECT state_json FROM kfm_feed_state WHERE feed='climdiv'")[0][0])
        self.serve("20261106", tmpcdv=b"1401022026  31.60\n")
        with self.assertRaisesRegex(core.FeedError, "CLIMDIV_FORMAT_CHANGED"):
            climate.climdiv(self.ctx)


def tuesdays(year, through):
    day = date(year, 1, 1) + timedelta((1 - date(year, 1, 1).weekday()) % 7)
    while day.year == year and day <= through:
        yield day
        day += timedelta(7)


class DroughtWeb:
    """The USDM statistics service for two Kansas counties and the state, with maps published through `through`."""

    def __init__(self, through=date(2026, 10, 27)):
        self.through, self.broken, self.fail_at, self.calls = through, {}, None, 0

    def __call__(self, url):
        self.calls += 1
        if self.fail_at == self.calls:
            raise core.FeedError("HTTP_500 " + url)
        parsed = urllib.parse.urlparse(url)
        query = dict(urllib.parse.parse_qsl(parsed.query))
        area, measure = parsed.path.split("/")[2:4]
        year, kind = int(query["startdate"].split("/")[2]), query["statisticsType"]
        level = "county" if area == "CountyStatistics" else "state"
        maps = [d for d in tuesdays(year - 1, self.through)][-1:] + list(tuesdays(year, self.through))
        if not list(tuesdays(year, self.through)):
            return b""
        shift = 1 if "Population" in measure else 0
        rows = [",".join(climate.USDM_HEADERS[level])]
        for day in sorted(maps, reverse=True):
            values = f"0.00,{100 - shift if kind == '1' else 60 - shift}.00,{40 + shift}.00,0.00,0.00,0.00"
            valid = f"{day:%Y-%m-%d},{day + timedelta(6):%Y-%m-%d},{kind}"
            if level == "county":
                rows += [f"{day:%Y%m%d},20001,Allen County,KS,{values},{valid}", f"{day:%Y%m%d},20003,Anderson County,KS,{values},{valid}"]
            else:
                rows.append(f"{day:%Y%m%d},KS,{values},{valid}")
        text = "\r\n".join(rows) + "\r\n"
        for old, new in self.broken.items():
            text = text.replace(old, new)
        return text.encode()


class DroughtTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.service = DroughtWeb()
        self.web.routes = {climate.USDM: self.service}
        self.first = patch.object(climate, "USDM_FIRST_YEAR", 2024)
        self.first.start()
        self.addCleanup(self.first.stop)

    def at(self, day):
        self.ctx.now = lambda: datetime(day.year, day.month, day.day, 15, tzinfo=timezone.utc)

    def test_years_load_newest_first_with_both_formats_and_only_their_own_maps(self):
        first = climate.drought(self.ctx, max_years=2)
        self.assertEqual((first["years"], first["files"], first["pending"], first["through"]), ([2026, 2025], 16, 1, "20261027"))
        weeks_2026 = len(list(tuesdays(2026, date(2026, 10, 27))))
        self.assertEqual(self.q("SELECT measure, statistic_format_id, COUNT(*) FROM kfm_usdm_county_stats WHERE map_date LIKE '2026%' GROUP BY 1,2"),
                         [("area_percent", 1, 2 * weeks_2026), ("area_percent", 2, 2 * weeks_2026),
                          ("population_percent", 1, 2 * weeks_2026), ("population_percent", 2, 2 * weeks_2026)])
        # The 2026 answer repeats 2025's last map; only the 2025 key holds it.
        self.assertEqual(self.q("SELECT COUNT(*), COUNT(DISTINCT file_id) FROM kfm_usdm_county_stats WHERE map_date='20251230'"), [(8, 4)])
        self.assertEqual(self.q("SELECT d0, d1, statistic_format_id FROM kfm_usdm_state_stats WHERE map_date='20261027' AND measure='area_percent' ORDER BY 3"),
                         [(100.0, 40.0, 1), (60.0, 40.0, 2)])
        kept = next((self.root / "data/raw/sql-feeds/drought/county/2026").glob("area_percent-1-*.csv.gz"))
        self.assertEqual(gzip.decompress(kept.read_bytes()), self.service(climate.usdm_url("county", "area_percent", 1, 2026)))
        # The backfill moves on to 2024, then nothing is due until Thursday's map.
        self.assertEqual(climate.drought(self.ctx, max_years=2)["years"], [2024])
        calls = self.service.calls
        self.assertEqual(climate.drought(self.ctx)["years"], [])
        self.assertEqual(self.service.calls, calls)

    def test_a_new_weekly_map_replaces_the_current_year_and_a_late_map_is_retried(self):
        climate.drought(self.ctx)
        self.at(date(2026, 11, 5))
        late = climate.drought(self.ctx)
        self.assertEqual((late["years"], late["files"], late["unchanged"], late["through"]), ([2026], 0, 8, "20261027"))
        self.service.through = date(2026, 11, 3)
        result = climate.drought(self.ctx)
        self.assertEqual((result["years"], result["files"], result["through"]), ([2026], 8, "20261103"))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usdm_county_stats WHERE map_date='20261103'"), [(8,)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usdm_county_stats WHERE map_date='20261027'"), [(8,)], "no duplicate rows")
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='superseded'"), [(8,)])

    def test_year_completion_and_the_yearly_recheck(self):
        state = {"years": {"2024": {"through": "20241231", "checked": "2025-10-01"}, "2025": {"through": "20251230", "checked": "2025-09-01"},
                           "2026": {"through": "20261027", "checked": "2026-11-04"}}}
        self.assertEqual(climate.usdm_due(state, date(2026, 11, 4)), [(2025, "recheck")])
        self.assertEqual(climate.usdm_due(state, date(2026, 11, 5)), [(2026, "new"), (2025, "recheck")])
        state["years"]["2025"]["through"] = "20251223"
        self.assertEqual(climate.usdm_due(state, date(2026, 1, 1))[:1], [(2025, "new")])
        self.assertEqual(climate.usdm_due({"years": {}}, date(2027, 1, 6))[0], (2026, "backfill"), "2027's first map is not out yet")

    def test_a_changed_or_wrong_answer_stops_the_feed(self):
        self.service.broken = {"StatisticFormatID": "StatisticFormat"}
        with self.assertRaisesRegex(core.FeedError, "USDM_COLUMNS_CHANGED"):
            climate.drought(self.ctx)
        self.service.broken = {"20003,Anderson County,KS": "31001,Adams County,NE"}
        with self.assertRaisesRegex(core.FeedError, "USDM_NOT_KANSAS"):
            climate.drought(self.ctx)
        self.service.broken = {}
        self.service.through = date(2023, 12, 31)
        with self.assertRaisesRegex(core.FeedError, "USDM_EMPTY_ANSWER"):
            climate.drought(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])

    def test_a_failure_part_way_keeps_whole_files_only_and_the_year_stays_due(self):
        self.service.fail_at = 5
        with self.assertRaisesRegex(core.FeedError, "HTTP_500"):
            climate.drought(self.ctx, max_years=1)
        self.assertEqual(self.q("SELECT COUNT(*), COUNT(DISTINCT file_id) FROM kfm_usdm_county_stats"), [(4 * 2 * len(list(tuesdays(2026, date(2026, 10, 27)))), 4)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usdm_state_stats"), [(0,)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_feed_state WHERE feed='drought'"), [(0,)])
        with patch.object(core, "finish_source", side_effect=core.FeedError("DISK_FULL")):
            with self.assertRaisesRegex(core.FeedError, "DISK_FULL"):
                climate.drought(self.ctx, max_years=1)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_usdm_state_stats"), [(0,)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources GROUP BY 1"), [("complete", 4)])
        result = climate.drought(self.ctx, max_years=1)
        self.assertEqual((result["years"], result["files"], result["unchanged"]), ([2026], 4, 4))


if __name__ == "__main__":
    unittest.main()
