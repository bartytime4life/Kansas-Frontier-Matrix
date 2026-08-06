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


class DocsMetaBlockStructureTests(DocsMetaBlockTestCase):
    def test_valid_fixture_passes_with_registry_parity(self) -> None:
        result = self._validate(FIXTURE_ROOT)

        self.assertEqual(result.outcome, "DOC_META_BLOCK_PASS")
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.counts["documents"], 3)
        self.assertEqual(result.counts["metadata_blocks"], 2)
        self.assertEqual(result.counts["missing_metadata_blocks"], 1)
        self.assertEqual(result.counts["registered_documents"], 2)
        self.assertEqual(result.registry_delta, ())
        self.assertEqual(result.findings, ())

    def test_json_and_digest_are_deterministic(self) -> None:
        first = self._validate(FIXTURE_ROOT)
        second = self._validate(FIXTURE_ROOT)

        self.assertEqual(first.report_digest, second.report_digest)
        self.assertEqual(first.to_json(), second.to_json())
        payload = json.loads(first.to_json())
        self.assertEqual(payload["profile"], "kfm.docs.meta-block.v1")
        self.assertTrue(payload["report_digest"].startswith("sha256:"))

    def test_valid_fixture_matches_reviewed_snapshot(self) -> None:
        expected = json.loads(
            (FIXTURE_ROOT / "expected_meta_block_report.json").read_text(
                encoding="utf-8"
            )
        )
        actual = json.loads(self._validate(FIXTURE_ROOT).to_json())
        self.assertEqual(actual, expected)

    def test_markdown_workbench_exposes_review_only_boundary(self) -> None:
        report = self._validate(FIXTURE_ROOT).to_markdown()
        self.assertIn("# KFM Documentation Metadata Workbench", report)
        self.assertIn("## Review-only document-registry delta", report)
        self.assertIn("never writes", report)
        self.assertIn("not doctrine", report)

    def test_required_profile_rejects_missing_block(self) -> None:
        result = self._validate(FIXTURE_ROOT, profile=meta_block.PROFILE_REQUIRED)
        self.assertEqual(result.outcome, "DOC_META_BLOCK_FAIL")
        self.assertIn("META_BLOCK_MISSING", self._codes(result))

    def test_malformed_delimiter_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "alpha.md"
        alpha.write_text(
            alpha.read_text(encoding="utf-8").replace(
                "[/KFM_META_BLOCK_V2] -->", "[/KFM_META_BLOCK_V2]"
            ),
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertEqual(result.outcome, "DOC_META_BLOCK_FAIL")
        self.assertIn("META_BLOCK_MALFORMED", self._codes(result))

    def test_duplicate_block_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "alpha.md"
        content = alpha.read_text(encoding="utf-8")
        block = content.split("# Alpha Fixture", 1)[0]
        alpha.write_text(block + content, encoding="utf-8")
        result = self._validate(root)
        self.assertIn("META_BLOCK_DUPLICATE", self._codes(result))

    def test_duplicate_key_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "alpha.md"
        alpha.write_text(
            alpha.read_text(encoding="utf-8").replace(
                "title: Alpha Fixture\n", "title: Alpha Fixture\ntitle: Repeated\n"
            ),
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertIn("META_BLOCK_DUPLICATE_KEY", self._codes(result))

    def test_missing_required_field_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "alpha.md"
        alpha.write_text(
            alpha.read_text(encoding="utf-8").replace(
                "responsibility: exercise bounded metadata validation\n", ""
            ),
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertIn("REQUIRED_FIELD_MISSING", self._codes(result))

    def test_owner_and_owners_conflict_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "alpha.md"
        alpha.write_text(
            alpha.read_text(encoding="utf-8").replace(
                "owner: fixture-owner\n",
                "owner: fixture-owner\nowners: [\"fixture-reviewer\"]\n",
            ),
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertIn("OWNER_FIELDS_CONFLICT", self._codes(result))

    def test_invalid_document_identity_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "alpha.md"
        alpha.write_text(
            alpha.read_text(encoding="utf-8").replace(
                "kfm://doc/fixture-alpha", "not a kfm id"
            ),
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertIn("DOC_ID_INVALID", self._codes(result))

    def test_owning_root_mismatch_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "alpha.md"
        alpha.write_text(
            alpha.read_text(encoding="utf-8").replace(
                "owning_root: docs/", "owning_root: tools/"
            ),
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertIn("OWNING_ROOT_PATH_MISMATCH", self._codes(result))

    def test_invalid_date_and_date_order_fail_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "alpha.md"
        content = alpha.read_text(encoding="utf-8")
        content = content.replace("created: 2026-08-01", "created: 2026-99-99")
        alpha.write_text(content, encoding="utf-8")
        result = self._validate(root)
        self.assertIn("DATE_INVALID", self._codes(result))

        content = content.replace("created: 2026-99-99", "created: 2026-08-03")
        content = content.replace("updated: 2026-08-01", "updated: 2026-08-02")
        alpha.write_text(content, encoding="utf-8")
        result = self._validate(root)
        self.assertIn("DATE_ORDER_INVALID", self._codes(result))

    def test_related_path_escape_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "alpha.md"
        alpha.write_text(
            alpha.read_text(encoding="utf-8").replace(
                "  - docs/beta.md", "  - ../../outside.md"
            ),
            encoding="utf-8",
        )
        result = self._validate(root)
        self.assertIn("RELATED_PATH_ESCAPE", self._codes(result))

    def test_duplicate_doc_id_across_documents_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        beta = root / "docs" / "beta.md"
        beta.write_text(
            beta.read_text(encoding="utf-8").replace(
                "kfm://doc/fixture-beta", "kfm://doc/fixture-alpha"
            ),
            encoding="utf-8",
        )
        result = self._validate(root, registry=False)
        self.assertIn("DUPLICATE_DOC_ID", self._codes(result))

