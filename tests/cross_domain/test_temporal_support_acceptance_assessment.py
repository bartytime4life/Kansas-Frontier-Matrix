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
MODULE_PATH = ROOT / "tools/validators/validate_temporal_support_acceptance_assessment.py"
SPEC = importlib.util.spec_from_file_location("temporal_support_acceptance_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TemporalSupportAcceptanceAssessmentTest(unittest.TestCase):
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
        self.assertEqual(len(results), 20)
        self.assertTrue(all(result["ok"] for result in results), results)

    def test_all_five_subject_families_have_a_passing_fixture(self) -> None:
        names = (
            "pass_released_layer",
            "pass_internal_evidence_bundle",
            "pass_internal_policy_decision",
            "pass_public_ai_envelope",
        )
        kinds = {self.candidate(name)["subject"]["kind"] for name in names}
        self.assertEqual(kinds, {"LAYER_MANIFEST", "EVIDENCE_BUNDLE", "POLICY_DECISION", "AI_ENVELOPE"})
        tile = copy.deepcopy(self.candidate("pass_released_layer"))
        tile["subject"]["kind"] = "TILE_ARTIFACT"
        tile["profile_spec_hash"] = MODULE.compute_profile_hash(tile)
        self.assertEqual(MODULE.validate_candidate(tile).outcome, "PASS")

    def test_undated_layer_is_denied(self) -> None:
        result = MODULE.validate_candidate(self.candidate("deny_undated_layer"))
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(result.codes, ["MISSING_VALID_TIME"])

    def test_unresolved_inputs_abstain(self) -> None:
        for name in ("abstain_incomplete_assessment", "abstain_subject_unresolved", "abstain_support_unresolved"):
            self.assertEqual(MODULE.validate_candidate(self.candidate(name)).outcome, "ABSTAIN")

    def test_profile_hash_binds_time_semantics(self) -> None:
        candidate = self.candidate("pass_released_layer")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["time_dimensions"]["valid_time"]["end"] = "2027-02-01T00:00:00Z"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_profile_carries_no_source_payload_or_runtime_answer(self) -> None:
        text = json.dumps(self.candidate("pass_released_layer"), sort_keys=True)
        for forbidden in ("source_payload", "runtime_answer", "policy_result", "published_url"):
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
