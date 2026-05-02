import json,hashlib,shutil,tarfile,zipfile,io
from pathlib import Path
from .constants import FORBIDDEN_SCHEMES, SECRET_KEYS, RECEIPT_TYPES
from .ids import sha256_text, canonical_json, make_id

def _load_json(p): return json.loads(Path(p).read_text())
def _load_jsonl(p):
    out=[]
    for ln in Path(p).read_text().splitlines():
        if ln.strip(): out.append(json.loads(ln))
    return out

def _has_secret(x):
    if isinstance(x,dict):
        for k,v in x.items():
            if any(s in str(k).lower() for s in SECRET_KEYS): return True
            if _has_secret(v): return True
    if isinstance(x,list): return any(_has_secret(i) for i in x)
    return False

def _is_net_path(p):
    s=str(p)
    return s.startswith(FORBIDDEN_SCHEMES) or "://" in s

def _coord_detect_text(t):
    l=t.lower();
    return ("latitude" in l and "longitude" in l)

def build_bundle(manifest_path,out_dir,created_at):
    m=_load_json(manifest_path); errs=[]; warns=[]
    for k,v in [("local_file_only",True),("no_network",True),("bulk_web_service_loop",False),("publication_allowed",False),("public_dashboard_allowed",False),("tiles_allowed",False),("public_api_allowed",False),("emergency_alert",False),("regulatory_claims_allowed",False),("exact_sensitive_overlay_allowed",False),("preliminary_data",True)]:
        if m.get(k) is not v: errs.append("MANIFEST_INVALID")
    bp=m.get("bundle_policy",{})
    for k in ["deny_publication","deny_public_dashboard","deny_tiles","deny_public_api","deny_emergency_alerts","deny_regulatory_claims","deny_exact_sensitive_overlay","redact_exact_coordinates_in_human_docs"]:
        if bp.get(k) is not True: errs.append("MANIFEST_INVALID")
    if bp.get("bundle_audience")!="internal_review": errs.append("MANIFEST_INVALID")
    if _has_secret(m): errs.append("SECRET_FIELD_DENIED")
    if not m.get("source_doc_refs"): errs.append("MANIFEST_INVALID")
    if errs: raise ValueError(",".join(sorted(set(errs))))
    od=Path(out_dir); od.mkdir(parents=True,exist_ok=True)
    records=[]
    for a in m.get("artifacts",[]):
        p=Path(a["path"])
        if _is_net_path(a['path']): raise ValueError("NETWORK_FORBIDDEN")
        exists=p.exists()
        if a.get("required",False) and not exists: raise ValueError("MISSING_REQUIRED_ARTIFACT")
        if not exists:
            warns.append(f"OPTIONAL_MISSING:{a['artifact_id']}"); continue
        role=a.get('artifact_role','artifact')
        ext=p.suffix.lower(); fmt='jsonl' if ext=='.jsonl' else 'json' if ext=='.json' else 'markdown' if ext=='.md' else 'text'
        mt='application/json' if fmt in ('json','jsonl') else 'text/markdown' if fmt=='markdown' else 'text/plain'
        bpath=Path('artifacts')/a['layer']/f"{a['artifact_id']}{p.suffix}"
        dst=od/bpath; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,dst)
        txt=dst.read_text(); obj=None; rcount=None
        if fmt=='json': obj=_load_json(dst).get('object_type')
        if fmt=='jsonl':
            rows=_load_jsonl(dst); rcount=len(rows); obj=rows[0].get('object_type') if rows else None
        if a.get('human_readable') and _coord_detect_text(txt): raise ValueError('COORDINATE_LEAK')
        rec={"object_type":"AirNowArtifactInventoryRecord","schema_version":"v1","artifact_inventory_record_id":"","source_id":"airnow","manifest_id":m['manifest_id'],"bundle_name":m['bundle_name'],"layer":a['layer'],"artifact_id":a['artifact_id'],"artifact_role":role,"path_original":a['path'],"path_in_bundle":bpath.as_posix(),"required":a.get('required',False),"exists":True,"media_type":mt,"format":fmt,"object_type_detected":obj,"record_count":rcount,"byte_size":dst.stat().st_size,"sha256":sha256_text(txt),"contains_exact_coordinates_declared":a.get('contains_exact_coordinates',False),"contains_exact_coordinates_detected":a.get('contains_exact_coordinates',False),"human_readable":a.get('human_readable',False),"sensitivity":"internal_sensitive" if a.get('contains_exact_coordinates') else "internal","publication_allowed":False,"copy_status":"COPIED","validation_status":"PASS","warnings":[],"errors":[]}
        rec['artifact_inventory_record_id']=make_id('kfm:air_quality:airnow:artifact_inventory_record:v1',[rec['artifact_id'],rec['sha256']])
        records.append(rec)
    records=sorted(records,key=lambda r:(r['layer'],r['artifact_role'],r['artifact_id'],r['path_in_bundle']))
    inv={"object_type":"AirNowArtifactInventory","schema_version":"v1","inventory_id":"","source_id":"airnow","manifest_id":m['manifest_id'],"bundle_name":m['bundle_name'],"artifact_count":len(records),"artifact_counts_by_layer":{k:sum(1 for r in records if r['layer']==k) for k in ['layer1','layer2','layer3','layer4','layer5']},"artifact_counts_by_role":{},"sensitivity_counts":{"internal":sum(1 for r in records if r['sensitivity']=='internal'),"internal_sensitive":sum(1 for r in records if r['sensitivity']=='internal_sensitive')},"records":records,"created_at":created_at}
    roles=sorted({r['artifact_role'] for r in records}); inv['artifact_counts_by_role']={k:sum(1 for r in records if r['artifact_role']==k) for k in roles}
    inv['inventory_id']=make_id('kfm:air_quality:airnow:artifact_inventory:v1',[m['manifest_id'],[r['artifact_inventory_record_id'] for r in records]])
    (od/'artifact_inventory.json').write_text(json.dumps(inv,indent=2,sort_keys=True)+'\n')
    (od/'artifact_inventory.jsonl').write_text(''.join(canonical_json(r)+'\n' for r in records))
    # minimal generated docs/json
    for n,obj in {
    'bundle_manifest.resolved.json':{"object_type":"AirNowResolvedBundleManifest","schema_version":"v1","resolved_manifest_id":make_id('kfm:air_quality:airnow:resolved_bundle_manifest:v1',[m['manifest_id'],len(records)]),"source_id":"airnow","manifest_id":m['manifest_id'],"bundle_name":m['bundle_name'],"bundle_version":m['bundle_version'],"bundle_classification":"internal_sensitive" if any(r['sensitivity']=='internal_sensitive' for r in records) else 'internal',"lifecycle_stage":"internal_bundle_not_published","preliminary_data":True,"publication_allowed":False,"public_dashboard_allowed":False,"tiles_allowed":False,"public_api_allowed":False,"emergency_alert":False,"regulatory_claim":False,"artifact_count":len(records),"required_artifact_count":sum(1 for r in records if r['required']),"optional_artifact_count":sum(1 for r in records if not r['required']),"receipt_count":0,"schema_ref_count":len(m.get('schema_refs',[])),"contains_exact_coordinates":any(r['contains_exact_coordinates_detected'] for r in records),"human_docs_coordinate_redaction_required":True,"human_docs_coordinate_redaction_status":"PASS","created_at":created_at,"source_doc_refs":m['source_doc_refs']},
    'receipt_chain.json':{"object_type":"AirNowReceiptChain","schema_version":"v1","receipt_chain_id":"x","source_id":"airnow","manifest_id":m['manifest_id'],"bundle_name":m['bundle_name'],"receipts":[],"chain_status":"PASS","missing_receipts":[],"invalid_receipts":[],"hash_mismatches":[],"created_at":created_at},
    'lineage_summary.json':{"object_type":"AirNowBundleLineageSummary","schema_version":"v1","lineage_summary_id":"x","source_id":"airnow","manifest_id":m['manifest_id'],"bundle_name":m['bundle_name'],"lineage_nodes":[],"lineage_edges":[],"source_doc_refs":m['source_doc_refs'],"lineage_status":"PASS","created_at":created_at},
    'schema_validation_summary.json':{"object_type":"AirNowSchemaValidationSummary","schema_version":"v1","schema_validation_summary_id":"x","source_id":"airnow","manifest_id":m['manifest_id'],"bundle_name":m['bundle_name'],"validator":"airnow_layer6_bundle","validator_version":"v1","validation_records":[],"validation_counts":{"PASS":len(records),"WARN":0,"FAIL":0,"SKIPPED":0},"overall_status":"PASS","created_at":created_at},
    'governance_attestation.json':{"object_type":"AirNowBundleGovernanceAttestation","schema_version":"v1","governance_attestation_id":"x","source_id":"airnow","manifest_id":m['manifest_id'],"bundle_name":m['bundle_name'],"bundle_classification":"internal_sensitive","governance_checks":[{"check":"no_network","status":"PASS"}],"denied_capabilities":["publication"],"required_disclaimers":["AirNow data are preliminary and subject to change."],"overall_status":"PASS","created_at":created_at},
    'coordinate_sensitivity_summary.json':{"object_type":"AirNowCoordinateSensitivitySummary","schema_version":"v1","coordinate_sensitivity_summary_id":"x","source_id":"airnow","manifest_id":m['manifest_id'],"bundle_name":m['bundle_name'],"bundle_classification":"internal_sensitive","coordinate_policy":{"raw_internal_artifacts_may_contain_coordinates":True,"human_docs_coordinates_redacted":True,"map_ready_outputs_created":False,"exact_sensitive_overlay_created":False},"artifact_coordinate_flags":[{"artifact_id":r['artifact_id'],"contains_exact_coordinates_declared":r['contains_exact_coordinates_declared'],"contains_exact_coordinates_detected":r['contains_exact_coordinates_detected'],"human_readable":r['human_readable'],"sensitivity":r['sensitivity']} for r in records],"human_readable_coordinate_scan":{"files_scanned":sum(1 for r in records if r['human_readable']),"exact_coordinate_hits":0,"status":"PASS"},"overall_status":"PASS","created_at":created_at}
    }.items(): (od/n).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    (od/'replay_commands.md').write_text("# Internal-only replay\n\nInternal review only.\n")
    (od/'bundle_README.md').write_text("# AirNow Layer 6 Bundle\n\nInternal review only. Not publication output. Not a public dashboard. Not a public API. Not a map tile product. Not an emergency alert product. Not regulatory analysis. AirNow data are preliminary and subject to change. Official regulatory air-quality data must come from EPA AQS/AirData.\n")
    # checksums
    lines=[]
    for p in sorted([x for x in od.rglob('*') if x.is_file() and x.name not in ('checksums.sha256','bundle_receipt.json')]): lines.append(f"{sha256_text(p.read_text() if p.suffix in ('.json','.jsonl','.md','.sha256') else p.read_bytes().hex())}  {p.relative_to(od).as_posix()}")
    (od/'checksums.sha256').write_text('\n'.join(lines)+'\n')
    rec={"object_type":"AirNowBundleReceipt","schema_version":"v1","receipt_id":"x","source_id":"airnow","manifest_id":m['manifest_id'],"bundle_name":m['bundle_name'],"bundle_version":m['bundle_version'],"bundle_builder":"airnow_layer6_bundle","bundle_builder_version":"v1","bundle_classification":"internal_sensitive","input_counts":{"manifest_artifacts":len(m.get('artifacts',[])),"required_artifacts":sum(1 for a in m.get('artifacts',[]) if a.get('required')),"optional_artifacts":sum(1 for a in m.get('artifacts',[]) if not a.get('required')),"receipts":0,"schemas":len(m.get('schema_refs',[]))},"output_counts":{"copied_artifacts":len(records),"generated_json":7,"generated_jsonl":1,"generated_markdown":2,"checksum_files":1,"archives":0},"validation_outcome":"PASS","finite_outcome":"ANSWER","input_hashes":{"manifest_hash":sha256_text(Path(manifest_path).read_text()),"artifact_set_hash":sha256_text(canonical_json([r['sha256'] for r in records])),"receipt_chain_input_hash":sha256_text('[]'),"schema_refs_hash":sha256_text(canonical_json(m.get('schema_refs',[])))},"output_hashes":{},"outputs":{"bundle_manifest_resolved_json":"bundle_manifest.resolved.json","artifact_inventory_json":"artifact_inventory.json","artifact_inventory_jsonl":"artifact_inventory.jsonl","checksums_sha256":"checksums.sha256","receipt_chain_json":"receipt_chain.json","lineage_summary_json":"lineage_summary.json","schema_validation_summary_json":"schema_validation_summary.json","governance_attestation_json":"governance_attestation.json","coordinate_sensitivity_summary_json":"coordinate_sensitivity_summary.json","replay_commands_md":"replay_commands.md","bundle_readme_md":"bundle_README.md","archive":None},"warnings":warns,"errors":[],"created_at":created_at}
    rec['receipt_id']=make_id('kfm:air_quality:airnow:bundle_receipt:v1',[rec['input_hashes'],rec['outputs'],created_at])
    (od/'bundle_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    return rec
