"""Validate proposed KFM TemporalAuthorityEnvelope records without network access.

The envelope binds shared identity, SourceDescriptor-role references, authority,
explicit temporal roles, geography, state, lineage, and governance references
around a domain-native object. A passing result proves only the bounded checks
implemented here. It does not resolve the referenced source role or evidence,
admit a source, evaluate policy, approve review, release, publish, or replace the
owning domain contract, SourceDescriptor, TemporalWindow, or KFM temporal
vocabulary.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import stat
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "common"
    / "temporal_authority_envelope.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures"
    / "contracts"
    / "v1"
    / "common"
    / "temporal_authority_envelope"
)
MAX_FILE_BYTES = 1_000_000
MAX_JSON_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard or overflowing number."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    object_type: str | None
    certainty: str | None

    @property
    def ok(self) -> bool:
        return not self.findings


def _object_no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite_number(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _json_depth_exceeded(value: str) -> bool:
    depth = 0
    in_string = False
    escaped = False
    for character in value:
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
            continue
        if character == '"':
            in_string = True
        elif character in "[{":
            depth += 1
            if depth > MAX_JSON_DEPTH:
                return True
        elif character in "]}":
            depth -= 1
    return False


def _has_symlink_component(path: Path) -> bool:
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def _read_bounded_regular_file(path: Path) -> tuple[str | None, list[Finding]]:
    if _has_symlink_component(path):
        return None, [Finding("UNSAFE_FILE", "/", "input must be a regular file")]

    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    descriptor: int | None = None
    try:
        descriptor = os.open(path, flags)
        file_stat = os.fstat(descriptor)
        if not stat.S_ISREG(file_stat.st_mode):
            return None, [Finding("UNSAFE_FILE", "/", "input must be a regular file")]
        if file_stat.st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds parser budget")]

        chunks: list[bytes] = []
        remaining = MAX_FILE_BYTES + 1
        while remaining:
            block = os.read(descriptor, min(64 * 1024, remaining))
            if not block:
                break
            chunks.append(block)
            remaining -= len(block)
        encoded = b"".join(chunks)
        if len(encoded) > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds parser budget")]
        return encoded.decode("utf-8"), []
    except (OSError, UnicodeError):
        return None, [Finding("READ_ERROR", "/", "input could not be read safely")]
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    text, findings = _read_bounded_regular_file(path)
    if text is None:
        return None, findings
    if _json_depth_exceeded(text):
        return None, [
            Finding(
                "JSON_COMPLEXITY_LIMIT",
                "/",
                "input exceeds JSON parser complexity limits",
            )
        ]

    try:
        value = json.loads(
            text,
            object_pairs_hook=_object_no_duplicates,
            parse_constant=_reject_nonfinite_number,
            parse_float=_parse_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("DUPLICATE_KEY", "/", "input contains a duplicate key")]
    except NonFiniteNumberError:
        return None, [Finding("NONFINITE_NUMBER", "/", "JSON numbers must be finite")]
    except json.JSONDecodeError:
        return None, [Finding("INVALID_JSON", "/", "input is not valid JSON")]
    except (RecursionError, ValueError):
        return None, [
            Finding(
                "JSON_COMPLEXITY_LIMIT",
                "/",
                "input exceeds JSON parser complexity limits",
            )
        ]

    if not isinstance(value, dict):
        return None, [Finding("ROOT_TYPE", "/", "input root must be an object")]
    return value, []


def _load_schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _json_pointer(parts: Sequence[object]) -> str:
    if not parts:
        return "/"
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(escaped)


def _schema_findings(
    validator: Draft202012Validator,
    envelope: Mapping[str, object],
) -> list[Finding]:
    try:
        errors = list(islice(validator.iter_errors(envelope), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [
            Finding(
                "SCHEMA_EVALUATION_LIMIT",
                "/",
                "schema evaluation exceeded complexity limits",
            )
        ]

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors[:MAX_SCHEMA_FINDINGS],
        key=lambda error: (
            _json_pointer(tuple(error.absolute_path)),
            str(error.validator or "schema"),
        ),
    )
    findings = [
        Finding(
            "SCHEMA",
            _json_pointer(tuple(error.absolute_path)),
            f"schema constraint failed: {error.validator or 'schema'}",
        )
        for error in errors
    ]
    if truncated:
        findings.append(
            Finding(
                "SCHEMA_FINDINGS_TRUNCATED",
                "/",
                "schema findings were truncated at the output limit",
            )
        )
    return findings


def _parse_aware_datetime(value: object) -> tuple[datetime | None, bool]:
    """Return a parsed aware datetime and whether a parseable value lacked a zone."""

    if not isinstance(value, str):
        return None, False
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None, False
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None, True
    return parsed, False


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _string_set(value: object) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {item for item in value if isinstance(item, str)}


def _semantic_findings(envelope: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    identity = _mapping(envelope.get("identity"))
    source = _mapping(envelope.get("source"))
    times = _mapping(envelope.get("time"))
    lineage = _mapping(envelope.get("lineage"))

    object_id = identity.get("object_id")
    revision_id = identity.get("revision_id")
    if isinstance(object_id, str) and object_id == revision_id:
        findings.append(
            Finding(
                "REVISION_ID_COLLAPSE",
                "/identity/revision_id",
                "revision identity must differ from stable object identity",
            )
        )

    source_descriptor_ref = source.get("source_descriptor_ref")
    source_role_ref = source.get("source_role_ref")
    if isinstance(source_descriptor_ref, str) and isinstance(source_role_ref, str):
        if source_role_ref != f"{source_descriptor_ref}#/source_role":
            findings.append(
                Finding(
                    "SOURCE_ROLE_REF_UNBOUND",
                    "/source/source_role_ref",
                    "source_role_ref must bind to the declared SourceDescriptor role field",
                )
            )

    parsed: dict[str, datetime] = {}
    for field in (
        "issued_at",
        "effective_at",
        "valid_from",
        "valid_to",
        "observed_at",
        "retrieved_at",
        "corrected_at",
        "superseded_at",
    ):
        value = times.get(field)
        timestamp, timezone_missing = _parse_aware_datetime(value)
        if timezone_missing:
            findings.append(
                Finding(
                    "TEMPORAL_TIMEZONE_REQUIRED",
                    f"/time/{field}",
                    "date-time must include a timezone offset",
                )
            )
        elif timestamp is not None:
            parsed[field] = timestamp

    valid_from = parsed.get("valid_from")
    valid_to = parsed.get("valid_to")
    if valid_from is not None and valid_to is not None and valid_from > valid_to:
        findings.append(
            Finding(
                "TEMPORAL_ORDER_INVALID",
                "/time/valid_to",
                "valid_to must not precede valid_from",
            )
        )

    retrieved_at = parsed.get("retrieved_at")
    if retrieved_at is not None:
        for field in ("issued_at", "observed_at", "corrected_at", "superseded_at"):
            timestamp = parsed.get(field)
            if timestamp is not None and timestamp > retrieved_at:
                findings.append(
                    Finding(
                        "SOURCE_TIME_AFTER_RETRIEVAL",
                        f"/time/{field}",
                        "source or lineage time cannot be later than represented retrieval",
                    )
                )

    issued_at = parsed.get("issued_at")
    corrected_at = parsed.get("corrected_at")
    superseded_at = parsed.get("superseded_at")
    if issued_at is not None and corrected_at is not None and corrected_at < issued_at:
        findings.append(
            Finding(
                "CORRECTION_BEFORE_ISSUANCE",
                "/time/corrected_at",
                "correction time must not precede issue time",
            )
        )
    if issued_at is not None and superseded_at is not None and superseded_at < issued_at:
        findings.append(
            Finding(
                "SUPERSESSION_BEFORE_ISSUANCE",
                "/time/superseded_at",
                "supersession time must not precede issue time",
            )
        )

    supersedes = _string_set(lineage.get("supersedes"))
    superseded_by = _string_set(lineage.get("superseded_by"))

    if isinstance(revision_id, str):
        for field, refs in (
            ("supersedes", supersedes),
            ("superseded_by", superseded_by),
        ):
            if revision_id in refs:
                findings.append(
                    Finding(
                        "SELF_LINEAGE_REFERENCE",
                        f"/lineage/{field}",
                        "lineage must not reference the current revision as its own neighbor",
                    )
                )

    if supersedes & superseded_by:
        findings.append(
            Finding(
                "LINEAGE_DIRECTION_CONFLICT",
                "/lineage",
                "the same revision cannot be both superseded and superseding",
            )
        )

    return findings


def validate_envelope(path: Path) -> ValidationResult:
    envelope, findings = _load_json_object(path)
    if envelope is None:
        return ValidationResult(tuple(sorted(findings)), None, None)

    try:
        validator = _load_schema_validator()
    except (OSError, UnicodeError, ValueError):
        return ValidationResult(
            (
                Finding(
                    "SCHEMA_UNAVAILABLE",
                    "/",
                    "TemporalAuthorityEnvelope schema could not be loaded",
                ),
            ),
            None,
            None,
        )

    findings.extend(_schema_findings(validator, envelope))
    findings.extend(_semantic_findings(envelope))
    identity = _mapping(envelope.get("identity"))
    state = _mapping(envelope.get("state"))
    object_type = identity.get("object_type")
    certainty = state.get("certainty")
    return ValidationResult(
        tuple(sorted(set(findings))),
        object_type if isinstance(object_type, str) else None,
        certainty if isinstance(certainty, str) else None,
    )


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": "temporal-authority-envelope-shape-binding-and-lineage-only",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _expected_codes(path: Path) -> tuple[str, ...]:
    expected_path = path.with_suffix(".expected_findings.txt")
    if not expected_path.is_file():
        return ()
    return tuple(
        sorted(
            line.strip()
            for line in expected_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    )


def _run_fixtures() -> int:
    valid = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("*.json"))
    semantic_invalid = sorted((FIXTURE_ROOT / "semantic_invalid").glob("*.json"))
    if not valid or not invalid or not semantic_invalid:
        print("FIXTURE_ERROR: every fixture lane must be non-empty")
        return 1

    ok = True
    for path in valid:
        result = validate_envelope(path)
        print(_serialize(path, result))
        ok = result.ok and ok

    for path in (*invalid, *semantic_invalid):
        result = validate_envelope(path)
        print(_serialize(path, result))
        actual = tuple(sorted({finding.code for finding in result.findings}))
        expected = _expected_codes(path)
        if result.ok or not expected or actual != expected:
            ok = False
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
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate proposed KFM TemporalAuthorityEnvelope records."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return _run_fixtures()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_envelope(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
