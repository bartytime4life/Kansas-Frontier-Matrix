#!/usr/bin/env python3
"""Validate fixture-only API developer-experience readiness declarations.

This local validator does not discover or call APIs, authenticate references or
consumer results, mutate documentation, decide policy or review, release,
deploy, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/release/api_developer_experience_readiness_assessment.schema.json"
FIXTURE_PATH = ROOT / "fixtures/contracts/v1/release/api_developer_experience_readiness_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
EXPECTED_OUTCOMES = ["ABSTAIN", "ANSWER", "DENY", "ERROR"]
EXPECTED_FAILURE_MODES = [
    "CITATION_UNRESOLVED",
    "EVIDENCE_STALE",
    "POLICY_DENIED",
    "REFERENCE_UNAVAILABLE",
    "SCHEMA_INVALID",
]


class DuplicateKeyError(ValueError):
    """Raised when JSON repeats an object key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-finite number token."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return [finding.code for finding in self.findings]


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("INPUT_TOO_LARGE")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT")]
    return value, []


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = list(
        Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ).iter_errors(candidate)
    )
    return [] if not errors else [Finding("SCHEMA_INVALID")]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _integrity_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED"))
    documentation = candidate["documentation"]
    prototype = candidate["prototype_validation"]
    governance = candidate["governance"]
    assert isinstance(documentation, Mapping)
    assert isinstance(prototype, Mapping)
    assert isinstance(governance, Mapping)
    if not all(
        _canonical_strings(value)
        for value in (
            documentation["documented_failure_modes"],
            prototype["prototype_fixture_refs"],
            governance["review_record_refs"],
        )
    ):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL"))
    return sorted(findings)


def _abstain_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    for key, label in (
        ("onboarding", "ONBOARDING"),
        ("documentation", "DOCUMENTATION"),
        ("prototype_validation", "PROTOTYPE_VALIDATION"),
        ("governance", "GOVERNANCE"),
    ):
        section = candidate[key]
        assert isinstance(section, Mapping)
        if section["state"] in {"INCOMPLETE", "UNKNOWN"}:
            findings.add(Finding(f"{label}_{section['state']}"))
    subject = candidate["api_subject"]
    assert isinstance(subject, Mapping)
    if subject["audience_class"] == "UNKNOWN" or subject["exposure_posture"] == "UNRESOLVED":
        findings.add(Finding("SUBJECT_UNRESOLVED"))
    return sorted(findings)


def _complete_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    subject = candidate["api_subject"]
    onboarding = candidate["onboarding"]
    documentation = candidate["documentation"]
    prototype = candidate["prototype_validation"]
    governance = candidate["governance"]
    assert isinstance(subject, Mapping)
    assert isinstance(onboarding, Mapping)
    assert isinstance(documentation, Mapping)
    assert isinstance(prototype, Mapping)
    assert isinstance(governance, Mapping)

    if any(
        onboarding[key] is None
        for key in (
            "getting_started_ref",
            "access_guidance_ref",
            "resource_ontology_ref",
            "versioning_guidance_ref",
            "support_path_ref",
        )
    ):
        findings.add(Finding("ONBOARDING_REFERENCE_REQUIRED"))
    if documentation["contract_documentation_ref"] is None or documentation["terminology_review_ref"] is None:
        findings.add(Finding("DOCUMENTATION_REFERENCE_REQUIRED"))

    examples = documentation["finite_outcome_examples"]
    outcomes = [example["outcome"] for example in examples]
    if outcomes != EXPECTED_OUTCOMES:
        findings.add(Finding("FINITE_OUTCOME_EXAMPLE_COVERAGE_REQUIRED"))
    if any(example["synthetic_data_only"] is not True for example in examples):
        findings.add(Finding("SYNTHETIC_EXAMPLE_REQUIRED"))
    if any(example["citation_duties_disclosed"] is not True for example in examples):
        findings.add(Finding("CITATION_DUTY_DISCLOSURE_REQUIRED"))
    if any(example["policy_semantics_disclosed"] is not True for example in examples):
        findings.add(Finding("POLICY_SEMANTICS_DISCLOSURE_REQUIRED"))
    if documentation["documented_failure_modes"] != EXPECTED_FAILURE_MODES:
        findings.add(Finding("FAILURE_MODE_COVERAGE_REQUIRED"))

    if not prototype["prototype_fixture_refs"]:
        findings.add(Finding("PROTOTYPE_FIXTURE_REQUIRED"))
    if prototype["consumer_validation_ref"] is None or prototype["prototype_receipt_ref"] is None:
        findings.add(Finding("PROTOTYPE_EVIDENCE_REQUIRED"))
    if prototype["runtime_behavior_claimed"] is not False:
        findings.add(Finding("PROTOTYPE_RUNTIME_OVERCLAIM"))

    if (
        governance["security_review_ref"] is None
        or governance["policy_review_ref"] is None
        or not governance["review_record_refs"]
    ):
        findings.add(Finding("GOVERNANCE_REVIEW_REQUIRED"))

    audience = subject["audience_class"]
    exposure = subject["exposure_posture"]
    if (audience in {"PARTNER_CLIENT", "PUBLIC_CLIENT"} and exposure != "PUBLIC_CANDIDATE") or (
        audience == "INTERNAL_DEVELOPER" and exposure != "INTERNAL_ONLY"
    ):
        findings.add(Finding("AUDIENCE_EXPOSURE_MISMATCH"))
    closure = ("release_readiness_ref", "correction_ref", "rollback_ref")
    if exposure == "PUBLIC_CANDIDATE" and any(governance[key] is None for key in closure):
        findings.add(Finding("PUBLIC_CLOSURE_REQUIRED"))
    if exposure == "INTERNAL_ONLY" and any(governance[key] is not None for key in closure):
        findings.add(Finding("INTERNAL_RELEASE_REFERENCE_FORBIDDEN"))
    return sorted(findings)


def validate_candidate(candidate: Mapping[str, object]) -> Result:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return Result("DENY", tuple(schema_findings))
    integrity = _integrity_findings(candidate)
    if integrity:
        return Result("DENY", tuple(integrity))
    sections = [candidate[key] for key in ("onboarding", "documentation", "prototype_validation", "governance")]
    if any(isinstance(section, Mapping) and section["state"] == "ERROR" for section in sections):
        return Result("ERROR", (Finding("READINESS_ASSESSMENT_ERROR"),))
    abstain = _abstain_findings(candidate)
    if abstain:
        return Result("ABSTAIN", tuple(abstain))
    complete = _complete_findings(candidate)
    return Result("DENY", tuple(complete)) if complete else Result("PASS", ())


def _merge(base: object, overlay: object) -> object:
    if isinstance(base, dict) and isinstance(overlay, dict):
        merged = copy.deepcopy(base)
        for key, value in overlay.items():
            merged[key] = _merge(merged[key], value) if key in merged else copy.deepcopy(value)
        return merged
    return copy.deepcopy(overlay)


def _resolve_base(manifest: Mapping[str, object], name: str) -> dict[str, object]:
    bases = manifest["bases"]
    assert isinstance(bases, Mapping)
    raw = copy.deepcopy(bases[name])
    assert isinstance(raw, dict)
    parent = raw.pop("extends", None)
    if parent is None:
        return raw
    assert isinstance(parent, str)
    resolved = _merge(_resolve_base(manifest, parent), raw)
    assert isinstance(resolved, dict)
    return resolved


def _replace(document: object, pointer: str, value: object) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


def materialize_fixture_case(manifest: Mapping[str, object], case: Mapping[str, object]) -> dict[str, object]:
    candidate = _resolve_base(manifest, str(case["base"]))
    for mutation in case.get("mutations", []):
        assert isinstance(mutation, Mapping)
        _replace(candidate, str(mutation["path"]), mutation.get("value"))
    profile_hash = compute_profile_hash(candidate)
    candidate["profile_spec_hash"] = case.get("profile_spec_hash_override", profile_hash)
    return candidate


def validate_fixture_manifest() -> list[dict[str, object]]:
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    for case in manifest["cases"]:
        result = validate_candidate(materialize_fixture_case(manifest, case))
        results.append(
            {
                "name": case["name"],
                "outcome": result.outcome,
                "findings": result.codes,
                "ok": result.outcome == case["expected_outcome"] and result.codes == case["expected_findings"],
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        for result in results:
            print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        return 0 if all(result["ok"] for result in results) else 1
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    candidate, findings = load_json_object(args.input)
    result = Result("ERROR", tuple(findings)) if candidate is None else validate_candidate(candidate)
    print(json.dumps({"authority": "NONE", "execution_mode": "FIXTURE_ONLY", "outcome": result.outcome, "findings": result.codes}, sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
