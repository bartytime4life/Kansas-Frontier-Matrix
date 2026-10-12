#!/usr/bin/env python3
"""Validate fixture-only sensitive-overlay gatehouse preflight summaries.

The profile consumes synthetic verification summaries, never raw consent,
Passport, Visa, access-token, identity-token, or genomic payloads. A clean
result is HOLD because this repository slice does not parse tokens, verify
signatures, resolve issuer trust, evaluate policy, sign receipts, start jobs,
emit artifacts, release, or publish.
"""

from __future__ import annotations

import argparse
import copy
import hmac
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(HASHING_SRC))

from hashing import compute_spec_hash  # noqa: E402
from tools.validators._common.public_safe_fixture import (  # noqa: E402
    validate_fixture_file,
)

SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/"
    "sensitive_overlay_gatehouse_preflight.schema.json"
)
FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/"
    "sensitive_overlay_gatehouse_preflight/cases.json"
)
PROFILE = "kfm.sensitive-overlay-gatehouse-preflight.fixture.v1"
MAX_CONSENT_TTL = timedelta(hours=24)
TILE_MEDIA_TYPES = frozenset(
    {"application/vnd.pmtiles", "application/vnd.mapbox-vector-tile"}
)
HOLDS = (
    "RAW_TOKEN_PARSING_UNWIRED",
    "CRYPTOGRAPHIC_TOKEN_VERIFICATION_UNWIRED",
    "ISSUER_AND_SOURCE_TRUST_CONFIGURATION_UNWIRED",
    "DUO_POLICY_EVALUATION_UNWIRED",
    "SIGNED_RECEIPT_EMISSION_UNWIRED",
    "TRE_ATTESTATION_AND_JOB_EXECUTION_UNWIRED",
    "RELEASE_AUTHORIZATION_NOT_EVALUATED",
)
NON_EFFECTS = (
    "no_raw_token_or_genomic_material",
    "no_network_or_key_fetch",
    "no_policy_evaluation",
    "no_job_start_or_artifact_emission",
    "no_signed_receipt",
    "no_release_deployment_publication_or_public_use",
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]


def _json_pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


@lru_cache(maxsize=1)
def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _parse_datetime(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed.astimezone(timezone.utc)


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("preflight_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_preflight_id(spec_hash: str) -> str:
    return (
        "kfm:sensitive-overlay-gatehouse-preflight:"
        + spec_hash.removeprefix("sha256:")[:24]
    )


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code, path))


def _consent_findings(
    document: Mapping[str, Any], evaluated_at: datetime, findings: set[Finding]
) -> None:
    consent = document["consent"]
    assert isinstance(consent, Mapping)
    if consent["verification_status"] != "VERIFIED":
        _add(findings, "CONSENT_VERIFICATION_UNCERTAIN", "/consent/verification_status")
    if consent["status"] != "ACTIVE":
        _add(findings, "CONSENT_NOT_ACTIVE", "/consent/status")
    if consent["token_hash"] is None:
        _add(findings, "CONSENT_TOKEN_HASH_REQUIRED", "/consent/token_hash")
    if consent["consent_receipt_ref"] is None:
        _add(findings, "CONSENT_RECEIPT_REQUIRED", "/consent/consent_receipt_ref")
    if consent["audience"] != "restricted_steward":
        _add(findings, "CONSENT_AUDIENCE_MISMATCH", "/consent/audience")
    if "restricted_genealogy_overlay" not in consent["scopes"]:
        _add(findings, "CONSENT_SCOPE_MISMATCH", "/consent/scopes")
    if consent["revoked"] is True:
        _add(findings, "CONSENT_REVOKED", "/consent/revoked")
    elif consent["revoked"] is not False:
        _add(findings, "CONSENT_REVOCATION_UNCERTAIN", "/consent/revoked")

    issued_at = _parse_datetime(consent["issued_at"])
    expires_at = _parse_datetime(consent["expires_at"])
    checked_at = _parse_datetime(consent["revocation_checked_at"])
    if issued_at is None or expires_at is None:
        _add(findings, "CONSENT_INTERVAL_UNRESOLVED", "/consent")
    elif issued_at > evaluated_at:
        _add(findings, "CONSENT_NOT_YET_VALID", "/consent/issued_at")
    elif evaluated_at >= expires_at:
        _add(findings, "CONSENT_EXPIRED", "/consent/expires_at")
    elif expires_at - issued_at > MAX_CONSENT_TTL:
        _add(findings, "CONSENT_TTL_EXCEEDED", "/consent/expires_at")
    elif evaluated_at + timedelta(seconds=document["requested_ttl_seconds"]) > expires_at:
        _add(findings, "CONSENT_TTL_INSUFFICIENT", "/consent/expires_at")
    if checked_at is None or checked_at != evaluated_at:
        _add(findings, "CONSENT_REVOCATION_CHECK_UNRESOLVED", "/consent/revocation_checked_at")


def _identity_findings(
    document: Mapping[str, Any], evaluated_at: datetime, findings: set[Finding]
) -> None:
    identity = document["identity"]
    assert isinstance(identity, Mapping)
    if identity["passport_hash"] is None:
        _add(findings, "PASSPORT_HASH_REQUIRED", "/identity/passport_hash")
    if identity["signature_status"] != "VERIFIED":
        _add(findings, "PASSPORT_SIGNATURE_UNCERTAIN", "/identity/signature_status")
    if identity["broker_trust"] != "VERIFIED":
        _add(findings, "PASSPORT_BROKER_TRUST_UNCERTAIN", "/identity/broker_trust")
    if identity["audience_match"] is not True:
        _add(findings, "PASSPORT_AUDIENCE_MISMATCH", "/identity/audience_match")
    if identity["visa_identity_link"] != "VERIFIED":
        _add(findings, "VISA_IDENTITY_LINK_UNCERTAIN", "/identity/visa_identity_link")

    passport_expires = _parse_datetime(identity["expires_at"])
    if passport_expires is None:
        _add(findings, "PASSPORT_EXPIRY_UNRESOLVED", "/identity/expires_at")
    elif evaluated_at >= passport_expires:
        _add(findings, "PASSPORT_EXPIRED", "/identity/expires_at")
    elif (
        evaluated_at + timedelta(seconds=document["requested_ttl_seconds"])
        > passport_expires
    ):
        _add(findings, "PASSPORT_TTL_INSUFFICIENT", "/identity/expires_at")

    controlled_grant_present = False
    for index, visa in enumerate(identity["visas"]):
        assert isinstance(visa, Mapping)
        base = f"/identity/visas/{index}"
        if visa["type"] == "ControlledAccessGrants":
            controlled_grant_present = True
            if visa["value_ref"] != document["target_ref"]:
                _add(findings, "VISA_TARGET_MISMATCH", f"{base}/value_ref")
        if visa["signature_status"] != "VERIFIED":
            _add(findings, "VISA_SIGNATURE_UNCERTAIN", f"{base}/signature_status")
        if visa["issuer_trust"] != "VERIFIED":
            _add(findings, "VISA_ISSUER_TRUST_UNCERTAIN", f"{base}/issuer_trust")
        if visa["source_trust"] != "VERIFIED":
            _add(findings, "VISA_SOURCE_TRUST_UNCERTAIN", f"{base}/source_trust")
        if visa["revocation_status"] != "CURRENT":
            _add(findings, "VISA_REVOCATION_UNCERTAIN", f"{base}/revocation_status")
        if visa["conditions_status"] != "SATISFIED":
            _add(findings, "VISA_CONDITIONS_UNSATISFIED", f"{base}/conditions_status")
        visa_expires = _parse_datetime(visa["expires_at"])
        if visa_expires is None:
            _add(findings, "VISA_EXPIRY_UNRESOLVED", f"{base}/expires_at")
        elif evaluated_at >= visa_expires:
            _add(findings, "VISA_EXPIRED", f"{base}/expires_at")
        elif (
            evaluated_at + timedelta(seconds=document["requested_ttl_seconds"])
            > visa_expires
        ):
            _add(findings, "VISA_TTL_INSUFFICIENT", f"{base}/expires_at")
    if not controlled_grant_present:
        _add(findings, "CONTROLLED_ACCESS_GRANT_REQUIRED", "/identity/visas")


def _data_use_findings(
    document: Mapping[str, Any], evaluated_at: datetime, findings: set[Finding]
) -> None:
    data_use = document["data_use"]
    assert isinstance(data_use, Mapping)
    if data_use["match_status"] != "VERIFIED":
        _add(findings, "DUO_MATCH_UNCERTAIN", "/data_use/match_status")
    if data_use["evaluator_ref"] is None:
        _add(findings, "DUO_EVALUATOR_REQUIRED", "/data_use/evaluator_ref")
    if data_use["ontology_digest"] is None:
        _add(findings, "DUO_ONTOLOGY_DIGEST_REQUIRED", "/data_use/ontology_digest")
    if _parse_datetime(data_use["evaluated_at"]) != evaluated_at:
        _add(findings, "DUO_EVALUATION_TIME_UNBOUND", "/data_use/evaluated_at")


def _egress_findings(document: Mapping[str, Any], findings: set[Finding]) -> None:
    egress = document["egress"]
    assert isinstance(egress, Mapping)
    if egress["execution_environment"] != "SYNTHETIC_TRE":
        _add(findings, "TRE_ENVIRONMENT_UNCERTAIN", "/egress/execution_environment")
    if egress["artifact_class"] != "MAP_TILES_ONLY":
        _add(findings, "TILE_ONLY_EGRESS_REQUIRED", "/egress/artifact_class")
    if egress["media_type"] not in TILE_MEDIA_TYPES:
        _add(findings, "TILE_MEDIA_TYPE_REQUIRED", "/egress/media_type")
    if egress["contains_raw_genomic_material"]:
        _add(findings, "RAW_GENOMIC_EGRESS_DENIED", "/egress/contains_raw_genomic_material")
    if egress["contains_row_level_data"]:
        _add(findings, "ROW_LEVEL_EGRESS_DENIED", "/egress/contains_row_level_data")
    if egress["contains_direct_identifiers"]:
        _add(findings, "DIRECT_IDENTIFIER_EGRESS_DENIED", "/egress/contains_direct_identifiers")
    if egress["outbound_network"]:
        _add(findings, "OUTBOUND_NETWORK_DENIED", "/egress/outbound_network")
    if egress["public_exposure"]:
        _add(findings, "PUBLIC_EXPOSURE_DENIED", "/egress/public_exposure")
    if egress["release_state"] != "NOT_RELEASED":
        _add(findings, "RELEASE_STATE_DENIED", "/egress/release_state")


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return ValidationResult(
            "DENY",
            (Finding("GATEHOUSE_SCHEMA_INVALID", _json_pointer(errors[0].absolute_path)),),
        )

    evaluated_at = _parse_datetime(document["evaluated_at"])
    assert evaluated_at is not None
    findings: set[Finding] = set()
    _consent_findings(document, evaluated_at, findings)
    _identity_findings(document, evaluated_at, findings)
    _data_use_findings(document, evaluated_at, findings)
    _egress_findings(document, findings)

    actual_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], actual_hash):
        _add(findings, "GATEHOUSE_SPEC_HASH_MISMATCH", "/spec_hash")
    actual_id = expected_preflight_id(actual_hash)
    if not hmac.compare_digest(document["preflight_id"], actual_id):
        _add(findings, "GATEHOUSE_ID_MISMATCH", "/preflight_id")
    return ValidationResult("DENY" if findings else "HOLD", tuple(sorted(findings)))


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError("fixture mutation path must be an absolute JSON pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    if isinstance(cursor, list):
        cursor[int(parts[-1])] = value
    else:
        cursor[parts[-1]] = value


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    for field in case.get("remove", []):
        document.pop(field, None)
    document["spec_hash"] = expected_spec_hash(document)
    document["preflight_id"] = expected_preflight_id(document["spec_hash"])
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "preflight_id_override" in case:
        document["preflight_id"] = case["preflight_id_override"]
    if "additional_field" in case:
        field = case["additional_field"]
        document[field["name"]] = field["value"]
    return document


def render_result(result: ValidationResult) -> str:
    return json.dumps(
        {
            "outcome": result.outcome,
            "authority": "NONE",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "holds": list(HOLDS),
            "non_effects": list(NON_EFFECTS),
            "profile": PROFILE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(
        json.dumps(
            {"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures},
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def _load_bounded_document(path: Path) -> tuple[Mapping[str, Any] | None, bool]:
    captured: dict[str, object] = {}

    def capture(candidate: object) -> list[Any]:
        captured["candidate"] = candidate
        return []

    parser_findings = validate_fixture_file(path, capture)
    candidate = captured.get("candidate")
    if parser_findings or not isinstance(candidate, Mapping):
        return None, False
    return candidate, True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.path is None:
        raise SystemExit("path is required unless --fixtures is used")
    document, parsed = _load_bounded_document(args.path)
    result = (
        validate_payload(document)
        if parsed and document is not None
        else ValidationResult("DENY", (Finding("GATEHOUSE_INPUT_INVALID", "/"),))
    )
    print(render_result(result))
    return 0 if result.outcome == "HOLD" else 1


if __name__ == "__main__":
    raise SystemExit(main())
