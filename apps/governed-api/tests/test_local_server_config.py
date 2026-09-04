from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from governed_api.main import DEFAULT_BIND, DEFAULT_PORT, resolve_server_address, serve

REPO_ROOT = Path(__file__).resolve().parents[3]


def _example_value(name: str) -> str:
    text = (REPO_ROOT / ".env.example").read_text(encoding="utf-8")
    match = re.search(rf"^{re.escape(name)}=(.+)$", text, re.MULTILINE)
    assert match is not None, f"{name} is missing from .env.example"
    return match.group(1).strip()


def test_source_fallback_remains_loopback_and_compatible() -> None:
    assert DEFAULT_BIND == "127.0.0.1"
    assert DEFAULT_PORT == 8000
    assert resolve_server_address({}) == (DEFAULT_BIND, DEFAULT_PORT)


def test_local_package_command_matches_environment_template() -> None:
    bind = _example_value("KFM_API_BIND")
    port = _example_value("KFM_API_PORT")
    scripts = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))[
        "scripts"
    ]
    command = scripts["local:api"]

    assert f"KFM_API_BIND={bind}" in command
    assert f"KFM_API_PORT={port}" in command
    assert resolve_server_address({"KFM_API_BIND": bind, "KFM_API_PORT": port}) == (
        bind,
        int(port),
    )


@pytest.mark.parametrize("host", ["127.0.0.1", "127.0.0.2", "localhost"])
def test_local_loopback_bindings_are_accepted(host: str) -> None:
    assert resolve_server_address({"KFM_API_BIND": host, "KFM_API_PORT": "8081"}) == (
        host,
        8081,
    )


@pytest.mark.parametrize(
    "host",
    ["", "0.0.0.0", "192.168.1.5", "example.com", "::", "::1"],
)
def test_non_supported_bindings_fail_closed(host: str) -> None:
    with pytest.raises(ValueError, match="KFM_API_BIND"):
        resolve_server_address({"KFM_API_BIND": host, "KFM_API_PORT": "8080"})


@pytest.mark.parametrize("port", ["", "0", "65536", "eight", "8.5", "-1", "٨٠٨٠"])
def test_invalid_ports_fail_closed(port: str) -> None:
    with pytest.raises(ValueError, match="KFM_API_PORT"):
        resolve_server_address({"KFM_API_BIND": "127.0.0.1", "KFM_API_PORT": port})


def test_serve_rejects_exposure_before_constructing_server() -> None:
    with pytest.raises(ValueError, match="loopback"):
        serve("0.0.0.0", 8080)
    with pytest.raises(ValueError, match="port"):
        serve("127.0.0.1", 0)
