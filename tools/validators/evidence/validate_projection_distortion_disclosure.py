#!/usr/bin/env python3
"""Validate the inactive ProjectionDistortionDisclosure fixture profile."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/projection_distortion_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/projection_distortion_disclosure/cases.json"
HASH_PREFIX = "sha256:"

RISK_BY_DIMENSION = {
    "area": "AREA_DISTORTION",
    "distance": "DISTANCE_DISTORTION",
    "direction": "DIRECTION_DISTORTION",
    "shape": "SHAPE_DISTORTION",
}
PUBLIC_USES = {"PUBLIC_MAP_CANDIDATE", "POLICY_CONTEXT_CANDIDATE"}
WIDE_SCOPES = {"STATEWIDE", "REGIONAL"}


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    codes: list[str]

    def as_dict(self) -> dict[str, object]:
        return {"outcome": self.outcome, "codes": self.codes}


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_profile_bytes(candidate: Mapping[str, object]) -> bytes:
    payload = {
        key: value
        for key, value in candidate.items()
        if key not in {"profile_spec_hash", "observed_at"}
    }
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("ascii")


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    return HASH_PREFIX + hashlib.sha256(_canonical_profile_bytes(candidate)).hexdigest()


def _deep_merge(base: object, patch: object) -> object:
    if isinstance(base, dict) and isinstance(patch, dict):
        merged = copy.deepcopy(base)
        for key, value in patch.items():
            merged[key] = _deep_merge(merged[key], value) if key in merged else copy.deepcopy(value)
        return merged
    return copy.deepcopy(patch)


def _schema_valid(candidate: object) -> bool:
    schema = _load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return not list(validator.iter_errors(candidate))


def _resolved(reference: object) -> bool:
    return isinstance(reference, dict) and reference.get("resolution") == "RESOLVED"


def validate_candidate(candidate: object) -> ValidationResult:
    if not _schema_valid(candidate):
        return ValidationResult("ERROR", ["SCHEMA_INVALID"])
    assert isinstance(candidate, dict)

    if candidate["profile_spec_hash"] != compute_profile_hash(candidate):
        return ValidationResult("DENY", ["PROFILE_SPEC_HASH_MISMATCH"])

    projection = candidate["projection"]
    if projection["state"] == "ERROR":
        return ValidationResult("ERROR", ["PROJECTION_EVALUATION_ERROR"])

    abstain: set[str] = set()
    if projection["state"] in {"INCOMPLETE", "UNKNOWN"}:
        abstain.add("PROJECTION_DECLARATION_INCOMPLETE")
    if candidate["claim_scope"] == "UNKNOWN":
        abstain.add("CLAIM_SCOPE_UNKNOWN")
    if projection["materiality"] == "UNKNOWN":
        abstain.add("MATERIALITY_UNKNOWN")
    if not _resolved(candidate["layer_manifest"]):
        abstain.add("LAYER_MANIFEST_UNRESOLVED")
    if not _resolved(candidate["evidence_bundle"]):
        abstain.add("EVIDENCE_BUNDLE_UNRESOLVED")
    if not _resolved(projection["distortion_assessment"]):
        abstain.add("DISTORTION_ASSESSMENT_UNRESOLVED")
    if abstain:
        return ValidationResult("ABSTAIN", sorted(abstain))

    deny: set[str] = set()
    if not all(
        projection[field]
        for field in ("crs_identifier", "projection_name", "area_of_use_ref", "transformation_ref")
    ) or projection["family"] == "UNKNOWN":
        deny.add("COMPLETE_PROJECTION_IDENTITY_REQUIRED")

    distortions = candidate["distortions"]
    if any(
        distortions[name] in {"NOT_EVALUATED", "UNKNOWN"}
        for name in RISK_BY_DIMENSION
    ) or distortions["scale_variation"] != "DECLARED":
        deny.add("COMPLETE_DISTORTION_DIMENSIONS_REQUIRED")

    risks = set(candidate["disclosure"]["material_risks"])
    if projection["materiality"] == "MATERIAL":
        if not risks:
            deny.add("MATERIAL_RISK_REQUIRED")
        for dimension, risk in RISK_BY_DIMENSION.items():
            if distortions[dimension] == "DISTORTED" and risk not in risks:
                deny.add(f"{risk}_RISK_REQUIRED")
    elif projection["materiality"] == "NOT_MATERIAL" and not projection["materiality_rationale_ref"]:
        deny.add("NOT_MATERIAL_RATIONALE_REQUIRED")

    if candidate["intended_use"] in PUBLIC_USES and candidate["claim_scope"] in WIDE_SCOPES:
        disclosure = candidate["disclosure"]
        if not disclosure["review_record_refs"]:
            deny.add("PUBLIC_REVIEW_REFERENCE_REQUIRED")
        if disclosure["evidence_drawer_section_ref"] is None:
            deny.add("PUBLIC_EVIDENCE_DRAWER_REFERENCE_REQUIRED")
        if disclosure["public_interpretation_caveat"] is None:
            deny.add("PUBLIC_INTERPRETATION_CAVEAT_REQUIRED")

    if deny:
        return ValidationResult("DENY", sorted(deny))
    return ValidationResult("PASS", [])


def build_fixture_candidate(case: Mapping[str, object]) -> dict[str, object]:
    manifest = _load_json(FIXTURE_PATH)
    candidate = _deep_merge(manifest["base_candidate"], case.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if case.get("tamper_profile_hash") is True:
        candidate["profile_spec_hash"] = HASH_PREFIX + ("f" * 64)
    return candidate


def validate_fixture_manifest() -> list[dict[str, object]]:
    manifest = _load_json(FIXTURE_PATH)
    results: list[dict[str, object]] = []
    for case in manifest["cases"]:
        actual = validate_candidate(build_fixture_candidate(case)).as_dict()
        expected = case["expected"]
        results.append({
            "name": case["name"],
            "outcome": actual["outcome"],
            "codes": actual["codes"],
            "ok": actual == expected,
        })
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args()
    if not args.fixtures:
        parser.error("only --fixtures is supported by this inactive validator")
    results = validate_fixture_manifest()
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if all(result["ok"] for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
