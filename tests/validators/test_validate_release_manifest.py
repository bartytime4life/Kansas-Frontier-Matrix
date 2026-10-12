from __future__ import annotations

import copy
import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/release/validate_release_manifest.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/release_manifest.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/release/release_manifest"
CASES_PATH = FIXTURE_ROOT / "cases.json"

SPEC = importlib.util.spec_from_file_location("validate_release_manifest", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ReleaseManifestValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))

    def _candidate(self, group: str, case_id: str) -> dict[str, object]:
        return MODULE.materialize_case(self.cases, self.cases[group][case_id])

    def test_schema_is_dual_profile_and_strict_branch_is_closed(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["execution_mode"], "FIXTURE_ONLY")
        self.assertEqual(len(schema["oneOf"]), 2)
        strict = schema["$defs"]["strict_profile"]
        self.assertFalse(strict["additionalProperties"])
        self.assertEqual(strict["properties"]["lifecycle_state"]["const"], "CANDIDATE")

    def test_legacy_minimal_profile_remains_valid(self) -> None:
        result = MODULE.validate_candidate(
            self._candidate("valid", "valid_legacy_minimal")
        )
        self.assertTrue(result.ok)

    def test_all_strict_valid_cases_pass(self) -> None:
        case_ids = sorted(
            name for name in self.cases["valid"] if name.endswith("_candidate")
        )
        self.assertEqual(len(case_ids), 3)
        for case_id in case_ids:
            with self.subTest(case_id=case_id):
                self.assertTrue(
                    MODULE.validate_candidate(self._candidate("valid", case_id)).ok
                )

    def test_matrix_has_exact_reviewed_polarity(self) -> None:
        self.assertEqual(len(self.cases["valid"]), 4)
        self.assertEqual(len(self.cases["invalid"]), 17)
        for group_name in ("valid", "invalid"):
            for case_id, record in sorted(self.cases[group_name].items()):
                with self.subTest(case=f"{group_name}/{case_id}"):
                    result = MODULE.validate_candidate(
                        MODULE.materialize_case(self.cases, record)
                    )
                    self.assertEqual(result.outcome, record["expected"]["outcome"])
                    self.assertEqual(
                        sorted({item.code for item in result.findings}),
                        record["expected"]["findings"],
                    )

    def test_schema_and_semantic_negative_names_do_not_collide(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        schema_ids = sorted(
            name for name in self.cases["invalid"] if name.startswith("invalid_")
        )
        semantic_ids = sorted(
            name
            for name in self.cases["invalid"]
            if name.startswith("semantic_invalid_")
        )
        self.assertEqual(len(schema_ids), 2)
        self.assertEqual(len(semantic_ids), 15)
        for case_id in schema_ids:
            self.assertTrue(
                list(validator.iter_errors(self._candidate("invalid", case_id))),
                case_id,
            )
        for case_id in semantic_ids:
            self.assertFalse(
                list(validator.iter_errors(self._candidate("invalid", case_id))),
                case_id,
            )

    def test_identity_reproduces_public_case(self) -> None:
        candidate = self._candidate("valid", "valid_public_candidate")
        self.assertEqual(
            MODULE.compute_manifest_spec_hash(candidate), candidate["spec_hash"]
        )
        self.assertEqual(MODULE.compute_manifest_id(candidate), candidate["id"])

    def test_identity_changes_with_semantic_content(self) -> None:
        candidate = self._candidate("valid", "valid_public_candidate")
        changed = copy.deepcopy(candidate)
        changed["title"] = "Different semantic title"
        self.assertNotEqual(
            MODULE.compute_manifest_spec_hash(changed), candidate["spec_hash"]
        )

    def test_duplicate_json_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"id":"a","id":"b"}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {item.code for item in result.findings}, {"JSON_DUPLICATE_KEY"}
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"id":"legacy","value":NaN}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {item.code for item in result.findings}, {"JSON_NONFINITE_NUMBER"}
        )

    def test_missing_file_is_error(self) -> None:
        result = MODULE.validate_record(REPO_ROOT / "missing-release-manifest.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual({item.code for item in result.findings}, {"FILE_NOT_FOUND"})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        candidate = self._candidate("valid", "valid_public_candidate")
        untrusted = "UNTRUSTED_RELEASE_TITLE_DO_NOT_ECHO"
        candidate["title"] = untrusted
        candidate["schema_negative_canary"] = True
        report = MODULE.serialize_label(
            "fixture:untrusted", MODULE.validate_candidate(candidate)
        )
        self.assertNotIn(untrusted, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_fixture_profile_is_no_network_and_cli_is_deterministic(self) -> None:
        with mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network access denied"),
        ), mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network access denied"),
        ):
            self.assertEqual(MODULE.run_fixture_profile(), 0)
            self.assertEqual(MODULE.run_fixture_profile(), 0)
        first = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        second = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(len(first.stdout.splitlines()), 21)


if __name__ == "__main__":
    unittest.main()
