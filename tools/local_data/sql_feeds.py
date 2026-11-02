"""Keep the pipeline PC's local SQL database growing from new public source data.

Each feed fetches only what is new for its source, keeps a Kansas-only raw copy with a receipt
(the original download's URL, size and SHA-256 included), and loads rows additively into
``observations.sqlite``: one transaction per source file, keyed by SHA-256 in ``kfm_sql_sources``,
so a rerun skips what is already loaded and an interrupted load leaves nothing behind. Downloads
run outside the pipeline lock; only database writes take it. The 85 GB aggregate ceiling and the
100 GB free-space floor of the original SQL build still apply.

    python -m tools.local_data.sql_feeds --root STORE --db observations.sqlite \
        [--tiger kansas-tiger-2025.gpkg] [--nwm-gpkg kansas-nwm.gpkg] [--lock pipeline.lock] \
        run FEED | status | snapshot --dest DIR [--keep 2] [--lock-held] | snapshot-check --dest DIR

Feeds: captures, iem-wind, ghcnd, storm-events, asos-5min, prism, nwm. ``snapshot`` and
``snapshot-check`` back up the database itself (``sql_snapshot.py``).
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
import fcntl
import gzip
import hashlib
import importlib
import json
import os
from pathlib import Path
import sqlite3
import sys
import time
from typing import Callable
import urllib.error
import urllib.request

CAP = 85_000_000_000
RESERVE = 5_000_000_000
FREE_FLOOR = 100_000_000_000
USER_AGENT = "KFM-pipeline-sql-feeds/1 (Kansas Frontier Matrix local research database)"
FEEDS = {
    "captures": "tools.local_data.sql_feed_sources:captures",
    "iem-wind": "tools.local_data.sql_feed_sources:iem_wind",
    "ghcnd": "tools.local_data.sql_feed_sources:ghcnd",
    "storm-events": "tools.local_data.sql_feed_sources:storm_events",
    "asos-5min": "tools.local_data.sql_feed_sources:asos_fivemin",
    "prism": "tools.local_data.sql_feed_prism:prism",
    "nwm": "tools.local_data.sql_feed_nwm:nwm",
}
SCHEMA = """
CREATE TABLE IF NOT EXISTS kfm_feed_state (
  feed TEXT PRIMARY KEY, state_json TEXT NOT NULL, updated_at TEXT NOT NULL) WITHOUT ROWID;
"""


class FeedError(RuntimeError):
    """A fixed, loggable reason a feed stopped."""


@dataclass
class Fetched:
    url: str
    body: bytes
    last_modified: str | None = None
    etag: str | None = None


def http_fetch(url: str, *, limit: int, timeout: int = 120, missing_ok: bool = False, attempts: int = 3) -> Fetched | None:
    """GET url with a byte ceiling. A 404 is None when missing_ok; other failures retry, then raise."""
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                body = response.read(limit + 1)
                if len(body) > limit:
                    raise FeedError(f"RESPONSE_TOO_LARGE {url}")
                return Fetched(url, body, response.headers.get("Last-Modified"), response.headers.get("ETag"))
        except urllib.error.HTTPError as error:
            if error.code == 404 and missing_ok:
                return None
            if error.code < 500 or attempt == attempts - 1:
                raise FeedError(f"HTTP_{error.code} {url}") from None
        except (urllib.error.URLError, TimeoutError, ConnectionError) as error:
            if attempt == attempts - 1:
                raise FeedError(f"FETCH_FAILED {url}: {error}") from None
        time.sleep(5 * 4 ** attempt)
    raise FeedError(f"FETCH_FAILED {url}")


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


@dataclass
class Context:
    root: Path
    db_path: Path
    tiger: Path | None = None
    nwm_gpkg: Path | None = None
    lock: Path | None = None
    fetch: Callable[..., Fetched | None] = http_fetch
    now: Callable[[], datetime] = utc_now
    log: Callable[[dict], None] = lambda line: print(json.dumps(line, sort_keys=True), flush=True)
    catalogs: list[Path] = field(default_factory=list)
    floor: int = FREE_FLOOR
    lock_depth: int = 0

    def note(self, event: str, **fields) -> None:
        self.log({"at": self.now().strftime("%Y-%m-%dT%H:%M:%SZ"), "event": event, **fields})


def store_raw(ctx: Context, feed: str, name: str, body: bytes, *, url: str, fetched: Fetched | None = None,
              original: bytes | None = None, extra: dict | None = None) -> tuple[Path, str]:
    """Write one immutable raw object and its receipt under data/raw/sql-feeds/<feed>/.

    body is what is kept (for curated sources, the Kansas-only subset); original, when given,
    is the full download, recorded only by size and SHA-256.
    """
    if "/" in feed or ".." in Path(name).parts or name.startswith("/"):
        raise FeedError("RAW_NAME_UNSAFE")
    path = ctx.root / "data/raw/sql-feeds" / feed / name
    receipt_path = ctx.root / "data/receipts/ingest/sql-feeds" / feed / (name + ".json")
    digest = sha256(body)
    if path.exists():
        if sha256(path.read_bytes()) != digest:
            raise FeedError(f"RAW_OBJECT_CHANGED {name}")
        return path, digest
    receipt = {"format": "kfm-sql-feed-receipt-v1", "feed": feed, "path": str(path.relative_to(ctx.root)), "sha256": digest,
               "bytes": len(body), "source_url": url, "retrieved_at": ctx.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
               "last_modified": fetched.last_modified if fetched else None, "etag": fetched.etag if fetched else None,
               **({"original": {"sha256": sha256(original), "bytes": len(original), "kept": False}} if original is not None else {}),
               **(extra or {})}
    for target, data in ((path, body), (receipt_path, (json.dumps(receipt, indent=1, sort_keys=True) + "\n").encode())):
        target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        temp = target.with_name(target.name + ".part")
        with open(temp, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temp, 0o600)
        os.replace(temp, target)
    return path, digest


def receipt_for(ctx: Context, path: Path) -> dict:
    relative = path.relative_to(ctx.root / "data/raw/sql-feeds")
    return json.loads((ctx.root / "data/receipts/ingest/sql-feeds" / (str(relative) + ".json")).read_text())


def gz(data: bytes) -> bytes:
    return gzip.compress(data, mtime=0)


def guard(ctx: Context) -> None:
    out = ctx.db_path.parent
    used = sum(p.stat().st_size for p in out.glob("*") if p.is_file()) + sum(p.stat().st_size for p in ctx.catalogs if p.exists())
    if used >= CAP - RESERVE:
        raise FeedError("CEILING_85GB_HEADROOM_STOP")
    stat = os.statvfs(out)
    if stat.f_bavail * stat.f_frsize < ctx.floor:
        raise FeedError("FREE_SPACE_FLOOR_REACHED")


def open_db(ctx: Context) -> sqlite3.Connection:
    if not ctx.db_path.is_file():
        raise FeedError("DATABASE_MISSING")
    db = sqlite3.connect(ctx.db_path, timeout=120, isolation_level=None)
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA synchronous=NORMAL")
    db.execute("PRAGMA busy_timeout=120000")
    if not db.execute("SELECT 1 FROM sqlite_master WHERE name='kfm_sql_sources'").fetchone():
        db.close()
        raise FeedError("BASE_BUILD_MISSING")
    with pipeline_lock(ctx):
        db.executescript(SCHEMA)
    return db


def get_state(db: sqlite3.Connection, feed: str) -> dict:
    row = db.execute("SELECT state_json FROM kfm_feed_state WHERE feed=?", (feed,)).fetchone()
    return json.loads(row[0]) if row else {}


def set_state(db: sqlite3.Connection, ctx: Context, feed: str, value: dict) -> None:
    db.execute("INSERT OR REPLACE INTO kfm_feed_state VALUES (?,?,?)",
               (feed, canonical(value), ctx.now().strftime("%Y-%m-%dT%H:%M:%SZ")))


def loaded(db: sqlite3.Connection, digest: str) -> bool:
    row = db.execute("SELECT state FROM kfm_sql_sources WHERE sha256=?", (digest,)).fetchone()
    if row and row[0] not in ("complete", "imported", "superseded"):
        raise FeedError("INCOMPLETE_SOURCE_RECORD")
    return row is not None


def begin_source(db: sqlite3.Connection, ctx: Context, source_id: str, path: Path, digest: str, url: str, receipt: dict) -> int | None:
    """Open the one transaction for a source file. None if this exact file is already loaded."""
    if loaded(db, digest):
        return None
    guard(ctx)
    db.execute("BEGIN IMMEDIATE")
    return db.execute("INSERT INTO kfm_sql_sources(source_id,source_path,sha256,source_bytes,source_url,receipt_json,state) VALUES (?,?,?,?,?,?,?)",
                      (source_id, str(path), digest, path.stat().st_size, url, canonical(receipt), "loading")).lastrowid


def finish_source(db: sqlite3.Connection, file_id: int, rows: int) -> None:
    db.execute("UPDATE kfm_sql_sources SET imported_rows=?, state='complete' WHERE file_id=?", (rows, file_id))
    db.execute("COMMIT")


@contextmanager
def pipeline_lock(ctx: Context, wait_seconds: int = 900):
    """The PC pipeline's exclusive lock (captures, analysis, backups). No-op when not configured.

    Re-entrant within one run: flock is held per open file, so a nested take would wait on itself.
    """
    if ctx.lock is None or ctx.lock_depth:
        ctx.lock_depth += 1
        try:
            yield
        finally:
            ctx.lock_depth -= 1
        return
    with open(ctx.lock, "a") as handle:
        deadline = time.monotonic() + wait_seconds
        while True:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() > deadline:
                    raise FeedError("PIPELINE_LOCK_BUSY") from None
                time.sleep(5)
        ctx.lock_depth = 1
        try:
            yield
        finally:
            ctx.lock_depth = 0
            fcntl.flock(handle, fcntl.LOCK_UN)


def resolve(feed: str):
    if feed not in FEEDS:
        raise FeedError(f"FEED_UNKNOWN {feed}")
    module, name = FEEDS[feed].split(":")
    return getattr(importlib.import_module(module), name)


def status(ctx: Context) -> dict:
    db = sqlite3.connect(f"file:{ctx.db_path}?mode=ro", uri=True)
    try:
        states = {feed: json.loads(body) | {"updated_at": at} for feed, body, at in
                  db.execute("SELECT feed,state_json,updated_at FROM kfm_feed_state")} \
            if db.execute("SELECT 1 FROM sqlite_master WHERE name='kfm_feed_state'").fetchone() else {}
        rows = db.execute("SELECT COALESCE(SUM(imported_rows),0), COUNT(*) FROM kfm_sql_sources WHERE state='complete'").fetchone()
    finally:
        db.close()
    return {"feeds": states, "source_rows": rows[0], "source_files": rows[1], "database_bytes": ctx.db_path.stat().st_size}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--db", type=Path, required=True)
    parser.add_argument("--tiger", type=Path)
    parser.add_argument("--nwm-gpkg", type=Path)
    parser.add_argument("--lock", type=Path)
    parser.add_argument("--catalog", type=Path, action="append", default=[], help="Other databases counted against the 85 GB ceiling")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("feed", choices=sorted(FEEDS))
    sub.add_parser("status")
    snap = sub.add_parser("snapshot", help="Verified copy of the database on the backup volume, keeping the newest --keep")
    snap.add_argument("--dest", type=Path, required=True)
    snap.add_argument("--keep", type=int, default=2)
    snap.add_argument("--lock-held", action="store_true", help="The caller already holds --lock (runtime/backup.sh)")
    check = sub.add_parser("snapshot-check", help="Re-read the newest copy for the monthly restore test")
    check.add_argument("--dest", type=Path, required=True)
    args = parser.parse_args(argv)
    os.umask(0o077)
    ctx = Context(root=args.root, db_path=args.db, tiger=args.tiger, nwm_gpkg=args.nwm_gpkg, lock=args.lock, catalogs=args.catalog)
    if args.command == "status":
        print(json.dumps(status(ctx), indent=1, sort_keys=True))
        return 0
    if args.command in ("snapshot", "snapshot-check"):
        from tools.local_data import sql_snapshot

        try:
            result = (sql_snapshot.snapshot(ctx, args.dest, keep=args.keep, lock_held=args.lock_held)
                      if args.command == "snapshot" else sql_snapshot.check(ctx, args.dest))
        except FeedError as error:
            ctx.note("snapshot_failed", command=args.command, reason=str(error))
            return 1
        print(json.dumps(result, sort_keys=True))
        return 0
    started = time.monotonic()
    try:
        summary = resolve(args.feed)(ctx)
    except FeedError as error:
        ctx.note("feed_failed", feed=args.feed, reason=str(error), seconds=round(time.monotonic() - started))
        return 1
    ctx.note("feed_done", feed=args.feed, seconds=round(time.monotonic() - started), **(summary or {}))
    return 0


if __name__ == "__main__":
    # Run the importable module, not this __main__ copy, so FeedError raised by a feed is the class caught here.
    from tools.local_data import sql_feeds

    sys.exit(sql_feeds.main())
