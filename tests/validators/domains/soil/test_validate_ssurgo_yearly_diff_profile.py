from __future__ import annotations

import importlib.util
import json
import socket
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = ROOT / "tools/validators/domains/soil/validate_ssurgo_yearly_diff_profile.py"
SPEC = importlib.util.spec_from_file_location("validate_ssurgo_yearly_diff_profile", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
CASES = ROOT / "fixtures/domains/soil/yearly_diff/cases.json"
PROFILE = ROOT / "pipeline_specs/soil/ssurgo_yearly_diff_profile.v1.json"
SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/ssurgo_yearly_diff_profile.schema.json"


class SoilYearlyDiffProfileTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_repository_profile_passes(self) -> None:
        result = MODULE.validate(PROFILE)
        self.assertEqual("PASS", result.outcome, result.findings)

    def test_fixture_manifest_has_exact_polarity(self) -> None:
        manifest = MODULE.load_fixture_manifest()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = MODULE.validate_payload(MODULE.materialize_case(manifest, case))
                actual = [
                    {"code": item.code, "field": item.field}
                    for item in result.findings
                ]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_source_roles_remain_distinct(self) -> None:
        manifest = MODULE.load_fixture_manifest()
        cases = {
            item["case_id"]: MODULE.materialize_case(manifest, item)
            for item in manifest["cases"]
        }
        ssurgo = cases["valid_ssurgo_no_change"]
        gnatsgo = cases["valid_gnatsgo_normalized_change"]
        self.assertEqual("AUTHORITATIVE_STATIC_SOIL_SURVEY", ssurgo["support_type"])
        self.assertEqual("GRIDDED_DERIVATIVE_SOIL", gnatsgo["support_type"])
        self.assertNotEqual(ssurgo["support_type"], gnatsgo["support_type"])

    def test_profile_is_non_publishing(self) -> None:
        profile = json.loads(PROFILE.read_text(encoding="utf-8"))
        self.assertIn(profile["output"]["target_zone"], {"WORK", "QUARANTINE"})
        self.assertIsNone(profile["provenance"]["publication_activity_ref"])
        self.assertTrue(all(value is False for value in profile["governance"].values()))

    def test_spec_hash_is_stable(self) -> None:
        profile = json.loads(PROFILE.read_text(encoding="utf-8"))
        declared = profile.pop("spec_hash")
        self.assertEqual(declared, MODULE.compute_spec_hash(profile))
        self.assertEqual(declared, MODULE.compute_spec_hash(profile))

    def test_fixture_runner_is_deterministic(self) -> None:
        self.assertEqual(0, MODULE.run_fixtures())
        self.assertEqual(0, MODULE.run_fixtures())

    def test_validation_does_not_open_network(self) -> None:
        def denied(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access denied")

        with mock.patch.object(socket, "socket", denied), mock.patch.object(
            socket, "create_connection", denied
        ), mock.patch.object(socket, "getaddrinfo", denied):
            self.assertEqual("PASS", MODULE.validate(PROFILE).outcome)
            self.assertEqual(0, MODULE.run_fixtures())


if __name__ == "__main__":
    unittest.main()
