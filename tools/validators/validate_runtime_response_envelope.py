#!/usr/bin/env python3
"""Validate RuntimeResponseEnvelope shape and precision-disclosure semantics.

A green result proves only the bounded local contract checks represented here.
It does not resolve EvidenceRefs, evaluate policy, authenticate review, establish
release state, authorize an answer, or publish.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/contracts/v1/runtime/runtime_response_envelope"
MAX_JSON_BYTES = 256 * 1024

sys.path.insert(0, str(REPO_ROOT))
from tools.validators._common.local_resolver import build_registry  # noqa: E402


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _constant(value: str) -> object:
    raise NonFiniteNumberError(value)


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError(value)
    return parsed


def _load(path: Path) -> tuple[Mapping[str, object] | None, str | None]:
    try:
        if path.is_symlink():
            return None, "INPUT_SYMLINK_DENIED"
        if not path.is_file():
            return None, "FILE_NOT_FOUND"
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, "FILE_TOO_LARGE"
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_constant,
            parse_float=_float,
        )
    except DuplicateKeyError:
        return None, "JSON_DUPLICATE_KEY"
    except NonFiniteNumberError:
        return None, "JSON_NONFINITE_NUMBER"
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None, "JSON_INVALID"
    except OSError:
        return None, "FILE_READ_ERROR"
    if not isinstance(value, dict):
        return None, "ROOT_NOT_OBJECT"
    return value, None


def _canonical_ref(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def semantic_findings(value: Mapping[str, object]) -> list[str]:
    findings: list[str] = []
    if value.get("outcome") != "ANSWER":
        return findings
    precision = value.get("precision_actually_used")
    if not isinstance(precision, dict):
        return findings  # schema reports the missing or malformed object
    top_refs = value.get("evidence_refs")
    precision_refs = precision.get("evidence_refs")
    if isinstance(top_refs, list) and isinstance(precision_refs, list):
        top = {_canonical_ref(item) for item in top_refs}
        if any(_canonical_ref(item) not in top for item in precision_refs):
            findings.append("PRECISION_EVIDENCE_NOT_TOP_LEVEL")
    spatial = precision.get("spatial")
    receipts = precision.get("transform_receipt_refs")
    if (
        isinstance(spatial, dict)
        and spatial.get("generalization_applied") is True
        and isinstance(receipts, list)
        and not receipts
    ):
        findings.append("GENERALIZATION_RECEIPT_REQUIRED")
    temporal = precision.get("temporal")
    if isinstance(temporal, dict):
        interval = temporal.get("observation_interval")
        if isinstance(interval, dict):
            start, end = interval.get("start"), interval.get("end")
            if isinstance(start, str) and isinstance(end, str):
                try:
                    start_instant = datetime.fromisoformat(start.replace("Z", "+00:00"))
                    end_instant = datetime.fromisoformat(end.replace("Z", "+00:00"))
                except ValueError:
                    pass  # The schema format checker reports malformed date-times.
                else:
                    if start_instant > end_instant:
                        findings.append("PRECISION_INTERVAL_INVERTED")
    return sorted(set(findings))


def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return Draft202012Validator(
        schema,
        registry=build_registry(REPO_ROOT),
        format_checker=FormatChecker(),
    )


def validate_path(path: Path, validator: Draft202012Validator) -> list[str]:
    value, load_error = _load(path)
    if load_error:
        return [load_error]
    assert value is not None
    errors = sorted(validator.iter_errors(value), key=lambda item: (list(item.path), item.message))
    if errors:
        return ["SCHEMA_INVALID"]
    return semantic_findings(value)


def _fixture_paths(root: Path) -> tuple[list[Path], list[Path]]:
    return sorted((root / "valid").glob("*.json")), sorted((root / "invalid").glob("*.json"))


def _run_files(paths: Iterable[Path], validator: Draft202012Validator) -> int:
    ok = True
    for path in paths:
        findings = validate_path(path, validator)
        if findings:
            print(f"FAIL {path}: {findings[0]}")
            ok = False
        else:
            print(f"OK {path}")
    return 0 if ok else 1


def _run_fixtures(validator: Draft202012Validator) -> int:
    valid, invalid = _fixture_paths(FIXTURES_ROOT)
    if not valid or not invalid:
        print("FAIL fixtur configuration: valid and invalid JSON lanes are required")
        return 1
    ok = True
    for path in valid:
        findings = validate_path(path, validator)
        if findings:
            print(f"FAIL  {path}: {findings[0]}")
            ok = False
        else:
            print(f"OK {path}")
    for path in invalid:
        findings = validate_path(path, validator)
        if findings:
            print(f"EXPECTED_FAIL {path}: {findings[0]}")
        else:
            print(f"FAIL {path}: expected rejection")
            ok = False
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if not args.fixtures and not args.files:
        print("No files provided", file=sys.stderr)
        return 2
    try:
        validator = _validator()
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR validator configuration: {type(exc).__name__}", file=sys.stderr)
        return 2
    if args.fixtures:
        return _run_fixtures(validator)
    return _run_files(args.files, validator)


if __name__ == "__main__":
    raise SystemExit(main())
