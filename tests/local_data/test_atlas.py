"""Private preview bounds and parity with source-scoped intake review holds."""
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
import zipfile

from tools.local_data import atlas, atlas_worker, intake, intake_service
from tools.local_data.manage import init_store


class AtlasTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "store"
        init_store(self.root)
        self.raw = self.root / "data/raw/source"
        self.raw.mkdir()
        self.file = self.raw / "points.csv"
        self.file.write_text("latitude,longitude,value\n38,-98,7\n39,-97,9\n")
        intake.analyze(self.root)
        self.model = atlas.Atlas(self.root)
        self.item = intake.list_items(self.root)["items"][0]

    def tearDown(self):
        self.temp.cleanup()

    def test_private_review_preview_does_not_grant_authority_or_invent_units(self):
        value = self.model.preview({"kind": "file", "id": self.item["id"]})
        self.assertEqual(value["displayedCount"], 2)
        self.assertEqual(value["authority"], {"admission": False, "evidence": False, "release": False})
        self.assertIsNone(value["units"])
        self.assertIn("review holds remain", " ".join(value["limitations"]))
        self.assertEqual(intake.get_item(self.root, self.item["id"])["status"], "review")

    def test_paths_bad_identifiers_band_values_and_unknown_request_fields_are_denied(self):
        requests = [{"kind": "file", "id": "../outside"}, {"kind": "file", "id": self.item["id"], "path": "/etc/passwd"},
                    {"kind": "file", "id": self.item["id"], "band": True}, {"kind": "file", "id": self.item["id"], "band": 101},
                    {"kind": {}, "id": self.item["id"]}, {"kind": "file", "id": self.item["id"], "representation": []},
                    {"kind": "file", "id": self.item["id"], "compareId": []}]
        for request in requests:
            with self.subTest(request=request), self.assertRaises(ValueError): self.model.preview(request)

    def test_source_digest_change_is_detected_even_with_preserved_size_and_mtime(self):
        info = self.file.stat()
        self.file.write_text(self.file.read_text().replace(",7", ",8"))
        os.utime(self.file, ns=(info.st_atime_ns, info.st_mtime_ns))
        with self.assertRaisesRegex(ValueError, "SOURCE_CHANGED_REANALYZE"):
            self.model.preview({"kind": "file", "id": self.item["id"]})

    def test_symlinks_and_source_paths_cannot_leave_the_store(self):
        link = self.raw / "link.csv"; link.symlink_to(self.file)
        with self.assertRaises(ValueError): atlas.safe_path(self.root, "data/raw/source/link.csv")
        with self.assertRaises(ValueError): atlas.safe_path(self.root, "../outside")

    def test_atlas_reads_keep_the_legacy_quarantine_binding_hold(self):
        source = self.root / "data/quarantine/one/objects/sha256" / ("a" * 64)
        source.mkdir(parents=True)
        (source / "payload").write_bytes(b"latitude,longitude\n38,-98\n")
        intake.analyze(self.root)
        with intake.open_index(self.root) as conn:
            conn.execute("DELETE FROM meta WHERE key='quarantine_binding_version'")
        with self.assertRaisesRegex(ValueError, "INTAKE_REANALYSIS_REQUIRED"): self.model.catalog()
        with self.assertRaisesRegex(ValueError, "INTAKE_REANALYSIS_REQUIRED"): self.model._item(self.item["id"])
        intake.analyze(self.root)
        self.assertEqual(self.model.catalog()["total"], 2)

    def test_preview_serializes_only_bounded_scalar_properties_and_wgs84(self):
        data = atlas.vector_data([{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-98, 38]},
                                   "properties": {"long": "a" * 2000, "nested": {"unsafe": 1}, "nan": float("nan")}}])
        props = data["data"]["features"][0]["properties"]
        self.assertEqual(len(props["long"]), 500)
        self.assertNotIn("nested", props)
        self.assertIsNone(props["nan"])
        with self.assertRaisesRegex(ValueError, "NO_DISPLAYABLE"):
            atlas.vector_data([{"geometry": {"type": "Point", "coordinates": [1000000, 2000000]}}])
        json.dumps(data, allow_nan=False)

    def test_feature_cap_is_explicitly_truncated_and_invalid_rows_are_not_zero(self):
        f = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-98, 38]}, "properties": {}}
        value = atlas.vector_data([f] * (atlas.FEATURE_LIMIT + 1))
        self.assertEqual(value["displayedCount"], atlas.FEATURE_LIMIT)
        self.assertTrue(value["truncated"])
        features, total = atlas.csv_features(b"latitude,longitude,value\n38,-98,1\n,,2\n")
        self.assertEqual((len(features), total), (1, 2))

    def test_prism_normal_annual_monthly_and_daily_clocks_stay_distinct(self):
        annual = atlas.classify_prism("normals/us/4km/ppt/monthly/PRISM_ppt_30yr_normal_4kmM4_2020.zip", "mm", "v1")
        monthly = atlas.classify_prism("normals/us/4km/ppt/monthly/PRISM_ppt_30yr_normal_4kmM4_202001_bil.zip", "mm", "v1")
        self.assertEqual(annual["period"], "annual")
        self.assertEqual(monthly["period"], "monthly")
        self.assertIn("normal 1991", annual["label"])
        self.assertIsNone(atlas.classify_prism("normals/us/4km/ppt/monthly/PRISM_ppt_4kmM4_201901_bil.zip", "mm", "v1"))

    def test_archive_readers_reject_traversal_and_links_without_extracting(self):
        for member in ["../outside.tif", "/outside.tif", "inside\\outside.tif"]:
            raw = io.BytesIO()
            with zipfile.ZipFile(raw, "w") as z: z.writestr(member, b"x")
            with zipfile.ZipFile(io.BytesIO(raw.getvalue())) as z:
                with self.subTest(member=member), self.assertRaisesRegex(ValueError, "ARCHIVE_UNSAFE"):
                    atlas_worker.archive_members(z)

    def test_map_extents_follow_the_selected_page(self):
        for name in ["second.csv", "third.csv"]: (self.raw / name).write_bytes(self.file.read_bytes())
        intake.analyze(self.root)
        desk = intake_service.Desk(self.root)
        first = desk.extents({"limit": 1, "offset": 0})
        second = desk.extents({"limit": 1, "offset": 1})
        self.assertEqual((first["scannedCount"], first["nextOffset"]), (1, 1))
        self.assertNotEqual(first["features"][0]["properties"]["id"], second["features"][0]["properties"]["id"])


if __name__ == "__main__":
    unittest.main()
