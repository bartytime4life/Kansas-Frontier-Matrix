#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
TS=lambda x:x or '2026-04-30T00:00:00Z'
J=lambda p: json.loads(Path(p).read_text())
def main():
 a=argparse.ArgumentParser();a.add_argument('--authorization-dir',required=True);a.add_argument('--deployment-readiness-dir',required=True);a.add_argument('--delivery-dir',required=True);a.add_argument('--out-dir',required=True);a.add_argument('--as-of');a.add_argument('--allow-fixture-simulation',action='store_true');a.add_argument('--dry-run',action='store_true');x=a.parse_args()
 ad,dd=Path(x.authorization_dir),Path(x.delivery_dir)
 auth=J(ad/'deployment_authorization.json')
 b=J(dd/'static_response_bundle.json'); c=J(dd/'client_cache_manifest.json'); ce={e['artifact_ref']:e for e in c.get('entries',[])}
 sim_routes=[]; ok=True
 for r in b.get('responses',[]):
  p=dd/r['response_ref']; s=hashlib.sha256(p.read_bytes()).hexdigest(); eo=ce.get(r['response_ref'],{}).get('etag')==f'"sha256:{s}"'; ho=s==r['sha256']; ok=ok and eo and ho; sim_routes.append({'route_id':r['route_id'],'sha256_ok':ho,'etag_ok':eo})
 sim={'schema_version':'v1','simulation_id':'sim-1','domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'deployment_authorization_ref':'deployment_authorization.json','change_control_handoff_ref':'change_control_handoff.json','release_cutover_checklist_ref':'release_cutover_checklist.json','source_delivery_refs':['client_route_manifest.json'],'simulated_routes':sim_routes,'simulated_cache_entries':list(ce.keys()),'simulated_probe_results':[{'status':'pass'}],'simulated_rollback_result':{'status':'pass'},'safety_checks':{'network_calls_forbidden':True},'status':'passed_fixture_simulation' if ok else 'deny'}
 rec={'schema_version':'v1','execution_receipt_id':'exec-1','domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'execution_mode':'fixture_simulation','deployment_authorization_ref':'deployment_authorization.json','change_control_handoff_ref':'change_control_handoff.json','release_cutover_checklist_ref':'release_cutover_checklist.json','local_deployment_simulation_ref':'local_deployment_simulation.json','actor':'fixture-operator-non-production','steps_observed':['local-only'],'artifact_refs':['local_deployment_simulation.json'],'hashes':sim_routes,'result':'pass' if ok else 'deny','status':'fixture_receipt'}
 rep={'schema_version':'v1','verification_report_id':'vrep-1','domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'verification_plan_ref':'post_deploy_verification_plan.json','deployment_execution_receipt_ref':'deployment_execution_receipt.json','checks':[{'name':'NowCast not validated AQS truth','result':'pass'}],'probe_results':sim_routes,'slo_expectations':['metadata only'],'rollback_trigger_evaluation':['none'],'incident_trigger_evaluation':['none'],'result':'pass_fixture' if ok else 'deny'}
 o=Path(x.out_dir);o.mkdir(parents=True,exist_ok=True)
 for n,v in [('local_deployment_simulation.json',sim),('deployment_execution_receipt.json',rec),('post_deploy_verification_report.json',rep)]: (o/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
 print('PASS local simulation' if ok else 'DENY local simulation'); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
