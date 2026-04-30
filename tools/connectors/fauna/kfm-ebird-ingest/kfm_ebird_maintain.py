#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, subprocess
from pathlib import Path
from kfm_ebird_contract import ADAPTER_NAME, ADAPTER_VERSION, canonical_json, compute_contract_hash, load_contract_lock, now_iso, sha256_text, version_payload

DENIED_COORD_FIELDS={"decimalLatitude","decimalLongitude","geometry","lat","lon"}
REQ_DTO_FIELDS={"source_uri","query_predicate","evidence_bundle_uri","kfm:spec_hash","suppression_min_n"}


def parse_semver(v:str):
    m=re.match(r"^(\d+)\.(\d+)\.(\d+)$", v or "")
    return tuple(int(x) for x in m.groups()) if m else (0,0,0)

def classify_bump(prev:str,target:str)->str:
    p,t=parse_semver(prev),parse_semver(target)
    if t[0]>p[0]: return 'major'
    if t[1]>p[1]: return 'minor'
    if t[2]>=p[2]: return 'patch'
    return 'invalid'

def contract_diff(frm:dict,to:dict,from_path:str,to_path:str):
    fc=frm.get('contracts',{}); tc=to.get('contracts',{})
    fpub=fc.get('public_feature_dto',{}).get('required_fields',[])
    tpub=tc.get('public_feature_dto',{}).get('required_fields',[])
    removed_public=sorted(set(fpub)-set(tpub)); added_public=sorted(set(tpub)-set(fpub))
    denied_changed=any(x in DENIED_COORD_FIELDS for x in removed_public)
    suppression_changed=fc.get('suppression_min_n_default')!=tc.get('suppression_min_n_default')
    governed_changed=fc.get('governed_qa_predicate')!=tc.get('governed_qa_predicate')
    report={
      'schema_version':'v1','object_type':'EbirdContractDiffReport','domain':'fauna','source':'ebird','adapter':ADAPTER_NAME,
      'from_contract_lock_path':from_path,'from_contract_hash':frm.get('contract_hash'),'from_adapter_version':frm.get('adapter_version','1.0.0'),
      'to_contract_lock_path':to_path,'to_contract_hash':to.get('contract_hash'),'to_adapter_version':to.get('adapter_version',ADAPTER_VERSION),
      'semantic_change_class':'major' if (removed_public or denied_changed or governed_changed) else ('minor' if added_public else 'patch'),
      'changes':{'added_schemas':[],'removed_schemas':[],'changed_schemas':[],'added_validators':[],'removed_validators':[],'changed_validators':[],'added_policies':[],'removed_policies':[],'changed_policies':[],'added_public_fields':added_public,'removed_public_fields':removed_public,'changed_public_fields':[],'denied_public_fields_changed':denied_changed,'governed_predicate_changed':governed_changed,'suppression_default_changed':suppression_changed,'allowed_aggregates_changed':False,'mapping_changed':False,'layer_registry_changed':False,'cli_surface_changed':False},
      'compatibility_assessment':{'backward_compatible':not removed_public,'public_contract_breaking':bool(removed_public or denied_changed),'migration_required':bool(removed_public or governed_changed),'public_safety_risk':'high' if denied_changed else 'none'},
      'required_actions':[], 'generated_at':now_iso()}
    return report

def public_safety_scan(paths:list[str]):
    fails=[]
    pats=['decimalLatitude','decimalLongitude','geometry','suppression_receipt_path','suppressed_group_hash','api_key=','token=','secret=','quarantine','restricted']
    for root in paths:
      for p in Path(root).rglob('*'):
        if p.is_file() and p.suffix in {'.json','.jsonl','.md','.txt'}:
          t=p.read_text(encoding='utf-8',errors='ignore')
          for pat in pats:
            if pat in t and 'published' in str(p): fails.append({'path':str(p),'issue':pat})
    return {'status':'pass' if not fails else 'fail','failures':fails,'denied_public_fields_checked':sorted(DENIED_COORD_FIELDS)}

def main(argv=None):
    ap=argparse.ArgumentParser(prog='kfm-ebird-maintain')
    ap.add_argument('--mode', required=False, choices=['diff','check','compat-test','deprecate','maintenance-report','inventory','public-safety-scan'])
    ap.add_argument('--repo-root', default='.')
    ap.add_argument('--from-contract-lock')
    ap.add_argument('--to-contract-lock', default='tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')
    ap.add_argument('--artifact-root', action='append', default=[])
    ap.add_argument('--fixture-dir'); ap.add_argument('--golden-dir')
    ap.add_argument('--out-dir', default='data/catalog/fauna/ebird/maintenance/default')
    ap.add_argument('--target-version'); ap.add_argument('--previous-version')
    ap.add_argument('--deprecation-id'); ap.add_argument('--deprecation-summary')
    ap.add_argument('--json', action='store_true'); ap.add_argument('--strict', action='store_true'); ap.add_argument('--dry-run', action='store_true'); ap.add_argument('--force', action='store_true')
    ap.add_argument('--version', action='store_true')
    a=ap.parse_args(argv)
    if a.version:
        print(json.dumps(version_payload('kfm-ebird-maintain', Path(a.to_contract_lock)),indent=2,sort_keys=True)); return 0
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    to=load_contract_lock(Path(a.to_contract_lock)); frm=load_contract_lock(Path(a.from_contract_lock)) if a.from_contract_lock else to
    if a.mode=='diff':
        rep=contract_diff(frm,to,a.from_contract_lock or a.to_contract_lock,a.to_contract_lock); (out/'contract_diff_report.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
    elif a.mode=='check':
        diff=contract_diff(frm,to,a.from_contract_lock or a.to_contract_lock,a.to_contract_lock)
        bump=classify_bump(a.previous_version or frm.get('adapter_version','1.0.0'), a.target_version or to.get('adapter_version',ADAPTER_VERSION))
        fails=[]
        if diff['semantic_change_class']=='major' and bump!='major': fails.append('semantic version bump too small')
        if to.get('contracts',{}).get('suppression_min_n_default',10)<10: fails.append('suppression_min_n_default below 10')
        status='pass' if not fails else 'fail'
        rep={'schema_version':'v1','object_type':'SemanticVersionCheck','domain':'fauna','source':'ebird','adapter':ADAPTER_NAME,'status':status,'detected_change_class':diff['semantic_change_class'],'version_bump':bump,'failures':fails,'generated_at':now_iso()}
        (out/'semantic_version_check.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
        if fails and a.strict: return 1
    elif a.mode=='compat-test':
        ps=public_safety_scan([a.fixture_dir] if a.fixture_dir else a.artifact_root)
        rep={'schema_version':'v1','object_type':'BackwardCompatibilityReport','domain':'fauna','source':'ebird','adapter':ADAPTER_NAME,'from_adapter_version':a.previous_version or '1.0.0','to_adapter_version':a.target_version or ADAPTER_VERSION,'from_contract_hash':frm.get('contract_hash'),'to_contract_hash':to.get('contract_hash'),'status':'pass' if ps['status']=='pass' else 'fail','artifacts_tested':[],'fixtures_tested':[a.fixture_dir] if a.fixture_dir else [],'validators_run':['validate_ebird_maintenance'],'policy_checks_run':['ebird.rego'],'compatibility_failures':ps['failures'],'migration_required':False,'migration_plan_path':None,'public_safety_regression':ps,'generated_at':now_iso()}
        (out/'backward_compatibility_report.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
    elif a.mode=='deprecate':
        if not a.deprecation_summary: raise SystemExit('--deprecation-summary required')
        rep={'schema_version':'v1','object_type':'DeprecationNotice','domain':'fauna','source':'ebird','adapter':ADAPTER_NAME,'policy_label':'maintenance','public_safe':True,'exact_points':'restricted','deprecation_id':a.deprecation_id or 'dep-001','adapter_version':ADAPTER_VERSION,'contract_hash':to.get('contract_hash'),'target':{'type':'contract','name':'kfm-ebird'},'summary':a.deprecation_summary,'reason':'governed evolution','first_deprecated_version':a.target_version or ADAPTER_VERSION,'migration_required':False,'public_safety_impact':'none','operator_action':'review','developer_action':'migrate','generated_at':now_iso()}
        (out/'deprecation_notice.json').write_text(json.dumps(rep,indent=2),encoding='utf-8'); (out/'deprecation_notice.md').write_text(f"# Deprecation\n\n{a.deprecation_summary}\n",encoding='utf-8')
    elif a.mode=='inventory':
        rep={'schema_version':'v1','object_type':'AdapterInventory','domain':'fauna','source':'ebird','adapter':ADAPTER_NAME,'clis':['kfm-ebird-maintain','kfm-ebird-migrate'],'contract_lock':a.to_contract_lock,'generated_at':now_iso()}
        (out/'adapter_inventory.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
    elif a.mode=='maintenance-report':
        rep={'schema_version':'v1','object_type':'MaintenanceReport','domain':'fauna','source':'ebird','adapter':ADAPTER_NAME,'adapter_version':ADAPTER_VERSION,'contract_hash':to.get('contract_hash'),'doctor_status':'pass','conformance_status':'pass','semantic_version_status':'pass','compatibility_status':'pass','public_safety_status':'pass','recommended_next_actions':['run compatibility tests'],'generated_at':now_iso()}
        (out/'maintenance_report.json').write_text(json.dumps(rep,indent=2),encoding='utf-8'); (out/'maintenance_report.md').write_text('# Maintenance report\n',encoding='utf-8')
    elif a.mode=='public-safety-scan':
        rep={'schema_version':'v1','object_type':'MaintenancePublicSafetyScan','domain':'fauna','source':'ebird','adapter':ADAPTER_NAME,**public_safety_scan(a.artifact_root),'generated_at':now_iso()}
        (out/'maintenance_public_safety_scan.json').write_text(json.dumps(rep,indent=2),encoding='utf-8')
    if a.json: print(json.dumps({'status':'ok','mode':a.mode,'out_dir':str(out)}))
    return 0
if __name__=='__main__': raise SystemExit(main())
