#!/usr/bin/env python3
"""Compare captured USGS 07146500 discharge pages offline; never fetch or write."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
from urllib.parse import parse_qsl, urlsplit

STATION = "USGS-07146500"
MAX_BYTES = 8 * 1024 * 1024
MAX_ROWS = 10_000
DETAIL_LIMIT = 100
FIELDS = ("value", "unit_of_measure", "approval_status", "qualifier", "method_category")
AUTHORITY = dict(source_admission=False, activation=False, promotion=False, release=False, publication=False)
STAMP = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|[+-]\d{2}:\d{2})")


class Problem(ValueError):
    def __init__(self, code, outcome="ERROR"):
        self.code, self.outcome = code, outcome
        super().__init__(code)


def require(condition, code, outcome="ERROR"):
    if not condition:
        raise Problem(code, outcome)


def unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "JSON_DUPLICATE_KEY")
        result[key] = value
    return result


def reject_constant(_value):
    raise Problem("JSON_NONFINITE")


def decode(raw):
    require(len(raw) <= MAX_BYTES, "INPUT_TOO_LARGE")
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=unique,
                          parse_constant=reject_constant, parse_float=Decimal)
    except (UnicodeError, json.JSONDecodeError, RecursionError, ValueError) as error:
        if isinstance(error, Problem):
            raise
        raise Problem("JSON_INVALID") from None


def read_regular(path):
    """Bound reads and refuse static symlink ancestors and non-regular inputs."""
    path = Path(path).absolute()
    require(not any(p.is_symlink() for p in (path, *path.parents)), "INPUT_SYMLINK")
    try:
        flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
        with os.fdopen(os.open(path, flags), "rb") as stream:
            info = os.fstat(stream.fileno())
            require(stat.S_ISREG(info.st_mode), "INPUT_NOT_REGULAR")
            require(info.st_size <= MAX_BYTES, "INPUT_TOO_LARGE")
            raw = stream.read(MAX_BYTES + 1)
        require(len(raw) <= MAX_BYTES, "INPUT_TOO_LARGE")
        return raw
    except OSError:
        raise Problem("INPUT_UNREADABLE") from None


def instant(value):
    require(isinstance(value, str) and STAMP.fullmatch(value) is not None, "TIME_INVALID")
    require(not value.endswith("-00:00"), "TIME_OFFSET_UNKNOWN", "ABSTAIN")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        raise Problem("TIME_INVALID") from None


def day(value):
    require(isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value), "DATE_INVALID")
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise Problem("DATE_INVALID") from None


def text(value, code, limit=128):
    require(isinstance(value, str) and 0 < len(value) <= limit
            and not any(ord(c) < 32 or ord(c) == 127 for c in value), code)
    return value


def numeric(value):
    if value is None:
        return None
    require(not isinstance(value, bool) and isinstance(value, (str, int, Decimal)), "VALUE_INVALID")
    source = str(value)
    require(len(source) <= 160 and re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", source), "VALUE_INVALID")
    try:
        number = Decimal(source)
        require(number.is_finite() and abs(number.as_tuple().exponent) <= 100, "VALUE_INVALID")
        rendered = format(number, "f")
    except (InvalidOperation, ValueError):
        raise Problem("VALUE_INVALID") from None
    if "." in rendered:
        rendered = rendered.rstrip("0").rstrip(".")
    return "0" if number == 0 else rendered


def query(url, collection):
    text(url, "QUERY_INVALID", 2048)
    try:
        parts = urlsplit(url)
    except ValueError:
        raise Problem("QUERY_INVALID") from None
    require(parts.scheme == "https" and parts.netloc == "api.waterdata.usgs.gov"
            and not parts.fragment
            and parts.path == f"/ogcapi/v1/collections/{collection}/items", "QUERY_NOT_ALLOWED")
    try:
        pairs = parse_qsl(parts.query, keep_blank_values=True, strict_parsing=True, max_num_fields=12)
    except ValueError:
        raise Problem("QUERY_INVALID") from None
    values = unique(pairs)
    allowed = {"f", "limit", "datetime", "monitoring_location_id", "parameter_code", "statistic_id", "time_series_id"}
    require(set(values) <= allowed and values.get("f") == "json"
            and values.get("monitoring_location_id") == STATION
            and values.get("parameter_code") == "00060", "QUERY_SCOPE_INVALID")
    require(re.fullmatch(r"[1-9]\d{0,4}", values.get("limit", "")) is not None
            and int(values["limit"]) <= MAX_ROWS, "QUERY_LIMIT_INVALID")
    interval = values.get("datetime", "").split("/")
    require(len(interval) == 2, "QUERY_INTERVAL_INVALID")
    clock = day if collection == "daily" else instant
    start, end = map(clock, interval)
    require(start <= end and (end - start).days <= (3660 if collection == "daily" else 366), "QUERY_INTERVAL_INVALID")
    if "statistic_id" in values:
        require(values["statistic_id"] == ("00003" if collection == "daily" else "00011"), "STATISTIC_UNSUPPORTED", "ABSTAIN")
    if "time_series_id" in values:
        require(re.fullmatch(r"[A-Za-z0-9_-]{1,128}", values["time_series_id"]), "SERIES_INVALID")
    # Query spelling/order may differ; every admitted filter must still agree.
    scope = {**values, "datetime": f"{start.isoformat()}/{end.isoformat()}"}
    return scope, start, end


def payload(raw, collection):
    """Accept a raw page or the retained watch export's receipt-bound first page."""
    document = decode(raw)
    binding = "payload_only"
    receipt = None
    if isinstance(document, dict) and "evidence_files" in document:
        require(document.get("station") == STATION and document.get("parameter") == "00060", "WATCH_IDENTITY_INVALID")
        files = document["evidence_files"]
        require(isinstance(files, dict), "WATCH_FILES_INVALID")
        body = files.get(f"{collection}-0.raw")
        sidecar = files.get(f"{collection}-receipt.json")
        require(isinstance(body, str) and isinstance(sidecar, str), "WATCH_PAGE_MISSING")
        receipt = decode(sidecar.encode("utf-8"))
        require(isinstance(receipt, dict) and receipt.get("error") is None, "CAPTURE_INCOMPLETE", "ABSTAIN")
        pages = receipt.get("pages")
        require(isinstance(pages, list) and len(pages) == 1 and isinstance(pages[0], dict), "CAPTURE_MULTIPAGE_UNSUPPORTED", "ABSTAIN")
        page = pages[0]
        raw = body.encode("utf-8")
        require(type(page.get("status")) is int and page["status"] == 200, "CAPTURE_HTTP_STATUS", "ABSTAIN")
        require(type(page.get("bytes")) is int and len(raw) == page["bytes"]
                and hashlib.sha256(raw).hexdigest() == page.get("sha256"), "CAPTURE_DIGEST_MISMATCH")
        document = decode(raw)
        binding = "retained_receipt_bound"
    require(isinstance(document, dict) and document.get("type") == "FeatureCollection", "COLLECTION_INVALID")
    links = document.get("links")
    require(isinstance(links, list) and len(links) <= 100 and all(isinstance(x, dict) for x in links), "LINKS_INVALID")
    require(not any(x.get("rel") == "next" for x in links), "PAGINATION_INCOMPLETE", "ABSTAIN")
    selves = [x.get("href") for x in links if x.get("rel") == "self"]
    require(len(selves) == 1, "SELF_QUERY_AMBIGUOUS")
    scope, start, end = query(selves[0], collection)
    if receipt is not None:
        require(query(receipt.get("query"), collection)[0] == scope
                and query(receipt["pages"][0].get("url"), collection)[0] == scope, "CAPTURE_QUERY_MISMATCH")
    features = document.get("features")
    require(isinstance(features, list) and len(features) <= MAX_ROWS, "FEATURES_INVALID")
    matched = document.get("numberMatched")
    if matched is not None:
        require(type(matched) is int and matched >= len(features), "MATCHED_COUNT_INVALID")
        require(matched == len(features), "MATCHED_COUNT_INCOMPLETE", "ABSTAIN")
    if "numberReturned" in document:
        require(type(document["numberReturned"]) is int and document["numberReturned"] == len(features), "RETURNED_COUNT_INVALID")
    if receipt is not None:
        require(type(receipt.get("feature_count")) is int and receipt["feature_count"] == len(features)
                and type(receipt["pages"][0].get("numberReturned")) is int
                and receipt["pages"][0]["numberReturned"] == len(features), "CAPTURE_COUNT_MISMATCH")
    require(len(features) < int(scope["limit"]), "PAGE_CAP_REACHED", "ABSTAIN")
    require(bool(features), "NO_OBSERVATIONS", "ABSTAIN")
    records, metadata, property_keys = {}, {}, set()
    required = {"time_series_id", "monitoring_location_id", "parameter_code", "statistic_id", "time", "value", "unit_of_measure", "approval_status", "qualifier"}
    for feature in features:
        require(isinstance(feature, dict) and feature.get("type") == "Feature", "FEATURE_INVALID")
        p = feature.get("properties")
        require(isinstance(p, dict) and required <= p.keys() and len(p) <= 64, "PROPERTY_MISSING")
        property_keys.update(p)
        require(len(property_keys) <= 64 and all(isinstance(k, str) and 0 < len(k) <= 128 for k in p),
                "PROPERTY_KEYS_BUDGET")
        require(p["monitoring_location_id"] == STATION and p["parameter_code"] == "00060", "OBSERVATION_SCOPE_INVALID")
        series = text(p["time_series_id"], "SERIES_INVALID")
        statistic = "00003" if collection == "daily" else "00011"
        require(p["statistic_id"] == statistic, "STATISTIC_UNSUPPORTED", "ABSTAIN")
        require("time_series_id" not in scope or scope["time_series_id"] == series, "OBSERVATION_SCOPE_INVALID")
        when = day(p["time"]) if collection == "daily" else instant(p["time"])
        require(start <= when <= end, "OBSERVATION_OUTSIDE_INTERVAL")
        identity = (series, statistic, when.isoformat())
        require(identity not in records, "DUPLICATE_IDENTITY")
        approval = p["approval_status"]
        require(approval in (None, "Approved", "Provisional"), "APPROVAL_UNSUPPORTED", "ABSTAIN")
        qualifier = p["qualifier"]
        if qualifier is not None:
            qualifier = [qualifier] if isinstance(qualifier, str) else qualifier
            require(isinstance(qualifier, list) and len(qualifier) <= 16, "QUALIFIER_INVALID")
            qualifier = [text(q, "QUALIFIER_INVALID", 80) for q in qualifier]
            require(len(set(qualifier)) == len(qualifier), "QUALIFIER_DUPLICATE")
            qualifier = sorted(qualifier)
        method = p.get("method_category")
        if method is not None:
            text(method, "METHOD_INVALID")
        records[identity] = dict(value=numeric(p["value"]), unit_of_measure=text(p["unit_of_measure"], "UNIT_INVALID", 80),
                                 approval_status=approval, qualifier=qualifier, method_category=method)
        revision = p.get("last_modified")
        if revision is not None:
            text(revision, "REVISION_METADATA_INVALID")
        metadata[identity] = revision
    require(len({key[:2] for key in records}) <= 4, "SERIES_BUDGET_EXCEEDED", "ABSTAIN")
    response_at = document.get("timeStamp")
    if response_at is not None:
        response_at = instant(response_at).isoformat()
    return dict(query=scope, source_url=selves[0], start=start, end=end, records=records,
                metadata=metadata, property_keys=sorted(property_keys), binding=binding,
                response_at=response_at, sha256=hashlib.sha256(raw).hexdigest())


def coverage(capture, collection):
    series = {}
    for key in capture["records"]:
        series.setdefault(key[:2], []).append(key[2])
    holes = []
    for (identifier, statistic), times in sorted(series.items()):
        if collection == "daily":
            seen = {day(t) for t in times}
            cursor = capture["start"]
            while cursor <= capture["end"]:
                if cursor not in seen:
                    holes.append((identifier, statistic, cursor.isoformat()))
                cursor += timedelta(days=1)
        else:
            clocks = sorted(instant(t) for t in times)
            points = [capture["start"], *clocks, capture["end"]]
            for left, right in zip(points, points[1:]):
                if (right-left).total_seconds() >= 21600:
                    holes.append((identifier, statistic, left.isoformat(), right.isoformat()))
    return dict(kind="missing_dates_in_query" if collection == "daily" else "at_least_six_hour_coverage_holes",
                count=len(holes), details=holes[:DETAIL_LIMIT], details_truncated=len(holes) > DETAIL_LIMIT,
                sha256=hashlib.sha256(json.dumps(holes, separators=(",", ":")).encode()).hexdigest())


def compare_bytes(prior_raw, current_raw, collection):
    try:
        require(isinstance(collection, str) and collection in {"continuous", "daily"}, "COLLECTION_UNSUPPORTED")
        prior, current = payload(prior_raw, collection), payload(current_raw, collection)
        require(prior["query"] == current["query"], "QUERY_SCOPE_MISMATCH", "ABSTAIN")
        if prior["response_at"] is not None and current["response_at"] is not None:
            require(instant(current["response_at"]) >= instant(prior["response_at"]),
                    "PROVIDER_RESPONSE_ORDER_REVERSED", "ABSTAIN")
        a, b = prior["records"], current["records"]
        changes, counts = [], Counter()
        for key in sorted(a.keys() | b.keys()):
            if key not in a or key not in b:
                fields = ["record_added" if key in b else "record_removed"]
            else:
                fields = [f for f in FIELDS if a[key][f] != b[key][f]]
            if fields:
                counts.update(fields)
                if len(changes) < DETAIL_LIMIT:
                    changes.append(dict(time_series_id=key[0], statistic_id=key[1], time=key[2],
                                        fields=fields, prior=a.get(key), current=b.get(key)))
        gaps = [coverage(c, collection) for c in (prior, current)]
        shape_changed = prior["property_keys"] != current["property_keys"]
        metadata_changed = sum(prior["metadata"][k] != current["metadata"][k] for k in a.keys() & b.keys())
        review = bool(counts) or shape_changed or gaps[0]["sha256"] != gaps[1]["sha256"]
        summaries = []
        for capture, gap in zip((prior, current), gaps):
            records = list(capture["records"].values())
            summaries.append(dict(sha256=capture["sha256"], capture_binding=capture["binding"], records=len(records),
                                  provider_response_at=capture["response_at"],
                                  null_values=sum(r["value"] is None for r in records),
                                  approval_status_counts=dict(sorted(Counter(r["approval_status"] or "UNKNOWN" for r in records).items())),
                                  property_keys=capture["property_keys"], captured_coverage=gap))
        return dict(profile="kfm.usgs-07146500-captured-comparison/v1", outcome="ANSWER",
                    decision="REVIEW" if review else "NO_DIFFERENCE_IN_CAPTURED_FIELDS",
                    station=STATION, parameter_code="00060", collection=collection, query=prior["query"],
                    prior=summaries[0], current=summaries[1], changed_field_counts=dict(sorted(counts.items())),
                    changes=changes, details_truncated=sum(1 for k in a.keys() | b.keys() if a.get(k) != b.get(k)) > DETAIL_LIMIT,
                    property_keys_changed=shape_changed, provider_metadata_changed_records=metadata_changed,
                    authority=dict(AUTHORITY),
                    limitation="Captured-field comparison only; no HTTP authentication, current-condition, outage, materiality or KFM release conclusion.")
    except Problem as error:
        return dict(profile="kfm.usgs-07146500-captured-comparison/v1", outcome=error.outcome,
                    reason_code=error.code, authority=dict(AUTHORITY))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prior", type=Path)
    parser.add_argument("current", type=Path, nargs="?")
    parser.add_argument("--collection", choices=("continuous", "daily"), required=True)
    parser.add_argument("--print-query", action="store_true", help="Print the validated public query only; perform no network request.")
    args = parser.parse_intermixed_args(argv)
    try:
        prior = read_regular(args.prior)
        if args.print_query:
            require(args.current is None, "QUERY_MODE_TAKES_ONE_INPUT")
            print(payload(prior, args.collection)["source_url"])
            return 0
        require(args.current is not None, "CURRENT_INPUT_REQUIRED")
        result = compare_bytes(prior, read_regular(args.current), args.collection)
    except Problem as error:
        result = dict(outcome=error.outcome, reason_code=error.code, authority=dict(AUTHORITY))
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False))
    return 0 if result["outcome"] == "ANSWER" else 1 if result["outcome"] == "ABSTAIN" else 2


if __name__ == "__main__":
    sys.exit(main())
