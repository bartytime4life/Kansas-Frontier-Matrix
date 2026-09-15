"""Synthetic Git repositories prove immutable inputs and conservative outputs."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[2] / "tools/generators/build_repository_convergence_inventory.py"
SPEC = importlib.util.spec_from_file_location("convergence_inventory", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RepositoryConvergenceInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.parent = Path(self.temp.name)
        self.repo = self.parent / "repo"
        self.repo.mkdir()
        self.git("init", "-q")
        self.git("config", "user.name", "Synthetic Test")
        self.git("config", "user.email", "synthetic@example.invalid")
        registry = {"entry_defaults": {"owner": "@synthetic-owner"}, "roots": [
            {"path": "docs/", "root_id": "root.docs", "class": "canonical", "exposure": "public", "mutation": "versioned", "retention": "durable"},
            {"path": "catalog/", "root_id": "root.catalog", "class": "deprecated", "exposure": "internal", "mutation": "immutable", "retention": "migration_bound"},
            {"path": "apps/", "root_id": "root.apps", "class": "canonical"},
            {"path": "control_plane/", "root_id": "root.control-plane", "class": "canonical"},
        ]}
        self.write("control_plane/root_registry.yaml", json.dumps(registry))
        self.write("docs/a.md", "# Alpha\n\n## Shared\n\nEvidenceBundle is a carrier reference.\n")
        self.write("docs/b.md", "# Alpha\n\n## Shared\n\nEvidenceBundle is a carrier reference.\n")
        self.write("docs/normalized.md", "# Alpha  \r\n\r\n## Shared\r\n\r\nEvidenceBundle is a carrier reference.\r\n")
        self.write("docs/consumer.md", "# Consumer\n\n[A](a.md#shared)\n\n`docs/a.md`\nhttps://user:credential@example.invalid/source?token=SECRET\n")
        self.write("catalog/legacy.md", "# Legacy\n\nKeep historical knowledge.\n")
        self.write("unknown/b.md", "# Alpha\n\n## Shared\n\nEvidenceBundle is a carrier reference.\n")
        self.write("apps/x/contracts/local.md", "# Local\n")
        self.write("apps/x/package.json", '{"name":"synthetic","scripts":{"test":"echo not-run"}}')
        self.write("docs/empty/.gitkeep", "")
        self.commit = self.save()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], stderr=subprocess.DEVNULL).decode().strip()

    def write(self, relative, text):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode())

    def save(self):
        self.git("add", "--all")
        self.git("commit", "-qm", "synthetic fixture")
        return self.git("rev-parse", "HEAD")

    def build(self, commit=None, **kwargs):
        return MODULE.build_inventory(self.repo, commit or self.commit, history_limit=20, **kwargs)

    def test_worktree_changes_and_untracked_secrets_never_change_pinned_inventory(self):
        before = self.build()
        self.write("docs/a.md", "WORKTREE_SECRET\n")
        self.write(".env", "UNTRACKED_SECRET\n")
        (self.repo / "catalog/legacy.md").unlink()
        after = self.build()
        self.assertEqual(before, after)
        self.assertNotIn("WORKTREE_SECRET", json.dumps(after))
        self.assertNotIn(".env", [row["path"] for row in after["paths"]])

    def test_symlink_target_is_not_read_or_interpreted(self):
        secret = self.parent / "secret.txt"
        secret.write_text("EvidenceBundle PRIVATE_SECRET\n")
        os.symlink(secret, self.repo / "docs/link.md")
        self.commit = self.save()
        result = self.build()
        row = next(row for row in result["paths"] if row["path"] == "docs/link.md")
        self.assertEqual(row["sha256"], hashlib.sha256(str(secret).encode()).hexdigest())
        self.assertEqual("nonregular_not_analyzed", row["text_analysis"])
        self.assertNotIn("docs/link.md", [row["path"] for row in result["markdown"]])
        secret.write_text("DIFFERENT_PRIVATE_SECRET\n")
        self.assertEqual(result, self.build())

    def test_unknown_frozen_and_duplicate_paths_never_become_deletion_authority(self):
        result = self.build()
        rows = {row["path"]: row for row in result["paths"]}
        self.assertEqual("canonical", rows["docs/a.md"]["root_class"])
        self.assertEqual("@synthetic-owner", rows["docs/a.md"]["owner"])
        self.assertEqual("HOLD", rows["docs/a.md"]["classification"])
        self.assertEqual("UNKNOWN", rows["unknown/b.md"]["root_class"])
        self.assertEqual("immutable", rows["catalog/legacy.md"]["mutability_inherited"])
        self.assertIn("AUTHORITY_TRANSITION_HOLD", rows["catalog/legacy.md"]["review_flags"])
        self.assertIn("NESTED_RESPONSIBILITY_NAME_REVIEW", rows["apps/x/contracts/local.md"]["review_flags"])
        self.assertTrue(all(row["classification"] == "HOLD" for row in result["paths"]))
        self.assertTrue(all(not row["deletion_authorized"] for row in result["no_loss_ledger"]))
        exact = next(group for group in result["duplicates"]["exact_bytes"] if "docs/a.md" in group["paths"])
        self.assertIn("docs/b.md", exact["paths"])
        self.assertNotIn("docs/normalized.md", exact["paths"])
        norm = next(group for group in result["duplicates"]["normalized_text"] if "docs/a.md" in group["paths"])
        self.assertIn("docs/normalized.md", norm["paths"])
        self.assertEqual("UNKNOWN", rows["docs/a.md"]["consumer_closure"])

    def test_references_have_lineage_and_urls_drop_credentials(self):
        result = self.build()
        refs = result["references"]
        self.assertTrue(any(row["source"] == "docs/consumer.md" and row["target"] == "docs/a.md" and row["status"] == "heuristic_match" for row in refs))
        self.assertTrue(any(row["target"] == "https://example.invalid/source" for row in refs))
        self.assertNotIn("SECRET", json.dumps(result))
        self.assertNotIn("credential", json.dumps(result))
        self.assertEqual(3, sum(row["literal_occurrences"] for row in result["object_families"] if row["family"] == "EvidenceBundle" and row["root"] == "docs/"))

    def test_history_is_last_touch_at_pin_not_current_head(self):
        original = self.build()
        self.write("docs/a.md", "# Changed after pin\n")
        next_commit = self.save()
        self.assertNotEqual(self.commit, next_commit)
        self.assertEqual(original, self.build())
        rows = {row["path"]: row for row in self.build(next_commit)["paths"]}
        self.assertEqual(next_commit, rows["docs/a.md"]["last_touch_first_parent"])
        self.assertEqual(self.commit, rows["docs/b.md"]["last_touch_first_parent"])
        self.assertEqual("UNKNOWN", rows["docs/a.md"]["last_meaningful_change"])

    def test_moving_refs_tree_ids_and_symlink_registry_are_denied(self):
        for value in ("HEAD", "main", self.commit[:7], self.git("rev-parse", "HEAD^{tree}")):
            with self.assertRaises(MODULE.InventoryError):
                self.build(value)
        registry = self.repo / "control_plane/root_registry.yaml"
        registry.unlink()
        os.symlink("../docs/a.md", registry)
        with self.assertRaises(MODULE.InventoryError):
            self.build(self.save())

    def test_duplicate_registry_keys_fail_closed(self):
        self.write("control_plane/root_registry.yaml", '{"roots":[],"roots":[]}')
        with self.assertRaises(MODULE.InventoryError):
            self.build(self.save())

    def test_newline_and_marker_like_paths_keep_exact_history_identity(self):
        for path in ("docs/\nline.md", "COMMIT:" + "a" * 40):
            self.write(path, "# Exact path\n")
        self.commit = self.save()
        rows = {row["path"]: row for row in self.build()["paths"]}
        self.assertEqual(self.commit, rows["docs/\nline.md"]["last_touch_first_parent"])
        self.assertEqual(self.commit, rows["COMMIT:" + "a" * 40]["last_touch_first_parent"])

    def test_markdown_fenced_examples_do_not_become_declared_metadata_or_headings(self):
        self.write("docs/fenced.md", "# Actual\n\n```markdown\ndoc_id: example-only\n# False title\n```\n\n## Real\n")
        self.commit = self.save()
        doc = next(row for row in self.build()["markdown"] if row["path"] == "docs/fenced.md")
        self.assertEqual(["Actual", "Real"], [heading["title"] for heading in doc["headings"]])
        self.assertEqual({}, doc["declared"])

    def test_oversized_text_still_gets_complete_byte_hash(self):
        self.write("docs/large.md", "x" * 3000)
        self.commit = self.save()
        result = self.build(text_limit=2000)
        row = next(row for row in result["paths"] if row["path"] == "docs/large.md")
        self.assertEqual(hashlib.sha256(b"x" * 3000).hexdigest(), row["sha256"])
        self.assertEqual("size_limit", row["text_analysis"])
        self.assertNotIn("docs/large.md", [doc["path"] for doc in result["markdown"]])

    def test_reports_are_deterministic_private_and_bound_by_completion_manifest(self):
        result = self.build()
        first, second = self.parent / "first", self.parent / "second"
        a = MODULE.write_reports(result, first, self.repo)
        b = MODULE.write_reports(result, second, self.repo)
        self.assertEqual(a, b)
        self.assertEqual(0o700, first.stat().st_mode & 0o777)
        for name, record in a["files"].items():
            payload = (first / name).read_bytes()
            self.assertEqual(record["sha256"], hashlib.sha256(payload).hexdigest())
            self.assertEqual(payload, (second / name).read_bytes())
        self.assertEqual(a, json.loads((first / "manifest.json").read_text()))

    def test_overwrite_checkout_and_output_symlink_are_denied(self):
        result = self.build()
        existing = self.parent / "existing"
        existing.mkdir()
        os.symlink(existing, self.parent / "link")
        for output in (existing, self.parent / "link", self.repo / "reports", self.repo / ".git" / "reports", self.parent / "link" / "child"):
            with self.assertRaises(MODULE.InventoryError):
                MODULE.write_reports(result, output, self.repo)
        with self.assertRaises(MODULE.InventoryError):
            MODULE.write_reports(result, self.repo / "sibling-reports", self.repo / "docs")
        self.assertFalse((self.repo / "sibling-reports").exists())

    def test_cli_dry_run_creates_no_output_or_repository_changes(self):
        before = self.git("status", "--porcelain")
        result = subprocess.run(["python3", str(SCRIPT), "--repo", str(self.repo), "--commit", self.commit, "--history-limit", "20"], capture_output=True, text=True, check=True)
        self.assertEqual(self.commit, json.loads(result.stdout)["commit"])
        self.assertEqual(before, self.git("status", "--porcelain"))
        self.assertEqual(["repo"], sorted(path.name for path in self.parent.iterdir()))


if __name__ == "__main__":
    unittest.main()
