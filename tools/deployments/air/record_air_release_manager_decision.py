#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
TS=lambda x:x or '2026-04-30T00:00:00Z'

def main():
 a=argparse.ArgumentParser();a.add_argument('--deployment-readiness-dir',required=True);a.add_argument('--decision',required=True);a.add_argument('--decided-by',required=True);a.add_argument('--role',required=True);a.add_argument('--out-dir',required=True);a.add_argument('--signature',default='fixture-signature');a.add_argument('--signature-type',default='fixture_signature');a.add_argument('--as-of');a.add_argument('--fixture-only',action='store_true');a.add_argument('--dry-run',action='store_true');x=a.parse_args()
 if x.decision=='approve_staging_candidate_handoff' and x.fixture_only: return 1
 if x.decision=='production_approval_blocked': pass
 if 'production' in x.decision: pass
 hid=hashlib.sha256((x.decision+TS(x.as_of)).encode()).hexdigest()[:12]
 d={'schema_version':'v1','decision_id':'rmd-'+hid,'domain':'atmosphere.air','decided_at':TS(x.as_of),'decided_by':x.decided_by,'role':x.role,'subject_refs':['deployment_readiness_report.json'],'decision':x.decision,'rationale':'fixture governance decision','required_actions':['non-production only'],'signature':x.signature,'signature_type':x.signature_type,'fixture_backed':True,'status':'recorded_non_production'}
 if x.signature_type=='fixture_signature' and x.decision not in ['approve_fixture_simulation','request_more_evidence','block_deployment','production_approval_blocked']: return 1
 if not x.dry_run:
  o=Path(x.out_dir);o.mkdir(parents=True,exist_ok=True)
  (o/'release_manager_decision.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
  (o/'deployment_authorization_events.jsonl').write_text(json.dumps({'schema_version':'v1','event_id':'evt-'+hid,'domain':'atmosphere.air','event_type':'release_manager_decision_recorded','created_at':TS(x.as_of),'as_of':TS(x.as_of),'actor':'fixture-release-manager-non-production','subject_refs':['release_manager_decision.json'],'evidence_refs':['deployment_readiness_report.json'],'result':'pass','details':{}},sort_keys=True)+'\n')
 print('PASS release manager decision'); return 0
if __name__=='__main__': raise SystemExit(main())
