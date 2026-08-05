#!/usr/bin/env python3
"""Validate the inactive Soil support-type anti-collapse fixture profile.

This validator performs no network access and grants no source, evidence,
policy, promotion, release, publication, or public-use authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[5]
PROFILE_PATH = REPO_ROOT / "pipeline_specs/soil/support_type_profile.v1.json"
PROFILE_SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/soil/support_type_profile.schema.json"
)
CANDIDATE_SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/soil/support_type_candidate.schema.json"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/soil/support_type"
MAX_JSON_BYTES = 1_048_576
SCOPE = "soil-support-type-profile-fixture-only"


class DuplicateKeyError(ValueError):
    """Raised for duplicate JSON member names."""


class NonFiniteNumberError(ValueError):
    """Raised for non-standard or non-finite JSON numbers."""


@dataclass(frozen=True, order=True)
class Finding:
    """One deterministic, non-value-bearing validation finding."""

    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def outcome(self) -> str:
        if not self.findings:
            return "PASS"
        if any(
            finding.code
            in {
                "FILE_NOT_FOUND",
                "FILE_READ_ERROR",
                "JSON_INVALID",
                "JSON_NOT_UTF8",
                "JSON_DUPLICATE_KEY",
                "JSON_NONFINITE_NUMBER",
                "ROOT_NOT_OBJECT",
                "SCHEMA_UNAVAILABLE",
                "PROFILE_INVALID",
            }
            for finding in self.findings
        ):
            return "ERROR"
        return "DENY"


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


def _canonical_without(value: dict[str, Any], field: str) -> bytes:
    return json.dumps(
        {key: item for key, item in value.items() if key != field},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _sha256(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _is_zero_digest(value: Any) -> bool:
    return isinstance(value, str) and value == "sha256:" + "0" * 64


def _sorted_unique_strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _schema_findings(
    value: dict[str, Any],
    schema_path: Path,
    code: str,
) -> list[Finding]:
    try:
        schema = _load_schema(schema_path)
        validator = Draft202012Validator(
            schema, format_checker=FormatChecker()
        )
        return [
            Finding(code, _pointer(error.absolute_path))
            for error in validator.iter_errors(value)
        ]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]


def _profile_findings(profile: dict[str, Any]) -> list[Finding]:
    findings = _schema_findings(
        profile, PROFILE_SCHEMA_PATH, "PROFILE_SCHEMA_INVALID"
    )
    if findings:
        return findings

    declared = profile.get("spec_hash")
    if _is_zero_digest(declared):
        findings.append(Finding("DIGEST_PLACEHOLDER", "/spec_hash"))
    if declared != _sha256(_canonical_without(profile, "spec_hash")):
        findings.append(Finding("PROFILE_HASH_MISMATCH", "/spec_hash"))

    rules = profile.get("support_types")
    if isinstance(rules, list):
        names = [
            rule.get("support_type")
            for rule in rules
            if isinstance(rule, dict)
        ]
        if names != sorted(names) or len(names) != len(set(names)):
            findings.append(
                Finding("SUPPORT_TYPES_NOT_CANONICAL", "/support_types")
            )
        for index, rule in enumerate(rules):
            if not isinstance(rule, dict):
                continue
            for field in (
                "source_families",
                "source_roles",
                "spatial_support",
                "claim_kinds",
                "forbidden_claim_kinds",
            ):
                if not _sorted_unique_strings(rule.get(field)):
                    findings.append(
                        Finding(
                            "PROFILE_ARRAY_NOT_CANONICAL",
                            f"/support_types/{index}/{field}",
                        )
                    )
    return findings


def validate_candidate(
    candidate: dict[str, Any],
    profile: dict[str, Any],
) -> ValidationResult:
    findings = _profile_findings(profile)
    if findings:
        return ValidationResult(tuple(sorted(set(findings))))

    findings.extend(
        _schema_findings(
            candidate,
            CANDIDATE_SCHEMA_PATH,
            "CANDIDATE_SCHEMA_INVALID",
        )
    )
    if any(finding.code == "SCHEMA_UNAVAILABLE" for finding in findings):
        return ValidationResult(tuple(sorted(set(findings))))

    for field in ("profile_spec_hash", "content_spec_hash"):
        if _is_zero_digest(candidate.get(field)):
            findings.append(Finding("DIGEST_PLACEHOLDER", f"/{field}"))

    for field in ("source_refs", "evidence_refs"):
        if not _sorted_unique_strings(candidate.get(field)):
            findings.append(
                Finding("REFS_NOT_CANONICAL", f"/{field}")
            )

    if candidate.get("profile_id") != profile.get("profile_id"):
        findings.append(Finding("PROFILE_ID_MISMATCH", "/profile_id"))
    if candidate.get("profile_version") != profile.get("profile_version"):
        findings.append(
            Finding("PROFILE_VERSION_MISMATCH", "/profile_version")
        )
    if candidate.get("profile_spec_hash") != profile.get("spec_hash"):
        findings.append(
            Finding(
                "PROFILE_HASH_BINDING_MISMATCH", "/profile_spec_hash"
            )
        )

    rules = profile.get("support_types")
    support_type = candidate.get("support_type")
    rule = None
    if isinstance(rules, list):
        for item in rules:
            if (
                isinstance(item, dict)
                and item.get("support_type") == support_type
            ):
                rule = item
                break
    if rule is None:
        findings.append(Finding("SUPPORT_TYPE_UNKNOWN", "/support_type"))
    else:
        checks = (
            (
                "source_family",
                "source_families",
                "SOURCE_FAMILY_NOT_ALLOWED",
            ),
            ("source_role", "source_roles", "SOURCE_ROLE_NOT_ALLOWED"),
            (
                "spatial_support",
                "spatial_support",
                "SPATIAL_SUPPORT_NOT_ALLOWED",
            ),
            ("claim_kind", "claim_kinds", "CLAIM_KIND_NOT_ALLOWED"),
        )
        for candidate_field, rule_field, code in checks:
            allowed = rule.get(rule_field)
            if (
                not isinstance(allowed, list)
                or candidate.get(candidate_field) not in allowed
            ):
                findings.append(Finding(code, f"/{candidate_field}"))
        forbidden = rule.get("forbidden_claim_kinds")
        if (
            isinstance(forbidden, list)
            and candidate.get("claim_kind") in forbidden
        ):
            findings.append(
                Finding("FORBIDDEN_CLAIM_KIND", "/claim_kind")
            )

    if candidate.get("public_use_requested") is not False:
        findings.append(
            Finding("PUBLIC_USE_DENIED", "/public_use_requested")
        )

    governance = candidate.get("governance")
    if isinstance(governance, dict):
        if any(
            governance.get(field) is not False
            for field in (
                "authority_created",
                "evidence_closure_claimed",
                "policy_evaluated",
                "promotion_authorized",
                "release_authorized",
                "publication_authorized",
            )
        ) or governance.get("release_ref") is not None:
            findings.append(
                Finding(
                    "CANDIDATE_GOVERNANCE_VIOLATION", "/governance"
                )
            )

    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(
    candidate_path: Path,
    *,
    profile_path: Path = PROFILE_PATH,
) -> ValidationResult:
    profile, profile_load_findings = _read_object(profile_path)
    if profile_load_findings or profile is None:
        findings = profile_load_findings or [
            Finding("PROFILE_INVALID", "/")
        ]
        return ValidationResult(tuple(sorted(set(findings))))

    candidate, candidate_load_findings = _read_object(candidate_path)
    if candidate_load_findings or candidate is None:
        findings = candidate_load_findings or [
            Finding("ROOT_NOT_OBJECT", "/")
        ]
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_candidate(candidate, profile)


def validate_fixture_tree(
    fixture_root: Path = FIXTURE_ROOT,
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    valid_paths = sorted((fixture_root / "valid").glob("*.json"))
    invalid_paths = sorted((fixture_root / "invalid").glob("*.json"))
    if not valid_paths:
        findings.append(Finding("VALID_FIXTURES_MISSING", "/valid"))
    if not invalid_paths:
        findings.append(Finding("INVALID_FIXTURES_MISSING", "/invalid"))

    for path in valid_paths:
        result = validate_file(path)
        if not result.ok:
            findings.append(
                Finding(
                    "VALID_FIXTURE_REJECTED", f"/valid/{path.name}"
                )
            )
    for path in invalid_paths:
        result = validate_file(path)
        if result.ok:
            findings.append(
                Finding(
                    "INVALID_FIXTURE_ACCEPTED", f"/invalid/{path.name}"
                )
            )
    return tuple(sorted(set(findings)))


def _report(result: ValidationResult) -> dict[str, Any]:
    return {
        "scope": SCOPE,
        "outcome": result.outcome,
        "findings": [
            {"code": finding.code, "field": finding.field}
            for finding in result.findings
        ],
        "authority": "NONE",
        "non_effects": [
            "no_source_admission",
            "no_evidence_resolution",
            "no_policy_evaluation",
            "no_promotion_release_or_publication",
        ],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate the inactive Soil support-type fixture profile."
    )
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--profile", type=Path, default=PROFILE_PATH)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--fixture-root", type=Path, default=FIXTURE_ROOT)
    args = parser.parse_args(argv)

    if args.fixtures:
        findings = validate_fixture_tree(args.fixture_root)
        result = ValidationResult(findings)
    elif args.candidate is not None:
        result = validate_file(args.candidate, profile_path=args.profile)
    else:
        parser.error("provide --candidate or --fixtures")

    print(json.dumps(_report(result), sort_keys=True))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
