"""Prove the opt-in synthetic HTTP seam without graduating public routes."""

from __future__ import annotations

from contextlib import contextmanager
from http.client import HTTPConnection
from io import BytesIO
import json
from pathlib import Path
import socket
import threading
import time
from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults

import pytest

from governed_api import local_fixture as local
from governed_api.main import app as default_app
from governed_api.routes.registry import ROUTES
from tools.validators.ui.validate_evidence_drawer_payload import (
    _schema_findings,
    _semantic_findings,
)


def _selection(slug="kansas-frame", scenario="current"):
    historical = scenario in {"stale", "withdrawn"}
    request = {
        "profile": local.SELECTION_PROFILE,
        "selection_id": f"selection:local-http:{slug}:{scenario}",
        "layer_id": f"layer:{slug}",
        "feature_id": f"feature:local-http:{slug}",
        "evidence_refs": [] if historical else [f"kfm:evidence:site-local:{slug}"],
    }
    if historical:
        request["history_evidence_refs"] = [f"kfm:evidence:site-local:{slug}"]
    return request


def _call(raw=None, *, app=None, **updates):
    raw = json.dumps(_selection()).encode() if raw is None else raw
    env = {}
    setup_testing_defaults(env)
    env.update({
        "REQUEST_METHOD": "POST", "PATH_INFO": local.PATH,
        "REMOTE_ADDR": "127.0.0.1", "HTTP_HOST": "127.0.0.1:8765",
        "HTTP_ORIGIN": local.DEFAULT_ORIGIN, "CONTENT_TYPE": "application/json",
        "CONTENT_LENGTH": str(len(raw)), "wsgi.input": BytesIO(raw),
    })
    env.update(updates)
    captured = {}

    def start_response(status, headers):
        captured.update(status=status, headers=dict(headers))

    body = b"".join((app or local.create_app())(env, start_response))
    assert int(captured["headers"]["Content-Length"]) == len(body)
    assert captured["headers"]["Cache-Control"] == "no-store"
    assert captured["headers"]["X-Content-Type-Options"] == "nosniff"
    assert not any(key.lower().startswith("access-control-") for key in captured["headers"])
    return captured["status"], json.loads(body) if body else None, captured["headers"]


def _assert_projection(payload):
    assert _schema_findings(payload) == []
    assert _semantic_findings(payload) == []
    assert "Local synthetic demonstration only" in payload["limitations"][0]
    rendered = json.dumps(payload)
    for marker in ("CANARY", "example.invalid", "secret", "raw/", "quarantine/"):
        assert marker not in rendered


@pytest.mark.parametrize("slug", ["kansas-frame", "county-locators"])
@pytest.mark.parametrize("scenario,outcome,reason", [
    ("current", "ANSWER", "SUPPORTED"),
    ("stale", "ABSTAIN", "STALE_EVIDENCE"),
    ("withdrawn", "ABSTAIN", "WITHDRAWN_EVIDENCE"),
    ("missing", "ABSTAIN", "MISSING_EVIDENCE"),
    ("denied", "DENY", "POLICY_DENIED"),
    ("error", "ERROR", "UPSTREAM_ERROR"),
])
def test_fixed_selections_have_canonical_finite_responses(slug, scenario, outcome, reason):
    status, payload, headers = _call(json.dumps(_selection(slug, scenario)).encode())
    assert status == ("503 Service Unavailable" if scenario == "error" else "200 OK")
    assert headers["X-KFM-Local-Fixture"] == "synthetic-only"
    assert (payload["outcome"], payload["reason_code"]) == (outcome, reason)
    assert payload["id"] == f"kfm:ui:evidence-drawer:local-http:{slug}:{scenario}"
    _assert_projection(payload)
    if scenario == "current":
        assert payload["evidence_refs"] == [f"kfm:evidence:site-local:{slug}"]
        assert "/blob/9dcdaec2cacbbf9880bd613b546a7314a2673ac5/" in payload["citations"][0]["href"]
    if scenario in {"denied", "error", "missing"}:
        assert payload["evidence_refs"] == payload["citations"] == []
        assert payload["history"] == {"negative_outcomes": [], "corrections": []}
    if scenario == "withdrawn":
        assert payload["evidence_refs"] == []
        assert payload["history"]["negative_outcomes"][0]["resolvable_as_current"] is False


@pytest.mark.parametrize("change", [
    {"feature_id": "feature:other"}, {"layer_id": "layer:other"},
    {"selection_id": "selection:other"}, {"evidence_refs": ["kfm:evidence:secret"]},
    {"history_evidence_refs": ["kfm:evidence:secret"]},
])
def test_unbound_tuple_fails_closed_without_echo(change):
    request = _selection()
    request.update(change)
    status, payload, _ = _call(json.dumps(request).encode())
    assert status == "404 Not Found"
    assert payload["reason_code"] == "MISSING_EVIDENCE"
    assert payload["evidence_refs"] == []
    _assert_projection(payload)


@pytest.mark.parametrize("raw", [
    b"{", b"[]", b"null", b"\xff", b'{"profile":NaN}', b'{"profile":1e400}',
    b'{"profile":1}', b'{"profile":"a","profile":"b"}',
    ("[" * 2000 + "]" * 2000).encode(),
    json.dumps({**_selection(), "path": "/secret/input"}).encode(),
    json.dumps({**_selection(), "profile": "wrong"}).encode(),
    json.dumps({**_selection(), "evidence_refs": ["x"] * 17}).encode(),
    json.dumps({**_selection(), "evidence_refs": ["x", "x"]}).encode(),
    json.dumps({**_selection(), "evidence_refs": [True]}).encode(),
    json.dumps({**_selection(), "feature_id": "x" * 161}).encode(),
    json.dumps({**_selection(), "history_evidence_refs": "secret"}).encode(),
])
def test_malformed_bounded_input_has_safe_error(raw):
    status, payload, _ = _call(raw)
    assert status == "400 Bad Request"
    assert payload["outcome"] == "ERROR"
    _assert_projection(payload)


@pytest.mark.parametrize("update,status", [
    ({"HTTP_HOST": "attacker.invalid:8765"}, "403 Forbidden"),
    ({"REMOTE_ADDR": "192.0.2.1"}, "403 Forbidden"),
    ({"HTTP_ORIGIN": None}, "403 Forbidden"),
    ({"HTTP_ORIGIN": "null"}, "403 Forbidden"),
    ({"HTTP_ORIGIN": "http://attacker.invalid"}, "403 Forbidden"),
    ({"HTTP_SEC_FETCH_SITE": "cross-site"}, "403 Forbidden"),
    ({"HTTP_COOKIE": "secret=token"}, "403 Forbidden"),
    ({"HTTP_AUTHORIZATION": "Bearer secret"}, "403 Forbidden"),
    ({"PATH_INFO": "/evidence"}, "404 Not Found"),
    ({"QUERY_STRING": "path=secret"}, "404 Not Found"),
    ({"REQUEST_METHOD": "GET"}, "405 Method Not Allowed"),
    ({"REQUEST_METHOD": "OPTIONS"}, "405 Method Not Allowed"),
    ({"CONTENT_TYPE": "text/plain"}, "415 Unsupported Media Type"),
    ({"HTTP_TRANSFER_ENCODING": "chunked"}, "400 Bad Request"),
    ({"HTTP_CONTENT_ENCODING": "gzip"}, "400 Bad Request"),
    ({"CONTENT_LENGTH": ""}, "411 Length Required"),
    ({"CONTENT_LENGTH": "-1"}, "411 Length Required"),
    ({"CONTENT_LENGTH": "secret"}, "411 Length Required"),
    ({"CONTENT_LENGTH": "0"}, "413 Content Too Large"),
    ({"CONTENT_LENGTH": str(local.MAX_REQUEST_BYTES + 1)}, "413 Content Too Large"),
    ({"CONTENT_LENGTH": "999"}, "400 Bad Request"),
])
def test_http_boundary_rejections_are_safe(update, status):
    observed, payload, _ = _call(**update)
    assert observed == status
    assert payload["outcome"] in {"ERROR", "ABSTAIN"}
    _assert_projection(payload)


def test_rejections_do_not_read_body_and_read_errors_are_safe():
    class BrokenInput:
        def read(self, _size):
            raise OSError("secret read failure")
    assert _call(**{"wsgi.input": BrokenInput()})[0] == "400 Bad Request"
    assert _call(CONTENT_LENGTH="16385", **{"wsgi.input": BrokenInput()})[0] == "413 Content Too Large"


def test_health_has_no_data_and_does_not_relax_data_origin_check():
    status, body, _ = _call(REQUEST_METHOD="GET", PATH_INFO=local.HEALTH_PATH, HTTP_ORIGIN=None)
    assert (status, body) == ("204 No Content", None)
    assert _call(REQUEST_METHOD="GET", PATH_INFO=local.HEALTH_PATH, HTTP_ORIGIN="null")[0] == "403 Forbidden"
    assert _call(HTTP_ORIGIN=None)[0] == "403 Forbidden"


@pytest.mark.parametrize("kwargs", [
    {"port": 0}, {"port": 65536}, {"port": True},
    {"allowed_origin": "https://127.0.0.1:4173"},
    {"allowed_origin": "http://localhost:4173"},
    {"allowed_origin": "http://127.0.0.1:4173/path"},
    {"allowed_origin": "http://user@127.0.0.1:4173"},
    {"allowed_origin": "http://127.0.0.1:4173/"},
    {"allowed_origin": "http://127.0.0.1:99999"},
])
def test_factory_refuses_noncanonical_trusted_configuration(kwargs):
    with pytest.raises(ValueError):
        local.create_app(**kwargs)


@contextmanager
def _http_server():
    server = make_server("127.0.0.1", 0, local.create_app(), handler_class=local._LocalRequestHandler)
    server.set_app(local.create_app(port=server.server_port, allowed_origin="http://127.0.0.1:4174"))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_port
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def test_real_http_listener_serves_bound_safe_projection_and_preserves_origin(capsys):
    with _http_server() as port:
        connection = HTTPConnection("127.0.0.1", port, timeout=3)
        connection.request("GET", local.HEALTH_PATH)
        health = connection.getresponse()
        assert health.status == 204
        assert health.read() == b""
        for scenario in ("current", "withdrawn", "denied", "error"):
            connection.request("POST", local.PATH, json.dumps(_selection("county-locators", scenario)), {
                "Origin": "http://127.0.0.1:4174", "Content-Type": "application/json",
            })
            response = connection.getresponse()
            assert response.status == (503 if scenario == "error" else 200)
            body = response.read()
            assert int(response.getheader("Content-Length")) == len(body)
            _assert_projection(json.loads(body))
        connection.request("POST", local.PATH, b"secret", {"Content-Type": "application/json"})
        response = connection.getresponse()
        assert response.status == 403
        assert b"secret" not in response.read()
        connection.close()
    assert "secret" not in capsys.readouterr().err


def test_http_parser_failure_does_not_echo_request_line(capsys):
    with _http_server() as port:
        with socket.create_connection(("127.0.0.1", port), timeout=1) as connection:
            connection.sendall(b"POST /__local__/evidence secret-request-value\r\n\r\n")
            chunks = []
            while chunk := connection.recv(8192):
                chunks.append(chunk)
            response = b"".join(chunks)
            assert b"secret-request-value" not in response
            # Bad HTTP versions can be treated as HTTP/0.9 by the base parser;
            # even then, the returned body is our fixed safe projection.
            body = response.split(b"\r\n\r\n", 1)[-1]
            _assert_projection(json.loads(body))
            assert json.loads(body)["outcome"] == "ERROR"
    assert capsys.readouterr().err == ""


@pytest.mark.parametrize("phase", ["headers", "body"])
def test_total_deadline_ends_trickled_requests_and_releases_worker(monkeypatch, capsys, phase):
    monkeypatch.setattr(local, "REQUEST_DEADLINE_SECONDS", 0.3)
    monkeypatch.setattr(local, "READ_TIMEOUT_SECONDS", 2)
    with _http_server() as port:
        with socket.create_connection(("127.0.0.1", port), timeout=1) as stalled:
            stalled.settimeout(0.025)
            started = time.monotonic()
            if phase == "body":
                stalled.sendall((
                    f"POST {local.PATH} HTTP/1.1\r\nHost: 127.0.0.1:{port}\r\n"
                    "Origin: http://127.0.0.1:4174\r\nContent-Type: application/json\r\n"
                    "Content-Length: 500\r\n\r\n"
                ).encode())
            else:
                stalled.sendall(f"POST {local.PATH} HTTP/1.1\r\nX-Secret: ".encode())
            closed = False
            # Each byte arrives well before the idle timeout. Only the total
            # deadline can release this worker within the asserted interval.
            while time.monotonic() - started < 1:
                try:
                    stalled.sendall(b"x")
                    if stalled.recv(1) == b"":
                        closed = True
                        break
                except (BrokenPipeError, ConnectionResetError):
                    closed = True
                    break
                except TimeoutError:
                    pass
                time.sleep(0.015)
            assert closed
            assert time.monotonic() - started < 0.9
        connection = HTTPConnection("127.0.0.1", port, timeout=1)
        connection.request("POST", local.PATH, json.dumps(_selection()), {
            "Origin": "http://127.0.0.1:4174", "Content-Type": "application/json",
        })
        response = connection.getresponse()
        assert response.status == 200
        _assert_projection(json.loads(response.read()))
        connection.close()
    assert capsys.readouterr().err == ""


def test_default_public_api_stays_negative_and_local_path_unregistered():
    assert set(ROUTES) == {"/bootstrap", "/layers", "/evidence"}
    for path in ROUTES:
        status, payload, _ = _call(app=default_app, PATH_INFO=path, REQUEST_METHOD="GET")
        assert status == "200 OK"
        assert (payload["outcome"], payload["reason_code"]) == ("ABSTAIN", "NOT_IMPLEMENTED")
    assert _call(app=default_app)[0] == "404 Not Found"


def test_profiles_remain_the_existing_frontend_profiles():
    root = Path(__file__).resolve().parents[3]
    assert f'"{local.SELECTION_PROFILE}"' in (root / "packages/maplibre/src/map-runtime-port.ts").read_text()
    assert f'"{local.DRAWER_PROFILE}"' in (root / "apps/explorer-web/src/adapters/GovernedClient.ts").read_text()
