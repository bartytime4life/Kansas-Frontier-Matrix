"""Validate fixture-only, license-respectful web delta profiles.

This profile is carried inside the existing ``SourceEventEnvelopeCandidate``
rather than creating a parallel event authority. A passing result proves only
bounded local shape, deterministic base-envelope integrity, source binding,
HTTP-state coherence, and license/payload-mode consistency. It performs no
network fetch, extraction, policy evaluation, source activation, lifecycle
write, release, publication, or public use.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators.validate_source_event_envelope import (
    Finding,
    MAX_FILE_BYTES,
    _load_json_object,
    validate_document as validate_base_document,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "source"
    / "web_delta_profile.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures"
    / "contracts"
    / "v1"
    / "source"
    / "web_delta_profile"
)
FIXTURE_FILES = tuple(sorted(FIXTURE_ROOT.glob("cases-*.json")))
MAX_SCHEMA_FINDINGS = 100
SCOPE = "source.web_delta_profile"
NON_EFFECTS = (
    "no_network_fetch_or_extraction",
    "no_cloudevents_conformance_claim",
    "no_source_activation",
    "no_raw_or_lifecycle_write",
    "no_evidence_policy_or_review_creation",
    "no_promotion_release_deployment_or_publication",
)
HASH_PREFIX = "sha256:"
ZERO_HASH = HASH_PREFIX + "0" * 64


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
        return {Finding("WEB_PROFILE_SCHEMA_UNAVAILABLE", "/payload/attributes")}
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
            "WEB_PROFILE_SCHEMA_INVALID",
            _json_pointer(tuple(error.absolute_path), "/payload/attributes"),
        )
        for error in errors
    }
    if truncated:
        findings.add(Finding("WEB_PROFILE_SCHEMA_FINDINGS_TRUNCATED", "/payload/attributes"))
    return findings


def _is_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 71
        and value.startswith(HASH_PREFIX)
        and all(character in "0123456789abcdef" for character in value[7:])
    )


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


def _license_rights_state(license_state: object) -> str | None:
    return {
        "permissive": "KNOWN",
        "restrictive": "KNOWN",
        "ambiguous": "CONFLICTED",
        "unknown": "UNKNOWN",
    }.get(license_state) if isinstance(license_state, str) else None


def _metadata_reason(license_state: object) -> str | None:
    return {
        "restrictive": "LICENSE_RESTRICTIVE_METADATA_ONLY",
        "ambiguous": "LICENSE_AMBIGUOUS_METADATA_ONLY",
        "unknown": "LICENSE_UNKNOWN_METADATA_ONLY",
    }.get(license_state) if isinstance(license_state, str) else None


def _semantic_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    payload = _mapping(candidate.get("payload"))
    attrs = _mapping(payload.get("attributes"))
    subject = _mapping(candidate.get("subject"))
    routing = _mapping(candidate.get("routing"))
    governance = _mapping(candidate.get("governance"))
    reasons = set(_string_list(routing.get("reason_codes")))

    canonical_url = attrs.get("web.canonical_url")
    source_pointer = attrs.get("web.source_pointer")
    if canonical_url != source_pointer or canonical_url != subject.get("subject_ref"):
        findings.add(Finding("WEB_RESOURCE_BINDING_INVALID", "/payload/attributes/web.canonical_url"))
    if not _safe_https_url(canonical_url):
        findings.add(Finding("WEB_URL_UNSAFE", "/payload/attributes/web.canonical_url"))

    etag_present = attrs.get("web.etag_present")
    last_modified_present = attrs.get("web.last_modified_present")
    if etag_present != (subject.get("etag") is not None):
        findings.add(Finding("HTTP_VALIDATOR_FLAG_MISMATCH", "/payload/attributes/web.etag_present"))
    if last_modified_present != (subject.get("last_modified") is not None):
        findings.add(Finding("HTTP_VALIDATOR_FLAG_MISMATCH", "/payload/attributes/web.last_modified_present"))

    expected_rights = _license_rights_state(attrs.get("web.license_state"))
    if expected_rights is not None and governance.get("rights_state") != expected_rights:
        findings.add(Finding("LICENSE_RIGHTS_STATE_MISMATCH", "/governance/rights_state"))

    for key in (
        "web.raw_digest",
        "web.canonical_old_ref",
        "web.canonical_new_digest",
        "web.diff_digest",
        "web.manifest_digest",
    ):
        value = attrs.get(key)
        if value == ZERO_HASH:
            findings.add(Finding("DIGEST_PLACEHOLDER", f"/payload/attributes/{key}"))

    status = attrs.get("web.http_status")
    mode = attrs.get("web.payload_mode")
    change_kind = attrs.get("web.change_kind")
    severity = attrs.get("web.severity")
    extraction = attrs.get("web.extraction_method")
    event_type = candidate.get("event_type")
    license_state = attrs.get("web.license_state")
    disposition = routing.get("disposition")
    review_required = routing.get("review_required")
    raw_digest = attrs.get("web.raw_digest")
    old_ref = attrs.get("web.canonical_old_ref")
    new_digest = attrs.get("web.canonical_new_digest")
    diff_digest = attrs.get("web.diff_digest")
    notice_fields = attrs.get("web.notice_fields")
    lossy_count = attrs.get("web.lossy_transform_count")

    if status == 304:
        if event_type != "SCHEDULED_POLL":
            findings.add(Finding("HEARTBEAT_EVENT_TYPE_INVALID", "/event_type"))
        if not (
            mode == "heartbeat"
            and change_kind == "unchanged"
            and severity == "none"
            and extraction == "none"
        ):
            findings.add(Finding("HEARTBEAT_STATE_INVALID", "/payload/attributes"))
        if any(value is not None for value in (raw_digest, new_digest, diff_digest)):
            findings.add(Finding("HEARTBEAT_CONTENT_PRESENT", "/payload/attributes"))
        if not etag_present and not last_modified_present:
            findings.add(Finding("HEARTBEAT_VALIDATOR_MISSING", "/payload/attributes"))
        if not (
            disposition == "NO_ACTION"
            and review_required is False
            and {"HTTP_NOT_MODIFIED", "NO_MATERIAL_CHANGE"}.issubset(reasons)
        ):
            findings.add(Finding("HEARTBEAT_ROUTING_INVALID", "/routing"))
        if lossy_count != 0:
            findings.add(Finding("HEARTBEAT_LOSSY_TRANSFORM_INVALID", "/payload/attributes/web.lossy_transform_count"))
    elif status == 200:
        expected_event = {"created": "OBJECT_CREATED", "updated": "OBJECT_UPDATED"}.get(change_kind)
        if expected_event is None or event_type != expected_event:
            findings.add(Finding("WEB_CHANGE_EVENT_TYPE_INVALID", "/event_type"))
        if mode == "heartbeat" or change_kind == "unchanged":
            findings.add(Finding("WEB_CHANGE_STATE_INVALID", "/payload/attributes"))
        if extraction == "none":
            findings.add(Finding("EXTRACTION_METHOD_INVALID", "/payload/attributes/web.extraction_method"))
        if not _is_hash(raw_digest) or raw_digest != subject.get("content_digest"):
            findings.add(Finding("RAW_DIGEST_BINDING_INVALID", "/payload/attributes/web.raw_digest"))

        if mode == "contentful":
            if license_state != "permissive":
                findings.add(Finding("CONTENTFUL_LICENSE_NOT_PERMITTED", "/payload/attributes/web.license_state"))
            if not _is_hash(new_digest) or not _is_hash(diff_digest):
                findings.add(Finding("CONTENTFUL_DIGESTS_MISSING", "/payload/attributes"))
            if notice_fields is not None:
                findings.add(Finding("CONTENTFUL_NOTICE_INVALID", "/payload/attributes/web.notice_fields"))
            if not (
                disposition == "PROPOSE_SOURCE_ADMISSION"
                and review_required is True
                and "LICENSE_PERMISSIVE_CONTENTFUL" in reasons
                and "SOURCE_EVENT_READY_FOR_ADMISSION_REVIEW" in reasons
            ):
                findings.add(Finding("CONTENTFUL_ROUTING_INVALID", "/routing"))
        elif mode == "metadata_only":
            if license_state == "permissive":
                findings.add(Finding("METADATA_ONLY_LICENSE_INVALID", "/payload/attributes/web.license_state"))
            if new_digest is not None or diff_digest is not None:
                findings.add(Finding("METADATA_ONLY_CONTENT_PRESENT", "/payload/attributes"))
            if not isinstance(notice_fields, str) or not notice_fields:
                findings.add(Finding("NOTICE_FIELDS_MISSING", "/payload/attributes/web.notice_fields"))
            else:
                fields = notice_fields.split("|")
                if fields != sorted(set(fields)):
                    findings.add(Finding("NOTICE_FIELDS_ORDER_INVALID", "/payload/attributes/web.notice_fields"))
            expected_reason = _metadata_reason(license_state)
            if not (
                disposition == "PROPOSE_QUARANTINE"
                and review_required is True
                and expected_reason is not None
                and expected_reason in reasons
            ):
                findings.add(Finding("METADATA_ONLY_ROUTING_INVALID", "/routing"))
            if not _string_list(governance.get("policy_refs")):
                findings.add(Finding("METADATA_ONLY_GOVERNANCE_INCOMPLETE", "/governance/policy_refs"))

        if change_kind == "created" and old_ref is not None:
            findings.add(Finding("OLD_REF_STATE_INVALID", "/payload/attributes/web.canonical_old_ref"))
        if change_kind == "updated" and not _is_hash(old_ref):
            findings.add(Finding("OLD_REF_STATE_INVALID", "/payload/attributes/web.canonical_old_ref"))

    if isinstance(lossy_count, int) and lossy_count > 0 and "LOSSY_TRANSFORM_RECORDED" not in reasons:
        findings.add(Finding("LOSSY_TRANSFORM_REASON_MISSING", "/routing/reason_codes"))

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
    attrs = _mapping(payload.get("attributes"))
    schema_findings = _profile_schema_findings(attrs)
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


def _load_fixture_cases() -> tuple[list[object], list[dict[str, object]]]:
    cases: list[object] = []
    load_findings: list[dict[str, object]] = []
    if not FIXTURE_FILES:
        return cases, [{"code": "FIXTURE_FILES_MISSING", "path": "/"}]

    for fixture_path in FIXTURE_FILES:
        fixture, findings = _load_json_object(fixture_path)
        if not isinstance(fixture, Mapping):
            load_findings.extend(
                {
                    "code": finding.code,
                    "file": fixture_path.name,
                    "path": finding.path,
                }
                for finding in findings
            )
            if not findings:
                load_findings.append(
                    {
                        "code": "FIXTURE_ROOT_INVALID",
                        "file": fixture_path.name,
                        "path": "/",
                    }
                )
            continue
        file_cases = fixture.get("cases")
        if not isinstance(file_cases, list):
            load_findings.append(
                {
                    "code": "FIXTURE_CASES_INVALID",
                    "file": fixture_path.name,
                    "path": "/cases",
                }
            )
            continue
        cases.extend(file_cases)
    return cases, load_findings


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    cases, suite_findings = _load_fixture_cases()
    if suite_findings:
        return False, {
            "authority": "NONE",
            "cases": len(cases),
            "execution_mode": "FIXTURE_ONLY",
            "findings": suite_findings,
            "non_effects": NON_EFFECTS,
            "outcome": "ERROR",
            "scope": SCOPE,
        }
    suite_findings = []
    for index, case in enumerate(cases):
        if not isinstance(case, Mapping):
            suite_findings.append({
                "case": index,
                "code": "FIXTURE_CASE_INVALID",
                "path": f"/cases/{index}",
            })
            continue
        result = validate_document(case.get("document"))
        actual = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        if result.outcome != case.get("expected_outcome"):
            suite_findings.append({
                "actual": result.outcome,
                "case": case.get("case_id"),
                "code": "FIXTURE_OUTCOME_MISMATCH",
                "expected": case.get("expected_outcome"),
            })
        if actual != case.get("expected_findings"):
            suite_findings.append({
                "actual": actual,
                "case": case.get("case_id"),
                "code": "FIXTURE_FINDINGS_MISMATCH",
                "expected": case.get("expected_findings"),
            })
    payload = {
        "authority": "NONE",
        "cases": len(cases),
        "execution_mode": "FIXTURE_ONLY",
        "findings": suite_findings,
        "non_effects": NON_EFFECTS,
        "outcome": "DENY" if suite_findings else "PASS",
        "scope": SCOPE,
    }
    return not suite_findings, payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only KFM license-respectful web delta profiles."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1

    if not args.files:
        parser.error("provide one or more files or use --fixtures")

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_file(path)
        print(_serialize(path, result))
        failed = failed or result.outcome != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
