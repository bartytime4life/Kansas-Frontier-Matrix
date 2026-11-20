"""Private supplied iNaturalist plant-query intake; no fetching, writing or admission.

Minimized snapshots support internal replay. Original body digests require the
original supplied capture for byte verification; minimization is not redaction.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, field, replace
from datetime import date
import json
from pathlib import Path
import re
import sys

from jsonschema import Draft202012Validator, FormatChecker
from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, timestamp, utc_time
from connectors.inaturalist.src.inaturalist import observations_api as obs
from tools.local_data.file_io import read_regular

ROOT = Path(__file__).resolve().parents[3]
MAX_ENVELOPE = 2 * 1024 * 1024
MAX_PAGE = 256 * 1024
MAX_CAPTURE = 1024 * 1024
MAX_OUTPUT = 8 * 1024 * 1024
MAX_PAGES, MAX_PER_PAGE, MAX_RECORDS, MAX_REPORTED = 16, 64, 256, 1_000_000
PLANT_TAXON = 47126
QUERY = obs.ObservationQuery(taxon_id=PLANT_TAXON)
SCHEMA = "schemas/contracts/v1/domains/flora/inaturalist_ingest_candidate.schema.json"
DESCRIPTOR = "data/registry/fauna/sources/inaturalist.yaml"
FIXTURE_ROOT = ROOT / "fixtures/domains/flora/inaturalist_ingest"
BASE_REASONS = ("SOURCE_ADMISSION_UNVERIFIED", "SOURCE_DESCRIPTOR_UNRESOLVED",
                "CROSS_DOMAIN_USE_UNREVIEWED", "RIGHTS_UNVERIFIED", "SENSITIVITY_NOT_EVALUATED")
AUTHORITIES = ("source_admitted", "review_completed", "evidence_closed", "lifecycle_write",
               "promotion_authorized", "release_authorized", "publication_authorized", "public_use_allowed",
               "taxonomy_authority", "geoprivacy_transform_authorized")


def spec_hash(c: dict) -> str:
    return digest_bytes(canonical_bytes({k: v for k, v in c.items() if k != "spec_hash"}))


def _check_users(value: object) -> None:
    # The source parser minimizes nested user dictionaries. Reject unexpected
    # scalar/container users or non-scalar id/login rather than returning them.
    if isinstance(value, list):
        for child in value:
            _check_users(child)
    elif isinstance(value, dict):
        for key, child in value.items():
            if key == "user" and child is not None:
                if not isinstance(child, dict) or set(child) - {"id", "login"}:
                    raise ValueError("INAT_MINIMIZED_USER_SHAPE")
                uid, login = child.get("id"), child.get("login")
                if ((uid is not None and (type(uid) is not int or not 1 <= uid <= 2**53))
                        or (login is not None and (not isinstance(login, str) or not 0 < len(login) <= 128))):
                    raise ValueError("INAT_MINIMIZED_USER_SHAPE")
            else:
                _check_users(child)


def _record_check(record: obs.ObservationCandidate, retrieved: str) -> dict:
    raw = json.loads(record.raw_record_json)
    _check_users(raw)
    taxon = raw.get("taxon") or {}
    ancestors = taxon.get("ancestor_ids")
    if ancestors is not None and (not isinstance(ancestors, list) or len(ancestors) > 64
            or any(type(i) is not int or not 1 <= i <= 2**53 for i in ancestors)):
        raise ValueError("INAT_ANCESTRY_SHAPE")
    lineage = record.taxon_id == PLANT_TAXON or PLANT_TAXON in (ancestors or [])
    if record.updated_at is not None and utc_time(record.updated_at) > utc_time(retrieved):
        raise ValueError("INAT_SOURCE_TIME_AFTER_CAPTURE")
    if record.observed_on is not None:
        try:
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", record.observed_on):
                raise ValueError
            observed = date.fromisoformat(record.observed_on)
        except ValueError:
            raise ValueError("INAT_OBSERVED_DATE") from None
        if observed > utc_time(retrieved).date():
            raise ValueError("INAT_SOURCE_TIME_AFTER_CAPTURE")
    return {"observation_id": record.observation_id,
            "flora_scope": "SOURCE_PLANT_LINEAGE" if lineage else "UNVERIFIED",
            "route": record.route if lineage else "QUARANTINE_CANDIDATE",
            "reason_codes": [] if lineage else ["FLORA_LINEAGE_UNVERIFIED"]}


def _assemble(parsed: list, snapshots: list) -> dict:
    ordered = sorted(zip(parsed, snapshots), key=lambda pair: pair[0].id_above)
    parsed, snapshots = map(list, zip(*ordered))
    if any(utc_time(a.retrieved_at) > utc_time(b.retrieved_at) for a, b in zip(parsed, parsed[1:])):
        raise ValueError("INAT_CAPTURE_TIME_ORDER")
    result = obs.reconcile(parsed)
    checks = [_record_check(r, p.retrieved_at) for p in parsed for r in p.records]
    ids = [r.observation_id for r in result.records]
    if len(set(ids)) != len(ids):
        raise ValueError("INAT_DUPLICATE_OBSERVATION")
    reasons = list(BASE_REASONS) + list(result.reasons)
    if any(r["route"] == "QUARANTINE_CANDIDATE" for r in checks):
        reasons.append("RECORD_QUARANTINE_CANDIDATES")
    c = {"object_type": "INaturalistFloraIngestCandidate", "schema_version": "1.0.0",
        "source_descriptor_ref": DESCRIPTOR,
        "query": {"taxon_id": PLANT_TAXON, "bounds": list(obs.KANSAS_CONTEXT),
                  "per_page": parsed[0].per_page},
        "pages": snapshots, "capture": json.loads(canonical_bytes(asdict(result))),
        "flora_checks": checks, "route": "HOLD", "reason_codes": reasons,
        "authority": {k: False for k in AUTHORITIES}}
    identity = [{k: p[k] for k in ("source_url", "source_body_sha256", "source_byte_length")} for p in snapshots]
    c["candidate_id"] = "inaturalist-ingest:" + digest_bytes(canonical_bytes(identity))
    c["spec_hash"] = spec_hash(c)
    if len(canonical_bytes(c)) > MAX_OUTPUT:
        raise ValueError("INAT_OUTPUT_BYTE_BOUND")
    return c


def _profile_page(body: bytes, url: str, retrieved: str):
    if timestamp(utc_time(retrieved)) != retrieved:
        raise ValueError("INAT_CANONICAL_CAPTURE_TIME")
    payload = decode_object(body, limit=MAX_PAGE)
    if obs._exceeds_nesting(payload, 32):
        raise ValueError("INAT_PAGE_NESTING_BOUND")
    page = obs.parse_page(body, status=200, source_url=url, retrieved_at=retrieved, max_bytes=MAX_PAGE)
    if (page.per_page > MAX_PER_PAGE or page.total_results > MAX_REPORTED
            or obs.page_url(QUERY, id_above=page.id_above, per_page=page.per_page) != url):
        raise ValueError("INAT_QUERY_PROFILE_BOUND")
    return page


def _build(envelope: dict) -> dict:
    if set(envelope) != {"pages"}:
        raise ValueError("INAT_CAPTURE_ENVELOPE_INVALID")
    pages = envelope["pages"]
    if not isinstance(pages, list) or not 1 <= len(pages) <= MAX_PAGES:
        raise ValueError("INAT_PAGE_COUNT_BOUND")
    parsed, snapshots, seen, total_bytes, total_records = [], [], set(), 0, 0
    for p in pages:
        if (not isinstance(p, dict) or set(p) != {"source_url", "status", "retrieved_at", "body"}
                or type(p["status"]) is not int or p["status"] != 200 or not isinstance(p["body"], str)):
            raise ValueError("INAT_PAGE_ENVELOPE_INVALID")
        raw = p["body"].encode()
        total_bytes += len(raw)
        if total_bytes > MAX_CAPTURE:
            raise ValueError("INAT_CAPTURE_BYTE_BOUND")
        retrieved = timestamp(utc_time(p["retrieved_at"]))
        page = _profile_page(raw, p["source_url"], retrieved)
        if page.source_url in seen:
            raise ValueError("INAT_DUPLICATE_PAGE_REQUEST")
        seen.add(page.source_url)
        total_records += len(page.records)
        if total_records > MAX_RECORDS:
            raise ValueError("INAT_RECORD_COUNT_BOUND")
        # Drop top-level incidental fields and user profile fields before returning
        # any replay snapshot. Never mislabel these bytes as the original body.
        minimized = canonical_bytes({"total_results": page.total_results, "per_page": page.per_page,
                                     "results": [json.loads(r.raw_record_json) for r in page.records]})
        snapshots.append({"source_url": page.source_url, "retrieved_at": retrieved,
            "source_body_sha256": digest_bytes(raw), "source_byte_length": len(raw),
            "minimized_body": minimized.decode(), "minimized_body_sha256": digest_bytes(minimized),
            "minimized_byte_length": len(minimized)})
        parsed.append(page)
    return _assemble(parsed, snapshots)


def validate_candidate(c: dict, *, original_capture: bytes | None = None) -> None:
    """Check minimized replay; optionally also bind every original supplied byte.

    With no original capture, original digests are lineage assertions, not verified
    preimages. The minimized digest is always verified. Neither mode authenticates
    a provider, persistent availability, biological truth or source approval.
    """
    schema = json.loads((ROOT / SCHEMA).read_text())
    if not Draft202012Validator(schema, format_checker=FormatChecker()).is_valid(c):
        raise ValueError("INAT_CANDIDATE_SCHEMA_INVALID")
    parsed, total_bytes, total_records = [], 0, 0
    seen = set()
    for p in c["pages"]:
        raw = p["minimized_body"].encode()
        if digest_bytes(raw) != p["minimized_body_sha256"] or len(raw) != p["minimized_byte_length"]:
            raise ValueError("INAT_MINIMIZED_BODY_IDENTITY")
        page = _profile_page(raw, p["source_url"], p["retrieved_at"])
        expected_minimized = canonical_bytes({"total_results": page.total_results, "per_page": page.per_page,
            "results": [json.loads(r.raw_record_json) for r in page.records]})
        if raw != expected_minimized or page.source_url in seen:
            raise ValueError("INAT_MINIMIZED_REPLAY_SHAPE")
        seen.add(page.source_url)
        total_bytes += p["source_byte_length"]
        total_records += len(page.records)
        if total_bytes > MAX_CAPTURE or total_records > MAX_RECORDS:
            raise ValueError("INAT_REPLAY_BUDGET")
        parsed.append(replace(page, body_sha256=p["source_body_sha256"]))
    expected = _assemble(parsed, c["pages"])
    if canonical_bytes(c) != canonical_bytes(expected):
        raise ValueError("INAT_CANDIDATE_REPLAY_MISMATCH")
    if original_capture is not None:
        original = _build(decode_object(original_capture, limit=MAX_ENVELOPE))
        if canonical_bytes(c) != canonical_bytes(original):
            raise ValueError("INAT_ORIGINAL_CAPTURE_MISMATCH")


@dataclass(frozen=True)
class IntakeResult:
    candidate: dict = field(repr=False)

    def summary(self) -> dict:
        validate_candidate(self.candidate)
        c, checks = self.candidate, self.candidate["flora_checks"]
        return {"outcome": "HOLD", "capture_outcome": c["capture"]["outcome"],
                "page_count": len(c["pages"]), "record_count": len(checks),
                "reported_total": c["capture"]["reported_total"],
                "quarantined": sum(r["route"] == "QUARANTINE_CANDIDATE" for r in checks),
                "plant_lineage_unverified": sum(r["flora_scope"] == "UNVERIFIED" for r in checks),
                "reason_codes": c["reason_codes"], "result_digest": c["spec_hash"], **c["authority"]}


def prepare_capture(raw: bytes) -> IntakeResult:
    """Build a held candidate and verify original-byte binding before returning it."""
    c = _build(decode_object(raw, limit=MAX_ENVELOPE))
    validate_candidate(c, original_capture=raw)
    return IntakeResult(c)


def replay_packet(raw: bytes) -> IntakeResult:
    p = decode_object(raw, limit=MAX_OUTPUT)
    if (set(p) != {"fixture_kind", "capture", "capture_sha256", "expected"}
            or p["fixture_kind"] != "SYNTHETIC_INATURALIST_PLANT_QUERY" or not isinstance(p["capture"], str)):
        raise ValueError("INAT_PACKET_SHAPE")
    capture = p["capture"].encode()
    if digest_bytes(capture) != p["capture_sha256"]:
        raise ValueError("INAT_PACKET_HASH")
    result = prepare_capture(capture)
    if canonical_bytes(result.candidate) != canonical_bytes(p["expected"]):
        raise ValueError("INAT_PACKET_GOLDEN_MISMATCH")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", choices=("complete", "count-drift", "empty"))
    args = parser.parse_args(argv)
    try:
        result = replay_packet(read_regular(FIXTURE_ROOT / (args.fixture + ".json"), MAX_OUTPUT))
    except (ValueError, OSError):
        print(canonical_bytes({"outcome": "ERROR", "reason": "INAT_FIXTURE_REPLAY_FAILED"}).decode(), file=sys.stderr)
        return 1
    print(canonical_bytes(result.summary()).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
