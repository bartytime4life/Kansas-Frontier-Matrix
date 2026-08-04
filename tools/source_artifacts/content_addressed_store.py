"""Fixture/reference content-addressed store for validated SourceArtifact bytes.

This helper is local and no-network. It does not define production storage,
retention, legal hold, lifecycle promotion, release, or public delivery.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators.validate_source_artifact import validate_artifact


def _load_metadata(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("metadata root must be an object")
    return value


def _digest_hex(metadata: dict[str, object]) -> str:
    value = metadata.get("content_digest")
    if not isinstance(value, str) or not value.startswith("sha256:") or len(value) != 71:
        raise ValueError("metadata content_digest is not a sha256 identity")
    return value.removeprefix("sha256:")


def object_path(store_root: Path, metadata: dict[str, object]) -> Path:
    digest = _digest_hex(metadata)
    return store_root / "sha256" / digest[:2] / digest[2:4] / f"{digest}.blob"


def _ensure_safe_root(store_root: Path) -> None:
    store_root.mkdir(parents=True, exist_ok=True)
    current = Path(store_root.absolute().anchor)
    for part in store_root.absolute().parts[1:]:
        current /= part
        if current.is_symlink():
            raise ValueError("store root contains a symlink component")
        if current.exists() and not current.is_dir():
            raise ValueError("store root must contain directories only")


def store(metadata_path: Path, payload_path: Path, store_root: Path) -> Path:
    result = validate_artifact(metadata_path, payload_path)
    if not result.ok:
        raise ValueError("metadata/payload pair failed SourceArtifact validation")
    metadata = _load_metadata(metadata_path)
    _ensure_safe_root(store_root)
    destination = object_path(store_root, metadata)
    destination.parent.mkdir(parents=True, exist_ok=True)
    for parent in (destination.parent, destination.parent.parent):
        if parent.is_symlink():
            raise ValueError("store shard contains a symlink")
    payload = payload_path.read_bytes()
    if destination.exists():
        if not destination.is_file() or destination.is_symlink():
            raise ValueError("existing object path is unsafe")
        if destination.read_bytes() != payload:
            raise ValueError("existing object bytes do not match digest identity")
        return destination
    temporary = destination.with_suffix(f".tmp-{os.getpid()}")
    try:
        with temporary.open("xb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        if temporary.exists():
            temporary.unlink()
    return destination


def verify(metadata_path: Path, store_root: Path) -> Path:
    metadata = _load_metadata(metadata_path)
    destination = object_path(store_root, metadata)
    if not destination.is_file() or destination.is_symlink():
        raise ValueError("content-addressed object is missing or unsafe")
    payload = destination.read_bytes()
    expected = metadata["content_digest"]
    actual = "sha256:" + hashlib.sha256(payload).hexdigest()
    if actual != expected or len(payload) != metadata.get("byte_length"):
        raise ValueError("stored bytes do not match SourceArtifact identity")
    return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Store or verify validated SourceArtifact bytes locally.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    store_parser = subparsers.add_parser("store")
    store_parser.add_argument("metadata", type=Path)
    store_parser.add_argument("payload", type=Path)
    store_parser.add_argument("store_root", type=Path)
    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("metadata", type=Path)
    verify_parser.add_argument("store_root", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "store":
            path = store(args.metadata, args.payload, args.store_root)
        else:
            path = verify(args.metadata, args.store_root)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"outcome": "FAIL", "reason": str(exc)}, sort_keys=True, separators=(",", ":")))
        return 1
    print(json.dumps({"object_path": path.as_posix(), "outcome": "PASS", "scope": "fixture-reference-store-only"}, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
