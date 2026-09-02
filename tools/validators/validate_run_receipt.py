"""Validate KFM RunReceipt records, including the Smart Sync HTTP profile.

The validator is deliberately no-network. It validates the proposed RunReceipt
schema and enforces bounded semantic checks that JSON Schema cannot express,
including digest equality for HTTP 200 decisions and safe conditional-header
syntax. It never fetches a source, resolves a SourceDescriptor, writes a
receipt, or grants promotion, release, or publication authority.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import stat
import sys
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from itertools import islice
from pathlib import Path
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.local_resolver import build_registry

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/runtime/run_receipt.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/runtime/run_receipt"
MAX_FILE_BYTES = 1_000_000
MAX_JSON_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100
_ETAG_RE = re.compile(r'^(?:W/)?"[\x21\x23-\x7e\x80-\xff]*"$')
_INVALID_PERCENT_ESCAPE_RE = re.compile(r"%(?![0-9A-Fa-f]{2})")
_MONTH = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
_WEEKDAY_ABBREVIATIONS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
_HTTP_DATE_PATTERNS = (
    re.compile(
        rf"^(?P<weekday>Mon|Tue|Wed|Thu|Fri|Sat|Sun), "
        rf"[0-9]{{2}} {_MONTH} [0-9]{{4}} "
        rf"[0-9]{{2}}:[0-9]{{2}}:[0-9]{{2}} GMT$"
    ),
    re.compile(
        rf"^(?P<weekday>Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), "
        rf"[0-9]{{2}}-{_MONTH}-[0-9]{{2}} "
        rf"[0-9]{{2}}:[0-9]{{2}}:[0-9]{{2}} GMT$"
    ),
    re.compile(
        rf"^(?P<weekday>Mon|Tue|Wed|Thu|Fri|Sat|Sun) {_MONTH} "
        rf"[ 0-9][0-9] [0-9]{{2}}:[0-9]{{2}}:[0-9]{{2}} [0-9]{{4}}$"
    ),
)


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
    decision: str | None
    http_status: int | None

    @property
    def ok(self) -> bool:
        return not self.findings


def _object_no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError("duplicate JSON object member")
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
        return None, [Finding("UNSAFE_FILE", "/", "receipt must be a regular file")]

    flags = (
        os.O_RDONLY
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0)
    )
    descriptor: int | None = None
    try:
        descriptor = os.open(path, flags)
        file_stat = os.fstat(descriptor)
        if not stat.S_ISREG(file_stat.st_mode):
            return None, [
                Finding("UNSAFE_FILE", "/", "receipt must be a regular file")
            ]
        if file_stat.st_size > MAX_FILE_BYTES:
            return None, [
                Finding("FILE_TOO_LARGE", "/", "receipt exceeds the parser budget")
            ]

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
            return None, [
                Finding("FILE_TOO_LARGE", "/", "receipt exceeds the parser budget")
            ]
        return encoded.decode("utf-8"), []
    except (OSError, UnicodeError):
        return None, [Finding("READ_ERROR", "/", "receipt file is not readable")]
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
                "receipt exceeds JSON parser complexity limits",
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
        return None, [Finding("DUPLICATE_KEY", "/", "receipt contains a duplicate key")]
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None, [Finding("INVALID_JSON", "/", "receipt is not finite UTF-8 JSON")]
    except NonFiniteNumberError:
        return None, [Finding("NONFINITE_NUMBER", "/", "receipt numbers must be finite")]
    except (RecursionError, ValueError):
        return None, [
            Finding(
                "JSON_COMPLEXITY_LIMIT",
                "/",
                "receipt exceeds JSON parser complexity limits",
            )
        ]

    if not isinstance(value, dict):
        return None, [Finding("ROOT_TYPE", "/", "receipt root must be an object")]
    return value, []


def _load_schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    registry = build_registry(REPO_ROOT)
    return Draft202012Validator(
        schema,
        registry=registry,
        format_checker=FormatChecker(),
    )


def _json_pointer(parts: Sequence[object]) -> str:
    if not parts:
        return "/"
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(escaped)


def _schema_findings(
    validator: Draft202012Validator,
    receipt: Mapping[str, object],
) -> list[Finding]:
    errors, truncated, evaluation_failed = _bounded_schema_errors(validator, receipt)
    if evaluation_failed:
        return [
            Finding(
                "SCHEMA_EVALUATION_LIMIT",
                "/",
                "RunReceipt schema evaluation exceeded complexity limits",
            )
        ]

    findings: list[Finding] = []
    errors = sorted(
        errors,
        key=lambda error: (
            tuple(str(part) for part in error.absolute_path),
            error.validator or "",
        ),
    )
    for error in errors:
        keyword = error.validator or "schema"
        findings.append(
            Finding(
                "SCHEMA",
                _json_pointer(tuple(error.absolute_path)),
                f"RunReceipt violates JSON Schema keyword {keyword}",
            )
        )
    if truncated:
        findings.append(
            Finding(
                "SCHEMA_FINDINGS_TRUNCATED",
                "/",
                "RunReceipt schema findings were truncated at the output limit",
            )
        )
    return findings


def _bounded_schema_errors(
    validator: Draft202012Validator,
    receipt: Mapping[str, object],
) -> tuple[list[ValidationError], bool, bool]:
    try:
        errors = list(islice(validator.iter_errors(receipt), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [], False, True
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    return errors[:MAX_SCHEMA_FINDINGS], truncated, False


def _parse_datetime(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _parse_http_date(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    match = None
    for pattern in _HTTP_DATE_PATTERNS:
        match = pattern.fullmatch(value)
        if match is not None:
            break
    if match is None:
        return None
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError):
        return None
    if parsed is None:
        return None
    parsed = parsed if parsed.tzinfo is not None else parsed.replace(tzinfo=timezone.utc)
    if _WEEKDAY_ABBREVIATIONS[parsed.weekday()] != match.group("weekday")[:3]:
        return None
    return parsed


def _valid_http_date(value: object) -> bool:
    return _parse_http_date(value) is not None


def _etag_opaque(value: object) -> str | None:
    if not isinstance(value, str) or _ETAG_RE.fullmatch(value) is None:
        return None
    return value[2:] if value.startswith("W/") else value


def _unsafe_url_text(value: str) -> bool:
    return (
        "\\" in value
        or "?" in value
        or "#" in value
        or _INVALID_PERCENT_ESCAPE_RE.search(value) is not None
        or any(
            character.isspace()
            or unicodedata.category(character) in {"Cc", "Cf", "Cs"}
            for character in value
        )
    )


def _validator_set_findings(value: object, field: str) -> list[Finding]:
    if not isinstance(value, dict):
        return []
    findings: list[Finding] = []
    etag = value.get("etag")
    if etag is not None and (not isinstance(etag, str) or _ETAG_RE.fullmatch(etag) is None):
        findings.append(
            Finding(
                "INVALID_ETAG",
                f"{field}/etag",
                "ETag must be a quoted strong or weak HTTP entity tag",
            )
        )
    last_modified = value.get("last_modified")
    if last_modified is not None and not _valid_http_date(last_modified):
        findings.append(
            Finding(
                "INVALID_HTTP_DATE",
                f"{field}/last_modified",
                "Last-Modified must be a timezone-aware HTTP date",
            )
        )
    return findings


def _all_zero_sha256(value: object) -> bool:
    return isinstance(value, str) and value == "sha256:" + ("0" * 64)


def _identity_findings(receipt: Mapping[str, object]) -> list[Finding]:
    if _all_zero_sha256(receipt.get("spec_hash")):
        return [
            Finding(
                "PLACEHOLDER_DIGEST",
                "/spec_hash",
                "all-zero SHA-256 placeholders are not valid identity bindings",
            )
        ]
    return []


def _smart_sync_findings(receipt: Mapping[str, object]) -> list[Finding]:
    profile = receipt.get("smart_sync")
    if not isinstance(profile, dict):
        return []

    findings: list[Finding] = []
    if _parse_datetime(profile.get("fetch_time")) is None:
        findings.append(
            Finding(
                "INVALID_FETCH_TIME",
                "/smart_sync/fetch_time",
                "fetch_time must be a timezone-aware ISO-8601 timestamp",
            )
        )

    source_url = profile.get("source_url")
    if isinstance(source_url, str):
        unsafe = _unsafe_url_text(source_url)
        try:
            parsed = urlsplit(source_url)
            hostname = parsed.hostname
            parsed_port = parsed.port
            unsafe = unsafe or (
                parsed.scheme != "https"
                or not hostname
                or parsed.username is not None
                or parsed.password is not None
                or parsed.query
                or parsed.fragment
                or parsed_port is not None and not 1 <= parsed_port <= 65535
            )
        except ValueError:
            unsafe = True
        if unsafe:
            findings.append(
                Finding(
                    "UNSAFE_SOURCE_URL",
                    "/smart_sync/source_url",
                    "source_url must be HTTPS with a host and no unsafe components",
                )
            )

    validators = profile.get("http_validators")
    request: object = None
    response: object = None
    if isinstance(validators, dict):
        request = validators.get("request")
        response = validators.get("response")
        findings.extend(
            _validator_set_findings(request, "/smart_sync/http_validators/request")
        )
        if response is not None:
            findings.extend(
                _validator_set_findings(response, "/smart_sync/http_validators/response")
            )

    if profile.get("http_status") == 304 and isinstance(request, dict):
        response_mapping = response if isinstance(response, dict) else {}
        request_etag = _etag_opaque(request.get("etag"))
        response_etag = _etag_opaque(response_mapping.get("etag"))
        if (
            request_etag is not None
            and response_etag is not None
            and request_etag != response_etag
        ):
            findings.append(
                Finding(
                    "NOT_MODIFIED_VALIDATOR_MISMATCH",
                    "/smart_sync/http_validators/response/etag",
                    "304 response validator conflicts with the conditional request",
                )
            )
        if request_etag is None:
            request_date = _parse_http_date(request.get("last_modified"))
            response_date = _parse_http_date(response_mapping.get("last_modified"))
            if (
                request_date is not None
                and response_date is not None
                and response_date > request_date
            ):
                findings.append(
                    Finding(
                        "NOT_MODIFIED_VALIDATOR_MISMATCH",
                        "/smart_sync/http_validators/response/last_modified",
                        "304 response validator conflicts with the conditional request",
                    )
                )

    prior_run = profile.get("prior_run_receipt_ref")
    if prior_run == receipt.get("run_id"):
        findings.append(
            Finding(
                "SELF_PRIOR_RECEIPT",
                "/smart_sync/prior_run_receipt_ref",
                "a Smart Sync receipt cannot use itself as its prior checkpoint",
            )
        )

    prior_digest = profile.get("prior_content_digest")
    content_digest = profile.get("content_digest")
    for field, value in (
        ("/smart_sync/prior_content_digest", prior_digest),
        ("/smart_sync/content_digest", content_digest),
    ):
        if _all_zero_sha256(value):
            findings.append(
                Finding(
                    "PLACEHOLDER_DIGEST",
                    field,
                    "all-zero SHA-256 placeholders are not valid identity bindings",
                )
            )

    status = profile.get("http_status")
    decision = profile.get("decision")
    if status == 200 and decision == "materialize" and content_digest == prior_digest:
        findings.append(
            Finding(
                "UNCHANGED_MATERIALIZATION",
                "/smart_sync/content_digest",
                "HTTP 200 content matching the prior digest must be recorded as no_op",
            )
        )
    if status == 200 and decision == "no_op" and content_digest != prior_digest:
        findings.append(
            Finding(
                "CHANGED_CONTENT_NO_OP",
                "/smart_sync/content_digest",
                "HTTP 200 no_op requires content to match the prior digest",
            )
        )

    return findings


def validate_receipt(path: Path) -> ValidationResult:
    """Validate one receipt without performing any network or durable writes."""

    receipt, findings = _load_json_object(path)
    if receipt is None:
        return ValidationResult(tuple(sorted(findings)), None, None)

    validator = _load_schema_validator()
    findings.extend(_schema_findings(validator, receipt))
    findings.extend(_identity_findings(receipt))
    findings.extend(_smart_sync_findings(receipt))

    profile = receipt.get("smart_sync")
    decision = profile.get("decision") if isinstance(profile, dict) else None
    http_status = profile.get("http_status") if isinstance(profile, dict) else None
    return ValidationResult(
        tuple(sorted(set(findings))),
        decision if isinstance(decision, str) else None,
        http_status if isinstance(http_status, int) else None,
    )


def _render(path: Path, result: ValidationResult) -> tuple[str, ...]:
    if result.ok:
        profile = "generic"
        if result.decision is not None and result.http_status is not None:
            profile = f"smart-sync status={result.http_status} decision={result.decision}"
        return (f"OK {path} profile={profile}",)
    return tuple(
        f"FAIL {path} code={finding.code} field={finding.field} detail={finding.detail}"
        for finding in result.findings
    )


def _expected_rejection_matches(
    path: Path,
    receipt: Mapping[str, object],
    result: ValidationResult,
    validator: Draft202012Validator,
) -> bool:
    sidecar = path.with_suffix(".expected_error.txt")
    try:
        if (
            _has_symlink_component(sidecar)
            or not sidecar.is_file()
            or sidecar.stat().st_size > 1024
        ):
            return False
        expected_text = sidecar.read_text(encoding="utf-8")
        expected = json.loads(
            expected_text,
            object_pairs_hook=_object_no_duplicates,
        )
    except (DuplicateKeyError, json.JSONDecodeError, OSError, UnicodeError):
        return False
    if not isinstance(expected, dict):
        return False

    kind = expected.get("kind")
    field = expected.get("field")
    contains = expected.get("contains")
    if (
        kind not in {"schema", "finding"}
        or not isinstance(field, str)
        or not field.startswith("/")
        or (
            contains is not None
            and (not isinstance(contains, str) or not contains or len(contains) > 128)
        )
    ):
        return False
    contains_text = contains.lower() if isinstance(contains, str) else None

    if kind == "schema":
        if set(expected) - {"kind", "field", "keyword", "contains"}:
            return False
        keyword = expected.get("keyword")
        if not isinstance(keyword, str) or not keyword:
            return False
        schema_errors, _, evaluation_failed = _bounded_schema_errors(
            validator, receipt
        )
        if evaluation_failed:
            return False
        return any(
            _json_pointer(tuple(error.absolute_path)) == field
            and (error.validator or "schema") == keyword
            and (contains_text is None or contains_text in error.message.lower())
            for error in schema_errors
        )

    if set(expected) - {"kind", "field", "code", "contains"}:
        return False
    code = expected.get("code")
    if not isinstance(code, str) or not code:
        return False
    return any(
        finding.code == code
        and finding.field == field
        and (contains_text is None or contains_text in finding.detail.lower())
        for finding in result.findings
    )


def _run_fixtures() -> int:
    valid_files = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    invalid_files = sorted((FIXTURE_ROOT / "invalid").glob("*.json"))
    ok = True
    if not valid_files:
        print(f"FAIL {FIXTURE_ROOT / 'valid'}: no JSON fixtures found")
        ok = False
    if not invalid_files:
        print(f"FAIL {FIXTURE_ROOT / 'invalid'}: no JSON fixtures found")
        ok = False

    validator = _load_schema_validator()

    for path in valid_files:
        result = validate_receipt(path)
        if result.ok:
            for line in _render(path, result):
                print(line)
        else:
            for line in _render(path, result):
                print(line)
            ok = False

    for path in invalid_files:
        receipt, load_findings = _load_json_object(path)
        if receipt is None:
            first = load_findings[0]
            print(
                f"FAIL {path} code={first.code} "
                f"field={first.field} detail={first.detail}"
            )
            ok = False
            continue
        result = validate_receipt(path)
        if result.ok:
            print(f"FAIL {path}: expected schema or semantic rejection")
            ok = False
        elif not _expected_rejection_matches(path, receipt, result, validator):
            print(f"FAIL {path}: expected-error sidecar did not match rejection")
            ok = False
        else:
            first = result.findings[0]
            print(
                f"EXPECTED_FAIL {path} code={first.code} "
                f"field={first.field} detail={first.detail}"
            )
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate KFM RunReceipt records without network access."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return _run_fixtures()
    if not args.files:
        parser.error("at least one receipt is required unless --fixtures is used")

    ok = True
    for path in args.files:
        result = validate_receipt(path)
        for line in _render(path, result):
            print(line)
        ok = result.ok and ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
