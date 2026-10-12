#!/usr/bin/env python3
"""Validate fixture-first temporal support assessments."""
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
SCHEMA = REPO_ROOT / "schemas/contracts/v1/evidence/temporal_support_assessment.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/evidence/temporal_support_assessment"
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


def semantic_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    if value.get("spec_hash") != canonical_hash(value):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    query = value.get("query")
    support = value.get("support")
    release = value.get("release_state")
    evaluated = _time(value.get("evaluated_at"))
    if not isinstance(query, dict) or not isinstance(support, dict) or not isinstance(release, dict) or evaluated is None:
        return findings + [Finding("TEMPORAL_FIELDS_INVALID", "/")]

    q_start, q_end = _time(query.get("start")), _time(query.get("end"))
    valid = support.get("valid_time")
    v_start = _time(valid.get("start")) if isinstance(valid, dict) else None
    v_end = _time(valid.get("end")) if isinstance(valid, dict) else None
    updated = _time(support.get("source_updated_at"))
    retrieved = _time(support.get("retrieved_at"))
    if None in {q_start, q_end, v_start, v_end, updated, retrieved}:
        findings.append(Finding("TEMPORAL_TIMESTAMP_INVALID", "/"))
        return findings
    assert q_start and q_end and v_start and v_end and updated and retrieved
    if q_start > q_end:
        findings.append(Finding("QUERY_INTERVAL_INVALID", "/query"))
    if v_start > v_end:
        findings.append(Finding("VALID_INTERVAL_INVALID", "/support/valid_time"))
    if updated > retrieved:
        findings.append(Finding("SOURCE_UPDATE_AFTER_RETRIEVAL", "/support/source_updated_at"))
    if retrieved > evaluated:
        findings.append(Finding("RETRIEVAL_AFTER_EVALUATION", "/support/retrieved_at"))

    conflicts = value.get("conflict_refs")
    basis_complete = support.get("temporal_basis_complete") is True
    out_of_scope = q_start < v_start or q_end > v_end or release.get("status") == "WITHDRAWN"
    ttl = support.get("freshness_ttl_seconds")
    stale = isinstance(ttl, int) and (evaluated - updated).total_seconds() > ttl
    if isinstance(conflicts, list) and conflicts:
        derived = "CONFLICTED"
    elif not basis_complete:
        derived = "UNKNOWN"
    elif out_of_scope:
        derived = "OUT_OF_SCOPE"
    elif stale:
        derived = "STALE"
    else:
        derived = "SUPPORTED"
    if value.get("outcome") != derived:
        findings.append(Finding("TEMPORAL_OUTCOME_MISMATCH", "/outcome"))

    required_reason = {
        "STALE": "TEMPORAL_STALE",
        "OUT_OF_SCOPE": "TEMPORAL_OUT_OF_SCOPE",
        "CONFLICTED": "TEMPORAL_CONFLICT",
        "UNKNOWN": "TEMPORAL_BASIS_INCOMPLETE",
    }.get(derived)
    reasons = value.get("reason_codes")
    obligations = value.get("obligations")
    if required_reason and (not isinstance(reasons, list) or required_reason not in reasons):
        findings.append(Finding("TEMPORAL_REASON_REQUIRED", "/reason_codes"))
    if derived != "SUPPORTED" and (not isinstance(obligations, list) or not obligations):
        findings.append(Finding("TEMPORAL_OBLIGATION_REQUIRED", "/obligations"))
    if derived == "CONFLICTED" and (not isinstance(conflicts, list) or len(conflicts) < 2):
        findings.append(Finding("TEMPORAL_CONFLICT_REFS_INSUFFICIENT", "/conflict_refs"))

    status = release.get("status")
    if status in {"CORRECTED", "WITHDRAWN", "SUPERSEDED"} and release.get("correction_ref") is None:
        findings.append(Finding("CORRECTION_REF_REQUIRED", "/release_state/correction_ref"))
    if status == "SUPERSEDED" and release.get("superseded_by_ref") is None:
        findings.append(Finding("SUPERSEDED_BY_REF_REQUIRED", "/release_state/superseded_by_ref"))
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
    return json.dumps({"file": display, "findings": [{"code": item.code, "path": item.path} for item in result.findings], "outcome": "PASS" if result.ok else "FAIL", "scope": "temporal-support-fixture-only"}, sort_keys=True, separators=(",", ":"))


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
