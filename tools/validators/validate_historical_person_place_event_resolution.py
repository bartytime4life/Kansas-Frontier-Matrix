#!/usr/bin/env python3
"""Validate a fixture-only historical person-place-event resolution candidate.

The validator is deterministic and no-network. A valid result proves only that a
synthetic candidate matches this bounded profile. It does not establish identity,
residence, migration, land ownership, patent validity, title, rights, policy,
review, release, or publication.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution"
PROFILE_ID = "kfm-people-dna-land-historical-person-place-event-resolution-v1"
OBJECT_FAMILY = "HistoricalPersonPlaceEventResolutionCandidate"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 50
COUNTABLE_AUTHORITIES = frozenset({"lcnaf", "viaf", "isni", "wikidata"})
PRIMARY_ORDER = ("lcnaf", "viaf", "isni", "wikidata", "local")
FORBIDDEN_RAW_DNA_KEYS = frozenset({
    "dna_segments", "genotype", "raw_dna", "raw_genotype", "sequence",
    "triangulation", "vendor_kit_id", "kit_id",
})
FORBIDDEN_PRIVATE_OR_PRECISE_KEYS = frozenset({
    "address", "coordinates", "latitude", "longitude", "parcel_id",
    "private_parcel_id", "street_address",
})


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")


def candidate_spec_hash(candidate: Mapping[str, Any]) -> str:
    payload = {key: value for key, value in candidate.items() if key != "spec_hash"}
    return "sha256:" + hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def load_candidate(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink() or not path.is_file():
            return None, [Finding("INPUT_NOT_REGULAR_FILE", "$")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "$")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "$")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "$")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "$")]
    except (OSError, UnicodeError, RecursionError, ValueError):
        return None, [Finding("INPUT_UNREADABLE", "$")]
    if not isinstance(value, dict):
        return None, [Finding("CANDIDATE_NOT_OBJECT", "$")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "$"))
    return findings


def _scan_forbidden(value: object, path: str, findings: set[Finding]) -> None:
    if isinstance(value, dict):
        for key in sorted(value):
            child = f"{path}.{key}"
            normalized = key.casefold()
            if normalized in FORBIDDEN_RAW_DNA_KEYS:
                findings.add(Finding("RAW_DNA_FIELD_DENIED", child))
            if normalized in FORBIDDEN_PRIVATE_OR_PRECISE_KEYS:
                findings.add(Finding("PRIVATE_OR_PRECISE_FIELD_DENIED", child))
            _scan_forbidden(value[key], child, findings)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _scan_forbidden(item, f"{path}[{index}]", findings)


def authority_points(candidate: Mapping[str, Any]) -> int:
    person = candidate.get("person")
    matches = person.get("authority_matches") if isinstance(person, dict) else None
    if not isinstance(matches, list):
        return 0
    for item in matches:
        if not isinstance(item, dict):
            continue
        refs = item.get("source_refs")
        if (
            item.get("authority") in COUNTABLE_AUTHORITIES
            and item.get("exact_match") is True
            and isinstance(refs, list)
            and len(set(ref for ref in refs if isinstance(ref, str))) >= 2
        ):
            return 3
    return 0


def co_mention_points(candidate: Mapping[str, Any]) -> int:
    place = candidate.get("place")
    mentions = candidate.get("co_mentions")
    if not isinstance(place, dict) or not isinstance(mentions, list):
        return 0
    county = place.get("county_fips")
    time_slice = place.get("time_slice")
    families: set[str] = set()
    source_refs: set[str] = set()
    for item in mentions:
        if not isinstance(item, dict):
            continue
        source_ref = item.get("source_ref")
        if source_ref in source_refs:
            continue
        if item.get("county_fips") == county and item.get("time_slice") == time_slice:
            family = item.get("source_family")
            if isinstance(family, str) and isinstance(source_ref, str):
                families.add(family)
                source_refs.add(source_ref)
    return 2 if len(families) >= 3 else 0


def glo_points(candidate: Mapping[str, Any]) -> int:
    place = candidate.get("place")
    anchor = candidate.get("glo_anchor")
    if not isinstance(place, dict) or not isinstance(anchor, dict):
        return 0
    place_legal = place.get("legal_description")
    anchor_legal = anchor.get("legal_description")
    if not isinstance(place_legal, dict) or not isinstance(anchor_legal, dict):
        return 0
    keys = ("township", "range", "section")
    exact = all(anchor_legal.get(key) == place_legal.get(key) for key in keys)
    return 2 if anchor.get("present") is True and anchor.get("exact_place_block") is True and exact else 0


def negative_points(candidate: Mapping[str, Any]) -> int:
    negatives = candidate.get("negative_evidence")
    if not isinstance(negatives, list):
        return 0
    return -3 if any(isinstance(item, dict) and item.get("strength") == "strong" for item in negatives) else 0


def expected_score(candidate: Mapping[str, Any]) -> int:
    return authority_points(candidate) + co_mention_points(candidate) + glo_points(candidate) + negative_points(candidate)


def expected_confidence(score: int) -> str:
    if score >= 5:
        return "high"
    if score >= 2:
        return "medium"
    return "low"


def expected_disposition(candidate: Mapping[str, Any], confidence: str) -> str:
    if negative_points(candidate) < 0:
        return "hold_for_review"
    if confidence == "high":
        return "candidate_review"
    if confidence == "medium":
        return "hold_for_review"
    return "abstain"


def _expected_primary(candidate: Mapping[str, Any]) -> str:
    person = candidate.get("person")
    matches = person.get("authority_matches") if isinstance(person, dict) else None
    exact: set[str] = set()
    if isinstance(matches, list):
        for item in matches:
            if isinstance(item, dict) and item.get("exact_match") is True:
                authority = item.get("authority")
                if authority in PRIMARY_ORDER:
                    exact.add(authority)
    return next((authority for authority in PRIMARY_ORDER if authority in exact), "local")


def validate_candidate(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set(_schema_findings(candidate))
    _scan_forbidden(candidate, "$", findings)

    scope = candidate.get("candidate_scope")
    if not isinstance(scope, dict):
        findings.add(Finding("CANDIDATE_SCOPE_INVALID", "$.candidate_scope"))
    else:
        if scope.get("synthetic_fixture") is not True or scope.get("historical_only") is not True:
            findings.add(Finding("SYNTHETIC_HISTORICAL_SCOPE_REQUIRED", "$.candidate_scope"))
        if scope.get("living_person") is not False:
            findings.add(Finding("LIVING_PERSON_DENIED", "$.candidate_scope.living_person"))
        if scope.get("public_release") is not False:
            findings.add(Finding("PUBLIC_RELEASE_DENIED", "$.candidate_scope.public_release"))

    governance = candidate.get("governance")
    if isinstance(governance, dict):
        if governance.get("release_state") != "not_released" or governance.get("public_exposure") is not False:
            findings.add(Finding("PUBLIC_RELEASE_DENIED", "$.governance"))
        if governance.get("promotion_eligible") is not False:
            findings.add(Finding("PROMOTION_ELIGIBILITY_DENIED", "$.governance.promotion_eligible"))
    else:
        findings.add(Finding("GOVERNANCE_INVALID", "$.governance"))

    person = candidate.get("person")
    if isinstance(person, dict) and person.get("primary_authority") != _expected_primary(candidate):
        findings.add(Finding("PRIMARY_AUTHORITY_ORDER_INVALID", "$.person.primary_authority"))

    score = expected_score(candidate)
    if candidate.get("score") != score:
        findings.add(Finding("SCORE_MISMATCH", "$.score"))
    confidence = expected_confidence(score)
    if candidate.get("confidence") != confidence:
        findings.add(Finding("CONFIDENCE_MISMATCH", "$.confidence"))
    disposition = expected_disposition(candidate, confidence)
    if candidate.get("disposition") != disposition:
        findings.add(Finding("DISPOSITION_MISMATCH", "$.disposition"))
    if isinstance(governance, dict) and governance.get("review_state") != disposition:
        findings.add(Finding("REVIEW_STATE_MISMATCH", "$.governance.review_state"))

    declared_hash = candidate.get("spec_hash")
    if declared_hash != candidate_spec_hash(candidate):
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))

    if candidate.get("profile_id") != PROFILE_ID or candidate.get("object_family") != OBJECT_FAMILY:
        findings.add(Finding("PROFILE_OR_OBJECT_FAMILY_INVALID", "$"))
    return sorted(findings)


def validate_file(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    candidate, findings = load_candidate(path)
    if candidate is None:
        return None, findings
    return candidate, validate_candidate(candidate)


def _expected_code(path: Path) -> str | None:
    sidecar = path.with_suffix(".expected_error.txt")
    try:
        if sidecar.is_symlink() or not sidecar.is_file() or sidecar.stat().st_size > 256:
            return None
        lines = [line.strip() for line in sidecar.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, UnicodeError):
        return None
    return lines[0] if len(lines) == 1 else None


def run_fixtures() -> int:
    valid_paths = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    invalid_paths = sorted((FIXTURE_ROOT / "invalid").glob("*.json"))
    failures: list[str] = []
    if not valid_paths or not invalid_paths:
        print("HISTORICAL_RESOLUTION_FIXTURES_ERROR nonempty valid and invalid lanes required")
        return 2
    for path in valid_paths:
        _, findings = validate_file(path)
        if findings:
            failures.append(f"valid/{path.name}")
    for path in invalid_paths:
        _, findings = validate_file(path)
        expected = _expected_code(path)
        if expected is None or expected not in {finding.code for finding in findings}:
            failures.append(f"invalid/{path.name}")
    if failures:
        for item in failures:
            print(f"HISTORICAL_RESOLUTION_FIXTURE_POLARITY_FAIL file={item}")
        return 1
    print(f"HISTORICAL_RESOLUTION_FIXTURES_VALID valid={len(valid_paths)} invalid={len(invalid_paths)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.paths:
            raise SystemExit("--fixtures cannot be combined with paths")
        return run_fixtures()
    if not args.paths:
        raise SystemExit("at least one path is required unless --fixtures is used")
    failed = False
    for path in args.paths:
        candidate, findings = validate_file(path)
        if findings:
            failed = True
            for finding in findings:
                print(f"HISTORICAL_RESOLUTION_INVALID file={path.name} code={finding.code} field={finding.field}")
        else:
            assert candidate is not None
            print(
                "HISTORICAL_RESOLUTION_VALID "
                f"file={path.name} score={candidate['score']} confidence={candidate['confidence']} "
                f"disposition={candidate['disposition']}"
            )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
