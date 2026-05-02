from .constants import POLLUTANT_MAP, AQI_CATEGORIES, CATEGORY_ALIASES
from .ids import source_record_hash, canonical_id, sha256_text
from .provenance import make_provenance
from .quarantine import make_quarantine

def _norm_cat_name(name):
    return CATEGORY_ALIASES.get(name, name)

def _pollutant(src):
    return POLLUTANT_MAP.get(str(src).upper()) or POLLUTANT_MAP.get(str(src))

def _validate_common(r):
    if r.get("preliminary_data") is not True: return ("PRELIMINARY_DATA_FALSE","preliminary_data must be true")
    if not r.get("provenance"): return ("MISSING_PROVENANCE","provenance required")
    if not r.get("reporting_area") or not r.get("state_code"): return ("MISSING_REPORTING_AREA","reporting_area/state_code required")
    p = _pollutant(r.get("parameter_name"))
    if not p: return ("UNKNOWN_POLLUTANT",f"ParameterName '{r.get('parameter_name')}' is not in the AirNow Layer 2 allowlist.")
    aqi = r.get("aqi")
    if not isinstance(aqi,int) or aqi<0 or aqi>500: return ("AQI_OUT_OF_RANGE","AQI must be integer in 0..500")
    cat = r.get("category") or {}
    num = cat.get("number"); name=_norm_cat_name(cat.get("name"))
    if num not in AQI_CATEGORIES: return ("AQI_CATEGORY_MISMATCH","category number missing or invalid")
    ename, lo, hi, _ = AQI_CATEGORIES[num]
    if name != ename or not(lo<=aqi<=hi): return ("AQI_CATEGORY_MISMATCH","category and AQI mismatch")
    return None

def normalize_record(r, manifest_id, created_at):
    rec_hash = source_record_hash(r)
    err = _validate_common(r)
    if err: return None, make_quarantine(r, rec_hash, manifest_id, err[0], err[1], created_at)
    t = r.get("object_type")
    pcode,pname,dunit = _pollutant(r.get("parameter_name"))
    if t == "AirNowObservation":
        if r.get("date_observed") is None or r.get("hour_observed") is None or r.get("local_time_zone") is None:
            return None, make_quarantine(r, rec_hash, manifest_id, "MISSING_TIMESTAMP", "date/hour/timezone required", created_at)
        seed = ["airnow",t,r["reporting_area"],r["state_code"],r["date_observed"],str(r["hour_observed"]),r["local_time_zone"],pcode,str(r["aqi"])]
        cid = canonical_id("kfm:air_quality:observation:airnow:v1",seed)
        ename,_,_,crange = AQI_CATEGORIES[r["category"]["number"]]
        return {"object_type":"CanonicalAirQualityObservation","schema_version":"v1","canonical_id":cid,"source_id":"airnow","source_object_type":t,"source_record_hash":rec_hash,"source_role":"preliminary_reporting_area_observation","lifecycle_stage":"normalized_not_published","preliminary_data":True,"publication_allowed":False,"emergency_alert":False,"observed_date_local":r["date_observed"],"observed_hour_local":r["hour_observed"],"local_time_zone":r["local_time_zone"],"observed_at_utc":None,"time_conversion_status":"NOT_ATTEMPTED_LOCAL_ABBREVIATION_ONLY","geography":{"reporting_area":r["reporting_area"],"state_code":r["state_code"],"latitude":r.get("latitude"),"longitude":r.get("longitude"),"spatial_role":"reporting_area_representative_point","exact_sensitive":False},"pollutant":{"source_parameter_name":r.get("parameter_name"),"canonical_parameter_code":pcode,"canonical_parameter_name":pname,"unit":dunit},"aqi":{"value":r["aqi"],"category_number":r["category"]["number"],"category_name":ename,"category_range":crange},"measurement":{"source_value":r.get("value"),"source_unit":str(r.get("unit","ug/m3")).lower(),"normalized_value":r.get("value"),"normalized_unit":str(r.get("unit","ug/m3")).lower(),"normalization_status":"PASSTHROUGH_SOURCE_UNIT"},"provenance":make_provenance(manifest_id,created_at)}, None
    if t == "AirNowForecast":
        if r.get("date_issue") is None or r.get("date_forecast") is None:
            return None, make_quarantine(r, rec_hash, manifest_id, "MISSING_TIMESTAMP", "date_issue/date_forecast required", created_at)
        seed=["airnow",t,r["reporting_area"],r["state_code"],r["date_issue"],r["date_forecast"],pcode,str(r["aqi"])]
        cid=canonical_id("kfm:air_quality:forecast:airnow:v1",seed)
        ename,_,_,crange = AQI_CATEGORIES[r["category"]["number"]]
        return {"object_type":"CanonicalAirQualityForecast","schema_version":"v1","canonical_id":cid,"source_id":"airnow","source_object_type":t,"source_record_hash":rec_hash,"source_role":"preliminary_reporting_area_forecast","lifecycle_stage":"normalized_not_published","preliminary_data":True,"publication_allowed":False,"emergency_alert":False,"date_issue":r["date_issue"],"date_forecast":r["date_forecast"],"forecast_time_basis":"daily_reporting_area_forecast","geography":{"reporting_area":r["reporting_area"],"state_code":r["state_code"],"latitude":r.get("latitude"),"longitude":r.get("longitude"),"spatial_role":"reporting_area_representative_point","exact_sensitive":False},"pollutant":{"source_parameter_name":r.get("parameter_name"),"canonical_parameter_code":pcode,"canonical_parameter_name":pname,"unit":dunit},"aqi":{"value":r["aqi"],"category_number":r["category"]["number"],"category_name":ename,"category_range":crange},"forecast":{"action_day":bool(r.get("action_day",False)),"discussion":r.get("discussion",""),"discussion_publication_allowed":False},"provenance":make_provenance(manifest_id,created_at,forecast=True)}, None
    return None, make_quarantine(r, rec_hash, manifest_id, "UNKNOWN_OBJECT_TYPE", f"unsupported object_type {t}", created_at)

def build_receipt(manifest_id, created_at, in_count, obs, fc, quar, manifest_hash, outpaths):
    hashes = sorted([x["source_record_hash"] for x in obs+fc+quar])
    batch_hash = sha256_text("|".join(hashes+[manifest_hash]))
    finite = "ANSWER" if (obs or fc) else "ABSTAIN"
    base={"object_type":"AirNowNormalizationReceipt","schema_version":"v1","manifest_id":manifest_id,"source_id":"airnow","normalizer":"airnow_layer2","normalizer_version":"v1","input_record_count":in_count,"normalized_observation_count":len(obs),"normalized_forecast_count":len(fc),"quarantined_record_count":len(quar),"validation_outcome":"PASS","finite_outcome":finite,"batch_hash":batch_hash,"outputs":outpaths,"warnings":[],"errors":[],"created_at":created_at}
    base["receipt_id"] = canonical_id("kfm:air_quality:airnow:normalization_receipt:v1", [manifest_id,batch_hash,created_at])
    return base
