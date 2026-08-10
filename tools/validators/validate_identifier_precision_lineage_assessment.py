#!/usr/bin/env python3
"""Validate fixture-only identifier and precision lineage assessments."""
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

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "packages/hashing/src"))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/common/identifier_precision_lineage_assessment.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/common/identifier_precision_lineage_assessment/cases.json"
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


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    digest = spec_hash.removeprefix("sha256:")
    return f"kfm:identifier-precision-lineage:{digest[:24]}"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def expected_outcome(document: Mapping[str, Any]) -> str:
    precision = document["precision"]
    identifiers = document["identifiers"]
    decision = document["crosswalk"]["decision"]
    if precision["transform"] == "WITHHELD" or decision == "NOT_MATCHED":
        return "ABSTAIN"
    if decision in {"AMBIGUOUS", "UNRESOLVED"} or any(
        item["status"] == "UNRESOLVED" for item in identifiers
    ):
        return "HOLD"
    return "RESOLVED"


def expected_summary(document: Mapping[str, Any]) -> dict[str, Any]:
    identifiers = document["identifiers"]
    return {
        "assertion_count": len(identifiers),
        "active_identifier_count": sum(item["status"] == "ACTIVE" for item in identifiers),
        "unresolved_identifier_count": sum(item["status"] == "UNRESOLVED" for item in identifiers),
        "lineage_outcome": expected_outcome(document),
        "effective_precision_m": document["precision"]["effective_precision_m"],
        "source_identity_preserved": True,
        "identity_resolution_authorized": False,
        "separate_policy_gate_required": True,
        "public_use_allowed": False,
    }


def _timestamps_valid(identifiers: Sequence[Mapping[str, Any]]) -> bool:
    for item in identifiers:
        start = datetime.fromisoformat(item["valid_time"]["start"].replace("Z", "+00:00"))
        end_value = item["valid_time"]["end"]
        if end_value is not None:
            end = datetime.fromisoformat(end_value.replace("Z", "+00:00"))
            if end <= start:
                return False
    return True


def _supersession_valid(identifiers: Sequence[Mapping[str, Any]]) -> bool:
    by_id = {item["assertion_id"]: item for item in identifiers}
    edges: dict[str, str] = {}
    for item in identifiers:
        source = item["assertion_id"]
        target = item["supersedes_assertion_id"]
        if target is not None:
            if target not in by_id or target == source:
                return False
            edges[source] = target
    for start in edges:
        seen: set[str] = set()
        cursor = start
        while cursor in edges:
            if cursor in seen:
                return False
            seen.add(cursor)
            cursor = edges[cursor]
    return True


def _crosswalk_valid(document: Mapping[str, Any]) -> tuple[bool, str]:
    identifiers = {item["assertion_id"]: item for item in document["identifiers"]}
    crosswalk = document["crosswalk"]
    left = crosswalk["from_assertion_id"]
    right = crosswalk["to_assertion_id"]
    if left == right or left not in identifiers or right not in identifiers:
        return False, "IDENTIFIER_PRECISION_CROSSWALK_BINDING_INVALID"
    if identifiers[left]["role"] != "SOURCE_NATIVE":
        return False, "IDENTIFIER_PRECISION_CROSSWALK_BINDING_INVALID"
    target = identifiers[right]
    decision = crosswalk["decision"]
    if decision == "MATCHED":
        valid = (
            target["role"] == "RESOLVED"
            and target["status"] == "ACTIVE"
            and target["confidence"] == "REVIEWED"
            and bool(crosswalk["evidence_refs"])
            and crosswalk["reviewer_state"] == "REVIEWED"
        )
    else:
        valid = (
            target["status"] == "UNRESOLVED"
            and target["confidence"] == "UNRESOLVED"
            and crosswalk["reviewer_state"] != "REVIEWED"
        )
    return valid, "IDENTIFIER_PRECISION_MATCH_STATE_INVALID"


def _precision_valid(precision: Mapping[str, Any]) -> bool:
    transform = precision["transform"]
    source = precision["source_precision_m"]
    effective = precision["effective_precision_m"]
    profile = precision["transform_profile_ref"]
    receipt = precision["transform_receipt_ref"]
    uncertainty = precision["uncertainty_class"]
    if transform == "NONE":
        return effective == source and profile is None and receipt is None and uncertainty in {
            "SOURCE_DECLARED", "APPROXIMATE"
        }
    if transform == "WITHHELD":
        return effective is None and profile is not None and receipt is not None and uncertainty == "WITHHELD"
    return (
        effective is not None
        and effective >= source
        and profile is not None
        and receipt is not None
        and uncertainty == "GENERALIZED"
    )


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return ValidationResult(
            "DENY", None,
            (Finding("IDENTIFIER_PRECISION_SCHEMA_INVALID", _json_pointer(errors[0].absolute_path)),),
        )

    identifiers = document["identifiers"]
    assertion_ids = [item["assertion_id"] for item in identifiers]
    if assertion_ids != sorted(set(assertion_ids)):
        return ValidationResult(
            "DENY", None, (Finding("IDENTIFIER_PRECISION_ASSERTION_ORDER_INVALID", "/identifiers"),)
        )
    identifier_keys = [(item["namespace"], item["value_digest"]) for item in identifiers]
    if len(identifier_keys) != len(set(identifier_keys)):
        return ValidationResult(
            "DENY", None, (Finding("IDENTIFIER_PRECISION_IDENTIFIER_REUSED", "/identifiers"),)
        )
    if not any(item["role"] == "SOURCE_NATIVE" for item in identifiers):
        return ValidationResult(
            "DENY", None, (Finding("IDENTIFIER_PRECISION_SOURCE_ID_MISSING", "/identifiers"),)
        )
    if not _timestamps_valid(identifiers):
        return ValidationResult(
            "DENY", None, (Finding("IDENTIFIER_PRECISION_VALID_TIME_INVALID", "/identifiers"),)
        )
    if not _supersession_valid(identifiers):
        return ValidationResult(
            "DENY", None, (Finding("IDENTIFIER_PRECISION_SUPERSESSION_INVALID", "/identifiers"),)
        )

    crosswalk_valid, crosswalk_code = _crosswalk_valid(document)
    if not crosswalk_valid:
        return ValidationResult("DENY", None, (Finding(crosswalk_code, "/crosswalk"),))
    if not _precision_valid(document["precision"]):
        return ValidationResult(
            "DENY", None, (Finding("IDENTIFIER_PRECISION_TRANSFORM_INVALID", "/precision"),)
        )

    summary = expected_summary(document)
    if document["summary"] != summary:
        return ValidationResult(
            "DENY", None, (Finding("IDENTIFIER_PRECISION_SUMMARY_MISMATCH", "/summary"),)
        )

    actual_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], actual_hash):
        return ValidationResult(
            "DENY", None, (Finding("IDENTIFIER_PRECISION_SPEC_HASH_MISMATCH", "/spec_hash"),)
        )
    actual_id = expected_assessment_id(actual_hash)
    if not hmac.compare_digest(document["assessment_id"], actual_id):
        return ValidationResult(
            "DENY", None, (Finding("IDENTIFIER_PRECISION_ID_MISMATCH", "/assessment_id"),)
        )
    status = "PASS" if summary["lineage_outcome"] == "RESOLVED" else "ABSTAIN"
    return ValidationResult(status, summary["lineage_outcome"], ())


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
        value = json.load(
            stream,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    if not isinstance(value, dict):
        raise ValueError("candidate root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        findings = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.status != case["expected_status"]
            or result.outcome != case["expected_outcome"]
            or findings != case["expected_findings"]
        ):
            failures.append({
                "case_id": case["case_id"],
                "expected_status": case["expected_status"],
                "actual_status": result.status,
                "expected_outcome": case["expected_outcome"],
                "actual_outcome": result.outcome,
                "expected_findings": case["expected_findings"],
                "actual_findings": findings,
            })
    print(json.dumps(
        {"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures},
        sort_keys=True,
        separators=(",", ":"),
    ))
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
    except (OSError, UnicodeError):
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_UNREADABLE", "/"),))
    except json.JSONDecodeError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INVALID", "/"),))
    except (ValueError, RecursionError):
        result = ValidationResult("ERROR", None, (Finding("JSON_ROOT_INVALID", "/"),))
    print(json.dumps({
        "status": result.status,
        "outcome": result.outcome,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
    }, sort_keys=True, separators=(",", ":")))
    return 0 if result.status in {"PASS", "ABSTAIN"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
