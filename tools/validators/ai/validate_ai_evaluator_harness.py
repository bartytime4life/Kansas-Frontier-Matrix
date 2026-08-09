#!/usr/bin/env python3
"""Validate generic and Pass 12 public-safe AI evaluator-harness records."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, sys
from decimal import Decimal
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[3]
FIXTURES=ROOT/'fixtures/contracts/v1/ai/evaluator_harness/cases.json'
SCHEMA=ROOT/'schemas/contracts/v1/ai/evaluator_harness.schema.json'
HASHING_SRC=ROOT/'packages/hashing/src'
if HASHING_SRC.is_dir(): sys.path.insert(0,str(HASHING_SRC))
try:
 from hashing import compute_spec_hash as _shared_hash
except Exception:
 _shared_hash=None

REQUIRED={'evaluation_id','artifact_kind','candidate_ref','evidence_refs','metrics','policy_outcome','deterministic','network_access','result','reason_codes','spec_hash'}

def _fallback_hash(v): return 'sha256:'+hashlib.sha256(json.dumps(v,ensure_ascii=False,allow_nan=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def profile_hash(record):
 subject={'profile':record.get('profile'),'profile_input':record.get('profile_input'),'candidate_ref':record.get('candidate_ref'),'evidence_refs':record.get('evidence_refs')}
 return _shared_hash(subject) if _shared_hash else _fallback_hash(subject)
def _dec(v): return Decimal(str(v))
def _metric(name,value,threshold,comparison): return {'name':name,'value':float(value),'threshold':float(threshold),'comparison':comparison}
def _rectangular(grid): return isinstance(grid,list) and bool(grid) and all(isinstance(r,list) and r for r in grid) and len({len(r) for r in grid})==1

def derive_public(record):
 p=record['profile_input']; profile=record['profile']; codes=[]
 if record.get('profile_spec_hash')!=profile_hash(record): return [],'DENY','FAIL',['PROFILE_SPEC_HASH_MISMATCH']
 if profile=='PUBLIC_SAFE_RASTER_V1':
  ref=p['reference_grid']; cand=p['candidate_grid']; th=p['thresholds']
  if not _rectangular(ref) or not _rectangular(cand) or len(ref)!=len(cand) or any(len(a)!=len(b) for a,b in zip(ref,cand)):
   return [_metric('coverage',0,_dec(th['min_coverage']),'gte'),_metric('max_abs_error',0,_dec(th['max_abs_error']),'lte'),_metric('rmse',0,_dec(th['max_rmse']),'lte')],'DENY','FAIL',['RASTER_SHAPE_MISMATCH']
  diffs=[_dec(b)-_dec(a) for rr,cc in zip(ref,cand) for a,b in zip(rr,cc) if a is not None and b is not None]
  total=sum(len(r) for r in ref); coverage=Decimal(len(diffs))/Decimal(total)
  if not diffs: rmse=Decimal(0); maxerr=Decimal(0)
  else: rmse=(sum((d*d for d in diffs),Decimal(0))/Decimal(len(diffs))).sqrt(); maxerr=max(abs(d) for d in diffs)
  metrics=[_metric('coverage',coverage,_dec(th['min_coverage']),'gte'),_metric('max_abs_error',maxerr,_dec(th['max_abs_error']),'lte'),_metric('rmse',rmse,_dec(th['max_rmse']),'lte')]
  if coverage<_dec(th['min_coverage']): return metrics,'HOLD','FAIL',['RASTER_COVERAGE_INSUFFICIENT']
  if maxerr>_dec(th['max_abs_error']): codes.append('RASTER_MAX_ABS_ERROR_EXCEEDED')
  if rmse>_dec(th['max_rmse']): codes.append('RASTER_RMSE_EXCEEDED')
  return metrics,('FAIL' if codes else 'PASS'),('FAIL' if codes else 'PASS'),codes
 claims=p['claims']; allowed=set(p['allowed_citation_refs']); th=p['thresholds']
 if not allowed:
  chars=sum(len(c['text']) for c in claims)
  metrics=[_metric('character_count',chars,th['max_characters'],'lte'),_metric('citation_coverage',0,_dec(th['min_citation_coverage']),'gte'),_metric('sensitive_hits',0,th['max_sensitive_hits'],'lte'),_metric('unsupported_claims',len(claims),th['max_unsupported_claims'],'lte')]
  return metrics,'HOLD','FAIL',['TEXT_CITATION_REGISTRY_EMPTY']
 supported=sum(1 for c in claims if any(r in allowed for r in c['citation_refs'])); unsupported=len(claims)-supported; coverage=Decimal(supported)/Decimal(len(claims)); chars=sum(len(c['text']) for c in claims)
 hits=sum(c['text'].casefold().count(term.casefold()) for c in claims for term in p['sensitive_terms'])
 metrics=[_metric('character_count',chars,th['max_characters'],'lte'),_metric('citation_coverage',coverage,_dec(th['min_citation_coverage']),'gte'),_metric('sensitive_hits',hits,th['max_sensitive_hits'],'lte'),_metric('unsupported_claims',unsupported,th['max_unsupported_claims'],'lte')]
 if hits>th['max_sensitive_hits']: return metrics,'DENY','FAIL',['TEXT_SENSITIVE_TERM_HIT']
 if coverage<_dec(th['min_citation_coverage']): codes.append('TEXT_CITATION_COVERAGE_LOW')
 if unsupported>th['max_unsupported_claims']: codes.append('TEXT_UNSUPPORTED_CLAIMS_EXCEEDED')
 if chars>th['max_characters']: codes.append('TEXT_CHARACTER_LIMIT_EXCEEDED')
 return metrics,('FAIL' if codes else 'PASS'),('FAIL' if codes else 'PASS'),codes

def evaluate(record):
 if not isinstance(record,dict) or not REQUIRED.issubset(record): return 'ERROR'
 # The execution boundary is semantic and fail-closed. Classify a network-enabled
 # or non-deterministic candidate as DENY even when the schema's const guards also
 # reject it, so callers receive the finite policy outcome rather than a parser error.
 if record.get('network_access') is not False or record.get('deterministic') is not True: return 'DENY'
 errors=list(Draft202012Validator(json.loads(SCHEMA.read_text()),format_checker=FormatChecker()).iter_errors(record))
 if errors: return 'ERROR'
 if not record.get('evidence_refs') or not isinstance(record.get('metrics'),list) or not record['metrics']: return 'DENY'
 if record.get('profile') in {'PUBLIC_SAFE_RASTER_V1','PUBLIC_SAFE_TEXT_V1'}:
  metrics,gate,result,codes=derive_public(record)
  if record.get('metrics')!=metrics or record.get('policy_outcome') != ('ALLOW' if gate in {'PASS','FAIL'} else gate) or record.get('result')!=result or record.get('reason_codes')!=codes: return 'DENY'
  return gate
 if record.get('policy_outcome') in {'DENY','HOLD'}: return record['policy_outcome']
 if record.get('policy_outcome')=='ERROR': return 'ERROR'
 try: passed=all((m['value']>=m['threshold'] if m['comparison']=='gte' else m['value']<=m['threshold']) for m in record['metrics'])
 except (KeyError,TypeError): return 'ERROR'
 expected='PASS' if passed else 'FAIL'
 return expected if record.get('result')==expected else 'DENY'

def replay(path=FIXTURES):
 data=json.loads(Path(path).read_text()); failures=[]
 for case in data['cases']:
  actual=evaluate(case['record'])
  if actual!=case['expected']: failures.append((case['name'],case['expected'],actual))
 return failures

def main():
 p=argparse.ArgumentParser(); p.add_argument('path',nargs='?'); p.add_argument('--fixtures',action='store_true'); a=p.parse_args()
 if a.fixtures:
  failures=replay()
  if failures:
   for f in failures: print('FAIL',*f)
   raise SystemExit(1)
  print('PASS evaluator harness fixtures'); return
 if not a.path: p.error('path required unless --fixtures')
 print(evaluate(json.loads(Path(a.path).read_text())))
if __name__=='__main__': main()
