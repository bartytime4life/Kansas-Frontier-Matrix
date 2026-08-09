#!/usr/bin/env python3
"""Validate fixture-first, no-network BriefingSignal IssueProjectionReceipt records."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

PROFILE = "kfm.briefing.issue-projection-receipt.v1"
SCHEMA_VERSION = "1.0.0"
SCOPE = "briefing-issue-projection-receipt"
MAX_JSON_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 100
CANONICAL_UTC_SECOND = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
RECEIPT_ID_PATTERN = re.compile(r"^kfm:issue-projection-receipt:[0-9a-f]{24}$")
DIGEST_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
OPEN_OPERATIONS = {
    "OPEN_SOURCE_DISCOVERY_ISSUE",
    "OPEN_OBJECT_MODEL_ISSUE",
    "OPEN_CORRECTIVE_ISSUE",
}
EXPECTED_OUTCOME = {
    "UPDATE_EXISTING_ISSUE": "PROPOSED",
    "OPEN_SOURCE_DISCOVERY_ISSUE": "PROPOSED",
    "OPEN_OBJECT_MODEL_ISSUE": "PROPOSED",
    "OPEN_CORRECTIVE_ISSUE": "PROPOSED",
    "HOLD_FOR_DEPENDENCY": "HELD",
    "REJECT_UNSAFE": "REJECTED",
    "NO_ACTION": "NO_ACTION",
    "ERROR": "ERROR",
}

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str

@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    payload: Mapping[str, object] | None

    @property
    def ok(self) -> bool:
        return not self.findings and self.payload is not None

class DuplicateKeyError(ValueError):
    pass

class NonFiniteNumberError(ValueError):
    pass

def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
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
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"

def canonical_json(value: object) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )

def canonical_receipt_payload(receipt: Mapping[str, object]) -> dict[str, object]:
    return {
        key: receipt[key]
        for key in sorted(receipt)
        if key not in {"receipt_id", "receipt_digest"}
    }

def compute_receipt_digest(receipt: Mapping[str, object]) -> str:
    payload = canonical_receipt_payload(receipt)
    digest = hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()
    return f"sha256:{digest}"

def compute_receipt_id(receipt: Mapping[str, object]) -> str:
    digest = compute_receipt_digest(receipt).removeprefix("sha256:")
    return f"kfm:issue-projection-receipt:{digest[:24]}"

def _is_canonical_utc_second(value: object) -> bool:
    if not isinstance(value, str) or CANONICAL_UTC_SECOND.fullmatch(value) is None:
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.isoformat(timespec="seconds").replace("+00:00", "Z") == value

def _load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
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
    receipt: Mapping[str, object],
) -> list[Finding]:
    try:
        errors = list(islice(validator.iter_errors(receipt), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_EVALUATION_LIMIT", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors,
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )[:MAX_SCHEMA_FINDINGS]
    findings = [
        Finding("SCHEMA_INVALID", _json_pointer(error.absolute_path))
        for error in errors
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings

def _list_of_ints(value: object) -> list[int]:
    if not isinstance(value, list):
        return []
    return [
        item
        for item in value
        if isinstance(item, int) and not isinstance(item, bool)
    ]

def _semantic_findings(receipt: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    if not _is_canonical_utc_second(receipt.get("recorded_at")):
        findings.append(
            Finding("RECORDED_AT_NOT_CANONICAL_UTC_SECOND", "/recorded_at")
        )

    projection = receipt.get("projection")
    inventory = receipt.get("inventory")
    if not isinstance(projection, Mapping) or not isinstance(inventory, Mapping):
        return findings

    declared = projection.get("declared_operation")
    projected = projection.get("projected_operation")
    outcome = projection.get("outcome")
    inventory_kind = inventory.get("kind")
    inventory_status = inventory.get("status")
    declared_targets = _list_of_ints(
        projection.get("declared_target_issue_ids")
    )
    targets = _list_of_ints(projection.get("target_issue_ids"))
    closed = _list_of_ints(projection.get("closed_issue_ids"))
    missing = _list_of_ints(projection.get("missing_issue_ids"))
    reasons = projection.get("reason_codes")

    for field, values in (
        ("declared_target_issue_ids", declared_targets),
        ("target_issue_ids", targets),
        ("closed_issue_ids", closed),
        ("missing_issue_ids", missing),
    ):
        if values != sorted(set(values)):
            findings.append(
                Finding("ISSUE_IDS_NOT_SORTED_UNIQUE", f"/projection/{field}")
            )
    if isinstance(reasons, list) and reasons != sorted(set(reasons)):
        findings.append(
            Finding("REASON_CODES_NOT_SORTED_UNIQUE", "/projection/reason_codes")
        )
    if isinstance(reasons, list) and "ISSUE_PROJECTION_DRY_RUN" not in reasons:
        findings.append(
            Finding(
                "DRY_RUN_REASON_REQUIRED",
                "/projection/reason_codes",
            )
        )

    declared_set = set(declared_targets)
    target_set = set(targets)
    closed_set = set(closed)
    missing_set = set(missing)
    if not target_set.issubset(declared_set):
        findings.append(
            Finding("TARGET_NOT_DECLARED", "/projection/target_issue_ids")
        )
    if not closed_set.issubset(declared_set):
        findings.append(
            Finding("CLOSED_NOT_DECLARED", "/projection/closed_issue_ids")
        )
    if not missing_set.issubset(declared_set):
        findings.append(
            Finding("MISSING_NOT_DECLARED", "/projection/missing_issue_ids")
        )
    if target_set & (closed_set | missing_set):
        findings.append(
            Finding("TARGET_STATE_OVERLAP", "/projection/target_issue_ids")
        )
    if closed_set & missing_set:
        findings.append(
            Finding("CLOSED_MISSING_OVERLAP", "/projection")
        )

    if isinstance(projected, str):
        expected = EXPECTED_OUTCOME.get(projected)
        if expected is not None and outcome != expected:
            findings.append(
                Finding("OUTCOME_OPERATION_MISMATCH", "/projection/outcome")
            )

    if declared != projected and not (
        declared == "UPDATE_EXISTING_ISSUE"
        and projected == "HOLD_FOR_DEPENDENCY"
    ):
        findings.append(
            Finding(
                "DECLARED_PROJECTED_OPERATION_MISMATCH",
                "/projection/projected_operation",
            )
        )

    if projected == "UPDATE_EXISTING_ISSUE":
        if inventory_kind != "FIXTURE_PROJECTION":
            findings.append(
                Finding("UPDATE_REQUIRES_FIXTURE_INVENTORY", "/inventory/kind")
            )
        if inventory_status != "BOUND_OPEN_TARGET":
            findings.append(
                Finding("UPDATE_REQUIRES_BOUND_OPEN_TARGET", "/inventory/status")
            )
        if len(targets) != 1 or targets != declared_targets:
            findings.append(
                Finding(
                    "UPDATE_TARGET_CARDINALITY_INVALID",
                    "/projection/target_issue_ids",
                )
            )
        if closed or missing:
            findings.append(
                Finding(
                    "UPDATE_TARGET_STATE_INVALID",
                    "/projection",
                )
            )
        if isinstance(reasons, list) and "ISSUE_INVENTORY_OPEN_TARGET" not in reasons:
            findings.append(
                Finding(
                    "UPDATE_OPEN_TARGET_REASON_REQUIRED",
                    "/projection/reason_codes",
                )
            )

    if projected in OPEN_OPERATIONS:
        if declared_targets or targets or closed or missing:
            findings.append(
                Finding(
                    "OPEN_OPERATION_EXISTING_TARGET_FORBIDDEN",
                    "/projection",
                )
            )
        if inventory_kind != "NOT_APPLICABLE":
            findings.append(
                Finding(
                    "OPEN_OPERATION_INVENTORY_FORBIDDEN",
                    "/inventory/kind",
                )
            )

    if projected == "HOLD_FOR_DEPENDENCY":
        if targets:
            findings.append(
                Finding("HOLD_TARGET_FORBIDDEN", "/projection/target_issue_ids")
            )
        if declared == "UPDATE_EXISTING_ISSUE":
            if not declared_targets:
                findings.append(
                    Finding(
                        "HELD_UPDATE_DECLARED_TARGET_REQUIRED",
                        "/projection/declared_target_issue_ids",
                    )
                )
            if inventory_status == "NOT_REQUIRED":
                findings.append(
                    Finding(
                        "HELD_UPDATE_INVENTORY_STATUS_INVALID",
                        "/inventory/status",
                    )
                )
            if inventory_kind not in {"MISSING", "FIXTURE_PROJECTION"}:
                findings.append(
                    Finding(
                        "HELD_UPDATE_INVENTORY_KIND_INVALID",
                        "/inventory/kind",
                    )
                )
        elif inventory_kind != "NOT_APPLICABLE":
            findings.append(
                Finding(
                    "DECLARED_HOLD_INVENTORY_FORBIDDEN",
                    "/inventory/kind",
                )
            )

    if projected in {"REJECT_UNSAFE", "NO_ACTION", "ERROR"}:
        if declared_targets or targets or closed or missing:
            findings.append(
                Finding(
                    "NON_TARGET_OPERATION_ISSUE_IDS_FORBIDDEN",
                    "/projection",
                )
            )
        if inventory_kind != "NOT_APPLICABLE":
            findings.append(
                Finding(
                    "NON_TARGET_OPERATION_INVENTORY_FORBIDDEN",
                    "/inventory/kind",
                )
            )

    if inventory_kind == "MISSING" and inventory_status != "REQUIRED":
        findings.append(
            Finding("MISSING_INVENTORY_STATUS_INVALID", "/inventory/status")
        )
    if inventory_kind == "FIXTURE_PROJECTION":
        if inventory_status == "TARGET_CLOSED" and not closed:
            findings.append(
                Finding("CLOSED_STATUS_REQUIRES_CLOSED_ID", "/projection/closed_issue_ids")
            )
        if inventory_status == "TARGET_MISSING" and not missing:
            findings.append(
                Finding("MISSING_STATUS_REQUIRES_MISSING_ID", "/projection/missing_issue_ids")
            )
        if inventory_status == "AMBIGUOUS_OPEN_TARGETS" and len(declared_targets) < 2:
            findings.append(
                Finding(
                    "AMBIGUOUS_STATUS_REQUIRES_MULTIPLE_DECLARED_TARGETS",
                    "/projection/declared_target_issue_ids",
                )
            )

    digest = receipt.get("receipt_digest")
    receipt_id = receipt.get("receipt_id")
    if isinstance(digest, str) and DIGEST_PATTERN.fullmatch(digest):
        if digest != compute_receipt_digest(receipt):
            findings.append(
                Finding("RECEIPT_DIGEST_MISMATCH", "/receipt_digest")
            )
    if isinstance(receipt_id, str) and RECEIPT_ID_PATTERN.fullmatch(receipt_id):
        if receipt_id != compute_receipt_id(receipt):
            findings.append(
                Finding("RECEIPT_ID_MISMATCH", "/receipt_id")
            )
    return findings

def validate_payload(
    receipt: Mapping[str, object],
    *,
    schema_path: Path,
) -> ValidationResult:
    """Validate an in-memory receipt without performing any external effects."""

    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return ValidationResult(
            (Finding("SCHEMA_UNAVAILABLE", "/"),),
            None,
        )
    schema_findings = _schema_findings(validator, receipt)
    if schema_findings:
        return ValidationResult(tuple(sorted(schema_findings)), None)
    semantic_findings = _semantic_findings(receipt)
    return ValidationResult(
        tuple(sorted(set(semantic_findings))),
        receipt if not semantic_findings else None,
    )

def validate_receipt(
    path: Path,
    *,
    schema_path: Path,
) -> ValidationResult:
    receipt, load_findings = _load_json_object(path)
    if receipt is None:
        return ValidationResult(tuple(sorted(load_findings)), None)
    return validate_payload(receipt, schema_path=schema_path)

def serialize_report(result: ValidationResult) -> str:
    return canonical_json(
        {
            "authority_created": False,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "repository_mutation_allowed": False,
            "scope": SCOPE,
            "status": "PASS" if result.ok else "FAIL",
        }
    )

def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve()
    repo_root = here.parents[3]
    default_schema = (
        repo_root
        / "schemas/contracts/v1/governance/issue_projection_receipt.schema.json"
    )
    parser = argparse.ArgumentParser(
        description="Validate local IssueProjectionReceipt records."
    )
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--schema", type=Path, default=default_schema)
    args = parser.parse_args(argv)
    reports: list[dict[str, object]] = []
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_receipt(path, schema_path=args.schema)
        reports.append(json.loads(serialize_report(result)))
        failed = failed or not result.ok
    print(canonical_json(reports))
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
