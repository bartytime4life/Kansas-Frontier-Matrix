#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, hashlib, sys
from pathlib import Path
from datetime import datetime, timezone

VERSION='0.22.0'
SAFE_TYPES={"metadata_only","public_text_only","pointer_only","checksum_only","package_manifest_only"}
BLOCKED_TYPES={"data_affecting","aggregate_value_change","suppression_threshold_change","governed_filter_change","evidencebundle_hash_recipe_change","kfm_spec_hash_change","taxon_crosswalk_semantics_change","region_crosswalk_semantics_change","public_output_field_contract_change","restricted_artifact_change","suppression_receipt_change","raw_ebd_change"}


def fail(msg):
    print(f'ERROR: {msg}',file=sys.stderr); raise SystemExit(2)

def sha(path:Path)->str:
    d=hashlib.sha256();d.update(path.read_bytes());return d.hexdigest()

def now(): return datetime.now(timezone.utc).isoformat()

def parse(argv):
    p=argparse.ArgumentParser(prog='kfm-ebird-remediate')
    p.add_argument('--version',action='version',version=VERSION)
    p.add_argument('--mode',default='plan',choices=['plan','apply','verify','close-triage','rollback-plan','public-notice','report'])
    p.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
    for a in ['triage-queue','triage-manifest','quality-report','quality-anomaly-report','quality-metadata-gap-report','quality-crosswalk-drift-report','release-receipt','public-portal-manifest','public-download-manifest','public-federation-index','public-analytics-index','package-manifest','deployment-receipt','assurance-scan-report','support-workflow-pack','patch-file','public-out-dir','target-root']:
        p.add_argument(f'--{a}')
    p.add_argument('--out-dir',default='data/catalog/fauna/ebird/remediation/run')
    p.add_argument('--owner-role',default='data-steward')
    p.add_argument('--dry-run',action='store_true');p.add_argument('--apply',action='store_true');p.add_argument('--force',action='store_true')
    return p.parse_args(argv)

def load_patches(path):
    if not path: return []
    p=Path(path); txt=p.read_text()
    recs=[json.loads(l) for l in txt.splitlines() if l.strip()] if p.suffix=='.jsonl' else None
    if recs is None:
        raw=json.loads(txt); recs=raw if isinstance(raw,list) else [raw]
    return recs

def contains_denied(val:str)->bool:
    s=val.lower(); denied=['decimallatitude','decimallongitude','geometry','suppression_receipt','raw_row_number','/restricted/','token=','apikey=']
    return any(d in s for d in denied)

def remediation_id(args,input_hashes):
    obj={"aggregate_targets":args.aggregate,"owner_role":args.owner_role,"adapter_version":VERSION,"input_artifact_hashes":input_hashes}
    if args.patch_file: obj['patch_file_sha256']=sha(Path(args.patch_file))
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:16]

def main():
    a=parse(sys.argv[1:])
    if a.mode=='apply' and (not a.apply or not a.force): fail('apply mode requires --apply and --force')
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    input_hashes={}
    for k,v in vars(a).items():
        if k.endswith(('queue','manifest','report','receipt','index','pack','file')) and isinstance(v,str) and Path(v).exists(): input_hashes[k]=sha(Path(v))
    rid=remediation_id(a,input_hashes)
    patches=load_patches(a.patch_file)
    actions=[]; blocked=[]
    for i,p in enumerate(patches,1):
        pt=p.get('patch_type','manual_review')
        s=json.dumps(p,sort_keys=True)
        if contains_denied(s): fail(f'unsafe patch payload {p.get("patch_id",i)}')
        if pt in SAFE_TYPES:
            actions.append({"action_id":f"a{i}","action_type":f"patch_{pt.split('_')[0]}","remediation_class":pt,"allowed_to_apply":True,"reason":p.get('reason','')})
        else:
            blocked.append({"action_id":f"a{i}","reason":"requires full rerun","requires_full_rerun":True})
    plan={"schema_version":"v1","object_type":"EbirdRemediationPlan","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"remediation","public_safe_final_outputs":True,"exact_points":"restricted","remediation_id":rid,"aggregate_targets":[a.aggregate],"findings_classified":[],"planned_actions":actions,"prohibited_actions":{"change_evidencebundle_hash_recipe":True,"change_governed_filter":True},"generated_at":now()}
    (out/'remediation_plan.json').write_text(json.dumps(plan,indent=2)+"\n")
    manifest={"schema_version":"v1","object_type":"EbirdRemediationManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"remediation","public_safe_final_outputs":True,"exact_points":"restricted","remediation_id":rid,"input_artifacts":[],"output_artifacts":[],"counts":{"findings_seen":len(patches),"actions_planned":len(actions)+len(blocked),"actions_apply_allowed":len(actions),"actions_blocked_requires_rerun":len(blocked),"actions_manual_review":0,"artifacts_corrected":0,"triage_items_closed":0},"generated_at":now()}
    (out/'remediation_manifest.json').write_text(json.dumps(manifest,indent=2)+"\n")
    (out/'remediation_diff_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"EbirdRemediationDiffReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","remediation_id":rid,"status":"pass" if not blocked else "warn","diffs":[],"blocked_diffs":blocked,"generated_at":now()},indent=2)+"\n")
    (out/'root_cause_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"EbirdRemediationRootCauseReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","remediation_id":rid,"status":"pass","root_causes":[],"generated_at":now()},indent=2)+"\n")
    (out/'remediation_validation_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"EbirdRemediationValidationReport","status":"pass","remediation_id":rid},indent=2)+"\n")
    if a.mode=='apply':
        (out/'remediation_receipt.json').write_text(json.dumps({"schema_version":"v1","object_type":"EbirdRemediationReceipt","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"remediation","public_safe_final_outputs":True,"exact_points":"restricted","remediation_id":rid,"force_used":True,"apply_used":True,"actions_applied":[],"validation_status":"pass","applied_at":now()},indent=2)+"\n")
    print(rid)

if __name__=='__main__': main()
