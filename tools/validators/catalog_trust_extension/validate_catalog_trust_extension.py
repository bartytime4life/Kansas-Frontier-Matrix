#!/usr/bin/env python3
"""Validate the bounded KFM CatalogTrustExtension payload without network.

A PASS proves only closed shape, exact spec_hash, and the semantic checks in
this module. It does not validate a complete STAC/DCAT/PROV host, resolve a
receipt or proof, create catalog closure, apply policy, approve review,
promote, release, publish, or authorize public use.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = REPO_ROOT / "packages" / "hashing" / "src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))

try:
    from hashing import CanonicalizationFailure, compute_spec_hash
except ImportError as exc:  # pragma: no cover - exercised by hosted environment setup
    raise RuntimeError("repository hashing package is unavailable") from exc

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "data"
    / "catalog_trust_extension.schema.json"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures" / "data" / "catalog_trust_extension"
FIXTURE_MANIFEST = FIXTURE_ROOT / "expected_findings_manifest.json"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
MAX_DOCUMENT_DEPTH = 64
MAX_DOCUMENT_NODES = 4_096
SCOPE = "catalog-trust-extension-payload-only"
SOURCE_ROLES = frozenset(
    {
        "observed",
        "regulatory",
        "modeled",
        "aggregate",
        "administrative",
        "candidate",
        "synthetic",
    }
)
ERROR_CODES = frozenset(
    {
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
        "SCHEMA_UNAVAILABLE",
        "SPEC_HASH_UNAVAILABLE",
    }
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"

    @property
    def error(self) -> bool:
        return self.outcome == "ERROR"


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _structure_is_bounded(value: object) -> bool:
    pending = [(value, 0)]
    visited = 0
    while pending:
        candidate, depth = pending.pop()
        visited += 1
        if visited > MAX_DOCUMENT_NODES or depth > MAX_DOCUMENT_DEPTH:
            return False
        if isinstance(candidate, dict):
            if len(candidate) > MAX_DOCUMENT_NODES - visited:
                return False
            pending.extend((item, depth + 1) for item in candidate.values())
        elif isinstance(candidate, list):
            if len(candidate) > MAX_DOCUMENT_NODES - visited:
                return False
            pending.extend((item, depth + 1) for item in candidate)
    return True


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
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
    if not _structure_is_bounded(value):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1")
        for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        )
        errors = list(
            islice(
                validator.iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        ValueError,
        RecursionError,
    ):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    ordered_errors = sorted(
        errors[:MAX_SCHEMA_FINDINGS],
        key=lambda item: (
            _pointer(item.absolute_path),
            str(item.validator),
            str(item.schema_path),
        ),
    )
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in ordered_errors
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    declared_hash = candidate.get("spec_hash")
    if isinstance(declared_hash, str):
        subject = dict(candidate)
        subject.pop("spec_hash", None)
        try:
            actual_hash = compute_spec_hash(subject)
        except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
            findings.append(Finding("SPEC_HASH_UNAVAILABLE", "/spec_hash"))
        else:
            if declared_hash != actual_hash:
                findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    trust_class = candidate.get("kfm:trust_class")
    proof_ref = candidate.get("kfm:proof_ref")
    if trust_class in {"proof", "publication"} and not isinstance(
        proof_ref, str
    ):
        findings.append(Finding("PROOF_REF_REQUIRED", "/kfm:proof_ref"))

    if (
        candidate.get("kfm:source_role") == "candidate"
        and trust_class == "publication"
    ):
        findings.append(
            Finding(
                "CANDIDATE_PUBLICATION_FORBIDDEN",
                "/kfm:trust_class",
            )
        )

    governance = candidate.get("governance")
    if isinstance(governance, dict):
        authority_fields = (
            "catalog_authorized",
            "promotion_authorized",
            "release_authorized",
            "publication_authorized",
            "public_use_allowed",
        )
        if any(governance.get(field) is not False for field in authority_fields):
            findings.append(
                Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance")
            )

    return findings


def _derive_outcome(findings: Sequence[Finding]) -> str:
    if any(finding.code in ERROR_CODES for finding in findings):
        return "ERROR"
    if findings:
        return "FAIL"
    return "PASS"


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        ordered = tuple(sorted(set(findings)))
        return ValidationResult(_derive_outcome(ordered), ordered)

    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(_derive_outcome(ordered), ordered)


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority_created": False,
            "file": _display_path(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _load_manifest() -> dict[str, Any]:
    try:
        value = json.loads(FIXTURE_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile() -> int:
    manifest = _load_manifest()
    cases = manifest.get("cases")
    if not isinstance(cases, list) or not cases:
        return 1

    passed = True
    seen_paths: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            passed = False
            continue
        relative_path = case.get("path")
        expected_outcome = case.get("expected_outcome")
        expected_findings = case.get("expected_findings")
        if (
            not isinstance(relative_path, str)
            or relative_path in seen_paths
            or not isinstance(expected_outcome, str)
            or not isinstance(expected_findings, list)
        ):
            passed = False
            continue
        seen_paths.add(relative_path)
        path = FIXTURE_ROOT / relative_path
        result = validate_record(path)
        print(_serialize(path, result))
        actual_findings = [
            {"code": finding.code, "field": finding.field}
            for finding in result.findings
        ]
        if (
            result.outcome != expected_outcome
            or actual_findings != expected_findings
        ):
            passed = False
            print(
                json.dumps(
                    {
                        "actual": {
                            "findings": actual_findings,
                            "outcome": result.outcome,
                        },
                        "expected": {
                            "findings": expected_findings,
                            "outcome": expected_outcome,
                        },
                        "file": _display_path(path),
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )

    discovered = {
        path.relative_to(FIXTURE_ROOT).as_posix()
        for directory in ("valid", "invalid")
        for path in (FIXTURE_ROOT / directory).glob("*.json")
    }
    if discovered != seen_paths:
        passed = False
    return 0 if passed else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate CatalogTrustExtension payloads."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        if args.files:
            print(
                "--fixtures cannot be combined with file arguments",
                file=sys.stderr,
            )
            return 2
        return run_fixture_profile()

    if not args.files:
        print("at least one file or --fixtures is required", file=sys.stderr)
        return 2

    exit_code = 0
    for path in args.files:
        result = validate_record(path)
        print(_serialize(path, result))
        if result.outcome == "FAIL":
            exit_code = max(exit_code, 1)
        elif result.outcome == "ERROR":
            exit_code = max(exit_code, 2)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
