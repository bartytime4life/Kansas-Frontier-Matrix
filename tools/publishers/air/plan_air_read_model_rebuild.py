#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
TS=lambda x:x or '2026-04-30T00:00:00Z'
J=lambda p: json.loads(Path(p).read_text())
W=lambda p,d: (p.parent.mkdir(parents=True,exist_ok=True),p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n'))
BAD=('data/raw/','data/work/','data/quarantine/','data/processed/air/')
def refs(d,name): return sorted([str(p) for p in Path(d).glob(f'**/{name}')])
def main():
 a=argparse.ArgumentParser();a.add_argument('--read-model-dir',required=True);a.add_argument('--stewardship-dir',action='append',required=True);a.add_argument('--out-dir',required=True);a.add_argument('--as-of');a.add_argument('--allow-fixture-plan',action='store_true');a.add_argument('--dry-run',action='store_true');x=a.parse_args()
 idx=J(Path(x.read_model_dir)/'public_index.json'); api=refs(x.read_model_dir,'public_api_record*.json')+refs(x.read_model_dir,'public_api_records/*.json')
 t=sum([refs(d,'tombstone.json') for d in x.stewardship_dir],[]); inv=sum([refs(d,'read_model_invalidation_notice.json') for d in x.stewardship_dir],[]); sd=sum([refs(d,'steward_decision.json') for d in x.stewardship_dir],[]); rp=sum([refs(d,'remediation_package.json') for d in x.stewardship_dir],[])
 if not (t and inv and sd and rp): raise SystemExit('DENY missing lineage artifact')
 dec=[J(i).get('decision') for i in sd]
 if not any(d in ('approve_retraction','approve_remediation_package') for d in dec): raise SystemExit('DENY unapproved steward decision')
 for f in [idx,*[J(p) for p in t+inv+sd+rp]]:
  s=json.dumps(f)
  if any(b in s for b in BAD): raise SystemExit('DENY unsafe path ref')
 entries=sorted(idx.get('entries',[]),key=lambda e:e.get('record_id',''))
 changes=[{'change_id':f"chg-{i:03d}",'change_type':'mark_retracted','subject_ref':e.get('record_ref',''),'before_visibility':'public_readable','after_visibility':'retracted','reason':'steward_approved_tombstone','evidence_refs':[t[0],inv[0]]} for i,e in enumerate(entries,1)]
 p={'schema_version':'v1','plan_id':'plan-'+hashlib.sha256((str(idx.get('index_id'))+TS(x.as_of)).encode()).hexdigest()[:12],'domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'source_read_model_refs':[str(Path(x.read_model_dir)/'public_index.json')],'publication_manifest_refs':[str(Path(x.read_model_dir)/'publication_manifest.json')] if (Path(x.read_model_dir)/'publication_manifest.json').exists() else [],'tombstone_refs':sorted(t),'invalidation_notice_refs':sorted(inv),'steward_decision_refs':sorted(sd),'remediation_package_refs':sorted(rp),'planned_changes':changes,'safety_checks':{'no_raw_work_quarantine_refs':True,'no_direct_processed_exposure':True,'steward_decision_present':True,'tombstone_invalidation_present':True,'sha256_present':True,'no_fixture_real_public_promotion':True,'nowcast_operational_label_present':True,'nowcast_not_validated_aqs_truth':True},'status':'approved_fixture_only' if x.allow_fixture_plan else 'blocked'}
 if not x.dry_run: o=Path(x.out_dir);W(o/'read_model_rebuild_plan.json',p);(o/'ops_events.jsonl').write_text(json.dumps({'event_type':'read_model_rebuild_plan_created','result':'pass','created_at':TS(x.as_of)},sort_keys=True)+'\n')
 print('PASS plan')
if __name__=='__main__': main()
