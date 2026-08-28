#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

PROFILE = "kfm.governance.evidence-resolution-record.v1"
FALSE_EFFECTS = (
    "evidence_created",
    "policy_evaluated",
    "lifecycle_written",
    "promoted",
    "released",
    "deployed",
    "published",
    "public_use_authorized",
)


def canonical_bytes(obj):
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def expected_record_id(record):
    payload = dict(record)
    payload.pop("record_id", None)
    return "kfm:evidence-resolution:" + hashlib.sha256(canonical_bytes(payload)).hexdigest()


def derive(record):
    findings = []
    if record.get("profile") != PROFILE:
        findings.append("PROFILE_INVALID")

    requested = record.get("requested_refs")
    rows = record.get("resolutions")

    if not isinstance(requested, list) or not requested:
        findings.append("REQUESTED_REFS_INVALID")
        requested = []
    if requested != sorted(requested) or len(requested) != len(set(requested)):
        findings.append("REQUESTED_REFS_NOT_SORTED_UNIQUE")

    if not isinstance(rows, list) or not rows:
        findings.append("RESOLUTIONS_INVALID")
        rows = []

    refs = [row.get("evidence_ref") for row in rows if isinstance(row, dict)]
    if refs != sorted(refs) or len(refs) != len(set(refs)):
        findings.append("RESOLUTIONS_NOT_SORTED_UNIQUE")
    if set(refs) != set(requested):
        findings.append("RESOLUTION_COVERAGE_MISMATCH")

    counts = {"RESOLVED": 0, "UNRESOLVED": 0, "DENIED": 0}
    for row in rows:
        if not isinstance(row, dict):
            findings.append("RESOLUTION_ROW_INVALID")
            continue
        status = row.get("status")
        if status not in counts:
            findings.append("RESOLUTION_STATUS_INVALID")
            continue
        counts[status] += 1
        has_bundle = bool(row.get("bundle_id")) or bool(row.get("bundle_digest"))
        if status == "RESOLVED":
            digest = row.get("bundle_digest", "")
            if not row.get("bundle_id") or not (
                isinstance(digest, str)
                and digest.startswith("sha256:")
                and len(digest) == 71
                and all(ch in "0123456789abcdef" for ch in digest[7:])
            ):
                findings.append("RESOLVED_BUNDLE_REQUIRED")
        elif has_bundle:
            findings.append("NONRESOLVED_BUNDLE_FORBIDDEN")

    effects = record.get("effects")
    if not isinstance(effects, dict) or any(effects.get(key) is not False for key in FALSE_EFFECTS):
        findings.append("AUTHORITY_EFFECT_FORBIDDEN")

    try:
        if record.get("record_id") != expected_record_id(record):
            findings.append("RECORD_ID_DRIFT")
    except (TypeError, ValueError):
        findings.append("RECORD_ID_ERROR")

    if findings:
        return "ERROR", sorted(set(findings))

    total = len(rows)
    if counts["DENIED"] == total:
        outcome = "DENIED"
    elif counts["RESOLVED"] == total:
        outcome = "COMPLETE"
    elif counts["RESOLVED"] == 0:
        outcome = "UNRESOLVED"
    else:
        outcome = "PARTIAL"

    if record.get("outcome") != outcome:
        return "ERROR", ["OUTCOME_DRIFT"]
    return outcome, []


def load(path):
    def reject_duplicate_keys(pairs):
        output = {}
        for key, value in pairs:
            if key in output:
                raise ValueError("duplicate JSON key")
            output[key] = value
        return output

    return json.loads(
        Path(path).read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"non-finite value: {value}")),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--cases", action="store_true")
    args = parser.parse_args()

    if args.cases:
        document = load("fixtures/contracts/v1/governance/evidence_resolution_record/cases.json")
        passed_all = True
        for case in document["cases"]:
            decision, findings = derive(case["candidate"])
            passed = decision == case["expected"]
            print(f"{case['name']}: {decision} {'PASS' if passed else 'FAIL'} {' '.join(findings)}")
            passed_all &= passed
        return 0 if passed_all else 1

    if not args.path:
        parser.error("path required unless --cases")
    try:
        record = load(args.path)
        decision, findings = derive(record)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"decision": "ERROR", "findings": ["INPUT_ERROR"], "detail": str(exc)}))
        return 2

    print(json.dumps({"decision": decision, "findings": findings}, sort_keys=True))
    return 0 if decision != "ERROR" else 1


if __name__ == "__main__":
    sys.exit(main())
