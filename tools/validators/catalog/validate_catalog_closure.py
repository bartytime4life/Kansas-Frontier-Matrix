#!/usr/bin/env python3
"""Validate deterministic STAC/DCAT/PROV agreement for one synthetic release packet.

The packet is a bounded test profile, not a replacement for STAC, DCAT, PROV,
ReleaseManifest, EvidenceBundle, policy, review, proof, or publication authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from typing import Any, Mapping

PROJECTIONS = ("stac", "dcat", "prov")
SHARED = (
    "release_id", "artifact_id", "artifact_digest", "evidence_refs",
    "rights_status", "sensitivity_status", "spatial_extent", "temporal_extent",
    "correction_ref", "rollback_ref",
)
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")


def finding(code: str, path: str, message: str) -> dict[str, str]:
    return {"code": code, "path": path, "message": message}


def report(findings: list[dict[str, str]]) -> dict[str, Any]:
    ordered = sorted(findings, key=lambda item: (item["code"], item["path"], item["message"]))
    return {"schema": "kfm.catalog_closure_validation.v1", "outcome": "PASS" if not ordered else "DENY",
            "findings": ordered, "authority_created": False, "publication_authorized": False}


def validate(packet: Any) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    if not isinstance(packet, dict):
        return report([finding("PACKET_NOT_OBJECT", "$", "packet must be an object")])
    if set(packet) != {"packet_version", "release", *PROJECTIONS}:
        return report([finding("PACKET_FIELDS_INVALID", "$", "packet fields differ from bounded profile")])
    if packet.get("packet_version") != "1.0.0":
        findings.append(finding("PACKET_VERSION_INVALID", "packet_version", "expected 1.0.0"))
    release = packet.get("release")
    if not isinstance(release, dict):
        return report(findings + [finding("RELEASE_NOT_OBJECT", "release", "release must be an object")])
    if set(release) != set(SHARED):
        findings.append(finding("RELEASE_FIELDS_INVALID", "release", "release fields differ from profile"))
    projection_ids: list[str] = []
    for name in PROJECTIONS:
        obj = packet.get(name)
        if not isinstance(obj, dict):
            findings.append(finding("PROJECTION_NOT_OBJECT", name, "projection must be an object")); continue
        if set(obj) != {"projection_id", *SHARED}:
            findings.append(finding("PROJECTION_FIELDS_INVALID", name, "projection fields differ from profile"))
        pid = obj.get("projection_id")
        if not isinstance(pid, str) or not pid:
            findings.append(finding("PROJECTION_ID_MISSING", f"{name}.projection_id", "stable ID required"))
        else:
            projection_ids.append(pid)
        for field in SHARED:
            if obj.get(field) != release.get(field):
                findings.append(finding("CROSS_PROJECTION_DISAGREEMENT", f"{name}.{field}",
                                        f"{field} differs from release closure record"))
    if len(projection_ids) != len(set(projection_ids)):
        findings.append(finding("DUPLICATE_PROJECTION_ID", "*.projection_id", "projection IDs must be unique"))
    digest = release.get("artifact_digest")
    if not isinstance(digest, str) or not DIGEST.fullmatch(digest):
        findings.append(finding("ARTIFACT_DIGEST_INVALID", "release.artifact_digest", "sha256 digest required"))
    refs = release.get("evidence_refs")
    if not isinstance(refs, list) or not refs or any(not isinstance(v, str) or not v for v in refs):
        findings.append(finding("EVIDENCE_REFS_EMPTY", "release.evidence_refs", "non-empty evidence refs required"))
    elif len(refs) != len(set(refs)):
        findings.append(finding("EVIDENCE_REFS_DUPLICATE", "release.evidence_refs", "evidence refs must be unique"))
    if release.get("rights_status") != "APPROVED":
        findings.append(finding("RIGHTS_NOT_APPROVED", "release.rights_status", "synthetic closure requires APPROVED"))
    if release.get("sensitivity_status") != "PUBLIC_SAFE":
        findings.append(finding("SENSITIVITY_NOT_PUBLIC_SAFE", "release.sensitivity_status", "PUBLIC_SAFE required"))
    bbox = release.get("spatial_extent")
    if not isinstance(bbox, list) or len(bbox) != 4 or any(not isinstance(v, (int, float)) for v in bbox):
        findings.append(finding("SPATIAL_EXTENT_INVALID", "release.spatial_extent", "four-number bbox required"))
    interval = release.get("temporal_extent")
    if not isinstance(interval, list) or len(interval) != 2 or any(not isinstance(v, str) or not v for v in interval):
        findings.append(finding("TEMPORAL_EXTENT_INVALID", "release.temporal_extent", "two-value interval required"))
    for field, code in (("correction_ref", "CORRECTION_REF_MISSING"), ("rollback_ref", "ROLLBACK_REF_MISSING")):
        value = release.get(field)
        if not isinstance(value, str) or not value:
            findings.append(finding(code, f"release.{field}", f"{field} required"))
    return report(findings)


def mutate(base: Mapping[str, Any], operation: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(base); parts = str(operation["path"]).split("."); cursor: Any = value
    for part in parts[:-1]: cursor = cursor[part]
    if operation["op"] == "delete": del cursor[parts[-1]]
    elif operation["op"] == "set": cursor[parts[-1]] = operation.get("value")
    else: raise ValueError(f"unsupported fixture mutation: {operation['op']}")
    return value


def run_fixtures(path: Path) -> dict[str, Any]:
    manifest = json.loads(path.read_text(encoding="utf-8")); base = manifest["base"]; results = []
    for case in manifest["cases"]:
        packet = copy.deepcopy(base)
        for operation in case.get("mutations", []): packet = mutate(packet, operation)
        result = validate(packet); codes = {item["code"] for item in result["findings"]}
        passed = result["outcome"] == case["expected_outcome"] and set(case.get("expected_codes", [])) <= codes
        results.append({"name": case["name"], "passed": passed, "outcome": result["outcome"],
                        "finding_codes": sorted(codes)})
    return {"schema": "kfm.catalog_closure_fixture_report.v1",
            "outcome": "PASS" if all(item["passed"] for item in results) else "ERROR", "cases": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path, nargs="?"); parser.add_argument("--fixtures", type=Path)
    args = parser.parse_args()
    if bool(args.packet) == bool(args.fixtures): parser.error("provide exactly one packet or --fixtures manifest")
    result = run_fixtures(args.fixtures) if args.fixtures else validate(json.loads(args.packet.read_text(encoding="utf-8")))
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["outcome"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
