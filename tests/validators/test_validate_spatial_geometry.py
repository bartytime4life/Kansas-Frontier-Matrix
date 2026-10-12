from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from hypothesis import given, seed, settings, strategies as st
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_spatial_geometry.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/spatial_geometry.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/spatial_geometry/cases.json"

SPEC = importlib.util.spec_from_file_location("validate_spatial_geometry", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

LONGITUDE = st.floats(
    min_value=-180,
    max_value=180,
    allow_nan=False,
    allow_infinity=False,
    width=32,
)
LATITUDE = st.floats(
    min_value=-90,
    max_value=90,
    allow_nan=False,
    allow_infinity=False,
    width=32,
)
POSITION = st.tuples(LONGITUDE, LATITUDE).map(list)


@st.composite
def rectangles(draw: st.DrawFn) -> list[list[float]]:
    west = draw(st.integers(min_value=-179, max_value=178))
    width = draw(st.integers(min_value=1, max_value=min(20, 180 - west)))
    south = draw(st.integers(min_value=-89, max_value=88))
    height = draw(st.integers(min_value=1, max_value=min(20, 90 - south)))
    east = west + width
    north = south + height
    return [
        [west, south],
        [east, south],
        [east, north],
        [west, north],
        [west, south],
    ]


def candidate(geometry_type: str, coordinates: object) -> dict[str, object]:
    return {
        "geometry": {"type": geometry_type, "coordinates": coordinates},
        "crs": "EPSG:4326",
        "precision_bucket": "region",
    }


class SpatialGeometryValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertEqual(schema["x-kfm"]["validator"], str(VALIDATOR_PATH.relative_to(REPO_ROOT)))

    def test_reviewed_fixture_profile_replays_exactly(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        lines = [json.loads(line) for line in completed.stdout.splitlines()]
        profile = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(len(lines), len(profile["cases"]))
        self.assertNotIn("FIXTURE_POLARITY_ERROR", completed.stdout)

    @seed(20260810)
    @settings(max_examples=80, deadline=None)
    @given(POSITION)
    def test_generated_valid_points_pass(self, position: list[float]) -> None:
        self.assertTrue(MODULE.validate_candidate(candidate("Point", position)).ok)

    @seed(20260811)
    @settings(max_examples=80, deadline=None)
    @given(st.lists(POSITION, min_size=2, max_size=20, unique_by=lambda item: tuple(item)))
    def test_generated_valid_lines_pass(self, line: list[list[float]]) -> None:
        self.assertTrue(MODULE.validate_candidate(candidate("LineString", line)).ok)

    @seed(20260812)
    @settings(max_examples=80, deadline=None)
    @given(rectangles())
    def test_generated_closed_rectangles_pass(self, ring: list[list[float]]) -> None:
        self.assertTrue(MODULE.validate_candidate(candidate("Polygon", [ring])).ok)

    @seed(20260813)
    @settings(max_examples=60, deadline=None)
    @given(rectangles())
    def test_generated_open_rings_fail_closed(self, ring: list[list[float]]) -> None:
        result = MODULE.validate_candidate(candidate("Polygon", [ring[:-1]]))
        self.assertIn("POLYGON_RING_OPEN", {finding.code for finding in result.findings})

    @seed(20260814)
    @settings(max_examples=80, deadline=None)
    @given(
        st.one_of(
            st.floats(min_value=180.0001, max_value=1e9, allow_nan=False, allow_infinity=False),
            st.floats(min_value=-1e9, max_value=-180.0001, allow_nan=False, allow_infinity=False),
        ),
        LATITUDE,
    )
    def test_generated_out_of_bounds_longitudes_fail(self, longitude: float, latitude: float) -> None:
        result = MODULE.validate_candidate(candidate("Point", [longitude, latitude]))
        self.assertIn("COORDINATE_OUT_OF_BOUNDS", {finding.code for finding in result.findings})

    @seed(20260815)
    @settings(max_examples=80, deadline=None)
    @given(POSITION)
    def test_generated_reports_are_deterministic_and_value_safe(self, position: list[float]) -> None:
        spatial = candidate("Point", position)
        first = MODULE._serialize("generated", MODULE.validate_candidate(spatial))
        second = MODULE._serialize("generated", MODULE.validate_candidate(spatial))
        self.assertEqual(first, second)
        self.assertNotIn(str(position[0]), first)
        self.assertNotIn(str(position[1]), first)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"geometry":{"type":"Point","coordinates":[0,0]},'
                '"crs":"EPSG:4326","crs":"EPSG:4326","precision_bucket":"coarse"}',
                encoding="utf-8",
            )
            result = MODULE.validate_spatial_geometry(path)
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_DUPLICATE_KEY"})

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text(
                '{"geometry":{"type":"Point","coordinates":[NaN,0]},'
                '"crs":"EPSG:4326","precision_bucket":"coarse"}',
                encoding="utf-8",
            )
            result = MODULE.validate_spatial_geometry(path)
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_NONFINITE_NUMBER"})

    def test_validator_has_no_network_or_geometry_repair_dependency(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        for denied in (
            "import requests",
            "import urllib",
            "import httpx",
            "import socket",
            "import shapely",
            "import geopandas",
            "import pyproj",
        ):
            self.assertNotIn(denied, source)


if __name__ == "__main__":
    unittest.main()
