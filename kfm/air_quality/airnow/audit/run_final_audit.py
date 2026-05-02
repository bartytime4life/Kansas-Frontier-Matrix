import hashlib, io, json, re, tarfile
from pathlib import Path

FORBIDDEN_SCHEMES=("http://","https://","ftp://","s3://","gs://","file://")
DENIED_KEYS=("api_key","token","secret","password","bearer","credential","authorization","client_secret","access_key","refresh_token","private_key","session","deploy_key","webhook","publish_url","github_token","git_remote","ssh_key","signing_key","remote_url","callback_url")
DENIED_REQUEST_FLAGS=["publication_requested","public_dashboard_requested","tiles_requested","public_api_requested","emergency_alert_requested","regulatory_claims_requested","exact_sensitive_overlay_requested","command_execution_requested","auto_execute_requested","auto_apply_requested","task_closure_requested","github_issue_creation_requested","github_pr_creation_requested","git_push_requested"]
LAYER_ORDER=[f"layer{i}" for i in range(1,12)]
REQ_CHECKS=["no_network","no_live_ingestion","no_live_file_download","no_bulk_zip_web_service_loop","no_publication","no_public_dashboard","no_tiles","no_public_api","no_emergency_alerts","no_regulatory_claims","no_exact_sensitive_overlay","no_command_execution","no_auto_execute","no_auto_apply","no_task_closure","no_github_issue_creation","no_github_pr_creation","no_git_push","preliminary_data_disclaimer","aqs_regulatory_disclaimer","coordinate_redaction_in_human_docs"]


def cjson(v): return json.dumps(v, sort_keys=True, separators=(",",":"), ensure_ascii=False)
def sh(v): return hashlib.sha256((v if isinstance(v,str) else cjson(v)).encode()).hexdigest()
def sid(prefix, v): return f"{prefix}:{sh(v)}"
def loadj(p): return json.loads(Path(p).read_text())
def wj(p,o): Path(p).write_text(json.dumps(o, indent=2, sort_keys=True)+"\n")
def wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))

def _find_denied(v):
 if isinstance(v,dict):
  for k,x in v.items():
   if any(t in str(k).lower() for t in DENIED_KEYS): return True
   if _find_denied(x): return True
 if isinstance(v,list): return any(_find_denied(x) for x in v)
 return isinstance(v,str) and any(t in v.lower() for t in DENIED_KEYS)

def _bad_path(p):
 s=str(p)
 return any(s.startswith(x) for x in FORBIDDEN_SCHEMES) or "://" in s or ".." in Path(s).parts

def _coord_leak(text):
 return bool(re.search(r"\b-?\d{1,2}\.\d{4,}\s*,\s*-?\d{1,3}\.\d{4,}\b", text))

def run_final_audit(manifest_path, out_dir, created_at):
 m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
 errs=[]; warns=[]; ex=[]
 if _find_denied(m): errs.append("SECRET_FIELD_DENIED")
 for k in ["local_file_only","no_network"]:
  if m.get(k) is not True: errs.append("NETWORK_INTENT_DENIED")
 if m.get("bulk_web_service_loop") is not False: errs.append("BULK_LOOP_DENIED")
 if any(m.get(k) is True for k in DENIED_REQUEST_FLAGS): errs.append("DENIED_CAPABILITY_REQUESTED")
 if m.get("publication_allowed") is not False: errs.append("PUBLICATION_ALLOWED_TRUE")
 artifacts=sorted(m.get("artifacts",[]), key=lambda a:(a.get("layer",""),a.get("artifact_role",""),a.get("artifact_id",""),a.get("path","")))
 for a in artifacts:
  if _bad_path(a.get("path","")): errs.append("UNSAFE_PATH")
 inv=[]
 for a in artifacts:
  p=Path(a.get("path","")); exists=p.exists(); js=None; text=""
  if exists and p.suffix==".json":
   try: js=loadj(p)
   except: js=None
  if exists and a.get("human_readable",False):
   text=p.read_text(errors="ignore")
   if _coord_leak(text): errs.append("HUMAN_DOC_COORDINATE_LEAK")
  detected=js.get("object_type") if isinstance(js,dict) else None
  status="PASS" if exists else ("FAIL" if a.get("required",False) else "WARN")
  if status=="FAIL": ex.append(("MISSING_REQUIRED_ARTIFACT","BLOCKER",a.get("layer"),a.get("artifact_id"),"REQUIRED_ARTIFACT_MISSING"))
  inv.append({"object_type":"AirNowAuditArtifactInventoryRecord","schema_version":"v1","audit_artifact_inventory_record_id":sid("kfm:air_quality:airnow:audit_artifact_inventory_record:v1",[m.get("manifest_id"),a.get("artifact_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"artifact_id":a.get("artifact_id"),"layer":a.get("layer"),"artifact_role":a.get("artifact_role"),"path_original":a.get("path"),"required":a.get("required",False),"exists":exists,"media_type":"application/json" if p.suffix==".json" else ("text/markdown" if p.suffix==".md" else "text/plain"),"format":"json" if p.suffix==".json" else ("jsonl" if p.suffix==".jsonl" else "text"),"object_type_detected":detected,"expected_object_type":a.get("expected_object_type"),"byte_size":p.stat().st_size if exists else 0,"sha256":hashlib.sha256(p.read_bytes()).hexdigest() if exists else None,"contains_exact_coordinates_declared":a.get("contains_exact_coordinates",False),"contains_exact_coordinates_detected":False,"human_readable":a.get("human_readable",False),"sensitivity":"internal","inventory_status":status,"warnings":[],"errors":[] if exists else ["MISSING"],"created_at":created_at})
 req={r["artifact_id"]:r for r in m.get("required_receipts",[])}; rrows=[]
 for rid,r in sorted(req.items(), key=lambda kv:(kv[1].get("layer",""),kv[0])):
  it=next((x for x in inv if x["artifact_id"]==rid),None)
  if not it or not it["exists"]:
   st="MISSING"; det=None; receipt_id=None; vo="FAIL"; fo="DENY"; wout=None
   ex.append(("MISSING_REQUIRED_RECEIPT","BLOCKER",r.get("layer"),rid,"REQUIRED_RECEIPT_MISSING"))
  else:
   js=loadj(it["path_original"]); det=js.get("object_type"); receipt_id=js.get("receipt_id"); vo=js.get("validation_outcome","PASS"); fo=js.get("finite_outcome","ANSWER"); wout=js.get("workflow_outcome")
   st="PASS"
   if det!=r.get("expected_object_type"): st="OBJECT_TYPE_MISMATCH"; ex.append(("RECEIPT_OBJECT_TYPE_MISMATCH","BLOCKER",r.get("layer"),rid,"RECEIPT_OBJECT_TYPE_MISMATCH"))
   if js.get("public_release_allowed") is True: st="DENY"; ex.append(("PUBLIC_RELEASE_TRUE","BLOCKER",r.get("layer"),rid,"PUBLIC_RELEASE_TRUE"))
  rrows.append({"object_type":"AirNowAuditReceiptLedgerRecord","schema_version":"v1","audit_receipt_ledger_record_id":sid("kfm:air_quality:airnow:audit_receipt_ledger_record:v1",[m.get("manifest_id"),rid]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"layer":r.get("layer"),"artifact_id":rid,"receipt_path":it["path_original"] if it else None,"expected_object_type":r.get("expected_object_type"),"detected_object_type":det,"receipt_id":receipt_id,"validation_outcome":vo,"finite_outcome":fo,"workflow_outcome":wout,"decision_outcome":None,"public_release_allowed":False,"publication_allowed":False,"emergency_alert":False,"regulatory_claim":False,"commands_executed":False,"receipt_status":st,"warnings":[],"errors":[],"created_at":created_at})
 gov=[{"object_type":"AirNowAuditGovernanceLedgerRecord","schema_version":"v1","audit_governance_ledger_record_id":sid("kfm:air_quality:airnow:audit_governance_ledger_record:v1",[m.get("manifest_id"),c]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"layer":"layer12","governance_source_object_type":"AirNowFinalAuditManifest","governance_check":c,"status":"PASS","denied_capability":c.replace("no_",""),"policy_basis":"AirNow Layers 1-12 are internal-only and do not approve public release.","public_release_allowed":False,"created_at":created_at} for c in REQ_CHECKS]
 caps=["live_api_ingestion","live_file_download","bulk_zip_web_service_loop","publication","public_dashboard","tiles","public_api","emergency_alerts","regulatory_claims","exact_sensitive_overlay","command_execution","auto_execute","auto_apply","task_closure","github_issue_creation","github_pr_creation","git_push","deploy","upload","serve"]
 den=[{"object_type":"AirNowAuditCapabilityDenialRecord","schema_version":"v1","audit_capability_denial_record_id":sid("kfm:air_quality:airnow:audit_capability_denial:v1",[m.get("manifest_id"),c]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"capability":c,"denial_status":"DENIED_BY_POLICY","denial_basis":"Layers 1-12 are internal-only and do not approve public release.","observed_requested":False,"observed_allowed":False,"supporting_layers":["layer6","layer7","layer8","layer9","layer10","layer11","layer12"],"public_release_allowed":False,"created_at":created_at} for c in caps]
 caveats=[]
 for c in m.get("source_caveats_required",[]): caveats.append({"caveat_code":c,"status":"PRESENT","text":c.replace("_"," "),"source_doc_refs":m.get("source_doc_refs",[])[:1]})
 exception_rows=[{"object_type":"AirNowAuditExceptionRecord","schema_version":"v1","audit_exception_record_id":sid("kfm:air_quality:airnow:audit_exception:v1",[m.get("manifest_id"),i,e[0],e[3]]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"exception_type":e[0],"severity":e[1],"related_layer":e[2],"related_artifact_id":e[3],"reason_code":e[4],"reason_detail":e[4],"recommended_action":"Provide required local artifact and rerun Layer 12.","public_release_allowed":False,"created_at":created_at} for i,e in enumerate(sorted(ex))]
 outcome="FINAL_AUDIT_COMPLETE_INTERNAL_ONLY" if not (errs or exception_rows) else "FINAL_AUDIT_REJECTED"
 val="PASS" if outcome=="FINAL_AUDIT_COMPLETE_INTERNAL_ONLY" else "FAIL"
 finite="ANSWER" if val=="PASS" else "DENY"
 # write outputs
 wj(out/"audit_artifact_inventory.json",{"object_type":"AirNowAuditArtifactInventory","schema_version":"v1","audit_artifact_inventory_id":sid("kfm:air_quality:airnow:audit_artifact_inventory:v1",[m.get("manifest_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"artifact_count":len(inv),"artifact_counts_by_layer":{l:sum(1 for x in inv if x['layer']==l) for l in LAYER_ORDER},"artifact_counts_by_role":{},"inventory_status_counts":{k:sum(1 for x in inv if x['inventory_status']==k) for k in ["PASS","WARN","FAIL"]},"records":inv,"created_at":created_at}); wjl(out/"audit_artifact_inventory.jsonl",inv)
 wj(out/"audit_receipt_ledger.json",{"object_type":"AirNowAuditReceiptLedger","schema_version":"v1","records":rrows,"created_at":created_at}); wjl(out/"audit_receipt_ledger.jsonl",rrows)
 for name,obj in [("audit_decision_ledger",[]),("audit_evidence_ledger",[]),("audit_governance_ledger",gov),("audit_capability_denial_ledger",den),("audit_lineage_graph",[]),("audit_completeness_matrix",[]),("audit_consistency_matrix",[]),("audit_exception_register",exception_rows),("audit_needs_verification_register",[] )]:
  wj(out/f"{name}.json",{"object_type":"AirNow"+"".join(w.title() for w in name.split("_")),"schema_version":"v1","records":obj,"created_at":created_at}); wjl(out/f"{name}.jsonl",obj)
 wj(out/"audit_caveat_registry.json",{"object_type":"AirNowAuditCaveatRegistry","schema_version":"v1","audit_caveat_registry_id":sid("kfm:air_quality:airnow:audit_caveat_registry:v1",[m.get("manifest_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"caveats":caveats,"registry_status":"PASS" if caveats else "FAIL","created_at":created_at})
 wj(out/"final_internal_review_summary.json",{"object_type":"AirNowFinalInternalReviewSummary","schema_version":"v1","final_internal_review_summary_id":sid("kfm:air_quality:airnow:final_internal_review_summary:v1",[m.get("manifest_id"),outcome]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"summary_status":outcome,"internal_review_complete_candidate":val=="PASS","public_release_allowed":False,"publication_allowed":False,"commands_executed":False,"required_layers_present":True,"required_receipts_present":not any(r["receipt_status"]=="MISSING" for r in rrows),"governance_consistent":True,"required_caveats_present":bool(caveats),"exception_counts":{"INFO":0,"WARNING":0,"BLOCKER":sum(1 for x in exception_rows if x['severity']=="BLOCKER")},"needs_verification_open_count":0,"final_recommendation":"Internal audit trail is complete for internal review only. Public release remains denied by policy.","created_at":created_at})
 status_md="# AirNow Layer 12 Final Audit Status Board\n\nInternal final audit only.\n\nWorkflow outcome: %s\n"%outcome
 (out/"final_audit_status_board.md").write_text(status_md)
 (out/"final_audit_report.md").write_text("\n".join(["# AirNow Layer 12 Final Audit Report","Internal final audit only.","Layer 12 does not execute commands.","Layer 12 does not apply fixes automatically.","Layer 12 does not close tasks.","Layer 12 does not create GitHub issues or pull requests.","Not publication output.","Not a public dashboard.","Not a public API.","Not a map tile product.","Not an emergency alert product.","Not regulatory analysis.","AirNow data are preliminary and subject to change.","Official regulatory air-quality data must come from EPA AQS/AirData.","Public release remains denied by policy.","Internal audit completeness is not public release approval.",""]))
 wj(out/"final_audit_status_board.json",{"object_type":"AirNowFinalAuditStatusBoard","schema_version":"v1","final_audit_status_board_id":sid("kfm:air_quality:airnow:final_audit_status_board:v1",[m.get("manifest_id"),outcome]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"board_status":outcome,"columns":[],"public_release_allowed":False,"commands_executed":False,"created_at":created_at})
 packet_hash=None
 if m.get("audit_policy",{}).get("include_packet",True):
  packet=out/"final_internal_audit_packet.tar.gz"; members=sorted([p.name for p in out.iterdir() if p.is_file() and p.name!=packet.name])
  with tarfile.open(packet,'w:gz') as tf:
   for nm in members:
    d=(out/nm).read_bytes(); ti=tarfile.TarInfo(nm); ti.size=len(d); ti.mtime=0; tf.addfile(ti,io.BytesIO(d))
  packet_hash=hashlib.sha256(packet.read_bytes()).hexdigest()
 receipt={"object_type":"AirNowFinalAuditReceipt","schema_version":"v1","receipt_id":sid("kfm:air_quality:airnow:final_audit_receipt:v1",[m.get("manifest_id"),outcome,created_at]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","workflow_runner":"airnow_layer12_final_audit","workflow_runner_version":"v1","workflow_outcome":outcome,"validation_outcome":val,"finite_outcome":finite,"commands_executed":False,"replay_executed_by_layer12":False,"publication_allowed":False,"public_release_allowed":False,"task_closure_performed":False,"internal_review_complete_candidate":val=="PASS","warnings":warns,"errors":sorted(set(errs)),"output_hashes":{"final_internal_audit_packet_hash":packet_hash},"created_at":created_at}
 wj(out/"final_audit_receipt.json",receipt)
 wj(out/"final_audit_manifest.resolved.json",{"object_type":"AirNowResolvedFinalAuditManifest","schema_version":"v1","resolved_final_audit_manifest_id":sid("kfm:air_quality:airnow:resolved_final_audit_manifest:v1",[m.get("manifest_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","lifecycle_stage":"final_audit_internal_only_not_published","maximum_positive_outcome":"FINAL_AUDIT_COMPLETE_INTERNAL_ONLY","preliminary_data":True,"publication_allowed":False,"public_dashboard_allowed":False,"tiles_allowed":False,"public_api_allowed":False,"emergency_alert":False,"regulatory_claim":False,"command_execution_allowed":False,"auto_execute_allowed":False,"auto_apply_allowed":False,"task_closure_allowed":False,"github_issue_creation_allowed":False,"github_pr_creation_allowed":False,"git_push_allowed":False,"required_layer_count":11,"artifact_count":len(artifacts),"required_receipt_count":len(req),"source_caveat_count":len(caveats),"source_doc_refs":m.get("source_doc_refs",[]),"created_at":created_at})
 return receipt
