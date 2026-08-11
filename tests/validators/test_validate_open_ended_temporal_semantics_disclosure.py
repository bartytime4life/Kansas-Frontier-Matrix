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

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/validate_open_ended_temporal_semantics_disclosure.py"
SPEC = importlib.util.spec_from_file_location("open_ended_temporal_semantics_disclosure_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class OpenEndedTemporalSemanticsDisclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(entry for entry in self.manifest["cases"] if entry["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_valid_closed_draft_2020_12(self) -> None:
        schema = MODULE._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 21)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_cases_cover_all_end_semantics(self) -> None:
        names = ("pass_explicit_end", "pass_unknown_end", "pass_current_until_superseded", "pass_now_relative_release_time")
        candidates = [self._candidate(name) for name in names]
        self.assertEqual({item["period"]["end_semantics"] for item in candidates}, set(MODULE.INTERPRETATIONS))
        self.assertTrue(all(MODULE.validate_candidate(item).outcome == "PASS" for item in candidates))

    def test_unresolved_and_incomplete_inputs_abstain(self) -> None:
        for name in ("abstain_claim_scope_unresolved", "abstain_disclosure_incomplete", "abstain_disclosure_unknown"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_open_end_and_sentinel_failures_deny(self) -> None:
        expected = {
            "deny_far_future_sentinel": ["FAR_FUTURE_SENTINEL_FORBIDDEN"],
            "deny_missing_as_of_time": ["AS_OF_TIME_REQUIRED"],
            "deny_end_semantics_mismatch": ["END_SEMANTICS_MISMATCH"],
            "deny_current_missing_now_basis": ["NOW_BASIS_REQUIRED"],
            "deny_interpretation_mismatch": ["INTERPRETATION_MISMATCH"],
            "deny_required_obligation_missing": ["REQUIRED_OBLIGATION_MISSING"],
            "deny_time_order_invalid": ["TIME_ORDER_INVALID"],
            "deny_public_review_record_missing": ["PUBLIC_REVIEW_RECORD_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_replays_and_binds_semantics(self) -> None:
        candidate = self._candidate("pass_unknown_end")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["period"]["as_of_time"] = "2026-08-11T14:00:01Z"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_public_case_requires_review_without_granting_authority(self) -> None:
        candidate = self._candidate("pass_public_explanation_reviewed")
        self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
        self.assertTrue(all(value is False for value in candidate["authority_claims"].values()))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
