#!/usr/bin/env python3
"""Loopback-only private land-record review runtime. No release or mutation API."""
from pathlib import Path
import argparse
import hmac
import json
import logging
import secrets
import sys
from urllib.parse import parse_qs
from wsgiref.simple_server import WSGIRequestHandler, make_server

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "packages/domains/people-dna-land/src")]
from people_dna_land.land_records import KINDS, SOURCES, canonical, iso_date, public_projection
from people_dna_land.land_store import audit, evidence_for, immutable, list_records, read_file, status

ASSETS = Path(__file__).parent / "static"
HEADERS = [("Cache-Control", "private, no-store"), ("X-Content-Type-Options", "nosniff"), ("Referrer-Policy", "no-referrer"),
           ("Content-Security-Policy", "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'")]


def application(root, token, port):
    if not isinstance(token, str) or len(token) < 40:
        raise ValueError("STRONG_REVIEW_TOKEN_REQUIRED")
    expected_auth = ("Bearer " + token).encode("utf-8", "surrogatepass")
    def app(environ, start_response):
        status_code, payload, media = "200 OK", None, "application/json"
        try:
            path = environ.get("PATH_INFO", "")
            host = environ.get("HTTP_HOST", "")
            if host not in {f"127.0.0.1:{port}", f"localhost:{port}"}:
                status_code, payload = "403 Forbidden", {"outcome": "DENY", "reason_code": "HOST_NOT_ALLOWED"}
            elif environ.get("REQUEST_METHOD") != "GET":
                status_code, payload = "405 Method Not Allowed", {"outcome": "DENY", "reason_code": "READ_ONLY_RUNTIME"}
            elif environ.get("HTTP_ORIGIN") and environ["HTTP_ORIGIN"] not in {f"http://127.0.0.1:{port}", f"http://localhost:{port}"}:
                status_code, payload = "403 Forbidden", {"outcome": "DENY", "reason_code": "ORIGIN_NOT_ALLOWED"}
            elif path == "/healthz":
                payload = {"process": "LIVE", "scope": "OWNER_REVIEW_ONLY", "public_records": 0}
            elif path in {"/", "/review", "/review.css", "/review.js"}:
                name, media = {"/": ("index.html", "text/html; charset=utf-8"), "/review": ("index.html", "text/html; charset=utf-8"),
                               "/review.css": ("review.css", "text/css; charset=utf-8"), "/review.js": ("review.js", "text/javascript; charset=utf-8")}[path]
                payload = read_file(ASSETS / name, 100_000)
            elif path == "/v1/land/records":
                status_code, payload = "403 Forbidden", public_projection(None)
            elif not path.startswith("/review/v1/"):
                status_code, payload = "404 Not Found", {"outcome": "ABSTAIN", "reason_code": "ROUTE_NOT_FOUND"}
            # Compare bytes: compare_digest raises TypeError on non-ASCII str, which would misreport a bad key as a bad query.
            elif not hmac.compare_digest(environ.get("HTTP_AUTHORIZATION", "").encode("utf-8", "surrogatepass"), expected_auth):
                status_code, payload = "401 Unauthorized", {"outcome": "DENY", "reason_code": "OWNER_REVIEW_AUTH_REQUIRED"}
            else:
                if len(environ.get("QUERY_STRING", "")) > 1024:
                    raise ValueError("QUERY_LIMIT")
                query = parse_qs(environ.get("QUERY_STRING", ""), keep_blank_values=True, max_num_fields=8)
                if any(len(v) != 1 or len(v[0]) > 128 for v in query.values()):
                    raise ValueError("QUERY_INVALID")
                args = {k: v[0] for k, v in query.items()}
                if path == "/review/v1/status" and not args:
                    payload = status(root)
                elif path == "/review/v1/evidence" and set(args) == {"digest"}:
                    payload = {"bundles": evidence_for(root, args["digest"]), "scope": "OWNER_REVIEW_ONLY"}
                elif path == "/review/v1/records" and set(args) <= {"source", "county", "kind", "start", "end", "after", "limit"}:
                    if "source" in args and args["source"] not in SOURCES or "kind" in args and args["kind"] not in KINDS:
                        raise ValueError("FILTER_INVALID")
                    for key in ("start", "end"):
                        if key in args:
                            iso_date(args[key], required=True)
                    if "start" in args and "end" in args and args["start"] > args["end"]:
                        raise ValueError("DATE_RANGE_INVALID")
                    limit = args.pop("limit", "25")
                    if not limit.isdigit() or str(int(limit)) != limit:
                        raise ValueError("LIMIT_INVALID")
                    payload = list_records(root, limit=int(limit), **args)
                else:
                    raise ValueError("QUERY_OR_ROUTE_INVALID")
        except (ValueError, TypeError, KeyError):
            # A failed static-asset read has already chosen its media type; the error body is JSON.
            status_code, payload, media = "400 Bad Request", {"outcome": "ABSTAIN", "reason_code": "INVALID_QUERY"}, "application/json"
        except Exception as error:
            # Exception names only; no private record text, filesystem path or token.
            logging.getLogger("kfm.land-runtime").error("LAND_STORE_UNAVAILABLE %s", type(error).__name__)
            status_code, payload, media = "503 Service Unavailable", {"outcome": "ABSTAIN", "reason_code": "STORE_UNAVAILABLE"}, "application/json"
        body = payload if isinstance(payload, bytes) else canonical(payload)
        start_response(status_code, [("Content-Type", media), ("Content-Length", str(len(body))), *HEADERS])
        return [body]
    return app


class PrivateLog(WSGIRequestHandler):
    def log_message(self, format, *args):
        # Default request logs contain filters and potentially sensitive locators.
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--port", type=int, default=5271)
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("Choose an unprivileged local port.")
    audit(args.root)
    key = args.root / ".review-token"
    if not key.exists():
        immutable(key, secrets.token_urlsafe(32).encode())
    if key.stat().st_mode & 0o077:
        raise ValueError("TOKEN_FILE_MUST_BE_PRIVATE")
    token = read_file(key, 256).decode()
    with make_server("127.0.0.1", args.port, application(args.root, token, args.port), handler_class=PrivateLog) as server:
        print(f"Private land review: http://127.0.0.1:{args.port}/review", flush=True)
        print("Review key: .review-token in the private store. No public release is active.", flush=True)
        server.serve_forever()


if __name__ == "__main__":
    main()
