"""Successful GET, HEAD, and not-modified behavior."""
from __future__ import annotations

import hashlib

from _support import Clock, FakeTransport, core, request, response, run


def test_success_preserves_exact_bytes_digest_source_head_and_no_authority():
    clock, body = Clock(), (b'{"a":', b"1}")
    expected = "sha256:" + hashlib.sha256(b'{"a":1}').hexdigest()
    fake = FakeTransport(clock, response(body=body))
    result = run(fake, request(expected_digest=expected), clock=clock)
    assert result.category is core.TransportCategory.SUCCESS
    assert result.payload and result.payload.chunks == body and result.payload.digest == expected
    assert (result.payload.byte_length, result.payload.media_type) == (7, "application/json")
    assert result.source_head and result.source_head.computed_digest == expected
    assert result.attempts[0].safe_locator == "https://source.example.test/data"
    sent_request, timeout_seconds, max_bytes, allow_redirects = fake.calls[0]
    assert sent_request.method.value == "GET"
    assert timeout_seconds == 5.0 and max_bytes == 64 and allow_redirects is False
    assert not result.authority_created and not result.repository_mutation_allowed


def test_head_and_not_modified_are_metadata_only():
    clock = Clock()
    head = run(FakeTransport(clock, response(body=())), request(method="HEAD"), clock=clock)
    assert head.category is core.TransportCategory.SUCCESS and head.payload is None and head.source_head
    unchanged = run(
        FakeTransport(clock, response(304, body=(), headers={"Content-Length": "0"})),
        clock=clock,
    )
    assert unchanged.category is core.TransportCategory.NOT_MODIFIED
    assert unchanged.payload is None and unchanged.failure is None
