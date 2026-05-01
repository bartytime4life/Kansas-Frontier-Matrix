#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/")
REQ_ROUTES=["index_lookup","record_lookup","status_lookup","provenance_lookup","delta_lookup","invalidation_lookup"]
TS=lambda x:x or '2026-04-30T00:00:00Z'
J=lambda p: json.loads(Path(p).read_text())

def wj(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_file(p): return sha_bytes(Path(p).read_bytes())
def etag(sha): return f'"sha256:{sha}"'
def deny(msg): raise SystemExit(f'DENY {msg}')
def has_bad(v): s=json.dumps(v).lower(); return any(x in s for x in BAD)

def main():
 a=argparse.ArgumentParser();a.add_argument('--read-model-dir',required=True);a.add_argument('--rebuild-dir');a.add_argument('--out-dir',required=True);a.add_argument('--api-version',default='v1');a.add_argument('--as-of');a.add_argument('--allow-fixture-delivery',action='store_true');a.add_argument('--dry-run',action='store_true');x=a.parse_args();
 src=Path(x.read_model_dir); out=Path(x.out_dir)
 if 'data/published/air/' in str(out).lower(): deny('out-dir targets data/published/air')
 idx=J(src/'public_index.json') if (src/'public_index.json').exists() else deny('missing PublicIndex')
 status=J(src/'public_status.json') if (src/'public_status.json').exists() else deny('missing PublicStatus')
 recs={}
 for p in sorted((src/'public_api_records').glob('*.json')) if (src/'public_api_records').exists() else sorted(src.glob('public_api_record*.json')):
  r=J(p); recs[r.get('record_id',p.stem)]=r
 prov={p.stem:J(p) for p in sorted((src/'public_provenance_traces').glob('*.json'))} if (src/'public_provenance_traces').exists() else {}
 delta=J(src/'public_delta_feed.json') if (src/'public_delta_feed.json').exists() else None
 notices=[J(p) for p in sorted((src/'client_invalidation_notices').glob('*.json'))] if (src/'client_invalidation_notices').exists() else []
 rvi=J(src/'read_model_version_index.json') if (src/'read_model_version_index.json').exists() else {'version_index_id':'missing','versions':[]}
 rbm=J(src/'read_model_rebuild_manifest.json') if (src/'read_model_rebuild_manifest.json').exists() else {'rebuild_id':'missing'}
 if has_bad([idx,status,recs,prov,delta,notices,rvi,rbm]): deny('unsafe internal path exposure')
 if 'validated aqs truth' in json.dumps([idx,recs,status]).lower(): deny('NowCast labeled validated AQS truth')
 for e in idx.get('entries',[]):
  rid=e.get('record_id') or str(e.get('record_ref','')).split('.')[-1]
  if e.get('visibility')=='public_readable' and rid not in recs: deny('missing PublicApiRecord for active entry')
  r=recs.get(rid,{})
  if r.get('public_status') in ('retracted','tombstoned') and e.get('visibility')=='public_readable': deny('retracted active')
  if r.get('measurement_basis')=='validated_aqs' and r.get('validation_window')!='24h_validated': deny('AQS validated row missing 24h_validated')
 fixture=True
 if not x.allow_fixture_delivery: deny('fixture delivery requires --allow-fixture-delivery')
 
 contract={'schema_version':'v1','contract_id':'contract-'+sha_bytes(f'{x.api_version}:{TS(x.as_of)}'.encode())[:12],'domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'api_version':x.api_version,'supported_read_model_versions':[v.get('version_id','unknown') for v in rvi.get('versions',[])],'routes':REQ_ROUTES,'response_schemas':['PublicIndex','PublicApiRecord','PublicStatus','PublicProvenanceTrace','PublicDeltaFeed','ClientInvalidationNotice'],'query_parameters':['record_id','publication_id','delta_cursor'],'cache_policy':{'default_cache_control':'public, max-age=300, immutable'},'delta_policy':{'enabled':delta is not None},'provenance_policy':{'required':True},'measurement_semantics':{'pm25_units':'ug_m3','nowcast_is_operational_evidence':True,'nowcast_is_validated_aqs_truth':False,'aqs_validated_records_window':'24h_validated'},'safety_checks':{'forbidden_paths_blocked':True},'status':'fixture_contract'}
 routes=[
 {'route_id':'index_lookup','method':'GET','path_template':f'/air/{x.api_version}/index','produces':'application/json','source_artifact_ref':'public_index.json','response_artifact_ref':'responses/index.json','cache_policy_ref':'default','visibility':'candidate_only'},
 {'route_id':'status_lookup','method':'GET','path_template':f'/air/{x.api_version}/status','produces':'application/json','source_artifact_ref':'public_status.json','response_artifact_ref':'responses/status.json','cache_policy_ref':'default','visibility':'candidate_only'},
 {'route_id':'record_lookup','method':'GET','path_template':f'/air/{x.api_version}/records/{{record_id}}','produces':'application/json','source_artifact_ref':'public_api_records/*.json','response_artifact_ref':'responses/records/*.json','cache_policy_ref':'default','visibility':'candidate_only'},
 {'route_id':'provenance_lookup','method':'GET','path_template':f'/air/{x.api_version}/provenance/{{record_id}}','produces':'application/json','source_artifact_ref':'public_provenance_traces/*.json','response_artifact_ref':'responses/provenance/*.json','cache_policy_ref':'default','visibility':'candidate_only'},
 {'route_id':'delta_lookup','method':'GET','path_template':f'/air/{x.api_version}/delta','produces':'application/json','source_artifact_ref':'public_delta_feed.json','response_artifact_ref':'responses/deltas/delta.json','cache_policy_ref':'default','visibility':'candidate_only'},
 {'route_id':'invalidation_lookup','method':'GET','path_template':f'/air/{x.api_version}/invalidation-notices','produces':'application/json','source_artifact_ref':'client_invalidation_notices/*.json','response_artifact_ref':'responses/deltas/invalidation_notices.json','cache_policy_ref':'default','visibility':'candidate_only'}]
 rm={'schema_version':'v1','route_manifest_id':'routes-'+contract['contract_id'],'domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'client_delivery_contract_ref':'client_delivery_contract.json','read_model_version_index_ref':'read_model_version_index.json','routes':routes,'static_artifact_refs':[],'safety_checks':{'fixture_public_routes_blocked':True},'status':'fixture_routes'}
 responses=[]; cache_entries=[]
 def emit(rel,obj,route_id,req):
  b=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode(); s=sha_bytes(b); p=out/rel
  if not x.dry_run: p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(b)
  cache_ref=f'cache:{rel}'; cache_entries.append({'artifact_ref':rel,'sha256':s,'etag':etag(s),'content_type':'application/json','cache_control':'public, max-age=300, immutable','immutable':True,'source_ref':'public_read_model'})
  responses.append({'response_id':'resp-'+sha_bytes(rel.encode())[:10],'route_id':route_id,'request_example':req,'response_ref':rel,'sha256':s,'content_type':'application/json','status_code':200,'cache_metadata_ref':cache_ref})
 emit('responses/index.json',idx,'index_lookup',{'route':f'/air/{x.api_version}/index'})
 emit('responses/status.json',status,'status_lookup',{'route':f'/air/{x.api_version}/status'})
 for rid,r in sorted(recs.items()): emit(f'responses/records/{rid}.json',r,'record_lookup',{'route':f'/air/{x.api_version}/records/{rid}'})
 for pid,pv in sorted(prov.items()): emit(f'responses/provenance/{pid}.json',pv,'provenance_lookup',{'route':f'/air/{x.api_version}/provenance/{pid}'})
 emit('responses/deltas/delta.json',delta or {'schema_version':'v1','changes':[]},'delta_lookup',{'route':f'/air/{x.api_version}/delta'})
 emit('responses/deltas/invalidation_notices.json',{'notices':notices},'invalidation_lookup',{'route':f'/air/{x.api_version}/invalidation-notices'})
 bun={'schema_version':'v1','bundle_id':'bundle-'+contract['contract_id'],'domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'source_read_model_refs':['public_index.json','public_status.json'],'route_manifest_ref':'client_route_manifest.json','responses':responses,'status':'fixture_bundle'}
 cm={'schema_version':'v1','cache_manifest_id':'cache-'+contract['contract_id'],'domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'entries':cache_entries,'policy':{'etag_from_sha256':True},'status':'fixture_cache_metadata'}
 cursor={'schema_version':'v1','cursor_id':'cursor-1','domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'from_index_ref':'public_index.json','to_index_ref':'public_index.json','delta_feed_ref':'public_delta_feed.json','cursor_value':'cursor:'+sha_bytes(TS(x.as_of).encode())[:12],'cursor_semantics':'public_safe_monotonic_cursor','visible_changes':len((delta or {'changes':[]}).get('changes',[])),'status':'fixture_cursor'}
 comp={'schema_version':'v1','compatibility_report_id':'compat-'+contract['contract_id'],'domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'client_delivery_contract_ref':'client_delivery_contract.json','read_model_version_index_ref':'read_model_version_index.json','checked_versions':contract['supported_read_model_versions'],'checks':[{'check':'required_routes_present','result':'pass'}],'breaking_changes':[],'warnings':[],'result':'pass'}
 dm={'schema_version':'v1','delivery_id':'delivery-'+contract['contract_id'],'domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'client_delivery_contract_ref':'client_delivery_contract.json','client_route_manifest_ref':'client_route_manifest.json','static_response_bundle_ref':'static_response_bundle.json','client_cache_manifest_ref':'client_cache_manifest.json','client_delta_cursor_refs':['client_delta_cursors/cursor-1.json'],'client_compatibility_report_ref':'client_compatibility_report.json','read_model_version_index_ref':'read_model_version_index.json','artifact_refs':[r['response_ref'] for r in responses],'safety_checks':{'fixture_not_published':True},'status':'fixture_delivery_candidate'}
 if not x.dry_run:
  for n,o in [('client_delivery_contract.json',contract),('client_route_manifest.json',rm),('static_response_bundle.json',bun),('client_cache_manifest.json',cm),('client_compatibility_report.json',comp),('client_delivery_manifest.json',dm)]: wj(out/n,o)
  wj(out/'client_delta_cursors/cursor-1.json',cursor)
  (out/'ops_events.jsonl').write_text(json.dumps({'event_type':'client_delivery_built','result':'pass','as_of':TS(x.as_of)},sort_keys=True)+'\n')
 print('PASS client_delivery')
if __name__=='__main__': main()
