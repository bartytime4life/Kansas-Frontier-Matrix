"""Record one injected-transport retrieval as a fixture-only SourceRetrievalEpisode.

Source-agnostic companion to ``artifact_handoff``: it maps a ``RetrievalResult`` onto the
repository contract ``schemas/contracts/v1/source/source_retrieval_episode.schema.json``
and returns an immutable value object whose construction re-checks identity, captured
state, and exact payload bytes. It performs no transport, storage, receipt emission,
lifecycle write, or admission. Canonical hashing (RFC 8785) is injected by the caller so
this package stays standard-library-only.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
import re
from typing import Callable

from .core import TransportCategory, redact_url
from ._transport_result import RetrievalResult

PREFIX = "kfm:source-retrieval-episode:"
EPISODE_ID = re.compile(r"kfm:source-retrieval-episode:[0-9a-f]{24}\Z")
SPEC_HASH = re.compile(r"sha256:[0-9a-f]{64}\Z")
SOURCE_ID = re.compile(r"[a-z0-9][a-z0-9._:-]{2,127}\Z")
PROFILE_REF = re.compile(r"kfm:[a-z0-9][a-z0-9._:/-]{5,220}\Z")
MAX_ELAPSED_MS = 3_600_000
MAX_RETRIES = 20
# Mirrors validate_source_retrieval_episode.recompute_result() for GET episodes.
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


class EpisodeInputError(ValueError):
    """Bounded, non-payload-bearing diagnostic for a retrieval that cannot be recorded."""


def _iso(value: datetime) -> str:
    if not isinstance(value, datetime) or value.tzinfo is None:
        raise EpisodeInputError("TIME_FORMAT")
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


@dataclass(frozen=True, slots=True)
class RetrievalEpisode:
    """A recorded GET episode. ``body`` is present exactly when the episode was captured.

    The episode is held as canonical JSON and ``episode`` returns a fresh copy, so it
    cannot be mutated after recording. Direct construction is re-validated.
    """
    source_url: str
    episode_json: str
    body: bytes | None

    def __post_init__(self) -> None:
        try:
            episode = json.loads(self.episode_json)
            transport, result = episode["transport"], episode["result"]
            spec, identity = episode["spec_hash"], episode["episode_id"]
        except (TypeError, ValueError, KeyError):
            raise EpisodeInputError("EPISODE_SHAPE") from None
        if (not isinstance(spec, str) or not SPEC_HASH.fullmatch(spec)
                or not isinstance(identity, str) or not EPISODE_ID.fullmatch(identity)
                or identity[len(PREFIX):] != spec[7:31]):
            raise EpisodeInputError("EPISODE_IDENTITY")
        if episode.get("governance") != GOVERNANCE:
            raise EpisodeInputError("EPISODE_GOVERNANCE")
        try:
            locator = redact_url(self.source_url)
        except (TypeError, ValueError):
            raise EpisodeInputError("EPISODE_LOCATOR") from None
        if episode.get("redacted_locator") != locator:
            raise EpisodeInputError("EPISODE_LOCATOR")
        captured = result.get("status") == "CAPTURED"
        if (captured != (transport.get("category") == "SUCCESS")
                or captured != (self.body is not None)
                or (self.body is not None and not isinstance(self.body, bytes))):
            raise EpisodeInputError("EPISODE_STATE")
        if captured and (not self.body or transport.get("body_bytes") != len(self.body)
                         or transport.get("body_digest")
                         != "sha256:" + sha256(self.body).hexdigest()):
            raise EpisodeInputError("EPISODE_INTEGRITY")

    @property
    def episode(self) -> dict:
        return json.loads(self.episode_json)

    @property
    def captured(self) -> bool:
        return self.body is not None


def build_retrieval_episode(result: RetrievalResult, *, source_url: str, source_id: str,
                            retrieval_profile_ref: str, attempted_at: datetime,
                            completed_at: datetime,
                            spec_hash: Callable[[dict], str]) -> RetrievalEpisode:
    """Map one GET ``RetrievalResult`` onto the episode contract.

    ``spec_hash`` must be the repository's canonical ``compute_spec_hash``. Outcomes the
    current contract cannot represent are refused rather than re-labelled: an HTTP 204,
    and a NOT_MODIFIED answer to a request this boundary never makes conditional, which is
    recorded as INVALID_RESPONSE_METADATA.
    """
    if not isinstance(result, RetrievalResult) or result.method.value != "GET":
        raise EpisodeInputError("RESULT_SHAPE")
    if not isinstance(source_id, str) or not SOURCE_ID.fullmatch(source_id):
        raise EpisodeInputError("SOURCE_ID")
    if not isinstance(retrieval_profile_ref, str) or not PROFILE_REF.fullmatch(retrieval_profile_ref):
        raise EpisodeInputError("PROFILE_REF")
    attempted, completed = _iso(attempted_at), _iso(completed_at)
    elapsed = int((completed_at - attempted_at).total_seconds() * 1000)
    if not 0 <= elapsed <= MAX_ELAPSED_MS:
        raise EpisodeInputError("TIME_ORDER")
    retries = max(0, sum(1 for a in result.attempts if a.attempt_number > 0) - 1)
    if retries > MAX_RETRIES:
        raise EpisodeInputError("RETRY_COUNT")
    status = result.attempts[-1].status_code
    if status == 204:
        raise EpisodeInputError("EMPTY_SUCCESS_UNREPRESENTABLE")
    category = result.category.value
    record = {"category": category, "http_status": status, "retry_count": retries,
              "elapsed_ms": elapsed, "etag": None, "last_modified": None,
              "content_length": None, "body_digest": None, "body_bytes": None,
              "content_type": None, "schema_fingerprint": None,
              "semantic_sentinel_digest": None}
    if result.category is TransportCategory.NOT_MODIFIED:
        record["category"] = category = "INVALID_RESPONSE_METADATA"
    elif result.category is TransportCategory.SUCCESS:
        head, payload = result.source_head, result.payload
        record.update({
            "etag": None if head.etag is None else head.etag.render(),
            "last_modified": None if head.last_modified is None else _iso(head.last_modified),
            "content_length": head.content_length, "body_digest": payload.digest,
            "body_bytes": payload.byte_length, "content_type": payload.media_type})
    result_status, reason = RESULTS[category]
    episode = {"object_type": "SourceRetrievalEpisode", "schema_version": "1.0.0",
               "profile": "kfm.source-retrieval-episode.fixture.v1", "source_id": source_id,
               "source_descriptor_ref": f"kfm://source/{source_id}",
               "retrieval_profile_ref": retrieval_profile_ref,
               "attempted_at": attempted, "completed_at": completed, "method": "GET",
               "redacted_locator": result.safe_locator,
               "request": {"conditional": False, "if_none_match_present": False,
                           "if_modified_since_present": False},
               "transport": record,
               "result": {"status": result_status, "reason_codes": [reason]},
               "governance": dict(GOVERNANCE)}
    digest = spec_hash(episode)
    if not isinstance(digest, str) or not SPEC_HASH.fullmatch(digest):
        raise EpisodeInputError("SPEC_HASH")
    episode["spec_hash"] = digest
    episode["episode_id"] = PREFIX + digest[7:31]
    body = b"".join(result.payload.chunks) if category == "SUCCESS" else None
    return RetrievalEpisode(source_url,
                            json.dumps(episode, sort_keys=True, separators=(",", ":")), body)
