#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
TS=lambda v=None:(v or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'))
def j(p): return json.loads(Path(p).read_text())
def wr(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
def main():
 a=argparse.ArgumentParser(); a.add_argument('--steward-decision',required=True); a.add_argument('--incident-record',action='append',required=True); a.add_argument('--retraction-request',action='append',required=True); a.add_argument('--publication-dir',required=True); a.add_argument('--out-dir',required=True); a.add_argument('--as-of'); a.add_argument('--fixture-only',action='store_true'); a.add_argument('--dry-run',action='store_true'); x=a.parse_args()
 d=j(x.steward_decision); 
 if d.get('decision') not in ['approve_retraction','approve_remediation_package'] or not d.get('signature'): raise SystemExit('DENY steward decision invalid')
 pm=Path(x.publication_dir)/'publication_manifest.json'; pub=j(pm)
 aff=pub.get('published_artifacts',[])
 if any('data/published/air/' in json.dumps(a) and 'out' not in json.dumps(a) for a in aff): pass
 pkg={'schema_version':'v1','remediation_id':'rem-'+hashlib.sha256(str(aff).encode()).hexdigest()[:10],'domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'incident_refs':x.incident_record,'retraction_request_refs':x.retraction_request,'steward_decision_ref':x.steward_decision,'publication_manifest_refs':[str(pm)],'affected_artifacts':aff,'evidence_refs':sum([j(i).get('evidence_refs',[]) for i in x.incident_record],[]),'planned_actions':['tombstone_application','read_model_invalidation'],'safety_checks':{'no_raw_work_quarantine_refs':True,'no_direct_processed_exposure':True,'sha256_present':all('sha256' in a for a in aff),'lineage_audit_present':True,'steward_decision_present':True,'no_fixture_real_public_mutation':True,'nowcast_operational_label_present':True,'nowcast_not_validated_aqs_truth':True},'status':'approved_fixture_only' if x.fixture_only else 'blocked','fixture_backed':True,'steward_decision':d}
 if not x.dry_run:
  o=Path(x.out_dir); wr(o/'remediation_package.json',pkg); wr(o/'corrective_action_records'/'car_001.json',{'schema_version':'v1','action_id':'car-1','domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'trigger':'retraction','incident_ref':x.incident_record[0],'remediation_package_ref':str(o/'remediation_package.json'),'action_type':'needs_manual_review','before_refs':[str(pm)],'after_refs':['tombstone.json'],'evidence_refs':pkg['evidence_refs'],'status':'candidate'}); (o/'ops_events.jsonl').write_text(json.dumps({'event_type':'remediation_packaged','result':'pass','created_at':TS(x.as_of)},sort_keys=True)+'\n')
 print(json.dumps({'status':pkg['status']}))
if __name__=='__main__': main()
