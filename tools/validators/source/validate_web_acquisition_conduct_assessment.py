"""Validate fixture-only web-acquisition conduct assessments.

The validator checks closed shape, deterministic identity, route, declared
terms and robots posture, rate limits, identity, proxy/distribution posture,
and review references. It performs no network request and grants no legal,
source, connector, policy, review, release, or publication authority.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/web_acquisition_conduct_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/source/web_acquisition_conduct_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "DISTRIBUTED_POSTURE_UNKNOWN",
    "PROXY_POSTURE_UNKNOWN",
    "RATE_LIMIT_UNRESOLVED",
    "REVIEW_PENDING",
    "REVIEW_UNKNOWN",
    "ROBOTS_REVIEW_UNKNOWN",
    "ROUTE_UNRESOLVED",
    "TERMS_REVIEW_UNKNOWN",
    "USER_AGENT_POSTURE_UNKNOWN",
}
WEB_ROUTES = {"BROWSER_AUTOMATION", "HTML_SCRAPE"}
NON_ROBOTS_ROUTES = {"OFFICIAL_API", "DOCUMENTED_DOWNLOAD"}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


class UnpairedSurrogateError(ValueError):
    """Raised when text cannot be represented as Unicode scalar values."""


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


def _contains_surrogate(value: object) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if isinstance(value, Mapping):
        return any(_contains_surrogate(key) or _contains_surrogate(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


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
    if _contains_surrogate(value):
        return None, [Finding("JSON_UNPAIRED_SURROGATE", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    if _contains_surrogate(value):
        raise UnpairedSurrogateError
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
    return canonical_hash(subject)


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path))
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


def _terms_findings(terms: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    state = terms.get("state")
    evidence_ref = terms.get("evidence_ref")
    if state == "UNKNOWN":
        findings.add(Finding("TERMS_REVIEW_UNKNOWN", "/terms_review/state"))
    else:
        if evidence_ref is None:
            findings.add(Finding("TERMS_EVIDENCE_REQUIRED", "/terms_review/evidence_ref"))
        if state == "RESTRICTS_AUTOMATION":
            findings.add(Finding("TERMS_AUTOMATION_RESTRICTED", "/terms_review/state"))
        elif state == "PROHIBITS_AUTOMATION":
            findings.add(Finding("TERMS_AUTOMATION_PROHIBITED", "/terms_review/state"))
    return findings


def _robots_findings(route: str, robots: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    state = robots.get("state")
    evidence_ref = robots.get("evidence_ref")
    if state == "UNKNOWN":
        findings.add(Finding("ROBOTS_REVIEW_UNKNOWN", "/robots_review/state"))
    elif state in {"ALLOWED", "DISALLOWED"} and evidence_ref is None:
        findings.add(Finding("ROBOTS_EVIDENCE_REQUIRED", "/robots_review/evidence_ref"))
    elif state == "NOT_APPLICABLE" and evidence_ref is not None:
        findings.add(Finding("ROBOTS_DECLARATION_INCOHERENT", "/robots_review/evidence_ref"))
    if state == "DISALLOWED":
        findings.add(Finding("ROBOTS_DISALLOWED", "/robots_review/state"))
    if route in WEB_ROUTES and state not in {"ALLOWED", "DISALLOWED", "UNKNOWN"}:
        findings.add(Finding("ROUTE_ROBOTS_INCOHERENT", "/robots_review/state"))
    if route in NON_ROBOTS_ROUTES and state not in {"NOT_APPLICABLE", "UNKNOWN"}:
        findings.add(Finding("ROUTE_ROBOTS_INCOHERENT", "/robots_review/state"))
    return findings


def _rate_findings(rate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    state = rate.get("state")
    concurrency = rate.get("max_concurrency")
    delay = rate.get("minimum_delay_ms")
    policy_ref = rate.get("policy_ref")
    if state == "UNRESOLVED":
        findings.add(Finding("RATE_LIMIT_UNRESOLVED", "/rate_limit/state"))
        if any(value is not None for value in (concurrency, delay, policy_ref)):
            findings.add(Finding("RATE_LIMIT_DECLARATION_INCOHERENT", "/rate_limit"))
    elif state == "DECLARED":
        if concurrency is None or delay is None or policy_ref is None:
            findings.add(Finding("RATE_LIMIT_DECLARATION_INCOHERENT", "/rate_limit"))
    elif concurrency is not None or delay is not None or policy_ref is None:
        findings.add(Finding("RATE_LIMIT_DECLARATION_INCOHERENT", "/rate_limit"))
    return findings


def _identity_findings(identity: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    user_agent = identity.get("user_agent_posture")
    proxy = identity.get("proxy_posture")
    distributed = identity.get("distributed_posture")
    if user_agent == "UNKNOWN":
        findings.add(Finding("USER_AGENT_POSTURE_UNKNOWN", "/identity/user_agent_posture"))
    elif user_agent == "DISGUISED":
        findings.add(Finding("USER_AGENT_DISGUISED", "/identity/user_agent_posture"))
    if proxy == "UNKNOWN":
        findings.add(Finding("PROXY_POSTURE_UNKNOWN", "/identity/proxy_posture"))
    elif proxy == "ROTATING_EVASION":
        findings.add(Finding("ROTATING_PROXY_EVASION", "/identity/proxy_posture"))
    if distributed == "UNKNOWN":
        findings.add(Finding("DISTRIBUTED_POSTURE_UNKNOWN", "/identity/distributed_posture"))
    elif distributed == "UNREVIEWED":
        findings.add(Finding("DISTRIBUTED_ACQUISITION_UNREVIEWED", "/identity/distributed_posture"))
    return findings


def _review_findings(review: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    refs = review.get("review_record_refs")
    if not _canonical_strings(refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/review/review_record_refs"))
    state = review.get("state")
    if state == "COMPLETE" and not refs:
        findings.add(Finding("COMPLETE_REVIEW_REFERENCE_REQUIRED", "/review/review_record_refs"))
    elif state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/review/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/review/state"))
    return findings


def _exception_findings(candidate: Mapping[str, object]) -> set[Finding]:
    terms = candidate["terms_review"]
    identity = candidate["identity"]
    review = candidate["review"]
    assert all(isinstance(item, Mapping) for item in (terms, identity, review))
    exceptional = (
        identity.get("proxy_posture") == "SOURCE_AUTHORIZED"
        or identity.get("distributed_posture") == "SOURCE_AUTHORIZED"
    )
    if not exceptional:
        return set()
    supported = (
        terms.get("state") == "PERMITS_AUTOMATION"
        and terms.get("source_agreement_ref") is not None
        and review.get("state") == "COMPLETE"
        and bool(review.get("review_record_refs"))
    )
    return set() if supported else {Finding("EXCEPTION_SUPPORT_INCOMPLETE", "/identity")}


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))
    route = candidate["acquisition_route"]
    terms = candidate["terms_review"]
    robots = candidate["robots_review"]
    rate = candidate["rate_limit"]
    identity = candidate["identity"]
    review = candidate["review"]
    assert isinstance(route, str)
    assert all(isinstance(item, Mapping) for item in (terms, robots, rate, identity, review))
    if route == "UNRESOLVED":
        findings.add(Finding("ROUTE_UNRESOLVED", "/acquisition_route"))
    findings.update(_terms_findings(terms))
    findings.update(_robots_findings(route, robots))
    findings.update(_rate_findings(rate))
    findings.update(_identity_findings(identity))
    findings.update(_review_findings(review))
    findings.update(_exception_findings(candidate))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    if _contains_surrogate(candidate):
        return ValidationResult("ERROR", (Finding("JSON_UNPAIRED_SURROGATE", "/"),))
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
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
        target[key] = None if value is None else _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {
                "outcome": "ERROR",
                "codes": sorted({item.code for item in load_findings}),
            },
        }]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({
            "name": entry["name"],
            "ok": observed == expected,
            "expected": expected,
            "observed": observed,
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only web-acquisition conduct assessments."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
