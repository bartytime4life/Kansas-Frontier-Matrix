#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CASES = ROOT / "fixtures/domains/soil/domain_layer_descriptor/cases.json"
PROFILE = "kfm.domains.soil.domain-layer-descriptor.v1"
FALSE_EFFECTS = {
    "catalog_written": False,
    "promoted": False,
    "released": False,
    "deployed": False,
    "published": False,
}
SUPPORT_TO_LAYER = {
    "authoritative_static_soil": "STATIC_SURVEY",
    "gridded_derivative_soil": "GRIDDED_DERIVATIVE",
    "station_soil_moisture": "STATION_OBSERVATION",
    "reference_station_soil_climate": "REFERENCE_STATION",
    "satellite_soil_moisture_grid": "SATELLITE_GRID",
    "profile_soil_evidence": "PROFILE_EVIDENCE",
    "soil_interpretation": "INTERPRETATION",
    "governed_change_evidence": "CHANGE_EVIDENCE",
}


def canonical_hash(candidate: dict) -> str:
    payload = dict(candidate)
    payload.pop("id", None)
    payload.pop("spec_hash", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def evaluate(candidate: dict) -> tuple[str, list[str]]:
    findings: list[str] = []
    if candidate.get("profile") != PROFILE or candidate.get("status") != "PROPOSED_INACTIVE":
        findings.append("PROFILE_MISMATCH")
    if candidate.get("domain") != "soil" or candidate.get("version") != "1.0.0":
        findings.append("IDENTITY_PROFILE_MISMATCH")
    support_type = candidate.get("support_type")
    expected_layer = SUPPORT_TO_LAYER.get(support_type)
    if expected_layer is None:
        findings.append("UNKNOWN_SUPPORT_TYPE")
    elif candidate.get("layer_family") != expected_layer:
        findings.append("SUPPORT_LAYER_COLLAPSE")
    if candidate.get("release_state") != "UNRELEASED" or candidate.get("release_ref") is not None:
        findings.append("RELEASE_OVERCLAIM")
    if candidate.get("lifecycle_stage") not in {"PROCESSED", "CATALOG"}:
        findings.append("LIFECYCLE_OVERCLAIM")
    if candidate.get("public_use_allowed") is not False:
        findings.append("PUBLIC_USE_OVERCLAIM")
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append("EFFECT_OVERCLAIM")
    for key in ("source_refs", "evidence_refs", "limitations"):
        values = candidate.get(key)
        if not isinstance(values, list) or not values or values != sorted(set(values)):
            findings.append(f"NONCANONICAL_{key.upper()}")
    if not candidate.get("rollback_ref"):
        findings.append("ROLLBACK_MISSING")
    temporal = candidate.get("temporal_scope")
    if not isinstance(temporal, dict) or temporal.get("kind") not in {"SOURCE_VINTAGE", "OBSERVED_TIME", "VALID_TIME", "RETRIEVED_TIME", "NOT_APPLICABLE"}:
        findings.append("TEMPORAL_SCOPE_INVALID")
    elif temporal.get("kind") == "NOT_APPLICABLE" and temporal.get("value") is not None:
        findings.append("TEMPORAL_SCOPE_INVALID")
    elif temporal.get("kind") != "NOT_APPLICABLE" and not isinstance(temporal.get("value"), str):
        findings.append("TEMPORAL_SCOPE_INVALID")
    digest = canonical_hash(candidate)
    if candidate.get("spec_hash") != f"sha256:{digest}":
        findings.append("SPEC_HASH_MISMATCH")
    if candidate.get("id") != f"soil-layer:{digest[:24]}":
        findings.append("ID_MISMATCH")
    if findings:
        authority_findings = {"RELEASE_OVERCLAIM", "LIFECYCLE_OVERCLAIM", "PUBLIC_USE_OVERCLAIM", "EFFECT_OVERCLAIM", "SUPPORT_LAYER_COLLAPSE"}
        return ("DENY" if any(item in authority_findings for item in findings) else "ERROR", sorted(set(findings)))
    return "PASS", []


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args()
    if args.fixtures:
        cases = json.loads(CASES.read_text(encoding="utf-8"))["cases"]
        failures = 0
        for case in cases:
            outcome, findings = evaluate(case["candidate"])
            print(json.dumps({"name": case["name"], "outcome": outcome, "findings": findings}, sort_keys=True))
            failures += outcome != case["expected_outcome"] or findings != case["expected_findings"]
        raise SystemExit(1 if failures else 0)
    if not args.path:
        parser.error("path or --fixtures required")
    outcome, findings = evaluate(json.loads(Path(args.path).read_text(encoding="utf-8")))
    print(json.dumps({"outcome": outcome, "findings": findings}, sort_keys=True))
    raise SystemExit(0 if outcome == "PASS" else 1)


if __name__ == "__main__":
    main()
