"""Validate the fixture-only STAC asset HEAD prefilter profile.

The profile evaluates recorded synthetic HEAD metadata for an already-known STAC
asset. It deliberately performs no network request and never downloads bytes.
A passing result proves only bounded shape, deterministic base-envelope
integrity, asset-state binding, finite prefilter classification, and routing
coherence. It creates no source, lifecycle, evidence, policy, review, release,
publication, or public-use authority.
"""

from __future__ import annotations

import argparse
import copy
import ipaddress
import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators.validate_source_event_envelope import (
    Finding,
    _expected_event_id,
    _load_json_object,
    compute_spec_hash,
    validate_document as validate_base_document,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "source"
    / "stac_asset_head_prefilter.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures"
    / "contracts"
    / "v1"
    / "source"
    / "stac_asset_head_prefilter"
    / "cases.json"
)
SCOPE = "source.stac_asset_head_prefilter"
MAX_SCHEMA_FINDINGS = 100
NON_EFFECTS = (
    "no_network_request",
    "no_asset_download",
    "no_source_activation",
    "no_raw_or_lifecycle_write",
    "no_evidence_policy_or_review_creation",
    "no_promotion_release_deployment_or_publication",
)


@dataclass(frozen=True)
class ProfileValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    event_id: str | None = None
    payload_spec_hash: str | None = None


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _string_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]


def _json_pointer(parts: Sequence[object], prefix: str = "") -> str:
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    suffix = "/" + "/".join(escaped) if escaped else ""
    return prefix + suffix or "/"


def _load_profile_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _profile_schema_findings(attributes: Mapping[str, object]) -> set[Finding]:
    try:
        validator = _load_profile_validator()
        errors = list(islice(validator.iter_errors(attributes), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return {Finding("STAC_PROFILE_SCHEMA_UNAVAILABLE", "/payload/attributes")}
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors[:MAX_SCHEMA_FINDINGS],
        key=lambda error: (
            _json_pointer(tuple(error.absolute_path), "/payload/attributes"),
            str(error.validator or "schema"),
        ),
    )
    findings = {
        Finding(
            "STAC_PROFILE_SCHEMA_INVALID",
            _json_pointer(tuple(error.absolute_path), "/payload/attributes"),
        )
        for error in errors
    }
    if truncated:
        findings.add(Finding("STAC_PROFILE_SCHEMA_FINDINGS_TRUNCATED", "/payload/attributes"))
    return findings


def _safe_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = urlsplit(value)
        host = parsed.hostname
        if parsed.scheme != "https" or not host or parsed.username or parsed.password:
            return False
        if parsed.fragment or host.lower() == "localhost" or host.lower().endswith(".localhost"):
            return False
        try:
            address = ipaddress.ip_address(host)
        except ValueError:
            return True
        return not (
            address.is_private
            or address.is_loopback
            or address.is_link_local
            or address.is_multicast
            or address.is_reserved
            or address.is_unspecified
        )
    except ValueError:
        return False


def _parse_aware_datetime(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed


def _expected_state(attrs: Mapping[str, object]) -> tuple[str, str, bool]:
    """Return expected decision, reason, and whether metadata are contradictory."""
    status = attrs.get("stac.http_status")
    if status == 304:
        return "UNCHANGED", "HTTP_NOT_MODIFIED", False
    if status in (401, 403):
        return "DENY", "ACCESS_DENIED", False
    if status == 404:
        return "UNAVAILABLE", "ASSET_NOT_FOUND", False
    if status == 410:
        return "UNAVAILABLE", "ASSET_GONE", False
    if status == 405:
        return "ERROR", "METHOD_NOT_ALLOWED", False
    if status == 429:
        return "ERROR", "RATE_LIMITED", False
    if status in (500, 502, 503, 504):
        return "ERROR", "UPSTREAM_ERROR", False

    comparisons: list[bool] = []
    for prior_key, observed_key in (
        ("stac.prior_etag", "stac.observed_etag"),
        ("stac.prior_last_modified", "stac.observed_last_modified"),
        ("stac.prior_content_length", "stac.observed_content_length"),
    ):
        prior = attrs.get(prior_key)
        observed = attrs.get(observed_key)
        if prior is not None and observed is not None:
            comparisons.append(prior == observed)

    if not comparisons:
        return "ERROR", "VALIDATOR_MISSING", False
    if any(comparisons) and not all(comparisons):
        return "ERROR", "VALIDATOR_CONFLICT", True
    if all(comparisons):
        return "UNCHANGED", "VALIDATOR_MATCH", False
    return "CHANGED", "VALIDATOR_CHANGED", False


def _expected_routing(decision: str, reason: str) -> tuple[str, bool, set[str]]:
    if decision == "UNCHANGED":
        return "NO_ACTION", False, {"NO_MATERIAL_CHANGE", reason}
    if decision == "CHANGED":
        return "PROPOSE_QUARANTINE", True, {"STAC_ASSET_CHANGED", reason}
    if decision == "UNAVAILABLE":
        return "PROPOSE_QUARANTINE", True, {"STAC_ASSET_UNAVAILABLE", reason}
    if decision == "DENY":
        return "PROPOSE_QUARANTINE", True, {"STAC_ACCESS_DENIED", reason}
    return "PROPOSE_QUARANTINE", True, {"STAC_PREFILTER_ERROR", reason}


def _semantic_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    payload = _mapping(candidate.get("payload"))
    attrs = _mapping(payload.get("attributes"))
    subject = _mapping(candidate.get("subject"))
    routing = _mapping(candidate.get("routing"))

    asset_href = attrs.get("stac.asset_href")
    if (
        asset_href != subject.get("subject_ref")
        or attrs.get("stac.media_type") != subject.get("media_type")
        or subject.get("native_id")
        != f"{attrs.get('stac.item_id')}#{attrs.get('stac.asset_key')}"
    ):
        findings.add(Finding("STAC_ASSET_BINDING_INVALID", "/payload/attributes/stac.asset_href"))
    if not _safe_https_url(asset_href):
        findings.add(Finding("STAC_ASSET_URL_UNSAFE", "/payload/attributes/stac.asset_href"))

    if subject.get("etag") != attrs.get("stac.prior_etag"):
        findings.add(Finding("STAC_PRIOR_STATE_UNBOUND", "/payload/attributes/stac.prior_etag"))
    if subject.get("last_modified") != attrs.get("stac.prior_last_modified"):
        findings.add(
            Finding("STAC_PRIOR_STATE_UNBOUND", "/payload/attributes/stac.prior_last_modified")
        )
    if subject.get("byte_count") != attrs.get("stac.prior_content_length"):
        findings.add(
            Finding("STAC_PRIOR_STATE_UNBOUND", "/payload/attributes/stac.prior_content_length")
        )

    prior_etag = attrs.get("stac.prior_etag")
    prior_modified = attrs.get("stac.prior_last_modified")
    if prior_etag is None and prior_modified is None:
        findings.add(Finding("STAC_PRIOR_VALIDATOR_MISSING", "/payload/attributes"))

    checked_at = _parse_aware_datetime(attrs.get("stac.checked_at"))
    occurred_at = _parse_aware_datetime(candidate.get("occurred_at"))
    received_at = _parse_aware_datetime(candidate.get("received_at"))
    if (
        checked_at is None
        or occurred_at is None
        or received_at is None
        or checked_at != occurred_at
        or checked_at > received_at
    ):
        findings.add(Finding("STAC_CHECK_TIME_INVALID", "/payload/attributes/stac.checked_at"))

    if candidate.get("event_type") != "SCHEDULED_POLL":
        findings.add(Finding("STAC_EVENT_TYPE_INVALID", "/event_type"))

    expected_decision, expected_reason, conflict = _expected_state(attrs)
    if conflict:
        findings.add(Finding("STAC_VALIDATOR_CONFLICT", "/payload/attributes"))
    if attrs.get("stac.decision") != expected_decision:
        findings.add(Finding("STAC_DECISION_MISMATCH", "/payload/attributes/stac.decision"))
    if attrs.get("stac.reason_code") != expected_reason:
        findings.add(Finding("STAC_REASON_CODE_MISMATCH", "/payload/attributes/stac.reason_code"))

    expected_disposition, expected_review, expected_reasons = _expected_routing(
        expected_decision, expected_reason
    )
    actual_reasons = set(_string_list(routing.get("reason_codes")))
    if (
        routing.get("disposition") != expected_disposition
        or routing.get("review_required") is not expected_review
        or actual_reasons != expected_reasons
    ):
        findings.add(Finding("STAC_ROUTING_MISMATCH", "/routing"))

    status = attrs.get("stac.http_status")
    if status in (200, 204):
        observed = (
            attrs.get("stac.observed_etag"),
            attrs.get("stac.observed_last_modified"),
            attrs.get("stac.observed_content_length"),
        )
        if all(value is None for value in observed):
            findings.add(Finding("STAC_VALIDATOR_MISSING", "/payload/attributes"))
    elif status == 304:
        if any(
            attrs.get(key) is not None
            for key in (
                "stac.observed_etag",
                "stac.observed_last_modified",
                "stac.observed_content_length",
            )
        ):
            findings.add(Finding("STAC_NOT_MODIFIED_METADATA_INVALID", "/payload/attributes"))
    else:
        if any(
            attrs.get(key) is not None
            for key in (
                "stac.observed_etag",
                "stac.observed_last_modified",
                "stac.observed_content_length",
            )
        ):
            findings.add(Finding("STAC_ERROR_METADATA_INVALID", "/payload/attributes"))

    return findings


def validate_document(candidate: object) -> ProfileValidationResult:
    base = validate_base_document(candidate)
    if base.outcome != "PASS":
        return ProfileValidationResult(
            base.outcome,
            tuple(base.findings),
            event_id=base.event_id,
            payload_spec_hash=base.payload_spec_hash,
        )
    if not isinstance(candidate, Mapping):
        return ProfileValidationResult("DENY", (Finding("ROOT_TYPE", "/"),))
    payload = _mapping(candidate.get("payload"))
    attributes = _mapping(payload.get("attributes"))
    schema_findings = _profile_schema_findings(attributes)
    if schema_findings:
        return ProfileValidationResult(
            "DENY",
            tuple(sorted(schema_findings)),
            event_id=base.event_id,
            payload_spec_hash=base.payload_spec_hash,
        )
    findings = _semantic_findings(candidate)
    return ProfileValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        event_id=base.event_id,
        payload_spec_hash=base.payload_spec_hash,
    )


def validate_file(path: Path) -> ProfileValidationResult:
    candidate, findings = _load_json_object(path)
    if candidate is None:
        return ProfileValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_document(candidate)


def _serialize(path: Path | None, result: ProfileValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "event_id": result.event_id,
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path is not None else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": NON_EFFECTS,
            "outcome": result.outcome,
            "payload_spec_hash": result.payload_spec_hash,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _decode_pointer_part(value: str) -> str:
    return value.replace("~1", "/").replace("~0", "~")


def _apply_fixture_overrides(
    document: dict[str, object], overrides: Mapping[str, object]
) -> None:
    for pointer in sorted(overrides):
        if not pointer.startswith("/"):
            raise ValueError("fixture override pointer must start with '/'")
        parts = [_decode_pointer_part(part) for part in pointer[1:].split("/")]
        target: object = document
        for part in parts[:-1]:
            if not isinstance(target, dict) or part not in target:
                raise ValueError(f"fixture override target does not exist: {pointer}")
            target = target[part]
        if not isinstance(target, dict) or not parts[-1] or parts[-1] not in target:
            raise ValueError(f"fixture override target does not exist: {pointer}")
        target[parts[-1]] = copy.deepcopy(overrides[pointer])


def materialize_fixture_case(
    base_document: Mapping[str, object], case: Mapping[str, object]
) -> dict[str, object]:
    """Expand one compact fixture descriptor and recompute derived identity."""
    document = copy.deepcopy(dict(base_document))
    overrides = case.get("overrides")
    if not isinstance(overrides, Mapping):
        raise ValueError("fixture overrides must be an object")
    _apply_fixture_overrides(document, overrides)
    payload = document.get("payload")
    if not isinstance(payload, dict):
        raise ValueError("fixture payload must be an object")
    attributes = payload.get("attributes")
    if not isinstance(attributes, dict):
        raise ValueError("fixture attributes must be an object")
    payload["payload_spec_hash"] = compute_spec_hash(attributes)
    document["event_id"] = _expected_event_id(document)
    return document


def _load_fixture_cases() -> tuple[
    Mapping[str, object] | None, list[Mapping[str, object]], list[dict[str, str]]
]:
    candidate, findings = _load_json_object(FIXTURE_PATH)
    if candidate is None:
        return None, [], [
            {"code": finding.code, "path": finding.path}
            for finding in findings
        ]
    base_document = candidate.get("base_document")
    if not isinstance(base_document, Mapping):
        return None, [], [{"code": "FIXTURE_BASE_INVALID", "path": "/base_document"}]
    raw_cases = candidate.get("cases")
    if not isinstance(raw_cases, list):
        return None, [], [{"code": "FIXTURE_CASES_INVALID", "path": "/cases"}]
    cases = [case for case in raw_cases if isinstance(case, Mapping)]
    if len(cases) != len(raw_cases):
        return None, [], [{"code": "FIXTURE_CASE_INVALID", "path": "/cases"}]
    return base_document, cases, []


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    base_document, cases, load_findings = _load_fixture_cases()
    failures: list[dict[str, object]] = list(load_findings)
    seen: set[str] = set()
    for case in cases:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id or case_id in seen:
            failures.append({"case_id": case_id, "code": "FIXTURE_ID_INVALID"})
            continue
        seen.add(case_id)
        try:
            if base_document is None:
                raise ValueError("fixture base is unavailable")
            document = materialize_fixture_case(base_document, case)
        except (KeyError, TypeError, ValueError):
            failures.append({"case_id": case_id, "code": "FIXTURE_MATERIALIZATION_ERROR"})
            continue
        result = validate_document(document)
        actual_findings = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        if result.outcome != case.get("expected_outcome") or actual_findings != case.get(
            "expected_findings"
        ):
            failures.append(
                {
                    "case_id": case_id,
                    "actual_outcome": result.outcome,
                    "expected_outcome": case.get("expected_outcome"),
                    "actual_findings": actual_findings,
                    "expected_findings": case.get("expected_findings"),
                }
            )
    payload = {
        "authority": "NONE",
        "cases": len(cases),
        "execution_mode": "FIXTURE_ONLY",
        "failures": failures,
        "non_effects": NON_EFFECTS,
        "outcome": "PASS" if not failures else "DENY",
        "scope": SCOPE,
    }
    return not failures, payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if args.candidate is None:
        parser.error("candidate is required unless --fixtures is used")
    result = validate_file(args.candidate)
    print(_serialize(args.candidate, result))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
