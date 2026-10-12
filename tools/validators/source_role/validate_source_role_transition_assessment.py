#!/usr/bin/env python3
"""Validate fixture-first source-role transition assessments."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA = REPO_ROOT / "schemas/contracts/v1/source/source_role_transition_assessment.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/source/source_role_transition_assessment"
MAX_BYTES = 2 * 1024 * 1024


class DuplicateKeyError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _pointer(parts: Iterable[object]) -> str:
    values = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(values) if values else "/"


def read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(value))
    payload.pop("spec_hash", None)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00").astimezone(timezone.utc)
    except ValueError:
        return None


def schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:100]]


def _derive(value: Mapping[str, Any]) -> tuple[str, str | None]:
    operation = value.get("operation")
    inputs = value.get("inputs")
    output = value.get("output")
    receipts = value.get("receipts")
    if not isinstance(inputs, list) or not isinstance(output, dict) or not isinstance(receipts, dict):
        return "ERROR", "SOURCE_ROLE_FIELDS_INVALID"
    roles = {item.get("source_role") for item in inputs if isinstance(item, dict)}
    output_role = output.get("source_role")
    if "CANDIDATE" in roles and operation in {"AGGREGATE", "MODEL", "SYNTHESIZE", "PROMOTE_LIFECYCLE"}:
        return "HOLD", "CANDIDATE_INPUT_REQUIRES_RESOLUTION"
    if operation in {"PASSTHROUGH", "GENERALIZE", "PROMOTE_LIFECYCLE"}:
        if len(roles) != 1:
            return "DENY", "SOURCE_ROLE_MULTI_INPUT_COLLAPSE_DENIED"
        if output_role not in roles:
            return "DENY", "SOURCE_ROLE_UPGRADE_DENIED"
        return "PASS", None
    if operation == "AGGREGATE":
        if output_role != "AGGREGATE":
            return "DENY", "AGGREGATE_OUTPUT_ROLE_REQUIRED"
        if receipts.get("aggregation_receipt_ref") is None:
            return "HOLD", "AGGREGATION_RECEIPT_REQUIRED"
        return "PASS", None
    if operation == "MODEL":
        if output_role != "MODELED":
            return "DENY", "MODELED_OUTPUT_ROLE_REQUIRED"
        if receipts.get("model_run_receipt_ref") is None:
            return "HOLD", "MODEL_RUN_RECEIPT_REQUIRED"
        return "PASS", None
    if operation == "SYNTHESIZE":
        if output_role != "SYNTHETIC":
            return "DENY", "SYNTHETIC_OUTPUT_ROLE_REQUIRED"
        if receipts.get("representation_receipt_ref") is None or receipts.get("reality_boundary_note_ref") is None:
            return "HOLD", "SYNTHETIC_BOUNDARY_SUPPORT_REQUIRED"
        return "PASS", None
    return "ERROR", "SOURCE_ROLE_OPERATION_UNKNOWN"


def semantic_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    if value.get("spec_hash") != canonical_hash(value):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    inputs = value.get("inputs")
    output = value.get("output")
    if isinstance(inputs, list):
        refs = [item.get("source_ref") for item in inputs if isinstance(item, dict)]
        if len(refs) != len(set(refs)):
            findings.append(Finding("SOURCE_ROLE_INPUT_DUPLICATE", "/inputs"))
        input_roles = {item.get("source_role") for item in inputs if isinstance(item, dict)}
        lineage = set(output.get("lineage_roles", [])) if isinstance(output, dict) else set()
        if input_roles != lineage:
            findings.append(Finding("SOURCE_ROLE_LINEAGE_MISMATCH", "/output/lineage_roles"))

    if value.get("outcome") == "ERROR":
        if value.get("validator_error_ref") is None:
            findings.append(Finding("SOURCE_ROLE_ERROR_REF_REQUIRED", "/validator_error_ref"))
        return findings

    derived, reason = _derive(value)
    if value.get("outcome") != derived:
        findings.append(Finding("SOURCE_ROLE_OUTCOME_MISMATCH", "/outcome"))
    reasons = value.get("reason_codes")
    if reason and (not isinstance(reasons, list) or reason not in reasons):
        findings.append(Finding("SOURCE_ROLE_REASON_REQUIRED", "/reason_codes"))
    if derived == "HOLD" and (not isinstance(value.get("obligations"), list) or not value.get("obligations")):
        findings.append(Finding("SOURCE_ROLE_HOLD_OBLIGATION_REQUIRED", "/obligations"))
    if derived == "PASS" and isinstance(reasons, list) and reasons:
        findings.append(Finding("SOURCE_ROLE_PASS_REASON_UNEXPECTED", "/reason_codes"))
    if _time(value.get("evaluated_at")) is None:
        findings.append(Finding("SOURCE_ROLE_TIME_INVALID", "/evaluated_at"))
    return findings


def validate(path: Path) -> Result:
    value, findings = read(path)
    if value is None:
        return Result(tuple(sorted(set(findings))))
    findings.extend(schema_findings(value))
    if not findings:
        findings.extend(semantic_findings(value))
    return Result(tuple(sorted(set(findings))))


def serialize(path: Path, result: Result) -> str:
    try:
        display = path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        display = path.name
    return json.dumps({"file": display, "findings": [{"code": item.code, "path": item.path} for item in result.findings], "outcome": "PASS" if result.ok else "FAIL", "scope": "source-role-transition-fixture-only"}, sort_keys=True, separators=(",", ":"))


def fixture_profile() -> int:
    valid = sorted((FIXTURES / "valid").glob("*.json"))
    invalid = sorted((FIXTURES / "invalid").glob("*.json"))
    if not valid or not invalid:
        return 1
    ok = True
    for path in valid:
        result = validate(path)
        print(serialize(path, result))
        ok = result.ok and ok
    for path in invalid:
        result = validate(path)
        print(serialize(path, result))
        ok = (not result.ok) and ok
    return 0 if ok else 1


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return fixture_profile()
    if not args.files:
        parser.error("provide files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        result = validate(path)
        print(serialize(path, result))
        rc = max(rc, 0 if result.ok else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
