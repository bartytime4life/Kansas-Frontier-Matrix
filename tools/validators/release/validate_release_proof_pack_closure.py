#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIXTURES = ROOT / "fixtures/contracts/v1/release/release_proof_pack_closure/cases.json"
AUTHORITY_FLAGS = {"promotion_authorized", "release_authorized", "publication_authorized", "mutation_performed"}
REF_LISTS = ("receipt_refs", "proof_refs", "catalog_refs", "review_refs")


def validate(record):
    if not isinstance(record, dict):
        return "ERROR"
    if record.get("object_type") != "ReleaseProofPackClosure":
        return "DENY"
    if record.get("candidate_state") not in {"CANDIDATE", "HELD"}:
        return "DENY"
    for key in ("release_manifest_ref", "correction_ref", "rollback_ref"):
        if not isinstance(record.get(key), str) or not record[key].strip():
            return "DENY"
    for key in REF_LISTS:
        values = record.get(key)
        if not isinstance(values, list) or not values or values != sorted(set(values)):
            return "DENY"
        if not all(isinstance(v, str) and v.strip() for v in values):
            return "DENY"
    governance = record.get("governance")
    if not isinstance(governance, dict) or set(governance) != AUTHORITY_FLAGS:
        return "DENY"
    if any(governance[k] is not False for k in AUTHORITY_FLAGS):
        return "DENY"
    outcome = record.get("outcome")
    if outcome not in {"PASS", "ABSTAIN", "DENY", "ERROR"}:
        return "ERROR"
    if outcome == "PASS" and record["candidate_state"] != "CANDIDATE":
        return "DENY"
    return outcome


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--fixtures", action="store_true")
    args = p.parse_args()
    if not args.fixtures:
        p.error("choose --fixtures")
    data = json.loads(FIXTURES.read_text())
    failures = []
    for case in data["cases"]:
        got = validate(case["record"])
        if got != case["expected"]:
            failures.append(f"{case['name']}: expected {case['expected']} got {got}")
    if failures:
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS {len(data['cases'])} cases")


if __name__ == "__main__":
    main()
