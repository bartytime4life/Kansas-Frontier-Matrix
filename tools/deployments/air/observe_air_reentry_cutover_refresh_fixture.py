#!/usr/bin/env python
from cutover_common import *
import argparse,sys
from pathlib import Path

req=['reentry_release_manager_refresh_decision.json','reentry_deployment_authorization_refresh.json','reentry_change_control_handoff_refresh.json','reentry_release_cutover_checklist_refresh.json','reentry_local_deployment_refresh_simulation.json','reentry_deployment_refresh_execution_receipt.json','reentry_post_deploy_verification_refresh_report.json','reentry_deployment_authorization_refresh_postcheck_report.json','reentry_deployment_authorization_refresh_audit_report.json','reentry_deployment_authorization_refresh_ledger_manifest.json']
def main():
 p=argparse.ArgumentParser();p.add_argument('--deployment-authorization-refresh-dir',action='append',default=[]);p.add_argument('--deployment-readiness-refresh-dir',action='append',default=[]);p.add_argument('--client-delivery-refresh-dir',action='append',default=[]);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--observation-mode',default='fixture_refresh_simulation');p.add_argument('--allow-fixture-observation',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 if (not a.allow_fixture_observation) or 'data/published/air/' in a.out_dir.lower(): return 1
 ad=Path(a.deployment_authorization_refresh_dir[0])
 miss=[f for f in req if not (ad/f).exists()]
 if miss: print('DENY missing',','.join(miss)); return 1
 o={'schema_version':'v1','observation_id':'obs-'+h({'ad':str(ad),'t':TS(a.as_of)})[:12],'domain':'atmosphere.air','created_at':TS(a.as_of),'as_of':TS(a.as_of),'deployment_authorization_refresh_ref':str(ad/'reentry_deployment_authorization_refresh.json'),'release_manager_refresh_decision_ref':str(ad/'reentry_release_manager_refresh_decision.json'),'change_control_handoff_refresh_ref':str(ad/'reentry_change_control_handoff_refresh.json'),'release_cutover_checklist_refresh_ref':str(ad/'reentry_release_cutover_checklist_refresh.json'),'deployment_refresh_execution_receipt_ref':str(ad/'reentry_deployment_refresh_execution_receipt.json'),'post_deploy_verification_refresh_report_ref':str(ad/'reentry_post_deploy_verification_refresh_report.json'),'deployment_authorization_refresh_postcheck_report_ref':str(ad/'reentry_deployment_authorization_refresh_postcheck_report.json'),'deployment_authorization_refresh_audit_report_ref':str(ad/'reentry_deployment_authorization_refresh_audit_report.json'),'deployment_authorization_refresh_ledger_manifest_ref':str(ad/'reentry_deployment_authorization_refresh_ledger_manifest.json'),'observed_environment':'local_fixture','observation_mode':a.observation_mode,'observations':[{'summary':'fixture-only refresh observation'}],'evidence_refs':[],'safety_checks':{'fixture_backed':True,'non_production':True},'status':'fixture_observed'}
 if scan(o): return 1
 if not a.dry_run:
  od=Path(a.out_dir);od.mkdir(parents=True,exist_ok=True);wj(od/'reentry_cutover_observation_refresh_record.json',o)
  (od/'reentry_cutover_observation_refresh_events.jsonl').write_text(js({'schema_version':'v1','event_id':'evt-'+o['observation_id'],'domain':'atmosphere.air','event_type':'cutover_observation_refresh_created','created_at':TS(a.as_of),'as_of':TS(a.as_of),'actor':'fixture-non-production-operator','subject_refs':['reentry_cutover_observation_refresh_record.json'],'evidence_refs':[],'result':'pass','details':{}})+'\n')
 print('PASS');return 0
if __name__=='__main__':sys.exit(main())
