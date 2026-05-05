#!/usr/bin/env python
import argparse,sys
from pathlib import Path
from cutover_common import *
req=['release_manager_decision.json','deployment_authorization.json','change_control_handoff.json','release_cutover_checklist.json','deployment_execution_receipt.json','post_deploy_verification_report.json','deployment_authorization_audit_report.json']
def main():
 p=argparse.ArgumentParser();
 p.add_argument('--authorization-dir',required=True);p.add_argument('--deployment-readiness-dir',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--observation-mode',default='fixture_simulation');p.add_argument('--allow-fixture-observation',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 if 'data/published/air/' in a.out_dir.lower() or not a.allow_fixture_observation: return 1
 ad=Path(a.authorization_dir)
 for f in req:
  if not (ad/f).exists(): print('DENY missing',f); return 1
 obs={'schema_version':'v1','observation_id':'obs-'+h({'a':a.authorization_dir,'t':TS(a.as_of)})[:12],'domain':'atmosphere.air','created_at':TS(a.as_of),'as_of':TS(a.as_of),'deployment_authorization_ref':'deployment_authorization.json','release_manager_decision_ref':'release_manager_decision.json','change_control_handoff_ref':'change_control_handoff.json','release_cutover_checklist_ref':'release_cutover_checklist.json','deployment_execution_receipt_ref':'deployment_execution_receipt.json','post_deploy_verification_report_ref':'post_deploy_verification_report.json','observed_environment':'local_fixture','observation_mode':a.observation_mode,'observations':[{'note':'fixture-only governed observation'}],'evidence_refs':['local_deployment_simulation.json','post_deploy_verification_report.json'],'safety_checks':{'non_production':True},'status':'fixture_observed'}
 if scan(obs): print('DENY content'); return 1
 if not a.dry_run:
  od=Path(a.out_dir); od.mkdir(parents=True,exist_ok=True); wj(od/'cutover_observation_record.json',obs)
  (od/'cutover_events.jsonl').write_text(js({'schema_version':'v1','event_id':'evt-'+obs['observation_id'],'domain':'atmosphere.air','event_type':'cutover_observation_created','created_at':TS(a.as_of),'as_of':TS(a.as_of),'actor':'fixture-non-production-actor','subject_refs':['cutover_observation_record.json'],'evidence_refs':obs['evidence_refs'],'result':'pass','details':{'mode':a.observation_mode}})+'\n')
 print('PASS cutover_observation'); return 0
if __name__=='__main__': sys.exit(main())
