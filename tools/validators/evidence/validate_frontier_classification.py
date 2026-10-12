#!/usr/bin/env python3
"""Validate the synthetic-only FrontierClassification fixture packet."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.evidence._frontier_classification_evaluate import (  # noqa: E402
    _assessment_ref,
    materialize_scenario,
)
from tools.validators.evidence._frontier_classification_common import (  # noqa: E402
    CASES_PATH,
    IDENTITY_PREFIX,
    MAX_FINDINGS,
    SCHEMA_PATH,
    SCOPE,
    CanonicalizationFailure,
    Finding,
    FixtureContext,
    JsonInputError,
    Result,
    _canonical_strings,
    _digest_ref,
    _identity_projection,
    _list,
    _mapping,
    _pointer,
    _set_pointer,
    _time,
    compute_spec_hash,
    load_json_file,
    seal,
    validate_access_observation,
    validate_county_year_panel,
    validate_frontier_definition,
    validate_population_observation,
)

def _schema_findings(candidate: object) -> tuple[Finding, ...]:
    try:
        schema = load_json_file(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(
                schema, format_checker=FormatChecker()
            ).iter_errors(candidate),
            key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator)),
        )
    except (JsonInputError, TypeError, ValueError, RecursionError):
        return (Finding("SCHEMA_UNAVAILABLE", "/"),)
    return tuple(
        sorted(
            {
                Finding("SCHEMA_INVALID", _pointer(tuple(error.absolute_path)))
                for error in errors[:MAX_FINDINGS]
            }
        )
    )


def _dependency_outcome(result: object) -> str | None:
    return getattr(result, "outcome", None)


def validate_context(context: FixtureContext) -> Result:
    if context.force_registry_error:
        return Result("ERROR", (Finding("FIXTURE_REGISTRY_ERROR", "/"),))
    candidate = context.candidate
    findings: set[Finding] = set(_schema_findings(candidate))
    if not isinstance(candidate, Mapping):
        return Result("DENY", tuple(sorted(findings)))
    if _mapping(candidate.get("subject")).get("synthetic_subject") is not True:
        findings.add(Finding("REAL_SUBJECT_DENIED", "/subject/synthetic_subject"))

    try:
        expected_hash = compute_spec_hash(_identity_projection(candidate))
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("CANONICALIZATION_ERROR", "/"))
        return Result("DENY", tuple(sorted(findings)))
    expected_id = IDENTITY_PREFIX + expected_hash.removeprefix("sha256:")
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("assessment_id") != expected_id:
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    if _dependency_outcome(validate_frontier_definition(context.definition)) != "PASS":
        findings.add(Finding("FRONTIER_DEFINITION_DEPENDENCY_INVALID", "/inputs/frontier_definition_ref"))
    if _dependency_outcome(validate_county_year_panel(context.panel)) != "PASS":
        findings.add(Finding("COUNTY_YEAR_PANEL_DEPENDENCY_INVALID", "/inputs/county_year_panel_ref"))
    for reference, wrapper in sorted(context.observations.items()):
        document = _mapping(wrapper.get("document"))
        result = (
            validate_access_observation(document)
            if wrapper.get("kind") == "ACCESS"
            else validate_population_observation(document)
        )
        if _dependency_outcome(result) != "PASS":
            findings.add(Finding("OBSERVATION_DEPENDENCY_INVALID", f"/registry/observations/{reference}"))

    inputs = _mapping(candidate.get("inputs"))
    expected_panel_ref = _digest_ref(
        "county-year-panel/synthetic-2020", context.panel["spec_hash"]
    )
    if (
        inputs.get("county_year_panel_ref") != expected_panel_ref
        or inputs.get("county_year_panel_id") != context.panel.get("panel_id")
        or inputs.get("county_year_panel_spec_hash") != context.panel.get("spec_hash")
    ):
        findings.add(Finding("PANEL_BINDING_MISMATCH", "/inputs"))
    expected_definition_ref = _mapping(context.panel.get("panel_scope")).get(
        "frontier_definition_ref"
    )
    if (
        inputs.get("frontier_definition_ref") != expected_definition_ref
        or inputs.get("frontier_definition_id") != context.definition.get("definition_id")
        or inputs.get("frontier_definition_spec_hash")
        != context.definition.get("spec_hash")
    ):
        findings.add(Finding("DEFINITION_BINDING_MISMATCH", "/inputs"))

    subject = _mapping(candidate.get("subject"))
    panel_scope = _mapping(context.panel.get("panel_scope"))
    if (
        subject.get("county_identifier_digest")
        != panel_scope.get("county_identifier_digest")
        or subject.get("calendar_year") != panel_scope.get("calendar_year")
        or subject.get("geography_version_ref")
        != panel_scope.get("geography_version_ref")
    ):
        findings.add(Finding("SUBJECT_PANEL_MISMATCH", "/subject"))

    method = _mapping(candidate.get("method"))
    definition_rule = _mapping(context.definition.get("classification")).get(
        "combination_rule"
    )
    if method.get("combination_rule") != definition_rule:
        findings.add(Finding("METHOD_COMBINATION_RULE_MISMATCH", "/method/combination_rule"))

    actual_traces = _list(candidate.get("criteria"))
    actual_keys = [
        _mapping(item).get("criterion_key") for item in actual_traces
    ]
    expected_keys = [item["criterion_key"] for item in context.expected_traces]
    if actual_keys != expected_keys:
        findings.add(Finding("CRITERION_TRACE_SET_MISMATCH", "/criteria"))
    elif actual_traces != context.expected_traces:
        findings.add(Finding("CRITERION_TRACE_MISMATCH", "/criteria"))
    if actual_keys != sorted(actual_keys) or len(actual_keys) != len(set(actual_keys)):
        findings.add(Finding("CRITERION_TRACE_ORDER_INVALID", "/criteria"))
    for index, raw in enumerate(actual_traces):
        trace = _mapping(raw)
        for field in ("reason_codes",):
            if not _canonical_strings(trace.get(field)):
                findings.add(Finding("TRACE_CODES_NOT_CANONICAL", f"/criteria/{index}/{field}"))

    if candidate.get("classification") != context.expected_classification:
        findings.add(Finding("CLASSIFICATION_OUTPUT_MISMATCH", "/classification"))
    if candidate.get("posture") != context.expected_posture:
        findings.add(Finding("POSTURE_OUTPUT_MISMATCH", "/posture"))

    classification = _mapping(candidate.get("classification"))
    if not _canonical_strings(classification.get("reason_codes")):
        findings.add(Finding("CLASSIFICATION_CODES_NOT_CANONICAL", "/classification/reason_codes"))
    posture = _mapping(candidate.get("posture"))
    if not _canonical_strings(posture.get("obligations")):
        findings.add(Finding("POSTURE_OBLIGATIONS_NOT_CANONICAL", "/posture/obligations"))

    generated_at = _time(_mapping(candidate.get("metadata")).get("generated_at"))
    if generated_at is None:
        findings.add(Finding("GENERATED_TIME_INVALID", "/metadata/generated_at"))

    lineage = _mapping(candidate.get("lineage"))
    corrected_refs = lineage.get("corrected_input_refs")
    if not isinstance(corrected_refs, list) or corrected_refs != sorted(set(corrected_refs)):
        findings.add(Finding("CORRECTED_INPUT_REFS_NOT_CANONICAL", "/lineage/corrected_input_refs"))
    if lineage.get("state") == "ORIGINAL":
        if (
            lineage.get("supersedes_assessment_ref") is not None
            or lineage.get("correction_record_ref") is not None
            or corrected_refs
        ):
            findings.add(Finding("ORIGINAL_LINEAGE_INVALID", "/lineage"))
    elif lineage.get("state") == "CORRECTED":
        if lineage.get("supersedes_assessment_ref") is None:
            findings.add(Finding("CORRECTION_PREDECESSOR_REQUIRED", "/lineage/supersedes_assessment_ref"))
        if lineage.get("correction_record_ref") is None:
            findings.add(Finding("CORRECTION_RECORD_REQUIRED", "/lineage/correction_record_ref"))
        if not corrected_refs:
            findings.add(Finding("CORRECTED_INPUT_REQUIRED", "/lineage/corrected_input_refs"))
        if lineage.get("supersedes_assessment_ref") == _assessment_ref(candidate):
            findings.add(Finding("ASSESSMENT_SELF_SUPERSESSION", "/lineage/supersedes_assessment_ref"))
        if context.prior_assessment is None:
            findings.add(Finding("PRIOR_ASSESSMENT_FIXTURE_REQUIRED", "/lineage/supersedes_assessment_ref"))
        elif lineage.get("supersedes_assessment_ref") != _assessment_ref(context.prior_assessment):
            findings.add(Finding("CORRECTION_PREDECESSOR_MISMATCH", "/lineage/supersedes_assessment_ref"))

    return Result("DENY" if findings else "PASS", tuple(sorted(findings)))


def load_fixture_manifest(path: Path = CASES_PATH) -> Mapping[str, Any]:
    manifest = load_json_file(path)
    if (
        not isinstance(manifest, Mapping)
        or not isinstance(manifest.get("base"), Mapping)
        or not isinstance(manifest.get("cases"), list)
    ):
        raise ValueError("fixture matrix is invalid")
    return manifest


def materialize_case(
    manifest: Mapping[str, Any], raw_case: Mapping[str, Any]
) -> FixtureContext:
    if not isinstance(raw_case.get("case_id"), str):
        raise ValueError("fixture case id is invalid")
    scenario = copy.deepcopy(dict(_mapping(manifest.get("base"))))
    for mutation in _list(raw_case.get("scenario_mutations")):
        if not isinstance(mutation, Mapping) or not isinstance(mutation.get("path"), str) or "value" not in mutation:
            raise ValueError("scenario mutation is invalid")
        _set_pointer(scenario, mutation["path"], mutation["value"])
    context = materialize_scenario(scenario)
    for mutation in _list(raw_case.get("candidate_mutations")):
        if not isinstance(mutation, Mapping) or not isinstance(mutation.get("path"), str) or "value" not in mutation:
            raise ValueError("candidate mutation is invalid")
        _set_pointer(context.candidate, mutation["path"], mutation["value"])
    if raw_case.get("reseal_candidate") is True:
        context.candidate = seal(context.candidate)
    context.force_registry_error = raw_case.get("force_registry_error") is True
    return context


def fixture_cases(
    path: Path = CASES_PATH,
) -> list[tuple[Mapping[str, Any], FixtureContext, Result]]:
    manifest = load_fixture_manifest(path)
    materialized = []
    for raw in _list(manifest.get("cases")):
        if not isinstance(raw, Mapping):
            raise ValueError("fixture case is invalid")
        context = materialize_case(manifest, raw)
        materialized.append((raw, context, validate_context(context)))
    return materialized


def fixture_profile(path: Path = CASES_PATH) -> int:
    try:
        cases = fixture_cases(path)
    except (JsonInputError, ValueError, TypeError, KeyError, IndexError, CanonicalizationFailure):
        print(
            json.dumps(
                {
                    "scope": SCOPE,
                    "status": "ERROR",
                    "reason": "FIXTURE_MATRIX_INVALID",
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2
    failures: list[dict[str, Any]] = []
    counts = {"FRONTIER": 0, "NOT_FRONTIER": 0, "UNCLASSIFIED": 0}
    for raw, context, result in cases:
        expected_outcome = raw.get("expected_validation_outcome")
        expected_findings = set(_list(raw.get("expected_findings")))
        actual_codes = {finding.code for finding in result.findings}
        expected_classification = raw.get("expected_classification")
        actual_classification = _mapping(context.candidate.get("classification")).get("value")
        if actual_classification in counts:
            counts[actual_classification] += 1
        reasons = set(
            _list(_mapping(context.candidate.get("classification")).get("reason_codes"))
        )
        expected_reasons = set(_list(raw.get("expected_classification_reasons")))
        if (
            result.outcome != expected_outcome
            or not expected_findings.issubset(actual_codes)
            or (
                expected_classification is not None
                and actual_classification != expected_classification
            )
            or not expected_reasons.issubset(reasons)
        ):
            failures.append(
                {
                    "case_id": raw.get("case_id"),
                    "expected_outcome": expected_outcome,
                    "actual_outcome": result.outcome,
                    "expected_findings": sorted(expected_findings),
                    "actual_findings": sorted(actual_codes),
                    "expected_classification": expected_classification,
                    "actual_classification": actual_classification,
                }
            )
    payload = {
        "cases": len(cases),
        "classification_counts": counts,
        "failures": failures,
        "scope": SCOPE,
        "status": "FAIL" if failures else "PASS",
    }
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return 1 if failures else 0


def _serialize_case(case_id: str, context: FixtureContext, result: Result) -> str:
    return json.dumps(
        {
            "assessment_id": context.candidate.get("assessment_id"),
            "case_id": case_id,
            "classification": _mapping(context.candidate.get("classification")).get("value"),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": [
                "no_network",
                "no_real_county_classification",
                "no_source_activation",
                "no_threshold_or_policy_change",
                "no_lifecycle_write",
                "no_review_or_release_authority",
                "no_publication_or_deployment",
                "no_public_api_or_map_output",
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--case", metavar="CASE_ID")
    args = parser.parse_args(argv)
    if args.fixtures:
        return fixture_profile()
    try:
        manifest = load_fixture_manifest()
        raw = next(
            item
            for item in _list(manifest.get("cases"))
            if isinstance(item, Mapping) and item.get("case_id") == args.case
        )
        context = materialize_case(manifest, raw)
        result = validate_context(context)
    except StopIteration:
        print(
            json.dumps(
                {
                    "case_id": args.case,
                    "findings": [{"code": "FIXTURE_CASE_NOT_FOUND", "path": "/"}],
                    "outcome": "ERROR",
                    "scope": SCOPE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2
    except (JsonInputError, ValueError, TypeError, KeyError, IndexError, CanonicalizationFailure):
        print(
            json.dumps(
                {
                    "case_id": args.case,
                    "findings": [{"code": "FIXTURE_REGISTRY_ERROR", "path": "/"}],
                    "outcome": "ERROR",
                    "scope": SCOPE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2
    print(_serialize_case(args.case, context, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(run())
