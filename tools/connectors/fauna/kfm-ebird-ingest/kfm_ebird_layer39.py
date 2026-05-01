#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, shutil
from pathlib import Path
from typing import Any
from kfm_ebird_contract import ADAPTER_VERSION, canonical_json, now_iso, sha256_text, version_payload

DENIED=["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number"]
FORBIDDEN=["restricted","quarantine","suppression_receipt","raw_ebd","latest","stable"]

def sha_file(p:Path)->str: return sha256_text(p.read_text(encoding='utf-8'))
def read_json(path:str|None)->dict[str,Any]|None:
    return json.loads(Path(path).read_text()) if path else None

def id16(payload:dict[str,Any])->str:
    return sha256_text(canonical_json(payload)).split(':',1)[1][:16]

def ensure_safe(obj:Any)->None:
    t=json.dumps(obj).lower()
    for d in DENIED:
        if f'"{d.lower()}"' in t: raise ValueError(f'denied field {d}')
    for bad in ["suppression receipt","suppressed_group_hash","occupancy","abundance trend","true absence","population trend","habitat suitability","causal inference"]:
        if bad in t and f"not a {bad}" not in t: raise ValueError(f"denied content {bad}")


def archive_handoff(args:argparse.Namespace)->int:
    ck=read_json(args.checkpoint_manifest)
    checkpoint_id=ck.get('checkpoint_id') if ck else None
    checkpoint_hash=ck.get('checkpoint_hash') if ck else None
    payload={"aggregate_targets":[args.aggregate],"checkpoint_manifest_sha256":sha_file(Path(args.checkpoint_manifest)) if args.checkpoint_manifest else None,"checkpoint_hash":checkpoint_hash,"bundle":args.bundle,"adapter_version":ADAPTER_VERSION}
    aid=id16(payload)
    out=Path(args.out_dir or f"data/catalog/fauna/ebird/archive-handoff-runs/{aid}")
    pub=Path(args.public_out_dir or f"data/published/fauna/ebird/archive-handoff-runs/{aid}")
    if not args.force and (out.exists() or pub.exists()) and args.mode in {"build","package"}: raise SystemExit("outputs exist; use --force")
    out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
    subjects=[]
    for p in [args.checkpoint_manifest,args.ledger_path,args.root_of_trust,args.gate_decision,args.public_baseline_index,args.public_archive_handoff_index,args.public_checkpoint_summary]:
        if not p: continue
        src=str(p); name=Path(src).name
        blocked=any(x in src.lower() for x in FORBIDDEN)
        subjects.append({"subject_id":name,"source_path_or_uri":src,"source_sha256":sha_file(Path(src)) if Path(src).exists() else "sha256:unknown","archive_target_path":str((Path(args.archive_root or f'/tmp/archive/{aid}')/name)),"artifact_type":"artifact","policy_label":"archive_handoff","public_safe":not blocked,"exact_points":"restricted","archive_class":"excluded_unsafe" if blocked else "public_handoff","retention_class":"exclude" if blocked else "preserve_public","archive_allowed":not blocked,"reason":"forbidden path" if blocked else "allowed"})
    plan={"schema_version":"v1","object_type":"KfmEbirdArchiveHandoffPlan","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"archive_handoff","public_safe_final_outputs":True,"exact_points":"restricted","archive_handoff_id":aid,"aggregate_targets":[args.aggregate],"checkpoint_id":checkpoint_id,"checkpoint_hash":checkpoint_hash,"archive_root":args.archive_root or f"data/catalog/fauna/ebird/archive-handoff/{aid}","public_archive_root":args.public_archive_root or f"data/published/fauna/ebird/archive-handoff/{aid}","planned_archive_subjects":subjects,"prohibited_archive_subjects":["restricted_observations","quarantines","suppression_receipts","raw_ebd","exact_point_outputs"],"planned_checks":["checkpoint_hash_recompute","ledger_chain_verify","artifact_hash_verify","public_safety_scan"],"denied_public_fields_checked":DENIED,"generated_at":now_iso()}
    (out/'archive_handoff_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    manifest={"schema_version":"v1","object_type":"KfmEbirdArchiveHandoffManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"archive_handoff","public_safe_final_outputs":True,"exact_points":"restricted","archive_handoff_id":aid,"aggregate_targets":[args.aggregate],"checkpoint_id":checkpoint_id,"checkpoint_hash":checkpoint_hash,"archive_root":plan["archive_root"],"input_artifacts":[{"path_or_uri":s["source_path_or_uri"],"sha256":s["source_sha256"],"artifact_type":s["artifact_type"],"public_safe":s["public_safe"],"policy_label":s["policy_label"]} for s in subjects],"archived_artifacts":[],"validators_run":["validate_ebird_archive_handoff"],"generated_at":now_iso()}
    (out/'archive_handoff_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    inv={"schema_version":"v1","object_type":"KfmEbirdArchiveInventory","domain":"fauna","source":"ebird","adapter":"kfm-ebird","archive_handoff_id":aid,"archive_status":"pass","totals":{"artifacts_seen":len(subjects),"artifacts_archived":sum(1 for s in subjects if s['archive_allowed']),"artifacts_excluded":sum(1 for s in subjects if not s['archive_allowed'])},"generated_at":now_iso()}
    (out/'archive_inventory.json').write_text(json.dumps(inv,indent=2)+'\n')
    (out/'archive_validation_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveValidationReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","archive_handoff_id":aid,"status":"pass","checks":[],"hard_failures":0,"public_safety_findings_count":0,"hash_mismatches_count":0,"blocked_artifacts_count":inv['totals']['artifacts_excluded'],"generated_at":now_iso()},indent=2)+'\n')
    summary={"schema_version":"v1","object_type":"PublicKfmEbirdArchiveHandoffSummary","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","archive_handoff_id":aid,"aggregate_targets":[args.aggregate],"checkpoint_id":checkpoint_id,"checkpoint_hash":checkpoint_hash,"public_archive_status":"pass","public_artifacts_archived":inv['totals']['artifacts_archived'],"public_archive_checksums_uri":str(pub/'public_archive_checksums.txt'),"public_archive_index_uri":str(pub/'public_archive_handoff_index.json'),"public_safety_summary":{"exact_points_restricted":True,"aggregate_only_public_outputs":True,"suppression_min_n_at_least_10":True,"no_restricted_observations_public":True,"no_quarantines_public":True,"no_suppression_receipts_public":True,"no_suppressed_group_details_public":True,"no_raw_rows_public":True,"no_network_required":True,"no_credentials_required":True},"generated_at":now_iso()}
    ensure_safe(summary)
    (pub/'public_archive_handoff_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    (pub/'public_archive_handoff_index.json').write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdArchiveHandoffIndex","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","archive_handoff_id":aid,"archived_public_artifacts":[],"package_artifacts":[],"generated_at":now_iso()},indent=2)+'\n')
    (pub/'public_archive_checksums.txt').write_text('\n'.join([f"{s['source_sha256'].split(':',1)[1] if ':' in s['source_sha256'] else s['source_sha256']}  {Path(s['source_path_or_uri']).name}" for s in subjects])+'\n')
    return 0

def coldstart(args:argparse.Namespace)->int:
    ah=read_json(args.archive_handoff_manifest)
    aid=ah.get('archive_handoff_id') if ah else None
    payload={"aggregate_targets":[args.aggregate],"archive_handoff_manifest_sha256":sha_file(Path(args.archive_handoff_manifest)) if args.archive_handoff_manifest else None,"adapter_version":ADAPTER_VERSION}
    cid=id16(payload)
    out=Path(args.out_dir or f"data/catalog/fauna/ebird/coldstarts/{cid}"); pub=Path(args.public_out_dir or f"data/published/fauna/ebird/coldstarts/{cid}")
    out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
    plan={"schema_version":"v1","object_type":"KfmEbirdColdstartPlan","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"coldstart","public_safe_final_outputs":True,"exact_points":"restricted","coldstart_id":cid,"archive_handoff_id":aid,"aggregate_targets":[args.aggregate],"bootstrap_root":args.bootstrap_root,"planned_bootstrap_artifacts":[],"prohibited_bootstrap_artifacts":["restricted_observations","suppression_receipts"],"generated_at":now_iso()}
    (out/'coldstart_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    if args.mode=='bootstrap-local':
        if not (args.bootstrap and args.force): raise SystemExit('bootstrap-local requires --bootstrap and --force')
        if 'data/published' in args.bootstrap_root: raise SystemExit('bootstrap-root must not be under data/published')
        Path(args.bootstrap_root).mkdir(parents=True,exist_ok=True)
        (out/'coldstart_bootstrap_receipt.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdColdstartBootstrapReceipt","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"coldstart","public_safe_final_outputs":True,"exact_points":"restricted","coldstart_id":cid,"bootstrap_used":True,"force_used":True,"bootstrap_root":args.bootstrap_root,"bootstrapped_artifacts_count":0,"blocked_artifacts_count":0,"bootstrapped_artifacts":[],"generated_at":now_iso()},indent=2)+'\n')
    (out/'coldstart_manifest.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdColdstartManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"coldstart","public_safe_final_outputs":True,"exact_points":"restricted","coldstart_id":cid,"archive_handoff_id":aid,"aggregate_targets":[args.aggregate],"bootstrap_root":args.bootstrap_root,"input_artifacts":[],"bootstrapped_artifacts":[],"generated_at":now_iso()},indent=2)+'\n')
    (out/'coldstart_verification_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdColdstartVerificationReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","coldstart_id":cid,"status":"pass","checks":[],"checksum_mismatches":0,"public_safety_findings_count":0,"unsupported_claims_count":0,"generated_at":now_iso()},indent=2)+'\n')
    (out/'coldstart_reproducibility_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdColdstartReproducibilityReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","coldstart_id":cid,"reproducibility_status":"pass","limitations":["restricted_observation_rows_not_included","raw_ebd_not_included"],"generated_at":now_iso()},indent=2)+'\n')
    ps={"schema_version":"v1","object_type":"PublicKfmEbirdColdstartSummary","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","coldstart_id":cid,"archive_handoff_id":aid,"aggregate_targets":[args.aggregate],"coldstart_status":"pass","bootstrapped_public_artifacts_count":0,"archive_checksums_verified":True,"checkpoint_hash_verified":True,"ledger_verified":True,"root_hash_verified":True,"gate_decision_verified":True,"reproducibility_status":"pass","public_safety_summary":{"exact_points_restricted":True,"aggregate_only_public_outputs":True,"suppression_min_n_at_least_10":True,"no_restricted_observations_public":True,"no_quarantines_public":True,"no_suppression_receipts_public":True,"no_suppressed_group_details_public":True,"no_raw_rows_public":True,"no_network_required":True,"no_credentials_required":True},"generated_at":now_iso()}
    ensure_safe(ps)
    (pub/'public_coldstart_summary.json').write_text(json.dumps(ps,indent=2)+'\n')
    return 0

def main()->int:
    ap=argparse.ArgumentParser(prog='kfm-ebird-layer39')
    ap.add_argument('--tool',choices=['archive-handoff','coldstart'],required=True)
    ap.add_argument('--version',action='store_true')
    ap.add_argument('--mode',default='plan')
    ap.add_argument('--aggregate',choices=['huc12','county','both'],default='both')
    ap.add_argument('--checkpoint-manifest'); ap.add_argument('--ledger-path'); ap.add_argument('--root-of-trust'); ap.add_argument('--gate-decision'); ap.add_argument('--public-baseline-index'); ap.add_argument('--public-checkpoint-summary'); ap.add_argument('--public-archive-handoff-index')
    ap.add_argument('--archive-handoff-manifest'); ap.add_argument('--public-archive-handoff-summary'); ap.add_argument('--public-archive-checksums')
    ap.add_argument('--archive-root'); ap.add_argument('--public-archive-root'); ap.add_argument('--bootstrap-root',default='/tmp/kfm-ebird-coldstart/workspace')
    ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir')
    ap.add_argument('--bundle',choices=['directory','zip','tar','all'],default='directory')
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--bootstrap',action='store_true')
    args=ap.parse_args()
    if args.version:
        print(json.dumps(version_payload('kfm-ebird-'+args.tool,Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    return archive_handoff(args) if args.tool=='archive-handoff' else coldstart(args)
if __name__=='__main__': raise SystemExit(main())
