#!/usr/bin/env python
import argparse,sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'deployments'/'air'))
from cutover_common import J,TS,wj,h,etag,scan
# simplified fixture-only builder
# ...
def main():
 p=argparse.ArgumentParser();[p.add_argument(x,required=True) for x in ('--cutover-dir','--authorization-dir','--deployment-readiness-dir','--delivery-dir','--out-dir')];p.add_argument('--ops-dir',action='append',default=[]);p.add_argument('--as-of');p.add_argument('--allow-fixture-handoff',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();cd=Path(a.cutover_dir);od=Path(a.out_dir)
 for r in ['cutover_observation_record.json','post_deploy_gate_evaluation.json','release_ledger_manifest.json','operational_acceptance_record.json','rollback_decision_record.json']:
  if not (cd/r).exists(): print('DENY'); return 1
 if J(cd/'post_deploy_gate_evaluation.json').get('result') in ('deny','blocked'): print('DENY'); return 1
 out={"schema_version":"1.0.0","handoff_package_id":f"handoff-{h({'as_of':TS(a.as_of)})[:12]}","domain":"atmosphere.air","created_at":TS(a.as_of),"as_of":TS(a.as_of),"cutover_observation_ref":str(cd/'cutover_observation_record.json'),"post_deploy_gate_evaluation_ref":str(cd/'post_deploy_gate_evaluation.json'),"release_ledger_manifest_ref":str(cd/'release_ledger_manifest.json'),"operational_acceptance_ref":str(cd/'operational_acceptance_record.json'),"rollback_decision_ref":str(cd/'rollback_decision_record.json'),"deployment_authorization_ref":str(Path(a.authorization_dir)/'deployment_authorization.json'),"client_delivery_manifest_ref":str(Path(a.delivery_dir)/'client_delivery_manifest.json'),"handoff_recipients":[{"label":"fixture-non-production-recipient"}],"responsibilities":["local-only"],"evidence_refs":[str(cd/'release_ledger_manifest.json')],"open_risks":[],"required_followups":[],"safety_checks":[{"name":"no_live_ops","pass":True}],"status":"fixture_handoff_candidate"}
 if scan(out): print('DENY'); return 1
 plan={"schema_version":"1.0.0","watch_plan_id":"watch-plan-"+h(out)[:12],"domain":"atmosphere.air","created_at":TS(a.as_of),"as_of":TS(a.as_of),"operational_handoff_package_ref":str(od/'operational_handoff_package.json'),"post_deploy_gate_evaluation_ref":str(cd/'post_deploy_gate_evaluation.json'),"public_slo_objectives":["local fixture checks"],"watch_window":{"mode":"fixture","minutes":60},"local_checks":["hashes","etags"],"incident_thresholds":["critical unresolved denies"],"rollback_thresholds":["warn+incident requires rollback"],"evidence_refs":[str(cd/'release_ledger_manifest.json')],"forbidden_actions":["no live endpoint probes"],"status":"fixture_watch_plan"}
 runbook={"schema_version":"1.0.0","runbook_activation_id":"runbook-"+h(plan)[:12],"domain":"atmosphere.air","created_at":TS(a.as_of),"as_of":TS(a.as_of),"operational_handoff_package_ref":str(od/'operational_handoff_package.json'),"watch_window_plan_ref":str(od/'watch_window_plan.json'),"release_ledger_manifest_ref":str(cd/'release_ledger_manifest.json'),"runbook_sections":["local review"],"roles":["fixture-ops-non-production"],"local_procedures":["read generated artifacts"],"forbidden_actions":["kubectl","terraform apply"],"evidence_refs":[str(cd/'rollback_decision_record.json')],"status":"fixture_runbook_candidate"}
 evt={"schema_version":"1.0.0","event_id":"evt-"+h(out)[:12],"domain":"atmosphere.air","event_type":"operational_handoff_created","created_at":TS(a.as_of),"as_of":TS(a.as_of),"actor":"fixture-operator-non-production","subject_refs":[str(od/'operational_handoff_package.json')],"evidence_refs":out['evidence_refs'],"result":"pass","details":{"etag":etag(h(out))}}
 if not a.dry_run:
  od.mkdir(parents=True,exist_ok=True);wj(od/'operational_handoff_package.json',out);wj(od/'watch_window_plan.json',plan);wj(od/'runbook_activation_candidate.json',runbook);(od/'operational_handoff_events.jsonl').write_text(json.dumps(evt,sort_keys=True)+'\n')
 print('PASS');return 0
if __name__=='__main__': raise SystemExit(main())
