#!/usr/bin/env python3
"""Validate the inactive, fixture-only ModeledSurface profile.

PASS proves bounded model/support, resolution, uncertainty, lineage, and
authority non-effects only. It performs no network access or model execution.
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

SCHEMA = ROOT / "schemas/contracts/v1/common/modeled_surface.schema.json"
CASES = ROOT / "fixtures/contracts/v1/common/modeled_surface/cases.json"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "modeled-surface-fixture-only-v1"
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
    "MODELED_SURFACE_ID_MISMATCH", "FIXTURE_MANIFEST_INVALID",
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
    subject.pop("modeled_surface_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))


def expected_surface_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "modeled-surface:" + digest[:24]


def assign_identity(candidate: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(candidate)
    result["spec_hash"] = canonical_spec_hash(result)
    result["modeled_surface_id"] = expected_surface_id(result)
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

    if candidate.get("source_role") != "MODEL":
        findings.append(Finding("SOURCE_ROLE_COLLAPSE", "/source_role"))
    if candidate.get("support_type") != "MODELED_ESTIMATE":
        findings.append(Finding("SUPPORT_TYPE_COLLAPSE", "/support_type"))
    if candidate.get("derived_only") is not True:
        findings.append(Finding("DERIVED_ONLY_REQUIRED", "/derived_only"))
    if candidate.get("field_truth_allowed") is not False:
        findings.append(Finding("FIELD_TRUTH_OVERCLAIM", "/field_truth_allowed"))

    for key in (
        "source_snapshot_refs", "modeled_artifact_refs", "content_digests",
        "evidence_refs", "limitations",
    ):
        if not _canonical(candidate.get(key)):
            findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", f"/{key}"))

    model = candidate.get("model") if isinstance(candidate.get("model"), Mapping) else {}
    if not _canonical(model.get("training_dataset_refs")):
        findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", "/model/training_dataset_refs"))
    lineage = candidate.get("lineage") if isinstance(candidate.get("lineage"), Mapping) else {}
    for key in ("corrects", "superseded_by", "conflict_refs"):
        if not _canonical(lineage.get(key)):
            findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", f"/lineage/{key}"))

    digests = candidate.get("content_digests")
    if isinstance(digests, list) and any(value == "sha256:" + "0" * 64 for value in digests):
        findings.append(Finding("PLACEHOLDER_CONTENT_DIGEST", "/content_digests"))

    times = candidate.get("times") if isinstance(candidate.get("times"), Mapping) else {}
    cutoff = _dt(times.get("training_data_cutoff_at"))
    modeled = _dt(times.get("modeled_at"))
    valid_from = _dt(times.get("valid_from"))
    valid_to = _dt(times.get("valid_to"))
    retrieved = _dt(times.get("retrieved_at"))
    corrected = _dt(times.get("corrected_at"))
    superseded = _dt(times.get("superseded_at"))
    if cutoff and modeled and cutoff > modeled:
        findings.append(Finding("TRAINING_CUTOFF_AFTER_MODEL_RUN", "/times/training_data_cutoff_at"))
    if valid_from and valid_to and valid_from > valid_to:
        findings.append(Finding("VALIDITY_INTERVAL_INVALID", "/times/valid_to"))
    if modeled and retrieved and modeled > retrieved:
        findings.append(Finding("MODEL_RUN_AFTER_RETRIEVAL", "/times/modeled_at"))
    if corrected and modeled and corrected < modeled:
        findings.append(Finding("CORRECTION_BEFORE_MODEL_RUN", "/times/corrected_at"))
    if superseded and modeled and superseded < modeled:
        findings.append(Finding("SUPERSESSION_BEFORE_MODEL_RUN", "/times/superseded_at"))

    space = candidate.get("space") if isinstance(candidate.get("space"), Mapping) else {}
    unresolved_geometry = space.get("geometry_role") == "UNRESOLVED"
    if unresolved_geometry and any(
        space.get(key) is not None
        for key in ("geography_ref", "geometry_digest", "horizontal_crs_ref")
    ):
        findings.append(Finding("UNRESOLVED_GEOMETRY_OVERCLAIM", "/space"))
    if not unresolved_geometry and any(
        space.get(key) is None
        for key in ("geography_ref", "geometry_digest", "horizontal_crs_ref")
    ):
        findings.append(Finding("RESOLVED_GEOMETRY_INCOMPLETE", "/space"))
    if space.get("scale") == "GRID" and (
        space.get("resolution_value") is None or space.get("resolution_unit") is None
    ):
        findings.append(Finding("GRID_RESOLUTION_REQUIRED", "/space/resolution_value"))

    if any(
        not model.get(key)
        for key in ("model_ref", "model_version", "method_ref", "parameter_digest")
    ):
        findings.append(Finding("MODEL_CONTEXT_INCOMPLETE", "/model"))
    training_refs = model.get("training_dataset_refs")
    if (
        not isinstance(training_refs, list)
        or not training_refs
        or any(
            model.get(key) is None
            for key in ("training_support_summary_ref", "training_extent_ref", "training_time_ref")
        )
    ):
        findings.append(Finding("TRAINING_SUPPORT_INCOMPLETE", "/model"))

    uncertainty = candidate.get("uncertainty") if isinstance(candidate.get("uncertainty"), Mapping) else {}
    uncertainty_kind = uncertainty.get("kind")
    uncertainty_ref = uncertainty.get("value_ref")
    confidence = uncertainty.get("confidence")
    if uncertainty_kind == "NOT_PROVIDED":
        if uncertainty_ref is not None:
            findings.append(Finding("UNCERTAINTY_REFERENCE_CONFLICT", "/uncertainty/value_ref"))
        if confidence != "UNKNOWN":
            findings.append(Finding("UNCERTAINTY_CONFIDENCE_OVERCLAIM", "/uncertainty/confidence"))
    elif uncertainty_ref is None:
        findings.append(Finding("UNCERTAINTY_REFERENCE_REQUIRED", "/uncertainty/value_ref"))
    if model.get("extrapolation_state") in {"OUTSIDE_SUPPORT", "UNKNOWN"} and confidence in {"CONFIRMED", "HIGH"}:
        findings.append(Finding("SUPPORT_CONFIDENCE_OVERCLAIM", "/uncertainty/confidence"))

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
        expected_id = expected_surface_id(candidate)
    except RuntimeError:
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("modeled_surface_id") != expected_id:
            findings.append(Finding("MODELED_SURFACE_ID_MISMATCH", "/modeled_surface_id"))
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
        candidate["modeled_surface_id"] = "modeled-surface:" + "0" * 24
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
            "model_execution": False,
            "evidence_resolution": False,
            "policy_evaluation": False,
            "review_approval": False,
            "lifecycle_write": False,
            "promotion": False,
            "release": False,
            "publication": False,
            "public_use": False,
            "field_truth": False,
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
    parser = argparse.ArgumentParser(description="Validate one fixture-only ModeledSurface candidate.")
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
