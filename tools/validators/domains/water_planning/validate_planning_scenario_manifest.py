#!/usr/bin/env python3
"""Deterministic, no-network checks for the synthetic PlanningScenarioManifest.

PASS proves local shape, content identity, and bounded cross-field semantics only.
It creates no evidence, policy, review, release, UI-rendering, or publication authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import JsonInputError, compute_spec_hash, load_json_file

SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/water_planning/planning_scenario_manifest.schema.json"
FIXTURES = ROOT / "fixtures/domains/water_planning/planning_scenario_manifest"
VALID_FIXTURE = FIXTURES / "valid/valid_1.json"
INVALID_FIXTURE = FIXTURES / "invalid/invalid_1.json"
CASES_PATH = FIXTURES / "cases.json"
DENIED_PUBLIC_PREFIXES = ("raw:", "work:", "quarantine:", "internal:", "canonical:")
AUTHORITY_FIELDS = (
    "evidence_resolved",
    "policy_approved",
    "review_approved",
    "release_authorized",
    "publication_authorized",
)


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def canonical_body(document: dict[str, Any]) -> dict[str, Any]:
    body = copy.deepcopy(document)
    body.pop("spec_hash", None)
    return body


def expected_spec_hash(document: dict[str, Any]) -> str:
    return compute_spec_hash(canonical_body(document))


def _canonical(values: object) -> bool:
    return (
        isinstance(values, list)
        and all(isinstance(item, str) for item in values)
        and values == sorted(values)
        and len(values) == len(set(values))
    )


def _ids(items: list[dict[str, Any]], field: str) -> list[str]:
    return [str(item[field]) for item in items]


def _reference_lists(document: dict[str, Any]) -> Iterable[list[str]]:
    for field in ("participation_refs", "evidence_refs", "model_refs", "policy_decision_refs", "review_refs"):
        yield document[field]
    for item in document["assumptions"]:
        yield item["evidence_refs"]
    for item in document["equity_dimensions"]:
        yield item["evidence_refs"]
    yield document["public_summary"]["evidence_refs"]
    for field in ("assumption_refs", "equity_dimension_refs", "participation_refs", "evidence_refs"):
        yield document["drawer_payload"][field]


def _referenced_evidence(document: dict[str, Any]) -> set[str]:
    refs = {item["source_ref"] for item in document["input_variables"]}
    refs.update(item["evidence_ref"] for item in document["data_vintages"])
    for item in document["assumptions"]:
        refs.update(item["evidence_refs"])
    for item in document["equity_dimensions"]:
        refs.update(item["evidence_refs"])
    refs.update(document["public_summary"]["evidence_refs"])
    refs.update(document["drawer_payload"]["evidence_refs"])
    return refs


def validate(document: Any) -> tuple[str, list[str]]:
    if not isinstance(document, dict):
        return "ERROR", ["ROOT_NOT_OBJECT"]

    schema_errors = list(_schema_validator().iter_errors(document))
    if schema_errors:
        return "FAIL", ["SCHEMA_INVALID"]

    findings: set[str] = set()

    if document["spec_hash"] != expected_spec_hash(document):
        findings.add("SPEC_HASH_MISMATCH")

    horizon = document["time_horizon"]
    baseline = date.fromisoformat(horizon["baseline_as_of"])
    starts = date.fromisoformat(horizon["horizon_start"])
    ends = date.fromisoformat(horizon["horizon_end"])
    if baseline > starts or starts >= ends:
        findings.add("TEMPORAL_ORDER_INVALID")

    identity_lists = (
        _ids(document["input_variables"], "variable_id"),
        _ids(document["data_vintages"], "dataset_ref"),
        _ids(document["assumptions"], "assumption_id"),
        _ids(document["equity_dimensions"], "dimension_id"),
    )
    if not all(_canonical(values) for values in identity_lists) or not all(
        _canonical(values) for values in _reference_lists(document)
    ):
        findings.add("REFERENCE_ORDER_INVALID")

    drawer = document["drawer_payload"]
    expected_drawer_refs = (
        drawer["assumption_refs"] == _ids(document["assumptions"], "assumption_id")
        and drawer["equity_dimension_refs"] == _ids(document["equity_dimensions"], "dimension_id")
        and drawer["participation_refs"] == document["participation_refs"]
        and drawer["evidence_refs"] == document["public_summary"]["evidence_refs"]
    )
    if not expected_drawer_refs:
        findings.add("DRAWER_REFERENCE_MISMATCH")

    if drawer["outcome"] != document["public_summary"]["outcome"]:
        findings.add("SURFACE_OUTCOME_MISMATCH")

    declared_evidence = set(document["evidence_refs"])
    if not _referenced_evidence(document).issubset(declared_evidence):
        findings.add("EVIDENCE_SCOPE_MISMATCH")

    public_refs = document["public_summary"]["evidence_refs"] + drawer["evidence_refs"]
    if any(ref.startswith(DENIED_PUBLIC_PREFIXES) for ref in public_refs):
        findings.add("INTERNAL_REFERENCE_DENIED")

    governance = document["governance"]
    if any(governance[field] is not False for field in AUTHORITY_FIELDS):
        findings.add("AUTHORITY_OVERCLAIM")

    if document["status"] == "READY_FOR_REVIEW" and (
        not document["policy_decision_refs"] or not document["review_refs"]
    ):
        findings.add("READY_REVIEW_BINDINGS_REQUIRED")

    if document["status"] == "HELD" and document["public_summary"]["outcome"] == "NARROWED":
        findings.add("HELD_SURFACE_OUTCOME_INVALID")

    return ("PASS", []) if not findings else ("FAIL", sorted(findings))


def mutate(base: dict[str, Any], mutations: dict[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(base)
    for dotted_path, value in mutations.items():
        parts = dotted_path.split(".")
        target: dict[str, Any] = document
        for part in parts[:-1]:
            target = target[part]
        target[parts[-1]] = value
    if "spec_hash" not in mutations:
        document["spec_hash"] = expected_spec_hash(document)
    return document


def run_fixtures() -> int:
    try:
        base = load_json_file(VALID_FIXTURE)
        invalid = load_json_file(INVALID_FIXTURE)
        cases = load_json_file(CASES_PATH)
    except JsonInputError:
        print("PLANNING_SCENARIO_MANIFEST_FIXTURE_ERROR code=INPUT_INVALID")
        return 2

    valid_outcome, valid_findings = validate(base)
    if valid_outcome != "PASS":
        print(f"PLANNING_SCENARIO_MANIFEST_FIXTURE_ERROR code=VALID_BASE_REJECTED findings={','.join(valid_findings)}")
        return 2
    if validate(invalid) != ("FAIL", ["SCHEMA_INVALID"]):
        print("PLANNING_SCENARIO_MANIFEST_FIXTURE_ERROR code=SCHEMA_NEGATIVE_ACCEPTED")
        return 2

    for case in cases:
        outcome, findings = validate(mutate(base, case["mutations"]))
        if outcome != case["expected_outcome"] or findings != case["expected_findings"]:
            print(
                "PLANNING_SCENARIO_MANIFEST_FIXTURE_ERROR "
                f"code=POLARITY_MISMATCH case={case['case_id']} outcome={outcome} "
                f"findings={','.join(findings)}"
            )
            return 2

    print(f"PLANNING_SCENARIO_MANIFEST_FIXTURES_VALID valid=1 schema_invalid=1 semantic={len(cases)}")
    return 0


def validate_path(path: Path) -> tuple[str, list[str]]:
    try:
        return validate(load_json_file(path))
    except JsonInputError:
        return "ERROR", ["INPUT_INVALID"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return run_fixtures()
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    outcome, findings = validate_path(args.path)
    print(json.dumps({"findings": findings, "outcome": outcome}, sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "FAIL": 1, "ERROR": 2}[outcome]


if __name__ == "__main__":
    raise SystemExit(main())
