import json
from pathlib import Path
from kfm.air_quality.airnow.normalize import normalize_record

FIX = Path(__file__).resolve().parents[1] / 'fixtures' / 'air_quality' / 'airnow'


def load_valid(name):
    return json.loads((FIX/'valid'/name).read_text())


def test_valid_observation_normalizes():
    rec = load_valid('observation_wichita_pm25.json')
    n,q = normalize_record(rec,'m1','2026-01-01T00:00:00Z'); assert q is None
    assert n['object_type']=='CanonicalAirQualityObservation'
    assert n['observed_at_utc'] is None

def test_valid_forecast_normalizes():
    rec = load_valid('forecast_wichita_ozone.json'); rec['provenance']={'source_doc_url':'https://docs.airnowapi.org/webservices'}; n,q=normalize_record(rec,'m1','2026-01-01T00:00:00Z'); assert q is None
    assert n['object_type']=='CanonicalAirQualityForecast'

def test_alias_and_stable_ids():
    rec=load_valid('forecast_wichita_ozone.json'); rec['parameter_name']='O3'; rec['provenance']={'source_doc_url':'https://docs.airnowapi.org/webservices'}
    a,_=normalize_record(rec,'m1','2026-01-01T00:00:00Z'); b,_=normalize_record(rec,'m1','2026-01-01T00:00:00Z')
    assert a['pollutant']['canonical_parameter_code']=='O3'
    assert a['canonical_id']==b['canonical_id']

def test_unknown_pollutant_quarantine():
    rec=load_valid('observation_wichita_pm25.json'); rec['parameter_name']='BENZENE'
    n,q=normalize_record(rec,'m1','2026-01-01T00:00:00Z'); assert n is None and q['reason_code']=='UNKNOWN_POLLUTANT'

def test_aqi_mismatch_quarantine():
    rec=load_valid('observation_wichita_pm25.json'); rec['aqi']=150
    n,q=normalize_record(rec,'m1','2026-01-01T00:00:00Z'); assert q['reason_code']=='AQI_CATEGORY_MISMATCH'

def test_prelim_false_and_missing_prov_quarantine():
    rec=load_valid('observation_wichita_pm25.json'); rec['preliminary_data']=False
    _,q=normalize_record(rec,'m1','2026-01-01T00:00:00Z'); assert q['reason_code']=='PRELIMINARY_DATA_FALSE'
    rec=load_valid('observation_wichita_pm25.json'); rec.pop('provenance')
    _,q=normalize_record(rec,'m1','2026-01-01T00:00:00Z'); assert q['reason_code']=='MISSING_PROVENANCE'
