#!/usr/bin/env python3
"""Validate one fixture-first MapReleaseManifest without network access."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/map_release_manifest.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/map/map_release_manifest"
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "map-release-manifest-fixture-profile-only"

REF_ARRAY_FIELDS = (
    "layer_manifest_refs",
    "style_manifest_refs",
    "evidence_refs",
    "policy_decision_refs",
    "rights_refs",
    "sensitivity_refs",
    "review_refs",
    "attestation_refs",
    "redaction_receipt_refs",
)
HOLD_REASONS = {
    "RIGHTS_UNRESOLVED",
    "SENSITIVITY_UNRESOLVED",
    "EVIDENCE_INCOMPLETE",
    "POLICY_UNRESOLVED",
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
    findings: tuple[Finding, ...]
    release_state: str | None = None

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def operational_error(self) -> bool:
        return any(
            finding.code.startswith(("INPUT_", "JSON_", "SCHEMA_UNAVAILABLE"))
            for finding in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
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
        return None, [Finding("INPUT_READ_ERROR", "/")]
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
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("map_release_id", None)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def expected_map_release_id(candidate: Mapping[str, Any]) -> str:
    return "map-release:" + canonical_spec_hash(candidate).removeprefix("sha256:")[:24]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _canonical_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _parse_utc(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo == timezone.utc else None


def _floating_ref(value: str) -> bool:
    lowered = value.lower()
    return (
        lowered.endswith(":latest")
        or "/latest" in lowered
        or "tag=latest" in lowered
        or "@latest" in lowered
    )


def _set_pointer(payload: Any, pointer: str, value: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.lstrip("/").split("/")
        if part
    ]
    if not parts:
        raise ValueError("root replacement is not supported")
    current = payload
    for part in parts[:-1]:
        if isinstance(current, list):
            current = current[int(part)]
        elif isinstance(current, dict):
            current = current[part]
        else:
            raise ValueError(f"cannot traverse patch path {pointer}")
    final = parts[-1]
    if isinstance(current, list):
        current[int(final)] = copy.deepcopy(value)
    elif isinstance(current, dict):
        current[final] = copy.deepcopy(value)
    else:
        raise ValueError(f"cannot set patch path {pointer}")


def materialize_case(cases: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    base = cases.get("base_payload")
    if not isinstance(base, dict):
        raise ValueError("base_payload must be an object")
    payload = copy.deepcopy(base)
    for patch in _array(case.get("patches")):
        if not isinstance(patch, dict) or not isinstance(patch.get("path"), str):
            raise ValueError("case patch must contain a path")
        _set_pointer(payload, patch["path"], patch.get("value"))
    payload["spec_hash"] = canonical_spec_hash(payload)
    payload["map_release_id"] = expected_map_release_id(payload)
    for patch in _array(case.get("post_identity_patches")):
        if not isinstance(patch, dict) or not isinstance(patch.get("path"), str):
            raise ValueError("post-identity patch must contain a path")
        _set_pointer(payload, patch["path"], patch.get("value"))
    return payload


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        if candidate.get("spec_hash") != canonical_spec_hash(candidate):
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("map_release_id") != expected_map_release_id(candidate):
            findings.append(Finding("MAP_RELEASE_ID_MISMATCH", "/map_release_id"))
    except (TypeError, ValueError, RecursionError):
        findings.append(Finding("IDENTITY_COMPUTATION_ERROR", "/"))

    for field in REF_ARRAY_FIELDS:
        if not _canonical_strings(_array(candidate.get(field))):
            findings.append(Finding(f"{field.upper()}_NOT_CANONICAL", f"/{field}"))

    reasons = _array(candidate.get("state_reason_codes"))
    if not _canonical_strings(reasons):
        findings.append(Finding("STATE_REASON_CODES_NOT_CANONICAL", "/state_reason_codes"))
    reason_set = {item for item in reasons if isinstance(item, str)}

    catalogs = _mapping(candidate.get("catalog_refs"))
    for name in ("stac", "dcat", "prov"):
        if not _canonical_strings(_array(catalogs.get(name))):
            findings.append(Finding("CATALOG_REFS_NOT_CANONICAL", f"/catalog_refs/{name}"))

    artifacts = _array(candidate.get("artifact_manifests"))
    artifact_ids: list[str] = []
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            continue
        artifact_id = artifact.get("artifact_id")
        if isinstance(artifact_id, str):
            artifact_ids.append(artifact_id)
        artifact_ref = artifact.get("artifact_ref")
        if isinstance(artifact_ref, str) and _floating_ref(artifact_ref):
            findings.append(Finding("FLOATING_ARTIFACT_REF_DENIED", f"/artifact_manifests/{index}/artifact_ref"))
    if artifact_ids != sorted(set(artifact_ids)) or len(artifact_ids) != len(artifacts):
        findings.append(Finding("ARTIFACT_MANIFESTS_NOT_CANONICAL", "/artifact_manifests"))

    state = candidate.get("release_state")
    published_at = candidate.get("published_at")
    public = _mapping(candidate.get("public_boundary"))
    correction = _mapping(candidate.get("correction"))
    rollback = _mapping(candidate.get("rollback"))
    redaction_refs = _array(candidate.get("redaction_receipt_refs"))

    if public.get("geometry_posture") in {"GENERALIZED", "RESTRICTED", "WITHHELD"} and not redaction_refs:
        findings.append(Finding("REDACTION_RECEIPT_REQUIRED", "/redaction_receipt_refs"))

    if state == "PUBLISHED":
        required_arrays = {
            "artifact_manifests": artifacts,
            "layer_manifest_refs": _array(candidate.get("layer_manifest_refs")),
            "style_manifest_refs": _array(candidate.get("style_manifest_refs")),
            "evidence_refs": _array(candidate.get("evidence_refs")),
            "policy_decision_refs": _array(candidate.get("policy_decision_refs")),
            "rights_refs": _array(candidate.get("rights_refs")),
            "sensitivity_refs": _array(candidate.get("sensitivity_refs")),
            "review_refs": _array(candidate.get("review_refs")),
            "attestation_refs": _array(candidate.get("attestation_refs")),
        }
        for field, values in required_arrays.items():
            if not values:
                findings.append(Finding("PUBLISHED_CLOSURE_INCOMPLETE", f"/{field}"))
        for name in ("stac", "dcat", "prov"):
            if not _array(catalogs.get(name)):
                findings.append(Finding("PUBLISHED_CATALOG_CLOSURE_INCOMPLETE", f"/catalog_refs/{name}"))
        if _parse_utc(published_at) is None:
            findings.append(Finding("PUBLISHED_AT_REQUIRED", "/published_at"))
        if public.get("rights_state") in {"UNKNOWN", "DENIED"}:
            findings.append(Finding("PUBLISHED_RIGHTS_NOT_RESOLVED", "/public_boundary/rights_state"))
        if public.get("sensitivity_state") in {"UNKNOWN", "DENIED"}:
            findings.append(Finding("PUBLISHED_SENSITIVITY_NOT_RESOLVED", "/public_boundary/sensitivity_state"))
        if rollback.get("rollback_target_ref") is None or rollback.get("rollback_card_ref") is None:
            findings.append(Finding("PUBLISHED_ROLLBACK_CLOSURE_REQUIRED", "/rollback"))
        if rollback.get("verified") is not True:
            findings.append(Finding("PUBLISHED_ROLLBACK_VERIFICATION_REQUIRED", "/rollback/verified"))
        if "RELEASE_CLOSED" not in reason_set:
            findings.append(Finding("PUBLISHED_REASON_REQUIRED", "/state_reason_codes"))
        for index, artifact in enumerate(artifacts):
            if not isinstance(artifact, dict):
                continue
            if artifact.get("artifact_type") in {"PMTILES", "COG"}:
                if artifact.get("range_supported") is not True:
                    findings.append(Finding("RANGE_SUPPORT_REQUIRED", f"/artifact_manifests/{index}/range_supported"))
                if artifact.get("cors_allowed") is not True:
                    findings.append(Finding("CORS_SUPPORT_REQUIRED", f"/artifact_manifests/{index}/cors_allowed"))
    else:
        if published_at is not None and state in {"CANDIDATE", "HELD"}:
            findings.append(Finding("UNPUBLISHED_STATE_HAS_PUBLISHED_AT", "/published_at"))

    if state == "CANDIDATE" and "CANDIDATE_PENDING_REVIEW" not in reason_set:
        findings.append(Finding("CANDIDATE_REASON_REQUIRED", "/state_reason_codes"))
    elif state == "HELD" and not (reason_set & HOLD_REASONS):
        findings.append(Finding("HELD_REASON_REQUIRED", "/state_reason_codes"))
    elif state == "STALE" and "STALE_RELEASE" not in reason_set:
        findings.append(Finding("STALE_REASON_REQUIRED", "/state_reason_codes"))
    elif state == "SUPERSEDED":
        if correction.get("superseded_by_ref") is None:
            findings.append(Finding("SUPERSEDED_BY_REF_REQUIRED", "/correction/superseded_by_ref"))
        if not _array(correction.get("cache_invalidation_refs")):
            findings.append(Finding("CACHE_INVALIDATION_REQUIRED", "/correction/cache_invalidation_refs"))
        if "SUPERSEDED_BY_NEW_RELEASE" not in reason_set:
            findings.append(Finding("SUPERSEDED_REASON_REQUIRED", "/state_reason_codes"))
    elif state == "WITHDRAWN":
        if correction.get("withdrawal_notice_ref") is None:
            findings.append(Finding("WITHDRAWAL_NOTICE_REQUIRED", "/correction/withdrawal_notice_ref"))
        if not _array(correction.get("cache_invalidation_refs")):
            findings.append(Finding("CACHE_INVALIDATION_REQUIRED", "/correction/cache_invalidation_refs"))
        if "WITHDRAWN_BY_STEWARD" not in reason_set:
            findings.append(Finding("WITHDRAWN_REASON_REQUIRED", "/state_reason_codes"))
    elif state == "ROLLED_BACK":
        if rollback.get("rollback_target_ref") is None or rollback.get("rollback_card_ref") is None:
            findings.append(Finding("ROLLBACK_REFERENCES_REQUIRED", "/rollback"))
        if rollback.get("verified") is not True:
            findings.append(Finding("ROLLBACK_VERIFICATION_REQUIRED", "/rollback/verified"))
        if rollback.get("restoration_receipt_ref") is None:
            findings.append(Finding("RESTORATION_RECEIPT_REQUIRED", "/rollback/restoration_receipt_ref"))
        if not _array(correction.get("cache_invalidation_refs")):
            findings.append(Finding("CACHE_INVALIDATION_REQUIRED", "/correction/cache_invalidation_refs"))
        if "ROLLBACK_EXECUTED" not in reason_set:
            findings.append(Finding("ROLLED_BACK_REASON_REQUIRED", "/state_reason_codes"))

    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    state = candidate.get("release_state")
    return ValidationResult(
        tuple(sorted(set(findings))),
        state if isinstance(state, str) else None,
    )


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": "PASS" if result.ok else "ERROR" if result.operational_error else "FAIL",
            "release_state": result.release_state,
            "scope": SCOPE,
            "authority": {
                "network_fetch": False,
                "artifact_load": False,
                "evidence_resolution": False,
                "policy_evaluation": False,
                "release_authorization": False,
                "cache_invalidation": False,
                "rollback_execution": False,
                "publication": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    try:
        cases = json.loads((FIXTURE_ROOT / "cases.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 2
    valid_cases = cases.get("valid_cases") if isinstance(cases, dict) else None
    invalid_cases = cases.get("invalid_cases") if isinstance(cases, dict) else None
    if not isinstance(valid_cases, list) or not isinstance(invalid_cases, list):
        return 2
    if not valid_cases or not invalid_cases:
        return 2
    passed = True
    for case in valid_cases:
        if not isinstance(case, dict):
            return 2
        name = str(case.get("name", "valid"))
        path = Path(f"fixture:valid:{name}")
        try:
            payload = materialize_case(cases, case)
        except (KeyError, TypeError, ValueError, IndexError):
            return 2
        result = validate_payload(payload)
        print(_serialize(path, result))
        if not result.ok or result.release_state != case.get("expected_state"):
            passed = False
    for case in invalid_cases:
        if not isinstance(case, dict):
            return 2
        name = str(case.get("name", "invalid"))
        path = Path(f"fixture:invalid:{name}")
        try:
            payload = materialize_case(cases, case)
        except (KeyError, TypeError, ValueError, IndexError):
            return 2
        result = validate_payload(payload)
        print(_serialize(path, result))
        expected = sorted(case.get("expected_codes", []))
        actual = sorted({finding.code for finding in result.findings})
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "file": name,
                        "expected_codes": expected,
                        "actual_codes": actual,
                        "outcome": "FIXTURE_EXPECTATION_MISMATCH",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate one fixture-first MapReleaseManifest.")
    parser.add_argument("path", nargs="?")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return run_fixture_profile()
    if not args.path:
        parser.error("path is required unless --fixtures is used")
    path = Path(args.path)
    result = validate_file(path)
    print(_serialize(path, result))
    if result.ok:
        return 0
    return 2 if result.operational_error else 1


if __name__ == "__main__":
    raise SystemExit(main())
