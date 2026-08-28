#!/usr/bin/env python3
"""Evaluate synthetic soil promotion materiality inputs.

The adapter emits the shared MaterialChangeAssessment shape. It performs no
network access and grants no source, policy, promotion, release, or publication
authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

PROFILE_PATH = ROOT / "pipeline_specs/soil/promotion_materiality_profile.v1.json"
PROFILE_SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/promotion_materiality_profile.schema.json"
INPUT_SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/promotion_materiality_input.schema.json"
ASSESSMENT_SCHEMA = ROOT / "schemas/contracts/v1/data/material_change_assessment.schema.json"
FIXTURES = ROOT / "fixtures/domains/soil/promotion_materiality"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
MAX_BYTES = 1_048_576
SCOPE = "soil-promotion-materiality-adapter-only"
DIMENSIONS = (
    ("content_spec_hash", "soil.hash.content_spec_hash"),
    ("policy_hash", "soil.hash.policy_hash"),
    ("schema_hash", "soil.hash.schema_hash"),
    ("source_descriptor_hash", "soil.hash.source_descriptor_hash"),
    ("validator_hash", "soil.hash.validator_hash"),
)

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


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise DuplicateKeyError(key)
        output[key] = value
    return output


def _reject_constant(value: str) -> None:
    raise NonFiniteNumberError(value)


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError(value)
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                return None, [Finding("FILE_NOT_FOUND", "/")]
            with os.fdopen(descriptor, "rb") as stream:
                descriptor = -1
                raw = stream.read(MAX_BYTES + 1)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
        if len(raw) > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_object, parse_constant=_reject_constant, parse_float=_finite_float)
    except FileNotFoundError:
        return None, [Finding("FILE_NOT_FOUND", "/")]
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_schema(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(value)
    return value


def _schema_findings(value: Mapping[str, Any], path: Path, code: str) -> list[Finding]:
    try:
        validator = Draft202012Validator(_load_schema(path), format_checker=FormatChecker())
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding(code, _pointer(error.absolute_path)) for error in validator.iter_errors(value)]


def _canonical_without(value: Mapping[str, Any], field: str) -> dict[str, Any]:
    return {key: item for key, item in value.items() if key != field}


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _canonical_refs(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _profile_findings(profile: Mapping[str, Any]) -> list[Finding]:
    findings = _schema_findings(profile, PROFILE_SCHEMA, "PROFILE_SCHEMA_INVALID")
    expected_dimensions = [{"dimension_id": dim, "criterion_id": criterion, "required": True} for dim, criterion in DIMENSIONS]
    if profile.get("substantive_dimensions") != expected_dimensions:
        findings.append(Finding("PROFILE_DIMENSIONS_MISMATCH", "/substantive_dimensions"))
    declared = profile.get("spec_hash")
    if isinstance(declared, str) and declared != compute_spec_hash(_canonical_without(profile, "spec_hash")):
        findings.append(Finding("PROFILE_HASH_MISMATCH", "/spec_hash"))
    governance = profile.get("governance")
    if not isinstance(governance, dict) or any(governance.get(field) is not False for field in ("source_activated","policy_evaluated","promotion_authorized","release_authorized","public_use_allowed")) or governance.get("release_ref") is not None:
        findings.append(Finding("PROFILE_GOVERNANCE_VIOLATION", "/governance"))
    return findings


def _input_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings = _schema_findings(candidate, INPUT_SCHEMA, "INPUT_SCHEMA_INVALID")
    evidence = candidate.get("evidence")
    if isinstance(evidence, dict):
        for field in ("validation_report_refs", "source_refs", "criterion_evidence_refs"):
            if not _canonical_refs(evidence.get(field)):
                findings.append(Finding("REFS_NOT_CANONICAL", f"/evidence/{field}"))
    timing = candidate.get("timing")
    if isinstance(timing, dict):
        baseline = _parse_time(timing.get("baseline_as_of"))
        candidate_time = _parse_time(timing.get("candidate_as_of"))
        assessed = _parse_time(timing.get("assessed_at"))
        if baseline and candidate_time and baseline > candidate_time:
            findings.append(Finding("BASELINE_AFTER_CANDIDATE", "/timing/baseline_as_of"))
        if candidate_time and assessed and candidate_time > assessed:
            findings.append(Finding("CANDIDATE_AFTER_ASSESSMENT", "/timing/candidate_as_of"))
    return findings


def _snapshot_digest(snapshot: Any) -> str:
    return compute_spec_hash({"status": "MISSING_BASELINE"} if snapshot is None else snapshot)


def _criterion(criterion_id: str, metric: str, changed: bool, refs: list[str], *, required: bool = False, count: int | None = None) -> dict[str, Any]:
    observed: Any = count if count is not None else changed
    threshold: Any = 1 if count is not None else True
    unit = "dimension_count" if count is not None else None
    return {"criterion_id": criterion_id, "metric": metric, "required": required, "result": "PASS" if changed else "FAIL", "observed_value": observed, "threshold": threshold, "unit": unit, "evidence_refs": refs}


def _governance_hash(assessment: Mapping[str, Any]) -> str:
    clone = json.loads(json.dumps(assessment))
    clone["governance"]["spec_hash"] = None
    return compute_spec_hash(clone)


def build_assessment(candidate: Mapping[str, Any], profile: Mapping[str, Any]) -> dict[str, Any]:
    baseline = candidate.get("baseline")
    current = candidate["candidate"]
    baseline_digest = _snapshot_digest(baseline)
    candidate_digest = _snapshot_digest(current)
    byte_changed = baseline_digest != candidate_digest
    evidence = candidate["evidence"]
    refs = evidence["criterion_evidence_refs"]

    criteria: list[dict[str, Any]] = []
    if baseline is None:
        semantic_changed = None
        classification = {"change_class":"UNDETERMINED","material":None,"outcome":"HOLD","reason_codes":["MISSING_BASELINE"]}
    elif candidate["evidence_complete"] is False:
        semantic_changed = None
        classification = {"change_class":"UNDETERMINED","material":None,"outcome":"HOLD","reason_codes":["INSUFFICIENT_EVIDENCE"]}
    else:
        changed_dimensions = []
        for dimension, criterion_id in DIMENSIONS:
            changed = baseline[dimension] != current[dimension]
            if changed:
                changed_dimensions.append(dimension)
            criteria.append(_criterion(criterion_id, dimension, changed, refs))
        if not byte_changed:
            semantic_changed = False
            criteria = []
            classification = {"change_class":"UNCHANGED","material":False,"outcome":"NON_EVENT","reason_codes":["NO_BYTE_CHANGE"]}
        elif not changed_dimensions:
            semantic_changed = False
            criteria.append(_criterion("soil.materiality.any_substantive_hash_changed", "substantive_hash_change_count", False, refs, required=True, count=0))
            classification = {"change_class":"BYTE_ONLY","material":False,"outcome":"NON_EVENT","reason_codes":["BYTE_ONLY_CHANGE","CANONICAL_EQUIVALENT"]}
        else:
            semantic_changed = True
            criteria.append(_criterion("soil.materiality.any_substantive_hash_changed", "substantive_hash_change_count", True, refs, required=True, count=len(changed_dimensions)))
            classification = {"change_class":"MATERIAL","material":True,"outcome":"PROMOTION_CANDIDATE","reason_codes":["DOMAIN_STATUS_CHANGE","MATERIALITY_THRESHOLD_MET"]}
    criteria.sort(key=lambda item: item["criterion_id"])
    assessment = {
        "object_type":"MaterialChangeAssessment","schema_version":"1.0.0","assessment_id":candidate["assessment_id"],"subject_ref":candidate["subject_ref"],"baseline_ref":candidate["baseline_ref"],"candidate_ref":candidate["candidate_ref"],
        "profile":{"profile_id":profile["profile_id"],"profile_version":profile["profile_version"],"spec_hash":profile["spec_hash"],"digest_algorithm":profile["digest_algorithm"],"canonicalization_profile":profile["canonicalization_profile"]},
        "comparison":{"baseline_digest":baseline_digest,"candidate_digest":candidate_digest,"byte_changed":byte_changed,"semantic_changed":semantic_changed},
        "criteria":criteria,"classification":classification,
        "evidence":{"diff_report_ref":evidence["diff_report_ref"],"validation_report_refs":evidence["validation_report_refs"],"source_refs":evidence["source_refs"]},
        "timing":candidate["timing"],"lineage":{"supersedes":None,"superseded_by":None},
        "governance":{"authority_created":False,"policy_evaluated":False,"promotion_authorized":False,"public_use_allowed":False,"release_ref":None,"spec_hash":"sha256:"+"0"*64},
    }
    assessment["governance"]["spec_hash"] = _governance_hash(assessment)
    return assessment


def assess(path: Path) -> AdapterResult:
    candidate, read_findings = _read(path)
    if candidate is None:
        return AdapterResult(None, tuple(sorted(set(read_findings))))
    try:
        profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"), object_pairs_hook=_unique_object, parse_constant=_reject_constant, parse_float=_finite_float)
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateKeyError, NonFiniteNumberError):
        return AdapterResult(None, (Finding("PROFILE_UNAVAILABLE", "/"),))
    findings = _profile_findings(profile) + _input_findings(candidate)
    if findings:
        return AdapterResult(None, tuple(sorted(set(findings))))
    assessment = build_assessment(candidate, profile)
    assessment_findings = _schema_findings(assessment, ASSESSMENT_SCHEMA, "ASSESSMENT_SCHEMA_INVALID")
    if assessment_findings:
        return AdapterResult(None, tuple(sorted(set(assessment_findings))))
    return AdapterResult(assessment, ())


def _serialize(path: Path, result: AdapterResult) -> str:
    outcome = "ERROR" if result.assessment is None else result.assessment["classification"]["outcome"]
    return json.dumps({"file":path.as_posix(),"findings":[{"code":item.code,"field":item.field} for item in result.findings],"outcome":outcome,"assessment":result.assessment,"scope":SCOPE}, sort_keys=True, separators=(",", ":"))


def run_fixtures() -> int:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    passed = True
    for case in manifest["cases"]:
        path = FIXTURES / case["input"]
        result = assess(path)
        outcome = "ERROR" if result.assessment is None else result.assessment["classification"]["outcome"]
        findings = sorted({item.code for item in result.findings})
        expected_assessment = None
        if case.get("expected_assessment"):
            expected_assessment = json.loads((FIXTURES / case["expected_assessment"]).read_text(encoding="utf-8"))
        match = outcome == case["expected_outcome"] and findings == case["expected_findings"] and (expected_assessment is None or result.assessment == expected_assessment)
        print(json.dumps({"case_id":case["case_id"],"outcome":outcome,"findings":findings,"suite_match":match}, sort_keys=True, separators=(",", ":")))
        passed = passed and match
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate fixture-only soil promotion materiality inputs.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    if not args.files:
        parser.error("provide files or --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item:item.as_posix()):
        result = assess(path)
        print(_serialize(path, result))
        failed = failed or result.assessment is None
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
