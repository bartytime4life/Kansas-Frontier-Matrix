"""Validate fixture-only recursive traversal safety candidates.

The validator checks finite recursion guards and observation declarations. It
does not parse or execute SQL, connect to a database, inspect graph values,
resolve evidence, decide policy or review, release, or publish.
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

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/recursive_traversal_safety_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/recursive_traversal_safety_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "ASSESSMENT_INCOMPLETE",
    "CYCLE_POLICY_ABSTAIN",
    "DIALECT_PARITY_UNRESOLVED",
    "REFERENCE_UNRESOLVED",
    "TRAVERSAL_TRUNCATED",
}
ERROR_CODES = {"ASSESSMENT_ERROR", "CYCLE_POLICY_ERROR", "DEPTH_LIMIT_POLICY_ERROR", "OBSERVATION_ERROR"}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_DATABASE_EXECUTION",
    "NO_EVIDENCE_RESOLUTION",
    "NO_PUBLICATION_AUTHORITY",
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
    payload = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(candidate), key=lambda error: (list(error.absolute_path), str(error.validator)))
    return [Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path)) for error in errors[:100]]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _reference_unresolved(value: object) -> bool:
    return isinstance(value, Mapping) and value.get("resolution") == "UNRESOLVED"


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("recorded_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/recorded_at"))

    assessment_state = candidate["assessment_state"]
    if assessment_state == "INCOMPLETE":
        findings.add(Finding("ASSESSMENT_INCOMPLETE", "/assessment_state"))
    elif assessment_state == "ERROR":
        findings.add(Finding("ASSESSMENT_ERROR", "/assessment_state"))

    limitations = candidate["limitations"]
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    if not _canonical_strings(candidate["evidence_bundle_refs"]):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/evidence_bundle_refs"))

    query_definition = candidate["query_definition"]
    dialect = candidate["dialect_semantics"]
    identities = candidate["identity_fields"]
    guard = candidate["guard_profile"]
    observation = candidate["observation"]
    assert isinstance(dialect, Mapping)
    assert isinstance(identities, list)
    assert isinstance(guard, Mapping)
    assert isinstance(observation, Mapping)

    for value, field in (
        (query_definition, "/query_definition/resolution"),
        (dialect["dialect_profile"], "/dialect_semantics/dialect_profile/resolution"),
        (guard["termination_predicate"], "/guard_profile/termination_predicate/resolution"),
        (guard["depth_cap_justification"], "/guard_profile/depth_cap_justification/resolution"),
    ):
        if _reference_unresolved(value):
            findings.add(Finding("REFERENCE_UNRESOLVED", field))

    parity_state = dialect["parity_state"]
    parity_fixture_ref = dialect["parity_fixture_ref"]
    if parity_state == "UNRESOLVED":
        findings.add(Finding("DIALECT_PARITY_UNRESOLVED", "/dialect_semantics/parity_state"))
    elif parity_state == "MISMATCH":
        findings.add(Finding("DIALECT_PARITY_MISMATCH", "/dialect_semantics/parity_state"))
    elif parity_state == "SYNTHETIC_PARITY" and parity_fixture_ref is None:
        findings.add(Finding("PARITY_FIXTURE_MISSING", "/dialect_semantics/parity_fixture_ref"))
    elif parity_state == "SINGLE_DIALECT_DECLARED" and parity_fixture_ref is not None:
        findings.add(Finding("PARITY_FIXTURE_UNEXPECTED", "/dialect_semantics/parity_fixture_ref"))

    cycle_identities = guard["cycle_identity_fields"]
    if not _canonical_strings(identities):
        findings.add(Finding("IDENTITY_FIELDS_NOT_CANONICAL", "/identity_fields"))
    if not _canonical_strings(cycle_identities):
        findings.add(Finding("CYCLE_IDENTITY_FIELDS_NOT_CANONICAL", "/guard_profile/cycle_identity_fields"))
    if not set(cycle_identities) <= set(identities):
        findings.add(Finding("CYCLE_IDENTITY_OUTSIDE_TRAVERSAL_IDENTITY", "/guard_profile/cycle_identity_fields"))

    if guard["cycle_strategy"] == "NONE":
        findings.add(Finding("CYCLE_STRATEGY_REQUIRED", "/guard_profile/cycle_strategy"))
    if guard["on_cycle"] == "IGNORE":
        findings.add(Finding("CYCLE_IGNORE_DENIED", "/guard_profile/on_cycle"))
    if guard["on_depth_limit"] == "SILENT_PARTIAL":
        findings.add(Finding("SILENT_PARTIAL_DENIED", "/guard_profile/on_depth_limit"))

    state = observation["execution_state"]
    depth = observation["recursion_depth"]
    cycle_detected = observation["cycle_detected"]
    visited_nodes = observation["visited_nodes"]
    visited_edges = observation["visited_edges"]
    receipt_ref = observation["receipt_ref"]
    values = (depth, cycle_detected, visited_nodes, visited_edges, receipt_ref)

    if state == "ERROR":
        findings.add(Finding("OBSERVATION_ERROR", "/observation/execution_state"))
    elif state == "NOT_RUN":
        if any(value is not None for value in values):
            findings.add(Finding("NOT_RUN_OBSERVATION_PRESENT", "/observation"))
    else:
        if any(value is None for value in values):
            findings.add(Finding("EXECUTED_OBSERVATION_INCOMPLETE", "/observation"))
        else:
            assert isinstance(depth, int)
            assert isinstance(cycle_detected, bool)
            assert isinstance(visited_nodes, int)
            assert isinstance(visited_edges, int)
            if depth > guard["max_depth"]:
                findings.add(Finding("DEPTH_CAP_EXCEEDED", "/observation/recursion_depth"))
            if visited_nodes > guard["max_nodes"]:
                findings.add(Finding("NODE_CAP_EXCEEDED", "/observation/visited_nodes"))
            if visited_edges > guard["max_edges"]:
                findings.add(Finding("EDGE_CAP_EXCEEDED", "/observation/visited_edges"))

        if state == "COMPLETE" and cycle_detected is not False:
            findings.add(Finding("OBSERVATION_STATE_MISMATCH", "/observation/cycle_detected"))
        elif state == "DEPTH_LIMIT_REACHED":
            if cycle_detected is not False or depth != guard["max_depth"]:
                findings.add(Finding("OBSERVATION_STATE_MISMATCH", "/observation"))
            depth_policy = guard["on_depth_limit"]
            if depth_policy == "ABSTAIN":
                findings.add(Finding("TRAVERSAL_TRUNCATED", "/observation/execution_state"))
            elif depth_policy == "DENY":
                findings.add(Finding("DEPTH_LIMIT_POLICY_DENY", "/guard_profile/on_depth_limit"))
            elif depth_policy == "ERROR":
                findings.add(Finding("DEPTH_LIMIT_POLICY_ERROR", "/guard_profile/on_depth_limit"))
        elif state == "CYCLE_DETECTED":
            if cycle_detected is not True:
                findings.add(Finding("OBSERVATION_STATE_MISMATCH", "/observation/cycle_detected"))
            cycle_policy = guard["on_cycle"]
            if cycle_policy == "ABSTAIN":
                findings.add(Finding("CYCLE_POLICY_ABSTAIN", "/guard_profile/on_cycle"))
            elif cycle_policy == "DENY":
                findings.add(Finding("CYCLE_POLICY_DENY", "/guard_profile/on_cycle"))
            elif cycle_policy == "ERROR":
                findings.add(Finding("CYCLE_POLICY_ERROR", "/guard_profile/on_cycle"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if codes & ERROR_CODES:
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
        if value is None:
            target.pop(key, None)
        else:
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
        return [{"name": "fixture_manifest", "ok": False, "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})}}]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({"name": entry["name"], "ok": observed == expected, "expected": expected, "observed": observed})
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only recursive traversal safety assessments.")
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
