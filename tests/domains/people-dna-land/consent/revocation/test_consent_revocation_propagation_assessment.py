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


REPO_ROOT = Path(__file__).resolve().parents[5]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/domains/people-dna-land/"
    "validate_consent_revocation_propagation_assessment.py"
)
SPEC = importlib.util.spec_from_file_location(
    "consent_revocation_propagation_assessment_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ConsentRevocationPropagationAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(
            entry for entry in self.manifest["cases"] if entry["name"] == name
        )

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_closed_inactive_and_non_authoritative(self) -> None:
        schema = MODULE._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["authority"], "NONE")
        self.assertFalse(schema["x-kfm"]["network"])
        self.assertFalse(schema["x-kfm"]["real_person_data"])
        self.assertFalse(schema["x-kfm"]["cleanup_execution"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 17)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_consent_states_and_scope_mismatch_are_explicit(self) -> None:
        expected = {
            "pass_active_scope_satisfied": ("ACTIVE", "SATISFIED"),
            "pass_revoked_fully_propagated": ("REVOKED", "DENY"),
            "pass_expired_fully_propagated": ("EXPIRED", "DENY"),
            "pass_unknown_status_abstains": ("UNKNOWN", "ABSTAIN"),
            "pass_status_lookup_error_fails_closed": ("ERROR", "ERROR"),
            "pass_scope_mismatch_denies_every_surface": ("ACTIVE", "DENY"),
        }
        for name, pair in expected.items():
            candidate = self._candidate(name)
            self.assertEqual(
                (candidate["consent_state"]["status"], candidate["declared_outcome"]),
                pair,
            )
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")

    def test_revocation_propagates_across_exact_closed_surface_set(self) -> None:
        candidate = self._candidate("pass_revoked_fully_propagated")
        dependencies = candidate["dependencies"]
        self.assertEqual(
            tuple(item["surface"] for item in dependencies), MODULE.EXPECTED_SURFACES
        )
        for item in dependencies:
            self.assertIsNotNone(item["action_receipt_ref"])
            if item["surface"] in MODULE.IMMEDIATE_SURFACES:
                self.assertEqual((item["state"], item["action"]), ("BLOCKED", "DENY_NEXT_USE"))
            else:
                self.assertIn(
                    (item["state"], item["action"]),
                    {("INVALIDATED", "INVALIDATE"), ("PURGED", "PURGE")},
                )

    def test_satisfied_outcome_remains_consent_dimension_only(self) -> None:
        candidate = self._candidate("pass_active_scope_satisfied")
        self.assertEqual(candidate["declared_outcome"], "SATISFIED")
        self.assertIn("CONSENT_DIMENSION_ONLY", candidate["limitations"])
        self.assertTrue(all(value is False for value in candidate["authority_claims"].values()))

    def test_negative_cases_have_exact_codes(self) -> None:
        expected = {
            "deny_revoked_answer_still_ready": ["REVOCATION_PROPAGATION_INCOMPLETE"],
            "deny_revoked_action_receipt_missing": ["ACTION_RECEIPT_REQUIRED"],
            "deny_revoked_receipt_missing": ["REVOCATION_RECEIPT_REQUIRED"],
            "deny_active_status_expired": ["ACTIVE_STATUS_EXPIRED"],
            "deny_status_observed_after_evaluation": ["STATUS_OBSERVED_AFTER_EVALUATION"],
            "deny_profile_hash_tamper": ["PROFILE_SPEC_HASH_MISMATCH"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_replays_and_binds_dependency_state(self) -> None:
        candidate = self._candidate("pass_revoked_fully_propagated")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["dependencies"][6]["state"] = "INVALIDATED"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_input_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            link.symlink_to(target)
            self.assertEqual(MODULE.load_json_object(duplicate)[1][0].code, "JSON_DUPLICATE_KEY")
            self.assertEqual(MODULE.load_json_object(nonfinite)[1][0].code, "JSON_NONFINITE_NUMBER")
            self.assertEqual(MODULE.load_json_object(link)[1][0].code, "INPUT_SYMLINK_DENIED")

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
