import json,hashlib
from pathlib import Path
BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/")
LIVE=("kubectl","terraform apply","https://","webhook","cdn purge","route53","cloudflare")
TS=lambda x:x or '2026-04-30T00:00:00Z'
J=lambda p: json.loads(Path(p).read_text())
def wj(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
def et(s): return f'"sha256:{s}"'
def fail(m): print('DENY',m); return 1

def build_plan(d,o,env,asof,allow,dry):
 if 'data/published/air/' in str(o).lower(): return fail('out-dir targets data/published/air')
 if env=='local_fixture' and not allow: return fail('fixture requires --allow-fixture-deployment-plan')
 req=['client_delivery_manifest.json','client_delivery_contract.json','client_route_manifest.json','static_response_bundle.json','client_cache_manifest.json','client_compatibility_report.json']
 for f in req:
  if not (d/f).exists(): return fail('missing '+f)
 routes,bundle,cache=J(d/'client_route_manifest.json'),J(d/'static_response_bundle.json'),J(d/'client_cache_manifest.json')
 txt=json.dumps([routes,bundle,cache]).lower()
 if any(b in txt for b in BAD): return fail('unsafe path')
 if any(l in txt for l in LIVE): return fail('live instruction')
 hid=hashlib.sha256((str(d)+TS(asof)).encode()).hexdigest()[:12]; ce={e['artifact_ref']:e for e in cache.get('entries',[])}; hr=[]
 for r in routes.get('routes',[]):
  for b in [x for x in bundle.get('responses',[]) if x.get('route_id')==r.get('route_id')]:
   if not b.get('sha256'): return fail('missing sha256')
   if ce.get(b['response_ref'],{}).get('etag')!=et(b['sha256']): return fail('bad etag')
   hr.append({'route_id':r['route_id'],'method':r['method'],'path_template':r['path_template'],'response_artifact_ref':b['response_ref'],'sha256':b['sha256'],'etag':et(b['sha256']),'cache_control':ce.get(b['response_ref'],{}).get('cache_control','public, max-age=300, immutable'),'visibility':'candidate_only'})
 envj={'schema_version':'v1','environment_id':'env-'+hid,'domain':'atmosphere.air','generated_at':TS(asof),'as_of':TS(asof),'environment':env,'environment_class':'fixture_only','allowed_actions':['plan_only'],'forbidden_actions':['deploy'],'artifact_roots':[str(d)],'public_boundary_policy':{'client_safe_only':True},'secret_policy':{'no_secrets_present':True},'status':'fixture_environment'}
 shm={'schema_version':'v1','hosting_manifest_id':'host-'+hid,'domain':'atmosphere.air','generated_at':TS(asof),'as_of':TS(asof),'client_delivery_manifest_ref':'client_delivery_manifest.json','route_manifest_ref':'client_route_manifest.json','static_response_bundle_ref':'static_response_bundle.json','cache_manifest_ref':'client_cache_manifest.json','hosted_routes':hr,'security_headers':{'x-content-type-options':'nosniff'},'artifact_refs':[x['response_artifact_ref'] for x in hr],'safety_checks':{'fixture_public_readable_blocked':True},'status':'fixture_hosting_candidate'}
 probe={'schema_version':'v1','probe_spec_id':'probe-'+hid,'domain':'atmosphere.air','created_at':TS(asof),'as_of':TS(asof),'client_delivery_manifest_ref':'client_delivery_manifest.json','routes_under_test':[{'route_id':h['route_id'],'method':h['method'],'path_template':h['path_template'],'expected_status_code':200,'expected_content_type':'application/json','expected_sha256':h['sha256'],'expected_etag':h['etag']} for h in hr],'expected_responses':[h['response_artifact_ref'] for h in hr],'fixtures':{'local_only':True},'safety_checks':{'network_calls_forbidden':True},'status':'fixture_probe_spec'}
 cp={'schema_version':'v1','cache_plan_id':'cache-'+hid,'domain':'atmosphere.air','created_at':TS(asof),'as_of':TS(asof),'client_cache_manifest_ref':'client_cache_manifest.json','client_delta_cursor_refs':['client_delta_cursors/cursor-1.json'],'client_invalidation_notice_refs':[],'planned_invalidations':[{'artifact_ref':h['response_artifact_ref'],'execution':'PROPOSED / NEEDS_VERIFICATION'} for h in hr],'forbidden_actions':['live purge'],'safety_checks':{'metadata_only':True},'status':'fixture_cache_plan'}
 rb={'schema_version':'v1','rollback_plan_id':'rb-'+hid,'domain':'atmosphere.air','created_at':TS(asof),'as_of':TS(asof),'current_delivery_manifest_ref':'client_delivery_manifest.json','previous_delivery_manifest_ref':'none','version_index_ref':'read_model_version_index.json','rollback_steps':['candidate supersession only'],'rollback_artifact_refs':['client_delivery_manifest.json'],'validation_checks':['hashes'], 'safety_checks':{'non_executable':True},'status':'fixture_rollback_plan'}
 dp={'schema_version':'v1','deployment_plan_id':'plan-'+hid,'domain':'atmosphere.air','created_at':TS(asof),'as_of':TS(asof),'environment_ref':'deployment_environment.json','client_delivery_manifest_ref':'client_delivery_manifest.json','static_hosting_manifest_ref':'static_hosting_manifest.json','client_compatibility_report_ref':'client_compatibility_report.json','deployment_steps':['governance review only'],'preflight_checks':['hashes'],'postflight_checks':['probes'],'rollback_plan_ref':'deployment_rollback_plan.json','cache_invalidation_plan_ref':'cache_invalidation_plan.json','synthetic_probe_spec_ref':'synthetic_probe_spec.json','safety_checks':{'non_executable':True},'status':'fixture_plan'}
 if not dry:
  o.mkdir(parents=True,exist_ok=True)
  for n,v in [('deployment_environment.json',envj),('static_hosting_manifest.json',shm),('synthetic_probe_spec.json',probe),('cache_invalidation_plan.json',cp),('deployment_rollback_plan.json',rb),('delivery_deployment_plan.json',dp)]: wj(o/n,v)
  (o/'deployment_change_records.jsonl').write_text(json.dumps({'schema_version':'v1','change_id':'chg-'+hid,'domain':'atmosphere.air','created_at':TS(asof),'as_of':TS(asof),'change_type':'deployment_plan_created','actor':'fixture-non-production-actor','subject_refs':['delivery_deployment_plan.json'],'evidence_refs':['client_delivery_manifest.json'],'result':'pass','details':{}},sort_keys=True)+'\n')
 print('PASS deployment_plan'); return 0
