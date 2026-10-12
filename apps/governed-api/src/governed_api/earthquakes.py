"""Versioned read-only USGS ComCat earthquake routes, the earthquake counterpart of storm_events.py."""
from datetime import datetime, timezone
from urllib.parse import parse_qs
import json
import logging
import time
import uuid

from release.core import EARTHQUAKES
from release.earthquake_projection import VERSION, negative, project

LOG = logging.getLogger("kfm.operational")
ROUTES = {"/v1/earthquakes/bootstrap": "bootstrap", "/v1/earthquakes/layers": "layers", "/v1/earthquakes/evidence": "evidence"}
MONTHS = {str(m): m for m in range(1, 13)}


def respond(environ, start_response, store):
    start = time.monotonic()
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    correlation = uuid.uuid4().hex
    status = "200 OK"
    try:
        if environ.get("REQUEST_METHOD", "GET") != "GET":
            status, payload = "405 Method Not Allowed", negative("METHOD_NOT_ALLOWED", now=now)
        elif len(environ.get("QUERY_STRING", "")) > 256:
            status, payload = "400 Bad Request", negative("INVALID_QUERY", now=now)
        else:
            try:
                query = parse_qs(environ.get("QUERY_STRING", ""), keep_blank_values=True, max_num_fields=16)
            except ValueError:
                query = {"invalid": []}
            if any(len(values) != 1 for values in query.values()):
                query = {"invalid": []}
            month = query.get("month", [None])[0]
            # Only the exact tokens 1..12: no leading zeros, signs or spaces.
            if set(query) - {"month"} or month is not None and month not in MONTHS:
                status, payload = "400 Bad Request", negative("INVALID_QUERY", now=now)
            else:
                active = store.active("earthquakes") if store is not None else None
                now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
                payload = (project(*active, view=ROUTES[environ["PATH_INFO"]], now=now, month=MONTHS.get(month))
                           if active else negative("NO_APPROVED_SNAPSHOT", now=now))
    except (OSError, ValueError, KeyError, TypeError, RuntimeError):
        status, payload = "503 Service Unavailable", negative("RELEASE_STORE_UNAVAILABLE", now=now, outcome="ERROR")
    except Exception:
        status, payload = "503 Service Unavailable", negative("SAFE_RUNTIME_ERROR", now=now, outcome="ERROR")
    if status == "200 OK" and payload["envelope"]["outcome"] == "ERROR":
        status = "500 Internal Server Error"
    # Fixed fields only: never reflect query strings, paths, evidence or errors.
    LOG.info(json.dumps({"event": "governed_read", "component": "governed-api", "build": VERSION,
                         "correlation_id": correlation, "source_id": EARTHQUAKES.source_id, "outcome": payload["envelope"]["outcome"],
                         "reason_code": payload["envelope"]["reason_code"], "duration_ms": round((time.monotonic()-start)*1000)}, separators=(",", ":")))
    body = json.dumps(payload, allow_nan=False).encode()
    start_response(status, [("Content-Type", "application/json"), ("Content-Length", str(len(body))), ("Cache-Control", "no-store"),
                            ("X-Content-Type-Options", "nosniff"), ("X-KFM-Correlation-ID", correlation), ("Allow", "GET")])
    return [body]
