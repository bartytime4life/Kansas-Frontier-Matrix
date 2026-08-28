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
MODULE_PATH = ROOT / "tools/validators/release/validate_api_contract_change_assessment.py"
SPEC = importlib.util.spec_from_file_location("api_contract_change_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ApiContractChangeAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 25)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_breaking_change_requires_reviewable_closure_without_authority(self) -> None:
        candidate = self._candidate("pass_breaking_major_change")
        self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
        self.assertFalse(any(candidate["authority_claims"].values()))

    def test_additive_patch_and_deprecation_profiles_pass(self) -> None:
        for name in (
            "pass_additive_minor_change",
            "pass_patch_correction",
            "pass_deprecation_minor_change",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "PASS")

    def test_unknown_impact_abstains(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("abstain_change_impact_unknown")).outcome,
            "ABSTAIN",
        )

    def test_missing_release_and_client_closure_fails_closed(self) -> None:
        for name in (
            "deny_compatibility_tests_missing",
            "deny_client_fixtures_missing",
            "deny_change_notice_missing",
            "deny_release_manifest_missing",
            "deny_rollback_card_missing",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_profile_does_not_adopt_exhaustive_version_policy(self) -> None:
        candidate = self._candidate("pass_breaking_major_change")
        self.assertIn("NO_VERSION_POLICY_ADOPTION", candidate["limitations"])
        self.assertNotIn("field_change_policy", candidate)

    def test_profile_hash_binds_change_semantics(self) -> None:
        candidate = self._candidate("pass_breaking_major_change")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["change_subject"]["client_behavior_impact"] = "NONE"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
