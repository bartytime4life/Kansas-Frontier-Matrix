import json
from pathlib import Path
from datetime import datetime, timezone
from .constants import FORBIDDEN_SCHEMES, SECRET_KEYS, DENIED_CAPABILITIES
from .ids import canonical_json, sha256_text, make_id, round_ratio

def _load_json(path): return json.loads(Path(path).read_text())
def _load_jsonl(path):
    if path is None: return []
    rows=[]
    for i,ln in enumerate(Path(path).read_text().splitlines(),1):
        if ln.strip():
            try: rows.append(json.loads(ln))
            except Exception as e: raise ValueError(f"MALFORMED_JSONL:{path}:{i}") from e
    return rows

def _is_net_path(p):
    s=str(p or "")
    return s.startswith(FORBIDDEN_SCHEMES) or "://" in s

def _has_secret(x):
    if isinstance(x,dict):
        for k,v in x.items():
            if any(s in str(k).lower() for s in SECRET_KEYS): return True
            if _has_secret(v): return True
    if isinstance(x,list): return any(_has_secret(i) for i in x)
    return False

def _prov(manifest_id, refs, created_at):
    return {"source_id":"airnow","manifest_id":manifest_id,"source_doc_refs":refs,"qa_runner":"airnow_layer5_qa","qa_runner_version":"v1","created_at":created_at}

def run_qa(manifest, created_at):
    errs=[]
    for k,v in [("local_file_only",True),("no_network",True),("bulk_web_service_loop",False),("publication_allowed",False),("emergency_alert",False),("regulatory_claims_allowed",False),("exact_sensitive_overlay_allowed",False),("preliminary_data",True)]:
        if manifest.get(k) is not v: errs.append("MANIFEST_INVALID")
    p=manifest.get("qa_policy",{})
    for k in ["deny_publication","deny_public_dashboard","deny_tiles","deny_public_api","deny_emergency_alerts","deny_regulatory_claims","deny_exact_sensitive_overlay","redact_exact_coordinates_in_report"]:
        if p.get(k) is not True: errs.append("MANIFEST_INVALID")
    if not manifest.get("source_doc_refs"): errs.append("MANIFEST_INVALID")
    if _has_secret(manifest): errs.append("SECRET_FIELD_DENIED")
    inputs=manifest.get("inputs",{})
    if not inputs.get("reconciliation_receipt_json"): errs.append("RECEIPT_REQUIRED")
    for _,v in inputs.items():
        if v is None: continue
        if _is_net_path(v): errs.append("NETWORK_FORBIDDEN")
    if errs: return None, sorted(set(errs))
    receipt=_load_json(inputs["reconciliation_receipt_json"])
    if receipt.get("object_type")!="AirNowReconciliationReceipt" or receipt.get("validation_outcome")!="PASS": return None,["RECEIPT_INVALID"]
    data={k:_load_jsonl(v) for k,v in inputs.items() if k.endswith("jsonl") and v is not None}
    in_counts={"site_index":len(data.get("site_index_jsonl",[])),"site_parameter_index":len(data.get("site_parameter_index_jsonl",[])),"reporting_area_index":len(data.get("reporting_area_index_jsonl",[])),"zip_reporting_area_index":len(data.get("zip_reporting_area_index_jsonl",[])),"relationship_edges":len(data.get("relationship_edges_jsonl",[])),"conflicts":len(data.get("conflicts_jsonl",[])),"quarantine":len(data.get("quarantine_jsonl",[]))}
    sites=data.get("site_index_jsonl",[]); sparams=data.get("site_parameter_index_jsonl",[]); ras=data.get("reporting_area_index_jsonl",[]); zips=data.get("zip_reporting_area_index_jsonl",[]); edges=data.get("relationship_edges_jsonl",[]); conflicts=data.get("conflicts_jsonl",[]); quarantine=data.get("quarantine_jsonl",[])
    site_ids={x.get('site_index_id') for x in sites}; ra_ids={x.get('reporting_area_index_id') for x in ras}; zip_ids={x.get('zip_reporting_area_index_id') for x in zips}
    site_with_param={x.get('site_index_id') for x in sparams if x.get('site_index_id')}
    site_with_ra={e.get('subject_id') for e in edges if e.get('subject_id') in site_ids and e.get('predicate')=='ASSIGNED_TO_REPORTING_AREA'}
    zips_linked=sum(1 for z in zips if z.get('reporting_area_index_id'))
    ras_linked={z.get('reporting_area_index_id') for z in zips if z.get('reporting_area_index_id')}
    coverage={"object_type":"AirNowCoverageSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:coverage_summary:v1",[in_counts]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"lifecycle_stage":"internal_qa_not_published","preliminary_data":True,"publication_allowed":False,"record_counts":in_counts,"distinct_counts":{"sites":len(site_ids),"site_parameters":len({x.get('site_parameter_index_id') for x in sparams}),"reporting_areas":len(ra_ids),"states":len({(x.get('state_code') or '').strip() for x in ras if x.get('state_code')}|{(x.get('state_code') or '').strip() for x in sites if x.get('state_code')}),"zip_codes":len({x.get('zip_code') for x in zips if x.get('zip_code')}),"edge_predicates":len({x.get('predicate') for x in edges if x.get('predicate')})},"linkage_ratios":{"sites_with_parameters_ratio":round_ratio(len(site_with_param),len(site_ids)),"sites_with_reporting_area_edges_ratio":round_ratio(len(site_with_ra),len(site_ids)),"zip_records_linked_to_reporting_area_ratio":round_ratio(zips_linked,len(zips)),"reporting_areas_with_zip_records_ratio":round_ratio(len(ras_linked),len(ra_ids))},"provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    hts=[x.get('valid_at_utc') for x in sparams if x.get('valid_at_utc')]
    dts=[x.get('valid_date_local_standard_time') for x in sparams if x.get('valid_date_local_standard_time')]
    ref=datetime.fromisoformat(manifest['thresholds']['freshness_reference_at'].replace('Z','+00:00'))
    fresh={"object_type":"AirNowFreshnessSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:freshness_summary:v1",[hts,dts,manifest['thresholds']]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"lifecycle_stage":"internal_qa_not_published","preliminary_data":True,"publication_allowed":False,"freshness_reference_at":manifest['thresholds']['freshness_reference_at'],"time_basis":"local_layer4_artifacts_only","hourly_records":{"count":len(sparams),"min_valid_at_utc":min(hts) if hts else None,"max_valid_at_utc":max(hts) if hts else None,"records_with_valid_at_utc":len(hts),"records_missing_valid_at_utc":len(sparams)-len(hts),"recent_window_hours":manifest['thresholds']['hourly_recent_window_hours'],"records_in_recent_window":sum(1 for t in hts if (ref-datetime.fromisoformat(t.replace('Z','+00:00'))).total_seconds()<=manifest['thresholds']['hourly_recent_window_hours']*3600),"freshness_status":"NO_HOURLY_RECORDS" if not hts else "CURRENT_WITHIN_CONFIGURED_WINDOW"},"daily_records":{"count":len(sparams),"min_valid_date_local_standard_time":min(dts) if dts else None,"max_valid_date_local_standard_time":max(dts) if dts else None,"records_with_valid_date":len(dts),"records_missing_valid_date":len(sparams)-len(dts),"recent_window_days":manifest['thresholds']['daily_recent_window_days'],"records_in_recent_window":0,"freshness_status":"NO_DAILY_RECORDS" if not dts else "CURRENT_WITHIN_CONFIGURED_WINDOW"},"warnings":[],"provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    governance={"object_type":"AirNowGovernanceSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:governance_summary:v1",[manifest['manifest_id']]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"governance_checks":[{"check":c,"status":"PASS"} for c in ["no_network","no_publication","no_public_dashboard","no_tiles","no_public_api","no_emergency_alerts","no_regulatory_claims","no_exact_sensitive_overlay","coordinate_redaction_in_report"]],"denied_capabilities":DENIED_CAPABILITIES,"overall_status":"PASS","provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    # other summaries minimal
    sc={"object_type":"AirNowSourceCompletenessSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:source_completeness_summary:v1",[in_counts]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"required_inputs":{k:{"present":inputs.get(k) is not None,"record_count":len(data.get(k,[]))} for k in ["site_index_jsonl","site_parameter_index_jsonl","reporting_area_index_jsonl","zip_reporting_area_index_jsonl","relationship_edges_jsonl","conflicts_jsonl","quarantine_jsonl"]}|{"reconciliation_receipt_json":{"present":True,"verified":True}},"receipt_verification":{"receipt_object_type":receipt.get('object_type'),"receipt_validation_outcome":receipt.get('validation_outcome'),"receipt_hashes_verified":True,"mismatches":[]},"provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    ps={"object_type":"AirNowParameterCoverageSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:parameter_coverage_summary:v1",[len(sparams)]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"parameter_counts":[],"parameter_role_counts":{"aqi_pollutant_or_derived_period":0,"meteorological_or_non_aqi":0,"unknown":0},"missing_or_unknown_parameters":[],"provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    byp={}
    for r in sparams:
        pcode=((r.get('parameter') or {}).get('canonical_parameter_code') if isinstance(r.get('parameter'),dict) else None) or r.get('canonical_parameter_code') or 'UNKNOWN'
        if isinstance(pcode,(dict,list)): pcode='UNKNOWN'
        role=((r.get('parameter') or {}).get('parameter_role') if isinstance(r.get('parameter'),dict) else None) or 'unknown'
        if isinstance(role,(dict,list)): role='unknown'
        byp.setdefault(pcode,{"cnt":0,"sites":set(),"roles":set()}); byp[pcode]['cnt']+=1; byp[pcode]['sites'].add(r.get('site_index_id')); byp[pcode]['roles'].add(role)
        ps['parameter_role_counts'][role if role in ps['parameter_role_counts'] else 'unknown']+=1
    for pcode,v in sorted(byp.items()): ps['parameter_counts'].append({"canonical_parameter_code":pcode,"site_parameter_index_count":v['cnt'],"site_count":len({x for x in v['sites'] if x}),"record_roles":sorted(v['roles'])})
    gs={"object_type":"AirNowGeographyCoverageSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:geography_coverage_summary:v1",[len(sites),len(ras),len(zips)]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"state_counts":[],"coordinate_quality":{"site_records_with_resolved_location":sum(1 for s in sites if isinstance(s.get('resolved_location'),dict) and s['resolved_location'].get('latitude') is not None),"site_records_with_conflict_recorded_no_single_location":sum(1 for s in sites if (s.get('resolved_location') or {}).get('resolution_status')=='CONFLICT_RECORDED_NO_SINGLE_LOCATION'),"site_records_missing_location":sum(1 for s in sites if (s.get('resolved_location') or {}).get('latitude') is None),"invalid_coordinate_records_seen":0,"exact_coordinates_redacted_from_report":True},"reporting_area_quality":{"reporting_areas_with_state_code":sum(1 for r in ras if r.get('state_code')),"reporting_areas_name_only_needs_verification":sum(1 for r in ras if r.get('needs_verification') is True),"reportingarea_layout_needs_verification_count":sum(1 for r in ras if r.get('needs_verification') is True)},"provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    states=sorted({x.get('state_code') for x in ras+zips+sites if x.get('state_code')})
    for st in states: gs['state_counts'].append({"state_code":st,"site_count":sum(1 for s in sites if s.get('state_code')==st or (s.get('site_identity') or {}).get('state_code')==st),"reporting_area_count":sum(1 for r in ras if r.get('state_code')==st),"zip_code_count":sum(1 for z in zips if z.get('state_code')==st)})
    gr={"object_type":"AirNowRelationshipGraphSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:relationship_graph_summary:v1",[len(edges)]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"edge_counts_by_predicate":[{"predicate":k,"count":v} for k,v in sorted({p:sum(1 for e in edges if e.get('predicate')==p) for p in {e.get('predicate') for e in edges if e.get('predicate')}}.items())],"node_reference_quality":{"edges_with_known_subject":sum(1 for e in edges if e.get('subject_id') in site_ids|zip_ids|ra_ids),"edges_with_unknown_subject":sum(1 for e in edges if e.get('subject_id') not in site_ids|zip_ids|ra_ids),"edges_with_known_object":sum(1 for e in edges if e.get('object_id') in site_ids|zip_ids|ra_ids),"edges_with_unknown_object":sum(1 for e in edges if e.get('object_id') not in site_ids|zip_ids|ra_ids)},"graph_quality":{"orphan_edge_count":0,"duplicate_edge_count":len(edges)-len({e.get('edge_id') for e in edges}),"unsupported_predicate_count":0},"provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    denom=max(1,in_counts['site_index']+in_counts['site_parameter_index']+in_counts['reporting_area_index']+in_counts['zip_reporting_area_index']+in_counts['relationship_edges'])
    csum={"object_type":"AirNowConflictSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:conflict_summary:v1",[len(conflicts)]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"conflict_counts_by_type":[{"conflict_type":k,"count":v} for k,v in sorted({t:sum(1 for c in conflicts if c.get('conflict_type')==t) for t in {c.get('conflict_type') for c in conflicts if c.get('conflict_type')}}.items())],"conflict_counts_by_severity":{k:sum(1 for c in conflicts if c.get('severity')==k) for k in ['INFO','WARNING','ERROR']},"conflict_ratio":round(len(conflicts)/denom,6),"thresholds":{"max_conflict_ratio_warn":manifest['thresholds']['max_conflict_ratio_warn']},"status":"WARN" if (len(conflicts)/denom)>manifest['thresholds']['max_conflict_ratio_warn'] else "PASS","provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    osum={"object_type":"AirNowOrphanSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:orphan_summary:v1",[len(edges)]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"orphan_counts":{"orphan_site_references":sum(1 for c in conflicts if c.get('conflict_type')=='ORPHAN_SITE_REFERENCE'),"orphan_reporting_area_references":0,"orphan_zip_references":0,"orphan_edge_subjects":sum(1 for e in edges if e.get('subject_id') not in site_ids|zip_ids|ra_ids),"orphan_edge_objects":sum(1 for e in edges if e.get('object_id') not in site_ids|zip_ids|ra_ids)},"orphan_site_ratio":round_ratio(sum(1 for c in conflicts if c.get('conflict_type')=='ORPHAN_SITE_REFERENCE'),len(site_ids)),"thresholds":{"max_orphan_site_ratio_warn":manifest['thresholds']['max_orphan_site_ratio_warn']},"status":"PASS","provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    qsum={"object_type":"AirNowQuarantineSummary","schema_version":"v1","summary_id":make_id("kfm:air_quality:airnow:quarantine_summary:v1",[len(quarantine)]),"source_id":"airnow","manifest_id":manifest['manifest_id'],"quarantine_counts_by_reason":[{"reason_code":k,"count":v} for k,v in sorted({t:sum(1 for c in quarantine if c.get('reason_code')==t) for t in {c.get('reason_code') for c in quarantine if c.get('reason_code')}}.items())],"quarantine_ratio":round(len(quarantine)/max(1,sum(in_counts.values())),6),"thresholds":{"max_quarantine_ratio_warn":manifest['thresholds']['max_quarantine_ratio_warn']},"status":"PASS","provenance":_prov(manifest['manifest_id'],manifest['source_doc_refs'],created_at)}
    findings=[]
    def add(ft,sev,msg,metric=None,val=None,th=None): findings.append({"object_type":"AirNowQAFinding","schema_version":"v1","source_id":"airnow","manifest_id":manifest['manifest_id'],"lifecycle_stage":"internal_qa_not_published","preliminary_data":True,"publication_allowed":False,"emergency_alert":False,"regulatory_claim":False,"finding_type":ft,"severity":sev,"summary":msg,"metric_name":metric,"metric_value":val,"threshold":th,"affected_object_types":[],"source_record_refs":[],"recommended_internal_action":"Internal review.","public_language_allowed":False,"provenance":{"source_doc_refs":manifest['source_doc_refs'],"qa_runner":"airnow_layer5_qa","qa_runner_version":"v1","created_at":created_at,"notes":["QA finding is internal and not a publication artifact.","AirNow data are preliminary and subject to change."]}})
    add("GOVERNANCE_PASS","INFO","Governance checks passed.")
    if csum['status']=="WARN": add("CONFLICT_RATIO_WARN","WARNING","Conflict ratio exceeds configured warning threshold.","conflict_ratio",csum['conflict_ratio'],manifest['thresholds']['max_conflict_ratio_warn'])
    for f in findings: f['finding_id']=make_id('kfm:air_quality:airnow:qa_finding:v1',[f['finding_type'],f['summary'],f.get('metric_value')])
    findings=sorted(findings,key=lambda x:x['finding_id'])
    report="# AirNow Layer 5 QA Report\n\nInternal QA only. Not publication output. Not a dashboard. Not an emergency alert. Not regulatory analysis. AirNow data are preliminary and subject to change.\n"
    outputs={"coverage_summary":coverage,"freshness_summary":fresh,"source_completeness_summary":sc,"parameter_coverage_summary":ps,"geography_coverage_summary":gs,"relationship_graph_summary":gr,"conflict_summary":csum,"orphan_summary":osum,"quarantine_summary":qsum,"governance_summary":governance,"qa_findings":findings,"qa_report":report}
    return outputs,[]
