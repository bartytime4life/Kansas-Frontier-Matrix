"""Validate fixture-only cartographic communication-risk assessments.

The validator checks closed shape, deterministic content identity, five-axis
review completeness, adjacent opaque assessment links, mitigation references,
review declarations, and UTC timestamps. It never renders or inspects a map,
resolves evidence, decides policy or review, or grants release or publication
authority.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/cartographic_communication_risk_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/map/cartographic_communication_risk_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
AXIS_ORDER = ("SELECTION", "FRAMING", "SCALE", "SYMBOLOGY", "OMISSION")
EXPECTED_CODES = {
    "SELECTION": {
        "ACCEPTABLE": "SELECTION_SCOPE_ACCEPTABLE",
        "MITIGATED": "SELECTION_RISK_MITIGATED",
        "UNRESOLVED": "SELECTION_RISK_UNRESOLVED",
        "MISLEADING": "SELECTION_RISK_MISLEADING",
    },
    "FRAMING": {
        "ACCEPTABLE": "FRAMING_CONTEXT_ACCEPTABLE",
        "MITIGATED": "FRAMING_RISK_MITIGATED",
        "UNRESOLVED": "FRAMING_RISK_UNRESOLVED",
        "MISLEADING": "FRAMING_RISK_MISLEADING",
    },
    "SCALE": {
        "ACCEPTABLE": "SCALE_SUPPORT_ACCEPTABLE",
        "MITIGATED": "SCALE_RISK_MITIGATED",
        "UNRESOLVED": "SCALE_RISK_UNRESOLVED",
        "MISLEADING": "SCALE_RISK_MISLEADING",
    },
    "SYMBOLOGY": {
        "ACCEPTABLE": "SYMBOLOGY_EVIDENCE_MATCH_ACCEPTABLE",
        "MITIGATED": "SYMBOLOGY_RISK_MITIGATED",
        "UNRESOLVED": "SYMBOLOGY_RISK_UNRESOLVED",
        "MISLEADING": "SYMBOLOGY_RISK_MISLEADING",
    },
    "OMISSION": {
        "ACCEPTABLE": "OMISSION_DISCLOSURE_ACCEPTABLE",
        "MITIGATED": "OMISSION_RISK_MITIGATED",
        "UNRESOLVED": "OMISSION_RISK_UNRESOLVED",
        "MISLEADING": "OMISSION_RISK_MISLEADING",
    },
}
ABSTAIN_CODES = {
    "CONSEQUENCE_UNRESOLVED",
    "REVIEW_PENDING",
    "REVIEW_UNKNOWN",
    "SUPPORTING_ASSESSMENT_UNRESOLVED",
    *(code for values in EXPECTED_CODES.values() for state, code in values.items() if state == "UNRESOLVED"),
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


class UnpairedSurrogateError(ValueError):
    """Raised when text cannot be represented as Unicode scalar values."""


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


def _contains_surrogate(value: object) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if isinstance(value, Mapping):
        return any(_contains_surrogate(key) or _contains_surrogate(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


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
    if _contains_surrogate(value):
        return None, [Finding("JSON_UNPAIRED_SURROGATE", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    if _contains_surrogate(value):
        raise UnpairedSurrogateError
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


def _support_findings(support: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    for name, raw_link in support.items():
        assert isinstance(raw_link, Mapping)
        state = raw_link.get("state")
        ref = raw_link.get("ref")
        digest = raw_link.get("digest")
        path = f"/supporting_assessments/{name}"
        if state == "RESOLVED" and (ref is None or digest is None):
            findings.add(Finding("SUPPORTING_ASSESSMENT_BINDING_REQUIRED", path))
        elif state == "UNRESOLVED":
            findings.add(Finding("SUPPORTING_ASSESSMENT_UNRESOLVED", path + "/state"))
        elif state == "NOT_APPLICABLE" and (ref is not None or digest is not None):
            findings.add(Finding("SUPPORTING_ASSESSMENT_BINDING_PROHIBITED", path))
    return findings


def _axis_findings(axes: object) -> set[Finding]:
    findings: set[Finding] = set()
    assert isinstance(axes, list)
    names = [item.get("axis") for item in axes if isinstance(item, Mapping)]
    if tuple(names) != AXIS_ORDER:
        findings.add(Finding("AXIS_SET_NOT_CANONICAL", "/risk_review/axes"))
    for index, raw_axis in enumerate(axes):
        assert isinstance(raw_axis, Mapping)
        name = raw_axis.get("axis")
        state = raw_axis.get("state")
        code = raw_axis.get("finding_code")
        refs = raw_axis.get("mitigation_refs")
        path = f"/risk_review/axes/{index}"
        if not _canonical_strings(refs):
            findings.add(Finding("ARRAY_NOT_CANONICAL", path + "/mitigation_refs"))
        assert isinstance(name, str) and isinstance(state, str) and isinstance(refs, list)
        if code != EXPECTED_CODES[name][state]:
            findings.add(Finding("AXIS_FINDING_CODE_INCOHERENT", path + "/finding_code"))
        if state == "MITIGATED" and not refs:
            findings.add(Finding("MITIGATION_REFERENCE_REQUIRED", path + "/mitigation_refs"))
        elif state != "MITIGATED" and refs:
            findings.add(Finding("MITIGATION_REFERENCE_PROHIBITED", path + "/mitigation_refs"))
        if state in {"UNRESOLVED", "MISLEADING"}:
            findings.add(Finding(EXPECTED_CODES[name][state], path + "/state"))
    return findings


def _review_findings(review: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    consequence = review.get("consequence")
    state = review.get("review_state")
    refs = review.get("review_record_refs")
    summary = review.get("communication_summary")
    if consequence == "UNRESOLVED":
        findings.add(Finding("CONSEQUENCE_UNRESOLVED", "/risk_review/consequence"))
    if not _canonical_strings(refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/risk_review/review_record_refs"))
    assert isinstance(refs, list)
    if state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/risk_review/review_state"))
    elif state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/risk_review/review_state"))
    elif state == "COMPLETE_FOR_DECLARED_SCOPE" and not refs:
        findings.add(Finding("REVIEW_RECORD_REQUIRED", "/risk_review/review_record_refs"))
    if state == "COMPLETE_FOR_DECLARED_SCOPE" and summary is None:
        findings.add(Finding("COMMUNICATION_SUMMARY_REQUIRED", "/risk_review/communication_summary"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("OBSERVED_AT_NOT_UTC", "/observed_at"))
    support = candidate["supporting_assessments"]
    review = candidate["risk_review"]
    assert isinstance(support, Mapping) and isinstance(review, Mapping)
    findings.update(_support_findings(support))
    findings.update(_axis_findings(review["axes"]))
    findings.update(_review_findings(review))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    if _contains_surrogate(candidate):
        return ValidationResult("ERROR", (Finding("JSON_UNPAIRED_SURROGATE", "/"),))
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


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    axis_patches = entry.get("axis_patches", {})
    assert isinstance(axis_patches, Mapping)
    axes = candidate["risk_review"]["axes"]
    assert isinstance(axes, list)
    for axis_name, axis_patch in axis_patches.items():
        for index, axis in enumerate(axes):
            if axis["axis"] == axis_name:
                axes[index] = _merge_patch(axis, axis_patch)
                break
        else:
            raise ValueError(f"unknown fixture axis: {axis_name}")
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
    parser = argparse.ArgumentParser(description="Validate fixture-only cartographic communication-risk assessments.")
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
