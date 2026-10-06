#!/usr/bin/env python3
"""Render dated provider-catalog options as a blocked owner selection receipt.

This offline example does not enumerate assets or claim a download occurred.
"""
import argparse
import hashlib
from pathlib import Path
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.local_data.acquisition import CACHE_LIMIT, SCHEMA  # noqa: E402
from tools.local_data.manage import canonical, load_json, utc_now  # noqa: E402


def queue(path: Path):
    value = load_json(path)
    if value.get("schema_version") != "kfm-acquisition-candidate-options-v1":
        raise ValueError("CANDIDATE_OPTIONS_INVALID")
    jobs = []
    now = utc_now()
    for item in value["candidates"]:
        uri = urlsplit(item["source_url"])
        if uri.scheme != "https" or not uri.hostname or uri.username or uri.password or uri.query or uri.fragment:
            raise ValueError("CATALOG_URL_INVALID")
        for scope in item["scopes"]:
            if scope not in {"kansas", "global"}:
                raise ValueError("SCOPE_INVALID")
            identifier = hashlib.sha256(canonical({"candidate": item, "scope": scope})).hexdigest()
            jobs.append({"job_id": identifier, "source_id": item["source_id"], "dataset_id": item["dataset_id"],
                         "label": item["label"] + (" — Kansas" if scope == "kansas" else " — full provider extent"),
                         "state": "blocked", "reason": "PAYLOAD_SELECTION_AND_CHECKSUM_REQUIRED",
                         "scope": scope, "expected_bytes": None, "approved_max_bytes": None,
                         "downloaded_bytes": 0, "sha256": None, "checksum_verified": False,
                         "temporal_start": item["temporal_start"], "temporal_end": item["temporal_end"],
                         "estimate_basis": "unknown", "rights_url": None,
                         "storage": "provider-remote", "source_url": item["source_url"],
                         "updated_at": now, "protected": False,
                         "coverage_note": item["coverage_note"], "catalog_verified_at": value["verified_at"],
                         "discovery_status": "catalog-only"})
    return {"schema_version": SCHEMA, "generated_at": now, "lifecycle": "candidate-only",
            "cache": {"limit_bytes": CACHE_LIMIT, "used_bytes": 0, "temporary_bytes": 0,
                      "replaceable_bytes": 0, "inspected": False}, "jobs": jobs}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=ROOT / "configs/examples/acquisition-candidates.json")
    parser.add_argument("--scope", choices=("kansas", "global"))
    args = parser.parse_args(argv)
    result = queue(args.catalog)
    if args.scope:
        result["jobs"] = [job for job in result["jobs"] if job["scope"] == args.scope]
    print(canonical(result).decode().strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
