#!/usr/bin/env python
import argparse,sys
from pathlib import Path
from cutover_common import *
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--cutover-dir',required=True);p.add_argument('--ledger',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--notice-type',default='fixture_cutover_summary');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 n={'schema_version':'v1','notice_id':'nt-'+h({'t':TS(a.as_of)})[:12],'domain':'atmosphere.air','created_at':TS(a.as_of),'as_of':TS(a.as_of),'notice_type':a.notice_type,'audience':['internal-governance'],'subject_refs':['release_ledger_manifest.json'],'evidence_refs':['post_deploy_gate_evaluation.json'],'message_summary':'Fixture cutover summary draft only.','public_safe_links':['release_ledger_manifest.json'],'redactions':['sensitive values removed'],'forbidden_actions':['no_external_delivery'],'status':'draft_fixture'}
 if scan(n): print('DENY notice'); sys.exit(1)
 if not a.dry_run: wj(Path(a.out_dir)/'stakeholder_notice_draft.json',n)
 print('PASS notice-draft')
