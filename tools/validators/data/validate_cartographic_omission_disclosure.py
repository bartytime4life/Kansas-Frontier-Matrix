"""Validate fixture-only cartographic omission disclosure candidates.

The validator proves closed shape, deterministic identity, canonical entry
ordering, and local disclosure coherence. It does not resolve references,
determine materiality, alter a layer, evaluate policy or review, render a map,
promote, release, deploy, publish, or authorize public use.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/cartographic_omission_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/data/cartographic_omission_disclosure/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "ASSESSMENT_INCOMPLETE",
    "ASSESSMENT_UNKNOWN",
    "EVIDENCE_SCOPE_UNRESOLVED",
    "MAP_PURPOSE_UNRESOLVED",
    "MATERIALITY_UNKNOWN",
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
        Finding(
            "SCHEMA_INVALID",
            "/" + "/".join(str(part) for part in error.absolute_path),
        )
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


def _canonical_refs(value: object) -> bool:
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

    map_purpose = candidate.get("map_purpose")
    evidence_scope = candidate.get("evidence_scope")
    if isinstance(map_purpose, Mapping) and map_purpose.get("resolution") == "UNRESOLVED":
        findings.add(Finding("MAP_PURPOSE_UNRESOLVED", "/map_purpose/resolution"))
    if isinstance(evidence_scope, Mapping) and evidence_scope.get("resolution") == "UNRESOLVED":
        findings.add(Finding("EVIDENCE_SCOPE_UNRESOLVED", "/evidence_scope/resolution"))

    entries = candidate.get("entries")
    assert isinstance(entries, list)
    ids = [entry.get("omission_id") for entry in entries if isinstance(entry, Mapping)]
    if ids != sorted(ids):
        findings.add(Finding("ENTRIES_NOT_CANONICAL", "/entries"))
    if len(ids) != len(set(ids)):
        findings.add(Finding("DUPLICATE_OMISSION_ID", "/entries"))

    subject_actions: list[tuple[object, object]] = []
    has_unknown_materiality = False
    for index, entry in enumerate(entries):
        assert isinstance(entry, Mapping)
        subject_actions.append((entry.get("subject_ref"), entry.get("action")))
        for name in ("evidence_refs", "policy_decision_refs", "review_record_refs"):
            if not _canonical_refs(entry.get(name)):
                findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/entries/{index}/{name}"))
        if entry.get("materiality") == "UNKNOWN":
            has_unknown_materiality = True
            findings.add(Finding("MATERIALITY_UNKNOWN", f"/entries/{index}/materiality"))
        if entry.get("materiality") == "MATERIAL" and entry.get("public_disclosure") == "NONE":
            findings.add(Finding("MATERIAL_OMISSION_UNDISCLOSED", f"/entries/{index}/public_disclosure"))
        if entry.get("action") == "SIMPLIFY" and entry.get("transform_receipt_ref") is None:
            findings.add(Finding("SIMPLIFICATION_RECEIPT_REQUIRED", f"/entries/{index}/transform_receipt_ref"))
        if entry.get("reason_code") in {"RIGHTS", "SENSITIVITY"} and not entry.get("policy_decision_refs"):
            findings.add(Finding("POLICY_REFERENCE_REQUIRED", f"/entries/{index}/policy_decision_refs"))
    if len(subject_actions) != len(set(subject_actions)):
        findings.add(Finding("DUPLICATE_SUBJECT_ACTION", "/entries"))

    assessment = candidate.get("assessment")
    assert isinstance(assessment, Mapping)
    state = assessment.get("state")
    known_gap = assessment.get("known_undisclosed_material_count")
    if state == "COMPLETE_FOR_DECLARED_SCOPE":
        if known_gap != 0 or has_unknown_materiality:
            findings.add(Finding("COMPLETENESS_CLAIM_INCOHERENT", "/assessment"))
    elif state == "INCOMPLETE":
        if known_gap == 0 and not has_unknown_materiality:
            findings.add(Finding("ASSESSMENT_STATE_INCOHERENT", "/assessment"))
        else:
            findings.add(Finding("ASSESSMENT_INCOMPLETE", "/assessment/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("ASSESSMENT_UNKNOWN", "/assessment/state"))
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
    parser = argparse.ArgumentParser(description="Validate fixture-only cartographic omission disclosures.")
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
