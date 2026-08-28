from __future__ import annotations

import copy
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators import validate_window_ordering_lint_profile as validator


class WindowOrderingLintProfileTests(unittest.TestCase):
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
        self.assertFalse(schema["x-kfm"]["sql_execution"])
        self.assertFalse(schema["x-kfm"]["authority_effects"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = validator.validate_fixture_manifest()
        self.assertEqual(22, len(results))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_positive_simple_qualified_multiwindow_and_masking_cases(self) -> None:
        for name in (
            "pass_lag_deterministic",
            "pass_qualified_identifiers",
            "pass_two_windows",
            "pass_comments_and_strings_are_ignored",
        ):
            candidate = self._candidate(name)
            self.assertEqual("PASS", validator.validate_candidate(candidate).outcome)
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_named_windows_and_computed_expressions_abstain(self) -> None:
        for name in ("abstain_named_window", "abstain_computed_order_expression"):
            self.assertEqual("ABSTAIN", validator.validate_candidate(self._candidate(name)).outcome)

    def test_ordering_invariants_deny(self) -> None:
        for name in (
            "deny_no_window_clause",
            "deny_window_order_missing",
            "deny_primary_not_first",
            "deny_tie_breaker_missing",
            "deny_tie_breaker_not_last",
            "deny_duplicate_order_key",
            "deny_window_count_too_low",
            "deny_window_count_too_high",
            "deny_multiple_statements",
            "deny_requirement_keys_not_distinct",
        ):
            self.assertEqual("DENY", validator.validate_candidate(self._candidate(name)).outcome)

    def test_lexical_and_parenthesis_failures_are_errors(self) -> None:
        for name in ("error_unterminated_string", "error_unbalanced_parenthesis"):
            self.assertEqual("ERROR", validator.validate_candidate(self._candidate(name)).outcome)

    def test_query_and_profile_hashes_bind_exact_sql(self) -> None:
        candidate = self._candidate("pass_lag_deterministic")
        self.assertEqual(candidate["query_digest"], validator.query_digest(candidate["sql"]))
        self.assertEqual(candidate["profile_spec_hash"], validator.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["sql"] += " "
        self.assertNotEqual(candidate["query_digest"], validator.query_digest(changed["sql"]))
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
