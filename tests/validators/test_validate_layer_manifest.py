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
VALIDATOR_PATH = REPO_ROOT / "tools/validators/data/validate_layer_manifest.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/layer_manifest.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/data/layer_manifest"
REGISTRY_PATH = REPO_ROOT / "tools/validators/validator_registry.json"

SPEC = importlib.util.spec_from_file_location(
    "validate_layer_manifest",
    VALIDATOR_PATH,
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class LayerManifestValidatorTests(unittest.TestCase):
    def _load(self, relative: str) -> dict[str, object]:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def test_schema_is_dual_profile_and_strict_branch_is_closed(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["execution_mode"], "FIXTURE_ONLY")
        self.assertEqual(len(schema["oneOf"]), 2)
        strict = schema["$defs"]["strict_profile"]
        self.assertFalse(strict["additionalProperties"])
        self.assertEqual(
            strict["properties"]["lifecycle_state"]["const"],
            "CANDIDATE",
        )

    def test_legacy_minimal_profile_remains_valid(self) -> None:
        result = MODULE.validate_record(
            FIXTURE_ROOT / "valid/valid_legacy_minimal.json"
        )
        self.assertTrue(result.ok)

    def test_all_strict_valid_fixtures_pass(self) -> None:
        paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*_candidate.json"))
        self.assertEqual(len(paths), 3)
        for path in paths:
            with self.subTest(path=path.name):
                self.assertTrue(MODULE.validate_record(path).ok)

    def test_manifest_has_exact_reviewed_polarity(self) -> None:
        manifest = self._load("expected_findings_manifest.json")
        valid = manifest["valid"]
        invalid = manifest["invalid"]
        self.assertEqual(len(valid), 4)
        self.assertEqual(len(invalid), 12)
        for group_name, group in (("valid", valid), ("invalid", invalid)):
            for filename, expected in sorted(group.items()):
                path = FIXTURE_ROOT / group_name / filename
                with self.subTest(path=f"{group_name}/{filename}"):
                    result = MODULE.validate_record(path)
                    self.assertEqual(result.outcome, expected["outcome"])
                    self.assertEqual(
                        sorted({item.code for item in result.findings}),
                        expected["findings"],
                    )

    def test_schema_and_semantic_negative_names_do_not_collide(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        )
        schema_invalid = sorted(
            (FIXTURE_ROOT / "invalid").glob("invalid_*.json")
        )
        semantic_invalid = sorted(
            (FIXTURE_ROOT / "invalid").glob("semantic_invalid_*.json")
        )
        self.assertEqual(len(schema_invalid), 2)
        self.assertEqual(len(semantic_invalid), 10)
        for path in schema_invalid:
            self.assertTrue(
                list(
                    validator.iter_errors(
                        json.loads(path.read_text(encoding="utf-8"))
                    )
                ),
                path.name,
            )
        for path in semantic_invalid:
            self.assertFalse(
                list(
                    validator.iter_errors(
                        json.loads(path.read_text(encoding="utf-8"))
                    )
                ),
                path.name,
            )

    def test_identity_reproduces_strict_fixture(self) -> None:
        candidate = self._load("valid/valid_public_pmtiles_candidate.json")
        self.assertEqual(
            MODULE.compute_manifest_spec_hash(candidate),
            candidate["spec_hash"],
        )
        self.assertEqual(
            MODULE.compute_manifest_id(candidate),
            candidate["id"],
        )

    def test_identity_ignores_only_stored_id_and_hash(self) -> None:
        candidate = self._load("valid/valid_public_pmtiles_candidate.json")
        changed = copy.deepcopy(candidate)
        changed["title"] = "Different semantic title"
        self.assertNotEqual(
            MODULE.compute_manifest_spec_hash(changed),
            candidate["spec_hash"],
        )

    def test_duplicate_json_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"id":"a","id":"b"}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {item.code for item in result.findings},
            {"JSON_DUPLICATE_KEY"},
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"id":"legacy","value":NaN}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {item.code for item in result.findings},
            {"JSON_NONFINITE_NUMBER"},
        )

    def test_missing_file_is_error(self) -> None:
        result = MODULE.validate_record(REPO_ROOT / "missing-layer.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {item.code for item in result.findings},
            {"FILE_NOT_FOUND"},
        )

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        candidate = self._load("valid/valid_public_pmtiles_candidate.json")
        untrusted = "UNTRUSTED_LAYER_TITLE_DO_NOT_ECHO"
        candidate["title"] = untrusted
        candidate["schema_negative_canary"] = True
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            report = MODULE.serialize(path, MODULE.validate_record(path))
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
            first = MODULE.run_fixture_profile()
            second = MODULE.run_fixture_profile()
        self.assertEqual(first, 0)
        self.assertEqual(second, 0)

        first_cli = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        second_cli = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(first_cli.returncode, 0, first_cli.stdout + first_cli.stderr)
        self.assertEqual(first_cli.stdout, second_cli.stdout)
        self.assertEqual(len(first_cli.stdout.splitlines()), 16)

    def test_validator_registry_entry_and_profile_membership(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        ids = [item["id"] for item in registry["validators"]]
        self.assertEqual(ids.count("layer-manifest"), 1)
        self.assertIn("layer-manifest", registry["profiles"]["release-dry-run"])
        self.assertIn("layer-manifest", registry["profiles"]["full"])
        self.assertEqual(registry["profiles"]["full"], ids)


if __name__ == "__main__":
    unittest.main()
