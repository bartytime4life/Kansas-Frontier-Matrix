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
MODULE_PATH = ROOT / "tools/validators/validate_period_boundary_predicate_disclosure.py"
SPEC = importlib.util.spec_from_file_location(
    "period_boundary_predicate_disclosure_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PeriodBoundaryPredicateDisclosureTests(unittest.TestCase):
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
        self.assertEqual(len(results), 26)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_fixtures_cover_all_thirteen_relations(self) -> None:
        relation_cases = [
            entry
            for entry in self.manifest["cases"]
            if entry["name"].startswith("pass_relation_")
        ]
        observed = {
            MODULE.compute_predicate(
                self._candidate(entry["name"])["left_window"],
                self._candidate(entry["name"])["right_window"],
            )
            for entry in relation_cases
        }
        self.assertEqual(observed, MODULE.PREDICATES)
        self.assertTrue(
            all(MODULE.validate_candidate(self._candidate(entry["name"])).outcome == "PASS" for entry in relation_cases)
        )

    def test_meeting_intersection_respects_boundary_inclusion(self) -> None:
        half_open = self._candidate("pass_relation_meets")
        closed = self._candidate("pass_closed_meeting_is_point")
        mixed = self._candidate("pass_mixed_explicit_meeting_is_point")
        self.assertEqual(MODULE.compute_intersection_shape(half_open["left_window"], half_open["right_window"]), "EMPTY")
        self.assertEqual(MODULE.compute_intersection_shape(closed["left_window"], closed["right_window"]), "POINT")
        self.assertEqual(MODULE.compute_intersection_shape(mixed["left_window"], mixed["right_window"]), "POINT")

    def test_unresolved_references_abstain(self) -> None:
        for name in (
            "abstain_claim_scope_unresolved",
            "abstain_window_reference_unresolved",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_semantic_mismatches_fail_closed(self) -> None:
        expected = {
            "deny_predicate_mismatch": ["PREDICATE_MISMATCH"],
            "deny_intersection_shape_mismatch": ["INTERSECTION_SHAPE_MISMATCH"],
            "deny_closed_convention_mismatch": ["INTERVAL_CONVENTION_MISMATCH"],
            "deny_mixed_convention_not_mixed": ["INTERVAL_CONVENTION_MISMATCH"],
            "deny_zero_duration_interval": ["INTERVAL_ORDER_INVALID"],
            "deny_non_utc_endpoint": ["UTC_TIMESTAMP_REQUIRED"],
            "deny_noncanonical_evidence_refs": ["EVIDENCE_REFS_NOT_CANONICAL"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_replays_and_binds_semantics(self) -> None:
        candidate = self._candidate("pass_relation_overlaps")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["explanation"] = "A materially different synthetic boundary explanation for hash replay."
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
