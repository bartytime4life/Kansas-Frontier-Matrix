"""Semantic checks for the inactive ProgramOutcomeChain profile."""
from __future__ import annotations

from typing import Any, Mapping

from program_outcome_chain_model import (
    ALLOWED_STAGE_STATUSES,
    ERROR_CODES,
    EXPECTED_CLAIM_CODES,
    FALSE_EFFECTS,
    REPEATABLE_STAGE_TYPES,
    REQUIRED_PREDECESSOR_TYPES,
    STAGE_ORDER,
    Finding,
    aware_datetime,
    canonical_spec_hash,
    canonical_string_array,
    expected_chain_id,
)


def semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    for key in ("source_snapshot_refs", "evidence_refs", "limitations"):
        if not canonical_string_array(candidate.get(key)):
            findings.append(
                Finding("NONCANONICAL_REFERENCE_ARRAY", f"/{key}")
            )

    lineage = (
        candidate.get("lineage")
        if isinstance(candidate.get("lineage"), Mapping)
        else {}
    )
    for key in ("corrects", "superseded_by", "conflict_refs"):
        if not canonical_string_array(lineage.get(key)):
            findings.append(
                Finding(
                    "NONCANONICAL_REFERENCE_ARRAY",
                    f"/lineage/{key}",
                )
            )

    stages = (
        candidate.get("stages")
        if isinstance(candidate.get("stages"), list)
        else []
    )
    seen_ids: set[str] = set()
    seen_types: dict[str, list[str]] = {}
    prior_ids: set[str] = set()
    last_rank = -1
    last_time = None

    for index, raw_stage in enumerate(stages):
        base = f"/stages/{index}"
        if not isinstance(raw_stage, Mapping):
            continue
        stage = raw_stage
        stage_id = stage.get("stage_id")
        stage_type = stage.get("stage_type")
        stage_status = stage.get("stage_status")
        depends_on = stage.get("depends_on")
        evidence_refs = stage.get("evidence_refs")

        if isinstance(stage_id, str):
            if stage_id in seen_ids:
                findings.append(
                    Finding("DUPLICATE_STAGE_ID", base + "/stage_id")
                )
            seen_ids.add(stage_id)

        if not canonical_string_array(depends_on):
            findings.append(
                Finding(
                    "NONCANONICAL_REFERENCE_ARRAY",
                    base + "/depends_on",
                )
            )
        if not canonical_string_array(evidence_refs):
            findings.append(
                Finding(
                    "NONCANONICAL_REFERENCE_ARRAY",
                    base + "/evidence_refs",
                )
            )

        if isinstance(stage_type, str) and stage_type in STAGE_ORDER:
            rank = STAGE_ORDER[stage_type]
            if rank < last_rank:
                findings.append(
                    Finding(
                        "STAGE_ORDER_INVALID",
                        base + "/stage_type",
                    )
                )
            last_rank = max(last_rank, rank)

            prior_same_type = seen_types.get(stage_type, [])
            if (
                prior_same_type
                and stage_type not in REPEATABLE_STAGE_TYPES
            ):
                findings.append(
                    Finding(
                        "NONREPEATABLE_STAGE_DUPLICATE",
                        base + "/stage_type",
                    )
                )

            if stage_status not in ALLOWED_STAGE_STATUSES[stage_type]:
                findings.append(
                    Finding(
                        "STAGE_STATUS_INVALID",
                        base + "/stage_status",
                    )
                )

            if (
                stage.get("public_claim_code")
                != EXPECTED_CLAIM_CODES[stage_type]
            ):
                findings.append(
                    Finding(
                        "PUBLIC_CLAIM_CODE_MISMATCH",
                        base + "/public_claim_code",
                    )
                )

            dependencies = (
                depends_on if isinstance(depends_on, list) else []
            )
            if any(ref not in prior_ids for ref in dependencies):
                findings.append(
                    Finding(
                        "DEPENDENCY_REFERENCE_INVALID",
                        base + "/depends_on",
                    )
                )

            for required_type in REQUIRED_PREDECESSOR_TYPES[stage_type]:
                prior_required = seen_types.get(required_type, [])
                path = (
                    base
                    + "/depends_on/"
                    + required_type.lower()
                )
                if not prior_required:
                    findings.append(
                        Finding("REQUIRED_PREDECESSOR_MISSING", path)
                    )
                elif prior_required[-1] not in dependencies:
                    findings.append(
                        Finding(
                            "REQUIRED_PREDECESSOR_REFERENCE_MISSING",
                            path,
                        )
                    )

            amount = stage.get("amount")
            if stage_type in {"AWARD", "PAYMENT"}:
                if not isinstance(amount, Mapping):
                    findings.append(
                        Finding("AMOUNT_REQUIRED", base + "/amount")
                    )
            elif amount is not None:
                findings.append(
                    Finding(
                        "AMOUNT_STAGE_MISMATCH",
                        base + "/amount",
                    )
                )

            geometry_ref = stage.get("geometry_ref")
            if stage_type in {
                "ELIGIBILITY_AREA",
                "PROJECT_FOOTPRINT",
            }:
                if not isinstance(geometry_ref, str):
                    findings.append(
                        Finding(
                            "GEOMETRY_REFERENCE_REQUIRED",
                            base + "/geometry_ref",
                        )
                    )
            elif geometry_ref is not None:
                findings.append(
                    Finding(
                        "GEOMETRY_STAGE_MISMATCH",
                        base + "/geometry_ref",
                    )
                )

            method_ref = stage.get("method_ref")
            uncertainty_ref = stage.get("uncertainty_ref")
            if stage_type in {
                "OUTCOME_OBSERVATION",
                "EVALUATION",
            }:
                if not isinstance(method_ref, str):
                    findings.append(
                        Finding(
                            "METHOD_REFERENCE_REQUIRED",
                            base + "/method_ref",
                        )
                    )
            elif method_ref is not None:
                findings.append(
                    Finding(
                        "METHOD_STAGE_MISMATCH",
                        base + "/method_ref",
                    )
                )

            if stage_type == "EVALUATION":
                if not isinstance(uncertainty_ref, str):
                    findings.append(
                        Finding(
                            "UNCERTAINTY_REFERENCE_REQUIRED",
                            base + "/uncertainty_ref",
                        )
                    )
            elif uncertainty_ref is not None:
                findings.append(
                    Finding(
                        "UNCERTAINTY_STAGE_MISMATCH",
                        base + "/uncertainty_ref",
                    )
                )

            if isinstance(stage_id, str):
                seen_types.setdefault(stage_type, []).append(stage_id)

        recorded_at = aware_datetime(stage.get("recorded_at"))
        if (
            recorded_at is not None
            and last_time is not None
            and recorded_at < last_time
        ):
            findings.append(
                Finding(
                    "STAGE_TIME_ORDER_INVALID",
                    base + "/recorded_at",
                )
            )
        if recorded_at is not None:
            last_time = recorded_at

        if isinstance(stage_id, str):
            prior_ids.add(stage_id)

    state = lineage.get("state")
    corrects = lineage.get("corrects", [])
    superseded_by = lineage.get("superseded_by", [])
    conflicts = lineage.get("conflict_refs", [])
    if state == "CURRENT" and (
        corrects or superseded_by or conflicts
    ):
        findings.append(
            Finding("CURRENT_LINEAGE_CONFLICT", "/lineage")
        )
    elif state == "CORRECTED" and not corrects:
        findings.append(
            Finding("CORRECTION_LINEAGE_INCOMPLETE", "/lineage")
        )
    elif state == "SUPERSEDED" and not superseded_by:
        findings.append(
            Finding("SUPERSESSION_LINEAGE_INCOMPLETE", "/lineage")
        )
    elif state == "CONFLICTED" and len(conflicts) < 2:
        findings.append(
            Finding("CONFLICT_LINEAGE_INCOMPLETE", "/lineage")
        )

    if (
        candidate.get("release_state") != "UNRELEASED"
        or candidate.get("release_ref") is not None
    ):
        findings.append(
            Finding("RELEASE_OVERCLAIM", "/release_state")
        )
    if candidate.get("public_use_allowed") is not False:
        findings.append(
            Finding("PUBLIC_USE_OVERCLAIM", "/public_use_allowed")
        )
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append(
            Finding("EFFECT_OVERCLAIM", "/effects")
        )

    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_chain_id(candidate)
    except RuntimeError:
        findings.append(
            Finding("HASHING_UNAVAILABLE", "/spec_hash")
        )
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(
                Finding("SPEC_HASH_MISMATCH", "/spec_hash")
            )
        if candidate.get("program_outcome_chain_id") != expected_id:
            findings.append(
                Finding(
                    "PROGRAM_OUTCOME_CHAIN_ID_MISMATCH",
                    "/program_outcome_chain_id",
                )
            )
    return findings


def outcome_for(findings: list[Finding]) -> str:
    if not findings:
        return "PASS"
    return (
        "ERROR"
        if any(finding.code in ERROR_CODES for finding in findings)
        else "DENY"
    )
