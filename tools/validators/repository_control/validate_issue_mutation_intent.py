#!/usr/bin/env python3
"""Validate fixture-only, target-pinned repository issue mutation intents.

This module has no GitHub client, network path, credential input, or external
writer. Declared attempts and readbacks are synthetic contract fixtures only.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
for dependency_path in (REPO_ROOT, REPO_ROOT / "packages/hashing/src"):
    if str(dependency_path) not in sys.path:
        sys.path.insert(0, str(dependency_path))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/repository_issue_mutation_intent.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT / "fixtures/contracts/v1/governance/repository_issue_mutation_intent"
)
CASES_PATH = FIXTURE_ROOT / "cases.json"
VALID_PATH = FIXTURE_ROOT / "valid/valid_already_satisfied_no_op.json"
INVALID_PATHS = (
    FIXTURE_ROOT / "invalid/invalid_action_chaining.json",
    FIXTURE_ROOT / "invalid/invalid_ambiguous_target.json",
    FIXTURE_ROOT / "invalid/invalid_unsupported_action.json",
)
OBJECT_TYPE = "RepositoryIssueMutationIntentCandidate"
PROFILE = "kfm.governance.repository-control.issue-mutation-intent.v1"
EXECUTION_MODE = "FIXTURE_ONLY_DECLARATION"
SCOPE = "governance.repository_control.issue_mutation_intent"
NON_EFFECTS = (
    "no_network_access",
    "no_external_mutation",
    "no_live_adapter",
    "no_pull_request_lifecycle_change",
    "no_repository_settings_change",
    "no_release_deployment_promotion_or_publication_change",
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    receipt_id: str | None = None


def _mapping(value: object, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{label} must be an object")
    return value


def _time(value: object, label: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label} must be an RFC 3339 timestamp")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError(f"{label} must be an RFC 3339 timestamp") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{label} must include a timezone")
    return parsed.astimezone(timezone.utc)


def _path(parts: Sequence[object]) -> str:
    rendered = "$"
    for part in parts:
        rendered += f"[{part}]" if isinstance(part, int) else "." + str(part)
    return rendered


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _deep_merge(base: Any, overrides: Any) -> Any:
    if not isinstance(base, Mapping) or not isinstance(overrides, Mapping):
        return copy.deepcopy(overrides)
    result = copy.deepcopy(dict(base))
    for key, value in overrides.items():
        result[key] = (
            _deep_merge(result[key], value)
            if key in result
            else copy.deepcopy(value)
        )
    return result


def _intent_fingerprint(intent: Mapping[str, Any]) -> str:
    return compute_spec_hash(
        {key: value for key, value in intent.items() if key != "intent_id"}
    )


def _target_fingerprint(intent: Mapping[str, Any]) -> str:
    return compute_spec_hash(
        {"repository": intent["repository"], "target": intent["target"]}
    )


def _readback_fingerprint(readback: Mapping[str, Any] | None) -> str | None:
    return compute_spec_hash(readback) if readback is not None else None


def _attempt_is_not_requested(attempt: Mapping[str, Any]) -> bool:
    return (
        attempt["status"] == "NOT_REQUESTED"
        and attempt["transport"] == "NONE"
        and attempt["request_emitted"] is False
        and attempt["response_status"] is None
        and attempt["error_code"] is None
    )


def _replay_error(
    intent: Mapping[str, Any], preflight: Mapping[str, Any]
) -> str | None:
    replay = preflight["replay"]
    fingerprint = _intent_fingerprint(intent)
    if replay["status"] == "UNSEEN":
        return (
            None
            if all(
                replay[key] is None
                for key in (
                    "idempotency_key",
                    "intent_fingerprint",
                    "previous_outcome",
                )
            )
            else "REPLAY_RECORD_INVALID"
        )
    if (
        replay["idempotency_key"] != intent["idempotency_key"]
        or replay["previous_outcome"] is None
        or replay["intent_fingerprint"] is None
    ):
        return "REPLAY_RECORD_INVALID"
    same = replay["intent_fingerprint"] == fingerprint
    if replay["status"] == "SAME_PARAMETERS":
        return None if same else "REPLAY_RECORD_INVALID"
    if replay["status"] == "DIFFERENT_PARAMETERS":
        return "REPLAY_RECORD_INVALID" if same else "IDEMPOTENCY_KEY_REUSED"
    return "REPLAY_RECORD_INVALID"


def _denial_reason(
    intent: Mapping[str, Any], preflight: Mapping[str, Any], evaluated_at: datetime
) -> str | None:
    if preflight["repository"] != intent["repository"]:
        return "WRONG_REPOSITORY"
    if any(
        preflight["target"][key] != intent["target"][key]
        for key in ("kind", "issue_number", "issue_node_id")
    ):
        return "TARGET_SUBSTITUTION"
    if preflight["target"]["state"] != intent["expected"]["state"]:
        return "STALE_TARGET_STATE"
    if preflight["target"]["revision"] != intent["expected"]["revision"]:
        return "STALE_TARGET_REVISION"

    authority = intent["authority"]
    observed = preflight["authority"]
    if authority["reference"] is None:
        return "MISSING_AUTHORITY"
    if any(
        observed[key] != authority[key]
        for key in ("reference", "actor_class", "expires_at")
    ):
        return "AUTHORITY_MISMATCH"
    if observed["decision"] != "ALLOW":
        return "AUTHORITY_NOT_ALLOWED"
    if _time(authority["expires_at"], "intent.authority.expires_at") <= evaluated_at:
        return "EXPIRED_INTENT"
    return _replay_error(intent, preflight)


def _readback_is_exact(
    intent: Mapping[str, Any],
    preflight: Mapping[str, Any],
    readback: Mapping[str, Any] | None,
    evaluated_at: datetime,
    *,
    applied: bool,
) -> bool:
    if readback is None or readback["repository"] != intent["repository"]:
        return False
    target = readback["target"]
    if any(
        target[key] != intent["target"][key]
        for key in ("kind", "issue_number", "issue_node_id")
    ):
        return False
    if target["state"] != "OPEN" or target["head_sha"] is not None:
        return False

    read_at = _time(readback["observed_at"], "readback.observed_at")
    before_at = _time(preflight["observed_at"], "preflight.observed_at")
    revision = _time(target["revision"], "readback.target.revision")
    before_revision = _time(
        preflight["target"]["revision"], "preflight.target.revision"
    )
    if read_at < before_at or read_at > evaluated_at or revision > read_at:
        return False

    before_labels = sorted(preflight["target"]["labels"])
    expected_labels = (
        sorted(set(before_labels + [intent["action"]["label"]]))
        if applied
        else before_labels
    )
    if sorted(target["labels"]) != expected_labels:
        return False
    return revision > before_revision if applied else revision == before_revision


def derive_receipt(
    evaluated_at_text: str,
    intent: Mapping[str, Any],
    preflight: Mapping[str, Any],
    attempt: Mapping[str, Any],
    readback: Mapping[str, Any] | None,
) -> dict[str, object]:
    evaluated_at = _time(evaluated_at_text, "evaluated_at")
    observed_at = _time(preflight["observed_at"], "preflight.observed_at")
    revision = _time(preflight["target"]["revision"], "preflight.target.revision")
    if observed_at > evaluated_at or revision > observed_at:
        outcome, reasons, status = "ERROR", ["READBACK_MISMATCH"], "UNKNOWN"
    else:
        denial = _denial_reason(intent, preflight, evaluated_at)
        if denial:
            if not _attempt_is_not_requested(attempt) or readback is not None:
                outcome, reasons, status = "ERROR", ["ATTEMPT_AFTER_DENIAL"], "UNKNOWN"
            else:
                outcome, reasons, status = "DENIED", [denial], "NOT_AVAILABLE"
        elif intent["action"]["label"] in preflight["target"]["labels"]:
            if not _attempt_is_not_requested(attempt) or not _readback_is_exact(
                intent, preflight, readback, evaluated_at, applied=False
            ):
                outcome, reasons, status = "ERROR", ["READBACK_MISMATCH"], "UNKNOWN"
            else:
                replayed = preflight["replay"]["status"] == "SAME_PARAMETERS"
                outcome, status = "NO_OP", "EXACT"
                reasons = [
                    "REPLAY_CONVERGED" if replayed else "ACTION_ALREADY_SATISFIED"
                ]
        elif preflight["replay"]["status"] == "SAME_PARAMETERS":
            outcome, reasons, status = (
                "ERROR",
                ["REPLAY_STATE_DIVERGENCE"],
                "UNKNOWN",
            )
        elif attempt["status"] == "FAILED":
            coherent = (
                attempt["transport"] == "DECLARED_GITHUB_API"
                and attempt["request_emitted"] is True
                and attempt["response_status"] is None
                and attempt["error_code"] is not None
                and readback is None
            )
            outcome, reasons, status = (
                ("ERROR", ["TRANSPORT_FAILURE"], "UNKNOWN")
                if coherent
                else ("ERROR", ["READBACK_MISMATCH"], "UNKNOWN")
            )
        elif attempt["status"] == "ATTEMPTED":
            coherent = (
                attempt["transport"] == "DECLARED_GITHUB_API"
                and attempt["request_emitted"] is True
                and attempt["response_status"] is None
                and attempt["error_code"] is None
                and readback is None
            )
            outcome, reasons, status = (
                ("ATTEMPTED", ["ACTION_ATTEMPT_RECORDED"], "NOT_AVAILABLE")
                if coherent
                else ("ERROR", ["READBACK_MISMATCH"], "UNKNOWN")
            )
        elif attempt["status"] == "SUCCEEDED":
            coherent = (
                attempt["transport"] == "DECLARED_GITHUB_API"
                and attempt["request_emitted"] is True
                and attempt["response_status"] == 200
                and attempt["error_code"] is None
                and _readback_is_exact(
                    intent, preflight, readback, evaluated_at, applied=True
                )
            )
            outcome, reasons, status = (
                ("APPLIED", ["ACTION_APPLIED_READBACK_EXACT"], "EXACT")
                if coherent
                else ("ERROR", ["READBACK_MISMATCH"], "UNKNOWN")
            )
        else:
            outcome, reasons, status = "ERROR", ["READBACK_MISMATCH"], "UNKNOWN"

    return {
        "receipt_id": "",
        "outcome": outcome,
        "reason_codes": reasons,
        "attempted": attempt["status"] in {"ATTEMPTED", "SUCCEEDED", "FAILED"},
        "applied": outcome == "APPLIED",
        "readback_status": status,
        "intent_fingerprint": _intent_fingerprint(intent),
        "target_fingerprint": _target_fingerprint(intent),
        "readback_fingerprint": _readback_fingerprint(readback),
    }


def _claims() -> dict[str, bool]:
    return {
        "deterministic_evaluation": True,
        "validator_network_accessed": False,
        "validator_external_mutation_performed": False,
        "external_state_authenticated": False,
        "authority_authenticated": False,
        "subject_execution_authenticated": False,
        "live_mutation_adapter_present": False,
        "mutation_verified": False,
        "pull_request_lifecycle_changed": False,
        "repository_settings_changed": False,
        "release_deployment_promotion_or_publication_changed": False,
    }


def _identity(candidate: Mapping[str, Any]) -> tuple[str, str]:
    projection = copy.deepcopy(dict(candidate))
    projection.pop("spec_hash", None)
    projection["receipt"].pop("receipt_id", None)
    digest = compute_spec_hash(projection)
    return (
        digest,
        "kfm:repository-issue-mutation-receipt:"
        + digest.removeprefix("sha256:"),
    )


def build_candidate(case: Mapping[str, Any]) -> dict[str, object]:
    source = copy.deepcopy(dict(case))
    source.pop("case_id", None)
    source.pop("expected", None)
    intent = _mapping(source["intent"], "intent")
    intent.pop("intent_id", None)
    fingerprint = _intent_fingerprint(intent)
    intent["intent_id"] = (
        "kfm:repository-issue-mutation-intent:"
        + fingerprint.removeprefix("sha256:")
    )
    replay = source["preflight"]["replay"]
    if replay["intent_fingerprint"] == "$CURRENT_INTENT_FINGERPRINT":
        replay["intent_fingerprint"] = fingerprint
    source["preflight"]["target"]["labels"] = sorted(
        source["preflight"]["target"]["labels"]
    )
    if source["readback"] is not None:
        source["readback"]["target"]["labels"] = sorted(
            source["readback"]["target"]["labels"]
        )

    candidate: dict[str, Any] = {
        "schema_version": "1.0.0",
        "object_type": OBJECT_TYPE,
        "profile": PROFILE,
        "execution_mode": EXECUTION_MODE,
        **source,
        "receipt": derive_receipt(
            source["evaluated_at"],
            intent,
            source["preflight"],
            source["attempt"],
            source["readback"],
        ),
        "spec_hash": "",
        "claims": _claims(),
    }
    digest, receipt_id = _identity(candidate)
    candidate["spec_hash"] = digest
    candidate["receipt"]["receipt_id"] = receipt_id
    return candidate


def validate_document(candidate: object) -> ValidationResult:
    findings: set[Finding] = set()
    errors = sorted(
        _schema_validator().iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    findings.update(
        Finding("SCHEMA_INVALID", _path(tuple(error.absolute_path))) for error in errors
    )
    if errors or not isinstance(candidate, Mapping):
        return ValidationResult("DENY", tuple(sorted(findings)))

    try:
        intent = candidate["intent"]
        expected_fingerprint = _intent_fingerprint(intent)
        expected_intent_id = (
            "kfm:repository-issue-mutation-intent:"
            + expected_fingerprint.removeprefix("sha256:")
        )
        if intent["intent_id"] != expected_intent_id:
            findings.add(Finding("INTENT_ID_MISMATCH", "$.intent.intent_id"))
        expected_receipt = derive_receipt(
            candidate["evaluated_at"],
            intent,
            candidate["preflight"],
            candidate["attempt"],
            candidate["readback"],
        )
        actual_receipt = candidate["receipt"]
        if {
            key: value for key, value in actual_receipt.items() if key != "receipt_id"
        } != {
            key: value for key, value in expected_receipt.items() if key != "receipt_id"
        }:
            findings.add(Finding("RECEIPT_DERIVATION_MISMATCH", "$.receipt"))
        expected_hash, expected_receipt_id = _identity(candidate)
        if candidate["spec_hash"] != expected_hash:
            findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
        if actual_receipt["receipt_id"] != expected_receipt_id:
            findings.add(Finding("RECEIPT_ID_MISMATCH", "$.receipt.receipt_id"))
    except (KeyError, TypeError, ValueError, CanonicalizationFailure):
        findings.add(Finding("SEMANTIC_INPUT_INVALID", "$"))
        expected_receipt_id = None
    return ValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        expected_receipt_id,
    )


def validate_file(path: Path) -> ValidationResult:
    try:
        return validate_document(load_json_file(path))
    except JsonInputError:
        return ValidationResult("ERROR", (Finding("INPUT_JSON_INVALID", "$"),))
    except (KeyError, TypeError, ValueError):
        return ValidationResult("ERROR", (Finding("INPUT_OR_DEPENDENCY_ERROR", "$"),))


def _cases() -> list[Mapping[str, Any]]:
    value = _mapping(load_json_file(CASES_PATH), "cases fixture")
    base = _mapping(value.get("base"), "cases fixture.base")
    raw_cases = value.get("cases")
    if not isinstance(raw_cases, list):
        raise ValueError("cases fixture.cases must be an array")
    cases = []
    for raw_case in raw_cases:
        raw_case = _mapping(raw_case, "case")
        merged = _deep_merge(base, _mapping(raw_case.get("overrides", {}), "overrides"))
        merged["case_id"] = raw_case["case_id"]
        merged["expected"] = copy.deepcopy(raw_case["expected"])
        cases.append(merged)
    return cases


def _invalid_candidate(path: Path) -> tuple[dict[str, Any], Mapping[str, Any]]:
    fixture = _mapping(load_json_file(path), "invalid fixture")
    if fixture.get("base") != "valid/valid_already_satisfied_no_op.json":
        raise ValueError("invalid-control fixture has an unsupported base")
    candidate = _mapping(load_json_file(VALID_PATH), "valid fixture")
    return (
        _deep_merge(candidate, _mapping(fixture.get("overrides"), "overrides")),
        _mapping(fixture.get("expected"), "expected"),
    )


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    issues: list[dict[str, object]] = []
    cases = _cases()
    for case in cases:
        candidate = build_candidate(case)
        actual = {
            "outcome": candidate["receipt"]["outcome"],
            "reason_codes": candidate["receipt"]["reason_codes"],
        }
        if validate_document(candidate).outcome != "PASS":
            issues.append({"case_id": case["case_id"], "code": "BUILT_CASE_INVALID"})
        if actual != case["expected"]:
            issues.append(
                {"case_id": case["case_id"], "code": "CASE_EXPECTATION_MISMATCH"}
            )

    if validate_file(VALID_PATH).outcome != "PASS":
        issues.append({"case_id": "valid_no_op", "code": "VALID_FIXTURE_INVALID"})
    for path in INVALID_PATHS:
        candidate, expected = _invalid_candidate(path)
        result = validate_document(candidate)
        if (
            result.outcome != expected["outcome"]
            or (expected["finding_code"], expected["path"])
            not in {(finding.code, finding.path) for finding in result.findings}
        ):
            issues.append(
                {"case_id": path.stem, "code": "INVALID_FIXTURE_POLARITY_MISMATCH"}
            )

    payload = {
        "authority": "NONE",
        "cases": len(cases),
        "execution_mode": EXECUTION_MODE,
        "findings": issues,
        "non_effects": list(NON_EFFECTS),
        "outcome": "DENY" if issues else "PASS",
        "scope": SCOPE,
    }
    return not issues, payload


def _serialize(result: ValidationResult, path: Path | None = None) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "candidate": str(path) if path else None,
            "execution_mode": EXECUTION_MODE,
            "findings": [finding.__dict__ for finding in result.findings],
            "non_effects": list(NON_EFFECTS),
            "outcome": result.outcome,
            "receipt_id": result.receipt_id,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--build-case")
    args = parser.parse_args(argv)

    if args.fixtures:
        try:
            ok, payload = run_fixture_suite()
        except Exception:
            ok, payload = False, {
                "authority": "NONE",
                "cases": 0,
                "execution_mode": EXECUTION_MODE,
                "findings": [{"code": "FIXTURE_SUITE_ERROR", "path": "$"}],
                "non_effects": list(NON_EFFECTS),
                "outcome": "ERROR",
                "scope": SCOPE,
            }
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1

    if args.build_case:
        matches = [case for case in _cases() if case["case_id"] == args.build_case]
        if len(matches) != 1:
            parser.error("--build-case must name exactly one fixture case")
        print(json.dumps(build_candidate(matches[0]), indent=2, sort_keys=True))
        return 0

    if args.candidate is None:
        parser.error("candidate is required unless --fixtures or --build-case is used")
    result = validate_file(args.candidate)
    print(_serialize(result, args.candidate))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
