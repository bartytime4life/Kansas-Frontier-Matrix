"""Geometry checks: synthetic defects are test cases, not historical evidence."""
import datetime as dt
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("county_geometry", ROOT / "scripts/qualify-county-geometry.py")
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
try:
    pyproj, shapely = g.dependencies()
    from shapely.geometry import Polygon, box, shape
    AVAILABLE = True
except ImportError:
    AVAILABLE = False


def row(start=18610129, end=18611231):
    return {"START_N": start, "END_N": end}


@unittest.skipUnless(AVAILABLE, "Requires documented offline GIS dependencies")
class GeometryTests(unittest.TestCase):
    def test_invalid_polygon_and_nonpolygon_are_rejected_without_repair(self):
        bowtie = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
        geometries = [bowtie, shapely.Point(0, 0), Polygon()]
        self.assertEqual([r["recordNumber"] for r in g.individual_validity(geometries)], [1, 2, 3])
        with self.assertRaisesRegex(ValueError, "COVERAGE_REQUIRES_VALID_POLYGONS"):
            g.coverage_epochs([row()], [bowtie])
        self.assertFalse(bowtie.is_valid)

    def test_shared_edge_is_valid_and_holes_are_not_claimed_missing_data(self):
        shapes = [box(0, 0, 1, 1), box(1, 0, 2, 1)]
        epoch = g.selected_epoch(g.coverage_epochs([row(), row()], shapes), dt.date(1861, 1, 29))
        self.assertTrue(epoch["coverageValid"])
        self.assertEqual(epoch["interiorOverlapRecordPairs"], [])
        hole = Polygon([(0, 0), (4, 0), (4, 4), (0, 4), (0, 0)],
                       [[(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]])
        self.assertTrue(g.selected_epoch(g.coverage_epochs([row()], [hole]),
                                        dt.date(1861, 1, 29))["coverageValid"])

    def test_overlap_containment_and_duplicate_polygons_all_fail(self):
        for second in [box(1, 0, 3, 2), box(.5, .5, 1, 1), box(0, 0, 2, 2)]:
            with self.subTest(second=second):
                epoch = g.selected_epoch(g.coverage_epochs([row(), row()], [box(0, 0, 2, 2), second]),
                                         dt.date(1861, 1, 29))
                self.assertFalse(epoch["coverageValid"])
                self.assertEqual(epoch["interiorOverlapRecordPairs"], [[1, 2]])

    def test_temporally_disjoint_same_polygon_is_not_an_overlap(self):
        rows = [row(end=18610129), row(start=18610130)]
        epochs = g.coverage_epochs(rows, [box(0, 0, 1, 1)] * 2)
        self.assertEqual(g.selected_epoch(epochs, dt.date(1861, 1, 29))["featureCount"], 1)
        self.assertTrue(g.selected_epoch(epochs, dt.date(1861, 1, 30))["coverageValid"])

    def test_end_only_transition_and_empty_coverage_are_retained(self):
        epochs = g.coverage_epochs([row(end=18610129)], [box(0, 0, 1, 1)])
        after = g.selected_epoch(epochs, dt.date(1861, 1, 30))
        self.assertEqual(after["validFrom"], "1861-01-30")
        self.assertEqual(after["featureCount"], 0)
        self.assertFalse(after["coverageValid"])
        with self.assertRaisesRegex(ValueError, "SELECTED_EPOCH"):
            g.selected_epoch(epochs, dt.date(2001, 1, 1))

    def test_explicit_operation_and_axis_order(self):
        transformer, receipt = g.coordinate_operation(pyproj.CRS("EPSG:4269").to_wkt(),
                                                       [-114, 33, -89, 49])
        self.assertEqual(receipt["operationId"], "EPSG:1188")
        self.assertEqual(receipt["operationAccuracyMetres"], 4)
        self.assertEqual(transformer.transform(-98.5, 38.5, errcheck=True), (-98.5, 38.5))
        self.assertFalse(receipt["networkEnabled"])
        self.assertFalse(receipt["ballparkAllowed"])

    def test_wrong_crs_and_extent_fail(self):
        with self.assertRaisesRegex(ValueError, "SOURCE_CRS"):
            g.coordinate_operation(pyproj.CRS("EPSG:4326").to_wkt(), [-100, 37, -99, 38])
        with self.assertRaises(ValueError):
            g.coordinate_operation(pyproj.CRS("EPSG:4269").to_wkt(), [-180, -60, 180, 90])

    def test_unavailable_named_operation_cannot_fall_back(self):
        with patch("pyproj.transformer.TransformerGroup") as group:
            group.return_value.transformers = []
            with self.assertRaisesRegex(ValueError, "EPSG_1188_UNAVAILABLE"):
                g.coordinate_operation(pyproj.CRS("EPSG:4269").to_wkt(), [-100, 37, -99, 38])

    def test_invalid_day_precedes_file_access(self):
        for day in [dt.date(2001, 1, 1), "1861-01-29", None]:
            with self.subTest(day=day), self.assertRaisesRegex(ValueError, "DATE_COVERAGE"):
                g.prepare("nonexistent.zip", day)


@unittest.skipUnless(AVAILABLE and os.environ.get("KFM_COUNTY_ARCHIVE"),
                     "Requires GIS dependencies and exact KFM_COUNTY_ARCHIVE")
class RealArchiveGeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.environ["KFM_COUNTY_ARCHIVE"]
        cls.result = g.prepare(cls.path, dt.date(1861, 1, 29))

    def test_all_versions_and_all_coverage_epochs(self):
        report = self.result["geometryQualification"]
        self.assertEqual(self.result["counts"]["boundaryVersions"], 341)
        self.assertEqual(report["individualSourceInvalid"], [])
        self.assertEqual(report["individualTransformedInvalid"], [])
        epochs = report["sourceCoverageEpochs"]
        self.assertEqual(len(epochs), 71)
        self.assertEqual(epochs, report["transformedCoverageEpochs"])
        bad = [e for e in epochs if not e["coverageValid"]]
        self.assertEqual([(e["validFrom"], e["validToExclusive"]) for e in bad],
                         [("1873-03-20", "1874-02-25"), ("1874-02-25", "1874-03-18")])
        for epoch in bad:
            self.assertEqual(epoch["interiorOverlapRecordPairs"],
                             [[268, 269], [268, 271], [268, 276], [269, 276], [271, 276]])
        self.assertEqual({r["recordNumber"] for r in report["sourceRecordDiagnostics"]}, {268, 269, 271, 276})

    def test_statehood_candidate_retains_identity_evidence_and_geometry(self):
        result = self.result
        candidate = result["geometryCandidate"]
        self.assertEqual(len(candidate["features"]), 50)
        self.assertEqual(candidate["selectedDay"], "1861-01-29")
        self.assertEqual(candidate["lifecycle"], "WORK")
        self.assertFalse(candidate["releaseEligible"])
        self.assertEqual(result["status"], "HOLD")
        self.assertFalse(result["snapshot"]["geometryIncluded"])
        self.assertEqual(len(result["snapshot"]["eventOnlyRecordsOnDay"]), 52)
        self.assertEqual(len(result["snapshot"]["undatedNameCrossReferences"]), 16)
        self.assertEqual([f["id"] for f in candidate["features"]],
                         [r["id"] for r in result["snapshot"]["boundaryVersions"]])
        for f in candidate["features"]:
            geometry = shape(f["geometry"])
            self.assertTrue(geometry.is_valid)
            self.assertEqual(f["properties"]["geometrySha256"], g.digest(f["geometry"]))
            for ref in f["properties"]["evidenceRefs"]:
                self.assertIn(ref["artifactId"], candidate["evidenceBundle"]["artifacts"])
            polygons = list(geometry.geoms) if geometry.geom_type == "MultiPolygon" else [geometry]
            for polygon in polygons:
                self.assertTrue(polygon.exterior.is_ccw)
                self.assertTrue(all(not ring.is_ccw for ring in polygon.interiors))
        self.assertEqual(result["geometryQualification"]["candidateSha256"], g.digest(candidate))
        self.assertNotIn("crs", candidate)  # RFC 7946 longitude/latitude
        self.assertIn(candidate["coordinateOperation"]["sourceProjectionEvidenceRef"]["artifactId"],
                      candidate["evidenceBundle"]["artifacts"])
        self.assertEqual(result["geometryQualification"]["repairs"], [])

    def test_disputed_date_is_quarantined_and_resolution_date_is_separate(self):
        result = g.prepare(self.path, dt.date(1874, 3, 17))
        self.assertIsNone(result["geometryCandidate"])
        self.assertEqual(result["geometryQualification"]["candidateState"], "QUARANTINE")
        resolved = g.prepare(self.path, dt.date(1874, 3, 18))
        self.assertIsNotNone(resolved["geometryCandidate"])
        self.assertEqual(resolved["status"], "HOLD")

    def test_cli_matches_api_is_deterministic_and_returns_quarantine_code(self):
        command = [sys.executable, str(ROOT / "scripts/qualify-county-geometry.py"), self.path, "--date"]
        success = subprocess.run(command + ["1861-01-29"], capture_output=True, text=True)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertEqual(json.loads(success.stdout), json.loads(json.dumps(self.result)))
        held = subprocess.run(command + ["1873-03-20"], capture_output=True, text=True)
        self.assertEqual(held.returncode, 2, held.stderr)
        self.assertIsNone(json.loads(held.stdout)["geometryCandidate"])
        invalid = subprocess.run(command + ["2001-01-01"], capture_output=True, text=True)
        self.assertEqual(invalid.returncode, 1)
        self.assertNotIn("geometryCandidate", json.loads(invalid.stdout))


if __name__ == "__main__":
    unittest.main()
