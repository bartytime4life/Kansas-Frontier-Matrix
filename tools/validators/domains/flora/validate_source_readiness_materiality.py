#!/usr/bin/env python3
"""Evaluate synthetic Flora occurrence-source readiness comparisons.

This deterministic, no-network adapter emits a shared MaterialChangeAssessment.
It does not activate sources, resolve evidence, evaluate policy, authorize
promotion, release, or publish.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[4]
PROFILE_PATH = REPO_ROOT / "pipeline_specs/flora/source_readiness/materiality_profile.v1.json"
PROFILE_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/flora/source_readiness/materiality_profile.schema.json"
CANDIDATE_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/flora/source_readiness/materiality_candidate.schema.json"
ASSESSMENT_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/material_change_assessment.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/flora/source_readiness/materiality"
SCOPE = "flora-source-readiness-materiality-adapter-only"
MAX_BYTES = 1_048_576
ZERO_SHA256 = "sha256:" + "0" * 64


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class AdapterResult:
    assessment: dict[str, Any] | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.assessment is not None and not self.findings


def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    if not path.is_file():
        return None, [Finding("FILE_NOT_FOUND", "/")]
    try:
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_object, parse_constant=_nonfinite)
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    return (value, []) if isinstance(value, dict) else (None, [Finding("ROOT_NOT_OBJECT", "/")])


def _pointer(parts: Iterable[Any]) -> str:
    items = [str(item).replace("~", "~0").replace("/", "~1") for item in parts]
    return "/" + "/".join(items) if items else "/"


def _load_schema(path: Path) -> dict[str, Any]:
    schema = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return schema


def _schema_errors(value: dict[str, Any], path: Path) -> list[Any]:
    validator = Draft202012Validator(_load_schema(path), format_checker=FormatChecker())
    return list(validator.iter_errors(value))


def _schema_findings(value: dict[str, Any], path: Path, code: str) -> list[Finding]:
    try:
        return [Finding(code, _pointer(error.absolute_path)) for error in _schema_errors(value, path)]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]


def _canonical_without(value: dict[str, Any], key: str) -> bytes:
    return json.dumps({k: v for k, v in value.items() if k != key}, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def _profile_findings(profile: dict[str, Any]) -> list[Finding]:
    findings = _schema_findings(profile, PROFILE_SCHEMA_PATH, "PROFILE_SCHEMA_INVALID")
    declared = profile.get("spec_hash")
    computed = "sha256:" + hashlib.sha256(_canonical_without(profile, "spec_hash")).hexdigest()
    if declared == ZERO_SHA256:
        findings.append(Finding("DIGEST_PLACEHOLDER", "/spec_hash"))
    elif isinstance(declared, str) and declared != computed:
        findings.append(Finding("PROFILE_HASH_MISMATCH", "/spec_hash"))
    governance = profile.get("governance", {})
    if profile.get("status") != "PROPOSED_INACTIVE" or any(governance.get(k) is not False for k in ("source_activated", "policy_evaluated", "promotion_authorized", "public_use_allowed")) or governance.get("release_ref") is not None:
        findings.append(Finding("PROFILE_GOVERNANCE_VIOLATION", "/governance"))
    return findings


def _parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _candidate_findings(candidate: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        errors = _schema_errors(candidate, CANDIDATE_SCHEMA_PATH)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    for error in errors:
        pointer = _pointer(error.absolute_path)
        if pointer.startswith("/metrics/"):
            code = "METRIC_MISSING" if error.validator == "required" else "METRIC_INVALID"
        elif pointer == "/" and error.validator == "additionalProperties":
            code = "INPUT_FIELD_UNKNOWN"
        elif pointer.startswith("/evidence") and error.validator == "required":
            code = "EVIDENCE_FIELDS_INVALID"
        elif pointer.startswith("/evidence/") and error.validator == "uniqueItems":
            code = "REFS_NOT_CANONICAL"
        else:
            code = "CANDIDATE_SCHEMA_INVALID"
        findings.append(Finding(code, pointer))
    if findings:
        return findings
    for field in ("baseline_digest", "candidate_digest"):
        if candidate[field] == ZERO_SHA256:
            findings.append(Finding("DIGEST_PLACEHOLDER", f"/{field}"))
    for field in ("validation_report_refs", "source_refs", "criterion_evidence_refs"):
        refs = candidate["evidence"][field]
        if refs != sorted(set(refs)):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/evidence/{field}"))
    timing = candidate["timing"]
    baseline = _parse_time(timing["baseline_as_of"])
    current = _parse_time(timing["candidate_as_of"])
    assessed = _parse_time(timing["assessed_at"])
    if baseline > current:
        findings.append(Finding("BASELINE_AFTER_CANDIDATE", "/timing/baseline_as_of"))
    if current > assessed:
        findings.append(Finding("CANDIDATE_AFTER_ASSESSMENT", "/timing/candidate_as_of"))
    return findings


def _criterion(identifier: str, metric: str, result: str, observed: Any, threshold: Any, unit: str | None, refs: list[str]) -> dict[str, Any]:
    return {"criterion_id": identifier, "metric": metric, "required": True, "result": result, "observed_value": observed, "threshold": threshold, "unit": unit, "evidence_refs": refs}


def _evaluate(candidate: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    baseline_digest = candidate["baseline_digest"]
    candidate_digest = candidate["candidate_digest"]
    byte_changed = baseline_digest != candidate_digest
    semantic_input = candidate["semantic_changed"]
    refs = list(candidate["evidence"]["criterion_evidence_refs"])
    criteria: list[dict[str, Any]] = []
    reasons: list[str]

    if not byte_changed:
        change_class, material, outcome, semantic, reasons = "UNCHANGED", False, "NON_EVENT", False, ["NO_BYTE_CHANGE"]
    elif semantic_input is False:
        change_class, material, outcome, semantic, reasons = "BYTE_ONLY", False, "NON_EVENT", False, ["BYTE_ONLY_CHANGE"]
    elif semantic_input is None or candidate["analysis_unit_kind"] != profile["analysis_unit_kind"]:
        change_class, material, outcome, semantic = "UNDETERMINED", None, "HOLD", None
        reasons = ["METRIC_UNAVAILABLE" if semantic_input is None else "PROFILE_UNRESOLVED"]
        criteria = [_criterion("source-readiness-evaluable", "flora.source_readiness.evaluable", "UNKNOWN", None, True, None, refs)]
    else:
        base = candidate["metrics"]["baseline"]
        current = candidate["metrics"]["candidate"]
        triggers = profile["triggers"]
        checks = [
            ("api-access-state-change", "flora.source_readiness.api_access_state_change", None if base["api_accessible"] is None or current["api_accessible"] is None else base["api_accessible"] != current["api_accessible"], current["api_accessible"], "changed", None),
            ("coordinate-uncertainty-p95-delta", "flora.source_readiness.coordinate_uncertainty_p95_delta_km", None if base["coordinate_uncertainty_p95_km"] is None or current["coordinate_uncertainty_p95_km"] is None else abs(current["coordinate_uncertainty_p95_km"] - base["coordinate_uncertainty_p95_km"]) > triggers["coordinate_uncertainty_p95_delta_km"]["threshold"], None if base["coordinate_uncertainty_p95_km"] is None or current["coordinate_uncertainty_p95_km"] is None else abs(current["coordinate_uncertainty_p95_km"] - base["coordinate_uncertainty_p95_km"]), triggers["coordinate_uncertainty_p95_delta_km"]["threshold"], "kilometre"),
            ("freshness-stale-state-change", "flora.source_readiness.freshness_stale_state_change", None if base["freshness_age_days"] is None or current["freshness_age_days"] is None else (base["freshness_age_days"] > triggers["freshness_stale_state_change"]["stale_after_days"]) != (current["freshness_age_days"] > triggers["freshness_stale_state_change"]["stale_after_days"]), current["freshness_age_days"], triggers["freshness_stale_state_change"]["stale_after_days"], "day"),
            ("georeferenced-fraction-delta", "flora.source_readiness.georeferenced_fraction_delta", None if base["georeferenced_fraction"] is None or current["georeferenced_fraction"] is None else abs(current["georeferenced_fraction"] - base["georeferenced_fraction"]) > triggers["georeferenced_fraction_delta"]["threshold"], None if base["georeferenced_fraction"] is None or current["georeferenced_fraction"] is None else abs(current["georeferenced_fraction"] - base["georeferenced_fraction"]), triggers["georeferenced_fraction_delta"]["threshold"], "fraction"),
            ("license-resolved-fraction-delta", "flora.source_readiness.license_resolved_fraction_delta", None if base["license_resolved_fraction"] is None or current["license_resolved_fraction"] is None else abs(current["license_resolved_fraction"] - base["license_resolved_fraction"]) > triggers["license_resolved_fraction_delta"]["threshold"], None if base["license_resolved_fraction"] is None or current["license_resolved_fraction"] is None else abs(current["license_resolved_fraction"] - base["license_resolved_fraction"]), triggers["license_resolved_fraction_delta"]["threshold"], "fraction"),
            ("sensitivity-posture-change", "flora.source_readiness.sensitivity_posture_change", None if base["sensitivity_posture"] is None or current["sensitivity_posture"] is None else base["sensitivity_posture"] != current["sensitivity_posture"], current["sensitivity_posture"], "changed", None),
            ("specimen-backed-fraction-delta", "flora.source_readiness.specimen_backed_fraction_delta", None if base["specimen_backed_fraction"] is None or current["specimen_backed_fraction"] is None else abs(current["specimen_backed_fraction"] - base["specimen_backed_fraction"]) > triggers["specimen_backed_fraction_delta"]["threshold"], None if base["specimen_backed_fraction"] is None or current["specimen_backed_fraction"] is None else abs(current["specimen_backed_fraction"] - base["specimen_backed_fraction"]), triggers["specimen_backed_fraction_delta"]["threshold"], "fraction"),
        ]
        criteria = [_criterion(i, m, "UNKNOWN" if passed is None else ("PASS" if passed else "FAIL"), observed, threshold, unit, refs) for i, m, passed, observed, threshold, unit in checks]
        if any(passed is None for _, _, passed, _, _, _ in checks):
            change_class, material, outcome, reasons = "UNDETERMINED", None, "HOLD", ["METRIC_UNAVAILABLE"]
        else:
            material = any(bool(passed) for _, _, passed, _, _, _ in checks)
            change_class = "MATERIAL" if material else "SEMANTIC_NON_MATERIAL"
            outcome = "PROMOTION_CANDIDATE" if material else "NON_EVENT"
            reasons = ["MATERIALITY_THRESHOLD_MET" if material else "BELOW_MATERIALITY_THRESHOLD"]
        semantic = True

    evidence = candidate["evidence"]
    return {
        "object_type": "MaterialChangeAssessment", "schema_version": "1.0.0",
        "assessment_id": candidate["assessment_id"], "subject_ref": candidate["subject_ref"],
        "baseline_ref": candidate["baseline_ref"], "candidate_ref": candidate["candidate_ref"],
        "profile": {"profile_id": profile["profile_id"], "profile_version": profile["profile_version"], "spec_hash": profile["spec_hash"], "digest_algorithm": profile["digest_algorithm"], "canonicalization_profile": profile["canonicalization_profile"]},
        "comparison": {"baseline_digest": baseline_digest, "candidate_digest": candidate_digest, "byte_changed": byte_changed, "semantic_changed": semantic},
        "criteria": criteria,
        "classification": {"change_class": change_class, "material": material, "outcome": outcome, "reason_codes": reasons},
        "evidence": {"diff_report_ref": evidence["diff_report_ref"], "validation_report_refs": list(evidence["validation_report_refs"]), "source_refs": list(evidence["source_refs"])},
        "timing": dict(candidate["timing"]), "lineage": {"supersedes": None, "superseded_by": None},
        "governance": {"authority_created": False, "policy_evaluated": False, "promotion_authorized": False, "public_use_allowed": False, "release_ref": None, "spec_hash": profile["spec_hash"]},
    }


def evaluate_candidate(candidate_path: Path, profile_path: Path = PROFILE_PATH) -> AdapterResult:
    profile, findings = _read(profile_path)
    if profile is None:
        return AdapterResult(None, tuple(sorted(set(findings))))
    findings = _profile_findings(profile)
    if findings:
        return AdapterResult(None, tuple(sorted(set(findings))))
    candidate, findings = _read(candidate_path)
    if candidate is None:
        return AdapterResult(None, tuple(sorted(set(findings))))
    findings = _candidate_findings(candidate)
    if findings:
        return AdapterResult(None, tuple(sorted(set(findings))))
    assessment = _evaluate(candidate, profile)
    findings = _schema_findings(assessment, ASSESSMENT_SCHEMA_PATH, "EMITTED_ASSESSMENT_SCHEMA_INVALID")
    return AdapterResult(None if findings else assessment, tuple(sorted(set(findings))))


def _serialize(path: Path, result: AdapterResult) -> str:
    payload: dict[str, Any] = {"file": path.as_posix(), "findings": [{"code": item.code, "field": item.field} for item in result.findings], "outcome": "PASS" if result.ok else "FAIL", "scope": SCOPE}
    if result.assessment:
        payload["change_class"] = result.assessment["classification"]["change_class"]
        payload["assessment_outcome"] = result.assessment["classification"]["outcome"]
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def run_fixture_profile() -> int:
    valid = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
    try:
        expected_outputs = json.loads((FIXTURE_ROOT / "valid/expected_outputs_manifest.json").read_text())
        expected_findings = json.loads((FIXTURE_ROOT / "invalid/expected_findings_manifest.json").read_text())
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    if not valid or not invalid:
        return 1
    passed = True
    for path in valid:
        result = evaluate_candidate(path)
        print(_serialize(path, result))
        actual = {} if not result.assessment else {"change_class": result.assessment["classification"]["change_class"], "outcome": result.assessment["classification"]["outcome"]}
        passed = passed and result.ok and actual == expected_outputs.get(path.name)
    for path in invalid:
        result = evaluate_candidate(path)
        print(_serialize(path, result))
        actual = sorted({item.code for item in result.findings})
        expected = sorted(expected_findings.get(path.name, []))
        passed = passed and not result.ok and bool(expected) and actual == expected
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate inactive synthetic Flora source-readiness materiality fixtures.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--profile", type=Path, default=PROFILE_PATH)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files or args.profile != PROFILE_PATH:
            parser.error("--fixtures cannot be combined with files or --profile")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = evaluate_candidate(path, args.profile)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
