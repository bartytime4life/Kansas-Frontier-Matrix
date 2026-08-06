#!/usr/bin/env python3
"""Reject secret-like and notification-address values in occurrence queries.

This validator is a narrow companion gate for the canonical fixture-only
OccurrenceRetrievalSnapshotCandidate profile. It does not define a new object
family or replace the canonical occurrence retrieval validator. A passing
result proves only that reviewed synthetic query predicate fields and values do
not contain the bounded email or secret-marker patterns checked here.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures/contracts/v1/source/occurrence_retrieval_snapshot/query_safety"
)
MAX_FILE_BYTES = 1_048_576
SCOPE = "source.occurrence_retrieval_query_safety"

EMAIL_RE = re.compile(
    r"(?i)(?<![A-Z0-9._%+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![A-Z0-9._%+-])"
)
SECRET_RE = re.compile(
    r"(?i)(?:^|[^a-z0-9])(?:password|passwd|secret|api[_-]?key|"
    r"access[_-]?token|refresh[_-]?token|authorization|bearer)(?:$|[^a-z0-9])"
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when non-standard NaN or infinity input is observed."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(
            item.code
            in {
                "FILE_NOT_FOUND",
                "FILE_READ_ERROR",
                "FILE_TOO_LARGE",
                "INPUT_SYMLINK_DENIED",
                "JSON_COMPLEXITY_LIMIT",
                "JSON_DUPLICATE_KEY",
                "JSON_INVALID",
                "JSON_NONFINITE_NUMBER",
                "JSON_NOT_UTF8",
                "ROOT_NOT_OBJECT",
                "QUERY_SAFETY_SHAPE_INVALID",
            }
            for item in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _load_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]

    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _strings(value: Any, path: str) -> Iterable[tuple[str, str]]:
    if isinstance(value, str):
        yield value, path
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _strings(item, f"{path}/{index}")
    elif isinstance(value, dict):
        for key in sorted(value):
            yield from _strings(value[key], f"{path}/{key}")


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    query = candidate.get("query_snapshot")
    if (
        candidate.get("object_type") != "OccurrenceRetrievalSnapshotCandidate"
        or not isinstance(query, dict)
        or not isinstance(query.get("predicates"), list)
    ):
        return [Finding("QUERY_SAFETY_SHAPE_INVALID", "/query_snapshot")]

    findings: set[Finding] = set()
    predicates = query["predicates"]
    for index, predicate in enumerate(predicates):
        if not isinstance(predicate, dict):
            findings.add(
                Finding(
                    "QUERY_SAFETY_SHAPE_INVALID",
                    f"/query_snapshot/predicates/{index}",
                )
            )
            continue
        field = predicate.get("field")
        if isinstance(field, str) and SECRET_RE.search(field):
            findings.add(
                Finding(
                    "OCCURRENCE_RETRIEVAL_QUERY_SECRET_VALUE_DENIED",
                    f"/query_snapshot/predicates/{index}/field",
                )
            )
        for text, path in _strings(
            predicate.get("value"),
            f"/query_snapshot/predicates/{index}/value",
        ):
            if EMAIL_RE.search(text):
                findings.add(
                    Finding(
                        "OCCURRENCE_RETRIEVAL_QUERY_EMAIL_VALUE_DENIED",
                        path,
                    )
                )
            if SECRET_RE.search(text):
                findings.add(
                    Finding(
                        "OCCURRENCE_RETRIEVAL_QUERY_SECRET_VALUE_DENIED",
                        path,
                    )
                )
    return sorted(findings)


def validate_query_safety(path: Path) -> ValidationResult:
    candidate, findings = _load_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display_path(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def validate_fixtures() -> bool:
    valid_paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
    invalid_root = FIXTURE_ROOT / "semantic_invalid"
    invalid_paths = sorted(invalid_root.glob("semantic_invalid_*.json"))
    try:
        manifest = json.loads(
            (invalid_root / "expected_findings_manifest.json").read_text(
                encoding="utf-8"
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        print(
            json.dumps(
                {"code": "FIXTURE_MANIFEST_INVALID", "outcome": "ERROR"},
                separators=(",", ":"),
            )
        )
        return False

    ok = bool(
        valid_paths
        and invalid_paths
        and isinstance(manifest, dict)
        and set(manifest) == {path.name for path in invalid_paths}
    )
    for path in valid_paths:
        result = validate_query_safety(path)
        print(_serialize(path, result))
        if not result.ok:
            ok = False
    for path in invalid_paths:
        result = validate_query_safety(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(manifest.get(path.name, [])) if isinstance(manifest, dict) else []
        if result.ok or actual != expected:
            ok = False
    if not ok:
        print(
            json.dumps(
                {"code": "FIXTURE_POLARITY_ERROR", "outcome": "ERROR"},
                separators=(",", ":"),
            )
        )
    return ok


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            print(
                json.dumps(
                    {"code": "ARGUMENT_CONFLICT", "outcome": "ERROR"},
                    separators=(",", ":"),
                )
            )
            return 2
        return 0 if validate_fixtures() else 1
    if args.path is None:
        print(
            json.dumps(
                {"code": "INPUT_REQUIRED", "outcome": "ERROR"},
                separators=(",", ":"),
            )
        )
        return 2
    result = validate_query_safety(args.path)
    print(_serialize(args.path, result))
    if result.ok:
        return 0
    return 2 if result.error else 1


if __name__ == "__main__":
    raise SystemExit(main())
