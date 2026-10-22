"""FAA APT_BASE -> held candidate. Original archive remains in private RAW.

This is not NTAD/BTS data; never assigns FAA authority to a community source.
"""
from copy import deepcopy
from datetime import date, datetime, timedelta
from pathlib import PurePosixPath
import csv
import hashlib
import io
import json
import math
import stat
import zipfile
import rfc8785

VERSION = "faa-apt-v1"
FIELDS = ("EFF_DATE", "SITE_NO", "SITE_TYPE_CODE", "STATE_CODE", "ARPT_ID", "ARPT_NAME", "CITY",
          "COUNTY_NAME", "COUNTY_ASSOC_STATE", "FACILITY_USE_CODE", "OWNERSHIP_TYPE_CODE",
          "ARPT_STATUS", "LAT_DECIMAL", "LONG_DECIMAL", "ELEV", "ICAO_ID", "SURVEY_METHOD_CODE")
SOURCE = "https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/2026-10-01/"


def canonical(value):
    # Existing KFM common spec_hash profile, pinned by the root distribution.
    return rfc8785.dumps(value)


def sha(value):
    return "sha256:" + hashlib.sha256(value).hexdigest()


def _record(original, edition, archive_sha256, retrieved_at):
    """One deterministic projection for preparation and consumption checks."""
    row = original
    row_digest = sha(canonical(original))
    lat, lon = float(row["LAT_DECIMAL"]), float(row["LONG_DECIMAL"])
    elev = float(row["ELEV"]) if row["ELEV"] else None
    entity = "faa:site:" + (row["SITE_NO"] + ":" + row["SITE_TYPE_CODE"]).lower()
    revision = "faa:revision:" + sha(canonical([entity, edition.isoformat(), row_digest])).split(":")[1]
    bundle_id = "faa:bundle:" + revision.split(":")[-1]
    ref = {"ref": "kfm://aviation/airport/" + revision, "kind": "record", "bundle_ref": bundle_id}
    bundle = {"bundle_id": bundle_id, "claim_scope": "FAA landing facility reference edition; research/context only, not navigation or flight planning.",
              "evidence_refs": [ref], "source_records": ["sha256:" + archive_sha256, row_digest],
              "citations": [SOURCE], "rights": {"license": "FAA source; independent product rights review required"},
              "sensitivity": {"level": "quarantine", "reason": "Unadmitted aviation candidate", "applied_at": retrieved_at},
              "transforms": ["kfm:transform:faa-apt:v1"], "checksums": {"archive": "sha256:" + archive_sha256, "record": row_digest}}
    bundle["spec_hash"] = {"value": sha(canonical(bundle))}
    return {"entity_id": entity, "revision_id": revision, "edition": edition.isoformat(),
            "valid_to_exclusive": (edition + timedelta(days=28)).isoformat(), "state": row["STATE_CODE"],
            "county_name": row["COUNTY_NAME"], "county_state": row["COUNTY_ASSOC_STATE"],
            "name": row["ARPT_NAME"], "faa_id": row["ARPT_ID"], "icao_id": row["ICAO_ID"] or None,
            "facility_type": row["SITE_TYPE_CODE"], "facility_use": row["FACILITY_USE_CODE"],
            "public_candidate": row["SITE_TYPE_CODE"] == "A" and row["FACILITY_USE_CODE"] == "PU" and row["OWNERSHIP_TYPE_CODE"] in {"PU", "PR"} and row["ARPT_STATUS"] == "O",
            "longitude": lon, "latitude": lat, "horizontal_datum": "UNVERIFIED_SOURCE_DATUM",
            "elevation": elev, "elevation_unit": "ft", "vertical_reference": "MSL",
            "original": original, "evidence_ref": ref, "bundle": bundle}


def prepare(archive, receipt, *, states=("KS",)):
    """States are an operator-configured surrounding-region set, max seven.

    County names are provider associations, not a spatial county/GEOID join.
    Future editions and non-public/military facilities remain held.
    """
    if not states or len(set(states)) != len(states) or len(states) > 7 or set(states) - {"KS", "CO", "NE", "MO", "OK", "IA", "AR"}:
        raise ValueError("REGION_INVALID")
    if len(archive) > 16 * 1024 * 1024 or receipt.get("sha256") != hashlib.sha256(archive).hexdigest():
        raise ValueError("CAPTURE_INTEGRITY_FAILED")
    edition = date.fromisoformat(receipt["edition"])
    retrieved = datetime.fromisoformat(receipt["retrieved_at"].replace("Z", "+00:00"))
    if retrieved.tzinfo is None or receipt.get("source_id") != "faa-nasr-apt" or receipt.get("url") != "https://nfdc.faa.gov/webContent/28DaySub/extra/01_Oct_2026_APT_CSV.zip" or edition.isoformat() != "2026-10-01":
        raise ValueError("CAPTURE_BINDING_INVALID")
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        members = z.infolist()
        if len(members) > 32 or len({m.filename for m in members}) != len(members):
            raise ValueError("ARCHIVE_LAYOUT_INVALID")
        for m in members:
            p = PurePosixPath(m.filename)
            if p.is_absolute() or ".." in p.parts or "\\" in m.filename or stat.S_ISLNK(m.external_attr >> 16) or m.flag_bits & 1 or m.file_size > 16 * 1024 * 1024 or m.file_size > 100 * max(m.compress_size, 1):
                raise ValueError("ARCHIVE_MEMBER_UNSAFE")
        if sum(m.file_size for m in members) > 64 * 1024 * 1024 or "APT_BASE.csv" not in z.namelist():
            raise ValueError("ARCHIVE_BUDGET_EXCEEDED")
        raw = z.read("APT_BASE.csv")  # CRC checked, no extraction, contact files never parsed.
    rows = csv.DictReader(io.StringIO(raw.decode("utf-8-sig"), newline=""))
    # Exact header set/order pinned from the inspected edition, including unused columns.
    header_digest = hashlib.sha256(canonical(rows.fieldnames)).hexdigest()
    if header_digest != HEADER_DIGEST:
        raise ValueError("SCHEMA_DRIFT")
    records, rejects, seen = [], [], set()
    total = 0
    for number, row in enumerate(rows, 2):
        total += 1
        if total > 30000 or None in row or any(v is None or len(v) > 4096 for v in row.values()):
            raise ValueError("CSV_STRUCTURE_INVALID")
        if row["STATE_CODE"] not in states:
            continue
        original = {k: row[k] for k in FIELDS}
        row_digest = sha(canonical(original))
        try:
            row_date = datetime.strptime(row["EFF_DATE"], "%Y/%m/%d").date()
            if row_date != edition:
                raise ValueError("EDITION_MISMATCH")
            import re
            if not re.fullmatch(r"\d{5}\.\d{0,3}", row["SITE_NO"]) or row["SITE_TYPE_CODE"] not in {"A", "H", "C", "G", "U", "B"}:
                raise ValueError("IDENTITY_INVALID")
            key = row["SITE_NO"] + ":" + row["SITE_TYPE_CODE"]
            if key in seen:
                raise ValueError("DUPLICATE_ENTITY")
            seen.add(key)
            lat, lon = float(row["LAT_DECIMAL"]), float(row["LONG_DECIMAL"])
            if not math.isfinite(lat) or not math.isfinite(lon) or not -90 <= lat <= 90 or not -180 <= lon <= 180:
                raise ValueError("COORDINATES_INVALID")
            elev = float(row["ELEV"]) if row["ELEV"] else None
            if elev is not None and (not math.isfinite(elev) or not -1500 <= elev <= 15000):
                raise ValueError("ELEVATION_INVALID")
            records.append(_record(original, edition, receipt["sha256"], receipt["retrieved_at"]))
        except (ValueError, OverflowError) as error:
            rejects.append({"row": number, "record_digest": row_digest, "reason": str(error), "original": original})
    records.sort(key=lambda r: r["revision_id"])
    payload = {"profile": "kfm.faa-airports-candidate/v1", "parser_version": VERSION, "edition": edition.isoformat(),
               "retrieved_at": receipt["retrieved_at"], "source_publication_time": None, "release_time": None,
               "archive_sha256": receipt["sha256"], "states": sorted(states), "release_state": "HELD",
               "rights_state": "REVIEW_REQUIRED", "source_rows": total, "coverage": "PARTIAL" if rejects else "REQUESTED_STATES",
               "future_at_capture": edition > retrieved.date(), "records": records, "rejects": rejects}
    payload["candidate_id"] = sha(canonical(payload))
    return payload


def verify_candidate(candidate):
    """Return a detached, integrity-checked private candidate; never authorize release.

    The outer seal covers every field. Rebuilding each record also prevents a
    rehashed container from assigning changed projections to an old revision.
    This is content integrity, not authentication of an FAA source capture.
    """
    candidate = deepcopy(candidate)
    if not isinstance(candidate, dict):
        raise ValueError("CANDIDATE_SHAPE_INVALID")
    subject = {k: v for k, v in candidate.items() if k != "candidate_id"}
    try:
        expected_id = sha(canonical(subject))
    except (TypeError, ValueError):
        raise ValueError("CANDIDATE_SHAPE_INVALID") from None
    if candidate.get("candidate_id") != expected_id:
        raise ValueError("CANDIDATE_DIGEST_MISMATCH")
    if (candidate.get("profile") != "kfm.faa-airports-candidate/v1"
            or candidate.get("parser_version") != VERSION
            or candidate.get("release_state") != "HELD"
            or candidate.get("rights_state") != "REVIEW_REQUIRED"
            or candidate.get("release_time") is not None):
        raise ValueError("CANDIDATE_STATE_INVALID")
    try:
        edition = date.fromisoformat(candidate["edition"])
        if not isinstance(candidate["records"], list):
            raise ValueError
        seen = set()
        for record in candidate["records"]:
            original = record["original"]
            if (not isinstance(original, dict) or set(original) != set(FIELDS)
                    or any(not isinstance(v, str) for v in original.values())):
                raise ValueError
            expected = _record(original, edition, candidate["archive_sha256"], candidate["retrieved_at"])
            if (canonical(record) != canonical(expected) or record["entity_id"] in seen
                    or datetime.strptime(original["EFF_DATE"], "%Y/%m/%d").date() != edition):
                raise ValueError
            seen.add(record["entity_id"])
    except (KeyError, TypeError, ValueError, OverflowError):
        raise ValueError("RECORD_BINDING_MISMATCH") from None
    return candidate


# Updated only after an explicit schema review; populated from the exact official edition.
HEADER_DIGEST = "5a6f818d3a354dfb983a166b964bf2dc7dc4f42b5ac5395a3345c137e7f0c02f"
