#!/usr/bin/env python3
"""Explicit, offline local-file synchronization into a private quarantine store."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import sys
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))
from tools.local_data.file_io import (  # noqa: E402
    capture_file, check_directory, fsync_directory, hash_regular, read_regular, write_new,
)

MAX_MANIFEST_BYTES = 4 * 1024 * 1024
MAX_ITEMS = 1000
MAX_FILE_BYTES = 1024**4
MAX_TOTAL_BYTES = 16 * 1024**4
DEFAULT_FILE_BYTES = 8 * 1024**3
DEFAULT_TOTAL_BYTES = 64 * 1024**3
DEFAULT_FREE_BYTES = 256 * 1024**2
LANES = ("raw", "work", "quarantine", "processed", "catalog", "triplets", "receipts", "proofs", "registry", "published")
MARKER = {"schema_version": "1", "scope": "local-quarantine-store"}
TOKEN = re.compile(r"^[a-z][a-z0-9._-]{0,63}$")
VERSION = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
SHA256 = re.compile(r"^[a-f0-9]{64}$")
MEDIA = re.compile(r"^[A-Za-z0-9!#$&^_.+-]+/[A-Za-z0-9!#$&^_.+-]+$")
ITEM_FIELDS = {"source_id", "dataset_id", "domain", "version", "relative_path", "source_uri", "media_type", "rights", "sensitivity", "sha256", "size_bytes", "captured_at"}
AUTHORITY = {"network": False, "source_admission": False, "promotion": False, "release": False, "publication": False}


def canonical(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("JSON_DUPLICATE_KEY")
        value[key] = item
    return value


def reject_number(_value: str) -> None:
    raise ValueError("JSON_NONFINITE_OR_FLOAT")


def parse_json(content: bytes) -> object:
    return json.loads(content, object_pairs_hook=unique_object, parse_constant=reject_number, parse_float=reject_number)


def load_json(path: Path, limit: int = MAX_MANIFEST_BYTES) -> object:
    return parse_json(read_regular(path, limit))


def safe_text(value: object, limit: int) -> bool:
    return isinstance(value, str) and 0 < len(value) <= limit and not any(ord(char) < 32 or ord(char) == 127 for char in value)


def relative_path(value: object) -> str:
    if not safe_text(value, 1024) or "\\" in value or ":" in value:
        raise ValueError("RELATIVE_PATH_UNSAFE")
    parts = value.split("/")
    if any(part in {"", ".", ".."} or part.endswith((" ", ".")) for part in parts) or PurePosixPath(value).is_absolute():
        raise ValueError("RELATIVE_PATH_UNSAFE")
    # Windows device names and alternate streams must not acquire platform-specific meaning.
    if any(part.split(".")[0].upper() in {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))} for part in parts):
        raise ValueError("RELATIVE_PATH_UNSAFE")
    return value


def timestamp(value: object) -> datetime:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", value):
        raise ValueError("UTC_TIMESTAMP_INVALID")
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        raise ValueError("UTC_TIMESTAMP_INVALID") from None


def source_uri(value: object) -> None:
    if not safe_text(value, 2048) or any(char.isspace() for char in value) or "\\" in value:
        raise ValueError("SOURCE_URI_UNSAFE")
    parsed = urlsplit(value)
    if parsed.scheme not in {"https", "kfm", "file-ref"} or parsed.query or parsed.fragment or parsed.username or parsed.password:
        raise ValueError("SOURCE_URI_UNSAFE")
    if (parsed.scheme in {"https", "kfm"} and not parsed.hostname) or (parsed.scheme == "file-ref" and not parsed.path):
        raise ValueError("SOURCE_URI_UNSAFE")


def validate_manifest(value: object, args: argparse.Namespace) -> dict:
    if not isinstance(value, dict) or set(value) != {"schema_version", "items"} or value["schema_version"] != "1":
        raise ValueError("MANIFEST_SHAPE_INVALID")
    items = value["items"]
    if not isinstance(items, list) or not 1 <= len(items) <= args.max_items:
        raise ValueError("MANIFEST_ITEM_LIMIT")
    total = 0
    identities, paths, objects = set(), {}, {}
    for item in items:
        if not isinstance(item, dict) or set(item) != ITEM_FIELDS:
            raise ValueError("ITEM_SHAPE_INVALID")
        for field in ("source_id", "dataset_id", "domain"):
            if not isinstance(item[field], str) or not TOKEN.fullmatch(item[field]):
                raise ValueError("ITEM_IDENTIFIER_INVALID")
            relative_path(item[field])
        if not isinstance(item["version"], str) or not VERSION.fullmatch(item["version"]):
            raise ValueError("ITEM_VERSION_INVALID")
        relative_path(item["version"])
        path = relative_path(item["relative_path"])
        source_uri(item["source_uri"])
        if not isinstance(item["media_type"], str) or len(item["media_type"]) > 255 or not MEDIA.fullmatch(item["media_type"]):
            raise ValueError("MEDIA_TYPE_INVALID")
        rights = item["rights"]
        if not isinstance(rights, dict) or set(rights) != {"license_id", "redistribution"}:
            raise ValueError("RIGHTS_SHAPE_INVALID")
        if rights["license_id"] is not None and not safe_text(rights["license_id"], 256):
            raise ValueError("LICENSE_INVALID")
        if rights["redistribution"] not in ("unknown", "allowed", "restricted", "denied"):
            raise ValueError("RIGHTS_VALUE_INVALID")
        if item["sensitivity"] not in ("unknown", "public", "restricted", "controlled"):
            raise ValueError("SENSITIVITY_INVALID")
        digest, size = item["sha256"], item["size_bytes"]
        if not isinstance(digest, str) or not SHA256.fullmatch(digest) or digest == "0" * 64:
            raise ValueError("CHECKSUM_INVALID")
        if type(size) is not int or not 1 <= size <= args.max_file_bytes:
            raise ValueError("FILE_BYTE_LIMIT")
        timestamp(item["captured_at"])
        identity = (item["source_id"], item["dataset_id"], item["version"], path)
        if identity in identities:
            raise ValueError("DUPLICATE_ITEM")
        identities.add(identity)
        if path.casefold() in paths and paths[path.casefold()] != (path, digest, size):
            raise ValueError("INPUT_PATH_CONFLICT")
        paths[path.casefold()] = (path, digest, size)
        object_key = (item["source_id"], digest)
        if object_key in objects and objects[object_key] != size:
            raise ValueError("OBJECT_SIZE_CONFLICT")
        objects[object_key] = size
        total += size
    if total > args.max_total_bytes:
        raise ValueError("TOTAL_BYTE_LIMIT")
    normalized = {"schema_version": "1", "items": sorted(items, key=lambda item: (item["source_id"], item["dataset_id"], item["version"], item["relative_path"]))}
    if len(canonical(normalized)) > MAX_MANIFEST_BYTES:
        raise ValueError("METADATA_BYTE_LIMIT")
    return normalized


def external_root(raw: str | None) -> Path:
    if not raw:
        raise ValueError("ROOT_REQUIRED")
    root = Path(raw).expanduser()
    if not root.is_absolute() or ".." in root.parts or not safe_text(str(root), 4096):
        raise ValueError("ROOT_MUST_BE_SAFE_ABSOLUTE_PATH")
    inspect_chain(root)
    # Collapse platform aliases such as a POSIX double-leading slash only after
    # rejecting static symlink components; lexical comparisons alone are unsafe.
    root = root.resolve()
    if root == Path(root.anchor) or root == REPO_ROOT or REPO_ROOT in root.parents or root in REPO_ROOT.parents:
        raise ValueError("ROOT_MUST_BE_SEPARATE_FROM_REPOSITORY")
    return root


def inspect_chain(path: Path) -> None:
    """Validate every existing directory component without creating anything."""
    current = Path(path.absolute().anchor)
    for part in path.absolute().parts[1:]:
        current /= part
        try:
            mode = current.lstat().st_mode
        except FileNotFoundError:
            continue
        if not stat.S_ISDIR(mode):
            raise ValueError("DIRECTORY_SYMLINK_OR_SPECIAL")


def exists(path: Path) -> bool:
    try:
        path.lstat()
        return True
    except FileNotFoundError:
        return False


def initialized(root: Path) -> bool:
    marker = root / ".kfm-local-store.json"
    if not exists(marker):
        return False
    if load_json(marker, 1024) != MARKER:
        raise ValueError("STORE_MARKER_INVALID")
    for lane in LANES:
        check_directory(root / "data" / lane)
    return True


def init_store(root: Path) -> dict:
    if exists(root) and os.name == "posix" and stat.S_IMODE(root.stat().st_mode) & 0o077:
        raise ValueError("ROOT_PERMISSIONS_NOT_PRIVATE")
    if initialized(root):
        return {"outcome": "NOOP", "root": str(root), "lanes": list(LANES)}
    for lane in LANES:
        inspect_chain(root / "data" / lane)
    check_directory(root, create=True)
    # A private top-level POSIX directory prevents accidental sibling-user reads.
    if os.name == "posix" and stat.S_IMODE(root.stat().st_mode) & 0o077:
        raise ValueError("ROOT_PERMISSIONS_NOT_PRIVATE")
    for lane in LANES:
        check_directory(root / "data" / lane, create=True)
    write_new(root / ".kfm-local-store.json", canonical(MARKER))
    return {"outcome": "INITIALIZED", "root": str(root), "lanes": list(LANES)}


def payload_path(root: Path, item: dict) -> Path:
    return root / "data/quarantine" / item["source_id"] / "objects/sha256" / item["sha256"] / "payload"


def run_id(manifest: dict) -> str:
    return "local-" + hashlib.sha256(canonical(manifest)).hexdigest()


def source_items(manifest: dict) -> dict[str, list[dict]]:
    result: dict[str, list[dict]] = {}
    for item in manifest["items"]:
        result.setdefault(item["source_id"], []).append(item)
    return result


def manifest_path(root: Path, source: str, run: str) -> Path:
    return root / "data/quarantine" / source / "runs" / run / "manifest.json"


def receipt_path(root: Path, source: str, run: str) -> Path:
    return root / "data/receipts/ingest/local-upload" / source / run / "ingest-receipt.json"


def full_manifest_path(root: Path, run: str) -> Path:
    return root / "data/receipts/ingest/local-upload" / run / "manifest.json"


def version_path(root: Path, item: dict) -> Path:
    identity = hashlib.sha256(item["relative_path"].encode("utf-8")).hexdigest()
    return root / "data/quarantine" / item["source_id"] / "versions" / item["dataset_id"] / item["version"] / (identity + ".json")


def receipt_digests(items: list[dict]) -> dict[str, str]:
    return {"payload:" + item["sha256"]: "sha256:" + item["sha256"] for item in items}


def receipt_bytes(items: list[dict]) -> int:
    return sum({item["sha256"]: item["size_bytes"] for item in items}.values())


def check_receipt(path: Path, source: str, run: str, items: list[dict]) -> None:
    receipt = load_json(path)
    fields = {"id", "source_id", "run_id", "started_at", "finished_at", "outcome", "bytes_in", "digests"}
    if not isinstance(receipt, dict) or set(receipt) != fields:
        raise ValueError("RECEIPT_INVALID")
    if (receipt["id"] != f"ingest:local-upload:{source}:{run}" or receipt["source_id"] != source or receipt["run_id"] != run or receipt["outcome"] != "SUCCESS" or type(receipt["bytes_in"]) is not int or receipt["bytes_in"] != receipt_bytes(items) or receipt["digests"] != receipt_digests(items)):
        raise ValueError("RECEIPT_INVALID")
    if timestamp(receipt["started_at"]) > timestamp(receipt["finished_at"]):
        raise ValueError("RECEIPT_TIME_INVALID")


def check_snapshots(root: Path, manifest: dict, *, required: bool = False) -> list[str]:
    missing = []
    run = run_id(manifest)
    complete = full_manifest_path(root, run)
    inspect_chain(complete.parent)
    if exists(complete):
        if read_regular(complete, MAX_MANIFEST_BYTES) != canonical(manifest):
            raise ValueError("MANIFEST_SNAPSHOT_CORRUPT")
    else:
        missing.append(str(complete.relative_to(root)))
    for item in manifest["items"]:
        binding = version_path(root, item)
        inspect_chain(binding.parent)
        if exists(binding):
            if read_regular(binding, MAX_MANIFEST_BYTES) != canonical(item):
                raise ValueError("CAPTURE_VERSION_CONFLICT_USE_NEW_VERSION")
        else:
            missing.append(str(binding.relative_to(root)))
    for source, items in source_items(manifest).items():
        snapshot = manifest_path(root, source, run)
        inspect_chain(snapshot.parent)
        if exists(snapshot):
            if read_regular(snapshot, MAX_MANIFEST_BYTES) != canonical({"schema_version": "1", "items": items}):
                raise ValueError("MANIFEST_SNAPSHOT_CORRUPT")
        else:
            missing.append(str(snapshot.relative_to(root)))
        receipt = receipt_path(root, source, run)
        inspect_chain(receipt.parent)
        if exists(receipt):
            check_receipt(receipt, source, run, items)
        else:
            missing.append(str(receipt.relative_to(root)))
    if required and missing:
        raise ValueError("CAPTURE_RECEIPT_OR_SNAPSHOT_MISSING")
    return missing


def downloads_root(raw: str, root: Path) -> Path:
    value = Path(raw).expanduser().absolute()
    if ".." in value.parts:
        raise ValueError("DOWNLOADS_PATH_UNSAFE")
    check_directory(value)
    value = value.resolve()
    if value == root or root in value.parents:
        raise ValueError("DOWNLOADS_MUST_BE_OUTSIDE_STORE")
    return value


def inspect_objects(root: Path, manifest: dict, downloads: Path | None, args: argparse.Namespace) -> list[dict]:
    result = []
    checked: dict[tuple[str, str], bool] = {}
    checked_inputs: set[str] = set()
    for item in manifest["items"]:
        target = payload_path(root, item)
        inspect_chain(target.parent)
        key = (item["source_id"], item["sha256"])
        if key not in checked:
            present = exists(target)
            if present:
                try:
                    digest, size = hash_regular(target, args.max_file_bytes, expected_size=item["size_bytes"])
                except ValueError as error:
                    if str(error) in {"INPUT_SIZE_MISMATCH_OR_LIMIT", "INPUT_CHANGED", "INPUT_BYTE_LIMIT"}:
                        raise ValueError("STORED_PAYLOAD_CORRUPT") from None
                    raise
                if digest != item["sha256"]:
                    raise ValueError("STORED_PAYLOAD_CORRUPT")
            checked[key] = present
        present = checked[key]
        # An already verified local object remains usable after the downloads
        # folder is cleaned. Missing objects always require the declared input.
        if not present and downloads is not None and item["relative_path"] not in checked_inputs:
            source = downloads.joinpath(*item["relative_path"].split("/"))
            digest, size = hash_regular(source, args.max_file_bytes, expected_size=item["size_bytes"])
            if digest != item["sha256"]:
                raise ValueError("INPUT_CHECKSUM_MISMATCH")
            checked_inputs.add(item["relative_path"])
        if downloads is None and not present:
            raise ValueError("STORED_PAYLOAD_MISSING")
        result.append({"source_id": item["source_id"], "dataset_id": item["dataset_id"], "version": item["version"], "relative_path": item["relative_path"], "destination": str(target.relative_to(root)), "size_bytes": item["size_bytes"], "sha256": item["sha256"], "action": "SKIP_VERIFIED" if present else "CAPTURE_QUARANTINE"})
    return result


def disk_budget(root: Path, objects: list[dict], manifest: dict, reserve: int) -> int:
    unique = {item["destination"]: item["size_bytes"] for item in objects if item["action"] == "CAPTURE_QUARANTINE"}
    # Include bounded manifests and per-source receipts, as well as free reserve.
    required = sum(unique.values()) + len(canonical(manifest)) * 3 + len(manifest["items"]) * 1024 + len(source_items(manifest)) * 4096 + reserve
    existing = root
    while not existing.exists():
        existing = existing.parent
    free = shutil.disk_usage(existing).free
    if free < required:
        raise ValueError("DISK_CAPACITY_INSUFFICIENT")
    return required


@contextmanager
def store_lock(root: Path):
    lock = root / ".local-data.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY | getattr(os, "O_NOFOLLOW", 0), 0o600)
    except FileExistsError:
        raise ValueError("STORE_LOCKED") from None
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(canonical({"pid": os.getpid(), "scope": "local-quarantine-sync"}))
            handle.flush()
            os.fsync(handle.fileno())
        yield
    finally:
        lock.unlink()
        fsync_directory(root)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def make_receipt(source: str, run: str, items: list[dict], started: str, outcome: str = "SUCCESS") -> dict:
    return {"id": f"ingest:local-upload:{source}:{run}", "source_id": source, "run_id": run, "started_at": started, "finished_at": utc_now(), "outcome": outcome, "bytes_in": receipt_bytes(items), "digests": receipt_digests(items)}


def sync_store(root: Path, manifest: dict, downloads: Path, args: argparse.Namespace) -> dict:
    if not initialized(root):
        raise ValueError("STORE_NOT_INITIALIZED_RUN_INIT")
    if os.name == "posix" and stat.S_IMODE(root.stat().st_mode) & 0o077:
        raise ValueError("ROOT_PERMISSIONS_NOT_PRIVATE")
    run = run_id(manifest)
    with store_lock(root):
        objects = inspect_objects(root, manifest, downloads, args)
        missing_metadata = check_snapshots(root, manifest)
        disk_budget(root, objects, manifest, args.min_free_bytes)
        started = utc_now()
        verified: dict[str, list[dict]] = {}
        captured, reused = 0, 0
        seen = set()
        try:
            for item in manifest["items"]:
                key = (item["source_id"], item["sha256"])
                if key in seen:
                    continue
                seen.add(key)
                target = payload_path(root, item)
                if exists(target):
                    reused += 1
                else:
                    if shutil.disk_usage(root).free < item["size_bytes"] + args.min_free_bytes:
                        raise ValueError("DISK_CAPACITY_INSUFFICIENT")
                    capture_file(downloads.joinpath(*item["relative_path"].split("/")), target, sha256=item["sha256"], size_bytes=item["size_bytes"], max_bytes=args.max_file_bytes)
                    captured += 1
                verified.setdefault(item["source_id"], []).append(item)
            for source, items in source_items(manifest).items():
                for item in items:
                    binding = version_path(root, item)
                    if not exists(binding):
                        write_new(binding, canonical(item))
                snapshot = manifest_path(root, source, run)
                if not exists(snapshot):
                    write_new(snapshot, canonical({"schema_version": "1", "items": items}))
                receipt = receipt_path(root, source, run)
                if not exists(receipt):
                    write_new(receipt, canonical(make_receipt(source, run, items, started)))
            complete = full_manifest_path(root, run)
            if not exists(complete):
                write_new(complete, canonical(manifest))
            check_snapshots(root, manifest, required=True)
        except (OSError, ValueError):
            # Record only bytes actually verified. A zero-capture failure cannot
            # satisfy IngestReceipt's nonempty digest map and is JSON CLI output
            # only. Attempt receipts never replace the final success receipt.
            for source, items in verified.items():
                attempt = receipt_path(root, source, run).parent / "attempts" / (uuid.uuid4().hex + ".json")
                try:
                    write_new(attempt, canonical(make_receipt(source, run, items, started, "PARTIAL")))
                except (OSError, ValueError):
                    pass
            raise
    return {"outcome": "SYNCED" if captured or missing_metadata else "NOOP", "run_id": run, "captured_objects": captured, "reused_objects": reused, "lifecycle": "QUARANTINE", "items": len(manifest["items"])}


def bounded_int(value: str) -> int:
    result = int(value)
    if result < 0:
        raise argparse.ArgumentTypeError("must be nonnegative")
    return result


def describe_file(args: argparse.Namespace) -> dict:
    """Create a manifest for one explicit file; metadata assertions stay unknown."""
    if not 1 <= args.max_file_bytes <= MAX_FILE_BYTES:
        raise ValueError("LIMIT_CONFIGURATION_INVALID")
    downloads = Path(args.downloads).expanduser().absolute()
    if ".." in downloads.parts:
        raise ValueError("DOWNLOADS_PATH_UNSAFE")
    check_directory(downloads)
    item = {"source_id": args.source_id, "dataset_id": args.dataset_id, "domain": args.domain, "version": args.version, "relative_path": args.file, "source_uri": args.source_uri, "media_type": args.media_type, "rights": {"license_id": None, "redistribution": "unknown"}, "sensitivity": "unknown", "sha256": "1" * 64, "size_bytes": 1, "captured_at": args.captured_at or utc_now()}
    validate_manifest({"schema_version": "1", "items": [item]}, args)
    digest, size = hash_regular(downloads.joinpath(*item["relative_path"].split("/")), args.max_file_bytes)
    item["sha256"], item["size_bytes"] = digest, size
    return validate_manifest({"schema_version": "1", "items": [item]}, args)


def check_limits(args: argparse.Namespace) -> None:
    if not 1 <= args.max_items <= MAX_ITEMS or not 1 <= args.max_file_bytes <= MAX_FILE_BYTES or not 1 <= args.max_total_bytes <= MAX_TOTAL_BYTES:
        raise ValueError("LIMIT_CONFIGURATION_INVALID")


def combine_manifests(args: argparse.Namespace) -> dict:
    """Combine explicit declarations without opening payloads or selecting winners."""
    check_limits(args)
    if not 2 <= len(args.manifest) <= MAX_ITEMS:
        raise ValueError("MANIFEST_INPUT_COUNT_INVALID")
    items = []
    remaining = MAX_MANIFEST_BYTES
    for path in args.manifest:
        if remaining <= 0:
            raise ValueError("METADATA_BYTE_LIMIT")
        content = read_regular(path, remaining)
        remaining -= len(content)
        manifest = validate_manifest(parse_json(content), args)
        if len(items) + len(manifest["items"]) > args.max_items:
            raise ValueError("MANIFEST_ITEM_LIMIT")
        items.extend(manifest["items"])
    return validate_manifest({"schema_version": "1", "items": items}, args)


def comparison_index(manifest: dict) -> dict[tuple[str, str, str], dict]:
    result = {}
    for item in manifest["items"]:
        key = (item["source_id"], item["dataset_id"], item["relative_path"])
        if key in result:
            raise ValueError("AMBIGUOUS_COMPARISON_VERSION")
        result[key] = item
    return result


def compare_manifests(args: argparse.Namespace) -> dict:
    """Compare two declared snapshots; omissions never authorize deletion."""
    check_limits(args)
    previous = validate_manifest(load_json(args.previous), args)
    proposed = validate_manifest(load_json(args.manifest), args)
    before, after = comparison_index(previous), comparison_index(proposed)
    counts = {name: 0 for name in ("added", "omitted", "changed", "unchanged", "version_conflicts")}
    changes = []
    for key in sorted(before.keys() | after.keys()):
        old, new = before.get(key), after.get(key)
        changed_fields = sorted(field for field in ITEM_FIELDS if old[field] != new[field]) if old and new else []
        status = "ADDED" if old is None else "OMITTED" if new is None else "CHANGED" if changed_fields else "UNCHANGED"
        conflict = bool(changed_fields and old["version"] == new["version"])
        payload_changed = any(old[field] != new[field] for field in ("sha256", "size_bytes")) if old and new else None
        counts[status.lower()] += 1
        counts["version_conflicts"] += int(conflict)
        changes.append({"source_id": key[0], "dataset_id": key[1], "relative_path": key[2], "status": status,
                        "previous_version": old["version"] if old else None, "proposed_version": new["version"] if new else None,
                        "changed_fields": changed_fields, "payload_changed": payload_changed, "version_conflict": conflict})
    return {"outcome": "COMPARED", "previous_run_id": run_id(previous), "proposed_run_id": run_id(proposed),
            "counts": counts, "changes": changes, "writes": False, "deletions": False, "byte_verification": False}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="command", required=True)
    for command in ("init", "plan", "sync", "verify"):
        child = commands.add_parser(command)
        child.add_argument("--root", default=os.environ.get("KFM_DATA_ROOT"))
        if command != "init":
            child.add_argument("--manifest", required=True, type=Path)
            child.add_argument("--max-items", type=bounded_int, default=1000)
            child.add_argument("--max-file-bytes", type=bounded_int, default=DEFAULT_FILE_BYTES)
            child.add_argument("--max-total-bytes", type=bounded_int, default=DEFAULT_TOTAL_BYTES)
            child.add_argument("--min-free-bytes", type=bounded_int, default=DEFAULT_FREE_BYTES)
        if command in {"plan", "sync"}:
            child.add_argument("--downloads", required=True)
    describe = commands.add_parser("describe", help="Print a manifest for one named local file; never write or scan a directory.")
    for name in ("downloads", "file", "source-id", "dataset-id", "domain", "version", "source-uri"):
        describe.add_argument("--" + name, required=True)
    describe.add_argument("--media-type", default="application/octet-stream")
    describe.add_argument("--captured-at")
    describe.add_argument("--max-file-bytes", type=bounded_int, default=DEFAULT_FILE_BYTES)
    describe.set_defaults(max_items=MAX_ITEMS, max_total_bytes=MAX_TOTAL_BYTES)
    for command in ("combine", "compare"):
        child = commands.add_parser(command, help="Read explicit manifests only; no payload, store, or network access.")
        if command == "combine":
            child.add_argument("--manifest", required=True, action="append", type=Path)
        else:
            child.add_argument("--previous", required=True, type=Path)
            child.add_argument("--manifest", required=True, type=Path)
        child.add_argument("--max-items", type=bounded_int, default=MAX_ITEMS)
        child.add_argument("--max-file-bytes", type=bounded_int, default=DEFAULT_FILE_BYTES)
        child.add_argument("--max-total-bytes", type=bounded_int, default=DEFAULT_TOTAL_BYTES)
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "describe":
            print(canonical(describe_file(args)).decode("utf-8"), end="")
            return 0
        if args.command == "combine":
            print(canonical(combine_manifests(args)).decode("utf-8"), end="")
            return 0
        if args.command == "compare":
            result = compare_manifests(args)
        else:
            result = run_store_command(args)
    except (OSError, UnicodeError, ValueError, RecursionError) as error:
        code = str(error) if isinstance(error, ValueError) and re.fullmatch(r"[A-Z_]+", str(error)) else "LOCAL_IO_OR_INPUT_ERROR"
        print(json.dumps({"outcome": "DENY", "code": code, "authority": AUTHORITY}, sort_keys=True), file=sys.stderr if args.command in {"describe", "combine", "compare"} else sys.stdout)
        return 1
    result["authority"] = AUTHORITY
    print(json.dumps(result, sort_keys=True))
    return 0


def run_store_command(args: argparse.Namespace) -> dict:
    root = external_root(args.root)
    if args.command == "init":
        result = init_store(root)
    else:
        check_limits(args)
        if not 0 <= args.min_free_bytes <= MAX_TOTAL_BYTES:
            raise ValueError("LIMIT_CONFIGURATION_INVALID")
        manifest = validate_manifest(load_json(args.manifest), args)
        if args.command == "verify":
            if not initialized(root):
                raise ValueError("STORE_NOT_INITIALIZED_RUN_INIT")
            objects = inspect_objects(root, manifest, None, args)
            check_snapshots(root, manifest, required=True)
            result = {"outcome": "VERIFIED", "run_id": run_id(manifest), "items": len(objects), "lifecycle": "QUARANTINE"}
        else:
            downloads = downloads_root(args.downloads, root)
            if args.command == "sync":
                result = sync_store(root, manifest, downloads, args)
            else:
                ready = initialized(root)
                objects = inspect_objects(root, manifest, downloads, args)
                missing = check_snapshots(root, manifest)
                budget = disk_budget(root, objects, manifest, args.min_free_bytes)
                result = {"outcome": "PLANNED", "run_id": run_id(manifest), "store_initialized": ready, "required_free_bytes": budget, "missing_metadata": missing, "objects": objects, "writes": False}
    return result


if __name__ == "__main__":
    raise SystemExit(main())
