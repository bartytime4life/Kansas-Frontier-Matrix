"""The chunked incremental snapshot: restores, pruning, interruption, damage and live writers, on throwaway databases."""
from __future__ import annotations

from contextlib import closing
from datetime import datetime, timedelta, timezone
import errno
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zlib

from tools.local_data import sql_chunks as chunks

REPO = Path(__file__).resolve().parents[2]
with closing(sqlite3.connect(":memory:")) as _probe:
    HAS_DBPAGE = chunks._has_dbpage(_probe)
    HAS_FTS5 = any("FTS5" in row[0] for row in _probe.execute("PRAGMA compile_options"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ChunkCase(unittest.TestCase):
    """A small database shaped like the bulk one: an appended WITHOUT ROWID table, an index whose inserts scatter, and sources."""

    journal = "delete"

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.db_path = self.root / "data" / "kfm-bulk.sqlite"
        self.db_path.parent.mkdir()
        self.dest = self.root / "backup" / "bulk-chunks"
        self.dest.parent.mkdir()
        self.tick = 0
        patcher = patch.object(chunks, "CHUNK", 16384)
        patcher.start()
        self.addCleanup(patcher.stop)
        with closing(self.open()) as db:
            db.executescript("""
                PRAGMA page_size=4096;
                CREATE TABLE kfm_sql_sources (file_id INTEGER PRIMARY KEY, state TEXT, imported_rows INTEGER);
                CREATE TABLE kfm_values (file_id INTEGER, row_number INTEGER, geo TEXT, value TEXT, PRIMARY KEY(file_id,row_number)) WITHOUT ROWID;
                CREATE INDEX kfm_values_geo ON kfm_values(geo);
            """)
            db.execute(f"PRAGMA journal_mode={self.journal}")
        self.load(300)

    def open(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def load(self, rows: int, db: sqlite3.Connection | None = None) -> None:
        own = db is None
        db = db or self.open()
        with db:
            file_id = db.execute("INSERT INTO kfm_sql_sources(state,imported_rows) VALUES ('complete',?)", (rows,)).lastrowid
            db.executemany("INSERT INTO kfm_values VALUES (?,?,?,?)",
                           ((file_id, n, f"geo{(n * 37) % 97:03d}", f"{file_id}-{n}-" + "x" * 80) for n in range(rows)))
        if own:
            db.close()

    def rows(self, path: Path) -> int:
        with closing(sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)) as db:
            return db.execute("SELECT COUNT(*) FROM kfm_values").fetchone()[0]

    def clock(self):
        self.tick += 1
        return datetime(2026, 11, 4, tzinfo=timezone.utc) + timedelta(hours=self.tick)

    def take(self, **options) -> dict:
        options.setdefault("device_check", False)
        return chunks.snapshot(self.db_path, self.dest, now=self.clock, **options)

    def manifests(self) -> list[str]:
        return sorted(p.name for p in (self.dest / "manifests").glob("*.json"))

    def manifest(self, name: str) -> dict:
        return json.loads((self.dest / "manifests" / name).read_text())

    def stored(self) -> set[str]:
        return {p.name[:-2] for p in (self.dest / "chunks").glob("*/*.z")}

    def restored(self, name: str, label: str = "restored") -> Path:
        """Rebuild a kept copy and prove it: integrity_check through restore, then the hash the snapshot reported."""
        target = self.root / f"{label}-{name}.sqlite"
        target.unlink(missing_ok=True)
        result = chunks.restore(self.dest, name, target)
        self.assertEqual(result["state"], "restored")
        self.assertEqual(sha(target), self.manifest(name)["sha256"])
        with closing(sqlite3.connect(target.as_uri() + "?mode=ro", uri=True)) as db:
            self.assertEqual(db.execute("PRAGMA integrity_check").fetchall(), [("ok",)])
            self.assertEqual(db.execute("PRAGMA journal_mode").fetchone()[0], "delete")
        return target


class SnapshotTests(ChunkCase):
    def test_a_restore_reproduces_each_kept_copy_exactly(self):
        first = self.take()
        self.assertEqual((first["state"], first["new_chunks"]), ("stored", len(set(self.manifest(first["snapshot"])["chunks"]))))
        self.assertEqual(sha(self.db_path), first["sha256"], "a rollback-journal source is copied byte for byte")
        before = self.db_path.read_bytes()
        self.load(50)
        second = self.take()
        self.assertEqual(self.manifests(), sorted([first["snapshot"], second["snapshot"]]))
        self.assertLess(second["new_chunks"], second["chunks"], "only what changed is written")
        self.assertEqual(self.rows(self.restored(first["snapshot"])), 300)
        self.assertEqual(self.rows(self.restored(second["snapshot"])), 350)
        self.assertEqual(self.restored(first["snapshot"], "again").read_bytes(), before)
        self.assertEqual(oct((self.dest / "manifests" / first["snapshot"]).stat().st_mode & 0o777), "0o600")
        self.assertEqual({oct(p.stat().st_mode & 0o777) for p in (self.dest / "chunks").glob("*/*.z")}, {"0o600"})

    def test_the_chunk_size_does_not_matter_to_a_restore(self):
        first = self.take()
        self.load(20)
        with patch.object(chunks, "CHUNK", 4096 * 3):
            second = self.take()
        self.assertEqual(self.rows(self.restored(first["snapshot"])), 300)
        self.assertEqual(self.rows(self.restored(second["snapshot"])), 320)

    def test_a_database_larger_than_the_cache_and_with_a_partial_last_chunk(self):
        self.load(5000)
        first = self.take()
        self.assertEqual(self.manifest(first["snapshot"])["bytes"] % chunks.CHUNK != 0, True, "the last chunk is short")
        self.assertEqual(self.rows(self.restored(first["snapshot"])), 5300)

    @unittest.skipUnless(HAS_FTS5, "this SQLite has no FTS5")
    def test_a_full_text_index_survives_the_round_trip(self):
        with closing(self.open()) as db, db:
            db.execute("CREATE VIRTUAL TABLE kfm_fts USING fts5(text)")
            db.executemany("INSERT INTO kfm_fts VALUES (?)", ((f"homestead claim number {n} county {n % 105}",) for n in range(4000)))
        first = self.take()
        with closing(self.open()) as db, db:
            db.executemany("INSERT INTO kfm_fts VALUES (?)", ((f"railroad depot {n}",) for n in range(2000)))
        second = self.take()
        with closing(sqlite3.connect(self.restored(second["snapshot"]))) as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM kfm_fts WHERE kfm_fts MATCH 'railroad'").fetchone()[0], 2000)
            self.assertEqual(db.execute("SELECT COUNT(*) FROM kfm_fts WHERE kfm_fts MATCH 'homestead'").fetchone()[0], 4000)
            db.execute("INSERT INTO kfm_fts(kfm_fts) VALUES ('integrity-check')")
        with closing(sqlite3.connect(self.restored(first["snapshot"]))) as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM kfm_fts WHERE kfm_fts MATCH 'railroad'").fetchone()[0], 0)

    def test_an_untouched_database_is_not_read_and_a_rewritten_one_is_not_stored_twice(self):
        first = self.take()
        with patch.object(chunks, "_store", side_effect=AssertionError("read")):
            untouched = self.take()
        self.assertEqual((untouched["state"], untouched["mode"], untouched["snapshot"]), ("unchanged", "untouched", first["snapshot"]))
        os.utime(self.db_path)
        same = self.take()
        self.assertEqual((same["state"], same["mode"], same["snapshot"]), ("unchanged", "read", first["snapshot"]))
        with patch.object(chunks, "_store", side_effect=AssertionError("read")):
            self.assertEqual(self.take()["mode"], "untouched", "the new file time was recorded")
        self.assertEqual(self.manifests(), [first["snapshot"]])

    def test_a_clock_behind_the_newest_copy_stops_the_run_instead_of_pruning_it(self):
        first = self.take()
        self.load(10)
        with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_CLOCK_BEHIND"):
            chunks.snapshot(self.db_path, self.dest, device_check=False, now=lambda: datetime(2020, 1, 1, tzinfo=timezone.utc))
        self.assertEqual(self.manifests(), [first["snapshot"]])

    def test_refusals(self):
        with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_SAME_DEVICE"):
            chunks.snapshot(self.db_path, self.dest)
        with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_DESTINATION_MISSING"):
            chunks.snapshot(self.db_path, self.root / "unmounted" / "store" / "bulk", device_check=False)
        self.assertFalse((self.root / "unmounted").exists())
        with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_KEEP_INVALID"):
            self.take(keep=0)
        with self.assertRaisesRegex(chunks.ChunkError, "DATABASE_MISSING"):
            chunks.snapshot(self.root / "none.sqlite", self.dest, device_check=False)
        first = self.take()
        with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_MISSING"):
            chunks.restore(self.dest, "../" + first["snapshot"], self.root / "out.sqlite")
        existing = self.root / "existing.sqlite"
        existing.write_bytes(b"keep me")
        with self.assertRaisesRegex(chunks.ChunkError, "RESTORE_TARGET_EXISTS"):
            chunks.restore(self.dest, first["snapshot"], existing)
        self.assertEqual(existing.read_bytes(), b"keep me")
        with self.assertRaisesRegex(chunks.ChunkError, "CHECK_LEVEL_INVALID"):
            chunks.check(self.dest, level="fast")
        with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_MISSING"):
            chunks.check(self.root / "backup" / "nothing")

    def test_one_run_at_a_time_per_destination(self):
        first = self.take()
        with chunks._exclusive(self.dest):
            with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_BUSY"):
                self.take()
            with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_BUSY"):
                chunks.check(self.dest)
            with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_BUSY"):
                chunks.restore(self.dest, first["snapshot"], self.root / "busy.sqlite")
        self.assertFalse((self.root / "busy.sqlite").exists())

    def test_a_killed_restores_partial_file_is_replaced(self):
        first = self.take()
        target = self.root / "out.sqlite"
        Path(str(target) + ".partial").write_bytes(b"half a restore")
        self.assertEqual(chunks.restore(self.dest, first["snapshot"], target)["state"], "restored")
        self.assertEqual(sha(target), first["sha256"])
        self.assertEqual(list(self.root.glob("out.sqlite.*")), [])

    def test_the_command_reports_json_and_a_fixed_reason(self):
        run = [sys.executable, "-m", "tools.local_data.sql_chunks"]
        taken = subprocess.run([*run, "snapshot", "--db", str(self.db_path), "--dest", str(self.dest), "--allow-same-device"],
                               cwd=REPO, capture_output=True, text=True, check=True)
        name = json.loads(taken.stdout)["snapshot"]
        checked = subprocess.run([*run, "check", "--dest", str(self.dest)], cwd=REPO, capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(checked.stdout)["state"], "verified")
        target = self.root / "cli.sqlite"
        back = subprocess.run([*run, "restore", "--dest", str(self.dest), "--manifest", name, "--to", str(target)],
                              cwd=REPO, capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(back.stdout)["sha256"], sha(target))
        refused = subprocess.run([*run, "snapshot", "--db", str(self.db_path), "--dest", str(self.dest)], cwd=REPO, capture_output=True, text=True)
        self.assertEqual((refused.returncode, json.loads(refused.stdout)["reason"]), (1, "SNAPSHOT_SAME_DEVICE"))


class PruningTests(ChunkCase):
    def test_pruning_keeps_every_kept_copy_restorable_and_removes_only_unused_chunks(self):
        names = []
        for rows in range(5):
            self.load(120)
            names.append(self.take()["snapshot"])
        self.assertEqual(self.manifests(), sorted(names[-2:]))
        used = {d for name in names[-2:] for d in self.manifest(name)["chunks"]}
        self.assertEqual(self.stored(), used, "chunks only the pruned copies used are gone, and nothing a kept copy needs")
        self.assertEqual(self.rows(self.restored(names[-2])), 300 + 4 * 120)
        self.assertEqual(self.rows(self.restored(names[-1])), 300 + 5 * 120)

    def test_keep_one_still_restores(self):
        self.take()
        self.load(40)
        newest = self.take(keep=1)
        self.assertEqual(self.manifests(), [newest["snapshot"]])
        self.assertEqual(self.rows(self.restored(newest["snapshot"])), 340)

    def test_the_newest_checked_copy_outlives_keep(self):
        checked = self.take()["snapshot"]
        chunks.check(self.dest, now=self.clock)
        later = []
        for _ in range(4):
            self.load(60)
            later.append(self.take()["snapshot"])
        self.assertEqual(self.manifests(), sorted([checked, *later[-2:]]))
        self.assertEqual(self.rows(self.restored(checked)), 300, "the known good copy still restores")
        chunks.check(self.dest, now=self.clock)
        self.load(60)
        newest = self.take()["snapshot"]
        self.assertEqual(self.manifests(), sorted([later[-1], newest]), "a newer check releases it")
        self.assertFalse((self.dest / "checks" / checked).exists())
        self.assertEqual(self.stored(), {d for n in self.manifests() for d in self.manifest(n)["chunks"]})

    def test_an_unreadable_manifest_stops_the_run_before_anything_is_removed(self):
        first = self.take()["snapshot"]
        before = self.stored()
        (self.dest / "manifests" / first).write_text("{not json")
        self.load(10)
        with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_MANIFEST_UNREADABLE"):
            self.take()
        self.assertEqual(self.stored(), before, "a manifest that cannot be read must not make its chunks look unused")


class InterruptionTests(ChunkCase):
    def test_a_failed_write_publishes_nothing_and_the_earlier_copy_restores(self):
        first = self.take()["snapshot"]
        before = self.db_path.read_bytes()
        self.load(100)
        real, calls = chunks._write_chunk, []

        def full(dest, digest, body):
            calls.append(digest)
            if len(calls) == 2:
                raise OSError(errno.ENOSPC, "No space left on device")
            real(dest, digest, body)

        with patch.object(chunks, "_write_chunk", full), self.assertRaisesRegex(OSError, "No space"):
            self.take()
        self.assertEqual(self.manifests(), [first])
        self.assertEqual(self.restored(first).read_bytes(), before)
        result = self.take()
        self.assertEqual(result["removed_leftovers"]["chunks"], 1, "the next run sweeps the failed run's chunk first")
        self.assertEqual(self.rows(self.restored(result["snapshot"])), 400)
        self.assertEqual(self.rows(self.restored(first)), 300)

    def kill_at(self, stage: str):
        """A real SIGKILL at one point of a real snapshot, in another process. The harness itself keeps nothing in memory."""
        code = f"""
from datetime import datetime
import os, signal, sys
from pathlib import Path
from tools.local_data import sql_chunks as c
c.CHUNK = {chunks.CHUNK}
die = lambda *a, **k: os.kill(os.getpid(), signal.SIGKILL)
stage = {stage!r}
if stage == "during-chunks":
    real, count = c._write_chunk, [0]
    def write(dest, digest, body):
        count[0] += 1
        if count[0] == 2:
            part = c._chunk(dest, digest).with_name(digest + ".z.part")
            part.parent.mkdir(exist_ok=True)
            part.write_bytes(body[:7])
            die()
        real(dest, digest, body)
    c._write_chunk = write
elif stage == "before-manifest":
    c._syncfs = die
elif stage == "half-manifest":
    real = c._write_json
    def half(path, value):
        path.with_name(path.name + ".part").write_text("half a manifest")
        die()
    c._write_json = half
elif stage == "before-prune":
    c._prune = die
elif stage == "during-prune":
    real = Path.unlink
    def unlink(self, *a, **k):
        if self.suffix == ".z":
            die()
        return real(self, *a, **k)
    Path.unlink = unlink
c.snapshot(Path({str(self.db_path)!r}), Path({str(self.dest)!r}), keep=2, device_check=False,
           now=lambda: datetime.fromisoformat({self.clock().isoformat()!r}))
"""
        done = subprocess.run([sys.executable, "-c", code], cwd=REPO, capture_output=True, text=True)
        self.assertEqual(done.returncode, -9, done.stderr)

    def test_a_killed_run_at_any_point_leaves_earlier_copies_restorable(self):
        for stage, published, oldest_kept in (("during-chunks", False, True), ("before-manifest", False, True), ("half-manifest", False, True),
                                              ("before-prune", True, True), ("during-prune", True, False)):
            with self.subTest(stage=stage):
                self.dest_reset()
                self.load(100)
                one = self.take()["snapshot"]
                self.load(100)
                two = self.take()["snapshot"]
                bytes_one, bytes_two = self.restored(one).read_bytes(), self.restored(two).read_bytes()
                count = self.rows(self.db_path)
                self.load(100)
                self.kill_at(stage)
                names = self.manifests()
                self.assertEqual(one in names, oldest_kept, "manifests are removed before their chunks")
                if oldest_kept:
                    self.assertEqual(self.restored(one).read_bytes(), bytes_one)
                self.assertEqual(self.restored(two).read_bytes(), bytes_two)
                if published:
                    newest = sorted(set(names) - {one, two})[0]
                    self.assertEqual(self.rows(self.restored(newest)), count + 100, "a published copy is complete")
                else:
                    self.assertEqual(sorted(names), sorted([one, two]))
                self.assertEqual(chunks.check(self.dest, now=self.clock)["state"], "verified")
                self.load(10)
                result = self.take()
                self.assertEqual(self.rows(self.restored(result["snapshot"])), count + 110)
                self.assertEqual(self.stored(), {d for n in self.manifests() for d in self.manifest(n)["chunks"]},
                                 "the next run leaves no chunk a manifest does not name")
                self.assertEqual([p for p in self.dest.rglob("*.part")], [])

    def dest_reset(self):
        shutil.rmtree(self.dest, ignore_errors=True)


class DamageTests(ChunkCase):
    def damage(self, digest: str, how: str = "wrong") -> None:
        path = chunks._chunk(self.dest, digest)
        if how == "wrong":
            path.write_bytes(zlib.compress(b"not the original chunk"))
        elif how == "cut":
            path.write_bytes(path.read_bytes()[:9])
        else:
            path.unlink()

    def test_damage_fails_the_check_and_the_next_copy_rewrites_it(self):
        for how in ("wrong", "cut", "missing"):
            with self.subTest(how=how):
                shutil.rmtree(self.dest, ignore_errors=True)
                first = self.take()
                self.assertEqual(chunks.check(self.dest, now=self.clock)["state"], "verified")
                digest = self.manifest(first["snapshot"])["chunks"][2]
                self.damage(digest, how)
                with self.assertRaisesRegex(chunks.ChunkError, f"SNAPSHOT_CHUNK_DAMAGED 1 first {digest}"):
                    chunks.check(self.dest, now=self.clock)
                target = self.root / "damaged.sqlite"
                with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_CHUNK_DAMAGED"):
                    chunks.restore(self.dest, first["snapshot"], target)
                self.assertEqual(list(self.root.glob("damaged.sqlite*")), [], "no partial restore is left")
                self.assertEqual(list((self.dest / "staging").glob("*")), [])
                second = self.take()   # the file is untouched, but a chunk is missing, so it is read and written again
                self.assertEqual((second["state"], second["new_chunks"]), ("unchanged", 1))
                self.assertEqual(self.rows(self.restored(first["snapshot"])), 300)
                self.assertEqual(chunks.check(self.dest, now=self.clock)["state"], "verified")

    def test_damage_to_a_chunk_only_an_older_copy_uses_is_found_too(self):
        first = self.take()
        self.load(100)
        second = self.take()
        only_old = sorted(set(self.manifest(first["snapshot"])["chunks"]) - set(self.manifest(second["snapshot"])["chunks"]))[0]
        self.damage(only_old)
        with self.assertRaisesRegex(chunks.ChunkError, f"SNAPSHOT_CHUNK_DAMAGED 1 first {only_old}"):
            chunks.check(self.dest, now=self.clock)
        self.assertEqual(self.rows(self.restored(second["snapshot"])), 400, "the newest copy still restores")

    def test_a_corrupt_database_fails_the_check_and_gets_no_receipt(self):
        with closing(self.open()) as db:
            page = db.execute("SELECT rootpage FROM sqlite_master WHERE name='kfm_values_geo'").fetchone()[0]
        with open(self.db_path, "r+b") as out:   # a b-tree page that no longer parses, as a bad sector would leave it
            out.seek((page - 1) * 4096)
            out.write(b"\xee" * 4096)
        first = self.take()
        with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_INTEGRITY_FAILED"):
            chunks.check(self.dest, now=self.clock)
        self.assertFalse((self.dest / "checks" / first["snapshot"]).exists())


class LiveWalTests(ChunkCase):
    journal = "wal"

    def writer(self) -> sqlite3.Connection:
        db = self.open()
        db.execute("PRAGMA wal_autocheckpoint=0")
        self.addCleanup(db.close)
        return db

    @unittest.skipUnless(HAS_DBPAGE, "this SQLite has no sqlite_dbpage")
    def test_commits_still_in_the_wal_are_in_the_copy_and_the_source_is_not_written(self):
        writer = self.writer()
        self.load(200, writer)
        wal = Path(str(self.db_path) + "-wal")
        self.assertGreater(wal.stat().st_size, 0)
        file_before, wal_before = sha(self.db_path), sha(wal)
        result = self.take()
        self.assertEqual((sha(self.db_path), sha(wal)), (file_before, wal_before), "no checkpoint, and nothing else written")
        self.assertEqual(result["source_mode"], "wal")
        target = self.restored(result["snapshot"])
        self.assertEqual(self.rows(target), 500, "pages in the WAL were read, not the older ones in the file")

    @unittest.skipUnless(HAS_DBPAGE, "this SQLite has no sqlite_dbpage")
    def test_writers_keep_committing_during_a_copy_and_it_holds_one_commit(self):
        writer = self.writer()
        self.load(200, writer)
        real, passes = chunks._read_pages, [0]

        def busy(db, page_size):
            for data in real(db, page_size):
                if passes[0] < 3:   # a writer gets through mid-copy, and is not blocked by the reader
                    self.load(100, writer)
                    passes[0] += 1
                yield data

        with patch.object(chunks, "_read_pages", busy):
            result = self.take()
        self.assertEqual(passes[0], 3)
        self.assertEqual(self.rows(self.restored(result["snapshot"])), 500, "the three later commits are not in this copy")
        self.assertEqual(self.manifest(result["snapshot"])["source_rows"], 500)
        self.assertEqual(self.rows(self.db_path), 800)
        next_copy = self.take()
        self.assertEqual(self.rows(self.restored(next_copy["snapshot"])), 800)

    @unittest.skipUnless(HAS_DBPAGE, "this SQLite has no sqlite_dbpage")
    def test_a_checkpoint_during_the_copy_does_not_disturb_it(self):
        writer = self.writer()
        self.load(200, writer)
        real, passes = chunks._read_pages, [0]

        def busy(db, page_size):
            for data in real(db, page_size):
                if not passes[0]:
                    self.load(100, writer)
                    writer.execute("PRAGMA wal_checkpoint(PASSIVE)").fetchall()
                    passes[0] += 1
                yield data

        with patch.object(chunks, "_read_pages", busy):
            result = self.take()
        self.assertEqual(self.rows(self.restored(result["snapshot"])), 500)

    def test_an_untouched_file_is_skipped_but_a_new_commit_in_the_wal_is_not(self):
        with closing(self.open()) as db:
            db.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchall()
        first = self.take()
        with patch.object(chunks, "_store", side_effect=AssertionError("read")):
            self.assertEqual(self.take()["mode"], "untouched")
        if not HAS_DBPAGE:
            return
        writer = self.writer()
        self.load(5, writer)
        second = self.take()
        self.assertEqual(second["state"], "stored")
        self.assertNotEqual(second["sha256"], first["sha256"])

    def test_without_sqlite_dbpage_a_wal_with_frames_is_refused_not_copied_stale(self):
        writer = self.writer()
        self.load(50, writer)
        with patch.object(chunks, "_has_dbpage", lambda db: False):
            with self.assertRaisesRegex(chunks.ChunkError, "SNAPSHOT_NEEDS_DBPAGE"):
                self.take()
        self.assertEqual(self.manifests(), [])

    def test_without_sqlite_dbpage_an_empty_wal_reads_the_file(self):
        with closing(self.open()) as db:
            db.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchall()
        with patch.object(chunks, "_has_dbpage", lambda db: False):
            result = self.take()
        self.assertEqual(self.rows(self.restored(result["snapshot"])), 300)
