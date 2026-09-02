from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CLASSIFICATION_VALIDATOR_PATH = (
    REPO_ROOT / "tools/validators/validate_classification_release.py"
)
SOIL_VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/domains/soil/validate_domain_observation.py"
)
SOIL_CASES_PATH = (
    REPO_ROOT / "fixtures/domains/soil/domain_observation/cases.json"
)


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


classification = _load_module(
    "classification_release_boundary_validator",
    CLASSIFICATION_VALIDATOR_PATH,
)
soil = _load_module(
    "soil_domain_observation_boundary_validator",
    SOIL_VALIDATOR_PATH,
)


class ClassificationObservationBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.classification_candidate = next(
            candidate
            for raw_case, candidate in classification.load_fixture_cases()
            if raw_case["name"] == "valid_current"
        )
        soil_cases = json.loads(
            SOIL_CASES_PATH.read_text(encoding="utf-8")
        )["cases"]
        cls.observation_candidate = next(
            case["candidate"]
            for case in soil_cases
            if case["name"] == "valid_station"
        )

    def test_each_candidate_passes_only_its_own_profile(self) -> None:
        self.assertTrue(
            classification.validate_payload(
                self.classification_candidate
            ).ok
        )
        soil_outcome, soil_findings = soil.evaluate(
            self.observation_candidate
        )
        self.assertEqual(soil_outcome, "PASS", soil_findings)

    def test_cross_profile_substitution_fails_closed(self) -> None:
        classification_result = classification.validate_payload(
            self.observation_candidate
        )
        self.assertNotEqual(classification_result.outcome, "PASS")

        soil_outcome, soil_findings = soil.evaluate(
            self.classification_candidate
        )
        self.assertNotEqual(soil_outcome, "PASS")
        self.assertTrue(soil_findings)

    def test_source_roles_and_support_types_remain_distinct(self) -> None:
        classification_pair = (
            self.classification_candidate["source_role"],
            self.classification_candidate["support_type"],
        )
        observation_pair = (
            "OBSERVATION",
            "DIRECT_MEASUREMENT",
        )
        self.assertEqual(
            classification_pair,
            ("CLASSIFICATION", "DERIVED_CLASSIFICATION"),
        )
        self.assertEqual(
            self.observation_candidate["source_role"],
            "direct_observation_measurement",
        )
        self.assertEqual(
            self.observation_candidate["support_type"],
            "station_soil_moisture",
        )
        self.assertNotEqual(classification_pair, observation_pair)

    def test_mesonet_station_fixture_cannot_be_statewide_classification(self) -> None:
        self.assertEqual(
            self.observation_candidate["temporal_support"]["kind"],
            "OBSERVED_TIME",
        )
        self.assertEqual(
            self.classification_candidate["space"]["scale"],
            "STATEWIDE",
        )
        self.assertEqual(
            self.classification_candidate["times"][
                "source_data_cutoff_at"
            ],
            "2026-08-04T12:00:00Z",
        )
        self.assertNotIn(
            "value",
            self.classification_candidate,
        )


if __name__ == "__main__":
    unittest.main()
