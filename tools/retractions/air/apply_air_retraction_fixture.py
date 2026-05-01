#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
TS=lambda v=None:(v or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'))
def j(p): return json.loads(Path(p).read_text())
def wr(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
def main():
 p=argparse.ArgumentParser(); p.add_argument('--remediation-package',required=True); p.add_argument('--publication-dir',required=True); p.add_argument('--out-dir',required=True); p.add_argument('--as-of'); p.add_argument('--dry-run',action='store_true'); a=p.parse_args()
 r=j(a.remediation_package); dec=r.get('steward_decision',{})
 if dec.get('decision')!='approve_retraction': raise SystemExit('DENY unapproved retraction execution')
 if not dec.get('signature'): raise SystemExit('DENY unsigned decision')
 if dec.get('signature_type')=='fixture_signature' and not r.get('fixture_backed',True): raise SystemExit('DENY fixture signature real execution')
 o=Path(a.out_dir); t={'schema_version':'v1','tombstone_id':'ts-'+hashlib.sha256(str(r).encode()).hexdigest()[:10],'domain':'atmosphere.air','created_at':TS(a.as_of),'reason':'fixture_retraction','status':'fixture_only'}
 n={'schema_version':'v1','invalidation_id':'inv-1','domain':'atmosphere.air','created_at':TS(a.as_of),'as_of':TS(a.as_of),'publication_manifest_ref':r['publication_manifest_refs'][0],'public_index_refs':['public_index.json'],'public_api_record_refs':['public_api_record.json'],'reason':'retraction','tombstone_ref':str(o/'tombstone.json'),'replacement_ref':'','visibility_change':'public_readable_to_retracted','status':'approved_fixture_only'}
 e={'schema_version':'v1','execution_id':'exec-1','domain':'atmosphere.air','created_at':TS(a.as_of),'as_of':TS(a.as_of),'remediation_package_ref':a.remediation_package,'steward_decision_ref':r['steward_decision_ref'],'retraction_request_ref':r['retraction_request_refs'][0],'publication_manifest_ref':r['publication_manifest_refs'][0],'tombstone_ref':str(o/'tombstone.json'),'invalidation_notice_ref':str(o/'read_model_invalidation_notice.json'),'affected_artifacts':r['affected_artifacts'],'execution_mode':'dry_run' if a.dry_run else 'fixture_only','status':'not_executed' if a.dry_run else 'executed_fixture_only'}
 wr(o/'tombstone.json',t); wr(o/'read_model_invalidation_notice.json',n); wr(o/'retraction_execution_manifest.json',e); wr(o/'corrective_action_records'/'car_apply.json',{'schema_version':'v1','action_id':'car-apply','domain':'atmosphere.air','created_at':TS(a.as_of),'as_of':TS(a.as_of),'trigger':'approved_retraction','incident_ref':r['incident_refs'][0],'remediation_package_ref':a.remediation_package,'action_type':'tombstone_application','before_refs':[r['publication_manifest_refs'][0]],'after_refs':[str(o/'tombstone.json')],'evidence_refs':r['evidence_refs'],'status':'executed_fixture_only'}); (o/'ops_events.jsonl').write_text(json.dumps({'event_type':'fixture_retraction_applied','result':'pass','created_at':TS(a.as_of)},sort_keys=True)+'\n')
 print(json.dumps({'status':e['status']}))
if __name__=='__main__': main()
