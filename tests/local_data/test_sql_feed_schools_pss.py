"""The NCES Private School Survey files: survey-round column names and the renamed zips."""
import io
import sqlite3
import zipfile

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feed_institutions as institutions


def zipped(member: str, text: str) -> bytes:
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w") as archive:
        archive.writestr(member, text)
    return out.getvalue()


class PssTests(FeedCase):
    def load(self, key: str, url: str) -> dict:
        db = sqlite3.connect(self.db_path)
        try:
            db.executescript(institutions.NCES_DDL)
            summary = {"files": {}, "rows": 0, "downloaded_bytes": 0, "missing": []}
            self.assertTrue(institutions._nces_file(self.ctx, db, key, url, summary))
            return summary
        finally:
            db.close()

    def test_survey_round_prefixes_of_the_1990s_files_are_recognized(self):
        for key, prefix, fips in (("pss/1995-1996", "Q", "QSTFIP"), ("pss/1997-1998", "R", "RSTFIP"), ("pss/1999-2000", "S", "SSTFIPS")):
            with self.subTest(key=key):
                url = institutions._pss_url(int(key[4:8]), int(key[9:13]))
                header = [f"{prefix}PIN", f"{prefix}CITY", f"{prefix}STABB", fips, f"{prefix}CNTY", f"{prefix}ZIP", "RELIG", "ORIENT", "NUMSTUDS"]
                rows = ["\t".join(header), "\t".join(["00000033", "GADSDEN", "AL", "1", "055", "35901", "1", "1", "109"]),
                        "\t".join(["00000044", "SALINA", "KS", "20", "169", "67401", "1", "1", "88"])]
                self.web.routes[url] = zipped("PSS_PU.txt", "\n".join(rows) + "\n")
                self.assertEqual(self.load(key, url)["rows"], 1)
                found = self.q("SELECT ppin, city, state, state_fips, county, zip, students FROM kfm_nces_pss_schools WHERE school_year = ?", key[4:])
                self.assertEqual(found, [("00000044", "SALINA", "KS", "20", "169", "67401", "88")])

    def test_every_survey_since_2011_uses_the_name_nces_publishes(self):
        expected = {"pss/1989-1990": "TXT_PSS8990.zip", "pss/2009-2010": "TXT_PSS0910.zip", "pss/2011-2012": "pss1112_pu_txt.zip",
                    "pss/2013-2014": "pss1314_pu_csv.zip", "pss/2023-2024": "pss2324_pu_csv.zip"}
        targets = dict(institutions._nces_targets(self.ctx, {"ccd_listing": {"files": []}}))
        for key, name in expected.items():
            self.assertEqual(targets[key], institutions.PSS_ZIPS + name)

    def test_a_recorded_404_under_the_old_name_is_due_again(self):
        old = {"checked": "2026-11-04", "missing": True, "url": institutions.PSS_ZIPS + "TXT_PSS1112.zip"}
        state = {"files": {"pss/2011-2012": old}}
        self.assertTrue(institutions._nces_due(state, "pss/2011-2012", institutions._pss_url(2011, 2012), self.ctx.now().date()))

    def test_year_suffixed_coordinates_of_the_recent_files_load(self):
        url = institutions._pss_url(2023, 2024)
        rows = ["PPIN,PINST,PCITY,PSTABB,PL_STABB,PCNTY,PZIP,LATITUDE24,LONGITUDE24,RELIG,ORIENT,NUMSTUDS",
                "K1,Prairie School,Salina,KS,KS,169,67401,38.84,-97.61,1,1,88"]
        self.web.routes[url] = zipped("pss2324_pu.csv", "\n".join(rows) + "\n")
        self.load("pss/2023-2024", url)
        self.assertEqual(self.q("SELECT name, latitude, longitude FROM kfm_nces_pss_schools"), [("Prairie School", 38.84, -97.61)])
