#!/usr/bin/env python3
"""Validate the inactive Soil time-caveat fixture profile.

The validator is deterministic and no-network. Outcomes describe only local
fixture consistency and grant no source, evidence, policy, review, promotion,
release, publication, or public-use authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[5]
PROFILE_PATH = REPO_ROOT / "pipeline_specs/soil/time_caveat_profile.v1.json"
PROFILE_SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/soil/time_caveat_profile.schema.json"
)
CANDIDATE_SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/soil/time_caveat_candidate.schema.json"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/soil/time_caveat"
MAX_JSON_BYTES = 1_048_576
SCOPE = "soil-time-caveat-profile-fixture-only"
EXIT_CODES = {"PASS": 0, "HOLD": 2, "DENY": 3, "ERROR": 4}


class DuplicateKeyError(ValueError):
    """Raised for duplicate JSON object members."""


class NonFiniteNumberError(ValueError):
    """Raised for non-standard JSON number tokens."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Assessment:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS" and not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_float,
        )
    except UnicodeError:
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
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1") for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_schema(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("schema root must be an object")
    Draft202012Validator.check_schema(value)
    return value


def _schema_findings(
    value: dict[str, Any],
    schema_path: Path,
    code: str,
) -> list[Finding]:
    try:
        validator = Draft202012Validator(
            _load_schema(schema_path),
            format_checker=FormatChecker(),
        )
        errors = sorted(
            validator.iter_errors(value),
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding(code, _pointer(error.absolute_path)) for error in errors]


def _canonical_without(value: dict[str, Any], field: str) -> bytes:
    return json.dumps(
        {key: item for key, item in value.items() if key != field},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _sha256(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _sorted_unique_strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def validate_profile(profile: dict[str, Any]) -> tuple[Finding, ...]:
    findings = _schema_findings(
        profile, PROFILE_SCHEMA_PATH, "PROFILE_SCHEMA_INVALID"
    )
    declared = profile.get("spec_hash")
    if declared == "sha256:" + "0" * 64:
        findings.append(Finding("DIGEST_PLACEHOLDER", "/spec_hash"))
    if isinstance(declared, str) and declared != _sha256(
        _canonical_without(profile, "spec_hash")
    ):
        findings.append(Finding("PROFILE_HASH_MISMATCH", "/spec_hash"))

    rules = profile.get("support_rules")
    if isinstance(rules, list):
        support_types = [
            rule.get("support_type")
            for rule in rules
            if isinstance(rule, dict)
        ]
        if support_types != sorted(set(support_types)):
            findings.append(
                Finding("SUPPORT_RULES_NOT_CANONICAL", "/support_rules")
            )
        for index, rule in enumerate(rules):
            if not isinstance(rule, dict):
                continue
            for field in (
                "source_roles",
                "claim_kinds",
                "forbidden_claim_kinds",
                "required_time_axes",
            ):
                if not _sorted_unique_strings(rule.get(field)):
                    findings.append(
                        Finding(
                            "PROFILE_ARRAY_NOT_CANONICAL",
                            f"/support_rules/{index}/{field}",
                        )
                    )
    return tuple(sorted(set(findings)))


def _rule_for(
    profile: dict[str, Any], support_type: str
) -> dict[str, Any] | None:
    rules = profile.get("support_rules")
    if not isinstance(rules, list):
        return None
    for rule in rules:
        if isinstance(rule, dict) and rule.get("support_type") == support_type:
            return rule
    return None


def _authority_claimed(candidate: dict[str, Any]) -> bool:
    governance = candidate.get("governance")
    if not isinstance(governance, dict):
        return False
    return any(
        governance.get(field) is not False
        for field in (
            "source_activated",
            "policy_evaluated",
            "release_authorized",
            "public_use_allowed",
        )
    ) or governance.get("release_ref") is not None


def assess_candidate(
    candidate: dict[str, Any],
    profile: dict[str, Any],
) -> Assessment:
    profile_findings = validate_profile(profile)
    if profile_findings:
        return Assessment("ERROR", profile_findings)

    if _authority_claimed(candidate):
        return Assessment(
            "DENY", (Finding("GOVERNANCE_AUTHORITY_CLAIM", "/governance"),)
        )

    schema_findings = _schema_findings(
        candidate, CANDIDATE_SCHEMA_PATH, "CANDIDATE_SCHEMA_INVALID"
    )
    if schema_findings:
        return Assessment("ERROR", tuple(sorted(set(schema_findings))))

    findings: list[Finding] = []
    holds: list[Finding] = []
    support_type = candidate["support_type"]
    rule = _rule_for(profile, support_type)
    if rule is None:
        return Assessment(
            "DENY", (Finding("SUPPORT_TYPE_UNMAPPED", "/support_type"),)
        )

    if candidate["source_role"] not in rule["source_roles"]:
        findings.append(Finding("SOURCE_ROLE_MISMATCH", "/source_role"))
    claim_kind = candidate["claim_kind"]
    if claim_kind in rule["forbidden_claim_kinds"]:
        findings.append(Finding("CLAIM_KIND_FORBIDDEN", "/claim_kind"))
    elif claim_kind not in rule["claim_kinds"]:
        findings.append(Finding("CLAIM_KIND_MISMATCH", "/claim_kind"))

    if not _sorted_unique_strings(candidate.get("evidence_refs")):
        findings.append(Finding("EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs"))

    time_basis = candidate["time_basis"]
    for axis in rule["required_time_axes"]:
        if time_basis.get(axis) is None:
            holds.append(Finding("TIME_AXIS_REQUIRED", f"/time_basis/{axis}"))

    parsed = {
        field: _parse_time(time_basis.get(field))
        for field in (
            "source_published_at",
            "observed_at",
            "valid_from",
            "valid_to",
            "retrieved_at",
            "evaluated_at",
        )
    }
    retrieved = parsed["retrieved_at"]
    evaluated = parsed["evaluated_at"]
    observed = parsed["observed_at"]
    source_published = parsed["source_published_at"]
    valid_from = parsed["valid_from"]
    valid_to = parsed["valid_to"]

    if retrieved and evaluated and retrieved > evaluated:
        findings.append(Finding("TIME_ORDER_INVALID", "/time_basis/retrieved_at"))
    if source_published and retrieved and source_published > retrieved:
        findings.append(
            Finding("TIME_ORDER_INVALID", "/time_basis/source_published_at")
        )
    if observed and retrieved and observed > retrieved:
        findings.append(Finding("TIME_ORDER_INVALID", "/time_basis/observed_at"))
    if valid_from and valid_to and valid_from > valid_to:
        findings.append(Finding("TIME_ORDER_INVALID", "/time_basis/valid_from"))
    if valid_from and evaluated and valid_from > evaluated:
        findings.append(
            Finding("FUTURE_VALIDITY_UNSUPPORTED", "/time_basis/valid_from")
        )

    if support_type == "authoritative_static_soil":
        if observed is not None:
            findings.append(
                Finding("STATIC_OBSERVATION_COLLAPSE", "/time_basis/observed_at")
            )
        if time_basis["stale_state"] != "NOT_APPLICABLE":
            findings.append(
                Finding("STATIC_STALE_STATE_INVALID", "/time_basis/stale_state")
            )

    if support_type in {"gridded_derivative_soil", "soil_interpretation"}:
        if observed is not None:
            findings.append(
                Finding("DERIVATIVE_OBSERVATION_COLLAPSE", "/time_basis/observed_at")
            )

    maximum_age = rule.get("maximum_age_seconds")
    stale_state = time_basis["stale_state"]
    if isinstance(maximum_age, int) and observed and evaluated:
        age_seconds = (evaluated - observed).total_seconds()
        if age_seconds < 0:
            findings.append(
                Finding("TIME_ORDER_INVALID", "/time_basis/observed_at")
            )
        else:
            actual_stale = age_seconds > maximum_age
            if actual_stale and stale_state == "FRESH":
                findings.append(
                    Finding("STALE_STATE_MISMATCH", "/time_basis/stale_state")
                )
            elif actual_stale:
                holds.append(Finding("SUPPORT_STALE", "/time_basis/observed_at"))
            elif stale_state == "STALE":
                holds.append(
                    Finding("STALE_STATE_REVIEW_REQUIRED", "/time_basis/stale_state")
                )
            elif stale_state == "UNKNOWN":
                holds.append(
                    Finding("STALE_STATE_UNKNOWN", "/time_basis/stale_state")
                )
            elif stale_state == "NOT_APPLICABLE":
                findings.append(
                    Finding("STALE_STATE_MISMATCH", "/time_basis/stale_state")
                )

    if findings:
        return Assessment("DENY", tuple(sorted(set(findings + holds))))
    if holds:
        return Assessment("HOLD", tuple(sorted(set(holds))))
    return Assessment("PASS", ())


def validate_path(
    candidate_path: Path,
    *,
    profile_path: Path = PROFILE_PATH,
) -> Assessment:
    profile, profile_read_findings = _read_object(profile_path)
    if profile is None:
        return Assessment("ERROR", tuple(sorted(profile_read_findings)))
    candidate, candidate_read_findings = _read_object(candidate_path)
    if candidate is None:
        return Assessment("ERROR", tuple(sorted(candidate_read_findings)))
    return assess_candidate(candidate, profile)


def _report(assessment: Assessment) -> dict[str, Any]:
    return {
        "outcome": assessment.outcome,
        "finding_codes": sorted({finding.code for finding in assessment.findings}),
        "scope": SCOPE,
        "authority": "NONE",
    }


def validate_fixtures() -> int:
    expected_by_lane = {
        "pass": "PASS",
        "hold": "HOLD",
        "deny": "DENY",
        "error": "ERROR",
    }
    cases = 0
    mismatches: list[str] = []
    counts = {outcome: 0 for outcome in EXIT_CODES}
    for lane, expected in expected_by_lane.items():
        for path in sorted((FIXTURE_ROOT / lane).glob("*.json")):
            cases += 1
            assessment = validate_path(path)
            counts[assessment.outcome] += 1
            if assessment.outcome != expected:
                mismatches.append(path.name)
    output = {
        "outcome": "PASS" if not mismatches and cases else "ERROR",
        "cases": cases,
        "counts": counts,
        "mismatch_count": len(mismatches),
        "scope": SCOPE,
        "authority": "NONE",
    }
    print(json.dumps(output, sort_keys=True))
    return 0 if output["outcome"] == "PASS" else 4


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the inactive Soil time-caveat fixture profile."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--candidate", type=Path)
    group.add_argument("--fixtures", action="store_true")
    parser.add_argument("--profile", type=Path, default=PROFILE_PATH)
    args = parser.parse_args()

    if args.fixtures:
        return validate_fixtures()

    assessment = validate_path(args.candidate, profile_path=args.profile)
    print(json.dumps(_report(assessment), sort_keys=True))
    return EXIT_CODES[assessment.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
