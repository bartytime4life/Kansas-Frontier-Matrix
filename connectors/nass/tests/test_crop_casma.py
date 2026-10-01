import importlib.util
from pathlib import Path
import unittest

MODULE = Path(__file__).resolve().parents[1] / "crop_casma.py"
spec = importlib.util.spec_from_file_location("crop_casma", MODULE)
crop = importlib.util.module_from_spec(spec)
spec.loader.exec_module(crop)


class CropCasmaPlanningTest(unittest.TestCase):
    def test_exact_day_and_kansas_scope(self):
        capabilities, coverage = crop.request_urls("2026-09-28")
        self.assertIn("GetCapabilities", capabilities)
        self.assertIn("SMAP-HYB-1KM-DAILY_2026.09.28_PM", coverage)
        self.assertIn("x%28-534000%2C125000%29", coverage)
        self.assertIn("y%281549000%2C1904000%29", coverage)
        self.assertNotIn("2026.09.27", coverage)

    def test_missing_or_malformed_availability_is_held(self):
        xml = b'<wcs:Capabilities xmlns:wcs="http://www.opengis.net/wcs/2.0"><wcs:CoverageId>SMAP-HYB-1KM-DAILY_2026.09.28_PM</wcs:CoverageId></wcs:Capabilities>'
        self.assertTrue(crop.advertised(xml, "2026-09-28"))
        self.assertFalse(crop.advertised(xml, "2026-09-27"))
        with self.assertRaises(crop.CaptureError):
            crop.advertised(b"<error>", "2026-09-28")
        with self.assertRaises(crop.CaptureError):
            crop.layer_name("2026-02-30")


if __name__ == "__main__":
    unittest.main()
