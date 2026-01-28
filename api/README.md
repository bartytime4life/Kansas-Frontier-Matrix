# 🧩 Kansas Frontier Matrix API (FastAPI)

![Python](https://img.shields.io/badge/Python-3.x-informational)
![FastAPI](https://img.shields.io/badge/FastAPI-⚡-success)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![PostGIS](https://img.shields.io/badge/PostGIS-🗺️-9cf)
![Neo4j](https://img.shields.io/badge/Neo4j-🧠-brightgreen)
![OPA](https://img.shields.io/badge/Governance-OPA%20%2B%20Rego-purple)

> 🔎 **Provenance-first backend**: KFM is designed so maps, stories, datasets, and even AI answers remain traceable to sources through a “truth path” (pipeline → catalog → DB → API → UI). 🧾

---

## 📌 What this folder is

This `api/` directory contains the **backend server** for Kansas Frontier Matrix (KFM): a **FastAPI** application exposing KFM data and services via:

- 🌐 **REST endpoints** (primary)
- 🧬 **GraphQL (optional)** if enabled

The backend is also where KFM enforces **validation + governance**: the UI and AI don’t bypass the API—they go *through it*. 🛡️

---

## 🗺️ “Truth Path” data flow (how KFM stays trustworthy)

```mermaid
flowchart LR
  raw[📥 Raw Inputs\n(data/raw/)] --> etl[🧪 Deterministic Pipelines\n(pipelines/)]
  etl --> processed[🧹 Processed Data\n(data/processed/)]
  processed --> meta[🗃️ Metadata\n(data/catalog/)]
  processed --> prov[🧾 Provenance\n(data/provenance/)]
  processed --> stores[🧠 Runtime Stores\nPostGIS • Neo4j • Search Index]
  stores --> api[🧩 Backend API\n(api/)]
  api --> ui[🖥️ Frontend UI\n(web/)]
  api --> ai[🤖 Focus Mode AI\n(via API)]
  policy[🛡️ OPA Policies\n(policy/)] -.enforces.-> api
  policy -.enforces.-> ai
```

**Key idea:** the API is the choke-point where policy + provenance are enforced consistently. ✅

---

## 🧱 Backend architecture (Clean Architecture-ish)

KFM’s API is intended to stay modular by separating **core logic** from **framework details**:

- 🧬 **Domain / Models**: core entities (often Pydantic models)
- 🧠 **Service layer**: business logic / use-cases (analysis, stories, queries)
- 🔌 **Adapters / Repositories**: PostGIS, Neo4j, search, external APIs
- 🌐 **FastAPI routes**: thin handlers that validate input and call services

> 🧠 Rule of thumb: routes should do **validation + orchestration**, not heavy computation.

---

## 🗂️ Suggested folder map

Your exact repo may vary, but KFM’s blueprint implies a structure like:

```text
api/
├─ 🚀 main.py                      # FastAPI app init: routers, CORS, startup/shutdown
├─ 🧭 routes/                      # HTTP endpoints grouped by domain
│  ├─ datasets.py
│  ├─ features.py
│  ├─ stories.py
│  ├─ search.py
│  └─ ai.py                        # Focus Mode endpoint(s)
├─ 🧬 models/ or domain/            # LandParcel, HistoricalEvent, StoryNode, etc.
├─ 🧠 services/                    # analysis_service.py, story_service.py, ...
├─ 🔌 db/ or adapters/             # PostGIS + Neo4j + (optional) search adapters
│  ├─ postgis.py                   # SQL / ORM integration
│  └─ neo4j.py                     # Cypher integration
└─ ✅ tests/                       # unit + integration tests (FastAPI TestClient)
```

---

## 🧰 Tech stack highlights

Common KFM backend components described in the blueprint:

- 🗺️ **PostGIS** (PostgreSQL spatial): spatial queries + vector/raster storage
- 🧠 **Neo4j**: knowledge-graph relationships (people/places/events/sources)
- 🔎 **Search index** (optional): full-text and/or embeddings search
- 🧩 **FastAPI**: REST (+ optional GraphQL), Pydantic validation, auto docs
- 🛡️ **OPA + Rego** policies: governance (data access + AI constraints)

---

## 🚀 Run locally (Docker Compose dev workflow)

> ⚠️ Most KFM setups run from the **repo root**, not from inside `api/`.

### 1) Start the stack

```bash
# from repo root
docker compose up --build
# or
docker-compose up --build
```

### 2) Explore the API docs

```text
Swagger UI: http://localhost:8000/docs
```

### 3) Optional: GraphQL interface (if enabled)

```text
GraphQL: http://localhost:8000/graphql
```

### 4) Databases (for debugging)

```text
PostGIS: localhost:5432
Neo4j UI: http://localhost:7474
```

### 5) Auto-reload while developing

If Compose mounts your code into the container and runs Uvicorn with `--reload`,
then editing files like `api/routes/datasets.py` should trigger a reload. 🔁

---

## 🔎 Using the API (examples)

> ✅ **Source of truth** for what exists: **Swagger UI** at `/docs`.

### REST examples (illustrative)

```bash
# list datasets (if implemented)
curl -s http://localhost:8000/datasets

# fetch a feature/entity by ID (if implemented)
curl -s http://localhost:8000/features/123

# search (if implemented)
curl -s "http://localhost:8000/search?q=railroad"
```

### GraphQL example (if enabled)

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

## 🤖 Focus Mode AI (backend-governed AI answers)

The “Focus Mode” assistant is designed to be:

- 🔒 **policy constrained** (no ungoverned chatbot behavior)
- 🧾 **provenance-aware** (answers should reference sources)
- 🧠 **API-mediated** (AI uses the same access rules as everyone else)

### Typical request shape (illustrative)

```bash
curl -s -X POST http://localhost:8000/ai/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "List major trails in Kansas and their purposes."
  }'
```

<details>
<summary>🧠 AI runtime configuration (common patterns)</summary>

Depending on how your environment is configured, the API may use:

- 🏠 **Local Ollama** (for local/private inference)
- ☁️ **OpenAI** (if enabled + API key present)

Common env/config names referenced in the blueprint include:
- `OLLAMA_MODEL`
- `AI_BACKEND_URL` (example: `http://host.docker.internal:11434`)
- `OPENAI_API_KEY`

> If AI isn’t configured, the endpoint may error or fall back to a “dummy AI” mode (implementation-dependent).

</details>

---

## 🛡️ Governance & policy-as-code (OPA + Rego)

KFM treats governance rules as first-class code:

- 📁 `/policy/` contains policies (often **OPA Rego**) for:
  - 📜 dataset licensing / metadata requirements
  - 🔐 access rules (roles vs dataset sensitivity)
  - 🤖 AI constraints (what can be answered, citation requirements, etc.)

### How it is enforced

- ✅ **CI enforcement** (ex: Conftest runs policy checks in PRs)
- 🧩 **Runtime enforcement**:
  - the API asks OPA “can user X access dataset Y?”
  - responses may be denied (403) or sanitized, depending on policy and implementation

> 🧠 Design goal: policies are the “source of truth,” versioned with the repo.

---

## ✅ Testing

Typical patterns:

```bash
# run tests inside the api container (if configured)
docker compose exec api pytest
# or
docker-compose exec api pytest
```

Testing strategy usually includes:
- 🧪 unit tests for services (mock adapters)
- 🔗 integration tests for endpoints (FastAPI TestClient)

---

## 🧯 Troubleshooting (common dev issues)

### Port conflicts
If you already have local services running, you may need to remap ports:
- `5432` (Postgres)
- `7474` (Neo4j)
- `8000` (API)
- `3000` (Web)

### Dependency order / DB readiness
Sometimes the API boots before DB is ready—re-run:

```bash
docker compose up
# or ensure compose depends_on is configured
```

### Volume permissions (Linux/Mac/Windows)
If the API container needs to write under `data/` and fails, verify that:
- host directories are writable
- the container user matches expected permissions

### Rebuild after dependency changes
```bash
docker compose up --build
# or
docker-compose build
```

---

## 🧭 Developer workflow: adding a new feature endpoint

A good “KFM-style” change is usually:

- [ ] 🧬 Add/extend a domain model (`api/models/` or `api/domain/`)
- [ ] 🔌 Add a repository method (PostGIS / Neo4j / search adapter)
- [ ] 🧠 Add a service function (business logic, testable)
- [ ] 🌐 Add a route handler (`api/routes/...py`)
- [ ] ✅ Add tests (unit + integration)
- [ ] 🛡️ Add/adjust policy rules (if it impacts access, privacy, or AI)

---

## 🔗 Related docs (repo-local)

- 📘 `../README.md` (project overview)
- 🧪 `../pipelines/` (data ingestion & processing)
- 🗃️ `../data/catalog/` + `../data/provenance/` (metadata + provenance)
- 🛡️ `../policy/` (OPA/Rego governance policies)
- 🧠 `../docs/` (architecture + story documentation)

---

## 🧩 Guiding principles (API layer)

- ✅ **Thin controllers**, thick services
- 🧾 **Provenance & traceability** are not optional
- 🛡️ **Policies enforce reality**, not vibes
- 🔁 **Deterministic pipelines** feed stable stores; API reads those stores
- 🧠 **AI is a client of the system**, not a shortcut around it