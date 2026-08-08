#!/usr/bin/env python3
import json, sys
from datetime import datetime, timezone
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

SCHEMA = Path(__file__).parents[3] / "schemas/contracts/v1/evidence/temporal_authority_envelope.schema.json"

def dt(v):
    return None if v is None else datetime.fromisoformat(v.replace("Z", "+00:00"))

def validate_doc(doc):
    schema=json.loads(SCHEMA.read_text())
    errors=[e.message for e in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(doc)]
    if errors: return errors
    t=doc["times"]
    vf,vt=dt(t["valid_from"]),dt(t["valid_to"])
    su,rt=dt(t["source_updated_at"]),dt(t["retrieved_at"])
    rel,cor=dt(t["released_at"]),dt(t["corrected_at"])
    if vf and vt and vf>vt: errors.append("valid_from must not exceed valid_to")
    if su and su>rt: errors.append("source_updated_at must not exceed retrieved_at")
    if rel and rel<rt: errors.append("released_at must not precede retrieved_at")
    if cor and (not rel or cor<rel): errors.append("corrected_at requires and must not precede released_at")
    if doc["temporal_posture"]=="SUPERSEDED" and not doc.get("supersedes_ref"): errors.append("SUPERSEDED requires supersedes_ref")
    if doc["temporal_posture"]=="WITHDRAWN" and not doc.get("withdrawal_ref"): errors.append("WITHDRAWN requires withdrawal_ref")
    fd=dt(doc["freshness_deadline"])
    if doc["temporal_posture"]=="CURRENT" and fd and fd < datetime.now(timezone.utc): errors.append("CURRENT envelope freshness_deadline is elapsed")
    return errors

def main():
    if len(sys.argv)!=2: raise SystemExit("usage: validate_temporal_authority_envelope.py FILE")
    errors=validate_doc(json.loads(Path(sys.argv[1]).read_text()))
    if errors:
        for e in errors: print(e, file=sys.stderr)
        raise SystemExit(1)
    print("valid")
if __name__=="__main__": main()
