"""Supplied NWS context capture rehearsal; never alerts, polls or writes.

Messages and instructions remain source-authored private context. Freshness is
computed at an explicit instant, never labeled current or used as KFM advice.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker
from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, timestamp, utc_time
from connectors.noaa.src.noaa import nws_alerts as nws
from tools.local_data.file_io import read_regular

ROOT = Path(__file__).resolve().parents[3]
MAX_SOURCE = 256 * 1024
MAX_PACKET = 4 * 1024 * 1024
MAX_FEATURES = 64
URL = "https://api.weather.gov/alerts/active?area=KS"
SCHEMA = "schemas/contracts/v1/domains/hazards/nws_context_ingest_candidate.schema.json"
DESCRIPTOR = "data/registry/atmosphere/sources/noaa_nws.yaml"
FIXTURE_ROOT = ROOT / "fixtures/domains/hazards/nws_context_ingest"
AUTHORITIES = ("source_admitted", "review_completed", "evidence_closed", "lifecycle_write",
               "promotion_authorized", "release_authorized", "publication_authorized", "public_use_allowed",
               "life_safety_authority", "alert_delivery_authorized")
BASE_REASONS = ("SOURCE_ADMISSION_UNVERIFIED", "SOURCE_DESCRIPTOR_UNRESOLVED",
                "RIGHTS_UNVERIFIED", "SENSITIVITY_NOT_EVALUATED")


def spec_hash(candidate: dict) -> str:
    return digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "spec_hash"}))


def _identity(c: dict) -> str:
    return "nws-context-ingest:" + digest_bytes(canonical_bytes({
        "source_url": c["context"]["source_url"], "artifact": c["artifact"]}))


def validate_candidate(c: dict) -> None:
    schema = json.loads((ROOT / SCHEMA).read_text())
    if not Draft202012Validator(schema, format_checker=FormatChecker()).is_valid(c):
        raise ValueError("NWS_CONTEXT_SCHEMA_INVALID")
    if spec_hash(c) != c["spec_hash"] or _identity(c) != c["candidate_id"]:
        raise ValueError("NWS_CONTEXT_HASH_INVALID")
    context, alerts = c["context"], c["context"]["alerts"]
    retrieved, at = utc_time(context["retrieved_at"]), utc_time(c["evaluated_at"])
    if (at < retrieved or timestamp(at) != c["evaluated_at"]
            or timestamp(retrieved) != context["retrieved_at"]
            or context["body_sha256"] != c["artifact"]["sha256"]
            or len({a["alert_id"] for a in alerts}) != len(alerts)):
        raise ValueError("NWS_CONTEXT_CAPTURE_INCONSISTENT")
    # Recompute the parser projection from its private source-faithful feature
    # snapshots. A new hash alone cannot bless rewritten freshness or lineage.
    features = []
    for alert in alerts:
        raw = alert["raw_feature_json"].encode()
        if digest_bytes(raw) != alert["feature_sha256"] or utc_time(alert["sent"]) > retrieved:
            raise ValueError("NWS_CONTEXT_FEATURE_INCONSISTENT")
        features.append(decode_object(raw, limit=MAX_PACKET))
    body = {"type": "FeatureCollection", "features": features}
    if context["outcome"] == "INCOMPLETE_CAPTURE":
        body["pagination"] = {"next": "unresolved-next-page"}
    replay = nws.parse_alerts(canonical_bytes(body), status=200, source_url=URL,
        retrieved_at=context["retrieved_at"], as_of=c["evaluated_at"], max_bytes=MAX_PACKET,
        max_features=MAX_FEATURES)
    expected = decode_object(canonical_bytes(asdict(replay)), limit=MAX_PACKET)
    expected["body_sha256"] = context["body_sha256"]  # exact original capture differs from canonical replay.
    if context != expected:
        raise ValueError("NWS_CONTEXT_PROJECTION_INCONSISTENT")
    reasons = list(BASE_REASONS) + context["reasons"]
    if any(a["route"] == "QUARANTINE_CANDIDATE" for a in alerts):
        reasons.append("MESSAGE_QUARANTINE_CANDIDATES")
    if c["reason_codes"] != reasons:
        raise ValueError("NWS_CONTEXT_REASONS_INCONSISTENT")


@dataclass(frozen=True)
class IntakeResult:
    candidate: dict = field(repr=False)

    def summary(self) -> dict:
        validate_candidate(self.candidate)
        c, alerts = self.candidate, self.candidate["context"]["alerts"]
        states = sorted({a["freshness_state"] for a in alerts})
        return {"outcome": "HOLD", "capture_outcome": c["context"]["outcome"],
                "message_count": len(alerts),
                "quarantined": sum(a["route"] == "QUARANTINE_CANDIDATE" for a in alerts),
                "freshness_counts": {s: sum(a["freshness_state"] == s for a in alerts) for s in states},
                "reason_codes": c["reason_codes"], "result_digest": c["spec_hash"], **c["authority"]}


def prepare_capture(raw: bytes, *, retrieved_at: str, as_of: str, status: int = 200) -> IntakeResult:
    """Prepare a private held candidate from one supplied 200 KS collection.

    Empty collections are not evidence of no hazards. Partial captures remain
    explicitly incomplete; no next-page URL is followed. HTTP non-200 responses
    are refused, including unbound 304s, rather than minting missing captures.
    """
    if type(status) is not int or status != 200:
        raise ValueError("NWS_CONTEXT_HTTP_STATUS")
    payload = decode_object(raw, limit=MAX_SOURCE)  # duplicate keys and all nonfinite numbers are refused.
    # Reject deep structures before the source parser, retaining its 32-level rule.
    if nws._exceeds_nesting(payload, nws.MAX_NESTING):
        raise ValueError("NWS_CONTEXT_NESTING_BOUND")
    retrieved_at, as_of = timestamp(utc_time(retrieved_at)), timestamp(utc_time(as_of))
    context = nws.parse_alerts(raw, status=status, source_url=URL, retrieved_at=retrieved_at,
                               as_of=as_of, max_bytes=MAX_SOURCE, max_features=MAX_FEATURES)
    context = decode_object(canonical_bytes(asdict(context)), limit=MAX_PACKET)
    reasons = list(BASE_REASONS) + context["reasons"]
    if any(a["route"] == "QUARANTINE_CANDIDATE" for a in context["alerts"]):
        reasons.append("MESSAGE_QUARANTINE_CANDIDATES")
    c = {"object_type": "NwsContextIngestCandidate", "schema_version": "1.0.0",
         "source_descriptor_ref": DESCRIPTOR, "source_role": "regulatory",
         "artifact": {"sha256": digest_bytes(raw), "byte_length": len(raw)},
         "evaluated_at": as_of, "context": context, "route": "HOLD", "reason_codes": reasons,
         "authority": {key: False for key in AUTHORITIES}}
    c["candidate_id"] = _identity(c)
    c["spec_hash"] = spec_hash(c)
    if len(canonical_bytes(c)) > MAX_PACKET:
        raise ValueError("NWS_CONTEXT_OUTPUT_BOUND")
    validate_candidate(c)
    return IntakeResult(c)


def replay_packet(raw: bytes) -> IntakeResult:
    p = decode_object(raw, limit=MAX_PACKET)
    if (set(p) != {"fixture_kind", "body", "body_sha256", "retrieved_at", "as_of", "expected"}
            or p["fixture_kind"] != "SYNTHETIC_NWS_CONTEXT" or not isinstance(p["body"], str)):
        raise ValueError("NWS_CONTEXT_PACKET_SHAPE")
    body = p["body"].encode()
    if digest_bytes(body) != p["body_sha256"]:
        raise ValueError("NWS_CONTEXT_PACKET_HASH")
    result = prepare_capture(body, retrieved_at=p["retrieved_at"], as_of=p["as_of"])
    if canonical_bytes(result.candidate) != canonical_bytes(p["expected"]):
        raise ValueError("NWS_CONTEXT_GOLDEN_MISMATCH")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", choices=("lineage", "expired-partial", "empty"))
    args = parser.parse_args(argv)
    try:
        result = replay_packet(read_regular(FIXTURE_ROOT / (args.fixture + ".json"), MAX_PACKET))
    except (ValueError, OSError):
        print(canonical_bytes({"outcome": "ERROR", "reason": "NWS_CONTEXT_REPLAY_FAILED"}).decode(), file=sys.stderr)
        return 1
    print(canonical_bytes(result.summary()).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
