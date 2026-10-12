#!/usr/bin/env python3
"""Fail-closed validator for narrow runtime-verification receipts and proofs.

The validator is deterministic and no-network. A PASS proves bounded local shape
and semantic consistency only. It does not establish source authority, evidence
closure, policy approval, reviewer identity, release, deployment, or publication.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_ROOT = REPO_ROOT / "schemas/contracts/v1/runtime/runtime_verification"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/runtime/runtime_verification"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "runtime-verification-receipt-proof-shape-and-local-semantics-only"
OUTCOMES = {"VERIFIED", "MISMATCH", "MISSING_DECLARATION", "INTERRUPTED", "ERROR"}
PROGRESS_FIELDS = {"bytes_processed", "checkpoint_index", "partial_digest", "status", "prior_receipt_ref"}


class DuplicateKeyError(ValueError):
    """JSON object repeated a member name."""


class NonFiniteNumberError(ValueError):
    """JSON used NaN or an infinite number."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    kind: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


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


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_resources() -> tuple[Registry, dict[str, Mapping[str, Any]]]:
    resources: dict[str, Resource] = {}
    schemas: dict[str, Mapping[str, Any]] = {}
    for path in sorted(SCHEMA_ROOT.glob("*.schema.json")):
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        schema_id = schema.get("$id")
        if not isinstance(schema_id, str) or not schema_id:
            raise ValueError("schema id missing")
        if schema_id in resources:
            raise ValueError("duplicate schema id")
        resources[schema_id] = Resource.from_contents(schema)
        schemas[path.stem.replace(".schema", "")] = schema
    return Registry().with_resources(resources.items()), schemas


def _schema_findings(kind: str, candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        registry, schemas = _schema_resources()
        schema = schemas[kind]
        validator = Draft202012Validator(
            schema,
            registry=registry,
            format_checker=FormatChecker(),
        )
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (KeyError, OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _kind(candidate: Mapping[str, Any]) -> str:
    object_type = candidate.get("object_type")
    if object_type == "RuntimeVerificationReceipt":
        return "receipt"
    if object_type == "RuntimeVerificationProof":
        return "proof"
    return "unknown"


def _digest_bytes(value: Any) -> bytes | None:
    if not isinstance(value, dict):
        return None
    if value.get("algorithm") != "sha256":
        return None
    encoding = value.get("encoding")
    encoded = value.get("value")
    if not isinstance(encoded, str):
        return None
    try:
        if encoding == "hex":
            if not (len(encoded) == 64 and encoded == encoded.lower()):
                return None
            decoded = bytes.fromhex(encoded)
        elif encoding == "base64":
            decoded = base64.b64decode(encoded, validate=True)
        else:
            return None
    except (ValueError, binascii.Error):
        return None
    return decoded if len(decoded) == 32 else None


def _receipt_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    if "outcome" in candidate:
        findings.append(Finding("RECEIPT_HAS_OUTCOME", "/outcome"))
    if "proof_id" in candidate:
        findings.append(Finding("RECEIPT_HAS_PROOF_ID", "/proof_id"))
    bytes_processed = candidate.get("bytes_processed")
    if isinstance(bytes_processed, bool) or not isinstance(bytes_processed, int):
        findings.append(Finding("RECEIPT_MISSING_BYTES", "/bytes_processed"))
    partial = candidate.get("partial_digest")
    if partial is not None and _digest_bytes(partial) is None:
        findings.append(Finding("DIGEST_INVALID", "/partial_digest"))
    return findings


def _proof_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    if "receipt_id" in candidate:
        findings.append(Finding("PROOF_HAS_RECEIPT_ID", "/receipt_id"))
    for field in sorted(PROGRESS_FIELDS):
        if field in candidate:
            findings.append(Finding("PROOF_HAS_PROGRESS_FIELD", f"/{field}"))

    outcome = candidate.get("outcome")
    if outcome not in OUTCOMES:
        findings.append(Finding("INVALID_OUTCOME", "/outcome"))

    expected_raw = candidate.get("expected_digest")
    observed_raw = candidate.get("observed_digest")
    expected = None if expected_raw is None else _digest_bytes(expected_raw)
    observed = None if observed_raw is None else _digest_bytes(observed_raw)

    if expected_raw is not None and expected is None:
        findings.append(Finding("DIGEST_INVALID", "/expected_digest"))
    if observed_raw is not None and observed is None:
        findings.append(Finding("DIGEST_INVALID", "/observed_digest"))

    manifest_ref = candidate.get("manifest_ref")
    if expected_raw is not None and not isinstance(manifest_ref, str):
        findings.append(Finding("FABRICATED_EXPECTED_DIGEST", "/expected_digest"))

    if outcome == "VERIFIED":
        if expected is None or observed is None:
            findings.append(Finding("PROOF_MISSING_DIGEST", "/"))
        elif expected != observed:
            findings.append(Finding("DIGEST_MISMATCH", "/observed_digest"))
    elif outcome == "MISMATCH":
        if expected is None or observed is None:
            findings.append(Finding("PROOF_MISSING_DIGEST", "/"))
        elif expected == observed:
            findings.append(Finding("DIGEST_EQUAL_WHEN_MISMATCH", "/observed_digest"))
    elif outcome == "MISSING_DECLARATION":
        if expected_raw is not None or manifest_ref is not None:
            findings.append(Finding("FABRICATED_EXPECTED_DIGEST", "/expected_digest"))
    elif outcome == "INTERRUPTED":
        if observed_raw is not None:
            findings.append(Finding("AMBIGUOUS_INTERRUPTED_PROOF", "/observed_digest"))

    return findings


def validate_path(path: Path, *, forced_kind: str = "auto") -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult("unknown", tuple(sorted(set(findings))))

    detected = _kind(candidate)
    kind = detected if forced_kind == "auto" else forced_kind
    if detected == "unknown" or kind not in {"receipt", "proof"}:
        findings.append(Finding("UNKNOWN_KIND", "/object_type"))
        return ValidationResult("unknown", tuple(sorted(set(findings))))

    findings.extend(_schema_findings(kind, candidate))
    if kind == "receipt":
        findings.extend(_receipt_findings(candidate))
    else:
        findings.extend(_proof_findings(candidate))
    return ValidationResult(kind, tuple(sorted(set(findings))))


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display_path(path),
            "kind": result.kind,
            "outcome": "PASS" if result.ok else "FAIL",
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(path: str) -> list[Path]:
    return sorted((FIXTURE_ROOT / path).glob("*.json"), key=lambda item: item.as_posix())


def run_fixture_profile() -> int:
    valid_files = _fixture_files("receipts/valid") + _fixture_files("proofs/valid")
    invalid_files = _fixture_files("receipts/invalid") + _fixture_files("proofs/invalid")
    try:
        manifest = json.loads(
            (FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    if not valid_files or not invalid_files or not isinstance(manifest, dict):
        return 1

    passed = True
    for path in valid_files:
        result = validate_path(path)
        print(_serialize(path, result))
        passed = result.ok and passed

    for path in invalid_files:
        result = validate_path(path)
        print(_serialize(path, result))
        relative = path.relative_to(FIXTURE_ROOT).as_posix()
        expected = sorted(manifest.get(relative, []))
        actual = sorted({finding.code for finding in result.findings})
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "file": relative,
                        "expected_codes": expected,
                        "actual_codes": actual,
                        "outcome": "FIXTURE_EXPECTATION_MISMATCH",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
    return 0 if passed else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument("--kind", choices=["auto", "receipt", "proof"], default="auto")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide at least one file or use --fixtures")

    passed = True
    for raw in args.files:
        path = Path(raw)
        result = validate_path(path, forced_kind=args.kind)
        print(_serialize(path, result))
        passed = result.ok and passed
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
