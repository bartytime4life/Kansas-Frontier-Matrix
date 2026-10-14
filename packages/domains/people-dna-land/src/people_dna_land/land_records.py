"""Closed, evidence-bound land-instrument candidates. No title or release authority.

The inputs are official rendered GLO index text or explicitly mapped lawful CSV
exports/transcriptions. A record of an instrument is not current ownership, a
completed arm's-length sale, or proof of a parcel boundary.
"""
from __future__ import annotations

import csv
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import re
from urllib.parse import parse_qs, unquote, urlsplit

PROFILE = "kfm.land-instrument-candidate/v1"
MAX_BYTES = 10 * 1024 * 1024
MAX_RECORDS = 1000
SOURCES = {
    "blm-glo": {"hosts": {"glorecords.blm.gov", "glo-entry-prod.blm.gov"}, "formats": {"glo-text", "mapped-csv"}},
    "blm-mlrs": {"hosts": {"reports.blm.gov", "mlrs.blm.gov"}, "formats": {"mapped-csv"}},
    "kshs-land-sales": {"hosts": {"www.kansashistory.gov", "www.kansasmemory.gov"}, "formats": {"mapped-csv"}},
    "sedgwick-deeds": {"hosts": {"www.sedgwickcounty.org", "www.sedgwick.gov"}, "formats": {"mapped-csv"}},
    "johnson-deeds": {"hosts": {"www.jocogov.org", "ims.jocogov.org"}, "formats": {"mapped-csv"}},
}
KINDS = {"patent", "deed", "warranty_deed", "quitclaim_deed", "railroad_sale", "tract_book_entry", "land_tenure_case", "sale_notice", "other_instrument"}
STATES = {"RECORDED", "ISSUED", "PROPOSED", "CASE_ACTION", "UNKNOWN"}
PRICE_KINDS = {"sale_price", "consideration", "nominal_consideration", "recorded_principal", "appraised_value", "minimum_bid"}
FIELDS = {"source_record_id", "instrument_type", "event_date", "recording_date", "county", "state", "transaction_status", "grantor", "grantee", "legal_description", "acres", "amount", "amount_kind", "currency", "notes"}
REQUIRED = {"source_record_id", "instrument_type", "event_date", "state", "transaction_status"}
HEX = re.compile(r"sha256:[a-f0-9]{64}\Z")


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False, separators=(",", ":")).encode()


def digest(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def stamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def instant(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", value):
        raise ValueError("UTC_TIMESTAMP_REQUIRED")
    datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    return value


def text(value, limit=2048, *, required=False):
    if value in (None, "", "-----") and not required:
        return None
    if not isinstance(value, str) or not value.strip() or len(value) > limit or any(ord(c) < 32 and c not in "\n\t" for c in value) or "\x7f" in value:
        raise ValueError("RECORD_TEXT_INVALID")
    return value.strip()


def iso_date(value, *, required=False):
    value = text(value, 10, required=required)
    if value is None:
        return None
    if not re.fullmatch(r"\d{4}-\d\d-\d\d", value):
        raise ValueError("DATE_FORMAT_INVALID")
    date.fromisoformat(value)
    return value


def decimal(value, *, positive=False):
    value = text(value, 32)
    if value is None:
        return None
    # No implicit commas, currency symbols, exponent, rounding or inferred USD.
    if not re.fullmatch(r"\d{1,18}(?:\.\d{1,6})?", value):
        raise ValueError("DECIMAL_FORMAT_INVALID")
    try:
        n = Decimal(value)
    except InvalidOperation:
        raise ValueError("DECIMAL_FORMAT_INVALID") from None
    if positive and n <= 0:
        raise ValueError("AREA_MUST_BE_POSITIVE")
    return format(n, "f")


def source_url(source: str, value: str) -> str:
    if source not in SOURCES or not isinstance(value, str) or len(value) > 2048 or any(c.isspace() or ord(c) < 32 for c in value):
        raise ValueError("SOURCE_URL_INVALID")
    u = urlsplit(value)
    if u.scheme != "https" or u.hostname not in SOURCES[source]["hosts"] or u.port not in (None, 443) or u.username or u.password or u.fragment or "\\" in value:
        raise ValueError("SOURCE_URL_NOT_ALLOWED")
    # Do not retain account/session identifiers, signatures, or bearer URLs.
    if re.search(r"token|secret|password|session|authorization|signature|api.?key|siwc", unquote(u.query), re.I):
        raise ValueError("SOURCE_URL_CREDENTIAL_QUERY")
    return value


def _glo_rows(raw: bytes):
    """Parse the observed 2026 GLO CDI/patent result-card text; refuse drift.

    A DOM text capture is a derivative, not the underlying patent image or an
    HTTP payload. Page position is retained as a locator, never used as identity.
    Hidden 'Show More' land rows remain explicitly incomplete.
    """
    content = raw.decode("utf-8")
    summary = re.findall(r"(\d+)-(\d+) of (\d+) results", content)
    if not summary or any(s != summary[0] for s in summary):
        raise ValueError("GLO_PAGE_SUMMARY_REQUIRED")
    start, end, total = map(int, summary[0])
    if not 1 <= start <= end <= total:
        raise ValueError("GLO_PAGE_RANGE_INVALID")
    cards = content.split("View Details\n")[1:]
    if len(cards) != end - start + 1:
        raise ValueError("GLO_PAGE_CARD_COUNT_MISMATCH")
    rows = []
    for ordinal, block in enumerate(cards, start):
        match = re.fullmatch(r"(Control Document Index \(CDI\)|Patent) Details:\nName\(s\):\n(.*?)\nDate:\n(.*?)\nState:\n(.*?)\nCounty:\n(.*?)\nDocument#:\n(.*?)\nDocument Type:\n(.*?)\nLand Description(?:s \((\d+)\))?:\nMeridian\tTownship\tRange\tSection\(s\)\tSubdivision\n(.*)", block, re.S)
        if match is None:
            raise ValueError("GLO_CARD_FORMAT_DRIFT")
        category, party, when, state, county, number, kind, nland, land = match.groups()
        land = re.split(r"\n\n?(?:Show More|\d+-\d+ of \d+ results)", land)[0].strip()
        lines = land.splitlines()
        if not lines or any(len(line.split("\t")) != 5 for line in lines):
            raise ValueError("GLO_LAND_TABLE_DRIFT")
        types = {"Patent": "patent", "Warranty deed": "warranty_deed", "Quit claim deed": "quitclaim_deed", "Act of congress": "other_instrument"}
        if kind not in types:
            raise ValueError("GLO_DOCUMENT_TYPE_UNMAPPED")
        when = datetime.strptime(when, "%m-%d-%Y").date().isoformat()
        key = digest(canonical([category, number, when, state, county, land]))
        rows.append({"source_record_id": "index-composite:" + key[7:], "instrument_type": types[kind], "event_date": when,
                     "recording_date": None, "state": "KS" if state == "Kansas" else state, "county": county,
                     "transaction_status": "RECORDED", "grantor": None, "grantee": party,
                     "legal_description": land, "acres": None, "amount": None, "amount_kind": None, "currency": None,
                     "notes": "GLO " + category + "; document " + number + "; " + kind,
                     "_flags": ["INDEX_ENTRY_ONLY", "COMPOSITE_IDENTITY", "CURRENT_OWNERSHIP_NOT_ESTABLISHED"] + (["LEGAL_DESCRIPTION_PARTIAL"] if nland and int(nland) != len(lines) else []),
                     "_locator": "result-card:" + str(ordinal)})
    return rows, {"start": start, "end": end, "reported_total": total, "scope": "KEYWORD_RESULTS", "complete": start == 1 and end == total}


def _csv_rows(raw: bytes, mapping: dict):
    if not isinstance(mapping, dict) or not REQUIRED <= set(mapping) <= FIELDS or any(not isinstance(v, str) or not v for v in mapping.values()) or len(set(mapping.values())) != len(mapping):
        raise ValueError("EXPLICIT_COLUMN_MAP_REQUIRED")
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig"), newline=""), strict=True)
    if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)) or set(mapping.values()) - set(reader.fieldnames):
        raise ValueError("CSV_HEADER_DRIFT")
    rows = []
    for ordinal, row in enumerate(reader, 2):
        if None in row or any(v is None for v in row.values()):
            raise ValueError("CSV_ROW_SHAPE_INVALID")
        if len(rows) >= MAX_RECORDS:
            raise ValueError("RECORD_LIMIT")
        rows.append({**{key: row[column] for key, column in mapping.items()}, "_locator": "csv-row:" + str(ordinal), "_flags": ["MAPPED_EXPORT_REVIEW_REQUIRED"]})
    if not rows:
        raise ValueError("EMPTY_EXPORT")
    return rows, {"scope": "EXPLICIT_EXPORT", "complete": False, "reported_total": None}


def make_record(row: dict, source: str, retrieved_at: str) -> dict:
    if not isinstance(row, dict) or set(row) - FIELDS - {"_locator", "_flags"} or not REQUIRED <= set(row):
        raise ValueError("RECORD_FIELDS_INVALID")
    key = text(row["source_record_id"], 256, required=True)
    kind, state = row["instrument_type"], row["state"]
    status = row["transaction_status"]
    if kind not in KINDS or state != "KS" or status not in STATES:
        raise ValueError("RECORD_SCOPE_OR_TYPE_INVALID")
    permitted = {"blm-glo": {"patent", "deed", "warranty_deed", "quitclaim_deed", "other_instrument"},
                 "blm-mlrs": {"land_tenure_case", "sale_notice"},
                 "kshs-land-sales": {"railroad_sale", "tract_book_entry", "deed"},
                 "sedgwick-deeds": {"deed", "warranty_deed", "quitclaim_deed"},
                 "johnson-deeds": {"deed", "warranty_deed", "quitclaim_deed"}}
    if source not in permitted or kind not in permitted[source]:
        raise ValueError("SOURCE_ROLE_TYPE_MISMATCH")
    if (kind == "sale_notice" and status != "PROPOSED") or (kind == "land_tenure_case" and status not in {"CASE_ACTION", "UNKNOWN"}):
        raise ValueError("CASE_OR_NOTICE_NOT_COMPLETED_SALE")
    event_date = iso_date(row["event_date"], required=True)
    recording_date = iso_date(row.get("recording_date"))
    if event_date > retrieved_at[:10] and status != "PROPOSED":
        raise ValueError("EVENT_DATE_IN_FUTURE")
    if recording_date and recording_date > retrieved_at[:10]:
        raise ValueError("RECORDING_DATE_IN_FUTURE")
    county = text(row.get("county"), 64)
    expected_county = {"sedgwick-deeds": "Sedgwick", "johnson-deeds": "Johnson"}.get(source)
    if expected_county and county != expected_county:
        raise ValueError("COUNTY_SOURCE_SCOPE_MISMATCH")
    amount = decimal(row.get("amount"))
    amount_kind, currency = text(row.get("amount_kind"), 32), text(row.get("currency"), 3)
    if amount is None and (amount_kind or currency) or amount is not None and (amount_kind not in PRICE_KINDS or currency != "USD"):
        raise ValueError("AMOUNT_ROLE_AND_CURRENCY_REQUIRED")
    if kind in {"land_tenure_case", "sale_notice"} and amount_kind in {"sale_price", "consideration", "recorded_principal"}:
        raise ValueError("CASE_OR_NOTICE_PRICE_NOT_SALE_PRICE")
    parties = [{"role": role, "label": label, "living_status": "UNKNOWN"} for role, field in (("grantor", "grantor"), ("grantee", "grantee")) if (label := text(row.get(field), 256))]
    value = {"profile": PROFILE, "id": "kfm:land:" + digest(canonical([source, key]))[7:], "source_id": source,
             "source_record_id": key, "instrument_type": kind, "event_date": event_date, "recording_date": recording_date,
             "state": state, "county": county, "transaction_status": status, "parties": parties,
             "legal_description": text(row.get("legal_description"), 8192), "acres": decimal(row.get("acres"), positive=True),
             "amount": {"value": amount, "kind": amount_kind, "currency": currency} if amount is not None else None,
             "notes": text(row.get("notes"), 4096), "geometry": None, "geometry_role": "UNLOCATED",
             "title_claim": "NOT_ESTABLISHED", "sale_completion": "NOT_ESTABLISHED", "rights_state": "PENDING",
             "sensitivity_state": "REVIEW_REQUIRED", "source_admission": "PENDING", "review_state": "PENDING", "release_state": "UNRELEASED",
             "flags": sorted(set(row.get("_flags", []) + ["RIGHTS_REVIEW_REQUIRED", "SENSITIVITY_REVIEW_REQUIRED"] + (["PARTY_IDENTITY_UNRESOLVED"] if parties else []) + (["PRICE_ABSENT"] if amount is None else [])))}
    value["record_digest"] = digest(canonical(value))
    value["evidence_ref"] = "kfm:evidence:land:" + value["record_digest"][7:]
    return value


def normalize(raw: bytes, manifest: dict, *, mapping=None, max_records=100) -> dict:
    if type(max_records) is not int or not 1 <= max_records <= MAX_RECORDS:
        raise ValueError("RECORD_LIMIT_INVALID")
    if not isinstance(raw, bytes) or not 0 < len(raw) <= MAX_BYTES or digest(raw) != manifest.get("payload_sha256") or len(raw) != manifest.get("bytes"):
        raise ValueError("CAPTURE_INTEGRITY_FAILED")
    source = manifest["source_id"]
    source_url(source, manifest["source_url"])
    retrieved = instant(manifest["retrieved_at"])
    fmt = manifest["format"]
    if fmt not in SOURCES[source]["formats"]:
        raise ValueError("SOURCE_FORMAT_NOT_ALLOWED")
    if fmt == "glo-text":
        if mapping is not None:
            raise ValueError("GLO_TEXT_MAP_NOT_ALLOWED")
        rows, coverage = _glo_rows(raw)
        # The visible range must agree with the recorded page scope; a keyword
        # result is not a state-boundary query or a claim of complete coverage.
        params = parse_qs(urlsplit(manifest["source_url"]).query)
        search_term = params.get("searchTerm", [None])[0]
        if search_term:
            params = parse_qs(urlsplit(search_term).query)
        if params.get("q") != ["Kansas"] or params.get("page") != [str((coverage["start"] - 1) // 25 + 1)] or params.get("pageSize") != ["25"]:
            raise ValueError("GLO_QUERY_SCOPE_MISMATCH")
    else:
        rows, coverage = _csv_rows(raw, mapping)
        if source == "kshs-land-sales":
            for row in rows:
                row["_flags"].append("TRANSCRIPTION_REVIEW_REQUIRED")
    if not 1 <= len(rows) <= max_records:
        raise ValueError("RECORD_LIMIT")
    records, locators, seen = [], {}, {}
    for row in rows:
        record = make_record(row, source, retrieved)
        if record["id"] in seen and seen[record["id"]] != record["record_digest"]:
            raise ValueError("DUPLICATE_IDENTITY_CONFLICT")
        seen[record["id"]] = record["record_digest"]
        locators.setdefault(record["record_digest"], []).append(row["_locator"])
        if record not in records:
            records.append(record)
    records.sort(key=lambda r: (r["event_date"], r["id"]))
    candidate = {"profile": "kfm.land-records-batch/v1", "capture_id": manifest["capture_id"], "source_id": source,
                 "records": records, "locators": locators, "coverage": coverage, "mapping": mapping,
                 "review_state": "PENDING", "release_state": "UNRELEASED"}
    candidate["candidate_id"] = digest(canonical(candidate))
    return candidate


def public_projection(_record):
    """There is deliberately no release writer in this intake implementation."""
    return {"outcome": "DENY", "reason_code": "LAND_RELEASE_NOT_IMPLEMENTED", "records": []}
