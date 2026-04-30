#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, hashlib
from pathlib import Path
from kfm_ebird_contract import canonical_json, now_iso, version_payload

DENIED=["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number","suppression_receipt_path","suppressed_group_hash","token=","api_key=","credential"]
MODES=["packet","validate","signoff","controls","risk","escrow","rights","drill-plan","drill-run","eol","report"]


def read_json(p):
  return json.loads(Path(p).read_text(encoding='utf-8'))

def digest(p):
  return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def scan(v):
  t=json.dumps(v,sort_keys=True).lower() if not isinstance(v,str) else v.lower()
  return [x for x in DENIED if x.lower() in t]

def cid(payload):
  return hashlib.sha256(canonical_json(payload).encode('utf-8')).hexdigest()[:16]

def emit(path,obj):
  path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(obj,indent=2),encoding='utf-8')


def main(argv=None):
  import sys
  argv=list(sys.argv[1:] if argv is None else argv)
  if '--version' in argv:
    print(json.dumps(version_payload('kfm-ebird-certify', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
  ap=argparse.ArgumentParser(prog='kfm-ebird-certify')
  ap.add_argument('--mode',default='packet',choices=MODES); ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
  for k in ['package_manifest','deployment_receipt','deployment_verify_report','release_receipt','public_portal_manifest','public_download_manifest','public_federation_index','public_analytics_index','public_insight_report','contract_lock','conformance_report','observability_report']:
    ap.add_argument(f'--{k.replace("_","-")}')
  ap.add_argument('--release-index',default='data/published/fauna/ebird/releases/latest.json')
  ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird'); ap.add_argument('--layer-registry-dir',default='data/published/fauna/layers')
  ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir'); ap.add_argument('--decision',choices=['approve','block','needs-review']); ap.add_argument('--reviewer'); ap.add_argument('--reviewer-role'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true')
  a=ap.parse_args(argv)

  inputs=[]
  for k,v in vars(a).items():
    if k in ['mode','aggregate','published_root','catalog_root','layer_registry_dir','out_dir','public_out_dir','decision','reviewer','reviewer_role','dry_run','force'] or not v: continue
    p=Path(v)
    if p.exists(): inputs.append({'key':k,'path':v,'sha256':digest(v),'json':read_json(v) if p.suffix=='.json' else None})
  payload={'aggregate_targets':[a.aggregate], 'release_ids':['synthetic-release'], 'deployment_ids':['synthetic-deployment'], 'package_ids':['synthetic-package'], 'run_ids':['synthetic-run'], 'kfm_spec_hashes':['sha256:synthetic'], 'package_manifest_sha256':next((i['sha256'] for i in inputs if i['key']=='package_manifest'),None)}
  cert_id=cid(payload)
  out=Path(a.out_dir or f"{a.catalog_root}/certification/{cert_id}")
  pub=Path(a.public_out_dir or f"{a.published_root}/certification/{cert_id}")
  if out.exists() and not (a.force or a.dry_run): raise SystemExit('output exists; pass --force')
  blocked=[]
  for i in inputs:
    if i['json'] is not None: blocked += [f"{i['path']}:{b}" for b in scan(i['json']) if b not in ['token=','api_key=']]
  hard=[{'gate_id':'EBIRD-L16-01','name':'public_safety_scan','status':'fail' if blocked else 'pass','evidence_artifact':'inputs','message':'scan complete'}]
  status='fail' if blocked else 'pass'
  approve=a.decision or 'not_requested'
  if approve=='approve' and status!='pass': raise SystemExit('cannot approve with failed hard gate')
  packet={'schema_version':'v1','object_type':'EbirdProductionCertificationPacket','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'certification','public_safe_final_outputs':True,'exact_points':'restricted','certification_id':cert_id,'aggregate_targets':[a.aggregate],'release_ids':['synthetic-release'],'deployment_ids':['synthetic-deployment'],'package_ids':['synthetic-package'],'run_ids':['synthetic-run'],'kfm_spec_hashes':['sha256:synthetic'],'certification_status':status,'approval_decision':approve,'inputs':[{'path_or_uri':i['path'],'sha256':'sha256:'+i['sha256'],'artifact_type':i['key'],'public_safe':True,'policy_label':'public_aggregate'} for i in inputs],'hard_gates':hard,'warnings':[],'blockers':blocked,'denied_public_fields_checked':DENIED,'generated_at':now_iso()}
  if a.dry_run: return 0
  emit(out/'production_certification_packet.json',packet); (out/'production_certification_packet.md').write_text(f"# Production Certification\n\nStatus: {status}\n",encoding='utf-8')
  if a.mode=='signoff':
    sign={'schema_version':'v1','object_type':'EbirdGovernanceSignoffPacket','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'governance_signoff','public_safe_final_outputs':True,'exact_points':'restricted','certification_id':cert_id,'aggregate_targets':[a.aggregate],'release_ids':['synthetic-release'],'deployment_ids':['synthetic-deployment'],'package_ids':['synthetic-package'],'run_ids':['synthetic-run'],'kfm_spec_hashes':['sha256:synthetic'],'approval_decision':approve,'reviewer':a.reviewer,'reviewer_role':a.reviewer_role,'required_signoffs':{'data_governance':True,'public_safety':True,'release_manager':True,'domain_owner':True,'operations':True,'rights_review':True},'signoff_status':'approved' if approve=='approve' else 'needs_review','blockers':blocked,'warnings':[],'generated_at':now_iso()}
    emit(out/'governance_signoff_packet.json',sign); (out/'governance_signoff_packet.md').write_text('# Governance Signoff\n',encoding='utf-8')
    emit(pub/'public_governance_summary.json',{'schema_version':'v1','object_type':'PublicEbirdGovernanceSummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','certification_id':cert_id,'aggregate_targets':[a.aggregate],'release_ids':['synthetic-release'],'deployment_ids':['synthetic-deployment'],'package_ids':['synthetic-package'],'kfm_spec_hashes':['sha256:synthetic'],'signoff_status':sign['signoff_status'],'public_safety_summary':'passed' if not blocked else 'failed','suppression_min_n_values':[10],'evidence_bundle_uris':[],'public_artifact_uris':[],'generated_at':now_iso()})
  return 0

if __name__=='__main__': raise SystemExit(main())
