# 🛰️ Kansas Frontier Matrix (KFM) API — `api/src/`

<p align="left">
  <a href="#-kansas-frontier-matrix-kfm-api--apisrc"><img alt="KFM API" src="https://img.shields.io/badge/Kansas%20Frontier%20Matrix-API-2b6cb0" /></a>
  <a href="#-local-development"><img alt="FastAPI" src="https://img.shields.io/badge/framework-FastAPI-009688?logo=fastapi&logoColor=white" /></a>
  <a href="#-contracts--schemas"><img alt="OpenAPI" src="https://img.shields.io/badge/contract-OpenAPI-85EA2D?logo=openapiinitiative&logoColor=white" /></a>
  <a href="#-auth-roles-and-redaction"><img alt="Auth" src="https://img.shields.io/badge/auth-JWT%20%2B%20RBAC%2FABAC-6f42c1" /></a>
  <a href="#-security--governance-contract"><img alt="Governance" src="https://img.shields.io/badge/governance-redaction%20%2B%20classification-critical" /></a>
  <a href="#-background-jobs--real-time-updates"><img alt="Workers" src="https://img.shields.io/badge/workers-queue%20%2B%20jobs-purple" /></a>
  <a href="#-logging-monitoring-and-health"><img alt="Observability" src="https://img.shields.io/badge/observability-logs%20%7C%20metrics%20%7C%20traces-7c3aed" /></a>
  <a href="#-local-development"><img alt="Ops" src="https://img.shields.io/badge/ops-docker--compose-2496ED?logo=docker&logoColor=white" /></a>
</p>

> 🧭 **Purpose:** `api/src/` is the **governed API boundary** for KFM — the one place where clients (UI + external integrations) access **catalog-backed views**, **graph-backed context**, **jobs/simulations**, and **evidence artifacts**.

> [!IMPORTANT]
> 🛑 **API boundary rule:** clients **must never** query internal stores (Neo4j/Postgres/object store) directly.  
> This layer enforces **contracts + auth + policy + redaction + classification propagation** by design.

> [!IMPORTANT]
> 🧱 **Pipeline order is absolute:** **ETL → STAC/DCAT/PROV Catalogs → Graph → API → UI → Story Nodes → Focus Mode**  
> If a result isn’t **cataloged + provenance-linked**, it isn’t *publishable* in KFM.

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
- [📚 Project reference library → implementation rules](#-project-reference-library--implementation-rules-uses-all-project-files)

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `api/src/README.md` |
| Status | Active ✅ |
| Last updated | **2026-01-07** |
| Scope | API boundary code, contracts, routers, middleware, workers, integrations |
| Promise | “No mystery data” — everything served is policy-checked & provenance-linked |

---

## ✨ What lives here

This folder is the **API boundary implementation** (the “front door” to KFM). Typical responsibilities:

- 📜 **Contract-first endpoints** (OpenAPI + JSON Schemas + examples)
- 🔐 **Authentication & authorization** (JWT, RBAC/ABAC, service-to-service patterns)
- 🧼 **Redaction + classification enforcement** (deny-by-default, “no privacy downgrade”)
- 🧾 **Evidence & provenance linking** (STAC/DCAT/PROV IDs, evidence bundles for Story/Focus)
- 🧠 **Orchestration** for long-running jobs (simulations, batch analyses, model runs)
- 🛰️ **Interoperable outputs** (GeoJSON/CSV/tiles/thumbnails, and pointers to COG/NetCDF artifacts)
- 📈 **Telemetry** (structured logs, request IDs, health/ready/metrics, tracing hooks)
- 🧯 **Abuse resistance** (request size limits, rate limiting, safe file handling, SSRF controls)

> [!TIP]
> If you’re unsure whether something belongs in `api/src/`, ask:  
> **“Is this enforcing governance, contracts, redaction, or translating internal stores into stable client responses?”**  
> If yes → it likely belongs here.

---

## 🔒 Security & governance contract

KFM treats security as a **design constraint** at the API boundary, not “policy later”.

### ✅ Minimum guarantees this layer must provide

- 🔐 **AuthN**: verify token signature, issuer, audience, expiry, key rotation (`kid`)
- 🧑‍⚖️ **AuthZ**: role/scope enforcement for every data access path (**no implicit allow**)
- 🧼 **Redaction**: remove/mask/generalize restricted fields (**deny-by-default**)
- 🧷 **Classification propagation**: outputs must be **≥ strictest input classification**  
  *(no privacy downgrade via aggregation or derived views)*
- 🧾 **Evidence pointers**: any response that “makes a claim” links to provenance (STAC/DCAT/PROV + run IDs)
- 🧯 **Abuse resistance**: request size limits, rate limiting, SSRF controls, safe file handling
- 🧾 **Auditable behavior**: request-id / trace-id / “who did what” logs (**never log secrets**)
- 🧬 **Reproducibility**: job endpoints store parameters + versions + artifacts; results are not “magic”

### 🧨 Threat posture (assume hostile inputs)
Treat everything as untrusted:
- GeoJSON & WKT payloads
- file uploads (archives, rasters, zips)
- external URLs (SSRF risk)
- 3D/model assets (parser risks)
- user-provided query filters (injection / cost amplification)

> [!CAUTION]
> “It’s internal” is not a defense. Internal systems are breached too. Build as if everything will be fuzzed. 🧪🛡️

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

### 🔍 “Where does this code go?” (fast rule)
- Route handlers = **IO + validation + auth gate + call use-case**
- Use-cases/services = **policy + orchestration + business decisions**
- Repositories/integrations = **how to talk to stores/APIs**
- Domain = **pure invariants** (no framework imports)

---

## 🧭 Architectural guardrails (don’t break these)

Project invariants for KFM-style development:

- ⛓️ **Pipeline ordering is absolute:** ETL → catalogs → graph → API → UI → story/focus  
- 🛑 **API boundary rule:** clients never query graph stores directly
- 🧬 **Provenance-first:** claim-like responses carry evidence pointers
- 🧷 **Classification propagation:** outputs ≥ strictest input classification
- 🧪 **Validation gates:** contract + schema + security checks fail CI when violated
- 🧼 **Pure logic stays pure:** routers thin; business logic lives in services/application
- 🧯 **Safe-by-default errors:** no stack traces; return error IDs + correlation IDs
- 🔁 **Idempotency:** “do work” endpoints support idempotency keys
- 🧵 **Bounded work:** avoid unbounded fanout / unbounded parsing / unbounded response sizes

> [!NOTE]
> The fastest way to create tech debt: “just put the query in the router.” Don’t. 😅

---

## 🗺️ High-level system flow

```mermaid
flowchart LR
  subgraph Data["📦 Data & Metadata"]
    A["Raw Sources"] --> B["ETL + Normalization"]
    B --> C["🏷️ STAC Items + Collections"]
    C --> D["🧾 DCAT Dataset Views"]
    C --> E["🧬 PROV Lineage Bundles"]
  end

  C --> G["🕸️ Graph (references back to catalogs)"]
  D --> H["🚪 API Boundary (contracts + auth + policy + redaction)"]
  E --> H
  G --> H

  H --> UI["🌐 UI (React + MapLibre/Cesium)"]
  H --> Ext["🔌 External Integrations"]

  H --> Jobs["🧵 Queue / Workers (simulations, batch, ML)"]
  Jobs --> Artifacts["📦 Object Store (results, thumbnails, tiles)"]
  Jobs --> C

  UI --> Story["📚 Story Nodes (governed narratives)"]
  Story --> Focus["🎯 Focus Mode (evidence bundle)"]
```

---

## 📦 Response envelope (recommended)

To make governance + debugging consistent, prefer a stable envelope:

```json
{
  "meta": {
    "request_id": "req_...",
    "classification": "public|internal|restricted",
    "provenance": {
      "dataset_ids": ["kfm.ks.ndvi.weekly.v1"],
      "stac": ["stac://collection/.../item/..."],
      "dcat": ["dcat://dataset/..."],
      "prov": ["prov://run/..."]
    },
    "warnings": ["redacted_fields_applied"]
  },
  "data": {}
}
```

### 🧾 Evidence bundle payload (Story Nodes + Focus Mode)
When the UI needs a “defensible narrative packet”, return an evidence-first shape:

```json
{
  "bundle_id": "evb_01HZZ...",
  "classification": "internal",
  "claims": [
    {
      "id": "claim_001",
      "text": "NDVI declined 0.12 vs baseline in July.",
      "support": {
        "stac_items": ["..."],
        "prov_runs": ["..."],
        "artifacts": [{"type": "plot", "href": "s3://.../ndvi_plot.png"}]
      },
      "uncertainty": {
        "type": "interval",
        "lower": -0.18,
        "upper": -0.07,
        "confidence": 0.9
      }
    }
  ]
}
```

> [!TIP]
> If you can’t confidently label the output classification, you should not return the data.

---

## 📁 Directory layout (inside `api/src`)

> 🧩 Recommended KFM structure: contracts separate from handlers, business logic separate from IO, and policy gates centralized.

```text
📁 api/
└── 📁 src/
    ├── 📁 contracts/                 # 📜 OpenAPI + shared contract fragments
    │   ├── 📄 openapi.yaml           # ✅ API source of truth
    │   └── 📁 schemas/               # ✅ JSON Schemas: STAC/DCAT/PROV/Evidence
    ├── 📁 routers/                   # 🚦 HTTP route handlers (FastAPI routers)
    │   ├── 📁 v1/
    │   │   ├── 📄 health.py
    │   │   ├── 📄 auth.py
    │   │   ├── 📄 fields.py
    │   │   ├── 📄 catalog.py
    │   │   ├── 📄 evidence.py
    │   │   ├── 📄 analysis.py
    │   │   └── 📄 simulations.py
    │   └── 📄 __init__.py
    ├── 📁 middleware/                # 🧱 auth, request-id, CORS, rate limits, caching
    ├── 📁 auth/                      # 🔐 JWT verification, role checks, service tokens
    ├── 📁 policy/                    # 🧷 classification/redaction + (optional) OPA bundles
    ├── 📁 services/                  # 🧠 use-cases; orchestration; policy gates
    ├── 📁 repositories/              # 🗃️ Postgres/Neo4j/object store adapters
    ├── 📁 integrations/              # 🔌 external APIs (GEE, NOAA, etc.)
    ├── 📁 tasks/                     # 🧵 worker jobs + queue adapters
    ├── 📁 telemetry/                 # 📈 logging, metrics, tracing helpers
    ├── 📁 utils/                     # 🧰 small + boring helpers
    ├── 📁 tests/                     # 🧪 unit + contract + integration (API-focused)
    └── 📄 main.py                    # 🚀 app entrypoint (FastAPI() app)
```

<details>
<summary><strong>🧠 Optional: “explicit clean architecture” package split</strong></summary>

```text
📁 api/src/
├── 📁 app/                  # FastAPI wiring (routers, middleware, DI)
├── 📁 domain/               # entities + invariants (pure Python)
├── 📁 application/          # use-cases (calls ports)
├── 📁 adapters/             # repositories/integrations (implements ports)
├── 📁 infrastructure/       # DB drivers, cloud clients, queue wiring
└── 📁 contracts/            # OpenAPI + JSON Schemas
```

</details>

---

## 📜 Contracts & schemas

### OpenAPI (source of truth)
- ✅ Keep OpenAPI **versioned**, **reviewed**, and **diff-checked** in CI
- 🧪 Add **contract tests** (examples validate against OpenAPI + JSON Schema)
- 🔄 Breaking changes require version bump (`/v2`) or parallel route set

### JSON Schema validation (gates)
Use JSON Schema to validate:
- request payloads (server-side)
- response envelopes (CI checks)
- evidence pointers + provenance bundles
- job result manifests (artifact metadata)

### Contract-first workflow (golden path)
1) edit OpenAPI + schema  
2) update service/use-case  
3) update router  
4) update tests + examples  
5) ship ✅

> [!TIP]
> If the schema can’t express the rule, the contract isn’t done yet.

---

## 🚀 Local development

### 1) Prereqs
- 🐍 Python (primary)
- 🐳 Docker (recommended for DB/graph/queues consistency)

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
KFM_CORS_ORIGINS=http://localhost:5173
KFM_REQUEST_MAX_BYTES=10485760   # 10MB
KFM_RATE_LIMIT_ENABLED=true
```

> [!CAUTION]
> Never commit real secrets. Use `.env` locally and secret managers in CI/prod.

### 3) Run dependencies (example compose)
```bash
docker compose up -d postgres neo4j redis
```

### 4) Run the API (example)
```bash
cd api

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

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

### RBAC + ABAC (recommended)
- **RBAC**: user roles (`viewer`, `editor`, `admin`)
- **ABAC**: data attributes (classification, license constraints, org ownership, export permissions)

### Redaction strategies (choose explicitly)
- ✂️ **Drop**: remove fields entirely
- 🫥 **Mask**: partially hide sensitive text/IDs
- 🧮 **Generalize**: reduce precision (e.g., centroid to county)
- 📉 **Aggregate**: roll up to safe statistics
- ⏳ **Delay**: only publish after review / time threshold
- 🚫 **Deny**: return 403 for restricted assets

### Classification propagation (strict)
If an endpoint aggregates multiple datasets, the output classification must be:
- **the strictest classification** of its inputs  
- plus any added restrictions introduced by inference risk

> ✅ Prefer “deny-by-default” middleware + explicit allowlists for fields.

---

## 🧵 Background jobs & real-time updates

### Long-running work (simulations / analyses / pipelines)
For expensive tasks:
- `POST /api/v1/.../run` → returns `job_id`
- `GET /api/v1/jobs/{job_id}` → status/progress
- `GET /api/v1/jobs/{job_id}/result` → stable pointers once published

**Job safety expectations**
- 🔁 Idempotency keys for create/run endpoints
- 🧯 Explicit timeouts/deadlines for workers
- 🧾 Provenance recorded for inputs + outputs (PROV run bundles)
- 🧪 Deterministic params: store seeds, versions, and exact inputs

### Real-time (optional)
- WebSockets or SSE for:
  - job progress changes
  - publish events (“new STAC item available”)
  - UI refresh triggers (layers/charts)

> [!TIP]
> Prefer push updates for progress to avoid poll-storms.

---

## 📈 Logging, monitoring, and health

Recommended minimum endpoints:
- `GET /health` ✅ liveness
- `GET /ready` ✅ readiness (DB/graph connectivity)
- `GET /metrics` 📊 (Prometheus style, if enabled)

Logging baseline (per request):
- method + route
- user id + org id (if authenticated)
- parameter metadata (never secrets)
- status code
- duration
- correlation/request id
- classification outcome (safe label only)

> [!IMPORTANT]
> Return safe errors to clients. Log stack traces internally with an error ID + request ID.

---

## 🧪 Testing strategy

A pragmatic KFM API test pyramid:

- ✅ **Unit tests**: services + policy gates + redaction + auth helpers
- 🔁 **Contract tests**: OpenAPI + JSON Schema validation (golden examples)
- 🧩 **Integration tests**: API ↔ Postgres/Neo4j/queue (happy path + timeouts)
- 🧨 **Security regression tests**: auth bypass attempts, redaction regressions, SSRF prevention

Example commands (adjust to repo):
```bash
pytest -q
pytest -q -m contract
pytest -q -m integration
pytest -q -m security
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

When adding/changing an endpoint, do this **in order**:

1) 📜 **Update the contract**
   - OpenAPI path + request/response schemas
   - expected error codes (401/403/404/422/5xx)
   - version bump decision if breaking

2) 🧠 **Implement the use-case**
   - service function (pure logic)
   - call repositories/integrations via interfaces (clean boundaries)
   - apply governance policy gates in the service layer (not in routers)

3) 🚦 **Add the router**
   - validate input
   - enforce auth + scopes
   - apply redaction + classification
   - return envelope + evidence pointers (when claim-like)

4) 🧪 **Add tests**
   - contract example validation
   - redaction regression cases
   - integration path (if it touches stores)

5) 📈 **Add telemetry**
   - structured logs
   - metrics/traces if relevant

6) 🔒 **Threat-check**
   - worst abuse case?
   - maximum data exposure if compromised?
   - output classification correct?

---

## 🔌 Interoperability & exports

Prefer standards-friendly outputs:
- 🗺️ GeoJSON (vector)
- 🧊 GeoTIFF / COG (raster) *(usually via object-store pointers)*
- 🌦️ NetCDF (gridded time series; if used)
- 📄 CSV (tabular)
- 🧬 PROV bundles (lineage)
- 🏷️ STAC/DCAT for discovery (catalog gate)

Where helpful:
- content negotiation (`Accept` headers)
- dedicated export endpoints (sync for small, async for large)
- stable IDs for datasets/collections/items and runs

---

## 🤝 Contributing notes

- ✅ Keep changes **small**, **contracted**, and **tested**
- 🧾 If you touch an endpoint, you likely touch:
  - `contracts/`
  - `routers/`
  - `services/`
  - `tests/`
- 🧠 Keep domain/use-case logic out of route handlers
- 🔐 Treat governance + redaction as non-optional engineering

---

## 🔗 Related docs (repo-level)

> These should exist at the repo root in a v13-aligned layout (add if missing).

- 📘 `../../docs/MASTER_GUIDE_v13.md`
- 🧭 `../../docs/architecture/`
- 🔐 `../../SECURITY.md`
- 🛡️ `../../docs/security/README.md`
- 🧩 `../../schemas/`
- 🧪 `../../tests/`

---

## 📚 Project reference library → implementation rules (uses all project files)

> Requirement: this section maps **every project file** to a concrete `api/src` convention, guardrail, or implementation rule.

<details>
<summary><strong>🧠 Expand: Influence map (all project files)</strong></summary>

| Project file | What it changes in `api/src` (practical impact) |
|---|---|
| `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx` | Defines boundary invariants, “catalog gate” rule, Story/Focus evidence flows, and system-of-systems integration posture |
| `Latest Ideas.docx` | Drives CI guardrails, governance enforcement emphasis, “policy as code” posture, and roadmap alignment for evidence bundles and 3D/tile delivery |
| `Data Spaces.pdf` | Strengthens pointer-over-payload design (serve references, not blobs), interoperability contracts, and trust signals in metadata |
| `Introduction to Digital Humanism.pdf` | Human-centered constraints: transparency, agency, and accountability; drives labeling of AI-assisted outputs and safe UX-facing explanations |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | Systems thinking: feedback loops and closure → encourages explicit state transitions (jobs), bounded behavior, and human-in-the-loop controls |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | Requires AI outputs be auditable/labeled; informs “evidence bundle” posture and dispute/appeal readiness |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | Informs GEE orchestration endpoints, time-series/derivative patterns, and catalog emission for remote-sensing jobs |
| `python-geospatial-analysis-cookbook.pdf` | CRS sanity, geometry transport conventions, PostGIS operations, and boundary transforms become explicit API conventions |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | Map-serving endpoints must avoid misleading defaults (ramps/legends/tiles); encourages evidence links for cartographic choices |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | Pushes offline/low-bandwidth patterns: tile endpoints, caching, small payloads, and location sensitivity awareness |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | Encourages robust indexing/paging, query cost awareness, stable IDs, and safe export patterns |
| `Scalable Data Management for Future Hardware.pdf` | Drives streaming, caching, concurrency bounds, and “avoid huge JSON blobs” discipline |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | Reinforces bounded queues/backpressure, safe concurrency, and avoiding runaway thread/worker behavior |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | Threat modeling mindset: segmentation, auth hardening, and safe network interaction patterns |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | Defensive posture: hostile inputs, unsafe parsing avoidance, strict validation, and minimal attack surface |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | Impacts quicklook/thumbnail endpoints: format choice, performance budgets, and content-type correctness |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | Informs 3D asset delivery: coordinate conventions, safe loading patterns, and keeping 3D as optional/policy-gated |
| `Spectral Geometry of Graphs.pdf` | Justifies explainable graph endpoints, bounded subgraph exports, and optional spectral metrics services |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | Demands simulation V&V posture: scenario metadata, reproducibility, explicit assumptions, and artifact tracking |
| `Generalized Topology Optimization for Structural Design.pdf` | Shapes optimization job contracts: objective/constraints metadata, reproducibility, and safe artifact delivery |
| `Understanding Statistics & Experimental Design.pdf` | Requires inference endpoints to include context/assumptions and avoid misleading comparisons; informs diagnostics-first outputs |
| `graphical-data-analysis-with-r.pdf` | Encourages EDA artifacts (distributions/outliers) and exploration-safe response designs |
| `regression-analysis-with-python.pdf` | Regression endpoints should emit diagnostics (residuals, checks) and avoid “trendline as truth” outputs |
| `Regression analysis using Python - slides-linear-regression.pdf` | Standardizes minimal regression output shapes (coeff tables, fit metrics) for UI + evidence bundles |
| `think-bayes-bayesian-statistics-in-python.pdf` | Bayesian endpoints treat uncertainty as first-class: priors disclosed, posteriors summarized, intervals returned |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | ML jobs should be artifact/version driven; discourages training inside API process; encourages model-card artifacts and reproducible configs |
| `A programming Books.pdf` | Contributor shelf: broad language/tool references for adapters, scripts, and future integrations |
| `B-C programming Books.pdf` | Contributor shelf: broad language/tool references for adapters, scripts, and future integrations |
| `D-E programming Books.pdf` | Contributor shelf: broad language/tool references for adapters, scripts, and future integrations |
| `F-H programming Books.pdf` | Contributor shelf: broad language/tool references for adapters, scripts, and future integrations |
| `I-L programming Books.pdf` | Contributor shelf: broad language/tool references for adapters, scripts, and future integrations |
| `M-N programming Books.pdf` | Contributor shelf: broad language/tool references for adapters, scripts, and future integrations |
| `O-R programming Books.pdf` | Contributor shelf: broad language/tool references for adapters, scripts, and future integrations |
| `S-T programming Books.pdf` | Contributor shelf: broad language/tool references for adapters, scripts, and future integrations |
| `U-X programming Books.pdf` | Contributor shelf: broad language/tool references for adapters, scripts, and future integrations |

</details>

---
🌾 **KFM API is the boundary of trust.** If it can’t be explained, versioned, licensed, governed, and reproduced — it doesn’t ship.