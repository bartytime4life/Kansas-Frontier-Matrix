"""Spatial sidecars for the SQL databases: one R-tree of bounding boxes per table that stores geometry.

Every feed table with a ``geometry_geojson`` column (or ``min_lon``/``min_lat``/``max_lon``/``max_lat``
columns, as the OSM tables have) gets a sidecar virtual table ``<table>_rtree(id, min_lon, max_lon,
min_lat, max_lat)``. Its ``id`` is ``file_id << 32 | row_number``, the row's stable identity across
reloads (rowids are not: a feed replaces a source file by deleting its rows and inserting new ones).
``kfm_spatial_index`` records which ``file_id`` values each sidecar covers, so a refresh after a feed
run only removes the superseded files' entries and adds the new files' entries, and a reader can tell
a current sidecar from a stale one by comparing those file ids (and the table's greatest file_id)
with the table itself.

The website's ``recovered-near`` question joins the sidecar to its table for "what is in this map
area" without scanning the table: a bounding-box question over 2.26 million OSM elements that took
11.7 s by scan answers through the R-tree in milliseconds.

    python -m tools.local_data.sql_feeds --root STORE --db observations.sqlite [--bulk-db kfm-bulk.sqlite] \
        [--lock pipeline.lock] spatial build|check [--table TABLE]

``build`` reconciles every geometry table under the pipeline lock; ``check`` reports each sidecar's
state read-only and exits 1 when any is missing or stale. ``sql_feeds.py run FEED`` refreshes the
written database's sidecars after a successful feed run.
"""
from __future__ import annotations

import json
import math
import sqlite3

from tools.local_data.sql_feeds import Context, FeedError, canonical, pipeline_lock

STATE_TABLE = "kfm_spatial_index"
STATE_SCHEMA = f"""
CREATE TABLE IF NOT EXISTS {STATE_TABLE} (
  table_name TEXT PRIMARY KEY, file_ids_json TEXT NOT NULL, max_file_id INTEGER, entries INTEGER NOT NULL,
  updated_at TEXT NOT NULL) WITHOUT ROWID;
"""
BBOX_COLUMNS = ("min_lon", "min_lat", "max_lon", "max_lat")
GEOMETRY_COLUMN = "geometry_geojson"
ROW_LIMIT = 1 << 32
BATCH = 20000
# Tables the framework owns, never spatial.
SKIP_PREFIXES = ("kfm_sql_", "kfm_feed_", "kfm_spatial_", "sqlite_")


def sidecar(table: str) -> str:
    return table + "_rtree"


def key(file_id: int, row_number: int) -> int:
    return (file_id << 32) | row_number


def _q(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def geometry_tables(db: sqlite3.Connection) -> dict[str, dict]:
    """table name -> {"bbox": has the four bbox columns, "geometry": has geometry_geojson}."""
    found = {}
    names = [row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    for name in names:
        if name.startswith(SKIP_PREFIXES) or name.endswith("_rtree") or "_rtree_" in name:
            continue
        columns = {row[1] for row in db.execute(f"PRAGMA table_info({_q(name)})")}
        if "file_id" not in columns or "row_number" not in columns:
            continue
        bbox, geometry = all(c in columns for c in BBOX_COLUMNS), GEOMETRY_COLUMN in columns
        if bbox or geometry:
            found[name] = {"bbox": bbox, "geometry": geometry}
    return found


def _walk(value, out: list) -> None:
    if isinstance(value, (list, tuple)):
        if len(value) >= 2 and isinstance(value[0], (int, float)) and isinstance(value[1], (int, float)):
            out.append((float(value[0]), float(value[1])))
        else:
            for item in value:
                _walk(item, out)


def bbox_of(text: str | None) -> tuple[float, float, float, float] | None:
    """(min_lon, min_lat, max_lon, max_lat) of a GeoJSON geometry, or None when it has no finite positions."""
    if not text:
        return None
    try:
        value = json.loads(text)
    except ValueError:
        return None
    if not isinstance(value, dict):
        return None
    positions: list[tuple[float, float]] = []
    if value.get("type") == "GeometryCollection":
        for member in value.get("geometries") or []:
            if isinstance(member, dict):
                _walk(member.get("coordinates"), positions)
    else:
        _walk(value.get("coordinates"), positions)
    positions = [(x, y) for x, y in positions if math.isfinite(x) and math.isfinite(y) and -180 <= x <= 180 and -90 <= y <= 90]
    if not positions:
        return None
    return (min(x for x, _ in positions), min(y for _, y in positions), max(x for x, _ in positions), max(y for _, y in positions))


def _file_ids(db: sqlite3.Connection, table: str) -> list[int]:
    return [int(row[0]) for row in db.execute(f"SELECT DISTINCT file_id FROM {_q(table)} ORDER BY file_id")]


def _recorded(db: sqlite3.Connection, table: str) -> dict | None:
    row = db.execute(f"SELECT file_ids_json, max_file_id, entries, updated_at FROM {STATE_TABLE} WHERE table_name=?", (table,)).fetchone()
    return {"file_ids": json.loads(row[0]), "max_file_id": row[1], "entries": row[2], "updated_at": row[3]} if row else None


def _add_file(db: sqlite3.Connection, table: str, info: dict, file_id: int) -> tuple[int, int]:
    """Insert the sidecar entries for one source file. Returns (entries, rows skipped for no usable box)."""
    rt, t = _q(sidecar(table)), _q(table)
    entries = 0
    if info["bbox"]:
        cursor = db.execute(
            f"INSERT INTO {rt}(id, min_lon, max_lon, min_lat, max_lat) "
            f"SELECT (file_id << 32) | row_number, min_lon, max_lon, min_lat, max_lat FROM {t} "
            f"WHERE file_id=? AND row_number < ? AND min_lon IS NOT NULL AND min_lat IS NOT NULL AND max_lon IS NOT NULL AND max_lat IS NOT NULL "
            f"AND min_lon BETWEEN -180 AND 180 AND max_lon BETWEEN -180 AND 180 AND min_lat BETWEEN -90 AND 90 AND max_lat BETWEEN -90 AND 90 "
            f"AND min_lon <= max_lon AND min_lat <= max_lat", (file_id, ROW_LIMIT))
        entries += cursor.rowcount
        where = f"WHERE file_id=? AND row_number < ? AND (min_lon IS NULL OR min_lat IS NULL OR max_lon IS NULL OR max_lat IS NULL)"
    else:
        where = "WHERE file_id=? AND row_number < ?"
    if info["geometry"]:
        rows = db.execute(f"SELECT row_number, {GEOMETRY_COLUMN} FROM {t} {where}", (file_id, ROW_LIMIT))
        batch = []
        while True:
            chunk = rows.fetchmany(BATCH)
            if not chunk:
                break
            for row_number, text in chunk:
                box = bbox_of(text)
                if box is None:
                    continue
                batch.append((key(file_id, int(row_number)), box[0], box[2], box[1], box[3]))
            if batch:
                db.executemany(f"INSERT INTO {rt}(id, min_lon, max_lon, min_lat, max_lat) VALUES (?,?,?,?,?)", batch)
                entries += len(batch)
                batch = []
    # Every row of the file that got no entry is skipped: no geometry, unreadable or empty GeoJSON, a box
    # outside the planet or inverted, or a row_number beyond the key space.
    total = db.execute(f"SELECT COUNT(*) FROM {t} WHERE file_id=?", (file_id,)).fetchone()[0]
    return entries, total - entries


def reconcile(db: sqlite3.Connection, ctx: Context, table: str, info: dict) -> dict:
    """Bring one table's sidecar up to date with the files the table holds now. Call with the lock held."""
    rt = _q(sidecar(table))
    current = _file_ids(db, table)
    db.execute("BEGIN IMMEDIATE")
    try:
        exists = db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (sidecar(table),)).fetchone()
        db.execute(f"CREATE VIRTUAL TABLE IF NOT EXISTS {rt} USING rtree(id, min_lon, max_lon, min_lat, max_lat)")
        recorded = _recorded(db, table)
        if recorded is None or not exists:
            # No record of what the sidecar covers: start it clean.
            db.execute(f"DELETE FROM {rt}")
            known: list[int] = []
        else:
            known = [int(f) for f in recorded["file_ids"]]
        removed = [f for f in known if f not in set(current)]
        added = [f for f in current if f not in set(known)]
        for file_id in removed:
            db.execute(f"DELETE FROM {rt} WHERE id >= ? AND id < ?", (key(file_id, 0), key(file_id + 1, 0)))
        entries = skipped = 0
        for file_id in added:
            e, s = _add_file(db, table, info, file_id)
            entries, skipped = entries + e, skipped + s
        total = db.execute(f"SELECT COUNT(*) FROM {rt}").fetchone()[0]
        db.execute(f"INSERT OR REPLACE INTO {STATE_TABLE} VALUES (?,?,?,?,?)",
                   (table, canonical(current), max(current) if current else None, total, ctx.now().strftime("%Y-%m-%dT%H:%M:%SZ")))
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise
    return {"table": table, "files": len(current), "added": len(added), "removed": len(removed), "entries": total, "new_entries": entries, "skipped": skipped}


def refresh(ctx: Context, db: sqlite3.Connection, tables: list[str] | None = None) -> list[dict]:
    """Reconcile every geometry table's sidecar (or the named ones) under the pipeline lock."""
    found = geometry_tables(db)
    chosen = list(found) if tables is None else tables
    unknown = [t for t in chosen if t not in found]
    if unknown:
        raise FeedError("SPATIAL_TABLE_UNKNOWN " + ",".join(unknown))
    results = []
    with pipeline_lock(ctx):
        db.executescript(STATE_SCHEMA)
        for table in chosen:
            result = reconcile(db, ctx, table, found[table])
            ctx.note("spatial_index", **result)
            results.append(result)
    return results


def refresh_after_feed(ctx: Context, feed: str) -> None:
    """After a feed wrote its database, bring that database's sidecars up to date; a failure is noted, never fatal."""
    try:
        db = sqlite3.connect(ctx.db_path, timeout=120, isolation_level=None)
        try:
            db.execute("PRAGMA busy_timeout=120000")
            refresh(ctx, db)
        finally:
            db.close()
    except (FeedError, sqlite3.Error) as error:
        ctx.note("spatial_index_failed", feed=feed, reason=str(error))


def check(db: sqlite3.Connection) -> list[dict]:
    """Read-only: each geometry table's sidecar state: current, stale (files changed since it was built) or missing."""
    has_state = db.execute("SELECT 1 FROM sqlite_master WHERE name=?", (STATE_TABLE,)).fetchone() is not None
    report = []
    for table, info in geometry_tables(db).items():
        exists = db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (sidecar(table),)).fetchone()
        recorded = _recorded(db, table) if has_state else None
        if not exists or recorded is None:
            report.append({"table": table, "state": "missing", "entries": 0})
            continue
        current = _file_ids(db, table)
        greatest = db.execute(f"SELECT MAX(file_id) FROM {_q(table)}").fetchone()[0]
        stale = [int(f) for f in recorded["file_ids"]] != current or recorded["max_file_id"] != greatest
        report.append({"table": table, "state": "stale" if stale else "current", "entries": recorded["entries"],
                       "files": len(current), "updated_at": recorded["updated_at"]})
    return report


def command(ctx: Context, action: str, table: str | None = None) -> tuple[int, list[dict]]:
    """The `spatial build|check` subcommand for one database. Returns (exit code, report)."""
    if action == "check":
        db = sqlite3.connect(ctx.db_path.resolve().as_uri() + "?mode=ro", uri=True)
        try:
            report = check(db)
        finally:
            db.close()
        if table is not None:
            report = [r for r in report if r["table"] == table]
        return (1 if any(r["state"] != "current" for r in report) or not report else 0), report
    # Do not recreate a requested database if it disappears after CLI preflight.
    db = sqlite3.connect(ctx.db_path.resolve().as_uri() + "?mode=rw", uri=True, timeout=120, isolation_level=None)
    try:
        db.execute("PRAGMA journal_mode=WAL")
        db.execute("PRAGMA busy_timeout=120000")
        return 0, refresh(ctx, db, None if table is None else [table])
    finally:
        db.close()
