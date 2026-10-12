#!/usr/bin/env python3
"""Validate read-only, fixture-backed BriefingSignal issue inventory projections.

The projection is intentionally narrow. It records only repository identity, issue
number, open/closed state, and update time. It is not live GitHub evidence, does not
create repository authority, and cannot authorize issue mutation. The validator is
deterministic, duplicate-key safe, no-network, and value-minimized.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/issue_inventory_projection.schema.json"
)
PROFILE = "kfm.briefing.issue-inventory.fixture.v1"
SCHEMA_VERSION = "1.0.0"
SCOPE = "briefing-issue-inventory-projection"
MAX_JSON_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 100
MAX_ISSUES = 256
CANONICAL_UTC_SECOND = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"
)
DIGEST_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
PROJECTION_ID_PATTERN = re.compile(r"^kfm:issue-inventory:[0-9a-f]{16}$")


@dataclass(frozen=True, order=True)
class Finding:
    """One deterministic finding that does not echo input values."""

    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    """Bounded validation result for one projection candidate."""

    findings: tuple[Finding, ...]
    payload: Mapping[str, object] | None

    @property
    def ok(self) -> bool:
        return not self.findings and self.payload is not None


class DuplicateKeyError(ValueError):
    """Raised when parsed JSON repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


def _reject_duplicate_keys(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite_number(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _json_pointer(parts: Iterable[object]) -> str:
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1")
        for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _canonical_json(value: object) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def canonical_projection_payload(
    projection: Mapping[str, object],
) -> dict[str, object]:
    """Return the exact digest-bearing payload."""

    return {
        key: projection[key]
        for key in sorted(projection)
        if key not in {"projection_id", "projection_digest"}
    }


def compute_projection_digest(
    projection: Mapping[str, object],
) -> str:
    payload = canonical_projection_payload(projection)
    digest = hashlib.sha256(
        _canonical_json(payload).encode("utf-8")
    ).hexdigest()
    return f"sha256:{digest}"


def compute_projection_id(
    projection: Mapping[str, object],
) -> str:
    digest = compute_projection_digest(projection).removeprefix("sha256:")
    return f"kfm:issue-inventory:{digest[:16]}"


def _is_canonical_utc_second(value: object) -> bool:
    if not isinstance(value, str) or not CANONICAL_UTC_SECOND.fullmatch(value):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.isoformat(timespec="seconds").replace("+00:00", "Z") == value


def _load_schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )


def _load_json_object(
    path: Path,
) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [
                Finding("INPUT_SYMLINK_DENIED", "/",)
            ]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite_number,
            parse_float=_parse_finite_float,
        )
    except (OSError, UnicodeError):
        return None, [Finding("INPUT_UNREADABLE", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]

    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/")]
    return value, []


def _schema_findings(
    validator: Draft202012Validator,
    projection: Mapping[str, object],
) -> list[Finding]:
    try:
        errors = list(
            islice(
                validator.iter_errors(projection),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_EVALUATION_LIMIT", "/")]

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors,
        key=lambda error: (
            _json_pointer(error.absolute_path),
            str(error.validator),
        ),
    )[:MAX_SCHEMA_FINDINGS]
    findings = [
        Finding(
            "SCHEMA_INVALID",
            _json_pointer(error.absolute_path),
        )
        for error in errors
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _semantic_findings(
    projection: Mapping[str, object],
) -> list[Finding]:
    findings: list[Finding] = []
    generated_at = projection.get("generated_at")
    issues = projection.get("issues")
    issue_count = projection.get("issue_count")

    if not _is_canonical_utc_second(generated_at):
        findings.append(
            Finding("GENERATED_AT_NOT_CANONICAL_UTC_SECOND", "/generated_at")
        )

    if isinstance(issues, list):
        numbers: list[int] = []
        for index, issue in enumerate(issues):
            if not isinstance(issue, Mapping):
                continue
            number = issue.get("number")
            updated_at = issue.get("updated_at")
            if isinstance(number, int) and not isinstance(number, bool):
                numbers.append(number)
            if not _is_canonical_utc_second(updated_at):
                findings.append(
                    Finding(
                        "ISSUE_UPDATED_AT_NOT_CANONICAL_UTC_SECOND",
                        f"/issues/{index}/updated_at",
                    )
                )
            if (
                _is_canonical_utc_second(generated_at)
                and _is_canonical_utc_second(updated_at)
                and isinstance(generated_at, str)
                and isinstance(updated_at, str)
                and updated_at > generated_at
            ):
                findings.append(
                    Finding(
                        "ISSUE_UPDATED_AFTER_PROJECTION",
                        f"/issues/{index}/updated_at",
                    )
                )
        if len(numbers) != len(set(numbers)):
            findings.append(
                Finding("ISSUE_NUMBER_DUPLICATE", "/issues")
            )
        if numbers != sorted(numbers):
            findings.append(
                Finding("ISSUES_NOT_SORTED", "/issues")
            )
        if isinstance(issue_count, int) and issue_count != len(issues):
            findings.append(
                Finding("ISSUE_COUNT_MISMATCH", "/issue_count")
            )
        if len(issues) > MAX_ISSUES:
            findings.append(
                Finding("ISSUE_COUNT_EXCEEDED", "/issues")
            )

    digest = projection.get("projection_digest")
    projection_id = projection.get("projection_id")
    if isinstance(digest, str) and DIGEST_PATTERN.fullmatch(digest):
        if digest != compute_projection_digest(projection):
            findings.append(
                Finding("PROJECTION_DIGEST_MISMATCH", "/projection_digest")
            )
    if (
        isinstance(projection_id, str)
        and PROJECTION_ID_PATTERN.fullmatch(projection_id)
        and projection_id != compute_projection_id(projection)
    ):
        findings.append(
            Finding("PROJECTION_ID_MISMATCH", "/projection_id")
        )

    return findings


def validate_projection(path: Path) -> ValidationResult:
    """Validate one local projection and return no input values on failure."""

    projection, load_findings = _load_json_object(path)
    if projection is None:
        return ValidationResult(
            findings=tuple(sorted(load_findings)),
            payload=None,
        )

    schema_findings = _schema_findings(
        _load_schema_validator(),
        projection,
    )
    if schema_findings:
        return ValidationResult(
            findings=tuple(sorted(schema_findings)),
            payload=None,
        )

    semantic_findings = _semantic_findings(projection)
    return ValidationResult(
        findings=tuple(sorted(semantic_findings)),
        payload=projection if not semantic_findings else None,
    )


def projection_summary(
    projection: Mapping[str, object],
) -> dict[str, object]:
    """Return the value-minimized projection metadata used by the router."""

    return {
        "authority_created": False,
        "generated_at": projection.get("generated_at"),
        "issue_count": projection.get("issue_count"),
        "live_state_verified": False,
        "projection_id": projection.get("projection_id"),
        "repository": projection.get("repository"),
        "repository_mutation_allowed": False,
    }


def bind_issue_inventory(
    *,
    declared_disposition: str,
    declared_reason_codes: Sequence[str],
    matched_issue_ids: Sequence[int],
    projection: Mapping[str, object] | None,
) -> dict[str, object]:
    """Bind an existing-issue route to one validated, read-only projection.

    The function never creates authority or mutation permission. It does not
    inspect issue titles, bodies, labels, assignees, comments, or permissions.
    """

    declared_targets = sorted(set(matched_issue_ids))
    base_reasons = list(dict.fromkeys(declared_reason_codes))
    result: dict[str, object] = {
        "closed_issue_ids": [],
        "declared_disposition": declared_disposition,
        "declared_target_issue_ids": declared_targets,
        "disposition": declared_disposition,
        "inventory_status": "NOT_REQUIRED",
        "missing_issue_ids": [],
        "reason_codes": base_reasons,
        "target_issue_ids": declared_targets,
    }

    if declared_disposition != "UPDATE_EXISTING_ISSUE":
        return result

    if projection is None:
        result.update(
            {
                "disposition": "HOLD_FOR_DEPENDENCY",
                "inventory_status": "REQUIRED",
                "reason_codes": base_reasons
                + ["ISSUE_INVENTORY_REQUIRED"],
                "target_issue_ids": [],
            }
        )
        return result

    issues = projection.get("issues")
    if not isinstance(issues, list):
        result.update(
            {
                "disposition": "HOLD_FOR_DEPENDENCY",
                "inventory_status": "INVALID",
                "reason_codes": base_reasons
                + ["ISSUE_INVENTORY_INVALID"],
                "target_issue_ids": [],
            }
        )
        return result

    state_by_number = {
        issue["number"]: issue["state"]
        for issue in issues
        if (
            isinstance(issue, Mapping)
            and isinstance(issue.get("number"), int)
            and isinstance(issue.get("state"), str)
        )
    }
    missing = [
        number for number in declared_targets
        if number not in state_by_number
    ]
    closed = [
        number for number in declared_targets
        if state_by_number.get(number) == "CLOSED"
    ]
    opened = [
        number for number in declared_targets
        if state_by_number.get(number) == "OPEN"
    ]
    result["missing_issue_ids"] = missing
    result["closed_issue_ids"] = closed

    if missing:
        result.update(
            {
                "disposition": "HOLD_FOR_DEPENDENCY",
                "inventory_status": "TARGET_MISSING",
                "reason_codes": base_reasons
                + ["ISSUE_INVENTORY_TARGET_MISSING"],
                "target_issue_ids": [],
            }
        )
        return result
    if not opened:
        result.update(
            {
                "disposition": "HOLD_FOR_DEPENDENCY",
                "inventory_status": "TARGET_CLOSED",
                "reason_codes": base_reasons
                + ["ISSUE_INVENTORY_TARGET_CLOSED"],
                "target_issue_ids": [],
            }
        )
        return result
    if len(opened) > 1:
        result.update(
            {
                "disposition": "HOLD_FOR_DEPENDENCY",
                "inventory_status": "AMBIGUOUS_OPEN_TARGETS",
                "reason_codes": base_reasons
                + ["ISSUE_INVENTORY_AMBIGUOUS_OPEN_TARGETS"],
                "target_issue_ids": [],
            }
        )
        return result

    result.update(
        {
            "inventory_status": "BOUND_OPEN_TARGET",
            "reason_codes": base_reasons
            + ["ISSUE_INVENTORY_OPEN_TARGET"],
            "target_issue_ids": opened,
        }
    )
    return result


def _serialize_report(
    result: ValidationResult,
) -> str:
    report: dict[str, object] = {
        "authority_created": False,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "live_state_verified": False,
        "repository_mutation_allowed": False,
        "scope": SCOPE,
        "status": "PASS" if result.ok else "FAIL",
    }
    if result.ok and result.payload is not None:
        report["projection"] = projection_summary(result.payload)
    return _canonical_json(report)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a local read-only BriefingSignal issue inventory "
            "projection."
        )
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)

    reports: list[dict[str, object]] = []
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_projection(path)
        failed = failed or not result.ok
        reports.append(json.loads(_serialize_report(result)))

    if len(reports) == 1:
        print(_canonical_json(reports[0]))
    else:
        print(
            _canonical_json(
                {
                    "authority_created": False,
                    "repository_mutation_allowed": False,
                    "results": reports,
                    "scope": SCOPE,
                    "status": "FAIL" if failed else "PASS",
                }
            )
        )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
