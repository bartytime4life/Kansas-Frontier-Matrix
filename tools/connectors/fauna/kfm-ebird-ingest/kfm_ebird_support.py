#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, hashlib
from pathlib import Path
from kfm_ebird_contract import canonical_json, now_iso, version_payload


def hashf(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def emit(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2),encoding='utf-8')

def main(argv=None):
  import sys
  argv=list(sys.argv[1:] if argv is None else argv)
  if '--version' in argv:
    print(json.dumps(version_payload('kfm-ebird-support', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
  ap=argparse.ArgumentParser(prog='kfm-ebird-support')
  ap.add_argument('--mode',default='build',choices=['build','validate','ticket-template','correction','takedown','playbook','report'])
  ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
  ap.add_argument('--certification-packet'); ap.add_argument('--governance-signoff'); ap.add_argument('--public-portal-manifest'); ap.add_argument('--public-download-manifest')
  ap.add_argument('--release-index',default='data/published/fauna/ebird/releases/latest.json'); ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird')
  ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true')
  a=ap.parse_args(argv)
  payload={'aggregate_targets':[a.aggregate],'kfm_spec_hashes':['sha256:synthetic'],'certification_packet_sha256':hashf(a.certification_packet) if a.certification_packet and Path(a.certification_packet).exists() else None}
  sid=hashlib.sha256(canonical_json(payload).encode()).hexdigest()[:16]
  out=Path(a.out_dir or f'{a.catalog_root}/support/{sid}'); pub=Path(a.public_out_dir or f'{a.published_root}/support/{sid}')
  if out.exists() and not (a.force or a.dry_run): raise SystemExit('output exists; pass --force')
  if a.dry_run: return 0
  pack={'schema_version':'v1','object_type':'EbirdSupportWorkflowPack','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'support','exact_points':'restricted','support_pack_id':sid,'aggregate_targets':[a.aggregate],'kfm_spec_hashes':['sha256:synthetic'],'workflows':[{'workflow_id':'correction','name':'data correction request','trigger':'public report','intake_fields':['public_artifact_uri','description'],'triage_steps':['validate'], 'validation_steps':['scan'], 'operator_actions':['review'], 'public_response_template':'received', 'escalation_path_role_only':['operations'], 'prohibited_actions':['publish_restricted']}],'generated_at':now_iso()}
  emit(out/'support_workflow_pack.json',pack); (out/'support_workflow_pack.md').write_text('# Support Workflow Pack\n',encoding='utf-8')
  (out/'operator_playbook.md').write_text('how to validate a report\nhow to run public-safety scan\nhow to run certification validate\nhow to open an incident\nhow to rollback latest pointer\nhow to disable a download link safely\nhow to update public notices\nhow to preserve audit trails\nwhat not to do\n',encoding='utf-8')
  emit(pub/'public_correction_request_workflow.json',{'schema_version':'v1','object_type':'PublicEbirdCorrectionRequestWorkflow','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','support_pack_id':sid,'purpose':'request corrections','intake_fields':{'requester_contact_optional':True,'public_artifact_uri':'','layer_id':'','feature_id_optional':True,'indicator_id_optional':True,'evidence_bundle_uri_optional':True,'kfm_spec_hash_optional':True,'description':'','correction_type':''},'correction_types':['citation','rights','stale_link','checksum','public_text','data_dictionary','aggregate_metadata','evidence_drawer','analytics_interpretation'],'do_not_submit':['exact_private_locations','credentials','private personal data','raw eBird files'],'expected_review_steps':['triage','validate'],'public_safety_notice':'no exact coordinates','generated_at':now_iso()})
  emit(pub/'public_takedown_request_workflow.json',{'schema_version':'v1','object_type':'PublicEbirdTakedownRequestWorkflow','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','support_pack_id':sid,'purpose':'request takedown','intake_fields':{'requester_contact_optional':True,'public_artifact_uri':'','reason':'','evidence':'','urgency':''},'reason_categories':['public_safety','rights_or_citation','suspected_restricted_data','sensitive_species_concern','checksum_or_integrity','unsupported_claim','other'],'immediate_operator_checks':['exact_coordinate_scan','restricted_path_scan','suppression_receipt_scan','suppressed_group_hash_scan','secret_scan','rollback_readiness'],'public_safety_notice':'no exact coordinates','generated_at':now_iso()})
  return 0

if __name__=='__main__': raise SystemExit(main())
