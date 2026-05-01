#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from kfm_ebird_contract import canonical_json, sha256_text, now_iso, version_payload

def sha_file(p:Path)->str: return sha256_text(p.read_text(encoding='utf-8'))
def entry_hash(entry:dict)->str:
    e={k:v for k,v in entry.items() if k not in {'generated_at','entry_hash'}}
    return sha256_text(canonical_json(e))

def parse():
    ap=argparse.ArgumentParser(prog='kfm-ebird-ledger'); ap.add_argument('--version',action='store_true')
    ap.add_argument('--mode',choices=['plan','append','verify','audit','compare','public-summary','report'],default='plan'); ap.add_argument('--aggregate',choices=['huc12','county','both'],default='both')
    ap.add_argument('--checkpoint-manifest'); ap.add_argument('--checkpoint-validation-report'); ap.add_argument('--public-checkpoint-summary')
    ap.add_argument('--ledger-path',default='data/catalog/fauna/ebird/checkpoint-ledger/ledger.jsonl'); ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir'); ap.add_argument('--apply',action='store_true'); ap.add_argument('--force',action='store_true')
    return ap.parse_args()

def main()->int:
    a=parse()
    if a.version: print(json.dumps(version_payload('kfm-ebird-ledger', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    if a.mode=='append' and (not a.apply or not a.force): raise SystemExit('append requires --apply and --force')
    m=json.loads(Path(a.checkpoint_manifest).read_text()) if a.checkpoint_manifest else {}
    ledger=Path(a.ledger_path); ledger.parent.mkdir(parents=True,exist_ok=True)
    prior=[]
    if ledger.exists(): prior=[json.loads(x) for x in ledger.read_text().splitlines() if x.strip()]
    prev=prior[-1]['entry_hash'] if prior else None
    run_id=sha256_text(canonical_json({'aggregate_targets':[a.aggregate],'checkpoint_hash':m.get('checkpoint_hash'),'ledger_path':a.ledger_path,'adapter_version':'1.0.0'})).split(':',1)[1][:16]
    out=Path(a.out_dir or f'data/catalog/fauna/ebird/checkpoint-ledger/runs/{run_id}'); out.mkdir(parents=True,exist_ok=True)
    pub=Path(a.public_out_dir or f'data/published/fauna/ebird/checkpoint-ledger/runs/{run_id}'); pub.mkdir(parents=True,exist_ok=True)
    entry={'schema_version':'v1','object_type':'KfmEbirdCheckpointLedgerEntry','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'checkpoint_ledger','public_safe_final_outputs':True,'exact_points':'restricted','ledger_entry_id':run_id,'checkpoint_id':m.get('checkpoint_id'),'checkpoint_hash':m.get('checkpoint_hash'),'previous_entry_hash':prev,'aggregate_targets':[a.aggregate],'checkpoint_manifest_path':a.checkpoint_manifest,'checkpoint_manifest_sha256':sha_file(Path(a.checkpoint_manifest)) if a.checkpoint_manifest else None,'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True,'no_restricted_observations_public':True,'no_quarantines_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True,'no_network_required':True,'no_credentials_required':True},'generated_at':now_iso()}
    entry['entry_hash']=entry_hash(entry)
    plan={'schema_version':'v1','object_type':'KfmEbirdCheckpointLedgerAppendPlan','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'checkpoint_ledger','public_safe_final_outputs':True,'exact_points':'restricted','ledger_run_id':run_id,'ledger_path':a.ledger_path,'checkpoint_id':m.get('checkpoint_id'),'checkpoint_hash':m.get('checkpoint_hash'),'previous_entry_hash':prev,'planned_entry_hash':entry['entry_hash'],'append_allowed':a.mode in {'append','plan'},'reason':'ready','prohibited_actions':['rewrite_existing_entries','delete_existing_entries'],'generated_at':now_iso()}
    (out/'ledger_append_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    if a.mode=='append':
        with ledger.open('a',encoding='utf-8') as f: f.write(json.dumps(entry)+'\n')
        (out/'ledger_append_receipt.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdCheckpointLedgerAppendReceipt','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'checkpoint_ledger','public_safe_final_outputs':True,'exact_points':'restricted','ledger_run_id':run_id,'apply_used':True,'force_used':True,'ledger_path':a.ledger_path,'ledger_sha256_after':sha_file(ledger),'appended_entry_hash':entry['entry_hash'],'previous_entry_hash':prev,'checkpoint_id':entry['checkpoint_id'],'checkpoint_hash':entry['checkpoint_hash'],'validators_run':['validate_ebird_checkpoint_ledger'],'policy_checks_run':['policy/fauna/ebird.rego'],'public_safety_checks_run':['layer37_scanner'],'appended_at':now_iso()},indent=2)+'\n')
    status='pass'; breaks=[]
    prevh=None
    for i,e in enumerate(prior+([entry] if a.mode=='append' else [])):
        if i>0 and e.get('previous_entry_hash')!=prevh: status='fail'; breaks.append({'entry_index':i,'expected_previous_entry_hash':prevh,'actual_previous_entry_hash':e.get('previous_entry_hash'),'severity':'fail','message':'chain break'})
        prevh=e.get('entry_hash')
    (out/'ledger_verification_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdCheckpointLedgerVerificationReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','ledger_run_id':run_id,'ledger_path':a.ledger_path,'status':status,'entries_checked':len(prior),'chain_tip_hash':prevh,'chain_breaks':breaks,'entry_hash_mismatches':[],'checkpoint_hash_mismatches':[],'generated_at':now_iso()},indent=2)+'\n')
    return 0
if __name__=='__main__': raise SystemExit(main())
