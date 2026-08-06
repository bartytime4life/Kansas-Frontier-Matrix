"""Command-line interface for bounded KFM spec-hash computation and comparison."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .core import (
    CANONICALIZATION_PROFILE,
    HASH_ALGORITHM,
    CanonicalizationFailure,
    JsonInputError,
    SpecHashFormatError,
    canonicalize_json,
    compute_spec_hash,
    is_valid_spec_hash,
    load_json_file,
    verify_spec_hash,
)

SCOPE = "common.spec_hash"
NON_EFFECTS = [
    "no_source_admission",
    "no_evidence_resolution",
    "no_policy_evaluation",
    "no_promotion_release_or_publication",
    "no_public_use_authority",
]


def _emit(payload: dict[str, object]) -> None:
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))


def _base(status: str) -> dict[str, object]:
    return {
        "authority": "NONE",
        "canonicalization": CANONICALIZATION_PROFILE,
        "hash_algorithm": HASH_ALGORITHM,
        "non_effects": NON_EFFECTS,
        "scope": SCOPE,
        "status": status,
    }


def _compute(path: Path) -> int:
    try:
        subject = load_json_file(path)
        canonical = canonicalize_json(subject)
        payload = _base("SPEC_HASH_CREATED")
        payload.update(
            {
                "canonical_bytes": len(canonical),
                "input": str(path),
                "spec_hash": compute_spec_hash(subject),
            }
        )
        _emit(payload)
        return 0
    except JsonInputError:
        payload = _base("JSON_INPUT_INVALID")
    except CanonicalizationFailure:
        payload = _base("CANONICALIZATION_ERROR")
    payload["input"] = str(path)
    _emit(payload)
    return 2


def _verify(subject_path: Path, hash_path: Path) -> int:
    try:
        subject = load_json_file(subject_path)
        stored = load_json_file(hash_path)
        if not isinstance(stored, dict) or set(stored) != {"value"}:
            raise SpecHashFormatError("hash record must contain exactly one value field")
        expected = stored.get("value")
        if not is_valid_spec_hash(expected):
            raise SpecHashFormatError("hash record value does not match the current grammar")
        result = verify_spec_hash(subject, expected)
        payload = _base("SPEC_HASH_MATCH" if result.matches else "SPEC_HASH_MISMATCH")
        payload.update(
            {
                "actual": result.actual,
                "expected": result.expected,
                "hash_record": str(hash_path),
                "input": str(subject_path),
            }
        )
        _emit(payload)
        return 0 if result.matches else 1
    except JsonInputError:
        payload = _base("JSON_INPUT_INVALID")
    except CanonicalizationFailure:
        payload = _base("CANONICALIZATION_ERROR")
    except SpecHashFormatError:
        payload = _base("SPEC_HASH_FORMAT_INVALID")
    payload.update({"hash_record": str(hash_path), "input": str(subject_path)})
    _emit(payload)
    return 2


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compute or verify deterministic RFC 8785 JCS + SHA-256 spec hashes."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    compute_parser = subparsers.add_parser("compute", help="compute a spec hash")
    compute_parser.add_argument("input", type=Path)

    verify_parser = subparsers.add_parser("verify", help="verify a stored spec hash")
    verify_parser.add_argument("input", type=Path)
    verify_parser.add_argument("hash_record", type=Path)

    args = parser.parse_args(argv)
    if args.command == "compute":
        return _compute(args.input)
    if args.command == "verify":
        return _verify(args.input, args.hash_record)
    parser.error("unsupported command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
