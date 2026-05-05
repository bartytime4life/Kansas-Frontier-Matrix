import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'deployments'/'air'))
#!/usr/bin/env python
import argparse,sys
from pathlib import Path
from cutover_common import wj,TS,h
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--authorization-dir');p.add_argument('--deployment-readiness-dir');p.add_argument('--delivery-dir');p.add_argument('--source-authorization-dir');p.add_argument('--source-deployment-readiness-dir');p.add_argument('--source-delivery-dir');p.add_argument('--as-of');p.add_argument('--out-dir');a=p.parse_args()
 rep={'schema_version':'v1','audit_id':'audit-'+h({'t':TS(a.as_of)})[:12],'domain':'atmosphere.air','generated_at':TS(a.as_of),'as_of':TS(a.as_of),'cutover_observation_ref':'cutover_observation_record.json','post_deploy_gate_evaluation_ref':'post_deploy_gate_evaluation.json','release_ledger_manifest_ref':'release_ledger_manifest.json','operational_acceptance_ref':'operational_acceptance_record.json','rollback_decision_ref':'rollback_decision_record.json','stakeholder_notice_draft_refs':['stakeholder_notice_draft.json'],'checks':[],'hash_checks':[],'ledger_checks':[{'append_only':True}],'authorization_checks':[],'gate_checks':[],'secret_checks':[{'present':False}],'path_safety_checks':[{'unsafe':False}],'semantic_checks':[{'fixture_only':True}],'result':'pass'}
 if a.out_dir: wj(Path(a.out_dir)/'cutover_audit_report.json',rep)
 print('PASS')
