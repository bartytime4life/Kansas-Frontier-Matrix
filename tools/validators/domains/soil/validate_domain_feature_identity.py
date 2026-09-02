#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
CASES=ROOT/'fixtures/domains/soil/domain_feature_identity/cases.json'
PROFILE='kfm.domains.soil.domain-feature-identity.v1'
FALSE_EFFECTS={'canonical_identity_created':False,'evidence_resolved':False,'policy_evaluated':False,'review_approved':False,'released':False,'published':False}
SUPPORT_ROLES={
 'authoritative_static_soil':{'SURVEY_FEATURE','COMPONENT','HORIZON','LINEAGE_JOIN','PROPERTY','CLASSIFICATION'},
 'gridded_derivative_soil':{'PROPERTY','CLASSIFICATION'},
 'station_soil_moisture':{'OBSERVATION'},
 'reference_station_soil_climate':{'OBSERVATION'},
 'satellite_soil_moisture_grid':{'OBSERVATION'},
 'profile_soil_evidence':{'PROFILE','HORIZON','PROPERTY'},
 'soil_interpretation':{'INTERPRETATION','CLASSIFICATION'},
 'governed_change_evidence':{'TEMPORAL_CAVEAT'},
}
def canonical_hash(c):
 p=dict(c);p.pop('id',None);p.pop('spec_hash',None)
 return hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
def evaluate(c):
 f=[]
 if c.get('profile')!=PROFILE or c.get('status')!='PROPOSED_INACTIVE':f.append('PROFILE_MISMATCH')
 if c.get('domain')!='soil' or c.get('version')!='1.0.0':f.append('IDENTITY_PROFILE_MISMATCH')
 support=c.get('support_type');role=c.get('object_role')
 if support not in SUPPORT_ROLES:f.append('UNKNOWN_SUPPORT_TYPE')
 elif role not in SUPPORT_ROLES[support]:f.append('SUPPORT_ROLE_COLLAPSE')
 for k in ('source_ref','source_role','source_native_id','source_native_key_family'):
  if not c.get(k):f.append('SOURCE_IDENTITY_MISSING')
 for k in ('evidence_refs','limitations'):
  v=c.get(k)
  if not isinstance(v,list) or not v or v!=sorted(set(v)):f.append(f'NONCANONICAL_{k.upper()}')
 t=c.get('temporal_scope')
 if not isinstance(t,dict) or t.get('kind') not in {'SOURCE_VINTAGE','OBSERVED_TIME','VALID_TIME','RETRIEVED_TIME','NOT_APPLICABLE'}:f.append('TEMPORAL_SCOPE_INVALID')
 elif t.get('kind')=='NOT_APPLICABLE' and t.get('value') is not None:f.append('TEMPORAL_SCOPE_INVALID')
 elif t.get('kind')!='NOT_APPLICABLE' and not isinstance(t.get('value'),str):f.append('TEMPORAL_SCOPE_INVALID')
 if c.get('public_use_allowed') is not False:f.append('PUBLIC_USE_OVERCLAIM')
 if c.get('effects')!=FALSE_EFFECTS:f.append('EFFECT_OVERCLAIM')
 d=canonical_hash(c)
 if c.get('spec_hash')!=f'sha256:{d}':f.append('SPEC_HASH_MISMATCH')
 if c.get('id')!=f'soil-identity:{d[:24]}':f.append('ID_MISMATCH')
 f=sorted(set(f)); authority={'SUPPORT_ROLE_COLLAPSE','PUBLIC_USE_OVERCLAIM','EFFECT_OVERCLAIM'}
 return ('DENY' if any(x in authority for x in f) else 'ERROR',f) if f else ('PASS',[])
def main():
 p=argparse.ArgumentParser();p.add_argument('path',nargs='?');p.add_argument('--fixtures',action='store_true');a=p.parse_args()
 if a.fixtures:
  bad=0
  for case in json.loads(CASES.read_text())['cases']:
   got=evaluate(case['candidate']);print(json.dumps({'name':case['name'],'outcome':got[0],'findings':got[1]},sort_keys=True));bad+=got!=(case['expected_outcome'],case['expected_findings'])
  raise SystemExit(1 if bad else 0)
 if not a.path:p.error('path or --fixtures required')
 o,f=evaluate(json.loads(Path(a.path).read_text()));print(json.dumps({'outcome':o,'findings':f},sort_keys=True));raise SystemExit(0 if o=='PASS' else 1)
if __name__=='__main__':main()
