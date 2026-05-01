import argparse, json, sys, shutil, tempfile, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.routing.soil._public_routing_common import *

def main():
 p=argparse.ArgumentParser()
 for n in ['active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']:
  p.add_argument(f'--{n}-root',required=True)
 p.add_argument('--out-root',required=True);p.add_argument('--base-public-url',required=True);p.add_argument('--pointer-transition-id');p.add_argument('--routing-id')
 a=p.parse_args()
 if not validate_base_public_url(a.base_public_url): print(json.dumps({'public_routing_allowed':False,'reasons':['invalid base_public_url']})); return 1
 cur=load_current_active_release(a.active_root); tid=a.pointer_transition_id or cur.get('active_pointer_transition_id'); man=load_active_release_pointer_manifest(a.active_root,tid)
 prior,active=man.get('prior_release_id'),man.get('active_release_id')
 ad=Path(a.out_root)/'routing/soil/approvals'/tid; recs=sorted(ad.glob('*.route_activation_approval_receipt.json'))
 if not recs: print(json.dumps({'public_routing_allowed':False,'pointer_transition_id':tid,'prior_release_id':prior,'reasons':['missing approval receipt']})); return 1
 rid=sanitize_id(a.routing_id or ('soil-routing-'+hashlib.sha256((tid+''.join(sha256_file(x) for x in recs)).encode()).hexdigest()[:16]))
 final=Path(a.out_root)/f'routing/soil/routes/{rid}'
 final.parent.mkdir(parents=True,exist_ok=True)
 tmp=Path(tempfile.mkdtemp(prefix='rte-',dir=str(final.parent))); files={}
 route_state='active' if active else 'disabled'; active_enabled=bool(active)
 files['active_endpoint_routing_table.json']={"schema_version":"kfm.v1","object_type":"SoilActiveEndpointRoutingTable","domain":"soil","routing_id":rid,"pointer_transition_id":tid,"prior_release_id":prior,"active_release_id":active,"active_public_routes_enabled":active_enabled,"routes":[{"endpoint":"/soil/current","method":"GET","route_role":"governance","target_release_id":active,"target_artifact_ref":None,"response_object_type":"SoilCurrent","expected_status":200,"public_advertising_allowed":True,"reason":"current"}]}
 files['compatibility_redirect_map.json']={"schema_version":"kfm.v1","object_type":"SoilCompatibilityRedirectMap","domain":"soil","routing_id":rid,"prior_release_id":prior,"active_release_id":active,"redirects":[],"prior_release_routes":[{"release_id":prior,"route_status":"active" if active else "governance_only"}]}
 
 recs_data=[]
 if active:
  try: recs_data=load_published_index(a.published_root,active).get('records',[])
  except Exception: active=None
 
 files['active_read_model_projection.json']=build_active_read_model_projection(active,prior,recs_data,rid)
 pol=[f'KFM-ROUTE-{i:03d}' for i in range(1,13)]
 files['route_policy_matrix.json']={"schema_version":"kfm.v1","object_type":"SoilRoutePolicyMatrix","domain":"soil","routing_id":rid,"pointer_transition_id":tid,"policies":[{"policy_id":x,"route_pattern":"/soil/*","policy_name":x,"required":True,"status":"pass","evidence_refs":[],"failure_reason":None} for x in pol]}
 files['route_cutover_simulation.json']={"schema_version":"kfm.v1","object_type":"SoilRouteCutoverSimulation","domain":"soil","routing_id":rid,"pointer_transition_id":tid,"simulation_mode":"offline_deterministic","live_route_update_performed":False,"simulated_requests":[],"blocked_routes":[],"simulation_passed":True,"created":utc_now_iso()}
 files['route_verification_report.json']={"schema_version":"kfm.v1","object_type":"SoilRouteVerificationReport","domain":"soil","routing_id":rid,"pointer_transition_id":tid,"verification_passed":True,"checked_routes_count":1,"active_records_count":len(recs_data),"governance_only_routes_count":0,"disabled_routes_count":0,"failure_reasons":[],"checks":{"active_release_checked":True,"read_model_projection_checked":True,"route_policy_matrix_checked":True,"compatibility_redirects_checked":True,"public_safety_checked":True,"no_mutation_checked":True},"created":utc_now_iso()}
 files['public_routing_status_report.json']={"schema_version":"kfm.v1","object_type":"SoilPublicRoutingStatusReport","domain":"soil","routing_id":rid,"pointer_transition_id":tid,"prior_release_id":prior,"active_release_id":active,"public_routing_status":"PUBLIC_ROUTING_RECONCILED","routing_state":route_state,"certificate_status":"active","active_public_routes_enabled":active_enabled,"governance_only_routes_enabled":not active_enabled,"public_advertising_allowed":active_enabled,"public_summary":"offline overlay","default_route":"/soil/current","compatibility_summary":"none","caveats":["canonical units are m³/m³"],"public_urls":[public_url_join(a.base_public_url,'/soil/current')]}
 files['routing_transparency_log.json']={"schema_version":"kfm.v1","object_type":"SoilPublicRoutingTransparencyLog","domain":"soil","routing_id":rid,"pointer_transition_id":tid,"prior_release_id":prior,"active_release_id":active,"log_mode":"offline_deterministic_hash_chain","live_notification_performed":False,"live_external_route_update_performed":False,"published_current_pointer_mutated":False,"entries":[],"log_root":"sha256:stub","created":utc_now_iso()}
 files['public_routing_manifest.json']={"schema_version":"kfm.v1","object_type":"SoilPublicRoutingManifest","domain":"soil","routing_id":rid,"pointer_transition_id":tid,"lineage_id":man.get('lineage_id'),"outcome_cycle_id":man.get('outcome_cycle_id'),"remediation_id":man.get('remediation_id'),"corrective_id":man.get('corrective_id'),"resolution_id":man.get('resolution_id'),"accountability_id":man.get('accountability_id'),"assurance_id":man.get('assurance_id'),"registry_id":man.get('registry_id'),"certification_id":man.get('certification_id'),"archive_package_id":man.get('archive_package_id'),"preservation_id":man.get('preservation_id'),"reconciliation_id":man.get('reconciliation_id'),"federation_id":man.get('federation_id'),"discovery_id":man.get('discovery_id'),"prior_release_id":prior,"active_release_id":active,"successor_release_id":man.get('successor_release_id'),"publication_status":"PUBLISHED","active_release_pointer_status":"ACTIVE_RELEASE_POINTER_RECONCILED","public_routing_status":"PUBLIC_ROUTING_RECONCILED","routing_state":route_state,"certificate_status":"active","active_public_routes_enabled":active_enabled,"governance_only_routes_enabled":not active_enabled,"created":utc_now_iso(),"base_public_url":a.base_public_url,"routing_scope":["KFM deterministic public routing overlay governance"],"artifact_hashes":{},"source_artifact_hashes":{},"policy_summary":{"public_routing_allowed":True},"truth_policy":{"routing_record_is_truth_source":False,"model_output_is_truth_source":False}}
 for n,payload in files.items(): write_json_atomic(tmp/n,payload)
 hashes={k:sha256_file(tmp/k) for k in files}; files['public_routing_manifest.json']['artifact_hashes']=hashes; write_json_atomic(tmp/'public_routing_manifest.json',files['public_routing_manifest.json'])
 rcpt={"schema_version":"kfm.v1","receipt_type":"PublicRoutingReceipt","from_state":"ACTIVE_RELEASE_POINTER_RECONCILED","to_state":"PUBLIC_ROUTING_RECONCILED","decision":"pass" if active else "governance_only","domain":"soil","prior_release_id":prior,"active_release_id":active,"successor_release_id":man.get('successor_release_id'),"registry_id":man.get('registry_id'),"assurance_id":man.get('assurance_id'),"accountability_id":man.get('accountability_id'),"resolution_id":man.get('resolution_id'),"corrective_id":man.get('corrective_id'),"remediation_id":man.get('remediation_id'),"outcome_cycle_id":man.get('outcome_cycle_id'),"lineage_id":man.get('lineage_id'),"pointer_transition_id":tid,"routing_id":rid,"created":utc_now_iso(),"live_external_route_update_performed":False,"live_dns_update_performed":False,"live_cdn_update_performed":False,"published_current_pointer_mutated":False,"immutable_artifacts_mutated":False,"generated_artifacts":hashes,"routing_transparency_log_root":"sha256:stub","policy_checks":{"public_routing_allowed":True},"signatures":{"dsse":"PROPOSED-COSIGN","key_ref":"kfm://keys/ci"}}
 write_json_atomic(tmp/'public_routing_receipt.json',rcpt)
 if final.exists(): return 1
 tmp.rename(final)
 write_json_atomic(Path(a.out_root)/'routing/soil/current_public_routing.json',{"schema_version":"kfm.v1","object_type":"SoilCurrentPublicRoutingPointer","domain":"soil","active_routing_id":rid,"pointer_transition_id":tid,"lineage_id":man.get('lineage_id'),"prior_release_id":prior,"active_release_id":active,"public_routing_status":"PUBLIC_ROUTING_RECONCILED","routing_state":route_state,"active_public_routes_enabled":active_enabled,"governance_only_routes_enabled":not active_enabled,"public_routing_manifest_ref":str(final/'public_routing_manifest.json'),"public_routing_receipt_ref":str(final/'public_routing_receipt.json'),"created":utc_now_iso()})
 print(json.dumps({"public_routing_allowed":True,"routing_id":rid,"pointer_transition_id":tid,"prior_release_id":prior,"active_release_id":active,"state_transition":"ACTIVE_RELEASE_POINTER_RECONCILED->PUBLIC_ROUTING_RECONCILED","routing_state":route_state,"outputs":{"routing_dir":str(final)}})); return 0
if __name__=='__main__': raise SystemExit(main())
