"""Keep the pipeline PC's local SQL database growing from new public source data.

Each feed fetches only what is new for its source, keeps a Kansas-only raw copy with a receipt
(the original download's URL, size and SHA-256 included), and loads rows additively into
``observations.sqlite``: one transaction per source file, keyed by SHA-256 in ``kfm_sql_sources``,
so a rerun skips what is already loaded and an interrupted load leaves nothing behind. Downloads
run outside the pipeline lock; only database writes take it. The 85 GB aggregate ceiling and the
100 GB free-space floor of the original SQL build still apply.

    python -m tools.local_data.sql_feeds --root STORE --db observations.sqlite \
        [--tiger kansas-tiger-2025.gpkg] [--nwm-gpkg kansas-nwm.gpkg] [--lock pipeline.lock] \
        [--bulk-db kfm-bulk.sqlite] run FEED | status | snapshot --dest DIR [--keep 2] [--lock-held] \
        | snapshot-check --dest DIR

Feeds: captures, iem-wind, ghcnd, storm-events, asos-5min, prism, nwm; and, from 2026-11-02,
usgs-daily, usgs-peaks, usgs-groundwater, water-quality, climdiv, drought, air-quality, nass,
kgs-oil-gas, fema, earthquakes, tornadoes, nws-warnings, cdc-places, census-acs, census-decennial,
eia-seds. ``BULK_FEEDS`` load a second database, ``--bulk-db``, kept outside the per-file
backup; both count against the ceiling. ``snapshot`` and ``snapshot-check`` back up the
database itself (``sql_snapshot.py``).
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
import fcntl
import gzip
import hashlib
import http.client
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

CAP = None   # the owner, 2026-11-02: "ignore all data caps and floors". Set a byte count to bring the ceiling back.
RESERVE = 5_000_000_000
FREE_FLOOR = 0
USER_AGENT = "KFM-pipeline-sql-feeds/1 (Kansas Frontier Matrix local research database)"
FEEDS = {
    "captures": "tools.local_data.sql_feed_sources:captures",
    "iem-wind": "tools.local_data.sql_feed_sources:iem_wind",
    "ghcnd": "tools.local_data.sql_feed_sources:ghcnd",
    "storm-events": "tools.local_data.sql_feed_sources:storm_events",
    "asos-5min": "tools.local_data.sql_feed_sources:asos_fivemin",
    "prism": "tools.local_data.sql_feed_prism:prism",
    "nwm": "tools.local_data.sql_feed_nwm:nwm",
    # Kansas sources the owner added on 2026-11-02, for the local database only.
    "usgs-daily": "tools.local_data.sql_feed_water:usgs_daily",
    "usgs-peaks": "tools.local_data.sql_feed_water:usgs_peaks",
    "usgs-groundwater": "tools.local_data.sql_feed_water:usgs_groundwater",
    "water-quality": "tools.local_data.sql_feed_water:water_quality",
    "climdiv": "tools.local_data.sql_feed_climate:climdiv",
    "drought": "tools.local_data.sql_feed_climate:drought",
    "air-quality": "tools.local_data.sql_feed_air:air_quality",
    "nass": "tools.local_data.sql_feed_nass:nass",
    "kgs-oil-gas": "tools.local_data.sql_feed_kgs:kgs_oil_gas",
    "fema": "tools.local_data.sql_feed_fema:fema",
    "earthquakes": "tools.local_data.sql_feed_hazards:earthquakes",
    "tornadoes": "tools.local_data.sql_feed_hazards:tornadoes",
    "nws-warnings": "tools.local_data.sql_feed_hazards:nws_warnings",
    "cdc-places": "tools.local_data.sql_feed_hazards:cdc_places",
    "census-acs": "tools.local_data.sql_feed_census:census_acs",
    "census-decennial": "tools.local_data.sql_feed_census:census_decennial",
    "eia-seds": "tools.local_data.sql_feed_census:eia_seds",
    # Recovered feeds: preserve the tables and receipt identities from the existing store.
    "airports": "tools.local_data.sql_feed_structures:airports",
    "obstacles": "tools.local_data.sql_feed_structures:obstacles",
    "dams": "tools.local_data.sql_feed_structures:dams",
    "mines": "tools.local_data.sql_feed_structures:mines",
    "grade-crossings": "tools.local_data.sql_feed_structures:grade_crossings",
    "rail-lines": "tools.local_data.sql_feed_structures:rail_lines",
    "gnis-names": "tools.local_data.sql_feed_places:gnis_names",
    "post-offices": "tools.local_data.sql_feed_places:post_offices",
    "county-boundaries": "tools.local_data.sql_feed_places:county_boundaries",
    "ceded-lands": "tools.local_data.sql_feed_places:ceded_lands",
    "railroads-history": "tools.local_data.sql_feed_places:railroads_history",
    "congress-kansas": "tools.local_data.sql_feed_places:congress_kansas",
    "nps-places": "tools.local_data.sql_feed_places:nps_places",
    "nrhp": "tools.local_data.sql_feed_places:nrhp",
    "pbdb": "tools.local_data.sql_feed_deeptime:pbdb",
    "macrostrat": "tools.local_data.sql_feed_deeptime:macrostrat",
    "radiocarbon": "tools.local_data.sql_feed_deeptime:radiocarbon",
    "neotoma": "tools.local_data.sql_feed_deeptime:neotoma",
    "idigbio-fossils": "tools.local_data.sql_feed_deeptime:idigbio_fossils",
    "banks": "tools.local_data.sql_feed_institutions:banks",
    "exempt-orgs": "tools.local_data.sql_feed_institutions:exempt_orgs",
    "museums-libraries": "tools.local_data.sql_feed_institutions:museums_libraries",
    "schools": "tools.local_data.sql_feed_institutions:schools",
    "historical-topo-maps": "tools.local_data.sql_feed_institutions:historical_topo_maps",
    "usgs-samples": "tools.local_data.sql_feed_institutions:usgs_samples",
    "wikidata-kansas": "tools.local_data.sql_feed_wikidata_plss:wikidata_kansas",
    "plss-grid": "tools.local_data.sql_feed_wikidata_plss:plss_grid",
    "bridges": "tools.local_data.sql_feed_bulk:bridges",
    "epa-facilities": "tools.local_data.sql_feed_bulk:epa_facilities",
    "newspaper-text": "tools.local_data.sql_feed_bulk:newspaper_text",
    "newspaper-text-rebuild": "tools.local_data.sql_feed_bulk:newspaper_text_rebuild",
    "osm-kansas": "tools.local_data.sql_feed_bulk:osm_kansas",
    "archive-texts": "tools.local_data.sql_feed_texts:archive_texts",
    "newspaper-directory": "tools.local_data.sql_feed_texts:newspaper_directory",
    "towers": "tools.local_data.sql_feed_texts:towers",
    "census-acs-full": "tools.local_data.sql_feed_census:census_acs_full",
    "census-decennial-full": "tools.local_data.sql_feed_census:census_decennial_full",
}
# Large feeds load a separately snapshotted database (--bulk-db).
BULK_FEEDS: frozenset[str] = frozenset({"archive-texts", "bridges", "census-acs-full", "census-decennial-full", "epa-facilities", "newspaper-text", "newspaper-text-rebuild", "osm-kansas"})
BULK_SCHEMA = """
CREATE TABLE IF NOT EXISTS kfm_sql_sources (
 file_id INTEGER PRIMARY KEY, source_id TEXT NOT NULL, source_path TEXT NOT NULL,
 sha256 TEXT NOT NULL UNIQUE, source_bytes INTEGER NOT NULL, source_url TEXT NOT NULL,
 receipt_json TEXT NOT NULL, imported_rows INTEGER NOT NULL DEFAULT 0, state TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS kfm_sql_build (
 name TEXT PRIMARY KEY, value TEXT NOT NULL) WITHOUT ROWID;
"""
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


def _get(url: str, read: Callable, *, timeout: int, missing_ok: bool, attempts: int):
    """GET url and pass the response to read. A 404 is None when missing_ok; other failures retry, then raise."""
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return read(response)
        except urllib.error.HTTPError as error:
            if error.code == 404 and missing_ok:
                return None
            if error.code < 500 or attempt == attempts - 1:
                raise FeedError(f"HTTP_{error.code} {url}") from None
        # IncompleteRead (a connection dropped mid-transfer, as IEM did on 2026-11-02) is an HTTPException,
        # not a ConnectionError: retried like the others.
        except (urllib.error.URLError, TimeoutError, ConnectionError, http.client.HTTPException) as error:
            if attempt == attempts - 1:
                raise FeedError(f"FETCH_FAILED {url}: {error}") from None
        time.sleep(5 * 4 ** attempt)
    raise FeedError(f"FETCH_FAILED {url}")


def http_fetch(url: str, *, limit: int, timeout: int = 120, missing_ok: bool = False, attempts: int = 3) -> Fetched | None:
    """GET url into memory with a byte ceiling."""
    def read(response):
        body = response.read(limit + 1)
        if len(body) > limit:
            raise FeedError(f"RESPONSE_TOO_LARGE {url}")
        return Fetched(url, body, response.headers.get("Last-Modified"), response.headers.get("ETag"))
    return _get(url, read, timeout=timeout, missing_ok=missing_ok, attempts=attempts)


def http_download(url: str, dest: Path, *, limit: int, timeout: int = 600, missing_ok: bool = False, attempts: int = 3) -> Fetched | None:
    """GET url into the file dest (replaced), with a byte ceiling, for downloads too large to hold in memory.
    The returned Fetched has an empty body."""
    def read(response):
        total = 0
        with open(dest, "wb") as out:
            while chunk := response.read(1 << 20):
                total += len(chunk)
                if total > limit:
                    raise FeedError(f"RESPONSE_TOO_LARGE {url}")
                out.write(chunk)
        return Fetched(url, b"", response.headers.get("Last-Modified"), response.headers.get("ETag"))
    return _get(url, read, timeout=timeout, missing_ok=missing_ok, attempts=attempts)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while chunk := handle.read(1 << 20):
            digest.update(chunk)
    return digest.hexdigest()


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
    download: Callable[..., Fetched | None] | None = None   # None: http_download, or ctx.fetch when that is replaced
    now: Callable[[], datetime] = utc_now
    log: Callable[[dict], None] = lambda line: print(json.dumps(line, sort_keys=True), flush=True)
    catalogs: list[Path] = field(default_factory=list)
    floor: int = FREE_FLOOR
    shared_dirs: list[Path] = field(default_factory=list)   # the other database's folder, counted against the ceiling
    bulk_db: Path | None = None
    lock_depth: int = 0

    def note(self, event: str, **fields) -> None:
        self.log({"at": self.now().strftime("%Y-%m-%dT%H:%M:%SZ"), "event": event, **fields})


def download(ctx: Context, url: str, dest: Path, *, limit: int, timeout: int = 600, missing_ok: bool = False) -> Fetched | None:
    """Stream url into dest (see http_download). Where a test replaced ctx.fetch, the download goes through it."""
    if ctx.download is not None:
        return ctx.download(url, dest, limit=limit, timeout=timeout, missing_ok=missing_ok)
    if ctx.fetch is http_fetch:
        return http_download(url, dest, limit=limit, timeout=timeout, missing_ok=missing_ok)
    fetched = ctx.fetch(url, limit=limit, timeout=timeout, missing_ok=missing_ok)
    if fetched is None:
        return None
    Path(dest).write_bytes(fetched.body)
    return Fetched(fetched.url, b"", fetched.last_modified, fetched.etag)


def temp_path(ctx: Context, name: str) -> Path:
    """A scratch file on the store's filesystem but outside data/, so the per-file backup never sees it."""
    if "/" in name or name.startswith("."):
        raise FeedError("TEMP_NAME_UNSAFE")
    folder = ctx.root / "tmp-sql-feeds"
    folder.mkdir(mode=0o700, exist_ok=True)
    return folder / f"{os.getpid()}-{name}"


def store_raw(ctx: Context, feed: str, name: str, body: bytes | Path, *, url: str, fetched: Fetched | None = None,
              original: bytes | Path | None = None, extra: dict | None = None) -> tuple[Path, str]:
    """Write one immutable raw object and its receipt under data/raw/sql-feeds/<feed>/.

    body is what is kept (for curated sources, the Kansas-only subset): bytes, or a file from
    temp_path() that is moved into place. original, when given, is the full download (bytes or a
    file, left where it is), recorded only by size and SHA-256.
    """
    if "/" in feed or ".." in Path(name).parts or name.startswith("/"):
        raise FeedError("RAW_NAME_UNSAFE")
    path = ctx.root / "data/raw/sql-feeds" / feed / name
    receipt_path = ctx.root / "data/receipts/ingest/sql-feeds" / feed / (name + ".json")
    is_file = isinstance(body, Path)
    digest, size = (file_sha256(body), body.stat().st_size) if is_file else (sha256(body), len(body))
    if path.exists():
        if (file_sha256(path) if is_file else sha256(path.read_bytes())) != digest:
            raise FeedError(f"RAW_OBJECT_CHANGED {name}")
        if is_file:
            body.unlink()
        return path, digest
    if original is not None:
        original = ({"sha256": file_sha256(original), "bytes": original.stat().st_size} if isinstance(original, Path)
                    else {"sha256": sha256(original), "bytes": len(original)})
    receipt = {"format": "kfm-sql-feed-receipt-v1", "feed": feed, "path": str(path.relative_to(ctx.root)), "sha256": digest,
               "bytes": size, "source_url": url, "retrieved_at": ctx.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
               "last_modified": fetched.last_modified if fetched else None, "etag": fetched.etag if fetched else None,
               **({"original": {**original, "kept": False}} if original is not None else {}),
               **(extra or {})}
    for target, data in ((path, body), (receipt_path, (json.dumps(receipt, indent=1, sort_keys=True) + "\n").encode())):
        target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        temp = target.with_name(target.name + ".part")
        if isinstance(data, Path):
            os.replace(data, temp)
            with open(temp, "rb") as handle:
                os.fsync(handle.fileno())
        else:
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
    if CAP is not None:
        files = {p.resolve() for d in [out, *ctx.shared_dirs] for p in d.glob("*") if p.is_file()}
        files.update(p.resolve() for p in ctx.catalogs if p.is_file())
        used = sum(p.stat().st_size for p in files)
        if used >= CAP - RESERVE:
            raise FeedError("CEILING_85GB_HEADROOM_STOP")
    stat = os.statvfs(out)
    if stat.f_bavail * stat.f_frsize < ctx.floor:
        raise FeedError("FREE_SPACE_FLOOR_REACHED")


def init_bulk(ctx: Context) -> None:
    """Create the bulk database (outside the per-file backup) with the base tables the feeds expect."""
    if ctx.db_path.is_file():
        return
    ctx.db_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    with pipeline_lock(ctx):
        db = sqlite3.connect(ctx.db_path, isolation_level=None)
        try:
            db.executescript(BULK_SCHEMA)
            db.execute("INSERT OR IGNORE INTO kfm_sql_build VALUES ('bulk-policy', ?)", (canonical({
                "created_at": ctx.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "scope": "Large Kansas feeds kept apart from observations.sqlite; same receipts and ceilings",
                "backup": "Separate verified SQLite snapshot (sql_snapshot.py)"}),))
        finally:
            db.close()
    os.chmod(ctx.db_path, 0o600)


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


def load_version(db: sqlite3.Connection, ctx: Context, *, source_id: str, key: str, path: Path, digest: str, url: str,
                 table: str, rows, width: int) -> dict:
    """Load one version of a provider file that is published again over time (a year's file, a bulk
    export), replacing the version loaded before: in one transaction its rows are deleted and its
    source record is marked superseded. key names the file across versions and is recorded in the
    receipt (store_raw extra={"key": key}). rows yields tuples of width values; each is stored as
    (file_id, row_number, *values), so table needs file_id as the first column of an index.
    Call with the pipeline lock held."""
    receipt = receipt_for(ctx, path)
    if receipt.get("key") != key:
        raise FeedError(f"RECEIPT_KEY_MISMATCH {key}")
    previous = db.execute("SELECT file_id, sha256 FROM kfm_sql_sources WHERE source_id=? AND state='complete' "
                          "AND json_extract(receipt_json,'$.key')=?", (source_id, key)).fetchall()
    if digest in {sha for _, sha in previous}:
        return {"state": "unchanged", "rows": 0, "superseded": 0}
    if loaded(db, digest):
        # The same bytes are already recorded for another key, or for an older version of this one.
        raise FeedError(f"SOURCE_CONTENT_SHARED {key}")
    file_id = begin_source(db, ctx, source_id, path, digest, url, receipt)
    try:
        for old, _ in previous:
            db.execute(f"DELETE FROM {table} WHERE file_id=?", (old,))
            db.execute("UPDATE kfm_sql_sources SET state='superseded' WHERE file_id=?", (old,))
        sql, batch, count = f"INSERT INTO {table} VALUES ({','.join('?' * (width + 2))})", [], 0
        for row in rows:
            if len(row) != width:
                raise FeedError(f"ROW_SHAPE {key} {count + len(batch) + 1}")
            batch.append((file_id, count + len(batch) + 1, *row))
            if len(batch) == 20000:
                db.executemany(sql, batch)
                count += len(batch)
                batch = []
        db.executemany(sql, batch)
        count += len(batch)
        finish_source(db, file_id, count)
    except BaseException:
        db.execute("ROLLBACK")
        raise
    return {"state": "loaded", "rows": count, "superseded": len(previous)}


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
    parser.add_argument("--bulk-db", type=Path, help="Database for the BULK_FEEDS, also counted against the ceiling")
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
    bulk = args.command == "run" and args.feed in BULK_FEEDS
    if bulk and not args.bulk_db:
        parser.error(f"{args.feed} loads the bulk database: pass --bulk-db")
    if args.bulk_db and args.bulk_db.resolve() == args.db.resolve():
        parser.error("--bulk-db must be different from --db")
    shared = [p.parent for p in ([args.db] if bulk else [args.bulk_db] if args.bulk_db else [])]
    ctx = Context(root=args.root, db_path=args.bulk_db if bulk else args.db, tiger=args.tiger, nwm_gpkg=args.nwm_gpkg,
                  lock=args.lock, catalogs=args.catalog, shared_dirs=shared, bulk_db=args.bulk_db)
    if args.command == "status":
        result = status(ctx)
        if ctx.bulk_db and ctx.bulk_db.is_file():
            result["bulk"] = status(Context(root=ctx.root, db_path=ctx.bulk_db))
        print(json.dumps(result, indent=1, sort_keys=True))
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
        if "retained_mismatch" in result:
            # A kept copy no longer has its recorded bytes: the new copy is published, but the backup volume needs a look.
            ctx.note("snapshot_failed", command=args.command, reason="SNAPSHOT_RETAINED_MISMATCH " + result["retained_mismatch"])
            return 1
        return 0
    started = time.monotonic()
    try:
        if bulk:
            init_bulk(ctx)
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
