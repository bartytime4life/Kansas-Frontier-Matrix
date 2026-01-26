<!--
📍 File: src/server/README.md
🧠 Purpose: Server-side API boundary for Kansas Frontier Matrix (KFM)
-->

# 🧭 KFM Server (`src/server/`) — Governed API Boundary 🔒🧾

![Python](https://img.shields.io/badge/Python-3.11%2B-informational?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-informational?logo=fastapi)
![GraphQL](https://img.shields.io/badge/GraphQL-Semantic%20Queries-informational?logo=graphql)
![OpenAPI](https://img.shields.io/badge/OpenAPI-Contract%20First-informational?logo=swagger)
![Postgres](https://img.shields.io/badge/PostgreSQL%20%2B%20PostGIS-Geo%20Truth-informational?logo=postgresql)
![Neo4j](https://img.shields.io/badge/Neo4j-Context%20Graph-informational?logo=neo4j)
![Elasticsearch](https://img.shields.io/badge/Search-Text%20%2B%20Index-informational?logo=elasticsearch)
![OPA](https://img.shields.io/badge/OPA-Policy%20as%20Code-informational?logo=openpolicyagent)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-informational?logo=ollama)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-Tracing%20%26%20Metrics-informational?logo=opentelemetry)
![OCI](https://img.shields.io/badge/OCI%20Artifacts-ORAS%20%2B%20Cosign-informational?logo=docker)

> ✅ **Evidence-first** • 🧾 **Provenance-first** • 🔒 **Policy-as-code** • 🧩 **Contract-first** • ♻️ **Reproducible-by-design**

> [!IMPORTANT]
> `src/server/` is the **single home** for all server-side API code (REST + GraphQL + tiles + Focus Mode).  
> The UI (web/AR/mobile), scripts, notebooks, and integrations **must** go through this boundary — **no direct UI → DB access**. 👮‍♂️

---

## ⚡ Quickstart (dev)

```bash
# 1) create env
python -m venv .venv && source .venv/bin/activate

# 2) install deps
pip install -r requirements.txt

# 3) run the API
uvicorn src.server.main:app --reload --port 8000
```

- REST docs: `/docs` + `/redoc` 📚  
- GraphQL endpoint: `/graphql` 🧬 *(Playground enabled in dev only)*

> [!TIP]
> Local dev is easiest when dependencies run in containers (PostGIS, Neo4j, OPA, Search, Ollama). 🐳

---

## 🗺️ Table of Contents

- [📦 What lives here](#-what-lives-here)
- [🚫 Non-goals](#-non-goals)
- [🧱 KFM server invariants](#-kfm-server-invariants)
- [🏗️ Architecture at a glance](#️-architecture-at-a-glance)
- [🗄️ Data stores & standards](#️-data-stores--standards)
- [🌐 API surface](#-api-surface)
- [🧾 Response envelopes](#-response-envelopes)
- [🧬 Provenance & evidence rules](#-provenance--evidence-rules)
- [🛡️ Policy & governance](#️-policy--governance)
- [🤖 Focus Mode boundary](#-focus-mode-boundary)
- [🔐 Security model](#-security-model)
- [📈 Observability & operations](#-observability--operations)
- [🧑‍💻 Local development](#-local-development)
- [🧪 Testing & CI](#-testing--ci)
- [🧩 Adding a new endpoint or resolver](#-adding-a-new-endpoint-or-resolver)
- [🧯 Troubleshooting](#-troubleshooting)
- [🧭 Roadmap hooks](#-roadmap-hooks)
- [📚 Project docs & reference library](#-project-docs--reference-library)
- [✅ TL;DR](#-tldr)

---

## 📦 What lives here

`src/server/` contains everything needed to expose KFM’s platform capabilities through a **governed API layer**:

- 🌐 **REST API (FastAPI)** for tiles, downloads, searches, actions, and cache-friendly endpoints
- 🧬 **GraphQL API** for relationship-heavy semantic traversals
- 🗺️ **Spatial endpoints** backed by PostGIS (bbox/time filters, features, tiles)
- 🕸️ **Knowledge graph adapters** backed by Neo4j (entities, relationships, provenance links)
- 🔎 **Search adapters** backed by a text index (e.g., Elasticsearch) and/or semantic embeddings
- 🤖 **Focus Mode** request handling (RAG + citations + policy validation)
- 🧾 **Narrative endpoints** (Story Nodes, Pulse Threads) with evidence manifests
- 🔐 **Policy enforcement** (OPA decisions at runtime + Conftest in CI)
- 📦 **Artifact/offline pack delivery** (OCI/ORAS + Cosign verification patterns)
- 📈 **Operational endpoints** (health/readiness/metrics/audit hooks)

---

## 🚫 Non-goals

This folder is **not** the home for heavy ingestion/ETL:

- ❌ Long-running pipelines, bulk transforms, large backfills  
- ❌ “Do everything in the API” map rendering pipelines  
- ❌ Ad-hoc scripts that bypass governance

> ✅ Pipelines produce **versioned artifacts + catalogs + provenance**.  
> ✅ The server **serves, validates, governs, and audits**.

---

## 🧱 KFM server invariants

These are the “KFM-clean” rules — **non-negotiable** ✅

### 1) Single governed gateway 🚪
- UI never queries PostGIS/Neo4j/Search directly.
- No “quick DB shortcut” even in dev.

### 2) Evidence is first-class 🧾
Every response must be **traceable**:
- Dataset IDs
- Catalog links (STAC/DCAT)
- Provenance links (PROV)
- Licensing + attribution signals

### 3) Policy is enforced in code 🔐
- CI gates reject invalid catalogs/schemas/policies.
- Runtime gates enforce access, redaction, and AI constraints.
- Audit logs record **policy bundle/version hash** for decisions.

### 4) Contracts are stable 🧩
- OpenAPI + GraphQL schema changes follow versioning rules.
- Prefer additive evolution; breaking changes create new versions.

### 5) Reproducibility beats convenience ♻️
- Prefer serving **prebuilt artifacts** (PMTiles/GeoParquet/COGs) over expensive on-demand generation.
- Artifacts are content-addressed and verifiable.

---

## 🏗️ Architecture at a glance

### 🌍 Outside the server (platform flow)

```mermaid
flowchart LR
  A[📥 Pipelines / Intake] --> B[📚 Catalogs<br/>STAC + DCAT + PROV]
  B --> C[🗺️ PostGIS<br/>Geo truth]
  B --> D[🕸️ Neo4j<br/>Context graph]
  B --> S[🔎 Search Index<br/>Docs & text]
  B --> O[📦 OCI Artifacts<br/>PMTiles / GeoParquet / Models]
  C --> E[🧭 Server API<br/>src/server]
  D --> E
  S --> E
  O --> E
  E --> F[🖥️ Web UI<br/>MapLibre/Cesium]
  E --> G[🤖 Focus Mode]
  E --> H[📱 AR / Mobile]
```

### 🧼 Inside the server (clean / hexagonal)

```mermaid
flowchart TB
  R[🌐 Routers & Resolvers] --> U[🧠 Use-cases / Services]
  U --> P[🔌 Ports (Interfaces)]
  P --> A1[🗄️ Adapter: PostGIS]
  P --> A2[🕸️ Adapter: Neo4j]
  P --> A3[🔎 Adapter: Search]
  P --> A4[🔐 Adapter: OPA]
  P --> A5[📦 Adapter: OCI/Artifacts]
  P --> A6[🤖 Adapter: Ollama/LLM]
```

**Rule of thumb:** routers/resolvers are thin. Business logic lives in services/use-cases and talks only to ports. Adapters own IO (DBs, graphs, LLMs, registries).

---

## 🗄️ Data stores & standards

### 🧠 “Truth stack” (what each store is for)
- 🗺️ **PostGIS** = spatial truth + fast geo queries + tile-building queries
- 🕸️ **Neo4j** = semantic truth + relationships + provenance linking
- 🔎 **Search index** = documents/narratives/full-text + fuzzy search (and optionally semantic search)
- 📦 **OCI artifact registry** = versioned, content-addressed packages (datasets, PMTiles, models)
- 🔐 **OPA** = policy decisions (authz, redaction, AI constraints)
- 🤖 **Ollama** = local LLM inference + embeddings (optional) for Focus Mode RAG

### 🧭 Standards KFM leans on
- **STAC** for spatial/temporal assets & indexing
- **DCAT** for discovery/licensing/publisher/distributions
- **PROV** for lineage & run history
- **Open formats** for serving: GeoJSON, MVT/PMTiles, GeoParquet, COG/GeoTIFF

> [!NOTE]
> KFM’s design explicitly avoids “black box layers”: even tiles should be traceable via attribution headers or a companion metadata endpoint.

---

## 🌐 API surface

> [!NOTE]
> This section shows **canonical shapes** and **recommended patterns**. Your exact routes may differ — keep the intent and invariants.

### REST (high-signal families)

| Domain | Example endpoints | Notes |
|---|---|---|
| ❤️ Health | `GET /api/health` • `GET /api/ready` | readiness checks dependencies |
| 📚 Catalog | `GET /api/v1/datasets` • `GET /api/v1/datasets/{id}` | browse + metadata |
| 🧬 Provenance | `GET /api/v1/datasets/{id}/prov` | PROV record / lineage |
| 🗺️ Tiles | `GET /api/v1/tiles/{layer}/{z}/{x}/{y}.pbf` | cacheable, CDN-friendly |
| 🧾 Tile metadata | `GET /api/v1/tiles/{layer}/meta` | attribution + dataset refs |
| 🔎 Search | `GET /api/v1/search?q=...` | full-text + filters |
| 📦 Downloads | `GET /api/v1/datasets/{id}/download` | file or signed URL |
| 📦 Artifacts | `GET /api/v1/artifacts/{digest}` | digest-pinned retrieval |
| 🧵 Narrative | `GET /api/v1/story` • `POST /api/v1/story` | evidence manifest required |
| ⚡ Pulse | `GET /api/v1/pulse` | “live feed” threads w/ citations |
| 🤖 Focus | `POST /api/v1/focus` | evidence-first Q&A |
| 🔐 Admin | `POST /api/v1/ingest` | restricted, audited, policy-gated |
| 📈 Metrics | `GET /api/metrics` | Prometheus / OTEL |

### GraphQL (semantic traversals)

GraphQL shines when traversing relationships in one request:

- `Person → events → locations → datasets → provenance`
- `Place → stories → citations → documents`
- `Dataset → lineage → derived products → artifacts`

**Mandatory guardrails:**
- query depth/recursion limits
- list pagination by default
- cost/complexity enforcement
- field-level redaction by policy

---

## 🧾 Response envelopes

KFM responses should be **data + evidence + policy context**.

### ✅ Standard JSON envelope (recommended)

```json
{
  "data": { },
  "provenance": {
    "dataset_ids": ["kfm.ks.counties.boundaries.v1"],
    "stac_refs": ["stac://..."],
    "dcat_refs": ["dcat://..."],
    "prov_refs": ["prov://..."],
    "citations": [
      { "label": "Kansas Historical Society, 1903 Flood Record", "url": "..." }
    ],
    "artifacts": [
      { "type": "pmtiles", "digest": "sha256:...", "verified": true }
    ]
  },
  "policy": {
    "decision": "allow",
    "policy_bundle_digest": "sha256:...",
    "redactions": ["geom_precision_reduced"]
  },
  "meta": {
    "request_id": "req_...",
    "generated_at": "2026-01-26T00:00:00Z"
  }
}
```

### 🗺️ Tiles are binary — where does provenance go?
For tiles (MVT/PNG), use one of these patterns:

- 📌 **Companion endpoint:** `/tiles/{layer}/meta` (preferred)
- 🧾 **HTTP headers:** `X-KFM-Dataset-Ids`, `X-KFM-Attribution`, `X-KFM-Policy`
- 🧩 **Signed URL manifest:** tile URL returns a JSON manifest containing tile template + evidence

---

## 🧬 Provenance & evidence rules

### Evidence triplet 🧾🧭🧬
Every published dataset should have:
- **DCAT** discovery/licensing/publisher/distributions
- **STAC** assets + spatial/temporal indexing
- **PROV** lineage/run history

### Stable IDs 🪪
Prefer structured IDs and explicit versioning:

- `kfm.ks.landcover.2000_2020.v1`
- `kfm.ks.counties.boundaries.v1`

### Narrative artifacts ship an evidence manifest 📜
For **Story Nodes** and **Pulse Threads**, require:
- human-facing citations (footnotes/links)
- machine-readable evidence manifest (JSON/YAML)
- optional run manifest links (pipeline ID, code version, hashes)

> [!IMPORTANT]
> **No mystery nodes**: every graph entity should trace back to a catalog/provenance reference.

---

## 🛡️ Policy & governance

### Policy-as-code everywhere ⚖️
KFM’s governance model assumes policies are:
- **versioned in Git**
- validated in **CI** (Conftest/OPA checks)
- enforced at **runtime** (OPA decisions)

Policies commonly enforce:
- license presence + compatibility
- sensitivity classification & role gating
- geo-obfuscation requirements (protected sites)
- “append-only / no silent rewrites”
- AI answer rules (citations required, hallucination checks)

### Runtime OPA integration points 🔐
- request authorization (roles/scopes/classification)
- field-level redaction (precision reduction, omit sensitive attributes)
- Focus Mode output validation (citations + safe language requirements)
- story/pulse submission requirements (evidence manifest required)

> [!NOTE]
> Audit logs should record the **policy bundle digest/hash** used for each decision, enabling “why was this denied?” explanations later.

---

## 🤖 Focus Mode boundary

Focus Mode is **advisory**, **evidence-backed**, and **policy-validated** — never autonomous.

### Focus Mode pipeline (RAG + governance) 🔍🧾🔒

```mermaid
flowchart LR
  U[👤 User question] --> PG[🛡 Prompt Gate<br/>sanitize & block injection]
  PG --> R[🔎 Retrieval<br/>graph + gis + search + embeddings]
  R --> CP[📦 Context Pack<br/>snippets + citations + IDs]
  CP --> LLM[🤖 LLM (Ollama)<br/>answer draft]
  LLM --> VAL[⚖️ OPA Validation<br/>citations, redactions, rules]
  VAL --> OUT[✅ Answer + Evidence Manifest]
  OUT --> UI[🖥️ UI renders<br/>citations + trace links]
```

### Guardrails (must-have) 🧱
- 🧼 **Input filtering:** prompt injection stripping + disallowed query blocking
- 🧰 **Tool sandboxing:** default is *no tools*; allowlist only
- 🧾 **Citation requirement:** answers must include sources (datasets/docs/graph nodes)
- 🕵️ **Hallucination checks:** e.g., “names referenced by AI must exist in the graph”
- 🧯 **Sensitive handling:** policy-based redaction/generalization + refusal when required
- 📉 **Monitoring:** citation coverage, latency, drift, user feedback, bias checks

### Ollama integration notes 🦙
- Support multiple models + version switching for A/B tests and rollback
- Optional embeddings + vector store (e.g., Chroma/Qdrant) for semantic retrieval
- Treat models as versioned artifacts like data (digest-pinned where possible)

---

## 🔐 Security model

### AuthN/AuthZ 🔑
- JWT/OAuth2 supported patterns
- role & scope-based authorization
- CORS configured for dev + prod
- rate limiting + throttles for public endpoints

### Sensitive location handling 🗺️🫥
For culturally sensitive/protected sites:
- return generalized geometry
- obfuscate coordinates / reduce precision
- require elevated roles for exact access
- audit access events (policy-gated)

### Supply-chain & artifact integrity 📦✅
When serving offline packs or derived artifacts:
- content-address artifacts (digests)
- verify signatures (Cosign)
- prefer OCI/ORAS distribution for reproducible pull + rollback
- log artifact digests returned to users (audit trail)

---

## 📈 Observability & operations

Minimum operational endpoints:
- `GET /api/health` → liveness
- `GET /api/ready` → dependency checks (PostGIS/Neo4j/OPA/Search/Ollama)
- `GET /api/metrics` → Prometheus/OTEL compatible (feature-flagged)

Operational signals we care about:
- dependency latency (PostGIS/Neo4j/Search/OPA/Ollama)
- GraphQL cost rejections (abuse prevention)
- tile cache hit rate (CDN vs origin)
- missing provenance links (orphan graph nodes)
- policy bundle drift vs expected version
- Focus Mode citation coverage + refusal rate

> [!TIP]
> Always propagate a **request ID** across logs + traces + downstream calls (DB/OPA/LLM) for clean audits.

---

## 🧑‍💻 Local development

### Prereqs ✅
- 🐍 Python 3.11+
- 🐳 Docker (recommended)
- 🗄️ Postgres + PostGIS
- 🕸️ Neo4j
- 🔎 Search index (optional in dev)
- 🔐 OPA
- 🤖 Ollama (if Focus Mode enabled)

### Suggested env vars 🔧

<details>
<summary><strong>Click to expand</strong> ✅</summary>

| Variable | Example | Notes |
|---|---|---|
| `KFM_ENV` | `dev` | environment mode |
| `KFM_API_HOST` | `0.0.0.0` | bind host |
| `KFM_API_PORT` | `8000` | bind port |
| `KFM_POSTGIS_DSN` | `postgresql://user:pass@localhost:5432/kfm` | PostGIS |
| `KFM_NEO4J_URI` | `bolt://localhost:7687` | Neo4j |
| `KFM_NEO4J_USER` | `neo4j` | Neo4j user |
| `KFM_NEO4J_PASSWORD` | `password` | Neo4j pass |
| `KFM_SEARCH_URL` | `http://localhost:9200` | Elasticsearch (optional) |
| `KFM_OPA_URL` | `http://localhost:8181` | policy engine |
| `KFM_OLLAMA_URL` | `http://localhost:11434` | LLM service |
| `KFM_JWT_ISSUER` | `https://issuer.example` | if auth enabled |
| `KFM_JWT_AUDIENCE` | `kfm-api` | if auth enabled |
| `KFM_CORS_ORIGINS` | `http://localhost:3000` | UI dev origin |
| `KFM_RATE_LIMIT_RPS` | `10` | public throttle |
| `KFM_ARTIFACT_REGISTRY` | `ghcr.io/<org>/kfm` | OCI artifacts (optional) |
| `KFM_ENABLE_GRAPHQL` | `true` | feature flag |
| `KFM_ENABLE_FOCUS_MODE` | `true` | feature flag |
| `KFM_ENABLE_METRICS` | `true` | feature flag |

</details>

---

## 🧪 Testing & CI

Recommended layers ✅
- ✅ Unit tests: domain + services (no network)
- ✅ Integration tests: adapters (dockerized PostGIS/Neo4j/OPA stubs)
- ✅ Contract tests: OpenAPI + GraphQL schema shape checks
- ✅ Policy tests: Conftest/OPA evaluation in CI
- ✅ Security checks: dependency scanning + linting

Example commands (adjust to repo tooling):

```bash
pytest
ruff check .
mypy .
```

---

## 🧩 Adding a new endpoint or resolver

Use this checklist to keep the server “KFM-clean” 🧼

### ✅ Checklist
- [ ] Define contract (Pydantic/OpenAPI and/or GraphQL SDL)
- [ ] Implement use-case in `application/` (no DB calls here)
- [ ] Access IO only through `ports/` (PostGIS/Neo4j/Search/OPA/Artifacts/LLM)
- [ ] Add policy checks (authz + classification + evidence requirements)
- [ ] Include provenance hooks (IDs, citations, manifests)
- [ ] Add tests (unit + integration as needed)
- [ ] Update docs (this README + domain README if present)

### 🤖 Focus Mode special rules
Focus endpoints must:
- include citations/source links
- avoid restricted data leakage (policy-enforced)
- produce structured provenance for audits
- support streaming responses (optional, but plan for it)

---

## 🧯 Troubleshooting

### “Ready” fails ❌
- 🗄️ PostGIS unreachable → check DSN, container network, migrations
- 🕸️ Neo4j unreachable → check bolt URI, auth, startup health
- 🔐 OPA unreachable → verify URL + policy bundle loaded
- 🤖 Ollama unreachable → verify service port (11434) + model pulled

### “Why was this denied?” 🕵️
- check response `policy.policy_bundle_digest`
- consult audit logs for request ID
- compare policy bundle version in runtime vs CI

### Tiles are slow 🐢
- prefer prebuilt PMTiles for heavy layers
- add CDN caching headers + ETags
- verify PostGIS indexes and tile SQL query plans

---

## 🧭 Roadmap hooks

These are already on the blueprint and should shape server decisions 🧠

- ⚡ **Pulse Threads**: geotagged narrative feed with citations
- 🧠 **Conceptual Attention Nodes**: focus control for AI/UI
- 📦 **Offline packs**: PMTiles + bundles for low-connectivity field use
- 🌎 **Federation**: multi-region deployments + shared contracts (GraphQL federation)
- 🛰️ **4D Digital Twin + AR**: same APIs, new clients (don’t fork endpoints)
- 🕵️ **Geo-obfuscation**: culturally sensitive/protected site handling
- ✅ **Artifact integrity**: OCI/ORAS + Cosign verification and audit trails

---

## 📚 Project docs & reference library

### 📘 Authoritative KFM docs (start here)
- 📌 **Platform Overview & Roadmap** (vision, layers, artifacts, federation)  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf](file-service://file-J9i6fUc35zPWB2U62zUnEN)  
- 🧱 **Comprehensive Architecture, Features, and Design** (stack, scale, backend patterns)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-Qj23Z329hf1Q1WD86hXYfL)  
- 🧭 **AI System Overview** (Focus Mode guardrails, OPA governance, auditing)  [oai_citation:2‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-P4zHoJicw1HG6bXmqFygG8)  
- 🧪 **Expanded Technical & Design Guide** (GraphQL vs REST, API principles & examples)  [oai_citation:3‡📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf](file-service://file-Tjmzn5F3sT5VNvVFhqj1Vo)  
- 🛠️ **Comprehensive Technical Documentation** (PostGIS+Neo4j+Search integration details)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-VgLA7nv34M5muqZ5MQxBLG)  
- 🖥️ **Comprehensive UI System Overview** (how UI consumes API + citations UX)  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf](file-service://file-MbEYbsLWBmpXVYXVF79c38)  
- 🤖 **Ollama Integration Overview** (local LLM + embeddings + RAG pipeline)  [oai_citation:6‡KFM AI Infrastructure – Ollama Integration Overview.pdf](file-service://file-HCn72HddNvaaXqpJL4svTv)  

### 🧰 Reference portfolios (open in Acrobat to browse embedded docs)
- 🤖 AI Concepts & more  [oai_citation:7‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- 🗺️ Maps / GoogleMaps / Virtual Worlds / Archaeological / WebGL  [oai_citation:8‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- 🧩 Various programming languages & resources  [oai_citation:9‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  
- 🗄️ Data Management / Data Science / Bayesian Methods  [oai_citation:10‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  
- 🧱 Mapping / Modeling / Python / Git / Docker / GraphQL / Linux / Security  [oai_citation:11‡Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf](file-service://file-2QvRgQbts8ENJQSRC6oGme)  
- 🛰️ GIS / Security / ArcGIS / Spark / TypeScript / Web Apps  [oai_citation:12‡Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf](file-service://file-TH7HttQXn8Bh1hVhcj858V)  

---

## ✅ TL;DR

`src/server/` is the **trust boundary**:

- 📡 **Serve** (REST + GraphQL + tiles + downloads)
- 🧾 **Explain** (citations + provenance + manifests)
- 🔐 **Govern** (OPA policies + redaction + audit trails)
- ♻️ **Reproduce** (versioned artifacts, digest-pinned, verifiable)

If a feature can’t satisfy those four, it doesn’t ship. 🚢