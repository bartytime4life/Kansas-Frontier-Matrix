"""Tests for bounded changed GENERATED_RECEIPT selection."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
SELECTOR_PATH = (
    REPO_ROOT
    / "tools"
    / "validators"
    / "docs"
    / "document-graph"
    / "select_changed_receipts.py"
)

SPEC = importlib.util.spec_from_file_location(
    "kfm_document_graph_changed_receipts", SELECTOR_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"unable to load selector module from {SELECTOR_PATH}")
SELECTOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SELECTOR)

MATCHING_PREFIX = "data/receipts/generated/genrec-docs-document-graph-"


class ChangedReceiptSelectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self._temporary_directory.cleanup)
        self.repo = Path(self._temporary_directory.name)

        self._git("init")
        self._git("config", "user.name", "KFM Test")
        self._git("config", "user.email", "kfm-test@example.invalid")

        self._write("README.md", "# Fixture repository\n")
        self._write(
            "data/receipts/generated/genrec-docs-document-graph-existing.json",
            "{}\n",
        )
        self._write("data/receipts/generated/genrec-other-existing.json", "{}\n")
        self.base = self._commit("fixture base")

    def _git(self, *arguments: str) -> str:
        result = subprocess.run(
            ["git", *arguments],
            cwd=self.repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return result.stdout.strip()

    def _write(self, relative_path: str, content: str) -> None:
        target = self.repo / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def _commit(self, message: str) -> str:
        self._git("add", "--all")
        self._git("commit", "--message", message)
        return self._git("rev-parse", "HEAD")

    def _select(self, head: str, *, mode: str = "direct") -> list[str]:
        return SELECTOR.changed_receipt_paths(
            self.repo,
            base_ref=self.base,
            head_ref=head,
            mode=mode,
            prefix=MATCHING_PREFIX,
        )

    def test_artifact_only_change_does_not_revalidate_historical_receipt(self) -> None:
        self._write("README.md", "# Fixture repository\n\nLater artifact edit.\n")
        head = self._commit("edit artifact only")
        self.assertEqual(self._select(head), [])

    def test_added_matching_receipt_is_selected(self) -> None:
        path = (
            "data/receipts/generated/"
            "genrec-docs-document-graph-new.json"
        )
        self._write(path, "{}\n")
        head = self._commit("add matching receipt")
        self.assertEqual(self._select(head), [path])

    def test_modified_matching_receipt_is_selected(self) -> None:
        path = (
            "data/receipts/generated/"
            "genrec-docs-document-graph-existing.json"
        )
        self._write(path, '{"changed":true}\n')
        head = self._commit("modify matching receipt")
        self.assertEqual(self._select(head), [path])

    def test_unrelated_receipt_prefix_is_ignored(self) -> None:
        self._write(
            "data/receipts/generated/genrec-other-existing.json",
            '{"changed":true}\n',
        )
        head = self._commit("modify unrelated receipt")
        self.assertEqual(self._select(head), [])

    def test_deleted_receipt_is_not_selected(self) -> None:
        (
            self.repo
            / "data/receipts/generated/"
            "genrec-docs-document-graph-existing.json"
        ).unlink()
        head = self._commit("delete matching receipt")
        self.assertEqual(self._select(head), [])

    def test_renamed_matching_receipt_selects_current_path(self) -> None:
        old_path = (
            self.repo
            / "data/receipts/generated/"
            "genrec-docs-document-graph-existing.json"
        )
        new_relative = (
            "data/receipts/generated/"
            "genrec-docs-document-graph-renamed.json"
        )
        new_path = self.repo / new_relative
        old_path.rename(new_path)
        head = self._commit("rename matching receipt")
        self.assertEqual(self._select(head), [new_relative])

    def test_merge_base_mode_selects_feature_receipt(self) -> None:
        path = (
            "data/receipts/generated/"
            "genrec-docs-document-graph-feature.json"
        )
        self._write(path, "{}\n")
        head = self._commit("add feature receipt")
        self.assertEqual(self._select(head, mode="merge-base"), [path])

    def test_cli_emits_nul_delimited_paths(self) -> None:
        path = (
            "data/receipts/generated/"
            "genrec-docs-document-graph-cli.json"
        )
        self._write(path, "{}\n")
        head = self._commit("add cli receipt")

        result = subprocess.run(
            [
                sys.executable,
                str(SELECTOR_PATH),
                "--repo-root",
                str(self.repo),
                "--base",
                self.base,
                "--head",
                head,
                "--mode",
                "direct",
                "--prefix",
                MATCHING_PREFIX,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        self.assertEqual(result.stdout, path.encode("utf-8") + b"\0")

    def test_invalid_ref_fails_closed(self) -> None:
        with self.assertRaises(SELECTOR.SelectionError):
            SELECTOR.changed_receipt_paths(
                self.repo,
                base_ref="missing-ref",
                head_ref="HEAD",
                mode="direct",
                prefix=MATCHING_PREFIX,
            )

    def test_prefix_escape_is_denied(self) -> None:
        with self.assertRaises(SELECTOR.SelectionError):
            SELECTOR.changed_receipt_paths(
                self.repo,
                base_ref=self.base,
                head_ref="HEAD",
                mode="direct",
                prefix="../generated/",
            )


if __name__ == "__main__":
    unittest.main()
