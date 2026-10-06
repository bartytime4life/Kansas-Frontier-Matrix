#!/usr/bin/env python3
"""Capture public Kansas-named 3DEP EPT metadata, never lidar payloads.

KS_ is a provider naming filter, not proof of complete Kansas spatial coverage.
An exact metadata snapshot and separate owner-importable selection inventory
are written to one new private external RAW candidate directory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlencode
from urllib.request import ProxyHandler, Request, build_opener
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.local_data.acquisition import CACHE_LIMIT, NoRedirect, SCHEMA  # noqa: E402
from tools.local_data.candidate_capture import create_candidate, write_candidate  # noqa: E402
from tools.local_data.manage import canonical, utc_now, unique_object  # noqa: E402

BUCKET = "https://usgs-lidar-public.s3.amazonaws.com/"
PAGE_LIMIT = 2 * 1024**2
TOTAL_LIMIT = 8 * 1024**2
PREFIX = re.compile(r"KS_[A-Za-z0-9_-]+/\Z")
NS = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}


def fetch(url: str) -> bytes:
    # Only the caller's fixed public bucket and generated listing/EPT paths.
    if not url.startswith(BUCKET):
        raise ValueError("DISCOVERY_URL_DENIED")
    with build_opener(ProxyHandler({}), NoRedirect()).open(
            Request(url, headers={"Accept-Encoding": "identity", "User-Agent": "KFM-3DEP-discovery/1"}),
            timeout=30) as response:
        if response.status != 200 or response.headers.get("Content-Encoding", "identity") != "identity":
            raise ValueError("DISCOVERY_RESPONSE_INVALID")
        body = response.read(PAGE_LIMIT + 1)
        if len(body) > PAGE_LIMIT:
            raise ValueError("DISCOVERY_PAGE_LIMIT")
        return body


def discover(*, max_projects: int = 128, transport=fetch) -> tuple[dict, dict, dict[str, bytes]]:
    if type(max_projects) is not int or not 1 <= max_projects <= 500:
        raise ValueError("PROJECT_LIMIT_INVALID")
    objects, captures, projects = {}, [], []
    total = 0
    def capture(url: str) -> bytes:
        nonlocal total
        raw = transport(url)
        total += len(raw)
        if len(raw) > PAGE_LIMIT or total > TOTAL_LIMIT:
            raise ValueError("DISCOVERY_BYTE_LIMIT")
        digest = hashlib.sha256(raw).hexdigest()
        objects[digest + ".metadata"] = raw
        captures.append({"source_url": url, "sha256": digest, "size_bytes": len(raw)})
        return raw
    url = BUCKET + "?" + urlencode({"list-type": 2, "delimiter": "/", "prefix": "KS_", "max-keys": max_projects})
    listing = capture(url)
    if b"<!DOCTYPE" in listing or b"<!ENTITY" in listing:
        raise ValueError("XML_ENTITY_DENIED")
    tree = ElementTree.fromstring(listing)
    prefixes = [entry.text for entry in tree.findall("s3:CommonPrefixes/s3:Prefix", NS)]
    if len(prefixes) > max_projects or any(not isinstance(p, str) or not PREFIX.fullmatch(p) for p in prefixes):
        raise ValueError("PROJECT_PREFIX_INVALID")
    if len(set(prefixes)) != len(prefixes):
        raise ValueError("DUPLICATE_PROJECT")
    incomplete = tree.findtext("s3:IsTruncated", namespaces=NS) != "false"
    for prefix in prefixes:
        endpoint = BUCKET + prefix + "ept.json"
        raw = capture(endpoint)
        def reject(_):
            raise ValueError("METADATA_NONFINITE")
        value = json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject)
        if not isinstance(value, dict) or value.get("dataType") not in {"laszip", "binary", "zstandard"}:
            raise ValueError("EPT_METADATA_INVALID")
        projects.append({"provider_work_unit": prefix[:-1], "source_url": endpoint,
                         "metadata_sha256": hashlib.sha256(raw).hexdigest(),
                         "metadata_bytes": len(raw), "point_count": value.get("points"),
                         "bounds": value.get("bounds"), "srs": value.get("srs"),
                         "temporal_start": None, "temporal_end": None,
                         "temporal_reason": "Acquisition dates not asserted by captured EPT metadata",
                         "payload_bytes": None, "payload_checksum": None})
    now = utc_now()
    discovery = {"schema_version": "kfm-3dep-discovery-v1", "captured_at": now,
                 "lifecycle": "candidate-only", "selection": "KS_ provider prefix",
                 "complete_for_prefix": not incomplete, "complete_for_state": False,
                 "metadata_bytes_captured": total, "project_count": len(projects),
                 "requests": captures, "projects": projects,
                 "source_admitted": False, "released": False, "published": False}
    jobs = []
    for item in projects:
        jobs.append({"job_id": hashlib.sha256(item["source_url"].encode()).hexdigest(),
                     "source_id": "usgs-3dep", "dataset_id": item["provider_work_unit"].lower(),
                     "label": item["provider_work_unit"], "state": "blocked",
                     "reason": "PAYLOAD_SELECTION_AND_CHECKSUM_REQUIRED", "scope": "kansas",
                     "expected_bytes": None, "approved_max_bytes": None, "downloaded_bytes": 0,
                     "sha256": None, "checksum_verified": False,
                     "temporal_start": None, "temporal_end": None, "estimate_basis": "unknown",
                     "rights_url": "https://www.usgs.gov/faqs/what-are-terms-uselicensing-map-services-and-data-national-map",
                     "storage": "provider-remote", "source_url": item["source_url"],
                     "updated_at": now, "protected": False})
    inventory = {"schema_version": SCHEMA, "generated_at": now, "lifecycle": "candidate-only",
                 "cache": {"limit_bytes": CACHE_LIMIT, "used_bytes": 0, "temporary_bytes": 0,
                           "replaceable_bytes": 0, "inspected": False}, "jobs": jobs}
    return discovery, inventory, objects


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--max-projects", type=int, default=128)
    args = parser.parse_args(argv)
    try:
        discovery, inventory, objects = discover(max_projects=args.max_projects)
        create_candidate(args.output_directory)
        for name, raw in objects.items():
            write_candidate(args.output_directory, name, raw)
        write_candidate(args.output_directory, "discovery.json", canonical(discovery))
        write_candidate(args.output_directory, "inventory.json", canonical(inventory))
        print(canonical({"outcome": "METADATA_CANDIDATE_CAPTURED", "project_count": discovery["project_count"],
                         "metadata_bytes_captured": discovery["metadata_bytes_captured"],
                         "complete_for_prefix": discovery["complete_for_prefix"],
                         "complete_for_state": False, "bulk_payload_bytes": 0}).decode().strip())
        return 0
    except (OSError, ValueError, KeyError, TypeError, ElementTree.ParseError):
        print('{"outcome":"ERROR","reason":"DISCOVERY_CAPTURE_FAILED"}')
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
