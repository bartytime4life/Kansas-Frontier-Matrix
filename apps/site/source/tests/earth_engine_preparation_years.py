"""Year-specific review gates for private Earth Engine display preparation."""
import importlib.util
import json
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts/earth-engine/prepare_display_set.py"
SPEC = importlib.util.spec_from_file_location("kfm_ee_prepare", MODULE)
prepare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prepare)
SHA = "a" * 64


def record(layer, ids):
    spec = prepare.LAYERS[layer]
    return {
        "status": "APPROVED_VISUAL_CONTEXT", "layerId": layer, "source": spec["source"],
        "sourceImageIds": ids, "sourceInventoryTaskId": "inventory-task",
        "sourceInventorySha256": SHA, "sampleTaskId": "sample-task",
        "statewideTaskId": "statewide-task", "sampleGeoTiffSha256": SHA,
        "statewideGeoTiffSha256": SHA, "masks": "checked", "terms": "checked",
        "processingParameters": "checked", "reviewer": "steward", "approvedAt": "2026-09-30",
        "limits": "reviewed visual context", "samplePassed": True, "statewidePassed": True,
        "driveCapacityChecked": True, "termsChecked": True, "boundarySha256": SHA,
        "units": spec["unit"], "resampling": spec["resampling"], "paletteSha256": SHA,
    }


class HistoricalReviewTests(unittest.TestCase):
    def checked(self, layer, year, value):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "review.json"
            path.write_text(json.dumps(value))
            return prepare.review(path, layer, year, SHA, SHA)

    def test_chirps_requires_every_day_of_the_requested_year(self):
        for year, expected in ((2023, 365), (2024, 366)):
            ids = ["UCSB-CHG/CHIRPS/DAILY/" + (date(year, 1, 1) + timedelta(days=i)).strftime("%Y%m%d") for i in range(expected)]
            self.assertEqual(prepare.expected_days(year), expected)
            self.assertEqual(len(self.checked("ee-chirps", year, record("ee-chirps", ids))["sourceImageIds"]), expected)
            with self.assertRaisesRegex(ValueError, "complete period"):
                self.checked("ee-chirps", year, record("ee-chirps", ids[:-1]))
            with self.assertRaisesRegex(ValueError, "every .* day"):
                self.checked("ee-chirps", year, record("ee-chirps", ids[:-1] + ["UCSB-CHG/CHIRPS/DAILY/20250101"]))

    def test_cdl_historical_palette_and_exact_year(self):
        old = record("ee-cdl", ["USDA/NASS/CDL/2012"])
        with self.assertRaisesRegex(ValueError, "historical CDL class"):
            self.checked("ee-cdl", 2012, old)
        old["historicalClassKeyChecked"] = True
        self.checked("ee-cdl", 2012, old)
        with self.assertRaisesRegex(ValueError, "exact 2013"):
            self.checked("ee-cdl", 2013, old)

    def test_terraclimate_and_sentinel_cannot_relabel_years(self):
        monthly = record("ee-terraclimate", [f"IDAHO_EPSCOR/TERRACLIMATE/1999{month:02d}" for month in range(1, 13)])
        self.checked("ee-terraclimate", 1999, monthly)
        with self.assertRaisesRegex(ValueError, "every 2000 month"):
            self.checked("ee-terraclimate", 2000, monthly)
        scenes = record("ee-sentinel2", ["COPERNICUS/S2_SR_HARMONIZED/20190601T000000_20190601T000000_T14SNL"])
        self.checked("ee-sentinel2", 2019, scenes)
        with self.assertRaisesRegex(ValueError, "entirely from 2020"):
            self.checked("ee-sentinel2", 2020, scenes)


if __name__ == "__main__":
    unittest.main()
