#!/usr/bin/env python3
"""Validate one synthetic, no-network historical-place resolution candidate."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas/contracts/v1/domains/settlements-infrastructure/historical_place_resolution.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/domains/settlements-infrastructure/historical_place_resolution"
PROFILE = "kfm-settlements-infrastructure-historical-place-resolution-v1"
FAMILY = "HistoricalPlaceResolutionCandidate"
CORROBORATIVE = {"period_map", "contemporary_newspaper", "local_history"}
FORBIDDEN = {
    "address", "coordinates", "current_owner", "dna", "genotype", "geometry",
    "infrastructure_dependency", "latitude", "living_person", "longitude",
    "parcel_id", "private_owner", "raw_genotype", "street_address",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError("non-finite JSON number")
    return parsed


def canonical(value: object) -> bytes:
    """Bounded canonical JSON; not a repository-wide RFC 8785 implementation."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode()


def normalize_name(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    folded = unicodedata.normalize("NFKD", unicodedata.normalize("NFKC", value).casefold())
    return " ".join("".join(ch for ch in folded if not unicodedata.combining(ch)).split())


def candidate_spec_hash(document: Mapping[str, Any]) -> str:
    payload = {key: value for key, value in document.items() if key != "spec_hash"}
    return "sha256:" + hashlib.sha256(canonical(payload)).hexdigest()


def expected_resolution_id(document: Mapping[str, Any]) -> str:
    query, candidates = document.get("query"), document.get("candidates")
    if not isinstance(query, dict) or not isinstance(candidates, list):
        return "sha256:" + "0" * 64
    payload = {
        "query": {
            "name": normalize_name(query.get("name")),
            "year": query.get("year"),
            "state_code": query.get("state_code"),
            "county_hint": normalize_name(query.get("county_hint")),
        },
        "candidate_refs": sorted(
            item["candidate_ref"] for item in candidates
            if isinstance(item, dict) and isinstance(item.get("candidate_ref"), str)
        ),
    }
    return "sha256:" + hashlib.sha256(canonical(payload)).hexdigest()


def expected_place_id(candidate: Mapping[str, Any]) -> str | None:
    ids = candidate.get("authority_ids")
    if not isinstance(ids, dict):
        return None
    name, ahcb, gnis = normalize_name(candidate.get("canonical_name")), ids.get("ahcb_slice"), ids.get("gnis")
    if not name or not isinstance(ahcb, str) or not isinstance(gnis, str):
        return None
    payload = {"canonical_name": name, "ahcb_slice": ahcb, "gnis": gnis}
    return "urn:kfm:place:sha256:" + hashlib.sha256(canonical(payload)).hexdigest()


def _supports(candidate: Mapping[str, Any], role: str, fields: set[str]) -> bool:
    records = candidate.get("source_support")
    if not isinstance(records, list):
        return False
    return any(
        isinstance(record, dict)
        and record.get("source_role") == role
        and isinstance(record.get("supports"), list)
        and fields <= {item for item in record["supports"] if isinstance(item, str)}
        for record in records
    )


def _matches(query: Mapping[str, Any], candidate: Mapping[str, Any]) -> bool:
    name = normalize_name(query.get("name"))
    names = {normalize_name(candidate.get("canonical_name"))}
    variants = candidate.get("variants")
    if isinstance(variants, list):
        names.update(normalize_name(item) for item in variants)
    if name not in names:
        return False
    interval, year = candidate.get("valid_time"), query.get("year")
    if not isinstance(interval, dict) or not isinstance(year, int):
        return False
    start, end = interval.get("start_year"), interval.get("end_year")
    if not isinstance(start, int) or year < start or (isinstance(end, int) and year > end):
        return False
    hint = normalize_name(query.get("county_hint"))
    county = normalize_name(candidate.get("county_at_query_time"))
    return hint is None or hint == county


def candidate_rank(query: Mapping[str, Any], candidate: Mapping[str, Any]) -> int:
    if not _matches(query, candidate):
        return 0
    ids = candidate.get("authority_ids")
    if not isinstance(ids, dict):
        return 0
    federal = ids.get("gnis") is not None and _supports(candidate, "federal_name_authority", {"canonical_name"})
    county = ids.get("ahcb_slice") is not None and _supports(candidate, "historical_county_authority", {"county_at_query_time"})
    corroborated = any(_supports(candidate, role, {"feature_type"}) for role in CORROBORATIVE)
    lifespan = ids.get("kshs_po") is not None and _supports(candidate, "post_office_lifespan", {"valid_time", "feature_type"})
    if candidate.get("feature_type") == "rail_stop":
        return 1 if county and (federal or corroborated) else 0
    if federal and county:
        if candidate.get("feature_type") == "post_office":
            return 2 if lifespan else 1
        return 2 if corroborated else 1
    return 1 if county and corroborated else 0


def derive(document: Mapping[str, Any]) -> dict[str, Any]:
    query, candidates = document.get("query"), document.get("candidates")
    if not isinstance(query, dict) or not isinstance(candidates, list):
        ranked: list[tuple[dict[str, Any], int]] = []
    else:
        ranked = [(item, candidate_rank(query, item)) for item in candidates if isinstance(item, dict)]
    reviewable = [item for item, rank in ranked if rank >= 1]
    strong = [item for item, rank in ranked if rank == 2]
    if len(strong) == len(reviewable) == 1:
        item = strong[0]
        ids = item["authority_ids"]
        reasons = ["UNIQUE_TIME_SCOPED_MATCH", "GNIS_AUTHORITY_PRESENT", "AHCB_SLICE_MATCH"]
        reasons += ["BGN_DECISION_PRESENT"] if ids.get("bgn_decision") else []
        reasons += ["POST_OFFICE_LIFESPAN_MATCH"] if item.get("feature_type") == "post_office" else ["PERIOD_CORROBORATION_PRESENT"]
        return {
            "resolution_id": expected_resolution_id(document),
            "resolved_candidate_ref": item.get("candidate_ref"),
            "place_id": expected_place_id(item),
            "primary_authority": "bgn_decision" if ids.get("bgn_decision") else "gnis",
            "confidence": "high", "disposition": "candidate_review", "reason_codes": reasons,
        }
    if reviewable:
        reason = "AMBIGUOUS_TIME_SCOPED_CANDIDATES" if len(reviewable) > 1 else (
            "RAIL_STOP_REQUIRES_REVIEW" if reviewable[0].get("feature_type") == "rail_stop" else "INCOMPLETE_AUTHORITY_SUPPORT"
        )
        return {
            "resolution_id": expected_resolution_id(document), "resolved_candidate_ref": None,
            "place_id": None, "primary_authority": "none", "confidence": "medium",
            "disposition": "hold_for_review", "reason_codes": [reason],
        }
    return {
        "resolution_id": expected_resolution_id(document), "resolved_candidate_ref": None,
        "place_id": None, "primary_authority": "none", "confidence": "low",
        "disposition": "abstain", "reason_codes": ["NO_TIME_SCOPED_AUTHORITY_MATCH"],
    }


def _pointer(parts: Iterable[object]) -> str:
    values = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(values) if values else "/"


def _scan(value: object, path: str, findings: set[Finding]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key.casefold() in FORBIDDEN:
                findings.add(Finding("FORBIDDEN_SENSITIVE_OR_PRECISE_FIELD", child_path))
            _scan(child, child_path, findings)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _scan(child, f"{path}[{index}]", findings)


def _semantic(candidate: Mapping[str, Any], index: int) -> set[Finding]:
    out: set[Finding] = set()
    prefix = f"$.candidates[{index}]"
    interval = candidate.get("valid_time")
    if isinstance(interval, dict) and isinstance(interval.get("start_year"), int) and isinstance(interval.get("end_year"), int):
        if interval["end_year"] < interval["start_year"]:
            out.add(Finding("VALID_TIME_ORDER_INVALID", f"{prefix}.valid_time"))
    canonical_name = normalize_name(candidate.get("canonical_name"))
    variants = candidate.get("variants")
    normalized = [normalize_name(item) for item in variants] if isinstance(variants, list) else []
    if canonical_name in normalized:
        out.add(Finding("NAME_VARIANT_COLLISION", f"{prefix}.variants"))
    present = [item for item in normalized if item]
    if len(present) != len(set(present)):
        out.add(Finding("NORMALIZED_VARIANT_DUPLICATE", f"{prefix}.variants"))
    ids = candidate.get("authority_ids")
    if isinstance(ids, dict):
        if (ids.get("gnis") or ids.get("bgn_decision")) and not _supports(candidate, "federal_name_authority", {"canonical_name"}):
            out.add(Finding("FEDERAL_AUTHORITY_SUPPORT_MISSING", f"{prefix}.source_support"))
        if ids.get("ahcb_slice") and not _supports(candidate, "historical_county_authority", {"county_at_query_time"}):
            out.add(Finding("AHCB_SUPPORT_MISSING", f"{prefix}.source_support"))
        if ids.get("kshs_po") and not _supports(candidate, "post_office_lifespan", {"valid_time", "feature_type"}):
            out.add(Finding("POST_OFFICE_SUPPORT_MISSING", f"{prefix}.source_support"))
    return out


def validate_candidate(document: Mapping[str, Any]) -> list[Finding]:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    findings = {
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(document)
    }
    _scan(document, "$", findings)
    governance = document.get("governance")
    if not isinstance(governance, dict):
        findings.add(Finding("GOVERNANCE_INVALID", "$.governance"))
    else:
        if governance.get("fixture_only") is not True or governance.get("historical_only") is not True:
            findings.add(Finding("SYNTHETIC_HISTORICAL_SCOPE_REQUIRED", "$.governance"))
        if governance.get("network_accessed") is not False or governance.get("live_source_activation") is not False:
            findings.add(Finding("LIVE_SOURCE_ACCESS_DENIED", "$.governance"))
        if governance.get("release_state") != "not_released" or governance.get("public_exposure") is not False:
            findings.add(Finding("PUBLIC_RELEASE_DENIED", "$.governance"))
        if governance.get("promotion_eligible") is not False:
            findings.add(Finding("PROMOTION_ELIGIBILITY_DENIED", "$.governance.promotion_eligible"))

    seen: set[str] = set()
    candidates = document.get("candidates")
    if isinstance(candidates, list):
        for index, candidate in enumerate(candidates):
            if not isinstance(candidate, dict):
                continue
            findings.update(_semantic(candidate, index))
            records = candidate.get("source_support")
            if isinstance(records, list):
                for record_index, record in enumerate(records):
                    ref = record.get("source_ref") if isinstance(record, dict) else None
                    if isinstance(ref, str):
                        if ref in seen:
                            findings.add(Finding("SOURCE_REF_REUSE", f"$.candidates[{index}].source_support[{record_index}].source_ref"))
                        seen.add(ref)

    expected, actual = derive(document), document.get("derived")
    if not isinstance(actual, dict):
        findings.add(Finding("DERIVED_STATE_INVALID", "$.derived"))
    else:
        codes = {
            "resolution_id": "RESOLUTION_ID_MISMATCH", "resolved_candidate_ref": "RESOLVED_CANDIDATE_MISMATCH",
            "place_id": "PLACE_ID_MISMATCH", "primary_authority": "PRIMARY_AUTHORITY_MISMATCH",
            "confidence": "CONFIDENCE_MISMATCH", "disposition": "DISPOSITION_MISMATCH",
            "reason_codes": "REASON_CODES_MISMATCH",
        }
        for field, code in codes.items():
            if actual.get(field) != expected[field]:
                findings.add(Finding(code, f"$.derived.{field}"))
        if expected["reason_codes"] == ["RAIL_STOP_REQUIRES_REVIEW"] and actual.get("disposition") == "candidate_review":
            findings.add(Finding("RAIL_STOP_REQUIRES_REVIEW", "$.derived.disposition"))
        if isinstance(governance, dict) and governance.get("review_state") != expected["disposition"]:
            findings.add(Finding("REVIEW_STATE_MISMATCH", "$.governance.review_state"))

    if document.get("profile_id") != PROFILE or document.get("object_family") != FAMILY:
        findings.add(Finding("PROFILE_OR_OBJECT_FAMILY_INVALID", "$"))
    if document.get("spec_hash") != candidate_spec_hash(document):
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    return sorted(findings)


def load_file(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > 2 * 1024 * 1024:
            return None, [Finding("INPUT_NOT_REGULAR_FILE", "$")]
        value = json.loads(path.read_text(encoding="utf-8"), parse_constant=lambda _: (_ for _ in ()).throw(ValueError()), parse_float=_finite)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_OR_INPUT_INVALID", "$")]
    return (value, []) if isinstance(value, dict) else (None, [Finding("CANDIDATE_NOT_OBJECT", "$")])


def validate_file(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    document, findings = load_file(path)
    return (document, validate_candidate(document)) if document is not None else (None, findings)


def run_fixtures() -> int:
    valid = sorted((FIXTURES / "valid").glob("*.json"))
    invalid = sorted((FIXTURES / "invalid").glob("*.json"))
    failures: list[str] = []
    if not valid or not invalid:
        return 2
    for path in valid:
        if validate_file(path)[1]:
            failures.append(f"valid/{path.name}")
    for path in invalid:
        expected_path = path.with_suffix(".expected_error.txt")
        expected = expected_path.read_text(encoding="utf-8").strip() if expected_path.is_file() else ""
        if expected not in {item.code for item in validate_file(path)[1]}:
            failures.append(f"invalid/{path.name}")
    if failures:
        for failure in failures:
            print(f"HISTORICAL_PLACE_FIXTURE_POLARITY_FAIL file={failure}")
        return 1
    print(f"HISTORICAL_PLACE_FIXTURES_VALID valid={len(valid)} invalid={len(invalid)}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.paths:
            parser.error("--fixtures cannot be combined with paths")
        return run_fixtures()
    if not args.paths:
        parser.error("at least one path is required unless --fixtures is used")
    failed = False
    for path in args.paths:
        document, findings = validate_file(path)
        if findings:
            failed = True
            for finding in findings:
                print(f"HISTORICAL_PLACE_INVALID file={path.name} code={finding.code} field={finding.field}")
        else:
            assert document is not None
            state = document["derived"]
            print(f"HISTORICAL_PLACE_VALID file={path.name} confidence={state['confidence']} disposition={state['disposition']}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
