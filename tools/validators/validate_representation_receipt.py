#!/usr/bin/env python3
"""Validate KFM RepresentationReceipt records without network access.

A passing result proves bounded shape and local consistency only. It does not
resolve evidence, evaluate policy, complete review, authorize release, or publish.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/receipts/representation_receipt.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/receipts/representation_receipt"
MAX_FILE_BYTES = 1_048_576
SCOPE = "representation-receipt-shape-and-local-consistency-only"


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


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    if not path.is_file():
        return None, [Finding("FILE_NOT_FOUND", "/")]
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
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
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: dict[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in validator.iter_errors(candidate)
    ]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _is_zero_digest(value: Any) -> bool:
    return isinstance(value, str) and value == "sha256:" + ("0" * 64)


def _sorted_unique_strings(values: list[Any]) -> bool:
    return (
        all(isinstance(item, str) for item in values)
        and values == sorted(set(values))
    )


def _artifact_refs(values: list[Any]) -> list[Any]:
    return [
        item.get("artifact_ref")
        for item in values
        if isinstance(item, dict)
    ]


def _semantic_findings(candidate: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    receipt_id = candidate.get("receipt_id")
    representation_type = candidate.get("representation_type")
    evidence_refs = _array(candidate.get("evidence_bundle_refs"))
    inputs = _array(candidate.get("inputs"))
    outputs = _array(candidate.get("outputs"))
    method = _mapping(candidate.get("method"))
    fidelity = _mapping(candidate.get("fidelity"))
    timing = _mapping(candidate.get("timing"))
    lineage = _mapping(candidate.get("lineage"))
    governance = _mapping(candidate.get("governance"))

    for field, value in (
        ("/method/spec_hash", method.get("spec_hash")),
        ("/method/parameters_hash", method.get("parameters_hash")),
    ):
        if _is_zero_digest(value):
            findings.append(Finding("DIGEST_PLACEHOLDER", field))

    for lane, values in (("inputs", inputs), ("outputs", outputs)):
        for index, item in enumerate(values):
            if isinstance(item, dict) and _is_zero_digest(item.get("digest")):
                findings.append(
                    Finding("DIGEST_PLACEHOLDER", f"/{lane}/{index}/digest")
                )

    if evidence_refs and not _sorted_unique_strings(evidence_refs):
        findings.append(
            Finding("REFS_NOT_CANONICAL", "/evidence_bundle_refs")
        )

    for lane, values in (("inputs", inputs), ("outputs", outputs)):
        refs = _artifact_refs(values)
        if (
            len(refs) != len(values)
            or not _sorted_unique_strings(refs)
        ):
            findings.append(Finding("ARTIFACTS_NOT_CANONICAL", f"/{lane}"))

    representation_fidelity = fidelity.get("representation_fidelity")
    information_loss = fidelity.get("information_loss")
    loss_notes = fidelity.get("loss_notes")

    if representation_fidelity == "EXACT" and information_loss is not False:
        findings.append(
            Finding("FIDELITY_LOSS_MISMATCH", "/fidelity/information_loss")
        )
    if representation_fidelity in {"GENERALIZED", "AGGREGATED", "SYNTHETIC"}:
        if information_loss is not True:
            findings.append(
                Finding("FIDELITY_LOSS_MISMATCH", "/fidelity/information_loss")
            )
        if not isinstance(loss_notes, str) or not loss_notes.strip():
            findings.append(
                Finding("LOSS_NOTES_REQUIRED", "/fidelity/loss_notes")
            )

    requires_boundary = (
        representation_type in {"THREE_D_SCENE", "SYNTHETIC_SURFACE"}
        or representation_fidelity in {"MODELED", "SYNTHETIC"}
    )
    if requires_boundary and not isinstance(
        candidate.get("reality_boundary_note_ref"), str
    ):
        findings.append(
            Finding(
                "REALITY_BOUNDARY_REQUIRED",
                "/reality_boundary_note_ref",
            )
        )

    represented_at = _parse_time(timing.get("represented_at"))
    input_as_of = _parse_time(timing.get("input_as_of"))
    if represented_at and input_as_of and input_as_of > represented_at:
        findings.append(Finding("INPUT_AFTER_REPRESENTATION", "/timing/input_as_of"))

    if receipt_id and lineage.get("supersedes") == receipt_id:
        findings.append(Finding("SELF_SUPERSESSION", "/lineage/supersedes"))
    if receipt_id and lineage.get("superseded_by") == receipt_id:
        findings.append(Finding("SELF_SUPERSESSION", "/lineage/superseded_by"))

    flag_fields = (
        "authority_created",
        "policy_evaluated",
        "review_completed",
        "release_authorized",
        "public_use_allowed",
    )
    if (
        any(governance.get(field) is not False for field in flag_fields)
        or governance.get("release_ref") is not None
    ):
        findings.append(
            Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance")
        )

    return findings


def validate_receipt(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": item.code, "field": item.field}
                for item in result.findings
            ],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(directory: Path, prefix: str) -> list[Path]:
    return sorted(
        directory.glob(f"{prefix}*.json"),
        key=lambda path: path.as_posix(),
    )


def _expected_manifest(directory: Path) -> dict[str, list[str]]:
    try:
        value = json.loads(
            (directory / "expected_findings_manifest.json").read_text(
                encoding="utf-8"
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile() -> int:
    valid_files = _fixture_files(FIXTURE_ROOT / "valid", "valid_")
    invalid_files = _fixture_files(FIXTURE_ROOT / "invalid", "invalid_")
    manifest = _expected_manifest(FIXTURE_ROOT / "invalid")
    if not valid_files or not invalid_files:
        return 1

    passed = True
    for path in valid_files:
        result = validate_receipt(path)
        print(_serialize(path, result))
        passed = passed and result.ok

    for path in invalid_files:
        result = validate_receipt(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(manifest.get(path.name, []))
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual": actual,
                        "expected": expected,
                        "file": path.as_posix(),
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate proposed KFM RepresentationReceipt records."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_receipt(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
