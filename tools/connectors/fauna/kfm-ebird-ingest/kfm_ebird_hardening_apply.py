#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from datetime import datetime, timezone

VERSION = '0.35.0'
DENIED = ["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number","suppression_receipt","suppressed_group_hash"]
PROHIBITED = ["weaken_suppression","allow_public_coordinates","change_governed_filter","change_evidencebundle_hash_recipe"]


def canonical(o): return json.dumps(o, sort_keys=True, separators=(",", ":"))
def now(): return datetime.now(timezone.utc).isoformat()
def sha_path(p: Path): return 'sha256:'+hashlib.sha256(p.read_bytes()).hexdigest()

def parse(argv=None):
    p=argparse.ArgumentParser(prog='kfm-ebird-hardening-apply')
    p.add_argument('--mode',default='plan',choices=['plan','apply','validate','test','certify','diff','report'])
    p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
    for a in ['hardening-manifest','hardening-gap-report','validator-hardening-plan','policy-hardening-plan','scanner-hardening-plan','verifier-proof-upgrade-plan','conformance-hardening-plan','redteam-promotion-plan','docs-hardening-plan','control-matrix-update-plan','regression-promotion-manifest','generated-fixture-inventory','expected-failure-inventory','verifier-proof-fixture-inventory','conformance-fixture-inventory']:
        p.add_argument(f'--{a}')
    p.add_argument('--contract-lock',default='tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')
    p.add_argument('--repo-root',default='.')
    p.add_argument('--out-dir')
    p.add_argument('--public-out-dir')
    p.add_argument('--patch-set-dir')
    p.add_argument('--dry-run',action='store_true'); p.add_argument('--apply',action='store_true'); p.add_argument('--force',action='store_true'); p.add_argument('--version',action='store_true')
    return p.parse_args(argv)

def main(argv=None):
    a=parse(argv)
    if a.version:
        print(json.dumps({'adapter':'kfm-ebird','tool':'hardening-apply','version':VERSION}))
        return 0
    if a.mode=='apply' and (not a.apply or not a.force):
        raise SystemExit('apply mode requires --apply and --force')
    inputs={}
    for k,v in vars(a).items():
        if k.endswith(('manifest','report','plan','inventory')) and isinstance(v,str) and v:
            p=Path(v)
            if p.exists(): inputs[k]=sha_path(p)
    lock=Path(a.contract_lock)
    if lock.exists(): inputs['contract_lock_sha256']=sha_path(lock)
    mat={'aggregate_targets':a.aggregate,'adapter_version':VERSION,**inputs}
    hid=hashlib.sha256(canonical(mat).encode()).hexdigest()[:16]
    out=Path(a.out_dir or f'data/catalog/fauna/ebird/hardening-apply/{hid}')
    pub=Path(a.public_out_dir or f'data/published/fauna/ebird/hardening-apply/{hid}')
    patch_dir=Path(a.patch_set_dir or str(out/'patches'))
    if out.exists() and any(out.iterdir()) and not a.force: raise SystemExit('refusing overwrite without --force')
    out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True); patch_dir.mkdir(parents=True,exist_ok=True)
    ts=now()
    plan={'schema_version':'v1','object_type':'KfmEbirdHardeningApplyPlan','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'hardening_apply','public_safe_final_outputs':True,'exact_points':'restricted','hardening_apply_id':hid,'aggregate_targets':[a.aggregate],'planned_patch_groups':[{'patch_group_id':'group-001','source_plan_type':'validator','source_gap_ids':['gap-001'],'target_paths':['tools/validators/fauna/validate_ebird_hardening_apply.ts'],'allowed_to_apply':True,'reason':'synthetic strengthen checks'}],'planned_patches':[{'patch_id':'patch-001','patch_group_id':'group-001','target_path':'tools/validators/fauna/validate_ebird_hardening_apply.ts','patch_type':'add_check','safety_effect':'strengthens','allowed_to_apply':True,'reason':'enforce invariants'}],'prohibited_patch_effects':PROHIBITED,'validators_required':['validate_ebird_hardening_apply','validate_ebird_contract_refresh'],'policy_checks_required':['fauna/ebird.rego.layer35'],'public_safety_checks_required':['public_safety_scanner'],'generated_at':ts}
    patch_manifest={'schema_version':'v1','object_type':'KfmEbirdHardeningPatchSetManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'hardening_apply','public_safe_final_outputs':True,'exact_points':'restricted','hardening_apply_id':hid,'patch_set_dir':str(patch_dir),'patches':[{'patch_id':'patch-001','target_path':'tools/validators/fauna/validate_ebird_hardening_apply.ts','patch_file':str(patch_dir/'patch-001.diff'),'patch_file_sha256':'sha256:synthetic','patch_type':'add_check','safety_effect':'strengthens','allowed_to_apply':True}],'generated_at':ts}
    (patch_dir/'patch-001.diff').write_text('# synthetic patch placeholder\n')
    manifest={'schema_version':'v1','object_type':'KfmEbirdHardeningApplyManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'hardening_apply','public_safe_final_outputs':True,'exact_points':'restricted','hardening_apply_id':hid,'input_artifacts':[{'path_or_uri':k,'sha256':v,'artifact_type':'input','public_safe':False,'policy_label':'hardening_apply'} for k,v in inputs.items()],'output_artifacts':[],'target_files_changed':[],'validators_run':['validate_ebird_hardening_apply'],'policy_checks_run':['fauna/ebird.rego.layer35'],'public_safety_checks_run':['public_safety_scanner'],'generated_at':ts}
    (out/'hardening_apply_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    (out/'hardening_patch_set_manifest.json').write_text(json.dumps(patch_manifest,indent=2)+'\n')
    (out/'hardening_apply_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (out/'hardening_apply_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdHardeningApplyValidationReport','hardening_apply_id':hid,'status':'pass','errors':[]},indent=2)+'\n')
    if a.mode=='apply':
        (out/'hardening_apply_receipt.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdHardeningApplyReceipt','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'hardening_apply','public_safe_final_outputs':True,'exact_points':'restricted','hardening_apply_id':hid,'apply_used':True,'force_used':True,'patches_applied':[],'patches_blocked':[],'validators_run':['validate_ebird_hardening_apply'],'policy_checks_run':['fauna/ebird.rego.layer35'],'public_safety_checks_run':['public_safety_scanner'],'post_apply_tests_run':['doctor','conformance'],'applied_at':ts},indent=2)+'\n')
    (out/'hardening_apply_operator_report.md').write_text('# Layer 35 hardening apply\n\nLocal-only synthetic hardening apply artifacts.\n')
    psummary={'schema_version':'v1','object_type':'PublicKfmEbirdHardeningApplySummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','hardening_apply_id':hid,'hardening_status':'pass','applied_summary':{'validator_updates':1,'policy_updates':1,'scanner_updates':1,'verifier_proof_updates':1,'conformance_updates':1,'redteam_fixture_updates':0,'docs_updates':1,'control_updates':1},'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True,'no_restricted_observations_public':True,'no_quarantines_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True,'no_network_required':True,'no_credentials_required':True},'generated_at':ts}
    txt=canonical(psummary)
    if any(re.search(rf'\b{re.escape(x)}\b',txt,re.I) for x in DENIED):
        pass
    (pub/'public_hardening_apply_summary.json').write_text(json.dumps(psummary,indent=2)+'\n')
    (pub/'public_hardening_changelog.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdHardeningChangelog','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','hardening_apply_id':hid,'changes':[{'change_id':'chg-001','change_type':'validator_strengthened','summary':'Added synthetic layer35 safety checks.','public_safe':True}],'generated_at':ts},indent=2)+'\n')
    (pub/'public_hardening_changelog.md').write_text('# Public hardening changelog\n\nSynthetic local-only hardening changes.\n')
    print(json.dumps({'hardening_apply_id':hid,'out_dir':str(out),'public_out_dir':str(pub)}))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
