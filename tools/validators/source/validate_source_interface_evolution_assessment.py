#!/usr/bin/env python3
"""Validate fixture-only source-interface evolution assessment candidates."""
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
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(HASHING_SRC))

from hashing import compute_spec_hash

SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/source/source_interface_evolution_assessment.schema.json"
)
FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/source/source_interface_evolution_assessment/cases.json"
)
MAX_JSON_BYTES = 1024 * 1024


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
    assessment_state: str | None
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


def _json_pointer(parts: Iterable[object]) -> str:
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1") for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _finding(code: str, path: str) -> Finding:
    return Finding(code, path)


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    digest = spec_hash.removeprefix("sha256:")
    return f"kfm:source-interface-evolution:{digest[:24]}"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _canonical(values: Sequence[str]) -> bool:
    return list(values) == sorted(set(values))


def _timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _latest_observation(document: Mapping[str, Any]) -> Mapping[str, Any]:
    return max(
        document["observations"],
        key=lambda item: (_timestamp(item["observed_at"]), item["observation_id"]),
    )


def expected_compatibility(document: Mapping[str, Any]) -> dict[str, Any]:
    declared = document["source_interface"]
    latest = _latest_observation(document)
    declared_capabilities = set(declared["declared_capabilities"])
    observed_capabilities = set(latest["capabilities"])
    added = sorted(observed_capabilities - declared_capabilities)
    removed = sorted(declared_capabilities - observed_capabilities)

    if latest["canonical_identity_ref"] != declared["canonical_identity_ref"]:
        classification = "INCOMPARABLE"
        reason_code = "CANONICAL_IDENTITY_MISMATCH"
    elif latest["redirect_target_ref"] is not None:
        classification = "REDIRECTED"
        reason_code = "REDIRECT_OBSERVED"
    elif latest["scope"] != "FULL_CONTRACT":
        classification = "PARTIAL_SAMPLE"
        reason_code = "OBSERVATION_SCOPE_INCOMPLETE"
    elif removed:
        classification = "BREAKING"
        reason_code = "CAPABILITY_REMOVED"
    elif added:
        classification = "ADDITIVE"
        reason_code = "CAPABILITY_ADDED"
    elif (
        latest["observed_profile_ref"] == declared["declared_profile_ref"]
        and latest["observed_version"] == declared["declared_version"]
    ):
        classification = "UNCHANGED"
        reason_code = "DECLARED_INTERFACE_MATCH"
    else:
        classification = "UNDOCUMENTED"
        reason_code = "DECLARATION_DRIFT"

    return {
        "latest_observation_id": latest["observation_id"],
        "classification": classification,
        "reason_code": reason_code,
        "added_capabilities": added,
        "removed_capabilities": removed,
        "comparison_evidence_refs": [latest["evidence_ref"]],
        "declared_identity_preserved": (
            latest["canonical_identity_ref"]
            == declared["canonical_identity_ref"]
        ),
        "observed_identity_authoritative": False,
    }


def _blocked_or_unknown(document: Mapping[str, Any]) -> list[str]:
    return sorted(
        consumer["consumer_id"]
        for consumer in document["consumers"]
        if consumer["status"] in {"BLOCKED", "UNKNOWN"}
    )


def expected_migration_fields(document: Mapping[str, Any]) -> dict[str, Any]:
    latest = _latest_observation(document)
    classification = expected_compatibility(document)["classification"]
    dual_read = document["migration"]["dual_read"]
    rollback_ref = document["migration"]["rollback_ref"]
    blocked = _blocked_or_unknown(document)
    asserted_state = latest["asserted_state"]

    if asserted_state == "RETIRED_ASSERTED":
        disposition = (
            "HOLD" if blocked else "PROPOSE_RETIREMENT_REVIEW"
        )
        blockers = blocked
    elif asserted_state in {
        "REACTIVATED_ASSERTED",
        "DEPRECATED",
        "SUNSET_SIGNALLED",
    }:
        disposition = "HOLD"
        blockers = []
    elif blocked:
        disposition = "HOLD"
        blockers = []
    elif classification == "UNCHANGED":
        disposition = "NO_CHANGE"
        blockers = []
    elif classification == "ADDITIVE":
        disposition = "PROPOSE_MIGRATION" if rollback_ref else "HOLD"
        blockers = []
    elif classification == "BREAKING":
        if not dual_read["enabled"] or dual_read["parity_status"] == "NOT_RUN":
            disposition = "PROPOSE_DUAL_READ"
        elif dual_read["parity_status"] == "MATCH" and rollback_ref:
            disposition = "PROPOSE_MIGRATION"
        elif dual_read["parity_status"] == "MISMATCH" and rollback_ref:
            disposition = "PROPOSE_ROLLBACK"
        else:
            disposition = "HOLD"
        blockers = []
    else:
        disposition = "HOLD"
        blockers = []

    return {"disposition": disposition, "retirement_blockers": blockers}


def expected_summary(document: Mapping[str, Any]) -> dict[str, Any]:
    latest = _latest_observation(document)
    blocked = _blocked_or_unknown(document)
    affected = sorted(
        consumer["consumer_id"]
        for consumer in document["consumers"]
        if (
            consumer["current_profile_ref"]
            != consumer["target_profile_ref"]
            or consumer["status"] != "READY"
        )
    )
    disposition = expected_migration_fields(document)["disposition"]
    asserted_state = latest["asserted_state"]

    if asserted_state == "RETIRED_ASSERTED":
        readiness = "BLOCKED" if blocked else "READY_FOR_SEPARATE_GATE"
    elif asserted_state in {
        "DEPRECATED",
        "SUNSET_SIGNALLED",
        "REACTIVATED_ASSERTED",
    }:
        readiness = "HOLD"
    else:
        readiness = "NOT_REQUESTED"

    state_by_disposition = {
        "NO_CHANGE": "UNCHANGED",
        "HOLD": "MIGRATION_HELD",
        "PROPOSE_DUAL_READ": "DUAL_READ_CANDIDATE",
        "PROPOSE_MIGRATION": "MIGRATION_CANDIDATE",
        "PROPOSE_ROLLBACK": "ROLLBACK_CANDIDATE",
        "PROPOSE_RETIREMENT_REVIEW": "RETIREMENT_REVIEW_CANDIDATE",
    }
    if disposition == "NO_CHANGE" and expected_compatibility(document)[
        "classification"
    ] != "UNCHANGED":
        assessment_state = "CHANGE_RECORDED"
    else:
        assessment_state = state_by_disposition[disposition]

    return {
        "observation_count": len(document["observations"]),
        "affected_consumer_ids": affected,
        "affected_consumer_count": len(affected),
        "blocked_or_unknown_consumer_ids": blocked,
        "retirement_readiness": readiness,
        "assessment_state": assessment_state,
        "trusted_surface_allowed": False,
    }


def _canonical_findings(document: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    declared = document["source_interface"]
    if not _canonical(declared["declared_capabilities"]):
        findings.append(
            _finding(
                "INTERFACE_DECLARED_CAPABILITY_ORDER_INVALID",
                "/source_interface/declared_capabilities",
            )
        )

    observations = document["observations"]
    expected_order = sorted(
        observations,
        key=lambda item: (_timestamp(item["observed_at"]), item["observation_id"]),
    )
    if observations != expected_order:
        findings.append(
            _finding("INTERFACE_OBSERVATION_ORDER_INVALID", "/observations")
        )
    observation_ids = [item["observation_id"] for item in observations]
    if len(observation_ids) != len(set(observation_ids)):
        findings.append(
            _finding("INTERFACE_OBSERVATION_ID_DUPLICATE", "/observations")
        )
    for index, observation in enumerate(observations):
        if not _canonical(observation["capabilities"]):
            findings.append(
                _finding(
                    "INTERFACE_OBSERVED_CAPABILITY_ORDER_INVALID",
                    f"/observations/{index}/capabilities",
                )
            )
        for field in ("response_shape_hash", "transport_fingerprint"):
            if observation[field] == "sha256:" + "0" * 64:
                findings.append(
                    _finding(
                        "INTERFACE_OBSERVATION_HASH_PLACEHOLDER",
                        f"/observations/{index}/{field}",
                    )
                )

    consumers = document["consumers"]
    if consumers != sorted(consumers, key=lambda item: item["consumer_id"]):
        findings.append(
            _finding("INTERFACE_CONSUMER_ORDER_INVALID", "/consumers")
        )
    consumer_ids = [item["consumer_id"] for item in consumers]
    if len(consumer_ids) != len(set(consumer_ids)):
        findings.append(
            _finding("INTERFACE_CONSUMER_ID_DUPLICATE", "/consumers")
        )
    for index, consumer in enumerate(consumers):
        for field in ("evidence_refs", "debt_refs"):
            if not _canonical(consumer[field]):
                findings.append(
                    _finding(
                        "INTERFACE_CONSUMER_REFERENCE_ORDER_INVALID",
                        f"/consumers/{index}/{field}",
                    )
                )

    if _timestamp(document["assessed_at"]) < _timestamp(
        _latest_observation(document)["observed_at"]
    ):
        findings.append(
            _finding("INTERFACE_ASSESSMENT_TIME_INVALID", "/assessed_at")
        )
    return findings


def _dual_read_findings(document: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    latest = _latest_observation(document)
    declared = document["source_interface"]
    dual_read = document["migration"]["dual_read"]
    classification = expected_compatibility(document)["classification"]
    asserted_state = latest["asserted_state"]

    if dual_read["enabled"]:
        if (
            dual_read["old_profile_ref"] != declared["declared_profile_ref"]
            or dual_read["new_profile_ref"] != latest["observed_profile_ref"]
            or not dual_read["evidence_refs"]
            or not _canonical(dual_read["evidence_refs"])
        ):
            findings.append(
                _finding(
                    "INTERFACE_DUAL_READ_BINDING_INVALID",
                    "/migration/dual_read",
                )
            )
    elif (
        dual_read["old_profile_ref"] is not None
        or dual_read["new_profile_ref"] is not None
        or dual_read["evidence_refs"]
        or dual_read["parity_status"] != "NOT_RUN"
    ):
        findings.append(
            _finding(
                "INTERFACE_DUAL_READ_DISABLED_STATE_INVALID",
                "/migration/dual_read",
            )
        )

    if (
        classification == "BREAKING"
        and asserted_state
        not in {"RETIRED_ASSERTED", "REACTIVATED_ASSERTED"}
        and not dual_read["enabled"]
    ):
        findings.append(
            _finding(
                "INTERFACE_BREAKING_CHANGE_WITHOUT_DUAL_READ",
                "/migration/dual_read/enabled",
            )
        )
    if (
        document["migration"]["disposition"]
        in {"PROPOSE_MIGRATION", "PROPOSE_ROLLBACK"}
        and document["migration"]["rollback_ref"] is None
    ):
        findings.append(
            _finding(
                "INTERFACE_ROLLBACK_REFERENCE_REQUIRED",
                "/migration/rollback_ref",
            )
        )
    return findings


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (
            _json_pointer(error.absolute_path),
            str(error.validator),
        ),
    )
    if errors:
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "INTERFACE_EVOLUTION_SCHEMA_INVALID",
                    _json_pointer(errors[0].absolute_path),
                ),
            ),
        )

    canonical_findings = _canonical_findings(document)
    if canonical_findings:
        return ValidationResult(
            "DENY",
            None,
            tuple(sorted(canonical_findings, key=lambda item: (item.path, item.code))),
        )

    latest = _latest_observation(document)
    if (
        latest["canonical_identity_ref"]
        != document["source_interface"]["canonical_identity_ref"]
    ):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "INTERFACE_CANONICAL_IDENTITY_CHANGED",
                    "/compatibility/declared_identity_preserved",
                ),
            ),
        )

    expected_compat = expected_compatibility(document)
    if document["compatibility"] != expected_compat:
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "INTERFACE_COMPATIBILITY_MISMATCH", "/compatibility"
                ),
            ),
        )

    expected_target = latest["observed_profile_ref"]
    if any(
        consumer["target_profile_ref"] != expected_target
        for consumer in document["consumers"]
    ):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "INTERFACE_CONSUMER_TARGET_UNBOUND", "/consumers"
                ),
            ),
        )

    dual_read_findings = _dual_read_findings(document)
    if dual_read_findings:
        return ValidationResult(
            "DENY",
            None,
            tuple(sorted(dual_read_findings, key=lambda item: (item.path, item.code))),
        )

    expected_migration = expected_migration_fields(document)
    if (
        document["migration"]["disposition"]
        != expected_migration["disposition"]
        or document["migration"]["retirement_blockers"]
        != expected_migration["retirement_blockers"]
    ):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding("INTERFACE_MIGRATION_MISMATCH", "/migration"),
            ),
        )

    expected_summary_value = expected_summary(document)
    if document["summary"] != expected_summary_value:
        return ValidationResult(
            "DENY",
            None,
            (
                _finding("INTERFACE_SUMMARY_MISMATCH", "/summary"),
            ),
        )

    actual_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], actual_hash):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding("INTERFACE_SPEC_HASH_MISMATCH", "/spec_hash"),
            ),
        )
    actual_id = expected_assessment_id(actual_hash)
    if not hmac.compare_digest(document["assessment_id"], actual_id):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding("INTERFACE_ASSESSMENT_ID_MISMATCH", "/assessment_id"),
            ),
        )
    return ValidationResult(
        "PASS", document["summary"]["assessment_state"], ()
    )


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError("fixture mutation path must be an absolute JSON pointer")
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer[1:].split("/")
    ]
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


def materialize_case(
    manifest: Mapping[str, Any], case: Mapping[str, Any]
) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])

    if not case.get("preserve_compatibility"):
        document["compatibility"] = expected_compatibility(document)
    if not case.get("preserve_migration"):
        expected = expected_migration_fields(document)
        document["migration"]["disposition"] = expected["disposition"]
        document["migration"]["retirement_blockers"] = expected[
            "retirement_blockers"
        ]
    if not case.get("preserve_summary"):
        document["summary"] = expected_summary(document)

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
        actual_findings = [
            {"code": item.code, "path": item.path} for item in result.findings
        ]
        if (
            result.status != case["expected_status"]
            or result.assessment_state != case["expected_assessment_state"]
            or actual_findings != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_status": case["expected_status"],
                    "actual_status": result.status,
                    "expected_assessment_state": case[
                        "expected_assessment_state"
                    ],
                    "actual_assessment_state": result.assessment_state,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual_findings,
                }
            )
    print(
        json.dumps(
            {
                "cases": len(manifest["cases"]),
                "failures": failures,
                "suite_match": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
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
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_DUPLICATE_KEY", "/"),)
        )
    except NonFiniteNumberError:
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_NONFINITE_NUMBER", "/"),)
        )
    except InputSymlinkError:
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_INPUT_SYMLINK_DENIED", "/"),)
        )
    except InputTooLargeError:
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_INPUT_TOO_LARGE", "/"),)
        )
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        ValueError,
        RecursionError,
    ):
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_INPUT_INVALID", "/"),)
        )
    print(
        json.dumps(
            {
                "status": result.status,
                "assessment_state": result.assessment_state,
                "findings": [
                    {"code": item.code, "path": item.path}
                    for item in result.findings
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
