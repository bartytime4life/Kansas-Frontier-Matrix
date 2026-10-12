"""Local conformance projection for an already staged USGS ComCat earthquake snapshot.

Same contract as storm_events_projection: the earthquake serving gate (ADR-0049)
must answer ELIGIBLE and every selected bundle replays evidence verification
before any record is returned. Records are catalog solutions (origin time,
epicenter, depth, magnitude) in the Kansas context envelope, never shaking
estimates or alerts; evidence is one bundle per UTC origin month part, and a
month filter selects every part of that month. Freshness is the age of the
capture: ComCat revises solutions after retrieval.
"""
from collections import Counter
from datetime import timedelta

from connectors_core.captured_json import utc_time
from hashing import compute_spec_hash
from policy_runtime.core import EARTHQUAKE_DECISION_PROFILE, EARTHQUAKE_SELF_RELEASE_LICENSES, serving_gate
from .core import EARTHQUAKES, validate_snapshot
from .water_projection import replay_evidence

VERSION = "kfm-earthquakes-v1"
# A capture older than this still answers, as stale-accepted: ComCat may have revised its solutions.
STALE_AFTER_DAYS = 30
ATTRIBUTION = ("U.S. Geological Survey, Earthquake Hazards Program, ANSS Comprehensive Earthquake Catalog (ComCat). "
               "Solutions may be revised. Catalog solutions, not shaking estimates or alerts.")


def negative(reason: str, *, now: str, outcome="ABSTAIN") -> dict:
    envelope = {"id": "earthquakes:" + reason.lower(), "version": VERSION, "issued_at": now,
                "outcome": outcome, "reason_code": reason, "evidence_refs": [],
                "policy_state": "withheld", "freshness": "unknown", "correction_state": "unknown"}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    return {"envelope": envelope}


def selection_summary(months: set, observations: list) -> dict:
    """Describes exactly the returned records, never the whole data year."""
    magnitudes = [r["magnitude"] for r in observations if r["magnitude"] is not None]
    return {"months": sorted(months), "observation_count": len(observations),
            "review_status": dict(sorted(Counter(r["review_status"] or "unknown" for r in observations).items())),
            "context_margin_count": sum(1 for r in observations if "CONTEXT_MARGIN" in r["flags"]),
            "magnitude_range": [min(magnitudes), max(magnitudes)] if magnitudes else None,
            "latest_event_date": max((r["origin_utc"][:10] for r in observations), default=None)}


def project(raw: bytes, decision: dict | None, *, view: str, now: str, month: int | None = None) -> dict:
    manifest, values = validate_snapshot(raw, profile=EARTHQUAKES)
    candidate, evidence, catalog = values["candidate.json"], values["evidence.json"], values["catalog.json"]
    reason = serving_gate(manifest, evidence, decision, now=now,
                          decision_profile=EARTHQUAKE_DECISION_PROFILE, licenses=EARTHQUAKE_SELF_RELEASE_LICENSES)
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
    observations = [r for r in candidate["observations"] if int(r["origin_utc"][5:7]) in months]
    stale = utc_time(now) - utc_time(candidate["retrieved_at"]) > timedelta(days=STALE_AFTER_DAYS)
    freshness = "stale-accepted" if stale else "current"
    precision = {"spatial": {"representation": "epicenter points in the Kansas context envelope",
                             "resolution": "EPSG:4326 longitude and latitude rounded to 4 decimal places",
                             "accuracy": ("Catalog epicenter estimates with kilometre-scale uncertainty; the envelope "
                                          "(-102.1 to -94.5, 36.9 to 40.1) is not the state boundary"),
                             "generalization_applied": False},
                 "temporal": {"granularity": "Origin time in UTC to the millisecond",
                              "observation_interval": {"start": manifest["start"], "end": manifest["end"]}, "freshness_class": freshness},
                 "attribute": {"measures": {"magnitude": "catalog magnitude of the stated magnitude_type",
                                            "depth_km": "hypocentral depth in kilometres"},
                               "classification_granularity": ("Magnitude types (ml, md, mb_lg, mww, ...) are not interchangeable; "
                                                              "automatic solutions are flagged; deleted solutions are withheld")},
                 "evidence_refs": refs,
                 "transform_receipt_refs": ["kfm://receipt/validation/" + values["validation.json"]["receipt_digest"].split(":")[1]]}
    envelope = {"id": "earthquakes:" + view, "version": VERSION, "issued_at": now, "outcome": "ANSWER",
                "reason_code": "RELEASED_SNAPSHOT", "evidence_refs": refs, "policy_state": "approved_snapshot",
                "freshness": freshness, "correction_state": "ACTIVE", "precision_actually_used": precision}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    common = {"package_id": manifest["package_id"], "source_id": EARTHQUAKES.source_id, "coverage": candidate["coverage"],
              "data_year": candidate["data_year"], "year_state": candidate["year_state"], "bounds": candidate["bounds"],
              "retrieved_at": candidate["retrieved_at"], "reviewed_at": decision["reviewed_at"],
              "released_at": decision["released_at"], "approval_expires_at": decision["expires_at"],
              "stale_after_days": STALE_AFTER_DAYS, "correction_state": "ACTIVE", "attribution": ATTRIBUTION,
              "life_safety": "not_for_life_safety"}
    if view == "bootstrap":
        data = {**common, "layers": [{"id": "usgs-earthquakes-ks", "title": "Reviewed USGS earthquakes, Kansas context envelope",
                                      "evidence_eligible": True}],
                "observation_count": len(observations), "months": sorted(months)}
    elif view == "layers":
        # The catalog summary always describes the whole data year; ``selection`` describes
        # exactly the records returned, so a month filter never reports year-level counts as its own.
        data = {**common, "dataset": {**catalog["dataset"], "scope": "data_year"},
                "selection": selection_summary(months, observations), "observations": observations}
    else:
        data = {**common, "entries": [{k: e[k] for k in ("month", "part", "evidence_ref", "bundle", "verification_history")} for e in selected]}
    return {"envelope": envelope, "data": data}
