<!-- 📍 Path: api/app/README.md -->

# 🧭 Kansas Frontier Matrix — API App (`api/app`) 🌾🗺️

![FastAPI](https://img.shields.io/badge/FastAPI-%F0%9F%9A%80-009688?style=for-the-badge)
![OpenAPI](https://img.shields.io/badge/OpenAPI-%F0%9F%93%9D-6BA4FF?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-%F0%9F%90%B3-2496ED?style=for-the-badge)
![PostGIS](https://img.shields.io/badge/PostGIS-%F0%9F%8C%8D-336791?style=for-the-badge)
![Neo4j](https://img.shields.io/badge/Neo4j-%F0%9F%95%B8%EF%B8%8F-4581C3?style=for-the-badge)
![OPA](https://img.shields.io/badge/OPA-%F0%9F%9B%A1%EF%B8%8F-7B61FF?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-%F0%9F%A4%96-111111?style=for-the-badge)

> **Evidence-first. Governed by design.**  
> This app is the **single entry point** for runtime access to Kansas Frontier Matrix (KFM) data & AI—**no direct DB access from UIs**.  
> **“No Source, No Answer.”** ✅📚

---

<details>
  <summary><strong>📚 Table of Contents</strong> (click to expand)</summary>

- [🎯 What lives here](#-what-lives-here)
- [🧱 Architecture in 90 seconds](#-architecture-in-90-seconds)
- [🚀 Quickstart](#-quickstart)
  - [🐳 Docker Compose (recommended)](#-docker-compose-recommended)
  - [🧪 Verify it’s running](#-verify-its-running)
- [🧩 API Surface (high-level)](#-api-surface-high-level)
  - [🩺 Health & meta](#-health--meta)
  - [🗂️ Catalog & datasets](#️-catalog--datasets)
  - [🧮 Ad-hoc query (safe SQL)](#-ad-hoc-query-safe-sql)
  - [🧱 Map tiles](#-map-tiles)
  - [🧬 GraphQL](#-graphql)
  - [🤖 Focus Mode (RAG + citations)](#-focus-mode-rag--citations)
- [⚙️ Configuration](#️-configuration)
- [🧑‍💻 Dev workflow](#-dev-workflow)
- [🛡️ Governance & safety](#️-governance--safety)
- [🧯 Troubleshooting](#-troubleshooting)

</details>

---

## 🎯 What lives here

This directory contains the **FastAPI application** for KFM, including:

- 🌐 **REST API** (versioned paths like `/api/v1/...`)
- 🧬 **GraphQL** endpoint (`/graphql`) for relationship-heavy queries
- 🧱 **Tile services** for raster + vector maps (`/tiles/...`)
- 🤖 **Focus Mode** endpoint (`/focus-mode/query`) — retrieval + generation with citations
- 🛡️ **Policy gates** (OPA / rules) and governance middleware hooks
- 🗃️ Adapters to runtime stores:
  - **PostGIS** (spatial queries, aggregations, tiles)
  - **Neo4j** (knowledge graph relationships)
  - **Search / embeddings index** (full-text + vector similarity)
  - **Object storage** (COGs, PMTiles, PDFs, large assets)

---

## 🧱 Architecture in 90 seconds

KFM enforces a **canonical “truth path”**:

**Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI** ✅

The API is where we enforce:

- ✅ authN/authZ
- ✅ auditing & provenance
- ✅ policy gates (fail-safe defaults)
- ✅ “No Source, No Answer” for AI outputs

### 🔁 Request flow (conceptual)

```mermaid
flowchart LR
  UI[🗺️ UI / Client] -->|HTTPS| API[🌐 FastAPI App]
  API -->|SQL/Spatial| PG[(🗃️ PostGIS)]
  API -->|Cypher| G[(🕸️ Neo4j)]
  API -->|Search| IDX[(🔎 Search / Vector Index)]
  API -->|Assets| OBJ[(📦 Object Storage)]
  API -->|Policy checks| OPA[🛡️ OPA / Rules]
  API -->|LLM calls (internal)| OLLAMA[🤖 Ollama]
  API --> UI
```

---

## 🚀 Quickstart

### 🐳 Docker Compose (recommended)

From the repo root (where `docker-compose.yml` and `.env.example` typically live):

1) **Create your environment file**
```bash
cp .env.example .env
```

2) **Start the dev stack**
```bash
docker-compose up --build
```

Typical dev stack services (names may vary):  
- `db` 🗃️ PostGIS (host port often **5432**)  
- `graph` 🕸️ Neo4j (host ports often **7474**/**7687**)  
- `api` 🌐 FastAPI (host port often **8000**)  
- `web` 🖥️ React dev server (host port often **3000**)  
- `ollama` 🤖 LLM service (host port often **11434**)  
- `opa` 🛡️ Policy agent (often **8181**, optional in dev)

> 💡 Compose networking lets containers reach each other by service name (example: `POSTGRES_HOST=db`, `OLLAMA_API_URL=http://ollama:11434`).

---

### 🧪 Verify it’s running

Once the stack is up, open:

- 🧾 Swagger UI: `http://localhost:8000/docs`
- 📜 OpenAPI JSON: `http://localhost:8000/openapi.json`
- 🧬 GraphQL: `http://localhost:8000/graphql`

Quick health checks:

```bash
curl -s http://localhost:8000/healthz
curl -s http://localhost:8000/readyz
curl -s http://localhost:8000/version
```

---

## 🧩 API Surface (high-level)

> Endpoints listed below reflect the KFM API design. Some routes may differ in your local branch—**Swagger (`/docs`) is the source of truth** for what is currently mounted.

### 🩺 Health & meta

- `GET /healthz` — liveness
- `GET /readyz` — dependency readiness (DBs, indexes, etc.)
- `GET /version` — service version

---

### 🗂️ Catalog & datasets

- `GET /api/v1/datasets/{id}`  
  Returns dataset metadata (DCAT summary + links to STAC/assets).

- `GET /api/v1/catalog/search`  
  Search datasets by keyword, bbox, or time range.

- `GET /api/v1/datasets/{id}/data?format=geojson&bbox=...`  
  Streams dataset features filtered by spatial/attribute constraints.

---

### 🧮 Ad-hoc query (safe SQL)

- `GET /api/v1/query?table=...&select=...&where=...&bbox=...`

This is a **constrained & logged** interface:
- ✅ validates allowed tables/views
- ✅ applies row/column permissions
- ✅ supports spatial filtering

---

### 🧱 Map tiles

To power map visualization clients (MapLibre, OpenLayers, etc.):

- Vector tiles: `GET /tiles/{layer}/{z}/{x}/{y}.pbf`
- Raster tiles: `GET /tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`)

---

### 🧬 GraphQL

- `POST /graphql`

GraphQL is built for **relationship-heavy** retrieval:
- Places ↔ datasets ↔ events ↔ stories
- typically resolves by querying **Neo4j + PostGIS** together

Example query (illustrative):

```graphql
query {
  storyNodes {
    id
    title
    yearRange
  }
}
```

---

### 🤖 Focus Mode (RAG + citations)

- `POST /focus-mode/query`

Focus Mode is the “map assistant”:
1) 🧼 **Prompt Gate** sanitizes user input
2) 🔎 **Retrieval** gathers evidence (Neo4j + PostGIS + search + vectors)
3) 🤖 **LLM generation** via Ollama **using provided sources only**
4) 🛡️ **OPA policy check** validates citations + safety + access controls
5) 🧾 **Audit logging** stores question, sources, model ID, policy decision

Example (illustrative):

```bash
curl -s http://localhost:8000/focus-mode/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What happened here in the 1930s?",
    "map_context": {"place_id": "finney_county", "year": 1935}
  }'
```

Expected response shape (illustrative):
- `answer` (with citation markers like `[1]`, `[2]`)
- `citations` (structured source metadata for UI click-through)
- `policy` / `audit_id` (optional, depending on implementation)

---

## ⚙️ Configuration

Configuration is primarily via `.env` / environment variables.

Common knobs referenced in KFM docs include:

### 🧩 API runtime

- `FASTAPI_PORT` — API port (often `8000`)
- `KFM_API_RELOAD` — dev hot reload (`true/false`)
- `KFM_API_WORKERS` — concurrency (production)
- `KFM_JWT_SECRET` — **required** for auth token signing (set a strong value)

### 🗃️ PostGIS (examples)

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- (often also `POSTGRES_HOST`, `POSTGRES_PORT` in dockerized setups)

### 🕸️ Neo4j (examples)

- `NEO4J_AUTH` (commonly `user/password`)
- (often `NEO4J_URI` or host/port vars depending on compose)

### 🤖 AI / Ollama (examples)

- `OLLAMA_API_URL` (example: `http://ollama:11434`)
- `OLLAMA_MODEL` (example: `kfm-llama2` or similar)

> ✅ Tip: If you change environment variables, restart the stack:
```bash
docker-compose down
docker-compose up --build
```

---

## 🧑‍💻 Dev workflow

### 🗂️ Suggested internal layout (adjust to actual tree)

This is the **intended clean separation** between HTTP, business logic, and external adapters:

```text
api/
└─ app/
   ├─ main.py              # FastAPI app startup
   ├─ api/                 # routers/controllers (HTTP boundary)
   │  └─ v1/
   │     ├─ routes/
   │     └─ schemas/
   ├─ services/            # use-cases / orchestration logic
   ├─ domain/              # core models (framework-agnostic)
   ├─ adapters/            # PostGIS/Neo4j/search clients
   ├─ governance/          # policy gates, provenance hooks
   ├─ ai/                  # focus pipeline, prompt templates, ollama client
   └─ tests/
```

### ➕ Add a new endpoint (pattern)

1) Create a route handler in `api/v1/routes/...`  
2) Delegate to a service in `services/...`  
3) Fetch data through an adapter in `adapters/...`  
4) Attach provenance metadata where relevant  
5) Add tests in `tests/`  
6) Validate it shows up in Swagger `/docs`

---

## 🛡️ Governance & safety

KFM treats governance as **first-class infrastructure**:

- ✅ **Provenance is mandatory**: publishable data must have linked metadata (DCAT/STAC/PROV).
- 🛡️ **Policy gates** block unsafe or ungoverned behavior (better to block than to leak).
- 🤖 **AI answers must include citations** or the system should refuse/fallback.
- 🧾 **Audit logs** enable review: question, sources, model version, policy decision.

> ⭐ Golden rule: **If you can’t cite it, don’t ship it.**

---

## 🧯 Troubleshooting

### 🔌 API can’t connect to DBs
- Check logs:
```bash
docker-compose logs api
docker-compose logs db
docker-compose logs graph
```
- Sometimes DBs aren’t ready yet → restart:
```bash
docker-compose up --build
```

### 🚪 Port conflicts
Common ports:
- Postgres/PostGIS: `5432`
- Neo4j: `7474`, `7687`
- API: `8000`
- Web: `3000`
- Ollama: `11434`

If something is already bound, change port mappings in compose.

### 🧠 Docker memory / performance
Large datasets + models can be heavy:
- Increase Docker memory allocation (especially on macOS/Windows)
- Consider smaller local models for dev

### 🗃️ Volume permission issues
If mounted volumes are not writable (common on Windows/macOS), align user IDs or adjust mount options.

---

🏁 **That’s it.** Start the stack, open `/docs`, and build from the truth path forward. 🌾🗺️