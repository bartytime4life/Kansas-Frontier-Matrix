#!/usr/bin/env python3
"""Validate the inactive, fixture-only AggregateStatistic profile.

PASS proves declaration closure and anti-local-truth boundaries only. It does
not fetch data, recompute a statistic, evaluate policy, release, or publish.
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

SCHEMA = ROOT / "schemas/contracts/v1/common/aggregate_statistic.schema.json"
CASES = ROOT / "fixtures/contracts/v1/common/aggregate_statistic/cases.json"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "aggregate-statistic-fixture-only-v1"
FALSE_EFFECTS = {
    "source_activated": False,
    "evidence_resolved": False,
    "policy_evaluated": False,
    "promoted": False,
    "released": False,
    "published": False,
}
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED", "JSON_INVALID", "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT", "SCHEMA_UNAVAILABLE",
    "HASHING_UNAVAILABLE", "SPEC_HASH_MISMATCH",
    "AGGREGATE_STATISTIC_ID_MISMATCH", "FIXTURE_MANIFEST_INVALID",
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
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("aggregate_statistic_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))


def expected_statistic_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "aggregate-statistic:" + digest[:24]


def assign_identity(candidate: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(candidate)
    result["spec_hash"] = canonical_spec_hash(result)
    result["aggregate_statistic_id"] = expected_statistic_id(result)
    return result


def _dt(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(
            value[:-1] + "+00:00" if value.endswith("Z") else value
        )
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _canonical(values: Any) -> bool:
    return (
        isinstance(values, list)
        and all(isinstance(value, str) for value in values)
        and values == sorted(set(values))
    )


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    if candidate.get("source_role") != "AGGREGATE":
        findings.append(Finding("SOURCE_ROLE_COLLAPSE", "/source_role"))
    if candidate.get("support_type") != "AGGREGATE_STATISTIC":
        findings.append(Finding("SUPPORT_TYPE_COLLAPSE", "/support_type"))
    if candidate.get("derived_only") is not True:
        findings.append(Finding("DERIVED_ONLY_REQUIRED", "/derived_only"))

    for key in (
        "source_snapshot_refs", "input_refs", "content_digests",
        "evidence_refs", "limitations",
    ):
        if not _canonical(candidate.get(key)):
            findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", f"/{key}"))
    lineage = candidate.get("lineage") if isinstance(candidate.get("lineage"), Mapping) else {}
    for key in ("corrects", "superseded_by", "conflict_refs"):
        if not _canonical(lineage.get(key)):
            findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", f"/lineage/{key}"))

    digests = candidate.get("content_digests")
    if isinstance(digests, list) and any(value == "sha256:" + "0" * 64 for value in digests):
        findings.append(Finding("PLACEHOLDER_CONTENT_DIGEST", "/content_digests"))

    times = candidate.get("times") if isinstance(candidate.get("times"), Mapping) else {}
    cutoff = _dt(times.get("source_data_cutoff_at"))
    source_release = _dt(times.get("source_released_at"))
    valid_from = _dt(times.get("valid_from"))
    valid_to = _dt(times.get("valid_to"))
    retrieved = _dt(times.get("retrieved_at"))
    corrected = _dt(times.get("corrected_at"))
    superseded = _dt(times.get("superseded_at"))
    if cutoff and source_release and cutoff > source_release:
        findings.append(Finding("DATA_CUTOFF_AFTER_SOURCE_RELEASE", "/times/source_data_cutoff_at"))
    if valid_from and valid_to and valid_from > valid_to:
        findings.append(Finding("VALIDITY_INTERVAL_INVALID", "/times/valid_to"))
    if source_release and retrieved and source_release > retrieved:
        findings.append(Finding("SOURCE_RELEASE_AFTER_RETRIEVAL", "/times/source_released_at"))
    if corrected and source_release and corrected < source_release:
        findings.append(Finding("CORRECTION_BEFORE_SOURCE_RELEASE", "/times/corrected_at"))
    if superseded and source_release and superseded < source_release:
        findings.append(Finding("SUPERSESSION_BEFORE_SOURCE_RELEASE", "/times/superseded_at"))

    geography = candidate.get("geography") if isinstance(candidate.get("geography"), Mapping) else {}
    unresolved_geometry = geography.get("geometry_role") == "UNRESOLVED"
    if unresolved_geometry and any(
        geography.get(key) is not None
        for key in ("aggregation_geography_ref", "geometry_digest")
    ):
        findings.append(Finding("UNRESOLVED_GEOMETRY_OVERCLAIM", "/geography"))
    if not unresolved_geometry and any(
        geography.get(key) is None
        for key in ("aggregation_geography_ref", "geometry_digest")
    ):
        findings.append(Finding("RESOLVED_GEOMETRY_INCOMPLETE", "/geography"))
    if geography.get("local_truth_allowed") is not False:
        findings.append(Finding("LOCAL_TRUTH_OVERCLAIM", "/geography/local_truth_allowed"))
    if geography.get("exact_local_geometry_allowed") is not False:
        findings.append(Finding("EXACT_LOCAL_GEOMETRY_OVERCLAIM", "/geography/exact_local_geometry_allowed"))

    computation = candidate.get("computation") if isinstance(candidate.get("computation"), Mapping) else {}
    family = candidate.get("statistic_family")
    if computation.get("source_release_ref") is None:
        findings.append(Finding("SOURCE_RELEASE_REQUIRED", "/computation/source_release_ref"))
    if family in {"PERCENTAGE", "RATE"} and computation.get("numerator_ref") is None:
        findings.append(Finding("NUMERATOR_REQUIRED", "/computation/numerator_ref"))
    if computation.get("denominator_kind") != "NONE" and computation.get("denominator_ref") is None:
        findings.append(Finding("DENOMINATOR_REQUIRED", "/computation/denominator_ref"))
    if computation.get("denominator_kind") == "NONE" and computation.get("denominator_ref") is not None:
        findings.append(Finding("DENOMINATOR_REFERENCE_CONFLICT", "/computation/denominator_ref"))
    weighted = computation.get("aggregation_method") in {"WEIGHTED_SUM", "WEIGHTED_MEAN"}
    if (weighted or computation.get("weighting_kind") != "NONE") and computation.get("weighting_ref") is None:
        findings.append(Finding("WEIGHTING_REFERENCE_REQUIRED", "/computation/weighting_ref"))
    if computation.get("weighting_kind") == "NONE" and computation.get("weighting_ref") is not None:
        findings.append(Finding("WEIGHTING_REFERENCE_CONFLICT", "/computation/weighting_ref"))
    if computation.get("missing_data_ref") is None:
        findings.append(Finding("MISSING_DATA_TREATMENT_UNBOUND", "/computation/missing_data_ref"))

    uncertainty = candidate.get("uncertainty") if isinstance(candidate.get("uncertainty"), Mapping) else {}
    if uncertainty.get("kind") == "NOT_PROVIDED":
        if uncertainty.get("value_ref") is not None:
            findings.append(Finding("UNCERTAINTY_REFERENCE_CONFLICT", "/uncertainty/value_ref"))
        if uncertainty.get("confidence") != "UNKNOWN":
            findings.append(Finding("UNCERTAINTY_CONFIDENCE_OVERCLAIM", "/uncertainty/confidence"))
    elif uncertainty.get("value_ref") is None:
        findings.append(Finding("UNCERTAINTY_REFERENCE_REQUIRED", "/uncertainty/value_ref"))

    state = lineage.get("state")
    corrects = lineage.get("corrects", [])
    superseded_by = lineage.get("superseded_by", [])
    conflicts = lineage.get("conflict_refs", [])
    if state == "CURRENT" and (corrects or superseded_by or conflicts or corrected or superseded):
        findings.append(Finding("CURRENT_LINEAGE_CONFLICT", "/lineage"))
    elif state == "CORRECTED" and (not corrects or corrected is None):
        findings.append(Finding("CORRECTION_LINEAGE_INCOMPLETE", "/lineage"))
    elif state == "SUPERSEDED" and (not superseded_by or superseded is None):
        findings.append(Finding("SUPERSESSION_LINEAGE_INCOMPLETE", "/lineage"))
    elif state == "CONFLICTED" and (len(conflicts) < 2 or not unresolved_geometry):
        findings.append(Finding("CONFLICT_LINEAGE_INCOMPLETE", "/lineage"))

    if candidate.get("release_state") != "UNRELEASED" or candidate.get("release_ref") is not None:
        findings.append(Finding("RELEASE_OVERCLAIM", "/release_state"))
    if candidate.get("public_use_allowed") is not False:
        findings.append(Finding("PUBLIC_USE_OVERCLAIM", "/public_use_allowed"))
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append(Finding("EFFECT_OVERCLAIM", "/effects"))

    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_statistic_id(candidate)
    except RuntimeError:
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("aggregate_statistic_id") != expected_id:
            findings.append(Finding("AGGREGATE_STATISTIC_ID_MISMATCH", "/aggregate_statistic_id"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    if not ordered:
        return ValidationResult("PASS", ordered)
    outcome = "ERROR" if any(item.code in ERROR_CODES for item in ordered) else "DENY"
    return ValidationResult(outcome, ordered)


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/") if part
    ]
    current: Any = candidate
    for part in parts[:-1]:
        if not isinstance(current, dict) or part not in current:
            raise ValueError("unknown mutation path")
        current = current[part]
    if not parts or not isinstance(current, dict):
        raise ValueError("invalid mutation path")
    current[parts[-1]] = copy.deepcopy(value)


def _load_fixture_document() -> dict[str, Any]:
    document, findings = _read(CASES)
    if (
        document is None or findings
        or not isinstance(document.get("bases"), dict)
        or not isinstance(document.get("cases"), list)
    ):
        raise ValueError("invalid fixture manifest")
    return document


def materialize_case(document: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    bases = document["bases"]
    base_name = case.get("base")
    if not isinstance(bases, Mapping) or base_name not in bases or not isinstance(bases[base_name], Mapping):
        raise ValueError("unknown fixture base")
    candidate = copy.deepcopy(dict(bases[base_name]))
    for mutation in case.get("mutations", []):
        if not isinstance(mutation, Mapping) or not isinstance(mutation.get("path"), str) or "value" not in mutation:
            raise ValueError("invalid mutation")
        _set_pointer(candidate, mutation["path"], mutation["value"])
    candidate = assign_identity(candidate)
    mode = case.get("identity_mode", "RECOMPUTE")
    if mode == "MISMATCH_SPEC_HASH":
        candidate["spec_hash"] = "sha256:" + "0" * 64
    elif mode == "MISMATCH_ID":
        candidate["aggregate_statistic_id"] = "aggregate-statistic:" + "0" * 24
    elif mode != "RECOMPUTE":
        raise ValueError("unknown identity mode")
    return candidate


def load_fixture_cases() -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _load_fixture_document()
    result: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for raw in document["cases"]:
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str) or raw["name"] in names:
            raise ValueError("invalid fixture case")
        names.add(raw["name"])
        result.append((raw, materialize_case(document, raw)))
    return result


def _serialize(result: ValidationResult, *, path: Path | None = None, case: str | None = None) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "scope": SCOPE,
        "authority": {
            "network_fetch": False,
            "source_activation": False,
            "statistic_computation": False,
            "evidence_resolution": False,
            "policy_evaluation": False,
            "review_approval": False,
            "lifecycle_write": False,
            "promotion": False,
            "release": False,
            "publication": False,
            "public_use": False,
            "local_truth": False,
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
        print(_serialize(ValidationResult("ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),)), case="fixture_manifest"))
        return 2
    mismatches = 0
    for raw, candidate in cases:
        result = validate_payload(candidate)
        actual = [item.code for item in result.findings]
        if result.outcome != raw.get("expected_outcome") or actual != raw.get("expected_findings"):
            mismatches += 1
        print(_serialize(result, case=raw["name"]))
    return 1 if mismatches else 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate one fixture-only AggregateStatistic candidate.")
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
