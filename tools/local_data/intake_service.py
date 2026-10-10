#!/usr/bin/env python3
"""Owner-operated loopback API and desk for the raw-data intake pipeline.

Serves the standalone Intake Desk at http://127.0.0.1:8771/ and a JSON API used by
the desk and the Explorer's local library page. The security envelope matches
the other local companions: exact loopback Host, an Origin allowlist, a
per-process session token on every POST, bounded JSON bodies, and no file paths
chosen by the browser. Analysis output is review material, never a map layer.
"""
from __future__ import annotations

import argparse
import json
import re
import secrets
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from tools.local_data import intake, intake_route  # noqa: E402

PORT = 8771
SELF_ORIGIN = f"http://127.0.0.1:{PORT}"
SITE_ORIGINS = {"http://127.0.0.1:4173", "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site"}
ORIGINS = SITE_ORIGINS | {SELF_ORIGIN}
DESK = Path(__file__).resolve().parent / "intake_desk"
ASSETS = {"/": ("index.html", "text/html; charset=utf-8"), "/desk.js": ("desk.js", "text/javascript; charset=utf-8"),
          "/desk.css": ("desk.css", "text/css; charset=utf-8")}
CSP = ("default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; "
       "base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
ID = re.compile(r"[a-f0-9]{32}\Z")
ERROR = re.compile(r"[A-Z][A-Z0-9_]{2,90}(:[A-Z][A-Z0-9_]{2,90})?\Z")
MAX_MAP_FEATURES = 5000


class Desk:
    """Holds the store, the configured inbox and the single background analysis job."""

    def __init__(self, root: Path, inbox: Path | None = None, budget: dict | None = None):
        self.root = root
        self.inbox = inbox
        self.budget = budget or intake_route.load_budget()
        self.token = secrets.token_urlsafe(32)
        self.lock = threading.RLock()
        self.cancel_event = threading.Event()
        self.thread: threading.Thread | None = None
        self.job = {"state": "idle", "discovered": 0, "analyzed": 0, "reused": 0, "failed": 0, "run_id": None, "error": None}

    def status(self) -> dict:
        with self.lock:
            job = dict(self.job)
        return {"schema": "kfm-intake-desk/v1", "analyzerVersion": intake.ANALYZER_VERSION, "inboxConfigured": self.inbox is not None,
                "job": job, "authority": {"network": False, "source_admission": False, "promotion": False, "release": False, "publication": False}}

    def start(self, value: dict) -> dict:
        if not isinstance(value, dict) or set(value) - {"includeInbox"} or not isinstance(value.get("includeInbox", False), bool):
            raise ValueError("ANALYZE_REQUEST_INVALID")
        include = value.get("includeInbox", False)
        if include and self.inbox is None:
            raise ValueError("INBOX_NOT_CONFIGURED")
        with self.lock:
            if self.job["state"] == "running":
                raise ValueError("ANALYSIS_ALREADY_RUNNING")
            self.cancel_event.clear()
            self.job = {"state": "running", "discovered": 0, "analyzed": 0, "reused": 0, "failed": 0, "run_id": None, "error": None}
            self.thread = threading.Thread(target=self._run, args=(self.inbox if include else None,), daemon=True, name="kfm-intake")
            self.thread.start()
            return dict(self.job)

    def cancel(self) -> dict:
        with self.lock:
            if self.job["state"] != "running":
                raise ValueError("NO_ACTIVE_ANALYSIS")
            self.cancel_event.set()
            return {"cancelling": True}

    def _progress(self, summary: dict) -> None:
        with self.lock:
            self.job.update({k: summary.get(k, self.job.get(k)) for k in ("discovered", "analyzed", "reused", "failed", "run_id")})

    def _run(self, inbox: Path | None) -> None:
        try:
            summary = intake.analyze(self.root, inbox=inbox, budget=self.budget, progress=self._progress, cancel=self.cancel_event)
            with self.lock:
                self._progress(summary)
                self.job["state"] = summary["state"]
        except Exception as error:  # reported as a code; details stay in the process
            with self.lock:
                self.job.update(state="failed", error=str(error) if ERROR.fullmatch(str(error)) else "ANALYSIS_FAILED")

    def extents(self, query: dict) -> dict:
        listing = intake.list_items(self.root, limit=intake.LIST_LIMIT, **query)
        features = []
        for item in listing["items"][:MAX_MAP_FEATURES]:
            b = item["bbox_wgs84"]
            if not b:
                continue
            ring = [[b[0], b[1]], [b[2], b[1]], [b[2], b[3]], [b[0], b[3]], [b[0], b[1]]]
            geometry = {"type": "Point", "coordinates": [b[0], b[1]]} if b[0] == b[2] and b[1] == b[3] else {"type": "Polygon", "coordinates": [ring]}
            features.append({"type": "Feature", "id": item["id"], "geometry": geometry,
                             "properties": {"id": item["id"], "status": item["status"], "domain": item["domain"], "kind": item["kind"],
                                            "label": item["name"][:120]}})
        return {"type": "FeatureCollection", "features": features, "total": listing["total"],
                "note": "Bounding boxes of indexed files; analysis extents, not released map layers."}


def _query(raw: str) -> dict:
    params = {k: v[0] for k, v in parse_qs(raw, max_num_fields=12).items()}
    allowed = {"status", "domain", "family", "lane", "text", "bbox", "limit", "offset", "include_missing"}
    if set(params) - allowed:
        raise ValueError("QUERY_FIELD_UNSUPPORTED")
    out: dict = {}
    for key in ("status", "domain", "family", "lane", "text"):
        if key in params:
            if len(params[key]) > 100:
                raise ValueError("QUERY_VALUE_TOO_LONG")
            out[key] = params[key]
    if "bbox" in params:
        try:
            box = [float(v) for v in params["bbox"].split(",")]
        except ValueError:
            raise ValueError("BBOX_INVALID") from None
        if len(box) != 4 or not (-180 <= box[0] <= box[2] <= 180 and -90 <= box[1] <= box[3] <= 90):
            raise ValueError("BBOX_INVALID")
        out["bbox"] = box
    for key in ("limit", "offset"):
        if key in params:
            if not params[key].isdigit() or len(params[key]) > 7:
                raise ValueError("PAGING_INVALID")
            out[key] = int(params[key])
    if params.get("include_missing") == "1":
        out["include_missing"] = True
    return out


def handler(desk: Desk):
    class Handler(BaseHTTPRequestHandler):
        server_version = "KFMIntakeDesk"
        sys_version = ""

        def log_message(self, *args):
            pass

        def host_ok(self) -> bool:
            return self.headers.get("Host") == f"127.0.0.1:{PORT}"

        def origin(self) -> str | None:
            value = self.headers.get("Origin")
            if value not in ORIGINS:
                return None
            try:
                return self._safe_header_value(value)
            except ValueError:
                return None

        def _safe_header_value(self, value: str) -> str:
            # Prevent HTTP response splitting via any control chars (including CR/LF/HTAB).
            if any(ord(ch) < 32 or ord(ch) == 127 for ch in value):
                raise ValueError("INVALID_HEADER_VALUE")
            return value

        def _safe_header_name(self, name: str) -> str:
            # Header field-names must not include control chars or ':'.
            if any(ord(ch) < 33 or ord(ch) == 127 or ch == ":" for ch in name):
                raise ValueError("INVALID_HEADER_NAME")
            return name

        def _send_header_safe(self, name: str, value: str) -> None:
            self.send_header(self._safe_header_name(name), self._safe_header_value(value))

        def answer(self, status: int, body, *, content_type="application/json", extra=()):
            encoded = body if isinstance(body, bytes) else json.dumps(body, sort_keys=True).encode()
            self.send_response(status)
            origin = self.origin()
            if origin is not None and origin != SELF_ORIGIN:
                self._send_header_safe("Access-Control-Allow-Origin", origin)
            self._send_header_safe("Vary", "Origin")
            self._send_header_safe("Cache-Control", "no-store")
            self._send_header_safe("X-Content-Type-Options", "nosniff")
            self._send_header_safe("Referrer-Policy", "no-referrer")
            self._send_header_safe("Content-Type", content_type)
            self._send_header_safe("Content-Length", str(len(encoded)))
            for key, value in extra:
                self._send_header_safe(key, value)
            self.end_headers()
            self.wfile.write(encoded)

        def do_OPTIONS(self):
            origin = self.origin()
            if not self.host_ok() or origin is None or origin == SELF_ORIGIN:
                return self.answer(403, {"error": "ORIGIN_REJECTED"})
            self.send_response(204)
            self._send_header_safe("Access-Control-Allow-Origin", origin)
            self._send_header_safe("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self._send_header_safe("Access-Control-Allow-Headers", "Content-Type, X-KFM-Session")
            self._send_header_safe("Access-Control-Allow-Private-Network", "true")
            self._send_header_safe("Access-Control-Max-Age", "600")
            self._send_header_safe("Vary", "Origin")
            self.end_headers()

        def do_GET(self):
            # Host pins the loopback name (DNS-rebinding defence). A present Origin must be
            # allowlisted; a missing Origin is a same-origin or top-level read, never a write.
            if not self.host_ok() or ("Origin" in self.headers and self.origin() is None):
                return self.answer(403, {"error": "ORIGIN_REJECTED"})
            parsed = urlsplit(self.path)
            path = parsed.path
            if path in ASSETS:
                name, content_type = ASSETS[path]
                content = (DESK / name).read_bytes()
                if name == "index.html":
                    content = content.replace(b"__KFM_SESSION__", desk.token.encode())
                return self.answer(200, content, content_type=content_type,
                                   extra=(("Content-Security-Policy", CSP), ("X-Frame-Options", "DENY")))
            try:
                if path == "/api/status":
                    body = desk.status()
                    if self.origin() in SITE_ORIGINS:
                        body["sessionToken"] = desk.token
                    return self.answer(200, body)
                if path == "/api/overview":
                    return self.answer(200, intake.overview(desk.root, desk.budget))
                if path == "/api/items":
                    return self.answer(200, intake.list_items(desk.root, **_query(parsed.query)))
                if path.startswith("/api/items/"):
                    identity = path.rsplit("/", 1)[-1]
                    if not ID.fullmatch(identity):
                        raise ValueError("ITEM_ID_INVALID")
                    return self.answer(200, intake.get_item(desk.root, identity))
                if path == "/api/extents":
                    query = _query(parsed.query)
                    query.pop("limit", None)
                    query.pop("offset", None)
                    return self.answer(200, desk.extents(query), content_type="application/geo+json")
                if path == "/api/budget":
                    return self.answer(200, intake_route.budget_state(desk.budget))
                if path == "/api/release-plan":
                    return self.answer(200, intake.release_plan(desk.root, desk.budget))
            except ValueError as error:
                code = str(error)
                status = 404 if code == "ITEM_NOT_FOUND" else 400
                return self.answer(status, {"error": code if ERROR.fullmatch(code) else "INVALID_REQUEST"})
            except Exception:  # never drop the connection or leak internals
                return self.answer(500, {"error": "INTERNAL_ERROR"})
            return self.answer(404, {"error": "NOT_FOUND"})

        def do_POST(self):
            if not self.host_ok() or self.origin() is None or not secrets.compare_digest(self.headers.get("X-KFM-Session", ""), desk.token):
                return self.answer(403, {"error": "SESSION_REJECTED"})
            if self.headers.get("Content-Type") != "application/json" or self.headers.get("Transfer-Encoding"):
                return self.answer(415, {"error": "JSON_REQUIRED"})
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 4096:
                    raise ValueError("REQUEST_BYTE_LIMIT")
                self.connection.settimeout(5)
                value = json.loads(self.rfile.read(length))
                if self.path == "/api/analyze":
                    result = desk.start(value)
                elif self.path == "/api/cancel":
                    if value != {}:
                        raise ValueError("EMPTY_CANCEL_REQUIRED")
                    result = desk.cancel()
                elif self.path == "/api/apply":
                    if not isinstance(value, dict) or set(value) != {"id", "action"} or not ID.fullmatch(str(value["id"])):
                        raise ValueError("APPLY_REQUEST_INVALID")
                    with desk.lock:
                        if desk.job["state"] == "running":
                            raise ValueError("ANALYSIS_ALREADY_RUNNING")
                    result = intake.apply(desk.root, value["id"], value["action"])
                else:
                    return self.answer(404, {"error": "NOT_FOUND"})
                self.answer(200, result)
            except (ValueError, KeyError, TypeError, OSError) as error:
                code = str(error)
                self.answer(400, {"error": code if ERROR.fullmatch(code) else "INVALID_REQUEST"})
            except Exception:
                self.answer(500, {"error": "INTERNAL_ERROR"})

    return Handler


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", help="initialized private store (default: KFM_DATA_ROOT)")
    parser.add_argument("--inbox", type=Path, help="read-only downloads directory the desk may analyze (e.g. ~/Downloads/KFM)")
    args = parser.parse_args(argv)
    root = intake.resolve_root(args.root)
    inbox = None
    if args.inbox:
        inbox = args.inbox.expanduser().resolve()
        if not inbox.is_dir() or inbox == root or root in inbox.parents or inbox in root.parents:
            parser.error("--inbox must be an existing directory separate from the store")
    desk = Desk(root, inbox)
    server = ThreadingHTTPServer(("127.0.0.1", PORT), handler(desk))
    print(f"KFM Intake Desk: {SELF_ORIGIN}/  (store {root}; Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        desk.cancel_event.set()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
