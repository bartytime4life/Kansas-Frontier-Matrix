"""Tests for fixture-only WBD HUC12 material-change assessments."""
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
REPO_ROOT=Path(__file__).resolve().parents[5]
MODULE_PATH=REPO_ROOT/"tools/validators/domains/hydrology/wbd_huc12_material_change/validate_wbd_huc12_material_change.py"
VALID=REPO_ROOT/"fixtures/domains/hydrology/wbd_huc12_material_change/valid";INVALID=REPO_ROOT/"fixtures/domains/hydrology/wbd_huc12_material_change/invalid"
SPEC=importlib.util.spec_from_file_location('kfm_wbd_huc12_material_change',MODULE_PATH);assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC);sys.modules[SPEC.name]=MODULE;SPEC.loader.exec_module(MODULE)
def load(d:Path,n:str)->dict[str,object]:v=json.loads((d/n).read_text());assert isinstance(v,dict);return v
def rehash(p:dict[str,object])->None:p['spec_hash']=MODULE.canonical_spec_hash(p)
def test_metadata_churn_and_ring_reversal_are_no_change()->None:
 p=load(VALID,'metadata_churn_no_change.json');first=MODULE.validate_payload(p);second=MODULE.validate_payload(copy.deepcopy(p));assert first==second;assert first.ok;assert p['decision']=={'outcome':'NO_CHANGE','change_types':[]};assert p['prior']['fingerprint']==p['current']['fingerprint']
def test_metadata_is_excluded_from_feature_fingerprint()->None:
 p=load(VALID,'metadata_churn_no_change.json');a=copy.deepcopy(p['prior']['feature']);b=copy.deepcopy(a);b['source_metadata']['load_date']='2099-01-01';b['source_metadata']['etag']='changed';assert MODULE.canonical_feature_fingerprint(a,6)==MODULE.canonical_feature_fingerprint(b,6)
def test_geometry_change_is_material()->None:
 p=load(VALID,'geometry_change.json');assert MODULE.validate_payload(p).ok;assert p['decision']=={'outcome':'MATERIAL_CHANGE','change_types':['geometry_change']}
def test_area_change_is_material()->None:
 p=load(VALID,'area_change.json');assert MODULE.validate_payload(p).ok;assert p['decision']=={'outcome':'MATERIAL_CHANGE','change_types':['area_change']}
def test_add_and_remove_are_finite()->None:
 a=load(VALID,'add.json');r=load(VALID,'remove.json');assert MODULE.validate_payload(a).ok and MODULE.validate_payload(r).ok;assert a['decision']['outcome']=='ADD';assert r['decision']['outcome']=='REMOVE'
def test_decision_mismatch_is_rejected()->None:
 p=load(INVALID,'decision_mismatch.json');result=MODULE.validate_payload(p);assert MODULE.Finding('DECISION_CHANGE_TYPES_MISMATCH','/decision/change_types') in result.findings;assert MODULE.Finding('DECISION_OUTCOME_MISMATCH','/decision/outcome') in result.findings
def test_feature_fingerprint_mismatch_is_rejected()->None:
 p=load(VALID,'metadata_churn_no_change.json');p['current']['feature']['areasqkm']=99;rehash(p);result=MODULE.validate_payload(p);assert MODULE.Finding('FEATURE_FINGERPRINT_MISMATCH','/current/fingerprint') in result.findings
def test_huc12_identity_mismatch_is_rejected()->None:
 p=load(VALID,'metadata_churn_no_change.json');p['current']['feature']['huc12']='102600030505';p['current']['fingerprint']=MODULE.canonical_feature_fingerprint(p['current']['feature'],6);rehash(p);result=MODULE.validate_payload(p);assert MODULE.Finding('HUC12_ID_MISMATCH','/current/feature/huc12') in result.findings
def test_coordinate_range_is_rejected()->None:
 p=load(VALID,'metadata_churn_no_change.json');p['current']['feature']['geometry']['coordinates'][0][0][0]=200;p['current']['fingerprint']='sha256:'+'0'*64;rehash(p);result=MODULE.validate_payload(p);assert MODULE.Finding('GEOMETRY_INVALID','/current/feature/geometry') in result.findings
def test_area_rounding_is_stable_at_six_decimals()->None:
 p=load(VALID,'metadata_churn_no_change.json');a=copy.deepcopy(p['prior']['feature']);b=copy.deepcopy(a);b['areasqkm']=a['areasqkm']+0.0000004;assert MODULE.canonical_feature_fingerprint(a,6)==MODULE.canonical_feature_fingerprint(b,6)
def test_seven_decimal_precision_is_supported()->None:
 p=load(VALID,'metadata_churn_no_change.json');p['normalization']['coordinate_precision']=7
 for side in ('prior','current'):p[side]['fingerprint']=MODULE.canonical_feature_fingerprint(p[side]['feature'],7)
 p['decision']=MODULE.expected_decision(p);rehash(p);assert MODULE.validate_payload(p).ok
def test_assessment_spec_hash_mismatch_is_rejected()->None:
 p=load(VALID,'metadata_churn_no_change.json');p['assessed_at']='2026-04-11T18:01:00Z';result=MODULE.validate_payload(p);assert MODULE.Finding('SPEC_HASH_MISMATCH','/spec_hash') in result.findings
