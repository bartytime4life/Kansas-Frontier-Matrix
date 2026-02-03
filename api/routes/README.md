# 🧭 `api/routes/` — API Route Handlers (REST + GraphQL)

![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![OpenAPI](https://img.shields.io/badge/Docs-OpenAPI%20(Swagger)-85EA2D?logo=swagger&logoColor=black)
![GraphQL](https://img.shields.io/badge/Query-GraphQL-E10098?logo=graphql&logoColor=white)
![Policy](https://img.shields.io/badge/Governance-OPA%20Policies-7D3C98)

> [!NOTE]
> This folder is the **public HTTP entrypoint** into the system: it defines the request/response surface area that *every* client consumes (web UI, scripts, external apps). Keep it **thin, typed, governed, and testable**. ✅

---

## 🎯 What lives here

✅ **In this folder**
- Route modules grouped by **resource domain** (datasets, tiles, AI, ingest, etc.)
- **`APIRouter`** definitions (or equivalent) + endpoint docstrings
- Request parsing + validation (Pydantic models / typed params)
- Dependency injection (auth context, DB session, policy decision hooks)
- HTTP concerns: pagination, caching headers, streaming responses, status codes

🚫 **Not in this folder**
- Heavy business logic (put it in services/use-cases)
- Direct raw DB access without a repository/service abstraction
- Hidden “backdoors” that bypass governance checks

---

## 🧩 Core principle: the “Truth Path” 🔒

KFM is designed as a **layered pipeline** where clients **never** talk to databases directly. The API is the *single gate* where authentication, authorization, auditing, and policy checks are enforced.  
This is how we guarantee “the map behind the map” (provenance-first outputs). 🗺️🧾

---

## 🗂️ Suggested folder layout

> [!TIP]
> Keep filenames **noun-based** (domain), and expose a single `router` per module.

```text
api/
  routes/
    README.md                 🧭 you are here
    __init__.py               📦 exports / router registry
    health.py                 🩺 /healthz, /readyz, /version
    datasets.py               🗃️ /api/v1/datasets/...
    catalog.py                🧾 /api/v1/catalog/...
    query.py                  🔎 /api/v1/query (safe/allowlisted)
    tiles.py                  🧱 /tiles/{layer}/{z}/{x}/{y}.(pbf|png|webp)
    ai.py                     🤖 /api/v1/ai/...
    ingest.py                 🏭 /api/v1/ingest/...
    graphql.py                🧬 /graphql
```

> If Focus Mode is separated, expect a module like:
> - `focus_mode.py` 🤖🧠 (AI query + retrieval + citations)

---

## 🛣️ Route map (what endpoints belong where)

> [!IMPORTANT]
> Paths are versioned for REST (`/api/v1/...`). Some infrastructural routes may be unversioned (e.g., `/tiles/...`, `/graphql`).

| Module | Base path(s) | Purpose |
|---|---|---|
| `health.py` 🩺 | `/healthz`, `/readyz`, `/version` | Liveness/readiness/version checks |
| `datasets.py` 🗃️ | `/api/v1/datasets` | Dataset metadata + dataset data access |
| `catalog.py` 🧾 | `/api/v1/catalog` | Dataset discovery/search |
| `query.py` 🔎 | `/api/v1/query` | **Constrained** ad-hoc queries (validated + logged) |
| `tiles.py` 🧱 | `/tiles` | Vector/raster tiles for map clients |
| `ai.py` 🤖 | `/api/v1/ai` | Focus Mode query, streaming, suggestions |
| `ingest.py` 🏭 | `/api/v1/ingest` | Admin-only pipeline triggers + status |
| `graphql.py` 🧬 | `/graphql` | GraphQL endpoint (schema-backed queries) |

---

## 🧪 Route module template

```python
# api/routes/datasets.py
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/v1/datasets",
    tags=["datasets"],
)

class DatasetSummary(BaseModel):
    id: str
    title: str
    description: str | None = None

@router.get("/{dataset_id}", response_model=DatasetSummary)
async def get_dataset(
    dataset_id: str,
    # user = Depends(get_user),
    # policy = Depends(enforce_policy),
):
    # ✅ validate inputs
    # ✅ call service layer (no heavy logic here)
    # ✅ enforce policy (deny/sanitize)
    # ✅ include provenance/citations when relevant
    return DatasetSummary(id=dataset_id, title="Example")
```

---

## 📦 Response contracts

### ✅ JSON responses
- Default to JSON for all standard endpoints.
- Use consistent pagination fields for list endpoints (e.g., `limit`, `offset`/`cursor`, `total`, `next`).

### 🧱 Binary responses (tiles)
- Vector tiles: `.pbf` (MVT)
- Raster tiles: `.png` / `.webp`
- Set caching headers intentionally (public layers vs restricted layers).

### ❌ Error responses
Use a standardized error shape everywhere:
- stable `code`
- human-readable `message`
- optional `details`
- HTTP status code matches semantics (400/401/403/404/409/422/429/500)

> [!TIP]
> If you want to go “fully standard,” consider RFC7807-style responses (`type`, `title`, `status`, `detail`, `instance`)—but keep it consistent system-wide.

---

## 🛡️ Governance & policy enforcement (OPA) 🔐

KFM follows a **fail-closed** philosophy:
- If metadata is missing, policy fails, or access is unclear → **block** by default.
- Every request is authenticated and checked against:
  - user role
  - dataset sensitivity classification
  - endpoint permissions
  - auditing rules

**Practical implications for route authors**
- Never return restricted records “because it’s convenient.”
- Prefer **policy-driven shaping**:
  - deny (403)
  - sanitize/mask (200 with redactions)
  - aggregate (coarse resolution)

---

## 🤖 AI routes (Focus Mode) must be evidence-backed 📚

AI endpoints should:
- perform retrieval against governed stores (catalog/graph/spatial/search)
- produce answers that include **citations**
- run policy checks on both:
  - the *inputs* (prompt/question constraints)
  - the *outputs* (citations present, restricted content blocked)

> [!NOTE]
> If an AI answer can’t be grounded in approved sources, it should refuse or respond with “insufficient evidence” instead of guessing.

---

## 🏭 Ingest routes are privileged operations

Endpoints that trigger pipelines or ingestion (e.g., `/api/v1/ingest/runPipeline`) are:
- admin/maintainer only
- audited
- strongly validated (no arbitrary command execution)
- ideally idempotent or safely retryable

---

## ✅ Adding a new route (checklist)

- [ ] Create `api/routes/<domain>.py`
- [ ] Define `router = APIRouter(prefix="...", tags=[...])`
- [ ] Add endpoints with:
  - [ ] typed inputs
  - [ ] typed outputs (response models)
  - [ ] policy enforcement hook(s)
  - [ ] provenance/citation fields where applicable
- [ ] Register the router in your app/router registry (commonly `api/routes/__init__.py` or `api/main.py`)
- [ ] Add tests:
  - [ ] happy path
  - [ ] unauthorized/forbidden path
  - [ ] policy-deny/policy-sanitize behavior
  - [ ] pagination edge cases (limit/offset/cursor)
- [ ] Verify docs:
  - [ ] OpenAPI shows correct tags/summaries/examples
  - [ ] GraphQL (if used) updated & introspectable
- [ ] Add/adjust rate limits + caching if endpoint is high-volume

---

## 🔍 Local developer sanity checks

- Swagger/OpenAPI UI: `/docs`
- OpenAPI JSON: `/openapi.json`
- GraphQL endpoint: `/graphql`

> [!TIP]
> When adding routes, treat OpenAPI as a **contract**: if it’s confusing in `/docs`, it’s confusing for users.

---

## 🧠 Style guide for route authors (tiny rules, big payoff)

- **Name endpoints by nouns + HTTP verbs**  
  ✅ `GET /api/v1/datasets/{id}`  
  ✅ `GET /api/v1/catalog/search`  
  ✅ `POST /api/v1/ai/query`
- **Keep handlers short** (aim: < ~50 lines; push logic into services)
- **Never bypass the governance layer**
- **Prefer streaming for large feature exports**
- **Always document query params** (bbox, time range, format, etc.)
- **Log with a request-id** and include it in error responses

---

## 🧾 Appendix: Endpoint examples (for quick alignment)

```text
GET  /api/v1/datasets/{id}
GET  /api/v1/catalog/search?bbox=...&q=...&time=...
GET  /api/v1/datasets/{id}/data?format=geojson&bbox=...

GET  /api/v1/query?table=...&select=...&where=...&bbox=...

GET  /tiles/{layer}/{z}/{x}/{y}.pbf
GET  /tiles/{layer}/{z}/{x}/{y}.png
GET  /tiles/{layer}/{z}/{x}/{y}.webp

POST /api/v1/ai/query
GET  /api/v1/ai/suggestions
GET  /api/v1/ai/stream

POST /api/v1/ingest/runPipeline
```

---

## 🧭 Related docs

- See the higher-level API overview in `api/README.md` (or the server API README in the repo, if present).
- For system-wide architecture + governance, look under `docs/architecture/`.

---