from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/evidence/validate_projection_distortion_disclosure.py"
SPEC = importlib.util.spec_from_file_location("projection_distortion_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ProjectionDistortionDisclosureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.cases = {case["name"]: case for case in cls.manifest["cases"]}

    def candidate(self, name: str) -> dict[str, object]:
        return MODULE.build_fixture_candidate(self.cases[name])

    def test_schema_is_draft_2020_12_valid(self) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_all_reviewed_cases_match_exactly(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 16)
        self.assertTrue(all(result["ok"] for result in results), results)

    def test_complete_profiles_pass_without_authority(self) -> None:
        for name in (
            "pass_statewide_public_material",
            "pass_regional_internal_not_material",
            "pass_local_exploratory_material",
        ):
            candidate = self.candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_declarations_abstain(self) -> None:
        for name in (
            "abstain_projection_incomplete",
            "abstain_scope_unknown",
            "abstain_distortion_assessment_unresolved",
            "abstain_materiality_unknown",
        ):
            self.assertEqual(MODULE.validate_candidate(self.candidate(name)).outcome, "ABSTAIN")

    def test_complete_and_public_disclosures_fail_closed(self) -> None:
        for name in (
            "deny_complete_missing_crs",
            "deny_dimension_not_evaluated",
            "deny_missing_distance_risk",
            "deny_not_material_rationale_missing",
            "deny_public_review_missing",
            "deny_public_caveat_missing",
        ):
            self.assertEqual(MODULE.validate_candidate(self.candidate(name)).outcome, "DENY")

    def test_profile_hash_binds_distortion_semantics(self) -> None:
        candidate = self.candidate("pass_statewide_public_material")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["distortions"]["distance"] = "PRESERVED_WITHIN_DECLARED_SCOPE"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_profile_carries_no_coordinates_or_source_payloads(self) -> None:
        candidate = self.candidate("pass_statewide_public_material")
        text = json.dumps(candidate, sort_keys=True)
        for forbidden in ("coordinates", "geometry", "source_payload", "transformed_points"):
            self.assertNotIn(forbidden, text)

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
