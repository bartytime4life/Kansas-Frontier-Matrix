
<div align="center">

# 🧰 **Kansas Frontier Matrix — API Utilities**  
`src/api/utils/README.md`

**DB Connections · Caching · Logging · Auth · Errors · Metrics**

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy&logo=github&color=blue)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate&logo=json&color=blue)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL&logo=github&color=informational)](../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security&logo=security&color=green)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue?logo=markdown)](../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — API Utilities"
version: "v1.7.0"
last_updated: "2025-10-17"
owners: ["@kfm-architecture", "@kfm-data"]
tags: ["api","utils","neo4j","cache","logging","auth","errors","metrics","pagination","mcp","semver","ci"]
status: "Stable"
license: "MIT"
semver_policy: "MAJOR.MINOR.PATCH"
ci_required_checks:
  - pre-commit
  - unit-tests
  - codeql
  - trivy
  - docs-validate
semantic_alignment:
  - ISO 8601
  - GeoJSON
  - STAC 1.0 (passthrough responses)
  - MCP-DL v6.2 (provenance/logging)
---
```

---

## 🎯 Purpose

The **`src/api/utils/`** package provides the **shared infrastructure foundation** for the KFM API layer — keeping routes lean, reproducible, and MCP-compliant.

It includes:
- **Database management** (Neo4j connection pooling)  
- **Caching** (in-memory TTL / Redis backend)  
- **Structured logging** & request tracing  
- **Auth / rate limiting** (API key or JWT)  
- **Error handling** & pagination helpers  
- **Prometheus metrics** for monitoring  

---

## 📂 Directory Layout

```
src/api/utils/
├── __init__.py
├── db.py           # Neo4j sessions, query helpers, health checks
├── cache.py        # TTL cache + optional Redis backend
├── logger.py       # Structured logging, request IDs, timing
├── auth.py         # API-key / bearer auth, rate limiting
├── errors.py       # Custom API exceptions + FastAPI handlers
├── pagination.py   # limit/offset helpers and Link headers
├── responses.py    # JSON/GeoJSON/STAC response builders
├── metrics.py      # Prometheus counters/histograms
└── README.md       # (this file)
```

---

## 🔌 Database Utilities (`db.py`)

```python
import os
from contextlib import contextmanager
from neo4j import GraphDatabase, basic_auth

URI  = os.getenv("NEO4J_URI",  "bolt://localhost:7687")
USER = os.getenv("NEO4J_USER", "neo4j")
PASS = os.getenv("NEO4J_PASS", "password")

_driver = GraphDatabase.driver(URI, auth=basic_auth(USER, PASS), max_connection_lifetime=300)

@contextmanager
def get_session(mode: str = "r"):
    access = "WRITE" if mode == "w" else "READ"
    with _driver.session(default_access_mode=access) as s:
        yield s

def healthcheck() -> bool:
    with get_session("r") as s:
        s.run("RETURN 1 AS ok")
    return True
```

---

## ⚡ Caching (`cache.py`)

```python
import time, functools
CACHE: dict = {}

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

```python
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

**FastAPI middleware:**
```python
from fastapi import FastAPI, Request
from src.api.utils.logger import log_request
import time

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

```python
import os
from fastapi import Header, HTTPException

def require_api_key(x_api_key: str | None = Header(default=None)):
    if not x_api_key or x_api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Invalid API key")
```

**Route usage:**
```python
from fastapi import Depends
@router.get("/secure")
def secure_endpoint(_=Depends(require_api_key)):
    return {"ok": True}
```

---

## 🧯 Error Handling (`errors.py`)

```python
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

**Register:**
```python
from src.api.utils.errors import APIError, api_error_handler
app.add_exception_handler(APIError, api_error_handler)
```

---

## 📄 Pagination (`pagination.py`)

```python
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

```python
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

```python
from prometheus_client import Counter, Histogram

REQS = Counter("kfm_api_requests_total", "API requests", ["route", "method", "code"])
LAT  = Histogram("kfm_api_latency_seconds", "API latency", ["route", "method"])

def observe(route: str, method: str, code: int, seconds: float):
    REQS.labels(route, method, code).inc()
    LAT.labels(route, method).observe(seconds)
```

Expose `/metrics` via `prometheus_client` ASGI if needed.

---

## 🧪 Example Route Using Utils

```python
from fastapi import APIRouter, Request
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

## 🧷 CI Acceptance Checklist

- [ ] Secrets via env/CI (no hardcoded credentials)  
- [ ] Logging with UUID request IDs  
- [ ] Pagination emits RFC-5988 headers  
- [ ] TTL cache respects expiry rules  
- [ ] `/metrics` endpoint exports Prometheus data  
- [ ] Unit tests validated by CI (CodeQL/Trivy clean)  

---

## 🛡️ Security & Compliance

- Environment secrets & least-privilege roles  
- Parameterized Cypher & sanitized logs (no PII)  
- Strict CORS + rate limits in prod  
- License + attribution included in metadata  

---

## 🧾 Version History

| Version | Date | Type | Notes |
| :------ | :--- | :-- | :---- |
| v1.7.0 | 2025-10-17 | Added | Versioning YAML, improved header/badges, clarified usage blocks, enhanced acceptance checklist. |
| v1.6.2 | 2025-10-17 | Fixed | Clean markdown format; unified examples; single-block delivery. |
| v1.6.1 | 2025-10-17 | Improved | Acceptance checklist + CI-ready sections. |
| v1.6.0 | 2025-10-16 | Added | Metrics, pagination, structured logs, and caching improvements. |

---

## 📚 References

- API Layer — `src/api/README.md`  
- Routes — `src/api/routes/README.md`  
- Schemas — `src/api/schemas/README.md`  
- Graph Queries — `src/graph/graph_queries.py`  
- MCP Docs — `docs/`

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*Reliable Utilities · Clear Contracts · Reproducible APIs*

</div>
```