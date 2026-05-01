#!/usr/bin/env python
import argparse,sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'deployments'/'air'))
from cutover_common import J,TS,wj,scan,h
p=argparse.ArgumentParser();p.add_argument('--stakeholder-notice-draft',required=True);p.add_argument('--handoff-dir',required=True);p.add_argument('--ledger',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--notice-type',default='fixture_cutover_summary');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
d=J(a.stakeholder_notice_draft)
out={"schema_version":"1.0.0","finalization_id":"notice-"+h({'as_of':TS(a.as_of)})[:12],"domain":"atmosphere.air","created_at":TS(a.as_of),"as_of":TS(a.as_of),"stakeholder_notice_draft_ref":a.stakeholder_notice_draft,"release_ledger_manifest_ref":a.ledger,"operational_handoff_package_ref":str(Path(a.handoff_dir)/'operational_handoff_package.json'),"notice_type":a.notice_type,"message_summary":d.get('message_summary','fixture summary'),"public_safe_links":d.get('public_safe_links',[]),"redactions":[],"approval_state":"candidate_finalized","forbidden_actions":["no email/slack/pagerduty send"],"status":"fixture_notice_finalized"}

Path(a.out_dir).mkdir(parents=True,exist_ok=True);wj(Path(a.out_dir)/'stakeholder_notice_finalization.json',out);(Path(a.out_dir)/'operational_handoff_events.jsonl').write_text(json.dumps({"schema_version":"1.0.0","event_id":"evt-notice","domain":"atmosphere.air","event_type":"stakeholder_notice_finalized_candidate","created_at":TS(a.as_of),"as_of":TS(a.as_of),"actor":"fixture-operator-non-production","subject_refs":[str(Path(a.out_dir)/'stakeholder_notice_finalization.json')],"evidence_refs":[a.ledger],"result":"pass","details":{}},sort_keys=True)+'\n')
print('PASS')
