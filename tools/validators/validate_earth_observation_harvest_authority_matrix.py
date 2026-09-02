#!/usr/bin/env python3
"""Validate the inactive Earth-observation harvest authority matrix.

A PASS proves closed shape, deterministic ordering/spec_hash, repository-reference
closure, and cross-row access-surface closure only. It authorizes no endpoint,
credential, source, network request, RAW admission, promotion, release, or public use.
"""
from __future__ import annotations
import argparse,json,math,os,stat,sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path,PurePosixPath
from typing import Any,Iterable,Mapping,Sequence
from jsonschema import Draft202012Validator,FormatChecker
ROOT=Path(__file__).resolve().parents[2]
HASH_SRC=ROOT/'packages/hashing/src'
if str(HASH_SRC) not in sys.path: sys.path.insert(0,str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402
MATRIX=ROOT/'control_plane/earth_observation_harvest_authority_matrix.json'
SCHEMA=ROOT/'schemas/contracts/v1/source/earth_observation_harvest_authority_matrix.schema.json'
FIXTURES=ROOT/'fixtures/contracts/v1/source/earth_observation_harvest_authority_matrix'; CASES=FIXTURES/'expected_findings_manifest.json'
MAX_BYTES=2*1024*1024; MAX_SCHEMA_FINDINGS=100; SCOPE='eo-harvest-authority-crosswalk-only'
class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
@dataclass(frozen=True,order=True)
class Finding: code:str; field:str
@dataclass(frozen=True)
class Result:
    findings:tuple[Finding,...]
    @property
    def ok(self)->bool:return not self.findings
    @property
    def outcome(self)->str:return 'PASS' if self.ok else 'ERROR'
def _unique(pairs:list[tuple[str,Any]])->dict[str,Any]:
    out={}
    for k,v in pairs:
        if k in out:raise DuplicateKeyError(k)
        out[k]=v
    return out
def _reject(_v:str)->None:raise NonFiniteNumberError
def _finite(v:str)->float:
    x=float(v)
    if not math.isfinite(x):raise NonFiniteNumberError
    return x
def _read(path:Path)->tuple[dict[str,Any]|None,list[Finding]]:
    try:
        if path.is_symlink():return None,[Finding('INPUT_SYMLINK_DENIED','/')]
        flags=os.O_RDONLY|getattr(os,'O_CLOEXEC',0)|getattr(os,'O_NOFOLLOW',0);fd=os.open(path,flags)
        try:
            if not stat.S_ISREG(os.fstat(fd).st_mode):return None,[Finding('INPUT_NOT_FILE','/')]
            with os.fdopen(fd,'rb') as s:fd=-1;raw=s.read(MAX_BYTES+1)
        finally:
            if fd>=0:os.close(fd)
        if len(raw)>MAX_BYTES:return None,[Finding('INPUT_TOO_LARGE','/')]
        value=json.loads(raw.decode('utf-8'),object_pairs_hook=_unique,parse_constant=_reject,parse_float=_finite)
    except FileNotFoundError:return None,[Finding('INPUT_NOT_FILE','/')]
    except (UnicodeDecodeError,json.JSONDecodeError):return None,[Finding('JSON_INVALID','/')]
    except DuplicateKeyError:return None,[Finding('JSON_DUPLICATE_KEY','/')]
    except NonFiniteNumberError:return None,[Finding('JSON_NONFINITE_NUMBER','/')]
    except OSError:return None,[Finding('INPUT_READ_ERROR','/')]
    if not isinstance(value,dict):return None,[Finding('ROOT_NOT_OBJECT','/')]
    return value,[]
def _ptr(parts:Iterable[Any])->str:
    items=[str(p).replace('~','~0').replace('/','~1') for p in parts];return '/'+ '/'.join(items) if items else '/'
def _schema(value:Mapping[str,Any])->list[Finding]:
    try:
        schema=json.loads(SCHEMA.read_text(encoding='utf-8'));Draft202012Validator.check_schema(schema);errors=list(islice(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(value),MAX_SCHEMA_FINDINGS+1))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError,RecursionError):return [Finding('SCHEMA_UNAVAILABLE','/')]
    findings=[Finding('SCHEMA_INVALID',_ptr(e.absolute_path)) for e in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors)>MAX_SCHEMA_FINDINGS:findings.append(Finding('SCHEMA_FINDINGS_TRUNCATED','/'))
    return findings
def _path(raw:Any)->PurePosixPath|None:
    if not isinstance(raw,str) or not raw or raw.startswith('/') or '\\' in raw:return None
    p=PurePosixPath(raw)
    if str(p)!=raw or any(x in {'.','..'} for x in p.parts):return None
    return p
def _semantic(value:Mapping[str,Any])->list[Finding]:
    findings=[];declared=value.get('spec_hash')
    if isinstance(declared,str) and declared!=compute_spec_hash({k:v for k,v in value.items() if k!='spec_hash'}):findings.append(Finding('MATRIX_SPEC_HASH_MISMATCH','/spec_hash'))
    entries=value.get('entries') if isinstance(value.get('entries'),list) else [];ids=[e.get('authority_id') for e in entries if isinstance(e,dict)]
    if ids!=sorted(ids):findings.append(Finding('ENTRIES_NOT_CANONICAL','/entries'))
    if len(ids)!=len(set(ids)):findings.append(Finding('AUTHORITY_ID_DUPLICATE','/entries'))
    by_id={e.get('authority_id'):e for e in entries if isinstance(e,dict)}
    for i,e in enumerate(entries):
        if not isinstance(e,dict):continue
        base=f'/entries/{i}'
        for field,allowed_root in (('catalog_doc_ref','docs/sources/catalog/'),('connector_ref','connectors/')):
            relative=_path(e.get(field))
            if relative is None or not str(relative).startswith(allowed_root):findings.append(Finding('REPO_REF_INVALID',f'{base}/{field}'));continue
            candidate=ROOT.joinpath(*relative.parts)
            try:
                if candidate.is_symlink() or not candidate.is_file():findings.append(Finding('REPO_REF_MISSING',f'{base}/{field}'))
            except OSError:findings.append(Finding('REPO_REF_UNREADABLE',f'{base}/{field}'))
        ref=e.get('access_surface_ref')
        if ref is not None:
            target=by_id.get(ref)
            if not isinstance(target,dict) or target.get('authority_role') not in {'ACCESS_SURFACE','CATALOG_ENDPOINT'}:findings.append(Finding('ACCESS_SURFACE_REF_UNRESOLVED',f'{base}/access_surface_ref'))
        reasons=e.get('reason_codes')
        if isinstance(reasons,list) and reasons!=sorted(set(reasons)):findings.append(Finding('REASON_CODES_NOT_CANONICAL',f'{base}/reason_codes'))
        harvest=e.get('harvest')
        if isinstance(harvest,dict):
            for field in ('allowed_operations','candidate_target_zones'):
                vals=harvest.get(field)
                if isinstance(vals,list) and vals!=sorted(set(vals)):findings.append(Finding('HARVEST_ARRAY_NOT_CANONICAL',f'{base}/harvest/{field}'))
            if harvest.get('network_authorized') is True and harvest.get('state')!='ACTIVE':findings.append(Finding('NETWORK_AUTHORITY_OVERREACH',f'{base}/harvest/network_authorized'))
        access=e.get('access')
        if isinstance(access,dict) and isinstance(access.get('endpoint_ref'),str) and '://' in access['endpoint_ref']:findings.append(Finding('RAW_ENDPOINT_FORBIDDEN',f'{base}/access/endpoint_ref'))
    return findings
def validate(path:Path)->Result:
    value,findings=_read(path)
    if value is None:return Result(tuple(sorted(set(findings))))
    findings.extend(_schema(value))
    if not findings:findings.extend(_semantic(value))
    return Result(tuple(sorted(set(findings))))
def run_fixtures()->int:
    try:cases=json.loads(CASES.read_text(encoding='utf-8'))['cases']
    except (OSError,UnicodeError,json.JSONDecodeError,KeyError):return 1
    passed=True
    for case in cases:
        result=validate(FIXTURES/case['input']);codes=sorted({f.code for f in result.findings});match=result.outcome==case['expected_outcome'] and codes==case['expected_findings']
        print(json.dumps({'case_id':case['case_id'],'outcome':result.outcome,'findings':codes,'suite_match':match},sort_keys=True,separators=(',',':')));passed=passed and match
    return 0 if passed else 1
def main(argv:Sequence[str]|None=None)->int:
    parser=argparse.ArgumentParser(description='Validate EO harvest authority matrix projections.');parser.add_argument('files',nargs='*',type=Path);parser.add_argument('--fixtures',action='store_true');args=parser.parse_args(argv)
    if args.fixtures:
        if args.files:parser.error('--fixtures cannot be combined with files')
        return run_fixtures()
    files=args.files or [MATRIX];failed=False
    for path in sorted(files,key=lambda p:p.as_posix()):
        result=validate(path);print(json.dumps({'file':path.as_posix(),'outcome':result.outcome,'findings':[{'code':f.code,'field':f.field} for f in result.findings],'scope':SCOPE},sort_keys=True,separators=(',',':')));failed=failed or not result.ok
    return 1 if failed else 0
if __name__=='__main__':raise SystemExit(main())
