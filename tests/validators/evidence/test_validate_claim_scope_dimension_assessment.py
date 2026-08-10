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
        self.assertEqual(len(MODULE.validate_fixture_manifest()), 15)

    def test_each_dimension_can_be_measured_without_authority(self) -> None:
        for name in ("pass_public_space_measured", "pass_internal_time_measured", "pass_internal_attribute_measured"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_scope_abstains(self) -> None:
        for name in ("abstain_incomplete_assessment", "abstain_unresolved_dimension", "abstain_evidence_scope_unresolved"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_complete_scope_failures_deny(self) -> None:
        for name in ("deny_partition_mismatch", "deny_complete_unresolved_dimension", "deny_no_controlled_dimension", "deny_no_measured_dimension", "deny_public_review_missing", "deny_public_caveat_missing", "deny_resolution_role_mismatch"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_profile_hash_binds_scope_roles(self) -> None:
        candidate = self._candidate("pass_public_space_measured")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["dimensions"]["space"]["role"] = "CONTROLLED"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
