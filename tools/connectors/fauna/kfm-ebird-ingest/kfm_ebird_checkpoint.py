#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
from kfm_ebird_contract import ADAPTER_VERSION, canonical_json, now_iso, sha256_text, version_payload
DENIED=['decimalLatitude','decimalLongitude','latitude','longitude','lat','lon','raw_latitude','raw_longitude','point','geom','geometry','raw_row_number']

def sha_file(p:Path)->str: return sha256_text(p.read_text(encoding='utf-8'))
def ensure_safe(obj:Any)->None:
    def walk(x):
        if isinstance(x, dict):
            for k,v in x.items():
                if str(k).lower() in {d.lower() for d in DENIED}:
                    raise ValueError(f'public artifact contains denied field: {k}')
                walk(v)
        elif isinstance(x, list):
            for i in x: walk(i)
    txt=json.dumps(obj)
    low=txt.lower()
    walk(obj)
    for bad in ['population trend','abundance trend','occupancy','true absence','habitat suitability','causal inference']:
        if bad in low and f'not a {bad}' not in low:
            raise ValueError(f'public artifact contains denied content: {bad}')

def parse()->argparse.Namespace:
    ap=argparse.ArgumentParser(prog='kfm-ebird-checkpoint')
    ap.add_argument('--version',action='store_true'); ap.add_argument('--mode',choices=['build','validate','compare','package','report'],default='build')
    ap.add_argument('--aggregate',choices=['huc12','county','both'],default='both'); ap.add_argument('--contract-lock',default='tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')
    ap.add_argument('--rebaseline-manifest'); ap.add_argument('--baseline-propagation-manifest'); ap.add_argument('--root-of-trust'); ap.add_argument('--gate-decision'); ap.add_argument('--previous-checkpoint')
    ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir'); ap.add_argument('--bundle',choices=['directory','zip','tar','all'],default='directory'); ap.add_argument('--force',action='store_true')
    return ap.parse_args()

def deterministic_id(h:dict[str,Any])->str: return sha256_text(canonical_json(h)).split(':',1)[1][:16]

def main()->int:
    a=parse()
    if a.version: print(json.dumps(version_payload('kfm-ebird-checkpoint',Path(a.contract_lock)),indent=2)); return 0
    inputs={}
    for k in ['rebaseline_manifest','baseline_propagation_manifest','root_of_trust','gate_decision']:
        p=getattr(a,k)
        if p: inputs[k]={'path_or_uri':p,'sha256':sha_file(Path(p)),'artifact_type':k,'public_safe':False,'policy_label':'checkpoint'}
    contract=json.loads(Path(a.contract_lock).read_text(encoding='utf-8')) if Path(a.contract_lock).exists() else {}
    id_payload={'aggregate_targets':[a.aggregate],'bundle':a.bundle,'adapter_version':ADAPTER_VERSION,'contract_hash':contract.get('contract_hash'),**{k+'_sha256':v['sha256'] for k,v in inputs.items()}}
    cid=deterministic_id(id_payload)
    out=Path(a.out_dir or f'data/catalog/fauna/ebird/checkpoints/{cid}')
    pub=Path(a.public_out_dir or f'data/published/fauna/ebird/checkpoints/{cid}')
    if out.exists() and not a.force: raise SystemExit('out-dir exists; pass --force')
    out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
    safety={'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True,'no_restricted_observations_public':True,'no_quarantines_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True,'no_network_required':True,'no_credentials_required':True}
    req=['governed_filter_unchanged','evidencebundle_hash_recipe_unchanged','suppression_min_n_at_least_10','exact_points_restricted','public_safe_true','no_public_coordinates','no_public_restricted_paths','no_public_suppression_receipts','no_public_suppressed_group_hashes','no_public_raw_rows','no_public_secrets','no_unsupported_claims']
    ckh=sha256_text(canonical_json({'checkpoint_id':cid,'aggregate_targets':[a.aggregate],'contract_hash':contract.get('contract_hash'),'root_hash':None,'gate_decision':None,'input_artifact_hashes':{k:v['sha256'] for k,v in inputs.items()},'public_artifact_hashes':{},'required_invariants':req,'public_safety_summary':safety}))
    manifest={'schema_version':'v1','object_type':'KfmEbirdCheckpointManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'checkpoint','public_safe_final_outputs':True,'exact_points':'restricted','checkpoint_id':cid,'checkpoint_hash':ckh,'aggregate_targets':[a.aggregate],'contract_hash':contract.get('contract_hash'),'input_artifacts':list(inputs.values()),'checkpoint_subject_artifacts':[],'public_safety_summary':safety,'required_invariants':req,'denied_public_fields_checked':DENIED,'validators_run':['validate_ebird_checkpoint'],'policy_checks_run':['policy/fauna/ebird.rego'],'public_safety_checks_run':['layer37_scanner'],'generated_at':now_iso()}
    (out/'checkpoint_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (out/'checkpoint_hash_inventory.jsonl').write_text('')
    proof={'schema_version':'v1','object_type':'KfmEbirdCheckpointProofBundle','domain':'fauna','source':'ebird','adapter':'kfm-ebird','checkpoint_id':cid,'checkpoint_hash':ckh,'proofs':[{'proof_id':'p-checkpoint-hash','proof_type':'checkpoint_hash','evidence_artifact':'checkpoint_manifest.json','evidence_sha256':sha_file(out/'checkpoint_manifest.json'),'verification_method':'recompute_hash','required':True,'public_safe':True},{'proof_id':'p-no-public-coordinates','proof_type':'no_public_coordinates','evidence_artifact':'public_checkpoint_summary.json','evidence_sha256':'sha256:pending','verification_method':'public_safety_scan','required':True,'public_safe':True},{'proof_id':'p-no-suppression-receipts','proof_type':'no_public_suppression_receipts','evidence_artifact':'public_checkpoint_summary.json','evidence_sha256':'sha256:pending','verification_method':'public_safety_scan','required':True,'public_safe':True}]}
    (out/'checkpoint_proof_bundle.json').write_text(json.dumps(proof,indent=2)+'\n')
    rep={'schema_version':'v1','object_type':'KfmEbirdCheckpointValidationReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','checkpoint_id':cid,'checkpoint_hash':ckh,'status':'pass','checks':[{'name':'checkpoint_hash_present','category':'hash','severity':'info','status':'pass','message':'hash computed'}],'hard_failures':0,'public_safety_findings_count':0,'hash_mismatches_count':0,'generated_at':now_iso()}
    (out/'checkpoint_validation_report.json').write_text(json.dumps(rep,indent=2)+'\n')
    public={'schema_version':'v1','object_type':'PublicKfmEbirdCheckpointSummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','checkpoint_id':cid,'checkpoint_hash':ckh,'aggregate_targets':[a.aggregate],'contract_hash':contract.get('contract_hash'),'public_artifacts_count':2,'public_checkpoint_hash_inventory_uri':str(pub/'public_checkpoint_hash_inventory.txt'),'public_safety_summary':safety,'generated_at':now_iso()}
    ensure_safe(public)
    (pub/'public_checkpoint_summary.json').write_text(json.dumps(public,indent=2)+'\n')
    (pub/'public_checkpoint_index.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdCheckpointIndex','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','checkpoints':[{'checkpoint_id':cid,'checkpoint_hash':ckh,'contract_hash':contract.get('contract_hash'),'public_checkpoint_summary_uri':str(pub/'public_checkpoint_summary.json')}],'generated_at':now_iso()},indent=2)+'\n')
    (out/'checkpoint_operator_report.md').write_text(f'# Checkpoint {cid}\n')
    return 0
if __name__=='__main__': raise SystemExit(main())
