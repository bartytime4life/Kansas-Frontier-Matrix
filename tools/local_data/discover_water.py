#!/usr/bin/env python3
"""Bounded USGS water period-of-record metadata discovery; no observations.

The Kansas bounding rectangle is explicit and may include border locations.
Period envelopes do not establish continuous records or absence of gaps.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import ProxyHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.local_data.acquisition import NoRedirect  # noqa: E402
from tools.local_data.candidate_capture import create_candidate, write_candidate  # noqa: E402
from tools.local_data.manage import canonical, unique_object, utc_now  # noqa: E402

BASE = "https://api.waterdata.usgs.gov/ogcapi/v1/collections/time-series-metadata/items"
BBOX = "-102.052,36.993,-94.588,40.003"
PAGE_BYTES = 2 * 1024**2
TOTAL_BYTES = 8 * 1024**2


def validate_url(url):
    parts = urlsplit(url)
    try:
        query = parse_qs(parts.query, strict_parsing=True)
    except ValueError:
        raise ValueError("METADATA_URL_DENIED") from None
    if (parts.scheme != "https" or parts.netloc != "api.waterdata.usgs.gov"
            or parts.path != urlsplit(BASE).path or parts.fragment
            or set(query) - {"f", "bbox", "limit", "cursor"}
            or query.get("bbox") != [BBOX] or query.get("f") != ["json"]
            or query.get("limit") != ["1000"] or any(len(v) != 1 for v in query.values())):
        raise ValueError("METADATA_URL_DENIED")
    return url


def fetch(url):
    validate_url(url)
    with build_opener(ProxyHandler({}), NoRedirect()).open(
            Request(url, headers={"Accept-Encoding": "identity", "User-Agent": "KFM-water-discovery/1"}), timeout=30) as response:
        if response.status != 200 or response.headers.get("Content-Encoding", "identity") != "identity":
            raise ValueError("METADATA_RESPONSE_INVALID")
        raw = response.read(PAGE_BYTES + 1)
        if len(raw) > PAGE_BYTES:
            raise ValueError("METADATA_PAGE_LIMIT")
        return raw


def discover(*, max_pages=4, transport=fetch):
    if type(max_pages) is not int or not 1 <= max_pages <= 16:
        raise ValueError("PAGE_COUNT_LIMIT")
    url = BASE + "?" + urlencode({"f": "json", "bbox": BBOX, "limit": 1000})
    objects, requests, records, seen = {}, [], [], set()
    total = 0
    for _ in range(max_pages):
        validate_url(url)
        if url in seen:
            raise ValueError("PAGINATION_CYCLE")
        seen.add(url)
        raw = transport(url)
        total += len(raw)
        if len(raw) > PAGE_BYTES or total > TOTAL_BYTES:
            raise ValueError("METADATA_BYTE_LIMIT")
        digest = hashlib.sha256(raw).hexdigest()
        objects[digest + ".metadata"] = raw
        requests.append({"source_url": url, "sha256": digest, "size_bytes": len(raw)})
        def reject(_):
            raise ValueError("METADATA_NONFINITE")
        value = json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject)
        features = value.get("features")
        if value.get("type") != "FeatureCollection" or not isinstance(features, list) or len(features) > 1000:
            raise ValueError("METADATA_SHAPE_INVALID")
        for feature in features:
            p = feature["properties"]
            records.append({"time_series_id": feature["id"], "monitoring_location_id": p["monitoring_location_id"],
                            "parameter_code": p.get("parameter_code"), "parameter_name": p.get("parameter_name"),
                            "statistic_id": p.get("statistic_id"), "unit_of_measure": p.get("unit_of_measure"),
                            "computation_period": p.get("computation_period_identifier"),
                            "begin": p.get("begin"), "end": p.get("end"),
                            "data_gap_interval": p.get("data_gap_interval"),
                            "gaps_verified": False, "geometry": feature.get("geometry"),
                            "source_metadata_sha256": digest})
        links = [link["href"] for link in value.get("links", []) if link.get("rel") == "next"]
        if len(links) > 1:
            raise ValueError("PAGINATION_AMBIGUOUS")
        url = links[0] if links else None
        if url is None:
            break
    return {"schema_version": "kfm-water-history-discovery-v1", "captured_at": utc_now(),
            "lifecycle": "candidate-only", "selection_bbox": BBOX,
            "geography_note": "Kansas bounding rectangle; state membership not verified",
            "metadata_bytes_captured": total, "pages_captured": len(requests),
            "complete_for_query": url is None, "next_page_available": url is not None,
            "series_count": len(records), "station_count": len({r["monitoring_location_id"] for r in records}),
            "requests": requests, "records": records,
            "source_admitted": False, "released": False, "published": False}, objects


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--max-pages", type=int, default=4)
    args = parser.parse_args(argv)
    try:
        result, objects = discover(max_pages=args.max_pages)
        create_candidate(args.output_directory)
        for name, raw in objects.items():
            write_candidate(args.output_directory, name, raw)
        write_candidate(args.output_directory, "discovery.json", canonical(result))
        print(canonical({key: result[key] for key in ("series_count", "station_count", "pages_captured",
                                                      "metadata_bytes_captured", "complete_for_query")}).decode().strip())
        return 0
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"ERROR","reason":"WATER_METADATA_DISCOVERY_FAILED"}')
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
