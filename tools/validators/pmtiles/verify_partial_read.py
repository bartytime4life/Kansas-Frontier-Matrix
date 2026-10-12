#!/usr/bin/env python3
"""Verify captured PMTiles range bytes against the existing PMIDX bundle.

This is a no-network compatibility verifier.  It proves that one declared
range equals a slice of supplied containing-leaf bytes, that the leaf digest
participates in the declared PMIDX Merkle root, and that the existing PMSIG
subject shape names the same archive digest, root, and build specification.

It deliberately does not verify the PMSIG cryptographically, authenticate the
PMIDX range table, recompute the whole-archive digest, adopt Bao/BLAKE3, execute
policy, or authorize release/publication.  Structural success is therefore a
``STRUCTURAL_HOLD``, never a healthy-artifact or publication decision.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from validate_attestation_bundle import _load_json, _signature_subject
from verify_merkle import (
    MAX_CHUNK_BYTES,
    MAX_LEAVES,
    MerkleValidationError,
    _hash_value,
    _integer,
    _load_index,
    _validate_ranges,
    merkle_root,
)

PROFILE = "kfm.pmtiles.partial-read.compat.v1"
MAX_ARCHIVE_BYTES = MAX_CHUNK_BYTES * MAX_LEAVES
CHECKS = (
    "PMIDX_DECLARED_RANGE_BINDING",
    "CAPTURED_RANGE_EQUALS_CONTAINING_LEAF_SLICE",
    "PMIDX_LEAF_SHA256_AND_MERKLE_ROOT",
    "PMSIG_SUBJECT_SHAPE_BINDING",
)
HOLDS = (
    "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
    "RANGE_METADATA_NOT_AUTHENTICATED",
    "BAO_OUTBOARD_PROOF_UNADOPTED",
    "FULL_ARCHIVE_DIGEST_NOT_RECOMPUTED",
    "POLICY_EVALUATION_NOT_RUN",
    "RELEASE_AUTHORIZATION_NOT_EVALUATED",
)


class PartialReadValidationError(ValueError):
    """One finite, non-echoing partial-read finding."""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class PartialReadResult:
    findings: tuple[str, ...]
    offset: int | None = None
    length: int | None = None
    leaf: int | None = None

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def status(self) -> str:
        return "STRUCTURAL_HOLD" if self.ok else "DENY"


def _load_binary(path: Path, *, prefix: str, expected_size: int) -> bytes:
    try:
        if path.is_symlink():
            raise PartialReadValidationError(f"{prefix}_SYMLINK_DENIED")
        if not path.is_file():
            raise PartialReadValidationError(f"{prefix}_NOT_FILE")
        size = path.stat().st_size
        if size != expected_size:
            raise PartialReadValidationError(f"{prefix}_SIZE_MISMATCH")
        if size < 1 or size > MAX_CHUNK_BYTES:
            raise PartialReadValidationError(f"{prefix}_SIZE_INVALID")
        value = path.read_bytes()
    except PartialReadValidationError:
        raise
    except OSError as exc:
        raise PartialReadValidationError(f"{prefix}_UNREADABLE") from exc
    if len(value) != expected_size:
        raise PartialReadValidationError(f"{prefix}_SIZE_MISMATCH")
    return value


def _inspect_partial_read(
    *,
    pmidx_path: Path,
    pmsig_path: Path,
    range_path: Path,
    leaf_path: Path,
    archive_size: int,
    offset: int,
    length: int,
) -> tuple[int, bytes, bytes]:
    try:
        archive_size = _integer(
            archive_size,
            "PARTIAL_ARCHIVE_SIZE_INVALID",
            127,
            MAX_ARCHIVE_BYTES,
        )
        offset = _integer(offset, "PARTIAL_RANGE_OFFSET_INVALID", 0, archive_size)
        length = _integer(length, "PARTIAL_RANGE_LENGTH_INVALID", 1, archive_size)
    except MerkleValidationError as exc:
        raise PartialReadValidationError(exc.code) from exc
    end = offset + length
    if end < offset or end > archive_size:
        raise PartialReadValidationError("PARTIAL_RANGE_OUT_OF_BOUNDS")

    try:
        index = _load_index(pmidx_path)
        if index.get("schema_version") != "kfm.pmidx.v1":
            raise MerkleValidationError("PMIDX_SCHEMA_VERSION_INVALID")
        spec_hash = _hash_value(index.get("spec_hash"), "PMIDX_SPEC_HASH_INVALID")
        archive_digest = _hash_value(
            index.get("pmtiles_sha256"), "PMIDX_ARCHIVE_DIGEST_INVALID"
        )
        merkle = index.get("merkle")
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
        raw_leaves = merkle.get("leaves")
        if (
            not isinstance(raw_leaves, list)
            or not raw_leaves
            or len(raw_leaves) > MAX_LEAVES
        ):
            raise MerkleValidationError("PMIDX_LEAVES_INVALID")
        leaves = [
            _hash_value(item, "PMIDX_LEAF_HASH_INVALID") for item in raw_leaves
        ]
        expected_leaf_count = (archive_size + chunk_bytes - 1) // chunk_bytes
        if len(leaves) != expected_leaf_count:
            raise MerkleValidationError("PMIDX_LEAF_COUNT_MISMATCH")
        if merkle_root(leaves, arity) != claimed_root:
            raise MerkleValidationError("PMIDX_MERKLE_ROOT_MISMATCH")
        _validate_ranges(
            index.get("ranges", []),
            archive_bytes=archive_size,
            chunk_bytes=chunk_bytes,
            leaf_count=len(leaves),
        )
    except MerkleValidationError as exc:
        raise PartialReadValidationError(exc.code) from exc

    declared_ranges = index.get("ranges")
    assert isinstance(declared_ranges, list)
    matching = [
        item
        for item in declared_ranges
        if isinstance(item, dict)
        and item.get("offset") == offset
        and item.get("length") == length
    ]
    if len(matching) != 1:
        raise PartialReadValidationError("PARTIAL_RANGE_NOT_DECLARED")
    leaf = matching[0].get("leaf")
    if isinstance(leaf, bool) or not isinstance(leaf, int):
        raise PartialReadValidationError("PMIDX_RANGE_INVALID")

    leaf_start = leaf * chunk_bytes
    expected_leaf_size = min(chunk_bytes, archive_size - leaf_start)
    range_bytes = _load_binary(
        range_path,
        prefix="PARTIAL_RANGE_BYTES",
        expected_size=length,
    )
    leaf_bytes = _load_binary(
        leaf_path,
        prefix="PARTIAL_LEAF_BYTES",
        expected_size=expected_leaf_size,
    )
    leaf_digest = "sha256:" + hashlib.sha256(leaf_bytes).hexdigest()
    if leaf_digest != leaves[leaf]:
        raise PartialReadValidationError("PARTIAL_LEAF_DIGEST_MISMATCH")
    relative_start = offset - leaf_start
    if range_bytes != leaf_bytes[relative_start:relative_start + length]:
        raise PartialReadValidationError("PARTIAL_RANGE_BYTES_MISMATCH")

    pmsig, load_findings = _load_json(pmsig_path, "PMSIG")
    if load_findings:
        raise PartialReadValidationError(sorted(item.code for item in load_findings)[0])
    assert pmsig is not None
    signature, signature_findings = _signature_subject(pmsig)
    if signature_findings:
        raise PartialReadValidationError(
            sorted(item.code for item in signature_findings)[0]
        )
    assert signature is not None
    if signature.pmtiles_sha256 != archive_digest:
        raise PartialReadValidationError("PMSIG_ARCHIVE_DIGEST_MISMATCH")
    if signature.pmidx_merkle_root != claimed_root:
        raise PartialReadValidationError("PMSIG_MERKLE_ROOT_MISMATCH")
    if signature.spec_hash != spec_hash:
        raise PartialReadValidationError("PMSIG_SPEC_HASH_MISMATCH")
    return leaf, range_bytes, leaf_bytes


def verify_partial_read(
    *,
    pmidx_path: Path,
    pmsig_path: Path,
    range_path: Path,
    leaf_path: Path,
    archive_size: int,
    offset: int,
    length: int,
) -> PartialReadResult:
    """Return one bounded structural result without echoing supplied bytes."""

    try:
        leaf, _, _ = _inspect_partial_read(
            pmidx_path=pmidx_path,
            pmsig_path=pmsig_path,
            range_path=range_path,
            leaf_path=leaf_path,
            archive_size=archive_size,
            offset=offset,
            length=length,
        )
    except PartialReadValidationError as exc:
        return PartialReadResult(findings=(exc.code,))
    return PartialReadResult(
        findings=(),
        offset=offset,
        length=length,
        leaf=leaf,
    )


def render_result(result: PartialReadResult) -> str:
    payload: dict[str, object] = {
        "profile": PROFILE,
        "status": result.status,
        "authority": "NONE",
        "checks": list(CHECKS),
        "holds": list(HOLDS),
        "findings": list(result.findings),
        "verified_range": None,
    }
    if result.ok:
        payload["verified_range"] = {
            "offset": result.offset,
            "length": result.length,
            "leaf": result.leaf,
        }
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pmidx", type=Path, required=True)
    parser.add_argument("--pmsig", type=Path, required=True)
    parser.add_argument("--range-bytes", type=Path, required=True)
    parser.add_argument("--leaf-bytes", type=Path, required=True)
    parser.add_argument("--archive-size", type=int, required=True)
    parser.add_argument("--offset", type=int, required=True)
    parser.add_argument("--length", type=int, required=True)
    args = parser.parse_args(argv)
    result = verify_partial_read(
        pmidx_path=args.pmidx,
        pmsig_path=args.pmsig,
        range_path=args.range_bytes,
        leaf_path=args.leaf_bytes,
        archive_size=args.archive_size,
        offset=args.offset,
        length=args.length,
    )
    sys.stdout.write(render_result(result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
