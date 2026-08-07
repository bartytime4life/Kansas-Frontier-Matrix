"""Deterministic tests for structural GeoJSON feature digests."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "packages/hashing/src"))

from hashing import GeoJSONDigestError, compute_geojson_feature_digests  # noqa: E402


def point(*, x: float = 1.0, status: str = "open", updated: str = "a") -> dict:
    return {
        "type": "Feature",
        "id": "feature-1",
        "geometry": {"type": "Point", "coordinates": [x, 2]},
        "properties": {"status": status, "updated_at": updated},
    }


class GeoJSONFeatureDigestTests(unittest.TestCase):
    def test_golden_vector_and_structural_invariance(self) -> None:
        candidate = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [1, 2]},
            "properties": {"name": "alpha"},
        }
        result = compute_geojson_feature_digests(candidate, crs="EPSG:4326")
        self.assertEqual(
            result.geometry_sha256,
            "sha256:794d83ef220b209249067faba710e478316ef8855e89eef3f90b8765609fb2aa",
        )
        self.assertEqual(
            result.record_sha256,
            "sha256:b3fc04347950c0fef2990fe7c70e3c04d1f225c6f4e604a6f18702a34b05cbdc",
        )
        noisy = {
            "properties": {"name": "alpha"},
            "geometry": {"coordinates": [1.000000049, 2], "type": "Point", "bbox": [0, 0, 2, 3]},
            "type": "Feature",
        }
        self.assertEqual(result, compute_geojson_feature_digests(noisy, crs="EPSG:4326"))

    def test_domains_profiles_exclusions_and_fail_closed(self) -> None:
        left = point(status="open", updated="a")
        right = point(status="closed", updated="b")
        snapshot = copy.deepcopy(left)
        a = compute_geojson_feature_digests(left, crs="EPSG:4326")
        b = compute_geojson_feature_digests(right, crs="EPSG:4326")
        self.assertEqual(a.geometry_sha256, b.geometry_sha256)
        self.assertNotEqual(a.record_sha256, b.record_sha256)
        right["properties"]["status"] = "open"
        a = compute_geojson_feature_digests(left, crs="EPSG:4326", excluded_property_keys=["updated_at"])
        b = compute_geojson_feature_digests(right, crs="EPSG:4326", excluded_property_keys=["updated_at"])
        self.assertEqual(a.record_sha256, b.record_sha256)
        self.assertNotEqual(a.geometry_sha256, compute_geojson_feature_digests(left, crs="EPSG:3857").geometry_sha256)
        self.assertNotEqual(a.record_sha256, compute_geojson_feature_digests(left, crs="EPSG:4326", include_feature_id=True, excluded_property_keys=["updated_at"]).record_sha256)
        self.assertEqual(left, snapshot)
        with self.assertRaises(GeoJSONDigestError):
            compute_geojson_feature_digests({"type": "Feature", "geometry": None}, crs="EPSG:4326")

    def test_cli_is_deterministic_bounded_and_non_authoritative(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "feature.json"
            path.write_text(json.dumps(point()) + "\n", encoding="utf-8")
            command = [sys.executable, str(ROOT / "tools/spec_hash/spec_hash.py"), "geojson-feature", str(path), "--crs", "EPSG:4326", "--exclude-property", "updated_at"]
            first = subprocess.run(command, check=False, capture_output=True, text=True)
            second = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertEqual((first.returncode, first.stdout), (0, second.stdout))
            payload = json.loads(first.stdout)
            self.assertEqual((payload["status"], payload["authority"]), ("GEOJSON_FEATURE_DIGESTS_CREATED", "NONE"))
            path.write_text('{"type":"Point","coordinates":[0,0]}\n', encoding="utf-8")
            failed = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertEqual(failed.returncode, 2)
            self.assertEqual(json.loads(failed.stdout)["status"], "GEOJSON_DIGEST_INPUT_INVALID")


if __name__ == "__main__":
    unittest.main()
