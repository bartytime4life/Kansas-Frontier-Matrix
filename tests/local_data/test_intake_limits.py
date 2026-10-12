"""Explicit discovery budgets and active-source handling in actual intake paths."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.local_data import intake, intake_service
from tools.local_data.manage import init_store


class IntakeLimitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "store"
        init_store(self.root)
        self.raw = self.root / "data/raw/source"
        self.raw.mkdir()
        for name in ["a.csv", "b.csv", "c.csv"]:
            (self.raw / name).write_text("latitude,longitude\n38,-98\n")

    def tearDown(self):
        self.temp.cleanup()

    def test_selected_limit_reaches_all_files_and_records_the_budget(self):
        result = intake.analyze(self.root, max_files=3)
        self.assertEqual((result["state"], result["discovered"], result["max_files"]), ("complete", 3, 3))
        self.assertEqual(intake.overview(self.root)["last_run"]["max_files"], 3)

    def test_limit_failure_is_not_complete_or_binding_upgrade(self):
        with self.assertRaisesRegex(intake.IntakeError, "INTAKE_FILE_LIMIT"):
            intake.analyze(self.root, max_files=2)
        with intake.open_index(self.root, allow_stale_bindings=True) as conn:
            self.assertEqual(conn.execute("SELECT state,discovered FROM runs").fetchone(), ("failed", 2))
            self.assertIsNone(conn.execute("SELECT value FROM meta WHERE key='quarantine_binding_version'").fetchone())
        self.assertEqual(intake.analyze(self.root, max_files=3)["state"], "complete")

    def test_file_budget_validation_is_bounded_and_independent_of_bytes(self):
        for value in [0, -1, True, 5_000_001, "3000000", None]:
            with self.subTest(value=value), self.assertRaisesRegex(intake.IntakeError, "LIMIT_INVALID"):
                intake.analyze(self.root, max_files=value)
        self.assertEqual(intake.file_limit(3_000_000), 3_000_000)
        self.assertEqual(intake.parser().parse_args(["analyze", "--max-files", "3000000"]).max_files, 3_000_000)

    def test_service_passes_selected_limit_to_background_analysis(self):
        desk = intake_service.Desk(self.root, max_files=3_000_000)
        with patch.object(intake, "analyze", return_value={"state": "complete"}) as analyze:
            desk._run(None)
        self.assertEqual(analyze.call_args.kwargs["max_files"], 3_000_000)
        self.assertEqual(desk.status()["maxFiles"], 3_000_000)

    def test_transfer_fragments_and_live_sqlite_state_are_not_profiled(self):
        for name in ["unfinished.part", "unfinished.partial", "unfinished.tmp", "catalog.sqlite", "catalog.sqlite-wal", "catalog.sqlite-shm"]:
            (self.raw / name).write_bytes(b"not-complete-source-data")
        counters = {}
        rows = list(intake.discover(self.root, counters=counters, max_files=3))
        self.assertEqual(len(rows), 3)
        self.assertEqual(counters["live_database_skipped"], 1)
        self.assertEqual(counters["transient_skipped"], 5)

    def test_stale_running_rows_are_recovered_only_inside_the_writer_lock(self):
        with intake.open_index(self.root, allow_stale_bindings=True) as conn:
            conn.execute("INSERT INTO runs(run_id,started_at,state) VALUES ('old','2000-01-01','running')")
        intake.analyze(self.root, max_files=3)
        with intake.open_index(self.root) as conn:
            self.assertEqual(conn.execute("SELECT state FROM runs WHERE run_id='old'").fetchone(), ("interrupted",))

    def test_raising_hash_budget_reprofiles_unchanged_unhashed_files(self):
        intake.analyze(self.root, max_files=3, hash_limit=1)
        result = intake.analyze(self.root, max_files=3, hash_limit=1024)
        self.assertEqual(result["analyzed"], 3)
        with intake.open_index(self.root) as conn:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM items WHERE sha256 IS NOT NULL").fetchone()[0], 3)


if __name__ == "__main__":
    unittest.main()
