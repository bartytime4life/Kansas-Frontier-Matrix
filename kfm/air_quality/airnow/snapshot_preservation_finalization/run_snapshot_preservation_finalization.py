import hashlib, json, re, tarfile
from pathlib import Path
from .constants import *
from .ids import sid
from .manifest import validate_manifest, validate_path_safe
from .loaders import loadj, loadjl, wj, wjl
from .checksums import sha256_path


def _deny(m, out, created_at, errs):
    r = {"object_type": "AirNowSnapshotPreservationFinalizationReceipt", "schema_version": "v1", "workflow_runner": "airnow_layer22_snapshot_preservation_finalization", "manifest_id": m.get("manifest_id"), "workflow_outcome": "SNAPSHOT_PRESERVATION_FINALIZATION_DENIED_REQUESTED_CAPABILITY", "validation_outcome": "FAIL", "finite_outcome": "DENY", "commands_executed": False, "finalization_actions_executed": False, "preservation_actions_executed": False, "preservation_copy_executed": False, "preservation_transfer_executed": False, "snapshot_export_executed": False, "snapshot_copy_executed": False, "snapshot_transfer_executed": False, "snapshot_published": False, "snapshot_released": False, "public_release_allowed": False, "errors": sorted(set(errs)), "output_hashes": {"snapshot_preservation_finalization_packet_hash": None}, "created_at": created_at}
    wj(out / 'snapshot_preservation_finalization_receipt.json', r)
    return r


def _packet(out: Path):
    packet = out / 'snapshot_preservation_finalization_packet.tar.gz'
    members = sorted([p for p in out.iterdir() if p.is_file() and p.name != packet.name])
    with tarfile.open(packet, 'w:gz', format=tarfile.PAX_FORMAT) as tf:
        for p in members:
            rel = p.name
            if rel.startswith('/') or '..' in Path(rel).parts:
                raise ValueError(f'INVALID_PACKET_MEMBER:{rel}')
            ti = tf.gettarinfo(str(p), arcname=rel)
            ti.mtime = 0
            ti.uid = ti.gid = 0
            ti.uname = ti.gname = 'root'
            with p.open('rb') as f:
                tf.addfile(ti, f)
    return packet


def run_snapshot_preservation_finalization(manifest_path, out_dir, created_at):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True); m = loadj(manifest_path); errs = validate_manifest(m)
    inp = m.get('layer21_inputs', {})
    for k in L21_REQUIRED:
        p = inp.get(k)
        if not p: errs.append(f"MISSING_REQUIRED_INPUT:layer21_inputs.{k}"); continue
        if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:layer21_inputs.{k}")
        elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:layer21_inputs.{k}")
    if errs: return _deny(m, out, created_at, errs)
    r21 = loadj(inp['snapshot_preservation_review_receipt'])
    if r21.get('object_type') != 'AirNowSnapshotPreservationReviewReceipt': errs.append('INVALID_LAYER21_RECEIPT_OBJECT_TYPE')
    for f in L21_DENIED_TRUE_FIELDS:
        if r21.get(f) is True: errs.append(f"LAYER21_RECEIPT_DENIED_CAPABILITY_REQUIRED:{f}")
    ac = loadjl(inp['snapshot_preservation_acceptance_candidates']); bl = loadjl(inp['residual_snapshot_preservation_blockers'])
    val = loadj(inp['snapshot_preservation_review_validation_results']); pol = loadj(inp['snapshot_preservation_review_policy_attestation']); cav = loadj(inp['snapshot_preservation_review_caveat_register']); ready = loadj(inp['snapshot_preservation_review_readiness_summary'])
    required_caveats = {"AIRNOW_PRELIMINARY_DATA", "AIRNOW_NOT_AQS_REGULATORY_DATA", "AIRNOW_NO_BULK_ZIP_WEB_SERVICE_LOOP", "SNAPSHOT_PRESERVATION_FINALIZATION_NOT_ACTION_EXECUTION", "SNAPSHOT_PRESERVATION_FINALIZATION_NOT_PUBLICATION"}
    if not required_caveats.issubset(set(cav.get('caveats', []))): errs.append('MISSING_REQUIRED_CAVEATS')
    for pth in [inp['snapshot_preservation_review_policy_attestation'], inp['snapshot_preservation_review_caveat_register']]:
        txt = Path(pth).read_text(errors='ignore').lower()
        if re.search(COORD_RE, txt): errs.append(f"COORDINATE_LEAK:{pth}")
        if any(t in txt for t in FORBIDDEN_TEXT_TERMS): errs.append(f"FORBIDDEN_LANGUAGE:{pth}")
    if errs: return _deny(m, out, created_at, errs)
    resolved = {"object_type": "AirNowSnapshotPreservationFinalizationResolvedManifest", "schema_version": "v1", "manifest_id": m.get('manifest_id'), "created_at": created_at}
    wj(out / 'snapshot_preservation_finalization_manifest.resolved.json', resolved)
    inv = []
    for k in sorted(L21_REQUIRED):
        p = Path(inp[k]); inv.append({"input_key": k, "path": inp[k], "sha256": sha256_path(p), "byte_size": p.stat().st_size})
    wj(out / 'snapshot_preservation_finalization_input_inventory.json', {"object_type": "AirNowSnapshotPreservationFinalizationInputInventory", "schema_version": "v1", "records": inv, "created_at": created_at}); wjl(out / 'snapshot_preservation_finalization_input_inventory.jsonl', inv)
    ledger = {"object_type": "AirNowSnapshotPreservationReviewFinalizationLedger", "schema_version": "v1", "ledger_id": sid('kfm:airnow:l22:ledger:v1', m.get('manifest_id', '')), "manifest_id": m.get('manifest_id'), "acceptance_count": len(ac), "blocker_count": len(bl), "validation_record_count": len(val.get('records', [])), "created_at": created_at}
    wj(out / 'snapshot_preservation_review_finalization_ledger.json', ledger); wjl(out / 'snapshot_preservation_review_finalization_ledger.jsonl', [ledger])
    outcome = 'INTERNAL_SNAPSHOT_PRESERVATION_REVIEW_READY' if not bl else 'INTERNAL_SNAPSHOT_PRESERVATION_REVIEW_PARTIAL'
    cand = {"object_type": "AirNowSnapshotPreservationDecisionCandidate", "schema_version": "v1", "candidate_id": sid('kfm:airnow:l22:candidate:v1', m.get('manifest_id', '')), "candidate_outcome": outcome, "outcome_ceiling": "SNAPSHOT_PRESERVATION_FINALIZATION_COMPLETE_INTERNAL_ONLY", "created_at": created_at}
    wj(out / 'snapshot_preservation_decision_candidate.json', cand); wjl(out / 'snapshot_preservation_decision_candidate_ledger.jsonl', [cand])
    wj(out / 'snapshot_preservation_acceptance_consolidation.json', {"object_type": "AirNowSnapshotPreservationAcceptanceConsolidation", "schema_version": "v1", "records": ac, "candidate_only": True, "created_at": created_at}); wjl(out / 'snapshot_preservation_acceptance_consolidation.jsonl', sorted(ac, key=lambda x: json.dumps(x, sort_keys=True)))
    wj(out / 'snapshot_preservation_blocker_consolidation.json', {"object_type": "AirNowSnapshotPreservationBlockerConsolidation", "schema_version": "v1", "records": bl, "residual_only": True, "created_at": created_at}); wjl(out / 'snapshot_preservation_blocker_consolidation.jsonl', sorted(bl, key=lambda x: json.dumps(x, sort_keys=True)))
    nonexec = {"object_type": "AirNowSnapshotPreservationNonExecutionAttestation", "schema_version": "v1", "commands_executed": False, "finalization_actions_executed": False, "preservation_actions_executed": False, "preservation_copy_executed": False, "preservation_transfer_executed": False, "snapshot_export_executed": False, "created_at": created_at}
    wj(out / 'snapshot_preservation_non_execution_attestation.json', nonexec)
    pcm = {"object_type": "AirNowSnapshotPreservationPolicyContinuityMatrix", "schema_version": "v1", "policy_status": "CONTINUED", "references": REFS, "created_at": created_at}
    wj(out / 'snapshot_preservation_policy_continuity_matrix.json', pcm); wjl(out / 'snapshot_preservation_policy_continuity_matrix.jsonl', [{"policy_status": "CONTINUED", "reference": r} for r in REFS])
    wj(out / 'snapshot_preservation_caveat_continuity_register.json', {"object_type": "AirNowSnapshotPreservationCaveatContinuityRegister", "schema_version": "v1", "caveats": cav.get('caveats', []), "created_at": created_at})
    wj(out / 'snapshot_preservation_readiness_final_summary.json', {"object_type": "AirNowSnapshotPreservationReadinessFinalSummary", "schema_version": "v1", "readiness_status": ready.get('readiness_status', 'UNKNOWN'), "candidate_outcome": outcome, "public_release_allowed": False, "preservation_execution_approved": False, "created_at": created_at})
    ex = {"object_type": "AirNowSnapshotPreservationFinalizationExceptionRegister", "schema_version": "v1", "records": [], "created_at": created_at}
    wj(out / 'snapshot_preservation_finalization_exception_register.json', ex); wjl(out / 'snapshot_preservation_finalization_exception_register.jsonl', [])
    wj(out / 'snapshot_preservation_finalization_rerun_plan.json', {"object_type": "AirNowSnapshotPreservationFinalizationRerunPlan", "schema_version": "v1", "rerun_required": False, "created_at": created_at})
    sb = {"object_type": "AirNowSnapshotPreservationFinalizationStatusBoard", "schema_version": "v1", "board_status": "SNAPSHOT_PRESERVATION_FINALIZATION_COMPLETE_INTERNAL_ONLY", "limitations": ["NOT_PUBLICATION", "NOT_EXECUTION", "NO_EXACT_COORDINATES"], "created_at": created_at}
    wj(out / 'snapshot_preservation_finalization_status_board.json', sb)
    (out / 'snapshot_preservation_finalization_status_board.md').write_text('# AirNow Layer 22 Snapshot Preservation Finalization Status Board\n\nInternal-only finalization planning complete; no preservation/copy/transfer/export/release execution; no exact coordinates.\n')
    (out / 'snapshot_preservation_finalization_report.md').write_text('# AirNow Layer 22 Snapshot Preservation Finalization Report\n\nFinal internal ledger compiled from Layer 21 artifacts; no public release, no publication, no execution actions.\n')
    packet_hash = None
    if m.get('finalization_policy', {}).get('include_packet') is True:
        packet_hash = sha256_path(_packet(out))
    rec = {"object_type": "AirNowSnapshotPreservationFinalizationReceipt", "schema_version": "v1", "workflow_runner": "airnow_layer22_snapshot_preservation_finalization", "manifest_id": m.get("manifest_id"), "workflow_outcome": "SNAPSHOT_PRESERVATION_FINALIZATION_COMPLETE_INTERNAL_ONLY", "validation_outcome": "PASS", "finite_outcome": "ANSWER", "commands_executed": False, "finalization_actions_executed": False, "preservation_actions_executed": False, "preservation_copy_executed": False, "preservation_transfer_executed": False, "snapshot_export_executed": False, "snapshot_copy_executed": False, "snapshot_transfer_executed": False, "snapshot_published": False, "snapshot_released": False, "public_release_allowed": False, "errors": [], "output_hashes": {"snapshot_preservation_finalization_packet_hash": packet_hash}, "created_at": created_at}
    wj(out / 'snapshot_preservation_finalization_receipt.json', rec); return rec
