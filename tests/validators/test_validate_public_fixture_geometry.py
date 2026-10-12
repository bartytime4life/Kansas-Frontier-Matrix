from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/sensitive_geometry/validate_public_fixture_geometry.py"
)

spec = importlib.util.spec_from_file_location(
    "validate_public_fixture_geometry",
    VALIDATOR_PATH,
)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)

PRECISE_POINT = {"type": "Point", "coordinates": [-98.123456, 38.123456]}
COARSE_POINT = {"type": "Point", "coordinates": [-98.25, 38.5]}


def _codes(document: object) -> set[str]:
    return {finding.code for finding in validator.validate_document(document)}


class PublicFixtureGeometryDocumentTests(unittest.TestCase):
    def test_precise_geometry_without_declaration_fails(self):
        self.assertEqual(
            _codes({"geometry": PRECISE_POINT}),
            {"PRECISE_GEOMETRY_WITHOUT_NON_PUBLIC_DECLARATION"},
        )

    def test_coarse_and_integer_geometry_passes(self):
        self.assertEqual(_codes({"geometry": COARSE_POINT}), set())
        self.assertEqual(
            _codes({"geometry": {"type": "Point", "coordinates": [-98, 38]}}),
            set(),
        )

    def test_nested_feature_geometry_is_scanned(self):
        document = {
            "type": "FeatureCollection",
            "features": [
                {"type": "Feature", "geometry": COARSE_POINT},
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [[-98.0, 38.0], [-97.1234, 38.0], [-97.0, 39.0], [-98.0, 38.0]]
                        ],
                    },
                },
            ],
        }
        findings = validator.validate_document(document)
        self.assertEqual(
            [finding.path for finding in findings],
            ["$.features[1].geometry.coordinates"],
        )

    def test_explicit_non_public_declarations_pass(self):
        governed = {
            "spatial": {"geometry": PRECISE_POINT},
            "governance": {"public_use_allowed": False},
        }
        exposure = {
            "spatial": {
                "geometry": PRECISE_POINT,
                "coordinate_exposure": "INTERNAL_EXACT",
            }
        }
        top_level = {"public_use_allowed": False, "geometry": PRECISE_POINT}
        for name, document in (
            ("governance", governed),
            ("exposure", exposure),
            ("top_level", top_level),
        ):
            with self.subTest(declaration=name):
                self.assertEqual(_codes(document), set())

    def test_public_declaration_fails_even_with_non_public_signal(self):
        self.assertEqual(
            _codes({"public_use_allowed": True, "geometry": PRECISE_POINT}),
            {"PRECISE_GEOMETRY_DECLARED_PUBLIC"},
        )
        conflicting = {
            "governance": {"public_use_allowed": True},
            "spatial": {
                "geometry": PRECISE_POINT,
                "coordinate_exposure": "INTERNAL_EXACT",
            },
        }
        self.assertEqual(_codes(conflicting), {"PRECISE_GEOMETRY_DECLARED_PUBLIC"})
        self.assertEqual(
            _codes({"geometry": PRECISE_POINT, "coordinate_exposure": "PUBLIC_EXACT"}),
            {"PRECISE_GEOMETRY_DECLARED_PUBLIC"},
        )

    def test_declaration_on_sibling_record_does_not_cover_location(self):
        document = {
            "records": [
                {"public_use_allowed": False},
                {"geometry": PRECISE_POINT},
            ]
        }
        self.assertEqual(
            _codes(document),
            {"PRECISE_GEOMETRY_WITHOUT_NON_PUBLIC_DECLARATION"},
        )

    def test_latitude_longitude_aliases_are_detected(self):
        for lat_key, lon_key in (
            ("latitude", "longitude"),
            ("lat", "lon"),
            ("lat", "lng"),
            ("decimalLatitude", "decimalLongitude"),
        ):
            with self.subTest(lat=lat_key):
                document = {lat_key: 38.123456, lon_key: -98.123456}
                self.assertEqual(
                    _codes(document),
                    {"PRECISE_GEOMETRY_WITHOUT_NON_PUBLIC_DECLARATION"},
                )
        self.assertEqual(_codes({"latitude": 38.5, "longitude": -98.5}), set())

    def test_bbox_wkt_and_embedded_json_are_detected(self):
        precise = (
            {"bbox": [-98.1234, 38.0, -97.0, 39.0]},
            {"location": "POINT(-98.123456 38.123456)"},
            {"location": "SRID=4326;POINT Z (-98.1234 38.5 10)"},
            {"payload": json.dumps({"geometry": PRECISE_POINT})},
        )
        for document in precise:
            with self.subTest(document=next(iter(document))):
                self.assertEqual(
                    _codes(document),
                    {"PRECISE_GEOMETRY_WITHOUT_NON_PUBLIC_DECLARATION"},
                )
        self.assertEqual(_codes({"location": "POINT(-98 38)"}), set())
        self.assertEqual(_codes({"bbox": [-102.0, 37.0, -94.6, 40.0]}), set())

    def test_non_numeric_values_are_not_positions(self):
        self.assertEqual(_codes({"coordinates": [True, False]}), set())
        self.assertEqual(_codes({"coordinates": ["-98.123456", "38.123456"]}), set())
        self.assertEqual(_codes({"lat": "38.123456", "lon": "-98.123456"}), set())


class PublicFixtureGeometryFileTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        repo_root_patch = patch.object(validator, "REPO_ROOT", self.root.resolve())
        repo_root_patch.start()
        self.addCleanup(repo_root_patch.stop)

    def _write(self, relative: str, payload: object) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        text = payload if isinstance(payload, str) else json.dumps(payload)
        path.write_text(text, encoding="utf-8")
        return path

    def _validate(self, exemptions: dict[str, str] | None = None):
        return validator.validate_paths([self.root / "fixtures"], exemptions or {})

    def test_expected_negative_lanes_are_skipped(self):
        for lane in ("invalid", "semantic_invalid", "schema_invalid", "deny", "invalid_case"):
            self._write(f"fixtures/a/{lane}/case.json", {"geometry": PRECISE_POINT})
        self._write("fixtures/a/valid/case.json", {"geometry": PRECISE_POINT})
        scanned, findings = self._validate()
        self.assertEqual(scanned, 1)
        self.assertEqual(
            [(finding.file, finding.code) for finding in findings],
            [
                (
                    "fixtures/a/valid/case.json",
                    "PRECISE_GEOMETRY_WITHOUT_NON_PUBLIC_DECLARATION",
                )
            ],
        )

    def test_geojson_files_are_scanned_and_invalid_json_fails_closed(self):
        self._write("fixtures/a/area.geojson", {"geometry": PRECISE_POINT})
        self._write("fixtures/a/broken.json", "{not json")
        self._write("fixtures/a/nan.json", '{"lat": NaN, "lon": 1}')
        self._write("fixtures/a/deep.json", "[" * 5000 + "]" * 5000)
        _, findings = self._validate()
        self.assertEqual(
            {(finding.file, finding.code) for finding in findings},
            {
                ("fixtures/a/area.geojson", "PRECISE_GEOMETRY_WITHOUT_NON_PUBLIC_DECLARATION"),
                ("fixtures/a/broken.json", "FIXTURE_JSON_INVALID"),
                ("fixtures/a/nan.json", "FIXTURE_JSON_INVALID"),
                ("fixtures/a/deep.json", "FIXTURE_JSON_INVALID"),
            },
        )

    def test_exemption_suppresses_only_its_own_file(self):
        exempt = "fixtures/source/input/native.json"
        self._write(exempt, {"decimalLatitude": 38.123456, "decimalLongitude": -98.1})
        self._write("fixtures/source/input/other.json", {"geometry": PRECISE_POINT})
        _, findings = self._validate({exempt: "reviewed source-native input"})
        self.assertEqual(
            [finding.file for finding in findings],
            ["fixtures/source/input/other.json"],
        )

    def test_exemption_that_no_longer_matches_is_stale(self):
        coarse = "fixtures/source/input/coarse.json"
        missing = "fixtures/source/input/missing.json"
        self._write(coarse, {"geometry": COARSE_POINT})
        _, findings = self._validate({coarse: "reason", missing: "reason"})
        self.assertEqual(
            {(finding.file, finding.code) for finding in findings},
            {(coarse, "EXEMPTION_STALE"), (missing, "EXEMPTION_STALE")},
        )

    def test_exemption_outside_scanned_roots_is_not_reported(self):
        self._write("fixtures/a/valid/case.json", {"geometry": COARSE_POINT})
        _, findings = validator.validate_paths(
            [self.root / "fixtures/a"],
            {"fixtures/b/elsewhere.json": "reason"},
        )
        self.assertEqual(findings, [])

    def test_cli_reports_paths_without_coordinate_values(self):
        self._write("fixtures/a/valid/case.json", {"geometry": PRECISE_POINT})
        stdout = io.StringIO()
        with patch.object(validator, "EXEMPTIONS", {}), redirect_stdout(stdout):
            exit_code = validator.main([str(self.root / "fixtures")])
        self.assertEqual(exit_code, 1)
        output = stdout.getvalue()
        self.assertNotIn("123456", output)
        summary = json.loads(output.strip().splitlines()[-1])
        self.assertEqual(summary["status"], "FAIL")
        self.assertEqual(summary["findings"], 1)

    def test_cli_rejects_missing_path(self):
        with redirect_stderr(io.StringIO()):
            exit_code = validator.main([str(self.root / "absent")])
        self.assertEqual(exit_code, 2)


class RepositoryFixtureGeometryTests(unittest.TestCase):
    def test_repository_fixtures_pass(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = validator.main([])
        self.assertEqual(exit_code, 0, stdout.getvalue())

    def test_exemptions_reference_existing_fixtures(self):
        for relative, reason in validator.EXEMPTIONS.items():
            with self.subTest(path=relative):
                self.assertTrue((REPO_ROOT / relative).is_file())
                self.assertTrue(reason.strip())


if __name__ == "__main__":
    unittest.main()
