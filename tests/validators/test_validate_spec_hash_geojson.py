"""Deterministic tests for structural GeoJSON feature digests."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "packages/hashing/src"))

from hashing import (  # noqa: E402
    GeoJSONDigestError,
    compute_geojson_feature_digests,
    geojson,
)


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
        a = compute_geojson_feature_digests(
            left, crs="EPSG:4326", excluded_property_keys=["updated_at"]
        )
        b = compute_geojson_feature_digests(
            right, crs="EPSG:4326", excluded_property_keys=["updated_at"]
        )
        self.assertEqual(a.record_sha256, b.record_sha256)
        self.assertNotEqual(
            a.geometry_sha256,
            compute_geojson_feature_digests(left, crs="EPSG:3857").geometry_sha256,
        )
        self.assertNotEqual(
            a.record_sha256,
            compute_geojson_feature_digests(
                left,
                crs="EPSG:4326",
                include_feature_id=True,
                excluded_property_keys=["updated_at"],
            ).record_sha256,
        )
        self.assertEqual(left, snapshot)
        with self.assertRaises(GeoJSONDigestError):
            compute_geojson_feature_digests({"type": "Feature", "geometry": None}, crs="EPSG:4326")

    def test_cli_is_deterministic_bounded_and_non_authoritative(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "feature.json"
            path.write_text(json.dumps( point()) + "\n", encoding="utf-8")
            command = [
                sys.executable,
                str(ROOT / "tools/spec_hash/spec_hash.py"),
                "geojson-feature",
                str(path),
                "--crs",
                "EPSG:4326",
                "--exclude-property",
                "updated_at",
            ]
            first = subprocess.run(command, check=False, capture_output=True, text=True)
            second = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertEqual((first.returncode, first.stdout), (0, second.stdout))
            payload = json.loads(first.stdout)
            self.assertEqual(
                (payload["status"], payload["authority"]),
                ("GEOJSON_FEATURE_DIGESTS_CREATED", "NONE"),
            )
            path.write_text('{"type":"Point","coordinates":[0,0]}\n', encoding="utf-8")
            failed = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertEqual(failed.returncode, 2)
            self.assertEqual(json.loads(failed.stdout)["status"], "GEOJSON_DIGEST_INPUT_INVALID")
            # A 401-digit integer used to escape as OverflowError with a traceback.
            path.write_text(
                '{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[1'
                + "0" * 400 + ',1]}}\n',
                encoding="utf-8",
            )
            overflow = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertEqual((overflow.returncode, overflow.stderr), (2, ""))
            self.assertEqual(json.loads(overflow.stdout)["status"], "GEOJSON_DIGEST_INPUT_INVALID")


def geometry(geometry_type: str, coordinates: object) -> dict:
    return {"type": geometry_type, "coordinates": coordinates}


class GeoJSONProfileBoundaryTests(unittest.TestCase):
    def test_parameters_are_validated(self) -> None:
        feature = point()
        for precision in (True, "7", 7.0, -1, 16):
            with self.subTest(precision=precision), self.assertRaises(GeoJSONDigestError):
                compute_geojson_feature_digests(feature, crs="EPSG:4326", coordinate_precision=precision)
        for crs in ("", "   ", None):
            with self.subTest(crs=crs), self.assertRaises(GeoJSONDigestError):
                compute_geojson_feature_digests(feature, crs=crs)
        for exclusions in ([""], [3]):
            with self.subTest(exclusions=exclusions), self.assertRaises(GeoJSONDigestError):
                compute_geojson_feature_digests(feature, crs="EPSG:4326", excluded_property_keys=exclusions)
        with self.assertRaises(GeoJSONDigestError):
            compute_geojson_feature_digests(feature, crs="EPSG:4326", include_feature_id="yes")
        trimmed = compute_geojson_feature_digests(feature, crs="  EPSG:4326 ", excluded_property_keys=["b", "a", "b"])
        self.assertEqual("EPSG:4326", trimmed.crs)
        self.assertEqual(("a", "b"), trimmed.excluded_property_keys)

    def test_coordinates_fail_closed(self) -> None:
        for value in (True, "1", None, float("nan"), float("inf"), 1e300, 10**400):
            with self.subTest(value=value), self.assertRaises(GeoJSONDigestError):
                geojson.normalize_geojson_geometry(geometry("Point", [value, 1]))
        for position in ([1], 1, {"x": 1}):
            with self.subTest(position=position), self.assertRaises(GeoJSONDigestError):
                geojson.normalize_geojson_geometry(geometry("Point", position))

    def test_quantization_rounds_half_even_and_folds_negative_zero(self) -> None:
        self.assertEqual(
            {"type": "Point", "coordinates": [1.2345678, 1.234568]},
            geojson.normalize_geojson_geometry(geometry("Point", [1.23456785, 1.23456795])),
        )
        self.assertEqual(
            {"type": "Point", "coordinates": [2, 4]},
            geojson.normalize_geojson_geometry(geometry("Point", [2.5, 3.5]), coordinate_precision=0),
        )
        self.assertEqual(
            geojson.compute_geojson_geometry_hash(geometry("Point", [-0.0, 1]), crs="EPSG:4326"),
            geojson.compute_geojson_geometry_hash(geometry("Point", [0, 1]), crs="EPSG:4326"),
        )

    def test_every_geometry_type_and_its_nesting(self) -> None:
        ring = [[0, 0], [1, 0], [1, 1], [0, 0]]
        valid = {
            "Point": [0, 0],
            "MultiPoint": [[0, 0], [1, 1]],
            "LineString": [[0, 0], [1, 1]],
            "MultiLineString": [[[0, 0], [1, 1]]],
            "Polygon": [ring],
            "MultiPolygon": [[ring]],
        }
        for geometry_type, coordinates in valid.items():
            with self.subTest(geometry_type=geometry_type):
                normalized = geojson.normalize_geojson_geometry(geometry(geometry_type, coordinates))
                self.assertEqual({"type": geometry_type, "coordinates": coordinates}, normalized)
                with self.assertRaises(GeoJSONDigestError):
                    geojson.normalize_geojson_geometry(geometry(geometry_type, 7))
        collection = {"type": "GeometryCollection", "geometries": [geometry("Point", [0, 0]), geometry("LineString", [[0, 0], [1, 1]])], "bbox": [0, 0, 1, 1]}
        self.assertNotIn("bbox", geojson.normalize_geojson_geometry(collection))
        self.assertIsNone(geojson.normalize_geojson_geometry(None))

    def test_malformed_geometries_fail_closed(self) -> None:
        nested = geometry("Point", [0, 0])
        for _ in range(geojson.MAX_GEOMETRY_DEPTH + 1):
            nested = {"type": "GeometryCollection", "geometries": [nested]}
        for value in (
            [0, 0],
            {"coordinates": [0, 0]},
            {"type": 1, "coordinates": [0, 0]},
            {"type": "Circle", "coordinates": [0, 0]},
            {"type": "Point"},
            {"type": "GeometryCollection"},
            {"type": "GeometryCollection", "geometries": [None]},
            nested,
        ):
            with self.subTest(value=str(value)[:60]), self.assertRaises(GeoJSONDigestError):
                geojson.normalize_geojson_geometry(value)

    def test_coordinate_budget_is_enforced(self) -> None:
        line = geometry("LineString", [[0, 0], [1, 1], [2, 2]])
        with mock.patch.object(geojson, "MAX_COORDINATE_VALUES", 5), self.assertRaises(GeoJSONDigestError):
            geojson.normalize_geojson_geometry(line)
        self.assertIsNotNone(geojson.normalize_geojson_geometry(line))

    def test_feature_envelope_is_validated(self) -> None:
        base = point()
        for feature in (
            [],
            {**base, "type": "FeatureCollection"},
            {key: value for key, value in base.items() if key != "geometry"},
            {key: value for key, value in base.items() if key != "properties"},
            {**base, "properties": ["status"]},
            {**base, "properties": {1: "numeric key"}},
        ):
            with self.subTest(feature=str(feature)[:60]), self.assertRaises(GeoJSONDigestError):
                compute_geojson_feature_digests(feature, crs="EPSG:4326")

    def test_null_properties_and_report_shape(self) -> None:
        empty = compute_geojson_feature_digests({**point(), "properties": {}}, crs="EPSG:4326")
        null = compute_geojson_feature_digests({**point(), "properties": None}, crs="EPSG:4326")
        self.assertEqual(empty.geometry_sha256, null.geometry_sha256)
        self.assertNotEqual(empty.record_sha256, null.record_sha256)
        self.assertEqual(
            null.geometry_sha256,
            geojson.compute_geojson_geometry_hash(point()["geometry"], crs="EPSG:4326"),
        )
        report = null.as_dict()
        self.assertEqual(
            ["coordinate_precision", "crs", "excluded_property_keys", "feature_id_included", "geometry_sha256", "profile", "record_sha256"],
            sorted(report),
        )
        self.assertEqual(geojson.GEOJSON_DIGEST_PROFILE, report["profile"])
        json.dumps(report)


if __name__ == "__main__":
    unittest.main()
