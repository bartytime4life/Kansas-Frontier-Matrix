#!/usr/bin/env python3
"""Validate fixture-only EntityLinkDecisionCandidate records."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import socket
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/entity_link_decision.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/data/entity_link_decision"
MAX_FILE_BYTES = 1_048_576
SCOPE = "data.entity_link_decision"


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

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
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
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    values = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(values) if values else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in Draft202012Validator(schema).iter_errors(candidate)
    ]


def _canonical_hash(candidate: Mapping[str, Any]) -> str:
    identity = json.loads(json.dumps(candidate))
    identity.pop("decision_id", None)
    identity.pop("spec_hash", None)
    encoded = json.dumps(identity, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _canonical_named_array(value: Any, key: str) -> bool:
    return isinstance(value, list) and all(isinstance(item, dict) and isinstance(item.get(key), str) for item in value) and [item[key] for item in value] == sorted({item[key] for item in value})


def _canonical_strings(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set()
    pair = candidate["pair"]
    left = pair["left"]
    right = pair["right"]
    matcher = candidate["matcher"]
    thresholds = candidate["thresholds"]
    checks = candidate["deterministic_checks"]
    evidence_refs = candidate["evidence_refs"]
    flags = candidate["flags"]
    decision = candidate["decision"]
    governance = candidate["governance"]

    expected_hash = _canonical_hash(candidate)
    if candidate["spec_hash"] != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate["decision_id"] != f"kfm://candidate/entity-link/{expected_hash.split(':', 1)[1]}":
        findings.add(Finding("DECISION_ID_MISMATCH", "/decision_id"))

    self_link = left["entity_ref"] == right["entity_ref"] or left["spec_hash"] == right["spec_hash"]
    if self_link:
        findings.add(Finding("SELF_LINK_DENIED", "/pair"))
    elif left["entity_ref"] >= right["entity_ref"]:
        findings.add(Finding("PAIR_ORDER_NOT_CANONICAL", "/pair"))
    if left["entity_type"] != right["entity_type"]:
        findings.add(Finding("ENTITY_TYPE_MISMATCH", "/pair"))
    if not _canonical_named_array(matcher["features"], "feature_id"):
        findings.add(Finding("FEATURES_NOT_CANONICAL", "/matcher/features"))
    if not _canonical_named_array(checks, "check_id"):
        findings.add(Finding("CHECKS_NOT_CANONICAL", "/deterministic_checks"))
    if not _canonical_strings(evidence_refs):
        findings.add(Finding("EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs"))
    if not _canonical_strings(decision["reason_codes"]):
        findings.add(Finding("REASON_CODES_NOT_CANONICAL", "/decision/reason_codes"))
    if thresholds["review_min"] >= thresholds["merge_candidate_min"]:
        findings.add(Finding("THRESHOLD_ORDER_INVALID", "/thresholds"))

    score = matcher["link_score"]
    action = decision["proposed_action"]
    required_results = [item["result"] for item in checks if item["required_for_merge"]]
    any_required_fail = "FAIL" in required_results
    all_required_pass = bool(required_results) and all(item == "PASS" for item in required_results)
    any_conflict = any(flags.values())

    if action == "PROPOSE_MERGE":
        if score < thresholds["merge_candidate_min"]:
            findings.add(Finding("MERGE_SCORE_BELOW_THRESHOLD", "/matcher/link_score"))
        if not all_required_pass:
            findings.add(Finding("MERGE_REQUIRED_CHECK_NOT_PASSED", "/deterministic_checks"))
        if len(evidence_refs) < 2:
            findings.add(Finding("MERGE_EVIDENCE_INSUFFICIENT", "/evidence_refs"))
        if any_conflict:
            findings.add(Finding("CONFLICT_REQUIRES_HOLD", "/flags"))
    elif action == "REVIEW":
        if score < thresholds["review_min"] or score >= thresholds["merge_candidate_min"]:
            findings.add(Finding("REVIEW_SCORE_OUTSIDE_BAND", "/matcher/link_score"))
        if any_required_fail:
            findings.add(Finding("FAILED_CHECK_REQUIRES_REJECT", "/deterministic_checks"))
        if any_conflict:
            findings.add(Finding("CONFLICT_REQUIRES_HOLD", "/flags"))
    elif action == "REJECT":
        if score >= thresholds["review_min"] and not any_required_fail:
            findings.add(Finding("REJECT_JUSTIFICATION_MISSING", "/decision/proposed_action"))
    elif action == "HOLD":
        if not any_conflict and len(evidence_refs) >= 2 and all(result != "UNKNOWN" for result in required_results):
            findings.add(Finding("HOLD_JUSTIFICATION_MISSING", "/decision/proposed_action"))

    if any(governance[field] is not False for field in (
        "authority_created",
        "policy_evaluated",
        "human_review_completed",
        "promotion_authorized",
        "public_use_allowed",
    )) or governance["release_state"] != "HOLD" or decision["auto_merge_performed"] is not False or decision["canonical_mutation_performed"] is not False:
        findings.add(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return sorted(findings)


def validate_document(candidate: Any) -> list[Finding]:
    if not isinstance(candidate, dict):
        return [Finding("ROOT_NOT_OBJECT", "/")]
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return sorted(set(schema_findings))
    return _semantic_findings(candidate)


def validate_file(path: Path | str) -> ValidationResult:
    candidate, findings = _read_object(Path(path))
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(validate_document(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps({
        "file": path.as_posix(),
        "findings": [{"code": item.code, "field": item.field} for item in result.findings],
        "outcome": "PASS" if result.ok else "FAIL",
        "scope": SCOPE,
    }, sort_keys=True, separators=(",", ":"))


def _manifest() -> dict[str, list[str]]:
    try:
        value = json.loads((FIXTURE_ROOT / "invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixtures() -> int:
    valid = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
    expected = _manifest()
    ok = bool(valid and invalid and set(expected) == {path.name for path in invalid})
    for path in valid:
        result = validate_file(path)
        print(_serialize(path, result))
        ok = ok and result.ok
    for path in invalid:
        result = validate_file(path)
        print(_serialize(path, result))
        actual = sorted({item.code for item in result.findings})
        wanted = sorted(expected.get(path.name, []))
        if result.ok or actual != wanted:
            ok = False
            print(json.dumps({"actual": actual, "expected": wanted, "file": path.as_posix(), "outcome": "FIXTURE_POLARITY_ERROR"}, sort_keys=True, separators=(",", ":")))
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    if not args.files:
        parser.error("provide files or use --fixtures")
    failed = False
    for path in sorted(args.files):
        result = validate_file(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
