"""Deterministic tests for recording injected-transport results as retrieval episodes."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import socket
import sys
from unittest.mock import patch

import pytest

ROOT = Path(__file__).resolve().parents[3]
for value in (str(ROOT), str(ROOT / "packages/connectors-core/src"),
              str(ROOT / "packages/hashing/src")):
    if value not in sys.path:
        sys.path.insert(0, value)

from connectors_core import core, transport  # noqa: E402
from connectors_core.retrieval_episode import (  # noqa: E402
    GOVERNANCE,
    RESULTS,
    EpisodeInputError,
    RetrievalEpisode,
    build_retrieval_episode,
    require_source,
)
from hashing import compute_spec_hash  # noqa: E402
from tools.validators.source import validate_source_retrieval_episode as validator  # noqa: E402

from _support import Clock, FakeTransport, Sleeper, profile, response, retry  # noqa: E402

URL = "https://source.example.test/data?token=secret&county=001"
BODY = b'{"ok":true}'
EXPECTED_OUTCOME = {"CAPTURED": "PASS", "RETRY_REQUIRED": "ABSTAIN",
                    "BLOCKED": "DENY", "ERROR": "ERROR"}


def record(*outcomes, spec_hash=compute_spec_hash, max_attempts=2, **kwargs):
    clock = Clock()
    request = transport.TransportRequest(transport.TransportMethod.GET, URL,
                                         {"Accept": "application/json"})
    attempted = clock.now()
    result = transport.execute_retrieval(
        FakeTransport(clock, *outcomes), request, profile=kwargs.pop("profile", profile()),
        retry_policy=retry(max_attempts=max_attempts), clock=clock, sleeper=Sleeper(clock),
        cancellation=kwargs.pop("cancellation", None))
    return build_retrieval_episode(
        result, source_url=URL, source_id="synthetic.ks.source",
        retrieval_profile_ref="kfm:source-profile:synthetic-retrieval-v1",
        attempted_at=attempted, completed_at=clock.now() + kwargs.pop("extra", timedelta()),
        spec_hash=spec_hash, **kwargs)


class Cancelled:
    def is_cancelled(self):
        return True


def emitted():
    yield record(response())
    yield record(response(503, (b"busy",)), response())
    yield record(response(body=(b"x" * 65,)))
    yield record(response(headers={"Content-Type": "text/html"}))
    yield record(response(headers={"Content-Length": "1"}))
    yield record(response(final_url="https://source.example.test/elsewhere"))
    for status in (302, 304, 401, 403, 404, 451):
        yield record(response(status, () if status == 304 else (b"x",),
                              headers={"Content-Length": "0" if status == 304 else "1"}))
    for status in (206, 429, 500):
        yield record(response(status, (b"x",)), response(status, (b"x",)))
    yield record(TimeoutError(), TimeoutError())
    yield record(cancellation=Cancelled())


def test_every_emitted_episode_passes_the_contract_validator():
    categories = set()
    for episode_record in emitted():
        episode = episode_record.episode
        categories.add(episode["transport"]["category"])
        result = validator.validate_payload(episode)
        reasons = episode["result"]["reason_codes"]
        assert [f.code for f in result.findings] == (
            [] if reasons == ["RETRIEVAL_BODY_CAPTURED"] else reasons)
        assert result.outcome == EXPECTED_OUTCOME[episode["result"]["status"]]
    assert categories == {"SUCCESS", "RESPONSE_TOO_LARGE", "INVALID_RESPONSE_METADATA",
                          "UNSAFE_METADATA", "AUTH_REQUIRED", "ACCESS_DENIED", "NOT_FOUND",
                          "RETRY_EXHAUSTED", "CANCELLED"}


def test_result_table_matches_validator_and_transport_categories():
    assert set(RESULTS) | {"NOT_MODIFIED"} == {c.value for c in core.TransportCategory}
    for category, (status, reason) in RESULTS.items():
        assert validator.recompute_result(
            {"method": "GET", "transport": {"category": category}}) == {
                "status": status, "reason_codes": [reason]}


def test_success_records_identity_and_keeps_body():
    episode_record = record(response())
    episode = episode_record.episode
    assert episode_record.captured and episode_record.body == BODY
    assert episode["redacted_locator"] == "https://source.example.test/data"
    assert episode["transport"]["body_digest"] == "sha256:" + hashlib.sha256(BODY).hexdigest()
    assert episode["transport"]["etag"] == 'W/"fixture-head"'
    assert episode["transport"]["last_modified"] == "2025-08-06T12:00:00Z"
    assert episode["governance"] == GOVERNANCE
    assert episode["spec_hash"] == compute_spec_hash(
        {k: v for k, v in episode.items() if k not in {"spec_hash", "episode_id"}})
    assert episode["episode_id"] == "kfm:source-retrieval-episode:" + episode["spec_hash"][7:31]


def test_retry_count_excludes_the_first_attempt():
    assert record(response()).episode["transport"]["retry_count"] == 0
    assert record(response(503, (b"busy",)), response()).episode["transport"]["retry_count"] == 1
    assert record(cancellation=Cancelled()).episode["transport"]["retry_count"] == 0


def test_episode_is_immutable_after_recording():
    episode_record = record(response())
    episode_record.episode["transport"]["body_digest"] = "sha256:" + "0" * 64
    assert episode_record.episode["transport"]["body_digest"].endswith(
        hashlib.sha256(BODY).hexdigest())
    with pytest.raises(AttributeError):
        episode_record.body = b"other"


@pytest.mark.parametrize("code,mutate", [
    ("EPISODE_INTEGRITY", lambda e, b: (e, b + b" ")),
    ("EPISODE_INTEGRITY", lambda e, b: ({**e, "transport": {**e["transport"],
                                          "body_bytes": len(b) + 1}}, b)),
    ("EPISODE_STATE", lambda e, b: (e, None)),
    ("EPISODE_STATE", lambda e, b: ({**e, "transport": {**e["transport"],
                                      "category": "RATE_LIMITED"}}, b)),
    ("EPISODE_IDENTITY", lambda e, b: ({**e, "episode_id":
                                         "kfm:source-retrieval-episode:" + "0" * 24}, b)),
    ("EPISODE_IDENTITY", lambda e, b: ({**e, "spec_hash": "sha256:short"}, b)),
    ("EPISODE_GOVERNANCE", lambda e, b: ({**e, "governance": {**e["governance"],
                                           "network_attempted": True}}, b)),
    ("EPISODE_LOCATOR", lambda e, b: ({**e, "redacted_locator":
                                        "https://source.example.test/other"}, b)),
    ("EPISODE_SHAPE", lambda e, b: ({k: v for k, v in e.items() if k != "result"}, b)),
])
def test_direct_construction_is_revalidated(code, mutate):
    good = record(response())
    episode, body = mutate(good.episode, good.body)
    with pytest.raises(EpisodeInputError) as info:
        RetrievalEpisode(URL, json.dumps(episode), body)
    assert info.value.args[0] == code


def test_uncaptured_episode_cannot_carry_body():
    held = record(response(403, (b"no",), headers={"Content-Length": "2"}))
    assert not held.captured and held.body is None
    with pytest.raises(EpisodeInputError) as info:
        RetrievalEpisode(URL, held.episode_json, BODY)
    assert info.value.args[0] == "EPISODE_STATE"
    with pytest.raises(EpisodeInputError) as info:
        RetrievalEpisode("https://other.example.test/data", record(response()).episode_json, BODY)
    assert info.value.args[0] == "EPISODE_LOCATOR"


@pytest.mark.parametrize("code,kwargs,outcomes", [
    ("EMPTY_SUCCESS_UNREPRESENTABLE", {}, (response(204, (), headers={"Content-Length": "0"}),)),
    ("SPEC_HASH", {"spec_hash": lambda _: "md5:x"}, (response(),)),
    ("TIME_ORDER", {"extra": timedelta(hours=2)}, (response(),)),
])
def test_unrepresentable_inputs_are_refused(code, kwargs, outcomes):
    with pytest.raises(EpisodeInputError) as info:
        record(*outcomes, **kwargs)
    assert info.value.args[0] == code


def test_identity_arguments_are_bounded():
    clock = Clock()
    result = transport.execute_retrieval(
        FakeTransport(clock, response()),
        transport.TransportRequest(transport.TransportMethod.GET, URL),
        profile=profile(), retry_policy=retry(max_attempts=1), clock=clock,
        sleeper=Sleeper(clock))
    good = dict(source_url=URL, source_id="synthetic.ks.source",
                retrieval_profile_ref="kfm:source-profile:synthetic-retrieval-v1",
                attempted_at=clock.now(), completed_at=clock.now(),
                spec_hash=compute_spec_hash)
    for key, value, code in (("source_id", "Bad Id", "SOURCE_ID"),
                             ("retrieval_profile_ref", "profile", "PROFILE_REF"),
                             ("attempted_at", datetime(2026, 1, 1), "TIME_FORMAT")):
        with pytest.raises(EpisodeInputError) as info:
            build_retrieval_episode(result, **{**good, key: value})
        assert info.value.args[0] == code
    with pytest.raises(EpisodeInputError) as info:
        build_retrieval_episode(object(), **good)
    assert info.value.args[0] == "RESULT_SHAPE"


def test_recording_opens_no_socket():
    with patch.object(socket, "socket", side_effect=AssertionError("network")), \
            patch.object(socket, "create_connection", side_effect=AssertionError("network")):
        assert record(response()).captured


def test_attempted_and_completed_are_utc_seconds():
    episode = record(response()).episode
    assert episode["attempted_at"].endswith("Z") and episode["completed_at"].endswith("Z")
    start = datetime.fromisoformat(episode["attempted_at"].replace("Z", "+00:00"))
    assert start.tzinfo == timezone.utc


def test_require_source_binds_connector_identity():
    good = record(response())
    assert require_source(good, source_id="synthetic.ks.source",
                          retrieval_profile_ref="kfm:source-profile:synthetic-retrieval-v1") is good
    for source_id, profile_ref in (("other.source", "kfm:source-profile:synthetic-retrieval-v1"),
                                   ("synthetic.ks.source", "kfm:source-profile:other-v1")):
        with pytest.raises(EpisodeInputError) as info:
            require_source(good, source_id=source_id, retrieval_profile_ref=profile_ref)
        assert info.value.args[0] == "EPISODE_SOURCE_MISMATCH"
    forged = json.loads(good.episode_json)
    forged["source_descriptor_ref"] = "kfm://source/other.source"
    with pytest.raises(EpisodeInputError):
        require_source(RetrievalEpisode(URL, json.dumps(forged), good.body),
                       source_id="synthetic.ks.source",
                       retrieval_profile_ref="kfm:source-profile:synthetic-retrieval-v1")
    with pytest.raises(TypeError):
        require_source({"episode": {}}, source_id="x", retrieval_profile_ref="y")
