#!/usr/bin/env python
import argparse,sys
from pathlib import Path
from cutover_common import *
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--cutover-dir',required=True);p.add_argument('--ledger',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--signature',default='fixture-signature');p.add_argument('--signature-type',default='fixture_signature');p.add_argument('--accepted-by',default='fixture-operator');p.add_argument('--role',default='release_manager');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 g=J(Path(a.cutover_dir)/'post_deploy_gate_evaluation.json')
 if not a.fixture_only or not g['result'].startswith('pass'): print('DENY acceptance'); sys.exit(1)
 rec={'schema_version':'v1','acceptance_id':'acc-'+h({'t':TS(a.as_of)})[:12],'domain':'atmosphere.air','created_at':TS(a.as_of),'as_of':TS(a.as_of),'cutover_observation_ref':'cutover_observation_record.json','post_deploy_gate_evaluation_ref':'post_deploy_gate_evaluation.json','release_ledger_manifest_ref':str(Path(a.ledger).name),'accepted_environment':'local_fixture','acceptance_decision':'accept_fixture_operation','acceptance_conditions':['non-production only'],'required_followups':['manual review'],'evidence_refs':['post_deploy_gate_evaluation.json'],'signature':a.signature,'signature_type':a.signature_type,'fixture_backed':True,'status':'fixture_accepted'}
 if not a.dry_run: wj(Path(a.out_dir)/'operational_acceptance_record.json',rec)
 print('PASS acceptance')
