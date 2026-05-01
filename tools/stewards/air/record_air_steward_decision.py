#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
TS=lambda v=None:(v or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'))

def main():
 p=argparse.ArgumentParser(); p.add_argument('--queue',required=True); p.add_argument('--item-id',required=True); p.add_argument('--decision',required=True); p.add_argument('--decided-by',required=True); p.add_argument('--role',required=True); p.add_argument('--out-dir',required=True); p.add_argument('--attestation'); p.add_argument('--signature'); p.add_argument('--signature-type'); p.add_argument('--as-of'); p.add_argument('--fixture-only',action='store_true'); p.add_argument('--dry-run',action='store_true'); a=p.parse_args()
 q=json.loads(Path(a.queue).read_text()); it=[i for i in q['items'] if i['item_id']==a.item_id][0]
 if not a.signature: raise SystemExit('DENY unsigned')
 st=a.signature_type or 'fixture_signature'
 if st=='fixture_signature' and not a.fixture_only: raise SystemExit('DENY fixture signature real execution')
 d={'schema_version':'v1','decision_id':'dec-'+hashlib.sha256((a.item_id+a.decision).encode()).hexdigest()[:10],'domain':'atmosphere.air','decided_at':TS(a.as_of),'decided_by':a.decided_by,'role':a.role,'subject_refs':[it['incident_ref'],it['retraction_request_ref'],it['publication_manifest_ref']],'decision':a.decision,'rationale':'fixture stewardship decision','required_actions':['build_remediation_package'],'attestation_ref':a.attestation or 'NEEDS_VERIFICATION','signature':a.signature,'signature_type':st,'fixture_backed':True,'non_production_label':'NON_PRODUCTION_FIXTURE_SIGNATURE'}
 if not a.dry_run:
  o=Path(a.out_dir); o.mkdir(parents=True,exist_ok=True); (o/'steward_decision.json').write_text(json.dumps(d,sort_keys=True,indent=2)+'\n'); (o/'ops_events.jsonl').write_text(json.dumps({'schema_version':'v1','event_type':'steward_decision_recorded','created_at':TS(a.as_of),'result':'pass'},sort_keys=True)+'\n')
 print(json.dumps({'decision':a.decision,'status':'fixture_only'}))
if __name__=='__main__': main()
