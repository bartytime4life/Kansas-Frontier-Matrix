"""Validate bounded fixture-only external-service operation receipt candidates.

The validator checks declaration, consumption, dependency, replay, disclosure,
and deterministic-identity coherence only. It never calls an external service,
authenticates billing, resolves evidence, decides policy or review, promotes,
releases, deploys, or publishes.
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
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/evidence/external_service_operation_receipt.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/evidence/external_service_operation_receipt/cases.json"
)
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "CONSUMPTION_UNRESOLVED",
    "OPERATION_INCOMPLETE",
    "REFERENCE_UNRESOLVED",
    "REPLAY_POLICY_UNRESOLVED",
    "SERVICE_VERSION_UNRESOLVED",
}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_COST_AUTHENTICATION",
    "NO_EVIDENCE_RESOLUTION",
    "NO_EXTERNAL_OPERATION",
    "NO_PUBLICATION_AUTHORITY",
]
PUBLIC_USE = "PUBLIC_CLAIM_SUPPORT_CANDIDATE"


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


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
    subject.pop("receipt_ref", None)
    return canonical_hash(subject)


def expected_receipt_ref(profile_hash: str) -> str:
    return "kfm:external-service-operation-receipt:" + profile_hash.removeprefix(
        "sha256:"
    )


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
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


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    expected_hash = compute_profile_hash(candidate)
    if candidate.get("profile_spec_hash") != expected_hash:
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("receipt_ref") != expected_receipt_ref(expected_hash):
        findings.add(Finding("RECEIPT_REF_MISMATCH", "/receipt_ref"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    operation = candidate["operation"]
    consumption = candidate["consumption"]
    dependency = candidate["dependency"]
    replay = candidate["replay"]
    disclosure = candidate["disclosure"]
    limitations = candidate["limitations"]
    assert isinstance(operation, Mapping)
    assert isinstance(consumption, Mapping)
    assert isinstance(dependency, Mapping)
    assert isinstance(replay, Mapping)
    assert isinstance(disclosure, Mapping)

    if not _canonical_strings(limitations):
        findings.add(Finding("LIMITATIONS_NOT_CANONICAL", "/limitations"))
    if limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    if not _canonical_strings(replay.get("limitations")):
        findings.add(Finding("REPLAY_LIMITATIONS_NOT_CANONICAL", "/replay/limitations"))
    for field in ("evidence_bundle_refs", "review_record_refs"):
        if not _canonical_strings(disclosure.get(field)):
            findings.add(
                Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/disclosure/{field}")
            )

    for field in (
        "platform_descriptor",
        "operation_spec",
        "input_snapshot",
        "output_artifact",
    ):
        reference = operation[field]
        assert isinstance(reference, Mapping)
        if reference.get("resolution") == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/operation/{field}"))

    version = operation["service_version"]
    assert isinstance(version, Mapping)
    if version.get("resolution") == "RESOLVED":
        if version.get("value") is None:
            findings.add(
                Finding("SERVICE_VERSION_REQUIRED", "/operation/service_version/value")
            )
    elif version.get("value") is not None:
        findings.add(
            Finding(
                "SERVICE_VERSION_RESOLUTION_MISMATCH",
                "/operation/service_version/value",
            )
        )
    else:
        findings.add(
            Finding(
                "SERVICE_VERSION_UNRESOLVED",
                "/operation/service_version/resolution",
            )
        )

    operation_state = candidate.get("operation_state")
    if operation_state == "ERROR":
        findings.add(Finding("OPERATION_ERROR", "/operation_state"))
        return sorted(findings)
    if operation_state == "INCOMPLETE":
        findings.add(Finding("OPERATION_INCOMPLETE", "/operation_state"))
        return sorted(findings)

    status = consumption.get("status")
    credit = consumption.get("credit_quantity")
    cost = consumption.get("cost_minor_units")
    currency = consumption.get("currency")
    measurement_ref = consumption.get("measurement_ref")
    pricing_ref = consumption.get("pricing_ref")
    has_value = credit is not None or cost is not None

    if (cost is None) != (currency is None):
        findings.add(
            Finding("COST_CURRENCY_PAIR_REQUIRED", "/consumption/cost_minor_units")
        )
    if status == "MEASURED":
        if not has_value:
            findings.add(
                Finding("MEASURED_CONSUMPTION_VALUE_REQUIRED", "/consumption/status")
            )
        if measurement_ref is None:
            findings.add(
                Finding(
                    "MEASUREMENT_REFERENCE_REQUIRED",
                    "/consumption/measurement_ref",
                )
            )
    elif status == "ESTIMATED":
        if not has_value:
            findings.add(
                Finding("ESTIMATED_CONSUMPTION_VALUE_REQUIRED", "/consumption/status")
            )
        if pricing_ref is None:
            findings.add(
                Finding("PRICING_REFERENCE_REQUIRED", "/consumption/pricing_ref")
            )
    elif status == "NOT_CHARGED":
        if any(
            value is not None
            for value in (credit, cost, currency, measurement_ref, pricing_ref)
        ):
            findings.add(
                Finding(
                    "NOT_CHARGED_FIELDS_MUST_BE_EMPTY",
                    "/consumption",
                )
            )
    elif status == "UNRESOLVED":
        if any(
            value is not None
            for value in (credit, cost, currency, measurement_ref, pricing_ref)
        ):
            findings.add(
                Finding(
                    "UNRESOLVED_CONSUMPTION_FIELDS_PRESENT",
                    "/consumption",
                )
            )
        else:
            findings.add(Finding("CONSUMPTION_UNRESOLVED", "/consumption/status"))

    replay_posture = replay.get("posture")
    replay_policy_ref = replay.get("policy_ref")
    if replay_posture == "UNRESOLVED":
        if replay_policy_ref is not None:
            findings.add(
                Finding(
                    "UNRESOLVED_REPLAY_POLICY_PRESENT",
                    "/replay/policy_ref",
                )
            )
        else:
            findings.add(Finding("REPLAY_POLICY_UNRESOLVED", "/replay/posture"))
    elif replay_policy_ref is None:
        findings.add(Finding("REPLAY_POLICY_REQUIRED", "/replay/policy_ref"))
    if replay_posture == "GOVERNED_REPLACEMENT" and dependency.get("vendor_locked"):
        findings.add(
            Finding(
                "REPLACEMENT_VENDOR_LOCK_CONFLICT",
                "/dependency/vendor_locked",
            )
        )

    caveat = disclosure.get("external_service_cost_caveat")
    if status != "NOT_CHARGED" and (
        not isinstance(caveat, str) or caveat.strip() != caveat
    ):
        findings.add(
            Finding(
                "EXTERNAL_SERVICE_COST_CAVEAT_REQUIRED",
                "/disclosure/external_service_cost_caveat",
            )
        )

    if candidate.get("intended_use") == PUBLIC_USE:
        if not isinstance(caveat, str) or caveat.strip() != caveat:
            findings.add(
                Finding(
                    "PUBLIC_COST_CAVEAT_REQUIRED",
                    "/disclosure/external_service_cost_caveat",
                )
            )
        if not disclosure.get("evidence_bundle_refs"):
            findings.add(
                Finding(
                    "PUBLIC_EVIDENCE_REFERENCE_REQUIRED",
                    "/disclosure/evidence_bundle_refs",
                )
            )
        if not disclosure.get("review_record_refs"):
            findings.add(
                Finding(
                    "PUBLIC_REVIEW_REFERENCE_REQUIRED",
                    "/disclosure/review_record_refs",
                )
            )
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if "OPERATION_ERROR" in codes:
        outcome = "ERROR"
    elif not codes:
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
        target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    profile_hash = compute_profile_hash(candidate)
    candidate["profile_spec_hash"] = profile_hash
    candidate["receipt_ref"] = expected_receipt_ref(profile_hash)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    if entry.get("tamper") == "receipt_ref":
        candidate["receipt_ref"] = (
            "kfm:external-service-operation-receipt:" + "f" * 64
        )
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {
                    "outcome": "ERROR",
                    "codes": sorted({finding.code for finding in load_findings}),
                },
            }
        ]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        assert isinstance(entry, Mapping)
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append(
            {
                "name": entry["name"],
                "ok": observed == expected,
                "expected": expected,
                "observed": observed,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only external-service operation receipts."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, load_findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(load_findings))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(
        json.dumps(
            {
                "outcome": result.outcome,
                "findings": [
                    {"code": finding.code, "field": finding.field}
                    for finding in result.findings
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
