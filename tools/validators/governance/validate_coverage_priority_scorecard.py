#!/usr/bin/env python3
"""Validate fixture-only coverage-aware priority scorecards.

A coherent scorecard returns HOLD, never ALLOW. Validation creates no ecological
claim, source activation, work assignment, policy, review, release, publication,
or public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
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

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/coverage_priority_scorecard.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/coverage_priority_scorecard/cases.json"
IDENTITY_PREFIX = "kfm:coverage-priority-scorecard:"
SCOPE = "coverage-priority-scorecard-fixture-only-v1"
METRICS = (
    "data_richness",
    "recency",
    "sampling_effort",
    "source_diversity",
    "geographic_coverage_gap",
    "uncertainty_reduction",
    "sensitivity_burden",
    "steward_capacity",
    "public_value",
    "review_cost",
)
COST_METRICS = frozenset({"sensitivity_burden", "review_cost"})
OBLIGATIONS = (
    "DISPLAY_ALL_SCORE_COMPONENTS",
    "LABEL_WORKFLOW_TRIAGE_ONLY",
    "DO_NOT_INFER_ECOLOGICAL_IMPORTANCE",
)


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


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _identity_projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {key: copy.deepcopy(value) for key, value in candidate.items() if key not in {"scorecard_id", "spec_hash"}}


def seal(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    digest = compute_spec_hash(_identity_projection(value))
    value["spec_hash"] = digest
    value["scorecard_id"] = IDENTITY_PREFIX + digest.removeprefix("sha256:")
    return value


def _component_scores(metrics: Mapping[str, Any], weights: Mapping[str, Any], strategy: str) -> dict[str, int | None]:
    components: dict[str, int | None] = {}
    for name in METRICS:
        metric = metrics.get(name)
        weight = weights.get(name)
        if metric is None:
            components[name] = None if strategy == "ABSTAIN" else 0
            continue
        contribution = int(metric) * int(weight)
        components[name] = -contribution if name in COST_METRICS else contribution
    return components


def _ranking(profile: Mapping[str, Any], candidates: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    weights = _mapping(profile.get("weights"))
    missingness = _mapping(profile.get("missingness"))
    strategy = str(missingness.get("strategy"))
    penalty_points = int(missingness.get("penalty_points", 0))
    cap = int(profile.get("source_role_cap_basis_points", 0))
    entries: list[dict[str, Any]] = []
    for candidate in candidates:
        metrics = _mapping(candidate.get("metrics"))
        components = _component_scores(metrics, weights, strategy)
        missing_count = sum(value is None for value in metrics.values())
        penalty = missing_count * penalty_points if strategy == "PENALIZE" else 0
        shares = candidate.get("source_role_shares")
        maximum_share = max((int(_mapping(item).get("share_basis_points", 0)) for item in shares), default=0) if isinstance(shares, list) else 0
        cap_exceeded = maximum_share > cap
        score: int | None
        if cap_exceeded or (missing_count and strategy == "ABSTAIN"):
            score = None
        else:
            score = sum(value for value in components.values() if value is not None) - penalty
        entries.append(
            {
                "area_ref": candidate.get("area_ref"),
                "component_scores": components,
                "missingness_penalty": penalty,
                "source_role_cap_exceeded": cap_exceeded,
                "score": score,
                "rank": None,
            }
        )
    ranked = sorted(entries, key=lambda item: (item["score"] is None, -(item["score"] or 0), str(item["area_ref"])))
    next_rank = 1
    for entry in ranked:
        if entry["score"] is not None:
            entry["rank"] = next_rank
            next_rank += 1
    return {"profile_id": profile.get("profile_id"), "entries": ranked}


def _stability(rankings: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    first, second = rankings[0], rankings[1]
    first_ranks = {entry.get("area_ref"): entry.get("rank") for entry in first.get("entries", []) if isinstance(entry, Mapping) and entry.get("rank") is not None}
    second_ranks = {entry.get("area_ref"): entry.get("rank") for entry in second.get("entries", []) if isinstance(entry, Mapping) and entry.get("rank") is not None}
    shared = sorted(set(first_ranks) & set(second_ranks))
    profile_ids = [first.get("profile_id"), second.get("profile_id")]
    if len(shared) < 2:
        return {
            "compared_profile_ids": profile_ids,
            "rank_correlation_milli": None,
            "rank_flip_count": None,
            "stable": False,
            "counterfactual_status": "INSUFFICIENT_COMPARABLE_RANKS",
        }
    sum_squared = sum((int(first_ranks[area]) - int(second_ranks[area])) ** 2 for area in shared)
    count = len(shared)
    correlation = round(1000 * (1 - (6 * sum_squared) / (count * (count * count - 1))))
    flips = sum(first_ranks[area] != second_ranks[area] for area in shared)
    return {
        "compared_profile_ids": profile_ids,
        "rank_correlation_milli": correlation,
        "rank_flip_count": flips,
        "stable": flips == 0,
        "counterfactual_status": "RANKING_UNCHANGED" if flips == 0 else "RANKING_CHANGED",
    }


def derive_outputs(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    profiles = [item for item in value.get("weight_profiles", []) if isinstance(item, Mapping)]
    candidates = [item for item in value.get("candidates", []) if isinstance(item, Mapping)]
    rankings = [_ranking(profile, candidates) for profile in profiles]
    value["rankings"] = rankings
    value["stability"] = _stability(rankings)
    unresolved = any(entry["score"] is None for ranking in rankings for entry in ranking["entries"])
    value["decision"] = {
        "outcome": "ABSTAIN" if unresolved else "HOLD",
        "reason_codes": ["PRIORITY_INPUT_INCOMPLETE" if unresolved else "COUNTERFACTUAL_RANKING_REVIEW_REQUIRED"],
        "obligations": list(OBLIGATIONS),
    }
    return value


def _semantic_shape_findings(candidate: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    profiles = candidate.get("weight_profiles")
    candidates = candidate.get("candidates")
    if not isinstance(profiles, list) or not isinstance(candidates, list):
        return {Finding("PRIORITY_INPUT_INVALID", "/")}

    profile_ids = [item.get("profile_id") for item in profiles if isinstance(item, Mapping)]
    if len(profile_ids) != len(set(profile_ids)):
        findings.add(Finding("WEIGHT_PROFILE_ID_DUPLICATE", "/weight_profiles"))
    for index, raw_profile in enumerate(profiles):
        profile = _mapping(raw_profile)
        weights = _mapping(profile.get("weights"))
        if sum(value for value in weights.values() if isinstance(value, int) and not isinstance(value, bool)) != 1000:
            findings.add(Finding("WEIGHT_SUM_INVALID", f"/weight_profiles/{index}/weights"))

    area_refs = [item.get("area_ref") for item in candidates if isinstance(item, Mapping)]
    if len(area_refs) != len(set(area_refs)):
        findings.add(Finding("CANDIDATE_AREA_DUPLICATE", "/candidates"))
    for index, raw_candidate in enumerate(candidates):
        item = _mapping(raw_candidate)
        metrics = _mapping(item.get("metrics"))
        declared = item.get("missing_metrics")
        expected = sorted(name.upper() for name in METRICS if metrics.get(name) is None)
        if not isinstance(declared, list) or sorted(declared) != expected:
            findings.add(Finding("MISSING_METRIC_DECLARATION_MISMATCH", f"/candidates/{index}/missing_metrics"))
        shares = item.get("source_role_shares")
        if isinstance(shares, list):
            roles = [_mapping(share).get("role_code") for share in shares]
            if len(roles) != len(set(roles)):
                findings.add(Finding("SOURCE_ROLE_DUPLICATE", f"/candidates/{index}/source_role_shares"))
            total = sum(int(_mapping(share).get("share_basis_points", 0)) for share in shares)
            if total != 10000:
                findings.add(Finding("SOURCE_ROLE_SHARE_SUM_INVALID", f"/candidates/{index}/source_role_shares"))
    return findings


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
    if candidate.get("scorecard_id") != expected_id:
        findings.add(Finding("SCORECARD_ID_MISMATCH", "/scorecard_id"))

    shape_findings = _semantic_shape_findings(candidate)
    findings.update(shape_findings)
    if not shape_findings:
        expected = derive_outputs(candidate)
        if candidate.get("rankings") != expected.get("rankings"):
            findings.add(Finding("RANKING_DERIVATION_MISMATCH", "/rankings"))
        if candidate.get("stability") != expected.get("stability"):
            findings.add(Finding("STABILITY_DERIVATION_MISMATCH", "/stability"))
        if candidate.get("decision") != expected.get("decision"):
            findings.add(Finding("PRIORITY_DECISION_MISMATCH", "/decision"))
    return Result("DENY" if findings else "HOLD", tuple(sorted(findings)))


def validate_file(path: Path | str) -> Result:
    try:
        return validate_document(load_json_file(path))
    except JsonInputError:
        return Result("DENY", (Finding("INPUT_JSON_INVALID", "/"),))
    except (KeyError, TypeError, ValueError, CanonicalizationFailure, IndexError):
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
        if not isinstance(expected_outcome, str) or not isinstance(expected_findings, list):
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
        parser.error("provide scorecard files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        result = validate_file(path)
        print(json.dumps({"file": _display(path), "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings], "outcome": result.outcome, "scope": SCOPE}, sort_keys=True, separators=(",", ":")))
        rc = max(rc, 0 if result.coherent else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
