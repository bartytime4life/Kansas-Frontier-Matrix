#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
CASES=ROOT/"fixtures/domains/soil/soil_component/cases.json"
# The workflow runs no schema check; the paired schema is closed and requires every property, nested objects included.
SCHEMA=ROOT/"schemas/contracts/v1/domains/soil/soil_component.schema.json"
SCHEMA_DOC=json.loads(SCHEMA.read_text(encoding="utf-8"))
FALSE_EFFECTS={"component_persisted":False,"evidence_resolved":False,"policy_evaluated":False,"review_approved":False,"released":False,"published":False}

def closed_shape_violations(value, schema, path="$"):
    """Paths that break the schema's closed objects or required fields, at every depth.

    The paired schemas use only properties, required, additionalProperties and items.
    """
    found = []
    properties = schema.get("properties")
    if isinstance(value, dict) and isinstance(properties, dict):
        if schema.get("additionalProperties") is False:
            found += [f"{path}.{key}" for key in sorted(set(value) - set(properties))]
        found += [f"{path}.{key}" for key in schema.get("required", []) if key not in value]
        for key, subschema in properties.items():
            if key in value:
                found += closed_shape_violations(value[key], subschema, f"{path}.{key}")
    items = schema.get("items")
    if isinstance(value, list) and isinstance(items, dict):
        for index, item in enumerate(value):
            found += closed_shape_violations(item, items, f"{path}[{index}]")
    return found


def expected_identity(c):
    x=dict(c); x.pop("id",None); x.pop("spec_hash",None)
    h=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
    return "sha256:"+h,"soil-component:"+h[:24]
def _evaluate(c):
    findings=[]
    if closed_shape_violations(c,SCHEMA_DOC): findings.append("FIELD_SET_INVALID")
    if c.get("profile")!="kfm.domains.soil.soil-component.v1" or c.get("status")!="PROPOSED_INACTIVE": findings.append("PROFILE_INVALID")
    if c.get("effects")!=FALSE_EFFECTS or any(v is not False for v in c["effects"].values()): findings.append("EFFECT_OVERCLAIM")
    if c.get("public_use_allowed") is not False: findings.append("PUBLIC_USE_OVERCLAIM")
    if c.get("release_state")!="UNRELEASED" or c.get("release_ref") is not None: findings.append("RELEASE_OVERCLAIM")
    if c.get("support_type") not in {"authoritative_static_soil","gridded_derivative_soil"}: findings.append("SUPPORT_TYPE_INVALID")
    p=c.get("component_percent")
    if not isinstance(p,(int,float)) or isinstance(p,bool) or not 0<=p<=100: findings.append("COMPONENT_PERCENT_INVALID")
    if not c.get("map_unit_ref") or not c.get("map_unit_native_id"): findings.append("MAP_UNIT_REF_MISSING")
    if c.get("source_native_key_family")!="COKEY": findings.append("SOURCE_KEY_FAMILY_MISMATCH")
    if not c.get("evidence_refs") or not c.get("rollback_ref") or not c.get("percent_method_ref"): findings.append("BOUNDARY_REF_MISSING")
    h,i=expected_identity(c)
    if c.get("spec_hash")!=h: findings.append("SPEC_HASH_MISMATCH")
    elif c.get("id")!=i: findings.append("ID_MISMATCH")
    findings=sorted(set(findings))
    if any(x in findings for x in ("PROFILE_INVALID","SPEC_HASH_MISMATCH","ID_MISMATCH","FIELD_SET_INVALID")): return "ERROR",findings
    if findings: return "DENY",findings
    return "PASS",[]


def evaluate(candidate):
    """Fail closed on non-object or structurally malformed candidates.

    Unhashable or mutually unorderable JSON values (for example a list where a
    string is expected) would otherwise escape as TypeError tracebacks.
    """
    if not isinstance(candidate, dict):
        return "ERROR", ["CANDIDATE_MALFORMED"]
    try:
        return _evaluate(candidate)
    except TypeError:
        return "ERROR", ["CANDIDATE_MALFORMED"]


def load_candidate(path):
    """Read one JSON candidate; return None when it cannot be read or parsed."""
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return None


def main():
    p=argparse.ArgumentParser(); p.add_argument("path",nargs="?"); p.add_argument("--fixtures",action="store_true"); a=p.parse_args()
    if a.fixtures:
        bad=0
        for row in json.loads(CASES.read_text())["cases"]:
            got=evaluate(row["candidate"]); print(row["name"],got[0],",".join(got[1])); bad += got!=(row["expected_outcome"],row["expected_findings"])
        raise SystemExit(1 if bad else 0)
    if not a.path: p.error("path or --fixtures required")
    candidate=load_candidate(a.path)
    out,find=("ERROR",["INPUT_UNREADABLE"]) if candidate is None else evaluate(candidate)
    print(json.dumps({"outcome":out,"findings":find},sort_keys=True))
    raise SystemExit(0 if out=="PASS" else 1)
if __name__=="__main__": main()
