#!/usr/bin/env python3
"""Validate fixture-only conditional decision closure candidates.

A PASS proves closed shape, canonical ordering, evidence-backed obligation
state, deterministic summary, identity, and explicit non-authority. It does not
evaluate policy, satisfy or waive a real obligation, approve review, promote,
release, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import stat
import sys
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages" / "hashing" / "src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/policy/conditional_decision_closure.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/policy/conditional_decision_closure"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "policy.conditional_decision_closure_candidate"
ERROR_CODES = frozenset(
    {
        "INPUT_NOT_FILE",
        "INPUT_READ_ERROR",
        "INPUT_SYMLINK_DENIED",
        "INPUT_TOO_LARGE",
        "JSON_DUPLICATE_KEY",
        "JSON_INVALID",
        "JSON_NONFINITE_NUMBER",
        "JSON_NOT_UTF8",
        "ROOT_NOT_OBJECT",
        "SCHEMA_INVALID",
        "SCHEMA_UNAVAILABLE",
    }
)
CLOSED_STATES = frozenset({"SATISFIED", "WAIVED", "SUPERSEDED"})
BLOCKING_REASON = {
    "OPEN": "OPEN_OBLIGATION_PRESENT",
    "EXPIRED": "EXPIRED_OBLIGATION_PRESENT",
    "VIOLATED": "VIOLATED_OBLIGATION_PRESENT",
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    closure_id: str | None = None

    @property
    def outcome(self) -> str:
        if any(item.code in ERROR_CODES for item in self.findings):
            return "ERROR"
        return "PASS" if not self.findings else "DENY"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        descriptor = os.open(
            path,
            os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0),
        )
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                return None, [Finding("INPUT_NOT_FILE", "/")]
            with os.fdopen(descriptor, "rb") as stream:
                descriptor = -1
                raw = stream.read(MAX_JSON_BYTES + 1)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
        if len(raw) > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_nonfinite,
            parse_float=_finite,
        )
    except FileNotFoundError:
        return None, [Finding("INPUT_NOT_FILE", "/")]
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
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema, format_checker=FormatChecker()
                ).iter_errors(value),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
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
        findings.append(Finding("SCHEMA_INVALID", "/"))
    return findings


def _canonical(values: object) -> bool:
    return isinstance(values, list) and values == sorted(set(values))


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _obligations(value: object) -> list[Mapping[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _identity_projection(value: Mapping[str, Any]) -> dict[str, Any]:
    return {
        key: item
        for key, item in value.items()
        if key not in {"closure_id", "spec_hash"}
    }


def expected_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    digest = compute_spec_hash(_identity_projection(value))
    identity = "kfm://policy/conditional-decision-closure/" + digest.removeprefix(
        "sha256:"
    )[:24]
    return digest, identity


def _semantic(value: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set()
    obligations = _obligations(value.get("obligations"))
    result = _mapping(value.get("result"))
    ids = [str(item.get("obligation_id", "")) for item in obligations]
    if ids != sorted(ids) or len(ids) != len(set(ids)):
        findings.add(Finding("OBLIGATION_ORDER_INVALID", "/obligations"))

    blocking_ids: list[str] = []
    closed_ids: list[str] = []
    blocking_reasons: set[str] = set()
    for index, obligation in enumerate(obligations):
        base = f"/obligations/{index}"
        obligation_id = str(obligation.get("obligation_id", ""))
        state = obligation.get("state")
        applicable = obligation.get("applicable") is True
        evidence_refs = obligation.get("evidence_refs")
        reason_codes = obligation.get("reason_codes")
        if not _canonical(evidence_refs):
            findings.add(Finding("EVIDENCE_REF_ORDER_INVALID", f"{base}/evidence_refs"))
        if not _canonical(reason_codes):
            findings.add(Finding("REASON_CODE_ORDER_INVALID", f"{base}/reason_codes"))

        if applicable and state == "NOT_APPLICABLE":
            findings.add(Finding("APPLICABILITY_STATE_INVALID", f"{base}/state"))
        if not applicable and state != "NOT_APPLICABLE":
            findings.add(Finding("APPLICABILITY_STATE_INVALID", f"{base}/state"))

        if state in CLOSED_STATES:
            closed_ids.append(obligation_id)
            if not evidence_refs or obligation.get("closed_at") is None:
                findings.add(Finding("CLOSURE_EVIDENCE_MISSING", base))
            if state == "WAIVED" and obligation.get("authority_ref") is None:
                findings.add(Finding("WAIVER_AUTHORITY_MISSING", f"{base}/authority_ref"))
            if state != "WAIVED" and obligation.get("authority_ref") is not None:
                findings.add(Finding("AUTHORITY_REF_UNEXPECTED", f"{base}/authority_ref"))
            if state == "SUPERSEDED" and obligation.get("superseded_by_ref") is None:
                findings.add(
                    Finding("SUPERSESSION_REF_MISSING", f"{base}/superseded_by_ref")
                )
            if state != "SUPERSEDED" and obligation.get("superseded_by_ref") is not None:
                findings.add(
                    Finding("SUPERSESSION_REF_UNEXPECTED", f"{base}/superseded_by_ref")
                )
        elif state == "NOT_APPLICABLE":
            if not evidence_refs:
                findings.add(Finding("APPLICABILITY_EVIDENCE_MISSING", base))
            if obligation.get("authority_ref") is not None:
                findings.add(Finding("AUTHORITY_REF_UNEXPECTED", f"{base}/authority_ref"))
            if obligation.get("superseded_by_ref") is not None:
                findings.add(
                    Finding("SUPERSESSION_REF_UNEXPECTED", f"{base}/superseded_by_ref")
                )
        else:
            blocking_ids.append(obligation_id)
            reason = BLOCKING_REASON.get(str(state))
            if reason:
                blocking_reasons.add(reason)
            if obligation.get("closed_at") is not None or evidence_refs:
                findings.add(Finding("OPEN_STATE_CLOSURE_UNEXPECTED", base))
            if obligation.get("authority_ref") is not None:
                findings.add(Finding("AUTHORITY_REF_UNEXPECTED", f"{base}/authority_ref"))
            if obligation.get("superseded_by_ref") is not None:
                findings.add(
                    Finding("SUPERSESSION_REF_UNEXPECTED", f"{base}/superseded_by_ref")
                )

    expected_outcome = "HOLD" if blocking_ids else "CLOSED_FOR_SEPARATE_GATE"
    expected_reasons = (
        sorted(blocking_reasons)
        if blocking_ids
        else ["ALL_APPLICABLE_OBLIGATIONS_CLOSED"]
    )
    if result.get("outcome") != expected_outcome:
        findings.add(Finding("RESULT_OUTCOME_MISMATCH", "/result/outcome"))
    if result.get("blocking_obligation_ids") != sorted(blocking_ids):
        findings.add(
            Finding("BLOCKING_OBLIGATION_IDS_MISMATCH", "/result/blocking_obligation_ids")
        )
    if result.get("closed_obligation_ids") != sorted(closed_ids):
        findings.add(
            Finding("CLOSED_OBLIGATION_IDS_MISMATCH", "/result/closed_obligation_ids")
        )
    if result.get("reason_codes") != expected_reasons:
        findings.add(Finding("RESULT_REASON_CODES_MISMATCH", "/result/reason_codes"))

    try:
        digest, identity = expected_identity(value)
        if value.get("spec_hash") != digest:
            findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if value.get("closure_id") != identity:
            findings.add(Finding("CLOSURE_ID_MISMATCH", "/closure_id"))
    except (CanonicalizationFailure, TypeError, ValueError):
        findings.add(Finding("IDENTITY_EVALUATION_ERROR", "/"))
    return sorted(findings)


def validate(path: Path) -> ValidationResult:
    value, findings = _read(path)
    if value is None:
        return ValidationResult(tuple(sorted(findings)))
    schema_findings = _schema_findings(value)
    if schema_findings:
        return ValidationResult(tuple(sorted(schema_findings)))
    semantic = tuple(_semantic(value))
    return ValidationResult(semantic, str(value.get("closure_id")))


def serialize(result: ValidationResult) -> str:
    return json.dumps(
        {
            "outcome": result.outcome,
            "scope": SCOPE,
            "closure_id": result.closure_id,
            "authority": "NONE",
            "findings": [
                {"code": item.code, "path": item.path} for item in result.findings
            ],
        },
        sort_keys=True,
    )


def run_fixtures() -> tuple[bool, dict[str, object]]:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False, {"outcome": "ERROR", "reason": "MANIFEST_UNREADABLE"}
    mismatches = []
    for case in manifest.get("cases", []):
        result = validate(FIXTURES / case["file"])
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            mismatches.append(
                {
                    "case_id": case["case_id"],
                    "outcome": result.outcome,
                    "findings": actual,
                }
            )
    payload = {
        "outcome": "PASS" if not mismatches else "DENY",
        "scope": SCOPE,
        "cases": len(manifest.get("cases", [])),
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "network_access": "NONE",
        "mismatches": mismatches,
    }
    return not mismatches, payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        ok, payload = run_fixtures()
        print(json.dumps(payload, sort_keys=True))
        return 0 if ok else 1
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate(args.path)
    print(serialize(result))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
