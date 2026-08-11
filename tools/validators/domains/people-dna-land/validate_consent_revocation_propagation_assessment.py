#!/usr/bin/env python3
"""Validate fixture-only consent revocation propagation assessments.

The validator checks one declared consent-status observation, seven scope
dimensions, and an exact dependency inventory. It does not issue consent,
authenticate receipts, execute cleanup, resolve evidence, evaluate policy,
release, or publish.
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


REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/people-dna-land/"
    "consent_revocation_propagation_assessment.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/domains/people-dna-land/consent_revocation_propagation/cases.json"
)
MAX_FILE_BYTES = 1_048_576
EXPECTED_SURFACES = ("READ", "ANSWER", "EXPORT", "TILE", "GRAPH", "INDEX", "CACHE")
IMMEDIATE_SURFACES = frozenset({"READ", "ANSWER", "EXPORT"})
MATERIALIZED_SURFACES = frozenset({"TILE", "GRAPH", "INDEX", "CACHE"})
EXPECTED_LIMITATIONS = [
    "CONSENT_DIMENSION_ONLY",
    "NO_CLEANUP_EXECUTION",
    "NO_EVIDENCE_OR_POLICY_AUTHORITY",
    "NO_REAL_PERSON_OR_DNA_DATA",
    "NO_RELEASE_OR_PUBLICATION_AUTHORITY",
]


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


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


def _load_schema() -> dict[str, object]:
    value = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("schema root must be an object")
    return value


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", _pointer(list(error.absolute_path)))
        for error in errors[:100]
    ]


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _all_scope_dimensions_match(scope: Mapping[str, object]) -> bool:
    return len(scope) == 7 and all(value is True for value in scope.values())


def _dependency_map(candidate: Mapping[str, object]) -> dict[str, Mapping[str, object]]:
    dependencies = candidate.get("dependencies")
    if not isinstance(dependencies, list):
        return {}
    result: dict[str, Mapping[str, object]] = {}
    for dependency in dependencies:
        if isinstance(dependency, Mapping) and isinstance(dependency.get("surface"), str):
            result[dependency["surface"]] = dependency
    return result


def _receipt_present(dependency: Mapping[str, object]) -> bool:
    return isinstance(dependency.get("action_receipt_ref"), str)


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))

    reason_codes = candidate.get("reason_codes")
    if not _canonical_strings(reason_codes):
        findings.add(Finding("REASON_CODES_NOT_CANONICAL", "/reason_codes"))
    reasons = set(reason_codes) if isinstance(reason_codes, list) else set()

    limitations = candidate.get("limitations")
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))

    evaluated_at = _parse_time(candidate.get("evaluated_at"))
    consent_state = candidate.get("consent_state")
    scope = candidate.get("scope_match")
    if not isinstance(consent_state, Mapping) or not isinstance(scope, Mapping):
        return sorted(findings)
    observed_at = _parse_time(consent_state.get("observed_at"))
    valid_until = _parse_time(consent_state.get("valid_until"))
    if observed_at and evaluated_at and observed_at > evaluated_at:
        findings.add(
            Finding("STATUS_OBSERVED_AFTER_EVALUATION", "/consent_state/observed_at")
        )

    dependencies = candidate.get("dependencies")
    surfaces = (
        [item.get("surface") for item in dependencies if isinstance(item, Mapping)]
        if isinstance(dependencies, list)
        else []
    )
    if tuple(surfaces) != EXPECTED_SURFACES:
        findings.add(Finding("DEPENDENCY_SURFACES_NOT_CANONICAL", "/dependencies"))
    by_surface = _dependency_map(candidate)

    status = consent_state.get("status")
    outcome = candidate.get("declared_outcome")
    scope_satisfied = _all_scope_dimensions_match(scope)

    expected_reason = {
        "ACTIVE": "ACTIVE_SCOPE_SATISFIED" if scope_satisfied else "CONSENT_SCOPE_MISMATCH",
        "REVOKED": "CONSENT_REVOKED",
        "EXPIRED": "CONSENT_EXPIRED",
        "UNKNOWN": "CONSENT_STATUS_UNKNOWN",
        "ERROR": "CONSENT_STATUS_LOOKUP_ERROR",
    }.get(status)
    if expected_reason and expected_reason not in reasons:
        findings.add(Finding("REASON_STATUS_MISMATCH", "/reason_codes"))

    if status == "ACTIVE":
        if valid_until is None:
            findings.add(Finding("ACTIVE_VALID_UNTIL_REQUIRED", "/consent_state/valid_until"))
        elif evaluated_at and evaluated_at > valid_until:
            findings.add(Finding("ACTIVE_STATUS_EXPIRED", "/consent_state/valid_until"))
        if scope_satisfied:
            if outcome != "SATISFIED":
                findings.add(Finding("ACTIVE_OUTCOME_MISMATCH", "/declared_outcome"))
            for surface in EXPECTED_SURFACES:
                dependency = by_surface.get(surface, {})
                if (
                    dependency.get("state") != "READY"
                    or dependency.get("action") != "NONE"
                    or dependency.get("action_receipt_ref") is not None
                ):
                    findings.add(Finding("ACTIVE_DEPENDENCY_NOT_READY", "/dependencies"))
                    break
        else:
            if outcome != "DENY":
                findings.add(Finding("SCOPE_OUTCOME_MISMATCH", "/declared_outcome"))
            for surface in EXPECTED_SURFACES:
                dependency = by_surface.get(surface, {})
                if (
                    dependency.get("state") != "BLOCKED"
                    or dependency.get("action") != "DENY_NEXT_USE"
                    or not _receipt_present(dependency)
                ):
                    findings.add(
                        Finding("SCOPE_PROPAGATION_INCOMPLETE", "/dependencies")
                    )
                    break

    elif status in {"REVOKED", "EXPIRED"}:
        if outcome != "DENY":
            findings.add(Finding("WITHDRAWAL_OUTCOME_MISMATCH", "/declared_outcome"))
        if status == "REVOKED" and not isinstance(
            consent_state.get("revocation_receipt_ref"), str
        ):
            findings.add(
                Finding(
                    "REVOCATION_RECEIPT_REQUIRED",
                    "/consent_state/revocation_receipt_ref",
                )
            )
        for surface in IMMEDIATE_SURFACES:
            dependency = by_surface.get(surface, {})
            if (
                dependency.get("state") != "BLOCKED"
                or dependency.get("action") != "DENY_NEXT_USE"
            ):
                findings.add(
                    Finding("REVOCATION_PROPAGATION_INCOMPLETE", "/dependencies")
                )
                break
        for surface in MATERIALIZED_SURFACES:
            dependency = by_surface.get(surface, {})
            state = dependency.get("state")
            action = dependency.get("action")
            if not (
                (state == "INVALIDATED" and action == "INVALIDATE")
                or (state == "PURGED" and action == "PURGE")
            ):
                findings.add(
                    Finding("REVOCATION_PROPAGATION_INCOMPLETE", "/dependencies")
                )
                break
        for dependency in by_surface.values():
            if not _receipt_present(dependency):
                findings.add(Finding("ACTION_RECEIPT_REQUIRED", "/dependencies"))
                break

    elif status in {"UNKNOWN", "ERROR"}:
        expected_outcome = "ABSTAIN" if status == "UNKNOWN" else "ERROR"
        if outcome != expected_outcome:
            findings.add(Finding("STATUS_OUTCOME_MISMATCH", "/declared_outcome"))
        for dependency in by_surface.values():
            state = dependency.get("state")
            action = dependency.get("action")
            if state not in {"BLOCKED", "PENDING"} or action not in {
                "DENY_NEXT_USE",
                "REVIEW",
            }:
                findings.add(Finding("UNRESOLVED_STATUS_FAIL_OPEN", "/dependencies"))
                break
            if state == "BLOCKED" and not _receipt_present(dependency):
                findings.add(Finding("ACTION_RECEIPT_REQUIRED", "/dependencies"))
                break

    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    return ValidationResult("PASS" if not findings else "DENY", tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    """Apply a deterministic merge patch with numeric list-index support."""

    if isinstance(base, list) and isinstance(patch, Mapping) and all(
        isinstance(key, str) and key.isdigit() for key in patch
    ):
        target = copy.deepcopy(base)
        for key in sorted(patch, key=int, reverse=True):
            index = int(key)
            if index >= len(target):
                raise ValueError("fixture list patch index out of range")
            if patch[key] is None:
                target.pop(index)
            else:
                target[index] = _merge_patch(target[index], patch[key])
        return target
    if not isinstance(patch, Mapping):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, Mapping) else {}
    assert isinstance(target, dict)
    for key, value in patch.items():
        if value is None:
            target.pop(key, None)
        else:
            target[key] = _merge_patch(target.get(key), value)
    return target


def _case_index(manifest: Mapping[str, object]) -> dict[str, Mapping[str, object]]:
    cases = manifest.get("cases")
    if not isinstance(cases, list):
        return {}
    return {
        entry["name"]: entry
        for entry in cases
        if isinstance(entry, Mapping) and isinstance(entry.get("name"), str)
    }


def materialize_fixture_case(
    manifest: Mapping[str, object],
    entry: Mapping[str, object],
    _seen: frozenset[str] = frozenset(),
) -> dict[str, object]:
    name = entry.get("name")
    if not isinstance(name, str) or name in _seen:
        raise ValueError("fixture case inheritance is invalid")
    parent_name = entry.get("from_case")
    if parent_name is None:
        base = manifest["base_candidate"]
    else:
        if not isinstance(parent_name, str):
            raise ValueError("fixture parent name is invalid")
        parent = _case_index(manifest).get(parent_name)
        if parent is None:
            raise ValueError("fixture parent is missing")
        base = materialize_fixture_case(manifest, parent, _seen | {name})
    candidate = _merge_patch(base, entry.get("patch", {}))
    if not isinstance(candidate, dict):
        raise ValueError("materialized fixture must be an object")
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {
                    "outcome": "ERROR",
                    "codes": sorted({item.code for item in load_findings}),
                },
            }
        ]
    cases = manifest.get("cases")
    if not isinstance(cases, list):
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {"outcome": "ERROR", "codes": ["FIXTURE_CASES_INVALID"]},
            }
        ]
    results: list[dict[str, object]] = []
    for entry in cases:
        if not isinstance(entry, Mapping):
            results.append(
                {
                    "name": "invalid-entry",
                    "ok": False,
                    "observed": {"outcome": "ERROR", "codes": ["FIXTURE_CASE_INVALID"]},
                }
            )
            continue
        try:
            candidate = materialize_fixture_case(manifest, entry)
            result = validate_candidate(candidate)
            observed = {"outcome": result.outcome, "codes": result.codes}
        except (KeyError, TypeError, ValueError, RecursionError):
            observed = {"outcome": "ERROR", "codes": ["FIXTURE_CASE_INVALID"]}
        expected = entry.get("expected")
        results.append(
            {
                "name": entry.get("name", "invalid-entry"),
                "ok": observed == expected,
                "expected": expected,
                "observed": observed,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only consent revocation propagation assessments."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
