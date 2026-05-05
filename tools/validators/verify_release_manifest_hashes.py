#!/usr/bin/env python3
"""Verify release_manifest.artifacts[].sha256 against local files."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

SHA256_RE = re.compile(r"^[a-fA-F0-9]{64}$")

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", nargs="?", default="artifacts/release_manifest.json")
    args = parser.parse_args()
    manifest_path = Path(args.manifest)
    if not manifest_path.is_file():
        return fail(f"missing release manifest: {manifest_path}")

    try:
        manifest: dict[str, Any] = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail(f"invalid release manifest JSON: {exc}")

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        return fail("release_manifest.artifacts must be a non-empty array")

    for idx, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            return fail(f"release_manifest.artifacts[{idx}] must be an object")
        path_value = artifact.get("path")
        expected = artifact.get("sha256")
        if not isinstance(path_value, str) or not path_value:
            return fail(f"release_manifest.artifacts[{idx}].path must be a non-empty string")
        if not isinstance(expected, str) or not SHA256_RE.match(expected):
            return fail(f"release_manifest.artifacts[{idx}].sha256 must be a sha256 hex digest")
        file_path = Path(path_value)
        if not file_path.is_file():
            return fail(f"release artifact missing or not a file: {file_path}")
        actual = sha256_file(file_path)
        if actual.lower() != expected.lower():
            return fail(f"sha256 mismatch for {file_path}: expected {expected}, actual {actual}")

    print(f"release manifest hashes OK: {len(artifacts)} artifact(s)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
