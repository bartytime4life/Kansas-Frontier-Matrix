"""Validate fixture-only OperationalTrustRollup declarations.

A result is a read-only projection. It does not resolve references, execute policy,
authenticate review, verify signatures, promote, release, deploy, or publish.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT=Path(__file__).resolve().parents[3]
SCHEMA_PATH=REPO_ROOT/'schemas/contracts/v1/release/operational_trust_rollup.schema.json'
FIXTURE_PATH=REPO_ROOT/'fixtures/contracts/v1/release/operational_trust_rollup/cases.json'
HASHING_SRC=REPO_ROOT/'packages/hashing/src'
if HASHING_SRC.is_dir():
    sys.path.insert(0,str(HASHING_SRC))
try:
    from hashing import compute_spec_hash as _shared_compute_spec_hash
except Exception:  # pragma: no cover
    _shared_compute_spec_hash=None


@dataclass(frozen=True,order=True)
class Finding:
    code:str
    field:str


@dataclass(frozen=True)
class RollupResult:
    outcome:str
    findings:tuple[Finding,...]
    summary:Mapping[str,object]

    @property
    def codes(self)->list[str]:
        return sorted({item.code for item in self.findings})


def _fallback_hash(value:object)->str:
    payload=json.dumps(value,ensure_ascii=False,allow_nan=False,sort_keys=True,separators=(",",":")).encode('utf-8')
    return 'sha256:'+hashlib.sha256(payload).hexdigest()


def compute_rollup_hash(candidate:Mapping[str,object])->str:
    subject=dict(candidate)
    subject.pop('rollup_spec_hash',None)
    if _shared_compute_spec_hash is not None:
        return _shared_compute_spec_hash(subject)
    return _fallback_hash(subject)


def _schema()->dict[str,object]:
    return json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))


def _schema_findings(candidate:object)->list[Finding]:
    validator=Draft202012Validator(_schema(),format_checker=FormatChecker())
    errors=sorted(validator.iter_errors(candidate),key=lambda error:(list(error.absolute_path),str(error.validator)))
    return [Finding('SCHEMA_INVALID','/'+ '/'.join(str(part) for part in error.absolute_path)) for error in errors[:100]]


COMPONENTS=('evidence','policy','signatures','validation','review','catalog','correction','rollback')
REQUIRED_REF_STATES={
    'evidence':{'RESOLVED','DENIED'},
    'policy':{'ALLOW','HOLD','DENY'},
    'signatures':{'VERIFIED','FAILED'},
    'validation':{'PASS','FAIL'},
    'review':{'APPROVED','CHANGES_REQUESTED','REJECTED'},
    'catalog':{'CLOSED'},
    'correction':{'READY'},
    'rollback':{'READY'},
}
STATUS_CODES={
    ('evidence','UNRESOLVED'):'EVIDENCE_UNRESOLVED',
    ('evidence','DENIED'):'EVIDENCE_DENIED',
    ('evidence','ERROR'):'EVIDENCE_ERROR',
    ('policy','HOLD'):'POLICY_HOLD',
    ('policy','DENY'):'POLICY_DENIED',
    ('policy','ERROR'):'POLICY_ERROR',
    ('signatures','PENDING'):'SIGNATURE_PENDING',
    ('signatures','FAILED'):'SIGNATURE_FAILED',
    ('signatures','ERROR'):'SIGNATURE_ERROR',
    ('validation','FAIL'):'VALIDATION_FAILED',
    ('validation','ERROR'):'VALIDATION_ERROR',
    ('review','PENDING'):'REVIEW_PENDING',
    ('review','CHANGES_REQUESTED'):'REVIEW_CHANGES_REQUESTED',
    ('review','REJECTED'):'REVIEW_REJECTED',
    ('review','ERROR'):'REVIEW_ERROR',
    ('catalog','OPEN'):'CATALOG_OPEN',
    ('catalog','ERROR'):'CATALOG_ERROR',
    ('correction','MISSING'):'CORRECTION_PATH_MISSING',
    ('correction','ERROR'):'CORRECTION_ERROR',
    ('rollback','MISSING'):'ROLLBACK_MISSING',
    ('rollback','ERROR'):'ROLLBACK_ERROR',
}


def _semantic_findings(candidate:Mapping[str,object])->list[Finding]:
    findings=[]
    if compute_rollup_hash(candidate)!=candidate.get('rollup_spec_hash'):
        findings.append(Finding('ROLLUP_SPEC_HASH_MISMATCH','/rollup_spec_hash'))
    scope=candidate.get('scope')
    if isinstance(scope,dict):
        refs=scope.get('artifact_refs')
        if isinstance(refs,list) and refs!=sorted(refs):
            findings.append(Finding('ARTIFACT_REFS_NOT_CANONICAL','/scope/artifact_refs'))
    for component in COMPONENTS:
        value=candidate.get(component)
        if not isinstance(value,dict):
            continue
        status=value.get('status')
        refs=value.get('refs')
        if status in REQUIRED_REF_STATES[component] and (not isinstance(refs,list) or not refs):
            findings.append(Finding('COMPONENT_REFERENCE_MISSING',f'/{component}/refs'))
        if isinstance(refs,list) and refs!=sorted(refs):
            findings.append(Finding('COMPONENT_REFS_NOT_CANONICAL',f'/{component}/refs'))
        code=STATUS_CODES.get((component,status))
        if code:
            findings.append(Finding(code,f'/{component}/status'))
    authority=candidate.get('authority_claims')
    if isinstance(authority,dict) and any(value is not False for value in authority.values()):
        findings.append(Finding('AUTHORITY_OVERCLAIM_DENIED','/authority_claims'))
    return findings


def validate_candidate(candidate:object)->RollupResult:
    schema_findings=_schema_findings(candidate)
    if schema_findings:
        return RollupResult('ERROR',tuple(sorted(schema_findings)),{})
    assert isinstance(candidate,dict)
    findings=_semantic_findings(candidate)
    codes={item.code for item in findings}
    error_codes={code for code in codes if code.endswith('_ERROR')}
    deny_codes={
        'ROLLUP_SPEC_HASH_MISMATCH','ARTIFACT_REFS_NOT_CANONICAL','COMPONENT_REFERENCE_MISSING',
        'COMPONENT_REFS_NOT_CANONICAL','EVIDENCE_DENIED','POLICY_DENIED','SIGNATURE_FAILED',
        'VALIDATION_FAILED','REVIEW_REJECTED','CORRECTION_PATH_MISSING','ROLLBACK_MISSING',
        'AUTHORITY_OVERCLAIM_DENIED'
    }
    hold_codes={'EVIDENCE_UNRESOLVED','POLICY_HOLD','SIGNATURE_PENDING','REVIEW_PENDING','REVIEW_CHANGES_REQUESTED','CATALOG_OPEN'}
    if codes & error_codes:
        outcome='ERROR'
    elif codes & deny_codes:
        outcome='DENY'
    elif codes & hold_codes:
        outcome='HOLD'
    else:
        outcome='READY'
    statuses=Counter(str(candidate[name]['status']) for name in COMPONENTS if isinstance(candidate.get(name),dict))
    summary={'component_count':len(COMPONENTS),'status_counts':dict(sorted(statuses.items()))}
    return RollupResult(outcome,tuple(sorted(findings)),summary)


def _merge_patch(base:object,patch:object)->object:
    """Apply a bounded RFC 7396-style merge patch to synthetic fixtures."""
    if not isinstance(patch,dict):
        return patch
    target=dict(base) if isinstance(base,dict) else {}
    for key,value in patch.items():
        if value is None:
            target.pop(key,None)
        else:
            target[key]=_merge_patch(target.get(key),value)
    return target


def materialize_fixture_case(manifest:Mapping[str,object],entry:Mapping[str,object])->object:
    return _merge_patch(manifest['base_candidate'],entry.get('patch',{}))


def validate_fixture_manifest(path:Path=FIXTURE_PATH)->list[dict[str,object]]:
    manifest=json.loads(path.read_text(encoding='utf-8'))
    results=[]
    for entry in manifest['cases']:
        candidate=materialize_fixture_case(manifest,entry)
        result=validate_candidate(candidate)
        observed={'outcome':result.outcome,'codes':result.codes}
        results.append({'name':entry['name'],'ok':observed==entry['expected'],'expected':entry['expected'],'observed':observed,'summary':result.summary})
    return results


def main(argv:Sequence[str]|None=None)->int:
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--fixtures',action='store_true')
    group.add_argument('--input',type=Path)
    args=parser.parse_args(argv)
    if args.fixtures:
        results=validate_fixture_manifest()
        print(json.dumps(results,indent=2,sort_keys=True))
        return 0 if all(item['ok'] for item in results) else 1
    candidate=json.loads(args.input.read_text(encoding='utf-8'))
    result=validate_candidate(candidate)
    print(json.dumps({'outcome':result.outcome,'codes':result.codes,'summary':result.summary},indent=2,sort_keys=True))
    return 0 if result.outcome=='READY' else 1


if __name__=='__main__':
    raise SystemExit(main())
