#!/usr/bin/env python3
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator
SCHEMA=Path(__file__).parents[3]/"schemas/contracts/v1/evidence/reality_boundary_note.schema.json"
def validate_doc(doc):
    errors=[e.message for e in Draft202012Validator(json.loads(SCHEMA.read_text())).iter_errors(doc)]
    if errors: return errors
    kind=doc["representation_kind"]; posture=doc["reality_posture"]
    transforms=[t.lower() for t in doc["transforms"]]
    if kind in {"SYNTHETIC","RECONSTRUCTED"} and posture=="DIRECT_EVIDENCE": errors.append("synthetic/reconstructed representation cannot claim DIRECT_EVIDENCE")
    if kind=="OBSERVED" and any(x in " ".join(transforms) for x in ["synthetic","reconstruct"]): errors.append("OBSERVED representation cannot carry synthetic/reconstruction transform")
    if posture in {"DIRECT_EVIDENCE","DERIVED_WITH_LIMITS"} and not doc["evidence_refs"]: errors.append("evidence-bearing posture requires evidence_refs")
    if kind in {"SYNTHETIC","RECONSTRUCTED","MODELED"} and not doc["transforms"]: errors.append("mediated representation requires transforms")
    return errors
if __name__=="__main__":
    errs=validate_doc(json.loads(Path(sys.argv[1]).read_text()))
    if errs:
        print("\n".join(errs), file=sys.stderr); raise SystemExit(1)
    print("valid")
