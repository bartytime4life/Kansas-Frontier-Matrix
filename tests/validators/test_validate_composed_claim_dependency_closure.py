from __future__ import annotations

import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES
from tools.validators.validate_composed_claim_dependency_closure import (
    FIXTURES_ROOT,
    SCHEMA_PATH,
    canonical_closure_id,
    canonical_graph_hash,
    canonical_spec_hash,
    main as validate_main,
    validate_closure_file,
)


class ComposedClaimDependencyClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_files = sorted((FIXTURES_ROOT / "valid").glob("valid_*.json"))
        self.semantic_files = sorted(
            (FIXTURES_ROOT / "semantic_invalid").glob("semantic_invalid_*.json")
        )
        self.schema_files = sorted((FIXTURES_ROOT / "invalid").glob("invalid_*.json"))

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_valid_fixtures_cover_every_finite_outcome(self) -> None:
        self.assertEqual(len(self.valid_files), 8)
        outcomes: set[str] = set()
        for path in self.valid_files:
            with self.subTest(path=path.name):
                self.assertEqual(validate_closure_file(path), [])
                payload = json.loads(path.read_text(encoding="utf-8"))
                outcomes.add(payload["closure_summary"]["outcome"])
                self.assertEqual(
                    payload["dependency_graph_hash"],
                    canonical_graph_hash(payload),
                )
                self.assertEqual(payload["closure_id"], canonical_closure_id(payload))
                self.assertEqual(payload["spec_hash"], canonical_spec_hash(payload))
        self.assertEqual(
            outcomes,
            {"SUPPORTED", "QUALIFIED", "ABSTAIN", "DENY", "ERROR"},
        )

    def test_semantic_invalid_fixtures_match_manifest_exactly(self) -> None:
        expected = json.loads(
            (
                FIXTURES_ROOT
                / "semantic_invalid/expected_findings_manifest.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual({path.name for path in self.semantic_files}, set(expected))
        for path in self.semantic_files:
            with self.subTest(path=path.name):
                actual = sorted({finding.code for finding in validate_closure_file(path)})
                self.assertEqual(actual, sorted(expected[path.name]))

    def test_schema_invalid_lane_is_distinct_and_non_vacuous(self) -> None:
        expected = json.loads(
            (
                FIXTURES_ROOT
                / "invalid/expected_findings_manifest.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual({path.name for path in self.schema_files}, set(expected))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for path in self.schema_files:
            with self.subTest(path=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertTrue(list(validator.iter_errors(payload)))
                actual = sorted({finding.code for finding in validate_closure_file(path)})
                self.assertEqual(actual, sorted(expected[path.name]))
        for path in self.semantic_files:
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(list(validator.iter_errors(payload)), [])

    def test_required_optional_and_alternative_roles_do_not_collapse(self) -> None:
        supported = json.loads(
            (
                FIXTURES_ROOT
                / "valid/valid_supported_required_and_alternative.json"
            ).read_text(encoding="utf-8")
        )
        qualified = json.loads(
            (
                FIXTURES_ROOT
                / "valid/valid_qualified_optional_unresolved.json"
            ).read_text(encoding="utf-8")
        )
        abstained = json.loads(
            (
                FIXTURES_ROOT
                / "valid/valid_abstain_alternative_unresolved.json"
            ).read_text(encoding="utf-8")
        )
        denied = json.loads(
            (
                FIXTURES_ROOT
                / "valid/valid_deny_alternative_denied.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(supported["closure_summary"]["outcome"], "SUPPORTED")
        self.assertTrue(supported["closure_summary"]["render_allowed"])
        self.assertEqual(qualified["closure_summary"]["outcome"], "QUALIFIED")
        self.assertTrue(qualified["closure_summary"]["render_allowed"])
        self.assertEqual(
            qualified["closure_summary"]["reason_codes"],
            ["OPTIONAL_DEPENDENCY_UNAVAILABLE"],
        )
        self.assertEqual(abstained["closure_summary"]["outcome"], "ABSTAIN")
        self.assertFalse(abstained["closure_summary"]["render_allowed"])
        self.assertEqual(denied["closure_summary"]["outcome"], "DENY")
        self.assertFalse(denied["closure_summary"]["render_allowed"])

    def test_mutual_exclusion_violation_is_error_not_partial_support(self) -> None:
        payload = json.loads(
            (
                FIXTURES_ROOT
                / "valid/valid_error_mutual_exclusion.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(payload["closure_summary"]["outcome"], "ERROR")
        self.assertFalse(payload["closure_summary"]["render_allowed"])
        self.assertEqual(
            payload["closure_summary"]["reason_codes"],
            [
                "ALTERNATIVE_GROUP_MAXIMUM_EXCEEDED",
                "MUTUAL_EXCLUSION_VIOLATION",
            ],
        )

    def test_duplicate_keys_and_oversize_inputs_fail_before_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text(
                '{"schema_version":"x","schema_version":"x"}',
                encoding="utf-8",
            )
            self.assertEqual(
                validate_closure_file(duplicate)[0].code,
                "FIXTURE_JSON_INVALID",
            )
            oversized = Path(temp_dir) / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(
                validate_closure_file(oversized)[0].code,
                "FIXTURE_TOO_LARGE",
            )

    def test_cli_fixture_and_single_file_polarity(self) -> None:
        self.assertEqual(validate_main(["--fixtures"]), 0)
        self.assertEqual(validate_main([str(self.valid_files[0])]), 0)
        self.assertEqual(validate_main([str(self.semantic_files[0])]), 1)
        self.assertEqual(validate_main([]), 2)

    def test_validator_has_no_network_dependency(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            for path in [
                *self.valid_files,
                *self.semantic_files,
                *self.schema_files,
            ]:
                validate_closure_file(path)


if __name__ == "__main__":
    unittest.main()
