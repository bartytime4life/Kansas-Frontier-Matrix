from __future__ import annotations

import json
import os
import subprocess
import unittest
from datetime import date
from pathlib import Path

from _support import FIXTURE_ROOT, VALIDATOR_DIR, copy_fixture, load_validator


stale_scan = load_validator()


class StaleScanCoreTests(unittest.TestCase):
    maxDiff = None

    def _scan(self, root: Path = FIXTURE_ROOT, **overrides):
        arguments = {
            "repo_root": root,
            "inputs": ("README.md", "docs"),
            "as_of": date(2026, 8, 7),
            "profile": "advisory",
            "review_window_days": 365,
            "placeholder_grace_days": 90,
            "type_windows": {},
            "git_diff": None,
            "warnings_as_errors": False,
        }
        arguments.update(overrides)
        return stale_scan.scan_stale_docs(**arguments)

    @staticmethod
    def _codes(result) -> set[str]:
        return {finding.code for finding in result.findings}

    def test_fixture_reports_expected_freshness_signals(self) -> None:
        result = self._scan()
        self.assertEqual(result.outcome, "DOC_STALE_SCAN_WARN")
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.counts["documents"], 3)
        self.assertEqual(result.counts["documents_with_metadata"], 3)
        self.assertEqual(
            self._codes(result),
            {
                "IMPLEMENTATION_CLAIM_REVIEW_DUE",
                "OWNER_PLACEHOLDER_STALE",
                "REVIEW_WINDOW_EXPIRED",
                "TEMPORARY_MARKER_EXPIRED",
                "VERIFICATION_DEBT_REVIEW_DUE",
            },
        )

    def test_json_and_digest_are_deterministic(self) -> None:
        first = self._scan()
        second = self._scan()
        self.assertEqual(first.report_digest, second.report_digest)
        self.assertEqual(first.to_json(), second.to_json())
        payload = json.loads(first.to_json())
        self.assertEqual(payload["profile"], "kfm.docs.stale-scan.v1")
        self.assertTrue(payload["report_digest"].startswith("sha256:"))

    def test_fixture_matches_reviewed_snapshot(self) -> None:
        expected = json.loads(
            (FIXTURE_ROOT / "expected_stale_scan_report.json").read_text(encoding="utf-8")
        )
        actual = json.loads(self._scan().to_json())
        self.assertEqual(actual, expected)

    def test_markdown_is_explicitly_non_authoritative(self) -> None:
        report = self._scan().to_markdown()
        self.assertIn("# KFM Documentation Freshness Workbench", report)
        self.assertIn("not doctrine", report)
        self.assertIn("IMPLEMENTATION_CLAIM_REVIEW_DUE", report)
        self.assertIn("docs/expired.md", report)

    def test_missing_review_date_warns_in_advisory_profile(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("updated: 2026-07-15\n", ""),
            encoding="utf-8",
        )
        result = self._scan(root)
        self.assertIn("REVIEW_DATE_MISSING", self._codes(result))
        self.assertEqual(result.outcome, "DOC_STALE_SCAN_WARN")

    def test_missing_review_date_fails_in_bounded_required_profile(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("updated: 2026-07-15\n", ""),
            encoding="utf-8",
        )
        result = self._scan(root, profile="bounded-required")
        finding = next(item for item in result.findings if item.code == "REVIEW_DATE_MISSING")
        self.assertEqual(finding.severity, "fail")
        self.assertEqual(result.exit_code, 1)

    def test_future_review_date_fails_closed(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("2026-07-15", "2026-09-01"),
            encoding="utf-8",
        )
        result = self._scan(root)
        self.assertIn("FUTURE_REVIEW_DATE", self._codes(result))
        self.assertEqual(result.exit_code, 1)

    def test_invalid_review_date_fails_closed(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("2026-07-15", "2026-02-30"),
            encoding="utf-8",
        )
        result = self._scan(root)
        self.assertIn("REVIEW_DATE_INVALID", self._codes(result))
        self.assertEqual(result.exit_code, 1)

    def test_created_after_review_date_fails_closed(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("created: 2026-05-01", "created: 2026-08-01"),
            encoding="utf-8",
        )
        result = self._scan(root)
        self.assertIn("DATE_ORDER_INVALID", self._codes(result))
        self.assertEqual(result.exit_code, 1)

    def test_type_specific_review_window_is_applied(self) -> None:
        result = self._scan(type_windows={"standard": 10})
        recent = next(item for item in result.documents if item["path"] == "docs/recent.md")
        self.assertEqual(recent["review_window_days"], 10)
        self.assertTrue(
            any(
                finding.code == "REVIEW_WINDOW_EXPIRED" and finding.path == "docs/recent.md"
                for finding in result.findings
            )
        )

    def test_warnings_as_errors_promotes_current_warnings(self) -> None:
        result = self._scan(warnings_as_errors=True)
        self.assertEqual(result.outcome, "DOC_STALE_SCAN_FAIL")
        self.assertTrue(all(item.severity == "fail" for item in result.findings))

    def test_malformed_meta_block_delegates_without_claiming_full_parse(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace(
                "<!-- [KFM_META_BLOCK_V2]",
                "<!-- [KFM_META_BLOCK_V2]\n<!-- [KFM_META_BLOCK_V2]",
            ),
            encoding="utf-8",
        )
        result = self._scan(root)
        self.assertIn("DELEGATE_TO_META_BLOCK", self._codes(result))
        self.assertFalse(
            any(
                item.code == "REVIEW_WINDOW_EXPIRED" and item.path == "docs/recent.md"
                for item in result.findings
            )
        )

    def test_path_escape_input_is_denied(self) -> None:
        with self.assertRaises(stale_scan.StaleScanError):
            self._scan(inputs=("../outside.md",))

    @unittest.skipIf(os.name == "nt", "symbolic-link behavior varies on Windows")
    def test_symbolic_link_input_is_denied(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        link = root / "linked.md"
        link.symlink_to(root / "README.md")
        with self.assertRaises(stale_scan.StaleScanError):
            self._scan(root, inputs=("linked.md",))

    def test_changed_file_ratchet_omits_unchanged_warnings(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "fixture@example.invalid"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Fixture"], cwd=root, check=True)
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "base"], cwd=root, check=True)
        base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
        recent = root / "docs" / "recent.md"
        recent.write_text(recent.read_text(encoding="utf-8") + "\nCurrent change.\n", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "change"], cwd=root, check=True)
        result = self._scan(root, git_diff=f"{base}...HEAD")
        self.assertEqual(result.findings, ())
        self.assertTrue(next(item for item in result.documents if item["path"] == "docs/recent.md")["current"])
        self.assertFalse(next(item for item in result.documents if item["path"] == "docs/expired.md")["current"])

    def test_changed_file_ratchet_downgrades_historical_failure(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        expired = root / "docs" / "expired.md"
        expired.write_text(
            expired.read_text(encoding="utf-8").replace("updated: 2024-01-15", "updated: invalid"),
            encoding="utf-8",
        )
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "fixture@example.invalid"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Fixture"], cwd=root, check=True)
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "base"], cwd=root, check=True)
        base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
        recent = root / "docs" / "recent.md"
        recent.write_text(recent.read_text(encoding="utf-8") + "\nCurrent change.\n", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "change"], cwd=root, check=True)
        result = self._scan(root, git_diff=f"{base}...HEAD")
        historical = next(item for item in result.findings if item.code == "REVIEW_DATE_INVALID")
        self.assertEqual(historical.severity, "warn")
        self.assertTrue(historical.historical)
        self.assertEqual(result.exit_code, 0)

    def test_static_import_boundary_contains_no_network_client(self) -> None:
        source = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(VALIDATOR_DIR.glob("*.py"))
        )
        for name in ("requests", "urllib.request", "httpx", "aiohttp", "socket"):
            self.assertNotIn(f"import {name}", source)
            self.assertNotIn(f"from {name}", source)


if __name__ == "__main__":
    unittest.main()
