"""Compact base-plus-mutation fixtures for VerificationBacklogItem."""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Mapping

from ._verification_backlog_item_io import REPO_ROOT, expected_item_id, expected_spec_hash, load_json
from ._verification_backlog_item_model import evaluate_document

FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/verification_backlog_item"
FIXTURE_BASE = FIXTURE_ROOT / "base.json"
FIXTURE_CASE_FILES = (
    FIXTURE_ROOT / "cases_ready_hold.json",
    FIXTURE_ROOT / "cases_error.json",
)

def _fixture_pointer_parts(value: object) -> list[str]:
    if not isinstance(value, str) or not value.startswith("/"):
        raise ValueError("fixture mutation path must be an absolute JSON pointer")
    if value == "/":
        return []
    return [part.replace("~1", "/").replace("~0", "~") for part in value[1:].split("/")]


def _apply_fixture_mutation(document: dict[str, object], mutation: Mapping[str, object]) -> None:
    parts = _fixture_pointer_parts(mutation.get("path"))
    if not parts:
        raise ValueError("fixture mutations may not replace the document root")
    target: object = document
    for part in parts[:-1]:
        if not isinstance(target, dict) or part not in target:
            raise ValueError("fixture mutation path does not resolve")
        target = target[part]
    if not isinstance(target, dict):
        raise ValueError("fixture mutation parent must be an object")
    leaf = parts[-1]
    operation = mutation.get("op")
    if operation == "set":
        if "value" not in mutation:
            raise ValueError("set mutation requires a value")
        target[leaf] = copy.deepcopy(mutation["value"])
    elif operation == "remove":
        if leaf not in target:
            raise ValueError("remove mutation path does not resolve")
        del target[leaf]
    else:
        raise ValueError("unsupported fixture mutation operation")


def load_fixture_cases() -> list[dict[str, object]]:
    base = load_json(FIXTURE_BASE)
    raw_cases: list[object] = []
    for path in FIXTURE_CASE_FILES:
        value = load_json(path).get("cases")
        if not isinstance(value, list):
            raise ValueError("fixture case manifest requires a cases array")
        raw_cases.extend(value)

    expanded: list[dict[str, object]] = []
    for case in raw_cases:
        if not isinstance(case, dict) or not isinstance(case.get("name"), str):
            raise ValueError("fixture case shape is invalid")
        document = copy.deepcopy(base)
        mutations = case.get("mutations", [])
        if not isinstance(mutations, list):
            raise ValueError("fixture mutations must be an array")
        for mutation in mutations:
            if not isinstance(mutation, dict):
                raise ValueError("fixture mutation must be an object")
            _apply_fixture_mutation(document, mutation)

        if case.get("recompute_identity", True) is True:
            document["item_id"] = expected_item_id(document)
        else:
            override = case.get("item_id_override")
            if not isinstance(override, str):
                raise ValueError("identity override is required")
            document["item_id"] = override

        if case.get("recompute_spec_hash", True) is True:
            document["spec_hash"] = expected_spec_hash(document)
        else:
            override = case.get("spec_hash_override")
            if not isinstance(override, str):
                raise ValueError("spec hash override is required")
            document["spec_hash"] = override

        expanded.append(
            {
                "name": case["name"],
                "document": document,
                "expected_outcome": case.get("expected_outcome"),
                "expected_findings": copy.deepcopy(case.get("expected_findings", [])),
            }
        )
    return expanded


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        cases = load_fixture_cases()
    except Exception:
        return False, {"authority": "NONE", "outcome": "ERROR", "cases": 0, "mismatches": ["FIXTURE_INPUT_INVALID"]}
    mismatches: list[dict[str, object]] = []
    for case in cases:
        document = case.get("document")
        if not isinstance(document, dict):
            mismatches.append({"case": case.get("name"), "expected": case.get("expected_outcome"), "actual": "ERROR"})
            continue
        evaluation = evaluate_document(document)
        expected_codes = sorted(case.get("expected_findings", [])) if isinstance(case.get("expected_findings"), list) else []
        actual_codes = sorted({finding.code for finding in evaluation.findings})
        if evaluation.outcome != case.get("expected_outcome") or actual_codes != expected_codes:
            mismatches.append(
                {
                    "case": case.get("name"),
                    "expected": {"outcome": case.get("expected_outcome"), "findings": expected_codes},
                    "actual": {"outcome": evaluation.outcome, "findings": actual_codes},
                }
            )
    return not mismatches, {
        "authority": "NONE",
        "outcome": "PASS" if not mismatches else "FAIL",
        "cases": len(cases),
        "mismatches": mismatches,
    }
