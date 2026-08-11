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

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/governance/validate_object_identity_kind_assessment.py"
SPEC = importlib.util.spec_from_file_location("validate_object_identity_kind_assessment", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ObjectIdentityKindAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.cases = {entry["name"]: entry for entry in cls.manifest["cases"]}

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self.cases[name])

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), len(self.cases))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_all_resolved_identity_kinds_pass_without_authority(self) -> None:
        for name in ("pass_entity", "pass_value_object", "pass_derived_artifact"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_postures_abstain(self) -> None:
        expected = {
            "abstain_identity_kind_unresolved": ["IDENTITY_KIND_UNRESOLVED"],
            "abstain_register_unresolved": ["REGISTER_BINDING_UNRESOLVED"],
            "abstain_not_registered": ["OBJECT_FAMILY_NOT_REGISTERED"],
            "abstain_review_pending": ["REVIEW_PENDING"],
            "abstain_review_unknown": ["REVIEW_UNKNOWN"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "ABSTAIN")
            self.assertEqual(result.codes, codes)

    def test_identity_semantics_fail_closed(self) -> None:
        for name in (
            "deny_entity_semantics",
            "deny_value_object_semantics",
            "deny_derived_artifact_semantics",
        ):
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "DENY")
            self.assertEqual(result.codes, ["IDENTITY_SEMANTICS_INCOHERENT"])

    def test_unresolved_kind_cannot_claim_identity_behavior(self) -> None:
        result = MODULE.validate_candidate(self._candidate("deny_unresolved_semantics"))
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            result.codes,
            ["IDENTITY_KIND_UNRESOLVED", "IDENTITY_SEMANTICS_INCOHERENT"],
        )

    def test_register_bindings_are_state_bound(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_resolved_binding_missing_digest")).codes,
            ["REGISTER_BINDING_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_unresolved_binding_present")).codes,
            ["REGISTER_BINDING_PROHIBITED", "REGISTER_BINDING_UNRESOLVED"],
        )

    def test_complete_review_requires_canonical_evidence_and_rationale(self) -> None:
        expected = {
            "deny_complete_without_review_ref": ["REVIEW_RECORD_REQUIRED"],
            "deny_complete_without_rationale": ["RATIONALE_SUMMARY_REQUIRED"],
            "deny_noncanonical_review_refs": ["ARRAY_NOT_CANONICAL"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_binds_identity_semantics(self) -> None:
        candidate = self._candidate("pass_entity")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["declaration"]["identity_kind"] = "VALUE_OBJECT"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_entity")
        candidate["declaration"]["rationale_summary"] = "invalid \ud800 text"
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
