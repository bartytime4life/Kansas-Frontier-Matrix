#!/usr/bin/env python3
"""Validate fixture-only SignedBundleTimestampEvidence records.

Validation records declared timestamp-material consistency only. It performs no
cryptographic verification, transparency lookup, policy evaluation, review,
promotion, release, deployment, publication, or public-use authorization.
"""

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

SCHEMA = ROOT / "schemas/contracts/v1/release/signed_bundle_timestamp_evidence.schema.json"
CASES = ROOT / "fixtures/contracts/v1/release/signed_bundle_timestamp_evidence/cases.json"
IDENTITY_PREFIX = "kfm:signed-bundle-timestamp-evidence:"
MAX_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 50


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def valid(self) -> bool:
        return not self.findings


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
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
            return None, (Finding("INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("INPUT_READ_ERROR", "/"),)
    except (RecursionError, ValueError):
        return None, (Finding("JSON_COMPLEXITY_LIMIT", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ROOT_NOT_OBJECT", "/"),)
    return value, ()


def identity_subject(value: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(value))
    subject.pop("evidence_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(identity_subject(value))
    evidence_id = IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]
    return spec_hash, evidence_id


def _merge(target: dict[str, Any], patch: Mapping[str, Any]) -> None:
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            _merge(target[key], value)
        else:
            target[key] = copy.deepcopy(value)


def materialize_case(corpus: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(corpus["base"])
    base_hash, base_id = canonical_identity(candidate)
    candidate["spec_hash"] = base_hash
    candidate["evidence_id"] = base_id
    _merge(candidate, case.get("patch", {}))
    if case.get("recompute_identity", True):
        spec_hash, evidence_id = canonical_identity(candidate)
        candidate["spec_hash"] = spec_hash
        candidate["evidence_id"] = evidence_id
    return candidate


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
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


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and value == sorted(set(value))


def _item_key(value: object) -> tuple[str, str]:
    if not isinstance(value, dict):
        return ("", "")
    return (str(value.get("kind", "")), str(value.get("evidence_ref", "")))


def expected_assessment(requirement_state: str, evidence_state: str) -> tuple[str, list[str]]:
    if evidence_state == "PRESENT":
        return "PASS", ["TIMESTAMP_EVIDENCE_PRESENT"]
    if evidence_state == "UNREADABLE":
        return "ERROR", ["TIMESTAMP_EVIDENCE_UNREADABLE"]
    if requirement_state == "REQUIRED":
        return "DENY", ["TIMESTAMP_EVIDENCE_REQUIRED_MISSING"]
    if requirement_state == "OPTIONAL":
        return "ABSTAIN", ["TIMESTAMP_EVIDENCE_OPTIONAL_ABSENT"]
    return "ABSTAIN", ["TIMESTAMP_REQUIREMENT_UNKNOWN"]


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    subject = candidate.get("subject")
    requirement = candidate.get("requirement")
    evidence = candidate.get("evidence")
    assessment = candidate.get("assessment")
    if not all(isinstance(value, dict) for value in (subject, requirement, evidence, assessment)):
        return [Finding("RECORD_SURFACE_INVALID", "/")]

    promotion_digest = subject.get("promotion_bundle_digest")
    cosign_digest = subject.get("cosign_bundle_digest")
    if not str(subject.get("promotion_bundle_ref", "")).endswith("@" + str(promotion_digest)):
        findings.append(Finding("PROMOTION_BUNDLE_REF_MISMATCH", "/subject/promotion_bundle_ref"))
    if not str(subject.get("cosign_bundle_ref", "")).endswith("@" + str(cosign_digest)):
        findings.append(Finding("COSIGN_BUNDLE_REF_MISMATCH", "/subject/cosign_bundle_ref"))

    requirement_state = str(requirement.get("state"))
    policy_ref = requirement.get("policy_bundle_ref")
    if requirement_state == "UNKNOWN" and policy_ref is not None:
        findings.append(Finding("UNKNOWN_REQUIREMENT_POLICY_REF_DENIED", "/requirement/policy_bundle_ref"))
    if requirement_state in {"OPTIONAL", "REQUIRED"} and policy_ref is None:
        findings.append(Finding("TIMESTAMP_POLICY_REF_REQUIRED", "/requirement/policy_bundle_ref"))

    evidence_state = str(evidence.get("state"))
    items = evidence.get("items")
    absence_codes = evidence.get("absence_reason_codes")
    if not isinstance(items, list) or not isinstance(absence_codes, list):
        return findings + [Finding("EVIDENCE_SURFACE_INVALID", "/evidence")]
    if [_item_key(item) for item in items] != sorted({_item_key(item) for item in items}):
        findings.append(Finding("TIMESTAMP_ITEMS_NOT_CANONICAL", "/evidence/items"))
    if not _canonical_strings(absence_codes):
        findings.append(Finding("ABSENCE_CODES_NOT_CANONICAL", "/evidence/absence_reason_codes"))

    if evidence_state == "PRESENT":
        if not items:
            findings.append(Finding("TIMESTAMP_EVIDENCE_ITEM_REQUIRED", "/evidence/items"))
        if absence_codes:
            findings.append(Finding("TIMESTAMP_ABSENCE_CODE_CONFLICT", "/evidence/absence_reason_codes"))
    else:
        if items:
            findings.append(Finding("TIMESTAMP_EVIDENCE_ITEM_CONFLICT", "/evidence/items"))
        if not absence_codes:
            findings.append(Finding("TIMESTAMP_ABSENCE_CODE_REQUIRED", "/evidence/absence_reason_codes"))

    for index, item in enumerate(items):
        if not isinstance(item, dict):
            continue
        role = item.get("subject_role")
        expected_digest = promotion_digest if role == "PROMOTION_BUNDLE" else cosign_digest
        if item.get("bound_subject_digest") != expected_digest:
            findings.append(Finding("TIMESTAMP_SUBJECT_DIGEST_MISMATCH", f"/evidence/items/{index}/bound_subject_digest"))
        kind = item.get("kind")
        if kind == "RFC3161" and item.get("rfc3161_policy_oid") is None:
            findings.append(Finding("RFC3161_POLICY_OID_REQUIRED", f"/evidence/items/{index}/rfc3161_policy_oid"))
        if kind == "SIGSTORE_SIGNED_ENTRY_TIMESTAMP":
            if role != "COSIGN_BUNDLE":
                findings.append(Finding("SIGSTORE_SUBJECT_ROLE_INVALID", f"/evidence/items/{index}/subject_role"))
            if subject.get("rekor_uuid") is None:
                findings.append(Finding("REKOR_UUID_REQUIRED", "/subject/rekor_uuid"))

    expected_outcome, expected_codes = expected_assessment(requirement_state, evidence_state)
    if assessment.get("outcome") != expected_outcome or assessment.get("reason_codes") != expected_codes:
        findings.append(Finding("TIMESTAMP_ASSESSMENT_MISMATCH", "/assessment"))

    try:
        expected_hash, expected_id = canonical_identity(candidate)
    except CanonicalizationFailure:
        findings.append(Finding("IDENTITY_CANONICALIZATION_ERROR", "/"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("evidence_id") != expected_id:
            findings.append(Finding("EVIDENCE_ID_MISMATCH", "/evidence_id"))
    return findings


def validate_candidate(candidate: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return Result("ERROR", tuple(sorted(set(schema_findings))))
    findings = _semantic_findings(candidate)
    if findings:
        return Result("ERROR", tuple(sorted(set(findings))))
    return Result(str(candidate["assessment"]["outcome"]), ())


def validate_record(path: Path) -> Result:
    candidate, findings = _read(path)
    if candidate is None:
        return Result("ERROR", tuple(sorted(set(findings))))
    return validate_candidate(candidate)


def _serialize(label: str, result: Result) -> str:
    return json.dumps(
        {
            "fixture": label,
            "findings": [item.code for item in result.findings],
            "outcome": result.outcome,
            "scope": "fixture-only-signed-bundle-timestamp-evidence",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    corpus, findings = _read(CASES)
    if corpus is None:
        print(_serialize("cases.json", Result("ERROR", findings)))
        return 1
    cases = corpus.get("cases")
    if not isinstance(cases, list):
        print(_serialize("cases.json", Result("ERROR", (Finding("CASE_CORPUS_INVALID", "/cases"),))))
        return 1
    passed = True
    for case in sorted(cases, key=lambda item: item.get("id", "") if isinstance(item, dict) else ""):
        if not isinstance(case, dict):
            passed = False
            continue
        result = validate_candidate(materialize_case(corpus, case))
        expected = case.get("expected", {})
        actual_codes = sorted({item.code for item in result.findings})
        if result.outcome != expected.get("outcome") or actual_codes != expected.get("findings"):
            passed = False
        print(_serialize(str(case.get("id", "invalid-case")), result))
    return 0 if passed else 1


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures does not accept file arguments")
        return run_fixture_profile()
    if not args.files:
        parser.print_usage(sys.stderr)
        return 2
    passed = True
    for raw in sorted(args.files):
        result = validate_record(Path(raw))
        print(_serialize(Path(raw).name, result))
        passed = result.valid and passed
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(run())

