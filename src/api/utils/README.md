<div align="center">

# 🧰 Kansas Frontier Matrix — API Utilities  
`src/api/utils/README.md`

**DB Connections · Caching · Logging · Auth · Errors · Metrics**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Code](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/api/utils/`** package provides **shared infrastructure helpers** used by the API layer:

- **Database utilities** for Neo4j and file-backed STAC reads  
- **Caching** for hot-path endpoints (in-memory / Redis)  
- **Logging & request tracing** (MCP-compliant provenance)  
- **Auth & rate-limiting** middleware (optional)  
- **Error handling** and **pagination** helpers  
- **Metrics** (Prometheus-friendly) and response helpers

These utilities keep route handlers small, consistent, and reproducible.

---

## 📂 Directory Layout

```

src/api/utils/
├── **init**.py
├── db.py           # Neo4j sessions, query helpers, health checks
├── cache.py        # Simple TTL cache + optional Redis backend
├── logger.py       # Structured logging, request IDs, timing
├── auth.py         # API-key / bearer auth, rate limiting (optional)
├── errors.py       # APIException classes + FastAPI handlers
├── pagination.py   # limit/offset helpers and link headers
├── responses.py    # JSON/GeoJSON/STAC response builders
├── metrics.py      # Prometheus counters/histograms
└── README.md       # (this file)

````

---

## 🔌 Database Utilities (`db.py`)

- Centralizes **Neo4j** configuration and connection pooling.  
- Exposes dependency-injected **read/write sessions** for FastAPI routes.  
- Adds **retry** and **timeout** semantics for long-running queries.

```python
# db.py
import os
from contextlib import contextmanager
from neo4j import GraphDatabase, basic_auth

URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
AUTH = basic_auth(os.getenv("NEO4J_USER", "neo4j"), os.getenv("NEO4J_PASS", "password"))
_driver = GraphDatabase.driver(URI, auth=AUTH, max_connection_lifetime=300)

@contextmanager
def get_session(mode: str = "r"):
    with _driver.session(default_access_mode=("WRITE" if mode == "w" else "READ")) as s:
        yield s

def healthcheck() -> bool:
    with get_session("r") as s:
        s.run("RETURN 1 AS ok")
    return True
````

**Usage in a route**:

```python
from fastapi import Depends, APIRouter
from src.api.utils.db import get_session

router = APIRouter()

@router.get("/places")
def list_places():
    with get_session("r") as s:
        res = s.run("MATCH (p:Place) RETURN p.name AS name, p.latitude AS lat, p.longitude AS lon")
        return [{"name": r["name"], "latitude": r["lat"], "longitude": r["lon"]} for r in res]
```

---

## ⚡ Caching (`cache.py`)

* Pluggable **in-memory TTL** cache (default) with an optional **Redis** backend.
* Decorator for route-level caching with key builders and invalidation.

```python
# cache.py
import time, functools
CACHE = {}

def ttl_cache(seconds: int = 60):
    def wrap(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            key = (fn.__name__, args, frozenset(kwargs.items()))
            now = time.time()
            if key in CACHE and (now - CACHE[key][0]) < seconds:
                return CACHE[key][1]
            res = fn(*args, **kwargs)
            CACHE[key] = (now, res)
            return res
        return inner
    return wrap
```

---

## 📝 Logging & Tracing (`logger.py`)

* **Structured logs** with ISO timestamps, request IDs, route, duration, and status.
* Adds **MCP provenance**: dataset IDs, query parameters, and graph query hashes.

```python
# logger.py
import logging, time, uuid
logger = logging.getLogger("kfm.api")
logger.setLevel(logging.INFO)

def log_request(path: str, status: int, start: float, meta: dict | None = None):
    rid = str(uuid.uuid4())[:8]
    logger.info({
        "rid": rid,
        "path": path,
        "status": status,
        "ms": int((time.time() - start) * 1000),
        "meta": meta or {}
    })
```

**FastAPI middleware snippet**:

```python
from fastapi import FastAPI, Request
from src.api.utils.logger import log_request
app = FastAPI()

@app.middleware("http")
async def access_log(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    log_request(str(request.url), response.status_code, start, meta={"method": request.method})
    return response
```

---

## 🔐 Auth & Rate Limiting (`auth.py`)

* Optional **API key** or **Bearer token** verification.
* **IP / key based** rate limiting (sliding window).

```python
# auth.py
from fastapi import Header, HTTPException

def require_api_key(x_api_key: str | None = Header(default=None)):
    if not x_api_key or x_api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Invalid API key")
```

Use in a route:

```python
@router.get("/secure")
def secure_endpoint(_=Depends(require_api_key)):
    return {"ok": True}
```

---

## 🧯 Errors (`errors.py`)

Centralized error shapes aligned with MCP provenance.

```python
# errors.py
from fastapi import Request
from fastapi.responses import JSONResponse

class APIError(Exception):
    def __init__(self, status: int, code: str, msg: str):
        self.status, self.code, self.msg = status, code, msg

async def api_error_handler(_: Request, exc: APIError):
    return JSONResponse(status_code=exc.status, content={
        "error": {"code": exc.code, "message": exc.msg}
    })
```

Register in `main.py`:

```python
app.add_exception_handler(APIError, api_error_handler)
```

---

## 📄 Pagination (`pagination.py`)

Helpers to parse `limit`/`offset` and emit **RFC-5988 Link** headers.

```python
# pagination.py
from fastapi import Request
def paginate(items, limit: int, offset: int):
    return items[offset: offset + limit]

def link_headers(req: Request, total: int, limit: int, offset: int) -> dict[str, str]:
    base = str(req.url).split("?")[0]
    def qp(o): return f"{base}?limit={limit}&offset={o}"
    links = []
    if offset + limit < total: links.append(f'<{qp(offset+limit)}>; rel="next"')
    if offset > 0: links.append(f'<{qp(max(0, offset-limit))}>; rel="prev"')
    return {"Link": ", ".join(links)} if links else {}
```

---

## 📦 Responses (`responses.py`)

Consistent JSON/GeoJSON/STAC encoders with `meta` blocks (provenance, license, timestamp).

```python
# responses.py
from fastapi.responses import JSONResponse
from datetime import datetime

def json_ok(data, meta: dict | None = None):
    return JSONResponse({
        "data": data,
        "meta": {"generated": datetime.utcnow().isoformat(), **(meta or {})}
    })
```

---

## 📈 Metrics (`metrics.py`)

Prometheus counters and histograms for request counts/latency.

```python
# metrics.py
from prometheus_client import Counter, Histogram

REQS = Counter("kfm_api_requests_total", "API requests", ["route", "method", "code"])
LAT  = Histogram("kfm_api_latency_seconds", "API latency", ["route", "method"])

def observe(route: str, method: str, code: int, seconds: float):
    REQS.labels(route, method, code).inc()
    LAT.labels(route, method).observe(seconds)
```

Expose `/metrics` in `main.py` using `prometheus_client` ASGI app if needed.

---

## 🧪 Example Route Using Utils

```python
from fastapi import APIRouter, Request, Depends
from src.api.utils.db import get_session
from src.api.utils.pagination import paginate, link_headers
from src.api.utils.responses import json_ok

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/")
def list_events(request: Request, limit: int = 50, offset: int = 0):
    with get_session("r") as s:
        res = s.run("MATCH (e:Event) RETURN e.id AS id, e.title AS title ORDER BY e.start_date")
        rows = [dict(r) for r in res]
    page = paginate(rows, limit, offset)
    headers = link_headers(request, total=len(rows), limit=limit, offset=offset)
    return json_ok(page, meta={"total": len(rows), "limit": limit, "offset": offset}), headers
```

---

## 🔁 Integration Flow

* **Upstream:** None (infrastructure package)
* **Downstream:** Used by all route modules in `src/api/routes/`
* **Automation:** `make api` runs server; CI executes **unit tests** for utils and routes

---

## 📚 References

* API Layer Overview → `src/api/README.md`
* Routes Overview → `src/api/routes/README.md`
* Schemas & Validation → `src/api/schemas/README.md`
* Knowledge Graph Queries → `src/graph/graph_queries.py`
* MCP Documentation & SOPs → `docs/`

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Reliable Utilities · Clear Contracts · Reproducible APIs*

</div>

