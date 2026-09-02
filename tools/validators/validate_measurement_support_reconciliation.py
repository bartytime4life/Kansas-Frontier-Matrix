#!/usr/bin/env python3
"""Validate fixture-only measurement-support reconciliation candidates.

PASS proves bounded local consistency only. This tool performs no network
access, scientific harmonization, source activation, evidence resolution,
policy evaluation, review approval, release, publication, or public use.
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
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/common/measurement_support_reconciliation.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/common/measurement_support_reconciliation/cases.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:measurement-support-reconciliation:"
ROLE_CHARACTER = {"OBSERVATION": "MEASURED", "MODEL": "MODELED", "DERIVED": "DERIVED"}


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
    profile_state: str | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


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


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("MEASUREMENT_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("MEASUREMENT_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("MEASUREMENT_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("MEASUREMENT_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("MEASUREMENT_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("MEASUREMENT_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("MEASUREMENT_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("MEASUREMENT_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"assessment_id", "spec_hash"}}
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _close(left: object, right: object, tolerance: float = 1e-9) -> bool:
    return isinstance(left, (int, float)) and isinstance(right, (int, float)) and math.isclose(float(left), float(right), rel_tol=tolerance, abs_tol=tolerance)


def _vertical_relation(left: Mapping[str, Any], right: Mapping[str, Any]) -> str:
    if left["kind"] == "UNKNOWN" or right["kind"] == "UNKNOWN":
        return "UNKNOWN"
    if left["kind"] != right["kind"]:
        return "MISMATCH"
    return "COMPATIBLE" if _close(left["lower_m"], right["lower_m"]) and _close(left["upper_m"], right["upper_m"]) else "MISMATCH"


def _temporal_relation(left: Mapping[str, Any], right: Mapping[str, Any]) -> str:
    left_start, left_end = _parse_time(left["start"]), _parse_time(left["end"])
    right_start, right_end = _parse_time(right["start"]), _parse_time(right["end"])
    assert left_start and left_end and right_start and right_end
    if left == right:
        return "COMPATIBLE"
    if max(left_start, right_start) < min(left_end, right_end):
        return "PARTIAL"
    return "MISMATCH"


def _spatial_relation(left: Mapping[str, Any], right: Mapping[str, Any], resampling: Mapping[str, Any]) -> str:
    if left == right:
        return "COMPATIBLE"
    if resampling["method"] in {"NEAREST", "BILINEAR", "AREA_WEIGHTED"} and resampling["profile_ref"] is not None and resampling["co_location_distance_m"] is not None and resampling["reviewed"]:
        return "RESAMPLED"
    return "MISMATCH"


def _unit_relation(left: Mapping[str, Any], right: Mapping[str, Any], transform: Mapping[str, Any]) -> str:
    if left["unit"] == right["unit"] and transform["operation"] == "IDENTITY" and transform["reviewed"]:
        return "IDENTITY"
    if transform["operation"] == "LINEAR" and transform["profile_ref"] is not None and transform["reviewed"]:
        return "CONVERTED"
    return "UNSUPPORTED"


def expected_reconciliation(value: Mapping[str, Any]) -> dict[str, Any]:
    left, right = value["supports"]
    parameter = "ALIGNED" if left["parameter"] == right["parameter"] else "MISMATCH"
    unit = _unit_relation(left, right, value["unit_transform"])
    vertical = _vertical_relation(left["vertical"], right["vertical"])
    temporal = _temporal_relation(left["temporal"], right["temporal"])
    spatial = _spatial_relation(left["spatial"], right["spatial"], value["resampling"])
    knowledge = "ALIGNED" if left["knowledge_character"] == right["knowledge_character"] else "QUALIFIED"
    reasons: list[str] = []
    unsupported = False
    if parameter == "MISMATCH":
        reasons.append("PARAMETER_MISMATCH")
        unsupported = True
    if unit == "UNSUPPORTED":
        reasons.append("UNIT_TRANSFORM_UNSUPPORTED")
        unsupported = True
    elif unit == "CONVERTED":
        reasons.append("UNIT_CONVERSION_APPLIED")
    if vertical == "MISMATCH":
        reasons.append("VERTICAL_SUPPORT_MISMATCH")
        unsupported = True
    elif vertical == "UNKNOWN":
        reasons.append("VERTICAL_SUPPORT_UNKNOWN")
        unsupported = True
    if temporal == "MISMATCH":
        reasons.append("TEMPORAL_SUPPORT_MISMATCH")
        unsupported = True
    elif temporal == "PARTIAL":
        reasons.append("TEMPORAL_OVERLAP_PARTIAL")
    if spatial == "MISMATCH":
        reasons.append("SPATIAL_SUPPORT_MISMATCH")
        unsupported = True
    elif spatial == "RESAMPLED":
        reasons.append("SPATIAL_RESAMPLING_DECLARED")
    if knowledge == "QUALIFIED":
        reasons.append("KNOWLEDGE_CHARACTER_DIFFERS")
    quality_states = {left["quality_state"], right["quality_state"]}
    if "UNKNOWN" in quality_states or "UNKNOWN" in {left["no_data_semantics"], right["no_data_semantics"]}:
        reasons.append("QUALITY_UNRESOLVED")
        unsupported = True
    elif "SUSPECT" in quality_states:
        reasons.append("QUALITY_SUSPECT")
    if unsupported:
        outcome, profile_state = "UNSUPPORTED", "HOLD"
    elif reasons:
        outcome, profile_state = "QUALIFIED", "REVIEW_REQUIRED"
    else:
        outcome, profile_state = "COMPARABLE", "REVIEW_REQUIRED"
        reasons = ["SUPPORTS_ALIGNED"]
    return {
        "parameter_relation": parameter,
        "unit_relation": unit,
        "vertical_relation": vertical,
        "temporal_relation": temporal,
        "spatial_relation": spatial,
        "knowledge_relation": knowledge,
        "outcome": outcome,
        "reason_codes": sorted(reasons),
        "profile_state": profile_state,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("MEASUREMENT_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [Finding("MEASUREMENT_SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("MEASUREMENT_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _semantic_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    supports = value["supports"]
    support_ids = [item["support_id"] for item in supports]
    if support_ids != sorted(support_ids):
        findings.add(Finding("MEASUREMENT_SUPPORT_ORDER_INVALID", "/supports"))
    if len(set(support_ids)) != len(support_ids):
        findings.add(Finding("MEASUREMENT_SUPPORT_ID_DUPLICATE", "/supports"))

    for index, support in enumerate(supports):
        if ROLE_CHARACTER[support["source_role"]] != support["knowledge_character"]:
            findings.add(Finding("MEASUREMENT_ROLE_CHARACTER_MISMATCH", f"/supports/{index}/knowledge_character"))
        if support["uncertainty"]["unit"] != support["unit"]:
            findings.add(Finding("MEASUREMENT_UNCERTAINTY_UNIT_MISMATCH", f"/supports/{index}/uncertainty/unit"))
        vertical = support["vertical"]
        lower, upper = vertical["lower_m"], vertical["upper_m"]
        if vertical["kind"] == "UNKNOWN":
            if lower is not None or upper is not None:
                findings.add(Finding("MEASUREMENT_VERTICAL_SHAPE_INVALID", f"/supports/{index}/vertical"))
        elif lower is None or upper is None or float(lower) < 0 or float(upper) < float(lower):
            findings.add(Finding("MEASUREMENT_VERTICAL_SHAPE_INVALID", f"/supports/{index}/vertical"))
        temporal = support["temporal"]
        start, end = _parse_time(temporal["start"]), _parse_time(temporal["end"])
        if start is None or end is None or end < start:
            findings.add(Finding("MEASUREMENT_TEMPORAL_WINDOW_INVALID", f"/supports/{index}/temporal"))
        elif int((end - start).total_seconds()) != temporal["duration_seconds"]:
            findings.add(Finding("MEASUREMENT_TEMPORAL_DURATION_MISMATCH", f"/supports/{index}/temporal/duration_seconds"))

    transform = value["unit_transform"]
    left, right = supports
    if transform["from_support_id"] != left["support_id"] or transform["to_support_id"] != right["support_id"]:
        findings.add(Finding("MEASUREMENT_TRANSFORM_BINDING_MISMATCH", "/unit_transform"))
    if transform["from_unit"] != left["unit"] or transform["to_unit"] != right["unit"]:
        findings.add(Finding("MEASUREMENT_TRANSFORM_UNIT_MISMATCH", "/unit_transform"))
    operation = transform["operation"]
    if operation == "IDENTITY":
        valid = left["unit"] == right["unit"] and transform["profile_ref"] is None and _close(transform["scale"], 1.0) and _close(transform["offset"], 0.0) and _close(transform["transformed_value"], left["value"]) and transform["reviewed"]
        if not valid:
            findings.add(Finding("MEASUREMENT_IDENTITY_TRANSFORM_INVALID", "/unit_transform"))
    elif operation == "LINEAR":
        if transform["profile_ref"] is None or transform["scale"] is None or transform["offset"] is None or transform["transformed_value"] is None or not transform["reviewed"]:
            findings.add(Finding("MEASUREMENT_LINEAR_TRANSFORM_INCOMPLETE", "/unit_transform"))
        else:
            expected = float(left["value"]) * float(transform["scale"]) + float(transform["offset"])
            if not _close(transform["transformed_value"], expected, 1e-8):
                findings.add(Finding("MEASUREMENT_TRANSFORM_VALUE_MISMATCH", "/unit_transform/transformed_value"))
    elif any(transform[key] is not None for key in ("profile_ref", "scale", "offset", "transformed_value")) or transform["reviewed"]:
        findings.add(Finding("MEASUREMENT_UNSUPPORTED_TRANSFORM_OVERCLAIM", "/unit_transform"))

    resampling = value["resampling"]
    if resampling["method"] == "NONE":
        if resampling["profile_ref"] is not None or resampling["co_location_distance_m"] is not None or not resampling["reviewed"]:
            findings.add(Finding("MEASUREMENT_RESAMPLING_NONE_INVALID", "/resampling"))
    elif resampling["method"] in {"NEAREST", "BILINEAR", "AREA_WEIGHTED"}:
        if resampling["profile_ref"] is None or resampling["co_location_distance_m"] is None or not resampling["reviewed"]:
            findings.add(Finding("MEASUREMENT_RESAMPLING_PROFILE_INCOMPLETE", "/resampling"))
    elif resampling["profile_ref"] is not None or resampling["co_location_distance_m"] is not None or resampling["reviewed"]:
        findings.add(Finding("MEASUREMENT_UNSUPPORTED_RESAMPLING_OVERCLAIM", "/resampling"))

    if value["reconciliation"] != expected_reconciliation(value):
        findings.add(Finding("MEASUREMENT_RECONCILIATION_SUMMARY_MISMATCH", "/reconciliation"))
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)
    findings = _semantic_findings(value)
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("MEASUREMENT_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("MEASUREMENT_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("MEASUREMENT_ID_MISMATCH", "/assessment_id"))
    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    profile_state = value["reconciliation"]["profile_state"]
    outcome = "ABSTAIN" if value["reconciliation"]["outcome"] == "UNSUPPORTED" else "PASS"
    return Result(outcome, profile_state, ())


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
    if not case.get("preserve_reconciliation", False):
        document["reconciliation"] = expected_reconciliation(document)
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
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or result.profile_state != case["expected_profile_state"] or actual != case["expected_findings"]:
            failures.append({"case_id": case["case_id"], "expected_outcome": case["expected_outcome"], "actual_outcome": result.outcome, "expected_profile_state": case["expected_profile_state"], "actual_profile_state": result.profile_state, "expected_findings": case["expected_findings"], "actual_findings": actual})
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps({"authority": {"scientific_authority_created": False, "evidence_resolved": False, "policy_evaluated": False, "review_approved": False, "release_authorized": False, "publication_authorized": False}, "execution_mode": "FIXTURE_ONLY", "file": path.as_posix(), "findings": [{"code": item.code, "path": item.path} for item in result.findings], "outcome": result.outcome, "profile_state": result.profile_state}, sort_keys=True, separators=(",", ":"))


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
    return {"PASS": 0, "ABSTAIN": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
