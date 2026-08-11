#!/usr/bin/env python3
"""Validate the inactive, fixture-only DrinkingWaterAdvisory profile.

PASS proves bounded local coherence only. It does not establish current health
status, activate a source, clear a live advisory, issue an alert, write
lifecycle state, release, deploy, publish, or authorize public use.
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

ROOT = Path(__file__).resolve().parents[4]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError as exc:
    compute_spec_hash = None  # type: ignore[assignment]
    HASH_ERROR: Exception | None = exc
else:
    HASH_ERROR = None

SCHEMA = (
    ROOT
    / "schemas/contracts/v1/domains/hazards/drinking_water_advisory.schema.json"
)
CASES = ROOT / "fixtures/domains/hazards/drinking_water_advisory/cases.json"
COMMON_CONTRACT = ROOT / "contracts/common/advisory_event_envelope.md"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "drinking-water-advisory-fixture-only-v1"
CONFIRMED_STATUSES = {
    "ISSUED",
    "ACTIVE_CONFIRMED",
    "UPDATED",
    "RESCINDED",
}
SOURCE_FAILURES = {
    "NOT_FOUND",
    "ACCESS_DENIED",
    "RATE_LIMITED",
    "MALFORMED",
    "STATUS_CHECK_FAILED",
}
FALSE_EFFECTS = {
    "source_activated": False,
    "evidence_resolved": False,
    "policy_evaluated": False,
    "health_determined": False,
    "lifecycle_written": False,
    "alert_issued": False,
    "released": False,
    "deployed": False,
    "published": False,
}
ERROR_CODES = {
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_INVALID",
    "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
    "HASHING_UNAVAILABLE",
    "SPEC_HASH_MISMATCH",
    "ADVISORY_ID_MISMATCH",
    "FIXTURE_MANIFEST_INVALID",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _nonfinite(_: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_float,
        )
    except UnicodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1")
        for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema,
                    format_checker=FormatChecker(),
                ).iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda error: (
                _pointer(error.absolute_path),
                str(error.validator),
            ),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("advisory_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))


def expected_advisory_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "drinking-water-advisory:" + digest[:24]


def assign_identity(candidate: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(candidate)
    result["spec_hash"] = canonical_spec_hash(result)
    result["advisory_id"] = expected_advisory_id(result)
    return result


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _canonical_strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _present_ref(value: Any) -> bool:
    return isinstance(value, str) and bool(value)


def _time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    shared = _mapping(candidate.get("shared_mechanics"))
    source = _mapping(candidate.get("source_surface"))
    identity = _mapping(candidate.get("identity"))
    authority = _mapping(candidate.get("authority"))
    advisory = _mapping(candidate.get("advisory"))
    scope = _mapping(candidate.get("scope"))
    controls = _mapping(candidate.get("controls"))

    if (
        shared.get("contract_ref") != "contracts/common/advisory_event_envelope.md"
        or not COMMON_CONTRACT.is_file()
        or COMMON_CONTRACT.is_symlink()
    ):
        findings.append(Finding("SHARED_MECHANICS_UNAVAILABLE", "/shared_mechanics"))

    status = advisory.get("normalized_status")
    outcome = source.get("source_check_outcome")
    previous_present = source.get("previous_record_present") is True
    current_present = source.get("current_record_present") is True
    clears = advisory.get("clears_prior_advisory") is True

    if status in CONFIRMED_STATUSES:
        if identity.get("resolution_status") != "RESOLVED" or not _present_ref(
            identity.get("public_water_system_ref")
        ):
            findings.append(Finding("SYSTEM_IDENTITY_REQUIRED", "/identity"))
        if (
            authority.get("issuance_authority_status") != "CONFIRMED"
            or not _present_ref(authority.get("issuance_authority_ref"))
            or not _present_ref(authority.get("issue_notice_ref"))
        ):
            findings.append(Finding("ISSUANCE_AUTHORITY_REQUIRED", "/authority"))
        if scope.get("scope_role") != "SERVICE_AREA":
            findings.append(Finding("SERVICE_AREA_REQUIRED", "/scope/scope_role"))
        if (
            not _present_ref(scope.get("service_area_ref"))
            or not _present_ref(scope.get("geometry_ref"))
            or scope.get("geometry_confidence") not in {"CONFIRMED", "APPROXIMATE"}
        ):
            findings.append(Finding("SERVICE_AREA_REQUIRED", "/scope"))

    if identity.get("resolution_status") != "RESOLVED" and _present_ref(
        identity.get("public_water_system_ref")
    ):
        findings.append(Finding("SYSTEM_IDENTITY_OVERCLAIM", "/identity"))
    if status == "IDENTITY_CONFLICT" and identity.get("resolution_status") not in {
        "UNRESOLVED",
        "CONFLICT",
    }:
        findings.append(Finding("IDENTITY_CONFLICT_REQUIRED", "/identity"))

    scope_role = scope.get("scope_role")
    if scope_role == "SERVICE_AREA":
        service_ref = scope.get("service_area_ref")
        admin_ref = scope.get("administrative_area_ref")
        if _present_ref(admin_ref) and service_ref == admin_ref:
            findings.append(Finding("ADMINISTRATIVE_SCOPE_COLLAPSE", "/scope"))
    elif scope_role == "ADMINISTRATIVE_CONTEXT":
        if (
            _present_ref(scope.get("service_area_ref"))
            or not _present_ref(scope.get("administrative_area_ref"))
            or scope.get("geometry_confidence") != "APPROXIMATE"
        ):
            findings.append(Finding("ADMINISTRATIVE_CONTEXT_INVALID", "/scope"))
        if status in CONFIRMED_STATUSES:
            findings.append(Finding("ADMINISTRATIVE_SCOPE_COLLAPSE", "/scope"))
    elif scope_role == "UNRESOLVED":
        if (
            scope.get("service_area_ref") is not None
            or scope.get("administrative_area_ref") is not None
            or scope.get("geometry_ref") is not None
            or scope.get("geometry_confidence") != "UNRESOLVED"
        ):
            findings.append(Finding("UNRESOLVED_SCOPE_OVERCLAIM", "/scope"))

    if outcome in SOURCE_FAILURES:
        if status != "STATUS_UNCONFIRMED" or clears or current_present:
            findings.append(Finding("SOURCE_FAILURE_FALSE_CLEAR", "/source_surface"))
    elif outcome == "SOURCE_CONFLICT":
        if status != "SOURCE_CONFLICT" or clears:
            findings.append(Finding("SOURCE_CONFLICT_REQUIRED", "/advisory"))
    elif status in {"ISSUED", "UPDATED"} and outcome != "FETCHED":
        findings.append(Finding("FETCHED_SOURCE_REQUIRED", "/source_surface/source_check_outcome"))
    elif status == "ACTIVE_CONFIRMED" and outcome not in {"FETCHED", "NOT_MODIFIED"}:
        findings.append(Finding("CURRENT_SOURCE_REQUIRED", "/source_surface/source_check_outcome"))

    absence = (
        source.get("source_mode") == "COMPLETE_SNAPSHOT"
        and source.get("snapshot_complete") is True
        and previous_present
        and not current_present
    )
    if absence and status != "RESCINDED":
        if status != "STATUS_UNCONFIRMED" or clears:
            findings.append(Finding("SOURCE_ABSENCE_FALSE_CLEAR", "/advisory"))
    if status in {"ISSUED", "ACTIVE_CONFIRMED", "UPDATED"} and not current_present:
        findings.append(Finding("CURRENT_RECORD_REQUIRED", "/source_surface/current_record_present"))

    if status == "RESCINDED":
        required_rescission = (
            outcome == "FETCHED"
            and previous_present
            and _present_ref(authority.get("rescission_notice_ref"))
            and _present_ref(authority.get("rescission_authority_ref"))
            and authority.get("rescission_authority_status") == "CONFIRMED"
            and _present_ref(controls.get("prior_advisory_ref"))
            and _time(advisory.get("rescinded_at")) is not None
            and clears
        )
        if not required_rescission:
            findings.append(Finding("RESCISSION_REQUIRED", "/advisory"))
    elif clears:
        findings.append(Finding("FALSE_CLEAR_ATTEMPT", "/advisory/clears_prior_advisory"))

    if previous_present and status != "ISSUED" and not _present_ref(
        controls.get("prior_advisory_ref")
    ):
        findings.append(Finding("PRIOR_LINEAGE_REQUIRED", "/controls/prior_advisory_ref"))
    if status == "STATUS_UNCONFIRMED" and previous_present and advisory.get(
        "last_confirmed_status"
    ) not in {"ISSUED", "ACTIVE_CONFIRMED", "UPDATED"}:
        findings.append(Finding("LAST_CONFIRMED_STATUS_REQUIRED", "/advisory/last_confirmed_status"))

    issued = _time(advisory.get("issued_at"))
    effective = _time(advisory.get("effective_at"))
    expires = _time(advisory.get("expires_at"))
    rescinded = _time(advisory.get("rescinded_at"))
    checked = _time(source.get("checked_at"))
    if (
        issued is None
        or effective is None
        or checked is None
        or issued > effective
        or effective > checked
        or (expires is not None and expires < effective)
        or (rescinded is not None and (rescinded < effective or rescinded > checked))
    ):
        findings.append(Finding("TEMPORAL_ORDER_INVALID", "/advisory"))

    if not _canonical_strings(controls.get("evidence_refs")):
        findings.append(Finding("NONCANONICAL_EVIDENCE_REFS", "/controls/evidence_refs"))
    if not _canonical_strings(candidate.get("limitations")):
        findings.append(Finding("NONCANONICAL_LIMITATIONS", "/limitations"))
    if (
        controls.get("release_state") != "UNRELEASED"
        or controls.get("release_ref") is not None
    ):
        findings.append(Finding("RELEASE_OVERCLAIM", "/controls"))
    if controls.get("public_use_allowed") is not False or controls.get("alerts_allowed") is not False:
        findings.append(Finding("PUBLIC_AUTHORITY_OVERCLAIM", "/controls"))
    if controls.get("not_for_life_safety") is not True:
        findings.append(Finding("LIFE_SAFETY_BOUNDARY_MISSING", "/controls/not_for_life_safety"))
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append(Finding("EFFECT_OVERCLAIM", "/effects"))

    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_advisory_id(candidate)
    except RuntimeError:
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("advisory_id") != expected_id:
            findings.append(Finding("ADVISORY_ID_MISMATCH", "/advisory_id"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    if not ordered:
        return ValidationResult("PASS", ordered)
    return ValidationResult(
        "ERROR" if any(finding.code in ERROR_CODES for finding in ordered) else "DENY",
        ordered,
    )


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        ordered = tuple(sorted(set(findings)))
        return ValidationResult("ERROR", ordered)
    return validate_payload(candidate)


def _decode_pointer(value: Any) -> list[str] | None:
    if not isinstance(value, str) or not value.startswith("/") or value == "/":
        return None
    decoded: list[str] = []
    for raw in value[1:].split("/"):
        output: list[str] = []
        index = 0
        while index < len(raw):
            if raw[index] != "~":
                output.append(raw[index])
                index += 1
            elif index + 1 < len(raw) and raw[index + 1] in {"0", "1"}:
                output.append("~" if raw[index + 1] == "0" else "/")
                index += 2
            else:
                return None
        decoded.append("".join(output))
    return decoded


def _apply_mutation(candidate: dict[str, Any], mutation: Mapping[str, Any]) -> bool:
    parts = _decode_pointer(mutation.get("path"))
    if parts is None or "value" not in mutation:
        return False
    parent: Any = candidate
    for part in parts[:-1]:
        if not isinstance(parent, dict) or part not in parent:
            return False
        parent = parent[part]
    if not isinstance(parent, dict) or parts[-1] not in parent:
        return False
    parent[parts[-1]] = copy.deepcopy(mutation["value"])
    return True


def load_fixture_cases() -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document, findings = _read(CASES)
    if document is None or findings:
        raise ValueError("fixture manifest unreadable")
    bases = document.get("bases")
    cases = document.get("cases")
    if (
        document.get("profile") != "kfm.drinking-water-advisory.fixtures.v1"
        or not isinstance(bases, Mapping)
        or not isinstance(cases, list)
        or not bases
        or not cases
    ):
        raise ValueError("fixture manifest invalid")
    materialized: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("fixture case invalid")
        name = case.get("name")
        base_name = case.get("base")
        mutations = case.get("mutations")
        expected = case.get("expected_outcome")
        expected_findings = case.get("expected_findings")
        if (
            not isinstance(name, str)
            or not name
            or name in names
            or not isinstance(base_name, str)
            or base_name not in bases
            or not isinstance(bases[base_name], Mapping)
            or not isinstance(mutations, list)
            or expected not in {"PASS", "DENY", "ERROR"}
            or not isinstance(expected_findings, list)
            or any(not isinstance(code, str) for code in expected_findings)
            or expected_findings != sorted(set(expected_findings))
        ):
            raise ValueError("fixture case invalid")
        candidate = copy.deepcopy(dict(bases[base_name]))
        for mutation in mutations:
            if not isinstance(mutation, Mapping) or not _apply_mutation(candidate, mutation):
                raise ValueError("fixture mutation invalid")
        candidate = assign_identity(candidate)
        if case.get("identity_mode") == "MISMATCH_SPEC_HASH":
            candidate["spec_hash"] = "sha256:" + "0" * 64
        elif case.get("identity_mode") not in {None, "ASSIGN"}:
            raise ValueError("fixture identity mode invalid")
        names.add(name)
        materialized.append((case, candidate))
    return materialized


def _render(name: str, result: ValidationResult) -> dict[str, Any]:
    return {
        "name": name,
        "outcome": result.outcome,
        "findings": sorted({finding.code for finding in result.findings}),
        "scope": SCOPE,
        "authority": {
            "network_fetch": False,
            "source_activation": False,
            "health_determination": False,
            "alert_authority": False,
            "lifecycle_write": False,
            "release": False,
            "deployment": False,
            "publication": False,
            "public_use": False,
        },
    }


def validate_fixtures() -> tuple[bool, list[dict[str, Any]]]:
    try:
        cases = load_fixture_cases()
    except ValueError:
        result = ValidationResult(
            "ERROR",
            (Finding("FIXTURE_MANIFEST_INVALID", "/"),),
        )
        return False, [_render("fixture_manifest", result)]
    rows: list[dict[str, Any]] = []
    ok = True
    for case, candidate in cases:
        result = validate_payload(candidate)
        row = _render(case["name"], result)
        rows.append(row)
        case_ok = (
            result.outcome == case["expected_outcome"]
            and row["findings"] == case["expected_findings"]
        )
        ok = ok and case_ok
    return ok, rows


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate inactive DrinkingWaterAdvisory fixtures."
    )
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        ok, rows = validate_fixtures()
        for row in rows:
            print(json.dumps(row, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if not args.paths:
        return 2
    ok = True
    for path in args.paths:
        result = validate_file(path)
        print(
            json.dumps(
                _render(path.name, result),
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        ok = ok and result.ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
