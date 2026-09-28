"""Offline ACS data-API request planning and supplied-response parsing; never fetches.

The Census data API returns estimates and margins of error as strings and
encodes suppression and other annotations as negative sentinel ("jam")
values. This module parses those values exactly: numbers become ``Decimal``,
jam values become named annotations with no numeric value, and nothing is
ever converted to zero. API keys are never part of a planned or accepted
provenance URL. Activation, disclosure review, cross-vintage joins, and
publication belong to owning layers.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from hashlib import sha256
import json
import re
from urllib.parse import parse_qs, urlencode, urlsplit

HOST = "https://api.census.gov"
DATASETS = frozenset({"acs/acs1", "acs/acs5", "acs/acs1/profile", "acs/acs5/profile",
                      "acs/acs1/subject", "acs/acs5/subject"})
KANSAS_FIPS = "20"
MAX_VARIABLES = 50
# Detailed (B01001_001E), profile (DP05_0001PE), and subject (S0101_C01_001E) variables.
VARIABLE = re.compile(r"(?:[A-Z][A-Z0-9]{1,10}(?:_C\d{2})?_\d{3,4}(?:E|M|EA|MA|PE|PM|PEA|PMA)"
                      r"|NAME|GEO_ID)\Z")
# Geography level -> (for-clause token, ordered geography columns, code widths).
GEOGRAPHIES = {
    "state": ("state", ("state",), (2,)),
    "county": ("county", ("state", "county"), (2, 3)),
    "county subdivision": ("county subdivision", ("state", "county", "county subdivision"),
                           (2, 3, 5)),
    "place": ("place", ("state", "place"), (2, 5)),
    "tract": ("tract", ("state", "county", "tract"), (2, 3, 6)),
    "block group": ("block group", ("state", "county", "tract", "block group"), (2, 3, 6, 1)),
}
# Published ACS annotation values; each means "no numeric value", never zero.
ANNOTATIONS = {
    "-999999999": "N_INSUFFICIENT_SAMPLE",
    "-888888888": "X_NOT_APPLICABLE",
    "-666666666": "ESTIMATE_NOT_COMPUTABLE",
    "-555555555": "MOE_CONTROLLED_NO_SAMPLING_ERROR",
    "-333333333": "MEDIAN_OPEN_ENDED_UPPER",
    "-222222222": "MOE_NOT_COMPUTABLE",
}
NUMBER = re.compile(r"-?\d+(?:\.\d+)?\Z")

# Explicit bound: the decoder's own recursion limit differs by interpreter (about
# 1,000 levels on 3.11, tens of thousands on 3.12+), so it cannot decide routing.
MAX_NESTING = 32


class AcsInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected candidate input."""


def _utc(value: object) -> str:
    try:
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    except (ValueError, TypeError, OverflowError):
        raise AcsInputError("UTC_TIME") from None


def _kind(variable: str) -> str:
    if variable in ("NAME", "GEO_ID"):
        return "text"
    suffix = variable.rsplit("_", 1)[1].lstrip("0123456789")
    if suffix.endswith("A"):
        return "annotation"
    return "moe" if suffix in ("M", "PM") else "estimate"


def acs_url(year: int, dataset: str, variables: tuple[str, ...] | list[str], geography: str,
            *, pair_moe: bool = True) -> str:
    """Plan one Kansas-scoped request URL; never includes an API key."""
    if type(year) is not int or not 2005 <= year <= 2100:
        raise AcsInputError("YEAR")
    if dataset not in DATASETS:
        raise AcsInputError("DATASET")
    if geography not in GEOGRAPHIES:
        raise AcsInputError("GEOGRAPHY")
    requested = list(dict.fromkeys(variables))
    if not requested or any(not isinstance(v, str) or not VARIABLE.fullmatch(v)
                            for v in requested):
        raise AcsInputError("VARIABLE")
    if pair_moe:
        for variable in list(requested):
            if _kind(variable) == "estimate":
                moe = variable[:-1] + "M" if variable.endswith("E") else variable
                if moe not in requested:
                    requested.append(moe)
    if len(requested) > MAX_VARIABLES:
        raise AcsInputError("VARIABLE_BOUND")
    token, columns, _ = GEOGRAPHIES[geography]
    params = {"get": ",".join(requested), "for": f"{token}:*" if geography != "state"
              else f"state:{KANSAS_FIPS}"}
    if geography == "block group":
        params["in"] = f"state:{KANSAS_FIPS} county:*"
    elif geography != "state":
        params["in"] = f"state:{KANSAS_FIPS}"
    return f"{HOST}/data/{year}/{dataset}?" + urlencode(params)


@dataclass(frozen=True)
class AcsRequest:
    year: int
    dataset: str
    variables: tuple[str, ...]
    geography: str


def _request(url: object) -> AcsRequest:
    if not isinstance(url, str) or len(url) > 8192 or any(ord(c) <= 32 for c in url):
        raise AcsInputError("SOURCE_URL")
    try:
        parsed = urlsplit(url)
        if parsed.scheme != "https" or parsed.netloc != "api.census.gov" or parsed.fragment:
            raise ValueError
        match = re.fullmatch(r"/data/(\d{4})/(acs/[a-z0-9/]+)", parsed.path)
        if match is None or match.group(2) not in DATASETS:
            raise ValueError
        raw = parse_qs(parsed.query, strict_parsing=True, keep_blank_values=True)
        if "key" in raw:
            # Credentials never belong in provenance URLs, receipts, or logs.
            raise AcsInputError("API_KEY_IN_URL")
        if set(raw) - {"get", "for", "in"} or any(len(v) != 1 for v in raw.values()):
            raise ValueError
        variables = tuple(raw["get"][0].split(","))
        if (not variables or len(variables) > MAX_VARIABLES or len(set(variables)) != len(variables)
                or any(not VARIABLE.fullmatch(v) for v in variables)):
            raise ValueError
        target = raw["for"][0]
        if target == f"state:{KANSAS_FIPS}":
            geography = "state"
        else:
            geography = next(level for level, (token, _, _) in GEOGRAPHIES.items()
                             if level != "state" and target == f"{token}:*")
        expected_in = {"state": None, "block group": f"state:{KANSAS_FIPS} county:*"}.get(
            geography, f"state:{KANSAS_FIPS}")
        if raw.get("in", [None])[0] != expected_in:
            raise ValueError
        return AcsRequest(int(match.group(1)), match.group(2), variables, geography)
    except AcsInputError:
        raise
    except (KeyError, ValueError, TypeError, StopIteration):
        raise AcsInputError("SOURCE_URL") from None


@dataclass(frozen=True)
class AcsValue:
    variable: str
    kind: str
    # Source string exactly as returned (None when the API returned null).
    raw: str | None
    value: Decimal | None
    annotation: str | None


@dataclass(frozen=True)
class AcsRowCandidate:
    geoid: str
    name: str | None
    values: tuple[AcsValue, ...]
    reasons: tuple[str, ...]
    route: str


@dataclass(frozen=True)
class AcsTableCandidate:
    source_url: str
    request: AcsRequest
    retrieved_at: str
    body_sha256: str
    empty_result: bool
    rows: tuple[AcsRowCandidate, ...]
    table_reasons: tuple[str, ...]
    # A returned table is not a complete geography inventory, and a GEOID is
    # scoped to this vintage: never join across vintages by code alone.
    coverage: str = "NOT_ESTABLISHED"
    admission: str = "NOT_ADMITTED"


def _value(variable: str, raw: object) -> tuple[AcsValue, str | None]:
    kind = _kind(variable)
    if raw is None:
        return AcsValue(variable, kind, None, None, "NULL_FROM_SOURCE"), None
    if not isinstance(raw, str) or len(raw) > 512:
        raise AcsInputError("VALUE_SHAPE")
    if kind in ("text", "annotation"):
        return AcsValue(variable, kind, raw, None, None), None
    if raw in ANNOTATIONS:
        return AcsValue(variable, kind, raw, None, ANNOTATIONS[raw]), None
    if not NUMBER.fullmatch(raw):
        raise AcsInputError("VALUE_NOT_NUMERIC")
    try:
        number = Decimal(raw)
    except InvalidOperation:
        raise AcsInputError("VALUE_NOT_NUMERIC") from None
    reason = "UNRECOGNIZED_NEGATIVE" if number < 0 else None
    return AcsValue(variable, kind, raw, None if reason else number, reason), reason


def _object_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    # The data API returns arrays of strings only; any object is malformed.
    raise AcsInputError("UNEXPECTED_OBJECT")


def _constant(_: str) -> None:
    raise AcsInputError("NONSTANDARD_JSON_NUMBER")


def _exceeds_nesting(value: object, limit: int) -> bool:
    """Whether containers nest deeper than ``limit``; iterative, early-exit, and holding
    at most one iterator per level, so wide payloads cost no extra memory."""
    if not isinstance(value, (dict, list)):
        return False
    stack = [iter(value.values() if isinstance(value, dict) else value)]
    if len(stack) > limit:
        return True
    while stack:
        for child in stack[-1]:
            if isinstance(child, (dict, list)):
                if len(stack) + 1 > limit:
                    return True
                stack.append(iter(child.values() if isinstance(child, dict) else child))
                break
        else:
            stack.pop()
    return False


def parse_response(body: bytes, *, status: int, source_url: str, retrieved_at: str,
                   max_bytes: int = 32 * 1024 * 1024, max_rows: int = 50_000
                   ) -> AcsTableCandidate:
    """Parse one supplied API response; reject a malformed table whole."""
    request = _request(source_url)
    retrieved = _utc(retrieved_at)
    if type(status) is not int or not isinstance(body, bytes) or len(body) > max_bytes:
        raise AcsInputError("RESPONSE_BOUND")
    digest = "sha256:" + sha256(body).hexdigest()
    if status == 204 and not body:
        # No rows for this request. This is not a statement that a value is zero.
        return AcsTableCandidate(source_url, request, retrieved, digest, True, (),
                                 ("EMPTY_RESULT_NOT_ABSENCE",))
    if status == 429:
        raise AcsInputError("RATE_LIMITED")
    if status != 200:
        raise AcsInputError("HTTP_STATUS")
    try:
        payload = json.loads(body.decode("utf-8"), object_pairs_hook=_object_pairs,
                             parse_constant=_constant)
    except AcsInputError:
        raise
    except RecursionError:
        # The decoder's own depth limit is interpreter-dependent; either way it is depth.
        raise AcsInputError("NESTING_DEPTH") from None
    except (UnicodeError, ValueError):
        raise AcsInputError("INVALID_JSON") from None
    if _exceeds_nesting(payload, MAX_NESTING):
        raise AcsInputError("NESTING_DEPTH")
    if (not isinstance(payload, list) or not payload
            or not all(isinstance(row, list) for row in payload)):
        raise AcsInputError("TABLE_SHAPE")
    header, rows = payload[0], payload[1:]
    _, geo_columns, widths = GEOGRAPHIES[request.geography]
    if header != [*request.variables, *geo_columns]:
        raise AcsInputError("HEADER_MISMATCH")
    if len(rows) > max_rows:
        raise AcsInputError("ROW_BOUND")
    table_reasons: list[str] = []
    estimates = [v for v in request.variables if _kind(v) == "estimate"]
    if any((v[:-1] + "M") not in request.variables for v in estimates if v.endswith("E")):
        table_reasons.append("ESTIMATE_WITHOUT_MOE")
    parsed_rows: list[AcsRowCandidate] = []
    seen: set[str] = set()
    for row in rows:
        if len(row) != len(header):
            raise AcsInputError("ROW_WIDTH")
        codes = row[len(request.variables):]
        if any(not isinstance(code, str) or not code.isdigit() or len(code) != width
               for code, width in zip(codes, widths)):
            raise AcsInputError("GEOGRAPHY_CODE")
        if codes[0] != KANSAS_FIPS:
            raise AcsInputError("STATE_SCOPE_MISMATCH")
        geoid = "".join(codes)
        if geoid in seen:
            raise AcsInputError("DUPLICATE_GEOID")
        seen.add(geoid)
        values, reasons = [], []
        name = None
        for variable, raw in zip(request.variables, row):
            value, reason = _value(variable, raw)
            values.append(value)
            if reason:
                reasons.append(reason)
            if variable == "NAME":
                name = value.raw
        parsed_rows.append(AcsRowCandidate(
            geoid, name, tuple(values), tuple(dict.fromkeys(reasons)),
            "QUARANTINE_CANDIDATE" if reasons else "RAW_CANDIDATE"))
    return AcsTableCandidate(source_url, request, retrieved, digest, not parsed_rows,
                             tuple(parsed_rows), tuple(table_reasons))
