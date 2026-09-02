#!/usr/bin/env python3
"""Validate fixture-only Geology subsurface public-geometry assessments.

The validator reads synthetic declarations only. It performs no network access,
opens no restricted input, embeds or inspects no coordinates, executes no geometry
transform or policy, authenticates no review, mutates no lifecycle state, and grants
no release, publication, or public-use authority.
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

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/geology/subsurface_public_geometry_assessment.schema.json"
FIXTURE_PATH = ROOT / "fixtures/contracts/v1/domains/geology/subsurface_public_geometry_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:geology:subsurface-public-geometry-assessment:"


class DuplicateKeyError(ValueError):
    """Raised when JSON repeats an object key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-finite number token."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return [finding.code for finding in self.findings]


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
            return None, [Finding("INPUT_SYMLINK_DENIED")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("INPUT_TOO_LARGE")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT")]
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


def compute_identity(candidate: Mapping[str, object]) -> tuple[str, str]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("spec_hash", None)
    subject.pop("assessment_id", None)
    spec_hash = canonical_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate))
    return [] if not errors else [Finding("SCHEMA_INVALID")]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return parsed.utcoffset() is not None and parsed.utcoffset().total_seconds() == 0


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _integrity_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    expected_hash, expected_id = compute_identity(candidate)
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH"))
    if candidate.get("assessment_id") != expected_id:
        findings.add(Finding("ASSESSMENT_ID_MISMATCH"))
    if not _is_utc(candidate.get("recorded_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED"))

    subject = candidate["subject"]
    projection = candidate["public_projection"]
    assert isinstance(subject, Mapping)
    assert isinstance(projection, Mapping)
    arrays = (
        subject["source_descriptor_refs"],
        subject["source_roles"],
        projection["reason_codes"],
        candidate["anti_collapse_assertions"],
    )
    if not all(_canonical_strings(value) for value in arrays):
        findings.add(Finding("REFERENCE_OR_VOCABULARY_ARRAY_NOT_CANONICAL"))
    return sorted(findings)


def _coherence_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    subject = candidate["subject"]
    internal = candidate["internal_support"]
    projection = candidate["public_projection"]
    governance = candidate["governance"]
    assert isinstance(subject, Mapping)
    assert isinstance(internal, Mapping)
    assert isinstance(projection, Mapping)
    assert isinstance(governance, Mapping)

    family = subject["object_family"]
    disposition = projection["disposition"]
    precision = projection["precision_class"]

    if subject["rights_state"] == "DENIED":
        findings.add(Finding("SOURCE_RIGHTS_DENIED"))
    if precision in {"EXACT", "SOURCE_PRECISION"}:
        findings.add(Finding("PUBLIC_PRECISION_NOT_SAFE"))

    if disposition == "GENERALIZED":
        closure = (
            projection["public_geometry_ref_digest"],
            projection["geometry_quality_scope_assessment_ref"],
            projection["redaction_receipt_ref"],
            projection["public_summary"],
        )
        if any(value is None for value in closure):
            findings.add(Finding("GENERALIZATION_CLOSURE_REQUIRED"))
    elif disposition == "WITHHELD":
        if projection["public_geometry_ref_digest"] is not None:
            findings.add(Finding("WITHHELD_GEOMETRY_MUST_BE_ABSENT"))
        if projection["redaction_receipt_ref"] is None:
            findings.add(Finding("WITHHOLD_RECEIPT_REQUIRED"))
    elif disposition == "DENIED":
        if projection["public_geometry_ref_digest"] is not None:
            findings.add(Finding("DENIED_GEOMETRY_MUST_BE_ABSENT"))

    if family == "WellLogReference":
        if internal["payload_state"] == "PAYLOAD_PUBLIC":
            findings.add(Finding("WELL_LOG_PAYLOAD_RELEASE_DENIED"))
        if internal["vertical_datum_ref"] is None:
            findings.add(Finding("VERTICAL_DATUM_REQUIRED"))
    elif internal["payload_state"] == "PAYLOAD_PUBLIC":
        findings.add(Finding("SUBSURFACE_PAYLOAD_RELEASE_DENIED"))

    if internal["horizontal_crs_ref"] is None:
        findings.add(Finding("HORIZONTAL_CRS_REQUIRED"))
    if internal["depth_reference_ref"] is None:
        findings.add(Finding("DEPTH_REFERENCE_REQUIRED"))

    if governance["assessment_state"] == "COMPLETE":
        complete_refs = (
            governance["policy_decision_ref"],
            governance["review_record_ref"],
            governance["validation_report_ref"],
            governance["correction_ref"],
            governance["rollback_ref"],
        )
        if any(value is None for value in complete_refs):
            findings.add(Finding("COMPLETE_ASSESSMENT_CLOSURE_REQUIRED"))
    return sorted(findings)


def _abstain_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    subject = candidate["subject"]
    governance = candidate["governance"]
    assert isinstance(subject, Mapping)
    assert isinstance(governance, Mapping)
    state = governance["assessment_state"]
    if state in {"INCOMPLETE", "UNKNOWN"}:
        findings.add(Finding(f"ASSESSMENT_{state}"))
    if subject["rights_state"] == "UNRESOLVED":
        findings.add(Finding("SOURCE_RIGHTS_UNRESOLVED"))
    if subject["sensitivity_state"] == "UNRESOLVED":
        findings.add(Finding("SENSITIVITY_UNRESOLVED"))
    return sorted(findings)


def validate_candidate(candidate: Mapping[str, object]) -> Result:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return Result("DENY", tuple(schema_findings))
    integrity = _integrity_findings(candidate)
    if integrity:
        return Result("DENY", tuple(integrity))
    governance = candidate["governance"]
    assert isinstance(governance, Mapping)
    if governance["assessment_state"] == "ERROR":
        return Result("ERROR", (Finding("GEOLOGY_SUBSURFACE_PUBLIC_GEOMETRY_ASSESSMENT_ERROR"),))
    coherence = _coherence_findings(candidate)
    if coherence:
        return Result("DENY", tuple(coherence))
    abstain = _abstain_findings(candidate)
    return Result("ABSTAIN", tuple(abstain)) if abstain else Result("PASS", ())


def _merge(base: object, overlay: object) -> object:
    if isinstance(base, dict) and isinstance(overlay, dict):
        merged = copy.deepcopy(base)
        for key, value in overlay.items():
            merged[key] = _merge(merged[key], value) if key in merged else copy.deepcopy(value)
        return merged
    return copy.deepcopy(overlay)


def _resolve_base(manifest: Mapping[str, object], name: str) -> dict[str, object]:
    bases = manifest["bases"]
    assert isinstance(bases, Mapping)
    raw = copy.deepcopy(bases[name])
    assert isinstance(raw, dict)
    parent = raw.pop("extends", None)
    if parent is None:
        return raw
    assert isinstance(parent, str)
    resolved = _merge(_resolve_base(manifest, parent), raw)
    assert isinstance(resolved, dict)
    return resolved


def _replace(document: object, pointer: str, value: object) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


def materialize_fixture_case(manifest: Mapping[str, object], case: Mapping[str, object]) -> dict[str, object]:
    candidate = _resolve_base(manifest, str(case["base"]))
    for mutation in case.get("mutations", []):
        assert isinstance(mutation, Mapping)
        _replace(candidate, str(mutation["path"]), mutation.get("value"))
    spec_hash, assessment_id = compute_identity(candidate)
    candidate["spec_hash"] = case.get("spec_hash_override", spec_hash)
    candidate["assessment_id"] = case.get("assessment_id_override", assessment_id)
    return candidate


def validate_fixture_manifest() -> list[dict[str, object]]:
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    for case in manifest["cases"]:
        result = validate_candidate(materialize_fixture_case(manifest, case))
        results.append({
            "name": case["name"],
            "outcome": result.outcome,
            "findings": result.codes,
            "ok": result.outcome == case["expected_outcome"] and result.codes == case["expected_findings"],
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("input cannot be combined with --fixtures")
        results = validate_fixture_manifest()
        for result in results:
            print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        return 0 if all(result["ok"] for result in results) else 1
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    candidate, findings = load_json_object(args.input)
    result = Result("ERROR", tuple(findings)) if candidate is None else validate_candidate(candidate)
    print(json.dumps({
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "outcome": result.outcome,
        "findings": result.codes,
    }, sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
