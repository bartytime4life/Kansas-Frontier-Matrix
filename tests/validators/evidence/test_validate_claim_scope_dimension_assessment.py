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
MODULE_PATH = ROOT / "tools/validators/evidence/validate_claim_scope_dimension_assessment.py"
SPEC = importlib.util.spec_from_file_location("claim_scope_dimension_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ClaimScopeDimensionAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 14)
        self.assertTrue(all(item["ok"] for item in results))

    def test_each_dimension_can_be_measured_without_authority(self) -> None:
        for name in (
            "pass_time_measured",
            "pass_space_measured_public_candidate",
            "pass_attribute_measured",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_dimension_profiles_abstain(self) -> None:
        for name in (
            "abstain_incomplete_time_role",
            "abstain_unknown_space_role",
            "abstain_unresolved_attribute_scope",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_role_interpretation_and_review_invariants_fail_closed(self) -> None:
        expected = {
            "deny_measured_dimension_mismatch": ["MEASURED_DIMENSION_MISMATCH"],
            "deny_interpretation_mismatch": ["INTERPRETATION_CLASS_MISMATCH"],
            "deny_two_measured_dimensions": ["DIMENSION_ROLE_CARDINALITY_INVALID"],
            "deny_public_review_missing": ["PUBLIC_REVIEW_REFERENCE_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_binds_scope_semantics(self) -> None:
        candidate = self._candidate("pass_time_measured")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["assessment"]["measured_dimension"] = "SPACE"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
