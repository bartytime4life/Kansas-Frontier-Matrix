"""Exact official-product selection for on-demand Kansas sheets."""
import importlib.util
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[4] / "connectors/usgs/topoview/fetch_sheet.py"
spec = importlib.util.spec_from_file_location("kfm_topoview_fetch", SOURCE)
fetch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetch)


class ProductSelectionTests(unittest.TestCase):
    def setUp(self):
        self.original_fetch = fetch.fetch_json
        self.request = {"version": 1, "id": 4628, "scanId": 122705, "name": "Topeka", "year": 1889,
                        "scale": 125000, "state": "KS", "footprint": [[[-96, 39], [-95.5, 39], [-95.5, 39.5], [-96, 39.5]]]}
        self.product = {"title": "Historical Topographic Map Collection for Topeka, KS 1889 1:125000-scale",
                        "urls": {"GeoTIFF": "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/KS_Topeka_122705_1889_125000_geo.tif"}}

    def tearDown(self):
        fetch.fetch_json = self.original_fetch

    def test_exact_kansas_match_and_ambiguous_or_wrong_state_hold(self):
        fetch.fetch_json = lambda _url: {"items": [self.product], "total": 1}
        self.assertEqual(fetch.product_for_request(self.request), self.product)
        fetch.fetch_json = lambda _url: {"items": [self.product, self.product], "total": 2}
        with self.assertRaisesRegex(ValueError, "exact official GeoTIFF match"):
            fetch.product_for_request(self.request)
        with self.assertRaisesRegex(ValueError, "not a Kansas"):
            fetch.product_for_request({**self.request, "state": "OK"})


if __name__ == "__main__":
    unittest.main()
