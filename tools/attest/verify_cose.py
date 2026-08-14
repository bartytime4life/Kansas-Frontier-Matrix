#!/usr/bin/env python3
"""Verify a KFM PMTiles signature bundle shape.

Cryptographic COSE verification is intentionally dependency-pluggable here.
Until a repository-approved COSE library and key registry are wired in, this tool
fails closed unless --shape-only is explicitly passed for development fixtures.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

SHA256_RE = re.compile(r"^sha256:[a-fA-F0-9]{64}$")
MAX_PMSIG_BYTES = 1024 * 1024


class ShapeValidationError(ValueError):
    """Finite PMSIG shape failure that never reflects untrusted values."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


class _DuplicateKeyError(ValueError):
    pass


class _NonFiniteNumberError(ValueError):
    pass


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> object:
    raise _NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise _NonFiniteNumberError
    return parsed


def _load_pmsig(path: Path) -> dict[str, object]:
    """Load one bounded JSON object without following a declared symlink."""

    try:
        if path.is_symlink():
            raise ShapeValidationError("PMSIG_SYMLINK_DENIED")
        if not path.is_file():
            raise ShapeValidationError("PMSIG_NOT_FILE")
        if path.stat().st_size > MAX_PMSIG_BYTES:
            raise ShapeValidationError("PMSIG_JSON_TOO_LARGE")
        raw = path.read_bytes()
        if len(raw) > MAX_PMSIG_BYTES:
            raise ShapeValidationError("PMSIG_JSON_TOO_LARGE")
        obj = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except ShapeValidationError:
        raise
    except _DuplicateKeyError as exc:
        raise ShapeValidationError("PMSIG_JSON_DUPLICATE_KEY") from exc
    except _NonFiniteNumberError as exc:
        raise ShapeValidationError("PMSIG_JSON_NONFINITE_NUMBER") from exc
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ShapeValidationError("PMSIG_JSON_INVALID") from exc
    except (OSError, RecursionError, ValueError) as exc:
        raise ShapeValidationError("PMSIG_JSON_UNREADABLE") from exc
    if not isinstance(obj, dict):
        raise ShapeValidationError("PMSIG_ROOT_INVALID")
    return obj


def fail(msg: str) -> int:
    print(f"DENY: {msg}", file=sys.stderr)
    return 1


def validate_shape(path: Path) -> None:
    obj = _load_pmsig(path)
    if obj.get("schema_version") != "kfm.pmsig.v1":
        raise ShapeValidationError("PMSIG_SCHEMA_VERSION_INVALID")
    subject = obj.get("subject")
    if not isinstance(subject, dict):
        raise ShapeValidationError("PMSIG_SUBJECT_INVALID")
    for field in ["pmtiles_sha256", "pmidx_merkle_root", "spec_hash"]:
        value = subject.get(field)
        if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
            raise ShapeValidationError("PMSIG_SUBJECT_DIGEST_INVALID")
    if not isinstance(obj.get("key_id"), str) or not obj["key_id"]:
        raise ShapeValidationError("PMSIG_KEY_ID_INVALID")
    if not isinstance(obj.get("signature"), str) or not obj["signature"]:
        raise ShapeValidationError("PMSIG_SIGNATURE_SHAPE_INVALID")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pmsig", nargs="+", type=Path)
    parser.add_argument("--shape-only", action="store_true", help="development only; skips cryptographic verification")
    args = parser.parse_args()

    status = 0
    for path in args.pmsig:
        try:
            validate_shape(path)
            if not args.shape_only:
                raise ShapeValidationError(
                    "PMSIG_CRYPTOGRAPHIC_VERIFICATION_UNWIRED"
                )
            print(f"ALLOW: {path}: signature bundle shape valid [shape-only]")
        except ShapeValidationError as exc:
            status |= fail(f"{path}: {exc.code}")
        except Exception:  # noqa: BLE001
            status |= fail(f"{path}: PMSIG_UNEXPECTED_ERROR")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
