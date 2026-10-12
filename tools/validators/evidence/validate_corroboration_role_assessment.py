#!/usr/bin/env python3
"""Validate fixture-only corroboration-role assessment candidates."""
from __future__ import annotations

import argparse
import copy
import hmac
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(HASHING_SRC))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/evidence/corroboration_role_assessment.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/evidence/corroboration_role_assessment/cases.json"
RELATION_REASON = {
    "SUPPORTS": "DECLARED_SUPPORT",
    "QUALIFIES": "DECLARED_QUALIFICATION",
    "CONTRADICTS": "DECLARED_CONTRADICTION",
    "DUPLICATES": "DECLARED_DUPLICATE",
}
MAX_JSON_BYTES = 1024 * 1024


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class InputSymlinkError(ValueError):
    pass


class InputTooLargeError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    outcome: str | None
    findings: tuple[Finding, ...]


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _json_pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _instant(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    return f"kfm:corroboration-role-assessment:{spec_hash.removeprefix('sha256:')[:24]}"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _expected_pair_ids(source_ids: Sequence[str]) -> list[str]:
    return [
        f"{left}::{right}"
        for index, left in enumerate(source_ids)
        for right in source_ids[index + 1 :]
    ]


def expected_pair_reason(pair: Mapping[str, Any]) -> str:
    compatibility = pair["role_compatibility"]
    if compatibility == "ROLE_COLLAPSE":
        return "ROLE_COLLAPSE"
    if compatibility == "PROHIBITED":
        return "PROHIBITED_ROLE_COMBINATION"
    if compatibility == "UNKNOWN":
        return "ROLE_COMPATIBILITY_UNKNOWN"
    independence = pair["independence"]
    if independence == "SHARED_UPSTREAM":
        return "SHARED_UPSTREAM_DEPENDENCY"
    if independence == "DERIVED_FROM":
        return "DERIVED_DEPENDENCY"
    if independence == "UNKNOWN":
        return "INDEPENDENCE_UNKNOWN"
    overlaps = {pair["spatial_overlap"], pair["temporal_overlap"]}
    if "NONE" in overlaps:
        return "NO_SPATIOTEMPORAL_OVERLAP"
    if "UNKNOWN" in overlaps:
        return "OVERLAP_UNKNOWN"
    return "INDEPENDENT_OVERLAP_COMPATIBLE"


def _pair_supports_independence(pair: Mapping[str, Any]) -> bool:
    return (
        pair["independence"] == "INDEPENDENT"
        and pair["spatial_overlap"] in {"FULL", "PARTIAL"}
        and pair["temporal_overlap"] in {"FULL", "PARTIAL"}
        and pair["role_compatibility"] == "COMPATIBLE"
    )


def expected_summary(document: Mapping[str, Any]) -> dict[str, Any]:
    sources = document["sources"]
    by_id = {source["source_id"]: source for source in sources}
    by_relationship = {
        relationship: sorted(
            source["source_id"]
            for source in sources
            if source["relationship"] == relationship
        )
        for relationship in (
            "SUPPORTS",
            "QUALIFIES",
            "CONTRADICTS",
            "DUPLICATES",
            "CANNOT_EVALUATE",
        )
    }
    independent_pairs = sorted(
        pair["pair_id"]
        for pair in document["pair_assessments"]
        if _pair_supports_independence(pair)
        and by_id[pair["left_source_id"]]["relationship"] == "SUPPORTS"
        and by_id[pair["right_source_id"]]["relationship"] == "SUPPORTS"
        and by_id[pair["left_source_id"]]["freshness"] == "CURRENT"
        and by_id[pair["right_source_id"]]["freshness"] == "CURRENT"
    )
    unsafe_compatibility = any(
        pair["role_compatibility"] in {"ROLE_COLLAPSE", "PROHIBITED", "UNKNOWN"}
        for pair in document["pair_assessments"]
    )
    if unsafe_compatibility or by_relationship["CANNOT_EVALUATE"]:
        outcome = "CANNOT_EVALUATE"
    elif by_relationship["CONTRADICTS"]:
        outcome = "CONTRADICTED"
    elif independent_pairs:
        qualified_overlap = any(
            pair["pair_id"] in independent_pairs
            and "PARTIAL" in {pair["spatial_overlap"], pair["temporal_overlap"]}
            for pair in document["pair_assessments"]
        )
        outcome = (
            "SUPPORTED_WITH_QUALIFICATION"
            if by_relationship["QUALIFIES"] or qualified_overlap
            else "SUPPORTED"
        )
    else:
        outcome = "INSUFFICIENT"
    return {
        "source_count": len(sources),
        "supporting_source_ids": by_relationship["SUPPORTS"],
        "qualifying_source_ids": by_relationship["QUALIFIES"],
        "contradicting_source_ids": by_relationship["CONTRADICTS"],
        "duplicate_source_ids": by_relationship["DUPLICATES"],
        "cannot_evaluate_source_ids": by_relationship["CANNOT_EVALUATE"],
        "independent_support_pair_ids": independent_pairs,
        "outcome": outcome,
        "source_count_is_confidence": False,
        "claim_resolution_allowed": False,
        "separate_evidence_policy_review_release_gates_required": True,
    }


def _source_state_valid(source: Mapping[str, Any], assessed_at: datetime) -> bool:
    observed_at = _instant(source["observed_at"])
    fresh_until_value = source["fresh_until"]
    if observed_at > assessed_at:
        return False
    if fresh_until_value is None:
        expected_freshness = "UNKNOWN"
    else:
        fresh_until = _instant(fresh_until_value)
        if fresh_until < observed_at:
            return False
        expected_freshness = "CURRENT" if fresh_until >= assessed_at else "STALE"
    if source["freshness"] != expected_freshness:
        return False
    if expected_freshness == "STALE":
        return source["relationship"] == "CANNOT_EVALUATE" and source["reason_codes"] == ["FRESHNESS_STALE"]
    if expected_freshness == "UNKNOWN":
        return source["relationship"] == "CANNOT_EVALUATE" and source["reason_codes"] == ["FRESHNESS_UNKNOWN"]
    relationship = source["relationship"]
    return relationship in RELATION_REASON and source["reason_codes"] == [RELATION_REASON[relationship]]


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return ValidationResult(
            "DENY",
            None,
            (Finding("CORROBORATION_ROLE_SCHEMA_INVALID", _json_pointer(errors[0].absolute_path)),),
        )

    assessed_at = _instant(document["assessed_at"])
    sources = document["sources"]
    source_ids = [source["source_id"] for source in sources]
    if source_ids != sorted(set(source_ids)):
        return ValidationResult("DENY", None, (Finding("CORROBORATION_SOURCE_ORDER_INVALID", "/sources"),))
    if len({source["source_descriptor_ref"] for source in sources}) != len(sources):
        return ValidationResult("DENY", None, (Finding("CORROBORATION_DESCRIPTOR_REF_REUSED", "/sources"),))
    for index, source in enumerate(sources):
        if not _source_state_valid(source, assessed_at):
            return ValidationResult("DENY", None, (Finding("CORROBORATION_SOURCE_STATE_INVALID", f"/sources/{index}"),))

    pairs = document["pair_assessments"]
    if [pair["pair_id"] for pair in pairs] != _expected_pair_ids(source_ids):
        return ValidationResult("DENY", None, (Finding("CORROBORATION_PAIR_MATRIX_INVALID", "/pair_assessments"),))
    by_id = set(source_ids)
    for index, pair in enumerate(pairs):
        left = pair["left_source_id"]
        right = pair["right_source_id"]
        if left >= right or pair["pair_id"] != f"{left}::{right}" or left not in by_id or right not in by_id:
            return ValidationResult("DENY", None, (Finding("CORROBORATION_PAIR_BINDING_INVALID", f"/pair_assessments/{index}"),))
        if pair["reason_codes"] != [expected_pair_reason(pair)]:
            return ValidationResult("DENY", None, (Finding("CORROBORATION_PAIR_REASON_MISMATCH", f"/pair_assessments/{index}/reason_codes"),))

    expected = expected_summary(document)
    if document["summary"] != expected:
        return ValidationResult("DENY", None, (Finding("CORROBORATION_SUMMARY_MISMATCH", "/summary"),))
    actual_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], actual_hash):
        return ValidationResult("DENY", None, (Finding("CORROBORATION_SPEC_HASH_MISMATCH", "/spec_hash"),))
    actual_id = expected_assessment_id(actual_hash)
    if not hmac.compare_digest(document["assessment_id"], actual_id):
        return ValidationResult("DENY", None, (Finding("CORROBORATION_ID_MISMATCH", "/assessment_id"),))
    return ValidationResult("PASS", expected["outcome"], ())


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError("fixture mutation path must be an absolute JSON pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    final = parts[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = value
    else:
        cursor[final] = value


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest root must be an object")
    return value


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if case.get("recompute_summary"):
        document["summary"] = expected_summary(document)
    document["spec_hash"] = expected_spec_hash(document)
    document["assessment_id"] = expected_assessment_id(document["spec_hash"])
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "assessment_id_override" in case:
        document["assessment_id"] = case["assessment_id_override"]
    return document


def _load_document(path: Path) -> Mapping[str, Any]:
    if path.is_symlink():
        raise InputSymlinkError
    if not path.is_file():
        raise OSError
    if path.stat().st_size > MAX_JSON_BYTES:
        raise InputTooLargeError
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream, object_pairs_hook=_unique_object, parse_constant=_reject_constant, parse_float=_finite_float)
    if not isinstance(value, dict):
        raise ValueError("candidate root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual_findings = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.status != case["expected_status"] or result.outcome != case["expected_outcome"] or actual_findings != case["expected_findings"]:
            failures.append({
                "case_id": case["case_id"],
                "expected_status": case["expected_status"],
                "actual_status": result.status,
                "expected_outcome": case["expected_outcome"],
                "actual_outcome": result.outcome,
                "expected_findings": case["expected_findings"],
                "actual_findings": actual_findings,
            })
    print(json.dumps({"cases":len(manifest["cases"]),"failures":failures,"suite_match":not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.path is None:
        raise SystemExit("path is required unless --fixtures is used")
    try:
        result = validate_payload(_load_document(args.path))
    except DuplicateKeyError:
        result = ValidationResult("ERROR", None, (Finding("JSON_DUPLICATE_KEY", "/"),))
    except NonFiniteNumberError:
        result = ValidationResult("ERROR", None, (Finding("JSON_NONFINITE_NUMBER", "/"),))
    except InputSymlinkError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_SYMLINK_DENIED", "/"),))
    except InputTooLargeError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_TOO_LARGE", "/"),))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_INVALID", "/"),))
    print(json.dumps({"status":result.status,"outcome":result.outcome,"findings":[{"code":item.code,"path":item.path} for item in result.findings]}, sort_keys=True, separators=(",", ":")))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
