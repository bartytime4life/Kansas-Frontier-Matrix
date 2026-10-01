import importlib.util
from hashlib import sha256
import json
from math import asinh, floor, pi, radians, tan
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import numpy as np
from PIL import Image
import rasterio
from rasterio.transform import from_origin

MODULE = Path(__file__).resolve().with_name("prepare.py")
spec = importlib.util.spec_from_file_location("crop_casma_prepare", MODULE)
prepare = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare)


class CropCasmaTilesTest(unittest.TestCase):
    def test_native_values_nodata_and_deterministic_tiles(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            capture = root / "capture"
            capture.mkdir()
            data = np.full((355, 659), 0.2, dtype=np.float32)
            data[180:, :] = -9999
            with rasterio.open(capture / "source.tif", "w", driver="GTiff", width=659, height=355,
                               count=1, dtype="float32", crs="EPSG:5070", nodata=-9999,
                               transform=from_origin(-534000, 1904000, 1000, 1000)) as dst:
                dst.write(data, 1)
            source_digest = "sha256:" + sha256((capture / "source.tif").read_bytes()).hexdigest()
            (capture / "manifest.json").write_text(json.dumps({"profile": "kfm.crop-casma-capture/v1",
                "state": "CAPTURED_CANDIDATE", "release_state": "UNRELEASED", "day": "2026-09-28",
                "layer": "SMAP-HYB-1KM-DAILY_2026.09.28_PM", "source_sha256": source_digest,
                "bounds_5070": [-534000, 1549000, 125000, 1904000]}))
            first = prepare.prepare(capture, root / "first")
            second = prepare.prepare(capture, root / "second")
            self.assertEqual(first["candidate_id"], second["candidate_id"])
            self.assertEqual(first["valid_cells"], 180 * 659)
            self.assertEqual(first["coverage_state"], "PARTIAL_AT_CHECKPOINTS")
            self.assertEqual([item["sha256"] for item in first["tiles"]], [item["sha256"] for item in second["tiles"]])
            # A Topeka pixel resolves to the original 0.2 cell, not a blended value.
            z, lon, lat = 9, -95.7, 39.1
            n = 2 ** z
            x_float = (lon + 180) / 360 * n
            y_float = (1 - asinh(tan(radians(lat))) / pi) / 2 * n
            x, y = floor(x_float), floor(y_float)
            with Image.open(root / "first" / "tiles" / str(z) / str(x) / f"{y}.png") as image:
                pixel = image.getpixel((floor((x_float - x) * 256), floor((y_float - y) * 256)))
            self.assertEqual(pixel[3], 255)
            self.assertTrue(all(abs(observed - expected) <= 1 for observed, expected in zip(pixel[:3], (233, 204, 99))))
            (capture / "source.tif").write_bytes(b"tampered")
            with self.assertRaisesRegex(ValueError, "SOURCE_DIGEST_MISMATCH"):
                prepare.prepare(capture, root / "third")


if __name__ == "__main__":
    unittest.main()
