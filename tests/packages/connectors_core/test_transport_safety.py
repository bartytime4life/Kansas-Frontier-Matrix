"""Import, profile, redaction, and static-boundary tests."""
from __future__ import annotations

import importlib
import socket
from unittest.mock import patch

import pytest

from _support import SRC, profile, request, transport


def test_import_profile_and_repr_are_side_effect_free_exact_host_and_secret_safe(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    before = list(tmp_path.iterdir())
    boom = AssertionError("ambient network")
    with (
        patch.object(socket.socket, "connect", side_effect=boom),
        patch.object(socket.socket, "connect_ex", side_effect=boom),
        patch.object(socket, "create_connection", side_effect=boom),
        patch.object(socket, "getaddrinfo", side_effect=boom),
    ):
        assert importlib.import_module("connectors_core.transport") is transport
    assert list(tmp_path.iterdir()) == before
    assert not hasattr(transport, "HttpTransport")

    req, prof = request(), profile()
    prof.validate_request(req)
    assert req.safe_locator == "https://source.example.test/data"
    assert req.header_names == ("accept", "authorization")
    assert all(token not in repr(req) for token in ("fixture-secret", "token=secret", "county=001"))
    with pytest.raises(TypeError):
        req.headers["accept"] = "text/plain"  # type: ignore[index]
    with pytest.raises(transport.TransportInputError):
        prof.validate_request(transport.TransportRequest("GET", "https://other.example.test/data"))
    with pytest.raises(transport.TransportInputError):
        transport.TransportRequest("GET", "https://user:secret@source.example.test/data")


def test_module_family_has_no_live_client_source_endpoint_or_lifecycle_dependency():
    source = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((SRC / "connectors_core").glob("*transport*.py"))
    )
    forbidden = (
        "import requests", "import httpx", "import aiohttp", "import urllib.request",
        "import socket", "import subprocess", "import boto3", "data/raw", "data/work",
        "data/quarantine", "data/processed", "data/catalog", "data/published", "release/",
        "api.k-state.edu", "usgs.gov",
    )
    assert all(token not in source for token in forbidden)
