from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from _support import (
    DocsMetaBlockTestCase, FIXTURE_ROOT, VALIDATOR_PATH, meta_block,
)


class DocsMetaBlockRegistryTests(DocsMetaBlockTestCase):
    def test_missing_registry_entry_emits_review_only_add_candidate(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        registry = root / "control_plane" / "document_registry.yaml"
        registry.write_text(
            registry.read_text(encoding="utf-8").split(
                "  - doc_id: kfm://doc/fixture-beta", 1
            )[0],
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertEqual(result.outcome, "DOC_META_BLOCK_WARN")
        self.assertIn("REGISTRY_ENTRY_MISSING", self._codes(result))
        self.assertEqual(len(result.registry_delta), 1)
        self.assertEqual(result.registry_delta[0].action, "ADD_REVIEW")
        delta = json.loads(result.registry_delta_json())
        self.assertTrue(delta["review_only"])
        self.assertFalse(delta["mutates_registry"])
        self.assertEqual(delta["entries"][0]["unresolved_fields"], ["authority"])

    def test_registry_doc_id_path_conflict_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        registry = root / "control_plane" / "document_registry.yaml"
        registry.write_text(
            registry.read_text(encoding="utf-8").replace(
                "path: docs/beta.md", "path: docs/other.md"
            ),
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertIn("REGISTRY_DOC_ID_PATH_CONFLICT", self._codes(result))
        self.assertEqual(result.registry_delta[0].action, "HOLD_CONFLICT")

    def test_registry_path_doc_id_conflict_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        registry = root / "control_plane" / "document_registry.yaml"
        registry.write_text(
            registry.read_text(encoding="utf-8").replace(
                "kfm://doc/fixture-beta", "kfm://doc/other-beta"
            ),
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertIn("REGISTRY_PATH_DOC_ID_CONFLICT", self._codes(result))

    def test_historical_failures_are_downgraded_by_git_ratchet(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        beta = root / "docs" / "beta.md"
        beta.write_text(
            beta.read_text(encoding="utf-8").replace(
                "kfm://doc/fixture-beta", "kfm://doc/fixture-alpha"
            ),
            encoding="utf-8",
        )
        base = self._init_git(root)
        readme = root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\nChanged.\n")
        self._git(root, "add", "README.md")
        self._git(root, "commit", "-qm", "change unrelated doc")

        result = self._validate(root, registry=False, git_diff=f"{base}...HEAD")
        self.assertEqual(result.outcome, "DOC_META_BLOCK_WARN")
        duplicates = [item for item in result.findings if item.code == "DUPLICATE_DOC_ID"]
        self.assertTrue(duplicates)
        self.assertTrue(all(item.historical for item in duplicates))
        self.assertTrue(all(item.severity == "WARN" for item in duplicates))

    def test_current_registry_warning_can_be_promoted_to_failure(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        registry = root / "control_plane" / "document_registry.yaml"
        registry.write_text(
            registry.read_text(encoding="utf-8").split(
                "  - doc_id: kfm://doc/fixture-beta", 1
            )[0],
            encoding="utf-8",
        )
        base = self._init_git(root)
        beta = root / "docs" / "beta.md"
        beta.write_text(
            beta.read_text(encoding="utf-8").replace(
                "title: Beta Fixture", "title: Beta Fixture Revised"
            ),
            encoding="utf-8",
        )
        self._git(root, "add", "docs/beta.md")
        self._git(root, "commit", "-qm", "change beta")

        result = self._validate(
            root,
            git_diff=f"{base}...HEAD",
            warnings_as_errors=True,
        )
        self.assertEqual(result.outcome, "DOC_META_BLOCK_FAIL")
        finding = next(item for item in result.findings if item.code == "REGISTRY_ENTRY_MISSING")
        self.assertEqual(finding.severity, "FAIL")
        self.assertFalse(finding.historical)

    def test_cli_writes_report_and_registry_delta_without_mutating_registry(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        report = root / "out" / "report.json"
        delta = root / "out" / "delta.json"
        registry = root / "control_plane" / "document_registry.yaml"
        before = registry.read_bytes()
        run = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "--repo-root",
                str(root),
                "--registry",
                "control_plane/document_registry.yaml",
                "--format",
                "json",
                "--output",
                str(report),
                "--registry-delta-output",
                str(delta),
                "README.md",
                "docs",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertTrue(report.is_file())
        self.assertTrue(delta.is_file())
        self.assertEqual(registry.read_bytes(), before)
        self.assertFalse(json.loads(delta.read_text(encoding="utf-8"))["mutates_registry"])

    @unittest.skipIf(os.name == "nt", "symlink semantics differ on Windows")
    def test_symbolic_link_in_scope_is_denied(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        (root / "docs" / "link.md").symlink_to(root / "docs" / "alpha.md")
        with self.assertRaises(meta_block.MetaBlockError):
            self._validate(root)

    def test_validator_has_no_network_client_import(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        for forbidden in ("import requests", "import urllib", "import socket", "httpx"):
            self.assertNotIn(forbidden, source)


