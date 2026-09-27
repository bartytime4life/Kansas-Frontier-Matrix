"""Run one planner-issued USGS earthquake GET through the shared injected transport.

Transport effects (the HTTP client, clock, sleeper, jitter, cancellation) are supplied
by the caller and executed by ``connectors_core.transport.execute_retrieval``, which
owns redirect blocking, byte budgets, retries, media-type and digest checks. This
module adds only the USGS URL allowlist and transport profile, and maps the result
onto a ``SourceRetrievalEpisode``. It imports no network library. The episode
contract currently fixes ``execution_mode: FIXTURE_ONLY`` and
``network_attempted: false``, so only synthetic transports are in scope.

Requires ``packages/connectors-core/src`` on the import path (see pyproject.toml).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import re
from typing import Callable

from connectors_core import core as cc
from connectors_core import transport as ct

from . import earthquake

SOURCE_ID = "usgs.earthquake"
PROFILE_ID = "usgs-earthquake-geojson-v1"
RETRIEVAL_PROFILE = f"kfm:source-profile:{PROFILE_ID}"
MAX_BYTES = 8 * 1024 * 1024
MAX_ELAPSED_MS = 3_600_000
MEDIA_TYPES = frozenset({"application/json", "application/geo+json"})
ACCEPT = "application/geo+json, application/json"
SPEC_HASH = re.compile(r"sha256:[0-9a-f]{64}\Z")
# Mirrors the contract validator's recompute_result(); drift fails the conformance test.
RESULTS = {
    "SUCCESS": ("CAPTURED", "RETRIEVAL_BODY_CAPTURED"),
    "TIMEOUT": ("RETRY_REQUIRED", "RETRIEVAL_TIMEOUT"),
    "RATE_LIMITED": ("RETRY_REQUIRED", "SOURCE_RATE_LIMITED"),
    "RETRY_EXHAUSTED": ("RETRY_REQUIRED", "RETRY_BUDGET_EXHAUSTED"),
    "CANCELLED": ("RETRY_REQUIRED", "RETRIEVAL_CANCELLED"),
    "AUTH_REQUIRED": ("BLOCKED", "AUTH_REQUIRED"),
    "ACCESS_DENIED": ("BLOCKED", "ACCESS_DENIED"),
    "NOT_FOUND": ("BLOCKED", "SOURCE_NOT_FOUND"),
    "RESPONSE_TOO_LARGE": ("BLOCKED", "RESPONSE_TOO_LARGE"),
    "INTEGRITY_MISMATCH": ("BLOCKED", "INTEGRITY_CHECK_FAILED"),
    "PARTIAL": ("BLOCKED", "PARTIAL_RESPONSE_DENIED"),
    "INVALID_RESPONSE_METADATA": ("BLOCKED", "INVALID_RESPONSE_METADATA"),
    "UNSAFE_METADATA": ("BLOCKED", "UNSAFE_RESPONSE_DENIED"),
    "TRANSPORT_ERROR": ("ERROR", "TRANSPORT_ERROR"),
}
GOVERNANCE = {"execution_mode": "FIXTURE_ONLY", "network_attempted": False,
              "source_activated": False, "source_artifact_created": False,
              "receipt_created": False, "evidence_created": False,
              "raw_write_performed": False, "current_data_claimed": False,
              "no_current_data_claimed": False, "promotion_authorized": False,
              "release_authorized": False, "publication_authorized": False,
              "public_use_allowed": False}


class FetchInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for a retrieval this module cannot record."""


def profile(max_bytes: int = MAX_BYTES, timeout_seconds: float = 30.0) -> ct.TransportProfile:
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_BYTES:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(PROFILE_ID, frozenset({"earthquake.usgs.gov"}), MEDIA_TYPES,
                               timeout_seconds=timeout_seconds, max_response_bytes=max_bytes)


def _iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


@dataclass(frozen=True)
class Retrieval:
    """A recorded episode; ``body`` is retained only when the episode was captured."""
    source_url: str
    episode: dict
    body: bytes | None

    @property
    def captured(self) -> bool:
        return self.episode["result"]["status"] == "CAPTURED"


def _transport_fields(result: ct.RetrievalResult) -> tuple[str, dict[str, object]]:
    category = result.category.value
    status = result.attempts[-1].status_code
    if status == 204:
        # A captured GET needs a non-empty body under the contract, so the FDSN
        # "no events" answer cannot be recorded as an episode yet.
        raise FetchInputError("EMPTY_SUCCESS_UNREPRESENTABLE")
    if category == "NOT_MODIFIED":
        # This module never sends conditional requests; a 304 answers nothing asked.
        return "INVALID_RESPONSE_METADATA", {}
    if category != "SUCCESS":
        return category, {}
    head, payload = result.source_head, result.payload
    return category, {
        "etag": None if head.etag is None else head.etag.render(),
        "last_modified": None if head.last_modified is None else _iso(head.last_modified),
        "content_length": head.content_length,
        "body_digest": payload.digest, "body_bytes": payload.byte_length,
        "content_type": payload.media_type}


def retrieve(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
             sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
             retry_policy: cc.RetryPolicy | None = None,
             jitter_source: ct.JitterSource | None = None,
             cancellation: ct.CancellationToken | None = None,
             max_bytes: int = MAX_BYTES) -> Retrieval:
    """Execute one GET with caller-supplied effects and record it as an episode.

    ``spec_hash`` is the repository's canonical ``compute_spec_hash`` (RFC 8785 JSON),
    injected so this connector adds no third-party dependency.
    """
    earthquake._request_kind(source_url)
    request = ct.TransportRequest(ct.TransportMethod.GET, source_url, {"Accept": ACCEPT})
    attempted = clock.now()
    result = ct.execute_retrieval(transport, request, profile=profile(max_bytes),
                                  retry_policy=retry_policy or cc.RetryPolicy(),
                                  clock=clock, sleeper=sleeper, jitter_source=jitter_source,
                                  cancellation=cancellation)
    completed = clock.now()
    elapsed = int((completed - attempted).total_seconds() * 1000)
    if not 0 <= elapsed <= MAX_ELAPSED_MS:
        raise FetchInputError("TIME_ORDER")
    attempts = [a for a in result.attempts if a.attempt_number > 0]
    retry_count = max(0, len(attempts) - 1)
    if retry_count > 20:
        raise FetchInputError("RETRY_COUNT")
    category, fields = _transport_fields(result)
    transport_record = {"category": category,
                        "http_status": result.attempts[-1].status_code,
                        "retry_count": retry_count, "elapsed_ms": elapsed, "etag": None,
                        "last_modified": None, "content_length": None, "body_digest": None,
                        "body_bytes": None, "content_type": None, "schema_fingerprint": None,
                        "semantic_sentinel_digest": None}
    transport_record.update(fields)
    result_status, reason = RESULTS[category]
    episode = {"object_type": "SourceRetrievalEpisode", "schema_version": "1.0.0",
               "profile": "kfm.source-retrieval-episode.fixture.v1",
               "source_id": SOURCE_ID, "source_descriptor_ref": f"kfm://source/{SOURCE_ID}",
               "retrieval_profile_ref": RETRIEVAL_PROFILE,
               "attempted_at": _iso(attempted), "completed_at": _iso(completed),
               "method": "GET", "redacted_locator": result.safe_locator,
               "request": {"conditional": False, "if_none_match_present": False,
                           "if_modified_since_present": False},
               "transport": transport_record,
               "result": {"status": result_status, "reason_codes": [reason]},
               "governance": dict(GOVERNANCE)}
    digest = spec_hash(episode)
    if not isinstance(digest, str) or not SPEC_HASH.fullmatch(digest):
        raise FetchInputError("SPEC_HASH")
    episode["spec_hash"] = digest
    episode["episode_id"] = "kfm:source-retrieval-episode:" + digest[7:31]
    body = b"".join(result.payload.chunks) if category == "SUCCESS" else None
    return Retrieval(source_url, episode, body)
