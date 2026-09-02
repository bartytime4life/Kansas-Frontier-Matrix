#!/usr/bin/env python3
"""Validate fixture-only drone capture authorization metadata.

This validator performs local declaration checks only. It does not contact an
authority, query airspace, decide law or policy, authorize flight, create
evidence, approve review, release, publish, or authorize public use.
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

ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/evidence/drone_capture_authorization_metadata.schema.json"
FIXTURE_PATH = ROOT / "fixtures/contracts/v1/evidence/drone_capture_authorization_metadata/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:drone-authorization-metadata:"


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
    subject.pop("metadata_id", None)
    spec_hash = canonical_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = list(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate)
    )
    return [] if not errors else [Finding("SCHEMA_INVALID")]


def _utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    if parsed.utcoffset() is None or parsed.utcoffset().total_seconds() != 0:
        return None
    return parsed


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _integrity_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    expected_hash, expected_id = compute_identity(candidate)
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH"))
    if candidate.get("metadata_id") != expected_id:
        findings.add(Finding("METADATA_ID_MISMATCH"))

    capture = candidate["capture"]
    authorization = candidate["authorization"]
    airspace = candidate["airspace_review"]
    safety = candidate["safety"]
    assert isinstance(capture, Mapping)
    assert isinstance(authorization, Mapping)
    assert isinstance(airspace, Mapping)
    assert isinstance(safety, Mapping)
    timestamps = [
        candidate["recorded_at"],
        capture["captured_from"],
        capture["captured_until"],
        authorization["reviewed_at"],
        authorization["valid_from"],
        authorization["valid_until"],
        airspace["reviewed_at"],
    ]
    if any(value is not None and _utc(value) is None for value in timestamps):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED"))
    if not _canonical_strings(safety["constraint_codes"]):
        findings.add(Finding("SAFETY_CONSTRAINT_CODES_NOT_CANONICAL"))
    return sorted(findings)


def _coherence_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    capture = candidate["capture"]
    authorization = candidate["authorization"]
    area = candidate["operating_area"]
    altitude = candidate["altitude"]
    airspace = candidate["airspace_review"]
    safety = candidate["safety"]
    governance = candidate["governance"]
    assert isinstance(capture, Mapping)
    assert isinstance(authorization, Mapping)
    assert isinstance(area, Mapping)
    assert isinstance(altitude, Mapping)
    assert isinstance(airspace, Mapping)
    assert isinstance(safety, Mapping)
    assert isinstance(governance, Mapping)

    capture_from = _utc(capture["captured_from"])
    capture_until = _utc(capture["captured_until"])
    assert capture_from is not None and capture_until is not None
    if capture_from > capture_until:
        findings.add(Finding("CAPTURE_WINDOW_INVALID"))

    auth_keys = (
        "evidence_ref",
        "identifier_digest",
        "authority_source_ref",
        "reviewed_at",
        "valid_from",
        "valid_until",
        "authorization_parameters_ref",
    )
    if authorization["evidence_state"] == "DOCUMENTED" and any(
        authorization[key] is None for key in auth_keys
    ):
        findings.add(Finding("DOCUMENTED_AUTHORIZATION_CLOSURE_REQUIRED"))

    valid_from = _utc(authorization["valid_from"])
    valid_until = _utc(authorization["valid_until"])
    if valid_from is not None and valid_until is not None:
        if valid_from > valid_until:
            findings.add(Finding("AUTHORIZATION_WINDOW_INVALID"))
        elif capture_from < valid_from or capture_until > valid_until:
            findings.add(Finding("CAPTURE_OUTSIDE_DECLARED_AUTHORIZATION_WINDOW"))

    if area["geometry_posture"] == "WITHHELD" and area["area_ref"] is not None:
        findings.add(Finding("WITHHELD_AREA_REFERENCE_FORBIDDEN"))
    if area["geometry_posture"] != "WITHHELD" and area["area_ref"] is None:
        findings.add(Finding("OPERATING_AREA_REFERENCE_REQUIRED"))
    if area["matches_capture_area"] is False:
        findings.add(Finding("OPERATING_AREA_MISMATCH"))

    altitude_values = (
        altitude["authorized_ceiling_m"],
        altitude["observed_maximum_m"],
        altitude["basis_ref"],
    )
    if altitude["reference"] == "UNKNOWN" and any(value is not None for value in altitude_values):
        findings.add(Finding("UNKNOWN_ALTITUDE_WITH_VALUES"))
    if altitude["reference"] != "UNKNOWN" and any(value is None for value in altitude_values):
        findings.add(Finding("ALTITUDE_DECLARATION_PARTIAL"))
    ceiling = altitude["authorized_ceiling_m"]
    observed = altitude["observed_maximum_m"]
    if isinstance(ceiling, (int, float)) and isinstance(observed, (int, float)) and observed > ceiling:
        findings.add(Finding("OBSERVED_ALTITUDE_EXCEEDS_DECLARED_CEILING"))

    known_airspace_results = {"CLEARED_WITH_CONSTRAINTS", "CONFLICT_DECLARED", "NO_CONFLICT_DECLARED"}
    if airspace["result"] in known_airspace_results and (
        airspace["review_ref"] is None or airspace["reviewed_at"] is None
    ):
        findings.add(Finding("AIRSPACE_REVIEW_CLOSURE_REQUIRED"))
    if airspace["result"] == "CLEARED_WITH_CONSTRAINTS" and airspace["constraints_ref"] is None:
        findings.add(Finding("AIRSPACE_CONSTRAINT_REFERENCE_REQUIRED"))
    if airspace["result"] == "CONFLICT_DECLARED":
        findings.add(Finding("AIRSPACE_CONFLICT_DECLARED"))

    if safety["constraint_codes"] and (
        safety["safety_plan_ref"] is None or safety["acknowledgment_ref"] is None
    ):
        findings.add(Finding("SAFETY_CONSTRAINT_CLOSURE_REQUIRED"))
    if airspace["result"] == "CLEARED_WITH_CONSTRAINTS" and not safety["constraint_codes"]:
        findings.add(Finding("DECLARED_CONSTRAINTS_NOT_ENUMERATED"))
    if governance["review_state"] == "DENIED":
        findings.add(Finding("HANDOFF_REVIEW_DENIED"))
    return sorted(findings)


def _abstain_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    authorization = candidate["authorization"]
    area = candidate["operating_area"]
    altitude = candidate["altitude"]
    airspace = candidate["airspace_review"]
    safety = candidate["safety"]
    governance = candidate["governance"]
    assert isinstance(authorization, Mapping)
    assert isinstance(area, Mapping)
    assert isinstance(altitude, Mapping)
    assert isinstance(airspace, Mapping)
    assert isinstance(safety, Mapping)
    assert isinstance(governance, Mapping)

    if candidate["record_state"] in {"INCOMPLETE", "UNKNOWN"}:
        findings.add(Finding(f"RECORD_{candidate['record_state']}"))
    if authorization["evidence_state"] != "DOCUMENTED":
        findings.add(Finding(f"AUTHORIZATION_EVIDENCE_{authorization['evidence_state']}"))
    if area["matches_capture_area"] is None:
        findings.add(Finding("OPERATING_AREA_MATCH_UNRESOLVED"))
    if altitude["reference"] == "UNKNOWN":
        findings.add(Finding("ALTITUDE_UNRESOLVED"))
    if airspace["result"] in {"INCOMPLETE", "UNKNOWN"}:
        findings.add(Finding(f"AIRSPACE_REVIEW_{airspace['result']}"))
    if safety["unresolved_count"] > 0:
        findings.add(Finding("SAFETY_CONSTRAINTS_UNRESOLVED"))
    if safety["safety_plan_ref"] is None or safety["acknowledgment_ref"] is None:
        findings.add(Finding("SAFETY_DOCUMENTATION_UNRESOLVED"))
    governance_keys = ("rights_ref", "safety_policy_ref", "evidence_bundle_ref")
    if any(governance[key] is None for key in governance_keys):
        findings.add(Finding("GOVERNANCE_REFERENCE_UNRESOLVED"))
    if governance["review_state"] == "PENDING":
        findings.add(Finding("HANDOFF_REVIEW_PENDING"))
    return sorted(findings)


def validate_candidate(candidate: Mapping[str, object]) -> Result:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return Result("DENY", tuple(schema_findings))
    integrity = _integrity_findings(candidate)
    if integrity:
        return Result("DENY", tuple(integrity))
    if candidate["record_state"] == "ERROR":
        return Result("ERROR", (Finding("AUTHORIZATION_METADATA_ERROR"),))
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


def materialize_fixture_case(
    manifest: Mapping[str, object], case: Mapping[str, object]
) -> dict[str, object]:
    candidate = _resolve_base(manifest, str(case["base"]))
    for mutation in case.get("mutations", []):
        assert isinstance(mutation, Mapping)
        _replace(candidate, str(mutation["path"]), mutation.get("value"))
    spec_hash, metadata_id = compute_identity(candidate)
    candidate["spec_hash"] = case.get("spec_hash_override", spec_hash)
    candidate["metadata_id"] = case.get("metadata_id_override", metadata_id)
    return candidate


def validate_fixture_manifest() -> list[dict[str, object]]:
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    for case in manifest["cases"]:
        result = validate_candidate(materialize_fixture_case(manifest, case))
        results.append(
            {
                "name": case["name"],
                "outcome": result.outcome,
                "findings": result.codes,
                "ok": result.outcome == case["expected_outcome"]
                and result.codes == case["expected_findings"],
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        for result in results:
            print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        return 0 if all(result["ok"] for result in results) else 1
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    candidate, findings = load_json_object(args.input)
    result = Result("ERROR", tuple(findings)) if candidate is None else validate_candidate(candidate)
    print(
        json.dumps(
            {
                "authority": "NONE",
                "execution_mode": "FIXTURE_ONLY",
                "outcome": result.outcome,
                "findings": result.codes,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
