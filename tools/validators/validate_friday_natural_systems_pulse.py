#!/usr/bin/env python3
"""Validate fixture-only FridayNaturalSystemsPulseCandidate records."""
from __future__ import annotations
import argparse, copy, hashlib, json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence
from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT=Path(__file__).resolve().parents[2]
SCHEMA_PATH=REPO_ROOT/'schemas/contracts/v1/data/friday_natural_systems_pulse.schema.json'
MATERIAL_SCHEMA_PATH=REPO_ROOT/'schemas/contracts/v1/data/material_change_assessment.schema.json'
FIXTURE_ROOT=REPO_ROOT/'fixtures/contracts/v1/data/friday_natural_systems_pulse'
UPSTREAM_ROOT=FIXTURE_ROOT/'upstream'; MAX_FILE_BYTES=1_048_576
SCOPE='friday-natural-systems-pulse-fixture-local-consistency-only'
EXPECTED_DOMAINS=('atmosphere','fauna_habitat','hydrology','soil','vegetation')
class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
@dataclass(frozen=True,order=True)
class Finding: code:str; field:str
@dataclass(frozen=True)
class ValidationResult:
    findings:tuple[Finding,...]
    @property
    def ok(self): return not self.findings

def _unique(pairs):
    out={}
    for k,v in pairs:
        if k in out: raise DuplicateKeyError
        out[k]=v
    return out
def _nonfinite(_): raise NonFiniteNumberError
def _read(path):
    if path.is_symlink(): return None,[Finding('FILE_SYMLINK_DENIED','/')],None
    if not path.is_file(): return None,[Finding('FILE_NOT_FOUND','/')],None
    try:
        if path.stat().st_size>MAX_FILE_BYTES: return None,[Finding('FILE_TOO_LARGE','/')],None
        raw=path.read_bytes(); obj=json.loads(raw.decode(),object_pairs_hook=_unique,parse_constant=_nonfinite)
    except UnicodeDecodeError:return None,[Finding('JSON_NOT_UTF8','/')],None
    except DuplicateKeyError:return None,[Finding('JSON_DUPLICATE_KEY','/')],None
    except NonFiniteNumberError:return None,[Finding('JSON_NONFINITE_NUMBER','/')],None
    except json.JSONDecodeError:return None,[Finding('JSON_INVALID','/')],None
    except OSError:return None,[Finding('FILE_READ_ERROR','/')],None
    return (obj,[],raw) if isinstance(obj,dict) else (None,[Finding('ROOT_NOT_OBJECT','/')],raw)
def _ptr(parts:Iterable[Any]):
    p=[str(x).replace('~','~0').replace('/','~1') for x in parts]; return '/'+('/'.join(p)) if p else '/'
def _schema_findings(obj,path,unavailable):
    try:s=json.loads(path.read_text());Draft202012Validator.check_schema(s)
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError):return [Finding(unavailable,'/')]
    return sorted({Finding('SCHEMA_INVALID',_ptr(e.absolute_path)) for e in Draft202012Validator(s,format_checker=FormatChecker()).iter_errors(obj)})
def _spec_hash(obj):
    p=copy.deepcopy(obj);p.pop('pulse_id',None);p.pop('spec_hash',None)
    return 'sha256:'+hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def _time(v):
    if not isinstance(v,str):return None
    try:d=datetime.fromisoformat(v.replace('Z','+00:00'))
    except ValueError:return None
    return d.astimezone(timezone.utc) if d.tzinfo else None
def _material_semantic_findings(obj):
    c,comp,g=(obj.get(k) for k in ('classification','comparison','governance'))
    if not all(isinstance(x,dict) for x in (c,comp,g)):return [Finding('ASSESSMENT_INVALID','/entries')]
    table={'UNCHANGED':(False,'NON_EVENT',False),'BYTE_ONLY':(False,'NON_EVENT',False),'SEMANTIC_NON_MATERIAL':(False,'NON_EVENT',True),'MATERIAL':(True,'PROMOTION_CANDIDATE',True),'UNDETERMINED':(None,'HOLD',None),'ERROR':(None,'ERROR',None)}
    t=table.get(c.get('change_class'));bad=t is None
    if t:
        m,o,s=t;bad|=c.get('material') is not m or c.get('outcome')!=o or (s is not None and comp.get('semantic_changed') is not s)
    bad|=any(g.get(k) is not False for k in ('authority_created','policy_evaluated','promotion_authorized','public_use_allowed')) or g.get('release_ref') is not None
    return [Finding('ASSESSMENT_INVALID','/entries')] if bad else []
def _assessment(entry,i):
    field=f'/entries/{i}';ref=entry.get('assessment_ref')
    if not isinstance(ref,str):return None,None,[Finding('ASSESSMENT_REF_INVALID',field)]
    rel=Path(ref)
    if rel.is_absolute() or '..' in rel.parts:return None,None,[Finding('ASSESSMENT_REF_ESCAPE',field)]
    target=REPO_ROOT/rel
    if target.is_symlink():return None,None,[Finding('ASSESSMENT_FILE_SYMLINK_DENIED',field)]
    try:r=target.resolve();r.relative_to(UPSTREAM_ROOT.resolve())
    except (OSError,ValueError):return None,None,[Finding('ASSESSMENT_REF_ESCAPE',field)]
    if not r.is_file():return None,None,[Finding('ASSESSMENT_FILE_NOT_FOUND',field)]
    obj,_,raw=_read(r)
    if obj is None or raw is None or _material_semantic_findings(obj):return None,None,[Finding('ASSESSMENT_INVALID',field)]
    return obj,'sha256:'+hashlib.sha256(raw).hexdigest(),[]
def _expected(outcomes):
    c={x:outcomes.count(x) for x in ('NON_EVENT','PROMOTION_CANDIDATE','HOLD','ERROR')}
    if c['ERROR']:o,e,r='ERROR',False,['DOMAIN_ASSESSMENT_ERROR','DOMAIN_COVERAGE_COMPLETE','NO_AUTOMATED_EMISSION']
    elif c['HOLD']:o,e,r='HOLD',False,['DOMAIN_ASSESSMENT_HOLD','DOMAIN_COVERAGE_COMPLETE','NO_AUTOMATED_EMISSION']
    elif c['PROMOTION_CANDIDATE']:o,e,r='PULSE_CANDIDATE',True,['DOMAIN_COVERAGE_COMPLETE','MATERIAL_CHANGE_PRESENT','WHOLE_BUNDLE_REVIEW_REQUIRED']
    else:o,e,r='NO_EVENT',False,['ALL_DOMAINS_NON_EVENT','DOMAIN_COVERAGE_COMPLETE','NO_AUTOMATED_EMISSION']
    return {'entry_count':len(outcomes),'non_event_count':c['NON_EVENT'],'material_count':c['PROMOTION_CANDIDATE'],'hold_count':c['HOLD'],'error_count':c['ERROR'],'emit_candidate':e,'outcome':o,'reason_codes':sorted(r)}
def _semantic(obj):
    f=[];entries,window,summary=(obj.get(k) for k in ('entries','window','summary'))
    if not isinstance(entries,list):return [Finding('ENTRIES_INVALID','/entries')]
    if not isinstance(window,dict) or not isinstance(summary,dict):return [Finding('PULSE_INVALID','/')]
    domains=[x.get('domain') for x in entries if isinstance(x,dict)]
    if domains!=sorted(domains):f.append(Finding('DOMAINS_NOT_CANONICAL','/entries'))
    if sorted(domains)!=list(EXPECTED_DOMAINS):f.append(Finding('DOMAIN_COVERAGE_INCOMPLETE','/entries'))
    start,end,assessed=(_time(window.get(k)) for k in ('start','end','assessed_at'))
    cadence=bool(start and end and assessed and start.weekday()==0 and start.strftime('%H:%M:%S')=='00:00:00' and end.weekday()==4 and end.strftime('%H:%M:%S')=='23:59:59' and end-start==timedelta(days=4,hours=23,minutes=59,seconds=59) and end<=assessed<=end+timedelta(hours=24))
    if not cadence:f.append(Finding('WINDOW_CADENCE_INVALID','/window'))
    outcomes=[]
    for i,e in enumerate(entries):
        if not isinstance(e,dict):continue
        a,h,err=_assessment(e,i);f+=err
        if a is None:continue
        field=f'/entries/{i}';actual=a['classification']['outcome'];outcomes.append(actual)
        for code,key,want in (('ASSESSMENT_CONTENT_HASH_MISMATCH','assessment_content_hash',h),('ASSESSMENT_ID_MISMATCH','assessment_id',a.get('assessment_id')),('ASSESSMENT_SPEC_HASH_MISMATCH','assessment_spec_hash',a.get('governance',{}).get('spec_hash')),('ASSESSMENT_OUTCOME_MISMATCH','assessment_outcome',actual)):
            if e.get(key)!=want:f.append(Finding(code,f'{field}/{key}'))
        subject=a.get('subject_ref')
        if not isinstance(subject,str) or not subject.endswith('/'+str(e.get('domain'))):f.append(Finding('ASSESSMENT_DOMAIN_MISMATCH',field))
        t=a.get('timing',{});at,ct=_time(t.get('assessed_at')),_time(t.get('candidate_as_of'))
        if start and end and (at is None or ct is None or not(start<=at<=end) or not(start<=ct<=end)):f.append(Finding('ASSESSMENT_OUTSIDE_WINDOW',field))
        action=e.get('recommended_action');want='NONE' if actual=='NON_EVENT' else 'REVIEW'
        if action in {'REBUILD','PR'}:f.append(Finding('EXECUTION_ACTION_NOT_ADMITTED',field+'/recommended_action'))
        elif action!=want:f.append(Finding('ENTRY_ACTION_MISMATCH',field+'/recommended_action'))
    if len(outcomes)==len(entries):
        want=_expected(outcomes)
        if any(summary.get(k)!=want[k] for k in ('entry_count','non_event_count','material_count','hold_count','error_count')):f.append(Finding('SUMMARY_COUNT_MISMATCH','/summary'))
        if summary.get('emit_candidate') is not want['emit_candidate']:f.append(Finding('SUMMARY_EMIT_MISMATCH','/summary/emit_candidate'))
        if summary.get('outcome')!=want['outcome']:f.append(Finding('SUMMARY_OUTCOME_MISMATCH','/summary/outcome'))
        if summary.get('reason_codes')!=want['reason_codes']:f.append(Finding('SUMMARY_REASONS_MISMATCH','/summary/reason_codes'))
    h=_spec_hash(obj)
    if obj.get('spec_hash')!=h:f.append(Finding('IDENTITY_MISMATCH','/spec_hash'))
    if obj.get('pulse_id')!=f"natural-systems-pulse:{str(window.get('end',''))[:10]}:{h.split(':')[1][:24]}":f.append(Finding('IDENTITY_MISMATCH','/pulse_id'))
    lin,g=obj.get('lineage'),obj.get('governance')
    if isinstance(lin,dict) and obj.get('pulse_id') in {lin.get('supersedes'),lin.get('superseded_by')}:f.append(Finding('SELF_SUPERSESSION','/lineage'))
    denied=('source_activation_allowed','network_access_allowed','rebuild_execution_allowed','issue_or_pr_creation_allowed','authority_created','policy_evaluated','review_authenticated','promotion_authorized','publication_allowed','public_use_allowed')
    if not isinstance(g,dict) or g.get('fixture_only') is not True or any(g.get(k) is not False for k in denied) or g.get('release_state')!='HOLD':f.append(Finding('GOVERNANCE_BOUNDARY_VIOLATION','/governance'))
    return sorted(set(f))
def validate_pulse(path):
    obj,f,_=_read(path)
    if obj is None:return ValidationResult(tuple(sorted(set(f))))
    sf=_schema_findings(obj,SCHEMA_PATH,'SCHEMA_UNAVAILABLE')
    return ValidationResult(tuple(sf if sf else _semantic(obj)))
def _serialize(path,r):return json.dumps({'file':path.as_posix(),'findings':[{'code':x.code,'field':x.field} for x in r.findings],'outcome':'PASS' if r.ok else 'FAIL','scope':SCOPE},sort_keys=True,separators=(',',':'))
def run_fixture_profile():
    valid=sorted((FIXTURE_ROOT/'valid').glob('valid_*.json'));d=FIXTURE_ROOT/'invalid';invalid=sorted(p for p in d.glob('*.json') if p.name!='expected_findings_manifest.json')
    try:m=json.loads((d/'expected_findings_manifest.json').read_text())
    except (OSError,json.JSONDecodeError):return 1
    if not valid or not invalid or set(m)!={p.name for p in invalid}:return 1
    ok=True
    for p in valid:r=validate_pulse(p);print(_serialize(p,r));ok&=r.ok
    for p in invalid:
        r=validate_pulse(p);print(_serialize(p,r));a,w=sorted({x.code for x in r.findings}),sorted(m[p.name])
        if r.ok or a!=w:ok=False;print(json.dumps({'actual':a,'expected':w,'file':p.as_posix(),'outcome':'FIXTURE_POLARITY_ERROR'},sort_keys=True,separators=(',',':')))
    return 0 if ok else 1
def main(argv:Sequence[str]|None=None):
    p=argparse.ArgumentParser();p.add_argument('files',nargs='*',type=Path);p.add_argument('--fixtures',action='store_true');a=p.parse_args(argv)
    if a.fixtures:
        if a.files:p.error('--fixtures cannot be combined with explicit files')
        return run_fixture_profile()
    if not a.files:p.error('provide files or --fixtures')
    bad=False
    for path in sorted(a.files,key=lambda x:x.as_posix()):r=validate_pulse(path);print(_serialize(path,r));bad|=not r.ok
    return int(bad)
if __name__=='__main__':raise SystemExit(main())
