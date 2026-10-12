"""Migration rejection, interruption recovery, and original preservation tests."""
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.local_data import consolidate as c


class ConsolidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "KFM-source"
        self.source.mkdir()
        self.allowed = self.root / "allowed"
        self.allowed.mkdir()
        self.repo = self.root / "repository"
        self.repo.mkdir()
        self.destination = self.allowed / "copy"
        self.receipts = self.root / "receipts"

    def tearDown(self):
        self.temp.cleanup()

    def put(self, relative, value=b"bytes"):
        target = self.source / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(value)
        return target

    def plan(self, **kwargs):
        args = dict(source=self.source, destination=self.destination, allowed_root=self.allowed,
                    repository=self.repo, owning_root="tools/", placement_basis="explicit test fixture", max_bytes=10000)
        return c.plan_copy(**{**args, **kwargs})

    def resign(self, plan):
        plan.pop("plan_sha256")
        plan["plan_sha256"] = hashlib.sha256(c.canonical(plan)).hexdigest()
        return plan

    def test_inventory_counts_hidden_runtime_bytes_without_reading_payloads(self):
        self.put("source/a", b"123")
        self.put(".wrangler/state", b"12345")
        with patch("builtins.open", side_effect=AssertionError("payload read")):
            scan = c.scan(self.source)
        self.assertTrue(scan["complete"])
        self.assertEqual((scan["files"], scan["bytes"]), (2, 8))
        self.assertIn(".wrangler", scan["protected"])

    def test_links_and_special_files_are_recorded_without_following(self):
        outside = self.root / "outside"; outside.mkdir(); (outside / "secret").write_bytes(b"secret")
        (self.source / "link").symlink_to(outside)
        os.mkfifo(self.source / "fifo")
        result = c.scan(self.source)
        self.assertEqual(result["files"], 0)
        self.assertEqual(result["links"][0]["target"], str(outside))
        self.assertEqual(result["special"], ["fifo"])
        with self.assertRaisesRegex(c.ConsolidationError, "PROTECTED_OR_LINKED"):
            self.plan()

    def test_symlink_ancestor_is_rejected(self):
        alias = self.root / "alias"; alias.symlink_to(self.source)
        self.assertFalse(c.scan(alias)["complete"])
        with self.assertRaises((OSError, c.ConsolidationError)):
            self.plan(source=alias)

    def test_limits_report_incomplete_instead_of_complete_partial_totals(self):
        self.put("a"); self.put("b")
        result = c.scan(self.source, max_entries=1)
        self.assertFalse(result["complete"])
        self.assertEqual(result["errors"][0]["code"], "SCAN_LIMIT")

    def test_every_project_gets_a_disposition_and_aliases_are_not_followed(self):
        self.put("a")
        (self.root / "MEGALODON").mkdir()
        (self.root / "KFM-current").symlink_to(self.source)
        result = c.inventory(self.root, self.repo, active_paths=[self.source / "a"])
        rows = {Path(r["path"]).name: r for r in result["folders"]}
        self.assertEqual(rows["KFM-source"]["disposition"], "preserve-active-consumers")
        self.assertEqual(rows["MEGALODON"]["disposition"], "exclude-separate-project")
        self.assertEqual(rows["KFM-current"]["kind"], "symlink")
        self.assertEqual(rows["repository"]["disposition"], "retain-canonical")

    def test_copy_verifies_bytes_keeps_originals_and_preserves_owner_execution(self):
        source = self.put("nested/start.sh", b"#!/bin/sh\nexit 0\n"); source.chmod(0o755)
        before = source.read_bytes()
        plan = self.plan()
        result = c.copy_plan(plan, self.receipts, reserve_bytes=0)
        self.assertEqual(source.read_bytes(), before)
        self.assertEqual((self.destination / "nested/start.sh").read_bytes(), before)
        self.assertEqual((self.destination / "nested/start.sh").stat().st_mode & 0o777, 0o700)
        self.assertTrue(result["originals_preserved"])
        self.assertIn("consumers-unchanged", result["state"])
        self.assertEqual(len(list(self.receipts.glob("*.json"))), 2)

    def test_interrupted_copy_resumes_without_overwriting_completed_files(self):
        self.put("a", b"a"); self.put("b", b"b")
        plan = self.plan()
        original = c.capture_file
        calls = []
        def interrupt(*args, **kwargs):
            calls.append(1)
            if len(calls) == 2: raise OSError("simulated interruption")
            return original(*args, **kwargs)
        with patch.object(c, "capture_file", side_effect=interrupt), self.assertRaises(OSError):
            c.copy_plan(plan, self.receipts, reserve_bytes=0)
        before = (self.destination / "a").stat().st_ino
        c.copy_plan(plan, self.receipts, reserve_bytes=0)
        self.assertEqual((self.destination / "a").stat().st_ino, before)
        self.assertEqual((self.destination / "b").read_bytes(), b"b")

    def test_destination_collision_is_never_merged(self):
        self.put("a"); self.destination.mkdir()
        with self.assertRaisesRegex(c.ConsolidationError, "DESTINATION_COLLISION"):
            self.plan()

    def test_changed_source_is_rejected_before_copy(self):
        file = self.put("a", b"old")
        plan = self.plan(); file.write_bytes(b"new")
        with self.assertRaisesRegex(c.ConsolidationError, "SOURCE_CHANGED"):
            c.copy_plan(plan, self.receipts, reserve_bytes=0)
        self.assertFalse(self.destination.exists())

    def test_changed_source_during_copy_prevents_success_receipt(self):
        file = self.put("a", b"old")
        plan = self.plan(); original = c.capture_file
        def changed(*args, **kwargs):
            original(*args, **kwargs); file.write_bytes(b"new")
        with patch.object(c, "capture_file", side_effect=changed), self.assertRaisesRegex(c.ConsolidationError, "DIGEST_MISMATCH"):
            c.copy_plan(plan, self.receipts, reserve_bytes=0)
        self.assertFalse(list(self.receipts.glob("*-verified.json")))

    def test_destination_digest_mismatch_and_extra_members_are_rejected(self):
        self.put("a", b"old"); plan = self.plan()
        c.copy_plan(plan, self.receipts, reserve_bytes=0)
        (self.destination / "a").write_bytes(b"new")
        with self.assertRaisesRegex(c.ConsolidationError, "DIGEST_MISMATCH"):
            c.verify_copy(plan)
        (self.destination / "a").write_bytes(b"old")
        (self.destination / "extra").write_bytes(b"x")
        with self.assertRaisesRegex(c.ConsolidationError, "MEMBERS_MISMATCH"):
            c.verify_copy(plan)

    def test_insufficient_space_does_not_create_destination(self):
        self.put("a"); plan = self.plan()
        with patch.object(c.shutil, "disk_usage", return_value=type("Usage", (), {"free": 0})()):
            with self.assertRaisesRegex(c.ConsolidationError, "INSUFFICIENT_COPY_SPACE"):
                c.copy_plan(plan, self.receipts)
        self.assertFalse(self.destination.exists())

    def test_git_runtime_and_secret_trees_require_separate_migration(self):
        for relative in [".git/config", ".wrangler/db.sqlite", ".env", "credentials.json"]:
            with self.subTest(relative=relative):
                file = self.put(relative)
                with self.assertRaisesRegex(c.ConsolidationError, "PROTECTED_OR_LINKED"):
                    self.plan()
                file.unlink()
                if file.parent != self.source: file.parent.rmdir()

    def test_external_data_store_cannot_be_copied_into_repository(self):
        self.put(".kfm-local-store.json", b"{}")
        with self.assertRaisesRegex(c.ConsolidationError, "EXTERNAL_STORE_MUST_REMAIN_SEPARATE"):
            self.plan(destination=self.repo / "data", allowed_root=self.repo)

    def test_overlap_containment_traversal_and_byte_limits(self):
        self.put("a", b"12345")
        for kwargs, reason in [({"destination": self.source / "copy"}, "OVERLAPPING"),
                               ({"destination": self.root / "outside"}, "OUTSIDE_ALLOWED"),
                               ({"source": str(self.source) + "/../KFM-source"}, "UNSAFE_ABSOLUTE"),
                               ({"max_bytes": 4}, "PLAN_BYTE_LIMIT"), ({"max_bytes": -1}, "INVALID_BYTE")]:
            with self.subTest(kwargs=kwargs), self.assertRaisesRegex(c.ConsolidationError, reason): self.plan(**kwargs)

    def test_plan_digest_is_checked_before_writes(self):
        self.put("a"); plan = self.plan(); plan["destination"] = str(self.root / "outside")
        with self.assertRaisesRegex(c.ConsolidationError, "PLAN_INTEGRITY_FAILED"):
            c.copy_plan(plan, self.receipts, reserve_bytes=0)

    def test_rehashed_plan_id_cannot_escape_receipt_root(self):
        self.put("a"); plan = self.plan(); plan["id"] = "../../outside"
        with self.assertRaisesRegex(c.ConsolidationError, "PLAN_ID_INVALID"):
            c.copy_plan(self.resign(plan), self.receipts, reserve_bytes=0)
        self.assertFalse(self.receipts.exists())

    def test_even_rehashed_plan_rejects_traversal_duplicates_secrets_and_bad_totals(self):
        self.put("a"); original = self.plan()
        for path in ["../outside", "/outside", "a/../b", ".env", ".git/config", "credentials.json"]:
            plan = json.loads(json.dumps(original)); plan["records"][0]["path"] = path
            with self.subTest(path=path), self.assertRaisesRegex(c.ConsolidationError, "PLAN_UNSAFE_MEMBER"):
                c.validate_plan(self.resign(plan))
        plan = json.loads(json.dumps(original)); plan["records"].append(plan["records"][0])
        with self.assertRaisesRegex(c.ConsolidationError, "PLAN_UNSAFE_MEMBER"):
            c.validate_plan(self.resign(plan))
        plan = json.loads(json.dumps(original)); plan["bytes"] += 1
        with self.assertRaisesRegex(c.ConsolidationError, "PLAN_TOTALS_MISMATCH"):
            c.validate_plan(self.resign(plan))

    def test_rollback_requires_no_pointer_change_because_original_remains(self):
        self.put("a"); plan = self.plan(); result = c.copy_plan(plan, self.receipts, reserve_bytes=0)
        self.assertTrue((self.source / "a").exists())
        self.assertIn("Consumers remain on the original path", result["rollback"])


if __name__ == "__main__":
    unittest.main()
