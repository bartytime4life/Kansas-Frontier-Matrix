#!/usr/bin/env python3
"""Inspect workstation folders and copy explicit, immutable migration selections.

This operator never deletes originals, relocates Git metadata, changes a service,
admits a source, or publishes data. Inventory totals are metadata observations,
not byte-integrity proof. Copy plans bind every regular file to a fresh digest.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import time
import uuid

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from tools.local_data.file_io import capture_file, hash_regular, read_regular, write_new

DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
SCHEMA = "kfm-workstation-consolidation/v1"
PROTECTED = {".git", ".wrangler", "credentials", "secrets", "runtime", "runtimes"}
SECRET_NAMES = {"credentials.json", "credential.json", "token.json", "tokens.json",
                "client_secret.json", "client_secrets.json"}
LANES = {"raw", "work", "quarantine", "processed", "catalog", "triplets",
         "receipts", "proofs", "registry", "published", "pre_raw"}


class ConsolidationError(ValueError):
    pass


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def absolute(value):
    path = Path(value)
    if not path.is_absolute() or ".." in path.parts or any(ord(c) < 32 for c in str(path)):
        raise ConsolidationError("UNSAFE_ABSOLUTE_PATH")
    return path


@contextmanager
def directory(path):
    """Anchor all existing ancestors with O_NOFOLLOW, including root aliases."""
    path = absolute(path)
    descriptor = os.open(path.anchor, DIR_FLAGS)
    try:
        for part in path.parts[1:]:
            child = os.open(part, DIR_FLAGS, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        yield descriptor
    finally:
        os.close(descriptor)


def identity(info):
    return [info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns]


def scan(path, *, max_entries=5_000_000, max_seconds=300, detail=False):
    """Count every regular file, including caches; report links without following.

    Errors, scan limits, or changing directories make the snapshot incomplete.
    No payload is read. The observation is not a transactional tree snapshot.
    """
    start = time.monotonic()
    result = {"files": 0, "bytes": 0, "directories": 0, "links": [], "special": [],
              "errors": [], "changed": [], "groups": {}, "protected": [], "complete": True}
    fingerprint = hashlib.sha256()
    entries = 0
    records = []

    def walk(fd, prefix="", depth=0):
        nonlocal entries
        if depth > 128:
            raise ConsolidationError("SCAN_DEPTH_LIMIT")
        before = os.fstat(fd)
        with os.scandir(fd) as iterator:
            children = sorted(iterator, key=lambda e: e.name)
        for entry in children:
            entries += 1
            if entries > max_entries or time.monotonic() - start > max_seconds:
                raise ConsolidationError("SCAN_LIMIT")
            relative = f"{prefix}/{entry.name}" if prefix else entry.name
            try:
                info = os.stat(entry.name, dir_fd=fd, follow_symlinks=False)
                kind = "directory" if stat.S_ISDIR(info.st_mode) else "file" if stat.S_ISREG(info.st_mode) else "link" if stat.S_ISLNK(info.st_mode) else "special"
                row = {"path": relative, "kind": kind, "identity": identity(info), "mode": stat.S_IMODE(info.st_mode)}
                fingerprint.update(canonical(row) + b"\n")
                if detail:
                    records.append(row)
                if entry.name in PROTECTED or entry.name in SECRET_NAMES or entry.name.startswith(".env"):
                    result["protected"].append(relative)
                if kind == "directory":
                    result["directories"] += 1
                    child = os.open(entry.name, DIR_FLAGS, dir_fd=fd)
                    try:
                        if identity(os.fstat(child)) != identity(info):
                            result["changed"].append(relative)
                        walk(child, relative, depth + 1)
                    finally:
                        os.close(child)
                elif kind == "file":
                    result["files"] += 1
                    result["bytes"] += info.st_size
                    parts = relative.split("/")
                    group = "/".join(parts[:3]) if len(parts) > 3 and parts[0] == "data" and parts[1] in LANES else parts[0] if len(parts) > 1 else "(top-level)"
                    counts = result["groups"].setdefault(group, {"files": 0, "bytes": 0})
                    counts["files"] += 1
                    counts["bytes"] += info.st_size
                elif kind == "link":
                    result["links"].append({"path": relative, "target": os.readlink(entry.name, dir_fd=fd)})
                else:
                    result["special"].append(relative)
            except OSError as error:
                result["errors"].append({"path": relative, "errno": error.errno})
        after = os.fstat(fd)
        if identity(before) != identity(after):
            result["changed"].append(prefix or ".")

    try:
        with directory(path) as fd:
            walk(fd)
    except (OSError, ConsolidationError) as error:
        result["errors"].append({"path": ".", "code": str(error) if isinstance(error, ConsolidationError) else error.errno})
    result["complete"] = not result["errors"] and not result["changed"]
    result["metadata_sha256"] = fingerprint.hexdigest()
    result["entries"] = entries
    result["elapsed_seconds"] = round(time.monotonic() - start, 3)
    if detail:
        result["records"] = records
    return result


def git_identity(path):
    """Read Git identity without refreshing indexes or running configured hooks."""
    if not (path / ".git").exists():
        return None
    result = {}
    env = {**os.environ, "GIT_OPTIONAL_LOCKS": "0", "GIT_TERMINAL_PROMPT": "0"}
    prefix = ["git", "-c", "core.fsmonitor=false", "-c", "core.hooksPath=/dev/null", "-C", str(path)]
    for name, arguments in [("head", ["rev-parse", "HEAD"]), ("branch", ["branch", "--show-current"]),
                            ("status", ["status", "--porcelain=v1", "--untracked-files=normal"]),
                            ("remotes", ["remote", "-v"]), ("common_dir", ["rev-parse", "--git-common-dir"])]:
        try:
            completed = subprocess.run(prefix + arguments, env=env, capture_output=True, text=True, timeout=15)
            value = re.sub(r"(https?://)[^/@\s]+:[^/@\s]+@", r"\1[redacted]@", completed.stdout.strip())
            result[name] = value if completed.returncode == 0 else {"error": "GIT_READ_FAILED", "returncode": completed.returncode}
        except subprocess.TimeoutExpired:
            result[name] = {"error": "GIT_READ_TIMEOUT"}
    return result


def inventory(projects, repository, *, active_paths=(), max_entries=5_000_000, max_seconds=300):
    projects, repository = absolute(projects), absolute(repository)
    active_paths = [absolute(p) for p in active_paths]
    folders = []
    with directory(projects) as fd:
        names = sorted(os.listdir(fd))
        for name in names:
            info = os.stat(name, dir_fd=fd, follow_symlinks=False)
            path = projects / name
            if stat.S_ISLNK(info.st_mode):
                folders.append({"path": str(path), "kind": "symlink", "target": os.readlink(name, dir_fd=fd),
                                "disposition": "preserve-alias; resolve-consumers-before-switch"})
                continue
            if not stat.S_ISDIR(info.st_mode):
                continue
            git = git_identity(path)
            candidate = "kfm" in name.casefold() or "kansas" in name.casefold() or bool(git and "Kansas-Frontier-Matrix" in str(git.get("remotes", "")))
            observed = scan(path, max_entries=max_entries, max_seconds=max_seconds)
            active = any(p == path or path in p.parents for p in active_paths)
            is_store = (path / ".kfm-local-store.json").is_file()
            role = "canonical-repository" if path == repository else "external-data-store" if is_store else "git-checkout" if git else "source-runtime-or-evidence-copy" if candidate else "separate-project"
            disposition = "retain-canonical" if path == repository else "hold-storage-boundary; curate-in-place" if is_store else "preserve-active-consumers" if active else "preserve-git-history; compare-before-relocation" if git and candidate else "inspect-unique-content-and-consumers-before-copy" if candidate else "exclude-separate-project"
            folders.append({"path": str(path), "kind": "directory", "kfm_candidate": candidate,
                            "role": role, "active_path_overlap": active, "writer_state": "confirmed-active-path" if active else "not-proven-inactive",
                            "git": git, "scan": observed, "disposition": disposition,
                            "rights": "unknown-unless-bound-source-evidence", "integrity": "metadata-only; not-rehashed"})
    return {"schema": SCHEMA, "operation": "inventory", "generated_at": now(),
            "projects_root": str(projects), "repository": str(repository),
            "scope": "all top-level directories; no symlink traversal; no payload reads; metadata observations",
            "folders": folders, "complete": all(r.get("scan", {}).get("complete", True) for r in folders)}


def plan_copy(source, destination, allowed_root, repository, *, owning_root, placement_basis, max_bytes):
    """Plan an explicit byte copy. Governance decisions must precede this call."""
    source, destination, allowed_root, repository = map(absolute, [source, destination, allowed_root, repository])
    if not isinstance(max_bytes, int) or isinstance(max_bytes, bool) or max_bytes < 0:
        raise ConsolidationError("INVALID_BYTE_LIMIT")
    if source == destination or source in destination.parents or destination in source.parents:
        raise ConsolidationError("OVERLAPPING_TREES")
    if allowed_root not in destination.parents:
        raise ConsolidationError("DESTINATION_OUTSIDE_ALLOWED_ROOT")
    if not owning_root.strip() or not placement_basis.strip():
        raise ConsolidationError("PLACEMENT_BASIS_REQUIRED")
    # Never use this copy interface to weaken the current external-store contract.
    if (source / ".kfm-local-store.json").exists() or source.name in LANES or "data" in source.parts:
        if destination == repository or repository in destination.parents:
            raise ConsolidationError("EXTERNAL_STORE_MUST_REMAIN_SEPARATE")
    if destination.exists() or destination.is_symlink():
        raise ConsolidationError("DESTINATION_COLLISION")
    with directory(allowed_root):
        pass
    observed = scan(source, detail=True)
    if not observed["complete"]:
        raise ConsolidationError("SOURCE_SCAN_INCOMPLETE")
    if observed["links"] or observed["special"] or observed["protected"] or any(r["path"] == ".kfm-copy-plan.json" for r in observed["records"]):
        raise ConsolidationError("PROTECTED_OR_LINKED_SOURCE_REQUIRES_SEPARATE_MIGRATION")
    if observed["bytes"] > max_bytes:
        raise ConsolidationError("PLAN_BYTE_LIMIT")
    records = []
    for row in observed["records"]:
        if row["kind"] == "file":
            path = source / row["path"]
            digest, size = hash_regular(path, max_bytes, expected_size=row["identity"][2])
            if identity(path.lstat()) != row["identity"]:
                raise ConsolidationError("SOURCE_CHANGED")
            records.append({**row, "sha256": digest, "bytes": size})
        else:
            records.append(row)
    if scan(source)["metadata_sha256"] != observed["metadata_sha256"]:
        raise ConsolidationError("SOURCE_CHANGED")
    value = {"schema": SCHEMA, "operation": "copy-plan", "id": str(uuid.uuid4()), "generated_at": now(),
             "source": str(source), "destination": str(destination), "allowed_root": str(allowed_root),
             "repository": str(repository), "owning_root": owning_root, "placement_basis": placement_basis,
             "bytes": observed["bytes"], "files": observed["files"], "max_bytes": max_bytes,
             "source_metadata_sha256": observed["metadata_sha256"], "records": records,
             "non_effects": ["source deletion", "consumer switch", "admission", "release", "publication"]}
    value["plan_sha256"] = hashlib.sha256(canonical(value)).hexdigest()
    return value


def validate_plan(value):
    if not isinstance(value, dict):
        raise ConsolidationError("PLAN_SHAPE_INVALID")
    original = dict(value)
    digest = original.pop("plan_sha256", None)
    if digest != hashlib.sha256(canonical(original)).hexdigest() or value.get("operation") != "copy-plan" or value.get("schema") != SCHEMA:
        raise ConsolidationError("PLAN_INTEGRITY_FAILED")
    try:
        if str(uuid.UUID(value.get("id", ""))) != value["id"]:
            raise ValueError
    except (ValueError, AttributeError, KeyError, TypeError):
        raise ConsolidationError("PLAN_ID_INVALID") from None
    source, destination, allowed_root = map(absolute, [value["source"], value["destination"], value["allowed_root"]])
    if allowed_root not in destination.parents or source == destination or source in destination.parents or destination in source.parents:
        raise ConsolidationError("PLAN_CONTAINMENT_FAILED")
    repository = absolute(value["repository"])
    if ((source / ".kfm-local-store.json").exists() or source.name in LANES or "data" in source.parts) and (destination == repository or repository in destination.parents):
        raise ConsolidationError("EXTERNAL_STORE_MUST_REMAIN_SEPARATE")
    if not isinstance(value.get("records"), list):
        raise ConsolidationError("PLAN_SHAPE_INVALID")
    if not isinstance(value.get("max_bytes"), int) or isinstance(value["max_bytes"], bool) or value["max_bytes"] < 0:
        raise ConsolidationError("INVALID_BYTE_LIMIT")
    seen = set()
    total = files = 0
    for row in value["records"]:
        if not isinstance(row, dict) or not isinstance(row.get("path"), str) or not isinstance(row.get("mode"), int) or isinstance(row["mode"], bool) or not 0 <= row["mode"] <= 0o7777:
            raise ConsolidationError("PLAN_UNSAFE_MEMBER")
        relative = Path(row["path"])
        if (relative.is_absolute() or not relative.parts or ".." in relative.parts or str(relative) != row["path"]
                or row["path"] in seen or row["path"] == ".kfm-copy-plan.json"
                or any(p in PROTECTED or p in SECRET_NAMES or p.startswith(".env") for p in relative.parts)):
            raise ConsolidationError("PLAN_UNSAFE_MEMBER")
        seen.add(row["path"])
        if row["kind"] not in {"file", "directory"}:
            raise ConsolidationError("PLAN_UNSAFE_MEMBER")
        if row["kind"] == "file":
            if (not isinstance(row.get("bytes"), int) or isinstance(row["bytes"], bool) or row["bytes"] < 0
                    or not re.fullmatch(r"[0-9a-f]{64}", str(row.get("sha256")))):
                raise ConsolidationError("PLAN_UNSAFE_MEMBER")
            files += 1
            total += row["bytes"]
    if total != value.get("bytes") or files != value.get("files") or total > value["max_bytes"]:
        raise ConsolidationError("PLAN_TOTALS_MISMATCH")
    return source, destination, allowed_root


def copy_plan(value, receipts, *, reserve_bytes=1024 ** 3):
    """Resume a verified copy without overwriting any existing destination file."""
    source, destination, allowed_root = validate_plan(value)
    receipts = absolute(receipts)
    if not isinstance(reserve_bytes, int) or isinstance(reserve_bytes, bool) or reserve_bytes < 0:
        raise ConsolidationError("INVALID_SPACE_RESERVE")
    if source == receipts or source in receipts.parents or destination == receipts or destination in receipts.parents:
        raise ConsolidationError("RECEIPTS_MUST_BE_SEPARATE")
    with directory(allowed_root):
        pass
    observed = scan(source)
    if not observed["complete"] or observed["metadata_sha256"] != value["source_metadata_sha256"]:
        raise ConsolidationError("SOURCE_CHANGED")
    # Each application has a durable unique receipt. A failed copy is resumable;
    # the destination is never treated as active until verified separately.
    write_new(receipts / f"{value['id']}-{uuid.uuid4()}-started.json", canonical({"schema": SCHEMA, "state": "copy-started", "plan_sha256": value["plan_sha256"], "time": now()}))
    if shutil.disk_usage(allowed_root).free < value["bytes"] + reserve_bytes:
        raise ConsolidationError("INSUFFICIENT_COPY_SPACE")
    if destination.exists():
        with directory(destination):
            pass
        marker = destination / ".kfm-copy-plan.json"
        if json.loads(read_regular(marker, 4096)).get("plan_sha256") != value["plan_sha256"]:
            raise ConsolidationError("DESTINATION_COLLISION")
    else:
        # Existing ancestors are validated by write_new; only private owned trees
        # are supported. Concurrent hostile ancestor replacement is out of scope.
        write_new(destination / ".kfm-copy-plan.json", canonical({"plan_sha256": value["plan_sha256"]}))
    for row in value["records"]:
        target = destination / row["path"]
        if row["kind"] == "directory":
            from tools.local_data.file_io import check_directory
            check_directory(target, create=True)
            continue
        if target.exists() or target.is_symlink():
            if hash_regular(target, row["bytes"], expected_size=row["bytes"])[0] != row["sha256"]:
                raise ConsolidationError("DESTINATION_CONTENT_COLLISION")
        else:
            capture_file(source / row["path"], target, sha256=row["sha256"], size_bytes=row["bytes"], max_bytes=row["bytes"])
        # Keep owner execution/read bits for source launchers, while making the
        # copy private. This does not reproduce group/world sharing permissions.
        os.chmod(target, row["mode"] & 0o700)
    receipt = verify_copy(value)
    write_new(receipts / f"{value['id']}-{uuid.uuid4()}-verified.json", canonical(receipt))
    return receipt


def verify_copy(value):
    source, destination, _allowed_root = validate_plan(value)
    for row in value["records"]:
        if row["kind"] == "file":
            for base in [source, destination]:
                digest, _size = hash_regular(base / row["path"], row["bytes"], expected_size=row["bytes"])
                if digest != row["sha256"]:
                    raise ConsolidationError("COPY_DIGEST_MISMATCH")
        else:
            with directory(destination / row["path"]):
                pass
    observed = scan(source)
    if not observed["complete"] or observed["metadata_sha256"] != value["source_metadata_sha256"]:
        raise ConsolidationError("SOURCE_CHANGED")
    actual = scan(destination, detail=True)
    expected = {r["path"] for r in value["records"]} | {".kfm-copy-plan.json"}
    if not actual["complete"] or {r["path"] for r in actual["records"]} != expected or actual["links"] or actual["special"]:
        raise ConsolidationError("DESTINATION_MEMBERS_MISMATCH")
    return {"schema": SCHEMA, "state": "copy-verified; consumers-unchanged", "generated_at": now(),
            "plan_sha256": value["plan_sha256"], "source": str(source), "destination": str(destination),
            "files": value["files"], "bytes": value["bytes"], "originals_preserved": True,
            "rollback": "Consumers remain on the original path; retain the copy until separately approved cleanup."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    inv = sub.add_parser("inventory")
    inv.add_argument("--projects", required=True)
    inv.add_argument("--repository", required=True)
    inv.add_argument("--active-path", action="append", default=[])
    inv.add_argument("--output", required=True)
    planning = sub.add_parser("plan")
    for name in ["source", "destination", "allowed-root", "repository", "owning-root", "placement-basis", "output"]:
        planning.add_argument("--" + name, required=True)
    planning.add_argument("--max-bytes", type=int, required=True)
    for name in ["copy", "verify"]:
        operation = sub.add_parser(name)
        operation.add_argument("--plan", required=True)
        if name == "copy":
            operation.add_argument("--receipts", required=True)
    args = parser.parse_args()
    try:
        if args.command == "inventory":
            value = inventory(args.projects, args.repository, active_paths=args.active_path)
            write_new(absolute(args.output), canonical(value))
            print(json.dumps({"output": args.output, "folders": len(value["folders"]), "complete": value["complete"]}))
        elif args.command == "plan":
            value = plan_copy(args.source, args.destination, args.allowed_root, args.repository,
                              owning_root=args.owning_root, placement_basis=args.placement_basis, max_bytes=args.max_bytes)
            write_new(absolute(args.output), canonical(value))
            print(json.dumps({"output": args.output, "files": value["files"], "bytes": value["bytes"], "plan_sha256": value["plan_sha256"]}))
        else:
            value = json.loads(read_regular(absolute(args.plan), 128 * 1024 ** 2))
            print(json.dumps(copy_plan(value, args.receipts) if args.command == "copy" else verify_copy(value)))
    except (ValueError, OSError) as error:
        print(json.dumps({"state": "held", "reason": str(error)}), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
