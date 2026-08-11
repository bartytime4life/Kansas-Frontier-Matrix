from __future__ import annotations

import copy
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators import validate_rolling_metric_window_disclosure as validator


class RollingMetricWindowDisclosureTests(unittest.TestCase):
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
        self.assertFalse(schema["x-kfm"]["analytics_execution"])
        self.assertFalse(schema["x-kfm"]["authority_effects"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = validator.validate_fixture_manifest()
        self.assertEqual(28, len(results))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_rows_range_and_groups_have_positive_coverage(self) -> None:
        expected = {
            "pass_rows_moving_average": "ROWS",
            "pass_range_duration": "RANGE",
            "pass_groups_rank": "GROUPS",
        }
        for name, unit in expected.items():
            candidate = self._candidate(name)
            self.assertEqual(unit, candidate["frame"]["unit"])
            self.assertEqual("PASS", validator.validate_candidate(candidate).outcome)

    def test_unresolved_references_and_parity_abstain(self) -> None:
        for name in (
            "abstain_claim_scope_unresolved",
            "abstain_time_definition_unresolved",
            "abstain_engine_parity_unresolved",
        ):
            self.assertEqual(
                "ABSTAIN", validator.validate_candidate(self._candidate(name)).outcome
            )

    def test_order_and_frame_fail_closed(self) -> None:
        names = (
            "deny_duplicate_ordering_field",
            "deny_tie_breaker_missing",
            "deny_window_time_not_first",
            "deny_time_field_mismatch",
            "deny_offset_missing",
            "deny_offset_unexpected",
            "deny_frame_bounds_reversed",
            "deny_range_offset_unit_missing",
            "deny_rows_offset_unit_present",
        )
        for name in names:
            self.assertEqual(
                "DENY", validator.validate_candidate(self._candidate(name)).outcome
            )

    def test_public_candidate_requires_review_and_release_references(self) -> None:
        for name in (
            "deny_public_review_missing",
            "deny_public_release_reference_missing",
        ):
            self.assertEqual(
                "DENY", validator.validate_candidate(self._candidate(name)).outcome
            )
        positive = self._candidate("pass_rows_moving_average")
        self.assertFalse(any(positive["authority_claims"].values()))

    def test_profile_hash_binds_window_semantics(self) -> None:
        candidate = self._candidate("pass_rows_moving_average")
        self.assertEqual(
            candidate["profile_spec_hash"], validator.compute_profile_hash(candidate)
        )
        changed = copy.deepcopy(candidate)
        changed["frame"]["start"]["offset"] = 5
        self.assertNotEqual(
            candidate["profile_spec_hash"], validator.compute_profile_hash(changed)
        )

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
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
                with self.subTest(path=path.name):
                    value, findings = validator.load_json_object(path)
                    self.assertIsNone(value)
                    self.assertEqual(code, findings[0].code)


if __name__ == "__main__":
    unittest.main()
