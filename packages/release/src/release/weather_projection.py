"""Local conformance projection for an already staged GHCN-Daily weather snapshot.

Same contract as water_projection: the weather serving gate (ADR-0045) must
answer ELIGIBLE and every read replays evidence verification before any
observation is returned. Observations are station-local daily values.
"""
from datetime import date

from connectors_core.captured_json import utc_time
from hashing import compute_spec_hash
from policy_runtime.core import WEATHER_DECISION_PROFILE, WEATHER_SELF_RELEASE_LICENSES, serving_gate
from .core import WEATHER, validate_snapshot
from .water_projection import replay_evidence

VERSION = "kfm-weather-v1"
ATTRIBUTION = ("Menne et al. (2012), Global Historical Climatology Network - Daily (GHCN-Daily), Version 3, "
               "NOAA NCEI, doi:10.7289/V5D21VHZ. Values are preliminary and may be revised.")


def negative(reason: str, *, now: str, outcome="ABSTAIN") -> dict:
    envelope = {"id": "weather:" + reason.lower(), "version": VERSION, "issued_at": now,
                "outcome": outcome, "reason_code": reason, "evidence_refs": [],
                "policy_state": "withheld", "freshness": "unknown", "correction_state": "unknown"}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    return {"envelope": envelope}


def project(raw: bytes, decision: dict | None, *, view: str, now: str, station_id: str | None = None) -> dict:
    manifest, values = validate_snapshot(raw, profile=WEATHER)
    candidate, evidence = values["candidate.json"], values["evidence.json"]
    reason = serving_gate(manifest, evidence, decision, now=now,
                          decision_profile=WEATHER_DECISION_PROFILE, licenses=WEATHER_SELF_RELEASE_LICENSES)
    if reason != "ELIGIBLE":
        return negative(reason, now=now)
    if view not in {"bootstrap", "layers", "evidence"}:
        return negative("ROUTE_NOT_FOUND", now=now)
    assert decision is not None
    selected = [entry for entry in evidence["entries"] if station_id is None or entry["station_id"] == station_id]
    if not selected:
        return negative("EVIDENCE_NOT_FOUND", now=now)
    failure = replay_evidence(selected, decision, now)
    if failure:
        return negative(failure[0], now=now, outcome=failure[1])
    refs = [entry["evidence_ref"] for entry in selected]
    station_ids = {e["station_id"] for e in selected}
    observations = [r for r in candidate["observations"] if r["station_id"] in station_ids]
    # A withheld value cannot make a day current.
    latest = max((r["observation_date"] for r in observations if r["value"] is not None), default=None)
    today = utc_time(now).date()
    freshness = ("unknown" if latest is None else
                 "stale-accepted" if (today - date.fromisoformat(latest)).days > candidate["stale_after_days"] else "current")
    precision = {"spatial": {"representation": "point", "resolution": "Provider station coordinates, EPSG:4326",
                             "accuracy": "GHCN-Daily station list coordinates; no inferred positional accuracy", "generalization_applied": False},
                 "temporal": {"granularity": "Station-local observation days, not UTC instants",
                              "observation_interval": {"start": manifest["start"], "end": manifest["end"]}, "freshness_class": freshness},
                 "attribute": {"measures": {"PRCP": "mm", "TMAX": "degC", "TMIN": "degC"}, "significant_precision": 1,
                               "classification_granularity": "Tenths as reported; missing and quality-flagged values withheld, never zero"},
                 "evidence_refs": refs,
                 "transform_receipt_refs": ["kfm://receipt/validation/" + values["validation.json"]["receipt_digest"].split(":")[1]]}
    envelope = {"id": "weather:" + view, "version": VERSION, "issued_at": now, "outcome": "ANSWER",
                "reason_code": "RELEASED_SNAPSHOT", "evidence_refs": refs, "policy_state": "approved_snapshot",
                "freshness": freshness, "correction_state": "ACTIVE", "precision_actually_used": precision}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    common = {"package_id": manifest["package_id"], "source_id": WEATHER.source_id, "coverage": candidate["coverage"],
              "retrieved_at": candidate["retrieved_at"], "reviewed_at": decision["reviewed_at"],
              "released_at": decision["released_at"], "approval_expires_at": decision["expires_at"],
              "stale_after_days": candidate["stale_after_days"], "correction_state": "ACTIVE", "attribution": ATTRIBUTION}
    if view == "bootstrap":
        data = {**common, "layers": [{"id": "ghcnd-daily-pilot", "title": "Reviewed NOAA GHCN-Daily station weather", "evidence_eligible": True}],
                "observation_count": len(observations)}
    elif view == "layers":
        data = {**common, "stations": [s for s in candidate["stations"] if s["id"] in station_ids], "observations": observations,
                "freshness_at_capture": {k: v for k, v in candidate["freshness_at_capture"].items() if k in station_ids}}
    else:
        data = {**common, "entries": [{k: e[k] for k in ("station_id", "evidence_ref", "bundle", "verification_history")} for e in selected]}
    return {"envelope": envelope, "data": data}
