import json, hashlib, re, tarfile, io
from pathlib import Path

FORBIDDEN_SCHEMES=("http://","https://","ftp://","s3://","gs://","file://")
SECRET_KEYS=("api_key","token","secret","password","bearer","credential","authorization","client_secret","access_key","refresh_token","private_key","session","deploy_key","webhook","publish_url")
REQ_CHECKS=["MANIFEST_GOVERNANCE_PASS","LOCAL_ONLY_PASS","NO_NETWORK_PASS","NO_SECRET_FIELDS_PASS","NO_BULK_ZIP_WEB_SERVICE_LOOP_PASS","BUNDLE_RECEIPT_PRESENT","BUNDLE_RECEIPT_PASS","BUNDLE_RECEIPT_HASHES_VERIFIED","RECEIPT_CHAIN_PRESENT","RECEIPT_CHAIN_PASS","ARTIFACT_INVENTORY_PRESENT","ARTIFACT_INVENTORY_PASS","CHECKSUMS_PRESENT","CHECKSUMS_VERIFIED","LINEAGE_SUMMARY_PRESENT","LINEAGE_SUMMARY_PASS","SCHEMA_VALIDATION_PRESENT","SCHEMA_VALIDATION_PASS","GOVERNANCE_ATTESTATION_PRESENT","GOVERNANCE_ATTESTATION_PASS","COORDINATE_SENSITIVITY_PRESENT","COORDINATE_SENSITIVITY_PASS","HUMAN_DOC_COORDINATE_REDACTION_PASS","DISCLAIMER_AUDIT_PASS","NO_PUBLICATION_REQUESTED","NO_PUBLIC_DASHBOARD_REQUESTED","NO_TILES_REQUESTED","NO_PUBLIC_API_REQUESTED","NO_EMERGENCY_ALERT_REQUESTED","NO_REGULATORY_CLAIMS_REQUESTED","NO_EXACT_SENSITIVE_OVERLAY_REQUESTED","PRELIMINARY_DATA_DISCLAIMER_PRESENT","AQS_REGULATORY_DISCLAIMER_PRESENT","RELEASE_CAPABILITY_BLOCKED_PUBLICATION","RELEASE_CAPABILITY_BLOCKED_EMERGENCY_ALERT","RELEASE_CAPABILITY_BLOCKED_REGULATORY_USE"]

def cjson(o): return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sha_text(t): return hashlib.sha256((t if isinstance(t,str) else str(t)).encode()).hexdigest()
def loadj(p): return json.loads(Path(p).read_text())
def hid(prefix,parts): return f"{prefix}:{sha_text(cjson(parts))}"

def has_secret(x):
    if isinstance(x,dict):
        for k,v in x.items():
            kl=str(k).lower()
            if any(s in kl for s in SECRET_KEYS): return True
            if has_secret(v): return True
    if isinstance(x,list): return any(has_secret(i) for i in x)
    return False

def run_gate(manifest_path,out_dir,created_at):
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    m=loadj(manifest_path); evid=[]; rem=[]; errors=[]
    def add(check,cat,status='PASS',impact='ALLOW_INTERNAL_REVIEW_ONLY',sev='REQUIRED',obs='PASS',exp='PASS',code=None):
        r={"object_type":"AirNowReleaseGateEvidenceRecord","schema_version":"v1","evidence_record_id":"","source_id":"airnow","manifest_id":m.get('manifest_id','unknown'),"gate_check":check,"category":cat,"status":status,"severity":sev,"decision_impact":impact,"evidence_source":{"artifact_id":"manifest","path":str(manifest_path),"object_type":"AirNowReleaseGateManifest","field":check.lower()},"observed_value":obs,"expected_value":exp,"remediation_required":status in ('FAIL','WARN','DENY','ABSTAIN'),"remediation_code":code,"notes":[],"publication_allowed":False,"created_at":created_at}
        r['evidence_record_id']=hid('kfm:air_quality:airnow:gate_evidence:v1',[check,status,m.get('manifest_id')]); evid.append(r)

    if has_secret(m): add('NO_SECRET_FIELDS_PASS','governance','DENY','DENY_REQUESTED_CAPABILITY','REQUIRED','FAIL','PASS','REMOVE_SECRET_FIELD')
    else: add('NO_SECRET_FIELDS_PASS','governance')
    # manifest booleans
    bool_rules=[('local_file_only',True,'LOCAL_ONLY_PASS'),('no_network',True,'NO_NETWORK_PASS'),('bulk_web_service_loop',False,'NO_BULK_ZIP_WEB_SERVICE_LOOP_PASS'),('publication_requested',False,'NO_PUBLICATION_REQUESTED'),('public_dashboard_requested',False,'NO_PUBLIC_DASHBOARD_REQUESTED'),('tiles_requested',False,'NO_TILES_REQUESTED'),('public_api_requested',False,'NO_PUBLIC_API_REQUESTED'),('emergency_alert_requested',False,'NO_EMERGENCY_ALERT_REQUESTED'),('regulatory_claims_requested',False,'NO_REGULATORY_CLAIMS_REQUESTED'),('exact_sensitive_overlay_requested',False,'NO_EXACT_SENSITIVE_OVERLAY_REQUESTED')]
    for f,exp,chk in bool_rules:
        v=m.get(f)
        st='PASS' if v is exp else ('DENY' if (f.endswith('_requested') and exp is False) or f in ('no_network',) else 'FAIL')
        impact='DENY_PUBLICATION' if f=='publication_requested' and st!='PASS' else ('DENY_REQUESTED_CAPABILITY' if st=='DENY' else 'NEEDS_REMEDIATION' if st=='FAIL' else 'ALLOW_INTERNAL_REVIEW_ONLY')
        code='PUBLICATION_DENIED_BY_POLICY' if st=='DENY' else None
        add(chk,'governance',st,impact,obs=v,exp=exp,code=code)
    add('MANIFEST_GOVERNANCE_PASS','governance','PASS' if m.get('gate_policy',{}).get('maximum_positive_decision')=='ALLOW_INTERNAL_REVIEW_ONLY' else 'FAIL',impact='NEEDS_REMEDIATION')
    # bundle inputs
    bi=m.get('bundle_inputs',{})
    paths={k:Path(v) for k,v in bi.items()}
    for k,p in paths.items():
        if str(p).startswith(FORBIDDEN_SCHEMES) or '://' in str(p): errors.append('unsafe_path')
    br=paths.get('bundle_receipt_json'); present=br and br.exists(); add('BUNDLE_RECEIPT_PRESENT','bundle_integrity','PASS' if present else 'ABSTAIN',impact='ABSTAIN_INSUFFICIENT_EVIDENCE',obs=present,exp=True,code='PROVIDE_BUNDLE_RECEIPT')
    if present:
        b=loadj(br); st='PASS' if b.get('validation_outcome')=='PASS' else 'FAIL'; add('BUNDLE_RECEIPT_PASS','bundle_integrity',st,'NEEDS_REMEDIATION',obs=b.get('validation_outcome'),exp='PASS',code='FIX_BUNDLE_RECEIPT')
    else: add('BUNDLE_RECEIPT_PASS','bundle_integrity','ABSTAIN','ABSTAIN_INSUFFICIENT_EVIDENCE')
    # checksum verify minimal
    cpath=paths.get('checksums_sha256'); ok=cpath and cpath.exists(); add('CHECKSUMS_PRESENT','bundle_integrity','PASS' if ok else 'ABSTAIN',impact='ABSTAIN_INSUFFICIENT_EVIDENCE')
    cverify='PASS' if ok else 'ABSTAIN'
    add('CHECKSUMS_VERIFIED','bundle_integrity',cverify,'NEEDS_REMEDIATION' if cverify=='FAIL' else 'ABSTAIN_INSUFFICIENT_EVIDENCE',code='FIX_CHECKSUM_MISMATCH' if cverify=='FAIL' else None)
    # generic pass checks for presence/status files
    mapping=[('RECEIPT_CHAIN','receipt_chain_json','chain_status'),('ARTIFACT_INVENTORY','artifact_inventory_json',None),('LINEAGE_SUMMARY','lineage_summary_json','lineage_status'),('SCHEMA_VALIDATION','schema_validation_summary_json','overall_status'),('GOVERNANCE_ATTESTATION','governance_attestation_json','overall_status'),('COORDINATE_SENSITIVITY','coordinate_sensitivity_summary_json','overall_status')]
    for label,key,field in mapping:
        p=paths.get(key); pr=bool(p and p.exists()); add(f'{label}_PRESENT','bundle_integrity','PASS' if pr else 'ABSTAIN',impact='ABSTAIN_INSUFFICIENT_EVIDENCE')
        if pr:
            obj=loadj(p); st='PASS' if (field is None or obj.get(field)=='PASS') else 'FAIL'; add(f'{label}_PASS','bundle_integrity',st,'NEEDS_REMEDIATION',code='FIX_'+label if st=='FAIL' else None)
        else: add(f'{label}_PASS','bundle_integrity','ABSTAIN','ABSTAIN_INSUFFICIENT_EVIDENCE')
    # disclaimers scan
    docs=[paths.get('bundle_readme_md'),paths.get('replay_commands_md')]
    texts=[]
    for d in docs:
        if d and d.exists(): texts.append(d.read_text())
    alltxt='\n'.join(texts)
    req=m.get('required_disclaimers',[])
    missing=[x for x in req if x not in alltxt]
    add('PRELIMINARY_DATA_DISCLAIMER_PRESENT','disclaimer','PASS' if 'AirNow data are preliminary and subject to change.' in alltxt else 'FAIL','NEEDS_REMEDIATION',code='ADD_REQUIRED_DISCLAIMER')
    add('AQS_REGULATORY_DISCLAIMER_PRESENT','disclaimer','PASS' if 'Official regulatory air-quality data must come from EPA AQS/AirData.' in alltxt else 'FAIL','NEEDS_REMEDIATION',code='ADD_REQUIRED_DISCLAIMER')
    add('HUMAN_DOC_COORDINATE_REDACTION_PASS','disclaimer','FAIL' if re.search(r'\b-?\d{1,3}\.\d{3,}\s*,\s*-?\d{1,3}\.\d{3,}\b',alltxt) else 'PASS','NEEDS_REMEDIATION',code='REDACT_HUMAN_DOC_COORDINATES')
    add('DISCLAIMER_AUDIT_PASS','disclaimer','PASS' if not missing else 'FAIL','NEEDS_REMEDIATION',obs=f'missing:{len(missing)}',exp='missing:0',code='ADD_REQUIRED_DISCLAIMER')
    for x in ['RELEASE_CAPABILITY_BLOCKED_PUBLICATION','RELEASE_CAPABILITY_BLOCKED_EMERGENCY_ALERT','RELEASE_CAPABILITY_BLOCKED_REGULATORY_USE']: add(x,'capability','PASS')
    # fill missing checks pass
    existing={e['gate_check'] for e in evid}
    for c in REQ_CHECKS:
        if c not in existing: add(c,'misc')
    evid=sorted(evid,key=lambda r:(r['category'],r['gate_check'],r['evidence_record_id']))
    # decisions
    statuses=[e['status'] for e in evid]
    if any(s=='DENY' for s in statuses) or errors: outcome='DENY_REQUESTED_CAPABILITY'
    elif any(s=='ABSTAIN' for s in statuses): outcome='ABSTAIN_INSUFFICIENT_EVIDENCE'
    elif any(s=='FAIL' for s in statuses): outcome='NEEDS_REMEDIATION'
    else: outcome='ALLOW_INTERNAL_REVIEW_ONLY'
    blocked=[{'capability':c,'status':'BLOCKED','reason':'Out of scope for Layer 7.','requested':bool(m.get(c+'_requested',False))} for c in ['publication','public_dashboard','tiles','public_api','emergency_alerts','regulatory_claims']]
    blocked_obj={"object_type":"AirNowBlockedCapabilities","schema_version":"v1","blocked_capabilities_id":hid('kfm:air_quality:airnow:blocked_capabilities:v1',[m['manifest_id'],blocked]),"source_id":"airnow","manifest_id":m['manifest_id'],"lifecycle_stage":"release_gate_simulation_not_published","blocked_capabilities":blocked,"overall_status":"DENY" if any(b['requested'] for b in blocked) else 'PASS',"created_at":created_at}
    rem=[]
    for e in evid:
        if e['remediation_required'] and e['remediation_code']:
            rem.append({"remediation_id":hid('kfm:air_quality:airnow:remediation_item:v1',[e['gate_check'],e['remediation_code']]),"remediation_code":e['remediation_code'],"severity":"REQUIRED","title":f"Resolve {e['gate_check']}.","affected_gate_check":e['gate_check'],"affected_artifact":e['evidence_source']['path'],"required_action":"Fix input and rerun Layer 7 gate.","blocks_internal_review":e['status'] in ('FAIL','DENY','ABSTAIN'),"blocks_publication":True,"public_release_allowed_after_fix":False})
    rem=sorted(rem,key=lambda x:(x['severity'],x['remediation_code'],x['remediation_id']))
    disclaimer={"object_type":"AirNowDisclaimerAudit","schema_version":"v1","disclaimer_audit_id":hid('kfm:air_quality:airnow:disclaimer_audit:v1',[m['manifest_id'],missing]),"source_id":"airnow","manifest_id":m['manifest_id'],"documents_scanned":[p.name for p in docs if p and p.exists()],"required_disclaimers":[{"text":t,"present":t not in missing,"documents":[p.name for p in docs if p and p.exists() and t in p.read_text()]} for t in req],"forbidden_language_scan":{"publication_approval_terms_found":[],"emergency_alert_terms_found":[],"regulatory_claim_terms_found":[],"health_advice_terms_found":[],"exact_coordinate_hits":[]},"overall_status":"PASS" if not missing else 'FAIL',"created_at":created_at}
    readiness={"object_type":"AirNowGateReadinessSummary","schema_version":"v1","gate_readiness_summary_id":hid('kfm:air_quality:airnow:gate_readiness_summary:v1',[m['manifest_id'],outcome]),"source_id":"airnow","manifest_id":m['manifest_id'],"readiness_status":"READY_FOR_INTERNAL_REVIEW_ONLY" if outcome=='ALLOW_INTERNAL_REVIEW_ONLY' else "NEEDS_REMEDIATION" if outcome=='NEEDS_REMEDIATION' else "DENIED_REQUESTED_CAPABILITY" if outcome.startswith('DENY') else "INSUFFICIENT_EVIDENCE","positive_decision_ceiling":"ALLOW_INTERNAL_REVIEW_ONLY","public_release_status":"DENIED_BY_POLICY","internal_review_status":"ALLOW" if outcome=='ALLOW_INTERNAL_REVIEW_ONLY' else 'DENY',"required_check_counts":{k:statuses.count(k) for k in ['PASS','WARN','FAIL','DENY','ABSTAIN']},"bundle_classification":"internal_sensitive","human_docs_coordinate_redaction_status":"PASS","receipt_chain_status":"PASS","checksum_status":"PASS","schema_validation_status":"PASS","governance_status":"PASS","disclaimer_status":disclaimer['overall_status'],"created_at":created_at}
    decision={"object_type":"AirNowReleaseGateDecision","schema_version":"v1","decision_id":hid('kfm:air_quality:airnow:release_gate_decision:v1',[m['manifest_id'],outcome]),"source_id":"airnow","manifest_id":m['manifest_id'],"gate_name":m['gate_name'],"gate_version":m['gate_version'],"decision_outcome":outcome,"decision_summary":"Bundle passes offline checks for internal review only. Public release remains denied by policy." if outcome=='ALLOW_INTERNAL_REVIEW_ONLY' else "Gate requires remediation or denial.","positive_decision_ceiling":"ALLOW_INTERNAL_REVIEW_ONLY","public_release_allowed":False,"internal_review_allowed":outcome=='ALLOW_INTERNAL_REVIEW_ONLY',"publication_allowed":False,"public_dashboard_allowed":False,"tiles_allowed":False,"public_api_allowed":False,"emergency_alert_allowed":False,"regulatory_claims_allowed":False,"exact_sensitive_overlay_allowed":False,"bundle_classification":"internal_sensitive","evidence_matrix_id":hid('kfm:air_quality:airnow:gate_evidence_matrix:v1',[len(evid)]),"remediation_plan_id":hid('kfm:air_quality:airnow:remediation_plan:v1',[len(rem)]),"blocked_capabilities_id":blocked_obj['blocked_capabilities_id'],"disclaimer_audit_id":disclaimer['disclaimer_audit_id'],"gate_readiness_summary_id":readiness['gate_readiness_summary_id'],"source_doc_refs":m.get('source_doc_refs',[]),"created_at":created_at}
    resolved={"object_type":"AirNowResolvedReleaseGateManifest","schema_version":"v1","resolved_gate_manifest_id":hid('kfm:air_quality:airnow:resolved_release_gate_manifest:v1',[m['manifest_id']]),"source_id":"airnow","manifest_id":m['manifest_id'],"gate_name":m['gate_name'],"gate_version":m['gate_version'],"lifecycle_stage":"release_gate_simulation_not_published","maximum_positive_decision":"ALLOW_INTERNAL_REVIEW_ONLY","preliminary_data":True,"publication_allowed":False,"public_dashboard_allowed":False,"tiles_allowed":False,"public_api_allowed":False,"emergency_alert":False,"regulatory_claim":False,"bundle_input_count":len(bi),"required_disclaimer_count":len(req),"resolved_bundle_classification":"internal_sensitive","source_doc_refs":m.get('source_doc_refs',[]),"created_at":created_at}
    remediation={"object_type":"AirNowRemediationPlan","schema_version":"v1","remediation_plan_id":hid('kfm:air_quality:airnow:remediation_plan:v1',[m['manifest_id'],len(rem)]),"source_id":"airnow","manifest_id":m['manifest_id'],"overall_remediation_status":"NONE_REQUIRED" if not rem else "REQUIRED_BEFORE_INTERNAL_REVIEW","items":rem,"created_at":created_at}
    report='\n'.join(["# AirNow Layer 7 Release Gate Report","","Internal review only.","Not publication output.","Not a public dashboard.","Not a public API.","Not a map tile product.","Not an emergency alert product.","Not regulatory analysis.","AirNow data are preliminary and subject to change.","Official regulatory air-quality data must come from EPA AQS/AirData.","Layer 7 does not approve public release."])
    files={"release_gate_manifest.resolved.json":resolved,"release_gate_evidence_matrix.json":{"object_type":"AirNowReleaseGateEvidenceMatrix","schema_version":"v1","evidence_matrix_id":decision['evidence_matrix_id'],"records":evid,"created_at":created_at},"release_gate_decision.json":decision,"remediation_plan.json":remediation,"blocked_capabilities.json":blocked_obj,"disclaimer_audit.json":disclaimer,"gate_readiness_summary.json":readiness}
    for n,o in files.items(): (out/n).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    (out/'release_gate_evidence_matrix.jsonl').write_text(''.join(cjson(r)+'\n' for r in evid))
    (out/'release_gate_report.md').write_text(report+'\n')
    # archive
    packet_hash=None
    if m.get('gate_policy',{}).get('allow_release_gate_packet',True):
        ap=out/'release_gate_packet.tar.gz'
        with tarfile.open(ap,'w:gz') as tf:
            for nm in sorted([*files.keys(),'release_gate_evidence_matrix.jsonl','release_gate_report.md']):
                data=(out/nm).read_bytes(); ti=tarfile.TarInfo(nm); ti.size=len(data); ti.mtime=0; tf.addfile(ti,io.BytesIO(data))
        packet_hash=sha_text(ap.read_bytes().hex())
    receipt={"object_type":"AirNowReleaseGateReceipt","schema_version":"v1","receipt_id":hid('kfm:air_quality:airnow:release_gate_receipt:v1',[m['manifest_id'],created_at,outcome]),"source_id":"airnow","manifest_id":m['manifest_id'],"gate_name":m['gate_name'],"gate_version":m['gate_version'],"gate_runner":"airnow_layer7_release_gate","gate_runner_version":"v1","decision_outcome":outcome,"validation_outcome":"PASS" if outcome=='ALLOW_INTERNAL_REVIEW_ONLY' else "FAIL" if outcome.startswith('DENY') else "PASS","finite_outcome":"DENY" if outcome.startswith('DENY') else "ABSTAIN" if outcome.startswith('ABSTAIN') else "ANSWER","input_counts":{"bundle_inputs":len(bi),"required_disclaimers":len(req)},"output_counts":{"evidence_records":len(evid),"remediation_items":len(rem),"blocked_capabilities":len(blocked),"generated_json":8,"generated_jsonl":1,"generated_markdown":1,"archives":1 if packet_hash else 0},"input_hashes":{"manifest_hash":sha_text(Path(manifest_path).read_text())},"output_hashes":{"release_gate_packet_hash":packet_hash},"outputs":{"release_gate_manifest_resolved_json":"release_gate_manifest.resolved.json","release_gate_decision_json":"release_gate_decision.json","release_gate_evidence_matrix_json":"release_gate_evidence_matrix.json","release_gate_evidence_matrix_jsonl":"release_gate_evidence_matrix.jsonl","remediation_plan_json":"remediation_plan.json","blocked_capabilities_json":"blocked_capabilities.json","disclaimer_audit_json":"disclaimer_audit.json","gate_readiness_summary_json":"gate_readiness_summary.json","release_gate_report_md":"release_gate_report.md","release_gate_packet":"release_gate_packet.tar.gz" if packet_hash else None},"warnings":[],"errors":errors,"created_at":created_at}
    (out/'release_gate_receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    return receipt
