"""Finite semantic outcomes for VerificationBacklogItem records."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping

from ._verification_backlog_item_io import (
    Evaluation,
    Finding,
    DuplicateKeyError,
    NonFiniteNumberError,
    _evidence_key,
    _nested,
    _parse_time,
    _schema_findings,
    _sorted_unique,
    expected_item_id,
    expected_spec_hash,
    load_json,
)

ARRAY_PATHS = (
    ("scope", "responsibility_roots"),
    ("scope", "object_families"),
    ("scope", "domain_lanes"),
    (None, "research_modes"),
    (None, "basis_refs"),
    ("resolution", "conflicts"),
    ("resolution", "residual_unknowns"),
    ("constraints", "notes"),
    ("impact", "surfaces"),
    ("impact", "owner_roles"),
    ("acceptance", "evidence_refs"),
    ("acceptance", "validation_tests"),
)
CONSTRAINT_FIELDS = ("rights", "sensitivity", "sovereignty", "security", "public_use")
UNRESOLVED_CONSTRAINTS = frozenset({"UNKNOWN", "REVIEW_REQUIRED"})

def _semantic_errors(document: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []

    for parent, key in ARRAY_PATHS:
        value = _nested(document, parent, key)
        field = f"$.{key}" if parent is None else f"$.{parent}.{key}"
        if not _sorted_unique(value):
            findings.append(Finding("CANONICAL_ORDER_REQUIRED", field))

    evidence = document.get("resolution", {}).get("primary_evidence", []) if isinstance(document.get("resolution"), dict) else []
    if isinstance(evidence, list):
        if evidence != sorted(evidence, key=lambda item: _evidence_key(item) if isinstance(item, dict) else ("", "", "")):
            findings.append(Finding("CANONICAL_EVIDENCE_ORDER_REQUIRED", "$.resolution.primary_evidence"))
        keys: set[tuple[str, str, str]] = set()
        modes = set(document.get("research_modes", [])) if isinstance(document.get("research_modes"), list) else set()
        for index, item in enumerate(evidence):
            if not isinstance(item, dict):
                continue
            key = _evidence_key(item)
            if key in keys:
                findings.append(Finding("DUPLICATE_PRIMARY_EVIDENCE", f"$.resolution.primary_evidence[{index}]"))
            keys.add(key)
            if item.get("mode") not in modes:
                findings.append(Finding("EVIDENCE_MODE_NOT_DECLARED", f"$.resolution.primary_evidence[{index}].mode"))
            if not _sorted_unique(item.get("limitations")):
                findings.append(Finding("CANONICAL_ORDER_REQUIRED", f"$.resolution.primary_evidence[{index}].limitations"))

    created = _parse_time(document.get("created_at"))
    updated = _parse_time(document.get("updated_at"))
    if created is not None and updated is not None and created > updated:
        findings.append(Finding("TEMPORAL_ORDER_INVALID", "$.updated_at"))

    if document.get("item_id") != expected_item_id(document):
        findings.append(Finding("ITEM_ID_MISMATCH", "$.item_id"))
    if document.get("spec_hash") != expected_spec_hash(document):
        findings.append(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))

    resolution = document.get("resolution") if isinstance(document.get("resolution"), dict) else {}
    constraints = document.get("constraints") if isinstance(document.get("constraints"), dict) else {}
    acceptance = document.get("acceptance") if isinstance(document.get("acceptance"), dict) else {}
    lineage = document.get("lineage") if isinstance(document.get("lineage"), dict) else {}
    state = document.get("work_state")
    unresolved_constraints = [
        key for key in CONSTRAINT_FIELDS if constraints.get(key) in UNRESOLVED_CONSTRAINTS
    ]

    if state == "RESOLVED":
        if resolution.get("status") != "CONFIRMED":
            findings.append(Finding("RESOLVED_STATUS_MUST_BE_CONFIRMED", "$.resolution.status"))
        if not evidence:
            findings.append(Finding("RESOLVED_PRIMARY_EVIDENCE_REQUIRED", "$.resolution.primary_evidence"))
        if not acceptance.get("evidence_refs"):
            findings.append(Finding("RESOLVED_ACCEPTANCE_EVIDENCE_REQUIRED", "$.acceptance.evidence_refs"))
        if not acceptance.get("validation_tests"):
            findings.append(Finding("RESOLVED_VALIDATION_TEST_REQUIRED", "$.acceptance.validation_tests"))
        if resolution.get("residual_unknowns"):
            findings.append(Finding("RESOLVED_WITH_RESIDUAL_UNKNOWNS", "$.resolution.residual_unknowns"))
        if unresolved_constraints:
            findings.append(Finding("RESOLVED_WITH_UNCLEARED_CONSTRAINT", "$.constraints"))
        if lineage.get("superseded_by_item_id") is not None:
            findings.append(Finding("RESOLVED_CANNOT_BE_SUPERSEDED", "$.lineage.superseded_by_item_id"))

    if state == "SUPERSEDED":
        target = lineage.get("superseded_by_item_id")
        if target is None:
            findings.append(Finding("SUPERSESSION_TARGET_REQUIRED", "$.lineage.superseded_by_item_id"))
        elif target == document.get("item_id"):
            findings.append(Finding("SELF_SUPERSESSION_DENIED", "$.lineage.superseded_by_item_id"))
        if resolution.get("status") != "CONFIRMED":
            findings.append(Finding("SUPERSESSION_STATUS_MUST_BE_CONFIRMED", "$.resolution.status"))
        if not evidence:
            findings.append(Finding("SUPERSESSION_EVIDENCE_REQUIRED", "$.resolution.primary_evidence"))
    elif lineage.get("superseded_by_item_id") is not None:
        findings.append(Finding("SUPERSESSION_TARGET_NOT_ALLOWED", "$.lineage.superseded_by_item_id"))

    if lineage.get("supersedes_item_id") == document.get("item_id"):
        findings.append(Finding("SELF_SUPERSESSION_DENIED", "$.lineage.supersedes_item_id"))

    if state == "BLOCKED":
        blockers = bool(
            resolution.get("conflicts")
            or resolution.get("residual_unknowns")
            or unresolved_constraints
            or not evidence
        )
        if not blockers:
            findings.append(Finding("BLOCKED_WITHOUT_BLOCKER", "$.work_state"))

    return findings


def _hold_findings(document: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    state = document.get("work_state")
    resolution = document.get("resolution") if isinstance(document.get("resolution"), dict) else {}
    constraints = document.get("constraints") if isinstance(document.get("constraints"), dict) else {}
    acceptance = document.get("acceptance") if isinstance(document.get("acceptance"), dict) else {}

    if state in {"OPEN", "IN_PROGRESS", "BLOCKED"}:
        findings.append(Finding("ITEM_UNRESOLVED", "$.work_state"))
    if resolution.get("status") != "CONFIRMED":
        findings.append(Finding("RESOLUTION_NOT_CONFIRMED", "$.resolution.status"))
    if not resolution.get("primary_evidence"):
        findings.append(Finding("PRIMARY_EVIDENCE_REQUIRED", "$.resolution.primary_evidence"))
    if not acceptance.get("evidence_refs"):
        findings.append(Finding("ACCEPTANCE_EVIDENCE_REQUIRED", "$.acceptance.evidence_refs"))
    if not acceptance.get("validation_tests"):
        findings.append(Finding("VALIDATION_TEST_REQUIRED", "$.acceptance.validation_tests"))
    if resolution.get("residual_unknowns"):
        findings.append(Finding("RESIDUAL_UNKNOWNS_REMAIN", "$.resolution.residual_unknowns"))
    if any(constraints.get(key) in UNRESOLVED_CONSTRAINTS for key in CONSTRAINT_FIELDS):
        findings.append(Finding("CONSTRAINT_REVIEW_REQUIRED", "$.constraints"))
    return findings


def evaluate_document(document: Mapping[str, object]) -> Evaluation:
    schema_errors = tuple(sorted(set(_schema_findings(document))))
    if schema_errors:
        return Evaluation("ERROR", schema_errors)
    semantic_errors = tuple(sorted(set(_semantic_errors(document))))
    if semantic_errors:
        return Evaluation("ERROR", semantic_errors)
    holds = tuple(sorted(set(_hold_findings(document))))
    return Evaluation("HOLD" if holds else "READY", holds)


def evaluate_path(path: Path) -> tuple[dict[str, object] | None, Evaluation]:
    try:
        document = load_json(path)
        return document, evaluate_document(document)
    except (json.JSONDecodeError, DuplicateKeyError, NonFiniteNumberError):
        return None, Evaluation("ERROR", (Finding("INPUT_JSON_INVALID", "$"),))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return None, Evaluation("ERROR", (Finding("INPUT_INVALID", "$"),))
