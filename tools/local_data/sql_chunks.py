"""Nightly incremental copy of a large SQLite database, stored as compressed chunks, without the pipeline lock.

A full verified copy of the bulk database at its expected 112 GB takes hours and holds the pipeline lock for about 25
minutes, because it writes the whole file again and walks every b-tree with ``PRAGMA quick_check``. This module replaces
the nightly copy for that one database (``sql_snapshot.py`` still serves observations.sqlite):

1. A read transaction on the database gives one consistent commit, whatever feeds write meanwhile; in WAL mode readers and
   writers do not block each other, so no pipeline lock is taken. Its pages are read in file order through ``sqlite_dbpage``,
   which sees that snapshot, WAL frames included. Nothing is written to the database, its WAL is not checkpointed, and a
   checkpoint cannot pass this reader, so the WAL can only grow by what feeds commit during the read.
2. The bytes are cut into fixed chunks. A chunk the store lacks is compressed and written once as
   ``chunks/ab/<sha256>.z``. The WAL flags in the page 1 header are set to rollback journal, so a rebuilt file is standalone.
3. After a ``syncfs`` of the backup volume, ``manifests/<stem>-<time>-<hex12>.json`` is renamed into place. It lists the
   chunks in order with the whole file's SHA-256. Only then are manifests older than the newest ``keep`` removed, and then
   the chunks no remaining manifest uses. Each run starts by removing every chunk no manifest uses, which is how an
   interrupted run is cleaned up: any chunk still present was made durable before a manifest named it, so reuse needs no
   re-read.

A database whose file and WAL have not changed since the newest copy (size and time) is not read at all.

``check`` is the weekly restore test. It rebuilds the newest copy from its chunks in ``staging/``, re-hashes every chunk and
the whole file, runs ``PRAGMA quick_check`` (or ``integrity_check``), compares the row counts and re-hashes the chunks only
older kept copies use. It records a receipt under ``checks/``, and pruning keeps the newest copy that has one, whatever
``keep`` says, so a problem found later still has a known good copy. A chunk that fails its hash is moved to ``quarantine/``,
the check fails, and the next snapshot writes it again if the database still holds those bytes.

The nightly run does not run ``quick_check``: that walk is what takes hours on a spinning disk. Between weekly checks a copy
is known to hold exactly the bytes read, not that those bytes form a healthy database.

``restore`` rebuilds a named copy to a new file and runs ``integrity_check``. One snapshot, check or restore runs at a time
per destination (``.snapshot.lock``). This module uses only the standard library and imports nothing else from the pipeline, so
it can run from its own release.
"""
from __future__ import annotations

import argparse
import ctypes
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing, contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import sys
import time
import zlib

FORMAT = "kfm-sql-chunk-manifest-v1"
CHECK_FORMAT = "kfm-sql-chunk-check-v1"
CHUNK = 4 << 20       # at 112 GB, 28,000 files instead of 112,000 to seek to on a spinning disk, for 1% more bytes (measured)
LEVEL = 1             # zlib; measured on this database's pages: 149 MB/s and 5.6:1, against 111 MB/s and 5.5:1 at level 3
WORKERS = 3           # threads hashing and compressing; both release the GIL on buffers this large
QUEUED = 8            # chunks in flight, so memory stays near QUEUED * CHUNK
LEVELS = ("quick", "integrity")
_NAME = re.compile(r"[A-Za-z0-9._-]+-\d{8}T\d{6}Z-[0-9a-f]{12}\.json")


class ChunkError(Exception):
    """A fixed reason the run stopped. Kept copies are untouched."""


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _fsync(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _syncfs(path: Path) -> None:
    """Flush everything on the backup volume once, instead of paying a journal commit per chunk on a spinning disk."""
    fd = os.open(path, os.O_RDONLY)
    try:
        libc = ctypes.CDLL(None, use_errno=True)
        if libc.syncfs(fd) != 0:
            raise OSError(ctypes.get_errno(), "syncfs")
    finally:
        os.close(fd)


def _write_json(path: Path, value: dict) -> None:
    temp = path.with_name(path.name + ".part")
    with open(temp, "w") as out:
        out.write(json.dumps(value, sort_keys=True) + "\n")
        out.flush()
        os.fsync(out.fileno())
    os.chmod(temp, 0o600)
    os.replace(temp, path)
    _fsync(path.parent)


def _chunk(dest: Path, digest: str) -> Path:
    return dest / "chunks" / digest[:2] / f"{digest}.z"


def _manifests(dest: Path, stem: str | None = None) -> list[tuple[Path, dict]]:
    """Every manifest of one database (or of all), oldest first. One that cannot be read stops the run: its chunks must not be
    mistaken for garbage."""
    out = []
    for path in sorted((dest / "manifests").glob("*.json")):
        if not _NAME.fullmatch(path.name) or (stem is not None and not path.name.startswith(stem + "-")):
            continue
        try:
            manifest = json.loads(path.read_text())
            if manifest["format"] != FORMAT or not isinstance(manifest["chunks"], list):
                raise ValueError
        except (OSError, ValueError, KeyError) as error:
            raise ChunkError(f"SNAPSHOT_MANIFEST_UNREADABLE {path.name}") from error
        out.append((path, manifest))
    return out


def _present(dest: Path) -> set[str]:
    return {p.name[:-2] for p in (dest / "chunks").glob("*/*.z")}


def _sweep(dest: Path) -> dict:
    """Remove what no manifest names: an interrupted run's chunks and part files, and chunks a crash left unpruned."""
    parts = [*(dest / "chunks").glob("*/*.part"), *(dest / "manifests").glob("*.part"), *(dest / "checks").glob("*.part")]
    for path in parts:
        path.unlink()
    used = {d for _, m in _manifests(dest) for d in m["chunks"]}
    present = _present(dest)
    extra = present - used
    for digest in extra:
        _chunk(dest, digest).unlink()
    return {"part_files": len(parts), "chunks": len(extra), "present": present & used}


@contextmanager
def _exclusive(dest: Path):
    """Held across a whole snapshot, check or restore, so one run never removes another's files."""
    with open(dest / ".snapshot.lock", "a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ChunkError("SNAPSHOT_BUSY") from None
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def _destination(db_path: Path | None, dest: Path, device_check: bool) -> Path:
    dest = dest.absolute()
    # The parent must already exist, so an unmounted backup volume fails instead of filling the system disk.
    if not dest.parent.is_dir():
        raise ChunkError("SNAPSHOT_DESTINATION_MISSING")
    for folder in (dest, dest / "chunks", dest / "manifests", dest / "checks"):
        folder.mkdir(mode=0o700, exist_ok=True)
    if device_check and db_path is not None and os.stat(dest).st_dev == os.stat(db_path).st_dev:
        raise ChunkError("SNAPSHOT_SAME_DEVICE")
    return dest


def _fingerprint(db_path: Path) -> dict:
    """What changes whenever a commit reaches the file or its WAL. An empty or missing WAL counts the same, because readers
    create and remove it."""
    db = db_path.stat()
    wal = db_path.with_name(db_path.name + "-wal")
    log = wal.stat() if wal.exists() else None
    return {"bytes": db.st_size, "mtime_ns": db.st_mtime_ns, "wal_bytes": log.st_size if log else 0,
            "wal_mtime_ns": log.st_mtime_ns if log and log.st_size else 0}


def _has_dbpage(db: sqlite3.Connection) -> bool:
    try:
        db.execute("SELECT 1 FROM sqlite_dbpage LIMIT 0").fetchall()
        return True
    except sqlite3.Error:
        return False


def _counts(db: sqlite3.Connection) -> dict:
    """The same counts as sql_snapshot, where the database has that table."""
    out = {"page_count": db.execute("PRAGMA page_count").fetchone()[0], "page_size": db.execute("PRAGMA page_size").fetchone()[0]}
    if db.execute("SELECT 1 FROM sqlite_master WHERE name='kfm_sql_sources'").fetchone():
        files, rows, last = db.execute("SELECT COUNT(*), COALESCE(SUM(imported_rows),0), COALESCE(MAX(file_id),0) "
                                       "FROM kfm_sql_sources WHERE state='complete'").fetchone()
        out.update(source_files=files, source_rows=rows, last_file_id=last)
    return out


def _standalone(first: bytes) -> bytes:
    """Page 1 with the file format bytes set to rollback journal. WAL mode is recorded only there, and the rest of the file
    is the same in both modes."""
    return first if first[18:20] == b"\x01\x01" else first[:18] + b"\x01\x01" + first[20:]


def _read_pages(db: sqlite3.Connection, page_size: int):
    """The open transaction's pages in file order, as chunks."""
    per_chunk = CHUNK // page_size
    cursor = db.execute("SELECT data FROM sqlite_dbpage")
    first = True
    while True:
        rows = cursor.fetchmany(per_chunk)
        if not rows:
            return
        data = b"".join(row[0] for row in rows)
        yield _standalone(data) if first else data
        first = False


def _read_file(db_path: Path, page_size: int, page_count: int):
    """For a build of SQLite without sqlite_dbpage: only sound when no WAL frame holds newer pages (see _chunks)."""
    left, first = page_size * page_count, True
    with open(db_path, "rb") as handle:
        while left > 0:
            data = handle.read(min(CHUNK, left))
            if not data:
                raise ChunkError("SNAPSHOT_SOURCE_SHORT")
            left -= len(data)
            yield _standalone(data) if first else data
            first = False


def _chunks(db: sqlite3.Connection, db_path: Path, counts: dict):
    if _has_dbpage(db):
        return _read_pages(db, counts["page_size"])
    wal = db_path.with_name(db_path.name + "-wal")
    if db.execute("PRAGMA journal_mode").fetchone()[0] == "wal" and wal.exists() and wal.stat().st_size:
        raise ChunkError("SNAPSHOT_NEEDS_DBPAGE")
    return _read_file(db_path, counts["page_size"], counts["page_count"])


def _write_chunk(dest: Path, digest: str, body: bytes) -> None:
    """Not flushed here: _syncfs does that for the whole run, before a manifest names this chunk."""
    path = _chunk(dest, digest)
    path.parent.mkdir(mode=0o700, exist_ok=True)
    part = path.with_name(path.name + ".part")
    with open(part, "xb") as out:
        os.fchmod(out.fileno(), 0o600)
        out.write(body)
    os.replace(part, path)


def _store(source, dest: Path, present: set[str]) -> dict:
    """Hash every chunk of source; compress and write those the store lacks. Stored chunks are not read."""
    whole, order, new, new_raw, new_body = hashlib.sha256(), [], 0, 0, 0
    have = set(present)

    def work(data: bytes):
        digest = hashlib.sha256(data).hexdigest()
        return digest, len(data), None if digest in have else zlib.compress(data, LEVEL)

    def finish(future) -> None:
        nonlocal new, new_raw, new_body
        digest, size, body = future.result()
        order.append(digest)
        if body is None or digest in have:
            return
        _write_chunk(dest, digest, body)
        have.add(digest)
        new, new_raw, new_body = new + 1, new_raw + size, new_body + len(body)

    bytes_read, pending = 0, deque()
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for data in source:
            whole.update(data)
            bytes_read += len(data)
            pending.append(pool.submit(work, data))
            while len(pending) >= QUEUED or (pending and pending[0].done()):
                finish(pending.popleft())
        while pending:
            finish(pending.popleft())
    return {"sha256": whole.hexdigest(), "bytes": bytes_read, "chunks": order, "new": new, "new_raw": new_raw, "new_body": new_body}


def _verified(dest: Path, manifests: list[tuple[Path, dict]]) -> Path | None:
    """The newest manifest with a check receipt."""
    for path, _ in reversed(manifests):
        if (dest / "checks" / path.name).is_file():
            return path
    return None


def _prune(dest: Path, stem: str, keep: int) -> list[str]:
    """Remove manifests past the newest ``keep`` (never the newest checked one), then the chunks nothing uses any more."""
    manifests = _manifests(dest, stem)
    protected = {p for p, _ in manifests[-keep:]} | {_verified(dest, manifests)}
    pruned = []
    for path, _ in manifests:
        if path not in protected:
            path.unlink()
            (dest / "checks" / path.name).unlink(missing_ok=True)
            pruned.append(path.name)
    if pruned:
        _fsync(dest / "manifests")
        used = {d for _, m in _manifests(dest) for d in m["chunks"]}
        for digest in _present(dest) - used:
            _chunk(dest, digest).unlink()
    return pruned


def snapshot(db_path: Path, dest: Path, *, keep: int = 2, device_check: bool = True, now=_now) -> dict:
    """Store a consistent copy of db_path as chunks, keeping the newest ``keep`` copies."""
    if keep < 1:
        raise ChunkError("SNAPSHOT_KEEP_INVALID")
    db_path = db_path.absolute()
    if not db_path.is_file():
        raise ChunkError("DATABASE_MISSING")
    dest = _destination(db_path, dest, device_check)
    with _exclusive(dest):
        return _snapshot(db_path, dest, keep, now)


def _snapshot(db_path: Path, dest: Path, keep: int, now) -> dict:
    started = time.monotonic()
    stem = db_path.stem
    swept = _sweep(dest)
    present, removed = swept.pop("present"), swept
    manifests = _manifests(dest, stem)
    newest = manifests[-1] if manifests else None
    seen = _fingerprint(db_path)
    if newest and newest[1].get("source_fingerprint") == seen and set(newest[1]["chunks"]) <= present:
        return {"state": "unchanged", "mode": "untouched", "database": stem, "snapshot": newest[0].name, "sha256": newest[1]["sha256"],
                "kept": [p.name for p, _ in manifests], "removed_leftovers": removed, "seconds": round(time.monotonic() - started, 1)}
    with closing(sqlite3.connect(db_path.as_uri() + "?mode=ro", uri=True, isolation_level=None, timeout=60)) as source:
        source.execute("PRAGMA query_only=ON")
        source.execute("BEGIN")
        counts = _counts(source)   # the first read fixes the snapshot this transaction sees
        mode = source.execute("PRAGMA journal_mode").fetchone()[0]
        stored = _store(_chunks(source, db_path, counts), dest, present)
        source.execute("COMMIT")
    if stored["bytes"] != counts["page_size"] * counts["page_count"]:
        raise ChunkError("SNAPSHOT_SOURCE_SHORT")
    previous = newest[1]["chunks"] if newest else []
    changed = sum(1 for a, b in zip(previous, stored["chunks"]) if a != b)
    report = {"database": stem, "sha256": stored["sha256"], "bytes": stored["bytes"], "chunks": len(stored["chunks"]),
              "chunk_bytes": CHUNK, "new_chunks": stored["new"], "new_raw_bytes": stored["new_raw"], "new_chunk_bytes": stored["new_body"],
              "changed_chunks": changed, "grown_chunks": max(0, len(stored["chunks"]) - len(previous)),
              "source_mode": mode, **counts}
    if newest and newest[1]["sha256"] == stored["sha256"]:
        _syncfs(dest)
        if newest[1].get("source_fingerprint") != seen:   # same bytes, newer file times: let the next run skip the read
            _write_json(newest[0], {**newest[1], "source_fingerprint": seen})
        return {**report, "state": "unchanged", "mode": "read", "snapshot": newest[0].name, "kept": [p.name for p, _ in manifests],
                "removed_leftovers": removed, "seconds": round(time.monotonic() - started, 1)}
    stamp = now().strftime("%Y%m%dT%H%M%SZ")
    if newest and stamp <= newest[1]["created_at"]:   # names sort by time, and pruning must never take the newest for the oldest
        raise ChunkError("SNAPSHOT_CLOCK_BEHIND")
    final = dest / "manifests" / f"{stem}-{stamp}-{stored['sha256'][:12]}.json"
    _syncfs(dest)   # every chunk this manifest names is on the disk before the manifest exists
    _write_json(final, {"format": FORMAT, "state": "hashed", "source": str(db_path), "created_at": stamp, "zlib_level": LEVEL,
                        "source_fingerprint": seen, **report, "chunks": stored["chunks"]})
    pruned = _prune(dest, stem, keep)
    return {**report, "state": "stored", "snapshot": final.name, "kept": [p.name for p, _ in _manifests(dest, stem)], "pruned": pruned,
            "removed_leftovers": removed, "seconds": round(time.monotonic() - started, 1)}


def _read_chunk(dest: Path, digest: str) -> bytes | None:
    """The chunk's bytes, or None when it is missing or no longer has its SHA-256."""
    try:
        data = zlib.decompress(_chunk(dest, digest).read_bytes())
    except (OSError, zlib.error):
        return None
    return data if hashlib.sha256(data).hexdigest() == digest else None


def _quarantine(dest: Path, digest: str) -> None:
    """Move a damaged chunk aside, so the next snapshot sees it missing and writes it again."""
    path = _chunk(dest, digest)
    if path.exists():
        folder = dest / "quarantine"
        folder.mkdir(mode=0o700, exist_ok=True)
        os.replace(path, folder / path.name)


def _rebuild(dest: Path, manifest: dict, target: Path) -> list[str]:
    """Write the copy to target and return the damaged chunks. With any damage the file is useless, and the scan continues only
    to name them all."""
    whole, damaged = hashlib.sha256(), []
    with open(target, "xb") as out:
        os.fchmod(out.fileno(), 0o600)
        for digest in manifest["chunks"]:
            data = _read_chunk(dest, digest)
            if data is None:
                damaged.append(digest)
                continue
            if not damaged:
                whole.update(data)
                out.write(data)
        out.flush()
        os.fsync(out.fileno())
    if not damaged and (target.stat().st_size != manifest["bytes"] or whole.hexdigest() != manifest["sha256"]):
        raise ChunkError("SNAPSHOT_DIGEST_MISMATCH")
    return damaged


def _verify(path: Path, manifest: dict, level: str) -> None:
    with closing(sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)) as copy:
        result = copy.execute(f"PRAGMA {level}_check").fetchall()
        counts, mode = _counts(copy), copy.execute("PRAGMA journal_mode").fetchone()[0]
    if result != [("ok",)]:
        raise ChunkError("SNAPSHOT_INTEGRITY_FAILED")
    if mode != "delete" or any(counts[k] != manifest[k] for k in counts):
        raise ChunkError("SNAPSHOT_COUNTS_MISMATCH")


def check(dest: Path, *, stem: str | None = None, level: str = "quick", now=_now) -> dict:
    """The restore test: rebuild and verify the newest copy, then re-hash the chunks only older kept copies use."""
    if level not in LEVELS:
        raise ChunkError("CHECK_LEVEL_INVALID")
    dest = dest.absolute()
    if not (dest / "manifests").is_dir():
        raise ChunkError("SNAPSHOT_MISSING")
    with _exclusive(dest):
        manifests = _manifests(dest, stem)
        if not manifests:
            raise ChunkError("SNAPSHOT_MISSING")
        path, manifest = manifests[-1]
        stage = dest / "staging"
        stage.mkdir(mode=0o700, exist_ok=True)
        for stale in stage.glob("*"):   # left by a killed run; .snapshot.lock is held, so none is in use
            stale.unlink()
        started = time.monotonic()
        target = stage / f"{os.getpid()}-check.sqlite"
        try:
            damaged = _rebuild(dest, manifest, target)
            if not damaged:
                _verify(target, manifest, level)
        finally:
            target.unlink(missing_ok=True)
        older = {d for _, m in manifests[:-1] for d in m["chunks"]} - set(manifest["chunks"])
        damaged += sorted(d for d in older if _read_chunk(dest, d) is None)
        for digest in set(damaged):
            _quarantine(dest, digest)
        if damaged:
            raise ChunkError(f"SNAPSHOT_CHUNK_DAMAGED {len(set(damaged))} first {damaged[0]}")
        receipt = {"format": CHECK_FORMAT, "snapshot": path.name, "sha256": manifest["sha256"], "bytes": manifest["bytes"], "level": level,
                   "result": "ok", "checked_at": now().strftime("%Y%m%dT%H%M%SZ"), "seconds": round(time.monotonic() - started, 1),
                   "older_chunks_rehashed": len(older)}
        _write_json(dest / "checks" / path.name, receipt)
        return {"state": "verified", **receipt, "kept": [p.name for p, _ in manifests]}


def restore(dest: Path, name: str, target: Path, *, level: str = "integrity") -> dict:
    """Rebuild the copy ``name`` (a manifest file name) to target, a new file, and check it before giving it that name."""
    if level not in LEVELS:
        raise ChunkError("CHECK_LEVEL_INVALID")
    dest, target = dest.absolute(), target.absolute()
    path = dest / "manifests" / name
    if not _NAME.fullmatch(name) or not path.is_file():
        raise ChunkError("SNAPSHOT_MISSING")
    if target.exists():
        raise ChunkError("RESTORE_TARGET_EXISTS")
    partial = target.with_name(target.name + ".partial")
    with _exclusive(dest):
        manifest = next(m for p, m in _manifests(dest) if p == path)
        started = time.monotonic()
        partial.unlink(missing_ok=True)   # left by a killed restore; .snapshot.lock is held, so none is in progress
        try:
            damaged = _rebuild(dest, manifest, partial)
            if damaged:
                raise ChunkError(f"SNAPSHOT_CHUNK_DAMAGED {len(set(damaged))} first {damaged[0]}")
            _verify(partial, manifest, level)
            os.replace(partial, target)
        finally:
            partial.unlink(missing_ok=True)
    return {"state": "restored", "snapshot": name, "to": str(target), "sha256": manifest["sha256"], "bytes": manifest["bytes"],
            "level": level, "seconds": round(time.monotonic() - started, 1)}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    snap = sub.add_parser("snapshot", help="Store the database's changed chunks, keeping the newest --keep copies")
    snap.add_argument("--db", type=Path, required=True)
    snap.add_argument("--dest", type=Path, required=True)
    snap.add_argument("--keep", type=int, default=2)
    snap.add_argument("--allow-same-device", action="store_true", help="For tests: the copy would die with the disk")
    test = sub.add_parser("check", help="Rebuild and verify the newest copy, the weekly restore test")
    test.add_argument("--dest", type=Path, required=True)
    test.add_argument("--stem", help="Only this database's copies")
    test.add_argument("--level", choices=LEVELS, default="quick")
    back = sub.add_parser("restore", help="Rebuild a kept copy (a manifest name) to a new file")
    back.add_argument("--dest", type=Path, required=True)
    back.add_argument("--manifest", required=True)
    back.add_argument("--to", type=Path, required=True)
    back.add_argument("--level", choices=LEVELS, default="integrity")
    args = parser.parse_args(argv)
    os.umask(0o077)
    try:
        if args.command == "snapshot":
            result = snapshot(args.db, args.dest, keep=args.keep, device_check=not args.allow_same_device)
        elif args.command == "check":
            result = check(args.dest, stem=args.stem, level=args.level)
        else:
            result = restore(args.dest, args.manifest, args.to, level=args.level)
    except (ChunkError, OSError, sqlite3.Error) as error:
        print(json.dumps({"state": "failed", "command": args.command, "reason": str(error)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
