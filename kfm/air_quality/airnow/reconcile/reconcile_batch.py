import json
from pathlib import Path
from .manifest import validate_manifest
from .ids import canonical_json, make_id, sha256_text
from .constants import COORD_TOLERANCE

def _load_jsonl(p):
    if p is None: return []
    rows=[]
    for ln in Path(p).read_text().splitlines():
        if ln.strip(): rows.append(json.loads(ln))
    return rows

def _load_json(p): return json.loads(Path(p).read_text())

def _hash_records(rows):
    return sha256_text('\n'.join(canonical_json(r) for r in rows))

def reconcile_from_manifest(m, created_at):
    errs=validate_manifest(m)
    if errs: return None, errs
    inputs=m['inputs']; prs=m['parse_receipts']
    for k,v in prs.items():
        if v and not Path(v).exists(): return None,['PARSE_RECEIPT_MISSING']
        if v:
            pr=_load_json(v)
            if pr.get('object_type')!='AirNowFileProductParseReceipt' or pr.get('validation_outcome')!='PASS': return None,['PARSE_RECEIPT_INVALID']
    hourly=_load_jsonl(inputs.get('hourly_aq_obs_jsonl')); daily=_load_jsonl(inputs.get('daily_data_jsonl')); sites=_load_jsonl(inputs.get('monitoring_site_locations_jsonl')); zips=_load_jsonl(inputs.get('cityzipcodes_jsonl')); ra=_load_jsonl(inputs.get('reportingarea_candidate_jsonl'))
    conflicts=[]; quarantine=[]; edges=[]; site_index=[]; sp_index=[]; ra_index=[]; zip_index=[]
    by_site={}
    def upsert_site(rec,src):
        aq=(rec.get('site',{}).get('aqsid') if rec.get('site') else rec.get('aqsid'))
        if not aq:
            quarantine.append({'object_type':'AirNowReconciliationQuarantineRecord','schema_version':'v1','quarantine_id':make_id('kfm:air_quality:airnow:reconciliation:quarantine:v1',[src,rec.get('source_record_hash')]),'source_id':'airnow','manifest_id':m['manifest_id'],'source_object_type':rec.get('object_type'),'source_record_hash':rec.get('source_record_hash'),'staging_id':rec.get('staging_id'),'reason_code':'MISSING_SITE_ID','reason_detail':'missing aqsid','finite_outcome':'ABSTAIN','publication_allowed':False,'emergency_alert':False,'raw_record':rec,'created_at':created_at}); return None
        s=by_site.setdefault(aq,{'aqsid':aq,'full_aqsid':(rec.get('site',{}).get('full_aqsid') if rec.get('site') else rec.get('full_aqsid')),'names':set(),'locs':[],'hashes':set(),'status':set(),'state':set(),'country':set(),'epa':set(),'conflict_refs':set()})
        site=rec.get('site',rec)
        if site.get('site_name'): s['names'].add(site['site_name'])
        if site.get('latitude') is not None and site.get('longitude') is not None: s['locs'].append((site.get('latitude'),site.get('longitude'),site.get('elevation_m'),site.get('gmt_offset_hours'),rec.get('object_type'),rec.get('source_record_hash')))
        for k,t in [('status','status'),('state_name','state'),('country_code','country'),('epa_region','epa')]:
            if site.get(k): s[t].add(site[k])
        if rec.get('source_record_hash'): s['hashes'].add(rec['source_record_hash'])
        return aq
    for r in sites+hourly: upsert_site(r,'site')
    for aq,s in sorted(by_site.items()):
        if len(s['names'])>1:
            cid=make_id('kfm:air_quality:airnow:conflict:v1',['SITE_NAME_CONFLICT',aq,sorted(s['names'])]); conflicts.append({'object_type':'AirNowReconciliationConflictRecord','schema_version':'v1','conflict_id':cid,'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_conflict_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'conflict_type':'SITE_NAME_CONFLICT','severity':'WARNING','entity_kind':'site','entity_identity':{'aqsid':aq},'candidate_values':[{'field':'site_name','value':n} for n in sorted(s['names'])],'resolution':{'resolution_status':'CONFLICT_RECORDED_NO_SINGLE_VALUE','selected_value':None,'policy_basis':'no overwrite'},'finite_outcome':'ANSWER','provenance':{}}); s['conflict_refs'].add(cid)
        res_loc=None; status='NO_LOCATION'
        if s['locs']:
            f=s['locs'][0];res_loc=f
            for l in s['locs'][1:]:
                if abs(l[0]-f[0])>COORD_TOLERANCE or abs(l[1]-f[1])>COORD_TOLERANCE:
                    cid=make_id('kfm:air_quality:airnow:conflict:v1',['SITE_COORDINATE_CONFLICT',aq]); conflicts.append({'object_type':'AirNowReconciliationConflictRecord','schema_version':'v1','conflict_id':cid,'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_conflict_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'conflict_type':'SITE_COORDINATE_CONFLICT','severity':'WARNING','entity_kind':'site','entity_identity':{'aqsid':aq},'candidate_values':[{'field':'latitude','value':x[0]} for x in s['locs']],'resolution':{'resolution_status':'CONFLICT_RECORDED_NO_SINGLE_VALUE','selected_value':None,'policy_basis':'no overwrite'},'finite_outcome':'ANSWER','provenance':{}}); s['conflict_refs'].add(cid); res_loc=None; break
            status='SINGLE_CONSISTENT_LOCATION' if res_loc else 'CONFLICT_RECORDED_NO_SINGLE_LOCATION'
        sid=make_id('kfm:air_quality:airnow:site_index:v1',[aq,s.get('full_aqsid')])
        site_index.append({'object_type':'AirNowSiteIndexRecord','schema_version':'v1','site_index_id':sid,'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_index_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'regulatory_claim':False,'site_identity':{'aqsid':aq,'full_aqsid':s.get('full_aqsid'),'identity_status':'MATCHED_AQSID_OR_FULL_AQSID'},'site_names':[{'site_name':n} for n in sorted(s['names'])],'resolved_location':({'latitude':res_loc[0],'longitude':res_loc[1],'elevation_m':res_loc[2],'gmt_offset_hours':res_loc[3],'resolution_status':status,'spatial_role':'monitoring_site_public_point_internal_index'} if res_loc else {'resolution_status':status}),'source_record_hashes':sorted(s['hashes']),'conflict_refs':sorted(s['conflict_refs']),'provenance':{'created_at':created_at}})
    site_id_by_aq={x['site_identity']['aqsid']:x['site_index_id'] for x in site_index}
    ra_keys=set()
    for h in hourly:
        aq=h.get('site',{}).get('aqsid'); sid=site_id_by_aq.get(aq)
        for rname in h.get('reporting_areas',[]): ra_keys.add((rname,None,'monitoring_site_assignment',h.get('source_record_hash')))
        if sid: edges.append({'object_type':'AirNowRelationshipEdge','schema_version':'v1','edge_id':make_id('kfm:air_quality:airnow:edge:v1',[sid,h.get('staging_id'),'SITE_OBSERVED_HOURLY_RECORD']),'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_relationship_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'subject_id':sid,'predicate':'SITE_OBSERVED_HOURLY_RECORD','object_id':h.get('staging_id'),'relationship_role':'site_hourly_staging_record','confidence':{'level':'SOURCE_DECLARED','basis':'parsed hourly record'},'source_record_hashes':[h.get('source_record_hash')]})
    zip_map={}
    for z in zips:
        ra_name=z.get('reporting_area'); sc=z.get('state_code'); zc=z.get('zip_code')
        if ra_name: ra_keys.add((ra_name,sc,'zip_reporting_area_lookup',z.get('source_record_hash')))
        if zc and ra_name:
            zip_map.setdefault(zc,set()).add((ra_name,sc))
    for zc,v in zip_map.items():
        if len(v)>1: conflicts.append({'object_type':'AirNowReconciliationConflictRecord','schema_version':'v1','conflict_id':make_id('kfm:air_quality:airnow:conflict:v1',['ZIP_REPORTING_AREA_CONFLICT',zc]),'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_conflict_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'conflict_type':'ZIP_REPORTING_AREA_CONFLICT','severity':'WARNING','entity_kind':'zip','entity_identity':{'zip_code':zc},'candidate_values':[{'field':'reporting_area','value':x[0]} for x in sorted(v)],'resolution':{'resolution_status':'CONFLICT_RECORDED_NO_SINGLE_VALUE','selected_value':None,'policy_basis':'no overwrite'},'finite_outcome':'ANSWER','provenance':{}})
    ra_id={}
    for name,sc,role,sh in sorted(ra_keys):
        rid=make_id('kfm:air_quality:airnow:reporting_area_index:v1',[name,sc])
        ra_id[(name,sc)]=rid
        ra_index.append({'object_type':'AirNowReportingAreaIndexRecord','schema_version':'v1','reporting_area_index_id':rid,'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_index_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'regulatory_claim':False,'reporting_area':name,'state_code':sc,'identity_status':'NAME_ONLY_NEEDS_VERIFICATION' if not sc else 'NAMED_REPORTING_AREA_STATE_MATCH','record_roles_observed':[role],'source_record_hashes':[sh] if sh else [],'needs_verification':(not sc),'conflict_refs':[],'provenance':{'created_at':created_at}})
    for z in zips:
        zc=z.get('zip_code'); rn=z.get('reporting_area'); sc=z.get('state_code')
        if not (zc and rn): continue
        zid=make_id('kfm:air_quality:airnow:zip_reporting_area_index:v1',[zc,rn,sc])
        rid=ra_id.get((rn,sc)) or ra_id.get((rn,None))
        zip_index.append({'object_type':'AirNowZipReportingAreaIndexRecord','schema_version':'v1','zip_reporting_area_index_id':zid,'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_lookup_index_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'zip_code':zc,'reporting_area':rn,'state_code':sc,'reporting_area_index_id':rid,'centroid':{'latitude':z.get('latitude'),'longitude':z.get('longitude'),'spatial_role':'zip_code_centroid_lookup'},'record_role':'zip_to_reporting_area_lookup','source_record_hashes':[z.get('source_record_hash')] if z.get('source_record_hash') else [],'conflict_refs':[],'provenance':{'created_at':created_at}})
        if rid: edges.append({'object_type':'AirNowRelationshipEdge','schema_version':'v1','edge_id':make_id('kfm:air_quality:airnow:edge:v1',[zid,rid,'ZIP_ASSIGNED_TO_REPORTING_AREA']),'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_relationship_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'subject_id':zid,'predicate':'ZIP_ASSIGNED_TO_REPORTING_AREA','object_id':rid,'relationship_role':'zip_reporting_area_lookup','confidence':{'level':'SOURCE_DECLARED','basis':'cityzipcodes lookup'},'source_record_hashes':[z.get('source_record_hash')]})
    for d in daily:
        aq=d.get('site',{}).get('aqsid') or d.get('aqsid')
        sid=site_id_by_aq.get(aq)
        if not sid:
            sid=make_id('kfm:air_quality:airnow:site_index:v1',[aq,None,'orphan']); site_id_by_aq[aq]=sid; site_index.append({'object_type':'AirNowSiteIndexRecord','schema_version':'v1','site_index_id':sid,'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_index_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'regulatory_claim':False,'site_identity':{'aqsid':aq,'full_aqsid':None,'identity_status':'ORPHAN_FROM_DAILY_DATA'},'site_names':[],'resolved_location':{'resolution_status':'NO_LOCATION'},'source_record_hashes':[d.get('source_record_hash')],'conflict_refs':[],'provenance':{'created_at':created_at}})
            conflicts.append({'object_type':'AirNowReconciliationConflictRecord','schema_version':'v1','conflict_id':make_id('kfm:air_quality:airnow:conflict:v1',['ORPHAN_SITE_REFERENCE',aq]),'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_conflict_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'conflict_type':'ORPHAN_SITE_REFERENCE','severity':'WARNING','entity_kind':'site','entity_identity':{'aqsid':aq},'candidate_values':[],'resolution':{'resolution_status':'PLACEHOLDER_SITE_CREATED','selected_value':sid,'policy_basis':'preserve daily linkage'},'finite_outcome':'ANSWER','provenance':{}})
        spid=make_id('kfm:air_quality:airnow:site_parameter_index:v1',[aq,d.get('parameter')])
        sp_index.append({'object_type':'AirNowSiteParameterIndexRecord','schema_version':'v1','site_parameter_index_id':spid,'source_id':'airnow','manifest_id':m['manifest_id'],'lifecycle_stage':'internal_index_not_published','preliminary_data':True,'publication_allowed':False,'emergency_alert':False,'site_index_id':sid,'site_identity':{'aqsid':aq,'full_aqsid':d.get('site',{}).get('full_aqsid')},'parameter':{'source_parameter_names':[d.get('parameter')],'canonical_parameter_code':d.get('parameter'),'parameter_role':'aqi_pollutant_or_derived_period'},'source_record_hashes':[d.get('source_record_hash')] if d.get('source_record_hash') else [],'conflict_refs':[],'provenance':{'created_at':created_at}})
    out={k:sorted(v,key=lambda x:next(iter([x.get(i) for i in ['site_index_id','site_parameter_index_id','reporting_area_index_id','zip_reporting_area_index_id','edge_id','conflict_id','quarantine_id'] if x.get(i)]),'')) for k,v in {'site_index':site_index,'site_parameter_index':sp_index,'reporting_area_index':ra_index,'zip_reporting_area_index':zip_index,'relationship_edges':edges,'conflicts':conflicts,'quarantine':quarantine}.items()}
    return out,[]
