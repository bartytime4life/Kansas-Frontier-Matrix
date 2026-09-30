"""Local/Worker conformance projection for an already staged water snapshot."""
from connectors_core.captured_json import utc_time
from evidence_resolver.core import PROFILE, evaluate_resolution_candidate
from hashing import compute_spec_hash
from policy_runtime.core import serving_gate
from .core import validate_snapshot


def negative(reason: str, *, now: str, outcome="ABSTAIN") -> dict:
    envelope = {"id": "water:" + reason.lower(), "version": "kfm-water-v1", "issued_at": now,
                "outcome": outcome, "reason_code": reason, "evidence_refs": [],
                "policy_state": "withheld", "freshness": "unknown", "correction_state": "unknown"}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    return {"envelope": envelope}


def project(raw: bytes, decision: dict | None, *, view: str, now: str, station_id: str | None = None) -> dict:
    manifest, values = validate_snapshot(raw)
    candidate, evidence = values["candidate.json"], values["evidence.json"]
    reason = serving_gate(manifest, evidence, decision, now=now)
    if reason != "ELIGIBLE":
        return negative(reason, now=now)
    if view not in {"bootstrap", "layers", "evidence"}:
        return negative("ROUTE_NOT_FOUND", now=now)
    assert decision is not None
    selected = [entry for entry in evidence["entries"] if station_id is None or entry["station_id"] == station_id]
    if not selected:
        return negative("EVIDENCE_NOT_FOUND", now=now)
    # Every read replays verification and checks bundle membership and identity.
    second = utc_time(now).strftime("%Y-%m-%dT%H:%M:%SZ")
    for entry in selected:
        bundle = entry["bundle"]
        if bundle["spec_hash"]["value"] != compute_spec_hash({k: v for k, v in bundle.items() if k != "spec_hash"}):
            return negative("EVIDENCE_DIGEST_MISMATCH", now=now, outcome="ERROR")
        resolution = evaluate_resolution_candidate({
            "profile": PROFILE, "evidence_ref": entry["evidence_ref"], "bundle_candidate": bundle,
            "lookup_context": {"bundle_id": bundle["bundle_id"], "current_head": True,
                               "policy_outcome": "ANSWER", "policy_decision_ref": decision["policy_ref"],
                               "correction_state": "ACTIVE", "correction_ref": None},
            "verification_history": entry["verification_history"],
            "verification_as_of": {"effective_as_of": second, "recorded_as_of": second}})
        if resolution.status != "RESOLVED":
            return negative("EVIDENCE_UNRESOLVED", now=now)
    refs = [entry["evidence_ref"] for entry in selected]
    observations = [r for r in candidate["observations"] if r["station_id"] in {e["station_id"] for e in selected}]
    latest = max((utc_time(r["observed_at"]) for r in observations), default=None)
    freshness = "unknown" if latest is None else "stale-accepted" if (utc_time(now) - latest).total_seconds() > candidate["stale_after_seconds"] else "current"
    precision = {"spatial": {"representation": "point", "resolution": "Provider station coordinates, EPSG:4326", "accuracy": "See station horizontal accuracy metadata; no inferred positional accuracy", "generalization_applied": False},
                 "temporal": {"granularity": "Provider observation instants", "observation_interval": {"start": manifest["start"], "end": manifest["end"]}, "freshness_class": freshness},
                 "attribute": {"measure": "Discharge", "unit": "ft^3/s", "significant_precision": 0, "classification_granularity": "Provider-reported values; no additional significant-figure guarantee"},
                 "evidence_refs": refs, "transform_receipt_refs": ["kfm://receipt/validation/" + values["validation.json"]["receipt_digest"].split(":")[1]]}
    envelope = {"id": "water:" + view, "version": "kfm-water-v1", "issued_at": now, "outcome": "ANSWER",
                "reason_code": "RELEASED_SNAPSHOT", "evidence_refs": refs, "policy_state": "approved_snapshot",
                "freshness": freshness, "correction_state": "ACTIVE", "precision_actually_used": precision}
    envelope["spec_hash"] = compute_spec_hash(envelope)
    common = {"package_id": manifest["package_id"], "source_id": "usgs-nwis", "coverage": candidate["coverage"],
              "retrieved_at": candidate["retrieved_at"], "reviewed_at": decision["reviewed_at"], "released_at": decision["released_at"], "approval_expires_at": decision["expires_at"],
              "stale_after_seconds": candidate["stale_after_seconds"], "correction_state": "ACTIVE",
              "attribution": "U.S. Geological Survey. Provisional observations are subject to revision."}
    if view == "bootstrap":
        data = {**common, "layers": [{"id": "usgs-water-pilot", "title": "Reviewed USGS discharge snapshot", "evidence_eligible": True}], "observation_count": len(observations)}
    elif view == "layers":
        data = {**common, "stations": [s for s in candidate["stations"] if s["id"] in {e["station_id"] for e in selected}], "observations": observations}
    else:
        data = {**common, "entries": [{k: e[k] for k in ("station_id", "evidence_ref", "bundle", "verification_history")} for e in selected]}
    return {"envelope": envelope, "data": data}
