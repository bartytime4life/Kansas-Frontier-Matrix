import json
from wsgiref.simple_server import make_server

from governed_api.routes.registry import ROUTES
from governed_api.stub import make_error_envelope


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


def serve(host: str = "127.0.0.1", port: int = 8000) -> None:
    with make_server(host, port, app) as server:
        server.serve_forever()


if __name__ == "__main__":
    serve()
