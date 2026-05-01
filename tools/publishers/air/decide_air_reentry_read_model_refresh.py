#!/usr/bin/env python3
import argparse, json
from pathlib import Path
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--read-model-refresh-manifest',required=True);p.add_argument('--refresh-plan',required=True);p.add_argument('--materialization-postcheck',required=True);p.add_argument('--materialization-audit',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--decision',default='approved_for_fixture_client_delivery_refresh_review');p.add_argument('--signature',default='fixture');p.add_argument('--signature-type',default='fixture_signature');p.add_argument('--decided-by',default='fixture');p.add_argument('--role',default='release_manager');p.add_argument('--as-of',default='2026-04-30T00:00:00Z');p.add_argument('--fixture-only',action='store_true');a=p.parse_args()
 for i in [a.materialization_postcheck,a.materialization_audit]:
  if json.loads(Path(i).read_text()).get('result') in {'deny','blocked'}: raise SystemExit('DENY')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
 d={'schema_version':'v1','decision_id':'dec1','domain':'atmosphere.air','decided_at':a.as_of,'as_of':a.as_of,'read_model_refresh_manifest_ref':a.read_model_refresh_manifest,'refresh_plan_ref':a.refresh_plan,'publication_receipt_candidate_ref':'fixture','materialization_postcheck_report_ref':a.materialization_postcheck,'materialization_audit_report_ref':a.materialization_audit,'decision':a.decision,'gates':[],'required_followups':[],'evidence_refs':[],'signature':a.signature,'signature_type':a.signature_type,'fixture_backed':True,'status':'fixture_candidate_ready'}
 (out/'reentry_read_model_refresh_decision.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
 print('PASS')
