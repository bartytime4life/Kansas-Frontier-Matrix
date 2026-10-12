"""Run planner- or manifest-issued Census GETs through the shared injected transport.

Two products, each with its own source identity and transport profile:

* ACS API tables (``retrieve_acs``): the URL must be exactly what ``acs_api.acs_url``
  emits for the request it encodes. That URL never carries an API key; ``key=`` is
  refused by ``acs_api._request``.
* TIGER/Line packages (``retrieve_tiger``): only packages listed in the committed
  source-reference manifest. The URL, byte budget and expected SHA-256 all come from
  the manifest entry, so a byte mismatch is an ``INTEGRITY_MISMATCH`` episode.

Transport effects are supplied by the caller and executed by
``connectors_core.transport.execute_retrieval``; results are recorded by
``connectors_core.retrieval_episode``. No network library is imported. The episode
contract fixes ``execution_mode: FIXTURE_ONLY``, so only synthetic transports are in
scope. Requires ``packages/connectors-core/src`` on the import path.
"""
from __future__ import annotations

from typing import Callable

from connectors_core import core as cc
from connectors_core import transport as ct
from connectors_core.retrieval_episode import (
    EpisodeInputError,
    RetrievalEpisode,
    build_retrieval_episode,
)

from . import acs_api, tiger_package

ACS_SOURCE_ID = "census.acs-api"
ACS_PROFILE_ID = "census-acs-api-json-v1"
ACS_RETRIEVAL_PROFILE = f"kfm:source-profile:{ACS_PROFILE_ID}"
ACS_MAX_BYTES = 32 * 1024 * 1024
TIGER_SOURCE_ID = "census.tiger-line"
TIGER_PROFILE_ID = "census-tiger-line-zip-v1"
TIGER_RETRIEVAL_PROFILE = f"kfm:source-profile:{TIGER_PROFILE_ID}"
TIGER_ARCHIVE = "https://www2.census.gov/geo/tiger/"

# Stable connector-level names for the shared value object and diagnostic.
Retrieval = RetrievalEpisode
FetchInputError = EpisodeInputError


def acs_profile(max_bytes: int = ACS_MAX_BYTES,
                timeout_seconds: float = 60.0) -> ct.TransportProfile:
    if type(max_bytes) is not int or not 1 <= max_bytes <= ACS_MAX_BYTES:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(ACS_PROFILE_ID, frozenset({"api.census.gov"}),
                               frozenset({"application/json"}),
                               timeout_seconds=timeout_seconds, max_response_bytes=max_bytes)


def tiger_profile(byte_length: int, timeout_seconds: float = 600.0) -> ct.TransportProfile:
    if type(byte_length) is not int or not 1 <= byte_length <= 1024 * 1024 * 1024:
        raise FetchInputError("RESPONSE_BOUND")
    return ct.TransportProfile(TIGER_PROFILE_ID, frozenset({"www2.census.gov"}),
                               frozenset({"application/zip"}),
                               timeout_seconds=timeout_seconds, max_response_bytes=byte_length)


def _require_planned_acs(source_url: str) -> None:
    request = acs_api._request(source_url)
    canonical = acs_api.acs_url(request.year, request.dataset, request.variables,
                                request.geography, pair_moe=False)
    if canonical != source_url:
        raise acs_api.AcsInputError("SOURCE_URL_SCOPE")


def tiger_entry(file_name: str, manifest: dict | None = None) -> dict:
    """Return the manifest entry for ``file_name`` with a URL inside the TIGER archive."""
    name = tiger_package.parse_file_name(file_name)
    entry = tiger_package.manifest_entry(
        tiger_package.load_manifest() if manifest is None else manifest, file_name)
    expected = f"{TIGER_ARCHIVE}TIGER{name.vintage}/{name.product}/{file_name}"
    digest = entry.get("sha256")
    if (entry.get("source_url") != expected or entry.get("product") != name.product
            or not isinstance(digest, str) or len(digest) != 64
            or any(c not in "0123456789abcdef" for c in digest)):
        raise tiger_package.TigerPackageError("MANIFEST_ENTRY_MISMATCH")
    return entry


def _execute(request: ct.TransportRequest, profile: ct.TransportProfile, *, source_url: str,
             source_id: str, profile_ref: str, transport, clock, sleeper, spec_hash,
             retry_policy, jitter_source, cancellation) -> Retrieval:
    attempted = clock.now()
    result = ct.execute_retrieval(transport, request, profile=profile,
                                  retry_policy=retry_policy or cc.RetryPolicy(),
                                  clock=clock, sleeper=sleeper, jitter_source=jitter_source,
                                  cancellation=cancellation)
    return build_retrieval_episode(result, source_url=source_url, source_id=source_id,
                                   retrieval_profile_ref=profile_ref, attempted_at=attempted,
                                   completed_at=clock.now(), spec_hash=spec_hash)


def retrieve_acs(source_url: str, *, transport: ct.Transport, clock: ct.Clock,
                 sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
                 retry_policy: cc.RetryPolicy | None = None,
                 jitter_source: ct.JitterSource | None = None,
                 cancellation: ct.CancellationToken | None = None,
                 max_bytes: int = ACS_MAX_BYTES) -> Retrieval:
    """Execute one planner-canonical ACS API GET and record it as an episode."""
    _require_planned_acs(source_url)
    request = ct.TransportRequest(ct.TransportMethod.GET, source_url,
                                  {"Accept": "application/json"})
    return _execute(request, acs_profile(max_bytes), source_url=source_url,
                    source_id=ACS_SOURCE_ID, profile_ref=ACS_RETRIEVAL_PROFILE,
                    transport=transport, clock=clock, sleeper=sleeper, spec_hash=spec_hash,
                    retry_policy=retry_policy, jitter_source=jitter_source,
                    cancellation=cancellation)


def retrieve_tiger(file_name: str, *, transport: ct.Transport, clock: ct.Clock,
                   sleeper: ct.Sleeper, spec_hash: Callable[[dict], str],
                   manifest: dict | None = None,
                   retry_policy: cc.RetryPolicy | None = None,
                   jitter_source: ct.JitterSource | None = None,
                   cancellation: ct.CancellationToken | None = None) -> Retrieval:
    """Execute one manifest-pinned TIGER/Line package GET and record it as an episode."""
    entry = tiger_entry(file_name, manifest)
    request = ct.TransportRequest(ct.TransportMethod.GET, entry["source_url"],
                                  {"Accept": "application/zip"},
                                  expected_digest="sha256:" + entry["sha256"])
    return _execute(request, tiger_profile(entry.get("byte_length")),
                    source_url=entry["source_url"], source_id=TIGER_SOURCE_ID,
                    profile_ref=TIGER_RETRIEVAL_PROFILE, transport=transport, clock=clock,
                    sleeper=sleeper, spec_hash=spec_hash, retry_policy=retry_policy,
                    jitter_source=jitter_source, cancellation=cancellation)
