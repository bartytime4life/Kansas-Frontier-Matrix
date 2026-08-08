#!/usr/bin/env python3
import json, sys
from datetime import datetime
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
SCHEMA=Path(__file__).parents[3]/"schemas/contracts/v1/source/source_health_assessment.schema.json"
FAILED={"TIMEOUT","HTTP_ERROR","PARSE_ERROR","AUTH_ERROR"}
def dt(v): return None if v is None else datetime.fromisoformat(v.replace("Z","+00:00"))
def validate_doc(doc):
    errs=[e.message for e in Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=FormatChecker()).iter_errors(doc)]
    if errs: return errs
    if doc["result_class"] in FAILED and doc["health_outcome"]=="HEALTHY": errs.append("failed retrieval cannot be HEALTHY")
    if doc["health_outcome"]=="UNAVAILABLE" and doc["result_class"] not in FAILED: errs.append("UNAVAILABLE requires failed result")
    fd=dt(doc["freshness_deadline"]); probe=dt(doc["probed_at"])
    if fd and probe>fd and doc["health_outcome"]=="HEALTHY": errs.append("elapsed freshness cannot be HEALTHY")
    if doc["material_change"] and "MATERIAL_CHANGE" not in doc["reasons"]: errs.append("material_change requires MATERIAL_CHANGE reason")
    if doc["result_class"]=="EMPTY" and doc["health_outcome"]=="HEALTHY": errs.append("empty probe cannot prove HEALTHY")
    return errs
if __name__=="__main__":
    errs=validate_doc(json.loads(Path(sys.argv[1]).read_text()))
    if errs: print("\n".join(errs), file=sys.stderr); raise SystemExit(1)
    print("valid")
