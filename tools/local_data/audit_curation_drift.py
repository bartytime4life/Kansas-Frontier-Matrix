"""Read-only source drift check against a verified local curation snapshot.

Run from the repository root with ``python3 -m tools.local_data.audit_curation_drift``.
This is a currentness check, not a new source inventory or admission decision.
"""

from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import gzip
import hashlib
import json
import os
import stat as stat_module
from pathlib import Path, PurePosixPath

from tools.local_data import review_curation

MAX_BASELINE_ROWS = 100_000
ACTIVE_SUFFIXES = ("/catalog.sqlite", "/catalog.sqlite-wal", "/catalog.sqlite-shm",
                   "/curation.log", "/.curation.lock", "/.download")


def _mutable(relative: str) -> bool:
    return relative.startswith("PRISM data/") and (
        relative.endswith(ACTIVE_SUFFIXES)
        or relative.startswith("PRISM data/Kansas/work/")
        or PurePosixPath(relative).suffix.lower() in (".part", ".tmp")
    )


def _digest_stable(path: Path) -> tuple[str, str]:
    try:
        before = path.stat()
        sha = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
                sha.update(chunk)
        after = path.stat()
    except OSError:
        return "", "read_error"
    identity = lambda stat: (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns)
    if identity(before) != identity(after):
        return "", "changed_during_hash"
    return sha.hexdigest(), "stable_hash"


def _load_baseline(path: Path) -> dict[str, dict[str, str]]:
    try:
        with gzip.open(path, "rt", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            required = {"original_path", "collection", "size_bytes", "mtime_ns", "sha256", "hash_state"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise review_curation.Held("INVALID_SOURCE_INVENTORY")
            rows = {}
            for row in reader:
                relative = row["original_path"]
                parts = PurePosixPath(relative).parts
                if (not relative or relative.startswith("/") or "\\" in relative
                        or ".." in parts or "." in parts or len(parts) < 2
                        or str(PurePosixPath(relative)) != relative
                        or parts[0] != row["collection"] or relative in rows):
                    raise review_curation.Held("INVALID_SOURCE_INVENTORY")
                try:
                    int(row["size_bytes"])
                    int(row["mtime_ns"])
                except (ValueError, TypeError) as exc:
                    raise review_curation.Held("INVALID_SOURCE_INVENTORY") from exc
                rows[relative] = row
                if len(rows) > MAX_BASELINE_ROWS:
                    raise review_curation.Held("SOURCE_INVENTORY_TOO_LARGE")
    except (OSError, UnicodeError, csv.Error) as exc:
        raise review_curation.Held("INVALID_SOURCE_INVENTORY") from exc
    return rows


def audit(raw: Path, baseline: dict[str, dict[str, str]]) -> dict:
    """Compare paths/stats; hash only new or stat-changed nonmutable files."""
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    seen: set[str] = set()
    changes: list[dict] = []
    counts: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    scan_errors: list[str] = []

    def record_error(error: OSError) -> None:
        scan_errors.append(type(error).__name__)

    for directory, dirs, files in os.walk(raw, followlinks=False, onerror=record_error):
        dirs.sort()
        files.sort()
        base = Path(directory)
        for name in dirs:
            path = base / name
            if path.is_symlink():
                relative = path.relative_to(raw).as_posix()
                collection = relative.split("/", 1)[0]
                counts[collection]["directory_symlink_held"] += 1
                changes.append({"path": relative, "collection": collection,
                                "state": "directory_symlink_held"})
        for name in files:
            path = base / name
            relative = path.relative_to(raw).as_posix()
            collection = relative.split("/", 1)[0]
            seen.add(relative)
            if path.is_symlink():
                state = "file_symlink_held"
                changes.append({"path": relative, "collection": collection, "state": state})
                counts[collection][state] += 1
                continue
            try:
                stat = path.stat()
            except OSError:
                state = "vanished_or_unreadable_during_scan"
                changes.append({"path": relative, "collection": collection, "state": state})
                counts[collection][state] += 1
                continue
            if not stat_module.S_ISREG(stat.st_mode):
                state = "special_file_held"
                changes.append({"path": relative, "collection": collection, "state": state})
                counts[collection][state] += 1
                continue
            old = baseline.get(relative)
            if _mutable(relative):
                state = "active_mutable" if old else "added_active_mutable"
                counts[collection][state] += 1
                if not old:
                    changes.append({"path": relative, "collection": collection,
                                    "state": state, "size_bytes": stat.st_size})
                continue
            if (old and int(old["size_bytes"]) == stat.st_size
                    and int(old["mtime_ns"]) == stat.st_mtime_ns):
                counts[collection]["unchanged_stat_only"] += 1
                continue
            sha, hash_state = _digest_stable(path)
            if hash_state != "stable_hash":
                state = hash_state
            elif old is None:
                state = "added_hashed"
            elif old["sha256"] == sha:
                state = "metadata_changed_bytes_same"
            else:
                state = "content_changed_hashed"
            changes.append({"path": relative, "collection": collection, "state": state,
                            "size_bytes": stat.st_size, "sha256": sha})
            counts[collection][state] += 1
    for relative, old in baseline.items():
        if relative not in seen:
            collection = old["collection"]
            state = "missing_since_snapshot"
            changes.append({"path": relative, "collection": collection, "state": state,
                            "prior_hash_state": old["hash_state"]})
            counts[collection][state] += 1
    state_counts = collections.Counter(change["state"] for change in changes)
    return {
        "status": "SCAN_INCOMPLETE" if scan_errors else (
            "SOURCE_DRIFT_REVIEW" if changes else "SOURCE_SNAPSHOT_STAT_MATCH"),
        "started_utc": started,
        "completed_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "baseline_files": len(baseline), "seen_paths": len(seen),
        "by_collection": {name: dict(counter) for name, counter in sorted(counts.items())},
        "change_counts": dict(sorted(state_counts.items())),
        "scan_error_count": len(scan_errors),
        "changes": sorted(changes, key=lambda item: item["path"]),
        "limits": ["Unchanged size and modification time do not reprove unchanged bytes",
                   "Mutable PRISM files can change during or after the scan",
                   "Symlinks are held; their targets are not treated as independent source files",
                   "This check does not admit, delete, release, deploy, or publish data"],
    }


def inspect(root: Path, bundle_name: str) -> dict:
    verified = review_curation.inspect(root, bundle_name)
    root = root.resolve(strict=True)
    raw = (root / "data/raw").resolve(strict=True)
    bundle = (root / "data/processed" / bundle_name).resolve(strict=True)
    if raw.parent != root / "data" or not raw.is_dir():
        raise review_curation.Held("INVALID_RAW_LOCATION")
    baseline = _load_baseline(bundle / "inventory/source_files.csv.gz")
    if len(baseline) != verified["source_files_at_snapshot"]:
        raise review_curation.Held("INVENTORY_COUNT_MISMATCH")
    result = audit(raw, baseline)
    result["bundle"] = bundle_name
    result["baseline_snapshot_utc"] = verified["snapshot_completed_utc"]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=os.environ.get("KFM_DATA_ROOT"),
                        help="External store root, or set KFM_DATA_ROOT")
    parser.add_argument("--bundle", required=True, help="Verified reconciliation bundle")
    parser.add_argument("--full", action="store_true", help="Include every changed path")
    args = parser.parse_args()
    try:
        if not args.root:
            raise review_curation.Held("MISSING_LOCAL_STORE")
        result = inspect(Path(args.root), args.bundle)
    except review_curation.Held as exc:
        print(json.dumps({"status": "HELD", "reason": exc.code}, sort_keys=True))
        return 1
    if not args.full:
        result["sample_changes"] = result.pop("changes")[:20]
    print(json.dumps(result, sort_keys=True))
    return 1 if result["status"] == "SCAN_INCOMPLETE" else 0


if __name__ == "__main__":
    raise SystemExit(main())
