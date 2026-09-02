"""Validate fixture-only participatory planning weight receipt candidates.

This module proves closed shape, deterministic identity, canonical ordering,
per-group normalization, and local declaration coherence. It does not collect
participants, resolve evidence, infer or aggregate preferences, compute a
planning score, determine consensus, evaluate policy or review, promote,
release, deploy, publish, or authorize public use.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/participatory_planning_weight_receipt.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/participatory_planning_weight_receipt/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "CONSENT_INCOMPLETE",
    "CONSENT_UNKNOWN",
    "DISSENT_UNKNOWN",
    "EVIDENCE_UNRESOLVED",
    "FACILITATION_INCOMPLETE",
    "FACILITATION_UNKNOWN",
    "SENSITIVITY_ANALYSIS_INCOMPLETE",
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


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
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


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    planning_scope = candidate["planning_scope"]
    method = candidate["method"]
    criteria = candidate["criteria"]
    weight_sets = candidate["stakeholder_weight_sets"]
    deliberation = candidate["deliberation"]
    governance = candidate["governance"]
    assert isinstance(planning_scope, Mapping)
    assert isinstance(method, Mapping)
    assert isinstance(criteria, list)
    assert isinstance(weight_sets, list)
    assert isinstance(deliberation, Mapping)
    assert isinstance(governance, Mapping)

    targets = planning_scope.get("target_population_refs")
    if not _canonical_strings(targets):
        findings.add(Finding("TARGET_POPULATIONS_NOT_CANONICAL", "/planning_scope/target_population_refs"))

    criterion_ids = [
        item.get("criterion_id") for item in criteria if isinstance(item, Mapping)
    ]
    if criterion_ids != sorted(criterion_ids) or len(criterion_ids) != len(set(criterion_ids)):
        findings.add(Finding("CRITERIA_NOT_CANONICAL", "/criteria"))
    criterion_set = set(criterion_ids)

    group_refs = [
        item.get("group_ref") for item in weight_sets if isinstance(item, Mapping)
    ]
    if len(group_refs) != len(set(group_refs)):
        findings.add(Finding("DUPLICATE_STAKEHOLDER_GROUP_REF", "/stakeholder_weight_sets"))
    elif group_refs != sorted(group_refs):
        findings.add(Finding("STAKEHOLDER_GROUPS_NOT_CANONICAL", "/stakeholder_weight_sets"))

    for index, weight_set in enumerate(weight_sets):
        assert isinstance(weight_set, Mapping)
        weights = weight_set["weights"]
        assert isinstance(weights, list)
        weight_ids = [
            item.get("criterion_id") for item in weights if isinstance(item, Mapping)
        ]
        if weight_ids != sorted(weight_ids):
            findings.add(Finding("WEIGHTS_NOT_CANONICAL", f"/stakeholder_weight_sets/{index}/weights"))
        if set(weight_ids) != criterion_set or len(weight_ids) != len(criterion_ids):
            findings.add(Finding("WEIGHT_CRITERIA_MISMATCH", f"/stakeholder_weight_sets/{index}/weights"))
        total = sum(
            int(item["basis_points"])
            for item in weights
            if isinstance(item, Mapping) and isinstance(item.get("basis_points"), int)
        )
        if total != 10000:
            findings.add(Finding("WEIGHT_SUM_INVALID", f"/stakeholder_weight_sets/{index}/weights"))

        consent_state = weight_set.get("consent_state")
        consent_ref = weight_set.get("consent_ref")
        if consent_state == "COMPLETE" and consent_ref is None:
            findings.add(Finding("CONSENT_REFERENCE_REQUIRED", f"/stakeholder_weight_sets/{index}/consent_ref"))
        elif consent_state == "INCOMPLETE":
            findings.add(Finding("CONSENT_INCOMPLETE", f"/stakeholder_weight_sets/{index}/consent_state"))
        elif consent_state == "UNKNOWN":
            findings.add(Finding("CONSENT_UNKNOWN", f"/stakeholder_weight_sets/{index}/consent_state"))
        if consent_state != "COMPLETE" and consent_ref is not None:
            findings.add(Finding("CONSENT_REFERENCE_INCOHERENT", f"/stakeholder_weight_sets/{index}/consent_ref"))

        dissent_state = weight_set.get("dissent_state")
        dissent_ref = weight_set.get("dissent_summary_ref")
        if dissent_state == "RECORDED" and dissent_ref is None:
            findings.add(Finding("DISSENT_SUMMARY_REQUIRED", f"/stakeholder_weight_sets/{index}/dissent_summary_ref"))
        elif dissent_state == "NONE" and dissent_ref is not None:
            findings.add(Finding("DISSENT_SUMMARY_UNEXPECTED", f"/stakeholder_weight_sets/{index}/dissent_summary_ref"))
        elif dissent_state == "UNKNOWN":
            findings.add(Finding("DISSENT_UNKNOWN", f"/stakeholder_weight_sets/{index}/dissent_state"))

    facilitation_state = method.get("facilitation_state")
    facilitation_ref = method.get("facilitation_record_ref")
    if facilitation_state == "DOCUMENTED" and facilitation_ref is None:
        findings.add(Finding("FACILITATION_REFERENCE_REQUIRED", "/method/facilitation_record_ref"))
    elif facilitation_state == "INCOMPLETE":
        findings.add(Finding("FACILITATION_INCOMPLETE", "/method/facilitation_state"))
    elif facilitation_state == "UNKNOWN":
        findings.add(Finding("FACILITATION_UNKNOWN", "/method/facilitation_state"))
    if facilitation_state != "DOCUMENTED" and facilitation_ref is not None:
        findings.add(Finding("FACILITATION_REFERENCE_INCOHERENT", "/method/facilitation_record_ref"))

    sensitivity_state = method.get("sensitivity_analysis_state")
    sensitivity_ref = method.get("sensitivity_analysis_ref")
    intended_output = planning_scope.get("intended_output")
    ranking_output = intended_output in {"SITE_SUITABILITY", "ROUTE_SUITABILITY"}
    if sensitivity_state == "COMPLETE" and sensitivity_ref is None:
        findings.add(Finding("SENSITIVITY_ANALYSIS_REFERENCE_REQUIRED", "/method/sensitivity_analysis_ref"))
    elif sensitivity_state == "NOT_APPLICABLE" and sensitivity_ref is not None:
        findings.add(Finding("SENSITIVITY_ANALYSIS_REFERENCE_UNEXPECTED", "/method/sensitivity_analysis_ref"))
    if ranking_output and sensitivity_state != "COMPLETE":
        findings.add(Finding("SENSITIVITY_ANALYSIS_INCOMPLETE", "/method/sensitivity_analysis_state"))

    conflict_refs = deliberation.get("conflict_summary_refs")
    if not _canonical_strings(conflict_refs):
        findings.add(Finding("CONFLICT_REFS_NOT_CANONICAL", "/deliberation/conflict_summary_refs"))
    conflict_count = deliberation.get("unresolved_conflict_count")
    if conflict_count and not conflict_refs:
        findings.add(Finding("CONFLICT_SUMMARY_REQUIRED", "/deliberation/conflict_summary_refs"))
    if conflict_count == 0 and conflict_refs:
        findings.add(Finding("CONFLICT_SUMMARY_UNEXPECTED", "/deliberation/conflict_summary_refs"))
    if conflict_count and all(
        isinstance(item, Mapping) and item.get("dissent_state") == "NONE"
        for item in weight_sets
    ):
        findings.add(Finding("UNRESOLVED_CONFLICT_WITHOUT_DISSENT", "/deliberation"))
    if deliberation.get("consensus_posture") != "NO_CONSENSUS_ASSERTED":
        findings.add(Finding("CONSENSUS_CLAIM_DENIED", "/deliberation/consensus_posture"))
    if len(weight_sets) > 1 and not deliberation.get("group_comparison_disclosed"):
        findings.add(Finding("GROUP_COMPARISON_DISCLOSURE_REQUIRED", "/deliberation/group_comparison_disclosed"))

    if governance.get("evidence_resolution") == "UNRESOLVED":
        findings.add(Finding("EVIDENCE_UNRESOLVED", "/governance/evidence_resolution"))
    if governance.get("policy_state") not in {"PENDING", "NOT_EVALUATED"}:
        findings.add(Finding("POLICY_OUTCOME_OVERCLAIM", "/governance/policy_state"))
    if governance.get("review_state") != "PENDING":
        findings.add(Finding("REVIEW_STATE_OVERCLAIM", "/governance/review_state"))
    if governance.get("release_state") != "NOT_RELEASED":
        findings.add(Finding("RELEASE_STATE_OVERCLAIM", "/governance/release_state"))

    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _resolve_pointer(root: object, path: str) -> tuple[object, str]:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in path.split("/")[1:]]
    if not parts:
        raise ValueError("root replacement is not supported")
    target = root
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    return target, parts[-1]


def _apply_mutations(candidate: dict[str, object], mutations: object) -> None:
    assert isinstance(mutations, list)
    for mutation in mutations:
        assert isinstance(mutation, Mapping)
        target, key = _resolve_pointer(candidate, str(mutation["path"]))
        if mutation.get("op") == "reverse":
            value = target[int(key)] if isinstance(target, list) else target[key]
            assert isinstance(value, list)
            value.reverse()
        else:
            value = copy.deepcopy(mutation.get("value"))
            if isinstance(target, list):
                target[int(key)] = value
            else:
                target[key] = value


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = copy.deepcopy(manifest["base_candidate"])
    assert isinstance(candidate, dict)
    _apply_mutations(candidate, entry.get("mutations", []))
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
            "observed": {
                "outcome": "ERROR",
                "codes": sorted({item.code for item in load_findings}),
            },
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
    parser = argparse.ArgumentParser(
        description="Validate fixture-only participatory planning weight receipt candidates."
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
    if candidate is None:
        result = ValidationResult("ERROR", tuple(sorted(findings)))
    else:
        result = validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
