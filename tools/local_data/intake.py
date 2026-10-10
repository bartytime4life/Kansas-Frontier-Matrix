#!/usr/bin/env python3
"""Raw-data intake pipeline: discover, profile, route, index and explicitly apply.

Stages
  1. discover  RAW and QUARANTINE files in the private KFM_DATA_ROOT store, plus an
               optional read-only inbox directory of downloads not yet captured.
  2. profile   each file by content (tools/local_data/intake_profile.py).
  3. route     each profile to local store / database / work lane / Git card /
               GitHub release candidate (tools/local_data/intake_route.py).
  4. index     results in ``data/work/intake/index.sqlite`` with an R*Tree extent
               table, reusing unchanged profiles on later runs.
  5. apply     only on explicit request: stage a verified review copy into the
               WORK lane or write a metadata card, each with an immutable receipt.

Analysis is read-only for source bytes. Nothing is deleted, promoted to
PROCESSED/PUBLISHED, committed, uploaded, or admitted as a source.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import shutil
import sqlite3
import stat
import sys
import threading
import time
import uuid
from contextlib import contextmanager
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from tools.local_data import intake_route  # noqa: E402
from tools.local_data.acquisition import validate_root  # noqa: E402
from tools.local_data.file_io import capture_file, check_directory, hash_regular, read_regular, write_new  # noqa: E402
from tools.local_data.intake_profile import ANALYZER_VERSION, profile_file  # noqa: E402
from tools.local_data.library import EXCLUDED_DIRECTORIES, EXCLUDED_FILES  # noqa: E402
from tools.local_data.manage import canonical, external_root, utc_now  # noqa: E402

INDEX_SCHEMA_VERSION = "1"
QUARANTINE_BINDING_VERSION = "source-and-digest/v1"
DEFAULT_HASH_LIMIT = 4 * 1024 ** 3
DEFAULT_STAGE_LIMIT = 8 * 1024 ** 3
FREE_SPACE_RESERVE = 1024 ** 3
MAX_FILES = 200_000
MAX_DEPTH = 32
LIST_LIMIT = 500


class IntakeError(ValueError):
    pass


def intake_dir(root: Path) -> Path:
    return root / "data/work/intake"


def item_id(lane: str, relative: str) -> str:
    return hashlib.sha256(f"{lane}\0{relative}".encode("utf-8")).hexdigest()[:32]


# --- discovery ------------------------------------------------------------

def _walk(base: Path, prefix: str = "", *, skip: set[str] | None = None, counters: dict | None = None):
    """Yield (relative_path, Path, stat) for regular files; never follow links."""
    counters = counters if counters is not None else {}
    stack = [(base, prefix, 0)]
    while stack:
        directory, rel, depth = stack.pop()
        if depth > MAX_DEPTH:
            counters["depth_limited"] = counters.get("depth_limited", 0) + 1
            continue
        try:
            entries = sorted(os.scandir(directory), key=lambda e: e.name)
        except (FileNotFoundError, NotADirectoryError, PermissionError):
            counters["unreadable"] = counters.get("unreadable", 0) + 1
            continue
        for entry in entries:
            lowered = entry.name.lower()
            if entry.name.startswith(".") or lowered in EXCLUDED_DIRECTORIES or lowered in EXCLUDED_FILES:
                continue
            child = f"{rel}/{entry.name}" if rel else entry.name
            if skip and child in skip:
                continue
            info = entry.stat(follow_symlinks=False)
            if stat.S_ISLNK(info.st_mode):
                counters["symlinks_skipped"] = counters.get("symlinks_skipped", 0) + 1
            elif stat.S_ISDIR(info.st_mode):
                stack.append((Path(entry.path), child, depth + 1))
            elif stat.S_ISREG(info.st_mode):
                yield child, Path(entry.path), info
            else:
                counters["special_skipped"] = counters.get("special_skipped", 0) + 1


def quarantine_bindings(root: Path) -> dict[tuple[str, str], list[dict]]:
    """Map (source directory, digest) to that source's declared capture bindings."""
    found: dict[tuple[str, str], list[dict]] = {}
    base = root / "data/quarantine"
    if not base.is_dir():
        return found
    for source in sorted(os.scandir(base), key=lambda e: e.name):
        versions = Path(source.path) / "versions"
        if not source.is_dir(follow_symlinks=False) or not versions.is_dir() or versions.is_symlink():
            continue
        for _rel, path, info in _walk(versions):
            if not path.name.endswith(".json") or info.st_size > 64 * 1024:
                continue
            try:
                value = json.loads(read_regular(path, 64 * 1024))
            except (ValueError, OSError):
                continue
            if (isinstance(value, dict) and isinstance(value.get("sha256"), str)
                    and value.get("source_id") == source.name):
                found.setdefault((source.name, value["sha256"]), []).append(value)
    for rows in found.values():
        rows.sort(key=lambda r: (str(r.get("source_id")), str(r.get("dataset_id")), str(r.get("version")), str(r.get("relative_path"))))
    return found


def discover(root: Path, inbox: Path | None = None, counters: dict | None = None):
    """Yield candidate items from RAW, QUARANTINE payloads and an optional inbox."""
    counters = counters if counters is not None else {}
    bindings = quarantine_bindings(root)
    count = 0

    def bump():
        nonlocal count
        count += 1
        if count > MAX_FILES:
            raise IntakeError("INTAKE_FILE_LIMIT")

    raw = root / "data/raw"
    for rel, path, info in _walk(raw, counters=counters):
        bump()
        yield {"lane": "raw", "relative_path": rel, "store_path": f"data/raw/{rel}", "path": path, "stat": info, "declared": None, "sha256": None}
    quarantine = root / "data/quarantine"
    for rel, path, info in _walk(quarantine, counters=counters):
        parts = rel.split("/")
        # Only content-addressed payloads are data; runs/versions are capture metadata.
        if len(parts) != 5 or parts[1:3] != ["objects", "sha256"] or parts[4] != "payload":
            continue
        bump()
        declared_rows = bindings.get((parts[0], parts[3]), [])
        declared = dict(declared_rows[0]) if declared_rows else None
        if declared is not None:
            declared["binding_count"] = len(declared_rows)
        yield {"lane": "quarantine", "relative_path": rel, "store_path": f"data/quarantine/{rel}", "path": path,
               "stat": info, "declared": declared, "sha256": parts[3]}
    if inbox is not None:
        for rel, path, info in _walk(inbox, counters=counters):
            bump()
            yield {"lane": "inbox", "relative_path": rel, "store_path": None, "path": path, "stat": info, "declared": None, "sha256": None}


# --- index ----------------------------------------------------------------

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS items (
  id TEXT PRIMARY KEY, lane TEXT NOT NULL, relative_path TEXT NOT NULL, store_path TEXT,
  size_bytes INTEGER NOT NULL, mtime_ns INTEGER NOT NULL, sha256 TEXT,
  declared_json TEXT, profile_json TEXT NOT NULL, decision_json TEXT NOT NULL,
  family TEXT, kind TEXT, domain TEXT, status TEXT, kansas TEXT, time_start TEXT, time_end TEXT,
  analyzer_version TEXT NOT NULL, analyzed_at TEXT NOT NULL, run_id TEXT NOT NULL, present INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS items_status ON items(status);
CREATE INDEX IF NOT EXISTS items_domain ON items(domain);
CREATE INDEX IF NOT EXISTS items_family ON items(family);
CREATE VIRTUAL TABLE IF NOT EXISTS item_extent USING rtree(rid, min_x, max_x, min_y, max_y);
CREATE TABLE IF NOT EXISTS runs (
  run_id TEXT PRIMARY KEY, started_at TEXT NOT NULL, finished_at TEXT, state TEXT NOT NULL,
  discovered INTEGER NOT NULL DEFAULT 0, analyzed INTEGER NOT NULL DEFAULT 0, reused INTEGER NOT NULL DEFAULT 0,
  failed INTEGER NOT NULL DEFAULT 0, summary_json TEXT
);
CREATE TABLE IF NOT EXISTS applications (
  seq INTEGER PRIMARY KEY AUTOINCREMENT, item_id TEXT NOT NULL, action TEXT NOT NULL, target TEXT,
  sha256 TEXT, applied_at TEXT NOT NULL, receipt_path TEXT NOT NULL
);
"""


@contextmanager
def open_index(root: Path, *, allow_stale_bindings: bool = False):
    """Open (and create) the private intake index inside the validated store."""
    base = intake_dir(root)
    check_directory(base, create=True)
    path = base / "index.sqlite"
    for name in ("index.sqlite", "index.sqlite-wal", "index.sqlite-shm", "index.sqlite-journal"):
        if (base / name).is_symlink():
            raise IntakeError("INDEX_SYMLINK_REJECTED")
    created = not path.exists()
    conn = sqlite3.connect(path, timeout=10, check_same_thread=False)
    try:
        if created and os.name == "posix":
            os.chmod(path, 0o600)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        conn.executescript(SCHEMA_SQL)
        conn.execute("INSERT OR IGNORE INTO meta(key, value) VALUES ('schema_version', ?)", (INDEX_SCHEMA_VERSION,))
        version = conn.execute("SELECT value FROM meta WHERE key='schema_version'").fetchone()[0]
        if version != INDEX_SCHEMA_VERSION:
            raise IntakeError("INDEX_SCHEMA_UNSUPPORTED")
        binding_version = conn.execute("SELECT value FROM meta WHERE key='quarantine_binding_version'").fetchone()
        if (not allow_stale_bindings and binding_version != (QUARANTINE_BINDING_VERSION,)
                and conn.execute("SELECT 1 FROM items WHERE lane='quarantine' LIMIT 1").fetchone()):
            # Digest-only indexes may contain another source's permissions.
            # Only a complete analysis can make their decisions usable again.
            raise IntakeError("INTAKE_REANALYSIS_REQUIRED")
        yield conn
        conn.commit()
    finally:
        conn.close()


@contextmanager
def writer_lock(root: Path):
    """One writer at a time (analysis or apply); readers are never blocked."""
    base = intake_dir(root)
    check_directory(base, create=True)
    fd = os.open(base / ".intake.lock", os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0), 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise IntakeError("INTAKE_BUSY") from None
        yield
    finally:
        os.close(fd)


def _row_item(row: sqlite3.Row | tuple, columns) -> dict:
    value = dict(zip(columns, row))
    value["declared"] = json.loads(value.pop("declared_json")) if value.get("declared_json") else None
    value["profile"] = json.loads(value.pop("profile_json"))
    value["decision"] = json.loads(value.pop("decision_json"))
    value["present"] = bool(value["present"])
    return value


ITEM_COLUMNS = ("id", "lane", "relative_path", "store_path", "size_bytes", "mtime_ns", "sha256", "declared_json",
                "profile_json", "decision_json", "family", "kind", "domain", "status", "kansas", "time_start",
                "time_end", "analyzer_version", "analyzed_at", "run_id", "present")


# --- analysis -------------------------------------------------------------

def analyze(root: Path, *, inbox: Path | None = None, budget: dict | None = None, hash_limit: int = DEFAULT_HASH_LIMIT,
            progress=lambda _state: None, cancel: threading.Event | None = None) -> dict:
    """Profile and route every discovered file; reuse profiles of unchanged files."""
    budget = budget or intake_route.load_budget()
    run_id = time.strftime("intake-%Y%m%dT%H%M%SZ-", time.gmtime()) + uuid.uuid4().hex[:8]
    counters: dict = {}
    summary = {"run_id": run_id, "started_at": utc_now(), "discovered": 0, "analyzed": 0, "reused": 0, "failed": 0,
               "by_status": {}, "by_family": {}, "by_lane": {}, "skipped": counters}
    with writer_lock(root), open_index(root, allow_stale_bindings=True) as conn:
        current_bindings = conn.execute("SELECT value FROM meta WHERE key='quarantine_binding_version'").fetchone() == (QUARANTINE_BINDING_VERSION,)
        conn.execute("INSERT INTO runs(run_id, started_at, state) VALUES (?, ?, 'running')", (run_id, summary["started_at"]))
        conn.commit()
        seen: set[str] = set()
        state = "complete"
        try:
            for found in discover(root, inbox, counters):
                if cancel is not None and cancel.is_set():
                    state = "cancelled"
                    break
                summary["discovered"] += 1
                info = found["stat"]
                identity = item_id(found["lane"], found["relative_path"])
                seen.add(identity)
                previous = conn.execute("SELECT size_bytes, mtime_ns, analyzer_version, profile_json, sha256, declared_json FROM items WHERE id=?", (identity,)).fetchone()
                sha256 = found["sha256"]
                # Domain, filename hints and review flags also depend on the
                # declaration, even when the payload bytes have not changed.
                # Legacy profiles may already be stale relative to their saved
                # declaration, so refresh all quarantine profiles on upgrade.
                if (previous and previous[0] == info.st_size and previous[1] == info.st_mtime_ns
                        and previous[2] == ANALYZER_VERSION
                        and (found["lane"] != "quarantine" or current_bindings)
                        and (json.loads(previous[5]) if previous[5] else None) == found["declared"]):
                    profile = json.loads(previous[3])
                    sha256 = sha256 or previous[4]
                    summary["reused"] += 1
                else:
                    try:
                        profile = profile_file(found["path"], display_path=(found["declared"] or {}).get("relative_path") or found["relative_path"],
                                               declared=found["declared"])
                        if sha256 is None and info.st_size <= hash_limit:
                            sha256, _size = hash_regular(found["path"], hash_limit, expected_size=info.st_size)
                        elif sha256 is None:
                            profile["issues"] = sorted(set(profile["issues"]) | {"not_hashed_size_limit"})
                        summary["analyzed"] += 1
                    except (ValueError, OSError) as error:
                        summary["failed"] += 1
                        profile = {"schema": "kfm-intake-profile/v1", "analyzer_version": ANALYZER_VERSION,
                                   "format": {"family": "unknown", "kind": "unknown", "media_type": "application/octet-stream"},
                                   "spatial": {"crs": None, "native_bbox": None, "bbox_wgs84": None, "kansas": "unknown", "geometry_types": {}},
                                   "temporal": {}, "structure": {}, "hints": {"domain": None, "review_flags": []},
                                   "issues": ["format_reader_failed", "read_error:" + (str(error) if str(error).isupper() else type(error).__name__)],
                                   "profiled_at": utc_now()}
                item = {"id": identity, "lane": found["lane"], "relative_path": found["relative_path"], "store_path": found["store_path"],
                        "size_bytes": info.st_size, "sha256": sha256, "declared": found["declared"]}
                decision = intake_route.decide(item, profile, budget)
                _upsert(conn, item, info, profile, decision, run_id)
                for key, value in (("by_status", decision["status"]), ("by_family", profile["format"]["family"]), ("by_lane", found["lane"])):
                    summary[key][value] = summary[key].get(value, 0) + 1
                if summary["discovered"] % 50 == 0:
                    conn.commit()
                    progress(dict(summary))
            if state == "complete":
                # Items that disappeared are kept as history, never deleted.
                scanned = ("raw", "quarantine", "inbox") if inbox is not None else ("raw", "quarantine")
                for (identity,) in conn.execute(f"SELECT id FROM items WHERE present=1 AND lane IN ({','.join('?' * len(scanned))})", scanned).fetchall():
                    if identity not in seen:
                        conn.execute("UPDATE items SET present=0 WHERE id=?", (identity,))
                conn.execute("INSERT INTO meta(key, value) VALUES ('quarantine_binding_version', ?) "
                             "ON CONFLICT(key) DO UPDATE SET value=excluded.value", (QUARANTINE_BINDING_VERSION,))
        except Exception:
            state = "failed"
            raise
        finally:
            summary["finished_at"] = utc_now()
            summary["state"] = state
            conn.execute("UPDATE runs SET finished_at=?, state=?, discovered=?, analyzed=?, reused=?, failed=?, summary_json=? WHERE run_id=?",
                         (summary["finished_at"], state, summary["discovered"], summary["analyzed"], summary["reused"],
                          summary["failed"], json.dumps(summary, sort_keys=True), run_id))
            conn.commit()
            progress(dict(summary))
    return summary


def _upsert(conn, item, info, profile, decision, run_id):
    temporal = profile.get("temporal") or {}
    conn.execute(
        """INSERT INTO items(id, lane, relative_path, store_path, size_bytes, mtime_ns, sha256, declared_json, profile_json,
           decision_json, family, kind, domain, status, kansas, time_start, time_end, analyzer_version, analyzed_at, run_id, present)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,1)
           ON CONFLICT(id) DO UPDATE SET size_bytes=excluded.size_bytes, mtime_ns=excluded.mtime_ns, sha256=excluded.sha256,
           declared_json=excluded.declared_json, profile_json=excluded.profile_json, decision_json=excluded.decision_json,
           family=excluded.family, kind=excluded.kind, domain=excluded.domain, status=excluded.status, kansas=excluded.kansas,
           time_start=excluded.time_start, time_end=excluded.time_end, analyzer_version=excluded.analyzer_version,
           analyzed_at=excluded.analyzed_at, run_id=excluded.run_id, present=1""",
        (item["id"], item["lane"], item["relative_path"], item["store_path"], info.st_size, info.st_mtime_ns, item["sha256"],
         json.dumps(item["declared"], sort_keys=True) if item["declared"] else None, json.dumps(profile, sort_keys=True),
         json.dumps(decision, sort_keys=True), profile["format"]["family"], profile["format"]["kind"], decision["domain"],
         decision["status"], profile["spatial"]["kansas"], temporal.get("content_start"), temporal.get("content_end"),
         ANALYZER_VERSION, profile.get("profiled_at") or utc_now(), run_id))
    rowid = conn.execute("SELECT rowid FROM items WHERE id=?", (item["id"],)).fetchone()[0]
    conn.execute("DELETE FROM item_extent WHERE rid=?", (rowid,))
    bbox = profile["spatial"].get("bbox_wgs84")
    if bbox:
        conn.execute("INSERT INTO item_extent(rid, min_x, max_x, min_y, max_y) VALUES (?,?,?,?,?)", (rowid, bbox[0], bbox[2], bbox[1], bbox[3]))


# --- queries --------------------------------------------------------------

def list_items(root: Path, *, status=None, domain=None, family=None, lane=None, bbox=None, text=None,
               include_missing=False, limit=100, offset=0) -> dict:
    """Filter indexed items; ``bbox`` is a WGS84 [min_x, min_y, max_x, max_y] intersection."""
    limit = max(1, min(int(limit), LIST_LIMIT))
    offset = max(0, int(offset))
    where, args = [], []
    for column, value in (("status", status), ("domain", domain), ("family", family), ("lane", lane)):
        if value:
            where.append(f"items.{column}=?")
            args.append(value)
    if not include_missing:
        where.append("items.present=1")
    if text:
        where.append("(items.relative_path LIKE ? ESCAPE '\\' OR items.declared_json LIKE ? ESCAPE '\\')")
        pattern = "%" + str(text)[:100].replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"
        args += [pattern, pattern]
    join = ""
    if bbox:
        x0, y0, x1, y1 = (float(v) for v in bbox)
        join = "JOIN item_extent ON item_extent.rid = items.rowid"
        where.append("item_extent.max_x >= ? AND item_extent.min_x <= ? AND item_extent.max_y >= ? AND item_extent.min_y <= ?")
        args += [x0, x1, y0, y1]
    clause = (" WHERE " + " AND ".join(where)) if where else ""
    with open_index(root) as conn:
        total = conn.execute(f"SELECT COUNT(*) FROM items {join}{clause}", args).fetchone()[0]
        rows = conn.execute(f"SELECT {', '.join('items.' + c for c in ITEM_COLUMNS)} FROM items {join}{clause} "
                            "ORDER BY items.status, items.domain, items.relative_path LIMIT ? OFFSET ?", args + [limit, offset]).fetchall()
    return {"schema": "kfm-intake-list/v1", "total": total, "limit": limit, "offset": offset,
            "items": [_summary(_row_item(r, ITEM_COLUMNS)) for r in rows]}


def _summary(item: dict) -> dict:
    profile, decision = item["profile"], item["decision"]
    declared_path = (item["declared"] or {}).get("relative_path")
    return {"id": item["id"], "lane": item["lane"], "relative_path": item["relative_path"], "size_bytes": item["size_bytes"],
            "name": (declared_path or item["relative_path"]).rsplit("/", 1)[-1],
            "sha256": item["sha256"], "kind": profile["format"]["kind"], "family": profile["format"]["family"],
            "domain": decision["domain"], "status": decision["status"], "kansas": profile["spatial"]["kansas"],
            "bbox_wgs84": profile["spatial"]["bbox_wgs84"], "time_start": item["time_start"], "time_end": item["time_end"],
            "holds": decision["holds"], "present": item["present"],
            "declared_label": "/".join(str((item["declared"] or {}).get(k)) for k in ("source_id", "dataset_id", "version")) if item["declared"] else None}


def get_item(root: Path, identity: str) -> dict:
    if not isinstance(identity, str) or len(identity) != 32 or any(c not in "0123456789abcdef" for c in identity):
        raise IntakeError("ITEM_ID_INVALID")
    with open_index(root) as conn:
        row = conn.execute(f"SELECT {', '.join(ITEM_COLUMNS)} FROM items WHERE id=?", (identity,)).fetchone()
        if row is None:
            raise IntakeError("ITEM_NOT_FOUND")
        applications = [dict(zip(("action", "target", "sha256", "applied_at", "receipt_path"), r)) for r in
                        conn.execute("SELECT action, target, sha256, applied_at, receipt_path FROM applications WHERE item_id=? ORDER BY seq", (identity,))]
    value = _row_item(row, ITEM_COLUMNS)
    value["applications"] = applications
    return value


def overview(root: Path, budget: dict | None = None) -> dict:
    budget = budget or intake_route.load_budget()
    with open_index(root) as conn:
        def grouped(column):
            return {str(k): {"files": n, "bytes": b or 0} for k, n, b in
                    conn.execute(f"SELECT {column}, COUNT(*), SUM(size_bytes) FROM items WHERE present=1 GROUP BY {column} ORDER BY {column}")}
        last = conn.execute("SELECT summary_json FROM runs WHERE state != 'running' ORDER BY started_at DESC LIMIT 1").fetchone()
        running = conn.execute("SELECT run_id FROM runs WHERE state='running' ORDER BY started_at DESC LIMIT 1").fetchone()
        totals = conn.execute("SELECT COUNT(*), COALESCE(SUM(size_bytes),0) FROM items WHERE present=1").fetchone()
        plan = release_plan_from(conn, budget)
        groups = {f"by_{column}": grouped(column) for column in ("status", "domain", "family", "lane")}
    return {"schema": "kfm-intake-overview/v1", "files": totals[0], "bytes": totals[1], **groups,
            "last_run": json.loads(last[0]) if last and last[0] else None, "running_run": running[0] if running else None,
            "budget": plan["budget_after_plan"], "release_plan_bytes": plan["selected_bytes"]}


def release_plan_from(conn, budget: dict) -> dict:
    """Greedy, deterministic selection of release candidates inside the remaining budget."""
    state = intake_route.budget_state(budget)
    remaining = state["available_for_new_data_bytes"]
    selected, deferred = [], []
    rows = conn.execute("SELECT id, relative_path, size_bytes, sha256, domain, decision_json FROM items WHERE present=1 AND status='ready' "
                        "ORDER BY domain, relative_path").fetchall()
    for identity, rel, size, sha256, domain, decision in rows:
        release = next(p for p in json.loads(decision)["placements"] if p["tier"] == "github_release")
        if release["action"] != "candidate":
            continue
        if sha256 is None:
            deferred.append({"id": identity, "reason": "SHA256_REQUIRED"})
        elif size <= remaining:
            remaining -= size
            selected.append({"id": identity, "relative_path": rel, "domain": domain, "bytes": size, "sha256": sha256,
                             "asset_parts": release.get("asset_parts", 1)})
        else:
            deferred.append({"id": identity, "reason": "GITHUB_BUDGET_EXCEEDED", "bytes": size})
    total = sum(r["bytes"] for r in selected)
    return {"schema": "kfm-intake-release-plan/v1", "status": "plan-only; no upload; owner review required",
            "selected": selected, "deferred": deferred, "selected_bytes": total,
            "budget_before_plan": state, "budget_after_plan": intake_route.budget_state(budget, total)}


def release_plan(root: Path, budget: dict | None = None) -> dict:
    budget = budget or intake_route.load_budget()
    with open_index(root) as conn:
        return release_plan_from(conn, budget)


# --- apply ----------------------------------------------------------------

IDENTITY_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")


def _validated_identity(identity: str) -> str:
    if not isinstance(identity, str) or not IDENTITY_RE.fullmatch(identity):
        raise IntakeError("IDENTITY_INVALID")
    try:
        parsed = uuid.UUID(identity)
    except (ValueError, AttributeError, TypeError):
        raise IntakeError("IDENTITY_INVALID") from None
    if str(parsed) != identity:
        raise IntakeError("IDENTITY_INVALID")
    return identity


def _receipt(root: Path, identity: str, action: str, body: dict) -> str:
    identity = _validated_identity(identity)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    relative = f"data/receipts/intake/{identity}/{stamp}-{action}-{uuid.uuid4().hex[:8]}.json"
    root_resolved = root.resolve(strict=False)
    target = (root / relative).resolve(strict=False)
    if not target.is_relative_to(root_resolved):
        raise IntakeError("UNSAFE_PATH")
    write_new(target, canonical(body))
    return relative


def apply(root: Path, identity: str, action: str, *, stage_limit: int = DEFAULT_STAGE_LIMIT) -> dict:
    """Explicitly apply one recommended placement: ``stage`` (WORK copy) or ``card`` (metadata card)."""
    identity = _validated_identity(identity)
    if action not in ("stage", "card"):
        raise IntakeError("ACTION_UNSUPPORTED")
    with writer_lock(root):
        item = get_item(root, identity)
        if not item["present"]:
            raise IntakeError("ITEM_NOT_PRESENT")
        tiers = {p["tier"]: p for p in item["decision"]["placements"]}
        source = root / item["store_path"] if item["store_path"] else None
        if action == "stage":
            placement = tiers["work_lane"]
            if placement["action"] != "stage" or source is None:
                raise IntakeError("STAGE_NOT_RECOMMENDED:" + placement["reason"])
            target = root / placement["target"]
            if not placement["target"].startswith("data/work/intake/") or ".." in Path(placement["target"]).parts:
                raise IntakeError("STAGE_TARGET_UNSAFE")
            size = item["size_bytes"]
            if size > stage_limit:
                raise IntakeError("STAGE_SIZE_LIMIT")
            if shutil.disk_usage(root).free < size + FREE_SPACE_RESERVE:
                raise IntakeError("INSUFFICIENT_FREE_SPACE")
            sha256 = item["sha256"] or hash_regular(source, stage_limit, expected_size=size)[0]
            if target.exists() or target.is_symlink():
                existing, _ = hash_regular(target, stage_limit)
                if existing != sha256:
                    raise IntakeError("STAGE_TARGET_CONFLICT")
                return {"outcome": "ALREADY_STAGED", "target": placement["target"]}
            # A verified copy, never a hard link: edits to the review copy cannot alter captured bytes.
            capture_file(source, target, sha256=sha256, size_bytes=size, max_bytes=stage_limit)
            body = {"schema": "kfm-intake-receipt/v1", "action": "stage", "item_id": identity, "source": item["store_path"],
                    "target": placement["target"], "sha256": sha256, "size_bytes": size, "domain": item["decision"]["domain"],
                    "applied_at": utc_now(), "lifecycle": "WORK review copy; not processed, admitted, or released"}
            result_target = placement["target"]
        else:
            placement = tiers["git_repo"]
            if placement["action"] != "metadata_card":
                raise IntakeError("CARD_NOT_RECOMMENDED:" + placement["reason"])
            card = intake_route.metadata_card(item, item["profile"], item["decision"])
            encoded = canonical(card)
            if len(encoded) > placement.get("max_bytes", 16384):
                raise IntakeError("CARD_SIZE_LIMIT")
            item_id = str(item["id"])
            result_target = f"data/work/intake/cards/{item_id}.json"
            path = root / result_target
            if path.exists():
                if read_regular(path, 1024 * 1024) == encoded:
                    return {"outcome": "ALREADY_WRITTEN", "target": result_target}
                result_target = f"data/work/intake/cards/{item_id}-{hashlib.sha256(encoded).hexdigest()[:12]}.json"
                path = root / result_target
            write_new(path, encoded)
            sha256 = hashlib.sha256(encoded).hexdigest()
            body = {"schema": "kfm-intake-receipt/v1", "action": "card", "item_id": identity, "target": result_target,
                    "sha256": sha256, "applied_at": utc_now(), "lifecycle": "metadata card for owner review; not committed"}
        receipt = _receipt(root, identity, action, body)
        with open_index(root) as conn:
            conn.execute("INSERT INTO applications(item_id, action, target, sha256, applied_at, receipt_path) VALUES (?,?,?,?,?,?)",
                         (identity, action, result_target, sha256, body["applied_at"], receipt))
    return {"outcome": "APPLIED", "action": action, "target": result_target, "receipt": receipt}


def cards(root: Path) -> list[dict]:
    """Metadata cards for every currently eligible item (stdout export for a repository PR)."""
    out = []
    with open_index(root) as conn:
        for row in conn.execute(f"SELECT {', '.join(ITEM_COLUMNS)} FROM items WHERE present=1 ORDER BY domain, relative_path"):
            item = _row_item(row, ITEM_COLUMNS)
            if any(p["tier"] == "git_repo" and p["action"] == "metadata_card" for p in item["decision"]["placements"]):
                out.append(intake_route.metadata_card(item, item["profile"], item["decision"]))
    return out


# --- CLI ------------------------------------------------------------------

def resolve_root(raw: str | None) -> Path:
    root = external_root(raw or os.environ.get("KFM_DATA_ROOT"))
    validate_root(root)
    return root


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", help="initialized private store (default: KFM_DATA_ROOT)")
    sub = p.add_subparsers(dest="command", required=True)
    a = sub.add_parser("analyze", help="profile and route RAW/QUARANTINE files (and an optional inbox)")
    a.add_argument("--inbox", type=Path, help="read-only directory of downloads not yet captured")
    a.add_argument("--hash-limit", type=int, default=DEFAULT_HASH_LIMIT, help="largest RAW file to hash (bytes)")
    ls = sub.add_parser("list", help="filter indexed items")
    for name in ("status", "domain", "family", "lane", "text"):
        ls.add_argument("--" + name)
    ls.add_argument("--bbox", help="min_lon,min_lat,max_lon,max_lat (WGS84)")
    ls.add_argument("--limit", type=int, default=100)
    ls.add_argument("--offset", type=int, default=0)
    show = sub.add_parser("show", help="full profile and decision for one item")
    show.add_argument("id")
    ap = sub.add_parser("apply", help="apply one recommended placement")
    ap.add_argument("id")
    ap.add_argument("action", choices=("stage", "card"))
    sub.add_parser("overview", help="totals, last run and GitHub budget")
    sub.add_parser("budget", help="GitHub storage budget (no store required)")
    sub.add_parser("release-plan", help="budget-checked GitHub release candidates (plan only)")
    sub.add_parser("cards", help="print eligible metadata cards as JSON")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "budget":
            result = intake_route.budget_state(intake_route.load_budget())
        else:
            root = resolve_root(args.root)
            if args.command == "analyze":
                inbox = None
                if args.inbox:
                    inbox = args.inbox.expanduser().resolve()
                    if not inbox.is_dir() or inbox == root or root in inbox.parents or inbox in root.parents:
                        raise IntakeError("INBOX_MUST_BE_SEPARATE_DIRECTORY")
                result = analyze(root, inbox=inbox, hash_limit=args.hash_limit,
                                 progress=lambda s: print(f"… {s['discovered']} files", file=sys.stderr, flush=True))
            elif args.command == "list":
                bbox = [float(v) for v in args.bbox.split(",")] if args.bbox else None
                if bbox is not None and len(bbox) != 4:
                    raise IntakeError("BBOX_INVALID")
                result = list_items(root, status=args.status, domain=args.domain, family=args.family, lane=args.lane,
                                    text=args.text, bbox=bbox, limit=args.limit, offset=args.offset)
            elif args.command == "show":
                result = get_item(root, args.id)
            elif args.command == "apply":
                result = apply(root, args.id, args.action)
            elif args.command == "overview":
                result = overview(root)
            elif args.command == "release-plan":
                result = release_plan(root)
            else:
                result = cards(root)
    except (ValueError, OSError, sqlite3.Error) as error:
        print(json.dumps({"outcome": "ERROR", "error": str(error) if str(error)[:1].isupper() else type(error).__name__}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
