#!/usr/bin/env python3
"""Validate CatalogMatrix STAC/DCAT/PROV alignment without network access.

PASS proves local schema and tuple alignment only. It does not emit catalogs,
resolve evidence, decide policy, approve review, release, publish, or authorize use.
"""
from __future__ import annotations
import argparse, json, math, os, re, stat, sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[2]
SCHEMA=ROOT/'schemas/contracts/v1/data/catalog_matrix.schema.json'
FIXTURES=ROOT/'fixtures/data/catalog_matrix'
MANIFEST=FIXTURES/'expected_findings_manifest.json'
MAX_BYTES=256*1024
DENIED_PREFIXES=('raw:','work:','quarantine:','internal:','canonical:','model:')
REF_RE=re.compile(r'^[A-Za-z0-9][A-Za-z0-9._~:/#?=&%+@-]{0,319}$')
ERROR_CODES={'FILE_NOT_FOUND','FILE_READ_ERROR','FILE_TOO_LARGE','INPUT_SYMLINK_DENIED','JSON_INVALID','JSON_DUPLICATE_KEY','JSON_NONFINITE_NUMBER','ROOT_NOT_OBJECT','SCHEMA_UNAVAILABLE','MANIFEST_INVALID'}
class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
@dataclass(frozen=True,order=True)
class Finding: code:str; field:str; detail:str
@dataclass(frozen=True)
class ValidationResult:
    findings:tuple[Finding,...]
    @property
    def ok(self): return not self.findings
    @property
    def error(self): return any(f.code in ERROR_CODES for f in self.findings)
    @property
    def outcome(self): return 'PASS' if self.ok else ('ERROR' if self.error else 'FAIL')
def _pairs(items):
    out={}
    for key,value in items:
        if key in out: raise DuplicateKeyError
        out[key]=value
    return out
def _constant(_): raise NonFiniteNumberError
def _float(value):
    parsed=float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed
def _read(path):
    fd=None
    try:
        if path.is_symlink(): return None,[Finding('INPUT_SYMLINK_DENIED','/','symbolic links are denied')]
        fd=os.open(path,os.O_RDONLY|getattr(os,'O_CLOEXEC',0)|getattr(os,'O_NOFOLLOW',0))
        info=os.fstat(fd)
        if not stat.S_ISREG(info.st_mode): return None,[Finding('FILE_NOT_FOUND','/','input is not a regular file')]
        if info.st_size>MAX_BYTES: return None,[Finding('FILE_TOO_LARGE','/','input exceeds 256 KiB')]
        with os.fdopen(fd,'rb') as stream: fd=None; raw=stream.read(MAX_BYTES+1)
        value=json.loads(raw.decode(),object_pairs_hook=_pairs,parse_constant=_constant,parse_float=_float)
    except FileNotFoundError: return None,[Finding('FILE_NOT_FOUND','/','input file was not found')]
    except DuplicateKeyError: return None,[Finding('JSON_DUPLICATE_KEY','/','duplicate members are denied')]
    except NonFiniteNumberError: return None,[Finding('JSON_NONFINITE_NUMBER','/','numbers must be finite')]
    except json.JSONDecodeError: return None,[Finding('JSON_INVALID','/','input is not valid JSON')]
    except (OSError,UnicodeError,RecursionError,ValueError): return None,[Finding('FILE_READ_ERROR','/','input could not be read safely')]
    finally:
        if fd is not None: os.close(fd)
    if not isinstance(value,dict): return None,[Finding('ROOT_NOT_OBJECT','/','JSON root must be an object')]
    return value,[]
def _pointer(parts:Iterable[object]):
    encoded=[str(p).replace('~','~0').replace('/','~1') for p in parts]
    return '/'+('/'.join(encoded)) if encoded else '/'
def _schema(value):
    try:
        schema=json.loads(SCHEMA.read_text()); Draft202012Validator.check_schema(schema)
        validator=Draft202012Validator(schema,format_checker=FormatChecker())
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError): return [Finding('SCHEMA_UNAVAILABLE','/','schema could not be loaded safely')]
    errors=sorted(validator.iter_errors(value),key=lambda e:(_pointer(e.absolute_path),str(e.validator)))
    return [Finding('SCHEMA_INVALID',_pointer(e.absolute_path),f'schema constraint failed: {e.validator}') for e in errors[:50]]
def _refs(value,field,code):
    if not isinstance(value,list) or any(not isinstance(x,str) for x in value): return []
    findings=[]
    if value!=sorted(set(value)): findings.append(Finding(code,field,'references must be sorted and unique'))
    if any(not REF_RE.fullmatch(x) for x in value): findings.append(Finding('REFERENCE_INVALID',field,'reference violates bounded grammar'))
    if any(x.casefold().startswith(DENIED_PREFIXES) for x in value): findings.append(Finding('INTERNAL_REFERENCE_DENIED',field,'lifecycle-private references are denied'))
    return findings
def _semantic(value:Mapping[str,object]):
    findings=_refs(value.get('evidence_refs'),'/evidence_refs','EVIDENCE_REFS_NOT_CANONICAL')+_refs(value.get('source_refs'),'/source_refs','SOURCE_REFS_NOT_CANONICAL')
    artifact=value.get('artifact'); records=value.get('records')
    if isinstance(artifact,dict) and isinstance(records,dict):
        for kind in ('stac','dcat','prov'):
            record=records.get(kind)
            if not isinstance(record,dict): continue
            if record.get('artifact_id')!=artifact.get('artifact_id'): findings.append(Finding('CATALOG_ARTIFACT_ID_MISMATCH',f'/records/{kind}/artifact_id','record and artifact identity differ'))
            if record.get('digest')!=artifact.get('digest'): findings.append(Finding('CATALOG_DIGEST_MISMATCH',f'/records/{kind}/digest','record and artifact digest differ'))
            if record.get('release_ref')!=artifact.get('release_ref'): findings.append(Finding('CATALOG_RELEASE_REF_MISMATCH',f'/records/{kind}/release_ref','record and artifact release reference differ'))
        record_refs=[r.get('record_ref') for r in records.values() if isinstance(r,dict)]
        if len(record_refs)!=len(set(record_refs)): findings.append(Finding('CATALOG_RECORD_REF_DUPLICATE','/records','standard record references must be unique'))
    refs=[value.get(k) for k in ('policy_decision_ref','review_ref','correction_path_ref','rollback_ref')]
    if any(isinstance(x,str) and x.casefold().startswith(DENIED_PREFIXES) for x in refs): findings.append(Finding('INTERNAL_REFERENCE_DENIED','/','lifecycle-private references are denied'))
    decision=value.get('decision'); reasons=value.get('reason_codes')
    if decision=='READY' and reasons: findings.append(Finding('READY_REASON_CODES_NOT_EMPTY','/reason_codes','READY requires an empty reason list'))
    if decision in {'HOLD','DENY'} and not reasons: findings.append(Finding('NON_READY_REASON_REQUIRED','/reason_codes','HOLD or DENY requires a reason'))
    return sorted(set(findings))
def validate_value(value):
    schema=_schema(value); return ValidationResult(tuple(sorted(set(schema or _semantic(value)))))
def validate(path):
    value,findings=_read(path); return ValidationResult(tuple(findings)) if value is None else validate_value(value)
def run_fixtures():
    manifest,findings=_read(MANIFEST)
    if manifest is None or findings or not isinstance(manifest.get('cases'),list): print('CATALOG_MATRIX_FIXTURES_ERROR code=MANIFEST_INVALID'); return 2
    failures=[]
    for case in manifest['cases']:
        result=validate(FIXTURES/case['path']); actual=sorted({f.code for f in result.findings})
        if result.outcome!=case['expected_outcome'] or actual!=sorted(case['expected_findings']): failures.append(case['case_id'])
        print(f"CATALOG_MATRIX_FIXTURE case={case['case_id']} outcome={result.outcome} findings={','.join(actual) if actual else '-'}")
    if failures:
        for case in failures: print(f'CATALOG_MATRIX_FIXTURE_MISMATCH case={case}')
        return 1
    print(f"CATALOG_MATRIX_FIXTURES_VALID cases={len(manifest['cases'])} no_network=true authority=local-alignment-only"); return 0
def main(argv=None):
    parser=argparse.ArgumentParser(); parser.add_argument('path',nargs='?',type=Path); parser.add_argument('--fixtures',action='store_true'); args=parser.parse_args(argv)
    if args.fixtures: return run_fixtures()
    if args.path is None: parser.error('path is required unless --fixtures is used')
    result=validate(args.path)
    for finding in result.findings: print(f'CATALOG_MATRIX_{result.outcome} code={finding.code} field={finding.field} detail={finding.detail}')
    if result.ok: print(f'CATALOG_MATRIX_PASS path={args.path} authority=local-alignment-only'); return 0
    return 2 if result.error else 1
if __name__=='__main__': sys.exit(main())
