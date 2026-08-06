"""Fail-closed status, redirect, media, size, length, and integrity behavior."""
from __future__ import annotations

import hashlib

import pytest

from _support import Clock, FakeTransport, core, request, response, run


@pytest.mark.parametrize(
    "reply,category,code,count",
    [
        (response(403, body=(), headers={"Content-Length": "0"}), core.TransportCategory.ACCESS_DENIED, "ACCESS_DENIED", 1),
        (response(302, body=(), headers={"Content-Length": "0"}), core.TransportCategory.UNSAFE_METADATA, "REDIRECT_BLOCKED", 1),
        (response(206, body=(b"partial",)), core.TransportCategory.RETRY_EXHAUSTED, "RETRY_EXHAUSTED", 3),
        (response(headers={"Content-Type": "text/html"}), core.TransportCategory.INVALID_RESPONSE_METADATA, "WRONG_MEDIA_TYPE", 1),
        (response(complete=False), core.TransportCategory.RETRY_EXHAUSTED, "RETRY_EXHAUSTED", 3),
    ],
)
def test_access_redirect_media_and_partial_fail_closed(reply, category, code, count):
    clock = Clock()
    result = run(FakeTransport(clock, *([reply] * count)), clock=clock)
    assert result.category is category and result.failure and result.failure.code == code
    assert result.payload is None


@pytest.mark.parametrize(
    "reply,req,category,code",
    [
        (response(body=(b"x" * 65,), headers={"Content-Length": "65"}), request(), core.TransportCategory.RESPONSE_TOO_LARGE, "DECLARED_RESPONSE_TOO_LARGE"),
        (response(body=(b"observed",)), request(expected_digest="sha256:" + hashlib.sha256(b"expected").hexdigest()), core.TransportCategory.INTEGRITY_MISMATCH, "INTEGRITY_MISMATCH"),
        (response(body=(b"abc",), headers={"Content-Length": "4"}), request(), core.TransportCategory.INVALID_RESPONSE_METADATA, "CONTENT_LENGTH_MISMATCH"),
    ],
)
def test_size_length_and_integrity_fail_without_payload(reply, req, category, code):
    clock = Clock()
    result = run(FakeTransport(clock, reply), req, clock=clock)
    assert result.category is category and result.failure and result.failure.code == code
    assert result.payload is None
