#!/usr/bin/env python3
"""Validate the inactive cross-surface temporal-support fixture profile."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/temporal_support_acceptance_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/temporal_support_acceptance_assessment/cases.json"
HASH_PREFIX = "sha256:"

REQUIRED_DIMENSIONS = {
    "TILE_ARTIFACT": ("valid_time", "retrieved_at"),
    "LAYER_MANIFEST": ("valid_time", "retrieved_at"),
    "EVIDENCE_BUNDLE": ("valid_time", "observed_at", "retrieved_at"),
    "POLICY_DECISION": ("valid_time", "as_of_time"),
    "AI_ENVELOPE": ("valid_time", "retrieved_at", "as_of_time"),
}
RELEASED_STATES = {"RELEASED", "CORRECTED", "WITHDRAWN"}


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
        if key not in {"profile_spec_hash", "evaluated_at"}
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
    validator = Draft202012Validator(_load_json(SCHEMA_PATH), format_checker=FormatChecker())
    return not list(validator.iter_errors(candidate))


def _instant(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def validate_candidate(candidate: object) -> ValidationResult:
    if not _schema_valid(candidate):
        return ValidationResult("ERROR", ["SCHEMA_INVALID"])
    assert isinstance(candidate, dict)

    if candidate["profile_spec_hash"] != compute_profile_hash(candidate):
        return ValidationResult("DENY", ["PROFILE_SPEC_HASH_MISMATCH"])
    if candidate["assessment_state"] == "ERROR":
        return ValidationResult("ERROR", ["ASSESSMENT_EVALUATION_ERROR"])

    abstain: set[str] = set()
    if candidate["assessment_state"] in {"INCOMPLETE", "UNKNOWN"}:
        abstain.add("ASSESSMENT_INCOMPLETE")
    if candidate["subject"]["resolution"] != "RESOLVED":
        abstain.add("SUBJECT_UNRESOLVED")
    if candidate["temporal_support_assessment"]["resolution"] != "RESOLVED":
        abstain.add("TEMPORAL_SUPPORT_ASSESSMENT_UNRESOLVED")
    if abstain:
        return ValidationResult("ABSTAIN", sorted(abstain))

    dimensions = candidate["time_dimensions"]
    deny: set[str] = set()
    for field in REQUIRED_DIMENSIONS[candidate["subject"]["kind"]]:
        if dimensions[field] is None:
            deny.add(f"MISSING_{field.upper()}")

    valid_time = dimensions["valid_time"]
    if valid_time is not None and _instant(valid_time["start"]) >= _instant(valid_time["end"]):
        deny.add("INVALID_VALID_TIME_INTERVAL")
    if dimensions["observed_at"] and dimensions["retrieved_at"]:
        if _instant(dimensions["observed_at"]) > _instant(dimensions["retrieved_at"]):
            deny.add("OBSERVED_AFTER_RETRIEVAL")
    if dimensions["source_updated_at"] and dimensions["retrieved_at"]:
        if _instant(dimensions["source_updated_at"]) > _instant(dimensions["retrieved_at"]):
            deny.add("SOURCE_UPDATED_AFTER_RETRIEVAL")

    release_state = candidate["release_state"]
    if release_state in RELEASED_STATES and dimensions["release_time"] is None:
        deny.add("RELEASE_TIME_REQUIRED")
    if release_state in {"CORRECTED", "WITHDRAWN"} and dimensions["correction_time"] is None:
        deny.add("CORRECTION_TIME_REQUIRED")
    if dimensions["release_time"] and dimensions["correction_time"]:
        if _instant(dimensions["correction_time"]) < _instant(dimensions["release_time"]):
            deny.add("CORRECTION_BEFORE_RELEASE")
    if release_state == "WITHDRAWN":
        deny.add("WITHDRAWN_SUBJECT_NOT_ACCEPTABLE")

    if candidate["intended_use"] == "PUBLIC_SURFACE_CANDIDATE":
        if release_state not in {"RELEASED", "CORRECTED"}:
            deny.add("PUBLIC_RELEASE_STATE_REQUIRED")
        if candidate["disclosure"]["evidence_drawer_section_ref"] is None:
            deny.add("PUBLIC_EVIDENCE_DRAWER_REFERENCE_REQUIRED")
        if candidate["disclosure"]["temporal_caveat"] is None:
            deny.add("PUBLIC_TEMPORAL_CAVEAT_REQUIRED")

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
        results.append({
            "name": case["name"],
            "outcome": actual["outcome"],
            "codes": actual["codes"],
            "ok": actual == case["expected"],
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
