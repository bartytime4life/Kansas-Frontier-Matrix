#!/usr/bin/env python3
"""Verify a KFM PMIDX sidecar against the bytes of a PMTiles archive."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path

MAX_JSON_BYTES = 16 * 1024 * 1024
MAX_CHUNK_BYTES = 64 * 1024 * 1024
MAX_LEAVES = 100_000
SHA256_RE = re.compile(r"^sha256:[a-f0-9]{64}$")


class MerkleValidationError(ValueError):
    """A finite, non-echoing PMIDX finding."""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


class _DuplicateKeyError(ValueError):
    pass


class _NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True)
class MerkleInspection:
    spec_hash: str
    pmtiles_sha256: str
    merkle_root: str
    chunk_bytes: int
    leaf_count: int
    range_count: int


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise _DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise _NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise _NonFiniteNumberError
    return parsed


def _load_index(path: Path) -> dict[str, object]:
    try:
        if path.is_symlink():
            raise MerkleValidationError("PMIDX_SYMLINK_DENIED")
        if not path.is_file():
            raise MerkleValidationError("PMIDX_NOT_FILE")
        if path.stat().st_size > MAX_JSON_BYTES:
            raise MerkleValidationError("PMIDX_JSON_TOO_LARGE")
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except MerkleValidationError:
        raise
    except _DuplicateKeyError as exc:
        raise MerkleValidationError("PMIDX_JSON_DUPLICATE_KEY") from exc
    except _NonFiniteNumberError as exc:
        raise MerkleValidationError("PMIDX_JSON_NONFINITE_NUMBER") from exc
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise MerkleValidationError("PMIDX_JSON_INVALID") from exc
    except (OSError, RecursionError, ValueError) as exc:
        raise MerkleValidationError("PMIDX_JSON_UNREADABLE") from exc
    if not isinstance(value, dict):
        raise MerkleValidationError("PMIDX_ROOT_INVALID")
    return value


def _sha256(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def _hash_value(value: object, code: str) -> str:
    if not isinstance(value, str):
        raise MerkleValidationError(code)
    normalized = value.lower()
    if not SHA256_RE.fullmatch(normalized):
        raise MerkleValidationError(code)
    return normalized


def _integer(value: object, code: str, minimum: int, maximum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise MerkleValidationError(code)
    if not minimum <= value <= maximum:
        raise MerkleValidationError(code)
    return value


def merkle_root(leaves: list[str], arity: int) -> str:
    """Recompute the existing PMIDX v1 raw-digest concatenation tree."""

    if not leaves:
        return _sha256(b"")
    level = [bytes.fromhex(item.removeprefix("sha256:")) for item in leaves]
    while len(level) > 1:
        level = [
            hashlib.sha256(b"".join(level[index:index + arity])).digest()
            for index in range(0, len(level), arity)
        ]
    return "sha256:" + level[0].hex()


def _archive_commitments(path: Path, chunk_bytes: int) -> tuple[str, list[str], int]:
    try:
        if path.is_symlink():
            raise MerkleValidationError("PMTILES_SYMLINK_DENIED")
        if not path.is_file():
            raise MerkleValidationError("PMTILES_NOT_FILE")
        archive_bytes = path.stat().st_size
        if archive_bytes < 127:
            raise MerkleValidationError("PMTILES_TOO_SMALL")
        expected_leaves = (archive_bytes + chunk_bytes - 1) // chunk_bytes
        if expected_leaves > MAX_LEAVES:
            raise MerkleValidationError("PMIDX_LEAF_LIMIT_EXCEEDED")
        digest = hashlib.sha256()
        leaves: list[str] = []
        with path.open("rb") as stream:
            while True:
                chunk = stream.read(chunk_bytes)
                if not chunk:
                    break
                if len(leaves) >= MAX_LEAVES:
                    raise MerkleValidationError("PMIDX_LEAF_LIMIT_EXCEEDED")
                digest.update(chunk)
                leaves.append(_sha256(chunk))
    except MerkleValidationError:
        raise
    except OSError as exc:
        raise MerkleValidationError("PMTILES_UNREADABLE") from exc
    return "sha256:" + digest.hexdigest(), leaves, archive_bytes


def _validate_ranges(
    value: object,
    *,
    archive_bytes: int,
    chunk_bytes: int,
    leaf_count: int,
) -> int:
    if not isinstance(value, list):
        raise MerkleValidationError("PMIDX_RANGES_INVALID")
    if len(value) > MAX_LEAVES:
        raise MerkleValidationError("PMIDX_RANGE_LIMIT_EXCEEDED")
    previous_end = 0
    for item in value:
        if not isinstance(item, dict):
            raise MerkleValidationError("PMIDX_RANGE_INVALID")
        offset = _integer(item.get("offset"), "PMIDX_RANGE_INVALID", 0, archive_bytes)
        length = _integer(item.get("length"), "PMIDX_RANGE_INVALID", 1, archive_bytes)
        leaf = _integer(item.get("leaf"), "PMIDX_RANGE_INVALID", 0, MAX_LEAVES)
        end = offset + length
        if end < offset or end > archive_bytes:
            raise MerkleValidationError("PMIDX_RANGE_OUT_OF_BOUNDS")
        if offset < previous_end:
            raise MerkleValidationError("PMIDX_RANGE_ORDER_INVALID")
        expected_first = offset // chunk_bytes
        expected_last = (end - 1) // chunk_bytes
        if expected_first != expected_last or leaf != expected_first or leaf >= leaf_count:
            raise MerkleValidationError("PMIDX_RANGE_LEAF_BINDING_INVALID")
        previous_end = end
    return len(value)


def inspect_index(pmidx_path: Path, pmtiles_path: Path) -> MerkleInspection:
    """Bind PMIDX commitments to archive bytes or raise a finite finding."""

    obj = _load_index(pmidx_path)
    if obj.get("schema_version") != "kfm.pmidx.v1":
        raise MerkleValidationError("PMIDX_SCHEMA_VERSION_INVALID")
    spec_hash = _hash_value(obj.get("spec_hash"), "PMIDX_SPEC_HASH_INVALID")
    claimed_archive = _hash_value(
        obj.get("pmtiles_sha256"), "PMIDX_ARCHIVE_DIGEST_INVALID"
    )
    merkle = obj.get("merkle")
    if not isinstance(merkle, dict):
        raise MerkleValidationError("PMIDX_MERKLE_INVALID")
    arity = _integer(merkle.get("arity"), "PMIDX_ARITY_INVALID", 2, 64)
    chunk_bytes = _integer(
        merkle.get("chunk_bytes"),
        "PMIDX_CHUNK_BYTES_INVALID",
        1,
        MAX_CHUNK_BYTES,
    )
    claimed_root = _hash_value(merkle.get("root"), "PMIDX_ROOT_HASH_INVALID")
    claimed_leaves = merkle.get("leaves")
    if not isinstance(claimed_leaves, list) or len(claimed_leaves) > MAX_LEAVES:
        raise MerkleValidationError("PMIDX_LEAVES_INVALID")
    leaves = [
        _hash_value(item, "PMIDX_LEAF_HASH_INVALID") for item in claimed_leaves
    ]

    archive_digest, computed_leaves, archive_bytes = _archive_commitments(
        pmtiles_path, chunk_bytes
    )
    if claimed_archive != archive_digest:
        raise MerkleValidationError("PMIDX_ARCHIVE_DIGEST_MISMATCH")
    if len(leaves) != len(computed_leaves):
        raise MerkleValidationError("PMIDX_LEAF_COUNT_MISMATCH")
    if leaves != computed_leaves:
        raise MerkleValidationError("PMIDX_LEAF_DIGEST_MISMATCH")
    if merkle_root(leaves, arity) != claimed_root:
        raise MerkleValidationError("PMIDX_MERKLE_ROOT_MISMATCH")

    range_count = _validate_ranges(
        obj.get("ranges", []),
        archive_bytes=archive_bytes,
        chunk_bytes=chunk_bytes,
        leaf_count=len(leaves),
    )
    return MerkleInspection(
        spec_hash=spec_hash,
        pmtiles_sha256=archive_digest,
        merkle_root=claimed_root,
        chunk_bytes=chunk_bytes,
        leaf_count=len(leaves),
        range_count=range_count,
    )


def verify(pmidx_path: Path, pmtiles_path: Path | None) -> int:
    if pmtiles_path is None:
        print("DENY: code=PMTILES_REQUIRED", file=sys.stderr)
        return 1
    try:
        inspect_index(pmidx_path, pmtiles_path)
    except MerkleValidationError as exc:
        print(f"DENY: code={exc.code}", file=sys.stderr)
        return 1
    print("STRUCTURAL_PASS: PMIDX commitments bind to archive bytes")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pmidx", type=Path)
    parser.add_argument("--pmtiles", type=Path, required=True)
    args = parser.parse_args()
    return verify(args.pmidx, args.pmtiles)


if __name__ == "__main__":
    raise SystemExit(main())
