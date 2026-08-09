#!/usr/bin/env python3
"""Validate fixture-only VerificationConvergencePlan records."""
from __future__ import annotations
import argparse, hashlib, json, math, re
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence
from jsonschema import Draft202012Validator

REPO_ROOT=Path(__file__).resolve().parents[3]
SCHEMA_PATH=REPO_ROOT/'schemas/contracts/v1/governance/verification_convergence_plan.schema.json'
MAX_JSON_BYTES=512*1024; MAX_FINDINGS=100
PRIORITY={'P0':0,'P1':1,'P2':2,'P3':3}
UTC_SECOND=re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$')
@dataclass(frozen=True,order=True)
class Finding: code:str; path:str
@dataclass(frozen=True)
class Result:
    findings:tuple[Finding,...]; payload:Mapping[str,object]|None; outcome:str
    @property
    def ok(self): return not self.findings and self.payload is not None
class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
def _pairs(pairs):
    out={}
    for k,v in pairs:
        if k in out: raise DuplicateKeyError
        out[k]=v
    return out
def _nonfinite(_): raise NonFiniteNumberError
def _float(v):
    x=float(v)
    if not math.isfinite(x): raise NonFiniteNumberError
    return x
def _pointer(parts:Iterable[object])->str:
    p=[str(x).replace('~','~0').replace('/','~1') for x in parts]
    return '/'+'/'.join(p) if p else '/'
def _canonical(v): return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)
def canonical_plan_payload(p): return {k:p[k] for k in sorted(p) if k not in {'plan_id','plan_digest'}}
def compute_plan_digest(p): return 'sha256:'+hashlib.sha256(_canonical(canonical_plan_payload(p)).encode()).hexdigest()
def compute_plan_id(p): return 'kfm:verification-convergence:'+compute_plan_digest(p).split(':',1)[1][:16]
def _load(path):
    try:
        if path.is_symlink(): return None,[Finding('INPUT_SYMLINK_DENIED','/')]
        if not path.is_file(): return None,[Finding('INPUT_NOT_FILE','/')]
        if path.stat().st_size>MAX_JSON_BYTES: return None,[Finding('INPUT_TOO_LARGE','/')]
        v=json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=_pairs,parse_constant=_nonfinite,parse_float=_float)
    except (OSError,UnicodeError): return None,[Finding('INPUT_UNREADABLE','/')]
    except json.JSONDecodeError: return None,[Finding('JSON_INVALID','/')]
    except DuplicateKeyError: return None,[Finding('JSON_DUPLICATE_KEY','/')]
    except NonFiniteNumberError: return None,[Finding('JSON_NONFINITE_NUMBER','/')]
    except (RecursionError,ValueError): return None,[Finding('JSON_COMPLEXITY_LIMIT','/')]
    return (v,[]) if isinstance(v,dict) else (None,[Finding('JSON_ROOT_INVALID','/')])
def _schema_findings(plan):
    schema=json.loads(SCHEMA_PATH.read_text())
    errors=list(islice(Draft202012Validator(schema).iter_errors(plan),MAX_FINDINGS+1))
    out=[Finding('SCHEMA_INVALID',_pointer(e.absolute_path)) for e in sorted(errors[:MAX_FINDINGS],key=lambda e:(_pointer(e.absolute_path),str(e.validator)))]
    if len(errors)>MAX_FINDINGS: out.append(Finding('SCHEMA_FINDINGS_TRUNCATED','/'))
    return out
def _actionable(c): return c.get('work_state') in {'OPEN','IN_PROGRESS'} and c.get('blockers')==[] and c.get('constraint_state') in {'CLEAR','RESTRICTED'}
def _semantic(plan):
    findings=[]; candidates=plan['candidates']; selected=plan['selected_item_ids']; deferred=plan['deferred_item_ids']; satisfied=set(plan['satisfied_dependency_ids'])
    ids=[c['item_id'] for c in candidates]
    expected=[c['item_id'] for c in sorted(candidates,key=lambda c:(PRIORITY[c['priority']],c['item_id']))]
    if ids!=expected: findings.append(Finding('CANDIDATES_NOT_CANONICAL_ORDER','/candidates'))
    if len(ids)!=len(set(ids)): findings.append(Finding('CANDIDATE_ID_DUPLICATE','/candidates'))
    if selected!=[i for i in ids if i in set(selected)]: findings.append(Finding('SELECTED_NOT_CANDIDATE_ORDER','/selected_item_ids'))
    if deferred!=[i for i in ids if i not in set(selected)]: findings.append(Finding('DEFERRED_COMPLEMENT_MISMATCH','/deferred_item_ids'))
    if len(selected)>plan['capacity']: findings.append(Finding('SELECTION_CAPACITY_EXCEEDED','/selected_item_ids'))
    by={c['item_id']:c for c in candidates}; prior=set()
    for item in selected:
        c=by.get(item)
        if c is None: findings.append(Finding('SELECTED_ITEM_UNKNOWN','/selected_item_ids')); continue
        if not _actionable(c): findings.append(Finding('SELECTED_ITEM_NOT_ACTIONABLE',f'/candidates/{ids.index(item)}'))
        if any(d not in satisfied and d not in prior for d in c['dependencies']): findings.append(Finding('SELECTED_DEPENDENCY_UNMET',f'/candidates/{ids.index(item)}/dependencies'))
        if not c['selection_reason_codes']: findings.append(Finding('SELECTED_REASON_REQUIRED',f'/candidates/{ids.index(item)}/selection_reason_codes'))
        prior.add(item)
    worst=max((PRIORITY[by[i]['priority']] for i in selected if i in by),default=99)
    for idx,c in enumerate(candidates):
        if c['item_id'] in set(selected): continue
        if not c['defer_reason_codes']: findings.append(Finding('DEFER_REASON_REQUIRED',f'/candidates/{idx}/defer_reason_codes'))
        if _actionable(c) and PRIORITY[c['priority']]<worst and not c['defer_reason_codes']: findings.append(Finding('HIGHER_PRIORITY_DEFERRAL_UNJUSTIFIED',f'/candidates/{idx}/defer_reason_codes'))
    if not UTC_SECOND.fullmatch(plan['generated_at']): findings.append(Finding('GENERATED_AT_NOT_CANONICAL','/generated_at'))
    if plan['plan_digest']!=compute_plan_digest(plan): findings.append(Finding('PLAN_DIGEST_MISMATCH','/plan_digest'))
    if plan['plan_id']!=compute_plan_id(plan): findings.append(Finding('PLAN_ID_MISMATCH','/plan_id'))
    if findings: return findings,'ERROR'
    return [], 'READY' if selected else 'HOLD'
def validate(path:Path)->Result:
    plan,findings=_load(path)
    if plan is None: return Result(tuple(sorted(findings)),None,'ERROR')
    findings=_schema_findings(plan)
    if findings: return Result(tuple(sorted(findings)),None,'ERROR')
    findings,outcome=_semantic(plan)
    if findings: return Result(tuple(sorted(findings)),None,'ERROR')
    if plan['outcome']!=outcome: return Result((Finding('OUTCOME_MISMATCH','/outcome'),),None,'ERROR')
    return Result((),plan,outcome)
def report(r): return {'authority_created':False,'findings':[{'code':f.code,'path':f.path} for f in r.findings],'outcome':r.outcome,'publication_authorized':False,'repository_mutation_allowed':False,'scope':'verification-convergence-plan','status':'FAIL' if r.outcome=='ERROR' else 'PASS'}
def main(argv:Sequence[str]|None=None)->int:
    p=argparse.ArgumentParser(); p.add_argument('files',nargs='+',type=Path); a=p.parse_args(argv)
    reports=[report(validate(x)) for x in sorted(a.files,key=lambda x:x.as_posix())]
    print(_canonical(reports)); return 1 if any(x['status']=='FAIL' for x in reports) else 0
if __name__=='__main__': raise SystemExit(main())
