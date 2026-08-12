from __future__ import annotations

import copy
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.source import validate_connector_load_budget_assessment as validator


class ConnectorLoadBudgetAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(validator.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(item for item in self.manifest["cases"] if item["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return validator.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_valid_closed_and_non_authoritative(self) -> None:
        schema = validator._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["x-kfm"]["network"])
        self.assertFalse(schema["x-kfm"]["connector_execution"])
        self.assertFalse(schema["x-kfm"]["authority_effects"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = validator.validate_fixture_manifest()
        self.assertEqual(23, len(results))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_all_execution_modes_have_positive_coverage(self) -> None:
        expected = {
            "pass_single_worker": "SINGLE_WORKER",
            "pass_threaded_per_source": "THREADED",
            "pass_distributed_shared_budget": "DISTRIBUTED",
        }
        for name, mode in expected.items():
            candidate = self._candidate(name)
            self.assertEqual(mode, candidate["execution"]["mode"])
            self.assertEqual("PASS", validator.validate_candidate(candidate).outcome)
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_dependencies_abstain(self) -> None:
        for name in (
            "abstain_budget_unresolved",
            "abstain_source_policy_requires_resolution",
            "abstain_conduct_unresolved",
            "abstain_review_pending",
        ):
            self.assertEqual("ABSTAIN", validator.validate_candidate(self._candidate(name)).outcome)

    def test_source_wide_scope_and_distribution_fail_closed(self) -> None:
        for name in (
            "deny_per_worker_scope",
            "deny_requested_concurrency_exceeds_budget",
            "deny_distributed_share_key_missing",
            "deny_non_distributed_share_key_present",
            "deny_single_worker_incoherent",
        ):
            self.assertEqual("DENY", validator.validate_candidate(self._candidate(name)).outcome)

    def test_retry_and_stop_controls_fail_closed(self) -> None:
        for name in (
            "deny_retry_after_not_honored",
            "deny_retry_cap_below_base",
            "deny_retry_none_incoherent",
            "deny_stop_condition_missing",
            "deny_stop_conditions_not_canonical",
        ):
            self.assertEqual("DENY", validator.validate_candidate(self._candidate(name)).outcome)

    def test_profile_hash_binds_budget_semantics(self) -> None:
        candidate = self._candidate("pass_threaded_per_source")
        self.assertEqual(candidate["profile_spec_hash"], validator.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["budget"]["max_concurrency"] = 8
        self.assertNotEqual(candidate["profile_spec_hash"], validator.compute_profile_hash(changed))

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
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
