#!/usr/bin/env python3
"""Deterministically normalize synthetic Darwin Core occurrence records.

This module is deliberately no-network and produces WORK-stage
``FloraOccurrenceCandidate`` objects only.  It does not admit a source, resolve
an EvidenceBundle, make a policy or review decision, generalize sensitive
geometry, authorize promotion or release, or publish an occurrence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

MAX_FILE_BYTES = 1_048_576
HASH_PROFILE = "kfm-fixture-json-v1"
NORMALIZER_ID = "flora-dwc-occurrence-normalizer"
NORMALIZER_VERSION = "1.0.0"
SCOPE = "flora-darwin-core-work-candidate-only"
SUPPORTED_PROFILES = ("GBIF_DWC", "IDIGBIO_DWC")


class DuplicateKeyError(ValueError):
    """Raised when an input JSON object repeats a key."""


class NonFiniteNumberError(ValueError):
    """Raised when an input JSON number is NaN or infinite."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class NormalizationResult:
    outcome: str
    findings: tuple[Finding, ...]
    candidate: Mapping[str, Any] | None = None

    @property
    def ok(self) -> bool:
        return self.outcome == "NORMALIZED" and self.candidate is not None


# Candidate field aliases are bounded and explicit.  This is an adapter profile,
# not a generic best-effort parser.
ALIASES: dict[str, tuple[str, ...]] = {
    "source_record_id": (
        "key",
        "gbifID",
        "gbifid",
        "uuid",
        "idigbio:uuid",
        "occurrenceID",
        "occurrenceid",
        "dwc:occurrenceID",
    ),
    "institution_code": (
        "institutionCode",
        "institutioncode",
        "dwc:institutionCode",
    ),
    "collection_code": (
        "collectionCode",
        "collectioncode",
        "dwc:collectionCode",
    ),
    "catalog_number": (
        "catalogNumber",
        "catalognumber",
        "dwc:catalogNumber",
    ),
    "scientific_name": (
        "scientificName",
        "scientificname",
        "dwc:scientificName",
    ),
    "taxon_id": (
        "taxonKey",
        "taxonkey",
        "taxonID",
        "taxonid",
        "dwc:taxonID",
    ),
    "taxon_rank": (
        "taxonRank",
        "taxonrank",
        "dwc:taxonRank",
    ),
    "basis_of_record": (
        "basisOfRecord",
        "basisofrecord",
        "dwc:basisOfRecord",
    ),
    "event_date": (
        "eventDate",
        "eventdate",
        "dwc:eventDate",
    ),
    "occurrence_status": (
        "occurrenceStatus",
        "occurrencestatus",
        "dwc:occurrenceStatus",
    ),
    "longitude": (
        "decimalLongitude",
        "decimallongitude",
        "dwc:decimalLongitude",
    ),
    "latitude": (
        "decimalLatitude",
        "decimallatitude",
        "dwc:decimalLatitude",
    ),
    "uncertainty": (
        "coordinateUncertaintyInMeters",
        "coordinateuncertaintyinmeters",
        "dwc:coordinateUncertaintyInMeters",
    ),
    "license": (
        "license",
        "dcterms:license",
        "rights",
    ),
    "rights_holder": (
        "rightsHolder",
        "rightsholder",
        "dcterms:rightsHolder",
    ),
    "information_withheld": (
        "informationWithheld",
        "informationwithheld",
        "dwc:informationWithheld",
    ),
    "data_generalizations": (
        "dataGeneralizations",
        "datageneralizations",
        "dwc:dataGeneralizations",
    ),
}


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def read_json_object(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    """Read one bounded UTF-8 JSON object without echoing untrusted values."""
    try:
        if path.is_symlink():
            return None, (Finding("INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("FILE_NOT_FOUND", "/"),)
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, (Finding("FILE_TOO_LARGE", "/"),)
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
                parse_float=_parse_finite_float,
            )
    except UnicodeDecodeError:
        return None, (Finding("JSON_NOT_UTF8", "/"),)
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("JSON_NONFINITE_NUMBER", "/"),)
    except json.JSONDecodeError:
        return None, (Finding("JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("FILE_READ_ERROR", "/"),)
    except (RecursionError, ValueError):
        return None, (Finding("JSON_COMPLEXITY_LIMIT", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _first(record: Mapping[str, Any], field: str) -> Any:
    for key in ALIASES[field]:
        if key in record:
            return record[key]
    return None


def _clean_text(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        value = str(value)
    if not isinstance(value, str):
        return None
    cleaned = " ".join(value.split())
    return cleaned or None


def _finite_number(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _canonical_digest(value: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def candidate_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    return _canonical_digest(projected)


def _candidate_id(source_id: str, source_record_id: str) -> str:
    key = f"{source_id}\x1f{source_record_id}".encode("utf-8")
    return "flora-occurrence-candidate:" + hashlib.sha256(key).hexdigest()[:32]


def _temporal_precision(event_date: str | None) -> str:
    if event_date is None:
        return "UNKNOWN"
    value = event_date.strip()
    if len(value) >= 10 and value[4:5] == "-" and value[7:8] == "-":
        return "DAY"
    if len(value) >= 7 and value[4:5] == "-":
        return "MONTH"
    if len(value) >= 4 and value[:4].isdigit():
        return "YEAR"
    return "UNKNOWN"


def _occurrence_status(value: str | None) -> str:
    normalized = (value or "").strip().upper().replace(" ", "_")
    if normalized in {"PRESENT", "PRESENCE"}:
        return "PRESENT"
    if normalized in {"ABSENT", "ABSENCE"}:
        return "ABSENT"
    return "UNKNOWN"


def _sensitivity_hints(record: Mapping[str, Any]) -> list[str]:
    hints: set[str] = set()
    if _clean_text(_first(record, "information_withheld")):
        hints.add("SOURCE_INFORMATION_WITHHELD")
    if _clean_text(_first(record, "data_generalizations")):
        hints.add("SOURCE_DATA_GENERALIZED")
    return sorted(hints)


def normalize_record(
    record: Mapping[str, Any], *, source_profile: str, source_id: str
) -> NormalizationResult:
    """Normalize one source record to a non-authoritative WORK candidate."""
    findings: list[Finding] = []
    profile = source_profile.strip().upper()
    clean_source_id = _clean_text(source_id)
    if profile not in SUPPORTED_PROFILES:
        findings.append(Finding("SOURCE_PROFILE_UNSUPPORTED", "/source_profile"))
    if clean_source_id is None:
        findings.append(Finding("SOURCE_ID_MISSING", "/source_id"))

    source_record_id = _clean_text(_first(record, "source_record_id"))
    scientific_name = _clean_text(_first(record, "scientific_name"))
    if source_record_id is None:
        findings.append(Finding("SOURCE_RECORD_ID_MISSING", "/source_record_id"))
    if scientific_name is None:
        findings.append(Finding("SCIENTIFIC_NAME_MISSING", "/scientific_name"))
    if findings:
        return NormalizationResult("ABSTAIN", tuple(sorted(set(findings))))

    raw_longitude = _first(record, "longitude")
    raw_latitude = _first(record, "latitude")
    longitude = _finite_number(raw_longitude)
    latitude = _finite_number(raw_latitude)
    has_longitude = raw_longitude not in (None, "")
    has_latitude = raw_latitude not in (None, "")
    if has_longitude != has_latitude:
        return NormalizationResult(
            "ERROR", (Finding("COORDINATE_PAIR_INCOMPLETE", "/spatial"),)
        )
    if has_longitude and (longitude is None or latitude is None):
        return NormalizationResult(
            "ERROR", (Finding("COORDINATE_NOT_NUMERIC", "/spatial"),)
        )
    if longitude is not None and latitude is not None:
        if not (-180.0 <= longitude <= 180.0 and -90.0 <= latitude <= 90.0):
            return NormalizationResult(
                "ERROR", (Finding("COORDINATE_OUT_OF_RANGE", "/spatial"),)
            )
        geometry: dict[str, Any] | None = {
            "type": "Point",
            "coordinates": [longitude, latitude],
        }
        coordinate_exposure = "INTERNAL_EXACT"
    else:
        geometry = None
        coordinate_exposure = "NO_COORDINATE"

    raw_uncertainty = _first(record, "uncertainty")
    uncertainty = _finite_number(raw_uncertainty)
    if raw_uncertainty not in (None, "") and uncertainty is None:
        return NormalizationResult(
            "ERROR", (Finding("UNCERTAINTY_NOT_NUMERIC", "/spatial/uncertainty_meters"),)
        )
    if uncertainty is not None and uncertainty < 0:
        return NormalizationResult(
            "ERROR", (Finding("UNCERTAINTY_NEGATIVE", "/spatial/uncertainty_meters"),)
        )

    event_date = _clean_text(_first(record, "event_date"))
    source_id_asserted = clean_source_id or "unreachable"
    candidate: dict[str, Any] = {
        "object_type": "FloraOccurrenceCandidate",
        "schema_version": "1.0.0",
        "candidate_id": _candidate_id(source_id_asserted, source_record_id),
        "hash_profile": HASH_PROFILE,
        "spec_hash": "",
        "source_context": {
            "source_id": source_id_asserted,
            "source_profile": profile,
            "source_record_id": source_record_id,
            "institution_code": _clean_text(_first(record, "institution_code")),
            "collection_code": _clean_text(_first(record, "collection_code")),
            "catalog_number": _clean_text(_first(record, "catalog_number")),
            "license": _clean_text(_first(record, "license")),
            "rights_holder": _clean_text(_first(record, "rights_holder")),
            "source_role": "OBSERVATION_CANDIDATE",
        },
        "taxon": {
            "scientific_name": scientific_name,
            "taxon_id": _clean_text(_first(record, "taxon_id")),
            "rank": _clean_text(_first(record, "taxon_rank")),
        },
        "occurrence": {
            "basis_of_record": _clean_text(_first(record, "basis_of_record")) or "UNKNOWN",
            "event_date": event_date,
            "occurrence_status": _occurrence_status(
                _clean_text(_first(record, "occurrence_status"))
            ),
        },
        "spatial": {
            "geometry": geometry,
            "crs": "EPSG:4326",
            "uncertainty_meters": uncertainty,
            "coordinate_exposure": coordinate_exposure,
        },
        "temporal": {
            "event_date_precision": _temporal_precision(event_date),
        },
        "sensitivity_hints": _sensitivity_hints(record),
        "provenance": {
            "input_digest": _canonical_digest(record),
            "normalizer_id": NORMALIZER_ID,
            "normalizer_version": NORMALIZER_VERSION,
        },
        "governance": {
            "lifecycle_state": "WORK",
            "source_admitted": False,
            "evidence_bundle_resolved": False,
            "policy_evaluated": False,
            "review_completed": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "publication_authorized": False,
            "public_use_allowed": False,
            "release_ref": None,
        },
    }
    candidate["spec_hash"] = candidate_spec_hash(candidate)
    return NormalizationResult("NORMALIZED", (), candidate)


def normalize_file(path: Path, *, source_profile: str, source_id: str) -> NormalizationResult:
    record, findings = read_json_object(path)
    if record is None:
        return NormalizationResult("ERROR", findings)
    return normalize_record(record, source_profile=source_profile, source_id=source_id)


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize_result(path: Path, result: NormalizationResult) -> str:
    return json.dumps(
        {
            "candidate": result.candidate,
            "file": _display_path(path),
            "findings": [
                {"code": item.code, "field": item.field} for item in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    )


def _fixture_manifest(root: Path) -> Mapping[str, Any]:
    path = root / "expected_outcomes.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile(root: Path) -> int:
    manifest = _fixture_manifest(root)
    cases = manifest.get("cases") if isinstance(manifest, dict) else None
    if not isinstance(cases, list) or not cases:
        print('{"outcome":"FIXTURE_MANIFEST_INVALID"}', file=sys.stderr)
        return 1
    passed = True
    for case in cases:
        if not isinstance(case, dict):
            passed = False
            continue
        input_rel = case.get("input")
        profile = case.get("source_profile")
        source_id = case.get("source_id")
        expected_outcome = case.get("outcome")
        expected_findings = sorted(case.get("findings", []))
        expected_rel = case.get("expected_candidate")
        if not all(isinstance(value, str) for value in (input_rel, profile, source_id, expected_outcome)):
            passed = False
            continue
        path = root / input_rel
        result = normalize_file(path, source_profile=profile, source_id=source_id)
        print(serialize_result(path, result))
        actual_findings = sorted({item.code for item in result.findings})
        if result.outcome != expected_outcome or actual_findings != expected_findings:
            passed = False
            print(
                json.dumps(
                    {
                        "actual_findings": actual_findings,
                        "actual_outcome": result.outcome,
                        "expected_findings": expected_findings,
                        "expected_outcome": expected_outcome,
                        "file": input_rel,
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
        if isinstance(expected_rel, str):
            try:
                expected_candidate = json.loads((root / expected_rel).read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError):
                expected_candidate = None
            if result.candidate != expected_candidate:
                passed = False
                print(
                    json.dumps(
                        {"file": input_rel, "outcome": "FIXTURE_CANDIDATE_MISMATCH"},
                        sort_keys=True,
                        separators=(",", ":"),
                    ),
                    file=sys.stderr,
                )
    return 0 if passed else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Normalize one bounded Darwin Core record to a Flora WORK candidate."
    )
    parser.add_argument("file", nargs="?", type=Path)
    parser.add_argument("--source-profile", choices=SUPPORTED_PROFILES)
    parser.add_argument("--source-id")
    parser.add_argument("--fixtures", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures is not None:
        if args.file is not None or args.source_profile is not None or args.source_id is not None:
            print("--fixtures cannot be combined with single-file arguments", file=sys.stderr)
            return 2
        return run_fixture_profile(args.fixtures)
    if args.file is None or args.source_profile is None or args.source_id is None:
        print("file, --source-profile, and --source-id are required", file=sys.stderr)
        return 2
    result = normalize_file(
        args.file, source_profile=args.source_profile, source_id=args.source_id
    )
    print(serialize_result(args.file, result))
    if result.outcome == "NORMALIZED":
        return 0
    if result.outcome == "ABSTAIN":
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
