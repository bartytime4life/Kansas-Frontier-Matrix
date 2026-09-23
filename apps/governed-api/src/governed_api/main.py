import json
from wsgiref.simple_server import make_server

from governed_api.routes.registry import ROUTES
from governed_api.stub import invoke_sync_fixture_operation, make_error_envelope


# Transport status for each guarded failure class. Only defects map to 500:
# a timeout or cancellation is an expected, finite negative state, so it must
# not be reported as a generic server failure (and cancellation stays ABSTAIN).
_FAILURE_STATUS = {
    "timeout": "504 Gateway Timeout",
    "cancellation": "503 Service Unavailable",
    "invalid_response": "500 Internal Server Error",
    "internal_defect": "500 Internal Server Error",
}

# Negative envelopes are request-specific and must not be cached or sniffed.
_BASE_HEADERS = (
    ("Cache-Control", "no-store"),
    ("X-Content-Type-Options", "nosniff"),
)


def _json_response(start_response, status: str, payload: dict, extra_headers=()):
    body = json.dumps(payload).encode("utf-8")
    headers = [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(body))),
        *_BASE_HEADERS,
        *extra_headers,
    ]
    start_response(status, headers)
    return [body]


def _transport_status(payload: dict, failure_kind: str | None) -> str:
    if failure_kind is not None:
        return _FAILURE_STATUS.get(failure_kind, "500 Internal Server Error")
    if payload["outcome"] == "ERROR":
        return "500 Internal Server Error"
    return "200 OK"


def app(environ, start_response):
    path = environ.get("PATH_INFO", "")
    method = environ.get("REQUEST_METHOD", "GET")

    if path in ROUTES and method != "GET":
        return _json_response(
            start_response,
            "405 Method Not Allowed",
            make_error_envelope("method-not-allowed"),
            extra_headers=(("Allow", "GET"),),
        )

    if method == "GET" and path in ROUTES:
        payload, failure_kind = invoke_sync_fixture_operation(
            ROUTES[path],
            environ.get("kfm.correlation_id", "unavailable"),
        )
        return _json_response(
            start_response, _transport_status(payload, failure_kind), payload
        )

    return _json_response(
        start_response,
        "404 Not Found",
        make_error_envelope("route-not-found"),
    )


def serve(host: str = "127.0.0.1", port: int = 8000) -> None:
    with make_server(host, port, app) as server:
        server.serve_forever()


if __name__ == "__main__":
    serve()
