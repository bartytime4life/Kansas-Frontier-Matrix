from hashlib import sha256
import json
from pathlib import Path
from runpy import run_path
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parents[1]
REFRESH = run_path(str(ROOT / "scripts/stage-science-refresh.py"))
LAB = "heat-and-rain"


def bundle(root, *, end="2025-12-31", capture="2026-11-27T00:00:00Z", source="a", value=5):
    period = {"from": "2020-01-01", "to": end}
    path = "science-data/daily-climate/sample.json"
    raw = json.dumps({"period": period, "records": [{"date": end, "tmax": value}]}).encode()
    asset = root / "public" / path
    asset.parent.mkdir(parents=True)
    asset.write_bytes(raw)
    manifest = root / REFRESH["MANIFEST"].format(LAB)
    manifest.parent.mkdir(parents=True)
    manifest.write_text(json.dumps({
        "period": period, "schema": "manifest/v1", "provider": "Example provider", "scope": "provider-context",
        "stations": [{
            "url": "/" + path, "id": "sample", "bytes": len(raw), "sha256": sha256(raw).hexdigest(),
            "source": {"url": "https://example.org/sample", "sha256": source * 64, "capturedAt": capture},
        }],
    }))
    return asset


class TestScienceRefresh(unittest.TestCase):
    def test_current_bundles_have_matching_assets(self):
        for _, labs in REFRESH["LANES"].values():
            for lab in labs:
                with self.subTest(lab=lab):
                    result = REFRESH["assess"](ROOT, ROOT, lab)
                    self.assertEqual(result["changedSourceObjects"], 0)
                    self.assertFalse(result["observationsChanged"])

    def test_same_bytes_do_not_look_like_an_update(self):
        with TemporaryDirectory() as directory:
            old = Path(directory) / "old"
            new = Path(directory) / "new"
            bundle(old)
            bundle(new, capture="2026-11-28T00:00:00Z")
            result = REFRESH["assess"](old, new, LAB)
            self.assertEqual(result["changedSourceObjects"], 0)
            self.assertFalse(result["observationsChanged"])

    def test_source_changes_and_observation_changes_are_counted_independently(self):
        with TemporaryDirectory() as directory:
            old = Path(directory) / "old"
            new = Path(directory) / "new"
            bundle(old)
            bundle(new, capture="2026-11-28T00:00:00Z", source="b")
            result = REFRESH["assess"](old, new, LAB)
            self.assertEqual(result["changedSourceObjects"], 1)
            self.assertFalse(result["observationsChanged"])

    def test_hold_corruption_older_captures_and_window_regressions(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            bundle(root / "old")
            damaged = bundle(root / "damaged")
            damaged.write_bytes(b"unexpected")
            bundle(root / "older", capture="2026-11-26T00:00:00Z", source="b")
            bundle(root / "shorter", end="2025-12-30")
            for candidate, reason in {
                "damaged": "SNAPSHOT_INTEGRITY_MISMATCH",
                "older": "OLDER_SOURCE_CAPTURE",
                "shorter": "COVERAGE_WINDOW_REGRESSION",
            }.items():
                with self.subTest(candidate=candidate), self.assertRaisesRegex(ValueError, reason):
                    REFRESH["assess"](root / "old", root / candidate, LAB)


if __name__ == "__main__":
    unittest.main()
