import hashlib, json, re
from pathlib import Path
from .constants import *
from .ids import sid
from .manifest import validate_manifest, validate_path_safe
from .loaders import loadj, loadjl, wj, wjl
from .checksums import sha256_path


def _deny(m, out, created_at, errs):
    r = {"object_type": "AirNowPreservationClosureFinalizationReceipt", "schema_version": "v1", "workflow_runner": "airnow_layer26_preservation_closure_finalization", "manifest_id": m.get("manifest_id"), "workflow_outcome": "PRESERVATION_CLOSURE_FINALIZATION_DENIED_REQUESTED_CAPABILITY", "validation_outcome": "FAIL", "finite_outcome": "DENY", "commands_executed": False, "finalization_actions_executed": False, "preservation_actions_executed": False, "preservation_copy_executed": False, "preservation_transfer_executed": False, "snapshot_export_executed": False, "snapshot_copy_executed": False, "snapshot_transfer_executed": False, "snapshot_published": False, "snapshot_released": False, "public_release_allowed": False, "errors": sorted(set(errs)), "output_hashes": {"preservation_closure_finalization_packet_hash": None}, "created_at": created_at}
    wj(out / 'preservation_closure_finalization_receipt.json', r)
    return r


def run_preservation_closure_finalization(manifest_path, out_dir, created_at):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True); m = loadj(manifest_path); errs = validate_manifest(m)
    inp = m.get('layer25_inputs', {})
    for k in L25_REQUIRED:
        p = inp.get(k)
        if not p: errs.append(f"MISSING_REQUIRED_INPUT:layer25_inputs.{k}"); continue
        if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:layer25_inputs.{k}")
        elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:layer25_inputs.{k}")
    if errs: return _deny(m, out, created_at, errs)
    r21 = loadj(inp['preservation_closure_review_receipt'])
    if r21.get('object_type') != 'AirNowPreservationClosureReviewReceipt': errs.append('INVALID_LAYER25_RECEIPT_OBJECT_TYPE')
    for f in L25_DENIED_TRUE_FIELDS:
        if r21.get(f) is True: errs.append(f"LAYER25_RECEIPT_DENIED_CAPABILITY_REQUIRED:{f}")
    ac = loadjl(inp['preservation_closure_acceptance_candidates']); bl = loadjl(inp['residual_preservation_closure_blockers'])
    val = loadj(inp['preservation_closure_review_validation_results']); pol = loadj(inp['preservation_closure_review_policy_attestation']); cav = loadj(inp['preservation_closure_review_caveat_register']); ready = loadj(inp['preservation_closure_review_readiness_summary'])
    for pth in [inp['preservation_closure_review_policy_attestation'], inp['preservation_closure_review_caveat_register']]:
        txt = Path(pth).read_text(errors='ignore').lower()
        if re.search(COORD_RE, txt): errs.append(f"COORDINATE_LEAK:{pth}")
        if any(t in txt for t in FORBIDDEN_TEXT_TERMS): errs.append(f"FORBIDDEN_LANGUAGE:{pth}")
    if errs: return _deny(m, out, created_at, errs)
    resolved = {"object_type": "AirNowPreservationClosureFinalizationResolvedManifest", "schema_version": "v1", "manifest_id": m.get('manifest_id'), "created_at": created_at}
    wj(out / 'preservation_closure_finalization_manifest.resolved.json', resolved)
    inv = []
    for k in sorted(L25_REQUIRED):
        p = Path(inp[k]); inv.append({"input_key": k, "path": inp[k], "sha256": sha256_path(p), "byte_size": p.stat().st_size})
    wj(out / 'preservation_closure_finalization_input_inventory.json', {"object_type": "AirNowPreservationClosureFinalizationInputInventory", "schema_version": "v1", "records": inv, "created_at": created_at}); wjl(out / 'preservation_closure_finalization_input_inventory.jsonl', inv)
    ledger = {"object_type": "AirNowPreservationClosureReviewFinalizationLedger", "schema_version": "v1", "ledger_id": sid('kfm:airnow:l26:ledger:v1', m.get('manifest_id', '')), "manifest_id": m.get('manifest_id'), "acceptance_count": len(ac), "blocker_count": len(bl), "validation_record_count": len(val.get('records', [])), "created_at": created_at}
    wj(out / 'preservation_closure_review_finalization_ledger.json', ledger); wjl(out / 'preservation_closure_review_finalization_ledger.jsonl', [ledger])
    outcome = 'INTERNAL_PRESERVATION_CLOSURE_REVIEW_READY' if not bl else 'INTERNAL_PRESERVATION_CLOSURE_REVIEW_PARTIAL'
    cand = {"object_type": "AirNowPreservationClosureDecisionCandidate", "schema_version": "v1", "candidate_id": sid('kfm:airnow:l26:candidate:v1', m.get('manifest_id', '')), "candidate_outcome": outcome, "outcome_ceiling": "PRESERVATION_CLOSURE_FINALIZATION_COMPLETE_INTERNAL_ONLY", "created_at": created_at}
    wj(out / 'preservation_closure_decision_candidate.json', cand); wjl(out / 'preservation_closure_decision_candidate_ledger.jsonl', [cand])
    wj(out / 'preservation_closure_acceptance_consolidation.json', {"object_type": "AirNowPreservationClosureAcceptanceConsolidation", "schema_version": "v1", "records": ac, "candidate_only": True, "created_at": created_at}); wjl(out / 'preservation_closure_acceptance_consolidation.jsonl', sorted(ac, key=lambda x: json.dumps(x, sort_keys=True)))
    wj(out / 'preservation_closure_blocker_consolidation.json', {"object_type": "AirNowPreservationClosureBlockerConsolidation", "schema_version": "v1", "records": bl, "residual_only": True, "created_at": created_at}); wjl(out / 'preservation_closure_blocker_consolidation.jsonl', sorted(bl, key=lambda x: json.dumps(x, sort_keys=True)))
    nonexec = {"object_type": "AirNowPreservationClosureNonExecutionAttestation", "schema_version": "v1", "commands_executed": False, "finalization_actions_executed": False, "preservation_actions_executed": False, "preservation_copy_executed": False, "preservation_transfer_executed": False, "snapshot_export_executed": False, "created_at": created_at}
    wj(out / 'preservation_closure_non_execution_attestation.json', nonexec)
    pcm = {"object_type": "AirNowPreservationClosurePolicyContinuityMatrix", "schema_version": "v1", "policy_status": "CONTINUED", "references": REFS, "created_at": created_at}
    wj(out / 'preservation_closure_policy_continuity_matrix.json', pcm); wjl(out / 'preservation_closure_policy_continuity_matrix.jsonl', [{"policy_status": "CONTINUED", "reference": r} for r in REFS])
    wj(out / 'preservation_closure_caveat_continuity_register.json', {"object_type": "AirNowPreservationClosureCaveatContinuityRegister", "schema_version": "v1", "caveats": cav.get('caveats', []), "created_at": created_at})
    wj(out / 'preservation_closure_readiness_final_summary.json', {"object_type": "AirNowPreservationClosureReadinessFinalSummary", "schema_version": "v1", "readiness_status": ready.get('readiness_status', 'UNKNOWN'), "candidate_outcome": outcome, "public_release_allowed": False, "preservation_execution_approved": False, "created_at": created_at})
    ex = {"object_type": "AirNowPreservationClosureFinalizationExceptionRegister", "schema_version": "v1", "records": [], "created_at": created_at}
    wj(out / 'preservation_closure_finalization_exception_register.json', ex); wjl(out / 'preservation_closure_finalization_exception_register.jsonl', [])
    wj(out / 'preservation_closure_finalization_rerun_plan.json', {"object_type": "AirNowPreservationClosureFinalizationRerunPlan", "schema_version": "v1", "rerun_required": False, "created_at": created_at})
    sb = {"object_type": "AirNowPreservationClosureFinalizationStatusBoard", "schema_version": "v1", "board_status": "PRESERVATION_CLOSURE_FINALIZATION_COMPLETE_INTERNAL_ONLY", "limitations": ["NOT_PUBLICATION", "NOT_EXECUTION", "NO_EXACT_COORDINATES"], "created_at": created_at}
    wj(out / 'preservation_closure_finalization_status_board.json', sb)
    (out / 'preservation_closure_finalization_status_board.md').write_text('# AirNow Layer 26 Preservation Closure Finalization Status Board\n\nInternal-only finalization planning complete; no preservation/copy/transfer/export/release execution; no exact coordinates.\n')
    (out / 'preservation_closure_finalization_report.md').write_text('# AirNow Layer 26 Preservation Closure Finalization Report\n\nFinal internal ledger compiled from Layer 25 artifacts; no public release, no publication, no execution actions.\n')
    packet_hash = None
    rec = {"object_type": "AirNowPreservationClosureFinalizationReceipt", "schema_version": "v1", "workflow_runner": "airnow_layer26_preservation_closure_finalization", "manifest_id": m.get("manifest_id"), "workflow_outcome": "PRESERVATION_CLOSURE_FINALIZATION_COMPLETE_INTERNAL_ONLY", "validation_outcome": "PASS", "finite_outcome": "ANSWER", "commands_executed": False, "finalization_actions_executed": False, "preservation_actions_executed": False, "preservation_copy_executed": False, "preservation_transfer_executed": False, "snapshot_export_executed": False, "snapshot_copy_executed": False, "snapshot_transfer_executed": False, "snapshot_published": False, "snapshot_released": False, "public_release_allowed": False, "errors": [], "output_hashes": {"preservation_closure_finalization_packet_hash": packet_hash}, "created_at": created_at}
    wj(out / 'preservation_closure_finalization_receipt.json', rec); return rec
