import json
from wsgiref.simple_server import make_server

from governed_api.routes.registry import ROUTES


def app(environ, start_response):
    path = environ.get("PATH_INFO", "")
    method = environ.get("REQUEST_METHOD", "GET")

    if path in ROUTES and method != "GET":
        body = b'{"detail":"Method Not Allowed"}'
        start_response("405 Method Not Allowed", [("Content-Type", "application/json"), ("Content-Length", str(len(body)))])
        return [body]

    if method == "GET" and path in ROUTES:
        payload = ROUTES[path]()
        body = json.dumps(payload).encode("utf-8")
        headers = [("Content-Type", "application/json"), ("Content-Length", str(len(body)))]
        start_response("200 OK", headers)
        return [body]

    body = b'{"detail":"Not Found"}'
    start_response("404 Not Found", [("Content-Type", "application/json"), ("Content-Length", str(len(body)))])
    return [body]


def serve(host: str = "127.0.0.1", port: int = 8000) -> None:
    with make_server(host, port, app) as server:
        server.serve_forever()


if __name__ == "__main__":
    serve()
