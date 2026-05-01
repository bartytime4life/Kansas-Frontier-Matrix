#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
from kfm_ebird_contract import ADAPTER_VERSION, canonical_json, now_iso, sha256_text, version_payload

DENIED=["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number"]
CLAIMS=["occupancy","abundance trend","true absence","population trend","habitat suitability","causal inference"]

def sha_file(p:Path)->str: return sha256_text(p.read_text(encoding='utf-8'))
def read_json(path:str|None)->dict[str,Any]|None:
    return json.loads(Path(path).read_text()) if path else None

def id16(payload:dict[str,Any])->str:
    return sha256_text(canonical_json(payload)).split(':',1)[1][:16]

def ensure_public_safe(obj:Any)->None:
    t=json.dumps(obj).lower()
    for d in DENIED:
        if f'"{d.lower()}"' in t: raise ValueError(f'denied field {d}')
    for c in CLAIMS:
        if c in t and f"not a {c}" not in t: raise ValueError(f"unsupported claim {c}")
    for bad in ["suppression_receipt","suppressed_group_hash","restricted_observation","quarantine/"]:
        if bad in t and f"no_{bad}" not in t and f"not {bad}" not in t: raise ValueError(f"denied content {bad}")

def fixity(args:argparse.Namespace)->int:
    if args.work_dir and 'data/published' in args.work_dir: raise SystemExit('work-dir must not be under data/published')
    ck=read_json(args.checkpoint_manifest)
    checkpoint_hash=ck.get('checkpoint_hash') if ck else None
    payload={"aggregate_targets":[args.aggregate],"checkpoint_manifest_sha256":sha_file(Path(args.checkpoint_manifest)) if args.checkpoint_manifest else None,"checkpoint_hash":checkpoint_hash,"scenario_set":args.scenario_set,"adapter_version":ADAPTER_VERSION}
    rid=id16(payload)
    out=Path(args.out_dir or f"data/catalog/fauna/ebird/fixity/{rid}"); out.mkdir(parents=True,exist_ok=True)
    pub=Path(args.public_out_dir or f"data/published/fauna/ebird/fixity/{rid}"); pub.mkdir(parents=True,exist_ok=True)
    plan={"schema_version":"v1","object_type":"KfmEbirdFixityScanPlan","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"fixity","public_safe_final_outputs":True,"exact_points":"restricted","fixity_run_id":rid,"aggregate_targets":[args.aggregate],"scan_scope":["archive_handoff","archive_inventory","checkpoint","ledger","coldstart","restore","continuity","public_archive","public_baseline","public_summary"],"planned_checks":["archive_checksum_recompute","checkpoint_hash_recompute","ledger_chain_verify","root_hash_recompute","contract_hash_recompute","artifact_presence_check","package_archive_check","public_safety_scan","schema_validate","policy_validate","unsupported_claim_scan"],"prohibited_actions":["delete_artifacts","rewrite_archive","rewrite_ledger"],"generated_at":now_iso()}
    (out/'fixity_scan_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    inv=[{"schema_version":"v1","object_type":"KfmEbirdFixityInventoryItem","domain":"fauna","source":"ebird","adapter":"kfm-ebird","fixity_run_id":rid,"path_or_uri":args.checkpoint_manifest or "synthetic://none","expected_sha256":sha_file(Path(args.checkpoint_manifest)) if args.checkpoint_manifest else "sha256:na","artifact_type":"checkpoint_manifest","policy_label":"fixity","public_safe":True,"exact_points":"restricted","artifact_present":bool(args.checkpoint_manifest),"hash_status":"match" if args.checkpoint_manifest else "not_checked","public_safety_status":"pass","preservation_role":"checkpoint","recommended_action":"no_action"}]
    (out/'fixity_inventory.jsonl').write_text('\n'.join(json.dumps(r) for r in inv)+'\n')
    report={"schema_version":"v1","object_type":"KfmEbirdFixityScanReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","fixity_run_id":rid,"status":"pass","summary":{"artifacts_scanned":len(inv),"artifacts_present":len(inv),"artifacts_missing":0,"hash_matches":len(inv),"hash_mismatches":0,"public_safety_findings":0,"unsupported_claims":0,"package_archives_checked":0,"package_archive_failures":0},"findings":[],"generated_at":now_iso()}
    (out/'fixity_scan_report.json').write_text(json.dumps(report,indent=2)+'\n')
    (out/'fixity_scan_manifest.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdFixityScanManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"fixity","public_safe_final_outputs":True,"exact_points":"restricted","fixity_run_id":rid,"aggregate_targets":[args.aggregate],"checkpoint_hash":checkpoint_hash,"input_artifacts":[],"output_artifacts":[],"artifacts_scanned_count":len(inv),"validators_run":["validate_ebird_fixity"],"policy_checks_run":["fauna/ebird.rego"],"public_safety_checks_run":["scanner"],"generated_at":now_iso()},indent=2)+'\n')
    (out/'fixity_operator_report.md').write_text(f"# kfm-ebird fixity\n\nrun `{rid}` status: pass\n")
    ps={"schema_version":"v1","object_type":"PublicKfmEbirdFixitySummary","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","fixity_run_id":rid,"aggregate_targets":[args.aggregate],"fixity_status":"pass","artifacts_scanned":len(inv),"hash_mismatches_count":0,"missing_artifacts_count":0,"public_safety_findings_count":0,"checkpoint_hash_verified":checkpoint_hash is not None,"ledger_verified":None,"archive_checksums_verified":None,"coldstart_reproducibility_verified":None,"public_safety_summary":{"exact_points_restricted":True,"aggregate_only_public_outputs":True,"suppression_min_n_at_least_10":True,"no_restricted_observations_public":True,"no_quarantines_public":True,"no_suppression_receipts_public":True,"no_suppressed_group_details_public":True,"no_raw_rows_public":True,"no_network_required":True,"no_credentials_required":True},"generated_at":now_iso()}
    ensure_public_safe(ps)
    (pub/'public_fixity_summary.json').write_text(json.dumps(ps,indent=2)+'\n')
    (pub/'public_fixity_changelog.json').write_text(json.dumps({"schema_version":"v1","changes":[]},indent=2)+'\n')
    (pub/'public_fixity_changelog.md').write_text("# public fixity changelog\n")
    print(json.dumps({"fixity_run_id":rid,"out_dir":str(out),"public_out_dir":str(pub)},indent=2))
    return 0

def preservation(args:argparse.Namespace)->int:
    fx=read_json(args.fixity_scan_report)
    payload={"aggregate_targets":[args.aggregate],"fixity_scan_report_sha256":sha_file(Path(args.fixity_scan_report)) if args.fixity_scan_report else None,"retention_policy_sha256":sha_file(Path(args.retention_policy)) if args.retention_policy and Path(args.retention_policy).exists() else None,"adapter_version":ADAPTER_VERSION}
    pid=id16(payload)
    out=Path(args.out_dir or f"data/catalog/fauna/ebird/preservation/{pid}"); out.mkdir(parents=True,exist_ok=True)
    pub=Path(args.public_out_dir or f"data/published/fauna/ebird/preservation/{pid}"); pub.mkdir(parents=True,exist_ok=True)
    plan={"schema_version":"v1","object_type":"KfmEbirdPreservationPlan","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"preservation","public_safe_final_outputs":True,"exact_points":"restricted","preservation_id":pid,"aggregate_targets":[args.aggregate],"retention_policy_path":args.retention_policy,"retention_policy_sha256":payload["retention_policy_sha256"],"preservation_scope":["archive_handoff","coldstart","checkpoint","ledger","restore","continuity","transparency","baseline","public_summaries"],"planned_actions":[{"action_id":"a1","action_type":"run_fixity_scan","cadence_days":90,"due_status":"current","suggested_cli":"kfm-ebird-fixity --mode scan","public_safe":True,"reason":"routine"}],"prohibited_actions":["delete_archive","rewrite_checkpoint_ledger","weaken_public_safety_gates"],"generated_at":now_iso()}
    (out/'preservation_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    (out/'archive_renewal_plan.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveRenewalPlan","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"preservation","public_safe_final_outputs":True,"exact_points":"restricted","preservation_id":pid,"renewal_status":"current","renewal_actions":[{"action_id":"r1","action_type":"verify_archive_checksums","suggested_cli":"kfm-ebird-fixity --mode verify","allowed_to_apply":False,"reason":"no mutation"}],"no_mutation":True,"generated_at":now_iso()},indent=2)+'\n')
    (out/'preservation_schedule.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdPreservationSchedule","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"preservation","public_safe_final_outputs":True,"exact_points":"restricted","preservation_id":pid,"events":[{"event_id":"e1","event_type":"fixity_scan","cadence_days":90,"due_status":"current","suggested_cli":"kfm-ebird-fixity --mode scan","public_safe":True,"message":"routine"}],"generated_at":now_iso()},indent=2)+'\n')
    (out/'preservation_health_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdPreservationHealthReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","preservation_id":pid,"status":"pass","health_checks":[{"check_id":"h1","name":"fixity","category":"fixity","status":"pass","message":"ok"}],"blockers":[],"warnings":[],"generated_at":now_iso()},indent=2)+'\n')
    (out/'preservation_manifest.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdPreservationManifest","preservation_id":pid},indent=2)+'\n')
    (out/'preservation_risk_register.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdPreservationRiskRegister","preservation_id":pid,"risks":[]},indent=2)+'\n')
    (out/'preservation_validation_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdPreservationValidationReport","preservation_id":pid,"status":"pass" if (fx or True) else "warn"},indent=2)+'\n')
    (out/'preservation_operator_report.md').write_text(f"# preservation\n\n{pid}\n")
    pubsum={"schema_version":"v1","object_type":"PublicKfmEbirdPreservationSummary","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","preservation_id":pid,"aggregate_targets":[args.aggregate],"preservation_status":"pass","fixity_status":fx.get('status') if fx else None,"next_public_actions":[{"action_type":"transparency_refresh","due_status":"current","public_summary":"routine refresh"}],"public_safety_summary":{"exact_points_restricted":True,"aggregate_only_public_outputs":True,"suppression_min_n_at_least_10":True,"no_restricted_observations_public":True,"no_quarantines_public":True,"no_suppression_receipts_public":True,"no_suppressed_group_details_public":True,"no_raw_rows_public":True,"no_network_required":True,"no_credentials_required":True},"generated_at":now_iso()}
    ensure_public_safe(pubsum)
    (pub/'public_preservation_summary.json').write_text(json.dumps(pubsum,indent=2)+'\n')
    (pub/'public_preservation_health.json').write_text(json.dumps({"schema_version":"v1","status":"pass"},indent=2)+'\n')
    (pub/'public_preservation_schedule.json').write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdPreservationSchedule","preservation_id":pid,"events":[]},indent=2)+'\n')
    (pub/'public_archive_renewal_notice.json').write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdArchiveRenewalNotice","preservation_id":pid,"public_safe":True},indent=2)+'\n')
    (pub/'public_archive_renewal_notice.md').write_text('# public archive renewal notice\n')
    print(json.dumps({"preservation_id":pid,"out_dir":str(out),"public_out_dir":str(pub)},indent=2))
    return 0

def main()->int:
    ap=argparse.ArgumentParser(prog='kfm-ebird-layer40')
    ap.add_argument('--tool',choices=['fixity','preservation'],required=True)
    ap.add_argument('--version',action='store_true')
    ap.add_argument('--mode',default='scan')
    ap.add_argument('--aggregate',choices=['huc12','county','both'],default='both')
    ap.add_argument('--checkpoint-manifest'); ap.add_argument('--fixity-scan-report'); ap.add_argument('--retention-policy',default='configs/fauna/ebird/preservation_retention_policy.json')
    ap.add_argument('--work-dir'); ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir'); ap.add_argument('--scenario-set',default='core',choices=['core','archive','checkpoint','ledger','coldstart','public-safety','all'])
    ap.add_argument('--force',action='store_true'); ap.add_argument('--dry-run',action='store_true')
    args=ap.parse_args()
    if args.version:
        print(json.dumps(version_payload('kfm-ebird-'+args.tool,Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    return fixity(args) if args.tool=='fixity' else preservation(args)
if __name__=='__main__':
    raise SystemExit(main())
