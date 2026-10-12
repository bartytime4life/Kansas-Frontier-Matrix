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
MODULE_PATH = ROOT / "tools/validators/data/validate_cartographic_omission_disclosure.py"
SPEC = importlib.util.spec_from_file_location("cartographic_omission_disclosure_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CartographicOmissionDisclosureTests(unittest.TestCase):
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
        self.assertEqual(len(results), 12)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_two_reviewed_complete_profiles_pass(self) -> None:
        for name in ("pass_complete_disclosure", "pass_sensitivity_policy_binding"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "PASS")

    def test_unresolved_and_incomplete_profiles_abstain(self) -> None:
        for name in ("abstain_unresolved_purpose", "abstain_incomplete_assessment", "abstain_unknown_materiality"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_material_disclosure_transform_and_policy_fail_closed(self) -> None:
        expected = {
            "deny_material_omission_hidden": ["MATERIAL_OMISSION_UNDISCLOSED"],
            "deny_simplification_without_receipt": ["SIMPLIFICATION_RECEIPT_REQUIRED"],
            "deny_sensitive_without_policy": ["POLICY_REFERENCE_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_canonical_and_completeness_claims_fail_closed(self) -> None:
        self.assertEqual(MODULE.validate_candidate(self._candidate("deny_noncanonical_entries")).codes, ["ENTRIES_NOT_CANONICAL"])
        self.assertEqual(MODULE.validate_candidate(self._candidate("deny_complete_with_known_gap")).codes, ["COMPLETENESS_CLAIM_INCOHERENT"])

    def test_profile_hash_replays_and_binds_semantics(self) -> None:
        candidate = self._candidate("pass_complete_disclosure")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["assessment"]["scope_statement"] = "A materially different synthetic review scope."
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
