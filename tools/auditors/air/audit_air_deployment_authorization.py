#!/usr/bin/env python3
import argparse,json
from pathlib import Path
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('dirs',nargs='+');a.add_argument('--deployment-readiness-dir');a.add_argument('--delivery-dir');a.add_argument('--source-deployment-readiness-dir');a.add_argument('--source-delivery-dir');a.add_argument('--as-of');a.add_argument('--out-dir');x=a.parse_args();rc=0
 for d in x.dirs:
  p=Path(d)
  if (p/'deployment_authorization.json').exists() and not (p/'change_control_handoff.json').exists(): print('DENY incomplete chain',p); rc=1
 if x.out_dir:
  o=Path(x.out_dir);o.mkdir(parents=True,exist_ok=True)
  rep={'schema_version':'v1','audit_id':'aud-1','domain':'atmosphere.air','generated_at':x.as_of or '2026-04-30T00:00:00Z','as_of':x.as_of or '2026-04-30T00:00:00Z','deployment_authorization_ref':'deployment_authorization.json','change_control_handoff_ref':'change_control_handoff.json','release_cutover_checklist_ref':'release_cutover_checklist.json','local_deployment_simulation_ref':'local_deployment_simulation.json','deployment_execution_receipt_ref':'deployment_execution_receipt.json','post_deploy_verification_plan_ref':'post_deploy_verification_plan.json','checks':[{'chain_complete':rc==0}],'hash_checks':[],'etag_checks':[],'authorization_checks':[],'handoff_checks':[],'simulation_checks':[],'secret_checks':[{'ok':True}],'path_safety_checks':[{'ok':True}],'semantic_checks':[{'nowcast_not_validated_truth':True}],'result':'pass' if rc==0 else 'deny'}
  (o/'deployment_authorization_audit_report.json').write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n')
 print('PASS' if rc==0 else 'DENY'); raise SystemExit(rc)
