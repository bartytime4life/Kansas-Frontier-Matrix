from __future__ import annotations

import copy
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators import validate_temporal_reference_integrity_assessment as validator


class TemporalReferenceIntegrityAssessmentTests(unittest.TestCase):
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
        self.assertFalse(schema["x-kfm"]["constraint_execution"])
        self.assertFalse(schema["x-kfm"]["authority_effects"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = validator.validate_fixture_manifest()
        self.assertEqual(28, len(results))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_modes_roles_and_constraints_have_positive_coverage(self) -> None:
        for name in (
            "pass_valid_time_geography_within",
            "pass_transaction_time_source_overlap",
            "pass_bitemporal_identity",
            "pass_subject_start_within_other",
            "pass_subject_end_within_source",
        ):
            self.assertEqual("PASS", validator.validate_candidate(self._candidate(name)).outcome)

    def test_unresolved_records_and_windows_abstain(self) -> None:
        for name in (
            "abstain_subject_record_unresolved",
            "abstain_target_record_unresolved",
            "abstain_subject_window_unresolved",
            "abstain_target_window_unresolved",
        ):
            self.assertEqual("ABSTAIN", validator.validate_candidate(self._candidate(name)).outcome)

    def test_missing_records_and_temporal_violations_deny(self) -> None:
        for name in (
            "deny_target_record_missing_quarantine_recommendation",
            "deny_subject_record_missing",
            "deny_subject_not_within_target",
            "deny_disjoint_overlap",
            "deny_shared_endpoint_excluded",
        ):
            self.assertEqual("DENY", validator.validate_candidate(self._candidate(name)).outcome)

    def test_axis_role_state_and_disposition_mismatches_deny(self) -> None:
        for name in (
            "deny_check_state_mismatch",
            "deny_overall_state_mismatch",
            "deny_mode_axis_set_mismatch",
            "deny_duplicate_temporal_axis",
            "deny_target_role_kind_mismatch",
            "deny_failure_action_mismatch",
            "deny_failure_review_reference_missing",
        ):
            self.assertEqual("DENY", validator.validate_candidate(self._candidate(name)).outcome)

    def test_boundary_inclusion_changes_overlap(self) -> None:
        denied = self._candidate("deny_shared_endpoint_excluded")
        check = denied["checks"][0]
        self.assertFalse(
            validator.evaluate_constraint(
                check["constraint"], check["subject_window"], check["target_window"]
            )
        )
        included = copy.deepcopy(denied)
        included["checks"][0]["target_window"]["start_inclusive"] = True
        self.assertTrue(
            validator.evaluate_constraint(
                check["constraint"],
                included["checks"][0]["subject_window"],
                included["checks"][0]["target_window"],
            )
        )

    def test_profile_hash_binds_both_bitemporal_axes(self) -> None:
        candidate = self._candidate("pass_bitemporal_identity")
        self.assertEqual(candidate["profile_spec_hash"], validator.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["checks"][1]["target_window"]["end_inclusive"] = True
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
