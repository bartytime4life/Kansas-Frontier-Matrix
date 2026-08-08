"""Schema, fixture, and projection tests for path aliases."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest

from jsonschema import Draft202012Validator

from tools.validators.directory_governance.path_alias_model import (
    ADOPTED_DOCTRINE_SHA256,
    EXPECTED_ROOT_REGISTRY_BASE,
    EXPECTED_ROOT_REGISTRY_SHA256,
    FIXTURE_ROOT,
    REGISTER_PATH,
    REPO_ROOT,
    SCHEMA_PATH,
)
from tools.validators.directory_governance.validate_path_alias_register import validate_register

from path_alias_test_support import PathAliasTestSupport


class PathAliasSchemaCases(PathAliasTestSupport, unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_valid_fixture_covers_all_compatibility_classes(self) -> None:
        fixture = self.valid_fixture()
        self.assertEqual(
            {"legacy", "mirror", "external_export", "transitional", "deprecated"},
            {entry["class"] for entry in fixture["aliases"]},
        )
        result = self.validate_payload(fixture)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("PASS", result.outcome)

    def test_reviewed_invalid_fixtures_fail_with_exact_codes(self) -> None:
        payload = json.loads((FIXTURE_ROOT / "invalid" / "cases.json").read_text(encoding="utf-8"))
        cases = payload["cases"]
        self.assertEqual(6, len(cases))
        base = self.valid_fixture()
        for case in cases:
            with self.subTest(name=case["name"]):
                candidate = copy.deepcopy(base)
                operations = case.get("operations") or [{"path": case["path"], "value": case["value"]}]
                for operation in operations:
                    current = candidate
                    for part in operation["path"][:-1]:
                        current = current[part]
                    current[operation["path"][-1]] = operation["value"]
                result = self.validate_payload(candidate)
                self.assertFalse(result.ok)
                self.assertEqual(case["expected_codes"], sorted({item.code for item in result.findings}))

    def test_current_register_binds_adopted_doctrine_and_root_registry(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        self.assertEqual(f"sha256:{ADOPTED_DOCTRINE_SHA256}", register["doctrine"]["sha256"])
        self.assertEqual(
            f"sha256:{EXPECTED_ROOT_REGISTRY_SHA256}",
            register["root_registry"]["sha256"],
        )
        self.assertEqual(EXPECTED_ROOT_REGISTRY_BASE, register["root_registry"]["base_ref"])
        self.assertTrue(
            all(
                item["source_digest"] == f"sha256:{ADOPTED_DOCTRINE_SHA256}"
                for item in register["aliases"]
            )
        )

    def test_current_register_records_only_accepted_directory_rules_mapping(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        self.assertEqual(1, len(register["aliases"]))
        alias = register["aliases"][0]
        self.assertEqual("docs/architecture/directory-rules.md", alias["old_path"])
        self.assertEqual("docs/doctrine/directory-rules.md", alias["canonical_target"])
        self.assertEqual("ADR-0029", alias["decision_ref"])
        self.assertEqual([], alias["writers"]["alias"])
        self.assertEqual("canonical_only", alias["write_rule"])
        self.assertEqual("legacy_body_read_only", alias["body_mode"])
        self.assertEqual("OPEN", alias["consumer_closure"])

    def test_current_register_passes_projection_semantics(self) -> None:
        result = validate_register(
            REGISTER_PATH,
            check_repository=False,
            enforce_projection_binding=False,
        )
        self.assertTrue(result.ok, result.findings)

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "tools/validators/directory_governance/validate_path_alias_register.py", "--fixtures"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)

    def test_current_cli_can_run_with_bounded_local_projection(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/directory_governance/validate_path_alias_register.py",
                "--skip-repository",
                "--skip-projection-binding",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)
