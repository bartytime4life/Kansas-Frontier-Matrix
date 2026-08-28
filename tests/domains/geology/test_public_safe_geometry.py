"""Deterministic tests for the Geology public-safe geometry fixture profile."""

from __future__ import annotations

import copy
from collections import Counter
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import urllib.request

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators.geology.public_safe_geometry import (
    validate_public_safe_geometry as validator,
)


class GeologyPublicSafeGeometryTests(unittest.TestCase):
    def test_schema_is_valid_closed_and_non_authoritative(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        for field in ("source_geometry", "public_derivative", "governance", "assessment"):
            self.assertFalse(schema["properties"][field]["additionalProperties"])
        self.assertEqual("NONE", schema["x-kfm"]["authority"])
        self.assertEqual("DENIED", schema["x-kfm"]["coordinate_material"])
        self.assertEqual("UNWIRED", schema["x-kfm"]["release_and_publication"])

    def test_exact_fixture_matrix(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(
                    validator.materialize_case(manifest, case)
                )
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_is_two_holds_and_fail_closed_denials(self) -> None:
        manifest = validator.load_fixtures()
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"HOLD", "DENY"}, set(outcomes))
        self.assertEqual(2, outcomes["HOLD"])
        self.assertEqual(16, outcomes["DENY"])
        self.assertNotIn("ALLOW", outcomes)

    def test_clean_decision_cases_cover_generalized_withheld_and_exact(self) -> None:
        manifest = validator.load_fixtures()
        clean = {
            case["case_id"]: validator.validate_payload(
                validator.materialize_case(manifest, case)
            )
            for case in manifest["cases"][:4]
        }
        self.assertEqual("HOLD", clean["generalized-borehole-hold"].outcome)
        self.assertEqual("DENY", clean["withheld-sample-deny"].outcome)
        self.assertEqual("DENY", clean["exact-resource-location-deny"].outcome)
        self.assertEqual("HOLD", clean["generalized-boundary-hold"].outcome)
        for result in clean.values():
            self.assertFalse(result.findings)

    def test_all_materialized_fixtures_are_metadata_only_and_not_released(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            document = validator.materialize_case(manifest, case)
            with self.subTest(case=case["case_id"]):
                self.assertTrue(
                    document["source_geometry"]["geometry_ref"].startswith(
                        "kfm:fixture:"
                    )
                )
                public_ref = document["public_derivative"]["geometry_ref"]
                self.assertTrue(
                    public_ref is None or public_ref.startswith("kfm:fixture:")
                )
                self.assertIsNone(document["governance"]["release_manifest_ref"])
                if case["case_id"] != "release-claim-denied":
                    self.assertEqual(
                        "NOT_RELEASED", document["governance"]["release_state"]
                    )
                    self.assertFalse(
                        document["governance"]["publication_authorized"]
                    )

    def test_fixture_contains_no_coordinate_payload_or_live_endpoint(self) -> None:
        text = validator.FIXTURES.read_text(encoding="utf-8")
        for marker in (
            '"coordinates"',
            '"bbox"',
            '"centroid"',
            '"latitude"',
            '"longitude"',
            '"wkt"',
            '"wkb"',
            "https://",
        ):
            self.assertNotIn(marker, text)

    def test_undeclared_coordinate_field_fails_schema_closed(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        document["coordinates"] = [1, 2]
        result = validator.validate_payload(document)
        self.assertEqual("DENY", result.outcome)
        self.assertIn(validator.Finding("SCHEMA_INVALID", "/"), result.findings)

    def test_validation_is_no_network(self) -> None:
        manifest = validator.load_fixtures()
        denied = AssertionError("public-safe geometry validation attempted network access")
        with (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
            mock.patch.object(socket.socket, "connect_ex", side_effect=denied),
            mock.patch.object(socket, "create_connection", side_effect=denied),
            mock.patch.object(socket, "getaddrinfo", side_effect=denied),
            mock.patch.object(urllib.request, "urlopen", side_effect=denied),
        ):
            for case in manifest["cases"]:
                validator.validate_payload(validator.materialize_case(manifest, case))

    def test_identity_and_spec_hash_are_deterministic(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        expected_hash = document["spec_hash"]
        expected_id = document["assessment_id"]
        reordered = dict(reversed(list(copy.deepcopy(document).items())))
        self.assertEqual(expected_hash, validator.expected_spec_hash(reordered))
        self.assertEqual(expected_id, validator.expected_assessment_id(expected_hash))
        reordered["requested_surface"] = "PUBLIC_API"
        self.assertNotEqual(expected_hash, validator.expected_spec_hash(reordered))

    def test_fixture_cli_and_bounded_input_cli(self) -> None:
        fixture_run = subprocess.run(
            [sys.executable, str(Path(validator.__file__)), "--fixtures"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, fixture_run.returncode, fixture_run.stderr)
        suite = json.loads(fixture_run.stdout)
        self.assertTrue(suite["suite_match"])
        self.assertEqual(18, suite["case_count"])
        self.assertEqual("NONE", suite["authority"])

        manifest = validator.load_fixtures()
        hold = validator.materialize_case(manifest, manifest["cases"][0])
        deny = validator.materialize_case(manifest, manifest["cases"][2])
        with tempfile.TemporaryDirectory() as raw:
            hold_path = Path(raw) / "hold.json"
            deny_path = Path(raw) / "deny.json"
            hold_path.write_text(json.dumps(hold), encoding="utf-8")
            deny_path.write_text(json.dumps(deny), encoding="utf-8")
            hold_run = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(hold_path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            deny_run = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(deny_path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(0, hold_run.returncode, hold_run.stderr)
        self.assertEqual("HOLD", json.loads(hold_run.stdout)["outcome"])
        self.assertEqual(1, deny_run.returncode, deny_run.stderr)
        self.assertEqual("DENY", json.loads(deny_run.stdout)["outcome"])

    def test_duplicate_json_fails_without_echoing_candidate_value(self) -> None:
        sentinel = "EXACT_LOCATION_SENTINEL_THAT_MUST_NOT_ECHO"
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "duplicate.json"
            path.write_text(
                '{"profile_id":"first","profile_id":"' + sentinel + '"}',
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(2, completed.returncode)
        self.assertNotIn(sentinel, completed.stdout)
        payload = json.loads(completed.stdout)
        self.assertEqual("ERROR", payload["outcome"])
        self.assertEqual("FIXTURE_JSON_INVALID", payload["findings"][0]["code"])

    def test_validator_has_no_network_or_geometry_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in (
            "requests",
            "urllib.request",
            "httpx",
            "aiohttp",
            "shapely",
            "geopandas",
            "pyproj",
            "rasterio",
        ):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
