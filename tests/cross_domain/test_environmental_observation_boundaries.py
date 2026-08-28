#!/usr/bin/env python3
"""Prove Soil, Atmosphere, and Hydrology fixture profiles do not collapse."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(REPO_ROOT))

from tools.validators.domains.atmosphere import (  # noqa: E402
    validate_public_safe_precipitation_fixture as atmosphere,
)
from tools.validators.domains.hydrology import (  # noqa: E402
    validate_public_safe_flow_fixture as hydrology,
)
from tools.validators.domains.soil import (  # noqa: E402
    validate_public_safe_fixture as soil,
)


FIXTURES = {
    "soil": REPO_ROOT / "fixtures/domains/soil/valid/public_safe_observation.json",
    "atmosphere": REPO_ROOT
    / "fixtures/domains/atmosphere/public_safe_precipitation/valid/public_safe_precipitation.json",
    "hydrology": REPO_ROOT
    / "fixtures/domains/hydrology/public_safe_flow/valid/public_safe_flow.json",
}
VALIDATORS = {
    "soil": soil,
    "atmosphere": atmosphere,
    "hydrology": hydrology,
}


class EnvironmentalObservationBoundaryTests(unittest.TestCase):
    def test_each_profile_accepts_only_its_own_fixture(self) -> None:
        payloads = {
            name: json.loads(path.read_text(encoding="utf-8"))
            for name, path in FIXTURES.items()
        }
        for validator_name, validator in VALIDATORS.items():
            for fixture_name, payload in payloads.items():
                with self.subTest(validator=validator_name, fixture=fixture_name):
                    findings = validator.validate_candidate(payload)
                    if validator_name == fixture_name:
                        self.assertEqual(findings, [])
                    else:
                        self.assertTrue(findings)

    def test_shared_place_and_time_do_not_imply_shared_domain_ownership(self) -> None:
        atmosphere_payload = json.loads(
            FIXTURES["atmosphere"].read_text(encoding="utf-8")
        )
        hydrology_payload = json.loads(
            FIXTURES["hydrology"].read_text(encoding="utf-8")
        )
        soil_payload = json.loads(FIXTURES["soil"].read_text(encoding="utf-8"))

        self.assertEqual(
            atmosphere_payload["spatial_support"],
            hydrology_payload["spatial_support"],
        )
        self.assertEqual(
            soil_payload["spatial_support"],
            hydrology_payload["spatial_support"],
        )
        self.assertEqual(
            atmosphere_payload["temporal_scope"],
            hydrology_payload["temporal_scope"],
        )
        self.assertNotEqual(
            atmosphere_payload["object_family"],
            hydrology_payload["object_family"],
        )

    def test_all_three_file_profiles_are_positive(self) -> None:
        for name, validator in VALIDATORS.items():
            with self.subTest(domain=name):
                self.assertEqual(validator.validate_file(FIXTURES[name]), [])


if __name__ == "__main__":
    unittest.main()
