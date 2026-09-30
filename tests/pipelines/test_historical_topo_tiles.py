"""A georeferenced source stays aligned and deterministic across tile zooms."""
import importlib.util
import json
import math
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import numpy as np
from PIL import Image
import rasterio
from rasterio.transform import from_origin
from rasterio.warp import transform

SOURCE = Path(__file__).resolve().parents[2] / "pipelines/normalize/geography/historical_topo_tiles.py"
spec = importlib.util.spec_from_file_location("kfm_historical_topo_tiles", SOURCE)
tiles = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tiles)


class GeoreferencedTileTests(unittest.TestCase):
    def test_alignment_and_deterministic_rerun(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            original = root / "122705.tif"
            pixels = np.zeros((3, 64, 64), dtype=np.uint8)
            pixels[0] = 220
            pixels[1] = 45
            pixels[2] = 15
            with rasterio.open(original, "w", driver="GTiff", width=64, height=64, count=3,
                               dtype="uint8", crs="EPSG:4326", transform=from_origin(-96, 39.1, .002, .002)) as dst:
                dst.write(pixels)
            receipt = root / "122705.capture.json"
            receipt.write_text(json.dumps({"version": 1, "sheet": {"id": 4628, "scanId": 122705,
                "name": "Topeka", "year": 1889, "scale": 125000, "state": "KS"},
                "geotiff": {"url": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/KS_Topeka_122705_1889_125000_geo.tif",
                            "sha256": tiles.sha256(original), "bytes": original.stat().st_size},
                "retrievedAt": "2026-09-30T00:00:00Z"}))
            first = tiles.prepare(receipt, root / "first")
            second = tiles.prepare(receipt, root / "second")
            one, two = (json.loads((folder / "manifest.json").read_text()) for folder in (first, second))
            self.assertEqual(one, two)
            self.assertEqual(one["bounds"], two["bounds"])
            self.assertGreater(one["maxZoom"], one["minZoom"])
            east, north = transform("EPSG:4326", "EPSG:3857", [-95.936], [39.036])
            for z in (one["minZoom"], one["maxZoom"]):
                tile_width = 2 * tiles.ORIGIN / 2 ** z
                x = math.floor((east[0] + tiles.ORIGIN) / tile_width)
                y = math.floor((tiles.ORIGIN - north[0]) / tile_width)
                address = f"{z}/{x}/{y}"
                self.assertIn(address, one["tiles"])
                west, south, _, top = tiles.tile_bounds(z, x, y)
                px = min(255, max(0, int((east[0] - west) / tile_width * 256)))
                py = min(255, max(0, int((top - north[0]) / tile_width * 256)))
                with Image.open(first / "tiles" / f"{address}.png") as image:
                    self.assertEqual(image.getpixel((px, py)), (220, 45, 15, 255))

    def test_kansas_border_sheet_preserves_cross_border_pixels(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            original = root / "123456.tif"
            pixels = np.full((3, 64, 64), 180, dtype=np.uint8)
            with rasterio.open(original, "w", driver="GTiff", width=64, height=64, count=3,
                               dtype="uint8", crs="EPSG:4326", transform=from_origin(-97.1, 37.05, .002, .002)) as dst:
                dst.write(pixels)
            receipt = root / "123456.capture.json"
            receipt.write_text(json.dumps({"version": 1, "sheet": {"id": 1, "scanId": 123456,
                "name": "Kansas border fixture", "year": 1950, "scale": 125000, "state": "KS"},
                "geotiff": {"url": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/KS_Kansas_border_fixture_123456_1950_125000_geo.tif",
                            "sha256": tiles.sha256(original), "bytes": original.stat().st_size},
                "retrievedAt": "2026-09-30T00:00:00Z"}))
            package = tiles.prepare(receipt, root / "packages")
            manifest = json.loads((package / "manifest.json").read_text())
            self.assertLess(manifest["bounds"][1], 37)
            self.assertGreater(manifest["bounds"][3], 37)
            self.assertGreater(len(manifest["tiles"]), 0)


if __name__ == "__main__":
    unittest.main()
