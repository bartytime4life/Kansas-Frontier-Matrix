#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

PROFILE = "kfm.map.representation-fitness.v1"


def _canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()


def expected_id(candidate):
    payload = dict(candidate)
    payload.pop("assessment_id", None)
    return "kfm:representation-fitness:" + hashlib.sha256(_canonical(payload)).hexdigest()


def _dt(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def evaluate(candidate):
    errors = []
    holds = []
    if candidate.get("profile") != PROFILE:
        errors.append("PROFILE_INVALID")
    refs = candidate.get("evidence_refs", [])
    if not isinstance(refs, list) or not refs or refs != sorted(refs) or len(refs) != len(set(refs)):
        errors.append("EVIDENCE_REFS_NOT_SORTED_UNIQUE")
    effects = candidate.get("effects", {})
    if any(effects.get(k) is not False for k in ("policy_evaluated", "release_authorized", "published", "public_use_authorized")):
        errors.append("AUTHORITY_EFFECT_FORBIDDEN")

    scale = candidate.get("scale", {})
    try:
        lo = int(scale["min_supported_denominator"])
        hi = int(scale["max_supported_denominator"])
        req = int(scale["requested_denominator"])
        if lo > hi:
            errors.append("SCALE_RANGE_INVALID")
        elif not lo <= req <= hi:
            holds.append("SCALE_OUTSIDE_SUPPORT")
    except (KeyError, TypeError, ValueError):
        errors.append("SCALE_INVALID")

    temporal = candidate.get("temporal", {})
    try:
        start = _dt(temporal["support_start"])
        end = _dt(temporal["support_end"])
        reqt = _dt(temporal["requested_at"])
        if start > end:
            errors.append("TEMPORAL_RANGE_INVALID")
        elif not start <= reqt <= end:
            holds.append("TEMPORAL_SUPPORT_MISMATCH")
    except (KeyError, TypeError, ValueError):
        errors.append("TEMPORAL_INVALID")

    use = candidate.get("intended_use")
    role = candidate.get("source_role")
    fidelity = candidate.get("fidelity")
    geometry = candidate.get("geometry_character")
    reality = candidate.get("reality_boundary_ref")

    if fidelity in {"MODELED", "SYNTHETIC"} or geometry == "SYNTHETIC" or role == "SYNTHETIC":
        if not reality:
            errors.append("REALITY_BOUNDARY_REQUIRED")

    if use == "MEASUREMENT":
        if role != "OBSERVATION": holds.append("MEASUREMENT_REQUIRES_OBSERVATION")
        if fidelity != "EXACT": holds.append("MEASUREMENT_REQUIRES_EXACT_FIDELITY")
        if geometry != "EXACT": holds.append("MEASUREMENT_REQUIRES_EXACT_GEOMETRY")
    elif use == "ANALYSIS":
        if role in {"CONTEXTUAL", "SYNTHETIC"}: holds.append("ANALYSIS_SUPPORT_ROLE_INSUFFICIENT")
        if fidelity == "SYNTHETIC": holds.append("ANALYSIS_SYNTHETIC_HOLD")
    elif use == "DECISION_SUPPORT":
        if role in {"CONTEXTUAL", "SYNTHETIC"}: holds.append("DECISION_SUPPORT_ROLE_INSUFFICIENT")
        if fidelity == "SYNTHETIC" or geometry == "SYNTHETIC": holds.append("DECISION_SUPPORT_SYNTHETIC_HOLD")
    elif use not in {"BROWSE", "CONTEXT"}:
        errors.append("INTENDED_USE_INVALID")

    try:
        if candidate.get("assessment_id") != expected_id(candidate):
            errors.append("ASSESSMENT_ID_DRIFT")
    except (TypeError, ValueError):
        errors.append("ASSESSMENT_ID_ERROR")

    if errors:
        return "ERROR", sorted(set(errors))
    derived = "HOLD" if holds else "FIT"
    if candidate.get("outcome") != derived:
        return "ERROR", ["OUTCOME_DRIFT"]
    return derived, sorted(set(holds))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("path", nargs="?")
    p.add_argument("--fixtures", action="store_true")
    args = p.parse_args()
    if args.fixtures:
        data = json.loads(Path("fixtures/contracts/v1/map/representation_fitness_assessment/cases.json").read_text())
        ok = True
        for case in data["cases"]:
            outcome, findings = evaluate(case["candidate"])
            passed = outcome == case["expected"]
            print(case["name"], outcome, "PASS" if passed else "FAIL", *findings)
            ok &= passed
        return 0 if ok else 1
    if not args.path:
        p.error("path required unless --fixtures")
    try:
        candidate = json.loads(Path(args.path).read_text())
        outcome, findings = evaluate(candidate)
    except Exception:
        print(json.dumps({"outcome": "ERROR", "findings": ["INPUT_ERROR"]}))
        return 2
    print(json.dumps({"outcome": outcome, "findings": findings}, sort_keys=True))
    return 0 if outcome != "ERROR" else 1


if __name__ == "__main__":
    sys.exit(main())
