"""Deterministic no-network tests for connectors_core pure primitives."""
from __future__ import annotations

import hashlib
import importlib
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/connectors-core/src"
if str(PACKAGE_SRC) not in sys.path:
    sys.path.insert(0, str(PACKAGE_SRC))

from connectors_core import core  # noqa: E402


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("connectors_core import attempted network access")


def test_import_is_side_effect_free_and_has_no_public_package_exports(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    before = list(tmp_path.iterdir())
    with (
        patch.object(socket.socket, "connect", side_effect=_unexpected_network),
        patch.object(socket.socket, "connect_ex", side_effect=_unexpected_network),
        patch.object(socket, "create_connection", side_effect=_unexpected_network),
        patch.object(socket, "getaddrinfo", side_effect=_unexpected_network),
    ):
        importlib.reload(core)
    assert list(tmp_path.iterdir()) == before

    import connectors_core

    # First slice remains internal: no package-level runtime API is exported.
    assert not hasattr(connectors_core, "RetryPolicy")
    assert not hasattr(connectors_core, "sha256_stream")


def test_etag_preserves_weakness_and_rejects_unsafe_values():
    strong = core.ETag.parse('"abc-123"')
    weak = core.ETag.parse('W/"abc-123"')
    assert strong.weak is False
    assert weak.weak is True
    assert strong.render() == '"abc-123"'
    assert weak.render() == 'W/"abc-123"'

    with pytest.raises(core.ConnectorPrimitiveError):
        core.ETag.parse("abc-123")
    with pytest.raises(core.ConnectorPrimitiveError):
        core.ETag.parse('"unsafe\\value"')


def test_response_header_projection_is_allowlisted_secret_safe_and_immutable():
    projected = core.sanitize_response_headers(
        {
            "ETag": 'W/"source-head"',
            "Last-Modified": "Wed, 06 Aug 2025 12:00:00 GMT",
            "Content-Length": "42",
            "Authorization": "Bearer should-not-survive",
            "X-Internal-Debug": "not allowlisted",
        }
    )
    assert projected == {
        "content-length": "42",
        "etag": 'W/"source-head"',
        "last-modified": "Wed, 06 Aug 2025 12:00:00 GMT",
    }
    assert "should-not-survive" not in repr(projected)
    with pytest.raises(TypeError):
        projected["etag"] = '"mutated"'  # type: ignore[index]

    with pytest.raises(core.ConnectorPrimitiveError):
        core.sanitize_response_headers({"ETag": '"bad\nvalue"'})


def test_source_head_preserves_time_etag_length_revision_and_digest():
    observed_at = datetime(2026, 8, 6, 12, 1, tzinfo=timezone.utc)
    expected_digest = "sha256:" + hashlib.sha256(b"fixture").hexdigest()
    head = core.SourceHeadObservation.from_headers(
        {
            "ETag": 'W/"source-head"',
            "Last-Modified": "Wed, 06 Aug 2025 12:00:00 GMT",
            "Content-Length": "7",
        },
        observed_at=observed_at,
        upstream_revision="release-2025-08-06",
        computed_digest=expected_digest,
    )
    assert head.etag == core.ETag("source-head", weak=True)
    assert head.last_modified == datetime(2025, 8, 6, 12, tzinfo=timezone.utc)
    assert head.content_length == 7
    assert head.upstream_revision == "release-2025-08-06"
    assert head.computed_digest == expected_digest

    with pytest.raises(core.ConnectorPrimitiveError):
        core.SourceHeadObservation.from_headers(
            {"Last-Modified": "Wed, 06 Aug 2027 12:00:00 GMT"},
            observed_at=observed_at,
        )


def test_retry_policy_is_bounded_deterministic_and_fail_closed():
    policy = core.RetryPolicy(
        max_attempts=3,
        base_delay_seconds=2.0,
        multiplier=2.0,
        max_delay_seconds=10.0,
        deadline_seconds=20.0,
        jitter_fraction=0.25,
    )

    first = policy.decide(
        core.TransportCategory.TIMEOUT,
        attempt_number=1,
        elapsed_seconds=1.0,
        jitter_unit=0.5,
    )
    assert first == core.RetryDecision(True, 2.0, 2, "transient_retry")

    rate_limited = policy.decide(
        core.TransportCategory.RATE_LIMITED,
        attempt_number=2,
        elapsed_seconds=5.0,
        retry_after_seconds=8.0,
        jitter_unit=0.5,
    )
    assert rate_limited == core.RetryDecision(True, 8.0, 3, "transient_retry")

    permanent = policy.decide(
        core.TransportCategory.ACCESS_DENIED,
        attempt_number=1,
        elapsed_seconds=1.0,
    )
    assert permanent.retry is False
    assert permanent.reason == "permanent_or_unsafe_failure"

    exhausted = policy.decide(
        core.TransportCategory.TIMEOUT,
        attempt_number=3,
        elapsed_seconds=3.0,
    )
    assert exhausted.retry is False
    assert exhausted.reason == "attempt_limit_reached"

    deadline_hold = policy.decide(
        core.TransportCategory.TIMEOUT,
        attempt_number=1,
        elapsed_seconds=19.0,
        jitter_unit=0.5,
    )
    assert deadline_hold.retry is False
    assert deadline_hold.reason == "deadline_would_be_exceeded"


def test_retry_policy_uses_only_injected_jitter():
    policy = core.RetryPolicy(
        max_attempts=3,
        base_delay_seconds=10.0,
        multiplier=1.0,
        max_delay_seconds=20.0,
        deadline_seconds=60.0,
        jitter_fraction=0.2,
    )
    low = policy.decide(
        core.TransportCategory.TRANSPORT_ERROR,
        attempt_number=1,
        elapsed_seconds=0.0,
        jitter_unit=0.0,
    )
    high = policy.decide(
        core.TransportCategory.TRANSPORT_ERROR,
        attempt_number=1,
        elapsed_seconds=0.0,
        jitter_unit=1.0,
    )
    assert low.delay_seconds == pytest.approx(8.0)
    assert high.delay_seconds == pytest.approx(12.0)


def test_streaming_sha256_is_exact_order_sensitive_and_bounded():
    chunks = [b"abc", bytearray(b"def"), memoryview(b"ghi")]
    result = core.sha256_stream(chunks)
    assert result.byte_length == 9
    assert result.digest == "sha256:" + hashlib.sha256(b"abcdefghi").hexdigest()

    reordered = core.sha256_stream([b"ghi", b"def", b"abc"])
    assert reordered.digest != result.digest

    with pytest.raises(core.ResponseTooLargeError) as exc_info:
        core.sha256_stream([b"1234", b"5678"], max_bytes=7)
    assert exc_info.value.limit == 7
    assert exc_info.value.observed == 8

    with pytest.raises(TypeError):
        core.sha256_stream(["not bytes"])  # type: ignore[list-item]


def test_integrity_mismatch_is_first_class_and_expected_digest_is_preserved():
    expected = "sha256:" + hashlib.sha256(b"expected").hexdigest()
    matched = core.verify_sha256_stream([b"expected"], expected)
    assert matched.status is core.IntegrityStatus.MATCH
    assert matched.expected_digest == expected
    assert matched.observed_digest == expected

    mismatched = core.verify_sha256_stream([b"observed"], expected)
    assert mismatched.status is core.IntegrityStatus.MISMATCH
    assert mismatched.expected_digest == expected
    assert mismatched.observed_digest != expected


def test_diagnostic_redaction_removes_credentials_queries_and_userinfo():
    message = (
        "authorization: Bearer super-secret "
        "api_key=abc123 "
        "https://example.test/path?token=xyz&county=001"
    )
    redacted = core.redact_text(message)
    assert "super-secret" not in redacted
    assert "abc123" not in redacted
    assert "xyz" not in redacted
    assert "county=001" not in redacted
    assert redacted.count("<redacted>") >= 3

    safe_url = core.redact_url(
        "https://user:password@example.test:8443/path/to/object?token=secret#fragment"
    )
    assert safe_url == "https://example.test:8443/path/to/object"
    assert "user" not in safe_url
    assert "password" not in safe_url
    assert "secret" not in safe_url

    with pytest.raises(core.ConnectorPrimitiveError):
        core.redact_url("file:///tmp/source")


def test_failure_detail_is_value_minimized_and_rejects_unredacted_construction():
    detail = core.make_failure_detail(
        core.TransportCategory.ACCESS_DENIED,
        code="SOURCE_ACCESS_DENIED",
        message="Authorization=Bearer top-secret token=abc",
        status_code=403,
        locator="https://user:pw@example.test/data?api_key=secret",
        attempt_count=1,
    )
    assert detail.category is core.TransportCategory.ACCESS_DENIED
    assert "top-secret" not in detail.public_message
    assert "abc" not in detail.public_message
    assert detail.safe_locator == "https://example.test/data"

    with pytest.raises(core.ConnectorPrimitiveError):
        core.FailureDetail(
            category=core.TransportCategory.TIMEOUT,
            code="TIMEOUT",
            public_message="token=leak",
        )


def test_source_module_has_no_network_lifecycle_or_source_specific_dependencies():
    source = (PACKAGE_SRC / "connectors_core/core.py").read_text(encoding="utf-8")
    forbidden_imports = (
        "import requests",
        "import httpx",
        "import aiohttp",
        "import boto3",
        "import socket",
        "import subprocess",
    )
    for token in forbidden_imports:
        assert token not in source

    forbidden_runtime_literals = (
        "data/raw",
        "data/work",
        "data/quarantine",
        "data/processed",
        "data/catalog",
        "data/published",
        "release/",
        "api.k-state.edu",
        "usgs.gov",
    )
    for token in forbidden_runtime_literals:
        assert token not in source
