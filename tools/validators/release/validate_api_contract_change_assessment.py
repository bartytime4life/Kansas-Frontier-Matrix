"""Validate fixture-only API contract change assessments.

The validator checks declarations only. It does not diff or mutate an API,
discover clients, execute compatibility tests, adopt version policy, authenticate
references, approve review, release, roll back, deploy, or publish.
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

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/api_contract_change_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/release/api_contract_change_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_API_MUTATION",
    "NO_CLIENT_DISCOVERY",
    "NO_COMPATIBILITY_EXECUTION",
    "NO_RELEASE_AUTHORITY",
    "NO_VERSION_POLICY_ADOPTION",
]
ABSTAIN_CODES = {
    "CHANGE_IMPACT_UNKNOWN",
    "COMPATIBILITY_INCOMPLETE",
    "COMPATIBILITY_UNKNOWN",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


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
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
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
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path))
        for error in errors[:100]
    ]


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


def _version(value: object) -> tuple[int, int, int]:
    assert isinstance(value, str)
    return tuple(int(part) for part in value.split("."))  # type: ignore[return-value]


def _version_bump(previous: tuple[int, int, int], candidate: tuple[int, int, int]) -> str | None:
    if candidate <= previous:
        return None
    if candidate[0] > previous[0]:
        return "MAJOR"
    if candidate[0] == previous[0] and candidate[1] > previous[1]:
        return "MINOR"
    if candidate[:2] == previous[:2] and candidate[2] > previous[2]:
        return "PATCH"
    return None


def _unknown_shape(subject: Mapping[str, object], compatibility: Mapping[str, object], release: Mapping[str, object]) -> bool:
    return (
        subject.get("declared_version_impact") == "UNKNOWN"
        and subject.get("change_kind") == "UNKNOWN"
        and all(subject.get(name) == "UNKNOWN" for name in (
            "response_shape_impact",
            "interpretation_impact",
            "client_behavior_impact",
            "evidence_handling_impact",
            "security_policy_impact",
        ))
        and subject.get("affected_resource_refs") == []
        and compatibility.get("declared_compatibility") == "UNKNOWN"
        and compatibility.get("compatibility_test_refs") == []
        and compatibility.get("client_fixture_refs") == []
        and compatibility.get("compatibility_rationale_ref") is None
        and compatibility.get("migration_guide_ref") is None
        and compatibility.get("deprecation_notice_ref") is None
        and release.get("change_notice_ref") is None
        and release.get("release_manifest_ref") is None
        and release.get("correction_notice_ref") is None
        and release.get("rollback_card_ref") is None
        and release.get("review_record_refs") == []
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    subject = candidate["change_subject"]
    compatibility = candidate["compatibility"]
    release = candidate["release_closure"]
    limitations = candidate["limitations"]
    assert isinstance(subject, Mapping)
    assert isinstance(compatibility, Mapping)
    assert isinstance(release, Mapping)
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    for path, value in (
        ("/change_subject/affected_resource_refs", subject.get("affected_resource_refs")),
        ("/compatibility/compatibility_test_refs", compatibility.get("compatibility_test_refs")),
        ("/compatibility/client_fixture_refs", compatibility.get("client_fixture_refs")),
        ("/release_closure/review_record_refs", release.get("review_record_refs")),
    ):
        if not _canonical_strings(value):
            findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", path))

    state = compatibility.get("state")
    if state == "ERROR":
        findings.add(Finding("COMPATIBILITY_ERROR", "/compatibility/state"))
        return sorted(findings)
    if state in {"INCOMPLETE", "UNKNOWN"}:
        findings.add(Finding(f"COMPATIBILITY_{state}", "/compatibility/state"))
        if not _unknown_shape(subject, compatibility, release):
            findings.add(Finding("COMPATIBILITY_STATE_INCOHERENT", "/compatibility"))
        return sorted(findings)

    if subject.get("previous_contract_digest") == subject.get("candidate_contract_digest"):
        findings.add(Finding("CONTRACT_DIGEST_NOT_CHANGED", "/change_subject/candidate_contract_digest"))

    previous = _version(subject.get("previous_version"))
    candidate_version = _version(subject.get("candidate_version"))
    bump = _version_bump(previous, candidate_version)
    if bump is None:
        findings.add(Finding("VERSION_NOT_ADVANCED", "/change_subject/candidate_version"))
    elif bump != subject.get("declared_version_impact"):
        findings.add(Finding("VERSION_BUMP_MISMATCH", "/change_subject/declared_version_impact"))

    # A coherent version transition is a prerequisite for interpreting the
    # compatibility declaration.  Stop here when it is invalid so callers get
    # the precise version finding instead of downstream, cascading labels.
    if bump is None or bump != subject.get("declared_version_impact"):
        return sorted(findings)

    impact_fields = (
        "response_shape_impact",
        "interpretation_impact",
        "client_behavior_impact",
        "evidence_handling_impact",
        "security_policy_impact",
    )
    if (
        subject.get("declared_version_impact") == "UNKNOWN"
        or subject.get("change_kind") == "UNKNOWN"
        or compatibility.get("declared_compatibility") == "UNKNOWN"
        or any(subject.get(name) == "UNKNOWN" for name in impact_fields)
    ):
        findings.add(Finding("CHANGE_IMPACT_UNKNOWN", "/change_subject"))
        return sorted(findings)

    if not compatibility.get("compatibility_test_refs"):
        findings.add(Finding("COMPATIBILITY_TEST_REFERENCE_REQUIRED", "/compatibility/compatibility_test_refs"))
    if not compatibility.get("client_fixture_refs"):
        findings.add(Finding("CLIENT_FIXTURE_REFERENCE_REQUIRED", "/compatibility/client_fixture_refs"))
    if compatibility.get("compatibility_rationale_ref") is None:
        findings.add(Finding("COMPATIBILITY_RATIONALE_REQUIRED", "/compatibility/compatibility_rationale_ref"))
    if release.get("change_notice_ref") is None:
        findings.add(Finding("CHANGE_NOTICE_REQUIRED", "/release_closure/change_notice_ref"))
    if release.get("release_manifest_ref") is None:
        findings.add(Finding("RELEASE_MANIFEST_REFERENCE_REQUIRED", "/release_closure/release_manifest_ref"))
    if release.get("rollback_card_ref") is None:
        findings.add(Finding("ROLLBACK_CARD_REFERENCE_REQUIRED", "/release_closure/rollback_card_ref"))
    if not release.get("review_record_refs"):
        findings.add(Finding("REVIEW_RECORD_REFERENCE_REQUIRED", "/release_closure/review_record_refs"))

    change_kind = subject.get("change_kind")
    declared_compatibility = compatibility.get("declared_compatibility")
    breaking = change_kind == "BREAKING" or subject.get("response_shape_impact") == "BREAKING"
    if breaking and (declared_compatibility != "INCOMPATIBLE" or bump != "MAJOR" or subject.get("declared_version_impact") != "MAJOR"):
        findings.add(Finding("BREAKING_CHANGE_INCOHERENT", "/change_subject"))
    elif declared_compatibility == "INCOMPATIBLE" and (bump != "MAJOR" or subject.get("declared_version_impact") != "MAJOR"):
        findings.add(Finding("INCOMPATIBLE_MAJOR_VERSION_REQUIRED", "/change_subject/declared_version_impact"))

    if (breaking or declared_compatibility == "INCOMPATIBLE") and compatibility.get("migration_guide_ref") is None:
        findings.add(Finding("MIGRATION_GUIDE_REQUIRED", "/compatibility/migration_guide_ref"))
    if change_kind == "ADDITIVE_COMPATIBLE" and (
        declared_compatibility != "BACKWARD_COMPATIBLE" or subject.get("response_shape_impact") != "ADDITIVE"
    ):
        findings.add(Finding("ADDITIVE_CHANGE_INCOHERENT", "/change_subject"))
    if change_kind == "PATCH_CORRECTION" and bump != "PATCH":
        findings.add(Finding("PATCH_CORRECTION_VERSION_INCOHERENT", "/change_subject/candidate_version"))

    correction_required = change_kind == "PATCH_CORRECTION" or any(
        subject.get(name) == "CHANGED"
        for name in ("interpretation_impact", "client_behavior_impact", "evidence_handling_impact")
    )
    if correction_required and release.get("correction_notice_ref") is None:
        findings.add(Finding("CORRECTION_NOTICE_REQUIRED", "/release_closure/correction_notice_ref"))
    if change_kind == "DEPRECATION" and compatibility.get("deprecation_notice_ref") is None:
        findings.add(Finding("DEPRECATION_NOTICE_REQUIRED", "/compatibility/deprecation_notice_ref"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if "COMPATIBILITY_ERROR" in codes:
        outcome = "ERROR"
    elif not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})},
        }]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({
            "name": entry["name"],
            "ok": observed == expected,
            "expected": expected,
            "observed": observed,
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only API contract change assessments.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = ValidationResult("ERROR", tuple(sorted(findings))) if candidate is None else validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
