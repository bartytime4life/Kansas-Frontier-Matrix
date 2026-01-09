<!-- According to a document from 2026-01-08 -->

# 🛰️ Kansas Frontier Matrix (KFM) API Boundary — `api/src/`

<p align="left">
  <a href="#-kansas-frontier-matrix-kfm-api-boundary--apisrc"><img alt="KFM API" src="https://img.shields.io/badge/Kansas%20Frontier%20Matrix-API%20Boundary-2b6cb0" /></a>
  <a href="#-contracts--schemas"><img alt="OpenAPI" src="https://img.shields.io/badge/contract-OpenAPI-85EA2D?logo=openapiinitiative&logoColor=white" /></a>
  <a href="#-security--governance-contract"><img alt="Governance" src="https://img.shields.io/badge/governance-deny--by--default%20%7C%20redaction%20%7C%20classification-critical" /></a>
  <a href="#-data--catalog-contract-stacdcatprov"><img alt="Catalogs" src="https://img.shields.io/badge/catalog-STAC%20%7C%20DCAT%20%7C%20PROV-845ef7" /></a>
  <a href="#-geospatial-contract-crs-geometry-tiles"><img alt="Geo" src="https://img.shields.io/badge/geospatial-PostGIS%20%7C%20CRS%20%7C%20tiles-0ea5e9" /></a>
  <a href="#-graph-contract-neo4j--bounded-analytics"><img alt="Graph" src="https://img.shields.io/badge/graph-Neo4j%20%7C%20bounded%20analytics-111827" /></a>
  <a href="#-background-jobs--events"><img alt="Jobs" src="https://img.shields.io/badge/jobs-queue%20%7C%20idempotent%20runs-purple" /></a>
  <a href="#-observability--health"><img alt="Observability" src="https://img.shields.io/badge/observability-logs%20%7C%20metrics%20%7C%20traces-7c3aed" /></a>
  <a href="#-security-hardening-checklist"><img alt="Security" src="https://img.shields.io/badge/security-hardening%20%7C%20abuse%20resistance-ef4444" /></a>
</p>

> 🧭 **Purpose:** `api/src/` implements KFM’s **governed boundary of trust** — the only place where clients (UI + external integrations) obtain **catalog-backed views**, **graph-backed context**, **jobs/simulations**, and **evidence bundles**.
>
> 🧱 **Non-goal:** don’t put ETL scripts, one-off admin tooling, or “just run this once” operations here. Those belong in `api/scripts/` (or CI), and must still obey the catalog + provenance gates.

> [!IMPORTANT]
> 🛑 **API boundary rule:** clients **must never** query internal stores (Neo4j/Postgres/object store) directly.  
> This layer enforces **contracts + auth + policy + redaction + classification propagation** by design.

> [!IMPORTANT]
> ⛓️ **Pipeline order is absolute:** **ETL → STAC/DCAT/PROV Catalogs → Graph → API → UI → Story Nodes → Focus Mode**  
> If it isn’t **cataloged + provenance-linked**, it isn’t *publishable* in KFM.

---

## 📌 Quick links

- [🧾 Doc metadata](#-doc-metadata)
- [🧭 What lives here](#-what-lives-here)
- [🧱 Architectural guardrails](#-architectural-guardrails-dont-break-these)
- [📁 Directory layout](#-directory-layout-inside-apisrc)
- [📜 Contracts & schemas](#-contracts--schemas)
- [🔒 Security & governance contract](#-security--governance-contract)
- [🧬 Data & catalog contract (STAC/DCAT/PROV)](#-data--catalog-contract-stacdcatprov)
- [🗺️ Geospatial contract (CRS, geometry, tiles)](#-geospatial-contract-crs-geometry-tiles)
- [🕸️ Graph contract (Neo4j + bounded analytics)](#-graph-contract-neo4j--bounded-analytics)
- [🧪 Analysis/ML contract (regression, Bayes, ML)](#-analysis--ml-contract-regression-bayes-ml)
- [🧮 Simulation & optimization contract (V&V)](#-simulation--optimization-contract-vv)
- [🧵 Background jobs & events](#-background-jobs--events)
- [📈 Observability & health](#-observability--health)
- [🧪 Testing & CI gates](#-testing--ci-gates)
- [🛡️ Security hardening checklist](#-security-hardening-checklist)
- [➕ Adding an endpoint](#-adding-an-endpoint-checklist)
- [🔌 Interoperability & exports](#-interoperability--exports)
- [📚 Project reference library → implementation rules](#-project-reference-library--implementation-rules-uses-all-project-files)

---

## 🧾 Doc metadata

> KFM docs follow a “protocol” so they can be audited, diffed, and enforced in CI.

```yaml
kfm_doc:
  path: api/src/README.md
  status: active
  last_updated: 2026-01-09
  doc_protocol: KFM-MDP (v13-aligned)
  scope:
    - API boundary code (FastAPI wiring + routers)
    - policy enforcement (authz/redaction/classification)
    - catalog-backed views (STAC/DCAT/PROV pointers)
    - job orchestration (analysis/simulation/ML as runs)
  promise: "No mystery data: everything served is policy-checked + provenance-linked"
```

---

## 🧭 What lives here

This folder is the **API boundary implementation** (the “front door” to KFM):

- 📜 **Contract-first endpoints** (OpenAPI + JSON Schemas + examples)
- 🔐 **Authentication & authorization** (JWT, RBAC/ABAC, service-to-service)
- 🧼 **Redaction + classification enforcement** (deny-by-default, no privacy downgrade)
- 🧾 **Evidence & provenance linking** (STAC/DCAT/PROV IDs, run IDs, artifact pointers)
- 🧵 **Orchestration** for long-running jobs (simulations, batch analyses, model runs)
- 🗺️ **Geospatial views** (GeoJSON, tiles, quicklooks, pointers to COG/NetCDF)
- 🕸️ **Graph context** (Neo4j as reference index, not a data dump)
- 📈 **Telemetry** (structured logs, request IDs, health/ready/metrics, tracing hooks)
- 🧯 **Abuse resistance** (request size limits, pagination, rate limits, safe parsing)

> [!TIP]
> If you’re unsure whether something belongs in `api/src/`, ask:  
> **“Is this enforcing governance / translating internal stores into stable, contracted client responses?”**  
> If yes → it likely belongs here.

---

## 🧱 Architectural guardrails (don’t break these)

KFM invariants that keep the system governable:

- ⛓️ **Pipeline ordering is absolute:** ETL → catalogs → graph → API → UI → story/focus  
- 🛑 **API boundary rule:** clients never query graph/DB/object store directly
- 🧷 **Classification propagation:** outputs must be **≥ strictest input classification**
- 🧼 **Deny-by-default:** policy gates default to *deny* until explicitly allowed
- 🧬 **Provenance-first:** claim-like outputs must carry evidence pointers
- 🧪 **Validation gates:** contract + schema + policy checks fail CI when violated
- 🧯 **Safe-by-default errors:** no stack traces; return error IDs + request IDs
- 🔁 **Idempotency:** “do work” endpoints support idempotency keys
- 🧵 **Bounded work:** no unbounded fanout, parsing, or response sizes (ever)
- 🧠 **Thin routers:** route handlers do IO + auth + validation + call use-case
- 🧱 **Pure logic stays pure:** domain/use-cases do not import FastAPI/DB drivers

> [!NOTE]
> The fastest way to create tech debt: “just put the query in the router.” Don’t. 😅

---

## 🗺️ High-level system flow

```mermaid
flowchart LR
  subgraph Data["📦 Data & Metadata (catalog-first)"]
    A["Raw Sources"] --> B["ETL + Normalization"]
    B --> C["🏷️ STAC Items + Collections"]
    C --> D["🧾 DCAT Dataset Views"]
    C --> E["🧬 PROV Lineage Bundles (runs)"]
  end

  C --> G["🕸️ Graph (references to catalogs)"]
  D --> H["🚪 API Boundary (contracts + auth + policy + redaction)"]
  E --> H
  G --> H

  H --> UI["🌐 UI (MapLibre/Cesium + Story Nodes)"]
  H --> Ext["🔌 External Integrations"]

  H --> Jobs["🧵 Queue / Workers (analysis, simulation, ML)"]
  Jobs --> Artifacts["📦 Object Store (results, tiles, thumbnails)"]
  Jobs --> C

  UI --> Story["📚 Story Nodes"]
  Story --> Focus["🎯 Focus Mode (evidence bundle + citations)"]
```

---

## 📁 Directory layout (inside `api/src`)

> Aim: contracts separate from handlers, business logic separate from IO, policy gates centralized.

```text
📁 api/
└── 📁 src/
    ├── 📁 contracts/                 # 📜 OpenAPI + shared contract fragments
    │   ├── 📄 openapi.yaml           # ✅ API source of truth
    │   ├── 📁 schemas/               # ✅ JSON Schemas: envelopes, STAC/DCAT/PROV/Evidence
    │   └── 📁 examples/              # 🧪 “golden” request/response fixtures for CI
    ├── 📁 routers/                   # 🚦 HTTP route handlers (thin)
    │   └── 📁 v1/
    ├── 📁 middleware/                # 🧱 request-id, auth, policy hooks, rate limits, caching
    ├── 📁 auth/                      # 🔐 JWT verification, role checks, service tokens
    ├── 📁 policy/                    # 🧷 classification/redaction + policy-as-code bundles (optional)
    ├── 📁 services/                  # 🧠 use-cases; orchestration; governance applied here
    ├── 📁 repositories/              # 🗃️ Postgres/Neo4j/object store adapters (ports/adapters)
    ├── 📁 integrations/              # 🔌 external APIs (GEE, NOAA, etc.)
    ├── 📁 tasks/                     # 🧵 worker jobs + queue adapters
    ├── 📁 telemetry/                 # 📈 logging, metrics, tracing helpers
    ├── 📁 utils/                     # 🧰 small + boring helpers
    ├── 📁 tests/                     # 🧪 unit + contract + integration (API-focused)
    └── 📄 main.py                    # 🚀 FastAPI() app entrypoint (wiring only)
```

<details>
<summary><strong>🧠 Optional: explicit Clean Architecture package split</strong></summary>

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
- ✅ OpenAPI is **reviewed**, **versioned**, and **diff-checked** in CI
- 🧪 Every endpoint has:
  - request/response schema
  - at least one “golden” example
  - explicit error codes (401/403/404/422/429/5xx)
- 🔄 Breaking changes require:
  - `/v2` (preferred) or
  - parallel routes with a deprecation plan

### JSON Schema gates
Use JSON Schema to validate:
- request payloads (server-side)
- response envelopes (CI checks)
- evidence + provenance bundles
- job manifests + artifact metadata

### Contract-first workflow (golden path)
1) edit OpenAPI + schema  
2) update service/use-case  
3) update router  
4) update tests + examples  
5) ship ✅

> [!TIP]
> If the schema can’t express the rule, the contract isn’t done yet.

---

## 📦 Response envelopes (standardized)

> KFM clients should be able to rely on a stable envelope: provenance, classification, warnings.

### ✅ Default envelope
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

### 🧨 Error envelope (safe-by-default)
```json
{
  "meta": {
    "request_id": "req_...",
    "classification": "public",
    "error_id": "err_01HZZ...",
    "warnings": []
  },
  "error": {
    "code": "POLICY_DENIED|VALIDATION_FAILED|NOT_FOUND|RATE_LIMITED",
    "message": "A safe, non-leaky message.",
    "details": []
  }
}
```

---

## 🔒 Security & governance contract

KFM treats security + governance as **design constraints at the boundary**, not “policy later”.

### ✅ Minimum guarantees this layer must provide

- 🔐 **AuthN**: verify JWT signature, issuer, audience, expiry, key rotation (`kid`)
- 🧑‍⚖️ **AuthZ**: RBAC + ABAC enforced on *every* access path (**no implicit allow**)
- 🧼 **Redaction**: remove/mask/generalize restricted fields (**deny-by-default**)
- 🧷 **Classification propagation**: output classification is **≥ strictest input classification**  
  *(no privacy downgrade via aggregation or derived views)*
- 🧾 **Evidence pointers**: “claim-like” responses link to provenance (STAC/DCAT/PROV + run IDs)
- 🧯 **Abuse resistance**: request size limits, pagination, rate limiting, SSRF controls
- 🧾 **Auditable behavior**: request-id / trace-id / “who did what” logs (**never log secrets**)
- 🧬 **Reproducibility**: jobs store parameters + versions + seeds; results are not “magic”
- 🧑‍⚖️ **Contestability-ready**: when ML/AI is involved, emit model/version + evidence + uncertainty

### 🧨 Threat posture: assume hostile inputs
Treat everything as untrusted:
- GeoJSON/WKT payloads
- file uploads (archives, rasters, zips)
- external URLs (SSRF risk)
- 3D/model assets (parser risks)
- user query filters (injection / cost amplification)

> [!CAUTION]
> “It’s internal” is not a defense. Internal systems are breached too. Build as if everything will be fuzzed. 🧪🛡️

---

## 🧬 Data & catalog contract (STAC/DCAT/PROV)

KFM’s publishing posture: **data outputs become real only when cataloged**.

### ✅ Canonical rule
- The API does **not** serve “mystery outputs”.
- The API serves **views backed by**:
  - STAC Items/Collections (assets + geometry + time + checksums)
  - DCAT datasets/distributions (discovery metadata)
  - PROV runs (inputs → activities → outputs)

### 🧾 “Pointers over payload” (Data Spaces posture)
Prefer returning **references** (IDs + URIs + checksums) over copying large payloads into responses:
- 🔗 `href` to an artifact (COG/NetCDF/Parquet/PNG tile set)
- 🧾 `prov://run/...` for lineage
- 🏷️ `stac://...` for discoverability

> [!TIP]
> If a client needs the heavy artifact, let it fetch via signed URL / controlled download endpoints — with policy checks.

---

## 🗺️ Geospatial contract (CRS, geometry, tiles)

KFM geospatial endpoints must be explicit and safe.

### ✅ CRS conventions
- Default response CRS: **EPSG:4326**
- If accepting geometries:
  - require clients to declare CRS (or default + document)
  - validate SRID and geometry validity early
  - transform at boundaries (repository/integration layer), not in routers

### ✅ Geometry conventions
- Always validate and normalize:
  - `is_valid` checks
  - ring winding (if relevant)
  - maximum vertex counts / simplification options (bounded work)
- Never trust client-provided bounding boxes without validation.

### 🧊 Raster conventions
- Prefer COG (Cloud Optimized GeoTIFF) pointers for large rasters.
- Quicklooks:
  - small, cached, content-addressed, and policy-gated
  - return checksums + content-type in metadata

### 🧱 Tiles & offline-friendly design
- Provide tile endpoints for UI/mobile constraints:
  - XYZ tiles (vector/raster)
  - time-aware tiles (where applicable)
- Support caching headers and stable cache keys derived from:
  - dataset_id + time range + style_id + classification

---

## 🕸️ Graph contract (Neo4j + bounded analytics)

KFM uses the graph as a **reference index**, not a dumping ground.

### ✅ Core rules
- Graph nodes/edges must reference stable IDs:
  - dataset IDs
  - STAC/DCAT/PROV IDs
  - entity IDs (domain)
- No raw sensitive payloads in the graph if catalogs already hold them.
- Do not expose arbitrary Cypher to clients. Provide bounded query templates.

### 🧠 Bounded analytics (spectral/metrics)
Graph analytics endpoints must be:
- bounded (explicit limits + timeouts)
- explainable (document what metrics mean)
- reproducible (publish run manifest + parameters)
- cataloged (results become artifacts linked via STAC/PROV)

---

## 🧪 Analysis & ML contract (regression, Bayes, ML)

KFM analysis endpoints are “governed inference”, not “trendline as truth”.

### ✅ Regression endpoints
Must emit:
- coefficients + fit metrics
- diagnostics pointers (residual plots, leverage points, checks)
- assumptions + warnings (e.g., heteroscedasticity risk)
- provenance: dataset IDs + run IDs + code version

### ✅ Bayesian endpoints
Must emit:
- priors disclosed (as data, not prose only)
- posterior summaries + credible intervals
- (optional) posterior draws as artifact pointers
- provenance + random seeds for reproducibility

### ✅ ML endpoints (inference + jobs)
Rules:
- training is not done in the API request thread
- models have model cards (version, data, eval, limitations)
- outputs are labeled as model outputs and include uncertainty where meaningful
- every inference result has provenance pointers

> [!IMPORTANT]
> If the API can’t explain “where the number came from” and “how uncertain it is”, it doesn’t ship.

---

## 🧮 Simulation & optimization contract (V&V)

Simulation and optimization are first-class citizens in KFM — but only when they’re reproducible and validated.

### ✅ Required simulation/optimization metadata
Every run must capture:
- scenario definition (inputs, constraints, boundary conditions)
- solver/version/config
- random seeds (if any)
- convergence criteria and stop reasons
- sensitivity hooks (what changes were tested)
- V&V outcomes (verification/validation checks) as artifacts

### ✅ V&V gate
Simulation/optimization results are “publishable” only when:
- they pass schema + invariants
- V&V outputs exist (even if they record known limitations)
- provenance links are complete

---

## 🧵 Background jobs & events

### Job pattern (recommended)
- `POST /api/v1/.../run` → returns `job_id`
- `GET /api/v1/jobs/{job_id}` → status/progress
- `GET /api/v1/jobs/{job_id}/result` → stable pointers once cataloged

### Job safety expectations
- 🔁 idempotency keys for create/run endpoints
- 🧯 explicit deadlines/timeouts for workers
- 🧾 PROV run bundle created for every job
- 🧪 deterministic params stored (seeds, versions, exact inputs)
- 🧵 bounded concurrency + backpressure (no runaway fanout)

### Events (optional)
- SSE/WebSockets for:
  - progress updates
  - publish events (“new STAC item available”)
  - UI refresh triggers (layers/charts/story nodes)

---

## 📈 Observability & health

### Recommended endpoints
- `GET /health` ✅ liveness
- `GET /ready` ✅ readiness (DB/graph connectivity)
- `GET /metrics` 📊 Prometheus style (if enabled)

### Logging baseline (per request)
- method + route
- user_id/org_id (if authenticated)
- parameter metadata (never secrets)
- status code + duration
- request_id / trace_id
- classification outcome (safe label only)

> [!IMPORTANT]
> Return safe errors to clients. Log stack traces internally with an error ID + request ID.

---

## 🚀 Local development

### 1) Prereqs ✅
- 🐍 Python (project-supported)
- 🐳 Docker + Compose (recommended)
- 🧰 `bash`, `curl`, `jq` (recommended)

### 2) Environment variables (typical)

Create `api/.env` (local only):

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

# Ops
KFM_CORS_ORIGINS=http://localhost:5173
KFM_REQUEST_MAX_BYTES=10485760   # 10MB
KFM_RATE_LIMIT_ENABLED=true
```

> [!CAUTION]
> Never commit real secrets. `.env` is local and gitignored.

### 3) Run dependencies
```bash
docker compose up -d postgres neo4j redis
```

### 4) Run the API
```bash
cd api

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

uvicorn <your_package>.main:app --reload --host 0.0.0.0 --port 8000
```

### 5) Docs UI
- `/docs` (Swagger UI)
- `/redoc` (ReDoc)

---

## 🧪 Testing & CI gates

A pragmatic KFM API test stack:

- ✅ **Unit tests**: services + policy gates + redaction + auth helpers
- 🔁 **Contract tests**: OpenAPI + JSON Schema validation (golden examples)
- 🧩 **Integration tests**: API ↔ Postgres/Neo4j/queue (timeouts included)
- 🧨 **Security regression tests**: auth bypass, redaction regressions, SSRF prevention
- 🧬 **Provenance gates**: job results must emit PROV + STAC/DCAT pointers

Example:
```bash
pytest -q
pytest -q -m contract
pytest -q -m integration
pytest -q -m security
```

---

## 🛡️ Security hardening checklist

> Defensive posture only. No “clever shortcuts.” ✅

- 🔐 **AuthZ everywhere**: every repo call has a policy context
- 🧼 **Redaction is centralized**: don’t hand-roll redaction inside routers
- 🧷 **No privacy downgrade**: aggregation must not leak restricted data
- 🚫 **SSRF controls**: block private IP ranges; allowlist hosts if URL fetch exists
- 📦 **Archive safety**: zip-slip prevention; size limits; recursion limits
- 🧱 **Request limits**: max bytes, max features, max geometry vertices
- 🧨 **Injection controls**:
  - parameterized SQL
  - avoid dynamic Cypher
  - validate filters (don’t pass raw client strings to query builders)
- 🧪 **Fuzz mindset**: assume parsers will be attacked (GeoJSON, image decoders, 3D loaders)
- 🧾 **No secrets in logs**: scrub tokens, headers, env vars
- 🧵 **Backpressure**: bounded worker pools and queue limits

---

## ➕ Adding an endpoint (checklist)

Do this **in order**:

1) 📜 **Update the contract**
   - OpenAPI path + request/response schemas
   - version bump decision if breaking

2) 🧠 **Implement the use-case**
   - service function (pure logic)
   - apply governance gates in the service layer

3) 🚦 **Add the router**
   - validate input
   - enforce auth + scopes
   - apply redaction + classification
   - return envelope + provenance pointers

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
   - classification correct?

---

## 🔌 Interoperability & exports

Prefer standards-friendly outputs:
- 🗺️ GeoJSON (vector)
- 🧊 GeoTIFF / COG (raster) *(via object-store pointers)*
- 🌦️ NetCDF (gridded time series; when used)
- 📄 CSV (tabular)
- 🧬 PROV bundles (lineage)
- 🏷️ STAC/DCAT for discovery

Where helpful:
- content negotiation (`Accept` headers)
- export endpoints (sync for small, async for large)
- stable IDs for datasets/collections/items/runs

---

## 📚 Project reference library → implementation rules (uses all project files)

> Requirement: map **every project file** to a concrete `api/src` convention, guardrail, or implementation rule.  
> This section is intentionally “practical”: what to do, and where to enforce it.

<details>
<summary><strong>🧠 Expand: Influence map (all project files)</strong></summary>

### 🧱 Core KFM system docs (architecture + workflow)
| Project file | Practical impact on `api/src` |
|---|---|
| Kansas Frontier Matrix — Comprehensive Technical Documentation.docx  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS) | Defines KFM boundary invariants, Story Nodes + Focus Mode evidence flows, and the “catalog gate” as a publishing requirement. |
| Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design (English).docx  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS) | Hardens the pipeline order rule and “no bypass governance” architecture; clarifies what the API must/ must-not serve. |
| Latest Ideas-1.docx  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) | Pushes “policy-as-code + auditability” posture; encourages CI gates and provenance artifacts as first-class outputs. |
| KFM Agent Architecture and Implementation Strategy.docx  [oai_citation:5‡Latest Ideas-1.docx](file-service://file-TARkXvBU3mhC6bnphF2faY) | Encourages safe automation patterns (watch/plan/execute), kill-switches, and “no direct-to-main” discipline; informs how API jobs and CI automation should behave. |
| MARKDOWN_GUIDE_v13.md.gdoc  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) | Standardizes v13 doc conventions for KFM readmes: structured metadata, deterministic examples, and enforceable guardrails. |
| Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx  [oai_citation:8‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz) | Keeps API docs usable: consistent headings, admonitions, diagrams, and “don’t hide critical governance info” style rules. |

### 🧬 Data spaces + governance + human-centered constraints
| Project file | Practical impact on `api/src` |
|---|---|
| Data Spaces.pdf  [oai_citation:9‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq) | Reinforces **pointers-over-payload**: serve references + metadata + access control, not giant blobs. |
| Introduction to Digital Humanism.pdf  [oai_citation:10‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ) | Requires transparency, oversight, and accountability; informs privacy-first defaults and explainable, contestable outputs. |
| On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf  [oai_citation:11‡On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf](file-service://file-NtashtRjti9J1THyYXkhAv)  [oai_citation:12‡On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf](file-service://file-NtashtRjti9J1THyYXkhAv) | Forces audit-ready ML outputs: evidence, restraint, and explainability pressure in endpoint design. |
| Principles of Biological Autonomy - book_9780262381833.pdf  [oai_citation:13‡Principles of Biological Autonomy - book_9780262381833.pdf](file-service://file-PwPXcX5554FpuRsF3iXTCf) | Systems thinking: explicit state transitions (jobs), feedback loops, bounded automation, and human-in-the-loop escape hatches. |

### 🛰️ Remote sensing + geospatial + mapping quality
| Project file | Practical impact on `api/src` |
|---|---|
| Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf  [oai_citation:14‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)  [oai_citation:15‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV) | Shapes GEE job endpoints: reproducible parameters, catalog emission, and careful handling of time series derivatives. |
| python-geospatial-analysis-cookbook.pdf  [oai_citation:16‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu) | Codifies CRS sanity and PostGIS conventions (transform at boundaries, explicit SRIDs, validate geometries). |
| making-maps-a-visual-guide-to-map-design-for-gis.pdf  [oai_citation:17‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP) | Forces cartographic integrity: styles/ramps/legends treated as documented choices; avoid misleading defaults. |
| Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf  [oai_citation:18‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj) | Drives offline/low-bandwidth support: tiles, caching, small payloads, and location sensitivity awareness. |
| compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf  [oai_citation:19‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)  [oai_citation:20‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi) | Informs quicklook/thumbnail endpoints: intentional formats, content-type correctness, and performance budgets. |

### 🗄️ Data engineering + scalability + concurrency
| Project file | Practical impact on `api/src` |
|---|---|
| PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf  [oai_citation:21‡PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf](file-service://file-742sw3gADJniEdmC19JeAC) | Pushes stable paging, query-cost awareness, correct indexes, safe export patterns, and migration discipline. |
| Scalable Data Management for Future Hardware.pdf  [oai_citation:22‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE) | Encourages streaming, bounded memory, incremental processing, and “don’t build huge JSON blobs.” |
| concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf  [oai_citation:23‡concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf](file-service://file-Y45SvXbmLoZL1MNmrcyqz6) | Reinforces bounded queues/backpressure, safe retries, and deterministic job state machines. |

### 🕸️ Graph theory + bounded analytics
| Project file | Practical impact on `api/src` |
|---|---|
| Spectral Geometry of Graphs.pdf  [oai_citation:24‡Spectral Geometry of Graphs.pdf](file-service://file-DWxRbQDZGktGtiWtzAQxs8) | Justifies explainable graph endpoints and bounded spectral/metric services with provenance artifacts. |

### 🧮 Modeling, simulation, and optimization (NASA-grade rigor)
| Project file | Practical impact on `api/src` |
|---|---|
| Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf  [oai_citation:25‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd) | Requires reproducibility, run manifests, V&V checks, scenario metadata, and sensitivity hooks for simulation endpoints. |
| Generalized Topology Optimization for Structural Design.pdf  [oai_citation:26‡Generalized Topology Optimization for Structural Design.pdf](file-service://file-PzydVyvSPdXWqYrXeFCNzj) | Shapes optimization job contracts: objective/constraints metadata, solver configs, convergence artifacts, and safe export. |

### 📊 Statistics, experimental design, and analysis integrity
| Project file | Practical impact on `api/src` |
|---|---|
| Understanding Statistics & Experimental Design.pdf  [oai_citation:27‡Understanding Statistics & Experimental Design.pdf](file-service://file-SdX6LMgi1uDRk5kd4H4Bg3) | Forces endpoints to state assumptions, avoid misleading inference, and output uncertainty where needed. |
| graphical-data-analysis-with-r.pdf  [oai_citation:28‡graphical-data-analysis-with-r.pdf](file-service://file-K7oxq5mFmdE9HrPPev6c7L) | Encourages EDA artifacts (outliers, distributions) and deterministic diagnostic outputs. |
| regression-analysis-with-python.pdf  [oai_citation:29‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM) | Requires regression diagnostics, explicit assumptions, and residual checks to avoid false confidence. |
| Regression analysis using Python - slides-linear-regression.pdf  [oai_citation:30‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR) | Standardizes minimal regression output shapes for UI consumption: coeff tables + fit metrics + diagnostics pointers. |
| think-bayes-bayesian-statistics-in-python.pdf  [oai_citation:31‡think-bayes-bayesian-statistics-in-python.pdf](file-service://file-LXwJApPMVhRZgyqLb9eg7c) | Makes uncertainty first-class: priors disclosed, posterior summaries + credible intervals, provenance recorded. |

### 🤖 ML engineering posture (training vs serving)
| Project file | Practical impact on `api/src` |
|---|---|
| Understanding Machine Learning_ From Theory to Algorithms (2014).pdf  [oai_citation:32‡U-X programming Books.pdf](file-service://file-Qo3sZaQ5dgapsf2Gv3n6tr) | Reinforces generalization awareness and careful separation of training/evaluation; discourages “fit and ship” endpoints. |
| Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf  [oai_citation:33‡Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf](file-service://file-GqygtUWf5Xyi3AjEaqEdQB) | Encourages artifact-driven ML: versioned exports, model cards, and training outside the request thread. |

### 🛡️ Security posture and hostile-input discipline
| Project file | Practical impact on `api/src` |
|---|---|
| ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf  [oai_citation:34‡ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf](file-service://file-Q7EeqPb17SD9sV8Fb12LQX) | Reinforces threat modeling, segmentation assumptions, and hardened network operations. |
| Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf  [oai_citation:35‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg) | Defensive coding: hostile input handling, safe parsing, and reduced attack surface (especially for file/geo parsers). |
| scipy-lecture-notes.pdf  [oai_citation:36‡S-T programming Books.pdf](file-service://file-FJGViMuoXECeHPiFup8mUK) | Supports numerics + reproducibility practices: deterministic computation, clear numerical stability choices in analysis endpoints. |

### 🌐 UI/3D delivery constraints that affect API responses
| Project file | Practical impact on `api/src` |
|---|---|
| responsive-web-design-with-html5-and-css3.pdf  [oai_citation:37‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK) | Pushes performance budgets and responsive delivery: smaller payloads, cacheable tiles/quicklooks, content negotiation. |
| webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf  [oai_citation:38‡webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf](file-service://file-7quELMw4FrspPczB9Y3BTp) | Shapes 3D asset delivery posture: coordinate sanity, safe loaders, and “3D is optional / degrade gracefully.” |

### 📚 Contributor shelf (broad programming references)
| Project file | Practical impact on `api/src` |
|---|---|
| A programming Books.pdf | Contributor shelf: general references; may be used for style and language-specific adapters (availability may vary). |
| B-C programming Books.pdf  [oai_citation:39‡B-C programming Books.pdf](file-service://file-7HTVQSpDmJyTNX3ZroTMxy) | Contributor shelf: general references; helps future adapters/integrations. |
| D-E programming Books.pdf  [oai_citation:40‡D-E programming Books.pdf](file-service://file-2BV3fPbrEfRn2KmoE6nnbP) | Contributor shelf. |
| F-H programming Books.pdf  [oai_citation:41‡F-H programming Books.pdf](file-service://file-6M57f592rSBag5JxTUMXGm) | Contributor shelf. |
| I-L programming Books.pdf  [oai_citation:42‡I-L programming Books.pdf](file-service://file-EXJqY2YqS6DgUWn8zoKCp5) | Contributor shelf. |
| M-N programming Books.pdf | Contributor shelf (availability may vary). |
| O-R programming Books.pdf | Contributor shelf (availability may vary). |
| S-T programming Books.pdf  [oai_citation:43‡S-T programming Books.pdf](file-service://file-FJGViMuoXECeHPiFup8mUK) | Contributor shelf + secure coding reminders. |
| U-X programming Books.pdf | Contributor shelf (availability may vary). |
| Objective-C Notes for Professionals.pdf  [oai_citation:44‡O-R programming Books.pdf](file-service://file-W5nMyLKLAEpf4b6wUEpzyq) | UI/client-adjacent reference when native tooling appears; not core to API, but supports edge integrations. |

</details>

---

<!--
Maintainers’ TODOs ✅ (keep or remove):
- Add/lock response envelopes + error schema in contracts/schemas.
- Add policy regression test suite (redaction/classification/no-downgrade).
- Add PROV run bundle schema + enforce for every async job result.
- Add explicit geo contract doc (CRS, geometry validation, paging, tile caching).
- Add “no arbitrary Cypher” enforcement and bounded analytics templates.
- Add model-card artifacts for any ML endpoints.
-->