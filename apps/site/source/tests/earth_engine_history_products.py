"""Real-raster and provenance regressions for historical Landsat and PRISM preparation."""
from contextlib import contextmanager
from datetime import date, timedelta
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
from PIL import Image
from rasterio.io import MemoryFile
from rasterio.transform import Affine
from rasterio.warp import transform_geom

MODULE = Path(__file__).resolve().parents[1] / "scripts/earth-engine/prepare_display_set.py"
SPEC = importlib.util.spec_from_file_location("kfm_history_products", MODULE)
prepare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prepare)
SHA = "a" * 64
LANDSAT = {
    "ee-landsat4": ("LT04", 1982, 1993), "ee-landsat5": ("LT05", 1984, 2012),
    "ee-landsat7": ("LE07", 1999, 2024), "ee-landsat8": ("LC08", 2013, 2025),
    "ee-landsat9": ("LC09", 2021, 2025),
}
ALBERS = Affine(30, 0, -60000, 0, -30, 1590000)
PRISM = Affine(0.041666666667, 0, -125.0208333333335, 0, -0.041666666667, 49.9375000000005) * Affine.translation(600, 280)


def record(layer, ids):
    spec = prepare.LAYERS[layer]
    return {
        "status": "APPROVED_VISUAL_CONTEXT", "layerId": layer, "source": spec["source"],
        "sourceImageIds": ids, "sourceInventoryTaskId": "inventory-test",
        "sourceInventorySha256": SHA, "sampleTaskId": "sample-test", "statewideTaskId": "statewide-test",
        "sampleGeoTiffSha256": SHA, "statewideGeoTiffSha256": SHA, "masks": "QA and count reviewed",
        "terms": "test-only review", "processingParameters": "source-specific test fixture",
        "reviewer": "test steward", "approvedAt": "2026-10-06", "limits": "synthetic test raster",
        "samplePassed": True, "statewidePassed": True, "driveCapacityChecked": True, "termsChecked": True,
        "boundarySha256": SHA, "units": spec["unit"], "resampling": spec["resampling"],
        "nativeGridChecked": True, "periodBasis": "source-system-index",
    }


def scene(layer, year):
    return f"LANDSAT/{LANDSAT[layer][0]}/C02/T1_L2/{LANDSAT[layer][0]}_028033_{year}0601"


def prism_ids(layer, year):
    if layer == "ee-prism-monthly":
        return [f"OREGONSTATE/PRISM/ANm/{year}{month:02d}" for month in range(1, 13)]
    days = (date(year + 1, 1, 1) - date(year, 1, 1)).days
    return ["OREGONSTATE/PRISM/ANd/" + (date(year, 1, 1) + timedelta(days=i)).strftime("%Y%m%d") for i in range(days)]


@contextmanager
def raster(data, crs="EPSG:5070", transform=ALBERS, nodata=-9999):
    """Exercise GDAL-backed GeoTIFF readers rather than mock dataset objects."""
    with MemoryFile() as memory:
        with memory.open(driver="GTiff", height=data.shape[1], width=data.shape[2], count=data.shape[0],
                         dtype="float32", crs=crs, transform=transform, nodata=nodata) as out:
            out.write(data.astype("float32"))
        with memory.open() as source:
            yield source


def footprint(source):
    b = source.bounds
    polygon = {"type": "Polygon", "coordinates": [[[b.left, b.bottom], [b.right, b.bottom],
                [b.right, b.top], [b.left, b.top], [b.left, b.bottom]]]}
    return transform_geom(source.crs, "EPSG:4326", polygon)


class HistoricalProductTests(unittest.TestCase):
    def checked(self, layer, year, value):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review.json"
            path.write_text(json.dumps(value))
            return prepare.review(path, layer, year, SHA, SHA)

    def test_each_landsat_mission_keeps_its_own_boundary_years(self):
        for layer, (_, first, last) in LANDSAT.items():
            for year in [first, last]:
                with self.subTest(layer=layer, year=year):
                    self.checked(layer, year, record(layer, [scene(layer, year)]))
            for year in [first - 1, last + 1, True, str(first), float(first)]:
                with self.subTest(layer=layer, refused=year), self.assertRaises(ValueError):
                    prepare.check_source_year(layer, year)

    def test_landsat_rejects_cross_mission_collection_invalid_date_and_year(self):
        layer = "ee-landsat8"
        invalid = [
            "LANDSAT/LC09/C02/T1_L2/LC09_028033_20240601",
            "LANDSAT/LC08/C02/T1_L2/LC09_028033_20240601",
            "LANDSAT/LC08/C01/T1_L2/LC08_028033_20240601",
            "LANDSAT/LC08/C02/T1_L2/LC08_028033_20230229",
            "LANDSAT/LC08/C02/T1_L2/LC08_028033_20241301",
            scene(layer, 2023), scene(layer, 2024) + "/other",
        ]
        for identity in invalid:
            with self.subTest(identity=identity), self.assertRaises(ValueError):
                self.checked(layer, 2024, record(layer, [identity]))

    def test_landsat_duplicate_scene_ids_do_not_increase_provenance(self):
        identity = scene("ee-landsat7", 2004)
        with self.assertRaisesRegex(ValueError, "duplicates"):
            self.checked("ee-landsat7", 2004, record("ee-landsat7", [identity, identity]))

    def test_review_approval_and_original_hashes_remain_required(self):
        baseline = record("ee-landsat9", [scene("ee-landsat9", 2024)])
        for key, value in [("status", "CANDIDATE"), ("samplePassed", False), ("statewidePassed", False),
                           ("driveCapacityChecked", False), ("termsChecked", False),
                           ("masks", ""), ("sourceInventorySha256", "not-a-hash"),
                           ("units", "digital numbers"), ("boundarySha256", "b" * 64)]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.checked("ee-landsat9", 2024, {**baseline, key: value})

    def test_prism_full_label_membership_includes_leap_day(self):
        for layer, year in [("ee-prism-monthly", 1895), ("ee-prism-monthly", 2025),
                            ("ee-prism-daily", 1981), ("ee-prism-daily", 2024)]:
            ids = prism_ids(layer, year)
            with self.subTest(layer=layer, year=year):
                self.checked(layer, year, record(layer, ids))
                with self.assertRaises(ValueError):
                    self.checked(layer, year, record(layer, ids[:-1]))
                with self.assertRaises(ValueError):
                    self.checked(layer, year, record(layer, ids[:-1] + [ids[0]]))
                wrong = ids[:-1] + [ids[-1].replace(str(year), str(year + 1))]
                with self.assertRaises(ValueError):
                    self.checked(layer, year, record(layer, wrong))
        self.assertEqual(len(prism_ids("ee-prism-daily", 2024)), 366)
        self.assertIn("OREGONSTATE/PRISM/ANd/20240229", prism_ids("ee-prism-daily", 2024))

    def test_prism_requires_native_grid_and_label_period_review(self):
        layer = "ee-prism-monthly"
        baseline = record(layer, prism_ids(layer, 2024))
        for change in [{"nativeGridChecked": False}, {"periodBasis": "system-time-start"},
                       {"sourceImageIds": [value.replace("ANm", "ANd") for value in baseline["sourceImageIds"]]}]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.checked(layer, 2024, {**baseline, **change})
        for layer, year in [("ee-prism-monthly", 1894), ("ee-prism-daily", 1980),
                            ("ee-prism-monthly", 2026), ("ee-prism-daily", 2026)]:
            with self.subTest(layer=layer, year=year), self.assertRaises(ValueError):
                prepare.check_source_year(layer, year)

    def test_real_landsat_tiffs_accept_only_documented_four_band_30m_grid(self):
        data = np.full((4, 4, 4), 0.15, dtype="float32"); data[3] = 2
        for layer in LANDSAT:
            with self.subTest(layer=layer), raster(data) as source:
                prepare.check_grid(source, layer)
                self.assertEqual(prepare.coverage(source, footprint(source), layer, False, LANDSAT[layer][2]), 1)
        cases = [dict(crs="EPSG:4326"), dict(transform=ALBERS * Affine.translation(.5, 0)),
                 dict(transform=ALBERS * Affine.scale(2, 2)), dict(nodata=-32768)]
        for kwargs in cases:
            with self.subTest(kwargs=kwargs), raster(data, **kwargs) as source, self.assertRaises(ValueError):
                prepare.check_grid(source, "ee-landsat8")
        with raster(data[:3]) as source, self.assertRaises(ValueError):
            prepare.check_grid(source, "ee-landsat8")

    def test_rgb_coverage_refuses_empty_fractional_and_missing_samples(self):
        data = np.full((4, 4, 4), 0.15, dtype="float32"); data[3] = 2
        for band, bad in [(3, 0), (3, .5), (3, np.nan), (3, np.inf), (2, -9999), (1, np.nan)]:
            broken = data.copy(); broken[band, 1, 1] = bad
            with self.subTest(band=band, bad=bad), raster(broken) as source, self.assertRaisesRegex(ValueError, "coverage"):
                prepare.coverage(source, footprint(source), "ee-landsat8", False, 2024)
        data[1] = 1.51
        with raster(data) as source, self.assertRaisesRegex(ValueError, "outside reviewed"):
            prepare.coverage(source, footprint(source), "ee-landsat8", False, 2024)

    def test_real_prism_tiffs_preserve_nad83_native_grid_not_terraclimate_grid(self):
        data = np.full((2, 4, 4), 600, dtype="float32"); data[1] = 12
        for layer in ["ee-prism-monthly", "ee-prism-daily"]:
            with self.subTest(layer=layer), raster(data, crs="EPSG:4269", transform=PRISM) as source:
                prepare.check_grid(source, layer)
        for crs, transform in [("EPSG:4326", PRISM), ("EPSG:4269", PRISM * Affine.translation(.5, 0)),
                               ("EPSG:4269", PRISM * Affine.scale(2, 2)), ("EPSG:5070", ALBERS)]:
            with self.subTest(crs=crs, transform=transform), raster(data, crs=crs, transform=transform) as source, self.assertRaises(ValueError):
                prepare.check_grid(source, "ee-prism-monthly")

    def test_prism_coverage_requires_every_month_or_day_and_plausible_mm(self):
        for layer, year, expected in [("ee-prism-monthly", 1895, 12), ("ee-prism-daily", 2023, 365), ("ee-prism-daily", 2024, 366)]:
            data = np.full((2, 4, 4), 600, dtype="float32"); data[1] = expected
            with self.subTest(layer=layer, year=year), raster(data, crs="EPSG:4269", transform=PRISM) as source:
                self.assertEqual(prepare.coverage(source, footprint(source), layer, False, year), 1)
            data[1, 0, 0] = expected - 1
            with raster(data, crs="EPSG:4269", transform=PRISM) as source, self.assertRaisesRegex(ValueError, "coverage"):
                prepare.coverage(source, footprint(source), layer, False, year)
        data[1] = 366; data[0] = 5001
        with raster(data, crs="EPSG:4269", transform=PRISM) as source, self.assertRaisesRegex(ValueError, "outside reviewed"):
            prepare.coverage(source, footprint(source), "ee-prism-daily", False, 2024)

    def test_colorization_preserves_rgb_order_and_missing_pixel_transparency(self):
        data = np.zeros((4, 256, 256), dtype="float32"); data[:, 2, 3] = [0, .15, .3, 1]
        good = np.zeros((256, 256), dtype=bool); good[2, 3] = True
        for layer in LANDSAT:
            with self.subTest(layer=layer):
                image = prepare.colorize(data, good, layer, {})
                self.assertEqual(image[2, 3].tolist(), [0, 143, 255, 255])
                self.assertEqual(image[0, 0].tolist(), [0, 0, 0, 0])

    def test_prism_mm_ramp_and_outside_mask_stay_explicit(self):
        data = np.zeros((2, 256, 256), dtype="float32"); good = np.zeros((256, 256), dtype=bool)
        data[0, 0, :3] = [0, 600, 1200]; good[0, :3] = True
        for layer in ["ee-prism-monthly", "ee-prism-daily"]:
            image = prepare.colorize(data, good, layer, {})
            self.assertEqual(image[0, :3].tolist(), [[255, 244, 194, 255], [121, 201, 188, 255], [35, 92, 168, 255]])
            self.assertEqual(int(image[1:, :, 3].sum()), 0)

    def test_real_tile_render_never_promotes_missing_landsat_count_to_color(self):
        data = np.full((4, 4, 4), .15, dtype="float32"); data[3] = 0
        with tempfile.TemporaryDirectory() as directory, raster(data) as source, patch.object(prepare, "MIN_ZOOM", 12):
            root = Path(directory)
            prepare.render_tiles(source, "ee-landsat8", root, "ks-2024-test", footprint(source), {}, 2024)
            tiles = list(root.rglob("*.png")); self.assertTrue(tiles)
            for tile in tiles:
                with Image.open(tile) as image:
                    self.assertEqual(int(np.asarray(image)[:, :, 3].sum()), 0)


if __name__ == "__main__":
    unittest.main()
