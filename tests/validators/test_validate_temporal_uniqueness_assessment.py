from __future__ import annotations

import copy
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators import validate_temporal_uniqueness_assessment as validator


class TemporalUniquenessAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(validator.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(item for item in self.manifest["cases"] if item["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return validator.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_valid_closed_draft_2020_12(self) -> None:
        schema = validator._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["x-kfm"]["table_inspection"])
        self.assertFalse(schema["x-kfm"]["constraint_execution"])
        self.assertFalse(schema["x-kfm"]["authority_effects"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = validator.validate_fixture_manifest()
        self.assertEqual(31, len(results))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_modes_conflict_rules_and_allowance_policies_have_positive_coverage(self) -> None:
        for name in (
            "pass_valid_time_half_open_nonoverlap",
            "pass_no_declared_peers",
            "pass_supersession_overlap_allowed",
            "pass_reviewed_parallel_overlap_allowed",
            "pass_transaction_time_nonoverlap",
            "pass_bitemporal_all_axes_rule_nonconflict",
        ):
            self.assertEqual("PASS", validator.validate_candidate(self._candidate(name)).outcome)

    def test_unresolved_profile_policy_records_and_windows_abstain(self) -> None:
        for name in (
            "abstain_key_profile_unresolved",
            "abstain_overlap_policy_unresolved",
            "abstain_subject_record_unresolved",
            "abstain_peer_record_unresolved",
            "abstain_subject_window_unresolved",
            "abstain_peer_window_unresolved",
        ):
            self.assertEqual("ABSTAIN", validator.validate_candidate(self._candidate(name)).outcome)

    def test_known_overlap_conflicts_deny(self) -> None:
        for name in (
            "deny_overlap_conflict",
            "deny_closed_endpoint_conflict",
            "deny_bitemporal_any_axis_conflict",
        ):
            result = validator.validate_candidate(self._candidate(name))
            self.assertEqual("DENY", result.outcome)
            self.assertIn("TEMPORAL_UNIQUENESS_CONFLICT", result.codes)

    def test_policy_lineage_state_and_action_guards_deny(self) -> None:
        for name in (
            "deny_supersession_lineage_missing",
            "deny_parallel_review_reference_missing",
            "deny_declared_state_mismatch",
            "deny_failure_action_and_review_required",
            "deny_failure_action_mismatch",
        ):
            self.assertEqual("DENY", validator.validate_candidate(self._candidate(name)).outcome)

    def test_endpoint_inclusion_changes_pair_conflict(self) -> None:
        candidate = self._candidate("pass_valid_time_half_open_nonoverlap")
        axis = candidate["comparisons"][0]["axes"][0]
        self.assertFalse(validator.intervals_overlap(axis["subject_window"], axis["peer_window"]))
        closed = copy.deepcopy(candidate)
        closed["comparisons"][0]["axes"][0]["subject_window"]["end_inclusive"] = True
        closed_axis = closed["comparisons"][0]["axes"][0]
        self.assertTrue(validator.intervals_overlap(closed_axis["subject_window"], closed_axis["peer_window"]))

    def test_profile_hash_binds_key_policy_and_bitemporal_axes(self) -> None:
        candidate = self._candidate("pass_bitemporal_all_axes_rule_nonconflict")
        self.assertEqual(candidate["profile_spec_hash"], validator.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["key_profile"]["pair_conflict_rule"] = "ANY_DECLARED_AXIS_OVERLAP"
        self.assertNotEqual(candidate["profile_spec_hash"], validator.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = validator.validate_fixture_manifest()
            second = validator.validate_fixture_manifest()
        self.assertEqual(first, second)

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
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
            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * (validator.MAX_FILE_BYTES + 1))
            for path, code in (
                (duplicate, "JSON_DUPLICATE_KEY"),
                (nonfinite, "JSON_NONFINITE_NUMBER"),
                (link, "INPUT_SYMLINK_DENIED"),
                (oversized, "FILE_TOO_LARGE"),
            ):
                value, findings = validator.load_json_object(path)
                self.assertIsNone(value)
                self.assertEqual(code, findings[0].code)


if __name__ == "__main__":
    unittest.main()
