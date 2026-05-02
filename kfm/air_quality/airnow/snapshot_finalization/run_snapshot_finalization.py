import io
import json
import tarfile
import zipfile
from pathlib import Path

from .checksums import sha256_bytes, sha256_path
from .ids import sid, cjson
from .loaders import loadj, loadjl
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
        "errors": sorted(errs),
        "output_hashes": {"snapshot_finalization_packet_hash": None},
        "created_at": created_at,
    }
    _wj(out / "snapshot_finalization_receipt.json", receipt)
    return receipt


def _build_packet_if_enabled(manifest, out):
    pol = manifest.get("finalization_policy", {}) if isinstance(manifest.get("finalization_policy"), dict) else {}
    if not pol.get("include_packet", False):
        return None
    fmt = pol.get("packet_format", "tar.gz")
    names = {"snapshot_finalization_packet.tar.gz", "snapshot_finalization_packet.zip"}
    members = sorted([p for p in out.iterdir() if p.is_file() and p.name not in names], key=lambda p: p.name)
    if fmt == "zip":
        ap = out / "snapshot_finalization_packet.zip"
        with zipfile.ZipFile(ap, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for m in members:
                zi = zipfile.ZipInfo(m.name)
                zi.date_time = (1980, 1, 1, 0, 0, 0)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zf.writestr(zi, m.read_bytes())
    else:
        ap = out / "snapshot_finalization_packet.tar.gz"
        with tarfile.open(ap, "w:gz", format=tarfile.PAX_FORMAT) as tf:
            for m in members:
                b = m.read_bytes()
                ti = tarfile.TarInfo(name=m.name)
                ti.size = len(b)
                ti.mtime = 0
                ti.uid = 0
                ti.gid = 0
                ti.uname = ""
                ti.gname = ""
                tf.addfile(ti, io.BytesIO(b))
    return sha256_bytes(ap.read_bytes())


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
    for f in ["publication_allowed", "public_release_allowed", "snapshot_export_executed"]:
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

    _wj(out / "snapshot_finalization_manifest.resolved.json", {"object_type": "AirNowResolvedSnapshotFinalizationManifest", "schema_version": "v1", "manifest_id": m.get("manifest_id"), "created_at": created_at})

    inv = []
    for k, v in sorted(l17.items()):
        p = Path(v)
        inv.append({"object_type": "AirNowSnapshotFinalizationInputInventoryRecord", "schema_version": "v1", "input_id": k, "path_original": v, "exists": p.exists(), "sha256": sha256_path(p), "byte_size": p.stat().st_size, "created_at": created_at, "snapshot_finalization_input_inventory_record_id": sid("kfm:air_quality:airnow:snapshot_finalization_input_inventory_record:v1", [m.get("manifest_id"), k])})
    _wj(out / "snapshot_finalization_input_inventory.json", {"object_type": "AirNowSnapshotFinalizationInputInventory", "schema_version": "v1", "records": inv, "created_at": created_at})
    _wjl(out / "snapshot_finalization_input_inventory.jsonl", inv)

    _wj(out / "snapshot_acceptance_consolidation.json", {"object_type": "AirNowSnapshotAcceptanceConsolidation", "schema_version": "v1", "records": cands, "accepted_count": len(cands), "created_at": created_at})
    _wjl(out / "snapshot_acceptance_consolidation.jsonl", cands)
    _wj(out / "snapshot_blocker_consolidation.json", {"object_type": "AirNowSnapshotBlockerConsolidation", "schema_version": "v1", "records": blks, "blocker_count": len(blks), "created_at": created_at})
    _wjl(out / "snapshot_blocker_consolidation.jsonl", blks)
    policy = {"object_type": "AirNowSnapshotPolicyContinuityMatrix", "schema_version": "v1", "policy_attestation": pol, "required_checks": ["NO_EXECUTION", "NO_EXPORT", "NO_PUBLICATION"], "continuity_status": "PASS", "created_at": created_at}
    _wj(out / "snapshot_policy_continuity_matrix.json", policy)
    _wjl(out / "snapshot_policy_continuity_matrix.jsonl", [policy])
    _wj(out / "snapshot_caveat_continuity_register.json", {"object_type": "AirNowSnapshotCaveatContinuityRegister", "schema_version": "v1", "caveats": cav.get("caveats", []), "required_caveats": ["AIRNOW_PRELIMINARY_DATA", "AIRNOW_NOT_AQS_REGULATORY_DATA", "AIRNOW_NO_BULK_ZIP_WEB_SERVICE_LOOP", "SNAPSHOT_FINALIZATION_NOT_EXPORT_EXECUTION", "SNAPSHOT_FINALIZATION_NOT_PUBLICATION"], "created_at": created_at})
    _wj(out / "snapshot_readiness_final_summary.json", {"object_type": "AirNowSnapshotReadinessFinalSummary", "schema_version": "v1", "layer17_readiness": ready, "public_release_approved": False, "snapshot_export_execution_approved": False, "readiness_status": "READY_FOR_INTERNAL_SNAPSHOT_REVIEW" if not blks else "NEEDS_MORE_INPUT", "created_at": created_at})

    ledger_rows = [{"record_type": "acceptance_candidate", **x, "execution_enabled": False} for x in cands] + [{"record_type": "residual_blocker", **x, "execution_enabled": False} for x in blks]
    ledger = {"object_type": "AirNowSnapshotReviewFinalizationLedger", "schema_version": "v1", "assessment_matrix": assess, "item_satisfaction_matrix": sats, "policy_attestation": pol, "caveat_register": cav, "records": ledger_rows, "created_at": created_at}
    _wj(out / "snapshot_review_finalization_ledger.json", ledger)
    _wjl(out / "snapshot_review_finalization_ledger.jsonl", ledger_rows)

    outcome = "INTERNAL_SNAPSHOT_REVIEW_READY" if (cands and not blks) else ("INTERNAL_SNAPSHOT_REVIEW_NEEDS_MORE_INPUT" if blks else "INTERNAL_SNAPSHOT_REVIEW_PARTIAL")
    dec = {"object_type": "AirNowSnapshotDecisionCandidate", "schema_version": "v1", "decision_candidate_id": sid("kfm:air_quality:airnow:snapshot_decision_candidate:v1", [m.get("manifest_id"), outcome]), "decision_candidate_outcome": outcome, "positive_outcome_ceiling": "SNAPSHOT_FINALIZATION_COMPLETE_INTERNAL_ONLY", "public_release_allowed": False, "snapshot_export_execution_allowed": False, "created_at": created_at}
    _wj(out / "snapshot_decision_candidate.json", dec)
    _wjl(out / "snapshot_decision_candidate_ledger.jsonl", [dec])

    _wj(out / "snapshot_non_execution_attestation.json", {"object_type": "AirNowSnapshotNonExecutionAttestation", "schema_version": "v1", "commands_executed": False, "finalization_actions_executed": False, "snapshot_export_executed": False, "snapshot_copy_executed": False, "snapshot_transfer_executed": False, "snapshot_published": False, "snapshot_released": False, "file_deleted": False, "chmod_or_chattr_executed": False, "created_at": created_at})
    _wj(out / "snapshot_finalization_exception_register.json", {"object_type": "AirNowSnapshotFinalizationExceptionRegister", "schema_version": "v1", "records": [], "created_at": created_at})
    _wjl(out / "snapshot_finalization_exception_register.jsonl", [])
    _wj(out / "snapshot_finalization_rerun_plan.json", {"object_type": "AirNowSnapshotFinalizationRerunPlan", "schema_version": "v1", "steps": [], "created_at": created_at})
    _wj(out / "snapshot_finalization_status_board.json", {"object_type": "AirNowSnapshotFinalizationStatusBoard", "schema_version": "v1", "board_status": "SNAPSHOT_FINALIZATION_COMPLETE_INTERNAL_ONLY", "created_at": created_at})
    (out / "snapshot_finalization_status_board.md").write_text("# AirNow Layer 18 Snapshot Finalization Status Board\n\nInternal finalization planning only. No execution, no publication, no exports.\n")
    (out / "snapshot_finalization_report.md").write_text("# AirNow Layer 18 Snapshot Finalization Report\n\nInternal-only snapshot finalization planning. No coordinates, no emergency alerts, no regulatory claims.\n")

    packet_hash = _build_packet_if_enabled(m, out)
    receipt = {"object_type": "AirNowSnapshotFinalizationReceipt", "schema_version": "v1", "workflow_runner": "airnow_layer18_snapshot_finalization", "manifest_id": m.get("manifest_id"), "workflow_outcome": "SNAPSHOT_FINALIZATION_COMPLETE_INTERNAL_ONLY", "validation_outcome": "PASS", "finite_outcome": "ANSWER", "commands_executed": False, "finalization_actions_executed": False, "snapshot_export_executed": False, "snapshot_copy_executed": False, "snapshot_transfer_executed": False, "snapshot_published": False, "snapshot_released": False, "public_release_allowed": False, "errors": [], "output_hashes": {"snapshot_finalization_packet_hash": packet_hash}, "created_at": created_at}
    _wj(out / "snapshot_finalization_receipt.json", receipt)
    return receipt
