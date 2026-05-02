import csv, json
from datetime import datetime
from pathlib import Path
from .ids import source_record_hash, make_id
from .quarantine import make_quarantine
from .constants import POLLUTANT_MAP, AQI_CATEGORY

PROV_NOTES=["AirNow data are preliminary and subject to change."]

def _prov(manifest,created_at,extra):
    return {"source_doc_refs":manifest.get('source_doc_refs',[]),"parser":"airnow_layer3_file_products","parser_version":"v1","created_at":created_at,"notes":PROV_NOTES+[extra]}

def _float(x): return None if x=='' else float(x)
def _int(x): return None if x=='' else int(x)

def parse_hourly(manifest,path,created_at):
    fields=["AQSID","SiteName","Status","EPARegion","Latitude","Longitude","Elevation","GMTOffset","CountryCode","StateName","ValidDate","ValidTime","DataSource","ReportingArea_PipeDelimited","OZONE_AQI","PM10_AQI","PM25_AQI","NO2_AQI","Ozone_Measured","PM10_Measured","PM25_Measured","NO2_Measured","PM25","PM25_Unit","OZONE","OZONE_Unit","NO2","NO2_Unit","CO","CO_Unit","SO2","SO2_Unit","PM10","PM10_Unit"]
    parsed=[];quar=[]
    for i,row in enumerate(csv.reader(path.open(),delimiter=',',quotechar='"'),1):
        raw='|'.join(row)
        if len(row)!=len(fields): quar.append(make_quarantine(manifest,i,'FIELD_COUNT_MISMATCH','hourly field mismatch',raw,created_at)); continue
        d=dict(zip(fields,row)); h=source_record_hash(d)
        try:
            dt=datetime.strptime(d['ValidDate']+' '+d['ValidTime'],'%m/%d/%y %H:%M')
            lat=float(d['Latitude']); lon=float(d['Longitude'])
            if not(-90<=lat<=90 and -180<=lon<=180): raise ValueError('coord')
        except Exception:
            quar.append(make_quarantine(manifest,i,'MALFORMED_TIMESTAMP','ValidDate/ValidTime could not be parsed as GMT/UTC.',raw,created_at,h)); continue
        rec={"object_type":"AirNowHourlyAQObsSiteHour","schema_version":"v1","source_id":"airnow","product_type":"hourly_aq_obs","source_record_hash":h,"manifest_id":manifest['manifest_id'],"lifecycle_stage":"parsed_staging_not_canonical_not_published","preliminary_data":True,"publication_allowed":False,"emergency_alert":False,"site":{"aqsid":d['AQSID'],"site_name":d['SiteName'],"status":d['Status'],"epa_region":d['EPARegion'],"country_code":d['CountryCode'],"state_name":d['StateName'],"latitude":lat,"longitude":lon,"elevation_m":_float(d['Elevation']),"gmt_offset_hours":_float(d['GMTOffset']),"spatial_role":"monitoring_site_public_point"},"time":{"valid_date_source":d['ValidDate'],"valid_time_source":d['ValidTime'],"valid_at_utc":dt.strftime('%Y-%m-%dT%H:%M:00Z'),"measurement_period_role":"beginning_of_hour"},"reporting_areas":[x.strip() for x in d['ReportingArea_PipeDelimited'].split('|') if x.strip()],"data_source":d['DataSource'],"aqi_by_parameter":{},"measured_flags":{},"concentrations_by_parameter":{},"warnings":[],"provenance":_prov(manifest,created_at,'Hourly AQ Obs staging record is monitoring-site based and is not a reporting-area observation.')}
        for src,key in [('OZONE_AQI','O3'),('PM10_AQI','PM10'),('PM25_AQI','PM25'),('NO2_AQI','NO2')]:
            if d[src] != '': rec['aqi_by_parameter'][key]={"value":int(d[src]),"source_field":src}
        for src,key in [('Ozone_Measured','O3'),('PM10_Measured','PM10'),('PM25_Measured','PM25'),('NO2_Measured','NO2')]: rec['measured_flags'][key]=d[src]=='1'
        for src,unit,key in [('PM25','PM25_Unit','PM25'),('OZONE','OZONE_Unit','O3'),('NO2','NO2_Unit','NO2'),('CO','CO_Unit','CO'),('SO2','SO2_Unit','SO2'),('PM10','PM10_Unit','PM10')]:
            if d[src] != '':
                val=float(d[src]);
                if val<0: rec['warnings'].append(f'NEGATIVE_CONCENTRATION:{key}')
                rec['concentrations_by_parameter'][key]={"value":val,"unit":d[unit],"source_field":src}
        rec['staging_id']=make_id('kfm:air_quality:airnow:file_product:hourly_aq_obs:v1',[manifest['product_type'],i,h,d['AQSID']])
        parsed.append(rec)
    return parsed,quar

def parse_daily(manifest,path,created_at):
    parsed=[];quar=[]
    for i,row in enumerate(csv.reader(path.open(),delimiter='|'),1):
        if len(row)!=13: quar.append(make_quarantine(manifest,i,'FIELD_COUNT_MISMATCH','daily field mismatch','|'.join(row),created_at)); continue
        d=dict(zip(['ValidDate','AQSID','SiteName','ParameterName','ReportingUnits','Value','AveragingPeriod','DataSource','AQI','AQICategory','Latitude','Longitude','FullAQSID'],row)); h=source_record_hash(d)
        try: lat=float(d['Latitude']); lon=float(d['Longitude'])
        except: quar.append(make_quarantine(manifest,i,'MALFORMED_COORDINATE','bad coordinate','|'.join(row),created_at,h)); continue
        aqi={"aqi_status":"SOURCE_SENTINEL_NOT_APPLICABLE"}
        if d['AQI']!='-999':
            try: av=int(d['AQI']); cat=int(d['AQICategory'])
            except: quar.append(make_quarantine(manifest,i,'MALFORMED_AQI','bad aqi','|'.join(row),created_at,h)); continue
            if not(0<=av<=500): quar.append(make_quarantine(manifest,i,'AQI_OUT_OF_RANGE','aqi out','|'.join(row),created_at,h)); continue
            aqi={"aqi_status":"PRESENT","value":av,"source_aqi_category_index":cat,"kfm_aqi_category_number":cat+1,"category_name":AQI_CATEGORY.get(cat)}
        pcode=POLLUTANT_MAP.get(d['ParameterName'].upper(),d['ParameterName'])
        rec={"object_type":"AirNowDailyDataSiteParameter","schema_version":"v1","source_id":"airnow","product_type":"daily_data_v2","source_record_hash":h,"manifest_id":manifest['manifest_id'],"lifecycle_stage":"parsed_staging_not_canonical_not_published","preliminary_data":True,"publication_allowed":False,"emergency_alert":False,"site":{"aqsid":d['AQSID'],"full_aqsid":d['FullAQSID'],"site_name":d['SiteName'],"latitude":lat,"longitude":lon,"spatial_role":"monitoring_site_public_point"},"time":{"valid_date_source":d['ValidDate'],"valid_date_local_standard_time":datetime.strptime(d['ValidDate'],'%m/%d/%y').strftime('%Y-%m-%d'),"time_basis":"daily_local_standard_time"},"parameter":{"source_parameter_name":d['ParameterName'],"canonical_parameter_code":pcode,"reporting_units":d['ReportingUnits'],"value":float(d['Value']),"averaging_period_hours":int(float(d['AveragingPeriod']))},"aqi":aqi,"data_source":d['DataSource'],"provenance":_prov(manifest,created_at,'Daily data site-parameter record is not an hourly observation.')}
        rec['staging_id']=make_id('kfm:air_quality:airnow:file_product:daily_data:v1',[manifest['product_type'],i,h,d['AQSID']]); parsed.append(rec)
    return parsed,quar

def parse_manifest_file(manifest,path,created_at):
    pt=manifest['product_type']
    if pt=='hourly_aq_obs': return parse_hourly(manifest,path,created_at)
    if pt=='daily_data_v2': return parse_daily(manifest,path,created_at)
    if pt=='monitoring_site_locations': return parse_sites(manifest,path,created_at)
    if pt=='cityzipcodes_lookup': return parse_cityzip(manifest,path,created_at)
    if pt=='reportingarea_candidate': return parse_reporting(manifest,path,created_at)
    return [],[]


def parse_sites(manifest,path,created_at):
    parsed=[];quar=[]
    for i,row in enumerate(csv.reader(path.open(),delimiter='|'),1):
        if len(row)==20 and row[-1]=='': row=row[:-1]
        if len(row)!=19: quar.append(make_quarantine(manifest,i,'FIELD_COUNT_MISMATCH','site field mismatch','|'.join(row),created_at)); continue
        d=dict(zip(['AQSID','ParameterName','SiteCode','SiteName','Status','AgencyID','AgencyName','EPARegion','Latitude','Longitude','Elevation','GMTOffset','CountryCode','MSACode','MSAName','StateCode','StateName','CountyCode','CountyName'],row)); h=source_record_hash(d)
        try: lat=float(d['Latitude']); lon=float(d['Longitude'])
        except: quar.append(make_quarantine(manifest,i,'MALFORMED_COORDINATE','bad coordinate','|'.join(row),created_at,h)); continue
        pcode=POLLUTANT_MAP.get(d['ParameterName'].upper(),d['ParameterName'])
        role='aqi_pollutant' if pcode in {'O3','PM25','PM10','NO2','SO2','CO'} else 'meteorological_or_non_aqi'
        rec={"object_type":"AirNowMonitoringSiteLocation","schema_version":"v1","source_id":"airnow","product_type":"monitoring_site_locations","source_record_hash":h,"manifest_id":manifest['manifest_id'],"lifecycle_stage":"parsed_staging_not_canonical_not_published","preliminary_data":True,"publication_allowed":False,"emergency_alert":False,"aqsid":d['AQSID'],"site_name":d['SiteName'],"status":d['Status'],"status_normalized":('ACTIVE' if d['Status'].lower()=='active' else 'INACTIVE' if d['Status'].lower()=='inactive' else 'OTHER'),"parameter_name":d['ParameterName'],"canonical_parameter_code":pcode,"parameter_role":role,"latitude":lat,"longitude":lon,"provenance":_prov(manifest,created_at,'Monitoring-site location metadata record; not a reporting-area observation.')}
        rec['staging_id']=make_id('kfm:air_quality:airnow:file_product:monitoring_site_locations:v1',[manifest['product_type'],i,h,d['AQSID']]);parsed.append(rec)
    return parsed,quar

def parse_cityzip(manifest,path,created_at):
    parsed=[];quar=[]
    rdr=csv.DictReader(path.open(),delimiter=',')
    expected=['zip_code','reporting_area','state_code','latitude','longitude']
    if rdr.fieldnames!=expected: return [],[make_quarantine(manifest,0,'HEADER_MISMATCH','header mismatch',str(rdr.fieldnames),created_at)]
    for i,d in enumerate(rdr,1):
        h=source_record_hash(d)
        if not d['reporting_area']: quar.append(make_quarantine(manifest,i,'MISSING_REPORTING_AREA','reporting_area required',str(d),created_at,h)); continue
        try: lat=float(d['latitude']); lon=float(d['longitude'])
        except: quar.append(make_quarantine(manifest,i,'MALFORMED_COORDINATE','bad coordinate',str(d),created_at,h)); continue
        rec={"object_type":"AirNowCityZipcodeAssociation","schema_version":"v1","source_id":"airnow","product_type":"cityzipcodes_lookup","source_record_hash":h,"manifest_id":manifest['manifest_id'],"lifecycle_stage":"parsed_lookup_staging_not_published","preliminary_data":True,"publication_allowed":False,"emergency_alert":False,"zip_code":d['zip_code'],"reporting_area":d['reporting_area'],"state_code":d['state_code'],"centroid":{"latitude":lat,"longitude":lon,"spatial_role":"zip_code_centroid_lookup"},"record_role":"zip_to_reporting_area_lookup","provenance":_prov(manifest,created_at,'Lookup association record; not observation or forecast.')}
        rec['staging_id']=make_id('kfm:air_quality:airnow:file_product:cityzipcodes:v1',[manifest['product_type'],i,h,d['zip_code']]); parsed.append(rec)
    return parsed,quar

def parse_reporting(manifest,path,created_at):
    parsed=[];quar=[]; field_order=manifest.get('field_order')
    for i,row in enumerate(csv.reader(path.open(),delimiter='|'),1):
        h=source_record_hash(row)
        if not field_order:
            quar.append(make_quarantine(manifest,i,'UNVERIFIED_REPORTINGAREA_LAYOUT','field_order missing', '|'.join(row),created_at,h)); continue
        d=dict(zip(field_order,row)); role=d.get('record_role') or manifest.get('declared_record_roles')
        if not role: quar.append(make_quarantine(manifest,i,'FORECAST_OBSERVATION_ROLE_CONFLICT','ambiguous role',str(d),created_at,h)); continue
        rec={"object_type":"AirNowReportingAreaCandidateRecord","schema_version":"v1","source_id":"airnow","product_type":"reportingarea_candidate","source_record_hash":h,"manifest_id":manifest['manifest_id'],"raw_fields":d,"record_role":role,"provenance":_prov(manifest,created_at,'Candidate parser only; official reportingarea.dat layout NEEDS_VERIFICATION.')}
        rec['staging_id']=make_id('kfm:air_quality:airnow:file_product:reportingarea_candidate:v1',[manifest['product_type'],i,h]);parsed.append(rec)
    return parsed,quar
