"""Validate fixture-only station spatial assignment assessment candidates.

The bounded profile uses synthetic EPSG:4326 points and simple polygon rings.
It performs no network access, source activation, canonical geography write,
location publication, promotion, release, or public use.
"""
from __future__ import annotations
import argparse, copy, hashlib, json, math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT=Path(__file__).resolve().parents[3]
SCHEMA_PATH=REPO_ROOT/"schemas/contracts/v1/common/station_spatial_assignment_assessment.schema.json"
FIXTURE_PATH=REPO_ROOT/"fixtures/contracts/v1/common/station_spatial_assignment_assessment/cases.json"
MAX_FILE_BYTES=1_048_576
IDENTITY_PREFIX="kfm:station-spatial-assignment:"
LEVEL_ORDER={"COUNTY":0,"HUC12":1,"STATE":2}
ID_FIELDS={"COUNTY":"county_geoid","HUC12":"huc12","STATE":"state_fips"}

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
@dataclass(frozen=True, order=True)
class Finding: code:str; field:str
@dataclass(frozen=True)
class ValidationResult:
    outcome:str; findings:tuple[Finding,...]
    @property
    def codes(self): return sorted({f.code for f in self.findings})

def _pairs(items):
    out={}
    for k,v in items:
        if k in out: raise DuplicateKeyError
        out[k]=v
    return out
def _nonfinite(_): raise NonFiniteNumberError
def _finite_float(v):
    x=float(v)
    if not math.isfinite(x): raise NonFiniteNumberError
    return x

def load_json_object(path:Path):
    try:
        if path.is_symlink(): return None,[Finding("INPUT_SYMLINK_DENIED","/")]
        if not path.is_file(): return None,[Finding("FILE_NOT_FOUND","/")]
        if path.stat().st_size>MAX_FILE_BYTES: return None,[Finding("FILE_TOO_LARGE","/")]
        value=json.loads(path.read_text(encoding="utf-8"),object_pairs_hook=_pairs,parse_constant=_nonfinite,parse_float=_finite_float)
    except DuplicateKeyError: return None,[Finding("JSON_DUPLICATE_KEY","/")]
    except NonFiniteNumberError: return None,[Finding("JSON_NONFINITE_NUMBER","/")]
    except (OSError,UnicodeError,json.JSONDecodeError,RecursionError,ValueError): return None,[Finding("JSON_INVALID","/")]
    if not isinstance(value,dict): return None,[Finding("ROOT_NOT_OBJECT","/")]
    return value,[]

def canonical_hash(v): return "sha256:"+hashlib.sha256(json.dumps(v,ensure_ascii=False,allow_nan=False,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def compute_identity_hash(c):
    s=copy.deepcopy(dict(c)); s.pop("assessment_id",None); s.pop("profile_spec_hash",None); return canonical_hash(s)
def compute_assessment_id(c): return IDENTITY_PREFIX+compute_identity_hash(c).split(":",1)[1][:24]
def compute_profile_hash(c):
    s=copy.deepcopy(dict(c)); s.pop("profile_spec_hash",None); return canonical_hash(s)
def bind_candidate(c):
    c=copy.deepcopy(c); c["assessment_id"]=compute_assessment_id(c); c["profile_spec_hash"]=compute_profile_hash(c); return c

def _schema_findings(c):
    schema=json.loads(SCHEMA_PATH.read_text(encoding="utf-8")); v=Draft202012Validator(schema,format_checker=FormatChecker())
    errors=sorted(v.iter_errors(c),key=lambda e:(tuple(str(p) for p in e.absolute_path),str(e.validator)))
    return [Finding("SCHEMA_INVALID","/"+"/".join(str(p) for p in e.absolute_path)) for e in errors[:100]]
def _is_utc(v):
    if not isinstance(v,str) or not v.endswith("Z"): return False
    try: datetime.fromisoformat(v[:-1]+"+00:00")
    except ValueError: return False
    return True

def _on_segment(p,a,b,eps=1e-12):
    cross=(p[0]-a[0])*(b[1]-a[1])-(p[1]-a[1])*(b[0]-a[0])
    if abs(cross)>eps: return False
    return min(a[0],b[0])-eps<=p[0]<=max(a[0],b[0])+eps and min(a[1],b[1])-eps<=p[1]<=max(a[1],b[1])+eps

def point_relation(point,ring):
    if len(ring)<4 or ring[0]!=ring[-1]: return "INVALID"
    inside=False
    for i in range(len(ring)-1):
        a,b=ring[i],ring[i+1]
        if _on_segment(point,a,b): return "BOUNDARY"
        if (a[1]>point[1]) != (b[1]>point[1]):
            x=a[0]+(point[1]-a[1])*(b[0]-a[0])/(b[1]-a[1])
            if x>point[0]: inside=not inside
    return "CONTAINS" if inside else "OUTSIDE"

def _expected_id_length(level): return {"STATE":2,"COUNTY":5,"HUC12":12}[level]
def _semantic_findings(c:Mapping[str,object]):
    findings=set()
    if c.get("assessment_id")!=compute_assessment_id(c): findings.add(Finding("ASSESSMENT_ID_MISMATCH","/assessment_id"))
    if c.get("profile_spec_hash")!=compute_profile_hash(c): findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH","/profile_spec_hash"))
    if not _is_utc(c.get("observed_at")): findings.add(Finding("UTC_TIMESTAMP_REQUIRED","/observed_at"))
    snapshots=c["boundary_snapshots"]; assignments=c["assignments"]; context=c["declared_context"]
    assert isinstance(snapshots,list) and isinstance(assignments,list) and isinstance(context,Mapping)
    skeys=[(LEVEL_ORDER[s["level"]],s["level"]) for s in snapshots]
    if skeys!=sorted(skeys): findings.add(Finding("SNAPSHOTS_NOT_CANONICAL","/boundary_snapshots"))
    levels=[s["level"] for s in snapshots]
    if sorted(levels)!=["COUNTY","HUC12","STATE"]: findings.add(Finding("SNAPSHOT_LEVEL_SET_INVALID","/boundary_snapshots"))
    akeys=[(LEVEL_ORDER[a["level"]],a["geography_id"]) for a in assignments]
    if akeys!=sorted(akeys): findings.add(Finding("ASSIGNMENTS_NOT_CANONICAL","/assignments"))
    point_obj=c["point"]; assert isinstance(point_obj,Mapping); point=[point_obj["longitude"],point_obj["latitude"]]
    relations={level:[] for level in LEVEL_ORDER}
    for idx,a in enumerate(assignments):
        level=a["level"]; gid=a["geography_id"]
        if len(gid)!=_expected_id_length(level): findings.add(Finding("GEOGRAPHY_ID_LEVEL_MISMATCH",f"/assignments/{idx}/geography_id"))
        relation=point_relation(point,a["polygon_ring"])
        if relation=="INVALID": findings.add(Finding("POLYGON_RING_INVALID",f"/assignments/{idx}/polygon_ring")); continue
        if relation!=a["declared_relation"]: findings.add(Finding("DECLARED_RELATION_MISMATCH",f"/assignments/{idx}/declared_relation"))
        relations[level].append((gid,relation))
    for level,items in relations.items():
        contains=[gid for gid,rel in items if rel=="CONTAINS"]
        boundaries=[gid for gid,rel in items if rel=="BOUNDARY"]
        declared=context[ID_FIELDS[level]]
        if len(contains)>1: findings.add(Finding("OVERLAPPING_ASSIGNMENTS",f"/assignments/{level}"))
        elif boundaries:
            if declared is not None: findings.add(Finding("BOUNDARY_DECLARATION_MUST_BE_NULL",f"/declared_context/{ID_FIELDS[level]}"))
        elif len(contains)==1:
            if declared!=contains[0]: findings.add(Finding("DECLARED_CONTEXT_MISMATCH",f"/declared_context/{ID_FIELDS[level]}"))
        elif declared is not None: findings.add(Finding("UNSUPPORTED_DECLARED_CONTEXT",f"/declared_context/{ID_FIELDS[level]}"))
    state=context["state_fips"]; county=context["county_geoid"]
    if state is not None and county is not None and not county.startswith(state): findings.add(Finding("STATE_COUNTY_PREFIX_MISMATCH","/declared_context/county_geoid"))
    return sorted(findings)

def validate_candidate(c):
    sf=_schema_findings(c)
    if sf: return ValidationResult("ERROR",tuple(sf))
    assert isinstance(c,dict)
    sem=_semantic_findings(c)
    if sem: return ValidationResult("DENY",tuple(sem))
    snapshots=c["boundary_snapshots"]; assignments=c["assignments"]
    if any(s["resolution_state"]=="UNRESOLVED" for s in snapshots): return ValidationResult("ABSTAIN",(Finding("BOUNDARY_SNAPSHOT_UNRESOLVED","/boundary_snapshots"),))
    by_level={level:[] for level in LEVEL_ORDER}
    for a in assignments: by_level[a["level"]].append(a["declared_relation"])
    if any("BOUNDARY" in rels for rels in by_level.values()): return ValidationResult("ABSTAIN",(Finding("POINT_ON_BOUNDARY","/assignments"),))
    if any("CONTAINS" not in rels for rels in by_level.values()): return ValidationResult("ABSTAIN",(Finding("ASSIGNMENT_NOT_RESOLVED","/assignments"),))
    return ValidationResult("PASS",())


def _resolve_parent(value: object, path: Sequence[object]) -> tuple[object, object]:
    if not path:
        raise ValueError("operation path must not be empty")
    current = value
    for part in path[:-1]:
        if isinstance(current, list) and isinstance(part, int):
            current = current[part]
        elif isinstance(current, dict) and isinstance(part, str):
            current = current[part]
        else:
            raise ValueError("operation path is invalid")
    return current, path[-1]


def _apply_operations(base: Mapping[str, object], operations: object) -> dict[str, object]:
    candidate = copy.deepcopy(dict(base))
    if not isinstance(operations, list):
        raise ValueError("operations must be a list")
    for operation in operations:
        if not isinstance(operation, Mapping):
            raise ValueError("operation must be an object")
        op = operation.get("op")
        path = operation.get("path")
        if not isinstance(path, list):
            raise ValueError("operation path must be a list")
        parent, key = _resolve_parent(candidate, path)
        if op == "set":
            value = copy.deepcopy(operation.get("value"))
            if isinstance(parent, list) and isinstance(key, int):
                parent[key] = value
            elif isinstance(parent, dict) and isinstance(key, str):
                parent[key] = value
            else:
                raise ValueError("set operation path is invalid")
        elif op == "delete":
            if isinstance(parent, list) and isinstance(key, int):
                del parent[key]
            elif isinstance(parent, dict) and isinstance(key, str):
                del parent[key]
            else:
                raise ValueError("delete operation path is invalid")
        else:
            raise ValueError("unsupported fixture operation")
    return candidate


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    base = manifest.get("base_candidate")
    if not isinstance(base, Mapping):
        raise ValueError("base_candidate must be an object")
    candidate = _apply_operations(base, entry.get("operations", []))
    candidate = bind_candidate(candidate)
    tamper = entry.get("tamper")
    if tamper == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    elif tamper == "assessment_id":
        candidate["assessment_id"] = IDENTITY_PREFIX + "f" * 24
    elif tamper is not None:
        raise ValueError("unsupported tamper mode")
    return candidate

def validate_fixture_manifest(path:Path=FIXTURE_PATH):
    m,errors=load_json_object(path)
    if m is None: return [{"name":"fixture_manifest","ok":False,"observed":{"outcome":"ERROR","codes":[e.code for e in errors]}}]
    out=[]
    for e in m.get("cases",[]):
        try:
            candidate=materialize_fixture_case(m,e); r=validate_candidate(candidate)
        except (KeyError,TypeError,ValueError):
            r=ValidationResult("ERROR",(Finding("FIXTURE_MATERIALIZATION_ERROR","/cases"),))
        expected=sorted(e.get("expected_codes",[]))
        out.append({"name":e.get("name"),"ok":r.outcome==e.get("expected_outcome") and r.codes==expected,"expected":{"outcome":e.get("expected_outcome"),"codes":expected},"observed":{"outcome":r.outcome,"codes":r.codes}})
    return out

def main(argv:Sequence[str]|None=None):
    p=argparse.ArgumentParser(); p.add_argument("path",nargs="?",type=Path); p.add_argument("--fixtures",action="store_true"); a=p.parse_args(argv)
    if a.fixtures:
        r=validate_fixture_manifest(); print(json.dumps(r,sort_keys=True)); return 0 if all(x["ok"] for x in r) else 1
    if a.path is None: p.error("path required unless --fixtures")
    c,e=load_json_object(a.path); r=ValidationResult("ERROR",tuple(e)) if c is None else validate_candidate(c)
    print(json.dumps({"outcome":r.outcome,"findings":[{"code":f.code,"field":f.field} for f in r.findings]},sort_keys=True)); return 0 if r.outcome=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
