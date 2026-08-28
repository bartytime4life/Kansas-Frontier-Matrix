from __future__ import annotations

import copy
import importlib.util
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_distinct_null_deduplication_assessment.py"
SPEC = importlib.util.spec_from_file_location("validate_distinct_null_deduplication_assessment", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class DistinctNullDeduplicationAssessmentTests(unittest.TestCase):
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
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 18)

    def test_pass_profiles_keep_identity_reconciliation_separate(self) -> None:
        for name in (
            "pass_count_population_distinct_pairs",
            "pass_dataset_explicit_grouping",
            "pass_entity_match_reconciliation",
            "pass_public_candidate_with_review",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "PASS")

    def test_reviewed_abstain_codes_are_exact(self) -> None:
        expected = {
            "abstain_unresolved_use_case": ["USE_CASE_UNRESOLVED"],
            "abstain_unresolved_null_equivalence": ["NULL_EQUIVALENCE_UNRESOLVED"],
            "abstain_fixture_not_run": ["FIXTURE_NOT_RUN"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual((result.outcome, result.codes), ("ABSTAIN", codes))

    def test_reviewed_deny_codes_are_exact(self) -> None:
        names = [name for name in self.cases if name.startswith("deny_")]
        for name in names:
            expected = self.cases[name]["expected"]
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual((result.outcome, result.codes), (expected["outcome"], expected["codes"]))

    def test_profile_hash_binds_null_and_tuple_semantics(self) -> None:
        candidate = self._candidate("pass_count_population_distinct_pairs")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["null_semantics"]["row_posture"] = "EXCLUDE_IF_ANY_NULL"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_noncanonical_field_order_denies_after_rehash(self) -> None:
        candidate = self._candidate("pass_count_population_distinct_pairs")
        candidate["distinct_fields"] = list(reversed(candidate["distinct_fields"]))
        candidate["profile_spec_hash"] = MODULE.compute_profile_hash(candidate)
        result = MODULE.validate_candidate(candidate)
        self.assertEqual((result.outcome, result.codes), ("DENY", ["DISTINCT_FIELDS_NOT_CANONICAL"]))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_count_population_distinct_pairs")
        candidate["disclosure"]["summary"] = "invalid \ud800 text"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual((result.outcome, result.codes), ("ERROR", ["CANONICALIZATION_FAILED"]))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)

    def test_loader_rejects_symlink_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "candidate.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "candidate-link.json"
            link.symlink_to(target)
            with self.assertRaises(MODULE.JsonInputError):
                MODULE.load_json_file(link)


if __name__ == "__main__":
    unittest.main()
