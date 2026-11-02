"""Nightly verified copy of the SQL database on the backup volume, keeping the newest two.

The per-file backup keeps every version of every file, so a database the feeds change every hour
would add a full copy each night. The owner chose on 2026-11-01 to back it up this way instead:
one page-level copy a night (SQLite's backup API, taken while the pipeline lock keeps writers
out), checked with ``PRAGMA quick_check`` and its row counts, renamed into place with its
SHA-256 in the name, and recorded by a receipt. Only after a new copy passes are copies older
than the newest ``keep`` deleted; their receipts stay. ``check`` re-reads the newest copy for the
monthly restore test without copying it anywhere. One snapshot or check runs at a time per
destination (``.snapshot.lock``), from cleanup to pruning; the pipeline lock covers only the copy.

The copy is a standalone rollback-journal file. To restore, copy it over ``observations.sqlite``
with the feeds and the local-data gateway stopped; the feeds switch it back to WAL on their next
open.
"""
from __future__ import annotations

from contextlib import closing, contextmanager, nullcontext
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError

FORMAT = "kfm-sql-snapshot-receipt-v1"
FLOOR_FRACTION = 0.20   # the per-file backup's own floor on the backup volume


def _hash(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _fsync(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _counts(db: sqlite3.Connection) -> dict:
    files, rows, last = db.execute("SELECT COUNT(*), COALESCE(SUM(imported_rows),0), COALESCE(MAX(file_id),0) "
                                   "FROM kfm_sql_sources WHERE state='complete'").fetchone()
    return {"source_files": files, "source_rows": rows, "last_file_id": last,
            "page_count": db.execute("PRAGMA page_count").fetchone()[0], "page_size": db.execute("PRAGMA page_size").fetchone()[0]}


def _named(dest: Path, stem: str) -> list[Path]:
    """Copies this job named (STEM-TIME-HEX12.sqlite), oldest first. Other files are never touched."""
    pattern = re.compile(rf"{re.escape(stem)}-\d{{8}}T\d{{6}}Z-[0-9a-f]{{12}}\.sqlite")
    return [p for p in sorted(dest.glob(f"{stem}-*.sqlite")) if pattern.fullmatch(p.name)]


def _kept(dest: Path, stem: str) -> list[tuple[Path, dict]]:
    """Verified copies (file and receipt both present), oldest first."""
    out = []
    for path in _named(dest, stem):
        receipt = dest / "receipts" / (path.name + ".json")
        if receipt.is_file():
            out.append((path, json.loads(receipt.read_text())))
    return out


@contextmanager
def _exclusive(dest: Path):
    """Held across a whole snapshot or check, so one run never removes or prunes another's files."""
    with open(dest / ".snapshot.lock", "a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise FeedError("SNAPSHOT_BUSY") from None
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def _clean_leftovers(dest: Path, stem: str) -> list[str]:
    """Remove what an interrupted run left: partial copies and their journals, a copy renamed into place
    whose receipt was never published, and that unpublished receipt. None of them is a kept copy."""
    names = {p.name for p, _ in _kept(dest, stem)}
    partial = re.compile(rf"{re.escape(stem)}-\d{{8}}T\d{{6}}Z\.sqlite\.partial(?:-journal)?")
    receipt = re.compile(rf"{re.escape(stem)}-\d{{8}}T\d{{6}}Z-[0-9a-f]{{12}}\.sqlite\.json\.part")
    leftovers = [*(p for p in dest.glob(f"{stem}-*.partial*") if partial.fullmatch(p.name)),
                 *(p for p in (dest / "receipts").glob(f"{stem}-*.part") if receipt.fullmatch(p.name)),
                 *(p for p in _named(dest, stem) if p.name not in names)]
    for path in leftovers:
        path.unlink()
    return sorted(p.name for p in leftovers)


def _destination(ctx, dest: Path, device_check: bool) -> Path:
    dest = dest.absolute()
    # The parent must already exist, so an unmounted backup volume fails instead of filling the system disk.
    if not dest.parent.is_dir():
        raise FeedError("SNAPSHOT_DESTINATION_MISSING")
    dest.mkdir(mode=0o700, exist_ok=True)
    (dest / "receipts").mkdir(mode=0o700, exist_ok=True)
    if device_check and os.stat(dest).st_dev == os.stat(ctx.db_path).st_dev:
        raise FeedError("SNAPSHOT_SAME_DEVICE")
    return dest


def snapshot(ctx, dest: Path, *, keep: int = 2, lock_held: bool = False, device_check: bool = True,
             floor_fraction: float = FLOOR_FRACTION) -> dict:
    """Copy, verify and keep the newest ``keep`` copies. lock_held: the caller already holds the pipeline lock."""
    if keep < 1:
        raise FeedError("SNAPSHOT_KEEP_INVALID")
    if not ctx.db_path.is_file():
        raise FeedError("DATABASE_MISSING")
    dest = _destination(ctx, dest, device_check)
    with _exclusive(dest):
        return _snapshot(ctx, dest, keep, lock_held, floor_fraction)


def _snapshot(ctx, dest: Path, keep: int, lock_held: bool, floor_fraction: float) -> dict:
    stem = ctx.db_path.stem
    removed = _clean_leftovers(dest, stem)
    wal = ctx.db_path.with_name(ctx.db_path.name + "-wal")
    needed = ctx.db_path.stat().st_size + (wal.stat().st_size if wal.exists() else 0)
    space = os.statvfs(dest)
    if space.f_bavail * space.f_frsize - needed < space.f_blocks * space.f_frsize * floor_fraction:
        raise FeedError("SNAPSHOT_SPACE_FLOOR")
    stamp = ctx.now().strftime("%Y%m%dT%H%M%SZ")
    partial = dest / f"{stem}-{stamp}.sqlite.partial"
    # runtime/backup.sh runs under run.sh's flock on the pipeline lock, so it passes lock_held.
    with nullcontext() if lock_held else core.pipeline_lock(ctx):
        with closing(sqlite3.connect(f"file:{ctx.db_path}?mode=ro", uri=True)) as source:
            before = _counts(source)
            with closing(sqlite3.connect(partial)) as copy:
                source.backup(copy)
                copy.execute("PRAGMA journal_mode=DELETE")
            if _counts(source) != before:
                partial.unlink()
                raise FeedError("SNAPSHOT_SOURCE_CHANGED")
    os.chmod(partial, 0o600)
    _fsync(partial)
    with closing(sqlite3.connect(f"file:{partial}?mode=ro", uri=True)) as copy:
        result = copy.execute("PRAGMA quick_check").fetchall()
        counts, mode = _counts(copy), copy.execute("PRAGMA journal_mode").fetchone()[0]
    if result != [("ok",)] or counts != before or mode != "delete":
        partial.unlink()
        raise FeedError("SNAPSHOT_CHECK_FAILED")
    digest, size = _hash(partial), partial.stat().st_size
    kept = _kept(dest, stem)
    mismatch = {}
    if kept and kept[-1][1]["sha256"] == digest:
        newest, recorded = kept[-1]
        # Skip the new copy only if the kept one still has the bytes its receipt records.
        if newest.stat().st_size == recorded["bytes"] and _hash(newest) == digest:
            partial.unlink()
            return {"state": "unchanged", "snapshot": newest.name, "sha256": digest, "kept": [p.name for p, _ in kept],
                    "removed_leftovers": removed}
        mismatch = {"retained_mismatch": newest.name}
    final = dest / f"{stem}-{stamp}-{digest[:12]}.sqlite"
    receipt = {"format": FORMAT, "state": "verified", "file": final.name, "sha256": digest, "bytes": size,
               "source": str(ctx.db_path), "created_at": stamp, "quick_check": "ok", **counts}
    receipt_path = dest / "receipts" / (final.name + ".json")
    if final.exists() or receipt_path.exists():
        partial.unlink()
        raise FeedError("SNAPSHOT_EXISTS")
    temp = receipt_path.with_name(receipt_path.name + ".part")
    temp.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")
    os.chmod(temp, 0o600)
    _fsync(temp)
    os.replace(partial, final)
    os.replace(temp, receipt_path)
    _fsync(dest)
    _fsync(dest / "receipts")
    kept = _kept(dest, stem)
    pruned = []
    # Only now, with the new copy verified and in place, are the older ones removed.
    for path, _ in kept[:-keep]:
        path.unlink()
        pruned.append(path.name)
    if pruned:
        _fsync(dest)
    return {"state": "verified", "snapshot": final.name, "sha256": digest, "bytes": size, **counts,
            "kept": [p.name for p, _ in kept[-keep:]], "pruned": pruned, "removed_leftovers": removed, **mismatch}


def check(ctx, dest: Path) -> dict:
    """Re-read the newest kept copy: bytes and SHA-256 against its receipt, integrity_check, row counts."""
    dest = dest.absolute()
    if not (dest / "receipts").is_dir():
        raise FeedError("SNAPSHOT_MISSING")
    with _exclusive(dest):
        return _check(ctx, dest)


def _check(ctx, dest: Path) -> dict:
    kept = _kept(dest, ctx.db_path.stem)
    if not kept:
        raise FeedError("SNAPSHOT_MISSING")
    path, receipt = kept[-1]
    if path.stat().st_size != receipt["bytes"] or _hash(path) != receipt["sha256"]:
        raise FeedError("SNAPSHOT_DIGEST_MISMATCH")
    with closing(sqlite3.connect(f"file:{path}?mode=ro", uri=True)) as copy:
        result = copy.execute("PRAGMA integrity_check").fetchall()
        counts = _counts(copy)
    if result != [("ok",)]:
        raise FeedError("SNAPSHOT_INTEGRITY_FAILED")
    if any(counts[k] != receipt[k] for k in counts):
        raise FeedError("SNAPSHOT_COUNTS_MISMATCH")
    return {"state": "verified", "snapshot": path.name, "sha256": receipt["sha256"], "bytes": receipt["bytes"],
            "created_at": receipt["created_at"], "integrity_check": "ok", "kept": [p.name for p, _ in kept]}

