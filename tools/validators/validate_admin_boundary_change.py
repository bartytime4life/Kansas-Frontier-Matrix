#!/usr/bin/env python3
"""Validate fixture-only AdminBoundaryChange records."""
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
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/common/admin_boundary_change.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/common/admin_boundary_change/cases.json"
PREFIX = "kfm:admin-boundary-change:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
REQUIRED_LIMITS = {
    "EVENT_ONLY",
    "NO_CROSS_VERSION_IDENTITY_INFERENCE",
    "NO_CROSSWALK_INFERENCE",
    "NO_GEOMETRY",
    "NO_OBSERVATION_TRANSFER",
    "NO_PUBLICATION_AUTHORITY",
    "SOURCE_ROLE_PRESERVED",
    "VERSION_BOUND",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
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
            return None, (Finding("ADMIN_BOUNDARY_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("ADMIN_BOUNDARY_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("ADMIN_BOUNDARY_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("ADMIN_BOUNDARY_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("ADMIN_BOUNDARY_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("ADMIN_BOUNDARY_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ADMIN_BOUNDARY_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    findings = {
        Finding("ADMIN_BOUNDARY_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = dict(value)
    subject.pop("change_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _aware_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _sorted_unique(values: Sequence[str]) -> bool:
    return list(values) == sorted(set(values))


def _event_cardinality_valid(change_type: str, lineage: Mapping[str, Any]) -> bool:
    source_versions = len(lineage["source_geography_version_refs"])
    target_versions = len(lineage["target_geography_version_refs"])
    predecessors = len(lineage["predecessor_feature_refs"])
    successors = len(lineage["successor_feature_refs"])
    if change_type == "CREATION":
        return source_versions == predecessors == 0 and target_versions >= 1 and successors >= 1
    if change_type == "DISSOLUTION":
        return source_versions >= 1 and predecessors >= 1 and target_versions == successors == 0
    if change_type == "SPLIT":
        return source_versions >= 1 and predecessors >= 1 and target_versions >= 2 and successors >= 2
    if change_type == "MERGER":
        return source_versions >= 2 and predecessors >= 2 and target_versions >= 1 and successors >= 1
    return source_versions >= 1 and predecessors >= 1 and target_versions >= 1 and successors >= 1


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    change = value["change"]
    lineage = value["lineage"]
    support = value["support"]
    disclosure = value["disclosure"]

    if _aware_datetime(change["retrieved_at"]) < _aware_datetime(change["source_published_at"]):
        findings.add(Finding("ADMIN_BOUNDARY_RETRIEVAL_PRECEDES_PUBLICATION", "/change/retrieved_at"))

    array_fields = (
        "source_geography_version_refs",
        "target_geography_version_refs",
        "predecessor_feature_refs",
        "successor_feature_refs",
    )
    for field in array_fields:
        if not _sorted_unique(lineage[field]):
            findings.add(Finding("ADMIN_BOUNDARY_LINEAGE_ORDER_INVALID", f"/lineage/{field}"))

    if set(lineage["source_geography_version_refs"]) & set(lineage["target_geography_version_refs"]):
        findings.add(Finding("ADMIN_BOUNDARY_VERSION_SIDES_OVERLAP", "/lineage/target_geography_version_refs"))
    if set(lineage["predecessor_feature_refs"]) & set(lineage["successor_feature_refs"]):
        findings.add(Finding("ADMIN_BOUNDARY_FEATURE_SIDES_OVERLAP", "/lineage/successor_feature_refs"))
    if not _event_cardinality_valid(change["change_type"], lineage):
        findings.add(Finding("ADMIN_BOUNDARY_EVENT_CARDINALITY_INVALID", "/lineage"))

    source_exists = bool(lineage["source_geography_version_refs"])
    target_exists = bool(lineage["target_geography_version_refs"])
    state = lineage["crosswalk_state"]
    crosswalk_ref = lineage["crosswalk_ref"]
    if not (source_exists and target_exists):
        if state != "NOT_APPLICABLE":
            findings.add(Finding("ADMIN_BOUNDARY_CROSSWALK_STATE_NOT_APPLICABLE_REQUIRED", "/lineage/crosswalk_state"))
        if crosswalk_ref is not None:
            findings.add(Finding("ADMIN_BOUNDARY_CROSSWALK_REF_UNEXPECTED", "/lineage/crosswalk_ref"))
    else:
        if state == "NOT_APPLICABLE":
            findings.add(Finding("ADMIN_BOUNDARY_CROSSWALK_STATE_REQUIRED", "/lineage/crosswalk_state"))
        elif state == "REFERENCED_NOT_RESOLVED" and crosswalk_ref is None:
            findings.add(Finding("ADMIN_BOUNDARY_CROSSWALK_REF_REQUIRED", "/lineage/crosswalk_ref"))
        elif state == "UNRESOLVED" and crosswalk_ref is not None:
            findings.add(Finding("ADMIN_BOUNDARY_CROSSWALK_REF_UNEXPECTED", "/lineage/crosswalk_ref"))

    if not _sorted_unique(support["evidence_refs"]):
        findings.add(Finding("ADMIN_BOUNDARY_EVIDENCE_ORDER_INVALID", "/support/evidence_refs"))
    limits = disclosure["interpretation_limits"]
    if not _sorted_unique(limits):
        findings.add(Finding("ADMIN_BOUNDARY_LIMIT_ORDER_INVALID", "/disclosure/interpretation_limits"))
    if not REQUIRED_LIMITS.issubset(set(limits)):
        findings.add(Finding("ADMIN_BOUNDARY_REQUIRED_LIMIT_MISSING", "/disclosure/interpretation_limits"))

    try:
        digest, identifier = canonical_identity(value)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("ADMIN_BOUNDARY_IDENTITY_ERROR", "/spec_hash"))
    else:
        if value["spec_hash"] != digest:
            findings.add(Finding("ADMIN_BOUNDARY_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["change_id"] != identifier:
            findings.add(Finding("ADMIN_BOUNDARY_CHANGE_ID_MISMATCH", "/change_id"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    findings = _semantic_findings(value)
    return Result("DENY", findings) if findings else Result("PASS", ())


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in manifest["variants"][case["base"]]:
        _replace(document, mutation["path"], mutation.get("value"))
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["change_id"] = case.get("change_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            failures.append({"case_id": case["case_id"], "actual_outcome": result.outcome, "actual_findings": actual})
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": ["no_network", "no_source_access", "no_geography_or_geometry_resolution", "no_crosswalk_execution", "no_identity_inference", "no_observation_transfer", "no_evidence_resolution", "no_policy_or_review_approval", "no_promotion_or_release", "no_public_use_or_publication"],
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
