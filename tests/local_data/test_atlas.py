"""Private preview bounds and parity with source-scoped intake review holds."""
import io
import json
import os
from pathlib import Path
import sqlite3
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
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


class AtlasWorkerBoundaryTests(unittest.TestCase):
    """The worker's pure guards; raster/vector reads need the operator's rasterio runtime."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.dir = Path(self.temp.name).resolve()
        self.file = self.dir / "grid.tif"
        self.file.write_bytes(b"not a real raster")

    def tearDown(self):
        self.temp.cleanup()

    def run_worker(self, request):
        completed = subprocess.run([sys.executable, "-I", str(Path(atlas_worker.__file__))], input=json.dumps(request),
                                   capture_output=True, text=True, timeout=60, check=False)
        self.assertEqual(0, completed.returncode, completed.stderr)
        return json.loads(completed.stdout)

    def test_worker_paths_must_be_absolute_regular_files_without_links(self):
        self.assertEqual(self.file, atlas_worker.regular(str(self.file)))
        (self.dir / "link.tif").symlink_to(self.file)
        (self.dir / "linked").symlink_to(self.dir, target_is_directory=True)
        for path in ("grid.tif", str(self.dir / "sub" / ".." / "grid.tif"), str(self.dir / "link.tif"),
                     str(self.dir / "linked" / "grid.tif"), str(self.dir)):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "ATLAS_PATH_INVALID"):
                atlas_worker.regular(path)

    def test_archive_rejects_encrypted_symlink_and_oversized_listings(self):
        link = zipfile.ZipInfo("grid.tif")
        link.external_attr = (stat.S_IFLNK | 0o777) << 16
        raw = io.BytesIO()
        with zipfile.ZipFile(raw, "w") as z:
            z.writestr(link, b"x")
        with zipfile.ZipFile(io.BytesIO(raw.getvalue())) as z, self.assertRaisesRegex(ValueError, "ATLAS_ARCHIVE_UNSAFE"):
            atlas_worker.archive_members(z)
        # zipfile clears flag_bits when writing, so the encrypted entry is presented directly.
        encrypted = zipfile.ZipInfo("grid.tif")
        encrypted.flag_bits = 0x1
        with self.assertRaisesRegex(ValueError, "ATLAS_ARCHIVE_UNSAFE"):
            atlas_worker.archive_members(mock.Mock(infolist=lambda: [encrypted]))
        fake = mock.Mock(infolist=lambda: [zipfile.ZipInfo(f"{i}.tif") for i in range(20001)])
        with self.assertRaisesRegex(ValueError, "ATLAS_ARCHIVE_MEMBER_LIMIT"):
            atlas_worker.archive_members(fake)

    def test_worker_errors_are_coded_and_never_echo_internals(self):
        self.assertEqual({"error": "ATLAS_PATH_INVALID"}, self.run_worker({"path": "relative.tif", "kind": "raster", "band": 1}))
        # A missing key or library raises an uncoded exception; only the generic code leaves the worker.
        self.assertEqual({"error": "ATLAS_SPATIAL_READER_FAILED"}, self.run_worker({"path": str(self.file)}))


class AtlasCatalogAndPreviewTests(AtlasTests):
    def test_catalog_filters_escape_like_wildcards_and_clamp_paging(self):
        (self.raw / "notes_100%.pdf").write_bytes(b"%PDF-1.4\n")
        intake.analyze(self.root)
        everything = self.model.catalog()
        self.assertEqual((2, "kfm-local-atlas-catalog/v1"), (everything["total"], everything["schema"]))
        by_name = {Path(i["relative_path"]).name: i for i in everything["items"]}
        self.assertEqual("vector", by_name["points.csv"]["preview"])
        self.assertEqual("unsupported", by_name["notes_100%.pdf"]["preview"])
        self.assertIn("historical-map tools", by_name["notes_100%.pdf"]["reason"])
        self.assertEqual(["notes_100%.pdf"], [Path(i["relative_path"]).name for i in self.model.catalog(text="100%")["items"]])
        # "%" is matched literally; as a LIKE wildcard it would also return points.csv.
        self.assertEqual(["notes_100%.pdf"], [Path(i["relative_path"]).name for i in self.model.catalog(text="%")["items"]])
        paged = self.model.catalog(limit=10_000, offset=-5)
        self.assertEqual((500, 0), (paged["limit"], paged["offset"]))
        self.assertEqual(1, self.model.catalog(limit=0)["limit"])
        self.assertEqual(0, self.model.catalog(lane="inbox")["total"])

    def test_catalog_bbox_uses_item_extents(self):
        inside = self.model.catalog(bbox=[-99, 37, -96, 40])["total"]
        outside = self.model.catalog(bbox=[10, 10, 11, 11])["total"]
        self.assertEqual((1, 0), (inside, outside))

    def test_preview_is_single_flight_and_file_kind_cannot_compare(self):
        self.model.render_lock.acquire()
        try:
            with self.assertRaisesRegex(ValueError, "ATLAS_PREVIEW_BUSY"):
                self.model.preview({"kind": "file", "id": self.item["id"]})
        finally:
            self.model.render_lock.release()
        with self.assertRaisesRegex(ValueError, "ATLAS_DIFFERENCE_REQUIRES_PRISM"):
            self.model.preview({"kind": "file", "id": self.item["id"], "compareId": self.item["id"]})
        with self.assertRaisesRegex(ValueError, "ATLAS_ITEM_NOT_FOUND"):
            self.model.preview({"kind": "file", "id": "0" * 32})
        self.assertTrue(self.model.render_lock.acquire(blocking=False))
        self.model.render_lock.release()

    def test_geojson_preview_rejects_foreign_crs_and_non_features(self):
        cases = {
            "ok.geojson": ({"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-98, 38]}, "properties": {"n": 1}}]}, None),
            "crs.geojson": ({"type": "FeatureCollection", "crs": {"properties": {"name": "EPSG:26914"}}, "features": []}, "ATLAS_GEOJSON_CRS_UNSUPPORTED"),
            "bare.geojson": ({"type": "Point", "coordinates": [-98, 38]}, "ATLAS_GEOJSON_INVALID"),
        }
        for name, (content, _) in cases.items():
            (self.raw / name).write_text(json.dumps(content))
        intake.analyze(self.root)
        items = {Path(i["relative_path"]).name: i for i in intake.list_items(self.root)["items"]}
        for name, (_, code) in cases.items():
            request = {"kind": "file", "id": items[name]["id"]}
            with self.subTest(name=name):
                if code is None:
                    value = self.model.preview(request)
                    self.assertEqual((1, ["n"]), (value["displayedCount"], value["numericFields"]))
                else:
                    with self.assertRaisesRegex(ValueError, code):
                        self.model.preview(request)

    def test_worker_process_failures_are_coded(self):
        path = self.file
        with self.assertRaisesRegex(ValueError, "ATLAS_SPATIAL_RUNTIME_UNAVAILABLE"):
            self.model._worker(path, "raster")
        model = atlas.Atlas(self.root, raster_python=Path(sys.executable))
        completed = subprocess.CompletedProcess([], 0, stdout='{"ok": true}', stderr="")
        with mock.patch.object(atlas.subprocess, "run", side_effect=subprocess.TimeoutExpired("worker", 28)), \
                self.assertRaisesRegex(ValueError, "ATLAS_PREVIEW_TIMEOUT"):
            model._worker(path, "raster")
        for result, code in ((subprocess.CompletedProcess([], 1, stdout="", stderr="boom"), "ATLAS_SPATIAL_READER_FAILED"),
                             (subprocess.CompletedProcess([], 0, stdout='{"error": "ATLAS_RASTER_OUTSIDE_KANSAS"}', stderr=""), "ATLAS_RASTER_OUTSIDE_KANSAS")):
            with self.subTest(code=code), mock.patch.object(atlas.subprocess, "run", return_value=result), \
                    self.assertRaisesRegex(ValueError, code):
                model._worker(path, "raster")

        def changes_source(*args, **kwargs):
            path.write_text(path.read_text() + "38,-96,1\n")
            return completed
        with mock.patch.object(atlas.subprocess, "run", side_effect=changes_source), \
                self.assertRaisesRegex(ValueError, "ATLAS_SOURCE_CHANGED"):
            model._worker(path, "raster")
        with mock.patch.object(atlas.subprocess, "run", return_value=completed) as run:
            self.assertEqual({"ok": True}, model._worker(path, "vector"))
        env = run.call_args.kwargs["env"]
        self.assertEqual("OFF", env["PROJ_NETWORK"])
        self.assertTrue(set(env) <= {"PATH", "LANG", "SYSTEMROOT", "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "PROJ_NETWORK", "GDAL_DISABLE_READDIR_ON_OPEN"})

    def test_real_worker_failure_surfaces_as_coded_error(self):
        # The test interpreter has no rasterio/pyshp, so the real worker fails closed with a code.
        model = atlas.Atlas(self.root, raster_python=Path(sys.executable))
        with self.assertRaisesRegex(ValueError, "ATLAS_SPATIAL_READER_FAILED"):
            model._worker(self.file.resolve(), "vector")


JAN = "normals/us/4km/ppt/monthly/PRISM_ppt_30yr_normal_4kmM4_202001_bil.zip"
FEB = "normals/us/4km/ppt/monthly/PRISM_ppt_30yr_normal_4kmM4_202002_bil.zip"
OTHER = "time_series/us/an/4km/tmean/daily/2024/prism_tmean_us_25m_20240101.zip"


class AtlasPrismTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "store"
        prism = self.root / atlas.PRISM_ROOT
        prism.mkdir(parents=True)
        self.geoids = [f"20{n:03d}" for n in range(1, 210, 2)]
        with sqlite3.connect(prism / "catalog.sqlite") as conn:
            conn.execute("CREATE TABLE grids (path TEXT, unit TEXT, processed_utc TEXT, source_metadata TEXT, status TEXT, tif_path TEXT, source_sha256 TEXT)")
            conn.execute("CREATE TABLE county_stats (path TEXT, county_geoid TEXT, mean REAL, minimum REAL, maximum REAL, valid_pixels INTEGER)")
            for path, unit, status in ((JAN, "mm", "complete"), (FEB, "mm", "complete"), (OTHER, "degC", "complete"),
                                       ("normals/us/4km/ppt/monthly/broken.zip", "mm", "complete"), (JAN.replace("202001", "202003"), "mm", "partial")):
                conn.execute("INSERT INTO grids VALUES (?,?,?,?,?,?,?)", (path, unit, "2026-10-01T00:00:00Z", json.dumps({"PRISM_DATASET_VERSION": "v1"}),
                                                                        status, path.replace(".zip", ".tif"), atlas.identity(path)))
            for i, geoid in enumerate(self.geoids):
                conn.execute("INSERT INTO county_stats VALUES (?,?,?,?,?,?)", (JAN, geoid, 10.0 + i, 9.0, 11.0 + i, 4))
                if geoid != self.geoids[0]:
                    conn.execute("INSERT INTO county_stats VALUES (?,?,?,?,?,?)", (FEB, geoid, 7.0 + i, 6.0, 8.0 + i, 4))
        counties = self.root / atlas.COUNTIES
        counties.parent.mkdir(parents=True)
        counties.write_text(json.dumps({"type": "FeatureCollection", "features": [
            {"type": "Feature", "properties": {"GEOID": geoid, "NAME": f"County {geoid}"},
             "geometry": {"type": "Point", "coordinates": [-101 + (i % 15) * 0.4, 37.2 + (i // 15) * 0.35]}}
            for i, geoid in enumerate(self.geoids)]}))
        self.model = atlas.Atlas(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def test_groups_and_frames_only_offer_complete_classified_grids(self):
        groups = self.model.groups()["groups"]
        self.assertEqual(2, len(groups))
        ppt = next(g for g in groups if g["variable"] == "ppt")
        self.assertEqual((2, "202001", "202002"), (ppt["frameCount"], ppt["start"], ppt["end"]))
        frames = self.model.frames(ppt["id"])
        self.assertEqual(["202002", "202001"], [f["key"] for f in frames["frames"]])
        self.assertEqual(1, self.model.frames(ppt["id"], offset=1, limit=1)["frames"].__len__())
        self.assertEqual(0, self.model.frames(ppt["id"], year="2019")["total"])
        for kwargs, code in (({"group": "missing"}, "ATLAS_GROUP_NOT_FOUND"), ({"group": ppt["id"], "year": "20x0"}, "ATLAS_YEAR_INVALID"),
                             ({"group": ppt["id"], "limit": 0}, "ATLAS_PAGING_INVALID"), ({"group": ppt["id"], "offset": -1}, "ATLAS_PAGING_INVALID")):
            with self.subTest(kwargs=kwargs), self.assertRaisesRegex(ValueError, code):
                self.model.frames(**kwargs)

    def test_county_choropleth_and_b_minus_a_difference(self):
        jan, feb = atlas.identity("prism:" + JAN), atlas.identity("prism:" + FEB)
        value = self.model.preview({"kind": "prism", "id": jan})
        self.assertEqual((105, ["value"], "mm"), (value["displayedCount"], value["numericFields"], value["units"]))
        self.assertEqual("climate normal", value["time"]["kind"])
        props = {f["properties"]["geoid"]: f["properties"] for f in value["data"]["features"]}
        self.assertEqual(10.0, props[self.geoids[0]]["value"])
        diff = self.model.preview({"kind": "prism", "id": feb, "compareId": jan})
        props = {f["properties"]["geoid"]: f["properties"] for f in diff["data"]["features"]}
        self.assertEqual(-3.0, props[self.geoids[1]]["value"])
        self.assertIsNone(props[self.geoids[0]]["value"])  # B missing for this county: no difference, not zero
        self.assertIn("B − A", diff["title"])
        self.assertEqual({"sha256A", "sha256B"} <= set(diff["source"]), True)

    def test_incompatible_or_missing_frames_and_bad_county_geometry_are_refused(self):
        jan, other = atlas.identity("prism:" + JAN), atlas.identity("prism:" + OTHER)
        for request, code in (({"kind": "prism", "id": "0" * 32}, "ATLAS_FRAME_NOT_FOUND"),
                              ({"kind": "prism", "id": jan, "compareId": "0" * 32}, "ATLAS_FRAME_NOT_FOUND"),
                              ({"kind": "prism", "id": jan, "compareId": other}, "ATLAS_DIFFERENCE_INCOMPATIBLE")):
            with self.subTest(code=code), self.assertRaisesRegex(ValueError, code):
                self.model.preview(request)
        counties = self.root / atlas.COUNTIES
        data = json.loads(counties.read_text())
        data["features"][1]["properties"]["GEOID"] = data["features"][0]["properties"]["GEOID"]
        counties.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "ATLAS_COUNTY_GEOMETRY_INVALID"):
            self.model.preview({"kind": "prism", "id": jan})

    def test_missing_catalog_is_reported(self):
        (self.root / atlas.PRISM_ROOT / "catalog.sqlite").unlink()
        with self.assertRaisesRegex(ValueError, "ATLAS_PRISM_NOT_AVAILABLE"):
            atlas.Atlas(self.root).groups()


if __name__ == "__main__":
    unittest.main()
