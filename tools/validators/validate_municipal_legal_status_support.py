#!/usr/bin/env python3
"""Validate the synthetic municipal legal-status support envelope.

A pass proves only bounded schema, source-role, temporal, and finite-outcome
invariants for synthetic records. It grants no real legal status, source
admission, EvidenceBundle closure, policy/review approval, release, deployment,
publication, or public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas/contracts/v1/domains/settlements-infrastructure/municipal-legal-status-support.schema.json"
PROFILE = ROOT / "fixtures/contracts/v1/domains/settlements-infrastructure/municipal_legal_status_support/fixture_profile.json"
MAX_BYTES = 1_048_576

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str

@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]
    derived_outcome: str | None = None
    derived_reason_codes: tuple[str, ...] = ()
    @property
    def ok(self) -> bool:
        return not self.findings
    @property
    def error(self) -> bool:
        return any(f.code.startswith(("FILE_", "JSON_", "INPUT_", "SCHEMA_UNAVAILABLE")) for f in self.findings)

def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out={}
    for key,value in pairs:
        if key in out: raise DuplicateKeyError
        out[key]=value
    return out

def _constant(_: str) -> None: raise NonFiniteNumberError

def _float(value: str) -> float:
    parsed=float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed

def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink(): return None,[Finding("INPUT_SYMLINK_DENIED","/")]
        if not path.is_file(): return None,[Finding("FILE_NOT_FOUND","/")]
        if path.stat().st_size > MAX_BYTES: return None,[Finding("FILE_TOO_LARGE","/")]
        value=json.loads(path.read_text(encoding="utf-8"),object_pairs_hook=_object,parse_constant=_constant,parse_float=_float)
    except UnicodeError: return None,[Finding("JSON_NOT_UTF8","/")]
    except DuplicateKeyError: return None,[Finding("JSON_DUPLICATE_KEY","/")]
    except NonFiniteNumberError: return None,[Finding("JSON_NONFINITE_NUMBER","/")]
    except json.JSONDecodeError: return None,[Finding("JSON_INVALID","/")]
    except OSError: return None,[Finding("FILE_READ_ERROR","/")]
    except (RecursionError,ValueError): return None,[Finding("JSON_COMPLEXITY_LIMIT","/")]
    if not isinstance(value,dict): return None,[Finding("JSON_ROOT_INVALID","/")]
    return value,[]

def _canonical_hash(candidate: Mapping[str, Any]) -> str:
    value=dict(candidate); value.pop("spec_hash",None)
    payload=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode("utf-8")
    return "sha256:"+hashlib.sha256(payload).hexdigest()

def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema=json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator=Draft202012Validator(schema,format_checker=FormatChecker())
        if any(validator.iter_errors(candidate)): return [Finding("SCHEMA_INVALID","/")]
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError,RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE","/")]
    return []

def _time(value: Any) -> datetime | None:
    if not isinstance(value,str): return None
    try: parsed=datetime.fromisoformat(value.replace("Z","+00:00"))
    except ValueError: return None
    return parsed if parsed.tzinfo else None

def _derived(candidate: Mapping[str, Any]) -> tuple[str,tuple[str,...]]:
    if candidate.get("input_state")=="ERROR":
        return "ERROR",("SYNTHETIC_INPUT_ERROR",)
    subject=candidate.get("subject")
    family=subject.get("identity_family") if isinstance(subject,dict) else None
    if family=="CensusPlace":
        return "DENY",("CENSUS_PLACE_NOT_MUNICIPALITY",)
    legal=candidate.get("legal_status_evidence")
    if not isinstance(legal,dict):
        return "ERROR",("LEGAL_EVIDENCE_PARTIAL",)
    source_ref,evidence_ref=legal.get("source_ref"),legal.get("evidence_ref")
    if (source_ref is None)!=(evidence_ref is None):
        return "ERROR",("LEGAL_EVIDENCE_PARTIAL",)
    if source_ref is None and evidence_ref is None:
        return "ABSTAIN",("LEGAL_STATUS_EVIDENCE_INSUFFICIENT",)
    if legal.get("source_date") is None:
        return "ABSTAIN",("LEGAL_STATUS_EVIDENCE_UNDATED",)
    claim=candidate.get("claim")
    as_of=_time(claim.get("as_of")) if isinstance(claim,dict) else None
    start,end=_time(legal.get("effective_from")),_time(legal.get("effective_to"))
    if as_of is not None and ((start is not None and as_of<start) or (end is not None and as_of>end)):
        return "ABSTAIN",("LEGAL_STATUS_EVIDENCE_OUT_OF_SCOPE",)
    return "ANSWER",("LEGAL_STATUS_SUPPORT_PRESENT",)

def _semantic(candidate: Mapping[str, Any]) -> tuple[list[Finding],str,tuple[str,...]]:
    findings=[]
    supplied=candidate.get("spec_hash")
    if isinstance(supplied,str) and supplied!=_canonical_hash(candidate):
        findings.append(Finding("SPEC_HASH_MISMATCH","/spec_hash"))
    legal=candidate.get("legal_status_evidence")
    if isinstance(legal,dict):
        if legal.get("source_role")!="administrative":
            findings.append(Finding("LEGAL_SOURCE_ROLE_INVALID","/legal_status_evidence/source_role"))
        start,end=_time(legal.get("effective_from")),_time(legal.get("effective_to"))
        if start is not None and end is not None and end<start:
            findings.append(Finding("LEGAL_VALID_TIME_ORDER","/legal_status_evidence"))
    census=candidate.get("census_geography_context")
    if isinstance(census,dict) and census.get("source_role")!="aggregate":
        findings.append(Finding("CENSUS_SOURCE_ROLE_INVALID","/census_geography_context/source_role"))
    outcome,reasons=_derived(candidate)
    if not findings:
        if candidate.get("outcome")!=outcome:
            findings.append(Finding("OUTCOME_MISMATCH","/outcome"))
        supplied_reasons=candidate.get("reason_codes")
        if not isinstance(supplied_reasons,list) or tuple(sorted(supplied_reasons))!=tuple(sorted(reasons)):
            findings.append(Finding("REASON_CODES_MISMATCH","/reason_codes"))
    return findings,outcome,reasons

def validate(candidate: Mapping[str, Any]) -> Result:
    semantic,outcome,reasons=_semantic(candidate)
    return Result(tuple(sorted(set(_schema_findings(candidate)+semantic))),outcome,reasons)

def _deep_merge(target: dict[str, Any],patch: Mapping[str, Any]) -> dict[str, Any]:
    for key,value in patch.items():
        if isinstance(value,dict) and isinstance(target.get(key),dict): _deep_merge(target[key],value)
        else: target[key]=copy.deepcopy(value)
    return target

def materialize_fixture(base: Mapping[str, Any],patch: Mapping[str, Any]) -> dict[str, Any]:
    candidate=_deep_merge(copy.deepcopy(dict(base)),patch)
    candidate["spec_hash"]=_canonical_hash(candidate)
    return candidate

def _load_profile() -> dict[str, Any]:
    value,findings=_read(PROFILE)
    if value is None: raise RuntimeError(",".join(f.code for f in findings))
    return value

def validate_fixtures() -> int:
    profile=_load_profile(); base=profile["base"]; rows=[]; ok=True
    for name,case in sorted(profile["valid"].items()):
        result=validate(materialize_fixture(base,case["patch"]))
        passed=result.ok and result.derived_outcome==case["expected_outcome"] and list(result.derived_reason_codes)==case["expected_reasons"]
        rows.append({"fixture":name,"expected_outcome":case["expected_outcome"],"actual_outcome":result.derived_outcome,"expected_reasons":case["expected_reasons"],"actual_reasons":list(result.derived_reason_codes),"validation":"PASS" if passed else "FAIL","findings":[f.code for f in result.findings]})
        ok=ok and passed
    for name,case in sorted(profile["invalid"].items()):
        result=validate(materialize_fixture(base,case["patch"]))
        actual=sorted({f.code for f in result.findings}); expected=sorted(case["expected_findings"]); passed=actual==expected
        rows.append({"fixture":name,"expected_findings":expected,"actual_findings":actual,"validation":"PASS" if passed else "FAIL"})
        ok=ok and passed
    print(json.dumps({"profile":profile["profile_id"],"ok":ok,"cases":rows},sort_keys=True,separators=(",",":")))
    return 0 if ok else 1

def _emit(path: Path,result: Result) -> None:
    print(json.dumps({"path":path.as_posix(),"outcome":"PASS" if result.ok else ("ERROR" if result.error else "FAIL"),"derived_outcome":result.derived_outcome,"reason_codes":list(result.derived_reason_codes),"findings":[{"code":f.code,"field":f.field} for f in result.findings]},sort_keys=True,separators=(",",":")))

def main(argv: list[str] | None=None) -> int:
    parser=argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("paths",nargs="*",type=Path); parser.add_argument("--fixtures",action="store_true")
    args=parser.parse_args(argv)
    if args.fixtures:
        if args.paths: parser.error("--fixtures does not accept file paths")
        return validate_fixtures()
    if not args.paths: parser.error("supply at least one JSON file or --fixtures")
    exit_code=0
    for path in args.paths:
        candidate,read_findings=_read(path)
        result=Result(tuple(read_findings)) if candidate is None else validate(candidate)
        _emit(path,result)
        if result.error: exit_code=max(exit_code,3)
        elif not result.ok: exit_code=max(exit_code,2)
    return exit_code

if __name__=="__main__":
    raise SystemExit(main())
