#!/usr/bin/env python3
"""Validate fixture-only field-level API authorization assessments.

A PASS proves only that declared field projections match a bounded synthetic
decision context. It does not create a route, authenticate a user, execute
policy, inspect values, emit a response, release, or publish.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/release/field_level_api_authorization_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/release/field_level_api_authorization_assessment/cases.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:field-level-api-authorization:"
SURFACE_BY_OPERATION = {
    "READ": "API_RESPONSE",
    "ANSWER": "AI_ANSWER",
    "EXPORT": "EXPORT",
    "DRAWER": "EVIDENCE_DRAWER",
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    assessment_state: str | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("FIELD_AUTH_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("FIELD_AUTH_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("FIELD_AUTH_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("FIELD_AUTH_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("FIELD_AUTH_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("FIELD_AUTH_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("FIELD_AUTH_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("FIELD_AUTH_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"assessment_id", "spec_hash"}}
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def expected_summary(value: Mapping[str, Any]) -> dict[str, Any]:
    fields = value["fields"]
    counts = {name: 0 for name in ("PUBLIC", "ROLE_SCOPED", "EMBARGOED", "NEVER_RETURN")}
    for field in fields:
        counts[field["classification"]] += 1
    return {
        "requested_count": sum(1 for field in fields if field["requested"]),
        "projected_count": sum(1 for field in fields if field["projected"]),
        "withheld_count": sum(1 for field in fields if field["requested"] and not field["projected"]),
        "classification_counts": counts,
        "assessment_state": "REVIEW_REQUIRED",
        "response_emitted": False,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("FIELD_AUTH_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("FIELD_AUTH_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("FIELD_AUTH_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _time(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")


def expected_field_decision(
    field: Mapping[str, Any],
    request_context: Mapping[str, Any],
    decision_context: Mapping[str, Any],
) -> tuple[bool, str]:
    if not field["requested"]:
        return False, "NOT_REQUESTED"
    if field["source_state"] != "PUBLISHED":
        return False, "SOURCE_NOT_PUBLISHED"
    if field["classification"] == "NEVER_RETURN":
        return False, "NEVER_RETURN"
    if field["classification"] == "EMBARGOED":
        embargo_until = field["embargo_until"]
        if embargo_until is None or _time(decision_context["evaluated_at"]) < _time(embargo_until):
            return False, "EMBARGO_ACTIVE"
    if decision_context["policy_outcome"] != "ANSWER":
        return False, "POLICY_NOT_ANSWER"

    if field["classification"] == "PUBLIC":
        projected_reason = "PROJECTED_PUBLIC"
    elif field["classification"] == "ROLE_SCOPED":
        if decision_context["grant_state"] != "ACTIVE":
            return False, "GRANT_INACTIVE"
        if field["required_role"] != request_context["audience_role"]:
            return False, "ROLE_MISMATCH"
        projected_reason = "PROJECTED_ROLE_MATCH"
    else:
        required_role = field["required_role"]
        if required_role is not None:
            if decision_context["grant_state"] != "ACTIVE":
                return False, "GRANT_INACTIVE"
            if required_role != request_context["audience_role"]:
                return False, "ROLE_MISMATCH"
        projected_reason = "PROJECTED_EMBARGO_EXPIRED"

    if field["evidence_ref"] is None:
        return False, "EVIDENCE_MISSING"
    return True, projected_reason


def _semantic_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    request_context = value["request_context"]
    decision_context = value["decision_context"]
    fields = value["fields"]

    if value["downstream_surface"] != SURFACE_BY_OPERATION[request_context["operation"]]:
        findings.add(Finding("FIELD_AUTH_OPERATION_SURFACE_MISMATCH", "/downstream_surface"))

    role_refs = [
        request_context["capability_ref"],
        request_context["api_contract_ref"],
        decision_context["policy_decision_ref"],
    ]
    if decision_context["obligation_set_ref"] is not None:
        role_refs.append(decision_context["obligation_set_ref"])
    if len(role_refs) != len(set(role_refs)):
        findings.add(Finding("FIELD_AUTH_REFERENCE_ROLE_COLLAPSE", "/decision_context"))

    field_names = [field["field_name"] for field in fields]
    if field_names != sorted(field_names):
        findings.add(Finding("FIELD_AUTH_FIELD_ORDER_INVALID", "/fields"))
    if len(field_names) != len(set(field_names)):
        findings.add(Finding("FIELD_AUTH_FIELD_NAME_DUPLICATE", "/fields"))

    for index, field in enumerate(fields):
        base = f"/fields/{index}"
        if field["obligation_refs"] != sorted(field["obligation_refs"]):
            findings.add(Finding("FIELD_AUTH_OBLIGATIONS_NOT_CANONICAL", f"{base}/obligation_refs"))

        classification = field["classification"]
        if classification == "PUBLIC":
            if field["required_role"] is not None or field["embargo_until"] is not None:
                findings.add(Finding("FIELD_AUTH_PUBLIC_METADATA_INVALID", base))
        elif classification == "ROLE_SCOPED":
            if field["required_role"] is None or field["embargo_until"] is not None:
                findings.add(Finding("FIELD_AUTH_ROLE_SCOPED_METADATA_INVALID", base))
            if not field["obligation_refs"]:
                findings.add(Finding("FIELD_AUTH_OBLIGATION_REQUIRED", f"{base}/obligation_refs"))
        elif classification == "EMBARGOED":
            if field["embargo_until"] is None:
                findings.add(Finding("FIELD_AUTH_EMBARGO_METADATA_INVALID", base))
            if not field["obligation_refs"]:
                findings.add(Finding("FIELD_AUTH_OBLIGATION_REQUIRED", f"{base}/obligation_refs"))
        elif field["required_role"] is not None or field["embargo_until"] is not None:
            findings.add(Finding("FIELD_AUTH_NEVER_RETURN_METADATA_INVALID", base))

        expected = expected_field_decision(field, request_context, decision_context)
        if (field["projected"], field["reason_code"]) != expected:
            findings.add(Finding("FIELD_AUTH_PROJECTION_MISMATCH", base))

    if value["summary"] != expected_summary(value):
        findings.add(Finding("FIELD_AUTH_SUMMARY_MISMATCH", "/summary"))
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)
    findings = _semantic_findings(value)
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("FIELD_AUTH_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("FIELD_AUTH_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("FIELD_AUTH_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    return Result("PASS", "REVIEW_REQUIRED", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", None, findings)
    return validate_payload(value)


def _set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.removeprefix("/").split("/")]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    last = parts[-1]
    if isinstance(cursor, list):
        cursor[int(last)] = replacement
    else:
        cursor[last] = replacement


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if not case.get("preserve_summary", False):
        document["summary"] = expected_summary(document)
    document["spec_hash"], document["assessment_id"] = canonical_identity(document)
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "assessment_id_override" in case:
        document["assessment_id"] = case["assessment_id_override"]
    return document


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    if not isinstance(value, dict):
        raise ValueError("fixture root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": finding.code, "path": finding.path} for finding in result.findings]
        if (
            result.outcome != case["expected_outcome"]
            or result.assessment_state != case["expected_assessment_state"]
            or actual != case["expected_findings"]
        ):
            failures.append({
                "case_id": case["case_id"],
                "expected_outcome": case["expected_outcome"],
                "actual_outcome": result.outcome,
                "expected_assessment_state": case["expected_assessment_state"],
                "actual_assessment_state": result.assessment_state,
                "expected_findings": case["expected_findings"],
                "actual_findings": actual,
            })
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps({
        "authority": {
            "creates_route": False,
            "authenticates": False,
            "executes_policy": False,
            "inspects_field_values": False,
            "emits_response": False,
            "authorizes_release": False,
            "publishes": False,
        },
        "execution_mode": "FIXTURE_ONLY",
        "file": path.as_posix(),
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "outcome": result.outcome,
        "assessment_state": result.assessment_state,
    }, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.input is None:
        raise SystemExit("input is required unless --fixtures is used")
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
