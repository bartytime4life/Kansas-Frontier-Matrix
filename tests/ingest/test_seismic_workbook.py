"""Synthetic OOXML fixtures; neither KGS workbook was supplied or fabricated here."""
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "tools/ingest/inspect_seismic_workbook.py"
spec = importlib.util.spec_from_file_location("seismic_workbook", MODULE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
S = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
P = "http://schemas.openxmlformats.org/package/2006/relationships"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def workbook(overrides=None):
    parts = {
        "[Content_Types].xml": '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>',
        "xl/workbook.xml": f'<workbook xmlns="{S}" xmlns:r="{R}"><sheets><sheet name="Synthetic" sheetId="1" r:id="r1"/></sheets></workbook>',
        "xl/_rels/workbook.xml.rels": f'<Relationships xmlns="{P}"><Relationship Id="r1" Type="{R}/worksheet" Target="worksheets/sheet1.xml"/></Relationships>',
        "xl/worksheets/sheet1.xml": f'<worksheet xmlns="{S}"><sheetData><row r="1"><c r="A1" t="inlineStr"><is><t>invented_header</t></is></c></row><row r="2"><c r="A2"><v>7</v></c></row></sheetData></worksheet>',
    }
    parts.update(overrides or {})
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        for name, body in parts.items():
            archive.writestr(name, body)
    return output.getvalue()


class WorkbookTests(unittest.TestCase):
    def inspect(self, body, **kwargs):
        return module.inspect_workbook(body, product_kind="recorded-earthquakes", **kwargs)

    def test_bounded_header_and_counts_not_events(self):
        report = self.inspect(workbook())
        self.assertEqual(report["outcome"], "REVIEW_REQUIRED")
        self.assertEqual(report["admission"], "NOT_ADMITTED")
        self.assertEqual(report["sheets"][0]["rows_present"], 2)
        self.assertEqual(report["sheets"][0]["candidate_headers"][0]["literal"], "invented_header")
        self.assertNotIn('"literal": "7"', json.dumps(report))
        self.assertNotIn("events", report)

    def test_felt_kind_is_caller_label(self):
        report = module.inspect_workbook(workbook(), product_kind="felt-reports")
        self.assertEqual(report["product_kind_supplied_by_caller"], "felt-reports")

    def test_deterministic_report(self):
        body = workbook()
        self.assertEqual(self.inspect(body), self.inspect(body))

    def test_missing_header_is_not_guessed(self):
        self.assertEqual(self.inspect(workbook(), header_row=3)["sheets"][0]["candidate_headers"], [])

    def test_formula_not_evaluated_or_echoed(self):
        body = workbook({"xl/worksheets/sheet1.xml": f'<worksheet xmlns="{S}"><sheetData><row r="1"><c r="A1"><f>WEBSERVICE("https://invalid.example/secret")</f><v>cached</v></c></row></sheetData></worksheet>'})
        report = self.inspect(body)
        self.assertEqual(report["sheets"][0]["formula_cells"], 1)
        self.assertEqual(report["sheets"][0]["candidate_headers"][0]["literal"], "[FORMULA_NOT_EVALUATED]")
        self.assertNotIn("secret", json.dumps(report))
        self.assertNotIn("cached", json.dumps(report))

    def test_external_relationship_count_only(self):
        body = workbook({"xl/worksheets/_rels/sheet1.xml.rels": f'<Relationships xmlns="{P}"><Relationship Id="e1" TargetMode="External" Target="https://invalid.example/secret"/></Relationships>'})
        report = self.inspect(body)
        self.assertEqual(report["external_relationships"], 1)
        self.assertNotIn("secret", json.dumps(report))

    def test_shared_string(self):
        report = self.inspect(workbook({
            "xl/sharedStrings.xml": f'<sst xmlns="{S}"><si><t>Synthetic shared header</t></si></sst>',
            "xl/worksheets/sheet1.xml": f'<worksheet xmlns="{S}"><sheetData><row r="1"><c r="A1" t="s"><v>0</v></c></row></sheetData></worksheet>',
        }))
        self.assertEqual(report["sheets"][0]["candidate_headers"][0]["literal"], "Synthetic shared header")

    def test_bad_shared_string_reference(self):
        body = workbook({"xl/worksheets/sheet1.xml": f'<worksheet xmlns="{S}"><sheetData><row r="1"><c r="A1" t="s"><v>999999</v></c></row></sheetData></worksheet>'})
        with self.assertRaisesRegex(module.WorkbookInspectionError, "SHARED_STRING_INDEX"):
            self.inspect(body)

    def test_active_content(self):
        for name in ("xl/vbaProject.bin", "xl/activeX/x.bin", "xl/embeddings/x.bin"):
            with self.subTest(name=name), self.assertRaisesRegex(module.WorkbookInspectionError, "ACTIVE_CONTENT"):
                self.inspect(workbook({name: b"not executable"}))

    def test_archive_traversal(self):
        for name in ("../evil", "/absolute", "xl/../evil", "xl\\evil", "C:/evil"):
            with self.subTest(name=name), self.assertRaisesRegex(module.WorkbookInspectionError, "ARCHIVE_MEMBER"):
                self.inspect(workbook({name: b"x"}))

    def test_dtd_and_entities_rejected(self):
        with self.assertRaisesRegex(module.WorkbookInspectionError, "XML_DECLARATION"):
            self.inspect(workbook({"xl/workbook.xml": '<!DOCTYPE x [<!ENTITY a "x">]><x/>'}))

    def test_non_utf8_profile_rejected(self):
        with self.assertRaisesRegex(module.WorkbookInspectionError, "XML_DECLARATION"):
            self.inspect(workbook({"xl/workbook.xml": "<workbook/>".encode("utf-16")}))

    def test_oversize_member(self):
        with self.assertRaisesRegex(module.WorkbookInspectionError, "EXPANSION_BOUND"):
            self.inspect(workbook({"large.bin": b"x" * (module.MAX_MEMBER + 1)}))

    def test_corrupt_zip(self):
        with self.assertRaisesRegex(module.WorkbookInspectionError, "WORKBOOK_UNREADABLE"):
            self.inspect(b"not a zip")

    def test_product_and_header_bounds(self):
        with self.assertRaisesRegex(module.WorkbookInspectionError, "PRODUCT_KIND_REQUIRED"):
            module.inspect_workbook(workbook(), product_kind="all earthquakes")
        for row in (0, 101, True):
            with self.subTest(row=row), self.assertRaisesRegex(module.WorkbookInspectionError, "HEADER_ROW_BOUND"):
                self.inspect(workbook(), header_row=row)

    def test_cli_and_missing_path(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.xlsx"
            path.write_bytes(workbook())
            args = [sys.executable, str(MODULE), str(path), "--kind", "felt-reports"]
            result = subprocess.run(args, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["outcome"], "REVIEW_REQUIRED")
            path.unlink()
            result = subprocess.run(args, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 1)
            self.assertNotIn(directory, result.stderr)

    @unittest.skipUnless(hasattr(__import__("os"), "O_NOFOLLOW"), "platform lacks leaf no-follow")
    def test_cli_refuses_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "sample.xlsx"
            target.write_bytes(workbook())
            link = Path(directory) / "link.xlsx"
            link.symlink_to(target)
            result = subprocess.run([sys.executable, str(MODULE), str(link), "--kind", "felt-reports"], capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
