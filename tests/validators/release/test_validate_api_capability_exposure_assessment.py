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

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/release/validate_api_capability_exposure_assessment.py"
SPEC = importlib.util.spec_from_file_location("api_capability_exposure_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ApiCapabilityExposureAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 30)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_profiles_remain_declarations_without_authority(self) -> None:
        for name in (
            "pass_public_read_candidate",
            "pass_internal_read_only",
            "pass_internal_governed_mutation",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_profiles_abstain(self) -> None:
        for name in ("abstain_incomplete_review", "abstain_unknown_capability"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_public_state_and_trust_boundary_fail_closed(self) -> None:
        for name in (
            "deny_direct_store_boundary",
            "deny_public_raw_state",
            "deny_public_processed_state",
            "deny_public_mutation",
            "deny_public_internal_boundary",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_public_governance_bypass_and_closure_fail_closed(self) -> None:
        for name in (
            "deny_public_evidence_bypass",
            "deny_public_policy_bypass",
            "deny_public_scrub_bypass",
            "deny_public_release_manifest_missing",
            "deny_public_correction_missing",
            "deny_public_rollback_missing",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_purpose_contract_documentation_and_review_are_required(self) -> None:
        for name in (
            "deny_placeholder_purpose",
            "deny_contract_missing",
            "deny_documentation_missing",
            "deny_risk_assessment_missing",
            "deny_review_record_missing",
            "deny_security_review_missing",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_outcome_and_prohibited_use_vocabularies_are_closed(self) -> None:
        for name in ("deny_finite_outcome_vocabulary", "deny_prohibited_use_set_incomplete"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_profile_hash_binds_capability_semantics(self) -> None:
        candidate = self._candidate("pass_public_read_candidate")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["capability"]["purpose_statement"] = "A different bounded synthetic purpose statement for review."
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_unsafe_json_inputs_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            nonfinite = root / "nonfinite.json"
            duplicate.write_text('{"value":1,"value":2}', encoding="utf-8")
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            self.assertEqual(
                ["JSON_DUPLICATE_KEY"],
                [finding.code for finding in MODULE.load_json_object(duplicate)[1]],
            )
            self.assertEqual(
                ["JSON_NONFINITE_NUMBER"],
                [finding.code for finding in MODULE.load_json_object(nonfinite)[1]],
            )

    def test_unpaired_surrogate_fails_closed(self) -> None:
        candidate = self._candidate("pass_public_read_candidate")
        candidate["capability"]["purpose_statement"] = "unsafe-\ud800"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["JSON_UNPAIRED_SURROGATE"])
        with self.assertRaises(MODULE.UnpairedSurrogateError):
            MODULE.canonical_hash(candidate)

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
