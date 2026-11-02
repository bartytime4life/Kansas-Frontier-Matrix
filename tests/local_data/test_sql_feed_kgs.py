"""KGS feed: oil and gas wells, leases, tops and production, and WWC5 water wells, without network access."""
from datetime import datetime, timezone
import hashlib
import io
from unittest.mock import patch
import zipfile

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_kgs as kgs, sql_feeds as core

# Real rows from the 2026-10-09 files. Names, operators and comments are kept whole (owner, 2026-11-02).
WELL = ["1001184249", "15-007-20056", "15007200560000", "Winters, W.W.", "1", "Aetna Gas Area", "37.0528605", "-98.9778514", "Calc. from footages",
        "34", "S", "15", "W", "29", "  N2 S2 SW", "1220", "-3960", "SE", "Midwest Oil Corp.", "Pohl, Henry", "1608", " KB", "1598.2026", "4950", "",
        "", "", "", "", "08-MAR-1968", "08-MAR-1968", "19-MAR-1968", "19-MAR-1968", "21-JAN-2014", "", "", "", "", "", "D&A",
        "Plugged and Abandoned", "plugged by JOHN HILLER, landowner", "Winters, W.W. 1"]
UNLOCATED = ["1001184206", "", "", "Bertha C. Sprague", "1-W", "UNNAMED", "", "", "Source unknown", "30", "S", "11", "W", "25", "", "", "", "",
             "Hart, Raymond (Residential)", "unavailable", "", "", "", "", "", "", "", "", "", "", "", "", "", "18-APR-2014", "", "", "", "", "",
             "OTHER()", "", "", "Bertha C. Sprague 1-W"]
LEASE = ["1001135839", "SNYDER", "122608", "15-131-20143, 15-131-20089-0002 ", "Buckeye West, LLC", "Nemaha", "1", "S", "14", "E", "1", "NENENE",
         "39.999519", "-95.78905", "OIL", "41020.92", "1985", "2026", "https://chasm.kgs.ku.edu/ords/oil.ogl5.MainLease?f_lc=1001135839"]
UNPRODUCED = ["1043937066", "Hustead A-2", "129112", "15-013-19018 ", "Stucky, Edward P.", "Brown", "1", "S", "15", "E", "3", "", "39.993698",
              "-95.720714", "NULL", "", "", "", "https://chasm.kgs.ku.edu/ords/oil.ogl5.MainLease?f_lc=1043937066"]
TOP = ["1001184249", "15-007-20056", "15007200560000", "-98.9778514", "37.0528605", "1608", "KB", 'Mississippi "Chat"', "3615", "", "Unknown",
       "15-APR-99", "Mississippian System"]


def production(month_year, product, amount, kid="1001135839", operator="Buckeye West, LLC"):
    return [kid, "SNYDER", "122608", "15-131-20143 ", "KANASKA", "Lansing Group", operator, "Nemaha", "1", "S", "14", "E", "1", "NENENE",
            "39.999519", "-95.78905", month_year, product, "2", amount, f"https://chasm.kgs.ku.edu/ords/oil.ogl5.MainLease?f_lc={kid}"]


def wwc5(**values):
    row = [""] * len(kgs.WWC5)
    for column, value in values.items():
        row[kgs.WWC5.index(column)] = value
    return row


WATER_WELLS = [
    wwc5(WELL_ID="3", COUNTY="Allen", TOWNSHIP="23", TWN_DIR="S", RANGE="19", RANGE_DIR="E", SECTION="26", SPOT="SW SW SW", LONGITUDE="-95.2975975",
         LATITUDE="38.0098162", LONG_LAT_TYPE="From PLSS", OWNER="Garrison, Guy", WELL_USE="Domestic", COMPLE_DATE="10-Jul-1978", STATUS="CONSTRUCTED",
         DIRECTIONS="from LaHarpe: 5 mi N, 1 mi W, 1 mi N", WELL_DEPTH="137", STATIC_DEPTH="43", DRILLER="Eureka Well Service", WELL_KID="1040081052",
         SCANNED="Y", URL="https://chasm.kgs.ku.edu/ords/wwc5.wwc5d2.well_details?well_id=3", NAD83_LONGITUDE="-95.2978544", NAD83_LATITUDE="38.0098482",
         CONTRACTORS_LICENSE_NUMBER="296"),
    # KGS escapes nothing: an inch mark and a line break inside values, as in the real file.
    wwc5(WELL_ID="452779", COUNTY="Republic", TOWNSHIP="1", RANGE="3", RANGE_DIR="W", SECTION="2", OWNER="City of Belleville",
         WELL_USE="Public Water Supply", CASING_THICKNESS='.375"', SCREEN_PERFORATION_MATERIAL="Stainless steel", NAD83_LONGITUDE="-97.631"),
    wwc5(WELL_ID="1057030070", COUNTY="Thomas", TOWNSHIP="7", RANGE="33", RANGE_DIR="W", SECTION="30", OWNER="Mattson, Herb",
         DIRECTIONS="2195 N Range Ave\r\nColby is 67701", LONGITUDE="-101.0535663", LATITUDE="39.4179881")]
LOGS = [["3", "-95.2975975", "38.0098162", "0", "1", "Soil", "KGS", "-95.2978544", "38.0098482"],
        ["3", "-95.2975975", "38.0098162", "1", "6", "Clay, yellow", "KGS", "-95.2978544", "38.0098482"]]


def kgs_zip(key, header, rows, member=None):
    text = "".join(",".join(f'"{v}"' for v in row) + "\r\n" for row in [header, *rows])
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(member or key + ".txt", text.encode())
    return out.getvalue()


def contents():
    files = {"ks_wells": (kgs.WELLS, [WELL, UNLOCATED]), "all_kansas_leases": (kgs.LEASES, [LEASE, UNPRODUCED]), "ks_tops": (kgs.TOPS, [TOP]),
             "oil_leases_2020_present": (kgs.PRODUCTION, [production("1-2020", "O", "161.8"), production("2-2020", "O", "")]),
             "gas_leases_2020_present": (kgs.PRODUCTION, [production("1-2020", "G", "1510")]),
             "wwc5_wells_full": (kgs.WWC5, WATER_WELLS), "wwc5_lith_log": (kgs.LITHOLOGY, LOGS)}
    for decade in kgs.DECADES:
        files[f"oil_leases_{decade}"] = (kgs.PRODUCTION, [production(f"1-{decade[:4]}", "O", "332", operator="Elk Oil Enterprises, LLC")])
        files[f"gas_leases_{decade}"] = (kgs.PRODUCTION, [production(f"1-{decade[:4]}", "G", "363")])
    return files


def listing(stamps):
    rows = [f'<tr><td valign="top"><img src="/icons/compressed.gif" alt="[   ]"></td><td><a href="{name}">{name}</a></td>'
            f'<td align="right">{stamp}  </td><td align="right"> 42M</td><td>&nbsp;</td></tr>' for name, stamp in stamps.items()]
    return ("<html><body><h1>Index of /PRS/Ora_Archive</h1><table>" + "\n".join(rows) + "</table></body></html>").encode()


class KgsTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.files = contents()
        self.stamps = {key + ".zip": ("2026-10-09 14:59" if "2020_present" in key or not key.endswith("9") else "2025-03-27 12:34")
                       for key in self.files}
        # Overlapping or older copies KGS also lists: never fetched.
        self.stamps.update({"oil_leases_2010_2018.zip": "2025-03-27 12:36", "oil_leases_2020_2029.zip": "2025-03-27 12:35",
                            "wwc5_wells.zip": "2026-10-09 15:10", "wwc5_Allen.txt": "2025-09-29 19:27"})
        self.serve()

    def serve(self, **zips):
        built = {key: kgs_zip(key, *spec) for key, spec in self.files.items()}
        built.update(zips)
        self.web.routes = {**{kgs.ARCHIVE + key + ".zip": body for key, body in built.items()}, kgs.ARCHIVE: listing(self.stamps)}

    def at(self, **day):
        self.ctx.now = lambda: datetime(2026, 11, 4, 15, 0, tzinfo=timezone.utc).replace(**day)

    def leftovers(self):
        return list((self.root / "tmp-sql-feeds").glob("*"))

    def test_four_files_a_run_backfill_the_archive_with_every_column(self):
        first = kgs.kgs_oil_gas(self.ctx)
        self.assertEqual(first["files"], ["ks_wells", "all_kansas_leases", "ks_tops", "oil_leases_2020_present"])
        self.assertEqual((first["rows"], len(first["pending"])), (7, 11))
        self.assertEqual(self.q("SELECT kid, lease, well, latitude, curr_operator, comments, lease_well_name, api_county FROM kfm_kgs_wells ORDER BY row_number"),
                         [("1001184249", "Winters, W.W.", "1", 37.0528605, "Pohl, Henry", "plugged by JOHN HILLER, landowner", "Winters, W.W. 1", "007"),
                          ("1001184206", "Bertha C. Sprague", "1-W", None, "unavailable", "", "Bertha C. Sprague 1-W", None)])
        self.assertEqual(self.q("SELECT lease_kid, lease, operator, county, production, year_start FROM kfm_kgs_leases ORDER BY row_number"),
                         [("1001135839", "SNYDER", "Buckeye West, LLC", "Nemaha", 41020.92, "1985"),
                          ("1043937066", "Hustead A-2", "Stucky, Edward P.", "Brown", None, "")])
        self.assertEqual(self.q("SELECT kid, formation, top, base FROM kfm_kgs_tops"), [("1001184249", 'Mississippi "Chat"', 3615.0, None)])
        self.assertEqual(self.q("SELECT lease_kid, field, operator, county, month_year, year, month, product, wells, production "
                                "FROM kfm_kgs_lease_production ORDER BY row_number"),
                         [("1001135839", "KANASKA", "Buckeye West, LLC", "Nemaha", "1-2020", 2020, 1, "O", 2, 161.8),
                          ("1001135839", "KANASKA", "Buckeye West, LLC", "Nemaha", "2-2020", 2020, 2, "O", 2, None)])
        self.assertEqual(len([r for r in self.q("PRAGMA table_info(kfm_kgs_wells)")]), 2 + len(kgs.WELLS) + 1)
        # The kept copy is the provider's zip byte for byte; the receipt records the CSV inside.
        kept = next((self.root / "data/raw/sql-feeds/kgs-oil-gas/ks_wells").glob("ks_wells-20261009-*.zip"))
        served = self.web.routes[kgs.ARCHIVE + "ks_wells.zip"]
        self.assertEqual(kept.read_bytes(), served)
        receipt = core.receipt_for(self.ctx, kept)
        text = zipfile.ZipFile(io.BytesIO(served)).read("ks_wells.txt")
        self.assertEqual((receipt["key"], receipt["listed"], receipt["rows"], receipt["terms"], receipt["content_sha256"]),
                         ("ks_wells", "2026-10-09 14:59", 2, kgs.TERMS, hashlib.sha256(text).hexdigest()))
        self.assertEqual(self.leftovers(), [])
        # The backfill moves on: 4, 4, 3, then nothing is due.
        self.assertEqual(kgs.kgs_oil_gas(self.ctx)["files"], ["gas_leases_2020_present", "wwc5_wells_full", "wwc5_lith_log", "oil_leases_1980_1989"])
        self.assertEqual(kgs.kgs_oil_gas(self.ctx)["files"], ["oil_leases_1990_1999", "oil_leases_2000_2009", "oil_leases_2010_2019", "gas_leases_1980_1989"])
        self.assertEqual(kgs.kgs_oil_gas(self.ctx)["files"], ["gas_leases_1990_1999", "gas_leases_2000_2009", "gas_leases_2010_2019"])
        self.assertFalse([u for u in self.web.calls if "wwc5_wells.zip" in u or "wwc5_Allen" in u or "2010_2018" in u or "2020_2029" in u])
        self.web.calls.clear()
        self.assertEqual(kgs.kgs_oil_gas(self.ctx), {"files": [], "rows": 0, "unchanged": [], "pending": []})
        self.assertEqual(self.web.calls, [kgs.ARCHIVE])
        self.assertEqual(self.q("SELECT product, COUNT(*), COUNT(DISTINCT file_id), MIN(year), MAX(year) FROM kfm_kgs_lease_production GROUP BY product"),
                         [("G", 5, 5, 1980, 2020), ("O", 6, 5, 1980, 2020)])
        self.assertEqual(self.q("SELECT DISTINCT operator FROM kfm_kgs_lease_production WHERE product='O' AND year < 2020"), [("Elk Oil Enterprises, LLC",)])
        # Water wells: values holding a quote or a line break come through exactly.
        self.assertEqual(self.q("SELECT well_id, county, owner, casing_thickness, directions, latitude, nad83_longitude FROM kfm_kgs_wwc5_wells ORDER BY row_number"),
                         [("3", "Allen", "Garrison, Guy", "", "from LaHarpe: 5 mi N, 1 mi W, 1 mi N", 38.0098162, -95.2978544),
                          ("452779", "Republic", "City of Belleville", '.375"', "", None, -97.631),
                          ("1057030070", "Thomas", "Mattson, Herb", "", "2195 N Range Ave\r\nColby is 67701", 39.4179881, None)])
        self.assertEqual(self.q("SELECT well_id, top, bottom, log, source FROM kfm_kgs_wwc5_lithology ORDER BY row_number"),
                         [("3", 0.0, 1.0, "Soil", "KGS"), ("3", 1.0, 6.0, "Clay, yellow", "KGS")])
        receipt = core.receipt_for(self.ctx, next((self.root / "data/raw/sql-feeds/kgs-oil-gas/wwc5_wells_full").glob("*.zip")))
        self.assertEqual((receipt["rows"], receipt["terms"]), (3, kgs.WWC5_TERMS))

    def backfill(self):
        for _ in range(4):
            kgs.kgs_oil_gas(self.ctx)

    def test_a_relisted_file_is_reloaded_after_the_recheck_interval(self):
        self.backfill()
        self.files["oil_leases_2020_present"][1].append(production("7-2026", "O", "44.5"))
        self.stamps["oil_leases_2020_present.zip"] = "2026-11-09 14:52"
        self.serve()
        self.at(day=20)
        self.assertEqual(kgs.kgs_oil_gas(self.ctx)["files"], [], "a change within 28 days of the last download waits")
        self.at(month=12, day=2)
        result = kgs.kgs_oil_gas(self.ctx)
        self.assertEqual((result["files"], result["rows"]), (["oil_leases_2020_present"], 3))
        self.assertEqual(self.q("SELECT month_year, production FROM kfm_kgs_lease_production p JOIN kfm_sql_sources s USING (file_id) "
                                "WHERE json_extract(s.receipt_json,'$.key')='oil_leases_2020_present' ORDER BY row_number"),
                         [("1-2020", 161.8), ("2-2020", None), ("7-2026", 44.5)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources GROUP BY state"), [("complete", 15), ("superseded", 1)])
        # Listed again with the same CSV in a rebuilt zip: recorded as seen, not stored or loaded again.
        self.stamps["oil_leases_2020_present.zip"] = "2026-12-09 14:52"
        spec = self.files["oil_leases_2020_present"]
        self.serve(oil_leases_2020_present=self.rebuilt("oil_leases_2020_present", *spec))
        self.at(year=2027, month=1, day=5)
        self.assertEqual(kgs.kgs_oil_gas(self.ctx)["unchanged"], ["oil_leases_2020_present"])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(16,)])
        self.assertEqual(len(list((self.root / "data/raw/sql-feeds/kgs-oil-gas/oil_leases_2020_present").glob("*.zip"))), 2)
        self.at(year=2027, month=3, day=1)
        self.web.calls.clear()
        kgs.kgs_oil_gas(self.ctx)
        self.assertEqual(self.web.calls, [kgs.ARCHIVE])

    @staticmethod
    def rebuilt(key, header, rows):
        """The same CSV in a zip with a different member date, as KGS's monthly rebuild gives."""
        text = "".join(",".join(f'"{v}"' for v in row) + "\r\n" for row in [header, *rows])
        out = io.BytesIO()
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(zipfile.ZipInfo(key + ".txt", (2026, 12, 9, 11, 10, 6)), text.encode(), zipfile.ZIP_DEFLATED)
        return out.getvalue()

    def test_a_changed_file_layout_stops_the_run(self):
        renamed = [c if c != "STATUS2" else "STATUS_2" for c in kgs.WELLS]
        cases = {"KGS_COLUMNS_CHANGED ks_wells": kgs_zip("ks_wells", renamed, [WELL]),
                 "KGS_ROW_SHAPE ks_wells 2": kgs_zip("ks_wells", kgs.WELLS, [WELL, WELL[:-1]]),
                 "KGS_ROW_SHAPE ks_wells 1": kgs_zip("ks_wells", kgs.WELLS, [WELL[:-1], WELL]),
                 "KGS_ZIP_CHANGED ks_wells": kgs_zip("ks_wells", kgs.WELLS, [WELL], member="ks_wells_2026.txt"),
                 "KGS_ZIP_INVALID ks_wells": b"<html>maintenance</html>"}
        for reason, body in cases.items():
            self.serve(ks_wells=body)
            with self.assertRaisesRegex(core.FeedError, reason + "$"):
                kgs.kgs_oil_gas(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertEqual(self.leftovers(), [])

    def test_a_load_that_fails_part_way_leaves_no_rows(self):
        real = kgs._rows

        def broken(path, key, kind):
            for n, row in enumerate(real(path, key, kind)):
                if kind.table == "kfm_kgs_lease_production" and n == 1:
                    raise core.FeedError("DISK_TROUBLE")
                yield row
        with patch.object(kgs, "_rows", broken), self.assertRaisesRegex(core.FeedError, "DISK_TROUBLE"):
            kgs.kgs_oil_gas(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_kgs_lease_production"), [(0,)])
        self.assertEqual(self.q("SELECT source_id, state FROM kfm_sql_sources ORDER BY file_id"),
                         [("kgs-wells", "complete"), ("kgs-leases", "complete"), ("kgs-tops", "complete")])
        self.assertEqual(self.leftovers(), [])
        # The failed file is retried first on the next run, from the copy already kept.
        self.assertEqual(kgs.kgs_oil_gas(self.ctx)["files"][0], "oil_leases_2020_present")
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_kgs_lease_production"), [(3,)])

    def test_a_file_gone_from_the_listing_is_reported_after_the_others_load(self):
        del self.stamps["wwc5_lith_log.zip"]
        self.serve()
        with self.assertRaisesRegex(core.FeedError, "KGS_FILE_MISSING wwc5_lith_log$"):
            kgs.kgs_oil_gas(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='complete'"), [(4,)])


if __name__ == "__main__":
    import unittest

    unittest.main()
