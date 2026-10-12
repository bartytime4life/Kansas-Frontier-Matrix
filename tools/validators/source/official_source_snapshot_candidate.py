#!/usr/bin/env python3
"""Build and validate immutable official-source snapshot candidates without network access."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/official_source_snapshot_candidate.schema.json"


def _dt(value: str | None) -> datetime | None:
    return None if value is None else datetime.fromisoformat(value.replace("Z", "+00:00"))


def _snapshot_id(source_id: str, source_url: str, retrieved_at: str, content_sha256: str | None) -> str:
    identity = {
        "content_sha256": content_sha256,
        "retrieved_at": retrieved_at,
        "source_id": source_id,
        "source_url": source_url,
    }
    encoded = json.dumps(identity, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "kfm:source-snapshot:" + hashlib.sha256(encoded).hexdigest()


def build_captured_candidate(
    payload_path: Path,
    *,
    source_id: str,
    source_url: str,
    retrieved_at: str,
    http_status: int = 200,
    media_type: str | None = "application/octet-stream",
    etag: str | None = None,
    last_modified: str | None = None,
) -> dict[str, object]:
    """Build a candidate from local bytes only; this function performs no network access."""
    payload = payload_path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    candidate: dict[str, object] = {
        "snapshot_id": _snapshot_id(source_id, source_url, retrieved_at, digest),
        "source_id": source_id,
        "source_url": source_url,
        "retrieved_at": retrieved_at,
        "http_status": http_status,
        "media_type": media_type,
        "etag": etag,
        "last_modified": last_modified,
        "retrieval_outcome": "CAPTURED",
        "content_sha256": digest,
        "content_length": len(payload),
        "source_activation_authorized": False,
        "evidence_bundle_emitted": False,
        "public_use_allowed": False,
    }
    return candidate


def validate_doc(doc: dict[str, object]) -> list[str]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = [
        error.message
        for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(doc)
    ]
    if errors:
        return errors

    outcome = doc["retrieval_outcome"]
    status = int(doc["http_status"])
    digest = doc["content_sha256"]
    length = doc["content_length"]

    if outcome == "CAPTURED":
        if not 200 <= status <= 299:
            errors.append("CAPTURED requires a 2xx HTTP status")
        if digest is None or length is None or int(length) <= 0:
            errors.append("CAPTURED requires non-empty digest-bound bytes")
    elif outcome == "NOT_MODIFIED":
        if status != 304:
            errors.append("NOT_MODIFIED requires HTTP 304")
        if digest is not None or length not in (None, 0):
            errors.append("NOT_MODIFIED cannot claim captured bytes")
    elif outcome == "FAILED" and (digest is not None or length not in (None, 0)):
        errors.append("FAILED cannot claim captured bytes")

    last_modified = _dt(doc.get("last_modified"))
    retrieved_at = _dt(str(doc["retrieved_at"]))
    if last_modified and retrieved_at and last_modified > retrieved_at:
        errors.append("last_modified cannot be later than retrieved_at")

    expected_id = _snapshot_id(
        str(doc["source_id"]),
        str(doc["source_url"]),
        str(doc["retrieved_at"]),
        digest if isinstance(digest, str) else None,
    )
    if doc["snapshot_id"] != expected_id:
        errors.append("snapshot_id does not match deterministic identity")

    if doc["source_activation_authorized"] or doc["evidence_bundle_emitted"] or doc["public_use_allowed"]:
        errors.append("snapshot candidate cannot create source, evidence, or public authority")
    return errors


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("payload", type=Path)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--retrieved-at", required=True)
    parser.add_argument("--http-status", type=int, default=200)
    parser.add_argument("--media-type", default="application/octet-stream")
    parser.add_argument("--etag")
    parser.add_argument("--last-modified")
    return parser


def main() -> int:
    args = _parser().parse_args()
    candidate = build_captured_candidate(
        args.payload,
        source_id=args.source_id,
        source_url=args.source_url,
        retrieved_at=args.retrieved_at,
        http_status=args.http_status,
        media_type=args.media_type,
        etag=args.etag,
        last_modified=args.last_modified,
    )
    errors = validate_doc(candidate)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(json.dumps(candidate, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
