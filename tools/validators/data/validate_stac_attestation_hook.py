#!/usr/bin/env python3
"""Validate a fixture-only STAC rel=attestation projection without network access."""
from __future__ import annotations
import argparse, copy, json, sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = ROOT / "schemas/contracts/v1/data/stac_attestation_hook.schema.json"
CASES = ROOT / "fixtures/data/stac_attestation_hook/cases.json"
SCOPE = "stac-attestation-hook-fixture-only"
MEDIA_TYPE = "application/vnd.kfm.evidence-bundle+json"
REQUIRED_STATES = frozenset({"CANDIDATE","RELEASED","WITHDRAWN","CORRECTED","SUPERSEDED"})
ZERO_DIGEST = "sha256:" + "0" * 64
ERROR_CODES = frozenset({"FILE_NOT_FOUND","FILE_READ_ERROR","FILE_TOO_LARGE","JSON_INVALID","JSON_DUPLICATE_KEY","JSON_NONFINITE_NUMBER","ROOT_NOT_OBJECT","SCHEMA_UNAVAILABLE","FIXTURE_SUITE_INVALID"})

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str

@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]
    @property
    def ok(self) -> bool: return not self.findings
    @property
    def error(self) -> bool: return any(item.code in ERROR_CODES for item in self.findings)

class DuplicateKey(ValueError): pass
class NonFinite(ValueError): pass

def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in items:
        if key in out: raise DuplicateKey
        out[key] = value
    return out

def _nonfinite(_value: str) -> None: raise NonFinite

def _pointer(parts: Iterable[Any]) -> str:
    values=[str(p).replace("~","~0").replace("/","~1") for p in parts]
    return "/" + "/".join(values) if values else "/"

def _load(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if not path.is_file(): return None, [Finding("FILE_NOT_FOUND","/")]
        if path.stat().st_size > 2_000_000: return None, [Finding("FILE_TOO_LARGE","/")]
        value=json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs, parse_constant=_nonfinite)
    except DuplicateKey: return None, [Finding("JSON_DUPLICATE_KEY","/")]
    except NonFinite: return None, [Finding("JSON_NONFINITE_NUMBER","/")]
    except json.JSONDecodeError: return None, [Finding("JSON_INVALID","/")]
    except (OSError, UnicodeError): return None, [Finding("FILE_READ_ERROR","/")]
    if not isinstance(value, dict): return None, [Finding("ROOT_NOT_OBJECT","/")]
    return value, []

def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema=json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors=Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value)
        return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors]
    except Exception:
        return [Finding("SCHEMA_UNAVAILABLE","/")]

def semantic_subject(value: Mapping[str, Any]) -> dict[str, Any]:
    return {key: copy.deepcopy(item) for key,item in value.items() if key not in {"spec_hash","projection_id"}}

def compute_record_spec_hash(value: Mapping[str, Any]) -> str:
    return compute_spec_hash(semantic_subject(value))

def compute_projection_id(value: Mapping[str, Any]) -> str:
    return "stac-attestation-hook:" + compute_record_spec_hash(value).split(":",1)[1][:24]

def _semantic(value: Mapping[str, Any]) -> list[Finding]:
    out: list[Finding] = []
    links=value.get("links", [])
    if not isinstance(links, list): return out
    tuples=[(item.get("rel"),item.get("href")) for item in links if isinstance(item, Mapping)]
    if tuples != sorted(tuples): out.append(Finding("LINKS_NOT_CANONICAL","/links"))
    if len(tuples) != len(set(tuples)): out.append(Finding("LINK_DUPLICATE","/links"))
    hooks=[item for item in links if isinstance(item, Mapping) and item.get("rel") == "attestation"]
    if value.get("release_state") in REQUIRED_STATES and len(hooks) == 0:
        out.append(Finding("ATTESTATION_LINK_REQUIRED","/links"))
    if len(hooks) > 1:
        out.append(Finding("ATTESTATION_LINK_COUNT_INVALID","/links"))
    if len(hooks) == 1:
        hook=hooks[0]
        if hook.get("href") != value.get("evidence_bundle_ref"): out.append(Finding("ATTESTATION_HREF_MISMATCH","/links"))
        if hook.get("certifies_spec_hash") != value.get("item_spec_hash"): out.append(Finding("CERTIFIED_SPEC_HASH_MISMATCH","/links"))
        if hook.get("type") != MEDIA_TYPE: out.append(Finding("ATTESTATION_MEDIA_TYPE_INVALID","/links"))
        if hook.get("bundle_digest") == ZERO_DIGEST: out.append(Finding("BUNDLE_DIGEST_PLACEHOLDER_DENIED","/links"))
        if "/latest" in str(hook.get("href","")).lower(): out.append(Finding("FLOATING_LATEST_REFERENCE","/links"))
    if value.get("spec_hash") != compute_record_spec_hash(value): out.append(Finding("SPEC_HASH_MISMATCH","/spec_hash"))
    if value.get("projection_id") != compute_projection_id(value): out.append(Finding("PROJECTION_ID_MISMATCH","/projection_id"))
    return out

def validate_payload(value: Mapping[str, Any]) -> Result:
    findings=_schema_findings(value)
    if not findings: findings.extend(_semantic(value))
    return Result(tuple(sorted(set(findings))))

def validate_record(path: Path) -> Result:
    value, findings=_load(path)
    if value is None: return Result(tuple(findings))
    return validate_payload(value)

def finalize(value: dict[str, Any]) -> dict[str, Any]:
    value=copy.deepcopy(value)
    value["spec_hash"]=compute_record_spec_hash(value)
    value["projection_id"]=compute_projection_id(value)
    return value

def mutate(base: Mapping[str, Any], name: str) -> dict[str, Any]:
    value=copy.deepcopy(dict(base))
    if name == "NONE": return finalize(value)
    if name == "UNRELEASED_NO_HOOK":
        value["release_state"]="UNRELEASED"; value["links"]=[item for item in value["links"] if item["rel"]!="attestation"]; return finalize(value)
    if name == "MISSING_HOOK":
        value["links"]=[item for item in value["links"] if item["rel"]!="attestation"]; return finalize(value)
    if name == "PROV_ONLY":
        value["links"]=[item for item in value["links"] if item["rel"]!="attestation"]
        value["links"].append({"rel":"prov","href":value["evidence_bundle_ref"],"type":MEDIA_TYPE,"certifies_spec_hash":value["item_spec_hash"],"bundle_digest":"sha256:"+"2b"*32})
        value["links"].sort(key=lambda item:(item["rel"],item["href"])); return finalize(value)
    hook=next(item for item in value["links"] if item["rel"]=="attestation")
    if name == "HREF_MISMATCH": hook["href"]="kfm://bundle/other"; return finalize(value)
    if name == "CERTIFIED_HASH_MISMATCH": hook["certifies_spec_hash"]="sha256:"+"3c"*32; return finalize(value)
    if name == "MEDIA_TYPE": hook["type"]="application/json"; return finalize(value)
    if name == "PLACEHOLDER_DIGEST": hook["bundle_digest"]=ZERO_DIGEST; return finalize(value)
    if name == "DUPLICATE_HOOK": value["links"].insert(1,copy.deepcopy(hook)); return finalize(value)
    if name == "UNORDERED_LINKS": value["links"]=list(reversed(value["links"])); return finalize(value)
    if name == "FLOATING_LATEST": value["evidence_bundle_ref"]="kfm://bundle/latest"; hook["href"]="kfm://bundle/latest"; return finalize(value)
    if name == "SPEC_HASH_MISMATCH": value=finalize(value); value["spec_hash"]="sha256:"+"4d"*32; return value
    if name == "AUTHORITY_OVERCLAIM": value["authority"]["publication_authorized"]=True; return finalize(value)
    if name == "MISSING_BUNDLE_REF": value.pop("evidence_bundle_ref",None); return finalize(value)
    raise ValueError("unknown fixture mutation")

def serialize(label: str, result: Result) -> str:
    return json.dumps({"file":label,"findings":[{"code":f.code,"field":f.field} for f in result.findings],"outcome":"PASS" if result.ok else ("ERROR" if result.error else "FAIL"),"scope":SCOPE,"authority_created":False},sort_keys=True,separators=(",",":"))

def fixture_suite() -> tuple[bool, list[str]]:
    suite, findings=_load(CASES)
    if suite is None: return False,[serialize("fixture-suite",Result(tuple(findings or [Finding("FIXTURE_SUITE_INVALID","/")]))) ]
    base=suite.get("base"); cases=suite.get("cases")
    if not isinstance(base, Mapping) or not isinstance(cases,list): return False,[serialize("fixture-suite",Result((Finding("FIXTURE_SUITE_INVALID","/"),)))]
    lines=[]; ok=True
    for case in cases:
        if not isinstance(case,Mapping): return False,[serialize("fixture-suite",Result((Finding("FIXTURE_SUITE_INVALID","/cases"),)))]
        candidate=mutate(base,str(case.get("mutation")))
        result=validate_payload(candidate)
        outcome="PASS" if result.ok else ("ERROR" if result.error else "FAIL")
        codes=sorted({f.code for f in result.findings})
        match=outcome==case.get("expected_outcome") and codes==case.get("expected_codes")
        ok &= match
        lines.append(json.dumps({"case_id":case.get("case_id"),"expected_outcome":case.get("expected_outcome"),"outcome":outcome,"findings":codes,"suite_match":match,"authority_created":False},sort_keys=True,separators=(",",":")))
    return ok,lines

def main(argv: Sequence[str] | None=None) -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("path",nargs="?",type=Path); parser.add_argument("--fixtures",action="store_true"); args=parser.parse_args(argv)
    if args.fixtures:
        ok,lines=fixture_suite()
        for line in lines: print(line)
        return 0 if ok else 1
    if args.path is None: parser.error("path is required unless --fixtures is used")
    result=validate_record(args.path); print(serialize(args.path.name,result)); return 0 if result.ok else 1

if __name__=="__main__": raise SystemExit(main())
