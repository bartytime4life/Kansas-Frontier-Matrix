#!/usr/bin/env python3
"""Validate fixture-only offline release capsule closure assessments."""
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

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "packages/hashing/src"))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/runtime/offline_release_capsule_assessment.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/runtime/offline_release_capsule_assessment/cases.json"
MAX_JSON_BYTES = 1024 * 1024
REQUIRED_ROLES = [
    "CITATION_SUMMARY",
    "EVIDENCE_SUMMARY",
    "GLYPH_MANIFEST",
    "PMTILES",
    "POLICY_SNAPSHOT",
    "SPRITE_MANIFEST",
    "STYLE",
    "VERIFICATION_MATERIAL",
]


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
    capsule_state: str | None
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


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    return f"kfm:offline-capsule:{spec_hash.removeprefix('sha256:')[:24]}"


def expected_capsule_assessment(document: Mapping[str, Any]) -> dict[str, Any]:
    capsule = document["capsule"]
    observation = document["observation"]
    missing = sorted(set(capsule["required_artifact_roles"]) - set(observation["present_artifact_roles"]))
    codes: set[str] = set()
    if capsule["correction_delta_ref"] is not None and not observation["correction_applied"]:
        codes.add("CORRECTION_UPDATE_PENDING")
    if observation["observed_manifest_digest"] != capsule["manifest_digest"]:
        codes.add("MANIFEST_DIGEST_MISMATCH")
    if observation["observed_release_id"] != capsule["release_id"]:
        codes.add("RELEASE_ID_MISMATCH")
    if missing:
        codes.add("REQUIRED_ARTIFACT_MISSING")
    if _parse_time(document["assessed_at"]) > _parse_time(capsule["trust_valid_until"]):
        codes.add("TRUST_FRESHNESS_EXPIRED")
    if observation["install_state"] == "INTERRUPTED":
        codes.add("UPDATE_INTERRUPTED")
    if capsule["withdrawal_delta_ref"] is not None:
        codes.add("WITHDRAWAL_DECLARED")

    if "WITHDRAWAL_DECLARED" in codes:
        state = "WITHDRAWN"
    elif "UPDATE_INTERRUPTED" in codes:
        state = "ROLLBACK_REQUIRED"
    elif codes & {"MANIFEST_DIGEST_MISMATCH", "RELEASE_ID_MISMATCH", "REQUIRED_ARTIFACT_MISSING"}:
        state = "INCOMPLETE"
    elif "TRUST_FRESHNESS_EXPIRED" in codes:
        state = "STALE"
    elif "CORRECTION_UPDATE_PENDING" in codes:
        state = "UPDATE_PENDING"
    else:
        state = "READY_FOR_SEPARATE_INSTALL_REVIEW"

    purge_required = state in {"WITHDRAWN", "ROLLBACK_REQUIRED"}
    reconnect_sync_required = observation["connectivity"] == "RECONNECTED" and bool(codes)
    return {
        "capsule_state": state,
        "finding_codes": sorted(codes),
        "missing_artifact_roles": missing,
        "purge_required": purge_required,
        "reconnect_sync_required": reconnect_sync_required,
        "trusted_render_allowed": False,
        "install_allowed": False,
        "separate_release_review_required": True,
    }


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _deny(code: str, path: str, capsule_state: str | None = None) -> ValidationResult:
    return ValidationResult("DENY", capsule_state, (Finding(code, path),))


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return _deny("OFFLINE_CAPSULE_SCHEMA_INVALID", _pointer(errors[0].absolute_path))

    capsule = document["capsule"]
    observation = document["observation"]
    if capsule["required_artifact_roles"] != REQUIRED_ROLES:
        return _deny("OFFLINE_CAPSULE_REQUIRED_ROLES_INVALID", "/capsule/required_artifact_roles")
    if observation["present_artifact_roles"] != sorted(set(observation["present_artifact_roles"])):
        return _deny("OFFLINE_CAPSULE_INVENTORY_NOT_CANONICAL", "/observation/present_artifact_roles")

    installed = _parse_time(capsule["installed_at"])
    verified = _parse_time(capsule["last_verified_at"])
    valid_until = _parse_time(capsule["trust_valid_until"])
    assessed = _parse_time(document["assessed_at"])
    if not installed <= verified <= assessed:
        return _deny("OFFLINE_CAPSULE_TIME_ORDER_INVALID", "/capsule/last_verified_at")
    if valid_until < verified:
        return _deny("OFFLINE_CAPSULE_TRUST_WINDOW_INVALID", "/capsule/trust_valid_until")
    if observation["correction_applied"] and capsule["correction_delta_ref"] is None:
        return _deny("OFFLINE_CAPSULE_CORRECTION_BINDING_INVALID", "/observation/correction_applied")
    if observation["withdrawal_applied"] and capsule["withdrawal_delta_ref"] is None:
        return _deny("OFFLINE_CAPSULE_WITHDRAWAL_BINDING_INVALID", "/observation/withdrawal_applied")
    if observation["install_state"] == "ROLLED_BACK" and capsule["rollback_release_ref"] is None:
        return _deny("OFFLINE_CAPSULE_ROLLBACK_BINDING_INVALID", "/capsule/rollback_release_ref")

    expected = expected_capsule_assessment(document)
    if document["capsule_assessment"] != expected:
        return _deny("OFFLINE_CAPSULE_REPORT_MISMATCH", "/capsule_assessment", expected["capsule_state"])
    spec_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], spec_hash):
        return _deny("OFFLINE_CAPSULE_SPEC_HASH_MISMATCH", "/spec_hash")
    assessment_id = expected_assessment_id(spec_hash)
    if not hmac.compare_digest(document["assessment_id"], assessment_id):
        return _deny("OFFLINE_CAPSULE_ID_MISMATCH", "/assessment_id")
    return ValidationResult("PASS", expected["capsule_state"], ())


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
        document["capsule_assessment"] = expected_capsule_assessment(document)
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
        value = json.load(
            stream,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
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
            or result.capsule_state != case["expected_capsule_state"]
            or actual_findings != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "actual_status": result.status,
                    "actual_capsule_state": result.capsule_state,
                    "actual_findings": actual_findings,
                }
            )
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
    print(json.dumps({"status": result.status, "capsule_state": result.capsule_state, "findings": [{"code": item.code, "path": item.path} for item in result.findings]}, sort_keys=True, separators=(",", ":")))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
