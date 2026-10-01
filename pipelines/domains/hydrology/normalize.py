"""Pure, deterministic USGS discharge transformation from verified captured bytes.

Produces review candidates only. A complete capture is neither source admission
nor evidence eligibility. Observation identity stays stable across revisions.
"""
from __future__ import annotations

from decimal import Decimal, InvalidOperation
import math

from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, timestamp, utc_time
from connectors.usgs.water_data.pilot_capture import MAX_PAGE_BYTES, MAX_TOTAL_BYTES, STATIONS, STALE_AFTER_SECONDS, request_plan, safe_page_url


def _text(value, label, maximum=256):
    if not isinstance(value, str) or not 0 < len(value) <= maximum or any(ord(c) < 32 for c in value):
        raise ValueError("INVALID_" + label)
    return value


def _geometry(value):
    if not isinstance(value, dict) or value.get("type") != "Point":
        raise ValueError("STATION_POINT_REQUIRED")
    coordinates = value.get("coordinates")
    if (not isinstance(coordinates, list) or len(coordinates) != 2
            or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not -180 <= v <= 180 or not math.isfinite(v) for v in coordinates)
            or not -180 <= coordinates[0] <= 180 or not -90 <= coordinates[1] <= 90):
        raise ValueError("INVALID_STATION_GEOMETRY")
    return {"type": "Point", "coordinates": coordinates}


def normalize_capture(manifest: dict, objects: dict[str, bytes], *, stale_after_seconds=STALE_AFTER_SECONDS) -> dict:
    """Check capture closure, preserve revisions, and select the latest revision."""
    if stale_after_seconds != STALE_AFTER_SECONDS:
        raise ValueError("UNSUPPORTED_PILOT_FRESHNESS")
    body = {key: value for key, value in manifest.items() if key != "capture_id"}
    if manifest.get("capture_id") != digest_bytes(canonical_bytes(body)):
        raise ValueError("CAPTURE_DIGEST_MISMATCH")
    if manifest.get("profile") != "kfm.usgs-water-pilot-capture/v1" or manifest.get("complete") is not True:
        raise ValueError("CAPTURE_INCOMPLETE")
    if manifest.get("station_ids") != list(STATIONS) or manifest.get("parameter_code") != "00060":
        raise ValueError("CAPTURE_SCOPE_MISMATCH")
    start, end = utc_time(manifest["start"]), utc_time(manifest["end"])
    retrieved = utc_time(manifest["captured_at"])
    plan = {(item["station_id"], item["collection"]): item for item in request_plan(manifest["start"], manifest["end"])}
    expected = {key: item["url"] for key, item in plan.items()}
    stations, revisions = {}, {}
    total = 0
    pages = manifest.get("pages")
    if not isinstance(pages, list) or not 4 <= len(pages) <= 12:
        raise ValueError("CAPTURE_PAGE_LIMIT")
    for page in pages:
        key = (page["station_id"], page["collection"])
        if key not in expected or expected[key] != page["url"]:
            raise ValueError("CAPTURE_PAGE_CHAIN_MISMATCH")
        safe_page_url(page["url"], plan[key])
        raw = objects.get(page["sha256"])
        if raw is None or digest_bytes(raw) != page["sha256"] or len(raw) != page["bytes"]:
            raise ValueError("PAGE_DIGEST_MISMATCH")
        total += len(raw)
        if total > MAX_TOTAL_BYTES:
            raise ValueError("CAPTURE_BYTE_LIMIT")
        value = decode_object(raw, limit=MAX_PAGE_BYTES)
        if value.get("type") != "FeatureCollection" or not isinstance(value.get("features"), list) or len(value["features"]) > 4000:
            raise ValueError("INVALID_FEATURE_COLLECTION")
        links = value.get("links")
        if not isinstance(links, list) or len(links) > 100 or any(not isinstance(link, dict) for link in links):
            raise ValueError("INVALID_PAGE_LINKS")
        next_links = [link for link in links if link.get("rel") == "next"]
        if len(next_links) > 1:
            raise ValueError("AMBIGUOUS_PAGINATION")
        expected[key] = next_links[0].get("href") if next_links else None
        if next_links:
            safe_page_url(expected[key], plan[key])
        page_time = timestamp(utc_time(page["retrieved_at"]))
        if utc_time(page_time) > retrieved:
            raise ValueError("RETRIEVAL_CLOCK_MISMATCH")
        for feature in value["features"]:
            if not isinstance(feature, dict) or feature.get("type") != "Feature" or not isinstance(feature.get("properties"), dict):
                raise ValueError("INVALID_FEATURE")
            p = feature["properties"]
            if key[1] == "monitoring-locations":
                if (feature.get("id") != key[0] or p.get("agency_code") != "USGS"
                        or p.get("monitoring_location_number") != key[0].removeprefix("USGS-")
                        or str(p.get("state_code")) not in {"20", "US:20"}):
                    raise ValueError("STATION_IDENTITY_MISMATCH")
                station = {"id": key[0], "name": _text(p.get("monitoring_location_name"), "STATION_NAME"),
                           "geometry": _geometry(feature.get("geometry")), "page_digest": page["sha256"],
                           "retrieved_at": page_time,
                           "horizontal_accuracy": p.get("horizontal_positional_accuracy"),
                           "original_horizontal_datum": p.get("original_horizontal_datum"),
                           "provider_revision_at": p.get("revision_modified")}
                if key[0] in stations and stations[key[0]] != station:
                    raise ValueError("CONFLICTING_STATION_METADATA")
                stations[key[0]] = station
                continue
            if p.get("monitoring_location_id") != key[0] or p.get("parameter_code") != "00060":
                raise ValueError("OBSERVATION_SCOPE_MISMATCH")
            observed, revised = utc_time(p["time"]), utc_time(p["last_modified"])
            if not start <= observed <= end or observed > retrieved or not observed <= revised <= utc_time(page_time):
                raise ValueError("OBSERVATION_TIME_MISMATCH")
            series = _text(p.get("time_series_id"), "SERIES_ID")
            source_id = _text(str(feature.get("id", "")), "FEATURE_ID")
            unit = _text(p.get("unit_of_measure"), "UNIT", 32)
            if unit != "ft^3/s":
                raise ValueError("UNSUPPORTED_DISCHARGE_UNIT")
            raw_value = p.get("value")
            if raw_value is None:
                amount = None
            else:
                if isinstance(raw_value, bool) or len(str(raw_value)) > 64:
                    raise ValueError("INVALID_DISCHARGE")
                try:
                    decimal = Decimal(str(raw_value))
                except InvalidOperation as exc:
                    raise ValueError("INVALID_DISCHARGE") from exc
                if not decimal.is_finite() or decimal.copy_abs() > Decimal("1e9"):
                    raise ValueError("INVALID_DISCHARGE")
                amount = float(decimal)
            approval = p.get("approval_status")
            if approval not in {"Provisional", "Approved", "P", "A"}:
                raise ValueError("UNKNOWN_PROVIDER_APPROVAL")
            qualifier = p.get("qualifier")
            qualifiers = [] if qualifier is None else [_text(qualifier, "QUALIFIER")]
            identity = digest_bytes(canonical_bytes([key[0], series, "00060", timestamp(observed)]))
            record = {"profile": "kfm.flow-observation/v1", "id": "kfm:flow:" + identity.split(":")[1],
                      "station_id": key[0], "time_series_id": series, "source_feature_id": source_id,
                      "statistic_id": _text(p.get("statistic_id"), "STATISTIC_ID", 5),
                      "method_category": p.get("method_category"),
                      "parameter_code": "00060", "observed_at": timestamp(observed),
                      "provider_revision_at": timestamp(revised), "retrieved_at": page_time,
                      "value": amount, "unit": unit, "qualifiers": qualifiers,
                      "approval_status": approval, "provisional": approval in {"Provisional", "P"},
                      "source_role": "observed_gauge", "page_digest": page["sha256"]}
            record["evidence_ref"] = "kfm:evidence:flow:" + identity.split(":")[1]
            record["record_digest"] = digest_bytes(canonical_bytes(record))
            revision_key = (record["id"], record["provider_revision_at"])
            if revision_key in revisions:
                old = revisions[revision_key]
                # Repeated pages may have distinct retrieval timestamps/digests.
                semantic = lambda r: {k: v for k, v in r.items() if k not in {"retrieved_at", "page_digest", "record_digest"}}
                if semantic(old) != semantic(record):
                    raise ValueError("CONFLICTING_OBSERVATION_REVISION")
                if canonical_bytes(record) < canonical_bytes(old):
                    revisions[revision_key] = record
            else:
                revisions[revision_key] = record
    if any(expected.values()) or set(stations) != set(STATIONS):
        raise ValueError("CAPTURE_CLOSURE_INCOMPLETE")
    latest = {}
    for record in sorted(revisions.values(), key=lambda r: (utc_time(r["provider_revision_at"]), r["record_digest"])):
        latest[record["id"]] = record
    observations = sorted(latest.values(), key=lambda r: (r["station_id"], r["observed_at"], r["id"]))
    latest_times = {station: max((r["observed_at"] for r in observations
                                  if r["station_id"] == station and r["value"] is not None), default=None)
                    for station in STATIONS}
    freshness = {station: ("EMPTY" if when is None else
                           "STALE" if (retrieved - utc_time(when)).total_seconds() > stale_after_seconds else "RECENT")
                 for station, when in latest_times.items()}
    candidate = {"profile": "kfm.usgs-water-candidate/v1", "capture_id": manifest["capture_id"],
                 "source_id": "usgs-nwis", "start": manifest["start"], "end": manifest["end"],
                 "retrieved_at": manifest["captured_at"], "stations": sorted(stations.values(), key=lambda s: s["id"]),
                 "observations": observations,
                 "revision_history": sorted(revisions.values(), key=lambda r: (r["id"], utc_time(r["provider_revision_at"]))),
                 "freshness_at_capture": freshness, "stale_after_seconds": stale_after_seconds,
                 "coverage": "EMPTY" if all(state == "EMPTY" for state in freshness.values()) else "PARTIAL" if "EMPTY" in freshness.values() else "COMPLETE",
                 "review_state": "PENDING", "source_admission": "PENDING", "release_state": "UNRELEASED"}
    candidate["candidate_id"] = digest_bytes(canonical_bytes(candidate))
    return candidate
