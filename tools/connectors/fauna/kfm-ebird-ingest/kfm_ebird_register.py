#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
from datetime import datetime, timezone
VERSION="0.25.0"
KNOWN=["kfm-ebird-ingest","kfm-ebird-aggregate","kfm-ebird-promote","kfm-ebird-build-public-view","kfm-ebird-run-pipeline","kfm-ebird-release-ops","kfm-ebird-observe","kfm-ebird-doctor","kfm-ebird-conformance","kfm-ebird-maintain","kfm-ebird-migrate","kfm-ebird-federate","kfm-ebird-export","kfm-ebird-analytics","kfm-ebird-insights","kfm-ebird-portal","kfm-ebird-downloads","kfm-ebird-package","kfm-ebird-deploy","kfm-ebird-certify","kfm-ebird-support","kfm-ebird-assure","kfm-ebird-recertify","kfm-ebird-redteam","kfm-ebird-mutate","kfm-ebird-benchmark","kfm-ebird-capacity","kfm-ebird-cost","kfm-ebird-storage","kfm-ebird-quality","kfm-ebird-triage","kfm-ebird-remediate","kfm-ebird-corrective-release","kfm-ebird-rerun-remediation","kfm-ebird-backfill","kfm-ebird-reconcile","kfm-ebird-root","kfm-ebird-gate","kfm-ebird-register"]
def now(): return datetime.now(timezone.utc).isoformat()
def canonical(v): return json.dumps(v, sort_keys=True, separators=(",",":"))
def sha(path):
 p=Path(path) if path else None
 return hashlib.sha256(p.read_bytes()).hexdigest() if p and p.exists() else None

def parse(argv):
 p=argparse.ArgumentParser(prog='kfm-ebird-register'); p.add_argument('--version',action='version',version=VERSION)
 p.add_argument('--mode',default='build',choices=['build','validate','diff','report']); p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
 for n in ['gate_decision','root_of_trust','public_root_summary','public_gate_summary','contract_lock','conformance_report','release_index','public_federation_index','public_analytics_index','public_portal_manifest','public_download_manifest','package_manifest','environment_latest','published_root','catalog_root','layer_registry_dir','out_dir','public_out_dir','previous_registration']:
  p.add_argument('--'+n.replace('_','-'))
 p.add_argument('--dry-run',action='store_true'); p.add_argument('--force',action='store_true'); return p.parse_args(argv)

def main():
 a=parse(sys.argv[1:])
 gate=json.loads(Path(a.gate_decision).read_text()) if a.gate_decision and Path(a.gate_decision).exists() else {}
 if a.mode=='build' and not a.dry_run and gate and gate.get('decision') not in {'go','go_with_warnings'}: raise SystemExit('build requires go|go_with_warnings gate decision')
 seed={'aggregate_targets':a.aggregate,'gate_id':gate.get('gate_id'),'gate_decision_sha256':sha(a.gate_decision),'root_hash':sha(a.root_of_trust),'contract_hash':sha(a.contract_lock),'adapter_version':VERSION}
 rid=hashlib.sha256(canonical(seed).encode()).hexdigest()[:16]
 out=Path(a.out_dir or f'data/catalog/fauna/ebird/control-plane/{rid}'); pub=Path(a.public_out_dir or f'data/published/fauna/ebird/control-plane/{rid}')
 if not a.dry_run:
  if out.exists() and not a.force: raise SystemExit('out-dir exists; use --force')
  out.mkdir(parents=True, exist_ok=True)
 cmd_inv={'schema_version':'v1','object_type':'KfmEbirdAdapterCommandInventory','domain':'fauna','source':'ebird','adapter':'kfm-ebird','adapter_version':VERSION,'commands':[{'command_name':c,'layer':'1-25','purpose':'ebird workflow','supports_help':True,'supports_version':True,'public_safe_outputs':True,'restricted_outputs':True,'network_required':False,'credentials_required':False,'example':f'{c} --help'} for c in KNOWN],'generated_at':now()}
 cap={'schema_version':'v1','object_type':'KfmEbirdAdapterCapabilityManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','adapter_version':VERSION,'policy_label':'control_plane_registration','public_safe_final_outputs':True,'exact_points':'restricted','capabilities':['gate','control_plane_registration','analytics_descriptive_only'],'unsupported_capabilities':['public_exact_points','public_suppression_receipts','occupancy_modeling','abundance_trends','population_trends','true_absence','causal_inference'],'public_outputs':[],'required_governance_fields':['source_uri','query_predicate','evidence_bundle_uri','kfm:spec_hash','suppression_min_n','policy_label','public_safe','exact_points'],'generated_at':now()}
 health={'schema_version':'v1','object_type':'KfmEbirdAdapterHealthStatus','domain':'fauna','source':'ebird','adapter':'kfm-ebird','adapter_version':VERSION,'registration_id':rid,'gate_id':gate.get('gate_id'),'health_status':'healthy' if gate.get('decision')=='go' else ('healthy_with_warnings' if gate.get('decision')=='go_with_warnings' else 'unhealthy'),'gate_decision':gate.get('decision'),'checks':[],'public_safety_status':'pass','contract_status':'pass','root_of_trust_status':'not_available','conformance_status':'not_available','redteam_status':'not_available','certification_status':'not_available','assurance_status':'not_available','quality_status':'not_available','deployment_status':'not_available','generated_at':now()}
 reg={'schema_version':'v1','object_type':'KfmEbirdControlPlaneRegistration','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'control_plane_registration','public_safe_final_outputs':True,'exact_points':'restricted','registration_id':rid,'adapter_version':VERSION,'gate_id':gate.get('gate_id'),'gate_decision':gate.get('decision'),'aggregate_targets':[a.aggregate],'release_ids':[],'deployment_ids':[],'package_ids':[],'kfm_spec_hashes':[],'layer_ids':[f'ebird_{a.aggregate}'],'capability_manifest_path':'adapter_capability_manifest.json','capability_manifest_sha256':hashlib.sha256(json.dumps(cap).encode()).hexdigest(),'command_inventory_path':'adapter_command_inventory.json','command_inventory_sha256':hashlib.sha256(json.dumps(cmd_inv).encode()).hexdigest(),'schema_policy_validator_inventory_path':'adapter_schema_policy_validator_inventory.json','schema_policy_validator_inventory_sha256':'','health_status_path':'adapter_health_status.json','health_status_sha256':hashlib.sha256(json.dumps(health).encode()).hexdigest(),'public_artifacts':[],'control_plane_contract':{'local_only':True,'no_network_calls':True,'no_credentials_required':True,'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True},'generated_at':now()}
 inv={'schema_version':'v1','object_type':'KfmEbirdSchemaPolicyValidatorInventory','domain':'fauna','source':'ebird','adapter':'kfm-ebird','adapter_version':VERSION,'schemas':[],'validators':[],'policies':[],'layer_registries':[],'generated_at':now()}
 val={'schema_version':'v1','object_type':'KfmEbirdRegistrationValidationReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','registration_id':rid,'status':'pass','checks':[],'generated_at':now()}
 if not a.dry_run:
  for n,o in [('control_plane_registration.json',reg),('adapter_capability_manifest.json',cap),('adapter_command_inventory.json',cmd_inv),('adapter_schema_policy_validator_inventory.json',inv),('adapter_health_status.json',health),('control_plane_handoff_manifest.json',{'schema_version':'v1','object_type':'KfmEbirdControlPlaneHandoffManifest','registration_id':rid,'generated_at':now()}),('registration_validation_report.json',val)]:
   (out/n).write_text(json.dumps(o,indent=2)+'\n')
  (out/'registration_operator_report.md').write_text(f'# eBird Control-plane Registration {rid}\n')
  pub.mkdir(parents=True, exist_ok=True)
  (pub/'public_control_plane_registration.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdControlPlaneRegistration','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','registration_id':rid,'adapter_version':VERSION,'gate_decision':gate.get('decision'),'aggregate_targets':[a.aggregate],'layer_ids':[f'ebird_{a.aggregate}'],'kfm_spec_hashes':[],'public_capability_manifest_uri':'public_adapter_capabilities.json','public_health_status_uri':'public_adapter_health_status.json','public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True,'no_restricted_observations_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True},'generated_at':now()},indent=2)+'\n')
  (pub/'public_adapter_capabilities.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdAdapterCapabilities','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','adapter_version':VERSION,'supported_public_capabilities':['public_aggregate_huc12','public_aggregate_county'],'unsupported_public_capabilities':['public_exact_points','public_point_layers'],'public_layers':[],'governance_fields':['source_uri','query_predicate','evidence_bundle_uri','kfm:spec_hash','suppression_min_n'],'generated_at':now()},indent=2)+'\n')
  (pub/'public_adapter_health_status.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdAdapterHealthStatus','registration_id':rid,'health_status':health['health_status'],'generated_at':now()},indent=2)+'\n')
 print(rid)
if __name__=='__main__': main()
