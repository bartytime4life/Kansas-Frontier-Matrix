#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from jsonschema import Draft202012Validator


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate HUC12⇄COMID manifest")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--crosswalk-root")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_iso8601(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def resolve_crosswalk_path(crosswalk: str, root: Path | None) -> Path | None:
    parsed = urlparse(crosswalk)
    if parsed.scheme in {"", "file"}:
        candidate = Path(parsed.path if parsed.scheme == "file" else crosswalk)
        if candidate.exists():
            return candidate
        if root:
            rooted = (root / candidate).resolve()
            if rooted.exists():
                return rooted
    return None


def sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return f"sha256:{hasher.hexdigest()}"


def build_ids(manifest: dict[str, Any]) -> tuple[str, str]:
    manifest_id = f"huc12@{manifest['snapshot_id']}::{manifest['spec_hash']}"
    start = parse_iso8601(manifest["valid_from"]).strftime("%Y%m%d")
    end = parse_iso8601(manifest["valid_to"]).strftime("%Y%m%d")
    timeslice_id = f"huc12::{manifest['snapshot_id']}::{start}-{end}"
    return manifest_id, timeslice_id


def validate(manifest_path: Path, schema_path: Path, crosswalk_root: Path | None) -> dict[str, Any]:
    errors: list[str] = []
    manifest = load_json(manifest_path)
    schema = load_json(schema_path)

    for err in sorted(Draft202012Validator(schema).iter_errors(manifest), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in err.path) or "<root>"
        errors.append(f"schema:{loc}:{err.message}")

    if "valid_from" in manifest and "valid_to" in manifest:
        try:
            if parse_iso8601(manifest["valid_from"]) > parse_iso8601(manifest["valid_to"]):
                errors.append("validity:valid_from must be <= valid_to")
        except ValueError as exc:
            errors.append(f"validity:invalid datetime format: {exc}")

    if "comid_crosswalk" in manifest and "crosswalk_digest" in manifest:
        resolved = resolve_crosswalk_path(manifest["comid_crosswalk"], crosswalk_root)
        if resolved:
            observed = sha256_file(resolved)
            if observed != manifest["crosswalk_digest"]:
                errors.append(
                    f"crosswalk_digest:mismatch expected={manifest['crosswalk_digest']} observed={observed}"
                )

    manifest_id = ""
    timeslice_id = ""
    required = {"snapshot_id", "spec_hash", "valid_from", "valid_to"}
    if required.issubset(set(manifest.keys())):
        try:
            manifest_id, timeslice_id = build_ids(manifest)
        except ValueError as exc:
            errors.append(f"ids:unable to construct IDs: {exc}")

    return {
        "ok": len(errors) == 0,
        "errors": errors,
        "manifest_id": manifest_id,
        "timeslice_id": timeslice_id,
    }


def main() -> int:
    args = parse_args()
    result = validate(Path(args.manifest), Path(args.schema), Path(args.crosswalk_root) if args.crosswalk_root else None)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
