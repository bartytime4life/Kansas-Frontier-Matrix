"""Build deterministic fixture-only TemporalQueryDisclosure candidates."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import datetime, timedelta, timezone
from typing import Sequence

PROFILE = "kfm.governance.temporal-query-disclosure.v1"
EXPLANATION_CODES = {
    "CURRENT_STATE": "CURRENT_STATE_AT_EVALUATION",
    "PRIOR_STATE": "PRIOR_VALID_STATE_AS_OF",
    "SEQUENCED": "VALID_TIME_SEQUENCE",
    "NONSEQUENCED": "TRANSACTION_HISTORY_SEQUENCE",
    "TRACKING_LOG": "TRACKING_LOG_HISTORY",
}
PERMISSIONS = {
    "execute_query": False,
    "resolve_evidence": False,
    "evaluate_policy": False,
    "create_review": False,
    "promote": False,
    "release": False,
    "deploy": False,
    "publish": False,
    "public_use": False,
}
NON_EFFECTS = [
    "does_not_execute_or_rewrite_a_query",
    "does_not_resolve_evidence_or_admit_sources",
    "does_not_create_policy_review_release_or_publication_authority",
    "does_not_replace_query_run_record_or_domain_temporal_contracts",
    "does_not_claim_snapshot_refs_are_released_or_public_safe",
]


def canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


def utc_second(value: str | None) -> str | None:
    if value is None:
        return None
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0) or parsed.microsecond:
        raise ValueError("timestamps must use UTC second precision")
    return parsed.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def payload_without_identity(value: dict[str, object]) -> dict[str, object]:
    payload = copy.deepcopy(value)
    payload.pop("disclosure_id", None)
    payload.pop("spec_hash", None)
    return payload


def compute_spec_hash(value: dict[str, object]) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(payload_without_identity(value))).hexdigest()


def compute_disclosure_id(value: dict[str, object]) -> str:
    candidate = copy.deepcopy(value)
    candidate.pop("disclosure_id", None)
    return "kfm:temporal-query-disclosure:" + hashlib.sha256(canonical_json(candidate)).hexdigest()


def build_disclosure(
    *,
    query_run_ref: str,
    temporal_query_type: str,
    time_basis: str,
    evaluated_at: str,
    requested_as_of: str | None,
    valid_start: str | None,
    valid_end: str | None,
    transaction_cutoff: str | None,
    snapshot_refs: Sequence[str],
    evidence_refs: Sequence[str],
) -> dict[str, object]:
    valid_interval: object = None
    if valid_start is not None or valid_end is not None:
        valid_interval = {"start": utc_second(valid_start), "end": utc_second(valid_end)}
    value: dict[str, object] = {
        "schema_version": "1.0.0",
        "profile": PROFILE,
        "profile_status": "PROPOSED_INACTIVE",
        "execution_mode": "FIXTURE_ONLY_NO_EXTERNAL_EFFECT",
        "authority": "NONE",
        "query_run_ref": query_run_ref,
        "temporal_query_type": temporal_query_type,
        "time_basis": time_basis,
        "evaluated_at": utc_second(evaluated_at),
        "requested_as_of": utc_second(requested_as_of),
        "valid_interval": valid_interval,
        "transaction_cutoff": utc_second(transaction_cutoff),
        "snapshot_refs": sorted(set(snapshot_refs)),
        "evidence_refs": sorted(set(evidence_refs)),
        "public_explanation_code": EXPLANATION_CODES[temporal_query_type],
        "permissions": dict(PERMISSIONS),
        "non_effects": list(NON_EFFECTS),
    }
    value["spec_hash"] = compute_spec_hash(value)
    value["disclosure_id"] = compute_disclosure_id(value)
    return value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query-run-ref", required=True)
    parser.add_argument("--temporal-query-type", choices=sorted(EXPLANATION_CODES), required=True)
    parser.add_argument("--time-basis", choices=["VALID_TIME", "TRANSACTION_TIME", "BITEMPORAL", "RELEASE_TIME"], required=True)
    parser.add_argument("--evaluated-at", required=True)
    parser.add_argument("--requested-as-of")
    parser.add_argument("--valid-start")
    parser.add_argument("--valid-end")
    parser.add_argument("--transaction-cutoff")
    parser.add_argument("--snapshot-ref", action="append", required=True)
    parser.add_argument("--evidence-ref", action="append", required=True)
    args = parser.parse_args(argv)
    value = build_disclosure(
        query_run_ref=args.query_run_ref,
        temporal_query_type=args.temporal_query_type,
        time_basis=args.time_basis,
        evaluated_at=args.evaluated_at,
        requested_as_of=args.requested_as_of,
        valid_start=args.valid_start,
        valid_end=args.valid_end,
        transaction_cutoff=args.transaction_cutoff,
        snapshot_refs=args.snapshot_ref,
        evidence_refs=args.evidence_ref,
    )
    print(json.dumps(value, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
