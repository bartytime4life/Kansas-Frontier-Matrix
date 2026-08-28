"""Command-line interface for bounded KFM deterministic content digests."""

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
from .geojson import (
    DEFAULT_COORDINATE_PRECISION,
    GEOJSON_DIGEST_PROFILE,
    GeoJSONDigestError,
    compute_geojson_feature_digests,
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


def _base(status: str, *, scope: str = SCOPE) -> dict[str, object]:
    return {
        "authority": "NONE",
        "canonicalization": CANONICALIZATION_PROFILE,
        "hash_algorithm": HASH_ALGORITHM,
        "non_effects": NON_EFFECTS,
        "scope": scope,
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


def _geojson_feature(
    path: Path,
    *,
    crs: str,
    precision: int,
    excluded_property_keys: Sequence[str],
    include_feature_id: bool,
) -> int:
    scope = "geojson.feature_digests"
    try:
        feature = load_json_file(path)
        digests = compute_geojson_feature_digests(
            feature,
            crs=crs,
            coordinate_precision=precision,
            excluded_property_keys=excluded_property_keys,
            include_feature_id=include_feature_id,
        )
        payload = _base("GEOJSON_FEATURE_DIGESTS_CREATED", scope=scope)
        payload.update(digests.as_dict())
        payload["input"] = str(path)
        _emit(payload)
        return 0
    except JsonInputError:
        payload = _base("JSON_INPUT_INVALID", scope=scope)
    except GeoJSONDigestError:
        payload = _base("GEOJSON_DIGEST_INPUT_INVALID", scope=scope)
    except CanonicalizationFailure:
        payload = _base("CANONICALIZATION_ERROR", scope=scope)
    payload.update(
        {
            "input": str(path),
            "normalization_profile": GEOJSON_DIGEST_PROFILE,
        }
    )
    _emit(payload)
    return 2


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compute or verify deterministic RFC 8785 JCS + SHA-256 content "
            "digests."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    compute_parser = subparsers.add_parser("compute", help="compute a spec hash")
    compute_parser.add_argument("input", type=Path)

    verify_parser = subparsers.add_parser("verify", help="verify a stored spec hash")
    verify_parser.add_argument("input", type=Path)
    verify_parser.add_argument("hash_record", type=Path)

    geojson_parser = subparsers.add_parser(
        "geojson-feature",
        help="compute separate structural geometry and record digests",
    )
    geojson_parser.add_argument("input", type=Path)
    geojson_parser.add_argument(
        "--crs",
        required=True,
        help="declared CRS bound into both digests, for example EPSG:4326",
    )
    geojson_parser.add_argument(
        "--precision",
        type=int,
        default=DEFAULT_COORDINATE_PRECISION,
        help="coordinate decimal places retained before RFC 8785 hashing",
    )
    geojson_parser.add_argument(
        "--exclude-property",
        action="append",
        default=[],
        dest="excluded_property_keys",
        help="top-level property key to exclude; repeat for multiple keys",
    )
    geojson_parser.add_argument(
        "--include-feature-id",
        action="store_true",
        help="bind the optional top-level GeoJSON Feature id into record_sha256",
    )

    args = parser.parse_args(argv)
    if args.command == "compute":
        return _compute(args.input)
    if args.command == "verify":
        return _verify(args.input, args.hash_record)
    if args.command == "geojson-feature":
        return _geojson_feature(
            args.input,
            crs=args.crs,
            precision=args.precision,
            excluded_property_keys=args.excluded_property_keys,
            include_feature_id=args.include_feature_id,
        )
    parser.error("unsupported command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
