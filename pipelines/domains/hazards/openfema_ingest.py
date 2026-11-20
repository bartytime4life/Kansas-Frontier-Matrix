"""Bounded supplied OpenFEMA declarations walk; administrative context, never writes.

No fetching, provider snapshot/completeness claim, hazard footprint, eligibility
determination or source admission. Source bodies and titles stay private.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker
from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, timestamp, utc_time
from connectors.fema.src.fema import openfema_declarations as of
from tools.local_data.file_io import read_regular

ROOT = Path(__file__).resolve().parents[3]
MAX_ENVELOPE = 2 * 1024 * 1024
MAX_PAGE = 256 * 1024
MAX_CAPTURE = 1024 * 1024
MAX_OUTPUT = 8 * 1024 * 1024
MAX_PAGES = 16
MAX_TOP = 64
MAX_RECORDS = 256
MAX_REPORTED = 1_000_000
SCHEMA = "schemas/contracts/v1/domains/hazards/openfema_ingest_candidate.schema.json"
DESCRIPTOR = "data/registry/hazards/sources/fema_disaster_declarations.yaml"
FIXTURE_ROOT = ROOT / "fixtures/domains/hazards/openfema_ingest"
BASE_REASONS = ("SOURCE_ADMISSION_UNVERIFIED", "SOURCE_DESCRIPTOR_UNRESOLVED",
                "RIGHTS_UNVERIFIED", "SENSITIVITY_NOT_EVALUATED")
AUTHORITIES = ("source_admitted", "review_completed", "evidence_closed", "lifecycle_write",
               "promotion_authorized", "release_authorized", "publication_authorized", "public_use_allowed",
               "eligibility_determination_authorized", "life_safety_authority")


def spec_hash(c: dict) -> str:
    return digest_bytes(canonical_bytes({k: v for k, v in c.items() if k != "spec_hash"}))


def _build(pages: list) -> dict:
    if not isinstance(pages, list) or not 1 <= len(pages) <= MAX_PAGES:
        raise ValueError("FEMA_PAGE_COUNT_BOUND")
    parsed, supplied, seen, total_bytes, total_records = [], {}, set(), 0, 0
    for p in pages:
        if (not isinstance(p, dict) or set(p) != {"source_url", "status", "retrieved_at", "body"}
                or type(p["status"]) is not int or p["status"] != 200 or not isinstance(p["body"], str)):
            raise ValueError("FEMA_PAGE_ENVELOPE_INVALID")
        raw = p["body"].encode()
        total_bytes += len(raw)
        if total_bytes > MAX_CAPTURE:
            raise ValueError("FEMA_CAPTURE_BYTE_BOUND")
        payload = decode_object(raw, limit=MAX_PAGE)
        if of._exceeds_nesting(payload, of.MAX_NESTING):
            raise ValueError("FEMA_PAGE_NESTING_BOUND")
        retrieved = timestamp(utc_time(p["retrieved_at"]))
        page = of.parse_page(raw, status=200, source_url=p["source_url"], retrieved_at=retrieved,
                             max_bytes=MAX_PAGE)
        if (page.request.top > MAX_TOP or page.reported_count > MAX_REPORTED
                or of.page_url(page.request.base_filter, after_id=page.request.after_id,
                               top=page.request.top) != p["source_url"]):
            raise ValueError("FEMA_QUERY_PROFILE_BOUND")
        if page.source_url in seen:
            raise ValueError("FEMA_DUPLICATE_PAGE_REQUEST")
        seen.add(page.source_url)
        total_records += len(page.records)
        if total_records > MAX_RECORDS:
            raise ValueError("FEMA_RECORD_COUNT_BOUND")
        if ((page.run_date is not None and utc_time(page.run_date) > utc_time(retrieved))
                or any(utc_time(r.last_refresh) > utc_time(retrieved)
                       or utc_time(r.declaration_date) > utc_time(retrieved) for r in page.records)):
            raise ValueError("FEMA_SOURCE_TIME_AFTER_CAPTURE")
        parsed.append(page)
        supplied[page.source_url] = {"source_url": page.source_url, "retrieved_at": retrieved,
            "body": p["body"], "body_sha256": digest_bytes(raw), "byte_length": len(raw)}
    parsed.sort(key=lambda p: p.request.after_id or "")
    if any(utc_time(a.retrieved_at) > utc_time(b.retrieved_at) for a, b in zip(parsed, parsed[1:])):
        raise ValueError("FEMA_CAPTURE_TIME_ORDER")
    result = of.reconcile(parsed)
    snapshots = [supplied[p.source_url] for p in parsed]
    capture = decode_object(canonical_bytes(asdict(result)), limit=MAX_OUTPUT)
    reasons = list(BASE_REASONS) + list(result.reasons)
    if any(r.route == "QUARANTINE_CANDIDATE" for r in result.records):
        reasons.append("RECORD_QUARANTINE_CANDIDATES")
    c = {"object_type": "OpenFemaDeclarationsIngestCandidate", "schema_version": "1.0.0",
        "source_descriptor_ref": DESCRIPTOR, "source_role": "administrative",
        "query": {"base_filter": parsed[0].request.base_filter, "top": parsed[0].request.top},
        "pages": snapshots, "capture": capture, "route": "HOLD", "reason_codes": reasons,
        "authority": {k: False for k in AUTHORITIES}}
    artifacts = [{k: p[k] for k in ("source_url", "body_sha256", "byte_length")} for p in snapshots]
    c["candidate_id"] = "openfema-ingest:" + digest_bytes(canonical_bytes(artifacts))
    c["spec_hash"] = spec_hash(c)
    if len(canonical_bytes(c)) > MAX_OUTPUT:
        raise ValueError("FEMA_OUTPUT_BYTE_BOUND")
    return c


def validate_candidate(c: dict) -> None:
    schema = json.loads((ROOT / SCHEMA).read_text())
    if not Draft202012Validator(schema, format_checker=FormatChecker()).is_valid(c):
        raise ValueError("FEMA_CANDIDATE_SCHEMA_INVALID")
    expected = _build([{k: p[k] for k in ("source_url", "retrieved_at", "body")} | {"status": 200}
                       for p in c["pages"]])
    if canonical_bytes(c) != canonical_bytes(expected):
        raise ValueError("FEMA_CANDIDATE_REPLAY_MISMATCH")


@dataclass(frozen=True)
class IntakeResult:
    candidate: dict = field(repr=False)

    def summary(self) -> dict:
        validate_candidate(self.candidate)
        c, records = self.candidate, self.candidate["capture"]["records"]
        return {"outcome": "HOLD", "capture_outcome": c["capture"]["outcome"],
                "page_count": len(c["pages"]), "record_count": len(records),
                "reported_count": c["capture"]["reported_count"],
                "quarantined": sum(r["route"] == "QUARANTINE_CANDIDATE" for r in records),
                "flagged": sum(bool(r["reasons"]) for r in records),
                "reason_codes": c["reason_codes"], "result_digest": c["spec_hash"], **c["authority"]}


def prepare_capture(raw: bytes) -> IntakeResult:
    """Reconcile supplied counted keyset pages; final HOLD never admits a source.

    Input order is immaterial; cursor order and per-page capture times are
    preserved. A short terminal page is required even for exact multiples.
    CAPTURE_CANDIDATE means an internally consistent reported walk, not a stable
    provider snapshot, world coverage, absence of hazards or aid eligibility.
    """
    envelope = decode_object(raw, limit=MAX_ENVELOPE)
    if set(envelope) != {"pages"}:
        raise ValueError("FEMA_CAPTURE_ENVELOPE_INVALID")
    c = _build(envelope["pages"])
    validate_candidate(c)
    return IntakeResult(c)


def replay_packet(raw: bytes) -> IntakeResult:
    p = decode_object(raw, limit=MAX_OUTPUT)
    if (set(p) != {"fixture_kind", "capture", "capture_sha256", "expected"}
            or p["fixture_kind"] != "SYNTHETIC_OPENFEMA_DECLARATIONS" or not isinstance(p["capture"], str)):
        raise ValueError("FEMA_PACKET_SHAPE")
    capture = p["capture"].encode()
    if digest_bytes(capture) != p["capture_sha256"]:
        raise ValueError("FEMA_PACKET_HASH")
    result = prepare_capture(capture)
    if canonical_bytes(result.candidate) != canonical_bytes(p["expected"]):
        raise ValueError("FEMA_PACKET_GOLDEN_MISMATCH")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", choices=("complete", "count-drift", "empty"))
    args = parser.parse_args(argv)
    try:
        result = replay_packet(read_regular(FIXTURE_ROOT / (args.fixture + ".json"), MAX_OUTPUT))
    except (ValueError, OSError):
        print(canonical_bytes({"outcome": "ERROR", "reason": "FEMA_FIXTURE_REPLAY_FAILED"}).decode(), file=sys.stderr)
        return 1
    print(canonical_bytes(result.summary()).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
