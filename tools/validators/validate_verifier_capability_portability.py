#!/usr/bin/env python3
"""Validate fixture-only verifier capability portability assessments."""
from __future__ import annotations

import argparse
import copy
import hmac
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "packages/hashing/src"))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/evidence/verifier_capability_portability.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/evidence/verifier_capability_portability/cases.json"
MAX_JSON_BYTES = 1024 * 1024

UNSUPPORTED_CODES = {
    "ALGORITHM_UNSUPPORTED",
    "CLOCK_UNAVAILABLE",
    "NETWORK_CAPABILITY_UNAVAILABLE",
    "RESOURCE_CAPACITY_INSUFFICIENT",
    "RESOURCE_EXHAUSTED",
    "REVOCATION_INPUT_UNAVAILABLE",
}
INCOMPARABLE_CODES = {
    "CANONICALIZATION_PROFILE_MISMATCH",
    "DEPENDENCY_PROFILE_DRIFT",
    "TIME_SOURCE_MISMATCH",
    "TRUST_MATERIAL_MISMATCH",
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class InputSymlinkError(ValueError):
    pass


class InputTooLargeError(ValueError):
    pass


@dataclass(frozen=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    portability_status: str | None
    findings: tuple[Finding, ...]


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _canonical_dependencies(values: Sequence[Mapping[str, Any]]) -> bool:
    names = [item["name"] for item in values]
    return names == sorted(set(names))


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    return f"kfm:verifier-portability:{spec_hash.removeprefix('sha256:')[:24]}"


def capability_finding_codes(document: Mapping[str, Any]) -> list[str]:
    profile = document["verifier_profile"]
    claim = document["capability_claim"]
    attempt = document["verification_attempt"]
    codes: set[str] = set()

    if profile["required_algorithm"] not in claim["supported_algorithms"]:
        codes.add("ALGORITHM_UNSUPPORTED")
    if profile["required_canonicalization"] not in claim["supported_canonicalization_profiles"]:
        codes.add("CANONICALIZATION_PROFILE_MISMATCH")
    if profile["trust_material_digest"] != claim["trust_material_digest"]:
        codes.add("TRUST_MATERIAL_MISMATCH")
    if _parse_time(document["assessed_at"]) > _parse_time(claim["trust_valid_until"]):
        codes.add("TRUST_MATERIAL_STALE")
    if profile["revocation_required"] and (
        claim["revocation_input_digest"] is None
        or claim["revocation_input_digest"] != profile["revocation_input_digest"]
    ):
        codes.add("REVOCATION_INPUT_UNAVAILABLE")
    if profile["dependencies"] != claim["dependency_versions"]:
        codes.add("DEPENDENCY_PROFILE_DRIFT")
    if claim["time_source"] == "UNAVAILABLE":
        codes.add("CLOCK_UNAVAILABLE")
    elif profile["time_source"] != claim["time_source"]:
        codes.add("TIME_SOURCE_MISMATCH")
    if profile["network_requirement"] == "REQUIRED" and not claim["network_available"]:
        codes.add("NETWORK_CAPABILITY_UNAVAILABLE")

    required = profile["required_capacity"]
    limits = claim["resource_limits"]
    usage = attempt["resource_usage"]
    if any(limits[key] < required[key] for key in required):
        codes.add("RESOURCE_CAPACITY_INSUFFICIENT")
    if any(usage[key] > limits[key] for key in limits):
        codes.add("RESOURCE_EXHAUSTED")
    return sorted(codes)


def expected_portability_assessment(document: Mapping[str, Any]) -> dict[str, Any]:
    codes = capability_finding_codes(document)
    if set(codes) & UNSUPPORTED_CODES:
        status = "UNSUPPORTED"
    elif set(codes) & INCOMPARABLE_CODES:
        status = "INCOMPARABLE"
    elif "TRUST_MATERIAL_STALE" in codes:
        status = "QUALIFIED"
    else:
        status = "PORTABLE"
    return {
        "portability_status": status,
        "finding_codes": codes,
        "equivalent_verification_claimed": False,
        "trusted_result_allowed": False,
        "separate_security_review_required": True,
    }


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _deny(code: str, path: str, portability_status: str | None = None) -> ValidationResult:
    return ValidationResult("DENY", portability_status, (Finding(code, path),))


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return _deny("VERIFIER_PORTABILITY_SCHEMA_INVALID", _pointer(errors[0].absolute_path))

    profile = document["verifier_profile"]
    claim = document["capability_claim"]
    attempt = document["verification_attempt"]
    if attempt["profile_ref"] != profile["profile_ref"]:
        return _deny("VERIFIER_PORTABILITY_PROFILE_BINDING_MISMATCH", "/verification_attempt/profile_ref")
    if (
        attempt["algorithm"] != profile["required_algorithm"]
        or attempt["canonicalization_profile"] != profile["required_canonicalization"]
    ):
        return _deny("VERIFIER_PORTABILITY_ATTEMPT_BINDING_MISMATCH", "/verification_attempt")
    if not _canonical_dependencies(profile["dependencies"]):
        return _deny("VERIFIER_PORTABILITY_PROFILE_NOT_CANONICAL", "/verifier_profile/dependencies")
    if not _canonical_dependencies(claim["dependency_versions"]):
        return _deny("VERIFIER_PORTABILITY_CLAIM_NOT_CANONICAL", "/capability_claim/dependency_versions")
    for path, values in (
        ("/capability_claim/supported_algorithms", claim["supported_algorithms"]),
        ("/capability_claim/supported_canonicalization_profiles", claim["supported_canonicalization_profiles"]),
        ("/verification_attempt/attempted_checks", attempt["attempted_checks"]),
    ):
        if values != sorted(set(values)):
            return _deny("VERIFIER_PORTABILITY_CLAIM_NOT_CANONICAL", path)

    expected = expected_portability_assessment(document)
    if document["portability_assessment"] != expected:
        return _deny("VERIFIER_PORTABILITY_REPORT_MISMATCH", "/portability_assessment", expected["portability_status"])

    spec_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], spec_hash):
        return _deny("VERIFIER_PORTABILITY_SPEC_HASH_MISMATCH", "/spec_hash")
    assessment_id = expected_assessment_id(spec_hash)
    if not hmac.compare_digest(document["assessment_id"], assessment_id):
        return _deny("VERIFIER_PORTABILITY_ID_MISMATCH", "/assessment_id")
    return ValidationResult("PASS", expected["portability_status"], ())


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    final = parts[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = value
    else:
        cursor[final] = value


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest root must be an object")
    return value


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if case.get("recompute_assessment"):
        document["portability_assessment"] = expected_portability_assessment(document)
    document["spec_hash"] = expected_spec_hash(document)
    document["assessment_id"] = expected_assessment_id(document["spec_hash"])
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "assessment_id_override" in case:
        document["assessment_id"] = case["assessment_id_override"]
    return document


def _load_document(path: Path) -> Mapping[str, Any]:
    if path.is_symlink():
        raise InputSymlinkError
    if not path.is_file():
        raise OSError
    if path.stat().st_size > MAX_JSON_BYTES:
        raise InputTooLargeError
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream, object_pairs_hook=_unique_object, parse_constant=_reject_constant, parse_float=_finite_float)
    if not isinstance(value, dict):
        raise ValueError("candidate root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual_findings = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.status != case["expected_status"]
            or result.portability_status != case["expected_portability_status"]
            or actual_findings != case["expected_findings"]
        ):
            failures.append({"case_id": case["case_id"], "actual_status": result.status, "actual_portability_status": result.portability_status, "actual_findings": actual_findings})
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


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
    try:
        result = validate_payload(_load_document(args.path))
    except DuplicateKeyError:
        result = ValidationResult("ERROR", None, (Finding("JSON_DUPLICATE_KEY", "/"),))
    except NonFiniteNumberError:
        result = ValidationResult("ERROR", None, (Finding("JSON_NONFINITE_NUMBER", "/"),))
    except InputSymlinkError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_SYMLINK_DENIED", "/"),))
    except InputTooLargeError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_TOO_LARGE", "/"),))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_INVALID", "/"),))
    print(json.dumps({"status": result.status, "portability_status": result.portability_status, "findings": [{"code": item.code, "path": item.path} for item in result.findings]}, sort_keys=True, separators=(",", ":")))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
