from __future__ import annotations

import copy
import importlib.util
import socket
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO_ROOT / "tools/validators/data/validate_analytical_view_manifest.py"
SPEC = importlib.util.spec_from_file_location("validate_analytical_view_manifest", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AnalyticalViewManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = MODULE.load_fixture_manifest()
        cls.cases = {case["name"]: case for case in cls.manifest["cases"]}

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_case(self.manifest, self.cases[name])

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(MODULE._SCHEMA)

    def test_fixture_names_are_unique_and_cover_finite_outcomes(self) -> None:
        names = [case["name"] for case in self.manifest["cases"]]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(
            {case["expected"]["outcome"] for case in self.manifest["cases"]},
            {"PASS", "ABSTAIN", "DENY", "ERROR"},
        )

    def test_exact_fixture_replay(self) -> None:
        self.assertEqual(len(MODULE.validate_fixture_manifest()), 20)

    def test_pass_profiles_cover_read_materialized_write_and_public_boundaries(self) -> None:
        for name in (
            "pass_read_only_database_view",
            "pass_materialized_view_direct_mutation_prohibited",
            "pass_internal_updatable_view_with_guard",
            "pass_public_read_only_candidate_with_review",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "PASS")

    def test_reviewed_abstain_codes_are_exact(self) -> None:
        for name in (item for item in self.cases if item.startswith("abstain_")):
            expected = self.cases[name]["expected"]
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual((result.outcome, result.codes), (expected["outcome"], expected["codes"]))

    def test_reviewed_deny_codes_are_exact(self) -> None:
        for name in (item for item in self.cases if item.startswith("deny_")):
            expected = self.cases[name]["expected"]
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual((result.outcome, result.codes), (expected["outcome"], expected["codes"]))

    def test_profile_hash_binds_definition_and_mutation_guard(self) -> None:
        candidate = self._candidate("pass_internal_updatable_view_with_guard")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["mutation"]["check_option_mode"] = "LOCAL"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_noncanonical_semantic_reference_denies_after_rehash(self) -> None:
        candidate = self._candidate("pass_read_only_database_view")
        candidate["semantic_dependencies"]["join_assessment_refs"] = [
            "kfm:join-assessment:synthetic-z:001",
            "kfm:join-assessment:synthetic-a:001",
        ]
        candidate["profile_spec_hash"] = MODULE.compute_profile_hash(candidate)
        result = MODULE.validate_candidate(candidate)
        self.assertEqual((result.outcome, result.codes), ("DENY", ["JOIN_REFS_NOT_CANONICAL"]))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_read_only_database_view")
        candidate["purpose"] = "invalid \ud800 view purpose"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual((result.outcome, result.codes), ("ERROR", ["CANONICALIZATION_FAILED"]))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
