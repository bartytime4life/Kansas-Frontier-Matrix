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
MODULE_PATH = ROOT / "tools/validators/data/validate_layer_legend_disclosure.py"
SPEC = importlib.util.spec_from_file_location("layer_legend_disclosure_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class LayerLegendDisclosureTests(unittest.TestCase):
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
        self.assertEqual(len(results), 16)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_complete_disclosures_pass(self) -> None:
        for name in (
            "pass_released_direct",
            "pass_modeled_with_uncertainty",
            "pass_denied_disabled_with_policy",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "PASS")

    def test_unresolved_disclosures_abstain(self) -> None:
        for name in (
            "abstain_unresolved_evidence",
            "abstain_incomplete_legend",
            "abstain_unknown_evidence_class",
            "abstain_unknown_release_state",
            "abstain_unknown_uncertainty",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_negative_state_and_sensitivity_visibility_fail_closed(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_denied_visible")).codes,
            ["NONRELEASED_ENTRY_VISIBLE", "WITHHELD_ENTRY_VISIBLE"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_sensitive_without_policy")).codes,
            ["POLICY_REFERENCE_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_withheld_visible")).codes,
            ["WITHHELD_ENTRY_VISIBLE"],
        )

    def test_interpretive_status_and_completeness_fail_closed(self) -> None:
        expected = {
            "deny_modeled_without_uncertainty": ["INTERPRETIVE_UNCERTAINTY_REQUIRED"],
            "deny_stale_without_status": ["STATUS_REFERENCE_REQUIRED"],
            "deny_complete_with_known_gap": ["COMPLETENESS_CLAIM_INCOHERENT"],
            "deny_noncanonical_entries": ["ENTRIES_NOT_CANONICAL"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_replays_and_binds_semantics(self) -> None:
        candidate = self._candidate("pass_released_direct")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["legend"]["scope_statement"] = "A materially different synthetic legend scope."
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
