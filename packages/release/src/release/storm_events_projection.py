"""Local conformance projection for an already staged NOAA Storm Events snapshot.

Same contract as soil_projection: the storm events serving gate (ADR-0047) must
answer ELIGIBLE and every selected bundle replays evidence verification before
any record is returned. Records are historical NWS event reports for a county or
forecast zone, never warnings; evidence is one bundle per month part, and a
month filter selects every part of that month. Freshness is the age of the NCEI
file vintage, the only clock a historical file has.
"""
from datetime import date

from connectors_core.captured_json import utc_time
from hashing import compute_spec_hash
from policy_runtime.core import STORM_EVENTS_DECISION_PROFILE, STORM_EVENTS_SELF_RELEASE_LICENSES, serving_gate
from .core import STORM_EVENTS, validate_snapshot
from .water_projection import replay_evidence

VERSION = "kfm-storm-events-v1"
ATTRIBUTION = ("NOAA National Centers for Environmental Information, Storm Events Database. Records are compiled from "
               "National Weather Service reports and may be revised. Historical event reports, not warnings.")


def negative(reason: str, *, now: str, outcome="ABSTAIN") -> dict:
    envelope = {"id": "storm-events:" + reason.lower(), "version": VERSION, "issued_at": now,
                "outcome": outcome, "reason_code": reason, "evidence_refs": [],
                "policy_state": "withheld", "freshness": "unknown", "correction_state": "unknown"}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    return {"envelope": envelope}


def project(raw: bytes, decision: dict | None, *, view: str, now: str, month: int | None = None) -> dict:
    manifest, values = validate_snapshot(raw, profile=STORM_EVENTS)
    candidate, evidence, catalog = values["candidate.json"], values["evidence.json"], values["catalog.json"]
    reason = serving_gate(manifest, evidence, decision, now=now,
                          decision_profile=STORM_EVENTS_DECISION_PROFILE, licenses=STORM_EVENTS_SELF_RELEASE_LICENSES)
    if reason != "ELIGIBLE":
        return negative(reason, now=now)
    if view not in {"bootstrap", "layers", "evidence"}:
        return negative("ROUTE_NOT_FOUND", now=now)
    assert decision is not None
    selected = [entry for entry in evidence["entries"] if month is None or entry["month"] == month]
    if not selected:
        return negative("EVIDENCE_NOT_FOUND", now=now)
    failure = replay_evidence(selected, decision, now)
    if failure:
        return negative(failure[0], now=now, outcome=failure[1])
    refs = [entry["evidence_ref"] for entry in selected]
    months = {e["month"] for e in selected}
    observations = [r for r in candidate["observations"] if int(r["begin_local"][5:7]) in months]
    age = (utc_time(now).date() - date.fromisoformat(candidate["vintage_created"])).days
    freshness = "current" if age <= candidate["stale_after_days"] else "stale-accepted"
    precision = {"spatial": {"representation": "county or forecast zone; report points where present",
                             "resolution": "NCEI county/zone FIPS; begin and end coordinates in EPSG:4326 when reported",
                             "accuracy": "Report points, not a path, footprint or area; selection by NCEI STATE_FIPS, not a spatial join",
                             "generalization_applied": False},
                 "temporal": {"granularity": "Event begin and end in reported local time; UTC only when the zone token carries an offset",
                              "observation_interval": {"start": manifest["start"], "end": manifest["end"]}, "freshness_class": freshness},
                 "attribute": {"measures": {"damage_property_usd": "nominal event-year USD", "damage_crops_usd": "nominal event-year USD"},
                               "classification_granularity": ("NCEI event types as reported; damage, magnitude and F/EF scale kept "
                                                              "as source strings; blank damage is unreported, never zero; narratives excluded")},
                 "evidence_refs": refs,
                 "transform_receipt_refs": ["kfm://receipt/validation/" + values["validation.json"]["receipt_digest"].split(":")[1]]}
    envelope = {"id": "storm-events:" + view, "version": VERSION, "issued_at": now, "outcome": "ANSWER",
                "reason_code": "RELEASED_SNAPSHOT", "evidence_refs": refs, "policy_state": "approved_snapshot",
                "freshness": freshness, "correction_state": "ACTIVE", "precision_actually_used": precision}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    common = {"package_id": manifest["package_id"], "source_id": STORM_EVENTS.source_id, "coverage": candidate["coverage"],
              "data_year": candidate["data_year"], "source_file": candidate["source_file"],
              "vintage_created": candidate["vintage_created"], "retrieved_at": candidate["retrieved_at"],
              "reviewed_at": decision["reviewed_at"], "released_at": decision["released_at"],
              "approval_expires_at": decision["expires_at"], "stale_after_days": candidate["stale_after_days"],
              "correction_state": "ACTIVE", "attribution": ATTRIBUTION, "life_safety": "not_for_life_safety"}
    if view == "bootstrap":
        data = {**common, "layers": [{"id": "noaa-storm-events-ks", "title": "Reviewed NOAA Storm Events, Kansas", "evidence_eligible": True}],
                "observation_count": len(observations), "months": sorted(months)}
    elif view == "layers":
        data = {**common, "dataset": catalog["dataset"], "observations": observations}
    else:
        data = {**common, "entries": [{k: e[k] for k in ("month", "part", "evidence_ref", "bundle", "verification_history")} for e in selected]}
    return {"envelope": envelope, "data": data}
