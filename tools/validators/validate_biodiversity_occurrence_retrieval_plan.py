#!/usr/bin/env python3
"""Validate fixture-first biodiversity occurrence retrieval-plan candidates.

The validator is deterministic and no-network. Passing proves only local schema,
query-digest, sampling-support, transfer-state, and non-authority invariants.
It does not activate eBird or GBIF, retrieve source bytes, resolve evidence,
evaluate policy, or authorize release, deployment, publication, or public use.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/biodiversity_occurrence_retrieval_plan.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/biodiversity_occurrence_retrieval_plan"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "biodiversity-occurrence-retrieval-planning-only"
ZERO_DIGEST = "sha256:" + ("0" * 64)
TERMINAL_STATES = {"SUCCEEDED", "FAILED", "CANCELLED", "EXPIRED"}
NON_SUCCESS_STATES = {"PLANNED", "SUBMITTED", "RUNNING", "FAILED", "CANCELLED", "EXPIRED", "UNKNOWN"}
ALLOWED_TRANSITIONS = {
    "PLANNED": {"SUBMITTED", "SUCCEEDED", "FAILED", "CANCELLED", "UNKNOWN"},
    "SUBMITTED": {"RUNNING", "SUCCEEDED", "FAILED", "CANCELLED", "UNKNOWN"},
    "RUNNING": {"RUNNING", "SUCCEEDED", "FAILED", "CANCELLED", "UNKNOWN"},
    "SUCCEEDED": {"EXPIRED"},
    "FAILED": {"EXPIRED"},
    "CANCELLED": {"EXPIRED"},
    "UNKNOWN": {"SUBMITTED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED", "EXPIRED"},
    "EXPIRED": set(),
}
SECRET_RE = re.compile(r"(?i)(password|passwd|secret|api[_-]?key|access[_-]?token|authorization|bearer)")
EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
INTERNAL_TOKENS = ("data/raw/", "data/work/", "data/quarantine/", "kfm://data/raw/", "kfm://data/work/", "kfm://data/quarantine/")


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
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(
            finding.code
            in {
                "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE",
                "INPUT_SYMLINK_DENIED", "JSON_COMPLEXITY_LIMIT",
                "JSON_DUPLICATE_KEY", "JSON_INVALID", "JSON_NONFINITE_NUMBER",
                "JSON_NOT_UTF8", "ROOT_NOT_OBJECT", "SCHEMA_UNAVAILABLE",
            }
            for finding in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
                parse_float=_parse_finite_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _sorted_unique_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _canonical_digest(value: Mapping[str, Any], field: str) -> str:
    projected = dict(value)
    projected.pop(field, None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    return _canonical_digest(candidate, "spec_hash")


def _canonical_query_digest(query_snapshot: Mapping[str, Any]) -> str:
    return _canonical_digest(query_snapshot, "query_digest")


def _iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from _iter_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _iter_strings(item)


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    source = _mapping(candidate.get("source_profile"))
    intent = _mapping(candidate.get("retrieval_intent"))
    geography = _mapping(intent.get("geography"))
    window = _mapping(intent.get("time_window"))
    query = _mapping(candidate.get("query_snapshot"))
    sampling = _mapping(candidate.get("sampling_support"))
    transfer = _mapping(candidate.get("transfer"))
    provenance = _mapping(candidate.get("provenance"))
    governance = _mapping(candidate.get("governance"))

    for field, value in (
        ("/spec_hash", candidate.get("spec_hash")),
        ("/query_snapshot/query_digest", query.get("query_digest")),
        ("/transfer/artifact_digest", transfer.get("artifact_digest")),
    ):
        if value == ZERO_DIGEST:
            findings.append(Finding("DIGEST_PLACEHOLDER", field))

    supplied_spec = candidate.get("spec_hash")
    if isinstance(supplied_spec, str):
        try:
            expected = _canonical_spec_hash(candidate)
        except (TypeError, ValueError, RecursionError):
            expected = None
        if expected is not None and supplied_spec != expected:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    supplied_query = query.get("query_digest")
    if isinstance(supplied_query, str):
        try:
            expected_query = _canonical_query_digest(query)
        except (TypeError, ValueError, RecursionError):
            expected_query = None
        if expected_query is not None and supplied_query != expected_query:
            findings.append(Finding("QUERY_DIGEST_MISMATCH", "/query_snapshot/query_digest"))

    arrays = (
        ("/domain_scope", _array(candidate.get("domain_scope"))),
        ("/sampling_support/support_units", _array(sampling.get("support_units"))),
        ("/sampling_support/observer_effort_fields", _array(sampling.get("observer_effort_fields"))),
        ("/transfer/reason_codes", _array(transfer.get("reason_codes"))),
        ("/provenance/input_refs", _array(provenance.get("input_refs"))),
    )
    for field, values in arrays:
        if not _sorted_unique_strings(values):
            code = "DOMAIN_SCOPE_NOT_CANONICAL" if field == "/domain_scope" else "REFS_OR_REASONS_NOT_CANONICAL"
            findings.append(Finding(code, field))

    parameters = _array(query.get("parameters"))
    names = [item.get("name") for item in parameters if isinstance(item, dict)]
    if len(names) != len(parameters) or not _sorted_unique_strings(names):
        findings.append(Finding("QUERY_PARAMETERS_NOT_CANONICAL", "/query_snapshot/parameters"))

    sensitive_query_values = [query.get("query_text")]
    for item in parameters:
        if isinstance(item, dict):
            sensitive_query_values.extend(_iter_strings(item.get("value")))
    if any(
        isinstance(value, str) and (SECRET_RE.search(value) or EMAIL_RE.search(value))
        for value in sensitive_query_values
    ):
        findings.append(Finding("QUERY_SECRET_OR_PII_LEAKAGE", "/query_snapshot"))

    family = source.get("source_family")
    product = source.get("product")
    source_role = source.get("source_role")
    language = query.get("query_language")
    transfer_mode = transfer.get("mode")
    expected = {
        ("EBIRD", "EBIRD_EBD_SED"): ("EBIRD_FILTER_PROFILE", "CITIZEN_SCIENCE_OBSERVATION", "MANUAL_APPROVED_BULK_FILE"),
        ("GBIF", "GBIF_OCCURRENCE_PREDICATE"): ("GBIF_PREDICATE_JSON", "AGGREGATED_OCCURRENCE", "ASYNCHRONOUS_JOB"),
        ("GBIF", "GBIF_OCCURRENCE_SQL"): ("GBIF_SQL", "AGGREGATED_OCCURRENCE", "ASYNCHRONOUS_JOB"),
    }.get((family, product))
    if expected is None or language != expected[0] or source_role != expected[1]:
        findings.append(Finding("SOURCE_PROFILE_QUERY_MISMATCH", "/source_profile"))
    if expected is None or transfer_mode != expected[2]:
        findings.append(Finding("TRANSFER_MODE_PROFILE_MISMATCH", "/transfer/mode"))

    kind = geography.get("kind")
    identifier = geography.get("identifier")
    geography_valid = (
        (kind == "STATE" and identifier == "KS")
        or (kind == "COUNTY" and isinstance(identifier, str) and re.fullmatch(r"20[0-9]{3}", identifier))
        or (kind == "HUC12" and isinstance(identifier, str) and re.fullmatch(r"[0-9]{12}", identifier))
    )
    if not geography_valid:
        findings.append(Finding("GEOGRAPHY_IDENTIFIER_INVALID", "/retrieval_intent/geography"))

    start = _parse_time(window.get("start"))
    end = _parse_time(window.get("end"))
    if start and end and start >= end:
        findings.append(Finding("TIME_WINDOW_INVALID", "/retrieval_intent/time_window"))

    absence_requested = intent.get("absence_claim_requested")
    if absence_requested is not False or sampling.get("absence_claim_allowed") is not False:
        findings.append(Finding("ABSENCE_INFERENCE_OVERCLAIM", "/sampling_support"))

    if family == "EBIRD":
        required_effort = [
            "ALL_SPECIES_REPORTED", "DISTANCE_KM", "DURATION_MINUTES", "PARTY_SIZE", "PROTOCOL_TYPE"
        ]
        ebird_valid = (
            sampling.get("mode") == "CHECKLIST_EFFORT"
            and sampling.get("support_units") == ["CHECKLIST", "OCCURRENCE_RECORD", "SAMPLING_EVENT"]
            and sampling.get("complete_checklists_required") is True
            and sampling.get("paired_product_required") is True
            and sampling.get("paired_product") == "SED"
            and sampling.get("zero_fill_allowed") is True
            and sampling.get("non_detection_inference_allowed") is True
            and sampling.get("observer_effort_fields") == required_effort
            and intent.get("purpose") == "EFFORT_AWARE_OCCURRENCE"
            and intent.get("requested_claim_role") == "CANDIDATE_SAMPLING_SUPPORT"
            and intent.get("result_granularity") == "CHECKLIST"
            and intent.get("non_detection_inference_requested") is True
        )
        if not ebird_valid:
            findings.append(Finding("EBIRD_SAMPLING_SUPPORT_INCOMPLETE", "/sampling_support"))
    elif family == "GBIF":
        purpose = intent.get("purpose")
        granularity = intent.get("result_granularity")
        role = intent.get("requested_claim_role")
        mode = sampling.get("mode")
        units = sampling.get("support_units")
        profile_ok = (
            (product == "GBIF_OCCURRENCE_PREDICATE" and purpose == "OCCURRENCE_RESEARCH" and granularity == "RECORD" and role == "CANDIDATE_OCCURRENCE_SUPPORT" and mode == "PRESENCE_ONLY" and units == ["OCCURRENCE_RECORD"])
            or (product == "GBIF_OCCURRENCE_SQL" and purpose == "AGGREGATE_SUMMARY" and granularity == "AGGREGATE" and role == "CANDIDATE_AGGREGATE_SUPPORT" and mode == "AGGREGATE_ONLY" and units == ["DATASET_AGGREGATE"])
        )
        no_effort = (
            sampling.get("complete_checklists_required") is False
            and sampling.get("paired_product_required") is False
            and sampling.get("paired_product") is None
            and sampling.get("zero_fill_allowed") is False
            and sampling.get("non_detection_inference_allowed") is False
            and sampling.get("observer_effort_fields") == []
            and intent.get("non_detection_inference_requested") is False
        )
        if not profile_ok or not no_effort:
            findings.append(Finding("GBIF_SAMPLING_SUPPORT_OVERCLAIM", "/sampling_support"))

    if (
        sampling.get("source_role_preserved") is not True
        or sampling.get("specimen_equivalence_claimed") is not False
        or sampling.get("no_detection_is_not_absence") is not True
        or sampling.get("missing_row_is_not_absence") is not True
    ):
        findings.append(Finding("SAMPLING_SUPPORT_BOUNDARY_VIOLATION", "/sampling_support"))

    history = _array(transfer.get("state_history"))
    parsed_history: list[tuple[str, datetime]] = []
    history_shape_ok = True
    for item in history:
        if not isinstance(item, dict):
            history_shape_ok = False
            continue
        state = item.get("state")
        at = _parse_time(item.get("at"))
        if not isinstance(state, str) or at is None:
            history_shape_ok = False
            continue
        parsed_history.append((state, at))
    if not history_shape_ok or not parsed_history or [at for _, at in parsed_history] != sorted(at for _, at in parsed_history):
        findings.append(Finding("TRANSFER_HISTORY_NOT_CANONICAL", "/transfer/state_history"))
    else:
        for (prior, _), (current, _) in zip(parsed_history, parsed_history[1:]):
            if current not in ALLOWED_TRANSITIONS.get(prior, set()):
                findings.append(Finding("TRANSFER_HISTORY_TRANSITION_INVALID", "/transfer/state_history"))
                break
        if transfer.get("state") != parsed_history[-1][0]:
            findings.append(Finding("TRANSFER_STATE_MISMATCH", "/transfer/state"))
        updated = _parse_time(transfer.get("updated_at"))
        if updated and updated != parsed_history[-1][1]:
            findings.append(Finding("TRANSFER_TIMESTAMP_INVALID", "/transfer/updated_at"))

    submitted_at = _parse_time(transfer.get("submitted_at"))
    terminal_at = _parse_time(transfer.get("terminal_at"))
    updated_at = _parse_time(transfer.get("updated_at"))
    recorded_at = _parse_time(provenance.get("recorded_at"))
    state = transfer.get("state")
    history_states = [item[0] for item in parsed_history]
    timestamp_invalid = False
    if state in TERMINAL_STATES and terminal_at is None:
        timestamp_invalid = True
    if state not in TERMINAL_STATES and terminal_at is not None:
        timestamp_invalid = True
    if "SUBMITTED" in history_states and submitted_at is None:
        timestamp_invalid = True
    if submitted_at and updated_at and submitted_at > updated_at:
        timestamp_invalid = True
    if terminal_at and updated_at and terminal_at != updated_at:
        timestamp_invalid = True
    if recorded_at and updated_at and updated_at > recorded_at:
        timestamp_invalid = True
    if timestamp_invalid:
        findings.append(Finding("TRANSFER_TIMESTAMP_INVALID", "/transfer"))

    transfer_id = transfer.get("transfer_id")
    artifact_ref = transfer.get("artifact_ref")
    artifact_digest = transfer.get("artifact_digest")
    citation_ref = transfer.get("citation_ref")
    bytes_available = transfer.get("bytes_available")
    success = transfer.get("terminal_success_confirmed")
    if state == "PLANNED" and transfer_id is not None:
        findings.append(Finding("TRANSFER_STATE_MISMATCH", "/transfer/transfer_id"))
    if state in {"SUBMITTED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED", "EXPIRED", "UNKNOWN"} and transfer_mode == "ASYNCHRONOUS_JOB" and transfer_id is None:
        findings.append(Finding("TRANSFER_STATE_MISMATCH", "/transfer/transfer_id"))
    if state == "SUCCEEDED":
        if not all([artifact_ref, artifact_digest, citation_ref]) or bytes_available is not True or success is not True or terminal_at is None:
            findings.append(Finding("TRANSFER_SUCCESS_INCOMPLETE", "/transfer"))
    elif state in {"FAILED", "CANCELLED", "EXPIRED"}:
        if artifact_ref is not None or artifact_digest is not None or bytes_available is not False or success is not False:
            findings.append(Finding("TRANSFER_FAILURE_ARTIFACT_OVERCLAIM", "/transfer"))
    elif state == "UNKNOWN":
        if artifact_ref is not None or artifact_digest is not None or citation_ref is not None or bytes_available is not False or success is not False:
            findings.append(Finding("TRANSFER_UNKNOWN_OVERCLAIM", "/transfer"))
    elif state in {"PLANNED", "SUBMITTED", "RUNNING"}:
        if artifact_ref is not None or artifact_digest is not None or bytes_available is not False or success is not False:
            findings.append(Finding("TRANSFER_PRETERMINAL_ARTIFACT_OVERCLAIM", "/transfer"))

    if any(any(token in text.lower() for token in INTERNAL_TOKENS) for text in _iter_strings(candidate)):
        findings.append(Finding("INTERNAL_LIFECYCLE_REFERENCE_DENIED", "/"))

    governance_flags = (
        "rights_cleared", "sensitivity_cleared", "source_admitted",
        "evidence_closure_claimed", "policy_evaluated", "review_complete",
        "promotion_authorized", "release_authorized", "publication_authorized",
        "public_use_allowed",
    )
    if (
        any(governance.get(field) is not False for field in governance_flags)
        or governance.get("release_state") != "HOLD"
        or governance.get("release_ref") is not None
        or source.get("live_source_activated") is not False
    ):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return findings


def validate_plan(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display_path(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def validate_fixtures() -> bool:
    valid_paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
    invalid_root = FIXTURE_ROOT / "invalid"
    invalid_paths = sorted(invalid_root.glob("invalid_*.json"))
    try:
        manifest = json.loads((invalid_root / "expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        print(json.dumps({"outcome": "ERROR", "code": "FIXTURE_MANIFEST_INVALID"}, separators=(",", ":")))
        return False
    ok = bool(valid_paths and invalid_paths and set(manifest) == {path.name for path in invalid_paths})
    for path in valid_paths:
        result = validate_plan(path)
        print(_serialize(path, result))
        if not result.ok:
            ok = False
    for path in invalid_paths:
        result = validate_plan(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(manifest.get(path.name, []))
        if result.ok or actual != expected:
            ok = False
    if not ok:
        print(json.dumps({"outcome": "ERROR", "code": "FIXTURE_POLARITY_ERROR"}, separators=(",", ":")))
    return ok


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            print(json.dumps({"outcome": "ERROR", "code": "ARGUMENT_CONFLICT"}, separators=(",", ":")))
            return 2
        return 0 if validate_fixtures() else 1
    if args.path is None:
        print(json.dumps({"outcome": "ERROR", "code": "INPUT_REQUIRED"}, separators=(",", ":")))
        return 2
    result = validate_plan(args.path)
    print(_serialize(args.path, result))
    if result.ok:
        return 0
    return 2 if result.error else 1


if __name__ == "__main__":
    raise SystemExit(main())
