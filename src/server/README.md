<!--
📍 File: src/server/README.md
🧠 Purpose: Server-side API boundary for Kansas Frontier Matrix (KFM)
-->

# 🧭 KFM Server (`src/server/`) — Governed API Boundary

![Python](https://img.shields.io/badge/Python-3.11%2B-informational?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20Layer-informational?logo=fastapi)
![OpenAPI](https://img.shields.io/badge/OpenAPI-Swagger-informational?logo=swagger)
![GraphQL](https://img.shields.io/badge/GraphQL-Semantic%20Queries-informational?logo=graphql)
![Postgres](https://img.shields.io/badge/PostgreSQL%20%2B%20PostGIS-Geo%20Truth-informational?logo=postgresql)
![Neo4j](https://img.shields.io/badge/Neo4j-Context%20Graph-informational?logo=neo4j)
![OPA](https://img.shields.io/badge/OPA-Policy%20as%20Code-informational?logo=openid)

> ✅ **Evidence-first** • 🧾 **Provenance-first** • 🔒 **Policy-as-code** • 🧩 **Contract-first**

> [!IMPORTANT]
> `src/server/` is the **single home** for all server-side API code (REST + GraphQL). Legacy API folders were consolidated to eliminate “double API” ambiguity and keep the server boundary crisp.

---

## 🗺️ Table of Contents

- [What lives here](#-what-lives-here)
- [Core responsibilities](#-core-responsibilities)
- [Architecture at a glance](#-architecture-at-a-glance)
- [Suggested folder layout](#-suggested-folder-layout)
- [API surface](#-api-surface)
- [Contracts & versioning](#-contracts--versioning)
- [Provenance & evidence rules](#-provenance--evidence-rules)
- [Policy & governance](#-policy--governance)
- [Security model](#-security-model)
- [Observability & health](#-observability--health)
- [Local development](#-local-development)
- [Testing](#-testing)
- [Adding a new endpoint](#-adding-a-new-endpoint)
- [Roadmap hooks](#-roadmap-hooks)
- [Project docs & reference library](#-project-docs--reference-library)

---

## 📦 What lives here

`src/server/` contains **everything** needed to expose KFM’s platform capabilities via an API boundary:

- 🌐 **REST API** (FastAPI) for core platform operations
- 🧬 **GraphQL endpoint** for semantic + relationship-heavy queries
- 🗺️ **Tile + spatial query endpoints** backed by PostGIS
- 🕸️ **Knowledge graph adapters** backed by Neo4j
- 🤖 **Focus Mode** request handling + citation/provenance packaging
- 🧾 **Story + narrative endpoints** (Story Nodes, Pulse Threads)
- 🔐 **Policy enforcement** (OPA checks in CI + runtime)
- 📈 **Operational endpoints** (health, metrics, audit hooks)

> [!NOTE]
> This folder is *not* the place for heavy ETL/processing. Pipelines should produce **versioned artifacts** + catalogs + provenance; the server **serves, validates, and governs**.

---

## 🎯 Core responsibilities

### 1) Be the **only** way clients access governed data
- The UI (web/AR/mobile), scripts, and external integrations **must** go through this server boundary.
- No “UI → DB direct” shortcuts. Ever. 👮

### 2) Serve data with **context**
KFM’s rule of thumb:

> **PostGIS stores geo truth** (vectors/rasters)  
> **Catalogs describe assets** (STAC/DCAT)  
> **Graph links context** (Neo4j)

This server stitches those together into user-facing responses.

### 3) Enforce **trust primitives**
- ✅ Schema validation
- ✅ Provenance presence (PROV)
- ✅ Catalog presence (STAC/DCAT)
- ✅ Licensing + sensitivity rules (FAIR/CARE)
- ✅ Policy-as-code gates (CI + runtime)
- ✅ Auditability (request IDs, run manifests, evidence manifests)

---

## 🧱 Architecture at a glance

### System flow (outside the server)

```mermaid
flowchart LR
  A[📥 Intake Pipelines] --> B[📚 Catalogs<br/>STAC + DCAT + PROV]
  B --> C[🗺️ PostGIS<br/>Geo truth]
  B --> D[🕸️ Neo4j<br/>Context graph]
  C --> E[🧭 Server API<br/>src/server]
  D --> E
  E --> F[🖥️ Web UI<br/>MapLibre/Cesium]
  E --> G[🤖 Focus Mode]
  E --> H[📱 AR / Mobile]
```

### Inside the server (clean / hexagonal)

```mermaid
flowchart TB
  R[🌐 Routers / Resolvers] --> U[🧠 Use-Cases / Services]
  U --> P[🔌 Ports (Interfaces)]
  P --> A1[🗄️ Adapter: PostGIS]
  P --> A2[🕸️ Adapter: Neo4j]
  P --> A3[🔎 Adapter: Search/Index]
  P --> A4[🔐 Adapter: OPA Policy]
  P --> A5[📦 Adapter: OCI Artifacts]
```

**Key idea:** business logic lives in services/use-cases and talks to *ports*; adapters handle databases, graph, policy engines, artifact registries, etc.

---

## 🗂️ Suggested folder layout

> [!TIP]
> If your actual tree differs, treat this as the **target layout** (north-star). Keep the *seams* (ports/adapters) even if filenames shift.

```text
src/server/
  📄 README.md                      # you are here 🙂
  🚀 main.py                        # app entry (FastAPI)
  ⚙️  settings.py                   # env + configuration
  📁 api/
    📁 routers/                     # REST routes grouped by domain
      📄 health.py
      📄 datasets.py
      📄 query.py
      📄 tiles.py
      📄 story.py
      📄 pulse.py
      📄 focus.py
      📄 ingest.py                  # admin-only
    📁 middleware/
      📄 cors.py
      📄 auth.py
      📄 rate_limit.py
      📄 request_id.py
  🧬 graphql/
    📄 schema.graphql               # contract (or generated)
    📄 resolvers.py
    📄 limits.py                    # depth / cost / pagination enforcement
  🧠 domain/
    📄 models.py                    # Dataset, StoryNode, PulseThread, etc.
    📄 types.py
  🧩 application/
    📄 services.py                  # use-cases: search, focus, story, tiles
  🔌 ports/
    📄 postgis.py                   # interfaces (ports)
    📄 neo4j.py
    📄 opa.py
    📄 artifacts.py
  🧷 adapters/
    📁 outbound/
      📁 postgis/
      📄 client.py
      📄 tiles.py                   # ST_AsMVT helpers, bbox queries, etc.
      📁 neo4j/
      📄 client.py
      📄 queries.py
      📁 opa/
      📄 client.py
      📁 oci/
      📄 oras_client.py             # verify + pull content-addressed artifacts
  📜 contracts/
    📄 openapi.yaml                 # optional: snapshot/hand-curated spec
    📄 schema.graphql               # optional: snapshot
  🛡️ policies/
    📄 README.md                    # how runtime checks map to rego
  🧪 tests/
    📁 unit/
    📁 integration/
```

---

## 🌐 API surface

### REST (examples)

> [!NOTE]
> FastAPI generates an OpenAPI spec (Swagger). In dev, interactive docs usually live at `/docs` and `/redoc` (unless disabled).

Common endpoint families:

| Domain | Example endpoints | Purpose |
|---|---|---|
| ✅ Health | `GET /api/health` | Liveness/readiness |
| 📚 Catalog / Datasets | `GET /api/v1/datasets` • `GET /api/datasets/{id}` | Browse datasets + metadata |
| 🔎 Query | `GET /api/v1/query?table=...` | Filtered data access (bbox/time/etc.) |
| 🗺️ Tiles | `GET /api/v1/tiles/{layer}/{z}/{x}/{y}.pbf` | Vector tiles (XYZ) |
| 🕸️ Graph | `POST /api/graph/query` | Graph traversals (when REST is better) |
| 📖 Story | `POST /api/story` | Submit Story Nodes (evidence required) |
| ⚡ Pulse | `GET /api/pulse` | “Live feed” narrative threads |
| 🤖 Focus | `POST /api/focus` | Q&A with citations + provenance |
| 🧰 Ingest (admin) | `POST /api/ingest` | Trigger ingestion / upload intake |

### GraphQL (semantic queries)

GraphQL is ideal for *relationship traversals*:

- `Person → events → locations`
- `Place → datasets → provenance`
- `ConceptualAttentionNode → linked narratives + datasets`

GraphQL guardrails are mandatory:
- depth/recursion limits
- pagination on lists
- query cost controls

---

## 🧾 Contracts & versioning

### Contract-first (recommended)

- **OpenAPI**: REST request/response schemas must be precise and stable.
- **GraphQL SDL**: schema changes require care; avoid breaking clients.
- **Generated clients** (optional): contract artifacts should allow UI and tools to generate typed clients.

### Versioning rules

- Prefer additive changes (new fields, new endpoints).
- Breaking changes → new API version (`/v2`), or a new GraphQL field/type while deprecating the old.

---

## 🧬 Provenance & evidence rules

### Evidence triplet: STAC + DCAT + PROV
Every dataset served by the API should be traceable across:
- **DCAT**: discovery + licensing + publisher
- **STAC**: spatial/temporal indexing + assets
- **PROV**: lineage + processing history

### IDs should be stable & meaningful
Example dataset IDs follow a structured pattern:

- `kfm.ks.landcover.2000_2020.v1`
- `kfm.ks.counties.boundaries.v1`

### Narrative artifacts must ship an evidence manifest
For **Story Nodes** and **Pulse Threads**, require:
- human-facing citation block
- machine-readable **Evidence Manifest** (YAML/JSON)
- optional: Run Manifest link(s)

---

## 🛡️ Policy & governance

### Policy-as-code everywhere
- ✅ CI gate: policy packs validate catalogs, provenance, and schemas before merge
- ✅ Runtime gate: the server enforces rules at request time (especially for AI answers)

Examples of what policies enforce:
- licensing present and compatible
- sensitivity classification and access rules
- geo-obfuscation where needed
- “no silent rewrites” / append-only expectations

### OPA integration points
- API request authorization (roles, dataset classification)
- Focus Mode answer validation (must include citations, must not leak restricted data)
- Story/Pulse submission checks (evidence manifest required)

---

## 🔐 Security model

### AuthN / AuthZ (planned / supported patterns)
- Token auth (JWT/OAuth2)
- Role-based access (e.g., public / contributor / moderator / admin)
- CORS configured for UI (dev + prod origins)
- Rate limiting + throttles for public endpoints

### Sensitive location handling
For culturally sensitive or protected sites:
- return generalized geometry
- blur/obfuscate coordinates
- require elevated role for exact access
- log access for audit (where appropriate)

### Supply-chain & artifact integrity (forward-looking)
When serving “offline packs” or derived artifacts:
- use **content-addressed** blobs
- verify signatures (Cosign)
- pull via OCI/ORAS for reproducible distribution and rollback

---

## 📈 Observability & health

Minimum operational endpoints:

- `GET /api/health` → basic liveness
- `GET /api/ready` → checks PostGIS/Neo4j/OPA connectivity
- `GET /api/metrics` → Prometheus/OpenTelemetry compatible (if enabled)

Operational checks we care about:
- orphaned graph nodes (no backing STAC/DCAT/PROV)
- missing distributions for catalog entries
- pipeline lag / stale layers
- policy pack version drift

---

## 🧑‍💻 Local development

> [!TIP]
> KFM server development is easiest with Docker running dependencies.

### Prereqs
- 🐍 Python 3.11+
- 🐳 Docker (recommended)
- 🗄️ Postgres + PostGIS
- 🕸️ Neo4j
- 🔐 OPA (or policy service)

### Typical workflow

```bash
# 1) create env
python -m venv .venv
source .venv/bin/activate

# 2) install deps (choose your tooling)
pip install -r requirements.txt

# 3) run server (example)
uvicorn src.server.main:app --reload --port 8000
```

### Environment variables (starter set)

<details>
<summary><strong>🔧 Suggested env vars</strong> (click to expand)</summary>

| Variable | Example | Notes |
|---|---|---|
| `KFM_ENV` | `dev` | environment mode |
| `KFM_API_HOST` | `0.0.0.0` | bind host |
| `KFM_API_PORT` | `8000` | bind port |
| `KFM_POSTGIS_DSN` | `postgresql://user:pass@localhost:5432/kfm` | PostGIS |
| `KFM_NEO4J_URI` | `bolt://localhost:7687` | Neo4j |
| `KFM_NEO4J_USER` | `neo4j` | Neo4j user |
| `KFM_NEO4J_PASSWORD` | `password` | Neo4j pass |
| `KFM_OPA_URL` | `http://localhost:8181` | policy engine |
| `KFM_JWT_ISSUER` | `https://issuer.example` | if auth enabled |
| `KFM_JWT_AUDIENCE` | `kfm-api` | if auth enabled |
| `KFM_CORS_ORIGINS` | `http://localhost:3000` | UI dev origin |
| `KFM_RATE_LIMIT_RPS` | `10` | public throttle |
| `KFM_ARTIFACT_REGISTRY` | `ghcr.io/...` | OCI artifacts (optional) |

</details>

---

## 🧪 Testing

Recommended layers:

- ✅ Unit tests: domain + services (no network)
- ✅ Integration tests: PostGIS/Neo4j adapters (dockerized)
- ✅ Contract tests: OpenAPI + GraphQL shape checks
- ✅ Policy tests: OPA/Conftest in CI

Example commands (adjust to your tooling):

```bash
pytest
ruff check .
mypy .
```

---

## 🧩 Adding a new endpoint

Use this checklist to keep the server “KFM-clean” 🧼:

### ✅ Endpoint checklist
- [ ] Define contract (Pydantic/OpenAPI and/or GraphQL SDL)
- [ ] Implement use-case in `application/` (no DB calls here)
- [ ] Use a `port` interface to access PostGIS/Neo4j/… (adapter behind it)
- [ ] Add policy checks (authz + data classification + evidence requirements)
- [ ] Add tests (unit + integration as needed)
- [ ] Ensure responses include provenance hooks (IDs, citations, manifests)
- [ ] Update docs (this README + any domain README)

### 🧠 Special case: Focus Mode
Focus endpoints must:
- include citations/source links
- avoid restricted data leakage
- produce structured provenance for audits
- support streaming responses (optional)

---

## 🧩 Roadmap hooks

These concepts are already “on the blueprint” and should shape server design:

- ⚡ **Pulse Threads**: geotagged “live feed” narratives backed by citations
- 🧠 **Conceptual Attention Nodes**: high-level concepts for AI/UI focus control
- 📦 **Offline packs**: PMTiles / artifact bundles for low-connectivity usage
- 🌎 **Federation**: multi-region deployments with shared contracts + governance
- 🛰️ **4D Digital Twin + AR**: same APIs, new clients (don’t fork endpoints)
- 🕵️ **Geo-obfuscation**: culturally sensitive/protected site handling

---

## 📚 Project docs & reference library

Authoritative KFM docs (start here):
- 📘 *Comprehensive Technical Documentation* (API endpoints, FastAPI/GraphQL basics)
- 🧱 *Comprehensive Architecture, Features, and Design* (stack + responsibilities)
- 🧭 *AI System Overview* (Focus Mode, RAG, governance checks)
- 📥 *Data Intake – Technical & Design Guide* (STAC/DCAT/PROV, run manifests, append-only)
- 🖥️ *Comprehensive UI System Overview* (how UI consumes REST/GraphQL, AR parity)
- ✨ *Innovative Concepts to Evolve KFM* (4D twin, cultural protocols, obfuscation)
- 🌟 *Latest Ideas & Future Proposals* (Pulse Threads, offline packs, roadmap)
- 💡 *Additional Project Ideas* (evidence manifests, deterministic patterns, OCI artifacts)
- 🧾 *Design Audit – Gaps & Enhancements* (quality bar + improvements)

Reference portfolios (open in Acrobat to browse embedded docs):
- 🤖 *AI Concepts & more* (AI patterns + research)
- 🗺️ *Maps / GoogleMaps / Virtual Worlds / Archaeological / WebGL* (rendering + mapping research)
- 🧰 *Various programming languages & resources* (implementation references)
- 🗄️ *Data Management / Data Science / Bayesian Methods* (architecture + methods)
- 📊 *Data Mining Concepts & Applications* (privacy, metrics, evaluation)
- 🧑‍🍳 *Python Geospatial Analysis Cookbook* (PostGIS & spatial processing patterns)

---

### ✅ TL;DR

This folder is the **trust boundary**:

- 📡 **Serve** (REST + GraphQL + tiles)
- 🧾 **Explain** (citations + provenance)
- 🔐 **Govern** (OPA policies + auditability)
- 🧩 **Scale** (stateless API + adapters)

If a feature can’t satisfy those four, it doesn’t ship. 🚢