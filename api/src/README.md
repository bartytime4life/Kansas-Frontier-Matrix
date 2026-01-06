# 🛰️ Kansas Frontier Matrix (KFM) API — `api/src`

[![KFM](https://img.shields.io/badge/Kansas%20Frontier%20Matrix-API-2b6cb0)](#-kansas-frontier-matrix-kfm-api--apisrc)
[![Framework](https://img.shields.io/badge/framework-FastAPI-009688?logo=fastapi&logoColor=white)](#-local-development)
[![Contract](https://img.shields.io/badge/contract-OpenAPI-85EA2D?logo=openapiinitiative&logoColor=white)](#-contracts--schemas)
[![Auth](https://img.shields.io/badge/auth-JWT%20%2B%20RBAC-6f42c1)](#-auth-roles-and-redaction)
[![Governance](https://img.shields.io/badge/governance-redaction%20%2B%20classification-critical)](#-security--governance-contract)
[![Ops](https://img.shields.io/badge/ops-docker--compose-2496ED?logo=docker&logoColor=white)](#-local-development)

> 🧭 **Purpose:** `api/src` is the **governed API boundary** for KFM — the single place where clients (UI + external integrations) access data, graph-backed views, simulations, and evidence artifacts.

> [!IMPORTANT]
> 🛑 **API boundary rule:** clients **must never** query internal stores (Neo4j/Postgres/object store) directly.  
> This layer enforces **contracts + auth + redaction + classification propagation** by design.

---

## 📌 Quick links

- [🧾 Doc metadata](#-doc-metadata)
- [✨ What lives here](#-what-lives-here)
- [🔒 Security & governance contract](#-security--governance-contract)
- [🧱 Clean architecture map](#-clean-architecture-map)
- [🧭 Architectural guardrails](#-architectural-guardrails-dont-break-these)
- [🗺️ High-level system flow](#️-high-level-system-flow)
- [📦 Response envelope](#-response-envelope-recommended)
- [📁 Directory layout](#-directory-layout-inside-apisrc)
- [📜 Contracts & schemas](#-contracts--schemas)
- [🚀 Local development](#-local-development)
- [🔐 Auth, roles, and redaction](#-auth-roles-and-redaction)
- [🧵 Background jobs & real-time updates](#-background-jobs--real-time-updates)
- [📈 Logging, monitoring, and health](#-logging-monitoring-and-health)
- [🧪 Testing strategy](#-testing-strategy)
- [➕ Adding an endpoint](#-adding-an-endpoint-checklist)
- [🔌 Interoperability & exports](#-interoperability--exports)
- [🤝 Contributing notes](#-contributing-notes)
- [🔗 Related docs](#-related-docs-repo-level)

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `api/src/README.md` |
| Status | Active ✅ |
| Last updated | **2026-01-06** |
| Applies to | API boundary code, contracts, routers, middleware, workers, integrations |

---

## ✨ What lives here

This folder is the **API boundary implementation** (the “front door” to KFM). Typical responsibilities:

- 📜 **Contract-first endpoints** (OpenAPI + JSON Schemas)
- 🔐 **Authentication & authorization** (JWT + RBAC/Scopes)
- 🧼 **Redaction + classification enforcement** (no data leakage)
- 🧠 **Orchestration** for long-running jobs (simulations, batch analyses, model runs)
- 🛰️ **Interoperable outputs** (GeoJSON/CSV/GeoTIFF/COG/NetCDF where relevant)
- 📈 **Telemetry** (structured logs, request IDs, health/ready/metrics, tracing hooks)

> [!TIP]
> If you’re unsure whether something belongs in `api/src`, ask:  
> **“Is this enforcing governance, contracts, redaction, or translating internal stores into stable client responses?”**  
> If yes → it likely belongs here.

---

## 🔒 Security & governance contract

KFM treats security as a **design constraint** at the API boundary, not “policy later”.

### ✅ Minimum guarantees this layer must provide

- 🔐 **AuthN**: verify token signature, issuer, audience, expiry, key rotation (`kid`)
- 🧑‍⚖️ **AuthZ**: role/scope enforcement for every data access path (no “implicit allow”)
- 🧼 **Redaction**: remove or transform restricted fields (deny-by-default)
- 🧷 **Classification propagation**: outputs must be **at least as restricted** as inputs  
  *(no privacy downgrade via aggregation or derived views)*
- 🧾 **Evidence pointers**: responses that make claims should link to provenance (STAC/DCAT/PROV IDs/URLs)
- 🧯 **Abuse resistance**: request size limits, rate limiting, SSRF controls, safe file handling
- 🧾 **Auditable behavior**: request-id / trace-id / “who did what” logs (never log secrets)

> [!IMPORTANT]
> Security reporting is private: see `../../SECURITY.md` and `../../docs/security/README.md` (once added).  
> **Never** handle vulnerability reports in public Issues/PR comments.

---

## 🧱 Clean architecture map

KFM’s API boundary is an **outer layer**. Domain and use-case logic must not depend on FastAPI, DB drivers, or cloud SDKs.

```mermaid
flowchart TB
  subgraph Outer["🧱 Frameworks & Drivers (outermost)"]
    UI["🖥️ UI Clients"]
    FW["🌐 FastAPI Routers + Middleware"]
    DB["🗄️ DB / Graph Drivers"]
    Cloud["☁️ Object Store / Cloud SDKs"]
    Queue["🧵 Workers / Queues"]
  end

  subgraph Adapters["🔌 Interface Adapters"]
    Repo["🗃️ Repositories (ports/adapters)"]
    Integrations["🔗 External Integrations"]
    Presenters["📦 Presenters / View Models"]
  end

  subgraph App["🧠 Application Layer"]
    UseCases["✅ Use-cases / Services (orchestration)"]
    Policies["🧷 Policy gates (classification/redaction)"]
  end

  subgraph Domain["💠 Domain (innermost)"]
    Entities["📚 Entities / Domain Models"]
    Rules["📐 Invariants / Business rules"]
  end

  UI --> FW
  FW --> Presenters
  FW --> Policies
  Policies --> UseCases
  UseCases --> Repo
  UseCases --> Integrations
  Repo --> DB
  Integrations --> Cloud
  UseCases --> Queue
  UseCases --> Entities
  Entities --> Rules
```

---

## 🧭 Architectural guardrails (don’t break these)

Project invariants for KFM-style development:

- ⛓️ **Pipeline ordering is absolute:** ETL → catalogs → graph → API → UI → story/focus  
- 🛑 **API boundary rule:** clients never query graph stores directly
- 🧬 **Provenance-first:** responses should carry evidence pointers when expressing a claim
- 🧷 **Classification propagation:** outputs ≥ strictest input classification
- 🧪 **Validation gates:** contract + schema + security checks should fail CI when violated
- 🧼 **Pure logic stays pure:** routers should be thin; business logic belongs in `services/` / `application/`
- 🧯 **Safe-by-default errors:** never leak stack traces or internals to clients; return error IDs
- 🔁 **Idempotency for “do work” endpoints:** job creation endpoints should support idempotency keys

> [!NOTE]
> The fastest way to create tech debt: “just put the query in the router.” Don’t.

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

  C --> G["🕸️ Neo4j Graph (references back to catalogs)"]
  D --> H["🛰️ API Layer (contracts + auth + redaction)"]
  E --> H
  G --> H

  H --> UI["🗺️ Map UI — React · MapLibre · (optional) Cesium"]
  H --> Ext["🔌 External Integrations (partners, pipelines)"]

  H --> Jobs["🧵 Job Queue / Workers (simulations, batch)"]
  Jobs --> Artifacts["📦 Artifacts Store (results, evidence)"]

  UI --> Story["📚 Story Nodes (governed narratives)"]
  Story --> Focus["🎯 Focus Mode (provenance-linked context bundle)"]
```

---

## 📦 Response envelope (recommended)

To make governance + debugging consistent, prefer a stable envelope:

```json
{
  "meta": {
    "request_id": "req_...",
    "classification": "public|restricted|confidential|... ",
    "provenance": {
      "stac": ["stac://..."],
      "dcat": ["dcat://..."],
      "prov": ["prov://..."]
    },
    "warnings": ["redacted_fields_applied"]
  },
  "data": {}
}
```

> [!TIP]
> If you can’t confidently label the output classification, you should not return the data.

---

## 📁 Directory layout (inside `api/src`)

> 🧩 This is the **recommended** structure for KFM-style API code.  
> If your repo differs, keep the same *intent* (contracts separate from handlers, business logic separate from IO).

```text
📁 api/
└── 📁 src/
    ├── 📁 contracts/                # 📜 OpenAPI + shared contract fragments
    │   ├── 📄 openapi.yaml
    │   └── 📁 schemas/              # ✅ JSON Schemas used by API + validators
    ├── 📁 routers/                  # 🚦 HTTP route handlers (FastAPI routers)
    │   ├── 📁 v1/
    │   │   ├── 📄 health.py
    │   │   ├── 📄 auth.py
    │   │   ├── 📄 fields.py
    │   │   ├── 📄 simulations.py
    │   │   └── 📄 catalog.py
    │   └── 📄 __init__.py
    ├── 📁 middleware/               # 🧱 auth, request-id, CORS, rate limits, caching, etc.
    ├── 📁 auth/                     # 🔐 JWT verification, role checks, service tokens
    ├── 📁 services/                 # 🧠 use-cases; orchestration; policy gates
    ├── 📁 repositories/             # 🗃️ persistence ports (Postgres, Neo4j, object store)
    ├── 📁 integrations/             # 🔌 external APIs (NOAA, tile servers, inference svc, etc.)
    ├── 📁 tasks/                    # 🧵 async jobs (Celery/RQ/worker adapters)
    ├── 📁 telemetry/                # 📈 logging, metrics, tracing helpers
    ├── 📁 utils/                    # 🧰 shared helpers (small + boring)
    ├── 📁 tests/                    # 🧪 unit + contract + integration tests (API-focused)
    └── 📄 main.py                   # 🚀 app entrypoint (FastAPI() app)
```

<details>
<summary><strong>🧠 Optional: “clean architecture flavored” package split</strong></summary>

If you want a more explicit split, you can group internals like this:

```text
📁 api/src/
├── 📁 app/                 # FastAPI app wiring (routers, middleware, DI)
├── 📁 domain/              # entities + invariants (no FastAPI imports)
├── 📁 application/         # use-cases (calls ports)
├── 📁 adapters/            # repositories/integrations (implements ports)
├── 📁 infrastructure/      # DB drivers, cloud clients, queue wiring
└── 📁 contracts/           # OpenAPI + JSON Schemas
```

</details>

---

## 📜 Contracts & schemas

### OpenAPI (source of truth)
- ✅ Keep OpenAPI **versioned** and **reviewed**
- 🧪 Add **contract tests** that lock known inputs → known outputs
- 🔄 Avoid breaking changes; if unavoidable, bump a version (`/v2`, new schemas)

### JSON Schemas (validation gates)
Use JSON Schema to validate:

- request payloads (server-side)
- response envelopes (CI checks)
- evidence pointers + provenance bundles

> [!TIP]
> Contract-first workflow: update **contracts first**, then handlers/services, then tests.

---

## 🚀 Local development

### 1) Prereqs
- 🐍 Python (primary service language)
- 🐳 Docker (recommended for DB/Neo4j/queues consistency)

### 2) Environment variables (typical)

Create `api/.env` (or your platform equivalent):

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

# Governance
KFM_REDACTION_MODE=strict
KFM_DEFAULT_CLASSIFICATION=public

# Stores
KFM_POSTGRES_URL=postgresql://user:pass@localhost:5432/kfm
KFM_NEO4J_URI=bolt://localhost:7687
KFM_NEO4J_USER=neo4j
KFM_NEO4J_PASSWORD=please-change-me

# Ops (recommended)
KFM_CORS_ORIGINS=http://localhost:3000
KFM_REQUEST_MAX_BYTES=10485760   # 10MB
```

> [!CAUTION]
> Never commit real secrets. Use `.env` locally and secret managers in CI/prod.

### 3) Run dependencies (example compose)

```bash
docker compose up -d postgres neo4j redis
```

### 4) Run the API (example)

```bash
# from repo root
cd api

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# FastAPI typical
uvicorn <your_package>.main:app --reload --host 0.0.0.0 --port 8000
```

### 5) Docs UI (FastAPI default)
- `/docs` (Swagger UI)
- `/redoc` (ReDoc)

---

## 🔐 Auth, roles, and redaction

### JWT authentication
Typical client call:

```http
Authorization: Bearer <jwt>
```

### What to enforce at the boundary
- 🧍 **Identity**: valid signature, issuer, audience, expiry
- 🧑‍🔬 **Roles/scopes**: least privilege for endpoints and dataset classes
- 🧷 **Operational access levels**: admin-only actions are explicitly gated
- 🔒 **Service-to-service auth**: service tokens or mTLS (when applicable)

### Redaction + classification propagation
Outputs must respect:

- user role/scopes
- dataset classification tags
- governance restrictions (sovereignty constraints, private infrastructure, etc.)

If an endpoint aggregates multiple datasets, the output classification must be:

- **the strictest classification** of its inputs
- plus any added restrictions introduced by derived inference risk

> ✅ Prefer “deny-by-default” middleware + explicit allowlists for fields.

---

## 🧵 Background jobs & real-time updates

### Long-running work (simulations / analyses / pipelines)

For expensive tasks:

- `POST /api/simulation/run` → returns `job_id`
- `GET /api/jobs/{job_id}` → progress + status + logs pointer (if allowed)
- results stored in DB/object store, referenced with provenance (PROV bundle IDs)

**Job safety expectations:**
- 🔁 Idempotency keys for create/run endpoints
- 🧯 Explicit timeouts/deadlines for workers
- 🧾 Provenance recorded for inputs + outputs (reproducibility)

### Streaming / real-time (optional)
- WebSockets or Server-Sent Events for:
  - job state changes
  - “new sensor data” notifications
  - UI refresh triggers (map layers / charts)

---

## 📈 Logging, monitoring, and health

Recommended minimum endpoints:

- `GET /health` ✅ liveness
- `GET /ready` ✅ readiness (DB/graph connectivity)
- `GET /metrics` 📊 (internal Prometheus-style metrics)

Logging baseline (per request):

- method + route
- user id (if authenticated)
- parameter metadata (never secrets)
- status code
- duration
- correlation/request id

> [!IMPORTANT]
> Return safe errors to clients. Log stack traces internally with an error ID.

---

## 🧪 Testing strategy

A pragmatic KFM API test pyramid:

- ✅ **Unit tests** (services + redaction logic + auth checks)
- 🔁 **Contract tests** (OpenAPI + JSON Schema validation)
- 🧩 **Integration tests** (API ↔ Postgres/Neo4j/queue)
- 🧨 **Security regression tests** (auth bypass attempts, redaction regressions)

Example commands (adjust to repo):

```bash
pytest -q
pytest -q -m contract
pytest -q -m integration
```

<details>
<summary><strong>🧷 Recommended “security regression” test cases</strong></summary>

- unauthenticated access to every protected route returns 401
- authenticated but unauthorized role returns 403
- redaction removes restricted fields (and is tested)
- SSRF protections block private IP ranges (if any URL-fetching exists)
- request size limits enforced for uploads/large payloads
- file path traversal attempts rejected (uploads/downloads)

</details>

---

## ➕ Adding an endpoint (checklist)

When adding or changing an endpoint, do this **in order**:

1) 📜 **Update the contract**
   - OpenAPI path + request/response schemas
   - expected error codes (401/403/404/422/5xx)
   - version bump decision if breaking

2) 🧠 **Implement the use-case**
   - service function (pure logic)
   - call repositories/integrations via interfaces (clean boundaries)

3) 🚦 **Add the router**
   - validate input
   - enforce auth + scopes
   - apply redaction + classification

4) 🧪 **Add tests**
   - contract snapshots
   - redaction regression cases
   - integration path (if it touches stores)

5) 📈 **Add telemetry**
   - structured logs
   - metrics / traces if relevant

6) 🔒 **Threat-check**
   - What’s the worst abuse case?
   - What’s the maximum data exposure if compromised?
   - Is the output classification correct?

---

## 🔌 Interoperability & exports

Prefer standards-friendly outputs:

- 🗺️ GeoJSON (vector)
- 🧊 GeoTIFF / COG (raster)
- 🌦️ NetCDF (climate / gridded time series)
- 📄 CSV (tabular)

Where helpful, support:

- content negotiation (`Accept` headers)
- dedicated export endpoints (`/api/export/...`)
- stable IDs for datasets/collections/items (STAC/DCAT) and lineage (PROV)

---

## 🤝 Contributing notes

- ✅ Keep changes **small**, **contracted**, and **tested**
- 🧾 If you touch an endpoint, you likely touch:
  - `contracts/`
  - `routers/`
  - `tests/`
- 🧠 Keep domain/use-case logic in `services/`, not in route handlers
- 🔐 Treat governance + redaction as non-optional engineering

---

## 🔗 Related docs (repo-level)

> These should exist at the repo root in a v13-aligned layout.

- 📘 `../../docs/MASTER_GUIDE_v13.md`
- 🧭 `../../docs/architecture/`
- 🔐 `../../SECURITY.md`
- 🛡️ `../../docs/security/README.md`
- 🧩 `../../schemas/`
- 🧪 `../../tests/`