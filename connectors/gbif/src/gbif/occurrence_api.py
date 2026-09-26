"""Offline GBIF occurrence-search planning and supplied-page parsing; never fetches.

Transport, activation, dataset-scoped rights review, sensitivity evaluation,
persistence, taxonomy anchoring and publication belong to owning layers. A
validated URL records intended provenance; it does not authenticate supplied
response bytes, establish completeness, or make any record public-safe.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
import re
from urllib.parse import parse_qs, urlencode, urlsplit

HOST = "https://api.gbif.org"
SEARCH_PATH = "/v1/occurrence/search"
# GBIF occurrence search serves at most 300 rows per page and refuses
# offset + limit beyond 100,000; larger captures need the async download product.
MAX_PAGE = 300
PAGING_CEILING = 100_000
BASIS_OF_RECORD = frozenset({
    "HUMAN_OBSERVATION", "MACHINE_OBSERVATION", "OBSERVATION", "PRESERVED_SPECIMEN",
    "FOSSIL_SPECIMEN", "LIVING_SPECIMEN", "MATERIAL_SAMPLE", "MATERIAL_CITATION",
    "OCCURRENCE"})
# The three licences GBIF accepts for occurrence data, keyed by canonical URL.
LICENSES = {
    "http://creativecommons.org/publicdomain/zero/1.0/legalcode": "CC0_1_0",
    "http://creativecommons.org/licenses/by/4.0/legalcode": "CC_BY_4_0",
    "http://creativecommons.org/licenses/by-nc/4.0/legalcode": "CC_BY_NC_4_0",
}
DATASET_KEY = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\Z")
YEAR_RANGE = re.compile(r"(\d{4})(?:,(\d{4}))?\Z")
QUERY_KEYS = frozenset({"country", "stateProvince", "taxonKey", "year", "basisOfRecord",
                        "hasCoordinate", "occurrenceStatus", "limit", "offset"})


class OccurrenceInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _integer(value: object, minimum: int, maximum: int) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise OccurrenceInputError("INTEGER_BOUND")
    return value


def _utc(value: object) -> str:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    except (ValueError, TypeError, OverflowError):
        raise OccurrenceInputError("UTC_TIME") from None


def _text(value: object, *, limit: int = 2048) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value or len(value) > limit or "\x00" in value:
        raise OccurrenceInputError("TEXT_SHAPE")
    return value


def _coordinate(value: object, bound: float) -> float | None:
    if value is None:
        return None
    if type(value) not in (int, float) or not math.isfinite(value) or abs(value) > bound:
        raise OccurrenceInputError("COORDINATE_RANGE")
    return float(value)


@dataclass(frozen=True)
class OccurrenceQuery:
    """Filter set for one bounded capture; stateProvince is a text filter, not a spatial join."""
    country: str = "US"
    state_province: str = "Kansas"
    taxon_key: int | None = None
    year: str | None = None
    basis_of_record: str | None = None
    has_coordinate: bool | None = None

    def params(self) -> dict[str, str]:
        if not re.fullmatch(r"[A-Z]{2}", self.country or ""):
            raise OccurrenceInputError("COUNTRY_CODE")
        _text(self.state_province, limit=64)
        params = {"country": self.country, "stateProvince": self.state_province}
        if self.taxon_key is not None:
            params["taxonKey"] = str(_integer(self.taxon_key, 0, 2**31 - 1))
        if self.year is not None:
            match = YEAR_RANGE.fullmatch(self.year) if isinstance(self.year, str) else None
            if match is None or (match.group(2) and match.group(2) < match.group(1)):
                raise OccurrenceInputError("YEAR_RANGE")
            params["year"] = self.year
        if self.basis_of_record is not None:
            if self.basis_of_record not in BASIS_OF_RECORD:
                raise OccurrenceInputError("BASIS_OF_RECORD")
            params["basisOfRecord"] = self.basis_of_record
        if self.has_coordinate is not None:
            if type(self.has_coordinate) is not bool:
                raise OccurrenceInputError("HAS_COORDINATE")
            params["hasCoordinate"] = "true" if self.has_coordinate else "false"
        return params


@dataclass(frozen=True)
class PagePlan:
    offset: int
    limit: int
    url: str


def plan_pages(query: OccurrenceQuery, *, max_records: int = 3000,
               page_size: int = MAX_PAGE) -> tuple[PagePlan, ...]:
    """Plan a finite offset sequence; never implies the result set fits within it.

    The first parsed page reports ``count``; a count above ``max_records`` or the
    GBIF paging ceiling must be routed to review or the async download product.
    """
    params = query.params()
    _integer(page_size, 1, MAX_PAGE)
    _integer(max_records, 1, PAGING_CEILING)
    return tuple(PagePlan(offset, min(page_size, max_records - offset),
                          f"{HOST}{SEARCH_PATH}?" + urlencode(
                              dict(params, limit=min(page_size, max_records - offset),
                                   offset=offset)))
                 for offset in range(0, max_records, page_size))


def _request(url: object) -> tuple[dict[str, str], int, int]:
    if not isinstance(url, str) or len(url) > 4096 or any(ord(c) <= 32 for c in url):
        raise OccurrenceInputError("SOURCE_URL")
    try:
        parsed = urlsplit(url)
        if (parsed.scheme != "https" or parsed.netloc != "api.gbif.org"
                or parsed.path != SEARCH_PATH or parsed.fragment):
            raise ValueError
        raw = parse_qs(parsed.query, strict_parsing=True, keep_blank_values=True)
        if set(raw) - QUERY_KEYS or any(len(v) != 1 or not v[0] for v in raw.values()):
            raise ValueError
        params = {key: value[0] for key, value in raw.items()}
        limit, offset = int(params.pop("limit")), int(params.pop("offset"))
        _integer(limit, 1, MAX_PAGE)
        _integer(offset, 0, PAGING_CEILING - limit)
        return params, offset, limit
    except (KeyError, ValueError, TypeError, OccurrenceInputError):
        raise OccurrenceInputError("SOURCE_URL") from None


def _object_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise OccurrenceInputError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _constant(_: str) -> None:
    raise OccurrenceInputError("NONSTANDARD_JSON_NUMBER")


@dataclass(frozen=True)
class OccurrenceCandidate:
    gbif_key: int
    dataset_key: str | None
    basis_of_record: str | None
    occurrence_status: str | None
    taxon_key: int | None
    scientific_name: str | None
    event_date: str | None
    # Coordinates are carried exactly as supplied; never de-obscured or re-rounded here.
    latitude: float | None
    longitude: float | None
    coordinate_uncertainty_m: float | None
    license_id: str | None
    route: str
    reasons: tuple[str, ...]
    # Normalized JSON retains every source field. Never log, render, or publish it.
    raw_record_json: str
    record_sha256: str
    # The connector cannot evaluate taxon or location sensitivity.
    sensitivity: str = "NOT_EVALUATED"
    admission: str = "NOT_ADMITTED"


def _classify(record: dict[str, object]) -> OccurrenceCandidate:
    key = record.get("key")
    if type(key) is not int or key < 0:
        raise OccurrenceInputError("OCCURRENCE_KEY")
    reasons: list[str] = []
    dataset = record.get("datasetKey")
    if not isinstance(dataset, str) or not DATASET_KEY.fullmatch(dataset):
        dataset = None
        reasons.append("DATASET_IDENTITY_MISSING")
    license_url = record.get("license")
    license_id = LICENSES.get(license_url.replace("https://", "http://")
                              if isinstance(license_url, str) else "")
    if license_id is None:
        reasons.append("LICENSE_UNRESOLVED")
    elif license_id == "CC_BY_NC_4_0":
        reasons.append("NONCOMMERCIAL_TERMS")
    if record.get("informationWithheld") not in (None, ""):
        reasons.append("INFORMATION_WITHHELD")
    if record.get("dataGeneralizations") not in (None, ""):
        reasons.append("DATA_GENERALIZED")
    basis = _text(record.get("basisOfRecord"), limit=64)
    if basis is not None and basis not in BASIS_OF_RECORD:
        reasons.append("BASIS_OF_RECORD_UNKNOWN")
    status = _text(record.get("occurrenceStatus"), limit=16)
    if status == "ABSENT":
        reasons.append("ABSENCE_ASSERTION")
    elif status not in (None, "PRESENT"):
        reasons.append("OCCURRENCE_STATUS_UNKNOWN")
    latitude = _coordinate(record.get("decimalLatitude"), 90)
    longitude = _coordinate(record.get("decimalLongitude"), 180)
    if (latitude is None) != (longitude is None):
        raise OccurrenceInputError("COORDINATE_PAIR")
    if latitude is None:
        reasons.append("COORDINATES_ABSENT")
    uncertainty = record.get("coordinateUncertaintyInMeters")
    if uncertainty is not None and (type(uncertainty) not in (int, float)
                                    or not math.isfinite(uncertainty) or uncertainty < 0):
        raise OccurrenceInputError("COORDINATE_UNCERTAINTY")
    taxon = record.get("taxonKey")
    if taxon is not None and (type(taxon) is not int or taxon < 0):
        raise OccurrenceInputError("TAXON_KEY")
    try:
        raw_json = json.dumps(record, sort_keys=True, ensure_ascii=True,
                              separators=(",", ":"), allow_nan=False)
    except (ValueError, RecursionError):
        raise OccurrenceInputError("RECORD_JSON") from None
    # Noncommercial terms and absence assertions are carried as flags; everything
    # else that leaves rights or precision unresolved goes to quarantine.
    blocking = [r for r in reasons if r not in {"NONCOMMERCIAL_TERMS", "ABSENCE_ASSERTION"}]
    return OccurrenceCandidate(
        key, dataset, basis, status, taxon, _text(record.get("scientificName"), limit=512),
        _text(record.get("eventDate"), limit=64), latitude, longitude,
        None if uncertainty is None else float(uncertainty), license_id,
        "QUARANTINE_CANDIDATE" if blocking else "RAW_CANDIDATE", tuple(reasons), raw_json,
        "sha256:" + sha256(raw_json.encode("utf-8")).hexdigest())


@dataclass(frozen=True)
class PageCandidate:
    source_url: str
    query: tuple[tuple[str, str], ...]
    offset: int
    limit: int
    count: int
    end_of_records: bool
    retrieved_at: str
    body_sha256: str
    records: tuple[OccurrenceCandidate, ...]


def parse_page(body: bytes, *, status: int, source_url: str, retrieved_at: str,
               max_bytes: int = 16 * 1024 * 1024) -> PageCandidate:
    """Parse one supplied search page; reject a malformed page whole, never drop rows."""
    params, offset, limit = _request(source_url)
    retrieved = _utc(retrieved_at)
    _integer(max_bytes, 1, 64 * 1024 * 1024)
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise OccurrenceInputError("RESPONSE_BOUND")
    if status != 200:
        raise OccurrenceInputError("HTTP_STATUS")
    try:
        payload = json.loads(body.decode("utf-8"), object_pairs_hook=_object_pairs,
                             parse_constant=_constant)
    except (UnicodeError, ValueError, RecursionError):
        raise OccurrenceInputError("INVALID_JSON") from None
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        raise OccurrenceInputError("PAGE_SHAPE")
    results = payload["results"]
    if (type(payload.get("offset")) is not int or type(payload.get("limit")) is not int
            or payload["offset"] != offset or payload["limit"] != limit):
        raise OccurrenceInputError("PAGE_WINDOW_MISMATCH")
    count, end = payload.get("count"), payload.get("endOfRecords")
    if type(count) is not int or count < 0 or type(end) is not bool:
        raise OccurrenceInputError("PAGE_METADATA")
    if len(results) > limit:
        raise OccurrenceInputError("PAGE_LIMIT_EXCEEDED")
    if not end and len(results) != limit:
        raise OccurrenceInputError("SHORT_PAGE_NOT_TERMINAL")
    records: list[OccurrenceCandidate] = []
    for record in results:
        if not isinstance(record, dict):
            raise OccurrenceInputError("RECORD_SHAPE")
        records.append(_classify(record))
    if len({item.gbif_key for item in records}) != len(records):
        raise OccurrenceInputError("DUPLICATE_OCCURRENCE_KEY")
    return PageCandidate(source_url, tuple(sorted(params.items())), offset, limit, count, end,
                         retrieved, "sha256:" + sha256(body).hexdigest(), tuple(records))


@dataclass(frozen=True)
class CaptureCandidate:
    outcome: str
    reasons: tuple[str, ...]
    reported_count: int | None
    records: tuple[OccurrenceCandidate, ...]
    page_sha256: tuple[str, ...]
    # Reconciliation proves page continuity only, never biological completeness or absence.
    coverage: str = "NOT_ESTABLISHED"
    admission: str = "NOT_ADMITTED"


def reconcile(pages: tuple[PageCandidate, ...] | list[PageCandidate]) -> CaptureCandidate:
    """Join parsed pages into one finite capture outcome.

    ``CAPTURE_CANDIDATE`` means contiguous, duplicate-free pages that reached
    ``endOfRecords`` with a record total equal to the reported count; every other
    shape is ``INCOMPLETE_CAPTURE`` (quarantine) or ``HOLD`` (paging ceiling).
    """
    if not pages:
        raise OccurrenceInputError("NO_PAGES")
    if any(not isinstance(page, PageCandidate) for page in pages):
        raise OccurrenceInputError("PAGE_TYPE")
    ordered = sorted(pages, key=lambda page: page.offset)
    reasons: list[str] = []
    if len({page.query for page in ordered}) != 1:
        raise OccurrenceInputError("MIXED_QUERY")
    counts = {page.count for page in ordered}
    if len(counts) != 1:
        reasons.append("COUNT_DRIFT")
    expected = 0
    for page in ordered:
        if page.offset != expected:
            reasons.append("PAGE_GAP_OR_OVERLAP")
            break
        expected += len(page.records)
    records = tuple(record for page in ordered for record in page.records)
    if len({record.gbif_key for record in records}) != len(records):
        reasons.append("DUPLICATE_ACROSS_PAGES")
    if not ordered[-1].end_of_records:
        reasons.append("END_OF_RECORDS_NOT_REACHED")
    if any(page.end_of_records for page in ordered[:-1]):
        reasons.append("EARLY_END_OF_RECORDS")
    reported = ordered[0].count if len(counts) == 1 else None
    if reported is not None and reported != len(records):
        reasons.append("COUNT_MISMATCH")
    if reported is not None and reported > PAGING_CEILING:
        return CaptureCandidate("HOLD", ("PAGING_CEILING_USE_ASYNC_DOWNLOAD", *reasons),
                                reported, records, tuple(p.body_sha256 for p in ordered))
    return CaptureCandidate("INCOMPLETE_CAPTURE" if reasons else "CAPTURE_CANDIDATE",
                            tuple(reasons), reported, records,
                            tuple(p.body_sha256 for p in ordered))
