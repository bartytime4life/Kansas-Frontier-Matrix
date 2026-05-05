#!/usr/bin/env python
import argparse,sys
from pathlib import Path
from cutover_common import *
def main():
 p=argparse.ArgumentParser();
 p.add_argument('--cutover-observation',required=True);p.add_argument('--authorization-dir',required=True);p.add_argument('--deployment-readiness-dir',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--ops-dir',action='append',default=[]);p.add_argument('--as-of');p.add_argument('--allow-fixture-gates',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 if not a.allow_fixture_gates: return 1
 o=J(a.cutover_observation)
 hard=[]
 for f in ['deployment_authorization.json','release_manager_decision.json','deployment_execution_receipt.json','post_deploy_verification_report.json']:
  if not (Path(a.authorization_dir)/f).exists(): hard.append('missing '+f)
 if o.get('observed_environment')=='production': hard.append('production blocked')
 result='pass_fixture' if not hard else 'deny'
 g={'schema_version':'v1','gate_evaluation_id':'gate-'+h({'o':a.cutover_observation,'t':TS(a.as_of)})[:12],'domain':'atmosphere.air','generated_at':TS(a.as_of),'as_of':TS(a.as_of),'cutover_observation_ref':'cutover_observation_record.json','deployment_authorization_ref':'deployment_authorization.json','deployment_execution_receipt_ref':'deployment_execution_receipt.json','post_deploy_verification_report_ref':'post_deploy_verification_report.json','synthetic_probe_report_ref':'synthetic_probe_report.json','public_slo_report_refs':['public_slo_report.json'],'incident_record_refs':[],'gates':[{'name':'authorization present','pass':not any('deployment_authorization' in x for x in hard)}],'hard_failures':hard,'warnings':[],'result':result}
 if scan(g): g['hard_failures'].append('unsafe content'); g['result']='deny'
 if not a.dry_run:
  od=Path(a.out_dir);od.mkdir(parents=True,exist_ok=True); wj(od/'post_deploy_gate_evaluation.json',g)
  (od/'cutover_events.jsonl').write_text(js({'schema_version':'v1','event_id':'evt-'+g['gate_evaluation_id'],'domain':'atmosphere.air','event_type':'post_deploy_gates_evaluated','created_at':TS(a.as_of),'as_of':TS(a.as_of),'actor':'fixture-non-production-actor','subject_refs':['post_deploy_gate_evaluation.json'],'evidence_refs':['cutover_observation_record.json'],'result':'pass' if g['result'].startswith('pass') else 'deny','details':{}})+'\n')
 print(('PASS' if result.startswith('pass') else 'DENY'),'post_deploy_gates'); return 0 if result.startswith('pass') else 1
if __name__=='__main__': sys.exit(main())
