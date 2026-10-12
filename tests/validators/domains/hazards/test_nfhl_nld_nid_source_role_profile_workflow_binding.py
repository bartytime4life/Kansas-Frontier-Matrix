from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

import yaml

from tools.validators.validate_generated_receipt import (
    WORKFLOW_MIGRATION_MANIFEST_SHA256,
)

ROOT = Path(__file__).resolve().parents[4]
WORKFLOW = ROOT / ".github/workflows/nfhl-nld-nid-source-role-profile.yml"
MIGRATION_MANIFEST = ROOT / "tools/ci/python-dependency-lock-migration.json"
SELF_PATH = (
    "tests/validators/domains/hazards/"
    "test_nfhl_nld_nid_source_role_profile_workflow_binding.py"
)
RECEIPT_PATH = (
    "data/receipts/generated/"
    "genrec-nfhl-nld-nid-source-role-profile-receipt-trigger-closure-20260829.json"
)
DIRECT_EXECUTION_TRIGGER_PATHS = {
    "contracts/domains/hazards/nfhl_nld_nid_source_role_profile.md",
    "schemas/contracts/v1/domains/hazards/nfhl_nld_nid_source_role_profile.schema.json",
    "fixtures/contracts/v1/domains/hazards/nfhl_nld_nid_source_role_profile/**",
    "tools/validators/domains/hazards/validate_nfhl_nld_nid_source_role_profile.py",
    "tests/validators/domains/hazards/test_validate_nfhl_nld_nid_source_role_profile.py",
    "schemas/contracts/v1/**",
    "schemas/contracts/v1/receipts/generated_receipt.schema.json",
    "packages/hashing/src/hashing/**",
    "tools/validators/validate_generated_receipt.py",
    "tools/validators/_common/local_resolver.py",
    "tools/ci/install_python_ci.py",
    "tools/ci/python-dependency-lock-migration.json",
    "tools/ci/python-test.lock",
    "pyproject.toml",
}


class NfhlNldNidSourceRoleProfileWorkflowBindingTests(unittest.TestCase):
    def test_direct_execution_dependencies_trigger_both_hosted_events(self) -> None:
        workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        triggers = workflow["on"]

        for event in ("pull_request", "push"):
            with self.subTest(event=event):
                paths = set(triggers[event]["paths"])
                self.assertTrue(
                    DIRECT_EXECUTION_TRIGGER_PATHS.issubset(paths),
                    f"{event} paths must include the complete source-role execution seam",
                )
                self.assertIn(SELF_PATH, paths)
                self.assertIn(RECEIPT_PATH, paths)

    def test_workflow_and_manifest_hashes_match_migration_pins(self) -> None:
        manifest = json.loads(MIGRATION_MANIFEST.read_text(encoding="utf-8"))
        entries = {
            entry["path"]: entry
            for entry in manifest["entries"]
        }
        workflow_path = WORKFLOW.relative_to(ROOT).as_posix()

        self.assertEqual(
            entries[workflow_path]["current_sha256"],
            "sha256:" + hashlib.sha256(WORKFLOW.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            WORKFLOW_MIGRATION_MANIFEST_SHA256,
            "sha256:" + hashlib.sha256(MIGRATION_MANIFEST.read_bytes()).hexdigest(),
        )


if __name__ == "__main__":
    unittest.main()
