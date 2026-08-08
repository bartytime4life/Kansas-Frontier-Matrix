#!/usr/bin/env python3
"""Validate the projection-only KFM Domain Lane Register without network access."""
from __future__ import annotations
import argparse, hashlib, json, math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[3]
REGISTER=ROOT/'control_plane/domain_lane_register.yaml'
SCHEMA=ROOT/'schemas/contracts/v1/governance/domain_lane_register.schema.json'
DOCTRINE_SHA='44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e'
LANES=('agriculture','archaeology','atmosphere','fauna','flora','geology','habitat','hazards','hydrology','people-dna-land','roads-rail-trade','settlements-infrastructure','soil')
CROSS=('matrix','scene','spatial')
ALIASES={'air':'atmosphere','settlement':'settlements-infrastructure','transport':'roads-rail-trade'}
MAX=4*1024*1024

class DuplicateKey(ValueError): pass
class NonFinite(ValueError): pass
@dataclass(frozen=True,order=True)
class Finding: code:str; field:str
@dataclass(frozen=True)
class Result:
    findings:tuple[Finding,...]
    @property
    def ok(self)->bool:return not self.findings
    @property
    def outcome(self)->str:
        codes={f.code for f in self.findings}
        if not codes:return 'PASS'
        if any(c.startswith(('INPUT_','JSON_','SCHEMA_','REPO_ROOT_')) for c in codes):return 'ERROR_VALIDATOR'
        if codes&{'AUTHORITY_BINDING_MISSING','DECISION_EVIDENCE_MISSING','DOMAIN_DOCUMENTATION_MISSING'}:return 'HOLD_UNRESOLVED'
        if codes&{'CANONICAL_LANE_MISSING','UNEXPECTED_DOMAIN_LANE','DOMAIN_ROOT_PRESENT'}:return 'FAIL_NEW_DRIFT'
        return 'FAIL_INVARIANT'

def _unique(pairs:list[tuple[str,Any]])->dict[str,Any]:
    out={}
    for k,v in pairs:
        if k in out:raise DuplicateKey
        out[k]=v
    return out

def _nonfinite(_:str)->None:raise NonFinite

def _float(v:str)->float:
    n=float(v)
    if not math.isfinite(n):raise NonFinite
    return n

def load(path:Path)->tuple[dict[str,Any]|None,list[Finding]]:
    try:
        if path.is_symlink():return None,[Finding('INPUT_SYMLINK_DENIED','/')]
        if not path.is_file():return None,[Finding('INPUT_NOT_FILE','/')]
        if path.stat().st_size>MAX:return None,[Finding('INPUT_TOO_LARGE','/')]
        value=json.loads(path.read_text(),object_pairs_hook=_unique,parse_constant=_nonfinite,parse_float=_float)
    except DuplicateKey:return None,[Finding('JSON_DUPLICATE_KEY','/')]
    except NonFinite:return None,[Finding('JSON_NONFINITE_NUMBER','/')]
    except json.JSONDecodeError:return None,[Finding('JSON_COMPATIBLE_YAML_REQUIRED','/')]
    except (OSError,UnicodeError):return None,[Finding('INPUT_READ_ERROR','/')]
    if not isinstance(value,dict):return None,[Finding('ROOT_NOT_OBJECT','/')]
    return value,[]

def ptr(parts:Iterable[Any])->str:
    bits=[str(x).replace('~','~0').replace('/','~1') for x in parts]
    return '/'+('/'.join(bits)) if bits else '/'

def schema_findings(value:Mapping[str,Any])->list[Finding]:
    try:
        schema=json.loads(SCHEMA.read_text());Draft202012Validator.check_schema(schema)
        errors=list(islice(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(value),101))
    except Exception:return [Finding('SCHEMA_UNAVAILABLE','/')]
    out=[Finding('SCHEMA_INVALID',ptr(e.absolute_path)) for e in sorted(errors[:100],key=lambda e:(ptr(e.absolute_path),str(e.validator)))]
    if len(errors)>100:out.append(Finding('SCHEMA_FINDINGS_TRUNCATED','/'))
    return out

def blob(path:Path)->str:
    raw=path.read_bytes();return hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()

def bindings(value:Mapping[str,Any],root:Path)->list[Finding]:
    out=[]
    checks=[(value.get('doctrine'),'sha256',lambda p:'sha256:'+hashlib.sha256(p.read_bytes()).hexdigest(),'/doctrine'),(value.get('narrative_register'),'git_blob',blob,'/narrative_register'),(value.get('root_registry'),'git_blob',blob,'/root_registry')]
    for item,key,fn,field in checks:
        if not isinstance(item,Mapping):continue
        path=root/str(item.get('path',''))
        if not path.is_file():out.append(Finding('AUTHORITY_BINDING_MISSING',field+'/path'));continue
        try:observed=fn(path)
        except OSError:out.append(Finding('AUTHORITY_BINDING_MISSING',field+'/path'));continue
        if observed!=item.get(key):out.append(Finding('AUTHORITY_DIGEST_MISMATCH',field+'/'+key))
    if not (root/'docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md').is_file():out.append(Finding('DECISION_EVIDENCE_MISSING','/doctrine/decision_ref'))
    return out

def semantic(value:Mapping[str,Any])->list[Finding]:
    out=[];doctrine=value.get('doctrine',{});rootreg=value.get('root_registry',{})
    if isinstance(doctrine,Mapping):
        if doctrine.get('sha256')!='sha256:'+DOCTRINE_SHA:out.append(Finding('DOCTRINE_DIGEST_MISMATCH','/doctrine/sha256'))
        if doctrine.get('decision_ref')!='ADR-0029':out.append(Finding('DECISION_EVIDENCE_MISSING','/doctrine/decision_ref'))
    if isinstance(rootreg,Mapping) and rootreg.get('base_ref')!=value.get('base_ref'):out.append(Finding('BASE_REF_MISMATCH','/root_registry/base_ref'))
    if tuple(value.get('cross_cutting_exclusions',[]))!=CROSS:out.append(Finding('CROSS_CUTTING_SET_MISMATCH','/cross_cutting_exclusions'))
    if value.get('unresolved_aliases')!=ALIASES:out.append(Finding('ALIAS_SET_MISMATCH','/unresolved_aliases'))
    defaults=value.get('lane_defaults',{})
    if isinstance(defaults,Mapping) and defaults.get('owner_identity') is not None:out.append(Finding('OWNER_IDENTITY_OVERCLAIM','/lane_defaults/owner_identity'))
    lanes=[x for x in value.get('lanes',[]) if isinstance(x,Mapping)];ids=[x.get('lane_id') for x in lanes]
    if ids!=sorted(ids):out.append(Finding('LANES_NOT_CANONICAL','/lanes'))
    if len(ids)!=len(set(ids)):out.append(Finding('LANE_ID_DUPLICATE','/lanes'))
    seen={x for x in ids if isinstance(x,str)}
    for x in sorted(set(LANES)-seen):out.append(Finding('CANONICAL_LANE_MISSING','/lanes/'+x))
    for x in sorted(seen-set(LANES)):out.append(Finding('UNEXPECTED_DOMAIN_LANE','/lanes/'+x))
    paths=[];aliases=[]
    for i,lane in enumerate(lanes):
        base=f'/lanes/{i}';lane_id=lane.get('lane_id');path=lane.get('documentation_path');alias=lane.get('code_alias');paths.append(path);aliases.append(alias)
        if isinstance(lane_id,str):
            if path!=f'docs/domains/{lane_id}/':out.append(Finding('DOCUMENTATION_PATH_MISMATCH',base+'/documentation_path'))
            if alias!=lane_id.replace('-','_'):out.append(Finding('CODE_ALIAS_MISMATCH',base+'/code_alias'))
    for values,code in ((paths,'DOCUMENTATION_PATH_DUPLICATE'),(aliases,'CODE_ALIAS_DUPLICATE')):
        vals=[x for x in values if isinstance(x,str)]
        if len(vals)!=len(set(vals)):out.append(Finding(code,'/lanes'))
    return out

def repository(value:Mapping[str,Any],root:Path)->list[Finding]:
    try:r=root.resolve(strict=True)
    except OSError:return [Finding('REPO_ROOT_UNAVAILABLE','/repo_root')]
    out=[]
    for i,lane in enumerate(value.get('lanes',[])):
        if not isinstance(lane,Mapping) or not isinstance(lane.get('lane_id'),str):continue
        lane_id=lane['lane_id']
        if not (r/f'docs/domains/{lane_id}').is_dir():out.append(Finding('DOMAIN_DOCUMENTATION_MISSING',f'/lanes/{i}/documentation_path'))
        if (r/lane_id).exists():out.append(Finding('DOMAIN_ROOT_PRESENT','/repo_roots/'+lane_id))
    return out

def validate(path:Path,*,repo_root:Path=ROOT,check_repository:bool=True,check_bindings:bool=True)->Result:
    value,out=load(path)
    if value is None:return Result(tuple(sorted(set(out))))
    out+=schema_findings(value)
    if not out:
        out+=semantic(value)
        if check_bindings:out+=bindings(value,repo_root)
        if check_repository:out+=repository(value,repo_root)
    return Result(tuple(sorted(set(out))))

def serialize(path:Path,result:Result)->str:
    try:name=path.resolve().relative_to(ROOT.resolve()).as_posix()
    except Exception:name=path.name
    return json.dumps({'file':name,'findings':[{'code':f.code,'field':f.field} for f in result.findings],'outcome':result.outcome,'scope':'domain-lane-register-projection-only','authority':{'creates_domain':False,'assigns_steward':False,'activates_source':False,'writes_lifecycle_state':False,'authorizes_release':False,'deploys':False,'promotes':False,'publishes':False}},sort_keys=True,separators=(',',':'))

def main(argv:Sequence[str]|None=None)->int:
    p=argparse.ArgumentParser();p.add_argument('path',nargs='?',type=Path,default=REGISTER);p.add_argument('--repo-root',type=Path,default=ROOT);p.add_argument('--no-repository-checks',action='store_true');p.add_argument('--no-binding-checks',action='store_true');a=p.parse_args(argv)
    result=validate(a.path,repo_root=a.repo_root,check_repository=not a.no_repository_checks,check_bindings=not a.no_binding_checks);print(serialize(a.path,result));return 0 if result.ok else 1
if __name__=='__main__':raise SystemExit(main())
