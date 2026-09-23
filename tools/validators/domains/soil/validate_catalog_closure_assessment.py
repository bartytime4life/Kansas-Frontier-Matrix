#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

NAMES = ["semantic_contract","schema","source_descriptor","support_type_profile","deterministic_identity","evidence_bundle","validation_report","rights_decision","sensitivity_decision","correction_target","rollback_target"]
FALSE_EFFECTS = {"catalog_written":False,"triplet_written":False,"promoted":False,"released":False,"deployed":False,"published":False,"public_use_authorized":False}
PROFILE = "kfm.domains.soil.catalog-closure-assessment.v1"
CASES = Path(__file__).resolve().parents[4] / "fixtures/contracts/v1/domains/soil/catalog_closure_assessment/cases.json"

def expected_id(c):
    x=dict(c); x.pop("assessment_id",None)
    raw=json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
    return "kfm:soil-catalog-closure:"+hashlib.sha256(raw).hexdigest()

def _derive(c):
    if c.get("profile") != PROFILE or c.get("effects") != FALSE_EFFECTS: return "ERROR"
    dims=c.get("dimensions")
    if not isinstance(dims,list) or len(dims)!=11: return "ERROR"
    names=[d.get("name") for d in dims if isinstance(d,dict)]
    if names != NAMES: return "ERROR"
    for d in dims:
        state=d.get("state"); ref=d.get("ref")
        if state not in {"SATISFIED","UNRESOLVED","DENIED"}: return "ERROR"
        if state == "SATISFIED" and not isinstance(ref,str): return "ERROR"
        if state != "SATISFIED" and ref is not None: return "ERROR"
    expected="READY_FOR_REVIEW" if all(d["state"]=="SATISFIED" for d in dims) else "HOLD"
    if c.get("outcome") != expected: return "ERROR"
    if c.get("assessment_id") != expected_id(c): return "ERROR"
    return expected


def derive(c):
    """Fail closed on non-object or structurally malformed candidates."""
    if not isinstance(c, dict):
        return "ERROR"
    try:
        return _derive(c)
    except (TypeError, AttributeError):
        return "ERROR"


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
        for case in json.loads(CASES.read_text())["cases"]:
            got=derive(case["candidate"]); print(case["name"],got)
            bad += got != case["expected"]
        raise SystemExit(1 if bad else 0)
    if not a.path: p.error("path or --fixtures required")
    candidate=load_candidate(a.path)
    outcome="ERROR" if candidate is None else derive(candidate)
    print(outcome)
    raise SystemExit(1 if outcome=="ERROR" else 0)
if __name__ == "__main__": main()
