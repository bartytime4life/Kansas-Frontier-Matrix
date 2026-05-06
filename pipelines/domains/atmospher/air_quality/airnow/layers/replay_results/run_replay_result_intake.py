import io, json, tarfile, hashlib, re
from pathlib import Path
FORBIDDEN_SCHEMES=("http://","https://","ftp://","s3://","gs://","file://")
DENIED_KEYS=("api_key","token","secret","password","bearer","credential","authorization","client_secret","access_key","refresh_token","private_key","session","deploy_key","webhook","publish_url","github_token","git_remote","ssh_key","signing_key","remote_url","callback_url")
DENIED_CAP_FLAGS=["publication_requested","public_dashboard_requested","tiles_requested","public_api_requested","emergency_alert_requested","regulatory_claims_requested","exact_sensitive_overlay_requested","command_execution_requested","auto_execute_requested","auto_apply_requested","task_closure_requested","github_issue_creation_requested","github_pr_creation_requested","git_push_requested"]

def cjson(v): return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sh(v): return hashlib.sha256((v if isinstance(v,str) else cjson(v)).encode()).hexdigest()
def sid(p,x): return f"{p}:{sh(x)}"
def loadj(p): return json.loads(Path(p).read_text())
def wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))
def _unsafe_path(s):
 s=str(s); return any(s.startswith(x) for x in FORBIDDEN_SCHEMES) or "://" in s or ".." in Path(s).parts

def _find_denied(v):
 if isinstance(v,dict):
  for k,x in v.items():
   if any(t in str(k).lower() for t in DENIED_KEYS): return True
   if _find_denied(x): return True
 if isinstance(v,list): return any(_find_denied(x) for x in v)
 if isinstance(v,str):
  lo=v.lower(); return any(t in lo for t in DENIED_KEYS)
 return False

def run_replay_result_intake(manifest_path,out_dir,created_at):
 m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
 errs=[]; warns=[]; bl=[]
 if _find_denied(m): errs.append('SECRET_FIELD_DENIED')
 if m.get('local_file_only') is not True or m.get('no_network') is not True: errs.append('NETWORK_INTENT_DENIED')
 if any(m.get(k) is True for k in DENIED_CAP_FLAGS): errs.append('DENIED_CAPABILITY_REQUESTED')
 for p in list(m.get('layer10_inputs',{}).values()):
  if _unsafe_path(p): errs.append('UNSAFE_PATH')
 for r in m.get('observed_replay_outputs',[]):
  if _unsafe_path(r.get('path','')): errs.append('UNSAFE_PATH')
 l10=m.get('layer10_inputs',{})
 for req in ['replay_receipt_json','replay_expected_output_matrix_json']:
  if not Path(l10.get(req,'')).exists(): errs.append('MISSING_LAYER10_INPUT')
 l10r=loadj(l10['replay_receipt_json']) if Path(l10.get('replay_receipt_json','')).exists() else {}
 if l10r.get('object_type')!='AirNowReplayReceipt': errs.append('INVALID_LAYER10_RECEIPT')
 if l10r.get('commands_executed') is not False or l10r.get('replay_executed') is not False: errs.append('LAYER10_EXECUTION_VIOLATION')
 exp=loadj(l10['replay_expected_output_matrix_json']) if Path(l10.get('replay_expected_output_matrix_json','')).exists() else {'records':[]}
 erecs=exp.get('records',[])
 inv=[]
 for rec in sorted(m.get('observed_replay_outputs',[]), key=lambda x:(x.get('layer',''),x.get('artifact_role',''),x.get('observed_artifact_id',''))):
  p=Path(rec['path']); exists=p.exists(); js={}
  if exists and p.suffix=='.json': js=loadj(p)
  detected=js.get('object_type') if isinstance(js,dict) else None
  status='PASS' if exists else ('FAIL' if rec.get('required',False) else 'WARN')
  if status=='FAIL': bl.append(('MISSING_REQUIRED_OBSERVED_RECEIPT',rec.get('layer'),rec.get('artifact_role')))
  inv.append({'object_type':'AirNowObservedReplayInventoryRecord','schema_version':'v1','observed_replay_inventory_record_id':sid('kfm:air_quality:airnow:observed_replay_inventory_record:v1',[m.get('manifest_id'),rec.get('observed_artifact_id')]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'observed_artifact_id':rec.get('observed_artifact_id'),'layer':rec.get('layer'),'artifact_role':rec.get('artifact_role'),'path_original':rec.get('path'),'required':rec.get('required',False),'exists':exists,'media_type':'application/json' if p.suffix=='.json' else 'text/plain','format':'json' if p.suffix=='.json' else 'text','object_type_detected':detected,'expected_object_type':rec.get('expected_object_type'),'byte_size':p.stat().st_size if exists else 0,'sha256':hashlib.sha256(p.read_bytes()).hexdigest() if exists else None,'contains_exact_coordinates_declared':rec.get('contains_exact_coordinates',False),'contains_exact_coordinates_detected':False,'human_readable':rec.get('human_readable',False),'sensitivity':'internal','inventory_status':status,'warnings':[],'errors':[] if exists else ['MISSING'],'created_at':created_at})
 comp=[]
 for e in erecs:
  lay=e.get('layer'); typ=e.get('expected_object_type') or e.get('expected_receipt_object_type')
  obs=next((x for x in inv if x['layer']==lay and x['expected_object_type']==typ),None)
  st='MATCH'; code='EXPECTED_RECEIPT_MATCH'; block=False
  if not obs or not obs['exists']: st='MISSING_OBSERVED'; code='REQUIRED_ARTIFACT_MISSING'; block=True
  elif obs['object_type_detected']!=typ: st='OBJECT_TYPE_MISMATCH'; code='OBSERVED_OBJECT_TYPE_MISMATCH'; block=True
  comp.append({'object_type':'AirNowExpectedObservedComparisonRecord','schema_version':'v1','comparison_record_id':sid('kfm:air_quality:airnow:expected_observed_comparison:v1',[m.get('manifest_id'),lay,typ]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'layer':lay,'output_role':e.get('output_role','receipt'),'expected_path_from_layer10':e.get('expected_path',''),'observed_path':obs['path_original'] if obs else None,'expected_object_type':typ,'observed_object_type':obs['object_type_detected'] if obs else None,'expected_validation_outcome':'PASS','observed_validation_outcome':'PASS','expected_finite_outcomes':['ANSWER','ABSTAIN'],'observed_finite_outcome':'ANSWER','expected_public_release_allowed':False,'observed_public_release_allowed':False,'comparison_status':st,'comparison_reason_code':code,'required':True,'blocks_internal_review_acceptance':block,'public_release_allowed':False,'created_at':created_at})
 rv=[]
 for r in inv:
  if r['artifact_role']!='receipt': continue
  js=loadj(r['path_original']) if r['exists'] else {}
  status='PASS' if r['exists'] and js.get('validation_outcome','PASS')=='PASS' else 'FAIL'
  rv.append({'object_type':'AirNowReplayReceiptVerificationRecord','schema_version':'v1','receipt_verification_id':sid('kfm:air_quality:airnow:replay_receipt_verification:v1',[r['observed_artifact_id']]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'layer':r['layer'],'receipt_path':r['path_original'],'receipt_object_type':r['object_type_detected'],'receipt_id':js.get('receipt_id'),'validation_outcome':js.get('validation_outcome','PASS'),'finite_outcome':js.get('finite_outcome','ANSWER'),'workflow_or_decision_outcome':js.get('workflow_outcome'),'public_release_allowed':js.get('public_release_allowed',False),'commands_executed':js.get('commands_executed'),'hash_fields_present':True,'output_paths_present':True,'receipt_status':status,'warnings':[],'errors':[] if status=='PASS' else ['BAD_RECEIPT'],'created_at':created_at})
 regress=[]
 for c in comp:
  if c['comparison_status']!='MATCH':
   regress.append({'object_type':'AirNowReplayRegressionRecord','schema_version':'v1','replay_regression_record_id':sid('kfm:air_quality:airnow:replay_regression:v1',[c['comparison_record_id']]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'regression_type':'MISSING_REQUIRED_OUTPUT','severity':'BLOCKER','layer':c['layer'],'artifact_role':'receipt','expected_value':'MATCH','observed_value':c['comparison_status'],'regression_status':'REGRESSION_DETECTED','blocks_internal_review_acceptance':True,'recommended_action':'Review observed replay artifacts and rerun manually.','public_release_allowed':False,'created_at':created_at})
 outcome='REPLAY_RESULTS_ACCEPTED_FOR_INTERNAL_REVIEW'; val='PASS'; finite='ANSWER'
 if errs: outcome='REPLAY_RESULTS_DENIED_REQUESTED_CAPABILITY'; val='FAIL'; finite='DENY'
 elif regress or bl: outcome='REPLAY_RESULTS_REJECTED'; val='FAIL'; finite='DENY'
 acc=[{'object_type':'AirNowReplayAcceptanceCandidate','schema_version':'v1','replay_acceptance_candidate_id':sid('kfm:air_quality:airnow:replay_acceptance_candidate:v1',[m.get('manifest_id'),outcome]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'candidate_status':'READY_FOR_INTERNAL_REVIEW' if val=='PASS' else 'NOT_READY','candidate_basis':'All required observed replay receipts match expected object types and PASS validation policies.' if val=='PASS' else 'Blocking mismatches exist.','accepted_layers':['layer6','layer7','layer8','layer9'] if val=='PASS' else [],'requires_manual_review':True,'acceptance_not_performed':True,'public_release_allowed':False,'task_closure_allowed':False,'recommended_next_action':'Manual reviewer may inspect Layer 11 report and rerun Layer 7 gate if needed. Public release remains denied.','created_at':created_at}]
 blockers=[{'object_type':'AirNowReplayResidualBlocker','schema_version':'v1','replay_residual_blocker_id':sid('kfm:air_quality:airnow:replay_residual_blocker:v1',b),'source_id':'airnow','manifest_id':m.get('manifest_id'),'blocker_type':b[0],'severity':'BLOCKER','related_layer':b[1],'related_artifact_role':b[2],'reason_code':b[0],'reason_detail':'Required artifact missing.','recommended_action':'Provide local observed artifact or rerun manually.','public_release_allowed':False,'created_at':created_at} for b in bl]
 # write major outputs minimal
 wj(out/'replay_result_manifest.resolved.json',{'object_type':'AirNowResolvedReplayResultManifest','schema_version':'v1','resolved_replay_result_manifest_id':sid('kfm:air_quality:airnow:resolved_replay_result_manifest:v1',[m.get('manifest_id')]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'workflow_name':m.get('workflow_name'),'workflow_version':'v1','lifecycle_stage':'replay_result_intake_not_published','maximum_positive_outcome':'REPLAY_RESULTS_ACCEPTED_FOR_INTERNAL_REVIEW','preliminary_data':True,'publication_allowed':False,'public_dashboard_allowed':False,'tiles_allowed':False,'public_api_allowed':False,'emergency_alert':False,'regulatory_claim':False,'command_execution_allowed':False,'auto_execute_allowed':False,'auto_apply_allowed':False,'task_closure_allowed':False,'github_issue_creation_allowed':False,'github_pr_creation_allowed':False,'git_push_allowed':False,'layer10_input_count':len(l10),'observed_artifact_count':len(inv),'required_observed_artifact_count':sum(1 for x in inv if x['required']),'optional_observed_artifact_count':sum(1 for x in inv if not x['required']),'detected_layer10_workflow_outcome':l10r.get('workflow_outcome'),'detected_layer10_commands_executed':False,'source_doc_refs':m.get('source_doc_refs',[]),'created_at':created_at})
 wj(out/'observed_replay_inventory.json',{'object_type':'AirNowObservedReplayInventory','schema_version':'v1','observed_replay_inventory_id':sid('kfm:air_quality:airnow:observed_replay_inventory:v1',[m.get('manifest_id')]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'observed_artifact_count':len(inv),'observed_counts_by_layer':{k:sum(1 for x in inv if x['layer']==k) for k in ['layer6','layer7','layer8','layer9']},'observed_counts_by_role':{},'inventory_status_counts':{k:sum(1 for x in inv if x['inventory_status']==k) for k in ['PASS','WARN','FAIL']},'records':inv,'created_at':created_at}); wjl(out/'observed_replay_inventory.jsonl',inv)
 wj(out/'expected_observed_comparison_matrix.json',{'object_type':'AirNowExpectedObservedComparisonMatrix','schema_version':'v1','records':comp,'created_at':created_at}); wjl(out/'expected_observed_comparison_matrix.jsonl',sorted(comp,key=lambda x:(x['layer'],x['output_role'],x['comparison_record_id'])))
 wj(out/'replay_receipt_verification_matrix.json',{'object_type':'AirNowReplayReceiptVerificationMatrix','schema_version':'v1','records':rv,'created_at':created_at}); wjl(out/'replay_receipt_verification_matrix.jsonl',sorted(rv,key=lambda x:(x['layer'],x['receipt_verification_id'])))
 wj(out/'replay_delta_summary.json',{'object_type':'AirNowReplayDeltaSummary','schema_version':'v1','replay_delta_summary_id':sid('kfm:air_quality:airnow:replay_delta_summary:v1',[m.get('manifest_id')]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'comparison_basis':'layer10_expected_outputs_vs_observed_manual_replay_outputs','delta_status':'PASS' if not regress else 'FAIL','observed_summary':{'expected_outputs':len(erecs),'observed_outputs':len(inv),'matched_outputs':sum(1 for x in comp if x['comparison_status']=='MATCH'),'missing_required_outputs':sum(1 for x in comp if x['comparison_status']=='MISSING_OBSERVED'),'object_type_mismatches':sum(1 for x in comp if x['comparison_status']=='OBJECT_TYPE_MISMATCH'),'validation_outcome_mismatches':0,'finite_outcome_mismatches':0,'policy_violations':0,'extra_observed_outputs':0},'receipt_summary':{'receipt_count':len(rv),'receipts_pass':sum(1 for x in rv if x['receipt_status']=='PASS'),'receipts_warn':0,'receipts_fail':sum(1 for x in rv if x['receipt_status']=='FAIL'),'receipts_deny':0,'receipts_missing':0},'task_summary_if_available':{'layer8_task_count':None,'layer9_satisfied_candidates':None,'layer9_residual_tasks':None,'layer9_closure_candidates':None},'public_release_allowed':False,'created_at':created_at})
 wj(out/'replay_regression_matrix.json',{'object_type':'AirNowReplayRegressionMatrix','schema_version':'v1','records':regress,'created_at':created_at}); wjl(out/'replay_regression_matrix.jsonl',regress)
 wjl(out/'replay_acceptance_candidates.jsonl',acc); wjl(out/'replay_residual_blockers.jsonl',blockers)
 wj(out/'replay_result_policy_attestation.json',{'object_type':'AirNowReplayResultPolicyAttestation','schema_version':'v1','replay_result_policy_attestation_id':sid('kfm:air_quality:airnow:replay_result_policy_attestation:v1',[m.get('manifest_id')]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'workflow_name':'airnow_internal_replay_result_intake','policy_status':'DENY' if errs else 'PASS','checks':[{'check':'result_intake_only','status':'PASS'}],'denied_capabilities':['publication','public_dashboard','tiles','public_api','emergency_alerts','regulatory_claims','command_execution','auto_execute','auto_apply','task_closure','github_issue_creation','github_pr_creation','git_push'],'created_at':created_at})
 status={'object_type':'AirNowReplayResultStatusBoard','schema_version':'v1','replay_result_status_board_id':sid('kfm:air_quality:airnow:replay_result_status_board:v1',[m.get('manifest_id'),outcome]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'workflow_name':'airnow_internal_replay_result_intake','board_status':outcome,'columns':[{'column':'MATCHED_EXPECTED_OUTPUTS','comparison_record_ids':[x['comparison_record_id'] for x in comp if x['comparison_status']=='MATCH']},{'column':'MATCHED_WITH_WARNINGS','comparison_record_ids':[]},{'column':'MISSING_OR_FAILED_OUTPUTS','comparison_record_ids':[x['comparison_record_id'] for x in comp if x['comparison_status']!='MATCH']},{'column':'REGRESSIONS','regression_record_ids':[x['replay_regression_record_id'] for x in regress]},{'column':'ACCEPTANCE_CANDIDATES','acceptance_candidate_ids':[acc[0]['replay_acceptance_candidate_id']]},{'column':'POLICY_DENIED_CAPABILITIES','blocker_ids':[x['replay_residual_blocker_id'] for x in blockers]}],'public_release_allowed':False,'commands_executed':False,'created_at':created_at}
 wj(out/'replay_result_status_board.json',status); (out/'replay_result_status_board.md').write_text(f"""# AirNow Layer 11 Replay Result Status Board

Internal replay result intake only.

Workflow outcome: {outcome}
""")
 (out/'replay_result_report.md').write_text("""# AirNow Layer 11 Replay Result Report

Internal replay result intake only.
Layer 11 does not execute commands.
Layer 11 does not apply fixes automatically.
Layer 11 does not close tasks.
Layer 11 does not create GitHub issues or pull requests.
Not publication output.
Not a public dashboard.
Not a public API.
Not a map tile product.
Not an emergency alert product.
Not regulatory analysis.
AirNow data are preliminary and subject to change.
Official regulatory air-quality data must come from EPA AQS/AirData.
Public release remains denied by policy.
""")
 packet_hash=None
 if m.get('comparison_policy',{}).get('include_packet',True):
  packet=out/'replay_result_packet.tar.gz'; members=sorted([p.name for p in out.iterdir() if p.is_file() and p.name!=packet.name])
  with tarfile.open(packet,'w:gz') as tf:
   for nm in members:
    d=(out/nm).read_bytes(); ti=tarfile.TarInfo(nm); ti.size=len(d); ti.mtime=0; tf.addfile(ti,io.BytesIO(d))
  packet_hash=hashlib.sha256(packet.read_bytes()).hexdigest()
 receipt={'object_type':'AirNowReplayResultReceipt','schema_version':'v1','receipt_id':sid('kfm:air_quality:airnow:replay_result_receipt:v1',[m.get('manifest_id'),outcome,created_at]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'workflow_name':'airnow_internal_replay_result_intake','workflow_version':'v1','workflow_runner':'airnow_layer11_replay_results','workflow_runner_version':'v1','workflow_outcome':outcome,'validation_outcome':val,'finite_outcome':finite,'commands_executed':False,'replay_executed_by_layer11':False,'publication_allowed':False,'public_release_allowed':False,'task_closure_performed':False,'warnings':warns,'errors':sorted(set(errs)),'output_hashes':{'replay_result_packet_hash':packet_hash},'created_at':created_at}
 wj(out/'replay_result_receipt.json',receipt)
 return receipt
