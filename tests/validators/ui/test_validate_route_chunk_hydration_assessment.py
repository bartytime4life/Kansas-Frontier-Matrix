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
MODULE_PATH = ROOT / "tools/validators/ui/validate_route_chunk_hydration_assessment.py"
SPEC = importlib.util.spec_from_file_location("validate_route_chunk_hydration_assessment", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RouteChunkHydrationAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.cases = {entry["name"]: entry for entry in cls.manifest["cases"]}

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self.cases[name])

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(
            json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        )

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), len(self.cases))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_finite_outcomes_are_covered(self) -> None:
        outcomes = {
            MODULE.validate_candidate(self._candidate(name)).outcome
            for name in self.cases
            if not name.startswith("error_")
        }
        self.assertEqual(outcomes, {"PASS", "ABSTAIN", "DENY"})

    def test_ready_candidate_remains_inactive_and_non_authoritative(self) -> None:
        candidate = self._candidate("pass_ready")
        self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
        self.assertEqual(candidate["chunk"]["load_mode"], "LAZY_ROUTE")
        self.assertFalse(any(candidate["authority_claims"].values()))

    def test_each_non_ready_state_fails_closed(self) -> None:
        for name in (
            "abstain_view_registry_hold",
            "abstain_render_hints_unknown",
            "abstain_evidence_partial",
            "abstain_access_unknown",
            "abstain_release_hold",
            "deny_view_registry_denied",
            "deny_access_denied",
            "deny_release_denied",
        ):
            self.assertNotEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "PASS")

    def test_derived_state_must_match_prerequisites(self) -> None:
        for name in ("deny_derived_disposition_mismatch", "deny_reason_code_mismatch"):
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "DENY")
            self.assertEqual(result.codes, ["DERIVED_STATE_INCOHERENT"])

    def test_chunk_and_reference_roles_are_bound(self) -> None:
        expected = {
            "deny_chunk_identity_mismatch": ["CHUNK_ID_NAME_MISMATCH"],
            "deny_reference_role_collapse": ["REFERENCE_ROLE_COLLAPSE"],
            "deny_direct_store_reference": ["DIRECT_STORE_REFERENCE_DENIED"],
            "deny_embedded_query_marker": ["EMBEDDED_QUERY_DENIED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_and_identity_bind_prerequisite_state(self) -> None:
        candidate = self._candidate("pass_ready")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        self.assertEqual(candidate["assessment_id"], MODULE.compute_assessment_id(candidate))
        changed = copy.deepcopy(candidate)
        changed["prerequisites"]["evidence_state"] = "PARTIAL"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))
        self.assertNotEqual(candidate["assessment_id"], MODULE.compute_assessment_id(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_ready")
        candidate["chunk"]["chunk_name"] = "invalid\ud800"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["JSON_UNPAIRED_SURROGATE"])
        with self.assertRaises(MODULE.UnpairedSurrogateError):
            MODULE.compute_profile_hash(candidate)

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            _, findings = MODULE.load_json_object(duplicate)
            self.assertEqual([item.code for item in findings], ["JSON_DUPLICATE_KEY"])
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            _, findings = MODULE.load_json_object(nonfinite)
            self.assertEqual([item.code for item in findings], ["JSON_NONFINITE_NUMBER"])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
