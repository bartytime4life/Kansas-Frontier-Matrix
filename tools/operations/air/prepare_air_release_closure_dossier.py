#!/usr/bin/env python
import argparse,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'deployments'/'air'))
from cutover_common import J,TS,wj,scan
p=argparse.ArgumentParser();p.add_argument('--handoff-dir',required=True);p.add_argument('--watch-evaluation',required=True);p.add_argument('--evidence-archive',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--notice-finalization',action='append',default=[]);p.add_argument('--signature',default='fixture-signature');p.add_argument('--signature-type',default='fixture_signature');p.add_argument('--closed-by');p.add_argument('--role');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');a=p.parse_args()
we=J(a.watch_evaluation)
if we.get('result') in ('deny','blocked'): print('DENY');sys.exit(1)
hd=Path(a.handoff_dir)
out={"schema_version":"1.0.0","closure_id":"closure-001","domain":"atmosphere.air","created_at":TS(a.as_of),"as_of":TS(a.as_of),"operational_handoff_package_ref":str(hd/'operational_handoff_package.json'),"watch_window_evaluation_ref":a.watch_evaluation,"runbook_activation_candidate_ref":str(hd/'runbook_activation_candidate.json'),"release_ledger_manifest_ref":str(Path(a.handoff_dir).parent/'cutover'/'release_ledger_manifest.json'),"operational_acceptance_ref":str(Path(a.handoff_dir).parent/'cutover'/'operational_acceptance_record.json'),"rollback_decision_ref":str(Path(a.handoff_dir).parent/'cutover'/'rollback_decision_record.json'),"stakeholder_notice_finalization_refs":a.notice_finalization,"evidence_archive_manifest_ref":a.evidence_archive,"closure_summary":"Fixture closure candidate only","open_items":[],"residual_risks":[],"decision":"close_fixture_release","signature":a.signature+':non-production','signature_type':a.signature_type,"fixture_backed":True,"status":"fixture_closed"}
if scan(out): print('DENY');sys.exit(1)
Path(a.out_dir).mkdir(parents=True,exist_ok=True);wj(Path(a.out_dir)/'release_closure_dossier.json',out);print('PASS')
