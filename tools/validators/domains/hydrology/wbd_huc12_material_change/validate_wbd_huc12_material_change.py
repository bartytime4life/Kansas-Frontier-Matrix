#!/usr/bin/env python3
"""Validate fixture-only WBD HUC12 material-change assessments."""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT=Path(__file__).resolve().parents[5]
SCHEMA_PATH=REPO_ROOT/"schemas/contracts/v1/domains/hydrology/wbd_huc12_material_change_assessment.schema.json"
MAX_JSON_BYTES=4*1024*1024; MAX_SCHEMA_FINDINGS=100

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
class GeometryError(ValueError): pass
@dataclass(frozen=True,order=True)
class Finding: code:str; path:str
@dataclass(frozen=True)
class ValidationResult:
 findings:tuple[Finding,...]
 @property
 def ok(self)->bool:return not self.findings

def _unique_object(pairs:list[tuple[str,Any]])->dict[str,Any]:
 out={}
 for k,v in pairs:
  if k in out: raise DuplicateKeyError(k)
  out[k]=v
 return out

def _reject_nonfinite(v:str)->None: raise NonFiniteNumberError(v)
def _pointer(parts:Iterable[object])->str:
 encoded=[str(x).replace('~','~0').replace('/','~1') for x in parts]; return '/'+('/'.join(encoded)) if encoded else '/'
def _load_payload(path:Path)->tuple[dict[str,Any]|None,list[Finding]]:
 try:
  if path.is_symlink(): return None,[Finding('INPUT_SYMLINK_DENIED','/')]
  if not path.is_file(): return None,[Finding('INPUT_NOT_FILE','/')]
  if path.stat().st_size>MAX_JSON_BYTES:return None,[Finding('INPUT_TOO_LARGE','/')]
  value=json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=_unique_object,parse_constant=_reject_nonfinite)
 except UnicodeError:return None,[Finding('JSON_NOT_UTF8','/')]
 except DuplicateKeyError:return None,[Finding('JSON_DUPLICATE_KEY','/')]
 except NonFiniteNumberError:return None,[Finding('JSON_NONFINITE_NUMBER','/')]
 except json.JSONDecodeError:return None,[Finding('JSON_INVALID','/')]
 except OSError:return None,[Finding('INPUT_UNREADABLE','/')]
 if not isinstance(value,dict):return None,[Finding('ROOT_NOT_OBJECT','/')]
 return value,[]
def _schema_validator()->Draft202012Validator:
 schema=json.loads(SCHEMA_PATH.read_text()); Draft202012Validator.check_schema(schema); return Draft202012Validator(schema,format_checker=FormatChecker())
def _schema_findings(payload:Mapping[str,Any])->list[Finding]:
 try: errors=list(islice(_schema_validator().iter_errors(payload),MAX_SCHEMA_FINDINGS+1))
 except (OSError,UnicodeError,json.JSONDecodeError,ValueError,RecursionError):return [Finding('SCHEMA_UNAVAILABLE','/')]
 truncated=len(errors)>MAX_SCHEMA_FINDINGS; ordered=sorted(errors,key=lambda e:(_pointer(e.absolute_path),str(e.validator)))[:MAX_SCHEMA_FINDINGS]
 findings=[Finding('SCHEMA_INVALID',_pointer(e.absolute_path)) for e in ordered]
 if truncated:findings.append(Finding('SCHEMA_FINDINGS_TRUNCATED','/'))
 return findings

def canonical_spec_hash(payload:Mapping[str,Any])->str:
 body={k:v for k,v in payload.items() if k!='spec_hash'}; encoded=json.dumps(body,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode(); return 'sha256:'+hashlib.sha256(encoded).hexdigest()
def _point(value:Any,precision:int)->tuple[float,float]:
 if not isinstance(value,list) or len(value)<2:raise GeometryError('point')
 x=float(value[0]);y=float(value[1])
 if not math.isfinite(x) or not math.isfinite(y) or not -180<=x<=180 or not -90<=y<=90:raise GeometryError('range')
 return (round(x,precision),round(y,precision))
def _min_rotation(points:list[tuple[float,float]])->list[tuple[float,float]]:
 candidates=[]
 for seq in (points,list(reversed(points))):
  candidates.extend(seq[i:]+seq[:i] for i in range(len(seq)))
 return min(candidates)
def _ring(value:Any,precision:int)->list[list[float]]:
 if not isinstance(value,list):raise GeometryError('ring')
 points=[_point(v,precision) for v in value]
 if len(points)>=2 and points[0]==points[-1]:points=points[:-1]
 if len(points)<3 or len(set(points))<3:raise GeometryError('vertices')
 normalized=_min_rotation(points); normalized.append(normalized[0]); return [[x,y] for x,y in normalized]
def _polygon(value:Any,precision:int)->list[Any]:
 if not isinstance(value,list) or not value:raise GeometryError('polygon')
 exterior=_ring(value[0],precision); holes=sorted((_ring(v,precision) for v in value[1:]),key=lambda r:json.dumps(r,separators=(',',':'))); return [exterior,*holes]
def canonical_geometry(geometry:Mapping[str,Any],precision:int)->dict[str,Any]:
 kind=geometry['type']; coords=geometry['coordinates']
 if kind=='Polygon':normalized=_polygon(coords,precision)
 elif kind=='MultiPolygon':normalized=sorted((_polygon(v,precision) for v in coords),key=lambda p:json.dumps(p,separators=(',',':')))
 else:raise GeometryError('type')
 return {'type':kind,'coordinates':normalized}
def canonical_feature_fingerprint(feature:Mapping[str,Any],precision:int)->str:
 payload={'geometry':canonical_geometry(feature['geometry'],precision),'areasqkm':round(float(feature['areasqkm']),6)}
 encoded=json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode(); return 'sha256:'+hashlib.sha256(encoded).hexdigest()
def _geometry_hash(feature:Mapping[str,Any],precision:int)->str:
 encoded=json.dumps(canonical_geometry(feature['geometry'],precision),sort_keys=True,separators=(',',':')).encode(); return hashlib.sha256(encoded).hexdigest()
def expected_decision(payload:Mapping[str,Any])->dict[str,Any]:
 prior=payload['prior']; current=payload['current']; precision=int(payload['normalization']['coordinate_precision'])
 if prior is None:return {'outcome':'ADD','change_types':['added']}
 if current is None:return {'outcome':'REMOVE','change_types':['removed']}
 changes=[]
 if round(float(prior['feature']['areasqkm']),6)!=round(float(current['feature']['areasqkm']),6):changes.append('area_change')
 if _geometry_hash(prior['feature'],precision)!=_geometry_hash(current['feature'],precision):changes.append('geometry_change')
 return {'outcome':'MATERIAL_CHANGE' if changes else 'NO_CHANGE','change_types':sorted(changes)}
def _semantic_findings(payload:Mapping[str,Any])->list[Finding]:
 findings=[]; precision=int(payload['normalization']['coordinate_precision']); geometry_valid=True
 for side in ('prior','current'):
  snapshot=payload[side]
  if snapshot is None:continue
  if snapshot['feature']['huc12']!=payload['huc12']:findings.append(Finding('HUC12_ID_MISMATCH',f'/{side}/feature/huc12'))
  try: expected=canonical_feature_fingerprint(snapshot['feature'],precision)
  except (GeometryError,TypeError,ValueError,KeyError):
   findings.append(Finding('GEOMETRY_INVALID',f'/{side}/feature/geometry'));geometry_valid=False;continue
  if snapshot['fingerprint']!=expected:findings.append(Finding('FEATURE_FINGERPRINT_MISMATCH',f'/{side}/fingerprint'))
 if geometry_valid:
  decision=expected_decision(payload)
  if payload['decision']['change_types']!=decision['change_types']:findings.append(Finding('DECISION_CHANGE_TYPES_MISMATCH','/decision/change_types'))
  if payload['decision']['outcome']!=decision['outcome']:findings.append(Finding('DECISION_OUTCOME_MISMATCH','/decision/outcome'))
 if payload['spec_hash']!=canonical_spec_hash(payload):findings.append(Finding('SPEC_HASH_MISMATCH','/spec_hash'))
 return findings
def validate_payload(payload:Mapping[str,Any])->ValidationResult:
 findings=_schema_findings(payload)
 if not findings:findings.extend(_semantic_findings(payload))
 return ValidationResult(tuple(sorted(set(findings))))
def validate_file(path:Path)->ValidationResult:
 payload,findings=_load_payload(path)
 if payload is None:return ValidationResult(tuple(sorted(findings)))
 return validate_payload(payload)
def _parser()->argparse.ArgumentParser:
 p=argparse.ArgumentParser(description='Validate a fixture-only WBD HUC12 material-change assessment.');p.add_argument('path',type=Path);return p
def main(argv:Sequence[str]|None=None)->int:
 args=_parser().parse_args(argv);result=validate_file(args.path);output={'ok':result.ok,'findings':[{'code':f.code,'path':f.path} for f in result.findings],'scope':'fixture-only-wbd-huc12-material-change','authority':{'network_fetch':False,'source_activation':False,'lifecycle_write':False,'promotion':False,'publication':False}};print(json.dumps(output,sort_keys=True,separators=(',',':')));return 0 if result.ok else 1
if __name__=='__main__':sys.exit(main())
