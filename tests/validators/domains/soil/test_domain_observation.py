from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
VALIDATOR = ROOT / "tools/validators/domains/soil/validate_domain_observation.py"
CASES = ROOT / "fixtures/domains/soil/domain_observation/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/domain_observation.schema.json"

SPEC = importlib.util.spec_from_file_location("soil_domain_observation_validator", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SoilDomainObservationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = json.loads(CASES.read_text(encoding="utf-8"))["cases"]
        cls.schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    def test_schema_is_closed_and_inactive(self) -> None:
        self.assertFalse(self.schema["additionalProperties"])
        self.assertEqual(
            self.schema["properties"]["profile"]["const"],
            "kfm.domains.soil.domain-observation.v1",
        )
        self.assertEqual(self.schema["properties"]["status"]["const"], "PROPOSED_INACTIVE")
        self.assertFalse(self.schema["properties"]["public_use_allowed"]["const"])
        self.assertFalse(self.schema["x-kfm"]["public_release_authority"])

    def test_fixture_matrix_matches_exact_outcomes(self) -> None:
        for case in self.cases:
            with self.subTest(case=case["name"]):
                outcome, findings = MODULE.evaluate(case["candidate"])
                self.assertEqual(outcome, case["expected_outcome"])
                self.assertEqual(findings, case["expected_findings"])

    def test_valid_candidate_has_deterministic_identity(self) -> None:
        candidate = self.cases[0]["candidate"]
        digest = MODULE.canonical_hash(candidate)
        self.assertEqual(candidate["spec_hash"], f"sha256:{digest}")
        self.assertEqual(candidate["id"], f"soil-observation:{digest[:24]}")

    def test_station_and_satellite_are_not_interchangeable(self) -> None:
        self.assertEqual(
            MODULE.SUPPORT_TO_KIND["station_soil_moisture"], "STATION_OBSERVATION"
        )
        self.assertEqual(
            MODULE.SUPPORT_TO_KIND["satellite_soil_moisture_grid"], "SATELLITE_RETRIEVAL"
        )
        self.assertNotEqual(
            MODULE.SUPPORT_TO_KIND["station_soil_moisture"],
            MODULE.SUPPORT_TO_KIND["satellite_soil_moisture_grid"],
        )

    def test_release_and_public_use_overclaim_are_denied(self) -> None:
        by_name = {case["name"]: case for case in self.cases}
        for name in ("release_overclaim", "public_overclaim"):
            outcome, _ = MODULE.evaluate(by_name[name]["candidate"])
            self.assertEqual(outcome, "DENY")


if __name__ == "__main__":
    unittest.main()
