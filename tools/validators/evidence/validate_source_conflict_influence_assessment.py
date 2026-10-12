#!/usr/bin/env python3
"""Validate fixture-only source-conflict influence assessments."""
from __future__ import annotations

import argparse
import copy
import hmac
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(HASHING_SRC))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/evidence/source_conflict_influence_assessment.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/evidence/source_conflict_influence_assessment/cases.json"
RELATION_REASON = {
    "CONSISTENT": "COMPARISON_CONSISTENT",
    "DIVERGENT": "COMPARISON_DIVERGENT",
    "CONFLICTING": "COMPARISON_CONFLICTING",
    "INSUFFICIENT": "COMPARISON_INSUFFICIENT",
    "INAPPLICABLE": "COMPARISON_INAPPLICABLE",
    "REVOKED_EVIDENCE": "COMPARISON_REVOKED_EVIDENCE",
}
RELATION_PRECEDENCE = (
    "REVOKED_EVIDENCE",
    "CONFLICTING",
    "DIVERGENT",
    "INSUFFICIENT",
    "CONSISTENT",
    "INAPPLICABLE",
)
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
    relationship: str | None
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


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    return f"kfm:source-conflict-influence:{spec_hash.removeprefix('sha256:')[:24]}"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def expected_overall(document: Mapping[str, Any]) -> str:
    relationships = {item["relationship"] for item in document["comparisons"]}
    return next(value for value in RELATION_PRECEDENCE if value in relationships)


def expected_summary(document: Mapping[str, Any]) -> dict[str, Any]:
    sources = document["sources"]
    by_role = {
        role: sorted(item["source_id"] for item in sources if item["influence_role"] == role)
        for role in ("DOMINANT", "CONTRIBUTING", "CONTEXT_ONLY", "EXCLUDED", "NON_INFLUENTIAL")
    }
    return {
        "source_count": len(sources),
        "comparison_count": len(document["comparisons"]),
        "overall_relationship": expected_overall(document),
        "dominant_source_ids": by_role["DOMINANT"],
        "contributing_source_ids": by_role["CONTRIBUTING"],
        "context_only_source_ids": by_role["CONTEXT_ONLY"],
        "excluded_source_ids": by_role["EXCLUDED"],
        "non_influential_source_ids": by_role["NON_INFLUENTIAL"],
        "claim_resolution_allowed": False,
        "separate_policy_gate_required": True,
    }


def _source_state_valid(source: Mapping[str, Any]) -> bool:
    eligibility = source["eligibility"]
    influence = source["influence_role"]
    evidence_ref = source["evidence_ref"]
    reasons = source["reason_codes"]
    if eligibility == "ELIGIBLE":
        return evidence_ref is not None and influence in {
            "DOMINANT", "CONTRIBUTING", "CONTEXT_ONLY", "NON_INFLUENTIAL"
        } and reasons == ["ELIGIBLE_FOR_COMPARISON"]
    if eligibility == "EXCLUDED":
        return influence == "EXCLUDED" and reasons == ["PROFILE_EXCLUDED"]
    if eligibility == "REVOKED":
        return evidence_ref is not None and influence == "EXCLUDED" and reasons == ["EVIDENCE_REVOKED"]
    return evidence_ref is None and influence == "NON_INFLUENTIAL" and reasons == ["SOURCE_INAPPLICABLE"]


def _expected_pair_ids(source_ids: Sequence[str]) -> list[str]:
    return [
        f"{left}::{right}"
        for index, left in enumerate(source_ids)
        for right in source_ids[index + 1 :]
    ]


def _required_relationship(left: Mapping[str, Any], right: Mapping[str, Any]) -> str | None:
    eligibility = {left["eligibility"], right["eligibility"]}
    if "REVOKED" in eligibility:
        return "REVOKED_EVIDENCE"
    if eligibility & {"EXCLUDED", "INAPPLICABLE"}:
        return "INAPPLICABLE"
    return None


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return ValidationResult(
            "DENY",
            None,
            (Finding("SOURCE_CONFLICT_SCHEMA_INVALID", _json_pointer(errors[0].absolute_path)),),
        )

    profile_axes = document["comparison_profile"]["axes"]
    if profile_axes != sorted(set(profile_axes)):
        return ValidationResult(
            "DENY", None, (Finding("SOURCE_CONFLICT_PROFILE_AXES_INVALID", "/comparison_profile/axes"),)
        )

    sources = document["sources"]
    source_ids = [item["source_id"] for item in sources]
    if source_ids != sorted(set(source_ids)):
        return ValidationResult(
            "DENY", None, (Finding("SOURCE_CONFLICT_SOURCE_ORDER_INVALID", "/sources"),)
        )
    if len({item["source_descriptor_ref"] for item in sources}) != len(sources):
        return ValidationResult(
            "DENY", None, (Finding("SOURCE_CONFLICT_DESCRIPTOR_REF_REUSED", "/sources"),)
        )
    for index, source in enumerate(sources):
        if not _source_state_valid(source):
            return ValidationResult(
                "DENY", None, (Finding("SOURCE_CONFLICT_SOURCE_STATE_INVALID", f"/sources/{index}"),)
            )
    if sum(item["influence_role"] == "DOMINANT" for item in sources) > 1:
        return ValidationResult(
            "DENY", None, (Finding("SOURCE_CONFLICT_MULTIPLE_DOMINANT", "/sources"),)
        )

    comparisons = document["comparisons"]
    if [item["pair_id"] for item in comparisons] != _expected_pair_ids(source_ids):
        return ValidationResult(
            "DENY", None, (Finding("SOURCE_CONFLICT_PAIR_MATRIX_INVALID", "/comparisons"),)
        )
    by_id = {item["source_id"]: item for item in sources}
    profile_axis_set = set(profile_axes)
    for index, comparison in enumerate(comparisons):
        left = comparison["left_source_id"]
        right = comparison["right_source_id"]
        pair_id = f"{left}::{right}"
        if left >= right or comparison["pair_id"] != pair_id or left not in by_id or right not in by_id:
            return ValidationResult(
                "DENY", None, (Finding("SOURCE_CONFLICT_PAIR_BINDING_INVALID", f"/comparisons/{index}"),)
            )
        axes = comparison["axes"]
        if axes != sorted(set(axes)) or not set(axes).issubset(profile_axis_set):
            return ValidationResult(
                "DENY", None, (Finding("SOURCE_CONFLICT_PAIR_AXES_INVALID", f"/comparisons/{index}/axes"),)
            )
        relationship = comparison["relationship"]
        if comparison["reason_codes"] != [RELATION_REASON[relationship]]:
            return ValidationResult(
                "DENY", None, (Finding("SOURCE_CONFLICT_RELATION_REASON_MISMATCH", f"/comparisons/{index}/reason_codes"),)
            )
        required = _required_relationship(by_id[left], by_id[right])
        if required is not None and relationship != required:
            return ValidationResult(
                "DENY", None, (Finding("SOURCE_CONFLICT_INELIGIBLE_PAIR_MISMATCH", f"/comparisons/{index}/relationship"),)
            )
        if required is None and relationship in {"INAPPLICABLE", "REVOKED_EVIDENCE"}:
            return ValidationResult(
                "DENY", None, (Finding("SOURCE_CONFLICT_ELIGIBLE_PAIR_MISMATCH", f"/comparisons/{index}/relationship"),)
            )

    expected = expected_summary(document)
    if document["summary"] != expected:
        return ValidationResult(
            "DENY", None, (Finding("SOURCE_CONFLICT_SUMMARY_MISMATCH", "/summary"),)
        )

    actual_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], actual_hash):
        return ValidationResult(
            "DENY", None, (Finding("SOURCE_CONFLICT_SPEC_HASH_MISMATCH", "/spec_hash"),)
        )
    actual_id = expected_assessment_id(actual_hash)
    if not hmac.compare_digest(document["assessment_id"], actual_id):
        return ValidationResult(
            "DENY", None, (Finding("SOURCE_CONFLICT_ID_MISMATCH", "/assessment_id"),)
        )
    return ValidationResult("PASS", expected["overall_relationship"], ())


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
        if result.status != case["expected_status"] or result.relationship != case["expected_relationship"] or actual_findings != case["expected_findings"]:
            failures.append({
                "case_id": case["case_id"],
                "expected_status": case["expected_status"],
                "actual_status": result.status,
                "expected_relationship": case["expected_relationship"],
                "actual_relationship": result.relationship,
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
        result = ValidationResult(
            "ERROR", None, (Finding("JSON_INPUT_SYMLINK_DENIED", "/"),)
        )
    except InputTooLargeError:
        result = ValidationResult(
            "ERROR", None, (Finding("JSON_INPUT_TOO_LARGE", "/"),)
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_INVALID", "/"),))
    print(json.dumps({"status":result.status,"relationship":result.relationship,"findings":[{"code":item.code,"path":item.path} for item in result.findings]}, sort_keys=True, separators=(",", ":")))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
