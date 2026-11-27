"""Private daily feed recovery, using journal fixtures and disposable checkpoints."""

from contextlib import redirect_stdout
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from tools.local_data import sql_feed_recovery as recovery, sql_feeds as core


NOW = datetime(2026, 11, 27, 18, tzinfo=timezone.utc)


def event(feed, event_kind, at, **fields):
    return {"feed": feed, "event": event_kind, "at": at, **fields}


def journal(*entries):
    return io.BytesIO(b"systemd service message\n" + b"".join(json.dumps(row).encode() + b"\n" for row in entries))


class RecoveryReportTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory(prefix="kfm-feed-recovery-")
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        self.db = self.root / "observations.sqlite"
        self.bulk = self.root / "bulk.sqlite"

    def make_database(self, path, *checkpoints):
        with sqlite3.connect(path) as db:
            db.executescript(core.SCHEMA)
            db.executemany("INSERT INTO kfm_feed_state VALUES (?, '{}', ?)", checkpoints)

    def report(self, entries, *selected):
        return recovery.report(entries, selected=selected, observations=self.db, bulk=self.bulk,
                               bulk_feeds=core.BULK_FEEDS, now=NOW)

    def test_report_distinguishes_run_receipts_from_checkpoints_and_never_creates_missing_db(self):
        self.make_database(self.db, ("ghcnd", "2026-11-27T11:00:00Z"), ("air-quality", "2026-11-26T13:00:00Z"))
        before = self.db.read_bytes()
        result = self.report(journal(
            event("ghcnd", "feed_done", "2026-11-27T12:00:00Z"),
            event("climdiv", "feed_done", "2026-11-25T12:00:00Z"),
            event("injected", "feed_done", "2026-11-27T12:00:00Z"),
            event("air-quality", "feed_done", "2026-11-27Z"),
            event("air-quality", "feed_done", "2026-11-28T12:00:00Z"),
        ), "ghcnd", "climdiv", "air-quality", "osm-kansas")
        rows = {row["feed"]: row for row in result["feeds"]}
        self.assertEqual(result["databases"], {"observations": "readable", "bulk": "missing"})
        self.assertEqual(rows["ghcnd"]["status"], "completed")
        self.assertEqual(rows["ghcnd"]["last_completed_at"], "2026-11-27T12:00:00Z")
        self.assertEqual(rows["ghcnd"]["last_sql_checkpoint_at"], "2026-11-27T11:00:00Z")
        self.assertEqual(rows["climdiv"]["status"], "overdue")
        self.assertEqual(rows["air-quality"]["status"], "missing-evidence")
        self.assertEqual(rows["air-quality"]["last_sql_checkpoint_at"], "2026-11-26T13:00:00Z")
        self.assertEqual(rows["osm-kansas"]["status"], "missing-evidence")
        self.assertFalse(self.bulk.exists())
        self.assertEqual(self.db.read_bytes(), before)

    def test_latest_overlapping_run_reports_start_even_if_older_attempt_finished_later(self):
        entries = journal(
            event("nwm", "feed_started", "2026-11-27T15:00:00Z", started_at="2026-11-27T15:00:00.001Z"),
            event("nwm", "feed_started", "2026-11-27T16:00:00Z", started_at="2026-11-27T16:00:00.002Z"),
            event("nwm", "feed_done", "2026-11-27T17:00:00Z", started_at="2026-11-27T15:00:00.001Z"),
            event("prism", "feed_started", "2026-11-27T04:00:00Z", started_at="2026-11-27T04:00:00.003Z"),
        )
        nwm, prism = self.report(entries, "nwm", "prism")["feeds"]
        self.assertEqual(nwm["status"], "in-progress")
        self.assertEqual(nwm["last_completed_at"], "2026-11-27T17:00:00Z")
        self.assertEqual(prism["status"], "missing-terminal-event")

    def test_failure_guidance_uses_only_reason_codes_and_uses_bulk_checkpoints(self):
        self.make_database(self.bulk, ("osm-kansas", "2026-11-27T03:00:00Z"))
        records = (
            event("osm-kansas", "feed_failed", "2026-11-27T04:00:00Z",
                  reason="HTTP_429 https://provider.example/?credential=private"),
            event("usgs-daily", "feed_failed", "2026-11-27T07:00:00Z",
                  reason="RAW_OBJECT_CHANGED /private/file"),
        )
        result = self.report(journal(*records), "usgs-daily", "osm-kansas")
        osm, usgs = result["feeds"]
        self.assertEqual(osm["last_sql_checkpoint_at"], "2026-11-27T03:00:00Z")
        self.assertEqual((osm["status"], osm["failure_code"]), ("retryable-failure", "HTTP_429"))
        self.assertEqual((usgs["status"], usgs["failure_code"]), ("review-required", "RAW_OBJECT_CHANGED"))
        self.assertNotIn("private", json.dumps(result))

    def test_persistent_holds_need_multiple_observations_and_reset_after_clear(self):
        dawn = event("captures", "feed_done", "2026-11-26T06:00:00Z",
                     held=3, held_reasons=["missing matching provenance receipt"])
        later = event("captures", "feed_done", "2026-11-27T15:00:00Z",
                      held=2, held_reasons=["file blockers", "unknown raw message"])
        cleared = event("captures", "feed_done", "2026-11-27T17:00:00Z", held=0, held_reasons=[])
        stalled = self.report(journal(dawn, later), "captures")["feeds"][0]["hold"]
        self.assertEqual(stalled["status"], "stalled")
        self.assertEqual(stalled["reason_codes"], ["CAPTURE_REVIEW_REQUIRED", "FILE_BLOCKERS"])
        self.assertEqual(self.report(journal(dawn), "captures")["feeds"][0]["hold"]["status"], "held-observation-stale")
        self.assertNotIn("hold", self.report(journal(dawn, later, cleared), "captures")["feeds"][0])

    def test_oversized_journal_fails_closed(self):
        with patch.object(recovery, "MAX_JOURNAL_LINE", 25):
            oversized = io.BytesIO(b"x" * 26 + b"\n")
            with self.assertRaisesRegex(ValueError, "JOURNAL_INPUT_LIMIT"):
                self.report(oversized, "captures")

    def test_cli_reads_explicit_feed_and_prints_a_report(self):
        stdout = io.StringIO()
        with patch("sys.stdin", io.TextIOWrapper(journal())), redirect_stdout(stdout):
            result = core.main(["--root", str(self.root), "--db", str(self.db),
                                "recovery-report", "--feed", "ghcnd"])
        self.assertEqual(result, 0)
        payload = json.loads(stdout.getvalue())
        self.assertEqual(payload["format"], "kfm-sql-feed-recovery-v1")
        self.assertEqual(payload["feeds"][0]["status"], "missing-evidence")

    def test_run_writes_correlated_evidence_for_handled_and_unexpected_errors(self):
        args = ["--root", str(self.root), "--db", str(self.db), "run", "ghcnd"]
        for error, code in ((core.FeedError("FETCH_FAILED provider"), "FETCH_FAILED provider"),
                            (RuntimeError("sensitive exception"), "UNEXPECTED_FEED_ERROR")):
            def fail(_):
                raise error

            stdout = io.StringIO()
            with patch.object(core, "resolve", return_value=fail), redirect_stdout(stdout):
                if isinstance(error, core.FeedError):
                    self.assertEqual(core.main(args), 1)
                else:
                    with self.assertRaises(RuntimeError):
                        core.main(args)
            start, failure = map(json.loads, stdout.getvalue().splitlines())
            self.assertEqual((start["event"], failure["event"]), ("feed_started", "feed_failed"))
            self.assertEqual(start["started_at"], failure["started_at"])
            self.assertEqual(failure["reason"], code)


if __name__ == "__main__":
    unittest.main()
