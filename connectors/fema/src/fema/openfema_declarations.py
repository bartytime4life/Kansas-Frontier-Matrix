"""Offline OpenFEMA Disaster Declarations Summaries (v2) planning and parsing; never fetches.

One OpenFEMA table only: there is no umbrella OpenFEMA admission. Every record
is an ``administrative`` FEMA action, never an observed hazard event, damage
extent, or aid eligibility for a person or property. A designated area is a
jurisdiction, not a hazard footprint. Declaration, incident, closeout, and
refresh times stay distinct. Activation, rights review, persistence, and any
Hazards-domain projection belong to owning layers.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
import re
from urllib.parse import parse_qs, urlencode, urlsplit

HOST = "https://www.fema.gov"
PATH = "/api/open/v2/DisasterDeclarationsSummaries"
ENTITY = "DisasterDeclarationsSummaries"
MAX_TOP = 10_000
KANSAS = ("KS", "20")
DECLARATION_TYPES = frozenset({"DR", "EM", "FM"})
# Fields this profile interprets; any other field is preserved and flagged as drift.
REQUIRED_FIELDS = frozenset({
    "femaDeclarationString", "disasterNumber", "state", "declarationType",
    "declarationDate", "fyDeclared", "incidentType", "declarationTitle",
    "ihProgramDeclared", "iaProgramDeclared", "paProgramDeclared", "hmProgramDeclared",
    "incidentBeginDate", "incidentEndDate", "disasterCloseoutDate", "tribalRequest",
    "fipsStateCode", "fipsCountyCode", "placeCode", "designatedArea",
    "declarationRequestNumber", "lastRefresh", "hash", "id"})
KNOWN_OPTIONAL_FIELDS = frozenset({
    "lastIAFilingDate", "incidentId", "region", "designatedIncidentTypes"})
DECLARATION_STRING = re.compile(r"(DR|EM|FM)-(\d{1,5})-([A-Z]{2})\Z")
RECORD_ID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\Z")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")


class OpenFemaInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _instant(value: object, code: str = "TIME_FORMAT") -> datetime:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc)
    except (ValueError, TypeError, OverflowError):
        raise OpenFemaInputError(code) from None


def _iso(value: datetime | None) -> str | None:
    return None if value is None else value.isoformat(timespec="seconds").replace("+00:00", "Z")


def _calendar_date(value: object) -> str:
    if not isinstance(value, str) or not DATE.fullmatch(value):
        raise OpenFemaInputError("DATE_BOUND")
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise OpenFemaInputError("DATE_BOUND") from None
    return value


def declaration_filter(*, declared_from: str | None = None, declared_to: str | None = None) -> str:
    """Kansas filter, optionally bounded by a half-open declaration-date window."""
    clauses = [f"state eq '{KANSAS[0]}'"]
    if declared_from is not None:
        clauses.append(f"declarationDate ge '{_calendar_date(declared_from)}T00:00:00.000Z'")
    if declared_to is not None:
        clauses.append(f"declarationDate lt '{_calendar_date(declared_to)}T00:00:00.000Z'")
    if declared_from is not None and declared_to is not None and declared_from >= declared_to:
        raise OpenFemaInputError("DATE_ORDER")
    return " and ".join(clauses)


# The only filter grammar this profile emits or accepts: Kansas, an optional
# half-open declaration window, and an optional keyset cursor on the record id.
FILTER = re.compile(
    r"state eq 'KS'"
    r"(?: and declarationDate ge '(?P<start>\d{4}-\d{2}-\d{2})T00:00:00\.000Z')?"
    r"(?: and declarationDate lt '(?P<stop>\d{4}-\d{2}-\d{2})T00:00:00\.000Z')?"
    r"(?: and id gt '(?P<after>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})')?"
    r"\Z")


@dataclass(frozen=True)
class PageRequest:
    base_filter: str
    after_id: str | None
    top: int
    declared_from: datetime | None
    declared_to: datetime | None

    @property
    def odata_filter(self) -> str:
        if self.after_id is None:
            return self.base_filter
        return f"{self.base_filter} and id gt '{self.after_id}'"


def _parse_filter(odata_filter: object, top: object) -> PageRequest:
    match = FILTER.fullmatch(odata_filter) if isinstance(odata_filter, str) else None
    if match is None:
        raise OpenFemaInputError("FILTER_SCOPE")
    if type(top) is not int or not 1 <= top <= MAX_TOP:
        raise OpenFemaInputError("PAGE_BOUND")
    bounds = []
    for key in ("start", "stop"):
        value = match.group(key)
        bounds.append(None if value is None else
                      datetime.strptime(_calendar_date(value), "%Y-%m-%d").replace(tzinfo=timezone.utc))
    if bounds[0] is not None and bounds[1] is not None and bounds[0] >= bounds[1]:
        raise OpenFemaInputError("DATE_ORDER")
    after = match.group("after")
    base = odata_filter if after is None else odata_filter[: -len(f" and id gt '{after}'")]
    return PageRequest(base, after, top, bounds[0], bounds[1])


def page_url(odata_filter: str, *, after_id: str | None = None, top: int = 1000) -> str:
    """One keyset page: ``id gt`` the previous page's last id, ordered by id, counted.

    Keyset paging is used instead of ``$skip`` so that rows inserted or deleted
    between requests cannot shift offsets and silently drop a record; each page's
    count is the number of rows remaining past the cursor, which ``reconcile``
    checks for consistency.
    """
    request = _parse_filter(odata_filter, top)
    if request.after_id is not None:
        raise OpenFemaInputError("FILTER_SCOPE")  # pass the cursor via after_id only
    if after_id is not None and not (isinstance(after_id, str) and RECORD_ID.fullmatch(after_id)):
        raise OpenFemaInputError("RECORD_ID")
    full = odata_filter if after_id is None else f"{odata_filter} and id gt '{after_id}'"
    return f"{HOST}{PATH}?" + urlencode({"$filter": full, "$orderby": "id", "$top": top,
                                         "$count": "true"})


def _request(url: object) -> PageRequest:
    if not isinstance(url, str) or len(url) > 4096 or any(ord(c) <= 32 for c in url):
        raise OpenFemaInputError("SOURCE_URL")
    parsed = urlsplit(url)
    if (parsed.scheme != "https" or parsed.netloc != "www.fema.gov" or parsed.path != PATH
            or parsed.fragment):
        raise OpenFemaInputError("SOURCE_URL")
    try:
        raw = parse_qs(parsed.query, strict_parsing=True)
        if set(raw) != {"$filter", "$orderby", "$top", "$count"}:
            raise ValueError
        if any(len(v) != 1 for v in raw.values()):
            raise ValueError
        if raw["$orderby"][0] != "id" or raw["$count"][0] != "true":
            raise ValueError
        return _parse_filter(raw["$filter"][0], int(raw["$top"][0]))
    except (KeyError, ValueError, OpenFemaInputError):
        raise OpenFemaInputError("SOURCE_URL") from None


@dataclass(frozen=True)
class DeclarationCandidate:
    record_id: str
    fema_declaration_string: str
    disaster_number: int
    declaration_type: str
    incident_type: str
    declaration_title: str
    # Time kinds are never collapsed into one event time.
    declaration_date: str
    incident_begin_date: str | None
    incident_end_date: str | None
    disaster_closeout_date: str | None
    last_refresh: str
    programs_declared: tuple[tuple[str, bool], ...]
    fips_state_code: str
    fips_county_code: str
    place_code: str
    designated_area: str
    designated_area_kind: str
    source_hash: str | None
    route: str
    reasons: tuple[str, ...]
    raw_record_json: str
    record_sha256: str
    source_role: str = "administrative"
    role_authority: str = "FEMA"
    geography_semantics: str = "DESIGNATED_JURISDICTION_NOT_HAZARD_FOOTPRINT"
    admission: str = "NOT_ADMITTED"


def _object_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise OpenFemaInputError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _constant(_: str) -> None:
    raise OpenFemaInputError("NONSTANDARD_JSON_NUMBER")


def _text(record: dict, key: str, limit: int = 512) -> str:
    value = record.get(key)
    if not isinstance(value, str) or not value or len(value) > limit:
        raise OpenFemaInputError("FIELD_SHAPE")
    return value


def _classify(record: object) -> DeclarationCandidate:
    if not isinstance(record, dict):
        raise OpenFemaInputError("RECORD_SHAPE")
    if REQUIRED_FIELDS - set(record):
        raise OpenFemaInputError("SCHEMA_FIELD_MISSING")
    reasons: list[str] = []
    if set(record) - REQUIRED_FIELDS - KNOWN_OPTIONAL_FIELDS:
        reasons.append("SCHEMA_DRIFT_ADDITIONAL_FIELD")
    record_id = _text(record, "id", 64)
    if not RECORD_ID.fullmatch(record_id):
        raise OpenFemaInputError("RECORD_ID")
    declaration = _text(record, "femaDeclarationString", 32)
    match = DECLARATION_STRING.fullmatch(declaration)
    number = record.get("disasterNumber")
    if type(number) is not int or number < 1:
        raise OpenFemaInputError("DISASTER_NUMBER")
    kind = _text(record, "declarationType", 4)
    if kind not in DECLARATION_TYPES:
        raise OpenFemaInputError("DECLARATION_TYPE")
    if match is None or match.group(1) != kind or int(match.group(2)) != number:
        reasons.append("DECLARATION_IDENTITY_INCONSISTENT")
    if (record.get("state"), record.get("fipsStateCode")) != KANSAS or (
            match is not None and match.group(3) != KANSAS[0]):
        raise OpenFemaInputError("STATE_SCOPE_MISMATCH")
    county, place = record.get("fipsCountyCode"), record.get("placeCode")
    if not (isinstance(county, str) and re.fullmatch(r"\d{3}", county)
            and isinstance(place, str) and re.fullmatch(r"\d{1,6}", place)):
        raise OpenFemaInputError("GEOGRAPHY_CODE")
    declared = _instant(record["declarationDate"])
    begin = None if record["incidentBeginDate"] is None else _instant(record["incidentBeginDate"])
    end = None if record["incidentEndDate"] is None else _instant(record["incidentEndDate"])
    closeout = (None if record["disasterCloseoutDate"] is None
                else _instant(record["disasterCloseoutDate"]))
    refreshed = _instant(record["lastRefresh"])
    if begin is None:
        reasons.append("INCIDENT_BEGIN_ABSENT")
    if end is None:
        reasons.append("INCIDENT_END_UNSET")
    elif begin is not None and end < begin:
        reasons.append("INCIDENT_END_BEFORE_BEGIN")
    if closeout is not None and closeout < declared:
        reasons.append("CLOSEOUT_BEFORE_DECLARATION")
    programs = []
    for key in ("ihProgramDeclared", "iaProgramDeclared", "paProgramDeclared",
                "hmProgramDeclared", "tribalRequest"):
        if type(record[key]) is not bool:
            raise OpenFemaInputError("PROGRAM_FLAG")
        programs.append((key, record[key]))
    source_hash = record.get("hash")
    if source_hash is not None and (not isinstance(source_hash, str) or len(source_hash) > 128):
        raise OpenFemaInputError("FIELD_SHAPE")
    try:
        raw_json = json.dumps(record, sort_keys=True, ensure_ascii=True,
                              separators=(",", ":"), allow_nan=False)
    except (ValueError, RecursionError):
        raise OpenFemaInputError("RECORD_JSON") from None
    # Unset incident end and additive schema drift are flags; inconsistent identity
    # or impossible time ordering goes to quarantine.
    blocking = {"DECLARATION_IDENTITY_INCONSISTENT", "INCIDENT_END_BEFORE_BEGIN",
                "CLOSEOUT_BEFORE_DECLARATION"}
    return DeclarationCandidate(
        record_id, declaration, number, kind, _text(record, "incidentType", 128),
        _text(record, "declarationTitle"), _iso(declared), _iso(begin), _iso(end),
        _iso(closeout), _iso(refreshed), tuple(programs), KANSAS[1], county, place,
        _text(record, "designatedArea", 256), "statewide" if county == "000" else "county",
        source_hash, "QUARANTINE_CANDIDATE" if blocking.intersection(reasons) else "RAW_CANDIDATE",
        tuple(reasons), raw_json, "sha256:" + sha256(raw_json.encode("utf-8")).hexdigest())


@dataclass(frozen=True)
class PageCandidate:
    source_url: str
    request: PageRequest
    reported_count: int
    run_date: str | None
    retrieved_at: str
    body_sha256: str
    records: tuple[DeclarationCandidate, ...]

    @property
    def is_last(self) -> bool:
        return len(self.records) < self.request.top


def parse_page(body: bytes, *, status: int, source_url: str, retrieved_at: str,
               max_bytes: int = 64 * 1024 * 1024) -> PageCandidate:
    """Parse one supplied page; metadata must echo the request, else the page is rejected."""
    request = _request(source_url)
    retrieved = _iso(_instant(retrieved_at, "UTC_TIME"))
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise OpenFemaInputError("RESPONSE_BOUND")
    if status == 429:
        raise OpenFemaInputError("RATE_LIMITED")
    if status != 200:
        raise OpenFemaInputError("HTTP_STATUS")
    try:
        payload = json.loads(body.decode("utf-8"), object_pairs_hook=_object_pairs,
                             parse_constant=_constant)
    except OpenFemaInputError:
        raise
    except (UnicodeError, ValueError, RecursionError):
        raise OpenFemaInputError("INVALID_JSON") from None
    if not isinstance(payload, dict) or not isinstance(payload.get(ENTITY), list):
        raise OpenFemaInputError("PAGE_SHAPE")
    metadata = payload.get("metadata")
    if not isinstance(metadata, dict):
        raise OpenFemaInputError("METADATA_ABSENT")
    count = metadata.get("count")
    if type(count) is not int or count < 0:
        raise OpenFemaInputError("COUNT_ABSENT")
    if (metadata.get("skip") not in (None, 0) or metadata.get("top") != request.top
            or metadata.get("filter") != request.odata_filter
            or metadata.get("entityname") not in (None, ENTITY)):
        raise OpenFemaInputError("METADATA_REQUEST_MISMATCH")
    rows = payload[ENTITY]
    if len(rows) > request.top:
        raise OpenFemaInputError("PAGE_LIMIT_EXCEEDED")
    records = tuple(_classify(row) for row in rows)
    ids = [record.record_id for record in records]
    if len(set(ids)) != len(ids):
        raise OpenFemaInputError("DUPLICATE_RECORD_ID")
    if ids != sorted(ids) or (request.after_id is not None and ids and ids[0] <= request.after_id):
        raise OpenFemaInputError("ORDER_NOT_DETERMINISTIC")
    for record in records:
        declared = _instant(record.declaration_date)
        # The provider or a saved response may not have honored the filter.
        if ((request.declared_from is not None and declared < request.declared_from)
                or (request.declared_to is not None and declared >= request.declared_to)):
            raise OpenFemaInputError("ROW_OUTSIDE_REQUESTED_WINDOW")
    run_date = metadata.get("rundate")
    return PageCandidate(source_url, request, count,
                         _iso(_instant(run_date)) if isinstance(run_date, str) else None,
                         retrieved, "sha256:" + sha256(body).hexdigest(), records)


def next_page_url(page: PageCandidate) -> str | None:
    if not isinstance(page, PageCandidate):
        raise OpenFemaInputError("PAGE_TYPE")
    if page.is_last:
        return None
    return page_url(page.request.base_filter, after_id=page.records[-1].record_id,
                    top=page.request.top)


@dataclass(frozen=True)
class CaptureCandidate:
    outcome: str
    reasons: tuple[str, ...]
    reported_count: int
    records: tuple[DeclarationCandidate, ...]
    page_sha256: tuple[str, ...]
    coverage: str = "NOT_ESTABLISHED"
    admission: str = "NOT_ADMITTED"


def reconcile(pages: tuple[PageCandidate, ...] | list[PageCandidate]) -> CaptureCandidate:
    """Join a keyset walk into one finite outcome.

    ``CAPTURE_CANDIDATE`` requires an unbroken cursor chain from the uncursored
    first page to a short final page, where every page's count equals the first
    page's count minus the records already seen. Any insertion or deletion
    during the walk breaks that equation and yields ``INCOMPLETE_CAPTURE``.
    """
    if not pages or any(not isinstance(page, PageCandidate) for page in pages):
        raise OpenFemaInputError("NO_PAGES" if not pages else "PAGE_TYPE")
    if len({(p.request.base_filter, p.request.top) for p in pages}) != 1:
        raise OpenFemaInputError("MIXED_QUERY")
    ordered = sorted(pages, key=lambda page: page.request.after_id or "")
    reasons: list[str] = []
    if ordered[0].request.after_id is not None:
        reasons.append("CURSOR_NOT_FROM_START")
    seen = 0
    for previous, page in zip([None, *ordered], ordered):
        if previous is not None and (
                not previous.records or page.request.after_id != previous.records[-1].record_id):
            reasons.append("CURSOR_GAP_OR_OVERLAP")
            break
        if page.reported_count != ordered[0].reported_count - seen:
            reasons.append("COUNT_DRIFT")
            break
        seen += len(page.records)
    if not ordered[-1].is_last:
        reasons.append("END_NOT_REACHED")
    if any(page.is_last for page in ordered[:-1]):
        reasons.append("EARLY_END")
    records = tuple(record for page in ordered for record in page.records)
    ids = [record.record_id for record in records]
    if len(set(ids)) != len(ids):
        reasons.append("DUPLICATE_ACROSS_PAGES")
    if ids != sorted(ids):
        reasons.append("ORDER_NOT_DETERMINISTIC")
    if not reasons and len(records) != ordered[0].reported_count:
        reasons.append("COUNT_MISMATCH")
    return CaptureCandidate("INCOMPLETE_CAPTURE" if reasons else "CAPTURE_CANDIDATE",
                            tuple(dict.fromkeys(reasons)), ordered[0].reported_count, records,
                            tuple(page.body_sha256 for page in ordered))
