#!/usr/bin/env python3
"""Validate fixture-only, use-specific observation fitness assessments.

A coherent candidate returns HOLD, never ALLOW. Exclusion retains evidence and
does not establish truth, analysis, policy, review, release, or publication
authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages" / "hashing" / "src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/observation_fitness_assessment.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/observation_fitness_assessment/cases.json"
IDENTITY_PREFIX = "kfm:observation-fitness:"
SCOPE = "observation-fitness-fixture-only-v1"


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def coherent(self) -> bool:
        return self.outcome == "HOLD" and not self.findings


DECISION_RULES: dict[str, tuple[str, str, tuple[str, ...]]] = {
    "FIT": (
        "INCLUDE",
        "OBSERVATION_FIT_FOR_DECLARED_USE",
        ("DISPLAY_DECLARED_USE", "PRESERVE_CONTEXT_SNAPSHOT"),
    ),
    "CONDITIONALLY_FIT": (
        "INCLUDE_WITH_QUALIFICATION",
        "PERSISTENCE_SUPPORT_INSUFFICIENT",
        ("DISPLAY_DECLARED_USE", "LABEL_SINGLE_OBSERVATION_LIMIT", "PRESERVE_CONTEXT_SNAPSHOT"),
    ),
    "EXCLUDED": (
        "RETAIN_AND_EXCLUDE",
        "OBSERVATION_UNFIT_FOR_DECLARED_USE",
        ("RETAIN_EXCLUDED_EVIDENCE", "DISPLAY_EXCLUSION_REASON", "REASSESS_AFTER_CONTEXT_CORRECTION"),
    ),
    "UNKNOWN": (
        "ABSTAIN",
        "OBSERVATION_FITNESS_UNRESOLVED",
        ("RETAIN_OBSERVATION_EVIDENCE", "RESOLVE_FITNESS_CONTEXT"),
    ),
}


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _list(value: object) -> list[Any]:
    return list(value) if isinstance(value, list) else []


def _identity_projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {key: copy.deepcopy(value) for key, value in candidate.items() if key not in {"assessment_id", "spec_hash"}}


def seal(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    digest = compute_spec_hash(_identity_projection(value))
    value["spec_hash"] = digest
    value["assessment_id"] = IDENTITY_PREFIX + digest.removeprefix("sha256:")
    return value


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _derive_state(candidate: Mapping[str, Any]) -> str:
    observation = _mapping(candidate.get("observation"))
    context = _mapping(candidate.get("context_snapshot"))
    confounders = [_mapping(item) for item in _list(context.get("confounders"))]
    quality = observation.get("quality_state")
    persistence = _mapping(context.get("persistence_support")).get("state")
    states = {item.get("state") for item in confounders}
    if quality in {"FAIL", "STALE"} or "PRESENT" in states:
        return "EXCLUDED"
    if quality == "UNKNOWN" or "UNKNOWN" in states or persistence == "UNKNOWN":
        return "UNKNOWN"
    if persistence == "UNSUPPORTED":
        return "CONDITIONALLY_FIT"
    return "FIT"


def _required_evidence(candidate: Mapping[str, Any]) -> set[str]:
    observation = _mapping(candidate.get("observation"))
    context = _mapping(candidate.get("context_snapshot"))
    refs: set[str] = set()
    for field in ("evidence_bundle_refs", "quality_evidence_refs"):
        refs.update(item for item in _list(observation.get(field)) if isinstance(item, str))
    for item in _list(context.get("confounders")):
        refs.update(ref for ref in _list(_mapping(item).get("evidence_refs")) if isinstance(ref, str))
    persistence = _mapping(context.get("persistence_support"))
    refs.update(ref for ref in _list(persistence.get("evidence_refs")) if isinstance(ref, str))
    return refs


def derive_outputs(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    state = _derive_state(value)
    handling, reason, obligations = DECISION_RULES[state]
    value["decision"] = {
        "state": state,
        "handling": handling,
        "reason_codes": [reason],
        "obligations": list(obligations),
        "retained_evidence_refs": sorted(_required_evidence(value)),
    }
    return value


def validate_document(candidate: object) -> Result:
    findings: set[Finding] = set()
    try:
        schema = load_json_file(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
            key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator)),
        )
    except (JsonInputError, ValueError, TypeError, RecursionError):
        return Result("DENY", (Finding("SCHEMA_UNAVAILABLE", "/"),))
    findings.update(Finding("SCHEMA_INVALID", _pointer(tuple(error.absolute_path))) for error in errors[:100])
    if errors or not isinstance(candidate, Mapping):
        return Result("DENY", tuple(sorted(findings)))

    try:
        expected_hash = compute_spec_hash(_identity_projection(candidate))
    except (CanonicalizationFailure, TypeError, ValueError):
        return Result("DENY", (Finding("CANONICALIZATION_ERROR", "/"),))
    expected_id = IDENTITY_PREFIX + expected_hash.removeprefix("sha256:")
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("assessment_id") != expected_id:
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    observation = _mapping(candidate.get("observation"))
    declared_use = _mapping(candidate.get("declared_use"))
    context = _mapping(candidate.get("context_snapshot"))
    observed = _time(observation.get("observed_at"))
    start = _time(declared_use.get("interval_start"))
    end = _time(declared_use.get("interval_end"))
    captured = _time(context.get("captured_at"))
    evaluated = _time(candidate.get("evaluated_at"))
    if None in {observed, start, end, captured, evaluated}:
        findings.add(Finding("FITNESS_TIME_INVALID", "/"))
    elif not (start < end and observed <= captured <= evaluated):
        findings.add(Finding("FITNESS_TIME_ORDER_INVALID", "/context_snapshot/captured_at"))

    confounders = [_mapping(item) for item in _list(context.get("confounders"))]
    codes = [item.get("code") for item in confounders]
    if len(codes) != len(set(codes)):
        findings.add(Finding("CONFOUNDER_CONTEXT_CONTRADICTORY", "/context_snapshot/confounders"))
    for index, item in enumerate(confounders):
        if item.get("state") == "PRESENT" and item.get("mask_ref") is None:
            findings.add(Finding("PRESENT_CONFOUNDER_MASK_REQUIRED", f"/context_snapshot/confounders/{index}/mask_ref"))

    expected = derive_outputs(candidate).get("decision")
    if candidate.get("decision") != expected:
        findings.add(Finding("FITNESS_DECISION_MISMATCH", "/decision"))

    correction = _mapping(candidate.get("correction_lineage"))
    if correction.get("state") == "ORIGINAL":
        if correction.get("supersedes_assessment_ref") is not None or _list(correction.get("corrected_mask_refs")) or correction.get("reinterpretation_required") is True:
            findings.add(Finding("ORIGINAL_CORRECTION_FIELDS_INVALID", "/correction_lineage"))
    elif correction.get("state") == "CORRECTED":
        if correction.get("supersedes_assessment_ref") is None:
            findings.add(Finding("CORRECTION_PREDECESSOR_REQUIRED", "/correction_lineage/supersedes_assessment_ref"))
        if not _list(correction.get("corrected_mask_refs")):
            findings.add(Finding("CORRECTED_MASK_REQUIRED", "/correction_lineage/corrected_mask_refs"))
        if correction.get("reinterpretation_required") is not True:
            findings.add(Finding("REINTERPRETATION_FLAG_REQUIRED", "/correction_lineage/reinterpretation_required"))

    return Result("DENY" if findings else "HOLD", tuple(sorted(findings)))


def validate_file(path: Path | str) -> Result:
    try:
        return validate_document(load_json_file(path))
    except JsonInputError:
        return Result("DENY", (Finding("INPUT_JSON_INVALID", "/"),))
    except (KeyError, TypeError, ValueError, CanonicalizationFailure):
        return Result("DENY", (Finding("INPUT_OR_DEPENDENCY_ERROR", "/"),))


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.lstrip("/").split("/")]
    if not parts or parts == [""]:
        raise ValueError("root replacement is not supported")
    parent: Any = candidate
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    if isinstance(parent, list):
        parent[int(parts[-1])] = copy.deepcopy(value)
    else:
        parent[parts[-1]] = copy.deepcopy(value)


def fixture_cases(path: Path = CASES_PATH) -> list[tuple[Mapping[str, Any], Result, str, tuple[str, ...]]]:
    matrix = load_json_file(path)
    if not isinstance(matrix, Mapping) or not isinstance(matrix.get("base"), Mapping) or not isinstance(matrix.get("cases"), list):
        raise ValueError("fixture matrix is invalid")
    base = seal(derive_outputs(matrix["base"]))
    materialized = []
    for raw_case in matrix["cases"]:
        if not isinstance(raw_case, Mapping) or not isinstance(raw_case.get("name"), str):
            raise ValueError("fixture case is invalid")
        candidate = copy.deepcopy(base)
        for mutation in raw_case.get("mutations", []):
            if not isinstance(mutation, Mapping) or not isinstance(mutation.get("path"), str) or "value" not in mutation:
                raise ValueError("fixture mutation is invalid")
            _set_pointer(candidate, mutation["path"], mutation["value"])
        if raw_case.get("rederive", True) is True:
            candidate = derive_outputs(candidate)
        if raw_case.get("reseal", True) is True:
            candidate = seal(candidate)
        expected_outcome = raw_case.get("expected_outcome")
        expected_findings = raw_case.get("expected_findings", [])
        if not isinstance(expected_outcome, str) or not isinstance(expected_findings, list) or not all(isinstance(code, str) for code in expected_findings):
            raise ValueError("fixture expectations are invalid")
        materialized.append((candidate, validate_document(candidate), expected_outcome, tuple(expected_findings)))
    return materialized


def fixture_profile(path: Path = CASES_PATH) -> int:
    try:
        cases = fixture_cases(path)
    except (JsonInputError, ValueError, TypeError, KeyError, IndexError, CanonicalizationFailure):
        print(json.dumps({"scope": SCOPE, "status": "FAIL", "reason": "FIXTURE_MATRIX_INVALID"}, sort_keys=True, separators=(",", ":")))
        return 1
    failures = []
    for index, (_candidate, result, expected_outcome, expected_findings) in enumerate(cases):
        codes = {finding.code for finding in result.findings}
        if result.outcome != expected_outcome or not set(expected_findings).issubset(codes):
            failures.append(index)
    print(json.dumps({"cases": len(cases), "failed_case_indexes": failures, "scope": SCOPE, "status": "FAIL" if failures else "PASS"}, sort_keys=True, separators=(",", ":")))
    return 1 if failures else 0


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return fixture_profile()
    if not args.files:
        parser.error("provide assessment files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        result = validate_file(path)
        print(json.dumps({"file": _display(path), "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings], "outcome": result.outcome, "scope": SCOPE}, sort_keys=True, separators=(",", ":")))
        rc = max(rc, 0 if result.coherent else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
