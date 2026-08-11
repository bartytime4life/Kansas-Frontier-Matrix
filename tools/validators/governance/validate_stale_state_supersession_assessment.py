"""Validate fixture-only KFM stale-state and supersession assessments.

The validator checks only declared coherence. It does not determine freshness or
truth, mutate an object, issue a correction, decide cross-lane propagation, or
authorize review, release, deployment, publication, or public use.
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
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/stale_state_supersession_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/stale_state_supersession_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:stale-supersession:"
ABSTAIN_CODES = {
    "ACTION_HELD",
    "LINEAGE_UNKNOWN",
    "MARKER_UNKNOWN",
    "REVIEW_PENDING",
    "REVIEW_UNKNOWN",
    "SOURCE_BASIS_UNRESOLVED",
    "SUBJECT_STATE_UNKNOWN",
}
DIRECT_STORE_MARKERS = (
    "postgres://",
    "neo4j://",
    "s3://",
    "file://",
    "data/raw",
    "data/work",
    "data/quarantine",
    "raw/",
    "work/",
    "quarantine/",
)
QUERY_MARKERS = ("match (", "select *", "sparql ", "graph_query", "cypher:")


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


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
    subject.pop("assessment_id", None)
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def compute_assessment_id(candidate: Mapping[str, object]) -> str:
    return IDENTITY_PREFIX + compute_profile_hash(candidate).split(":", 1)[1][:24]


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


def _as_time(value: object) -> datetime | None:
    if not _is_utc(value):
        return None
    assert isinstance(value, str)
    return datetime.fromisoformat(value[:-1] + "+00:00")


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _walk_strings(value: object, path: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(value, str):
        yield path or "/", value
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk_strings(item, f"{path}/{index}")
    elif isinstance(value, Mapping):
        for key in sorted(value):
            escaped = str(key).replace("~", "~0").replace("/", "~1")
            yield from _walk_strings(value[key], f"{path}/{escaped}")


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("assessment_id") != compute_assessment_id(candidate):
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    evaluated_at = candidate.get("evaluated_at")
    if not _is_utc(evaluated_at):
        findings.add(Finding("EVALUATED_AT_NOT_UTC", "/evaluated_at"))

    subject = candidate["subject"]
    stale = candidate["stale_evaluation"]
    lineage = candidate["lineage"]
    response = candidate["proposed_response"]
    review = candidate["review"]
    assert all(isinstance(item, Mapping) for item in (subject, stale, lineage, response, review))

    for field, value in (
        ("/stale_evaluation/basis_refs", stale["basis_refs"]),
        ("/lineage/lineage_refs", lineage["lineage_refs"]),
        ("/proposed_response/decision_refs", response["decision_refs"]),
        ("/proposed_response/affected_surface_refs", response["affected_surface_refs"]),
        ("/review/record_refs", review["record_refs"]),
    ):
        if not _canonical_strings(value):
            findings.add(Finding("REFERENCES_NOT_CANONICAL", field))

    marker = stale["marker"]
    detected_at = stale["detected_at"]
    basis_refs = stale["basis_refs"]
    state = subject["declared_state"]
    if state == "UNKNOWN":
        findings.add(Finding("SUBJECT_STATE_UNKNOWN", "/subject/declared_state"))
    if marker == "UNKNOWN":
        findings.add(Finding("MARKER_UNKNOWN", "/stale_evaluation/marker"))
    elif marker == "NONE":
        if detected_at is not None or basis_refs:
            findings.add(Finding("NONE_MARKER_HAS_SUPPORT", "/stale_evaluation"))
        if state in {"STALE", "SUPERSEDED", "WITHDRAWN"}:
            findings.add(Finding("STATE_MARKER_CONTRADICTION", "/subject/declared_state"))
    else:
        if detected_at is None:
            findings.add(Finding("MARKER_DETECTED_AT_REQUIRED", "/stale_evaluation/detected_at"))
        elif not _is_utc(detected_at):
            findings.add(Finding("DETECTED_AT_NOT_UTC", "/stale_evaluation/detected_at"))
        elif _as_time(evaluated_at) and _as_time(detected_at) and _as_time(detected_at) > _as_time(evaluated_at):
            findings.add(Finding("DETECTED_AFTER_EVALUATION", "/stale_evaluation/detected_at"))
        if not basis_refs:
            findings.add(Finding("SOURCE_BASIS_UNRESOLVED", "/stale_evaluation/basis_refs"))

    relation = lineage["relation"]
    predecessor = lineage["predecessor_ref"]
    successor = lineage["successor_ref"]
    effective_at = lineage["effective_at"]
    lineage_refs = lineage["lineage_refs"]
    subject_ref = subject["object_ref"]
    if relation == "UNKNOWN":
        findings.add(Finding("LINEAGE_UNKNOWN", "/lineage/relation"))
    elif relation == "NONE":
        if successor is not None or effective_at is not None or lineage_refs:
            findings.add(Finding("NONE_LINEAGE_HAS_LINKAGE", "/lineage"))
    else:
        if effective_at is None:
            findings.add(Finding("LINEAGE_EFFECTIVE_AT_REQUIRED", "/lineage/effective_at"))
        elif not _is_utc(effective_at):
            findings.add(Finding("EFFECTIVE_AT_NOT_UTC", "/lineage/effective_at"))
        if not lineage_refs:
            findings.add(Finding("LINEAGE_SUPPORT_REQUIRED", "/lineage/lineage_refs"))
        if not lineage["prior_retained"]:
            findings.add(Finding("PRIOR_ARTIFACT_NOT_RETAINED", "/lineage/prior_retained"))

    if relation in {"SUPERSEDED_BY", "NEW_RECEIPT_CROSS_REFERENCE"} and successor is None:
        findings.add(Finding("SUCCESSOR_REQUIRED", "/lineage/successor_ref"))
    if relation == "WITHDRAWN_WITHOUT_SUCCESSOR" and successor is not None:
        findings.add(Finding("WITHDRAWAL_SUCCESSOR_DENIED", "/lineage/successor_ref"))
    if successor == subject_ref or predecessor == subject_ref or (
        successor is not None and successor == predecessor
    ):
        findings.add(Finding("LINEAGE_SELF_REFERENCE", "/lineage"))
    if lineage["silent_rebind"]:
        findings.add(Finding("SILENT_REBIND_DENIED", "/lineage/silent_rebind"))

    family = subject["object_family"]
    if family == "AI_RECEIPT" and relation == "SUPERSEDED_BY":
        findings.add(Finding("AI_RECEIPT_RETROACTIVE_SUPERSESSION_DENIED", "/lineage/relation"))
    if relation == "NEW_RECEIPT_CROSS_REFERENCE" and family != "AI_RECEIPT":
        findings.add(Finding("NEW_RECEIPT_RELATION_FAMILY_MISMATCH", "/subject/object_family"))
    if family in {"SCHEMA", "POLICY"} and relation == "SUPERSEDED_BY":
        decision_refs = response["decision_refs"]
        if not decision_refs or not any(str(ref).startswith("kfm://adr/") for ref in decision_refs):
            findings.add(Finding("ADR_REFERENCE_REQUIRED", "/proposed_response/decision_refs"))

    action = response["action"]
    if action == "HOLD":
        findings.add(Finding("ACTION_HELD", "/proposed_response/action"))
    elif action == "MARK_STALE" and (state != "STALE" or marker in {"NONE", "UNKNOWN"}):
        findings.add(Finding("ACTION_STATE_INCOHERENT", "/proposed_response/action"))
    elif action == "SUPERSEDE" and relation not in {"SUPERSEDED_BY", "UNKNOWN"}:
        findings.add(Finding("ACTION_LINEAGE_INCOHERENT", "/proposed_response/action"))
    elif action == "WITHDRAW" and relation != "WITHDRAWN_WITHOUT_SUCCESSOR":
        findings.add(Finding("ACTION_LINEAGE_INCOHERENT", "/proposed_response/action"))
    elif action == "REISSUE_AS_NEW" and (
        relation != "NEW_RECEIPT_CROSS_REFERENCE" or family != "AI_RECEIPT"
    ):
        findings.add(Finding("ACTION_LINEAGE_INCOHERENT", "/proposed_response/action"))
    elif action == "NO_ACTION" and (
        marker != "NONE" or relation != "NONE" or state != "CURRENT"
    ):
        findings.add(Finding("ACTION_STATE_INCOHERENT", "/proposed_response/action"))

    if stale["substance_status"] == "INCORRECT" and not (
        response["correction_ref"] or response["withdrawal_ref"]
    ):
        findings.add(Finding("INCORRECT_WITHOUT_CORRECTION", "/proposed_response"))
    if subject["exposure"] == "PUBLISHED":
        if action in {"SUPERSEDE", "WITHDRAW"} and response["rollback_ref"] is None:
            findings.add(Finding("PUBLISHED_ROLLBACK_REQUIRED", "/proposed_response/rollback_ref"))
        if marker != "NONE" and not response["affected_surface_refs"]:
            findings.add(Finding("PUBLISHED_SURFACES_REQUIRED", "/proposed_response/affected_surface_refs"))

    review_state = review["state"]
    if review_state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/review/state"))
    elif review_state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/review/state"))
    elif not review["record_refs"]:
        findings.add(Finding("REVIEW_RECORD_REQUIRED", "/review/record_refs"))

    for path, value in _walk_strings(candidate):
        lowered = value.casefold()
        if any(marker_text in lowered for marker_text in DIRECT_STORE_MARKERS):
            findings.add(Finding("DIRECT_STORE_REFERENCE_DENIED", path))
        if any(marker_text in lowered for marker_text in QUERY_MARKERS):
            findings.add(Finding("EMBEDDED_QUERY_DENIED", path))
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
        outcome = "REVIEW_REQUIRED"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if isinstance(base, list) and isinstance(patch, Mapping) and all(
        isinstance(key, str) and key.isdigit() for key in patch
    ):
        target = copy.deepcopy(base)
        for key in sorted(patch, key=int):
            index = int(key)
            if index >= len(target):
                raise ValueError("fixture list patch index out of range")
            target[index] = _merge_patch(target[index], patch[key])
        return target
    if not isinstance(patch, Mapping):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, Mapping) else {}
    assert isinstance(target, dict)
    for key, value in patch.items():
        target[key] = None if value is None else _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    if not isinstance(candidate, dict):
        raise ValueError("materialized fixture must be an object")
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    candidate["assessment_id"] = compute_assessment_id(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    elif entry.get("tamper") == "assessment_id":
        candidate["assessment_id"] = IDENTITY_PREFIX + "f" * 24
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
        description="Validate fixture-only stale-state and supersession assessments."
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
    return 0 if result.outcome == "REVIEW_REQUIRED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
