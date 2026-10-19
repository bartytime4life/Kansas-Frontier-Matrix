"""Validate fixture-only Atlas-card delta assessment candidates."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/atlas_card_delta_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/atlas_card_delta_assessment/cases.json"
SCOPE = "governance.atlas_card_delta_assessment"
CARD_FIELDS = (
    "candidate_authority_families",
    "dependency_ids",
    "evidence_refs",
    "normalized_statement",
    "spec_hash",
    "stable_id",
    "truth_label",
)
COLLECTION_FIELDS = (
    "changed_fields",
    "evidence_refs_added",
    "evidence_refs_removed",
    "dependency_ids_added",
    "dependency_ids_removed",
    "candidate_authority_families_added",
    "candidate_authority_families_removed",
)
DENY_CODES = {
    "ATLAS_IDENTITY_CHANGED",
    "AUTHORITY_EFFECT_OVERREACH",
    "CARD_SPEC_HASH_NOT_CHANGED",
    "COLLECTION_NOT_SORTED_UNIQUE",
    "DELTA_AUTHORITY_FAMILIES_ADDED_MISMATCH",
    "DELTA_AUTHORITY_FAMILIES_REMOVED_MISMATCH",
    "DELTA_CHANGED_FIELDS_MISMATCH",
    "DELTA_DEPENDENCIES_ADDED_MISMATCH",
    "DELTA_DEPENDENCIES_REMOVED_MISMATCH",
    "DELTA_ENDPOINTS_MISSING",
    "DELTA_EVIDENCE_ADDED_MISMATCH",
    "DELTA_EVIDENCE_REMOVED_MISMATCH",
    "DELTA_TRANSITION_MISMATCH",
    "DELTA_TRUTH_TRANSITION_MISMATCH",
    "SCHEMA_INVALID",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]


class InputError(ValueError):
    pass


def _load_json(path: Path) -> Any:
    try:
        if path.is_symlink() or not path.is_file():
            raise InputError("not a regular file")
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError) as exc:
        raise InputError("unsafe JSON input") from exc


_SCHEMA_VALIDATOR = Draft202012Validator(
    _load_json(SCHEMA_PATH), format_checker=FormatChecker()
)


def _schema_findings(value: object) -> set[Finding]:
    findings: set[Finding] = set()
    for error in _SCHEMA_VALIDATOR.iter_errors(value):
        path = "$" + "".join(
            f"[{part}]" if isinstance(part, int) else f".{part}"
            for part in error.absolute_path
        )
        findings.add(Finding("SCHEMA_INVALID", path))
    return findings


def _sorted_unique(value: object) -> bool:
    return isinstance(value, list) and value == sorted(value) and len(value) == len(set(value))


def _values(card: Mapping[str, Any] | None, field: str) -> list[str]:
    if card is None:
        return []
    value = card.get(field, [])
    return list(value) if isinstance(value, list) else []


def _transition(before: Mapping[str, Any] | None, after: Mapping[str, Any] | None) -> str:
    if before is None and after is not None:
        return "ADDED"
    if before is not None and after is None:
        return "REMOVED"
    if before == after:
        return "UNCHANGED"
    return "MODIFIED"


def _changed_fields(before: Mapping[str, Any] | None, after: Mapping[str, Any] | None) -> list[str]:
    if before is None or after is None:
        return list(CARD_FIELDS)
    return sorted(field for field in CARD_FIELDS if before.get(field) != after.get(field))


def _difference(left: list[str], right: list[str]) -> list[str]:
    return sorted(set(left) - set(right))


def evaluate_candidate(candidate: object) -> ValidationResult:
    findings = _schema_findings(candidate)
    if findings or not isinstance(candidate, dict):
        return ValidationResult("DENY", tuple(sorted(findings)))

    before = candidate["before"]
    after = candidate["after"]
    delta = candidate["declared_delta"]

    for card_name, card in (("before", before), ("after", after)):
        if isinstance(card, dict):
            for field in ("candidate_authority_families", "dependency_ids", "evidence_refs"):
                if not _sorted_unique(card[field]):
                    findings.add(Finding("COLLECTION_NOT_SORTED_UNIQUE", f"$.{card_name}.{field}"))
    for field in COLLECTION_FIELDS:
        if not _sorted_unique(delta[field]):
            findings.add(Finding("COLLECTION_NOT_SORTED_UNIQUE", f"$.declared_delta.{field}"))
    if not _sorted_unique(candidate["source_errors"]):
        findings.add(Finding("COLLECTION_NOT_SORTED_UNIQUE", "$.source_errors"))

    if before is None and after is None:
        findings.add(Finding("DELTA_ENDPOINTS_MISSING", "$.before"))

    if isinstance(before, dict) and isinstance(after, dict):
        if before["stable_id"] != after["stable_id"]:
            findings.add(Finding("ATLAS_IDENTITY_CHANGED", "$.after.stable_id"))
        semantic_changed = any(
            before[field] != after[field] for field in CARD_FIELDS if field != "spec_hash"
        )
        if semantic_changed and before["spec_hash"] == after["spec_hash"]:
            findings.add(Finding("CARD_SPEC_HASH_NOT_CHANGED", "$.after.spec_hash"))

    expected_transition = _transition(before, after)
    if delta["transition"] != expected_transition:
        findings.add(Finding("DELTA_TRANSITION_MISMATCH", "$.declared_delta.transition"))

    expected_changed = _changed_fields(before, after)
    if delta["changed_fields"] != expected_changed:
        findings.add(Finding("DELTA_CHANGED_FIELDS_MISMATCH", "$.declared_delta.changed_fields"))

    comparisons = (
        (
            "evidence_refs_added",
            _difference(_values(after, "evidence_refs"), _values(before, "evidence_refs")),
            "DELTA_EVIDENCE_ADDED_MISMATCH",
        ),
        (
            "evidence_refs_removed",
            _difference(_values(before, "evidence_refs"), _values(after, "evidence_refs")),
            "DELTA_EVIDENCE_REMOVED_MISMATCH",
        ),
        (
            "dependency_ids_added",
            _difference(_values(after, "dependency_ids"), _values(before, "dependency_ids")),
            "DELTA_DEPENDENCIES_ADDED_MISMATCH",
        ),
        (
            "dependency_ids_removed",
            _difference(_values(before, "dependency_ids"), _values(after, "dependency_ids")),
            "DELTA_DEPENDENCIES_REMOVED_MISMATCH",
        ),
        (
            "candidate_authority_families_added",
            _difference(
                _values(after, "candidate_authority_families"),
                _values(before, "candidate_authority_families"),
            ),
            "DELTA_AUTHORITY_FAMILIES_ADDED_MISMATCH",
        ),
        (
            "candidate_authority_families_removed",
            _difference(
                _values(before, "candidate_authority_families"),
                _values(after, "candidate_authority_families"),
            ),
            "DELTA_AUTHORITY_FAMILIES_REMOVED_MISMATCH",
        ),
    )
    for field, expected, code in comparisons:
        if delta[field] != expected:
            findings.add(Finding(code, f"$.declared_delta.{field}"))

    expected_truth = {
        "from": before["truth_label"] if isinstance(before, dict) else None,
        "to": after["truth_label"] if isinstance(after, dict) else None,
    }
    if delta["truth_transition"] != expected_truth:
        findings.add(Finding("DELTA_TRUTH_TRANSITION_MISMATCH", "$.declared_delta.truth_transition"))

    if any(candidate["authority_effects"].values()):
        findings.add(Finding("AUTHORITY_EFFECT_OVERREACH", "$.authority_effects"))

    if candidate["source_errors"]:
        findings.add(Finding("SOURCE_INPUT_ERROR", "$.source_errors"))

    if isinstance(after, dict):
        if after["truth_label"] in {"UNKNOWN", "NEEDS_VERIFICATION"}:
            findings.add(Finding("TARGET_TRUTH_UNRESOLVED", "$.after.truth_label"))
        if after["truth_label"] == "CONFIRMED" and not after["evidence_refs"]:
            findings.add(Finding("CONFIRMED_WITHOUT_EVIDENCE", "$.after.evidence_refs"))

    if any(item.code == "SOURCE_INPUT_ERROR" for item in findings):
        outcome = "ERROR"
    elif any(item.code in DENY_CODES for item in findings):
        outcome = "DENY"
    elif findings:
        outcome = "ABSTAIN"
    else:
        outcome = "PASS"
    return ValidationResult(outcome, tuple(sorted(findings)))


def run_fixture_suite() -> tuple[bool, Mapping[str, Any]]:
    suite = _load_json(FIXTURE_PATH)
    if not isinstance(suite, dict) or not isinstance(suite.get("cases"), list):
        raise InputError("fixture suite shape invalid")
    output: list[dict[str, Any]] = []
    ok = True
    for case in suite["cases"]:
        if not isinstance(case, dict):
            raise InputError("fixture case shape invalid")
        result = evaluate_candidate(case.get("candidate"))
        actual_codes = [finding.code for finding in result.findings]
        expected = case.get("expected", {})
        case_ok = (
            isinstance(expected, dict)
            and result.outcome == expected.get("outcome")
            and actual_codes == expected.get("finding_codes")
        )
        ok = ok and case_ok
        output.append(
            {
                "actual_findings": actual_codes,
                "actual_outcome": result.outcome,
                "case_id": case.get("case_id"),
                "expected_findings": expected.get("finding_codes") if isinstance(expected, dict) else None,
                "expected_outcome": expected.get("outcome") if isinstance(expected, dict) else None,
                "ok": case_ok,
            }
        )
    return ok, {"cases": output, "ok": ok, "scope": SCOPE}


def _serialize(result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures == bool(args.input):
        parser.error("provide exactly one of --fixtures or --input")
    try:
        if args.fixtures:
            ok, report = run_fixture_suite()
            print(json.dumps(report, sort_keys=True, separators=(",", ":")))
            return 0 if ok else 1
        result = evaluate_candidate(_load_json(args.input))
        print(_serialize(result))
        return 0 if result.outcome == "PASS" else (2 if result.outcome == "ERROR" else 1)
    except InputError as exc:
        print(
            json.dumps(
                {
                    "authority": "NONE",
                    "findings": [{"code": "INPUT_ERROR", "path": "$"}],
                    "outcome": "ERROR",
                    "scope": SCOPE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
