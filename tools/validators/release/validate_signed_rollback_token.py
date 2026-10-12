#!/usr/bin/env python3
"""Validate fixture-only SignedRollbackToken readiness records."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/release/signed_rollback_token.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/release/signed_rollback_token/cases.json"
PREFIX = "kfm:signed-rollback-token:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("ROLLBACK_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("ROLLBACK_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("ROLLBACK_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("ROLLBACK_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("ROLLBACK_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("ROLLBACK_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ROLLBACK_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def signing_payload(value: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "object_type": value["object_type"],
        "schema_version": value["schema_version"],
        "profile": value["profile"],
        "issued_at": value["issued_at"],
        "alias_ref": value["alias_ref"],
        "current": copy.deepcopy(value["current"]),
        "rollback_target": copy.deepcopy(value["rollback_target"]),
        "closure": copy.deepcopy(value["closure"]),
        "revert_receipt_template": copy.deepcopy(value["revert_receipt_template"]),
    }


def signing_payload_digest(value: Mapping[str, Any]) -> str:
    return compute_spec_hash(signing_payload(value))


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"token_id", "spec_hash"}}
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def _business_findings(value: Mapping[str, Any]) -> tuple[str, tuple[Finding, ...]]:
    errors: set[Finding] = set()
    denials: set[Finding] = set()
    holds: set[Finding] = set()

    current = value["current"]
    target = value["rollback_target"]
    closure = value["closure"]
    signature = value["signature"]
    receipt = value["revert_receipt_template"]

    if value["evaluation_state"] == "ERROR":
        errors.add(Finding("ROLLBACK_CURRENT_STATE_ERROR", "/evaluation_state"))

    if current["state"] == "ERROR":
        errors.add(Finding("ROLLBACK_CURRENT_STATE_ERROR", "/current/state"))
    elif current["state"] == "UNKNOWN":
        holds.add(Finding("ROLLBACK_CURRENT_STATE_UNKNOWN", "/current/state"))
    else:
        current_complete = all(
            current[key] is not None
            for key in ("release_ref", "manifest_digest", "spec_hash", "alias_revision")
        )
        if not current_complete:
            denials.add(Finding("ROLLBACK_CURRENT_STATE_INCOMPLETE", "/current"))
        else:
            if target["alias_revision"] >= current["alias_revision"]:
                denials.add(Finding("ROLLBACK_TARGET_NOT_PRIOR", "/rollback_target/alias_revision"))
            if (
                target["release_ref"] == current["release_ref"]
                or target["spec_hash"] == current["spec_hash"]
            ):
                denials.add(Finding("ROLLBACK_TARGET_EQUALS_CURRENT", "/rollback_target/release_ref"))
            receipt_ok = (
                receipt["prior_alias_revision"] == current["alias_revision"]
                and receipt["next_alias_revision"] == current["alias_revision"] + 1
                and receipt["source_release_ref"] == current["release_ref"]
                and receipt["target_release_ref"] == target["release_ref"]
                and receipt["target_spec_hash"] == target["spec_hash"]
            )
            if not receipt_ok:
                denials.add(Finding("ROLLBACK_REVERT_RECEIPT_MISMATCH", "/revert_receipt_template"))

    target_state = target["verification_state"]
    if target_state == "ERROR":
        errors.add(Finding("ROLLBACK_TARGET_ERROR", "/rollback_target/verification_state"))
    elif target_state == "UNKNOWN":
        holds.add(Finding("ROLLBACK_TARGET_UNKNOWN", "/rollback_target/verification_state"))
    elif target_state == "DENIED":
        denials.add(Finding("ROLLBACK_TARGET_UNVERIFIED", "/rollback_target/verification_state"))

    policy_state = closure["policy_outcome"]
    if policy_state == "ERROR":
        errors.add(Finding("ROLLBACK_POLICY_ERROR", "/closure/policy_outcome"))
    elif policy_state == "ABSTAIN":
        holds.add(Finding("ROLLBACK_POLICY_ABSTAIN", "/closure/policy_outcome"))
    elif policy_state == "DENY":
        denials.add(Finding("ROLLBACK_POLICY_DENIED", "/closure/policy_outcome"))

    review_state = closure["review_outcome"]
    if review_state == "ERROR":
        errors.add(Finding("ROLLBACK_REVIEW_ERROR", "/closure/review_outcome"))
    elif review_state == "PENDING":
        holds.add(Finding("ROLLBACK_REVIEW_PENDING", "/closure/review_outcome"))
    elif review_state == "REJECTED":
        denials.add(Finding("ROLLBACK_REVIEW_REJECTED", "/closure/review_outcome"))

    signature_state = signature["state"]
    if signature_state == "ERROR":
        errors.add(Finding("ROLLBACK_SIGNATURE_ERROR", "/signature/state"))
    elif signature_state == "UNKNOWN":
        holds.add(Finding("ROLLBACK_SIGNATURE_UNKNOWN", "/signature/state"))
    elif signature_state == "MISSING":
        denials.add(Finding("ROLLBACK_SIGNATURE_MISSING", "/signature/state"))
    elif signature_state == "INVALID":
        denials.add(Finding("ROLLBACK_SIGNATURE_INVALID", "/signature/state"))
    else:
        if any(signature[key] is None for key in ("verification_ref", "envelope_digest", "subject_digest")):
            denials.add(Finding("ROLLBACK_SIGNATURE_EVIDENCE_INCOMPLETE", "/signature"))
        else:
            try:
                expected_subject = signing_payload_digest(value)
            except CanonicalizationFailure:
                errors.add(Finding("ROLLBACK_SIGNATURE_ERROR", "/signature/subject_digest"))
            else:
                if signature["subject_digest"] != expected_subject:
                    denials.add(Finding("ROLLBACK_SIGNATURE_SUBJECT_MISMATCH", "/signature/subject_digest"))

    if errors:
        return "ERROR", tuple(sorted(errors))
    if denials:
        return "DENY", tuple(sorted(denials))
    if holds:
        return "HOLD", tuple(sorted(holds))
    return "READY", (Finding("ROLLBACK_TOKEN_READY", "/result/outcome"),)


def recompute_result(value: Mapping[str, Any]) -> dict[str, Any]:
    outcome, findings = _business_findings(value)
    return {"outcome": outcome, "reason_codes": [finding.code for finding in findings]}


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("ROLLBACK_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("ROLLBACK_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("ROLLBACK_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("ROLLBACK_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("ROLLBACK_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["token_id"] != expected_id:
            findings.add(Finding("ROLLBACK_ID_MISMATCH", "/token_id"))
    if value["result"] != recompute_result(value):
        findings.add(Finding("ROLLBACK_RESULT_MISMATCH", "/result"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    outcome, findings = _business_findings(value)
    if outcome == "READY":
        return Result("PASS", ())
    if outcome == "HOLD":
        return Result("ABSTAIN", findings)
    if outcome == "DENY":
        return Result("DENY", findings)
    return Result("ERROR", findings)


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    if document["signature"]["state"] == "VERIFIED" and document["signature"]["subject_digest"] is not None:
        document["signature"]["subject_digest"] = case.get(
            "signature_subject_override", signing_payload_digest(document)
        )
    document["result"] = copy.deepcopy(case.get("result_override", recompute_result(document)))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["token_id"] = case.get("token_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    passed = True
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        match = result.outcome == case["expected_outcome"] and actual == case["expected_findings"]
        print(json.dumps({"case_id": case["case_id"], "outcome": result.outcome, "findings": actual, "suite_match": match}, sort_keys=True, separators=(",", ":")))
        passed = passed and match
    return 0 if passed else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_cryptography",
                "no_alias_mutation",
                "no_rollback_execution",
                "no_revert_receipt_write",
                "no_promotion",
                "no_deployment",
                "no_publication",
            ],
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
