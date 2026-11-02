"""NASS Quick Stats feed: Kansas cuts of the national bulk files, without network access."""
from datetime import datetime, timezone
import gzip
import json
from unittest.mock import patch

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_nass as nass, sql_feeds as core

# A real crops row (Sedgwick County winter wheat), with the 39 columns in the provider's order.
BASE = ["SURVEY", "CROPS", "FIELD CROPS", "WHEAT", "WINTER", "ALL PRODUCTION PRACTICES", "ALL UTILIZATION PRACTICES", "YIELD", "BU / ACRE",
        "WHEAT, WINTER - YIELD, MEASURED IN BU / ACRE", "TOTAL", "NOT SPECIFIED", "COUNTY", "20", "20", "KS", "KANSAS", "80", "SOUTH CENTRAL",
        "173", "173", "SEDGWICK", "", "", "00000000", "", "", "9000", "UNITED STATES", "KANSAS, SOUTH CENTRAL, SEDGWICK", "2024", "ANNUAL",
        "00", "00", "YEAR", "", "2025-02-28 15:00:00", "48.5", "\x00"]
AT = {c: i for i, c in enumerate(nass.COLUMNS)}


def line(**changes) -> bytes:
    values = list(BASE)
    for column, value in changes.items():
        values[AT[column]] = value
    return "\t".join(values).encode("latin-1") + b"\r\n"


HEADER = "\t".join(nass.COLUMNS).encode() + b"\r\n"
KANSAS = [line(),
          line(AGG_LEVEL_DESC="STATE", ASD_CODE="", ASD_DESC="", COUNTY_ANSI="", COUNTY_CODE="", COUNTY_NAME="", LOCATION_DESC="KANSAS",
               VALUE="(D)", **{"CV_%": ""}),
          line(COMMODITY_DESC="SORGHUM", DOMAINCAT_DESC="CHEMICAL, INSECTICIDE: (CYFLUMETOFEN\xff= 138831)", YEAR="2023", VALUE="2,236,000")]
OTHERS = [line(STATE_ANSI="31", STATE_FIPS_CODE="31", STATE_ALPHA="NE", STATE_NAME="NEBRASKA", COUNTY_NAME="DOUGLAS", LOCATION_DESC="NEBRASKA"),
          line(AGG_LEVEL_DESC="NATIONAL", STATE_ANSI="", STATE_FIPS_CODE="99", STATE_ALPHA="US", STATE_NAME="US TOTAL", ASD_CODE="",
               COUNTY_ANSI="", LOCATION_DESC="US TOTAL"),
          line(AGG_LEVEL_DESC="REGION : MULTI-STATE", STATE_ANSI="", STATE_FIPS_CODE="00", STATE_ALPHA="", STATE_NAME="", ASD_CODE="",
               COUNTY_ANSI="", REGION_DESC="PROGRAM STATES", LOCATION_DESC="PROGRAM STATES"),
          line(STATE_ANSI="19", STATE_FIPS_CODE="19", STATE_ALPHA="IA", STATE_NAME="IOWA", ASD_CODE="20", COUNTY_ANSI="020")]


def national(kansas=KANSAS, others=OTHERS, header=HEADER) -> bytes:
    body = [header]
    for n, row in enumerate(kansas):
        body += [others[n % len(others)], row]
    return gzip.compress(b"".join(body + others))


def listing(dates) -> bytes:
    return "".join(f'<a href="/datasets/qs.{k}_{d}.txt.gz" class="gz" download=\'qs.{k}_{d}.txt.gz\'>' for k, d in dates.items()).encode()


class NassTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.files = {}
        self.serve({k: "20261031" for k in nass.KINDS})

    def serve(self, dates, changes=None):
        for kind, dated in dates.items():
            if (kind, dated) not in self.files:
                rows = [line(SECTOR_DESC=kind.upper(), YEAR=str(2000 + n)) for n in range(len(nass.KINDS))] if kind != "crops" else KANSAS
                self.files[(kind, dated)] = national(rows)
        self.files.update(changes or {})
        self.web.routes = {**{nass.NASS + f"qs.{k}_{d}.txt.gz": body for (k, d), body in self.files.items()}, nass.NASS: listing(dates)}

    def at(self, day):
        self.ctx.now = lambda: datetime(2026, 11, 4, 15, 0, tzinfo=timezone.utc).replace(**day)

    def leftovers(self):
        return list((self.root / "tmp-sql-feeds").glob("*"))

    def test_kansas_rows_only_two_kinds_a_run_until_every_kind_is_current(self):
        first = nass.nass(self.ctx)
        self.assertEqual((first["kinds"], first["rows"], first["pending"]), (["crops", "animals_products"], 8, ["economics", "demographics", "environmental"]))
        rows = self.q("SELECT state_alpha, state_fips_code, agg_level_desc, county_ansi, year, value, cv_pct, domaincat_desc FROM kfm_nass_quickstats "
                      "WHERE sector_desc='CROPS' ORDER BY row_number")
        self.assertEqual(rows, [("KS", "20", "COUNTY", "173", 2024, "48.5", None, "NOT SPECIFIED"), ("KS", "20", "STATE", "", 2024, "(D)", "", "NOT SPECIFIED"),
                                ("KS", "20", "COUNTY", "173", 2023, "2,236,000", None, "CHEMICAL, INSECTICIDE: (CYFLUMETOFEN\xff= 138831)")])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_nass_quickstats WHERE state_alpha<>'KS'"), [(0,)])
        # The kept copy is the Kansas lines byte for byte; the receipt records the national file.
        kept = next((self.root / "data/raw/sql-feeds/nass/crops").rglob("*.txt.gz"))
        self.assertEqual(gzip.decompress(kept.read_bytes()), HEADER + b"".join(KANSAS))
        receipt = core.receipt_for(self.ctx, kept)
        self.assertEqual((receipt["key"], receipt["file_date"], receipt["kansas_rows"], receipt["original"]["bytes"]),
                         ("qs.crops", "20261031", 3, len(self.files[("crops", "20261031")])))
        self.assertEqual(self.leftovers(), [])
        self.assertEqual(nass.nass(self.ctx)["kinds"], ["economics", "demographics"])
        self.assertEqual(nass.nass(self.ctx)["kinds"], ["environmental"])
        # Every kind is current: a rerun reads the listing and downloads nothing.
        self.web.calls.clear()
        again = nass.nass(self.ctx)
        self.assertEqual((again["kinds"], again["pending"], self.web.calls), ([], [], [nass.NASS]))
        self.assertEqual(self.q("SELECT COUNT(*), COUNT(DISTINCT file_id) FROM kfm_nass_quickstats"), [(23, 5)])

    def test_crops_runs_alone_once_the_run_byte_budget_is_spent(self):
        result = nass.nass(self.ctx, run_bytes=1)
        self.assertEqual((result["kinds"], len(result["pending"])), (["crops"], 4))

    def test_a_newer_file_replaces_the_kind_no_sooner_than_the_minimum_interval(self):
        nass.nass(self.ctx, max_kinds=1)
        revised = [KANSAS[0], line(YEAR="2025", VALUE="51.0"), KANSAS[2]]
        self.serve({"crops": "20261105"}, {("crops", "20261105"): national(revised)})
        self.web.calls.clear()
        self.assertEqual(nass.nass(self.ctx, max_kinds=1)["kinds"], [], "a newer file within 30 days of the last download waits")
        self.assertNotIn(nass.NASS + "qs.crops_20261105.txt.gz", self.web.calls)
        self.at({"month": 12, "day": 5})
        result = nass.nass(self.ctx, max_kinds=1)
        self.assertEqual((result["kinds"], result["rows"]), (["crops"], 3))
        self.assertEqual(self.q("SELECT year, value FROM kfm_nass_quickstats ORDER BY row_number"), [(2024, "48.5"), (2025, "51.0"), (2023, "2,236,000")])
        self.assertEqual(self.q("SELECT state FROM kfm_sql_sources ORDER BY file_id"), [("superseded",), ("complete",)])
        # NASS republishes with only national rows changed: the date is recorded, nothing is stored or loaded.
        self.serve({"crops": "20270110"}, {("crops", "20270110"): national(revised, OTHERS[1:])})
        self.at({"year": 2027, "month": 1, "day": 10})
        result = nass.nass(self.ctx, max_kinds=1)
        self.assertEqual((result["kinds"], result["unchanged"]), ([], ["crops"]))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(2,)])
        self.assertEqual(len(list((self.root / "data/raw/sql-feeds/nass/crops").rglob("*.txt.gz"))), 2)
        self.at({"year": 2027, "month": 3, "day": 1})
        self.assertEqual(nass.nass(self.ctx, max_kinds=1)["unchanged"], [])
        db = core.open_db(self.ctx)
        self.assertEqual(core.get_state(db, "nass")["seen"]["crops"], "20270110")
        db.close()

    def test_a_file_replaced_before_its_download_waits_for_the_next_listing(self):
        self.web.routes[nass.NASS + "qs.crops_20261031.txt.gz"] = None
        result = nass.nass(self.ctx, max_kinds=1)
        self.assertEqual((result["kinds"], result["replaced"]), ([], ["crops"]))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertEqual(self.leftovers(), [])

    def test_a_changed_header_or_state_code_stops_the_run(self):
        renamed = HEADER.replace(b"CV_%", b"CV_PCT")
        self.serve({"crops": "20261031"}, {("crops", "20261031"): national(header=renamed)})
        with self.assertRaisesRegex(core.FeedError, "NASS_COLUMNS_CHANGED qs.crops_20261031.txt.gz"):
            nass.nass(self.ctx)
        self.serve({"crops": "20261031"}, {("crops", "20261031"): national([line(STATE_FIPS_CODE="31")])})
        with self.assertRaisesRegex(core.FeedError, "NASS_STATE_MISMATCH"):
            nass.nass(self.ctx)
        self.serve({"crops": "20261031"}, {("crops", "20261031"): national([line()[:-30] + b"\r\n"])})
        with self.assertRaisesRegex(core.FeedError, "NASS_ROW_SHAPE"):
            nass.nass(self.ctx)
        self.serve({"crops": "20261031"}, {("crops", "20261031"): national()[:-40]})
        with self.assertRaisesRegex(core.FeedError, "NASS_GZIP_INVALID"):
            nass.nass(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertEqual(self.leftovers(), [])

    def test_a_load_that_fails_part_way_leaves_the_version_loaded_before(self):
        nass.nass(self.ctx, max_kinds=1)
        self.serve({"crops": "20261205"}, {("crops", "20261205"): national([line(YEAR="2025")] * 2 + [line(YEAR="2026")])})
        self.at({"month": 12, "day": 5})
        real = nass._rows

        def broken(path):
            for n, row in enumerate(real(path)):
                if n == 2:
                    raise core.FeedError("DISK_TROUBLE")
                yield row
        with patch.object(nass, "_rows", broken), self.assertRaisesRegex(core.FeedError, "DISK_TROUBLE"):
            nass.nass(self.ctx, max_kinds=1)
        self.assertEqual(self.q("SELECT year FROM kfm_nass_quickstats ORDER BY row_number"), [(2024,), (2024,), (2023,)])
        self.assertEqual(self.q("SELECT state FROM kfm_sql_sources"), [("complete",)])
        self.assertEqual(self.leftovers(), [])
        # The kind is still due and loads on the next run.
        self.assertEqual(nass.nass(self.ctx, max_kinds=1)["kinds"], ["crops"])
        self.assertEqual(self.q("SELECT year FROM kfm_nass_quickstats ORDER BY row_number"), [(2025,), (2025,), (2026,)])
        state = json.loads(self.q("SELECT state_json FROM kfm_feed_state WHERE feed='nass'")[0][0])
        self.assertEqual((state["seen"]["crops"], state["checked"]["crops"]), ("20261205", "2026-12-05"))


if __name__ == "__main__":
    import unittest

    unittest.main()
