#!/usr/bin/env python3
"""Verify a KFM PMIDX sidecar against a PMTiles archive."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SHA256_RE = re.compile(r"^sha256:[a-fA-F0-9]{64}$")


def fail(msg: str) -> int:
    print(f"DENY: {msg}", file=sys.stderr)
    return 1


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def merkle_root(leaves: list[str], arity: int) -> str:
    if not leaves:
        return sha256_bytes(b"")
    level = [bytes.fromhex(x.split(":", 1)[1]) for x in leaves]
    while len(level) > 1:
        nxt = []
        for i in range(0, len(level), arity):
            group = level[i:i + arity]
            nxt.append(hashlib.sha256(b"".join(group)).digest())
        level = nxt
    return "sha256:" + level[0].hex()


def validate_hash(name: str, value: object) -> None:
    if not isinstance(value, str) or not SHA256_RE.match(value):
        raise ValueError(f"{name} must be sha256:<64 hex>")


def verify(pmidx_path: Path, pmtiles_path: Path | None) -> int:
    try:
        obj = json.loads(pmidx_path.read_text(encoding="utf-8"))
        if obj.get("schema_version") != "kfm.pmidx.v1":
            raise ValueError("schema_version must be kfm.pmidx.v1")
        validate_hash("spec_hash", obj.get("spec_hash"))
        validate_hash("pmtiles_sha256", obj.get("pmtiles_sha256"))
        merkle = obj.get("merkle")
        if not isinstance(merkle, dict):
            raise ValueError("merkle must be an object")
        arity = int(merkle.get("arity"))
        if arity < 2:
            raise ValueError("merkle.arity must be >= 2")
        validate_hash("merkle.root", merkle.get("root"))
        leaves = merkle.get("leaves")
        if not isinstance(leaves, list):
            raise ValueError("merkle.leaves must be an array")
        for idx, leaf in enumerate(leaves):
            validate_hash(f"merkle.leaves[{idx}]", leaf)
        computed = merkle_root(leaves, arity)
        if computed != merkle["root"]:
            raise ValueError(f"merkle root mismatch: expected {merkle['root']}, computed {computed}")
        if pmtiles_path:
            digest = sha256_file(pmtiles_path)
            if digest != obj["pmtiles_sha256"]:
                raise ValueError(f"pmtiles digest mismatch: expected {obj['pmtiles_sha256']}, computed {digest}")
    except Exception as exc:  # noqa: BLE001
        return fail(f"{pmidx_path}: {exc}")

    print(f"ALLOW: {pmidx_path}: sidecar Merkle commitments verified")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pmidx", type=Path)
    parser.add_argument("--pmtiles", type=Path)
    args = parser.parse_args()
    return verify(args.pmidx, args.pmtiles)


if __name__ == "__main__":
    raise SystemExit(main())
