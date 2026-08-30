from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from tools.validators.validate_pipeline_spec_declarations import (
    FIXTURE_ROOT,
    REPO_ROOT,
    SCHEMA_PATH,
    canonical_hash,
    validate_declaration,
    validate_fixtures,
    validate_repository,
)


class PipelineSpecDeclarationValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_all_current_yaml_declarations_pass(self) -> None:
        paths = sorted((REPO_ROOT / "pipeline_specs").rglob("*.yaml"))
        self.assertEqual(110, len(paths))
        result = validate_repository()
        self.assertTrue(result.ok, result.findings)
        self.assertEqual(110, result.checked_count)

    def test_all_current_declarations_are_explicitly_inactive(self) -> None:
        identities: set[str] = set()
        for path in sorted((REPO_ROOT / "pipeline_specs").rglob("*.yaml")):
            candidate = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertEqual("KfmPipelineSpecDeclaration", candidate["object_type"], path)
            self.assertEqual("PROPOSED_INACTIVE", candidate["status"], path)
            self.assertFalse(candidate["lifecycle"]["writes_targets"], path)
            execution = candidate["execution"]
            for field in (
                "network_access",
                "source_activation",
                "lifecycle_write",
                "promotion",
                "release",
                "publication",
            ):
                self.assertEqual("DENIED", execution[field], (path, field))
            self.assertNotIn(candidate["spec_id"], identities, path)
            identities.add(candidate["spec_id"])

    def test_json_profiles_remain_separate_schema_backed_objects(self) -> None:
        paths = sorted((REPO_ROOT / "pipeline_specs").rglob("*.json"))
        self.assertEqual(9, len(paths))
        for path in paths:
            candidate = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual("PROPOSED_INACTIVE", candidate["status"], path)

    def test_fixture_profile_passes(self) -> None:
        result = validate_fixtures()
        self.assertTrue(result.ok, result.findings)
        self.assertEqual(4, result.checked_count)

    def test_hash_mismatch_is_detected(self) -> None:
        candidate = yaml.safe_load(
            (FIXTURE_ROOT / "valid/stage_boundary.yaml").read_text(encoding="utf-8")
        )
        candidate["purpose"] += " Changed after hashing."
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "changed.yaml"
            path.write_text(yaml.safe_dump(candidate, sort_keys=False), encoding="utf-8")
            result, _ = validate_declaration(path, check_references=False)
        self.assertIn("SPEC_HASH_MISMATCH", {item.code for item in result.findings})

    def test_canonical_hash_excludes_only_spec_hash(self) -> None:
        candidate = yaml.safe_load(
            (FIXTURE_ROOT / "valid/stage_boundary.yaml").read_text(encoding="utf-8")
        )
        expected = candidate["spec_hash"]
        mutated = copy.deepcopy(candidate)
        mutated["spec_hash"] = "sha256:" + "0" * 64
        self.assertEqual(expected, canonical_hash(mutated))

    def test_duplicate_yaml_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text(
                "schema_version: 1.0.0\nschema_version: 1.0.0\n",
                encoding="utf-8",
            )
            result, _ = validate_declaration(path, check_references=False)
        self.assertEqual(
            {"YAML_DUPLICATE_KEY"},
            {item.code for item in result.findings},
        )

    def test_yaml_aliases_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "alias.yaml"
            path.write_text("source_docs: &docs []\ncopy: *docs\n", encoding="utf-8")
            result, _ = validate_declaration(path, check_references=False)
        self.assertEqual({"YAML_ALIAS_DENIED"}, {item.code for item in result.findings})

    def test_missing_reference_fails_closed(self) -> None:
        candidate = yaml.safe_load(
            (FIXTURE_ROOT / "valid/stage_boundary.yaml").read_text(encoding="utf-8")
        )
        candidate["source_docs"] = ["docs/does-not-exist.md"]
        candidate["spec_hash"] = canonical_hash(candidate)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "candidate.yaml"
            path.write_text(yaml.safe_dump(candidate, sort_keys=False), encoding="utf-8")
            result, _ = validate_declaration(path, repo_root=root, check_references=True)
        self.assertIn("REFERENCE_NOT_FOUND", {item.code for item in result.findings})

    def test_domain_and_spec_identity_must_match_declared_path(self) -> None:
        candidate = yaml.safe_load(
            (FIXTURE_ROOT / "valid/stage_boundary.yaml").read_text(encoding="utf-8")
        )
        candidate["domain_id"] = "soil"
        candidate["spec_id"] = "kfm.pipeline.soil.ingest"
        candidate["spec_hash"] = canonical_hash(candidate)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.yaml"
            path.write_text(yaml.safe_dump(candidate, sort_keys=False), encoding="utf-8")
            result, _ = validate_declaration(path, check_references=False)
        self.assertEqual(
            {"DOMAIN_PATH_MISMATCH", "SPEC_ID_DOMAIN_MISMATCH"},
            {
                item.code
                for item in result.findings
                if item.code in {"DOMAIN_PATH_MISMATCH", "SPEC_ID_DOMAIN_MISMATCH"}
            },
        )

    def test_validator_registry_wires_repository_and_changed_area_modes(self) -> None:
        registry = json.loads(
            (REPO_ROOT / "tools/validators/validator_registry.json").read_text(
                encoding="utf-8"
            )
        )
        entries = {item["id"]: item for item in registry["validators"]}
        entry = entries["pipeline-spec-declarations"]
        fixture_entry = entries["pipeline-spec-declaration-fixtures"]
        self.assertIn("pipeline-spec-declarations", registry["profiles"]["full"])
        self.assertIn(
            "pipeline-spec-declaration-fixtures", registry["profiles"]["full"]
        )
        self.assertEqual([], entry["args"])
        self.assertEqual(["--fixtures"], fixture_entry["args"])
        self.assertIn("pipeline_specs/**/*.yaml", entry["path_globs"])
        self.assertEqual(entry["path_globs"], fixture_entry["path_globs"])

    def test_cli_repository_and_fixture_profiles_pass(self) -> None:
        for extra in ((), ("--fixtures",)):
            with self.subTest(extra=extra):
                completed = subprocess.run(
                    [
                        sys.executable,
                        "tools/validators/validate_pipeline_spec_declarations.py",
                        *extra,
                    ],
                    cwd=REPO_ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
                report = json.loads(completed.stdout)
                self.assertEqual("PASS", report["outcome"])

    def test_workflow_watches_every_material_surface(self) -> None:
        workflow = (
            REPO_ROOT / ".github/workflows/pipeline-spec-declarations.yml"
        ).read_text(encoding="utf-8")
        for path in (
            "pipeline_specs/**",
            "contracts/pipeline_spec_declaration.md",
            "schemas/contracts/v1/pipeline_spec_declaration.schema.json",
            "fixtures/contracts/v1/pipeline_spec_declaration/**",
            "tools/validators/validate_pipeline_spec_declarations.py",
            "tests/validators/test_validate_pipeline_spec_declarations.py",
        ):
            self.assertEqual(2, workflow.count(f'- "{path}"'), path)


if __name__ == "__main__":
    unittest.main()
