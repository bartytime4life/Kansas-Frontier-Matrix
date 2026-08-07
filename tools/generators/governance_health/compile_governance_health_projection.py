#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

PROFILE = "kfm.governance.health-projection.v1"
INDICATORS = (
    "evidence_ref_resolution_rate",
    "cite_or_abstain_compliance",
    "release_with_rollback_rate",
    "derivative_invalidation_coverage",
    "sensitive_lane_fail_closed_rate",
    "ai_receipt_presence_rate",
    "adr_completeness",
)
EXPECTED_FAMILY = {
    "evidence_ref_resolution_rate": "EVIDENCE_RESOLUTION",
    "cite_or_abstain_compliance": "CITATION_VALIDATION",
    "release_with_rollback_rate": "RELEASE_MANIFEST",
    "derivative_invalidation_coverage": "CORRECTION_NOTICE",
    "sensitive_lane_fail_closed_rate": "POLICY_DECISION",
    "ai_receipt_presence_rate": "AI_RECEIPT",
    "adr_completeness": "ADR_CHANGE",
}


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


def digest(obj):
    return "sha256:" + hashlib.sha256(canonical(obj)).hexdigest()


def ratio(passed, total):
    return {"numerator": passed, "denominator": total, "value": None if total == 0 else passed / total}


def compile_projection(source):
    if not isinstance(source, dict):
        raise ValueError("source root must be object")
    observations = source.get("observations", [])
    drift = source.get("drift_entries", [])
    if not isinstance(observations, list) or not isinstance(drift, list):
        raise ValueError("observations and drift_entries must be arrays")

    seen_refs = set()
    counts = {name: [0, 0] for name in INDICATORS}
    for row in observations:
        if not isinstance(row, dict):
            raise ValueError("observation must be object")
        indicator = row.get("indicator")
        if indicator not in counts:
            raise ValueError("unknown indicator")
        if row.get("source_family") != EXPECTED_FAMILY[indicator]:
            raise ValueError("source family does not match indicator")
        ref = row.get("source_record_ref")
        if not isinstance(ref, str) or not ref or ref in seen_refs:
            raise ValueError("source references must be non-empty and unique")
        seen_refs.add(ref)
        if not isinstance(row.get("passed"), bool):
            raise ValueError("passed must be boolean")
        counts[indicator][1] += 1
        counts[indicator][0] += int(row["passed"])

    open_drift = 0
    max_age = None
    for row in drift:
        if not isinstance(row, dict):
            raise ValueError("drift entry must be object")
        ref = row.get("source_record_ref")
        if not isinstance(ref, str) or not ref or ref in seen_refs:
            raise ValueError("source references must be non-empty and unique")
        seen_refs.add(ref)
        if not isinstance(row.get("open"), bool):
            raise ValueError("drift open must be boolean")
        age = row.get("age_days")
        if not isinstance(age, int) or age < 0:
            raise ValueError("drift age_days must be nonnegative integer")
        if row["open"]:
            open_drift += 1
            max_age = age if max_age is None else max(max_age, age)

    indicators = {name: ratio(*counts[name]) for name in INDICATORS}
    indicators["open_drift_count"] = open_drift
    indicators["max_open_drift_age_days"] = max_age

    covered = sum(1 for name in INDICATORS if counts[name][1] > 0) + int(bool(drift))
    if covered == 0:
        coverage = "EMPTY"
    elif covered == 8:
        coverage = "COMPLETE"
    else:
        coverage = "PARTIAL"

    source_digest = digest(source)
    body = {
        "profile": PROFILE,
        "source_digest": source_digest,
        "coverage_state": coverage,
        "indicators": indicators,
        "effects": {
            "policy_evaluated": False,
            "release_authorized": False,
            "published": False,
            "enforcement_changed": False,
        },
    }
    projection_id = "kfm:governance-health:" + hashlib.sha256(canonical(body)).hexdigest()
    return {"profile": PROFILE, "projection_id": projection_id, **{k: v for k, v in body.items() if k != "profile"}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args()
    try:
        if args.fixtures:
            doc = json.loads(Path("fixtures/contracts/v1/governance/governance_health_projection/cases.json").read_text(encoding="utf-8"))
            ok = True
            for case in doc["cases"]:
                result = compile_projection(case["input"])
                passed = result["coverage_state"] == case["expected_coverage"]
                print(case["name"], result["coverage_state"], "PASS" if passed else "FAIL")
                ok &= passed
            return 0 if ok else 1
        if not args.input:
            parser.error("input required unless --fixtures")
        source = json.loads(Path(args.input).read_text(encoding="utf-8"))
        print(json.dumps(compile_projection(source), sort_keys=True, indent=2))
        return 0
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        print(json.dumps({"coverage_state": "ERROR", "reason": "INVALID_INPUT"}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
