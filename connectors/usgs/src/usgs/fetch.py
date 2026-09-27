"""Classify one supplied USGS earthquake response as a fixture-only retrieval episode.

This module performs no transport. The retrieval-episode contract
(``schemas/contracts/v1/source/source_retrieval_episode.schema.json``) currently fixes
``execution_mode: FIXTURE_ONLY`` and ``network_attempted: false``, so live retrieval is
not an authorized capability here. A caller supplies bytes and response metadata that
were obtained elsewhere; this module bounds them, maps them to the contract's
transport category and result, and keeps the body only for a captured response.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from hashlib import sha256
import re
from typing import Callable
from urllib.parse import urlsplit

from . import earthquake

SOURCE_ID = "usgs.earthquake"
RETRIEVAL_PROFILE = "kfm:source-profile:usgs-earthquake-geojson-v1"
MAX_BYTES = 8 * 1024 * 1024
MAX_ELAPSED_MS = 3_600_000
CONTENT_TYPES = frozenset({"application/json", "application/geo+json"})
CONTENT_TYPE = re.compile(r"[a-z0-9!#$&^_.+-]+/[a-z0-9!#$&^_.+-]+(?:;[ -~]{1,128})?\Z")
ETAG = re.compile(r'(?:W/)?"[\x21\x23-\x5b\x5d-\x7e]{0,512}"\Z')
FAILURES = frozenset({"TIMEOUT", "CANCELLED", "RETRY_EXHAUSTED", "TRANSPORT_ERROR"})
STATUS_CATEGORIES = {206: "PARTIAL", 401: "AUTH_REQUIRED", 403: "ACCESS_DENIED",
                     451: "ACCESS_DENIED", 404: "NOT_FOUND", 429: "RATE_LIMITED"}
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
    """Bounded, non-payload-bearing diagnostic for input this module cannot classify."""


def _instant(value: object) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise FetchInputError("TIME_FORMAT")
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        raise FetchInputError("TIME_FORMAT") from None
    return parsed.astimezone(timezone.utc)


def _iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _headers(pairs: object) -> dict[str, str]:
    if not isinstance(pairs, (tuple, list)):
        raise FetchInputError("HEADERS")
    result: dict[str, str] = {}
    for pair in pairs:
        if (not isinstance(pair, (tuple, list)) or len(pair) != 2
                or not all(isinstance(item, str) for item in pair)):
            raise FetchInputError("HEADERS")
        name = pair[0].strip().lower()
        if name in result:
            raise FetchInputError("DUPLICATE_HEADER")
        result[name] = pair[1].strip()
    return result


def _locator(source_url: str) -> str:
    parsed = urlsplit(source_url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


@dataclass(frozen=True)
class Retrieval:
    """A classified episode; ``body`` is retained only when the episode was captured."""
    source_url: str
    episode: dict
    body: bytes | None

    @property
    def captured(self) -> bool:
        return self.episode["result"]["status"] == "CAPTURED"


def _success_metadata(headers: dict[str, str], body: bytes, completed: datetime,
                      max_bytes: int) -> tuple[str, dict[str, object]]:
    if not body:
        return "INVALID_RESPONSE_METADATA", {}
    if len(body) > max_bytes:
        return "RESPONSE_TOO_LARGE", {}
    if headers.get("content-encoding", "identity").lower() != "identity":
        return "UNSAFE_METADATA", {}
    content_type = headers.get("content-type", "").lower().replace("; ", ";")
    if not CONTENT_TYPE.fullmatch(content_type) or content_type.split(";")[0] not in CONTENT_TYPES:
        return "INVALID_RESPONSE_METADATA", {}
    length = headers.get("content-length")
    if length is not None and (not length.isdigit() or int(length) != len(body)):
        return "INTEGRITY_MISMATCH", {}
    etag = headers.get("etag")
    if etag is not None and not ETAG.fullmatch(etag):
        return "INVALID_RESPONSE_METADATA", {}
    modified = headers.get("last-modified")
    if modified is not None:
        try:
            moment = parsedate_to_datetime(modified)
        except (TypeError, ValueError):
            return "INVALID_RESPONSE_METADATA", {}
        if moment.tzinfo is None or moment > completed:
            return "INVALID_RESPONSE_METADATA", {}
        modified = _iso(moment)
    return "SUCCESS", {"etag": etag, "last_modified": modified,
                       "content_length": None if length is None else int(length),
                       "body_digest": "sha256:" + sha256(body).hexdigest(),
                       "body_bytes": len(body), "content_type": content_type}


def classify_response(*, source_url: str, attempted_at: str, completed_at: str,
                      spec_hash: Callable[[dict], str], status: int | None = None,
                      headers: tuple[tuple[str, str], ...] = (), body: bytes | None = None,
                      failure: str | None = None, retry_count: int = 0,
                      max_bytes: int = MAX_BYTES) -> Retrieval:
    """Classify supplied response material; never opens a connection.

    ``spec_hash`` is the repository's canonical ``compute_spec_hash`` (RFC 8785 JSON),
    injected so this connector stays standard-library-only.
    """
    earthquake._request_kind(source_url)
    attempted, completed = _instant(attempted_at), _instant(completed_at)
    elapsed = int((completed - attempted).total_seconds() * 1000)
    if not 0 <= elapsed <= MAX_ELAPSED_MS:
        raise FetchInputError("TIME_ORDER")
    if type(retry_count) is not int or not 0 <= retry_count <= 20:
        raise FetchInputError("RETRY_COUNT")
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_BYTES:
        raise FetchInputError("RESPONSE_BOUND")
    fields: dict[str, object] = {}
    if failure is not None:
        if failure not in FAILURES or status is not None or body is not None:
            raise FetchInputError("FAILURE_SHAPE")
        category = failure
    else:
        if type(status) is not int or not 100 <= status <= 599 or not isinstance(body, bytes):
            raise FetchInputError("RESPONSE_SHAPE")
        parsed_headers = _headers(headers)
        if status == 200:
            category, fields = _success_metadata(parsed_headers, body, completed, max_bytes)
        elif status == 204:
            # The contract requires a non-empty body for a captured GET, so the FDSN
            # "no events" answer cannot be represented as an episode yet.
            raise FetchInputError("EMPTY_SUCCESS_UNREPRESENTABLE")
        else:
            category = STATUS_CATEGORIES.get(status, "TRANSPORT_ERROR"
                                             if status >= 500 or status < 200
                                             else "INVALID_RESPONSE_METADATA")
    captured = category == "SUCCESS"
    transport = {"category": category, "http_status": status, "retry_count": retry_count,
                 "elapsed_ms": elapsed, "etag": None, "last_modified": None,
                 "content_length": None, "body_digest": None, "body_bytes": None,
                 "content_type": None, "schema_fingerprint": None,
                 "semantic_sentinel_digest": None}
    transport.update(fields)
    result_status, reason = RESULTS[category]
    episode = {"object_type": "SourceRetrievalEpisode", "schema_version": "1.0.0",
               "profile": "kfm.source-retrieval-episode.fixture.v1",
               "source_id": SOURCE_ID, "source_descriptor_ref": f"kfm://source/{SOURCE_ID}",
               "retrieval_profile_ref": RETRIEVAL_PROFILE,
               "attempted_at": _iso(attempted), "completed_at": _iso(completed),
               "method": "GET", "redacted_locator": _locator(source_url),
               "request": {"conditional": False, "if_none_match_present": False,
                           "if_modified_since_present": False},
               "transport": transport,
               "result": {"status": result_status, "reason_codes": [reason]},
               "governance": dict(GOVERNANCE)}
    digest = spec_hash(episode)
    if not isinstance(digest, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
        raise FetchInputError("SPEC_HASH")
    episode["spec_hash"] = digest
    episode["episode_id"] = "kfm:source-retrieval-episode:" + digest[7:31]
    return Retrieval(source_url, episode, body if captured else None)
