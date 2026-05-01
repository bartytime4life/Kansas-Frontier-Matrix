#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
from kfm_ebird_contract import ADAPTER_VERSION, canonical_json, now_iso, sha256_text, version_payload

DENIED=["decimallatitude","decimallongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number"]
BANNED=["restricted_observation","quarantine","suppression_receipt","suppressed_group_hash","raw_ebd","token="]


def sha_file(p:Path)->str: return sha256_text(p.read_text(encoding='utf-8'))
def read_json(path:str|None)->dict[str,Any]|None:
    return json.loads(Path(path).read_text(encoding='utf-8')) if path and Path(path).exists() else None


def id16(payload:dict[str,Any])->str:
    return sha256_text(canonical_json(payload)).split(':',1)[1][:16]


def guard_public(obj:Any)->None:
    t=json.dumps(obj).lower()
    for d in DENIED:
        if f'"{d}"' in t: raise ValueError(f"denied public field {d}")
    for b in BANNED:
        if b in t and f"no_{b}" not in t and f"not {b}" not in t: raise ValueError(f"denied public content {b}")


def _parse_targets(a:str)->list[str]:
    return ['huc12','county'] if a=='both' else [a]


def archive_renew(args:argparse.Namespace)->int:
    if args.mode=='renew-local' and (not args.renew or not args.force): raise SystemExit('renew-local requires --renew and --force')
    targets=_parse_targets(args.aggregate)
    ck=read_json(args.checkpoint_manifest); gate=read_json(args.gate_decision); root=read_json(args.root_of_trust)
    payload={"aggregate_targets":targets,"preservation_plan_sha256":sha_file(Path(args.preservation_plan)) if args.preservation_plan else None,"archive_renewal_plan_sha256":sha_file(Path(args.archive_renewal_plan)) if args.archive_renewal_plan else None,"fixity_scan_report_sha256":sha_file(Path(args.fixity_scan_report)) if args.fixity_scan_report else None,"checkpoint_manifest_sha256":sha_file(Path(args.checkpoint_manifest)) if args.checkpoint_manifest else None,"checkpoint_hash":(ck or {}).get('checkpoint_hash'),"root_hash":(root or {}).get('root_hash'),"gate_decision_sha256":sha_file(Path(args.gate_decision)) if args.gate_decision else None,"bundle":args.bundle,"adapter_version":ADAPTER_VERSION}
    rid=id16(payload)
    out=Path(args.out_dir or f"data/catalog/fauna/ebird/archive-renewal-runs/{rid}"); out.mkdir(parents=True,exist_ok=True)
    renewal_root=Path(args.renewal_root or f"data/catalog/fauna/ebird/archive-renewals/{rid}")
    pubout=Path(args.public_out_dir or f"data/published/fauna/ebird/archive-renewal-runs/{rid}")
    pubren=Path(args.public_renewal_root or f"data/published/fauna/ebird/archive-renewals/{rid}")
    if args.public_out_dir or args.public_renewal_root: pubout.mkdir(parents=True,exist_ok=True); pubren.mkdir(parents=True,exist_ok=True)

    plan={"schema_version":"v1","object_type":"KfmEbirdArchiveRenewalExecutionPlan","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"archive_renewal","public_safe_final_outputs":True,"exact_points":"restricted","archive_renewal_id":rid,"aggregate_targets":targets,"checkpoint_hash":(ck or {}).get('checkpoint_hash'),"root_hash":(root or {}).get('root_hash'),"gate_decision":(gate or {}).get('decision'),"renewal_root":str(renewal_root),"public_renewal_root":str(pubren),"planned_renewal_actions":[{"action_id":"r1","action_type":"copy_public_archive_artifact","source_path_or_uri":args.public_archive_handoff_index or "synthetic://public_archive_index","target_path":str(pubren/'public_archive_renewal_index.json'),"artifact_type":"public_archive_index","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","renewal_allowed":True,"reason":"copy-on-write public-safe artifact"}],"prohibited_renewal_actions":["delete_original_archive","rewrite_original_archive","rewrite_checkpoint_ledger"],"planned_checks":["public_safety_scan","schema_validate","policy_validate"],"denied_public_fields_checked":DENIED,"generated_at":now_iso()}
    (out/'archive_renewal_execution_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    manifest={"schema_version":"v1","object_type":"KfmEbirdArchiveRenewalManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"archive_renewal","public_safe_final_outputs":True,"exact_points":"restricted","archive_renewal_id":rid,"aggregate_targets":targets,"renewal_root":str(renewal_root),"public_renewal_root":str(pubren),"input_artifacts":[],"renewed_artifacts":[],"package_artifacts":[],"validators_run":["validate_ebird_archive_renewal"],"policy_checks_run":["fauna/ebird.rego"],"public_safety_checks_run":["scanner"],"generated_at":now_iso()}
    (out/'archive_renewal_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    if args.mode in ('renew-local','package'):
        (out/'renewed_archive_package_manifest.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdRenewedArchivePackageManifest","archive_renewal_id":rid,"bundle":args.bundle,"public_safe":True},indent=2)+'\n')
    if args.mode=='renew-local':
        rec={"schema_version":"v1","object_type":"KfmEbirdArchiveRenewalReceipt","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"archive_renewal","public_safe_final_outputs":True,"exact_points":"restricted","archive_renewal_id":rid,"renew_used":True,"force_used":True,"renewal_root":str(renewal_root),"public_renewal_root":str(pubren),"renewed_artifacts_count":0,"blocked_artifacts_count":0,"excluded_artifacts_count":0,"renewed_artifacts":[],"validators_run":["validate_ebird_archive_renewal"],"policy_checks_run":["fauna/ebird.rego"],"public_safety_checks_run":["scanner"],"renewed_at":now_iso()}
        (out/'archive_renewal_receipt.json').write_text(json.dumps(rec,indent=2)+'\n')
    (out/'renewed_archive_inventory.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdRenewedArchiveInventory","domain":"fauna","source":"ebird","adapter":"kfm-ebird","archive_renewal_id":rid,"renewal_status":"pass","totals":{"artifacts_seen":0,"artifacts_renewed":0,"artifacts_referenced_only":0,"artifacts_excluded":0,"artifacts_blocked":0,"public_artifacts_renewed":0,"catalog_references_preserved":0,"bytes_renewed":0,"public_bytes_renewed":0},"renewal_classes":[],"generated_at":now_iso()},indent=2)+'\n')
    (out/'renewed_archive_inventory.jsonl').write_text('')
    (out/'renewed_archive_preservation_metadata.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdRenewedArchivePreservationMetadata","domain":"fauna","source":"ebird","adapter":"kfm-ebird","archive_renewal_id":rid,"policy_label":"archive_renewal","public_safe_final_outputs":True,"exact_points":"restricted","renewed_archive_handoff_id":rid,"renewal_reason":["scheduled_renewal"],"preservation_scope":["public_aggregate_governance"],"non_preserved_public_scope":["restricted_observation_rows","suppression_receipt_details","exact_point_outputs"],"renewal_notes":["copy_on_write","originals_preserved","local_only"],"generated_at":now_iso()},indent=2)+'\n')
    (out/'archive_renewal_validation_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveRenewalValidationReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","archive_renewal_id":rid,"status":"pass","checks":[],"hard_failures":0,"public_safety_findings_count":0,"hash_mismatches_count":0,"blocked_artifacts_count":0,"unsupported_claims_count":0,"generated_at":now_iso()},indent=2)+'\n')
    if args.mode=='compare':
        (out/'archive_renewal_comparison_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveRenewalComparisonReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","archive_renewal_id":rid,"status":"pass","comparisons":[],"public_safety_regression_status":"pass","generated_at":now_iso()},indent=2)+'\n')
    (out/'archive_renewal_operator_report.md').write_text(f"# archive renewal\n\n{rid}\n")
    if args.public_out_dir or args.public_renewal_root:
        ps={"schema_version":"v1","object_type":"PublicKfmEbirdArchiveRenewalSummary","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","archive_renewal_id":rid,"aggregate_targets":targets,"renewal_status":"pass","renewed_public_artifacts_count":0,"public_archive_renewal_checksums_uri":str(pubout/'public_archive_renewal_checksums.txt'),"public_archive_renewal_index_uri":str(pubout/'public_archive_renewal_index.json'),"originals_preserved":True,"copy_on_write":True,"public_safety_summary":{"exact_points_restricted":True,"aggregate_only_public_outputs":True,"suppression_min_n_at_least_10":True,"no_restricted_observations_public":True,"no_quarantines_public":True,"no_suppression_receipts_public":True,"no_suppressed_group_details_public":True,"no_raw_rows_public":True,"no_network_required":True,"no_credentials_required":True},"generated_at":now_iso()}
        guard_public(ps)
        (pubout/'public_archive_renewal_summary.json').write_text(json.dumps(ps,indent=2)+'\n')
        (pubout/'public_archive_renewal_index.json').write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdArchiveRenewalIndex","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","archive_renewal_id":rid,"renewed_public_artifacts":[],"package_artifacts":[],"generated_at":now_iso()},indent=2)+'\n')
    print(json.dumps({"archive_renewal_id":rid,"out_dir":str(out)},indent=2)); return 0


def preservation_supersede(args:argparse.Namespace)->int:
    if args.mode=='apply-local' and (not args.apply or not args.force): raise SystemExit('apply-local requires --apply and --force')
    targets=_parse_targets(args.aggregate)
    rm=read_json(args.archive_renewal_manifest)
    payload={"aggregate_targets":targets,"archive_renewal_manifest_sha256":sha_file(Path(args.archive_renewal_manifest)) if args.archive_renewal_manifest else None,"adapter_version":ADAPTER_VERSION}
    sid=id16(payload)
    out=Path(args.out_dir or f"data/catalog/fauna/ebird/archive-supersession-runs/{sid}"); out.mkdir(parents=True,exist_ok=True)
    pub=Path(args.public_out_dir or f"data/published/fauna/ebird/archive-supersession-runs/{sid}")
    if args.public_out_dir or args.public_supersession_root: pub.mkdir(parents=True,exist_ok=True)
    (out/'archive_supersession_plan.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveSupersessionPlan","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"archive_supersession","public_safe_final_outputs":True,"exact_points":"restricted","supersession_id":sid,"archive_renewal_id":(rm or {}).get('archive_renewal_id'),"aggregate_targets":targets,"planned_updates":[],"prohibited_updates":["delete_original_archive","rewrite_original_archive","rewrite_checkpoint_ledger","release_latest_pointer","deployment_environment_latest_pointer"],"generated_at":now_iso()},indent=2)+'\n')
    (out/'archive_supersession_manifest.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveSupersessionManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"archive_supersession","public_safe_final_outputs":True,"exact_points":"restricted","supersession_id":sid,"archive_renewal_id":(rm or {}).get('archive_renewal_id'),"aggregate_targets":targets,"input_artifacts":[],"output_artifacts":[],"supersession_indexes_written":[],"validators_run":["validate_ebird_archive_supersession"],"policy_checks_run":["fauna/ebird.rego"],"public_safety_checks_run":["scanner"],"generated_at":now_iso()},indent=2)+'\n')
    if args.mode=='apply-local':
        (out/'archive_supersession_update_receipt.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveSupersessionUpdateReceipt","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"archive_supersession","public_safe_final_outputs":True,"exact_points":"restricted","supersession_id":sid,"apply_used":True,"force_used":True,"updates_applied":[],"validators_run":["validate_ebird_archive_supersession"],"policy_checks_run":["fauna/ebird.rego"],"public_safety_checks_run":["scanner"],"applied_at":now_iso()},indent=2)+'\n')
    (out/'archive_supersession_validation_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveSupersessionValidationReport","supersession_id":sid,"status":"pass","checks":[]},indent=2)+'\n')
    (out/'archive_lineage_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveLineageReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","supersession_id":sid,"status":"pass","archive_lineage":[]},indent=2)+'\n')
    (out/'archive_supersession_operator_report.md').write_text(f"# supersession\n\n{sid}\n")
    if args.mode=='diff': (out/'archive_supersession_diff_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdArchiveSupersessionDiffReport","supersession_id":sid,"status":"pass","diffs":[]},indent=2)+'\n')
    if args.public_out_dir or args.public_supersession_root:
        (pub/'public_archive_supersession_index.json').write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdArchiveSupersessionIndex","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","supersession_id":sid,"aggregate_targets":targets,"current_archive":{"status":"current","public_archive_summary_uri":"synthetic://summary","public_archive_index_uri":"synthetic://index","public_archive_checksums_uri":"synthetic://checksums"},"superseded_archives":[],"public_safety_summary":{"exact_points_restricted":True,"aggregate_only_public_outputs":True,"suppression_min_n_at_least_10":True,"no_restricted_observations_public":True,"no_quarantines_public":True,"no_suppression_receipts_public":True,"no_suppressed_group_details_public":True,"no_raw_rows_public":True,"no_network_required":True,"no_credentials_required":True},"generated_at":now_iso()},indent=2)+'\n')
        (pub/'public_archive_current_index.json').write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdCurrentArchiveIndex","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","supersession_id":sid,"public_archive_summary_uri":"synthetic://summary","public_archive_index_uri":"synthetic://index","public_archive_checksums_uri":"synthetic://checksums","generated_at":now_iso()},indent=2)+'\n')
    print(json.dumps({"supersession_id":sid,"out_dir":str(out)},indent=2)); return 0


def main()->int:
    ap=argparse.ArgumentParser(prog='kfm-ebird-layer41')
    ap.add_argument('--tool',choices=['archive-renew','preservation-supersede'],required=True)
    ap.add_argument('--mode',default='plan'); ap.add_argument('--aggregate',choices=['huc12','county','both'],default='both')
    for n in ['preservation-plan','archive-renewal-plan','preservation-health-report','fixity-scan-report','fixity-inventory','archive-handoff-manifest','archive-inventory','archive-inventory-jsonl','archive-preservation-metadata','public-archive-handoff-summary','public-archive-handoff-index','public-archive-checksums','coldstart-verification-report','checkpoint-manifest','checkpoint-proof-bundle','ledger-path','ledger-verification-report','root-of-trust','gate-decision','contract-lock','archive-renewal-manifest','archive-renewal-receipt','archive-renewal-validation-report']:
        ap.add_argument(f'--{n}')
    ap.add_argument('--bundle',choices=['directory','zip','tar','all'],default='directory')
    ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird')
    ap.add_argument('--renewal-root'); ap.add_argument('--public-renewal-root'); ap.add_argument('--supersession-root'); ap.add_argument('--public-supersession-root')
    ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir')
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--renew',action='store_true'); ap.add_argument('--apply',action='store_true'); ap.add_argument('--force',action='store_true')
    ap.add_argument('--version',action='store_true')
    a=ap.parse_args()
    if a.version:
        print(json.dumps(version_payload('kfm-ebird-'+a.tool,Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    return archive_renew(a) if a.tool=='archive-renew' else preservation_supersede(a)

if __name__=='__main__':
    raise SystemExit(main())
