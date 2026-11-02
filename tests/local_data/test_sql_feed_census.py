"""Census ACS, 2020 Census and EIA SEDS feeds, without network access."""
from datetime import datetime, timezone
import gzip
import io
import json
import unittest
from unittest.mock import patch
from xml.sax.saxutils import escape
import zipfile

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_census as census, sql_feeds as core

ACS = census.ACS.format(vintage=2024)


def listing(entries: dict) -> bytes:
    """A www2.census.gov (Apache) directory page."""
    rows = "".join(f'<tr><td valign="top"><img src="/icons/text.gif" alt="[TXT]"></td><td><a href="{name}">{name}</a></td>'
                   f'<td align="right">{when}  </td><td align="right"> 64M</td><td>&nbsp;</td></tr>\n' for name, when in entries.items())
    return f'<html><body><table><tr><th><a href="?C=N;O=D">Name</a></th></tr>{rows}</table></body></html>'.encode()


def put(z, name, body):
    """A member with a fixed time, so the same fixture always zips to the same bytes."""
    z.writestr(zipfile.ZipInfo(name, (2021, 7, 26, 11, 44, 18)), body, compress_type=zipfile.ZIP_DEFLATED)


def xlsx(sheets: dict) -> bytes:
    """A workbook with shared strings, as the Census Bureau's are."""
    strings, index = [], {}

    def cell(ref, text):
        if text not in index:
            index[text] = len(strings)
            strings.append(text)
        return f'<c r="{ref}" t="s"><v>{index[text]}</v></c>'
    main = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w") as z:
        for n, rows in enumerate(sheets.values(), 1):
            body = "".join(f'<row r="{r}">' + "".join(cell(f"{chr(65 + c)}{r}", v) for c, v in enumerate(row) if v != "") + "</row>"
                           for r, row in enumerate(rows, 1))
            put(z, f"xl/worksheets/sheet{n}.xml", f'<worksheet xmlns="{main}"><sheetData>{body}</sheetData></worksheet>')
        put(z, "xl/sharedStrings.xml", f'<sst xmlns="{main}">' + "".join(f"<si><t>{escape(s)}</t></si>" for s in strings) + "</sst>")
        put(z, "xl/workbook.xml", f'<workbook xmlns="{main}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                   "<sheets>" + "".join(f'<sheet name="{escape(name)}" sheetId="{n}" r:id="rId{n}"/>' for n, name in enumerate(sheets, 1))
                   + "</sheets></workbook>")
        put(z, "xl/_rels/workbook.xml.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   + "".join(f'<Relationship Id="rId{n}" Type="worksheet" Target="worksheets/sheet{n}.xml"/>' for n in range(1, len(sheets) + 1))
                   + "</Relationships>")
    return out.getvalue()


def zipped(members: dict) -> bytes:
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w") as z:
        for name, body in members.items():
            put(z, name, body)
    return out.getvalue()


# --- ACS ----------------------------------------------------------------------------------------------------------

def acs_geo(**values):
    return "|".join(values.get(c, "") for c in census.ACS_GEOS_COLUMNS)


GEOS = "\n".join(["|".join(census.ACS_GEOS_COLUMNS),
                  acs_geo(FILEID="ACSSF", STUSAB="US", SUMLEVEL="010", COMPONENT="00", US="1", GEO_ID="0100000US", NAME="United States"),
                  acs_geo(FILEID="ACSSF", STUSAB="KS", SUMLEVEL="040", COMPONENT="00", STATE="20", GEO_ID="0400000US20", NAME="Kansas"),
                  acs_geo(FILEID="ACSSF", STUSAB="KS", SUMLEVEL="050", COMPONENT="00", STATE="20", COUNTY="001", GEO_ID="0500000US20001",
                          NAME="Allen County, Kansas"),
                  acs_geo(FILEID="ACSSF", STUSAB="NE", SUMLEVEL="050", COMPONENT="00", STATE="31", COUNTY="001", GEO_ID="0500000US31001",
                          NAME="Adams County, Nebraska"),
                  acs_geo(FILEID="ACSSF", STUSAB="US", SUMLEVEL="860", COMPONENT="00", ZCTA5="66002", GEO_ID="860Z200US66002", NAME="ZCTA5 66002"),
                  acs_geo(FILEID="ACSSF", STUSAB="US", SUMLEVEL="860", COMPONENT="00", ZCTA5="68001", GEO_ID="860Z200US68001", NAME="ZCTA5 68001"),
                  ]) + "\n"
SHELLS = ("Table ID|Line|Indent|Unique ID|Label|Title|Universe|Type\n"
          "B01003|1.0|0|B01003_001|Total|Total Population|Total population|int\n"
          "B19013|1.0|0|B19013_001|Median household income in the past 12 months (in 2024 inflation-adjusted dollars)|"
          "Median Household Income in the Past 12 Months (in 2024 Inflation-Adjusted Dollars)|Households|int\n"
          "B25003|1.0|0|B25003_001|Total:|Tenure|Occupied housing units|int\n"
          "B25003|2.0|1|B25003_002|Owner occupied|Tenure|Occupied housing units|int\n"
          "B25003|3.0|1|B25003_003|Renter occupied|Tenure|Occupied housing units|int\n")
GEO_IDS = ["0100000US", "0400000US20", "0500000US20001", "0500000US31001", "860Z200US66002", "860Z200US68001"]
KANSAS = {"0400000US20", "0500000US20001", "860Z200US66002"}
VALUES = {
    "B01003": [[334922499, -555555555], [2937524, -555555555], [12589, -555555555], [30946, -555555555], [1925, 302], [14000, 600]],
    "B19013": [[80734, 166], [74049, 410], [60689, 4364], [70000, 3000], [-666666666, -222222222], [90000, 8000]],
    "B25003": [[127482180, 230435, 83347320, 286301, 44134860, 179611], [1155040, 3209, 773720, 4174, 381320, 3912],
               [5046, 160, 3685, 205, 1361, 214], [12000, 90, 8000, 100, 4000, 120], [705, 82, 600, 75, 105, 49],
               [5000, 80, 4000, 90, 1000, 70]],
}


def acs_table(table, values=None, header=None):
    values = values or VALUES[table]
    width = len(values[0]) // 2
    header = header or "|".join(["GEO_ID", *(f"{table}_{k}{n:03d}" for n in range(1, width + 1) for k in "EM")])
    return (header + "\n" + "".join("|".join([g, *map(str, v)]) + "\n" for g, v in zip(GEO_IDS, values))).encode()


class AcsTests(FeedCase):
    TABLES = ("B01003", "B19013", "B25003")

    def setUp(self):
        super().setUp()
        self.listed = {t: "2026-01-29 07:30" for t in self.TABLES}
        self.files = {t: acs_table(t) for t in self.TABLES}
        self.geos = GEOS.encode()
        self.serve()

    def serve(self):
        data = {f"acsdt5y2024-{t.lower()}.dat": when for t, when in self.listed.items()}
        self.web.routes = {
            ACS + "documentation/Geos20245YR.txt": self.geos, ACS + "documentation/ACS20245YR_Table_Shells.txt": SHELLS.encode(),
            ACS + "documentation/": listing({"Geos20245YR.txt": "2026-01-22 07:15", "ACS20245YR_Table_Shells.txt": "2026-01-22 07:15",
                                             "README.txt": "2026-01-22 07:15"}),
            **{ACS + f"data/5YRData/acsdt5y2024-{t.lower()}.dat": body for t, body in self.files.items()},
            ACS + "data/5YRData/": listing({"5YRData.zip": "2026-01-29 07:30", **data}),
        }

    def run_acs(self, **options):
        return census.census_acs(self.ctx, **{"tables": self.TABLES, **options})

    def test_a_first_run_loads_kansas_geographies_values_and_labels_only(self):
        result = self.run_acs(tables=(*self.TABLES, "B99999"))
        self.assertEqual((result["tables_loaded"], result["rows"], result["geographies"], result["variables"]), (3, 15, 3, 5))
        self.assertEqual(result["absent"], ["2024/B99999"])
        self.assertEqual({g for (g,) in self.q("SELECT DISTINCT geo_id FROM kfm_census_acs_values")}, KANSAS)
        self.assertEqual({g for (g,) in self.q("SELECT geo_id FROM kfm_census_acs_geographies WHERE vintage=2024")}, KANSAS)
        # Annotation values are kept as published; labels and names join on the long form.
        self.assertEqual(self.q("SELECT estimate, margin_of_error FROM kfm_census_acs_values WHERE geo_id='860Z200US66002' AND variable='B19013_001'"),
                         [(-666666666, -222222222)])
        self.assertEqual(self.q("SELECT g.name, x.label, x.indent, v.estimate, v.margin_of_error FROM kfm_census_acs_values v "
                                "JOIN kfm_census_acs_geographies g USING(geo_id, vintage) JOIN kfm_census_acs_variables x "
                                "ON x.unique_id=v.variable AND x.vintage=v.vintage WHERE v.variable='B25003_002' AND g.sumlevel='050'"),
                         [("Allen County, Kansas", "Owner occupied", 1, 3685, 205)])
        kept = next((self.root / "data/raw/sql-feeds/census-acs/acs5/2024").glob("kansas-acsdt5y2024-b19013-*.dat.gz"))
        lines = gzip.decompress(kept.read_bytes()).decode().splitlines()
        self.assertEqual((lines[0], [l.split("|")[0] for l in lines[1:]]), ("GEO_ID|B19013_E001|B19013_M001", sorted(KANSAS)))
        receipt = core.receipt_for(self.ctx, kept)
        self.assertEqual((receipt["key"], receipt["original"]["bytes"], receipt["original"]["kept"]),
                         ("acs5/2024/B19013", len(self.files["B19013"]), False))
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])

    def test_a_rerun_reads_only_the_listings(self):
        self.run_acs()
        self.web.calls.clear()
        again = self.run_acs()
        self.assertEqual((again["tables_loaded"], again["rows"], again["pending"]), (0, 0, 0))
        self.assertEqual(self.web.calls, [ACS + "documentation/", ACS + "data/5YRData/"])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_census_acs_values"), [(15,)])

    def test_a_republished_file_replaces_its_version(self):
        self.run_acs()
        changed = [list(v) for v in VALUES["B19013"]]
        changed[2] = [61000, 4400]
        self.listed.update(B19013="2026-03-30 15:30", B01003="2026-03-30 15:30")
        self.files["B19013"] = acs_table("B19013", changed)
        self.serve()
        result = self.run_acs()
        self.assertEqual((result["tables"], result["unchanged"]), (["acs5/2024/B19013"], ["acs5/2024/B01003"]))
        self.assertEqual(self.q("SELECT estimate, margin_of_error FROM kfm_census_acs_values WHERE geo_id='0500000US20001' AND table_id='B19013'"),
                         [(61000, 4400)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_census_acs_values"), [(15,)])
        self.assertEqual(self.q("SELECT state, COUNT(*) FROM kfm_sql_sources WHERE source_id='census-acs5' GROUP BY state ORDER BY state"),
                         [("complete", 3), ("superseded", 1)])
        self.web.calls.clear()
        self.assertEqual(self.run_acs()["tables"], [])
        self.assertFalse([u for u in self.web.calls if u.endswith(".dat")])

    def test_the_backfill_stops_at_its_per_run_cap_and_resumes(self):
        # 2025 has only its 1-year files so far: not published yet, not an error.
        acs2025 = census.ACS.format(vintage=2025)
        self.web.routes = {acs2025 + "documentation/": listing({"Geos20251YR.txt": "2026-09-10 07:00"}),
                           acs2025 + "data/5YRData/": listing({}), **self.web.routes}
        first = self.run_acs(max_tables=2, vintages=(2024, 2025, 2026))
        self.assertEqual((first["tables_loaded"], first["pending"], first["unpublished"]), (2, 1, [2025, 2026]))
        second = self.run_acs(max_tables=2)
        self.assertEqual((second["tables"], second["pending"]), (["acs5/2024/B25003"], 0))
        self.assertEqual(self.run_acs(max_tables=2)["tables_loaded"], 0)

    def test_a_changed_header_stops_the_feed(self):
        self.files["B25003"] = acs_table("B25003", header="GEO_ID|B25003_E001|B25003_M001|B25003_E002|B25003_X002|B25003_E003|B25003_M003")
        self.serve()
        with self.assertRaisesRegex(core.FeedError, "ACS_COLUMNS_CHANGED acsdt5y2024-b25003.dat"):
            self.run_acs()
        self.assertEqual(self.q("SELECT DISTINCT table_id FROM kfm_census_acs_values ORDER BY 1"), [("B01003",), ("B19013",)])
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])

    def test_a_changed_geography_header_stops_the_feed(self):
        self.geos = GEOS.replace("TL_GEO_ID", "TLGEOID").encode()
        self.serve()
        with self.assertRaisesRegex(core.FeedError, "ACS_GEOS_COLUMNS_CHANGED"):
            self.run_acs()
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])

    def test_a_failure_part_way_leaves_no_partial_rows(self):
        real, calls = census._num, []

        def failing(value):
            calls.append(value)
            if len(calls) == 7:
                raise RuntimeError("disk went away")
            return real(value)
        with patch.object(census, "_num", failing), self.assertRaisesRegex(RuntimeError, "disk went away"):
            self.run_acs(tables=("B25003",))
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_census_acs_values"), [(0,)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE source_id='census-acs5' OR state='loading'"), [(0,)])
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])
        self.assertEqual(self.run_acs(tables=("B25003",))["rows"], 9)


# --- 2020 Census ----------------------------------------------------------------------------------------------------

def dec_geo(fileid, sumlev, comp, logrecno, geoid, name, pop="0", hu="0"):
    v = dict.fromkeys(census.DEC_GEO_COLUMNS, "")
    v.update(FILEID=fileid, STUSAB="KS", SUMLEV=sumlev, GEOVAR="00", GEOCOMP=comp, CHARITER="000", CIFSN="00", LOGRECNO=logrecno,
             GEOID=geoid, STATE="20", NAME=name, POP100=pop, HU100=hu, AREALAND="1295764235", AREAWATR="13021929",
             INTPTLAT="+37.8842285", INTPTLON="-095.3009448", FUNCSTAT="A")
    return "|".join(v[c] for c in census.DEC_GEO_COLUMNS)


def dec_segment(fileid, seg, rows):
    return "".join("|".join([fileid, "KS", "000", f"{seg:02d}", logrecno, *map(str, values)]) + "\n" for logrecno, values in rows)


LEAD = [["File Identification", "FILEID"], ["State/US-Abbreviation (USPS)", "STUSAB"], ["Characteristic Iteration", "CHARITER"],
        ["Characteristic Iteration File Sequence Number", "CIFSN"], ["Logical Record Number", "LOGRECNO"]]
PL_FIELDS = xlsx({
    "CONTENT EXPLANATION": [["The content of this workbook is derived from the technical documentation."]],
    "2020 P.L. Segment 1 Definitions": [["TABLE NUMBER AND CONTENTS", "DATA DICTIONARY REFERENCE NAME", "SEGMENT", "MAX SIZE", "DATA TYPE", "NOTES"],
                                        *LEAD, ["Total:", "P0010001", "01", "9", "N", "P1. RACE [3]"],
                                        ["Population of one race:", "P0010002", "01", "9", "N", "Universe: Total population"],
                                        ["White alone", "P0010003", "01", "9", "N", ""]],
    "2020 P.L. Segment 2 Definitions": [["TABLE NUMBER AND CONTENTS", "DATA DICTIONARY REFERENCE NAME", "DATA SEGMENT", "MAX SIZE", "DATA TYPE", "NOTES"],
                                        *LEAD, ["Total:", "H0010001", "02", "9", "N", "H1. OCCUPANCY STATUS FOR HOUSING"],
                                        ["Occupied", "H0010002", "02", "9", "N", "UNITS [3]"],
                                        ["Vacant", "H0010003", "02", "9", "N", "Universe: Housing units"]],
})
DHC_TABLES = [("P1", 1, 1, "TOTAL POPULATION [1]", [("P0010001", "Total")]),
              ("P12", 1, 2, "SEX BY AGE [2]", [("P0120001", "Total:"), ("P0120002", "Male:")]),
              ("P13", 1, 3, "MEDIAN AGE BY SEX [1]", [("P0130001", "Both sexes")]),
              ("P12A", 2, 1, None, [("P012A001", "Total:"), ("P012A002", "Male:")]),
              ("P12J", 2, 2, "SEX BY AGE (BLACK OR AFRICAN AMERICAN ALONE, NOT HISPANIC OR LATINO) [2]", [("P012J001", "Total:"), ("P012J002", "Male:")]),
              ("PCT12A", 3, 1, "SEX BY SINGLE-YEAR AGE (WHITE ALONE) [2]", [("PCT012A001", "Total:"), ("PCT012A002", "Male:")])]
DHC_MATRIX = [["2020 Census Demographic and Housing Characteristics File (DHC)\nTable Matrix (Shells)"],
              ["Person (P) or Housing (H)", "Table number", "Data dictionary reference name", "Segment", "Max size", "Table contents"]]
for _table, _seg, _, _title, _labels in DHC_TABLES:
    # P12A's title row has no table number, as PCT9G's does in the real matrix: the crosswalk names it.
    DHC_MATRIX += [["P", "" if _title is None else _table, "", "", "", _title or "SEX BY AGE (WHITE ALONE) [2]"],
                   ["P", _table, "", "", "", "Universe: Total population"],
                   *(["P", _table, name, str(_seg), "9", label] for name, label in _labels), [""]]
DHC_FIELDS = xlsx({"DHC Table Matrix": DHC_MATRIX,
                   "DHC Table_Segments": [["TABLE_ID", "SEGMENT_\nNUMBER", "TOTAL_\nRECORDS", "TABLE_SORT_ORDER"],
                                          *([t + "  ", str(s), str(len(labels)), str(o)] for t, s, o, _, labels in DHC_TABLES)],
                   "DHC Table ID Crosswalk": [["2020 Census DHC Crosswalk"], ["2020 DHC Table Number", "2010 SF1  Table Number", "Title"],
                                              ["P12A", "P12A", "SEX BY AGE FOR SELECTED AGE CATEGORIES (WHITE ALONE)"]]})
PL_GEO = [dec_geo("PLST", "040", "00", "0000001", "0400000US20", "Kansas", "2937880", "1275689"),
          dec_geo("PLST", "050", "00", "0000002", "0500000US20001", "Allen County", "12526", "6054"),
          dec_geo("PLST", "750", "00", "0000003", "7500000US200019526001000", "Block 1000", "3", "1"),
          dec_geo("PLST", "700", "00", "0000004", "7000000US20001000100", "Voting District 1", "500", "200")]
DHC_GEO = [dec_geo("DHCST", "040", "00", "0000001", "0400000US20", "Kansas", "2937880", "1275689"),
           dec_geo("DHCST", "040", "01", "0000002", "0400001US20", "Kansas -- Urban", "2124059", "910571"),
           dec_geo("DHCST", "050", "00", "0000003", "0500000US20001", "Allen County", "12526", "6054"),
           dec_geo("DHCST", "100", "00", "0000004", "1000000US200019526001000", "Block 1000", "3", "1"),
           dec_geo("DHCST", "140", "00", "0000005", "1400000US20001952600", "Census Tract 9526", "3000", "1500"),
           dec_geo("DHCST", "700", "00", "0000006", "7000000US20001000100", "Voting District 1", "500", "200")]


def pl_zip(seg1=None):
    rows = [(f"{n:07d}", v) for n, v in enumerate(seg1 or [[2937880, 2657373, 2222462], [12526, 11744, 11180], [3, 3, 3], [500, 490, 480]], 1)]
    return zipped({"ks000012020.pl": dec_segment("PLST", 1, rows),
                   "ks000022020.pl": dec_segment("PLST", 2, [(f"{n:07d}", [10, 9, 1]) for n in range(1, 5)]),
                   "ksgeo2020.pl": "\n".join(PL_GEO) + "\n"})


def dhc_zip(seg1=None, seg2_extra=False, geo=None):
    seg1 = seg1 or [[2937880, 2937880, 1462305, 37.0], [2124059, 2124059, 1050000, 36.1], [12526, 12526, 6221, 41.8], [3, 3, 2, "."],
                    [3000, 3000, 1500, "."], [500, 500, 250, 39.0]]
    seg2 = [[100, 50, 9, 4], [90, 45, 8, 4], [11180, 5520, 20, 10], [3, 2, 0, 0], [2900, 1450, 5, 2], [480, 240, 2, 1]]
    return zipped({"ks000012020.dhc": dec_segment("DHCST", 1, [(f"{n:07d}", v) for n, v in enumerate(seg1, 1)]),
                   "ks000022020.dhc": dec_segment("DHCST", 2, [(f"{n:07d}", v + ([7] if seg2_extra and n == 3 else [])) for n, v in enumerate(seg2, 1)]),
                   "ks000032020.dhc": dec_segment("DHCST", 3, [(f"{n:07d}", [1, 1]) for n in range(1, 7)]),
                   "ksgeo2020.dhc": "\n".join(geo or DHC_GEO) + "\n"})


class DecennialTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.serve()

    def serve(self, pl=None, dhc=None):
        (pl_url, pl_layout, _), (dhc_url, dhc_layout, _) = census.DEC_SOURCES["pl"], census.DEC_SOURCES["dhc"]
        self.web.routes = {pl_url: pl or pl_zip(), pl_layout: PL_FIELDS, dhc_url: dhc or dhc_zip(), dhc_layout: DHC_FIELDS}

    def test_a_first_run_loads_the_kept_geographies_and_selected_tables(self):
        result = census.census_decennial(self.ctx)
        self.assertEqual(result["complete"], ["pl", "dhc"])
        self.assertEqual(result["segments"], ["pl2020/segment-01", "pl2020/segment-02", "dhc2020/segment-01", "dhc2020/segment-02"])
        self.assertEqual(self.q("SELECT product, COUNT(*) FROM kfm_census_decennial_values GROUP BY 1 ORDER BY 1"), [("dhc", 18), ("pl", 12)])
        # Blocks, voting districts and geographic components are not loaded as values; PL blocks stay as geography rows.
        self.assertEqual(self.q("SELECT product, sumlev, pop100, hu100 FROM kfm_census_decennial_geographies ORDER BY product, logrecno"),
                         [("dhc", "040", 2937880, 1275689), ("dhc", "050", 12526, 6054), ("dhc", "140", 3000, 1500),
                          ("pl", "040", 2937880, 1275689), ("pl", "050", 12526, 6054), ("pl", "750", 3, 1)])
        self.assertEqual({g for (g,) in self.q("SELECT DISTINCT geoid FROM kfm_census_decennial_values")},
                         {"0400000US20", "0500000US20001", "1400000US20001952600"})
        self.assertEqual(self.q("SELECT DISTINCT table_id FROM kfm_census_decennial_values WHERE product='dhc' ORDER BY 1"),
                         [("P1",), ("P12",), ("P12A",), ("P13",)])
        self.assertEqual(self.q("SELECT geoid, value, typeof(value) FROM kfm_census_decennial_values WHERE variable='P0130001' ORDER BY geoid"),
                         [("0400000US20", 37, "integer"), ("0500000US20001", 41.8, "real"), ("1400000US20001952600", ".", "text")])
        self.assertEqual(self.q("SELECT table_id, variable, segment, position, label, title, universe FROM kfm_census_decennial_variables "
                                "WHERE variable IN ('H0010002', 'P012A002', 'P012J001') ORDER BY variable"),
                         [("H1", "H0010002", 2, 2, "Occupied", "OCCUPANCY STATUS FOR HOUSING UNITS", "Housing units"),
                          ("P12A", "P012A002", 2, 2, "Male:", "SEX BY AGE FOR SELECTED AGE CATEGORIES (WHITE ALONE)", "Total population"),
                          ("P12J", "P012J001", 2, 3, "Total:", "SEX BY AGE (BLACK OR AFRICAN AMERICAN ALONE, NOT HISPANIC OR LATINO)",
                           "Total population")])
        kept = next((self.root / "data/raw/sql-feeds/census-decennial/dhc2020").glob("kansas-ks000022020.dhc-*.txt.gz"))
        lines = gzip.decompress(kept.read_bytes()).decode().splitlines()
        self.assertEqual(lines[0], "FILEID|STUSAB|CHARITER|CIFSN|LOGRECNO|P012A001|P012A002")
        self.assertEqual([l.split("|")[4] for l in lines[1:]], ["0000001", "0000003", "0000005"])
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])

    def test_a_rerun_makes_no_request_until_the_yearly_recheck(self):
        census.census_decennial(self.ctx)
        self.web.calls.clear()
        again = census.census_decennial(self.ctx)
        self.assertEqual((again["segments"], again["rows"], self.web.calls), ([], 0, []))

    def test_a_republished_zip_replaces_the_changed_segment(self):
        census.census_decennial(self.ctx)
        seg1 = [[2937880, 2937880, 1462305, 37.0], [2124059, 2124059, 1050000, 36.1], [12530, 12530, 6223, 41.9], [3, 3, 2, "."],
                [3000, 3000, 1500, "."], [500, 500, 250, 39.0]]
        self.serve(dhc=dhc_zip(seg1))
        self.ctx.now = lambda: datetime(2027, 11, 6, 15, 0, tzinfo=timezone.utc)
        result = census.census_decennial(self.ctx)
        self.assertEqual((result["segments"], result["unchanged"]), (["dhc2020/segment-01"], ["pl", "dhc2020/segment-02"]))
        self.assertEqual(self.q("SELECT value FROM kfm_census_decennial_values WHERE geoid='0500000US20001' AND variable='P0010001' "
                                "AND product='dhc'"), [(12530,)])
        self.assertEqual(self.q("SELECT product, COUNT(*) FROM kfm_census_decennial_values GROUP BY 1 ORDER BY 1"), [("dhc", 18), ("pl", 12)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE state='superseded'"), [(1,)])

    def test_the_first_load_stops_at_its_segment_cap_and_resumes(self):
        dhc_url = census.DEC_SOURCES["dhc"][0]
        first = census.census_decennial(self.ctx, max_segments=2)
        self.assertEqual((first["complete"], first["pending"]), (["pl"], ["dhc"]))
        self.assertNotIn(dhc_url, self.web.calls)
        self.web.calls.clear()
        second = census.census_decennial(self.ctx, max_segments=2)
        self.assertEqual((second["complete"], second["segments"]), (["pl", "dhc"], ["dhc2020/segment-01", "dhc2020/segment-02"]))
        self.assertNotIn(census.DEC_SOURCES["pl"][0], self.web.calls)
        self.web.calls.clear()
        self.assertEqual(census.census_decennial(self.ctx, max_segments=2)["segments"], [])
        self.assertEqual(self.web.calls, [])

    def test_changed_segment_or_header_widths_stop_the_feed(self):
        self.serve(dhc=dhc_zip(seg2_extra=True))
        with self.assertRaisesRegex(core.FeedError, "DEC_COLUMNS_CHANGED ks000022020.dhc"):
            census.census_decennial(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_census_decennial_values WHERE table_id='P12A'"), [(0,)])
        short = [*DHC_GEO[:2], DHC_GEO[2].rsplit("|", 1)[0], *DHC_GEO[3:]]
        self.serve(dhc=dhc_zip(geo=short))
        with self.assertRaisesRegex(core.FeedError, "DEC_GEO_COLUMNS_CHANGED ksgeo2020.dhc"):
            census.census_decennial(self.ctx)
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])

    def test_a_failure_part_way_leaves_no_partial_rows(self):
        real, calls = census._num, []

        def failing(value):
            calls.append(value)
            if len(calls) == 4:
                raise RuntimeError("disk went away")
            return real(value)
        with patch.object(census, "_num", failing), self.assertRaisesRegex(RuntimeError, "disk went away"):
            census.census_decennial(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_census_decennial_values"), [(0,)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources WHERE source_id LIKE '%segment' OR state='loading'"), [(0,)])
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])
        self.assertEqual(census.census_decennial(self.ctx)["rows"], 30)


# --- EIA SEDS --------------------------------------------------------------------------------------------------------

def seds_series(code, state, data, **extra):
    name = {"KS": "Kansas", "NE": "Nebraska"}.get(state, "Federal Offshore - Gulf of Mexico")
    item = {"series_id": f"SEDS.{code}.{state}.A", "name": f"Total end-use energy consumption, {name}", "units": "Billion Btu", "f": "A",
            "description": f"Total end-use energy consumption, {name} See http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm",
            "copyright": "None", "source": "SEDS, EIA, U.S. Energy Information Administration",
            **({"iso3166": f"USA-{state}", "geography": f"USA-{state}"} if state in ("KS", "NE") else {}),
            "start": "2022", "end": "2024", "last_updated": "2026-06-26T15:32:24-04:00", "geoset_id": f"SEDS.{code}.A", "data": data}
    item.update(extra)
    return item


def seds_zip(ks_2024=1000, broken=None):
    lines = [{"category_id": "40203", "parent_category_id": "371", "name": "State Energy Data System (SEDS)", "notes": "", "childseries": []},
             {"category_id": "40208", "parent_category_id": "40203", "name": "Total End-Use Sectors", "notes": "",
              "childseries": ["SEDS.TETXB.KS.A", "SEDS.TETXB.NE.A"]},
             seds_series("TETXB", "KS", [["2024", ks_2024], ["2023", 990.5], ["2022", None]]),
             seds_series("TETXB", "NE", [["2024", 800], ["2023", 790]]),
             seds_series("TEICB", "KS", [["2024", 349716], ["2023", 352054]], name="Total energy consumption in the industrial sector, Kansas"),
             seds_series("TEPRB", "X3", [["2024", 5]]),
             {"geoset_id": "SEDS.TETXB.A", "name": "Total end-use energy consumption.", "units": "Billion Btu"},
             {"relation_id": "SEDS.FFTCB.A", "name": "Fossil fuel total consumption by fuel", "geoset_ids": ["SEDS.CLTCB.A"], "summable": "Y"}]
    if broken:
        lines.append(broken)
    return zipped({"SEDS.txt": "".join(json.dumps(l) + "\r\n" for l in lines)})


def manifest(updated="2026-06-26T15:32:24-04:00"):
    return json.dumps({"dataset": {"SEDS": {"last_updated": updated, "accessURL": census.SEDS_URL, "name": "State Energy Data System (SEDS)"}}}).encode()


class SedsTests(FeedCase):
    def setUp(self):
        super().setUp()
        self.web.routes = {census.SEDS_MANIFEST: manifest(), census.SEDS_URL: seds_zip()}

    def test_a_first_run_loads_the_kansas_series_and_categories(self):
        result = census.eia_seds(self.ctx)
        self.assertEqual((result["state"], result["series"], result["values"]), ("loaded", 2, 5))
        self.assertEqual(self.q('SELECT series_id, units, "start", "end", geography FROM kfm_eia_seds_series ORDER BY series_id'),
                         [("SEDS.TEICB.KS.A", "Billion Btu", "2022", "2024", "USA-KS"), ("SEDS.TETXB.KS.A", "Billion Btu", "2022", "2024", "USA-KS")])
        self.assertEqual(self.q("SELECT period, value FROM kfm_eia_seds_values WHERE series_id='SEDS.TETXB.KS.A' ORDER BY period"),
                         [("2022", None), ("2023", 990.5), ("2024", 1000)])
        self.assertEqual(self.q("SELECT category_id, series_id FROM kfm_eia_seds_category_series"), [("40208", "SEDS.TETXB.KS.A")])
        self.assertEqual(self.q("SELECT category_id, parent_category_id, name FROM kfm_eia_seds_categories ORDER BY category_id"),
                         [("40203", "371", "State Energy Data System (SEDS)"), ("40208", "40203", "Total End-Use Sectors")])
        kept = next((self.root / "data/raw/sql-feeds/eia-seds/seds").glob("kansas-SEDS-*.txt.gz"))
        kept_ids = [json.loads(l).get("series_id") for l in gzip.decompress(kept.read_bytes()).splitlines()]
        self.assertEqual(kept_ids, [None, None, "SEDS.TETXB.KS.A", "SEDS.TEICB.KS.A"])
        self.assertEqual(core.receipt_for(self.ctx, kept)["original"]["bytes"], len(seds_zip()))

    def test_a_rerun_reads_only_the_manifest_until_a_month_passes(self):
        census.eia_seds(self.ctx)
        self.web.calls.clear()
        self.assertEqual(census.eia_seds(self.ctx)["state"], "current")
        self.assertEqual(self.web.calls, [census.SEDS_MANIFEST])
        self.ctx.now = lambda: datetime(2026, 12, 5, 15, 0, tzinfo=timezone.utc)
        self.assertEqual(census.eia_seds(self.ctx)["state"], "unchanged")
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_eia_seds_values"), [(5,)])

    def test_a_new_release_replaces_the_loaded_version(self):
        census.eia_seds(self.ctx)
        self.web.routes = {census.SEDS_MANIFEST: manifest("2027-06-25T15:00:00-04:00"), census.SEDS_URL: seds_zip(ks_2024=1012)}
        result = census.eia_seds(self.ctx)
        self.assertEqual((result["state"], result["superseded"]), ("loaded", 1))
        self.assertEqual(self.q("SELECT value FROM kfm_eia_seds_values WHERE series_id='SEDS.TETXB.KS.A' AND period='2024'"), [(1012,)])
        self.assertEqual(self.q("SELECT (SELECT COUNT(*) FROM kfm_eia_seds_series), (SELECT COUNT(*) FROM kfm_eia_seds_values), "
                                "(SELECT COUNT(*) FROM kfm_eia_seds_categories), (SELECT COUNT(*) FROM kfm_eia_seds_category_series)"),
                         [(2, 5, 2, 1)])

    def test_changed_series_fields_stop_the_feed(self):
        broken = seds_series("TERCB", "KS", [])
        del broken["data"]
        self.web.routes[census.SEDS_URL] = seds_zip(broken=broken)
        with self.assertRaisesRegex(core.FeedError, "SEDS_COLUMNS_CHANGED SEDS.TERCB.KS.A"):
            census.eia_seds(self.ctx)
        self.web.routes[census.SEDS_URL] = seds_zip(broken=seds_series("TERCB", "KS", [], geography="USA-NE"))
        with self.assertRaisesRegex(core.FeedError, "SEDS_STATE_MISMATCH SEDS.TERCB.KS.A"):
            census.eia_seds(self.ctx)
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_sql_sources"), [(0,)])
        self.assertEqual(list((self.root / "tmp-sql-feeds").iterdir()), [])

    def test_a_failure_part_way_leaves_no_partial_rows(self):
        with patch.object(core, "finish_source", side_effect=RuntimeError("disk went away")), self.assertRaisesRegex(RuntimeError, "disk"):
            census.eia_seds(self.ctx)
        self.assertEqual(self.q("SELECT (SELECT COUNT(*) FROM kfm_eia_seds_series), (SELECT COUNT(*) FROM kfm_eia_seds_values), "
                                "(SELECT COUNT(*) FROM kfm_eia_seds_categories), (SELECT COUNT(*) FROM kfm_sql_sources)"), [(0, 0, 0, 0)])
        self.assertEqual(self.q("SELECT COUNT(*) FROM kfm_feed_state WHERE feed='eia-seds'"), [(0,)])
        self.assertEqual(census.eia_seds(self.ctx)["state"], "loaded")


class ListingTests(unittest.TestCase):
    def test_the_directory_page_gives_each_files_listed_time(self):
        row = ('<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="acsdt5y2024-b01001.dat">'
               'acsdt5y2024-b01001.dat</a></td><td align="right">2026-01-29 07:30  </td><td align="right">191M</td><td>&nbsp;</td></tr>')
        self.assertEqual(census._listing(row.encode()), {"acsdt5y2024-b01001.dat": "2026-01-29 07:30"})


if __name__ == "__main__":
    unittest.main()
