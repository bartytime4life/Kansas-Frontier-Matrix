from __future__ import annotations

import ipaddress
import json
import os
from collections.abc import Mapping
from wsgiref.simple_server import make_server

from governed_api.routes.registry import ROUTES
from governed_api.stub import make_error_envelope

DEFAULT_BIND = "127.0.0.1"
DEFAULT_PORT = 8000


def _json_response(start_response, status: str, payload: dict):
    body = json.dumps(payload).encode("utf-8")
    headers = [("Content-Type", "application/json"), ("Content-Length", str(len(body)))]
    start_response(status, headers)
    return [body]


def app(environ, start_response):
    path = environ.get("PATH_INFO", "")
    method = environ.get("REQUEST_METHOD", "GET")

    if path in ROUTES and method != "GET":
        return _json_response(
            start_response,
            "405 Method Not Allowed",
            make_error_envelope("method-not-allowed"),
        )

    if method == "GET" and path in ROUTES:
        return _json_response(start_response, "200 OK", ROUTES[path]())

    return _json_response(
        start_response,
        "404 Not Found",
        make_error_envelope("route-not-found"),
    )


def _is_supported_loopback(host: str) -> bool:
    if host == "localhost":
        return True
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        return False
    return address.version == 4 and address.is_loopback


def resolve_server_address(
    environment: Mapping[str, str] | None = None,
) -> tuple[str, int]:
    """Resolve the local server address without permitting network exposure."""

    values = os.environ if environment is None else environment
    host = values.get("KFM_API_BIND", DEFAULT_BIND).strip()
    raw_port = values.get("KFM_API_PORT", str(DEFAULT_PORT)).strip()

    if not host:
        raise ValueError("KFM_API_BIND must not be empty")
    if not _is_supported_loopback(host):
        raise ValueError("KFM_API_BIND must be localhost or an IPv4 loopback address")
    if not raw_port.isascii() or not raw_port.isdecimal():
        raise ValueError("KFM_API_PORT must be an integer from 1 through 65535")

    port = int(raw_port)
    if not 1 <= port <= 65535:
        raise ValueError("KFM_API_PORT must be an integer from 1 through 65535")
    return host, port


def serve(host: str = DEFAULT_BIND, port: int = DEFAULT_PORT) -> None:
    if not _is_supported_loopback(host):
        raise ValueError("governed API may bind only to a supported loopback address")
    if isinstance(port, bool) or not isinstance(port, int) or not 1 <= port <= 65535:
        raise ValueError("governed API port must be an integer from 1 through 65535")

    with make_server(host, port, app) as server:
        server.serve_forever()


def main() -> None:
    try:
        host, port = resolve_server_address()
    except ValueError as error:
        raise SystemExit(f"KFM_API_CONFIG_ERROR: {error}") from error

    print(f"KFM Governed API listening on http://{host}:{port}/", flush=True)
    serve(host, port)


if __name__ == "__main__":
    main()
