# 🗺️ Kansas Frontier Matrix (KFM)

> **Governed, evidence-first geospatial + historical knowledge system** for Kansas: **data → pipeline → APIs → maps/stories → Focus Mode (auditable AI)**.

![Governed](https://img.shields.io/badge/Governance-Governed-2b6cb0)
![Evidence-first](https://img.shields.io/badge/Principle-Evidence--First-2f855a)
![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%20%2B%20CARE-805ad5)
![Clean Architecture](https://img.shields.io/badge/Architecture-Clean%20Layers-4a5568)
![Trust membrane](https://img.shields.io/badge/Security-Trust%20Membrane-c05621)

---

## Table of contents

- [What KFM is](#what-kfm-is)
- [Core principles](#core-principles)
- [Quickstart](#quickstart)
  - [Run with Docker Compose](#run-with-docker-compose)
  - [Build & run from source](#build--run-from-source)
- [Architecture at a glance](#architecture-at-a-glance)
- [Repo layout](#repo-layout)
- [Governed data pipeline](#governed-data-pipeline)
- [Story Nodes & Focus Mode](#story-nodes--focus-mode)
- [Contributing](#contributing)
- [Security](#security)
- [Documentation](#documentation)
- [License](#license)
- [Support](#support)

---

## What KFM is

KFM is a **monorepo** that co-evolves **code, datasets, and governed narratives** in one versioned history—so the repository itself acts like a **traceable “data lake”** where lineage can be inspected via commits and metadata.  
It is designed to support:

- **Interactive maps** (React + MapLibre) and time-aware exploration (timeline/layer controls).
- **A governed backend API** (FastAPI) that mediates all data access and enforces policies.
- **Multiple governed stores** for different access patterns:
  - **PostgreSQL + PostGIS** for spatial-relational queries
  - **Neo4j** for knowledge-graph relationships
  - **Search + semantic retrieval** (Elasticsearch/OpenSearch and/or a vector index)
- **Story Nodes**: Markdown-driven interactive narratives with strict structure + citations.
- **Focus Mode**: a Q&A assistant that is **grounded in KFM’s own evidence** and returns **cited answers**.

> [!IMPORTANT]
> **KFM is “evidence-first.”** Any user-visible claim—map layer metadata, story narrative statements, and AI answers—should be traceable to data sources via **metadata and provenance** (e.g., DCAT/STAC/PROV + citations).

---

## Core principles

### ✅ Evidence-first by design
- Dataset dialogs and Focus Mode include an **Audit** view that surfaces provenance chains.
- Story Nodes require **citations for factual claims** and are validated in CI.

### ✅ Clean architecture boundaries (layered design)
KFM follows clean-layer separation to keep core rules stable while swapping infrastructure:

- **Domain**: pure entities/models
- **Use Case / Services**: workflows & business logic
- **Integration / Interfaces**: ports/contracts + adapters
- **Infrastructure**: PostGIS/Neo4j/search, FastAPI routers, React UI, CI/CD, containers

### ✅ Trust membrane
Frontend and external clients **never** access databases directly.  
All access flows through the governed API layer so that permissions, provenance, and policy checks stay centralized.

---

## Quickstart

> [!NOTE]
> KFM’s guides describe Docker Compose as the simplest local environment. If your repository uses different service names/ports, treat the values below as **defaults** and verify in your `docker-compose.yml` and `.env`.

### Run with Docker Compose

```bash
# from repo root
docker compose up --build
# or (legacy):
docker-compose up --build
```

Common dev endpoints (defaults; verify in `.env` / compose):

| Component | Typical dev URL |
|---|---|
| Frontend (React dev server) | `http://localhost:3000` |
| Backend API (FastAPI) | `http://localhost:8000` |
| Neo4j Browser UI | `http://localhost:7474` |
| Elasticsearch/OpenSearch | `http://localhost:9200` |
| PostgreSQL/PostGIS | `localhost:5432` |

Dev ergonomics (typical Compose setup):
- Backend container runs Uvicorn with `--reload` and mounts source for hot reload.
- Frontend dev server hot reloads when editing files.

Troubleshooting basics:

```bash
# view logs
docker compose logs -f

# restart after env changes
docker compose down
docker compose up --build

# exec into a running service
docker compose exec backend bash
```

### Build & run from source

> [!CAUTION]
> These commands are representative. Your exact module paths, entrypoints, and package managers may differ.

#### Backend (FastAPI)

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

# Typical env vars (examples)
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/postgres"
export NEO4J_URL="bolt://neo4j:password@localhost:7687"

# Typical run (example)
uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend (React + MapLibre)

```bash
cd frontend
npm install
npm start
```

Common configuration patterns:
- In dev, the React server may proxy API requests to `localhost:8000` (see `package.json` / proxy config).
- In production, the frontend often needs an API base URL (e.g., `REACT_APP_API_URL`) at build time.

---

## Architecture at a glance

```mermaid
flowchart LR
  UI[React + MapLibre UI] -->|HTTP (governed)| API[FastAPI Backend API]

  subgraph Stores[Governed stores]
    PG[(PostgreSQL + PostGIS)]
    N4J[(Neo4j Knowledge Graph)]
    SRCH[(Elasticsearch/OpenSearch + Vector Index)]
    OBJ[(Files/Tiles/Object storage)]
  end

  API --> PG
  API --> N4J
  API --> SRCH
  API --> OBJ
```

Key operational rule:
- **UI never talks to stores directly**; all queries go through the API boundary.

---

## Repo layout

> [!NOTE]
> The implementation/blueprint docs describe the *expected* monorepo structure. Your repo may use `api/` + `web/` naming instead of `backend/` + `frontend/`.

```text
.
├── backend/                        # FastAPI app (clean architecture layers)
│   ├── domain/                     # Core entities/models (no DB/UI deps)
│   ├── services/                   # Use-cases / workflows / business logic
│   ├── adapters/                   # Repository implementations / integrations
│   └── api/                        # Routers/controllers (FastAPI endpoints)
│
├── frontend/                       # React + MapLibre UI
│   └── src/
│
├── data/                           # Governed datasets & metadata
│   ├── raw/                        # Immutable snapshots + manifests
│   ├── work/                       # Intermediate/transient artifacts
│   ├── processed/                  # Clean/standard outputs
│   ├── stac/                       # STAC metadata (spatiotemporal assets)
│   ├── catalog/
│   │   └── dcat/                   # DCAT catalog metadata
│   └── prov/                       # W3C PROV lineage records
│
├── docs/                           # Governed documentation (Markdown)
│   ├── standards/                  # Protocols & standards
│   ├── templates/                  # Governed templates (Universal Doc, Story Node v3, API contract)
│   ├── governance/                 # ROOT_GOVERNANCE, ETHICS, SOVEREIGNTY, etc.
│   ├── stories/                    # Story Nodes (or docs/reports/<topic>/story_nodes/)
│   ├── api/                        # API docs, contract extensions, etc.
│   ├── ci/                         # CI checklists, validation procedures
│   └── reference/                  # External references used by KFM
│
├── deploy/                         # Kubernetes/Helm/GitOps manifests (if present)
├── scripts/                        # Utility scripts (validators, loaders, helpers)
├── tests/                          # Test suites (or backend/tests/)
└── .github/workflows/              # CI workflows
```

---

## Governed data pipeline

All data flows through a governed “truth path” that enforces:
- **immutability** at raw ingest,
- **validation gates** between stages,
- **metadata completeness** (manifest + STAC/DCAT + PROV),
- **fail-closed** CI enforcement.

```mermaid
flowchart LR
  RAW[data/raw/<domain>/ + source manifest] -->|ETL| WORK[data/work/ intermediates]
  WORK -->|ETL| PROC[data/processed/ outputs]
  PROC --> META[data/stac/ + data/catalog/dcat/]
  PROC --> PROV[data/prov/ lineage]
  PROC -->|load| PG[(PostGIS)]
  PROC -->|upsert| N4J[(Neo4j)]
  PROC -->|index| SRCH[(Search/Vector)]

  META --> API[FastAPI API]
  PROV --> API
  API --> UI[React UI + Focus Mode]
```

### Dataset identity & provenance
- Every dataset should have a **stable identifier** used in catalog, graph, stories, and citations (example: `kfm:hydrology:rivers_v1`).
- Every raw dataset should include a **manifest** capturing provenance context (source, acquisition date, checksum, license, etc.).
- Every processed dataset should have PROV linking inputs → transform activity → outputs.

> [!IMPORTANT]
> **No dataset should appear in the UI/API without a provenance chain.** If metadata is missing, the pipeline should fail closed.

---

## Story Nodes & Focus Mode

### Story Nodes (governed narratives)
A Story Node is a curated narrative designed to *drive* the UI:
- Written in **Markdown** with required sections and citations.
- Paired with a structured “map choreography” configuration (JSON/YAML/front-matter) for steps (center/zoom/layers/time slice).
- Stored in the repo (commonly under `docs/stories/`).

Story validation (typical CI checks):
- Follows Story Node Template v3 structure (Overview, Steps, Conclusion, etc.).
- Citations present for factual claims.
- Media references exist and include alt text.
- Dataset IDs referenced in the story exist in the catalog.

### Focus Mode (auditable Q&A)
Focus Mode is a conversational assistant integrated into the KFM UI:

- **Grounded only in KFM’s knowledge base** (no open internet).
- Uses retrieval from catalog/graph/search to assemble context.
- Returns answers with **clickable citations** and logs interactions for audit.
- May run a **local LLM** (via Ollama) for privacy and offline deployments.

> [!CAUTION]
> If a user requests sensitive location details or culturally restricted knowledge, the system should **generalize/redact** and route content for governance review.

---

## Contributing

KFM treats **code, data, and docs** as first-class governed artifacts. CI enforces standards for all three.

### Contribution workflow (typical)
1. Open or select an issue.
2. Branch → implement changes with tests + docs.
3. Run local checks (lint/tests/validators).
4. Open a PR; CI runs build + tests + data/doc validators.
5. Review focuses on:
   - architecture boundary compliance,
   - provenance completeness,
   - sensitivity/CARE considerations,
   - readability + accessibility.

### ✅ Definition of Done checklists

#### Code changes
- [ ] Changes respect clean architecture boundaries (no business logic in route handlers).
- [ ] Frontend does **not** bypass the API (trust membrane).
- [ ] Tests updated/added (unit + integration/contract where applicable).
- [ ] No secrets committed; configs via `.env` / secret manager.
- [ ] CI is green.

#### Data additions
- [ ] Raw file added under `data/raw/…` **without modification**
- [ ] Source manifest created with required fields (source, acquisition date, checksum, license, etc.)
- [ ] Processing code added/updated to produce `data/processed/…`
- [ ] STAC/DCAT metadata added/updated
- [ ] PROV lineage record added/updated
- [ ] Validators pass (schema checks, link checks, policy checks)

#### Story Nodes / docs
- [ ] Uses the correct template (Story Node v3 / Universal Doc / API contract extension)
- [ ] All substantive claims have citations
- [ ] Links and images resolve; images include alt text
- [ ] Markdown lint passes; document renders cleanly

---

## Security

> [!IMPORTANT]
> KFM’s repo security should assume a modern DevSecOps baseline (branch protections + secret scanning + least-privilege CI).

Recommended practices:
- Protect `main` with required reviews + required status checks.
- Require **signed commits** for critical branches.
- Enable **secret scanning** + push protection.
- Use Dependabot and code scanning (e.g., CodeQL).
- Harden GitHub Actions:
  - `GITHUB_TOKEN` least privilege by default
  - pin third-party actions to SHAs
  - restrict secrets exposure and protect reusable workflows

---

## Documentation

All official documentation lives under `docs/` and is organized by purpose:

- `docs/standards/` — protocols & standards
- `docs/templates/` — governed Markdown templates
- `docs/governance/` — higher-level policy docs
- `docs/stories/` (or `docs/reports/<topic>/story_nodes/`) — Story Nodes
- `docs/api/` — API docs + contract extensions
- `docs/ci/` — validation procedures and checklists
- `docs/reference/` — external references curated for KFM

Documentation quality expectations:
- Use tables, task lists, callouts, Mermaid, and collapsible details appropriately.
- Pass markdown lint, structure/schema validation, link checks, and sensitivity/accessibility scans.

<details>
<summary><strong>Glossary (selected)</strong></summary>

- **Governed document**: Markdown that follows an approved template and passes governance + CI validation.
- **Provenance linkages**: explicit references to datasets/docs/commits that substantiate claims.
- **FAIR/CARE**: data governance principles (Findable/Accessible/Interoperable/Reusable + Collective Benefit/Authority to Control/Responsibility/Ethics).
- **Story Node**: narrative Markdown driving Focus Mode UI with evidence linking.
- **Focus Mode**: read-only UI mode presenting story content + related evidence, with grounded Q&A.

</details>

---

## License

KFM commonly separates licensing for:
- **Code** (often MIT)
- **Docs/Data** (often CC-BY)

> [!NOTE]
> Verify the authoritative licenses in the repository root (e.g., `LICENSE`, `LICENSE-DATA`, `LICENSE-DOCS`) and follow any dataset-specific license terms recorded in manifests.

---

## Support

- Use the repo’s issue tracker for bugs, requests, and proposals.
- For sensitive data concerns (CARE / sovereignty / restricted locations), follow governance escalation procedures in `docs/governance/`.

---