"""Deterministic synthetic tests; no Census access, geometry decoding, or admission claim."""
from dataclasses import FrozenInstanceError
from hashlib import sha256
import importlib.util
import io
from pathlib import Path
import socket
import struct
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

PATH = Path(__file__).resolve().parents[1] / "src/census/tiger_package.py"
SPEC = importlib.util.spec_from_file_location("kfm_census_tiger_package_tested", PATH)
tp = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = tp
SPEC.loader.exec_module(tp)
NAD83 = (b'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",'
         b'SPHEROID["GRS_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],'
         b'UNIT["Degree",0.017453292519943295]]')
KANSAS_BBOX = (-99.0, 38.0, -98.0, 39.0)


def shape_header(shape_type, count, bbox, *, body_bytes=0, code=9994):
    total = 100 + body_bytes
    return (struct.pack(">i", code) + b"\0" * 20 + struct.pack(">i", total // 2)
            + struct.pack("<ii", 1000, shape_type) + struct.pack("<4d", *bbox)
            + b"\0" * 32)


def dbf(fields, rows, *, flag=b" "):
    header_len = 32 + 32 * len(fields) + 1
    record_len = 1 + sum(length for _, length in fields)
    out = bytearray(struct.pack("<B3BIHH", 0x03, 125, 1, 1, len(rows), header_len, record_len))
    out += b"\0" * 20
    for name, length in fields:
        out += name.encode().ljust(11, b"\0") + b"C" + b"\0" * 4 + bytes([length, 0]) + b"\0" * 14
    out += b"\r"
    for row in rows:
        out += flag + b"".join(str(value).encode().ljust(length)[:length]
                               for value, (_, length) in zip(row, fields))
    return bytes(out) + b"\x1a"


def package(stem, *, shape_type=5, fields=(("STATEFP", 2), ("GEOID", 11)),
            rows=(("20", "20001000100"), ("20", "20001000200")), bbox=KANSAS_BBOX,
            prj=NAD83, extra=None, drop=(), shx_count=None, flag=b" "):
    count = len(rows) if shx_count is None else shx_count
    members = {
        ".shp": shape_header(shape_type, count, bbox, body_bytes=16 * count) + b"\0" * 16 * count,
        ".shx": shape_header(shape_type, count, bbox, body_bytes=8 * count) + b"\0" * 8 * count,
        ".dbf": dbf(list(fields), list(rows), flag=flag),
        ".prj": prj,
        ".cpg": b"UTF-8",
        ".shp.iso.xml": b"<metadata/>",
    }
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for suffix, data in members.items():
            if suffix not in drop:
                archive.writestr(stem + suffix, data)
        for name, data in (extra or {}).items():
            archive.writestr(name, data)
    return buffer.getvalue()


def entry_for(file_name, body, product):
    return {"file_name": file_name, "product": product, "byte_length": len(body),
            "sha256": sha256(body).hexdigest()}


def inspect(file_name="tl_2025_20_tract.zip", product="TRACT", **kwargs):
    body = package(file_name[:-4], **kwargs)
    return tp.inspect_package(body, file_name=file_name, entry=entry_for(file_name, body, product))


class NameAndManifestTests(unittest.TestCase):
    def test_file_names(self):
        name = tp.parse_file_name("tl_2025_20001_areawater.zip")
        self.assertEqual((name.scope, name.product, name.identity_field),
                         ("county", "AREAWATER", "HYDROID"))
        self.assertEqual(tp.parse_file_name("tl_2025_us_rails.zip").scope, "national")
        for bad in ("tl_2025_20_unknown.zip", "tl_2025_2_tract.zip", "../tl_2025_20_tract.zip",
                    "tl_2025_20_tract.tar"):
            with self.subTest(bad=bad), self.assertRaises(tp.TigerPackageError):
                tp.parse_file_name(bad)

    def test_committed_manifest_entries_resolve(self):
        manifest = tp.load_manifest()
        entry = tp.manifest_entry(manifest, "tl_2025_20_tract.zip")
        self.assertEqual(entry["product"], "TRACT")
        packages = manifest["inventory"]["packages"]
        self.assertTrue(all(tp.parse_file_name(p["file_name"]).product == p["product"]
                            for p in packages))
        with self.assertRaises(tp.TigerPackageError):
            tp.manifest_entry(manifest, "tl_2025_20_nothing.zip")

    def test_integrity_against_entry(self):
        body = package("tl_2025_20_tract")
        entry = entry_for("tl_2025_20_tract.zip", body, "TRACT")
        for changed, code in (({"byte_length": 1}, "SIZE_MISMATCH"),
                              ({"sha256": "0" * 64}, "SHA256_MISMATCH"),
                              ({"product": "BG"}, "MANIFEST_ENTRY_MISMATCH")):
            with self.subTest(code=code), self.assertRaises(tp.TigerPackageError) as caught:
                tp.inspect_package(body, file_name="tl_2025_20_tract.zip",
                                   entry={**entry, **changed})
            self.assertEqual(str(caught.exception), code)


class InspectionTests(unittest.TestCase):
    def test_clean_state_package(self):
        candidate = inspect()
        self.assertEqual(candidate.route, "RAW_CANDIDATE")
        self.assertEqual((candidate.feature_count, candidate.kansas_feature_count), (2, 2))
        self.assertEqual((candidate.crs, candidate.shape_type), ("NAD83_GEOGRAPHIC", 5))
        self.assertEqual(candidate.identity_field, "GEOID")
        self.assertEqual([f.name for f in candidate.fields], ["STATEFP", "GEOID"])
        self.assertEqual((candidate.source_role, candidate.admission),
                         ("REFERENCE_GEOMETRY_CANDIDATE", "NOT_ADMITTED"))
        with self.assertRaises(FrozenInstanceError):
            candidate.route = "PUBLISHED"

    def test_path_source_matches_bytes(self):
        body = package("tl_2025_20_tract")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "tl_2025_20_tract.zip"
            path.write_bytes(body)
            from_path = tp.inspect_package(path, file_name=path.name,
                                           entry=entry_for(path.name, body, "TRACT"))
        self.assertEqual(from_path, tp.inspect_package(
            body, file_name=path.name, entry=entry_for(path.name, body, "TRACT")))

    def test_scope_and_content_quarantine(self):
        cases = {
            "STATE_SCOPE_MISMATCH": {"rows": (("20", "20001000100"), ("40", "40001000100"))},
            "IDENTITY_DUPLICATE": {"rows": (("20", "20001000100"), ("20", "20001000100"))},
            "IDENTITY_EMPTY": {"rows": (("20", ""), ("20", "20001000200"))},
            "IDENTITY_FIELD_ABSENT": {"fields": (("STATEFP", 2), ("NAME", 10)),
                                      "rows": (("20", "a"), ("20", "b"))},
            "CRS_UNRECOGNIZED": {"prj": b'PROJCS["Web_Mercator"]'},
            "SHAPE_TYPE_UNEXPECTED": {"shape_type": 3},
            "BBOX_OUTSIDE_KANSAS_CONTEXT": {"bbox": (-80.0, 30.0, -79.0, 31.0)},
            "BBOX_NOT_GEOGRAPHIC": {"bbox": (-11000000.0, 4500000.0, -10900000.0, 4600000.0)},
            "UNEXPECTED_MEMBER": {"extra": {"readme.txt": b"x"}},
            "DELETED_RECORDS_PRESENT": {"flag": b"*"},
        }
        for reason, kwargs in cases.items():
            with self.subTest(reason=reason):
                candidate = inspect(**kwargs)
                self.assertIn(reason, candidate.reasons)
                self.assertEqual(candidate.route, "QUARANTINE_CANDIDATE")

    def test_county_scope(self):
        fields = (("STATEFP", 2), ("COUNTYFP", 3), ("HYDROID", 22))
        good = inspect("tl_2025_20001_areawater.zip", "AREAWATER", fields=fields,
                       rows=(("20", "001", "h1"), ("20", "001", "h2")))
        self.assertEqual(good.route, "RAW_CANDIDATE")
        bad = inspect("tl_2025_20001_areawater.zip", "AREAWATER", fields=fields,
                      rows=(("20", "001", "h1"), ("20", "003", "h2")))
        self.assertIn("COUNTY_SCOPE_MISMATCH", bad.reasons)
        other_state = inspect("tl_2025_40001_areawater.zip", "AREAWATER", fields=fields,
                              rows=(("40", "001", "h1"),))
        self.assertIn("STATE_OUTSIDE_KANSAS_SCOPE", other_state.reasons)

    def test_national_packages_are_flagged_not_selected(self):
        rails = inspect("tl_2025_us_rails.zip", "RAILS", shape_type=3,
                        fields=(("LINEARID", 22), ("FULLNAME", 20)),
                        rows=(("r1", "A"), ("r2", "B")), bbox=(-120.0, 30.0, -70.0, 48.0))
        self.assertEqual(rails.route, "RAW_CANDIDATE")
        self.assertIsNone(rails.kansas_feature_count)
        self.assertEqual(rails.reasons, ("NATIONAL_PACKAGE_REQUIRES_SPATIAL_SELECTION",))
        county = inspect("tl_2025_us_county.zip", "COUNTY",
                         rows=(("20", "20001"), ("40", "40001"), ("20", "20003")))
        self.assertEqual(county.kansas_feature_count, 2)
        self.assertEqual(county.reasons, ("NATIONAL_PACKAGE_ATTRIBUTE_SELECTION_ONLY",))

    def test_structural_failures_reject(self):
        cases = {
            "MEMBER_MISSING": {"drop": (".dbf",)},
            "FEATURE_COUNT_MISMATCH": {"shx_count": 3},
            "MEMBER_PATH": {"extra": {"../escape.txt": b"x"}},
        }
        for code, kwargs in cases.items():
            with self.subTest(code=code), self.assertRaises(tp.TigerPackageError) as caught:
                inspect(**kwargs)
            self.assertEqual(str(caught.exception), code)
        bomb = {"tl_2025_20_tract.extra": b"\0" * 5_000_000}
        with self.assertRaises(tp.TigerPackageError) as caught:
            inspect(extra=bomb)
        self.assertEqual(str(caught.exception), "MEMBER_BOUND")
        not_zip = b"not a zip"
        with self.assertRaises(tp.TigerPackageError):
            tp.inspect_package(not_zip, file_name="tl_2025_20_tract.zip",
                               entry=entry_for("tl_2025_20_tract.zip", not_zip, "TRACT"))

    def test_corrupt_headers_reject(self):
        stem = "tl_2025_20_tract"
        good = package(stem)
        with zipfile.ZipFile(io.BytesIO(good)) as source:
            members = {info.filename: source.read(info) for info in source.infolist()}
        for member, mutate, code in (
                (".shp", lambda b: struct.pack(">i", 1) + b[4:], "SHAPE_HEADER"),
                (".shp", lambda b: b + b"\0" * 8, "SHAPE_LENGTH"),
                (".dbf", lambda b: b[:-5], "DBF_SIZE"),
                (".dbf", lambda b: b[:10] + struct.pack("<H", 99) + b[12:],
                 "DBF_RECORD_LENGTH")):
            changed = dict(members)
            changed[stem + member] = mutate(members[stem + member])
            buffer = io.BytesIO()
            with zipfile.ZipFile(buffer, "w") as archive:
                for name, data in changed.items():
                    archive.writestr(name, data)
            body = buffer.getvalue()
            with self.subTest(code=code), self.assertRaises(tp.TigerPackageError) as caught:
                tp.inspect_package(body, file_name=stem + ".zip",
                                   entry=entry_for(stem + ".zip", body, "TRACT"))
            self.assertEqual(str(caught.exception), code)


    def test_duplicate_member_names_reject(self):
        stem = "tl_2025_20_tract"
        buffer = io.BytesIO(package(stem))
        with zipfile.ZipFile(buffer, "a") as archive, \
                self.assertWarns(UserWarning):
            archive.writestr(stem + ".prj", b'PROJCS["shadow"]')
        body = buffer.getvalue()
        with self.assertRaises(tp.TigerPackageError) as caught:
            tp.inspect_package(body, file_name=stem + ".zip",
                               entry=entry_for(stem + ".zip", body, "TRACT"))
        self.assertEqual(str(caught.exception), "MEMBER_PATH")


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            inspect()


if __name__ == "__main__":
    unittest.main()
