from __future__ import annotations

import copy
import json
import unittest

from tools.validators.domains.hazards.validate_usdm_materiality import compute_assessment, fixture_cases, validate_candidate

VALID, INVALID = fixture_cases()


class USDMMaterialityTests(unittest.TestCase):
    def test_valid_fixture_states(self) -> None:
        expected = {
            "material.json": ("MATERIAL", "PROMOTION_CANDIDATE"),
            "unchanged.json": ("UNCHANGED", "NON_EVENT"),
            "non_material.json": ("SEMANTIC_NON_MATERIAL", "NON_EVENT"),
            "hold_geometry_only.json": ("UNDETERMINED", "HOLD"),
        }
        for name, state in expected.items():
            with self.subTest(name=name):
                result = validate_candidate(VALID[name.removesuffix(".json")])
                self.assertTrue(result.ok, result.findings)
                self.assertIsNotNone(result.computed)
                self.assertEqual((result.computed.state, result.computed.outcome), state)

    def test_material_criteria_are_deterministic(self) -> None:
        candidate = copy.deepcopy(VALID["material"])
        assessment = compute_assessment(candidate)
        self.assertEqual(
            assessment.triggered_criteria,
            ("D1_D4_AREA_THRESHOLD", "D2_D4_AREA_THRESHOLD", "GEOMETRY_CHANGED_WITH_METRICS"),
        )

    def test_geometry_only_change_holds(self) -> None:
        candidate = copy.deepcopy(VALID["hold_geometry_only"])
        assessment = compute_assessment(candidate)
        self.assertEqual(assessment.state, "UNDETERMINED")
        self.assertEqual(assessment.outcome, "HOLD")

    def test_severe_category_appearance_is_material(self) -> None:
        candidate = copy.deepcopy(VALID["non_material"])
        candidate = copy.deepcopy(candidate)
        candidate["current"]["area_percent"]["d3_d4"] = 0.1
        candidate["current"]["area_percent"]["d2_d4"] = 6.2
        candidate["current"]["geometry_digest"] = "sha256:" + "3" * 64
        assessment = compute_assessment(candidate)
        self.assertEqual(assessment.state, "MATERIAL")
        self.assertIn("D3_APPEARED", assessment.triggered_criteria)

    def test_invalid_fixtures_match_exact_findings(self) -> None:
        for name, candidate, expected in INVALID:
            with self.subTest(name=name):
                result = validate_candidate(candidate)
                self.assertEqual(sorted({item.code for item in result.findings}), sorted(expected))

    def test_legal_declaration_fields_are_not_admitted(self) -> None:
        candidate = copy.deepcopy(VALID["material"])
        candidate["current"]["administrative_stage"] = "warning"
        result = validate_candidate(candidate)
        self.assertIn("UNEXPECTED_SNAPSHOT_FIELD", {item.code for item in result.findings})


if __name__ == "__main__":
    unittest.main()
