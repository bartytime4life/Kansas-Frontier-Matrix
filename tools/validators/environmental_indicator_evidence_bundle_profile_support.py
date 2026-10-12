"""Materialize compact synthetic fixture cases for the environmental profile.

This helper performs bounded local JSON loading and deterministic JSON-pointer
mutations only. It performs no network access and creates no evidence, policy,
review, lifecycle, release, or publication authority.
"""

from __future__ import annotations

import copy
import sys
from collections.abc import Mapping
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages" / "hashing" / "src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import JsonInputError, load_json_file

FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures"
    / "contracts"
    / "v1"
    / "evidence"
    / "environmental_indicator_evidence_bundle_profile"
    / "cases.json"
)


def _fixture_pointer_parts(path: object) -> tuple[str, ...] | None:
    if not isinstance(path, str) or not path.startswith("/") or path == "/":
        return None
    parts: list[str] = []
    for raw in path[1:].split("/"):
        part = raw.replace("~1", "/").replace("~0", "~")
        if not part:
            return None
        parts.append(part)
    return tuple(parts)


def _apply_fixture_mutations(
    base_document: Mapping[str, object],
    mutations: object,
) -> tuple[dict[str, object] | None, list[dict[str, str]]]:
    if not isinstance(mutations, list):
        return None, [{"code": "FIXTURE_MUTATIONS_INVALID", "path": "/mutations"}]
    document: dict[str, object] = copy.deepcopy(dict(base_document))
    findings: list[dict[str, str]] = []
    for index, mutation in enumerate(mutations):
        if not isinstance(mutation, Mapping):
            findings.append(
                {"code": "FIXTURE_MUTATION_INVALID", "path": f"/mutations/{index}"}
            )
            continue
        parts = _fixture_pointer_parts(mutation.get("path"))
        operation = mutation.get("op")
        if parts is None or operation not in {"set", "remove"}:
            findings.append(
                {
                    "code": "FIXTURE_MUTATION_INVALID",
                    "path": f"/mutations/{index}",
                }
            )
            continue
        parent: object = document
        valid_parent = True
        for part in parts[:-1]:
            if not isinstance(parent, dict) or part not in parent:
                valid_parent = False
                break
            parent = parent[part]
        if not valid_parent or not isinstance(parent, dict):
            findings.append(
                {
                    "code": "FIXTURE_MUTATION_PATH_INVALID",
                    "path": f"/mutations/{index}/path",
                }
            )
            continue
        leaf = parts[-1]
        if operation == "remove":
            if leaf not in parent:
                findings.append(
                    {
                        "code": "FIXTURE_MUTATION_PATH_INVALID",
                        "path": f"/mutations/{index}/path",
                    }
                )
            else:
                del parent[leaf]
        else:
            if "value" not in mutation:
                findings.append(
                    {
                        "code": "FIXTURE_MUTATION_VALUE_MISSING",
                        "path": f"/mutations/{index}/value",
                    }
                )
            else:
                parent[leaf] = copy.deepcopy(mutation["value"])
    return (document if not findings else None), findings


def load_fixture_cases() -> tuple[list[Mapping[str, object]], list[dict[str, str]]]:
    findings: list[dict[str, str]] = []
    try:
        candidate = load_json_file(FIXTURE_PATH)
    except JsonInputError:
        return [], [{"code": "FIXTURE_INPUT_ERROR", "path": "/"}]
    if not isinstance(candidate, Mapping):
        return [], [{"code": "FIXTURE_ROOT_INVALID", "path": "/"}]
    if candidate.get("execution_mode") != "FIXTURE_ONLY":
        findings.append(
            {"code": "FIXTURE_EXECUTION_MODE_INVALID", "path": "/execution_mode"}
        )
    base_document = candidate.get("base_document")
    if not isinstance(base_document, Mapping):
        return [], [{"code": "FIXTURE_BASE_INVALID", "path": "/base_document"}]
    cases = candidate.get("cases")
    if not isinstance(cases, list):
        return [], [{"code": "FIXTURE_CASES_INVALID", "path": "/cases"}]
    valid_cases: list[Mapping[str, object]] = []
    seen_ids: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, Mapping):
            findings.append(
                {"code": "FIXTURE_CASE_INVALID", "path": f"/cases/{index}"}
            )
            continue
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id or case_id in seen_ids:
            findings.append(
                {"code": "FIXTURE_CASE_ID_INVALID", "path": f"/cases/{index}/case_id"}
            )
            continue
        seen_ids.add(case_id)
        if case.get("expected_outcome") not in {"PASS", "DENY"}:
            findings.append(
                {
                    "code": "FIXTURE_EXPECTED_OUTCOME_INVALID",
                    "path": f"/cases/{index}/expected_outcome",
                }
            )
            continue
        if not isinstance(case.get("expected_findings"), list):
            findings.append(
                {
                    "code": "FIXTURE_EXPECTED_FINDINGS_INVALID",
                    "path": f"/cases/{index}/expected_findings",
                }
            )
            continue
        document, mutation_findings = _apply_fixture_mutations(
            base_document,
            case.get("mutations"),
        )
        if mutation_findings or document is None:
            findings.extend(
                {
                    "code": item["code"],
                    "path": f"/cases/{index}{item['path']}",
                }
                for item in mutation_findings
            )
            continue
        valid_cases.append(
            {
                "case_id": case_id,
                "document": document,
                "expected_outcome": case["expected_outcome"],
                "expected_findings": case["expected_findings"],
            }
        )
    return valid_cases, findings

