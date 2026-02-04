---
title: "PostGIS Adapter 🐘🗺️"
path: "api/adapters/postgis/README.md"
version: "KFM-MDP v11.2.6"
last_updated: "2026-02-03"
status: "active"
doc_kind: "readme"
owners:
  - "KFM Engineering"
  - "GIS/DB Working Group"
tags:
  - "kfm"
  - "api"
  - "adapters"
  - "postgis"
  - "spatial-sql"
  - "mvt"
  - "provenance"
  - "policy-gate"
license: "Apache-2.0"
---

# PostGIS Adapter 🐘🗺️

![adapter](https://img.shields.io/badge/layer-adapter-blue)
![db](https://img.shields.io/badge/db-PostGIS-316192)
![contract](https://img.shields.io/badge/contract-fail--closed-red)
![provenance](https://img.shields.io/badge/provenance-evidence--first-brightgreen)

The **PostGIS adapter** is the **single, governed** access point from the KFM API layer into **PostgreSQL/PostGIS**.  
It encapsulates *all* spatial database interactions so the rest of the system never “talks SQL” directly.

> KFM’s backend uses adapter modules to encapsulate interactions with PostGIS (and other stores), keeping concerns separated and enforceable.  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
> The abstraction layer enables swapping implementations (e.g., PostGIS → other spatial stores) with minimal changes above.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🎯 Why this adapter exists

### ✅ Enforces the KFM “Truth Path”
This adapter helps ensure the platform flow stays canonical:

**UI/Clients → API → Adapter → PostGIS** (no bypasses)

### ✅ Keeps business logic clean
Routes/services ask for **domain operations** (e.g., “get tiles”, “query features”, “resolve place geometry”), not raw SQL strings.

### ✅ Centralizes governance
Security, performance, provenance hooks, query logging, and policy constraints belong **here**, not scattered across handlers.

---

## 🧩 Responsibilities

### 1) Connection + transaction boundaries 🔌
- Owns engine/pool lifecycle (or receives it via DI)
- Enforces transaction semantics (`read-only`, `repeatable read` where needed)
- Ensures safe shutdown and connection hygiene

### 2) Spatial query execution 🧠
- Prepared statements / parameter binding (no string concatenation)
- Schema scoping + allowlisted tables/views
- Spatial filters: bbox, intersects, within, buffer, distance, etc.
- SRID normalization + geometry validation

### 3) Tile generation + map serving 🧱
Common responsibilities (as implemented/needed):
- MVT tile generation (e.g., `ST_AsMVT`, `ST_AsMVTGeom`)
- Simplification/generalization by zoom
- Attribute projection + column allowlists
- Deterministic ordering for stable tiles

### 4) Provenance + audit hooks 🧾
- Attach query metadata to logs/trace spans:
  - dataset IDs
  - STAC/DCAT references
  - request IDs / user scopes
  - policy decision IDs (OPA)
- Emit “evidence pointers” so results can be cited downstream

### 5) Performance + observability 📈
- Query timing + row counts + cache hints
- Slow-query thresholds
- EXPLAIN (dev-only) toggles for tuning

---

## 📁 Suggested local layout (within this folder)

> Keep filenames simple and intention-revealing. Avoid mixing domain policy with SQL glue.

```text
api/adapters/postgis/
├─ README.md                 👈 you are here
├─ client.py                 🔌 engine/pool, session helpers
├─ queries/
│  ├─ tiles.sql              🧱 MVT / raster tile SQL templates
│  ├─ features.sql           🧭 feature search/filter SQL templates
│  └─ health.sql             🩺 readiness checks
├─ repo/
│  ├─ layers_repo.py         🗺️ layer + tiles entrypoints
│  ├─ places_repo.py         📍 gazetteer/geometry lookups
│  └─ datasets_repo.py       🧾 dataset metadata joins
├─ models.py                 🧩 typed DTOs for adapter outputs
├─ errors.py                 🚨 exception mapping + fail-closed defaults
└─ tests/
   ├─ test_queries.py        ✅ query unit tests
   └─ test_integration.py    🧪 PostGIS container tests
```

---

## 🔐 Security & governance rules (non-negotiable)

### Deny-by-default 🚫
- If a request cannot be mapped to an allowlisted operation, **fail closed**
- Never expose raw SQL errors to clients (sanitize and map)

### Least privilege 👮
Use dedicated DB roles:
- `kfm_api_reader` (read-only)
- `kfm_api_writer` (if needed; avoid in public endpoints)
- Optional RLS policies for restricted datasets

### Parameterization only 🧷
All user-controlled inputs must be bound parameters:
- bbox, SRID, limits, text search, ids, zoom, time ranges

### Geometry sanity 🧼
- Enforce expected SRID (e.g., 4326 at API boundary; transform inside DB if needed)
- Validate geometry (reject invalid unless explicitly repairing in a controlled pipeline stage)

---

## 🧪 Testing strategy

### Unit tests ✅
- SQL template rendering
- Input validation (bbox, zoom, ids, time ranges)
- Exception mapping (DB timeout → 503, policy deny → 403, etc.)

### Integration tests 🧪
- Use ephemeral PostGIS (e.g., docker/testcontainers)
- Apply migrations
- Load tiny fixture datasets
- Validate:
  - spatial predicates
  - tile output determinism
  - SRID transformations
  - performance expectations (basic thresholds)

---

## ⚙️ Configuration (expected env vars)

> Exact naming depends on repo conventions; keep these centralized and documented.

```bash
POSTGIS_HOST=localhost
POSTGIS_PORT=5432
POSTGIS_DB=kfm
POSTGIS_USER=kfm_api_reader
POSTGIS_PASSWORD=***           # never commit
POSTGIS_SCHEMA=public
POSTGIS_STATEMENT_TIMEOUT_MS=30000
POSTGIS_POOL_SIZE=10
POSTGIS_MAX_OVERFLOW=20
```

Pair this with `.env.example` in the repo root and ensure CI checks for drift.

---

## 🧭 Example adapter contract

### ✅ Good: domain operation (what the API calls)
```python
tiles = postgis_layers_repo.get_vector_tile(
    layer_id="counties",
    z=8, x=59, y=96,
    time=None,
    filters={"state_fips": "20"},
)
```

### ❌ Bad: raw SQL leaking into handlers
```python
sql = f"SELECT * FROM {table} WHERE ST_Intersects(geom, {bbox})"
```

---

## 🚀 Performance notes (practical defaults)

- Prefer **bbox-first** filtering (index-friendly)
- Use `GIST` / `SP-GiST` where appropriate
- For tiles:
  - simplify geometry based on zoom
  - restrict columns
  - cap feature counts per tile (fail closed or degrade gracefully)
- Keep “expensive joins” behind explicit endpoints (and track them)

---

## 🔄 Change management

### Migrations 🧱
- All schema changes go through migrations (never ad-hoc)
- Migration PRs must include:
  - rollback notes
  - updated adapter queries/tests
  - performance considerations (index updates)

### Backward compatibility 🧷
- Adapter must support old clients during transition windows
- Use feature flags where needed (API-level)

---

## 🔗 Related docs

- `docs/architecture/system_overview.md` 🧠
- `docs/architecture/ai/RAG_RETRIEVAL.md` 🤖
- `docs/architecture/ai/PROMPT_GATE.md` 🚦
- `docs/architecture/diagrams/` 🗺️

---

## 📚 Sources (project internal)

- KFM architecture notes referencing PostGIS as core geospatial database + adapter module pattern.  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- KFM technical blueprint notes on adapter abstraction enabling store swaps with minimal upstream changes.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- (Repo-linked reference required by tooling)  [oai_citation:4‡graphical-data-analysis-with-r.pdf](sediment://file_00000000778871f58bf725232fae201b)