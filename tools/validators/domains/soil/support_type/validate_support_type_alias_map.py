#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
ALIAS_MAP = ROOT / "pipeline_specs/soil/support_type_alias_map.v1.json"
CANONICAL_PROFILE = ROOT / "pipeline_specs/soil/support_type_profile.v1.json"
EXPECTED = {
    "interpretation": "soil_interpretation",
    "pedon_evidence": "profile_soil_evidence",
    "satellite_grid_soil_moisture": "satellite_soil_moisture_grid",
}
FALSE_GOVERNANCE = {
    "source_activated": False,
    "evidence_resolved": False,
    "policy_evaluated": False,
    "promotion_authorized": False,
    "release_authorized": False,
    "public_use_allowed": False,
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_tokens(profile: dict) -> set[str]:
    return {item["support_type"] for item in profile["support_types"]}


def validate(alias_map: dict, profile: dict) -> list[str]:
    findings: list[str] = []
    if alias_map.get("object_type") != "SoilSupportTypeAliasMap":
        findings.append("BAD_OBJECT_TYPE")
    if alias_map.get("schema_version") != "1.0.0":
        findings.append("BAD_SCHEMA_VERSION")
    if alias_map.get("status") != "PROPOSED_INACTIVE":
        findings.append("BAD_STATUS")
    if alias_map.get("canonical_profile") != "pipeline_specs/soil/support_type_profile.v1.json":
        findings.append("BAD_CANONICAL_PROFILE")
    if alias_map.get("governance") != FALSE_GOVERNANCE:
        findings.append("GOVERNANCE_ESCALATION")

    aliases = alias_map.get("aliases")
    if not isinstance(aliases, list):
        return findings + ["ALIASES_NOT_ARRAY"]
    if [item.get("alias") for item in aliases if isinstance(item, dict)] != sorted(EXPECTED):
        findings.append("ALIAS_SET_OR_ORDER_MISMATCH")
        return findings

    canon = canonical_tokens(profile)
    observed: dict[str, str] = {}
    for item in aliases:
        if not isinstance(item, dict):
            findings.append("BAD_ALIAS_ENTRY")
            continue
        alias = item.get("alias")
        target = item.get("canonical")
        if item.get("class_preserved") is not True:
            findings.append(f"CLASS_NOT_PRESERVED:{alias}")
        if alias in canon:
            findings.append(f"ALIAS_SHADOWS_CANONICAL:{alias}")
        if target not in canon:
            findings.append(f"UNKNOWN_CANONICAL:{target}")
        observed[str(alias)] = str(target)

    if observed != EXPECTED:
        findings.append("LOSSLESS_MAPPING_MISMATCH")
    return findings


def normalize(token: str, alias_map: dict, profile: dict) -> str | None:
    canon = canonical_tokens(profile)
    if token in canon:
        return token
    mapping = {item["alias"]: item["canonical"] for item in alias_map["aliases"]}
    return mapping.get(token)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--token")
    args = parser.parse_args()
    alias_map = load(ALIAS_MAP)
    profile = load(CANONICAL_PROFILE)
    findings = validate(alias_map, profile)
    if findings:
        for finding in findings:
            print(finding)
        raise SystemExit(1)
    if args.token is not None:
        value = normalize(args.token, alias_map, profile)
        if value is None:
            print("DENY_UNKNOWN_SUPPORT_TYPE")
            raise SystemExit(2)
        print(value)
        return
    print("PASS support_type_alias_map canonical=8 aliases=3 no_network=true authority=compatibility_only")


if __name__ == "__main__":
    main()
