#!/usr/bin/env python3
"""Owner-operated loopback API and desk for the raw-data intake pipeline.

Serves the standalone Intake Desk at http://127.0.0.1:8771/ and a JSON API used by
the desk and the Explorer's local library page. The security envelope matches
the other local companions: exact loopback Host, an Origin allowlist, a
operator-provisioned per-process session token on every API request, bounded JSON bodies, and no file paths
chosen by the browser. Analysis and bounded private atlas previews are review
material; they never grant source admission, release, or publication authority.
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
from tools.local_data import intake, intake_route, atlas, review_packages  # noqa: E402
from tools.local_data.loopback_session import session_matches, print_connection_links  # noqa: E402

PORT = 8771
SELF_ORIGIN = f"http://127.0.0.1:{PORT}"
SITE_ORIGINS = {"http://127.0.0.1:4173", "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site"}
ORIGINS = SITE_ORIGINS | {SELF_ORIGIN}
DESK = Path(__file__).resolve().parent / "intake_desk"
ASSETS = {"/": ("index.html", "text/html; charset=utf-8"), "/desk.js": ("desk.js", "text/javascript; charset=utf-8"),
          "/reviews.js": ("reviews.js", "text/javascript; charset=utf-8"),
          "/desk.css": ("desk.css", "text/css; charset=utf-8")}
CSP = ("default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data: blob:; "
       "base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
ID = re.compile(r"[a-f0-9]{32}\Z")
ERROR = re.compile(r"[A-Z][A-Z0-9_]{2,90}(:[A-Z][A-Z0-9_]{2,90})?\Z")
MAX_MAP_FEATURES = 5000


class Desk:
    """Holds the store, the configured inbox and the single background analysis job."""

    def __init__(self, root: Path, inbox: Path | None = None, budget: dict | None = None, raster_python: Path | None = None, *, max_files: int = intake.MAX_FILES, review_bindings=(), read_only=False):
        self.root = root
        self.atlas = atlas.Atlas(root, raster_python=raster_python)
        self.reviews = review_packages.ReviewPackages(root, review_bindings)
        self.read_only = read_only
        self.inbox = inbox
        self.budget = budget or intake_route.load_budget()
        self.max_files = intake.file_limit(max_files)
        self.token = secrets.token_urlsafe(32)
        self.lock = threading.RLock()
        self.cancel_event = threading.Event()
        self.thread: threading.Thread | None = None
        self.job = {"state": "idle", "discovered": 0, "analyzed": 0, "reused": 0, "failed": 0, "run_id": None, "error": None}

    def status(self) -> dict:
        with self.lock:
            job = dict(self.job)
        return {"schema": "kfm-intake-desk/v1", "analyzerVersion": intake.ANALYZER_VERSION, "inboxConfigured": self.inbox is not None,
                "maxFiles": self.max_files, "analysisAllowed": not self.read_only, "job": job, "authority": {"network": False, "source_admission": False, "promotion": False, "release": False, "publication": False}}

    def start(self, value: dict) -> dict:
        if self.read_only:
            raise ValueError("READ_ONLY_DESK")
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

    def refresh_periodically(self, seconds: int, stop: threading.Event) -> None:
        """Honor an existing operator-selected schedule without overlapping scans."""
        while not stop.wait(seconds):
            with self.lock:
                if self.job["state"] != "running":
                    self.start({})

    def _run(self, inbox: Path | None) -> None:
        try:
            summary = intake.analyze(self.root, inbox=inbox, budget=self.budget, progress=self._progress, cancel=self.cancel_event, max_files=self.max_files)
            with self.lock:
                self._progress(summary)
                self.job["state"] = summary["state"]
        except Exception as error:  # reported as a code; details stay in the process
            with self.lock:
                self.job.update(state="failed", error=str(error) if ERROR.fullmatch(str(error)) else "ANALYSIS_FAILED")

    def extents(self, query: dict) -> dict:
        listing = intake.list_items(self.root, **query)
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
                "offset": listing["offset"], "limit": listing["limit"], "scannedCount": len(listing["items"]),
                "displayedCount": len(features), "nextOffset": listing["offset"] + len(listing["items"]) if listing["offset"] + len(listing["items"]) < listing["total"] else None,
                "note": "Bounding boxes on this catalog page; file extents, not measured coverage or released map layers."}


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


def handler(desk: Desk, *, port=PORT):
    self_origin = f"http://127.0.0.1:{port}"
    origins = SITE_ORIGINS | {self_origin}
    class Handler(BaseHTTPRequestHandler):
        server_version = "KFMIntakeDesk"
        sys_version = ""

        def log_message(self, *args):
            pass

        def host_ok(self) -> bool:
            return self.headers.get("Host") == f"127.0.0.1:{port}"

        def origin(self) -> str | None:
            value = self.headers.get("Origin")
            if value not in origins:
                return None
            try:
                return self._safe_header_value(value)
            except ValueError:
                return None

        def _safe_header_value(self, value: str) -> str:
            # Prevent HTTP response splitting: canonicalize line breaks, then reject
            # any remaining control chars (including HTAB) and DEL.
            sanitized = value.replace("\r", "").replace("\n", "")
            if any(ord(ch) < 32 or ord(ch) == 127 for ch in sanitized):
                raise ValueError("INVALID_HEADER_VALUE")
            return sanitized

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
            if origin is not None and origin != self_origin:
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
            if not self.host_ok() or origin is None or origin == self_origin:
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
            # allowlisted. Neither header authenticates a local process; API reads need a capability.
            if not self.host_ok() or ("Origin" in self.headers and self.origin() is None):
                return self.answer(403, {"error": "ORIGIN_REJECTED"})
            parsed = urlsplit(self.path)
            path = parsed.path
            if path in ASSETS:
                name, content_type = ASSETS[path]
                content = (DESK / name).read_bytes()
                return self.answer(200, content, content_type=content_type,
                                   extra=(("Content-Security-Policy", CSP), ("X-Frame-Options", "DENY")))
            if not session_matches(self.headers, desk.token):
                return self.answer(403, {"error": "SESSION_REJECTED"})
            # WORK review is local to this desk, not a new Explorer/public data route.
            if path.startswith("/api/reviews") and "Origin" in self.headers and self.origin() != self_origin:
                return self.answer(403, {"error": "PRIVATE_REVIEW_ORIGIN_REQUIRED"})
            if desk.read_only and path != "/api/status" and not path.startswith("/api/reviews"):
                return self.answer(403, {"error": "READ_ONLY_DESK"})
            try:
                if path == "/api/reviews":
                    if parsed.query:
                        raise ValueError("REVIEW_QUERY_INVALID")
                    return self.answer(200, desk.reviews.catalog())
                if path.startswith("/api/reviews/"):
                    parts = path.split("/")
                    params = parse_qs(parsed.query, max_num_fields=2, keep_blank_values=True)
                    if (len(parts) != 5 or not all(review_packages.ID.fullmatch(p) for p in parts[3:])
                            or set(params) - {"text"} or any(len(v) != 1 for v in params.values())):
                        raise ValueError("REVIEW_REQUEST_INVALID")
                    body, content_type = desk.reviews.preview(parts[3], parts[4], text=params.get("text", [""])[0])
                    return self.answer(200, body, content_type=content_type)
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
                    return self.answer(200, desk.extents(query), content_type="application/geo+json")
                if path == "/api/atlas/catalog":
                    return self.answer(200, desk.atlas.catalog(**_query(parsed.query)))
                if path == "/api/atlas/prism/groups":
                    if parsed.query:
                        raise ValueError("ATLAS_QUERY_INVALID")
                    return self.answer(200, desk.atlas.groups())
                if path == "/api/atlas/prism/frames":
                    params = parse_qs(parsed.query, max_num_fields=5)
                    if set(params) - {"group", "year", "offset", "limit"} or any(len(v) != 1 for v in params.values()):
                        raise ValueError("ATLAS_QUERY_INVALID")
                    return self.answer(200, desk.atlas.frames(params.get("group", [""])[0], year=params.get("year", [None])[0],
                                       offset=int(params.get("offset", ["0"])[0]), limit=int(params.get("limit", ["366"])[0])))
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
            if not self.host_ok() or self.origin() is None or not session_matches(self.headers, desk.token):
                return self.answer(403, {"error": "SESSION_REJECTED"})
            if desk.read_only:
                return self.answer(403, {"error": "READ_ONLY_DESK"})
            if self.headers.get("Content-Type") != "application/json" or self.headers.get("Transfer-Encoding"):
                return self.answer(415, {"error": "JSON_REQUIRED"})
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 4096:
                    raise ValueError("REQUEST_BYTE_LIMIT")
                self.connection.settimeout(5)
                value = json.loads(self.rfile.read(length))
                if self.path == "/api/atlas/preview":
                    result = desk.atlas.preview(value)
                elif self.path == "/api/analyze":
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
    parser.add_argument("--port", type=int, default=PORT, help="loopback port, 1024–65535; default 8771")
    parser.add_argument("--read-only", action="store_true", help="disable all POST operations and analysis; suitable for a parallel private review desk")
    parser.add_argument("--inbox", type=Path, help="read-only downloads directory the desk may analyze (e.g. ~/Downloads/KFM)")
    parser.add_argument("--max-files", type=int, default=intake.MAX_FILES, help="explicit discovery ceiling, at most 5,000,000 files")
    parser.add_argument("--refresh-seconds", type=int, default=0, help="0 disables automatic analysis; otherwise repeat on a 300 to 86400 second interval")
    parser.add_argument("--raster-python", type=Path, help="trusted local Python with rasterio, numpy and pyshp for bounded map previews")
    parser.add_argument("--review-package", action="append", default=[], metavar="WORK_MANIFEST@SHA256",
                        help="explicit relative WORK review-manifest.json and exact digest; private desk only, at most 16")
    args = parser.parse_args(argv)
    if not 1024 <= args.port <= 65535 or (args.read_only and args.refresh_seconds):
        parser.error("--port must be 1024–65535; --read-only requires --refresh-seconds 0")
    if args.refresh_seconds != 0 and not 300 <= args.refresh_seconds <= 86400:
        parser.error("--refresh-seconds must be 0 or between 300 and 86400")
    root = intake.resolve_root(args.root)
    inbox = None
    if args.inbox:
        inbox = args.inbox.expanduser().resolve()
        if not inbox.is_dir() or inbox == root or root in inbox.parents or inbox in root.parents:
            parser.error("--inbox must be an existing directory separate from the store")
    desk = Desk(root, inbox, raster_python=args.raster_python, max_files=args.max_files, review_bindings=args.review_package, read_only=args.read_only)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler(desk, port=args.port))
    stop_refresh = threading.Event()
    if args.refresh_seconds:
        desk.start({})
        threading.Thread(target=desk.refresh_periodically, args=(args.refresh_seconds, stop_refresh), daemon=True, name="kfm-intake-refresh").start()
    self_origin = f"http://127.0.0.1:{args.port}"
    print(f"KFM Intake Desk: {self_origin}/  (store {root}; Ctrl+C to stop)", flush=True)
    print_connection_links(desk.token, "intake", SITE_ORIGINS | {self_origin})
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        stop_refresh.set()
        desk.cancel_event.set()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
