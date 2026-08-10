#!/usr/bin/env python3
"""Plan and normalize county-scoped USGS Water Data captures offline.

This module never performs transport.  It builds credential-free request plans
and normalizes caller-supplied, already captured OGC API FeatureCollections.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Mapping, Sequence
from urllib.parse import parse_qs, urlencode, urlparse

BASE = "https://api.waterdata.usgs.gov/ogcapi/v0/collections"
MAX_INPUT_BYTES = 8 * 1024 * 1024
MAX_PAGES = 100
MAX_FEATURES_PER_PAGE = 10_000
INPUT_KEYS = {
    "profile",
    "county_code",
    "start_date",
    "end_date",
    "parameter_code",
    "statistic_id",
    "captured_at",
    "source_descriptor_ref",
    "retrieval_receipt_ref",
    "monitoring_location_pages",
    "daily_value_captures",
}
LOCATION_REQUIRED = {
    "agency_code",
    "monitoring_location_number",
    "monitoring_location_name",
    "state_code",
    "county_code",
    "site_type_code",
}
DAILY_REQUIRED = {
    "time_series_id",
    "monitoring_location_id",
    "parameter_code",
    "statistic_id",
    "time",
    "value",
    "unit_of_measure",
    "approval_status",
    "qualifier",
    "last_modified",
}
LOCATION_ID = re.compile(r"^[A-Z0-9]+-[0-9A-Za-z._-]{4,32}$")
FIVE_DIGIT_CODE = re.compile(r"^[0-9]{5}$")
KANSAS_COUNTY = re.compile(r"^20[0-9]{3}$")


class CaptureError(ValueError):
    """Raised when captured source material cannot be normalized safely."""


def _canonical_digest(value: Any) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _exact_keys(value: Mapping[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        missing = sorted(expected - set(value))
        extra = sorted(set(value) - expected)
        raise CaptureError(f"{label} keys differ; missing={missing}, extra={extra}")


def _string(value: Any, label: str, minimum: int = 1, maximum: int = 512) -> str:
    if not isinstance(value, str) or not minimum <= len(value) <= maximum:
        raise CaptureError(f"{label} must be a string of length {minimum}..{maximum}")
    return value


def _bounded_int(value: Any, label: str, minimum: int, maximum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not minimum <= value <= maximum:
        raise CaptureError(f"{label} must be an integer between {minimum} and {maximum}")
    return value


def _date(value: Any, label: str) -> date:
    text = _string(value, label, 10, 10)
    try:
        parsed = date.fromisoformat(text)
    except ValueError as exc:
        raise CaptureError(f"{label} must be an ISO date") from exc
    if parsed.isoformat() != text:
        raise CaptureError(f"{label} must be a canonical ISO date")
    return parsed


def _timestamp(value: Any, label: str) -> str:
    text = _string(value, label, 20, 64)
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError as exc:
        raise CaptureError(f"{label} must be an RFC 3339 timestamp") from exc
    if parsed.tzinfo is None:
        raise CaptureError(f"{label} must include a timezone")
    return text


def _code(value: Any, label: str) -> str:
    text = _string(value, label, 5, 5)
    if not FIVE_DIGIT_CODE.fullmatch(text):
        raise CaptureError(f"{label} must contain five digits")
    return text


def _county(value: Any) -> str:
    text = _string(value, "county_code", 5, 5)
    if not KANSAS_COUNTY.fullmatch(text):
        raise CaptureError("county_code must be a five-digit Kansas county FIPS code")
    return text


def _location_id(value: Any, label: str = "monitoring_location_id") -> str:
    text = _string(value, label, 6, 64)
    if not LOCATION_ID.fullmatch(text):
        raise CaptureError(f"{label} has an invalid source identifier")
    return text


def _request_step(collection: str, query: list[tuple[str, str]]) -> dict[str, Any]:
    return {
        "method": "GET",
        "collection": collection,
        "url": f"{BASE}/{collection}/items?{urlencode(query)}",
        "expected_media_type": "application/geo+json",
        "pagination_strategy": "FOLLOW_REL_NEXT_UNTIL_ABSENT",
        "api_key_included": False,
    }


def build_monitoring_location_request(county_code: str, limit: int = 1000) -> dict[str, Any]:
    """Build the modern monitoring-locations request for one Kansas county."""

    county = _county(county_code)
    page_limit = _bounded_int(limit, "limit", 1, 10_000)
    return _request_step(
        "monitoring-locations",
        [("f", "json"), ("county_code", county), ("limit", str(page_limit))],
    )


def build_daily_request(
    monitoring_location_id: str,
    start_date: str,
    end_date: str,
    parameter_code: str,
    statistic_id: str,
    limit: int = 1000,
) -> dict[str, Any]:
    """Build one modern daily-values request for one monitoring location."""

    location = _location_id(monitoring_location_id)
    start = _date(start_date, "start_date")
    end = _date(end_date, "end_date")
    if start > end:
        raise CaptureError("start_date must not be after end_date")
    parameter = _code(parameter_code, "parameter_code")
    statistic = _code(statistic_id, "statistic_id")
    page_limit = _bounded_int(limit, "limit", 1, 10_000)
    return _request_step(
        "daily",
        [
            ("f", "json"),
            ("monitoring_location_id", location),
            ("parameter_code", parameter),
            ("statistic_id", statistic),
            ("datetime", f"{start.isoformat()}/{end.isoformat()}"),
            ("limit", str(page_limit)),
        ],
    )


def _feature_collection(page: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(page, dict) or page.get("type") != "FeatureCollection":
        raise CaptureError(f"{label} must be a GeoJSON FeatureCollection")
    features = page.get("features")
    links = page.get("links")
    if not isinstance(features, list) or len(features) > MAX_FEATURES_PER_PAGE:
        raise CaptureError(f"{label}.features must be a bounded array")
    if not isinstance(links, list) or len(links) > 100:
        raise CaptureError(f"{label}.links must be a bounded array")
    return page


def _safe_next_href(
    href: Any,
    collection: str,
    label: str,
    required_query: Mapping[str, str],
) -> None:
    text = _string(href, label, 16, 2048)
    parsed = urlparse(text)
    expected_path = f"/ogcapi/v0/collections/{collection}/items"
    if (
        parsed.scheme != "https"
        or parsed.hostname != "api.waterdata.usgs.gov"
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path != expected_path
        or parsed.fragment
    ):
        raise CaptureError(f"{label} is not a safe modern USGS Water Data URL")
    query = parse_qs(parsed.query, keep_blank_values=True)
    if "api_key" in query:
        raise CaptureError(f"{label} must not embed an API key")
    for key, expected in required_query.items():
        if query.get(key) != [expected]:
            raise CaptureError(f"{label} does not preserve the {key} query")


def _page_chain(
    value: Any,
    collection: str,
    label: str,
    required_query: Mapping[str, str],
) -> list[Mapping[str, Any]]:
    if not isinstance(value, list) or not 1 <= len(value) <= MAX_PAGES:
        raise CaptureError(f"{label} must contain 1..{MAX_PAGES} pages")
    pages: list[Mapping[str, Any]] = []
    for index, raw in enumerate(value):
        page = _feature_collection(raw, f"{label}[{index}]")
        next_links = []
        for link_index, link in enumerate(page["links"]):
            if not isinstance(link, dict):
                raise CaptureError(f"{label}[{index}].links[{link_index}] must be an object")
            if link.get("rel") == "next":
                _safe_next_href(
                    link.get("href"),
                    collection,
                    f"{label}[{index}].links[{link_index}].href",
                    required_query,
                )
                next_links.append(link)
        if len(next_links) > 1:
            raise CaptureError(f"{label}[{index}] contains multiple next links")
        if index < len(value) - 1 and not next_links:
            raise CaptureError(f"{label}[{index}] is missing its next link")
        if index == len(value) - 1 and next_links:
            raise CaptureError(f"{label} is incomplete because the final page has a next link")
        pages.append(page)
    return pages


def _location_features(pages: Sequence[Mapping[str, Any]], county: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    seen: set[str] = set()
    for page_index, page in enumerate(pages):
        for feature_index, feature in enumerate(page["features"]):
            label = f"monitoring_location_pages[{page_index}].features[{feature_index}]"
            if not isinstance(feature, dict) or feature.get("type") != "Feature":
                raise CaptureError(f"{label} must be a GeoJSON Feature")
            location = _location_id(feature.get("id"), f"{label}.id")
            if location in seen:
                raise CaptureError("monitoring location identifiers must be unique")
            seen.add(location)
            properties = feature.get("properties")
            if not isinstance(properties, dict) or not LOCATION_REQUIRED <= set(properties):
                raise CaptureError(f"{label}.properties lacks required source fields")
            agency = _string(properties["agency_code"], f"{label}.agency_code", 1, 16)
            number = _string(
                properties["monitoring_location_number"],
                f"{label}.monitoring_location_number",
                4,
                32,
            )
            if location != f"{agency}-{number}":
                raise CaptureError(f"{label}.id does not match agency and location number")
            location_county = _string(properties["county_code"], f"{label}.county_code", 5, 5)
            if location_county != county:
                raise CaptureError(f"{label}.county_code does not match the request county")
            state_code = _string(properties["state_code"], f"{label}.state_code", 2, 2)
            if state_code != "20":
                raise CaptureError(f"{label}.state_code is not Kansas")
            result.append(
                {
                    "monitoring_location_id": location,
                    "agency_code": agency,
                    "monitoring_location_number": number,
                    "monitoring_location_name": _string(
                        properties["monitoring_location_name"],
                        f"{label}.monitoring_location_name",
                        1,
                        256,
                    ),
                    "state_code": state_code,
                    "county_code": location_county,
                    "site_type_code": _string(
                        properties["site_type_code"], f"{label}.site_type_code", 1, 16
                    ),
                    "source_role": "ADMINISTRATIVE",
                }
            )
    return sorted(result, key=lambda item: item["monitoring_location_id"])


def _decimal_string(value: Any, label: str) -> str:
    text = _string(value, label, 1, 128)
    try:
        parsed = Decimal(text)
    except InvalidOperation as exc:
        raise CaptureError(f"{label} must be a decimal string") from exc
    if not parsed.is_finite():
        raise CaptureError(f"{label} must be finite")
    return text


def _daily_features(
    captures: Any,
    location_ids: set[str],
    start: date,
    end: date,
    parameter: str,
    statistic: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    if not isinstance(captures, list) or len(captures) > 10_000:
        raise CaptureError("daily_value_captures must be a bounded array")
    observations: list[dict[str, Any]] = []
    plan: list[dict[str, Any]] = []
    capture_digests: list[dict[str, Any]] = []
    seen_captures: set[str] = set()
    seen_features: set[str] = set()
    ordered_captures = sorted(
        captures,
        key=lambda item: str(item.get("monitoring_location_id", "")) if isinstance(item, dict) else "",
    )
    for capture_index, capture in enumerate(ordered_captures):
        label = f"daily_value_captures[{capture_index}]"
        if not isinstance(capture, dict) or set(capture) != {"monitoring_location_id", "pages"}:
            raise CaptureError(f"{label} must contain monitoring_location_id and pages")
        capture_location = _location_id(capture["monitoring_location_id"], f"{label}.monitoring_location_id")
        if capture_location not in location_ids:
            raise CaptureError(f"{label} references an unknown monitoring location")
        if capture_location in seen_captures:
            raise CaptureError("daily capture locations must be unique")
        seen_captures.add(capture_location)
        pages = _page_chain(
            capture["pages"],
            "daily",
            f"{label}.pages",
            {
                "monitoring_location_id": capture_location,
                "parameter_code": parameter,
                "statistic_id": statistic,
                "datetime": f"{start.isoformat()}/{end.isoformat()}",
            },
        )
        capture_digests.append(
            {
                "monitoring_location_id": capture_location,
                "page_digests": [_canonical_digest(page) for page in pages],
            }
        )
        plan.append(
            build_daily_request(
                capture_location,
                start.isoformat(),
                end.isoformat(),
                parameter,
                statistic,
            )
        )
        for page_index, page in enumerate(pages):
            for feature_index, feature in enumerate(page["features"]):
                item_label = f"{label}.pages[{page_index}].features[{feature_index}]"
                if not isinstance(feature, dict) or feature.get("type") != "Feature":
                    raise CaptureError(f"{item_label} must be a GeoJSON Feature")
                feature_id = _string(feature.get("id"), f"{item_label}.id", 1, 128)
                if feature_id in seen_features:
                    raise CaptureError("daily feature identifiers must be unique")
                seen_features.add(feature_id)
                properties = feature.get("properties")
                if not isinstance(properties, dict) or not DAILY_REQUIRED <= set(properties):
                    raise CaptureError(f"{item_label}.properties lacks required source fields")
                location = _location_id(
                    properties["monitoring_location_id"], f"{item_label}.monitoring_location_id"
                )
                if location != capture_location:
                    raise CaptureError(f"{item_label} is in the wrong location capture")
                actual_parameter = _code(properties["parameter_code"], f"{item_label}.parameter_code")
                actual_statistic = _code(properties["statistic_id"], f"{item_label}.statistic_id")
                if actual_parameter != parameter or actual_statistic != statistic:
                    raise CaptureError(f"{item_label} parameter/statistic does not match the request")
                observed_date = _date(properties["time"], f"{item_label}.time")
                if not start <= observed_date <= end:
                    raise CaptureError(f"{item_label}.time is outside the requested interval")
                approval = _string(properties["approval_status"], f"{item_label}.approval_status")
                if approval not in {"Approved", "Provisional"}:
                    raise CaptureError(f"{item_label}.approval_status is not supported")
                qualifier = properties["qualifier"]
                if qualifier is not None:
                    qualifier = _string(qualifier, f"{item_label}.qualifier", 1, 128)
                observations.append(
                    {
                        "feature_id": feature_id,
                        "time_series_id": _string(
                            properties["time_series_id"], f"{item_label}.time_series_id", 1, 128
                        ),
                        "monitoring_location_id": location,
                        "parameter_code": actual_parameter,
                        "statistic_id": actual_statistic,
                        "time": observed_date.isoformat(),
                        "value": _decimal_string(properties["value"], f"{item_label}.value"),
                        "unit_of_measure": _string(
                            properties["unit_of_measure"], f"{item_label}.unit_of_measure", 1, 64
                        ),
                        "approval_status": approval,
                        "qualifier": qualifier,
                        "last_modified": _timestamp(
                            properties["last_modified"], f"{item_label}.last_modified"
                        ),
                        "source_role": "AGGREGATE_DAILY",
                    }
                )
    if seen_captures != location_ids:
        missing = sorted(location_ids - seen_captures)
        raise CaptureError(f"daily captures are missing locations: {missing}")
    observations.sort(
        key=lambda item: (
            item["monitoring_location_id"],
            item["time"],
            item["time_series_id"],
            item["feature_id"],
        )
    )
    return observations, sorted(plan, key=lambda item: item["url"]), capture_digests


def normalize_capture(request: Mapping[str, Any]) -> dict[str, Any]:
    """Normalize complete, captured county and daily FeatureCollections."""

    if not isinstance(request, dict):
        raise CaptureError("request must be an object")
    _exact_keys(request, INPUT_KEYS, "request")
    if request["profile"] != "kfm.usgs-water.nwis-county-capture.v1":
        raise CaptureError("profile is not supported")
    county = _county(request["county_code"])
    start = _date(request["start_date"], "start_date")
    end = _date(request["end_date"], "end_date")
    if start > end:
        raise CaptureError("start_date must not be after end_date")
    parameter = _code(request["parameter_code"], "parameter_code")
    statistic = _code(request["statistic_id"], "statistic_id")
    captured_at = _timestamp(request["captured_at"], "captured_at")
    source_descriptor_ref = _string(request["source_descriptor_ref"], "source_descriptor_ref", 8, 512)
    retrieval_receipt_ref = _string(
        request["retrieval_receipt_ref"], "retrieval_receipt_ref", 8, 512
    )

    location_pages = _page_chain(
        request["monitoring_location_pages"],
        "monitoring-locations",
        "monitoring_location_pages",
        {"county_code": county},
    )
    locations = _location_features(location_pages, county)
    if not locations:
        raise CaptureError("monitoring location capture contains no locations")
    observations, daily_plan, daily_capture_digests = _daily_features(
        request["daily_value_captures"],
        {item["monitoring_location_id"] for item in locations},
        start,
        end,
        parameter,
        statistic,
    )
    approved = sum(item["approval_status"] == "Approved" for item in observations)
    provisional = sum(item["approval_status"] == "Provisional" for item in observations)
    dates = [item["time"] for item in observations]

    result: dict[str, Any] = {
        "object_type": "NwisCountyCaptureManifest",
        "schema_version": "1.0.0",
        "profile": "kfm.usgs-water.nwis-county-capture.v1",
        "county_code": county,
        "start_date": start.isoformat(),
        "end_date": end.isoformat(),
        "parameter_code": parameter,
        "statistic_id": statistic,
        "request_plan": {
            "monitoring_locations": build_monitoring_location_request(county),
            "daily_values": daily_plan,
        },
        "capture_binding": {
            "captured_at": captured_at,
            "source_descriptor_ref": source_descriptor_ref,
            "retrieval_receipt_ref": retrieval_receipt_ref,
            "monitoring_location_page_digests": [
                _canonical_digest(page) for page in location_pages
            ],
            "daily_value_capture_digests": daily_capture_digests,
        },
        "monitoring_locations": locations,
        "observations": observations,
        "summary": {
            "monitoring_location_count": len(locations),
            "observation_count": len(observations),
            "approved_count": approved,
            "provisional_count": provisional,
            "first_observation_date": min(dates) if dates else None,
            "last_observation_date": max(dates) if dates else None,
        },
        "governance": {
            "execution_mode": "CAPTURED_INPUT_ONLY",
            "network_attempted": False,
            "credentials_read": False,
            "source_activated": False,
            "raw_written": False,
            "evidence_resolved": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "publication_authorized": False,
            "public_use_authorized": False,
        },
    }
    result["result_digest"] = _canonical_digest(result)
    return result


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CaptureError(f"duplicate JSON member: {key}")
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise CaptureError(f"non-finite JSON number: {value}")


def load_capture(path: Path) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise CaptureError("input must be a regular non-symlink file")
    if path.stat().st_size > MAX_INPUT_BYTES:
        raise CaptureError("input exceeds the 8 MiB limit")
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CaptureError(f"input is not readable strict UTF-8 JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise CaptureError("input root must be an object")
    return value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        result = normalize_capture(load_capture(args.input))
    except CaptureError as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
