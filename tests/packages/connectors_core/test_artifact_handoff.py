"""Deterministic tests for the internal retrieval-to-SourceArtifact handoff."""
from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import importlib
import json
from pathlib import Path
import socket
import sys
from unittest.mock import patch

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "packages/connectors-core/src"
for value in (str(ROOT), str(SRC)):
    if value not in sys.path:
        sys.path.insert(0, value)

from connectors_core import artifact_handoff as handoff_module  # noqa: E402
from connectors_core import core, transport  # noqa: E402
from connectors_core.artifact_handoff import (  # noqa: E402
    ArtifactHandoffContext,
    ArtifactHandoffError,
    ParserIdentity,
    RightsSnapshot,
    build_source_artifact_handoff,
)
from tools.validators.validate_source_artifact import validate_artifact  # noqa: E402

FIXTURE = ROOT / "fixtures/packages/connectors_core/artifact_handoff/valid_context.json"
SCHEMA = ROOT / "schemas/contracts/v1/source/source_artifact.schema.json"
MODULE = SRC / "connectors_core/artifact_handoff.py"


def _time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def context() -> ArtifactHandoffContext:
    raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
    rights = raw.pop("rights_snapshot")
    parser = raw.pop("parser")
    return ArtifactHandoffContext(
        **raw,
        parameter_names=tuple(raw["parameter_names"]),
        header_names=tuple(raw["header_names"]),
        correction_refs=tuple(raw["correction_refs"]),
        rights_snapshot=RightsSnapshot(captured_at=_time(rights.pop("captured_at")), **rights),
        parser=ParserIdentity(**parser),
    )


def successful_result(body: tuple[bytes, ...] = (b'{"ok":', b"true}")) -> transport.RetrievalResult:
    observed_at = datetime(2026, 8, 6, 18, 5, tzinfo=timezone.utc)
    content = b"".join(body)
    digest = "sha256:" + hashlib.sha256(content).hexdigest()
    payload = transport.CapturedPayload(body, digest, len(content), "application/json")
    source_head = core.SourceHeadObservation(
        observed_at=observed_at,
        last_modified=datetime(2026, 8, 5, 12, tzinfo=timezone.utc),
        content_length=len(content),
        computed_digest=digest,
    )
    attempt = transport.AttemptRecord(
        attempt_number=1,
        category=core.TransportCategory.SUCCESS,
        code="FETCH_SUCCESS",
        observed_at=observed_at,
        duration_seconds=0.25,
        safe_locator="https://source.example.test/data",
        status_code=200,
        byte_length=len(content),
        digest=digest,
    )
    return transport.RetrievalResult(
        method=transport.TransportMethod.GET,
        category=core.TransportCategory.SUCCESS,
        safe_locator="https://source.example.test/data",
        attempts=(attempt,),
        payload=payload,
        source_head=source_head,
    )


def test_success_preserves_exact_bytes_and_validates_existing_source_artifact_profile(tmp_path):
    result = successful_result()
    handoff = build_source_artifact_handoff(result, context())
    metadata = handoff.metadata_dict()
    payload_path = tmp_path / "capture.json"
    metadata_path = tmp_path / "metadata.json"
    payload_path.write_bytes(handoff.payload_bytes())
    metadata_path.write_text(json.dumps(metadata, sort_keys=True) + "\n", encoding="utf-8")

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    ).validate(metadata)
    validation = validate_artifact(metadata_path, payload_path)

    assert validation.ok, validation.findings
    assert handoff.payload_chunks == result.payload.chunks
    assert handoff.payload_bytes() == b'{"ok":true}'
    assert metadata["artifact_id"] == f"source-artifact:{result.payload.digest}"
    assert metadata["immutable_storage_ref"] == f"cas:{result.payload.digest}"
    assert metadata["content_digest"] == result.payload.digest
    assert metadata["byte_length"] == result.payload.byte_length
    assert metadata["source_reported_at"] == "2026-08-05T12:00:00Z"
    assert metadata["retrieved_at"] == "2026-08-06T18:05:00Z"


def test_locator_request_context_and_governance_are_deterministic_and_secret_safe():
    result = successful_result()
    ctx = replace(
        context(),
        parameter_names=("site", "format", "site"),
        header_names=("accept", "accept"),
    )
    handoff = build_source_artifact_handoff(result, ctx)
    metadata = handoff.metadata_dict()
    locator = metadata["source_locator"]
    expected_locator_digest = "sha256:" + hashlib.sha256(
        b"api_record\nhttps://source.example.test/data"
    ).hexdigest()

    assert locator["value"] == "https://source.example.test/data"
    assert locator["locator_digest"] == expected_locator_digest
    assert metadata["request_context"]["parameter_names"] == ["format", "site"]
    assert metadata["request_context"]["header_names"] == ["accept"]
    assert metadata["request_context"]["secrets_embedded"] is False
    assert metadata["governance"] == {
        "public_use_allowed": False,
        "authority_created": False,
        "release_ref": None,
        "spec_hash": context().governance_spec_hash,
    }
    rendered = json.dumps(metadata, sort_keys=True) + repr(handoff)
    assert "token=" not in rendered and "Bearer" not in rendered
    assert not handoff.authority_created
    assert not handoff.lifecycle_write_allowed
    assert not handoff.receipt_created
    assert not handoff.repository_mutation_allowed


def test_metadata_is_deeply_immutable_but_plain_copy_is_editable():
    handoff = build_source_artifact_handoff(successful_result(), context())
    with pytest.raises(TypeError):
        handoff.metadata["object_type"] = "Other"  # type: ignore[index]
    with pytest.raises(TypeError):
        handoff.metadata["governance"]["authority_created"] = True  # type: ignore[index]
    copy = handoff.metadata_dict()
    copy["object_type"] = "Other"
    assert handoff.metadata["object_type"] == "SourceArtifact"


def test_head_not_modified_and_failure_results_never_create_artifact_handoff():
    observed_at = datetime(2026, 8, 6, 18, 5, tzinfo=timezone.utc)
    source_head = core.SourceHeadObservation(observed_at=observed_at)
    head_attempt = transport.AttemptRecord(
        1,
        core.TransportCategory.SUCCESS,
        "HEAD_SUCCESS",
        observed_at,
        0.1,
        "https://source.example.test/data",
        status_code=200,
    )
    head = transport.RetrievalResult(
        transport.TransportMethod.HEAD,
        core.TransportCategory.SUCCESS,
        "https://source.example.test/data",
        (head_attempt,),
        source_head=source_head,
    )
    not_modified_attempt = replace(
        head_attempt,
        category=core.TransportCategory.NOT_MODIFIED,
        code="NOT_MODIFIED",
        status_code=304,
    )
    not_modified = transport.RetrievalResult(
        transport.TransportMethod.GET,
        core.TransportCategory.NOT_MODIFIED,
        "https://source.example.test/data",
        (not_modified_attempt,),
        source_head=source_head,
        prior_artifact_retained=True,
    )
    timeout_attempt = replace(
        head_attempt,
        category=core.TransportCategory.TIMEOUT,
        code="TRANSPORT_TIMEOUT",
        status_code=None,
    )
    timeout = transport.RetrievalResult(
        transport.TransportMethod.GET,
        core.TransportCategory.TIMEOUT,
        "https://source.example.test/data",
        (timeout_attempt,),
        failure=core.make_failure_detail(
            core.TransportCategory.TIMEOUT,
            code="TRANSPORT_TIMEOUT",
            message="The injected transport timed out.",
            locator="https://source.example.test/data?token=secret",
        ),
    )

    for result in (head, not_modified, timeout):
        with pytest.raises(ArtifactHandoffError):
            build_source_artifact_handoff(result, context())


def test_source_head_digest_length_and_rights_time_must_match_payload():
    result = successful_result()
    mismatched_head = replace(
        result.source_head,
        computed_digest="sha256:" + ("d" * 64),
    )
    with pytest.raises(ArtifactHandoffError, match="digest"):
        build_source_artifact_handoff(replace(result, source_head=mismatched_head), context())

    mismatched_length = replace(result.source_head, content_length=result.payload.byte_length + 1)
    with pytest.raises(ArtifactHandoffError, match="length"):
        build_source_artifact_handoff(replace(result, source_head=mismatched_length), context())

    late_rights = replace(
        context(),
        rights_snapshot=replace(
            context().rights_snapshot,
            captured_at=datetime(2026, 8, 6, 18, 6, tzinfo=timezone.utc),
        ),
    )
    with pytest.raises(ArtifactHandoffError, match="rights snapshot"):
        build_source_artifact_handoff(result, late_rights)


def test_conflict_and_supersession_lineage_fail_closed():
    result = successful_result()
    conflict = replace(
        context(),
        retrieval_outcome="SOURCE_CONFLICT",
        conflict_group_ref="kfm://source-conflict/fixture-one",
    )
    metadata = build_source_artifact_handoff(result, conflict).metadata_dict()
    assert metadata["retrieval_outcome"] == "SOURCE_CONFLICT"
    assert metadata["lineage"]["conflict_group_ref"] == "kfm://source-conflict/fixture-one"

    with pytest.raises(ArtifactHandoffError, match="conflict_group_ref"):
        replace(context(), conflict_group_ref="kfm://source-conflict/fixture-one")
    with pytest.raises(ArtifactHandoffError, match="conflict_group_ref"):
        replace(context(), retrieval_outcome="SOURCE_CONFLICT")
    with pytest.raises(ArtifactHandoffError, match="correction"):
        replace(
            context(),
            supersedes_artifact_ref="source-artifact:sha256:" + ("e" * 64),
        )

    self_ref = f"source-artifact:{result.payload.digest}"
    self_superseding = replace(
        context(),
        supersedes_artifact_ref=self_ref,
        correction_refs=("kfm://correction/fixture-one",),
    )
    with pytest.raises(ArtifactHandoffError, match="supersede itself"):
        build_source_artifact_handoff(result, self_superseding)


def test_import_is_side_effect_free_and_static_boundary_has_no_effect_clients(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    before = list(tmp_path.iterdir())
    boom = AssertionError("ambient network")
    with (
        patch.object(socket.socket, "connect", side_effect=boom),
        patch.object(socket.socket, "connect_ex", side_effect=boom),
        patch.object(socket, "create_connection", side_effect=boom),
        patch.object(socket, "getaddrinfo", side_effect=boom),
    ):
        assert importlib.reload(handoff_module) is handoff_module
    assert list(tmp_path.iterdir()) == before

    source = MODULE.read_text(encoding="utf-8")
    forbidden = (
        "import requests",
        "import httpx",
        "import aiohttp",
        "import urllib.request",
        "import socket",
        "import subprocess",
        "open(",
        "Path(",
        "data/raw",
        "data/work",
        "data/quarantine",
        "data/processed",
        "data/catalog",
        "data/published",
        "release/",
        "EvidenceBundle",
        "PolicyDecision",
    )
    assert all(token not in source for token in forbidden)
