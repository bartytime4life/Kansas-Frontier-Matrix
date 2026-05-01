#!/usr/bin/env python
import argparse,sys
from pathlib import Path
from cutover_common import *
def main():
 p=argparse.ArgumentParser();
 p.add_argument('--cutover-dir',required=True);p.add_argument('--authorization-dir',required=True);p.add_argument('--deployment-readiness-dir',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--previous-ledger');p.add_argument('--as-of');p.add_argument('--allow-fixture-ledger',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 if not a.allow_fixture_ledger: return 1
 cd=Path(a.cutover_dir);obs=J(cd/'cutover_observation_record.json') if (cd/'cutover_observation_record.json').exists() else None;g=J(cd/'post_deploy_gate_evaluation.json')
 if not obs: print('DENY missing cutover'); return 1
 entries=[];prev=''
 for etype,sub,res in [('authorization_recorded',['deployment_authorization.json'],'pass'),('cutover_observed',['cutover_observation_record.json'],'pass'),('post_deploy_gates_evaluated',['post_deploy_gate_evaluation.json'],'pass' if g['result'].startswith('pass') else 'deny')]:
  core={'schema_version':'v1','ledger_entry_id':'le-'+h({'t':TS(a.as_of),'e':etype,'p':prev})[:12],'domain':'atmosphere.air','created_at':TS(a.as_of),'as_of':TS(a.as_of),'entry_type':etype,'actor':'fixture-non-production-actor','subject_refs':sub,'evidence_refs':['deployment_authorization.json'],'artifact_hashes':{},'previous_entry_ref':prev,'result':res,'details':{'fixture_backed':True}}
  core['entry_hash']=h(core); prev=core['ledger_entry_id']; entries.append(core)
 chain=h([e['entry_hash'] for e in entries])
 m={'schema_version':'v1','ledger_id':'ledger-'+h({'t':TS(a.as_of)})[:12],'domain':'atmosphere.air','generated_at':TS(a.as_of),'as_of':TS(a.as_of),'entry_refs':[e['ledger_entry_id'] for e in entries],'head_entry_ref':entries[-1]['ledger_entry_id'],'chain_hash':chain,'source_refs':['cutover_observation_record.json','post_deploy_gate_evaluation.json'],'safety_checks':{'append_only':True},'status':'fixture_ledger'}
 if not a.dry_run:
  od=Path(a.out_dir);od.mkdir(parents=True,exist_ok=True); (od/'release_ledger_entries.jsonl').write_text('\n'.join(js(e) for e in entries)+'\n'); wj(od/'release_ledger_manifest.json',m)
 print('PASS ledger'); return 0
if __name__=='__main__': sys.exit(main())
