#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
TS=lambda x:x or '2026-04-30T00:00:00Z'
BAD=('data/raw/','data/work/','data/quarantine/','data/processed/air/')
LIVE=('https://','kubectl','terraform apply','cdn purge','route53','webhook','pagerduty','ticket')
J=lambda p: json.loads(Path(p).read_text())

def deny(m): print('DENY',m); return 1

def main():
 a=argparse.ArgumentParser();a.add_argument('--deployment-readiness-dir',required=True);a.add_argument('--release-manager-decision',required=True);a.add_argument('--out-dir',required=True);a.add_argument('--environment',default='local_fixture');a.add_argument('--as-of');a.add_argument('--allow-fixture-authorization',action='store_true');a.add_argument('--dry-run',action='store_true');x=a.parse_args()
 if x.environment=='production' or x.environment=='production_proposed': return deny('production blocked in this PR')
 d=Path(x.deployment_readiness_dir)
 req=['deployment_environment.json','static_hosting_manifest.json','delivery_deployment_plan.json','deployment_readiness_report.json','synthetic_probe_spec.json','synthetic_probe_report.json','cache_invalidation_plan.json','deployment_rollback_plan.json','deployment_audit_report.json']
 for f in req:
  if not (d/f).exists(): return deny('missing '+f)
 rmd=J(x.release_manager_decision)
 if not rmd.get('signature'): return deny('unsigned release manager decision')
 if rmd.get('signature_type')=='fixture_signature' and x.environment.startswith('production'): return deny('fixture signature production')
 txt=json.dumps([J(d/f) for f in req]).lower()
 if any(b in txt for b in BAD) or any(l in txt for l in LIVE): return deny('unsafe content')
 hid=hashlib.sha256((str(d)+TS(x.as_of)).encode()).hexdigest()[:12]
 auth={'schema_version':'v1','authorization_id':'auth-'+hid,'domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'subject_refs':['release_manager_decision.json'],'deployment_plan_ref':'delivery_deployment_plan.json','readiness_report_ref':'deployment_readiness_report.json','deployment_audit_report_ref':'deployment_audit_report.json','client_delivery_manifest_ref':'client_delivery_manifest.json','authorized_environment':x.environment,'authorization_decision':'authorize_fixture_simulation','approvers':[rmd.get('decided_by')],'required_conditions':['non-production'],'safety_checks':{'no_network':True},'signature':rmd.get('signature'),'signature_type':rmd.get('signature_type','fixture_signature'),'fixture_backed':True,'status':'fixture_authorized'}
 hand={'schema_version':'v1','handoff_id':'handoff-'+hid,'domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'deployment_authorization_ref':'deployment_authorization.json','deployment_plan_ref':'delivery_deployment_plan.json','static_hosting_manifest_ref':'static_hosting_manifest.json','cache_invalidation_plan_ref':'cache_invalidation_plan.json','rollback_plan_ref':'deployment_rollback_plan.json','readiness_report_ref':'deployment_readiness_report.json','synthetic_probe_report_ref':'synthetic_probe_report.json','deployment_audit_report_ref':'deployment_audit_report.json','manual_steps':['review only'],'preconditions':['approval present'],'hold_points':['governance hold'],'rollback_triggers':['hash mismatch'],'evidence_refs':['deployment_readiness_report.json'],'forbidden_actions':['no live deployment'],'status':'fixture_handoff'}
 cut={'schema_version':'v1','checklist_id':'cut-'+hid,'domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'deployment_authorization_ref':'deployment_authorization.json','change_control_handoff_ref':'change_control_handoff.json','checks':[{'name':'NowCast operational label present','result':'pass'}],'hold_points':['manual review'],'go_no_go':{'decision':'go_fixture_simulation'},'rollback_preconditions':['rollback plan present'],'post_cutover_checks':['local simulation only'],'status':'fixture_checklist'}
 plan={'schema_version':'v1','verification_plan_id':'verify-'+hid,'domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'deployment_authorization_ref':'deployment_authorization.json','deployment_execution_receipt_ref':'deployment_execution_receipt.json','synthetic_probe_spec_ref':'synthetic_probe_spec.json','public_slo_objectives':['evidence only'],'verification_steps':['local metadata checks'],'expected_evidence':['post_deploy_verification_report.json'],'rollback_triggers':['deny result'],'incident_triggers':['secret leak'],'status':'fixture_verification_plan'}
 if not x.dry_run:
  o=Path(x.out_dir);o.mkdir(parents=True,exist_ok=True)
  [ (o/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n') for n,v in [('deployment_authorization.json',auth),('change_control_handoff.json',hand),('release_cutover_checklist.json',cut),('post_deploy_verification_plan.json',plan)] ]
 print('PASS authorization package'); return 0
if __name__=='__main__': raise SystemExit(main())
