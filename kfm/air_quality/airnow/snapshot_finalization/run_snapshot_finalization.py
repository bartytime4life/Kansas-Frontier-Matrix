import json
from pathlib import Path
from .ids import sid, cjson
from .loaders import loadj, loadjl
from .checksums import sha256_path
from .manifest import validate_manifest, validate_path_safe


def _wj(p, o):
    Path(p).write_text(json.dumps(o, indent=2, sort_keys=True) + "\n")


def _wjl(p, rows):
    Path(p).write_text("".join(cjson(r) + "\n" for r in rows))


def _deny(m, out, created_at, errs):
    receipt = {
        "object_type": "AirNowSnapshotFinalizationReceipt",
        "schema_version": "v1",
        "workflow_runner": "airnow_layer18_snapshot_finalization",
        "manifest_id": m.get("manifest_id"),
        "workflow_outcome": "SNAPSHOT_FINALIZATION_DENIED_REQUESTED_CAPABILITY",
        "validation_outcome": "FAIL",
        "finite_outcome": "DENY",
        "commands_executed": False,
        "finalization_actions_executed": False,
        "snapshot_export_executed": False,
        "snapshot_copy_executed": False,
        "snapshot_transfer_executed": False,
        "snapshot_published": False,
        "snapshot_released": False,
        "public_release_allowed": False,
        "errors": errs,
        "created_at": created_at,
    }
    _wj(out / "snapshot_finalization_receipt.json", receipt)
    return receipt


def run_snapshot_finalization(manifest_path, out_dir, created_at):
    m = loadj(manifest_path)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    errs = validate_manifest(m)
    l17 = m.get("layer17_inputs", {})
    req = [
        "snapshot_review_receipt_json",
        "snapshot_acceptance_candidates_jsonl",
        "residual_snapshot_blockers_jsonl",
        "snapshot_review_assessment_matrix_json",
        "snapshot_item_satisfaction_matrix_json",
        "snapshot_review_policy_attestation_json",
        "snapshot_review_caveat_register_json",
        "snapshot_review_readiness_summary_json",
    ]
    for k in req:
        p = l17.get(k)
        if not p:
            errs.append(f"MISSING_REQUIRED_INPUT:{k}")
            continue
        if not validate_path_safe(p):
            errs.append(f"UNSAFE_PATH:{k}")
        elif not Path(p).exists():
            errs.append(f"MISSING_INPUT_FILE:{k}")
    if errs:
        return _deny(m, out, created_at, errs)

    rcp = loadj(l17["snapshot_review_receipt_json"])
    if rcp.get("object_type") != "AirNowSnapshotReviewReceipt":
        errs.append("INVALID_LAYER17_RECEIPT_OBJECT_TYPE")
    deny_fields = [
        "publication_allowed",
        "public_release_allowed",
        "snapshot_export_executed",
        "snapshot_copy_executed",
        "snapshot_transfer_executed",
        "snapshot_published",
        "snapshot_released",
        "archive_transfer_allowed",
        "file_deletion_allowed",
        "legal_hold_creation_allowed",
        "official_archive_certification_allowed",
        "commands_executed",
        "final_accession_execution_allowed",
        "task_closure_allowed",
    ]
    for f in deny_fields:
        if rcp.get(f) is True:
            errs.append(f"LAYER17_RECEIPT_FORBIDDEN:{f}")
    if errs:
        return _deny(m, out, created_at, errs)

    cands = sorted(loadjl(l17["snapshot_acceptance_candidates_jsonl"]), key=lambda x: x.get("candidate_id", ""))
    blks = sorted(loadjl(l17["residual_snapshot_blockers_jsonl"]), key=lambda x: x.get("blocker_id", ""))
    assess = loadj(l17["snapshot_review_assessment_matrix_json"])
    sats = loadj(l17["snapshot_item_satisfaction_matrix_json"])
    pol = loadj(l17["snapshot_review_policy_attestation_json"])
    cav = loadj(l17["snapshot_review_caveat_register_json"])
    ready = loadj(l17["snapshot_review_readiness_summary_json"])

    _wj(out / "snapshot_finalization_manifest.resolved.json", {
        "object_type": "AirNowResolvedSnapshotFinalizationManifest",
        "schema_version": "v1",
        "manifest_id": m.get("manifest_id"),
        "created_at": created_at,
        "authoritative_references": m.get("authoritative_references", []),
    })

    inv = []
    for k, v in sorted(l17.items()):
        p = Path(v)
        inv.append({
            "object_type": "AirNowSnapshotFinalizationInputInventoryRecord",
            "schema_version": "v1",
            "input_id": k,
            "path_original": v,
            "exists": p.exists(),
            "sha256": sha256_path(p),
            "byte_size": p.stat().st_size,
            "created_at": created_at,
            "snapshot_finalization_input_inventory_record_id": sid("kfm:air_quality:airnow:snapshot_finalization_input_inventory_record:v1", [m.get("manifest_id"), k]),
        })
    _wj(out / "snapshot_finalization_input_inventory.json", {"object_type": "AirNowSnapshotFinalizationInputInventory", "schema_version": "v1", "records": inv, "created_at": created_at})
    _wjl(out / "snapshot_finalization_input_inventory.jsonl", inv)

    _wj(out / "snapshot_acceptance_consolidation.json", {"object_type": "AirNowSnapshotAcceptanceConsolidation", "schema_version": "v1", "records": cands, "accepted_count": len(cands), "created_at": created_at})
    _wjl(out / "snapshot_acceptance_consolidation.jsonl", cands)
    _wj(out / "snapshot_blocker_consolidation.json", {"object_type": "AirNowSnapshotBlockerConsolidation", "schema_version": "v1", "records": blks, "blocker_count": len(blks), "created_at": created_at})
    _wjl(out / "snapshot_blocker_consolidation.jsonl", blks)
    policy = {"object_type": "AirNowSnapshotPolicyContinuityMatrix", "schema_version": "v1", "policy_attestation": pol, "continuity_status": "PASS", "created_at": created_at}
    _wj(out / "snapshot_policy_continuity_matrix.json", policy)
    _wjl(out / "snapshot_policy_continuity_matrix.jsonl", [policy])
    _wj(out / "snapshot_caveat_continuity_register.json", {"object_type": "AirNowSnapshotCaveatContinuityRegister", "schema_version": "v1", "caveats": cav.get("caveats", []), "created_at": created_at})
    _wj(out / "snapshot_readiness_final_summary.json", {"object_type": "AirNowSnapshotReadinessFinalSummary", "schema_version": "v1", "layer17_readiness": ready, "readiness_status": "READY_FOR_INTERNAL_SNAPSHOT_REVIEW" if not blks else "NEEDS_MORE_INPUT", "created_at": created_at})

    ledger = {"object_type": "AirNowSnapshotReviewFinalizationLedger", "schema_version": "v1", "assessment_matrix": assess, "item_satisfaction_matrix": sats, "policy_attestation": pol, "caveat_register": cav, "created_at": created_at}
    _wj(out / "snapshot_review_finalization_ledger.json", ledger)
    _wjl(out / "snapshot_review_finalization_ledger.jsonl", [ledger])

    outcome = "INTERNAL_SNAPSHOT_REVIEW_READY" if (cands and not blks) else ("INTERNAL_SNAPSHOT_REVIEW_NEEDS_MORE_INPUT" if blks else "INTERNAL_SNAPSHOT_REVIEW_PARTIAL")
    dec = {"object_type": "AirNowSnapshotDecisionCandidate", "schema_version": "v1", "decision_candidate_id": sid("kfm:air_quality:airnow:snapshot_decision_candidate:v1", [m.get("manifest_id"), outcome]), "decision_candidate_outcome": outcome, "positive_outcome_ceiling": "SNAPSHOT_FINALIZATION_COMPLETE_INTERNAL_ONLY", "created_at": created_at}
    _wj(out / "snapshot_decision_candidate.json", dec)
    _wjl(out / "snapshot_decision_candidate_ledger.jsonl", [dec])

    _wj(out / "snapshot_non_execution_attestation.json", {"object_type": "AirNowSnapshotNonExecutionAttestation", "schema_version": "v1", "commands_executed": False, "finalization_actions_executed": False, "snapshot_export_executed": False, "snapshot_copy_executed": False, "snapshot_transfer_executed": False, "snapshot_published": False, "snapshot_released": False, "created_at": created_at})
    _wj(out / "snapshot_finalization_exception_register.json", {"object_type": "AirNowSnapshotFinalizationExceptionRegister", "schema_version": "v1", "records": [], "created_at": created_at})
    _wjl(out / "snapshot_finalization_exception_register.jsonl", [])
    _wj(out / "snapshot_finalization_rerun_plan.json", {"object_type": "AirNowSnapshotFinalizationRerunPlan", "schema_version": "v1", "steps": [], "created_at": created_at})
    _wj(out / "snapshot_finalization_status_board.json", {"object_type": "AirNowSnapshotFinalizationStatusBoard", "schema_version": "v1", "board_status": "SNAPSHOT_FINALIZATION_COMPLETE_INTERNAL_ONLY", "created_at": created_at})
    (out / "snapshot_finalization_status_board.md").write_text("# AirNow Layer 18 Snapshot Finalization Status Board\n\nInternal finalization planning only.\n")
    (out / "snapshot_finalization_report.md").write_text("# AirNow Layer 18 Snapshot Finalization Report\n\nInternal-only snapshot finalization planning.\n")

    receipt = {"object_type": "AirNowSnapshotFinalizationReceipt", "schema_version": "v1", "workflow_runner": "airnow_layer18_snapshot_finalization", "manifest_id": m.get("manifest_id"), "workflow_outcome": "SNAPSHOT_FINALIZATION_COMPLETE_INTERNAL_ONLY", "validation_outcome": "PASS", "finite_outcome": "ANSWER", "commands_executed": False, "finalization_actions_executed": False, "snapshot_export_executed": False, "snapshot_copy_executed": False, "snapshot_transfer_executed": False, "snapshot_published": False, "snapshot_released": False, "public_release_allowed": False, "errors": [], "created_at": created_at}
    _wj(out / "snapshot_finalization_receipt.json", receipt)
    return receipt
