from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = (
    ROOT
    / "tools/validators/release/"
    "validate_tile_delivery_strategy_assessment.py"
)
SPEC = importlib.util.spec_from_file_location(
    "validate_tile_delivery_strategy_assessment",
    MODULE_PATH,
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TileDeliveryStrategyAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = MODULE.load_fixtures()
        cls.cases = {
            case["case_id"]: case for case in cls.manifest["cases"]
        }

    def candidate(self, case_id: str) -> dict[str, object]:
        return MODULE.materialize_case(self.manifest, self.cases[case_id])

    def test_schema_is_valid_and_closed(self) -> None:
        schema = json.loads(MODULE.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            schema["properties"]["object_type"]["const"],
            "TileDeliveryStrategyAssessment",
        )

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 20)
        self.assertTrue(all(result["ok"] for result in results), results)

    def test_all_finite_outcomes_are_covered(self) -> None:
        outcomes = {
            MODULE.validate_payload(self.candidate(case_id)).outcome
            for case_id in self.cases
        }
        self.assertEqual(outcomes, {"PASS", "HOLD", "DENY", "ERROR"})

    def test_each_strategy_has_one_coherent_pass(self) -> None:
        passing = {
            self.candidate(case_id)["declaration"]["selected_strategy"]
            for case_id in self.cases
            if case_id.startswith("pass_")
        }
        self.assertEqual(
            passing,
            {
                "PMTILES_ARCHIVE",
                "XYZ_SERVICE",
                "MARTIN_POSTGIS",
                "MBTILES_LOCAL",
            },
        )

    def test_strategy_specific_boundaries(self) -> None:
        pmtiles = self.candidate("pass_pmtiles_immutable_public_archive")
        self.assertEqual(MODULE.recommend_strategy(pmtiles), "PMTILES_ARCHIVE")
        self.assertTrue(pmtiles["declaration"]["public_safe_input"])
        self.assertTrue(pmtiles["declaration"]["range_hosting_ready"])
        self.assertIsNotNone(
            pmtiles["controls"]["tile_artifact_manifest_ref"]
        )

        xyz = self.candidate("pass_xyz_partial_mutation_service")
        self.assertEqual(MODULE.recommend_strategy(xyz), "XYZ_SERVICE")
        self.assertTrue(
            xyz["declaration"]["per_tile_invalidation_required"]
        )
        self.assertIsNotNone(
            xyz["controls"]["map_service_protocol_assessment_ref"]
        )

        martin = self.candidate("pass_martin_dynamic_steward_mediation")
        self.assertEqual(MODULE.recommend_strategy(martin), "MARTIN_POSTGIS")
        self.assertEqual(martin["declaration"]["audience"], "STEWARD")
        self.assertTrue(martin["declaration"]["server_mediation_required"])

        mbtiles = self.candidate("pass_mbtiles_local_offline_package")
        self.assertEqual(MODULE.recommend_strategy(mbtiles), "MBTILES_LOCAL")
        self.assertEqual(mbtiles["declaration"]["audience"], "LOCAL")
        self.assertTrue(mbtiles["declaration"]["offline_required"])

    def test_public_safety_and_mediation_fail_closed(self) -> None:
        expected = {
            "deny_public_unsafe_input": "PUBLIC_UNSAFE_INPUT_DENIED",
            "deny_public_mbtiles": "MBTILES_PUBLIC_DELIVERY_DENIED",
            "deny_public_access_control_conflict": (
                "PUBLIC_ACCESS_CONTROL_CONFLICT"
            ),
            "deny_static_delivery_bypasses_mediation": (
                "STATIC_DELIVERY_BYPASSES_MEDIATION"
            ),
        }
        for case_id, code in expected.items():
            with self.subTest(case_id=case_id):
                result = MODULE.validate_payload(self.candidate(case_id))
                self.assertEqual(result.outcome, "DENY")
                self.assertEqual(result.findings[0].code, code)

    def test_every_materialized_case_denies_operational_authority(self) -> None:
        for case_id in self.cases:
            with self.subTest(case_id=case_id):
                candidate = self.candidate(case_id)
                if case_id == "deny_authority_overclaim":
                    continue
                self.assertFalse(any(candidate["authority"].values()))
                self.assertFalse(candidate["assessment"]["execution_authorized"])

    def test_identity_binds_delivery_semantics(self) -> None:
        candidate = self.candidate("pass_pmtiles_immutable_public_archive")
        digest, assessment_id = MODULE.canonical_identity(candidate)
        self.assertEqual(candidate["spec_hash"], digest)
        self.assertEqual(candidate["assessment_id"], assessment_id)
        changed = copy.deepcopy(candidate)
        changed["declaration"]["range_hosting_ready"] = False
        self.assertNotEqual(digest, MODULE.canonical_identity(changed)[0])

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            self.assertEqual(
                [
                    finding.code
                    for finding in MODULE.validate_file(duplicate).findings
                ],
                ["TILE_STRATEGY_JSON_DUPLICATE_KEY"],
            )
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            self.assertEqual(
                [
                    finding.code
                    for finding in MODULE.validate_file(nonfinite).findings
                ],
                ["TILE_STRATEGY_JSON_NONFINITE_NUMBER"],
            )

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with (
            mock.patch.object(
                socket,
                "create_connection",
                side_effect=AssertionError("network denied"),
            ),
            mock.patch.object(
                socket,
                "socket",
                side_effect=AssertionError("network denied"),
            ),
            mock.patch.object(
                socket,
                "getaddrinfo",
                side_effect=AssertionError("network denied"),
            ),
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)

    def test_contract_and_source_map_preserve_non_effects(self) -> None:
        contract = (
            ROOT / "contracts/release/tile_delivery_strategy_assessment.md"
        ).read_text(encoding="utf-8")
        source_map = (
            ROOT
            / "docs/intake/exploratory/"
            "tile-delivery-strategy-assessment-source-map.md"
        ).read_text(encoding="utf-8")
        for token in (
            "pmtiles_archive",
            "xyz_service",
            "martin_postgis",
            "mbtiles_local",
        ):
            self.assertIn(token, contract.lower())
        for token in ("no network", "release", "deployment", "publication"):
            self.assertIn(token, source_map.lower())


if __name__ == "__main__":
    unittest.main()
