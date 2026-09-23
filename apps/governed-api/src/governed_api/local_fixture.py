"""Opt-in loopback transport for existing synthetic Explorer projections.

This app is deliberately separate from the default negative-only API. It owns
no evidence repository or policy/release authority. The fixed trust labels are
synthetic UI test states, never decisions about a source or a release.
"""

from __future__ import annotations

import argparse
import json
import re
import socket
import threading
from types import MappingProxyType
from urllib.parse import urlsplit
from wsgiref.simple_server import WSGIRequestHandler, make_server


PATH = "/__local__/evidence"
HEALTH_PATH = "/__local__/health"
SELECTION_PROFILE = "kfm.explorer.map-feature-selection.v1"
DRAWER_PROFILE = "kfm.explorer.evidence-drawer.public-safe.v1"
DEFAULT_PORT = 8765
DEFAULT_ORIGIN = "http://127.0.0.1:4173"
MAX_REQUEST_BYTES = 16 * 1024
MAX_RESPONSE_BYTES = 16 * 1024
READ_TIMEOUT_SECONDS = 3
REQUEST_DEADLINE_SECONDS = 3
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}\Z")
_REQUIRED = frozenset({"profile", "selection_id", "layer_id", "feature_id", "evidence_refs"})
_ALLOWED = _REQUIRED | {"history_evidence_refs"}
_SCENARIOS = ("current", "stale", "withdrawn", "missing", "denied", "error")
_LAYERS = MappingProxyType({
    "kansas-frame": "Generalized Kansas extent",
    "county-locators": "County locator starter points",
})
_CITATION = (
    "https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/"
    "9dcdaec2cacbbf9880bd613b546a7314a2673ac5/"
    "apps/explorer-web/src/features/living_atlas/registry.ts"
)
_DISCLOSURE = (
    "Local synthetic demonstration only; trust labels simulate UI states. "
    "No evidence, policy, review, release, or publication authority is established."
)


def _projection(scenario: str, slug: str | None = None) -> dict:
    """Build only server-authored, public-safe synthetic text and references."""
    outcome, reason, summary = {
        "current": ("ANSWER", "SUPPORTED", "This synthetic layer supports an interface demonstration only."),
        "stale": ("ABSTAIN", "STALE_EVIDENCE", "The synthetic evidence is stale and cannot support a current claim."),
        "withdrawn": ("ABSTAIN", "WITHDRAWN_EVIDENCE", "The synthetic evidence is withdrawn and retained only as audit history."),
        "missing": ("ABSTAIN", "MISSING_EVIDENCE", "No eligible synthetic evidence is available for this selection."),
        "denied": ("DENY", "POLICY_DENIED", "This synthetic selection is denied. No protected detail is exposed."),
        "error": ("ERROR", "UPSTREAM_ERROR", "The local synthetic evidence service could not complete this request."),
    }[scenario]
    ref = f"kfm:evidence:site-local:{slug}" if slug is not None else None
    supported = scenario == "current"
    title = f"Synthetic {_LAYERS[slug]}" if supported and slug in _LAYERS else "Local synthetic evidence"
    payload = {
        "profile": DRAWER_PROFILE,
        "id": f"kfm:ui:evidence-drawer:local-http:{slug or 'unavailable'}:{scenario}",
        "outcome": outcome,
        "reason_code": reason,
        "title": title,
        "summary": summary,
        "evidence_refs": [ref] if supported or scenario == "stale" else [],
        "citations": [{"label": "Repository synthetic layer declaration", "href": _CITATION}] if supported else [],
        "limitations": [_DISCLOSURE],
        "trust_state": {
            "source_role": "context",
            "policy": "ALLOW" if supported else outcome,
            "review": "REVIEWED" if supported or scenario in {"stale", "withdrawn"} else "PENDING",
            "release": "WITHDRAWN" if scenario == "withdrawn" else "RELEASED" if supported or scenario == "stale" else "UNRELEASED",
            "freshness": "CURRENT" if supported else "STALE" if scenario == "stale" else "UNKNOWN",
            "correction": "NONE",
        },
        "history": {"negative_outcomes": [], "corrections": []},
    }
    if scenario == "withdrawn":
        payload["history"]["negative_outcomes"] = [{
            "evidence_ref": ref,
            "state": "WITHDRAWN",
            "reason_code": "WITHDRAWN_EVIDENCE",
            "recorded_at": "2026-09-01T00:00:00Z",
            "visible_in_runtime": True,
            "resolvable_as_current": False,
        }]
    return payload


def _encode_projection(scenario: str, slug: str | None = None) -> bytes:
    # This transport has a narrower closed response domain than the canonical
    # schema: only these server-authored projections may be serialized. Canonical
    # schema and cross-field validation are exercised against every response in
    # tests; no client/provider payload can be used as the response object.
    if scenario not in _SCENARIOS or (slug is not None and slug not in _LAYERS):
        raise ValueError("unsupported synthetic projection")
    if slug is None and scenario not in {"missing", "error"}:
        raise ValueError("synthetic layer required")
    body = json.dumps(_projection(scenario, slug), sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    if len(body) > MAX_RESPONSE_BYTES:
        raise ValueError("synthetic response exceeds transport bound")
    return body


# Immutable, fully assembled bytes keep request input out of response creation.
_RESPONSES = MappingProxyType({
    (slug, scenario): _encode_projection(scenario, slug)
    for slug in _LAYERS for scenario in _SCENARIOS
})
_ERROR = _encode_projection("error")
_MISSING = _encode_projection("missing")


def _request_key(value: object) -> tuple[str, str] | None:
    if type(value) is not dict or not _REQUIRED.issubset(value) or not set(value).issubset(_ALLOWED):
        raise ValueError("invalid selection")
    if value["profile"] != SELECTION_PROFILE:
        raise ValueError("invalid selection")
    if any(type(value[field]) is not str or _SAFE_ID.fullmatch(value[field]) is None
           for field in ("selection_id", "layer_id", "feature_id")):
        raise ValueError("invalid selection")
    current = value["evidence_refs"]
    history = value.get("history_evidence_refs", [])
    if type(current) is not list or type(history) is not list:
        raise ValueError("invalid selection")
    refs = current + history
    if len(refs) > 16 or any(type(ref) is not str or _SAFE_ID.fullmatch(ref) is None for ref in refs):
        raise ValueError("invalid selection")
    if len(set(refs)) != len(refs):
        raise ValueError("invalid selection")
    for slug in _LAYERS:
        if value["layer_id"] != f"layer:{slug}" or value["feature_id"] != f"feature:local-http:{slug}":
            continue
        ref = f"kfm:evidence:site-local:{slug}"
        for scenario in _SCENARIOS:
            historical = scenario in {"stale", "withdrawn"}
            if (value["selection_id"] == f"selection:local-http:{slug}:{scenario}"
                    and current == ([] if historical else [ref])
                    and history == ([ref] if historical else [])):
                return slug, scenario
    return None


def _object_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _reject_number(_value):
    # The existing selection shape contains no numbers, at any nesting level.
    raise ValueError("number not permitted")


def _response(start_response, status: str, body: bytes, extra_headers=()):
    start_response(status, [
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Length", str(len(body))),
        ("Cache-Control", "no-store"),
        ("X-Content-Type-Options", "nosniff"),
        ("X-KFM-Local-Fixture", "synthetic-only"),
        *extra_headers,
    ])
    return [body]


def create_app(*, port: int = DEFAULT_PORT, allowed_origin: str = DEFAULT_ORIGIN):
    """Trusted startup configuration only; request fields cannot override it."""
    if type(port) is not int or not 1 <= port <= 65535:
        raise ValueError("loopback port required")
    if type(allowed_origin) is not str:
        raise ValueError("loopback origin required")
    origin = urlsplit(allowed_origin)
    try:
        origin_port = origin.port
    except ValueError:
        raise ValueError("loopback origin required") from None
    if (origin.scheme != "http" or origin.hostname != "127.0.0.1"
            or origin_port is None or not 1 <= origin_port <= 65535
            or allowed_origin != f"http://127.0.0.1:{origin_port}"):
        raise ValueError("loopback origin required")
    expected_host = f"127.0.0.1:{port}"

    def app(environ, start_response):
        if (environ.get("REMOTE_ADDR") != "127.0.0.1"
                or environ.get("HTTP_HOST") != expected_host
                or environ.get("HTTP_AUTHORIZATION") or environ.get("HTTP_COOKIE")
                or environ.get("HTTP_SEC_FETCH_SITE") == "cross-site"):
            return _response(start_response, "403 Forbidden", _ERROR)
        # A non-browser readiness probe has no Origin. This exception exposes
        # only an empty 204; every data request still requires the exact Origin.
        if (environ.get("PATH_INFO") == HEALTH_PATH
                and environ.get("REQUEST_METHOD") == "GET"
                and not environ.get("QUERY_STRING", "")
                and environ.get("HTTP_ORIGIN") in {None, allowed_origin}):
            return _response(start_response, "204 No Content", b"")
        if environ.get("HTTP_ORIGIN") != allowed_origin:
            return _response(start_response, "403 Forbidden", _ERROR)
        if environ.get("PATH_INFO") != PATH or environ.get("QUERY_STRING", ""):
            return _response(start_response, "404 Not Found", _MISSING)
        if environ.get("REQUEST_METHOD") != "POST":
            return _response(start_response, "405 Method Not Allowed", _ERROR, (("Allow", "POST"),))
        if environ.get("CONTENT_TYPE", "").lower() not in {"application/json", "application/json; charset=utf-8"}:
            return _response(start_response, "415 Unsupported Media Type", _ERROR)
        if environ.get("HTTP_TRANSFER_ENCODING") or environ.get("HTTP_CONTENT_ENCODING"):
            return _response(start_response, "400 Bad Request", _ERROR)
        size_text = environ.get("CONTENT_LENGTH", "")
        if type(size_text) is not str or re.fullmatch(r"[0-9]{1,5}", size_text) is None:
            return _response(start_response, "411 Length Required", _ERROR)
        size = int(size_text)
        if not 0 < size <= MAX_REQUEST_BYTES:
            return _response(start_response, "413 Content Too Large", _ERROR)
        try:
            raw = environ["wsgi.input"].read(size)
            if type(raw) is not bytes or len(raw) != size:
                raise ValueError("incomplete request")
            value = json.loads(raw.decode("utf-8"), object_pairs_hook=_object_pairs,
                               parse_constant=_reject_number, parse_float=_reject_number,
                               parse_int=_reject_number)
            key = _request_key(value)
        except (ValueError, UnicodeError, RecursionError, KeyError, TypeError, OSError):
            return _response(start_response, "400 Bad Request", _ERROR)
        if key is None:
            return _response(start_response, "404 Not Found", _MISSING)
        status = "503 Service Unavailable" if key[1] == "error" else "200 OK"
        return _response(start_response, status, _RESPONSES[key])

    return app


class _LocalRequestHandler(WSGIRequestHandler):
    def setup(self):
        self.request.settimeout(READ_TIMEOUT_SECONDS)
        super().setup()
        # An idle timeout alone lets a trickling request occupy the single
        # development worker indefinitely. The timer covers header parsing,
        # body reads, application execution, and response writes together.
        self._deadline_timer = threading.Timer(
            REQUEST_DEADLINE_SECONDS, self._expire_connection
        )
        self._deadline_timer.daemon = True
        self._deadline_timer.start()

    def _expire_connection(self):
        try:
            self.connection.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass  # A completed/closed connection needs no further action.

    def finish(self):
        try:
            super().finish()
        finally:
            self._deadline_timer.cancel()
            self._deadline_timer.join(timeout=0.1)

    def handle(self):
        try:
            super().handle()
        except OSError:
            # Deadline expiry can interrupt header parsing before WSGI starts.
            # The socket is already closed to traffic; do not log request data.
            pass

    def get_stderr(self):
        # wsgiref may otherwise print a traceback while writing to an expired
        # connection. The development profile emits no request diagnostics.
        return _DiscardErrors()

    def send_error(self, code, message=None, explain=None):
        # BaseHTTPRequestHandler's HTML errors can echo a malformed request
        # line before WSGI runs. Keep that earlier boundary fixed and safe too.
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(_ERROR)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-KFM-Local-Fixture", "synthetic-only")
        self.send_header("Connection", "close")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(_ERROR)
        self.close_connection = True

    def log_message(self, _format, *args):
        # Never log request paths, untrusted input, or exception details.
        pass


class _DiscardErrors:
    def write(self, value):
        return len(value)

    def flush(self):
        pass


def serve(*, port: int = DEFAULT_PORT, allowed_origin: str = DEFAULT_ORIGIN) -> None:
    app = create_app(port=port, allowed_origin=allowed_origin)
    with make_server("127.0.0.1", port, app, handler_class=_LocalRequestHandler) as server:
        print(f"Synthetic-only evidence transport: http://127.0.0.1:{port}{PATH}", flush=True)
        server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--ui-origin", default=DEFAULT_ORIGIN)
    args = parser.parse_args()
    serve(port=args.port, allowed_origin=args.ui_origin)
