#!/usr/bin/env python3
"""Validate proposed KFM DatasetVersion records without network access.

A green result proves bounded JSON shape, deterministic version identity, digest
syntax, time ordering, canonical local reference arrays, and selected lifecycle /
lineage consistency only. It does not activate or fetch sources, resolve evidence,
decide rights or sensitivity, authorize release, publish, or permit public use.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/dataset_version.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/data/dataset_version"
MAX_FILE_BYTES = 1_048_576
MAX_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100
SCOPE = "dataset-version-shape-identity-lifecycle-and-lineage-only"
ERROR_CODES = frozenset({
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "INPUT_NOT_REGULAR_FILE", "JSON_COMPLEXITY_LIMIT", "JSON_DUPLICATE_KEY",
    "JSON_INVALID", "JSON_NONFINITE_NUMBER", "JSON_NOT_UTF8", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE", "SCHEMA_EVALUATION_LIMIT",
})


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


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
        return any(finding.code in ERROR_CODES for finding in self.findings)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _too_deep(text: str) -> bool:
    depth = 0
    in_string = False
    escaped = False
    for char in text:
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char in "[{":
            depth += 1
            if depth > MAX_DEPTH:
                return True
        elif char in "]}":
            depth -= 1
    return False


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.exists():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_REGULAR_FILE", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    if _too_deep(text):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    try:
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(
    schema_validator: Draft202012Validator,
    candidate: Mapping[str, Any],
) -> list[Finding]:
    try:
        errors = list(islice(schema_validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_EVALUATION_LIMIT", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(tuple(error.absolute_path)))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(tuple(item.absolute_path)), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _canonical_strings(value: Any) -> bool:
    values = _array(value)
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def canonical_dataset_version_id(candidate: Mapping[str, Any]) -> str:
    projection = {
        "dataset_id": candidate.get("dataset_id"),
        "version_label": candidate.get("version_label"),
        "representation_kind": candidate.get("representation_kind"),
        "source_ref": candidate.get("source_ref"),
        "content_digest": candidate.get("content_digest"),
        "spec_hash": candidate.get("spec_hash"),
        "temporal": candidate.get("temporal"),
        "lifecycle_stage": candidate.get("lifecycle_stage"),
    }
    encoded = json.dumps(
        projection,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "kfm:dataset-version:sha256:" + hashlib.sha256(encoded).hexdigest()


def _aware_datetime(value: Any) -> tuple[datetime | None, bool]:
    if not isinstance(value, str):
        return None, False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None, False
    return parsed, parsed.tzinfo is None or parsed.utcoffset() is None


def _placeholder_digest(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("sha256:") and set(value[7:]) == {"0"}


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    temporal = _mapping(candidate.get("temporal"))
    rights = _mapping(candidate.get("rights"))
    sensitivity = _mapping(candidate.get("sensitivity"))
    provenance = _mapping(candidate.get("provenance"))
    lineage = _mapping(candidate.get("lineage"))

    supplied_id = candidate.get("id")
    if isinstance(supplied_id, str):
        try:
            expected_id = canonical_dataset_version_id(candidate)
        except (TypeError, ValueError, RecursionError):
            expected_id = None
        if expected_id is not None and supplied_id != expected_id:
            findings.append(Finding("DATASET_VERSION_ID_MISMATCH", "/id"))

    for field in ("/content_digest", "/spec_hash"):
        if _placeholder_digest(candidate.get(field[1:])):
            findings.append(Finding("DIGEST_PLACEHOLDER_DENIED", field))

    temporal_fields = {
        "/temporal/source_published_at": temporal.get("source_published_at"),
        "/temporal/retrieved_at": temporal.get("retrieved_at"),
        "/temporal/ingested_at": temporal.get("ingested_at"),
    }
    parsed: dict[str, datetime] = {}
    for field, value in temporal_fields.items():
        if value is None:
            continue
        moment, naive = _aware_datetime(value)
        if naive:
            findings.append(Finding("TEMPORAL_TIMEZONE_REQUIRED", field))
        if moment is not None:
            parsed[field] = moment
    retrieved = parsed.get("/temporal/retrieved_at")
    ingested = parsed.get("/temporal/ingested_at")
    published = parsed.get("/temporal/source_published_at")
    if retrieved is not None and ingested is not None and retrieved > ingested:
        findings.append(Finding("TEMPORAL_ORDER_INVALID", "/temporal/ingested_at"))
    if published is not None and retrieved is not None and published > retrieved:
        findings.append(Finding("TEMPORAL_ORDER_INVALID", "/temporal/retrieved_at"))
    window = _mapping(temporal.get("effective_window"))
    if window:
        start, start_naive = _aware_datetime(window.get("start"))
        end, end_naive = _aware_datetime(window.get("end"))
        if start_naive:
            findings.append(Finding("TEMPORAL_TIMEZONE_REQUIRED", "/temporal/effective_window/start"))
        if end_naive:
            findings.append(Finding("TEMPORAL_TIMEZONE_REQUIRED", "/temporal/effective_window/end"))
        if start is not None and end is not None and start > end:
            findings.append(Finding("TEMPORAL_ORDER_INVALID", "/temporal/effective_window/end"))

    canonical_arrays = {
        "/rights/obligations": rights.get("obligations"),
        "/sensitivity/transform_refs": sensitivity.get("transform_refs"),
        "/provenance/evidence_refs": provenance.get("evidence_refs"),
        "/provenance/validation_refs": provenance.get("validation_refs"),
        "/provenance/run_receipt_refs": provenance.get("run_receipt_refs"),
        "/provenance/input_version_refs": provenance.get("input_version_refs"),
        "/lineage/supersedes": lineage.get("supersedes"),
        "/lineage/correction_refs": lineage.get("correction_refs"),
    }
    for field, value in canonical_arrays.items():
        if not _canonical_strings(value):
            findings.append(Finding("REFS_NOT_CANONICAL", field))

    self_refs = [
        lineage.get("previous_version_ref"),
        lineage.get("superseded_by"),
        lineage.get("rollback_target"),
        *_array(lineage.get("supersedes")),
    ]
    if isinstance(supplied_id, str) and supplied_id in self_refs:
        findings.append(Finding("VERSION_SELF_REFERENCE", "/lineage"))

    stage = candidate.get("lifecycle_stage")
    kind = candidate.get("representation_kind")
    release_ref = candidate.get("release_ref")
    evidence_refs = _array(provenance.get("evidence_refs"))
    validation_refs = _array(provenance.get("validation_refs"))
    run_refs = _array(provenance.get("run_receipt_refs"))
    input_refs = _array(provenance.get("input_version_refs"))

    if stage in {"RAW", "WORK", "QUARANTINE", "PROCESSED"} and release_ref is not None:
        findings.append(Finding("UNRELEASED_STAGE_WITH_RELEASE_REF", "/release_ref"))
    if kind == "processed_derivative" and (not run_refs or not input_refs):
        findings.append(Finding("PROCESSED_LINEAGE_INCOMPLETE", "/provenance"))
    if kind == "corrected_version" and (
        lineage.get("previous_version_ref") is None or not _array(lineage.get("correction_refs"))
    ):
        findings.append(Finding("CORRECTED_LINEAGE_INCOMPLETE", "/lineage"))
    if kind == "published_version" and stage != "PUBLISHED":
        findings.append(Finding("PUBLISHED_KIND_STAGE_MISMATCH", "/lifecycle_stage"))
    if stage == "PUBLISHED":
        if release_ref is None:
            findings.append(Finding("PUBLISHED_RELEASE_REQUIRED", "/release_ref"))
        if kind != "published_version":
            findings.append(Finding("PUBLISHED_KIND_STAGE_MISMATCH", "/representation_kind"))
        if rights.get("state") != "ALLOWED" or rights.get("decision_ref") is None:
            findings.append(Finding("PUBLISHED_RIGHTS_NOT_ALLOWED", "/rights"))
        if sensitivity.get("state") != "PUBLIC_SAFE" or sensitivity.get("decision_ref") is None:
            findings.append(Finding("PUBLISHED_SENSITIVITY_NOT_SAFE", "/sensitivity"))
        if not evidence_refs or not validation_refs:
            findings.append(Finding("PUBLISHED_SUPPORT_INCOMPLETE", "/provenance"))
    elif stage in {"CATALOG", "TRIPLET"} and (not evidence_refs or not validation_refs):
        findings.append(Finding("CATALOG_SUPPORT_INCOMPLETE", "/provenance"))

    governance = _mapping(candidate.get("governance"))
    if any(governance.get(field) is not False for field in (
        "authority_created", "evidence_closure_claimed", "policy_decision_created",
        "release_authority_created", "publication_authority_created",
        "public_use_authority_created",
    )):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings


def validate_dataset_version(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    try:
        schema_validator = _schema_validator()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return ValidationResult((Finding("SCHEMA_UNAVAILABLE", "/"),))
    schema_findings = _schema_findings(schema_validator, candidate)
    findings.extend(schema_findings)
    if not schema_findings:
        findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
    return json.dumps(
        {
            "file": _display(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixtures(directory: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in directory.glob("*.json")
            if path.name != "expected_findings_manifest.json"
        ),
        key=lambda path: path.name,
    )


def _expected() -> dict[str, list[str]]:
    raw = json.loads(
        (FIXTURE_ROOT / "invalid/expected_findings_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    if not isinstance(raw, dict):
        raise ValueError
    return {
        key: sorted(code for code in value if isinstance(code, str))
        for key, value in raw.items()
        if isinstance(key, str) and isinstance(value, list)
    }


def validate_fixtures() -> int:
    valid = _fixtures(FIXTURE_ROOT / "valid")
    invalid = _fixtures(FIXTURE_ROOT / "invalid")
    if not valid or not invalid:
        print("ERROR: valid and invalid fixture lanes must both be non-empty")
        return 1
    try:
        expected = _expected()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        print("ERROR: expected findings manifest could not be loaded")
        return 1
    ok = sorted(expected) == [path.name for path in invalid]
    for path in valid:
        result = validate_dataset_version(path)
        print(_serialize(path, result))
        ok = result.ok and ok
    for path in invalid:
        result = validate_dataset_version(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        wanted = expected.get(path.name, [])
        if result.ok or actual != wanted:
            ok = False
            print(
                json.dumps(
                    {
                        "actual": actual,
                        "expected": wanted,
                        "file": path.name,
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
    if ok:
        print(
            f"CONFIRMED: {len(valid)} valid and {len(invalid)} invalid "
            "DatasetVersion fixtures passed exact polarity."
        )
        return 0
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate proposed KFM DatasetVersion records."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return validate_fixtures()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_dataset_version(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
