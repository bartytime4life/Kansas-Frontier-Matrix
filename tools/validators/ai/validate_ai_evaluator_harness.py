#!/usr/bin/env python3
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIXTURES = ROOT / "fixtures/contracts/v1/ai/evaluator_harness/cases.json"
REQUIRED = {"evaluation_id","artifact_kind","candidate_ref","evidence_refs","metrics","policy_outcome","deterministic","network_access","result","reason_codes","spec_hash"}

def evaluate(record):
    if not isinstance(record, dict) or not REQUIRED.issubset(record):
        return "ERROR"
    if record.get("network_access") is not False or record.get("deterministic") is not True:
        return "DENY"
    if not record.get("evidence_refs") or not isinstance(record.get("metrics"), list) or not record["metrics"]:
        return "DENY"
    if record.get("policy_outcome") in {"DENY","HOLD"}:
        return "DENY"
    if record.get("policy_outcome") == "ERROR":
        return "ERROR"
    try:
        metrics_pass = all((m["value"] >= m["threshold"] if m["comparison"] == "gte" else m["value"] <= m["threshold"]) for m in record["metrics"])
    except (KeyError, TypeError):
        return "ERROR"
    expected = "PASS" if metrics_pass else "FAIL"
    return expected if record.get("result") == expected else "DENY"

def replay(path=FIXTURES):
    data=json.loads(Path(path).read_text())
    failures=[]
    for case in data["cases"]:
        actual=evaluate(case["record"])
        if actual != case["expected"]:
            failures.append((case["name"], case["expected"], actual))
    return failures

def main():
    p=argparse.ArgumentParser()
    p.add_argument("path", nargs="?")
    p.add_argument("--fixtures", action="store_true")
    a=p.parse_args()
    if a.fixtures:
        failures=replay()
        if failures:
            for f in failures: print("FAIL", *f)
            raise SystemExit(1)
        print("PASS evaluator harness fixtures")
        return
    if not a.path: p.error("path required unless --fixtures")
    record=json.loads(Path(a.path).read_text())
    print(evaluate(record))

if __name__=="__main__":
    main()
