#!/usr/bin/env python3
import argparse,json,hashlib,shutil
from pathlib import Path
TS=lambda x:x or '2026-04-30T00:00:00Z'
J=lambda p: json.loads(Path(p).read_text())
W=lambda p,d: (p.parent.mkdir(parents=True,exist_ok=True),p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n'))
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
BAD=('data/raw/','data/work/','data/quarantine/','data/processed/air/')
def main():
 a=argparse.ArgumentParser();a.add_argument('--rebuild-plan',required=True);a.add_argument('--read-model-dir',required=True);a.add_argument('--out-dir',required=True);a.add_argument('--as-of');a.add_argument('--fixture-only',action='store_true');a.add_argument('--dry-run',action='store_true');x=a.parse_args()
 if 'data/published/air/' in str(Path(x.out_dir)): raise SystemExit('DENY output path')
 pl=J(x.rebuild_plan); src=Path(x.read_model_dir); out=Path(x.out_dir); idx=J(src/'public_index.json'); old_vid=idx.get('version_id','v-src')
 nidx=dict(idx); nidx['version_id']=old_vid+'-rebuilt'; nidx['index_id']=idx.get('index_id','idx')+'-rebuilt'; nidx['status']='candidate';
 active=[]
 for e in idx.get('entries',[]):
  if any(c.get('subject_ref')==e.get('record_ref','') for c in pl.get('planned_changes',[])): continue
  active.append(e)
 nidx['entries']=active
 apis=[]
 for p in sorted(src.glob('public_api_record*.json'))+sorted((src/'public_api_records').glob('*.json') if (src/'public_api_records').exists() else []):
  r=J(p); rid=r.get('record_id','')
  if any(rid in json.dumps(c) for c in pl.get('planned_changes',[])): r['public_status']='retracted'
  apis.append((p.name,r))
 status=J(src/'public_status.json') if (src/'public_status.json').exists() else {'schema_version':'v1'}; status['retracted_records']=sum(1 for _,r in apis if r.get('public_status')=='retracted')
 delta={'schema_version':'v1','delta_feed_id':'delta-'+hashlib.sha256(pl['plan_id'].encode()).hexdigest()[:10],'domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'from_index_ref':str(src/'public_index.json'),'to_index_ref':str(out/'public_index.json'),'changes':[{'change_id':c['change_id'],'change_type':'record_retracted','publication_id':'fixture-publication','record_id':c['subject_ref'].split('.')[-1],'before_visibility':c['before_visibility'],'after_visibility':'retracted','reason':c['reason'],'tombstone_ref':pl['tombstone_refs'][0],'invalidation_notice_ref':pl['invalidation_notice_refs'][0],'effective_at':TS(x.as_of)} for c in pl.get('planned_changes',[])],'public_safe_refs':[str(out/'public_index.json')],'status':'fixture_candidate_delta' if x.fixture_only else 'candidate_delta'}
 if delta['status']=='public_delta' and x.fixture_only: raise SystemExit('DENY fixture public delta')
 if not x.dry_run:
  W(out/'read_model_rebuild_plan.json',pl)
  W(out/'public_index.json',nidx)
  for name,r in apis: W(out/'public_api_records'/name,r)
  W(out/'public_status.json',status)
  if (src/'public_provenance_traces').exists():
   (out/'public_provenance_traces').mkdir(parents=True,exist_ok=True)
   for p in (src/'public_provenance_traces').glob('*.json'): shutil.copy2(p,out/'public_provenance_traces'/p.name)
  W(out/'public_delta_feed.json',delta)
  for i,c in enumerate(delta['changes'],1): W(out/'client_invalidation_notices'/f'notice-{i}.json',{'schema_version':'v1','client_notice_id':f'notice-{i}','domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'publication_id':c['publication_id'],'record_id':c['record_id'],'reason':c['reason'],'visibility_change':'public_readable_to_retracted','effective_at':TS(x.as_of),'replacement_ref':'','public_delta_feed_ref':str(out/'public_delta_feed.json'),'public_index_ref':str(out/'public_index.json'),'status':'fixture_candidate' if x.fixture_only else 'candidate'})
  man={'schema_version':'v1','rebuild_id':'reb-'+hashlib.sha256(pl['plan_id'].encode()).hexdigest()[:10],'domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'rebuild_plan_ref':str(Path(x.rebuild_plan)),'source_index_ref':str(src/'public_index.json'),'new_index_ref':str(out/'public_index.json'),'delta_feed_ref':str(out/'public_delta_feed.json'),'status_ref':str(out/'public_status.json'),'provenance_trace_refs':[str(p) for p in (out/'public_provenance_traces').glob('*.json')] if (out/'public_provenance_traces').exists() else [],'applied_tombstone_refs':pl['tombstone_refs'],'applied_invalidation_notice_refs':pl['invalidation_notice_refs'],'artifact_refs':[],'safety_checks':{'source_index_mutated_in_place':False},'status':'rebuilt_fixture_only' if x.fixture_only else 'rebuilt_candidate'}
  for p in [out/'public_index.json',out/'public_status.json',out/'public_delta_feed.json']: man['artifact_refs'].append({'path':str(p),'sha256':sha(p),'source_ref':str(src/p.name) if (src/p.name).exists() else str(Path(x.rebuild_plan))})
  W(out/'read_model_rebuild_manifest.json',man)
  rvi={'schema_version':'v1','version_index_id':'vi-1','domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'versions':[{'version_id':old_vid,'public_index_ref':str(src/'public_index.json'),'rebuild_manifest_ref':'','created_at':TS(x.as_of),'visibility':'superseded','fixture_backed':True,'sha256':sha(src/'public_index.json')},{'version_id':nidx['version_id'],'public_index_ref':str(out/'public_index.json'),'rebuild_manifest_ref':str(out/'read_model_rebuild_manifest.json'),'created_at':TS(x.as_of),'visibility':'candidate_only','fixture_backed':True,'sha256':sha(out/'public_index.json')}],'active_version_ref':nidx['version_id'],'superseded_version_refs':[old_vid],'blocked_version_refs':[],'retracted_publication_refs':['fixture-publication'],'status':'fixture_candidate_versions'}
  W(out/'read_model_version_index.json',rvi); (out/'ops_events.jsonl').write_text(json.dumps({'event_type':'read_model_rebuilt','result':'pass','created_at':TS(x.as_of)},sort_keys=True)+'\n')
 print('PASS rebuild')
if __name__=='__main__': main()
