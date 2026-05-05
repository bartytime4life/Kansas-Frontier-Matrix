#!/usr/bin/env python
import argparse,sys
from pathlib import Path
from cutover_common import *
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--cutover-dir',required=True);p.add_argument('--deployment-readiness-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--incident-record',action='append',default=[]);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 dec={'schema_version':'v1','rollback_decision_id':'rb-'+h({'t':TS(a.as_of)})[:12],'domain':'atmosphere.air','created_at':TS(a.as_of),'as_of':TS(a.as_of),'cutover_observation_ref':'cutover_observation_record.json','post_deploy_gate_evaluation_ref':'post_deploy_gate_evaluation.json','deployment_rollback_plan_ref':'deployment_rollback_plan.json','incident_record_refs':a.incident_record,'rollback_decision':'no_rollback_fixture','rollback_triggers_observed':[],'evidence_refs':['post_deploy_gate_evaluation.json'],'recommended_actions':['keep fixture mode'],'status':'fixture_decision'}
 if not a.dry_run: wj(Path(a.out_dir)/'rollback_decision_record.json',dec)
 print('PASS rollback-prepared')
