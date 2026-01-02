# 🛰️ Kansas Frontier Matrix (KFM) API — `api/src`

[![API](https://img.shields.io/badge/KFM-API-2b6cb0)](#-kansas-frontier-matrix-kfm-api--apisrc)
[![Contract](https://img.shields.io/badge/contract-OpenAPI-85EA2D?logo=openapiinitiative&logoColor=white)](#-contracts--schemas)
[![Framework](https://img.shields.io/badge/framework-FastAPI-009688?logo=fastapi&logoColor=white)](#-local-development)
[![Auth](https://img.shields.io/badge/auth-JWT-6f42c1)](#-auth-roles-and-redaction)
[![Ops](https://img.shields.io/badge/ops-docker--compose-2496ED?logo=docker&logoColor=white)](#-local-development)

> 🧭 **Purpose:** this directory contains the **governed API boundary** for KFM — the single place where clients (UI + external integrations) access data, graph-backed views, simulations, and evidence artifacts.

---

## ✨ What lives here

This folder is the **API boundary implementation** (the “front door” to KFM). Typical responsibilities:

- 🧾 **Contract-first endpoints** (OpenAPI + JSON Schemas)
- 🔐 **Authentication & authorization** (JWT + roles + access levels)
- 🧼 **Redaction + classification enforcement** (no data leakage)
- 🧠 **Orchestration** for long-running jobs (simulations, batch analyses, model runs)
- 🛰️ **Interoperable outputs** (GeoJSON/CSV/GeoTIFF/NetCDF, where relevant)
- 📈 **Telemetry** (structured request logs, health checks, performance metrics)

---

## 🧭 Architectural guardrails (don’t break these)

These are project invariants for KFM-style development:

- ⛓️ **Pipeline ordering is absolute:** data must flow in the canonical sequence (ETL → catalogs → graph → API → UI → story/focus).  
- 🛑 **API boundary rule:** clients must **never** query graph stores directly. The API is the enforcement point for contracts + redaction.
- 🧬 **Provenance-first:** API responses should be able to carry evidence pointers (STAC/DCAT/PROV IDs/links) whenever the response expresses a claim.
- 🧷 **Classification propagation:** outputs must be **at least** as restricted as their inputs (no “privacy downgrade” through aggregation).
- 🧪 **Validation gates:** schema/contract checks + security checks should fail CI if invariants are violated.

> ✅ If you’re unsure whether something belongs in `api/src`, ask:  
> “Is this enforcing governance, contracts, redaction, or translating internal stores into stable client responses?”  
> If yes → it likely belongs here.

---

## 🗺️ High-level system flow

```mermaid
flowchart LR
  subgraph Data["📦 Data & Metadata"]
    A["Raw Sources"] --> B["ETL + Normalization"]
    B --> C["STAC Items + Collections"]
    C --> D["DCAT Dataset Views"]
    C --> E["PROV Lineage Bundles"]
  end

  C --> G["Neo4j Graph (references back to catalogs)"]
  G --> H["API Layer (contracts + redaction)"]
  H --> I["Map UI — React · MapLibre · (optional) Cesium"]
  I --> J["Story Nodes (governed narratives)"]
  J --> K["Focus Mode (provenance-linked context bundle)"]
```

---

## 📁 Directory layout (inside `api/src`)

> 🧩 This is the **recommended** structure for KFM-style API code. If your repo differs, keep the same *intent* (contracts separate from handlers, business logic separate from IO).

```text
📁 api/
└── 📁 src/
    ├── 📁 contracts/                # 📜 OpenAPI + shared contract fragments
    │   ├── 📄 openapi.yaml
    │   └── 📁 schemas/              # ✅ JSON Schemas used by API + validators
    ├── 📁 routers/                  # 🚦 HTTP route handlers (FastAPI routers / Flask blueprints)
    │   ├── 📁 v1/
    │   │   ├── 📄 health.py
    │   │   ├── 📄 auth.py
    │   │   ├── 📄 fields.py
    │   │   ├── 📄 simulations.py
    │   │   └── 📄 catalog.py
    │   └── 📄 __init__.py
    ├── 📁 middleware/               # 🧱 auth, request-id, CORS, rate limits, caching, etc.
    ├── 📁 auth/                     # 🔐 JWT verification, role checks, service tokens
    ├── 📁 services/                 # 🧠 business logic (use-cases; orchestration)
    ├── 📁 repositories/             # 🗃️ persistence ports (Postgres, Neo4j, object store)
    ├── 📁 integrations/             # 🔌 external APIs (NOAA, tile servers, ML inference service, etc.)
    ├── 📁 tasks/                    # 🧵 async jobs (Celery/RQ/worker adapters)
    ├── 📁 telemetry/                # 📈 logging, metrics, tracing helpers
    ├── 📁 utils/                    # 🧰 shared helpers (small + boring)
    ├── 📁 tests/                    # 🧪 unit + contract + integration tests (API-focused)
    └── 📄 main.py                   # 🚀 app entrypoint (FastAPI() / Flask app)
```

---

## 📜 Contracts & schemas

### OpenAPI (source of truth)
- ✅ Keep your OpenAPI definition **versioned** and **reviewed**.
- 🧪 Add **contract tests** that lock known inputs → known outputs.
- 🔄 Avoid breaking changes; if unavoidable, bump a version (e.g., `/v2`).

### JSON Schemas (validation gates)
- Use JSON Schema to validate:
  - Request payloads (server-side)
  - Response envelopes (CI checks)
  - “Evidence pointers” and provenance bundles (when returned)

> 💡 Contract-first workflow: update **contracts first**, then handlers/services, then tests.

---

## 🚀 Local development

### 1) Prereqs
- 🐍 Python (recommended for the main KFM REST API service)
- 🐳 Docker (recommended for running dependencies like DB/Neo4j/queues consistently)

### 2) Environment variables (typical)
Create an `api/.env` (or your platform’s equivalent) with values like:

```bash
# App
KFM_ENV=dev
KFM_LOG_LEVEL=INFO
KFM_API_HOST=0.0.0.0
KFM_API_PORT=8000

# Auth
KFM_JWT_ISSUER=kfm
KFM_JWT_AUDIENCE=kfm-ui
KFM_JWT_PUBLIC_KEY_PATH=./secrets/jwt_public.pem

# Data stores
KFM_POSTGRES_URL=postgresql://user:pass@localhost:5432/kfm
KFM_NEO4J_URI=bolt://localhost:7687
KFM_NEO4J_USER=neo4j
KFM_NEO4J_PASSWORD=please-change-me

# Governance
KFM_REDACTION_MODE=strict
KFM_DEFAULT_CLASSIFICATION=public
```

### 3) Run the API (example)
> ⚠️ Adjust the module path to your project (entrypoint varies by repo).

```bash
# from repo root
cd api

# install deps (pick the toolchain your repo uses)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# run (FastAPI typical)
uvicorn <your_package>.main:app --reload --host 0.0.0.0 --port 8000
```

### 4) Run dependencies (example compose)
```bash
docker compose up -d postgres neo4j redis
```

---

## 🔐 Auth, roles, and redaction

### JWT authentication
Typical client call pattern:

```http
Authorization: Bearer <jwt>
```

What to enforce at the API boundary:

- 🧍 **Identity** (valid signature, issuer, expiry)
- 🧑‍🔬 **Role checks** (user vs researcher vs admin)
- 🧷 **Operational access levels** for sensitive actions (admin-only endpoints)
- 🔒 **Inter-service auth** (service tokens) for internal microservice calls

### Redaction + classification propagation
- Output must respect:
  - user role
  - dataset classification tags
  - governance restrictions (e.g., sovereignty constraints)
- If an endpoint aggregates multiple datasets, the response’s classification must be **the strictest** of its inputs.

> ✅ Make it hard to accidentally leak data: prefer “deny-by-default” middleware + explicit allowlists.

---

## 🧵 Background jobs & real-time updates

### Long-running work (simulations / analyses / pipelines)
For expensive tasks:

- `POST /api/simulation/run` → returns `job_id`
- `GET /api/jobs/{job_id}` → progress + status + logs pointer (if allowed)
- results stored in DB/object store, referenced with provenance (PROV bundle IDs)

### Streaming / real-time (optional)
- WebSockets or Server-Sent Events for:
  - “new sensor data” notifications
  - job state changes
  - UI live refresh triggers (map layers / charts)

---

## 📈 Logging, monitoring, and health

Recommended minimum endpoints:

- `GET /health` ✅ (liveness)
- `GET /ready` ✅ (readiness; confirms DB/graph connectivity)
- `GET /metrics` 📊 (if you expose Prometheus-style metrics internally)

Logging baseline (per request):

- method + route
- user id (if authenticated)
- parameters (careful: never log secrets)
- status code
- duration
- correlation/request id

> 🧯 For errors: return a safe error message to clients + log stack traces internally with an error ID.

---

## 🧪 Testing strategy

A pragmatic KFM API test pyramid:

- ✅ **Unit tests** (services + redaction logic + auth checks)
- 🔁 **Contract tests** (OpenAPI + JSON Schema validation)
- 🧩 **Integration tests** (API ↔ Postgres/Neo4j/queue)
- 🧨 **Security tests** (auth bypass attempts, redaction regression cases)

Example commands (adjust to repo):

```bash
pytest -q
pytest -q -m contract
pytest -q -m integration
```

---

## ➕ Adding an endpoint (checklist)

When adding or changing an endpoint, do this **in order**:

1) 📜 **Update the contract**
   - OpenAPI path + request/response schemas
   - expected error codes (401/403/404/422/5xx)
   - versioning decision if breaking

2) 🧠 **Implement the use-case**
   - add service function (pure logic)
   - call repositories/integrations via interfaces (clean boundaries)

3) 🚦 **Add the router**
   - validate input
   - enforce auth + roles
   - apply redaction + classification

4) 🧪 **Add tests**
   - contract test snapshots
   - redaction regression cases
   - integration path (if it touches stores)

5) 📈 **Add telemetry**
   - structured logs
   - metrics / traces if relevant

---

## 🔌 Interoperability & exports

KFM endpoints should prefer standards-friendly outputs:

- 🗺️ GeoJSON (vector)
- 🧊 GeoTIFF / COG (raster)
- 🌦️ NetCDF (climate / gridded time series)
- 📄 CSV exports (tabular)

Where helpful, support:

- content negotiation (Accept headers)
- dedicated export endpoints (`/api/export/...`)
- stable IDs for datasets/collections/items (STAC/DCAT) and lineage (PROV)

---

## 🤝 Contributing notes

- ✅ Keep changes **small**, **contracted**, and **tested**
- 🧾 If you touch an endpoint, you likely need to touch:
  - `contracts/`
  - `routers/`
  - `tests/`
- 🧠 Keep “domain logic” in `services/`, not in route handlers
- 🔐 Treat governance + redaction as non-optional engineering, not “policy later”

---

## 🔗 Related docs (repo-level)

> These should exist at the repo root in a v13-aligned layout.

- 📘 `../../docs/MASTER_GUIDE_v13.md`
- 🧭 `../../docs/architecture/`
- 🧩 `../../schemas/`
- 🧪 `../../tests/`

---

### ✅ Quick self-check (before you PR)
- [ ] Did I update OpenAPI + schemas first?
- [ ] Did I add tests that would fail if my endpoint regresses?
- [ ] Did I verify redaction + classification propagation?
- [ ] Did I avoid direct client access to internal stores?
- [ ] Did I keep logs safe (no secrets, no sensitive payloads)?