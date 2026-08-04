#!/usr/bin/env python3
"""Evaluate synthetic Habitat land-cover materiality candidates.

The adapter emits the shared MaterialChangeAssessment shape, performs no network
access, and grants no source, policy, promotion, release, or publication authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[4]
PROFILE_PATH = REPO_ROOT / "pipeline_specs/habitat/land_cover/materiality_profile.v1.json"
PROFILE_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/habitat/land_cover/materiality_profile.schema.json"
ASSESSMENT_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/material_change_assessment.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/habitat/land_cover/materiality"
MAX_FILE_BYTES = 1_048_576
SCOPE = "habitat-land-cover-materiality-adapter-only"
_ALLOWED_FIELDS = {
    "assessment_id", "subject_ref", "baseline_ref", "candidate_ref",
    "baseline_digest", "candidate_digest", "semantic_changed",
    "analysis_unit_kind", "analysis_unit_area_ha", "metrics", "evidence", "timing",
}
_METRICS = {"reclassification_fraction", "max_net_class_delta_ha"}
_EVIDENCE_FIELDS = {
    "diff_report_ref", "validation_report_refs", "source_refs", "criterion_evidence_refs"
}
_SHA256 = re.compile(r"^sha256:[a-f0-9]{64}$")


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
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    if not path.is_file():
        return None, [Finding("FILE_NOT_FOUND", "/")]
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
            )
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
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_schema(path: Path) -> dict[str, Any]:
    schema = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    if not isinstance(schema, dict):
        raise ValueError("schema root must be an object")
    return schema


def _canonical_without(value: dict[str, Any], field: str) -> bytes:
    return json.dumps(
        {key: item for key, item in value.items() if key != field},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _sha256(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _is_zero_digest(value: Any) -> bool:
    return isinstance(value, str) and value == "sha256:" + "0" * 64


def _sorted_unique_strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _profile_findings(profile: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        schema = _load_schema(PROFILE_SCHEMA_PATH)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        findings.extend(
            Finding("PROFILE_SCHEMA_INVALID", _pointer(error.absolute_path))
            for error in validator.iter_errors(profile)
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]

    declared = profile.get("spec_hash")
    if _is_zero_digest(declared):
        findings.append(Finding("DIGEST_PLACEHOLDER", "/spec_hash"))
    if isinstance(declared, str) and declared != _sha256(
        _canonical_without(profile, "spec_hash")
    ):
        findings.append(Finding("PROFILE_HASH_MISMATCH", "/spec_hash"))
    if profile.get("status") != "PROPOSED_INACTIVE":
        findings.append(Finding("PROFILE_NOT_INACTIVE", "/status"))

    governance = profile.get("governance")
    if (
        not isinstance(governance, dict)
        or any(
            governance.get(field) is not False
            for field in (
                "source_activated",
                "policy_evaluated",
                "promotion_authorized",
                "public_use_allowed",
            )
        )
        or governance.get("release_ref") is not None
    ):
        findings.append(
            Finding("PROFILE_GOVERNANCE_VIOLATION", "/governance")
        )
    return findings


def _candidate_findings(candidate: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    for field in sorted(set(candidate) - _ALLOWED_FIELDS):
        findings.append(Finding("INPUT_FIELD_UNKNOWN", f"/{field}"))
    for field in sorted(_ALLOWED_FIELDS - set(candidate)):
        findings.append(Finding("INPUT_FIELD_MISSING", f"/{field}"))

    for field in ("baseline_digest", "candidate_digest"):
        value = candidate.get(field)
        if not isinstance(value, str) or not _SHA256.fullmatch(value):
            findings.append(Finding("DIGEST_INVALID", f"/{field}"))
        elif _is_zero_digest(value):
            findings.append(Finding("DIGEST_PLACEHOLDER", f"/{field}"))

    area = candidate.get("analysis_unit_area_ha")
    if not _is_number(area) or float(area) <= 0:
        findings.append(
            Finding("ANALYSIS_UNIT_AREA_INVALID", "/analysis_unit_area_ha")
        )

    semantic = candidate.get("semantic_changed")
    if semantic is not None and not isinstance(semantic, bool):
        findings.append(
            Finding("SEMANTIC_STATE_INVALID", "/semantic_changed")
        )

    metrics = candidate.get("metrics")
    if not isinstance(metrics, dict):
        findings.append(Finding("METRIC_MISSING", "/metrics"))
    else:
        for field in sorted(_METRICS - set(metrics)):
            findings.append(Finding("METRIC_MISSING", f"/metrics/{field}"))
        for field in sorted(set(metrics) - _METRICS):
            findings.append(Finding("METRIC_UNKNOWN", f"/metrics/{field}"))
        reclass = metrics.get("reclassification_fraction")
        if reclass is not None and (
            not _is_number(reclass) or not 0 <= float(reclass) <= 1
        ):
            findings.append(
                Finding("METRIC_INVALID", "/metrics/reclassification_fraction")
            )
        net_area = metrics.get("max_net_class_delta_ha")
        if net_area is not None and (
            not _is_number(net_area) or float(net_area) < 0
        ):
            findings.append(
                Finding("METRIC_INVALID", "/metrics/max_net_class_delta_ha")
            )

    evidence = candidate.get("evidence")
    if not isinstance(evidence, dict) or set(evidence) != _EVIDENCE_FIELDS:
        findings.append(Finding("EVIDENCE_FIELDS_INVALID", "/evidence"))
    else:
        for field in (
            "validation_report_refs",
            "source_refs",
            "criterion_evidence_refs",
        ):
            if not _sorted_unique_strings(evidence.get(field)):
                findings.append(
                    Finding("REFS_NOT_CANONICAL", f"/evidence/{field}")
                )

    timing = candidate.get("timing")
    timing_fields = {"assessed_at", "baseline_as_of", "candidate_as_of"}
    if not isinstance(timing, dict) or set(timing) != timing_fields:
        findings.append(Finding("TIMING_FIELDS_INVALID", "/timing"))
    else:
        assessed = _parse_time(timing.get("assessed_at"))
        baseline = _parse_time(timing.get("baseline_as_of"))
        current = _parse_time(timing.get("candidate_as_of"))
        if assessed is None:
            findings.append(Finding("TIME_INVALID", "/timing/assessed_at"))
        if baseline is None:
            findings.append(Finding("TIME_INVALID", "/timing/baseline_as_of"))
        if current is None:
            findings.append(Finding("TIME_INVALID", "/timing/candidate_as_of"))
        if baseline and current and baseline > current:
            findings.append(
                Finding("BASELINE_AFTER_CANDIDATE", "/timing/baseline_as_of")
            )
        if current and assessed and current > assessed:
            findings.append(
                Finding("CANDIDATE_AFTER_ASSESSMENT", "/timing/candidate_as_of")
            )
    return findings


def _criterion(
    criterion_id: str,
    metric: str,
    *,
    required: bool,
    passed: bool | None,
    observed: Any,
    threshold: Any,
    unit: str | None,
    refs: list[str],
) -> dict[str, Any]:
    result = "UNKNOWN" if passed is None else ("PASS" if passed else "FAIL")
    return {
        "criterion_id": criterion_id,
        "metric": metric,
        "required": required,
        "result": result,
        "observed_value": observed,
        "threshold": threshold,
        "unit": unit,
        "evidence_refs": refs,
    }


def _emit(
    candidate: dict[str, Any],
    profile: dict[str, Any],
) -> dict[str, Any]:
    baseline_digest = candidate["baseline_digest"]
    candidate_digest = candidate["candidate_digest"]
    byte_changed = baseline_digest != candidate_digest
    semantic_input = candidate["semantic_changed"]
    evidence = candidate["evidence"]
    criterion_refs = list(evidence["criterion_evidence_refs"])
    criteria: list[dict[str, Any]] = []

    if not byte_changed:
        change_class = "UNCHANGED"
        material = False
        outcome = "NON_EVENT"
        reasons = ["NO_BYTE_CHANGE"]
        semantic = False
    elif semantic_input is False:
        change_class = "BYTE_ONLY"
        material = False
        outcome = "NON_EVENT"
        reasons = ["BYTE_ONLY_CHANGE"]
        semantic = False
    elif (
        semantic_input is None
        or candidate["analysis_unit_kind"] != profile["analysis_unit_kind"]
    ):
        change_class = "UNDETERMINED"
        material = None
        outcome = "HOLD"
        semantic = None
        reasons = [
            "METRIC_UNAVAILABLE"
            if semantic_input is None
            else "PROFILE_UNRESOLVED"
        ]
        criteria = [
            _criterion(
                "county-materiality-any",
                "habitat.land_cover.county_materiality_any",
                required=True,
                passed=None,
                observed=None,
                threshold=True,
                unit=None,
                refs=criterion_refs,
            )
        ]
    else:
        triggers = profile["triggers"]
        reclassification = float(
            candidate["metrics"]["reclassification_fraction"]
        )
        net_area = float(candidate["metrics"]["max_net_class_delta_ha"])
        reclass_threshold = float(
            triggers["reclassification_fraction"]["threshold"]
        )
        net_threshold = max(
            float(triggers["net_area_change"]["absolute_threshold_ha"]),
            float(candidate["analysis_unit_area_ha"])
            * float(triggers["net_area_change"]["fraction_threshold"]),
        )
        reclass_pass = reclassification > reclass_threshold
        net_pass = net_area > net_threshold
        material = reclass_pass or net_pass
        change_class = "MATERIAL" if material else "SEMANTIC_NON_MATERIAL"
        outcome = "PROMOTION_CANDIDATE" if material else "NON_EVENT"
        reasons = [
            "MATERIALITY_THRESHOLD_MET"
            if material
            else "BELOW_MATERIALITY_THRESHOLD"
        ]
        semantic = True
        criteria = [
            _criterion(
                "county-materiality-any",
                "habitat.land_cover.county_materiality_any",
                required=True,
                passed=material,
                observed=material,
                threshold=True,
                unit=None,
                refs=criterion_refs,
            ),
            _criterion(
                "net-area-change",
                "habitat.land_cover.max_net_class_delta_ha",
                required=False,
                passed=net_pass,
                observed=net_area,
                threshold=net_threshold,
                unit="hectare",
                refs=criterion_refs,
            ),
            _criterion(
                "reclassification-fraction",
                "habitat.land_cover.reclassification_fraction",
                required=False,
                passed=reclass_pass,
                observed=reclassification,
                threshold=reclass_threshold,
                unit="fraction",
                refs=criterion_refs,
            ),
        ]

    return {
        "object_type": "MaterialChangeAssessment",
        "schema_version": "1.0.0",
        "assessment_id": candidate["assessment_id"],
        "subject_ref": candidate["subject_ref"],
        "baseline_ref": candidate["baseline_ref"],
        "candidate_ref": candidate["candidate_ref"],
        "profile": {
            "profile_id": profile["profile_id"],
            "profile_version": profile["profile_version"],
            "spec_hash": profile["spec_hash"],
            "digest_algorithm": profile["digest_algorithm"],
            "canonicalization_profile": profile["canonicalization_profile"],
        },
        "comparison": {
            "baseline_digest": baseline_digest,
            "candidate_digest": candidate_digest,
            "byte_changed": byte_changed,
            "semantic_changed": semantic,
        },
        "criteria": criteria,
        "classification": {
            "change_class": change_class,
            "material": material,
            "outcome": outcome,
            "reason_codes": reasons,
        },
        "evidence": {
            "diff_report_ref": evidence["diff_report_ref"],
            "validation_report_refs": list(
                evidence["validation_report_refs"]
            ),
            "source_refs": list(evidence["source_refs"]),
        },
        "timing": dict(candidate["timing"]),
        "lineage": {"supersedes": None, "superseded_by": None},
        "governance": {
            "authority_created": False,
            "policy_evaluated": False,
            "promotion_authorized": False,
            "public_use_allowed": False,
            "release_ref": None,
            "spec_hash": profile["spec_hash"],
        },
    }


def _assessment_findings(
    assessment: dict[str, Any],
) -> list[Finding]:
    try:
        schema = _load_schema(ASSESSMENT_SCHEMA_PATH)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("ASSESSMENT_SCHEMA_UNAVAILABLE", "/")]
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        Finding(
            "EMITTED_ASSESSMENT_SCHEMA_INVALID",
            _pointer(error.absolute_path),
        )
        for error in validator.iter_errors(assessment)
    ]


def evaluate_candidate(
    candidate_path: Path,
    profile_path: Path = PROFILE_PATH,
) -> AdapterResult:
    profile, findings = _read_object(profile_path)
    if profile is None:
        return AdapterResult(None, tuple(sorted(set(findings))))
    profile_findings = _profile_findings(profile)
    if profile_findings:
        return AdapterResult(None, tuple(sorted(set(profile_findings))))

    candidate, findings = _read_object(candidate_path)
    if candidate is None:
        return AdapterResult(None, tuple(sorted(set(findings))))
    candidate_findings = _candidate_findings(candidate)
    if candidate_findings:
        return AdapterResult(None, tuple(sorted(set(candidate_findings))))

    assessment = _emit(candidate, profile)
    output_findings = _assessment_findings(assessment)
    if output_findings:
        return AdapterResult(None, tuple(sorted(set(output_findings))))
    return AdapterResult(assessment, ())


def _serialize(path: Path, result: AdapterResult) -> str:
    payload: dict[str, Any] = {
        "file": path.as_posix(),
        "findings": [
            {"code": item.code, "field": item.field}
            for item in result.findings
        ],
        "outcome": "PASS" if result.ok else "FAIL",
        "scope": SCOPE,
    }
    if result.assessment is not None:
        classification = result.assessment["classification"]
        payload["change_class"] = classification["change_class"]
        payload["assessment_outcome"] = classification["outcome"]
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def _files(directory: Path, prefix: str) -> list[Path]:
    return sorted(
        directory.glob(f"{prefix}*.json"),
        key=lambda path: path.as_posix(),
    )


def run_fixture_profile() -> int:
    valid_files = _files(FIXTURE_ROOT / "valid", "valid_")
    invalid_files = _files(FIXTURE_ROOT / "invalid", "invalid_")
    try:
        expected_outputs = json.loads(
            (
                FIXTURE_ROOT / "valid/expected_outputs_manifest.json"
            ).read_text(encoding="utf-8")
        )
        expected_findings = json.loads(
            (
                FIXTURE_ROOT / "invalid/expected_findings_manifest.json"
            ).read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    if not valid_files or not invalid_files:
        return 1

    passed = True
    for path in valid_files:
        result = evaluate_candidate(path)
        print(_serialize(path, result))
        actual = (
            {
                "change_class": result.assessment["classification"][
                    "change_class"
                ],
                "outcome": result.assessment["classification"]["outcome"],
            }
            if result.assessment is not None
            else {}
        )
        if not result.ok or actual != expected_outputs.get(path.name, {}):
            passed = False
            print(
                json.dumps(
                    {
                        "actual": actual,
                        "expected": expected_outputs.get(path.name, {}),
                        "file": path.as_posix(),
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )

    for path in invalid_files:
        result = evaluate_candidate(path)
        print(_serialize(path, result))
        actual = sorted({item.code for item in result.findings})
        expected = sorted(expected_findings.get(path.name, []))
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual": actual,
                        "expected": expected,
                        "file": path.as_posix(),
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate synthetic Habitat land-cover comparisons under the "
            "inactive materiality profile."
        )
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--profile", type=Path, default=PROFILE_PATH)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files or args.profile != PROFILE_PATH:
            parser.error(
                "--fixtures cannot be combined with explicit files or --profile"
            )
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
