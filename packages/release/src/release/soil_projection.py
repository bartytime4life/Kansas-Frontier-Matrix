"""Local conformance projection for an already staged USCRN daily soil snapshot.

Same contract as weather_projection: the soil serving gate (ADR-0046) must
answer ELIGIBLE and every read replays evidence verification before any
observation is returned. Observations are station-point daily values on the
station's local-standard-time day; evidence is one bundle per station and depth.
"""
from datetime import date, timedelta

from connectors_core.captured_json import utc_time
from hashing import compute_spec_hash
from policy_runtime.core import SOIL_DECISION_PROFILE, SOIL_SELF_RELEASE_LICENSES, serving_gate
from .core import SOIL, validate_snapshot
from .water_projection import replay_evidence

VERSION = "kfm-soil-v1"
# USCRN daily01 days are local standard time (no daylight saving). Manhattan
# (Riley County) and Oakley (Logan County) are both on Central time.
STANDARD_OFFSET_HOURS = {"53974": -6, "03067": -6}
ATTRIBUTION = ("NOAA National Centers for Environmental Information, U.S. Climate Reference Network (USCRN) daily01 "
               "product; Diamond et al. (2013), Bull. Amer. Meteor. Soc. 94, 485-498, doi:10.1175/BAMS-D-12-00170.1. "
               "Values may be revised.")


def negative(reason: str, *, now: str, outcome="ABSTAIN") -> dict:
    envelope = {"id": "soil:" + reason.lower(), "version": VERSION, "issued_at": now,
                "outcome": outcome, "reason_code": reason, "evidence_refs": [],
                "policy_state": "withheld", "freshness": "unknown", "correction_state": "unknown"}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    return {"envelope": envelope}


def project(raw: bytes, decision: dict | None, *, view: str, now: str, station_id: str | None = None) -> dict:
    manifest, values = validate_snapshot(raw, profile=SOIL)
    candidate, evidence = values["candidate.json"], values["evidence.json"]
    reason = serving_gate(manifest, evidence, decision, now=now,
                          decision_profile=SOIL_DECISION_PROFILE, licenses=SOIL_SELF_RELEASE_LICENSES)
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
    # As at capture, a station is current only through a reported soil moisture value, compared
    # with the current day in the station's local standard time, not the UTC date.
    latest: dict[str, str] = {}
    for r in observations:
        if r["variable"] == "SOIL_MOISTURE" and r["value"] is not None and r["observation_date"] > latest.get(r["station_id"], ""):
            latest[r["station_id"]] = r["observation_date"]
    instant = utc_time(now)
    ages = [((instant + timedelta(hours=STANDARD_OFFSET_HOURS[s])).date() - date.fromisoformat(d)).days for s, d in latest.items()]
    freshness = ("unknown" if not ages else
                 "current" if min(ages) <= candidate["stale_after_days"] else "stale-accepted")
    precision = {"spatial": {"representation": "point", "resolution": "USCRN station coordinates, EPSG:4326",
                             "accuracy": "NCEI daily01 row coordinates; a station point, not a field, county or region", "generalization_applied": False},
                 "temporal": {"granularity": "Station local-standard-time days, not UTC instants",
                              "observation_interval": {"start": manifest["start"], "end": manifest["end"]}, "freshness_class": freshness},
                 "attribute": {"measures": {"SOIL_MOISTURE": "m3/m3", "SOIL_TEMP": "degC"}, "depths_cm": list(SOIL.series_values),
                               "significant_precision": {"SOIL_MOISTURE": 3, "SOIL_TEMP": 1},
                               "classification_granularity": "Daily values as reported; missing and out-of-range values withheld, never zero"},
                 "evidence_refs": refs,
                 "transform_receipt_refs": ["kfm://receipt/validation/" + values["validation.json"]["receipt_digest"].split(":")[1]]}
    envelope = {"id": "soil:" + view, "version": VERSION, "issued_at": now, "outcome": "ANSWER",
                "reason_code": "RELEASED_SNAPSHOT", "evidence_refs": refs, "policy_state": "approved_snapshot",
                "freshness": freshness, "correction_state": "ACTIVE", "precision_actually_used": precision}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    common = {"package_id": manifest["package_id"], "source_id": SOIL.source_id, "coverage": candidate["coverage"],
              "retrieved_at": candidate["retrieved_at"], "reviewed_at": decision["reviewed_at"],
              "released_at": decision["released_at"], "approval_expires_at": decision["expires_at"],
              "stale_after_days": candidate["stale_after_days"], "correction_state": "ACTIVE", "attribution": ATTRIBUTION}
    if view == "bootstrap":
        data = {**common, "layers": [{"id": "uscrn-daily-soil-pilot", "title": "Reviewed NOAA USCRN daily soil moisture and temperature", "evidence_eligible": True}],
                "observation_count": len(observations)}
    elif view == "layers":
        data = {**common, "stations": [s for s in candidate["stations"] if s["id"] in station_ids], "observations": observations,
                "freshness_at_capture": {k: v for k, v in candidate["freshness_at_capture"].items() if k in station_ids}}
    else:
        data = {**common, "entries": [{k: e[k] for k in ("station_id", "series", "evidence_ref", "bundle", "verification_history")} for e in selected]}
    return {"envelope": envelope, "data": data}
