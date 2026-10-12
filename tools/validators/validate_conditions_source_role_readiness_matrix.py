#!/usr/bin/env python3
"""Validate the inactive ConditionsSourceRoleReadinessMatrix profile.

PASS proves bounded local matrix coherence and repository-path presence only.
It does not select a source, resolve evidence, adopt a profile, write lifecycle
state, evaluate policy, release, publish, or authorize public use.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
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
    / "schemas/contracts/v1/common/conditions_source_role_readiness_matrix.schema.json"
)
CASES = (
    ROOT
    / "fixtures/contracts/v1/common/conditions_source_role_readiness_matrix/cases.json"
)
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "conditions-source-role-readiness-matrix-fixture-only-v1"
ROLE_ORDER = (
    "AGGREGATE",
    "CLASSIFICATION",
    "FORECAST",
    "MODEL",
    "OBSERVATION",
    "SURVEY",
)
ROLE_SUPPORT = {
    "AGGREGATE": "AGGREGATE_STATISTIC",
    "CLASSIFICATION": "DERIVED_CLASSIFICATION",
    "FORECAST": "PREDICTION",
    "MODEL": "MODELED_ESTIMATE",
    "OBSERVATION": "DIRECT_MEASUREMENT",
    "SURVEY": "SURVEY_PRODUCT",
}
APPROVED_BOUND_NATIVE = {
    "CLASSIFICATION": ("CLASSIFICATION", "DERIVED_CLASSIFICATION"),
    "FORECAST": ("FORECAST", "PREDICTION"),
    "OBSERVATION": (
        "direct_observation_measurement",
        "station_soil_moisture",
    ),
}
PATH_FIELDS = ("contract_ref", "schema_ref", "validator_ref", "fixture_ref")
MAPPING_FIELDS = (
    "native_source_role",
    "native_support_type",
    "common_source_role",
    "common_support_type",
)
FALSE_EFFECTS = {
    "source_activated": False,
    "evidence_resolved": False,
    "policy_evaluated": False,
    "profile_adopted": False,
    "lifecycle_written": False,
    "promoted": False,
    "released": False,
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
    "MATRIX_ID_MISMATCH",
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
                Draft202012Validator(schema).iter_errors(candidate),
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
    subject.pop("matrix_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))


def expected_matrix_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "conditions-source-role-matrix:" + digest[:24]


def assign_identity(candidate: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(candidate)
    result["spec_hash"] = canonical_spec_hash(result)
    result["matrix_id"] = expected_matrix_id(result)
    return result


def _canonical_strings(value: Any, *, allow_empty: bool) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _safe_repo_path(value: Any) -> Path | None:
    if not isinstance(value, str) or not value or "\\" in value:
        return None
    pure = PurePosixPath(value)
    if pure.is_absolute() or ".." in pure.parts or "." in pure.parts:
        return None
    target = ROOT.joinpath(*pure.parts)
    try:
        target.resolve().relative_to(ROOT.resolve())
    except (OSError, ValueError):
        return None
    return target


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    bindings = candidate.get("bindings")
    if not isinstance(bindings, list):
        return [Finding("ROLE_SET_INVALID", "/bindings")]

    observed_roles = [
        binding.get("role") if isinstance(binding, Mapping) else None
        for binding in bindings
    ]
    role_set_valid = observed_roles == list(ROLE_ORDER)
    if not role_set_valid:
        findings.append(Finding("ROLE_SET_INVALID", "/bindings"))

    holds = 0
    for index, raw_binding in enumerate(bindings):
        if not isinstance(raw_binding, Mapping):
            continue
        role = raw_binding.get("role")
        if role not in ROLE_SUPPORT or not role_set_valid:
            continue
        path = f"/bindings/{index}"
        if raw_binding.get("intended_support_type") != ROLE_SUPPORT[role]:
            findings.append(
                Finding("ROLE_SUPPORT_MAPPING_INVALID", path + "/intended_support_type")
            )

        reason_codes = raw_binding.get("reason_codes")
        if not _canonical_strings(reason_codes, allow_empty=True):
            findings.append(Finding("NONCANONICAL_REASON_CODES", path + "/reason_codes"))

        readiness = raw_binding.get("readiness")
        if readiness == "BOUND":
            if role not in APPROVED_BOUND_NATIVE:
                findings.append(Finding("UNREVIEWED_ROLE_BINDING", path + "/readiness"))
            dependencies = [raw_binding.get(key) for key in PATH_FIELDS + MAPPING_FIELDS]
            if any(not isinstance(value, str) or not value for value in dependencies):
                findings.append(Finding("BOUND_DEPENDENCY_INCOMPLETE", path))
            else:
                if (
                    raw_binding.get("common_source_role") != role
                    or raw_binding.get("common_support_type") != ROLE_SUPPORT[role]
                ):
                    findings.append(Finding("BOUND_COMMON_MAPPING_INVALID", path))
                expected_native = APPROVED_BOUND_NATIVE.get(role)
                if expected_native is not None and (
                    raw_binding.get("native_source_role"),
                    raw_binding.get("native_support_type"),
                ) != expected_native:
                    findings.append(Finding("BOUND_NATIVE_MAPPING_INVALID", path))
                for key in PATH_FIELDS:
                    target = _safe_repo_path(raw_binding.get(key))
                    if target is None:
                        findings.append(Finding("BOUND_PATH_INVALID", path + f"/{key}"))
                    elif not target.is_file() or target.is_symlink():
                        findings.append(Finding("BOUND_PATH_MISSING", path + f"/{key}"))
            if reason_codes:
                findings.append(Finding("BOUND_REASON_CONFLICT", path + "/reason_codes"))
        elif readiness == "HOLD":
            holds += 1
            if any(raw_binding.get(key) is not None for key in PATH_FIELDS + MAPPING_FIELDS):
                findings.append(Finding("HOLD_BINDING_OVERCLAIM", path))
            if not reason_codes:
                findings.append(Finding("HOLD_REASON_REQUIRED", path + "/reason_codes"))

    if role_set_valid:
        expected_outcome = "PARTIAL_READY" if holds else "FULLY_READY"
        if candidate.get("matrix_outcome") != expected_outcome:
            findings.append(Finding("MATRIX_OUTCOME_MISMATCH", "/matrix_outcome"))

    if not _canonical_strings(candidate.get("limitations"), allow_empty=False):
        findings.append(Finding("NONCANONICAL_LIMITATIONS", "/limitations"))
    if candidate.get("public_use_allowed") is not False:
        findings.append(Finding("PUBLIC_USE_OVERCLAIM", "/public_use_allowed"))
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append(Finding("EFFECT_OVERCLAIM", "/effects"))

    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_matrix_id(candidate)
    except RuntimeError:
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("matrix_id") != expected_id:
            findings.append(Finding("MATRIX_ID_MISMATCH", "/matrix_id"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
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
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
        if part
    ]
    if not parts:
        raise ValueError("invalid mutation path")
    current: Any = candidate
    for part in parts[:-1]:
        if isinstance(current, dict):
            if part not in current:
                raise ValueError("unknown mutation path")
            current = current[part]
        elif isinstance(current, list) and part.isdigit():
            index = int(part)
            if index >= len(current):
                raise ValueError("unknown mutation path")
            current = current[index]
        else:
            raise ValueError("unknown mutation path")
    final = parts[-1]
    if isinstance(current, dict) and final in current:
        current[final] = copy.deepcopy(value)
    elif isinstance(current, list) and final.isdigit() and int(final) < len(current):
        current[int(final)] = copy.deepcopy(value)
    else:
        raise ValueError("unknown mutation path")


def _load_fixture_document() -> dict[str, Any]:
    document, findings = _read(CASES)
    if (
        document is None
        or findings
        or not isinstance(document.get("bases"), dict)
        or not isinstance(document.get("cases"), list)
    ):
        raise ValueError("invalid fixture manifest")
    return document


def materialize_case(
    document: Mapping[str, Any], case: Mapping[str, Any]
) -> dict[str, Any]:
    bases = document["bases"]
    base_name = case.get("base")
    if (
        not isinstance(bases, Mapping)
        or base_name not in bases
        or not isinstance(bases[base_name], Mapping)
    ):
        raise ValueError("unknown fixture base")
    candidate = copy.deepcopy(dict(bases[base_name]))
    for mutation in case.get("mutations", []):
        if (
            not isinstance(mutation, Mapping)
            or not isinstance(mutation.get("path"), str)
            or "value" not in mutation
        ):
            raise ValueError("invalid mutation")
        _set_pointer(candidate, mutation["path"], mutation["value"])
    candidate = assign_identity(candidate)
    mode = case.get("identity_mode", "RECOMPUTE")
    if mode == "MISMATCH_SPEC_HASH":
        candidate["spec_hash"] = "sha256:" + "0" * 64
    elif mode == "MISMATCH_ID":
        candidate["matrix_id"] = "conditions-source-role-matrix:" + "0" * 24
    elif mode != "RECOMPUTE":
        raise ValueError("unknown identity mode")
    return candidate


def load_fixture_cases() -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _load_fixture_document()
    result: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for raw in document["cases"]:
        if (
            not isinstance(raw, dict)
            or not isinstance(raw.get("name"), str)
            or raw["name"] in names
        ):
            raise ValueError("invalid fixture case")
        names.add(raw["name"])
        result.append((raw, materialize_case(document, raw)))
    return result


def _serialize(
    result: ValidationResult,
    *,
    path: Path | None = None,
    case: str | None = None,
) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "scope": SCOPE,
        "authority": {
            "network_fetch": False,
            "source_activation": False,
            "evidence_resolution": False,
            "policy_evaluation": False,
            "review_approval": False,
            "profile_adoption": False,
            "lifecycle_write": False,
            "promotion": False,
            "release": False,
            "publication": False,
            "public_use": False,
        },
    }
    if path is not None:
        try:
            payload["file"] = path.resolve().relative_to(ROOT.resolve()).as_posix()
        except (OSError, ValueError):
            payload["file"] = path.name
    if case is not None:
        payload["case"] = case
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def replay_fixtures() -> int:
    try:
        cases = load_fixture_cases()
    except (OSError, UnicodeError, ValueError, RuntimeError, RecursionError):
        result = ValidationResult(
            "ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),)
        )
        print(_serialize(result, case="fixture_manifest"))
        return 2
    mismatches = 0
    for raw, candidate in cases:
        result = validate_payload(candidate)
        actual = [finding.code for finding in result.findings]
        if (
            result.outcome != raw.get("expected_outcome")
            or actual != raw.get("expected_findings")
        ):
            mismatches += 1
        print(_serialize(result, case=raw["name"]))
    return 1 if mismatches else 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate one fixture-only conditions source-role readiness matrix."
    )
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            parser.error("--fixtures does not accept a path")
        return replay_fixtures()
    if args.path is None:
        parser.error("path or --fixtures is required")
    result = validate_file(args.path)
    print(_serialize(result, path=args.path))
    return 0 if result.outcome == "PASS" else 1 if result.outcome == "DENY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
