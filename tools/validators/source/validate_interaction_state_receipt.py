"""Validate fixture-only interaction state receipt candidates.

The validator operates on local declarations only. It does not open a browser,
execute script, submit a form, follow redirects, access a source, retain secret
values, create a SourceArtifact, write lifecycle data, release, or publish.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/interaction_state_receipt.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/source/interaction_state_receipt/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"ASSESSMENT_INCOMPLETE", "ASSESSMENT_UNKNOWN", "REDACTION_PROFILE_UNRESOLVED"}
BASE_OBLIGATIONS = {"DYNAMIC_RESULT_NOT_EVIDENCE", "NO_SENSITIVE_VALUE_RETENTION"}
KIND_ACTIONS = {
    "FORM_SUBMISSION": {"FORM_SUBMIT"},
    "BROWSER_SCRIPT": {"SCRIPT_EXECUTE"},
    "REDIRECT_CHAIN": {"REDIRECT"},
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


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
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs, parse_constant=_nonfinite, parse_float=_finite_float)
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
    encoded = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def canonical_identity(candidate: Mapping[str, object]) -> tuple[str, str]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("receipt_id", None)
    subject.pop("receipt_spec_hash", None)
    digest = canonical_hash(subject)
    return digest, "kfm:interaction-state-receipt:" + digest.removeprefix("sha256:")[:24]


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
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


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    expected_hash, expected_id = canonical_identity(candidate)
    if candidate.get("receipt_spec_hash") != expected_hash:
        findings.add(Finding("RECEIPT_SPEC_HASH_MISMATCH", "/receipt_spec_hash"))
    if candidate.get("receipt_id") != expected_id:
        findings.add(Finding("RECEIPT_ID_MISMATCH", "/receipt_id"))
    if not _is_utc(candidate.get("recorded_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/recorded_at"))

    interaction = candidate["interaction"]
    redaction = candidate["redaction"]
    result = candidate["result"]
    assessment = candidate["assessment"]
    assert isinstance(interaction, Mapping) and isinstance(redaction, Mapping) and isinstance(result, Mapping) and isinstance(assessment, Mapping)
    steps = interaction["steps"]
    assert isinstance(steps, list)

    for field, value in (("sensitive_state_classes", interaction["sensitive_state_classes"]), ("redacted_classes", redaction["redacted_classes"]), ("failure_reason_codes", result["failure_reason_codes"]), ("obligations", assessment["obligations"]), ("review_record_refs", assessment["review_record_refs"])):
        if not _canonical_strings(value):
            findings.add(Finding("ARRAY_NOT_CANONICAL", f"/{'interaction' if field == 'sensitive_state_classes' else 'redaction' if field == 'redacted_classes' else 'result' if field == 'failure_reason_codes' else 'assessment'}/{field}"))

    if [step["index"] for step in steps] != list(range(len(steps))):
        findings.add(Finding("STEP_INDEX_SEQUENCE_INVALID", "/interaction/steps"))
    for left, right in zip(steps, steps[1:]):
        if left["state_after_digest"] is not None and left["state_after_digest"] != right["state_before_digest"]:
            findings.add(Finding("STEP_STATE_CHAIN_MISMATCH", f"/interaction/steps/{right['index']}/state_before_digest"))
    if any(step["outcome"] != "SUCCEEDED" for step in steps[:-1]):
        findings.add(Finding("TERMINAL_STEP_NOT_LAST", "/interaction/steps"))

    actions = {step["action"] for step in steps}
    kind = interaction["kind"]
    if kind in KIND_ACTIONS and not KIND_ACTIONS[str(kind)] <= actions:
        findings.add(Finding("INTERACTION_KIND_ACTION_MISMATCH", "/interaction/kind"))
    if kind == "COMPOSITE" and len(actions & {"FORM_SUBMIT", "SCRIPT_EXECUTE", "REDIRECT"}) < 2:
        findings.add(Finding("INTERACTION_KIND_ACTION_MISMATCH", "/interaction/kind"))

    sensitive = interaction["sensitive_state_classes"]
    redacted = redaction["redacted_classes"]
    if sensitive != redacted:
        findings.add(Finding("REDACTION_COVERAGE_MISMATCH", "/redaction/redacted_classes"))
    profile = redaction["profile"]
    assert isinstance(profile, Mapping)
    if sensitive:
        if profile["resolution"] != "RESOLVED":
            findings.add(Finding("SENSITIVE_REDACTION_PROFILE_REQUIRED", "/redaction/profile/resolution"))
        if redaction["redaction_receipt_ref"] is None:
            findings.add(Finding("SENSITIVE_REDACTION_RECEIPT_REQUIRED", "/redaction/redaction_receipt_ref"))
    elif profile["resolution"] == "UNRESOLVED":
        findings.add(Finding("REDACTION_PROFILE_UNRESOLVED", "/redaction/profile/resolution"))

    state = assessment["state"]
    if state == "INCOMPLETE":
        findings.add(Finding("ASSESSMENT_INCOMPLETE", "/assessment/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("ASSESSMENT_UNKNOWN", "/assessment/state"))

    obligations = set(assessment["obligations"])
    required = set(BASE_OBLIGATIONS)
    if sensitive:
        required.add("REDACTION_REVIEW_REQUIRED")
    if result["outcome"] == "CAPTURED":
        required.add("SOURCE_ARTIFACT_HANDOFF_REQUIRED")
    if not required <= obligations:
        findings.add(Finding("REQUIRED_OBLIGATION_MISSING", "/assessment/obligations"))

    last = steps[-1]
    if result["outcome"] == "CAPTURED":
        coherent = (
            last["action"] == "CAPTURE"
            and last["outcome"] == "SUCCEEDED"
            and result["capture_artifact_ref"] is not None
            and result["capture_artifact_digest"] is not None
            and result["capture_state"] in {"SOURCE_CAPTURE_CANDIDATE", "QUARANTINE_CANDIDATE"}
            and result["failure_reason_codes"] == []
        )
        if not coherent:
            findings.add(Finding("CAPTURE_RESULT_INCOHERENT", "/result"))
    else:
        coherent = (
            last["outcome"] == result["outcome"]
            and result["capture_artifact_ref"] is None
            and result["capture_artifact_digest"] is None
            and result["capture_state"] == "NOT_APPLICABLE"
            and bool(result["failure_reason_codes"])
        )
        if not coherent:
            findings.add(Finding("NON_CAPTURE_RESULT_INCOHERENT", "/result"))
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
        target[key] = None if value is None else _merge_patch(target.get(key), value)
    return target


def _apply_mutation(candidate: dict[str, object], mutation: object) -> None:
    interaction = candidate["interaction"]
    redaction = candidate["redaction"]
    result = candidate["result"]
    assessment = candidate["assessment"]
    assert isinstance(interaction, dict) and isinstance(redaction, dict) and isinstance(result, dict) and isinstance(assessment, dict)
    steps = interaction["steps"]
    assert isinstance(steps, list)
    if mutation == "step_index_gap":
        steps[1]["index"] = 3
    elif mutation == "state_chain_mismatch":
        steps[1]["state_before_digest"] = "sha256:" + "9" * 64
    elif mutation == "form_action_missing":
        steps[1]["action"] = "WAIT_FOR_STATE"
    elif mutation == "sensitive_coverage_mismatch":
        redaction["redacted_classes"] = list(redaction["redacted_classes"][:-1])
    elif mutation == "sensitive_receipt_missing":
        redaction["redaction_receipt_ref"] = None
    elif mutation == "capture_obligation_missing":
        assessment["obligations"] = [item for item in assessment["obligations"] if item != "SOURCE_ARTIFACT_HANDOFF_REQUIRED"]
    elif mutation == "capture_result_incoherent":
        steps[-1]["outcome"] = "FAILED"
    elif mutation == "terminal_step_not_last":
        steps[0]["outcome"] = "FAILED"


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    _apply_mutation(candidate, entry.get("mutation"))
    candidate["receipt_spec_hash"], candidate["receipt_id"] = canonical_identity(candidate)
    if entry.get("tamper") == "receipt_hash":
        candidate["receipt_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest() -> list[tuple[str, str, list[str]]]:
    manifest, findings = load_json_object(FIXTURE_PATH)
    if manifest is None or findings:
        raise ValueError("fixture manifest is unreadable")
    results: list[tuple[str, str, list[str]]] = []
    for entry in manifest["cases"]:
        assert isinstance(entry, Mapping)
        result = validate_candidate(materialize_fixture_case(manifest, entry))
        expected = entry["expected"]
        assert isinstance(expected, Mapping)
        name = str(entry["name"])
        if result.outcome != expected["outcome"] or result.codes != expected["codes"]:
            raise AssertionError(f"{name}: expected {expected}, got {result.outcome} {result.codes}")
        results.append((name, result.outcome, result.codes))
    return results


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        for name, outcome, codes in validate_fixture_manifest():
            print(json.dumps({"case": name, "codes": codes, "outcome": outcome}, sort_keys=True, separators=(",", ":")))
        return 0
    if not args.files:
        parser.error("provide files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        candidate, findings = load_json_object(path)
        result = ValidationResult("ERROR", tuple(findings)) if candidate is None else validate_candidate(candidate)
        print(json.dumps({"file": path.name, "codes": result.codes, "outcome": result.outcome}, sort_keys=True, separators=(",", ":")))
        rc = max(rc, 0 if result.outcome == "PASS" else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
