# Kansas Frontier Matrix (KFM)

> **A provenance-first geospatial knowledge system for Kansas.**  
> KFM integrates maps, data, historical narratives, and AI-assisted analysis using a governed  
> **“pipeline → catalogs → databases → API → UI”** architecture so that every map, story, and answer is traceable back to sources.

<!-- Badges: replace placeholders with real repo URLs/workflow names -->
[![CI](https://img.shields.io/badge/CI-passing-brightgreen)](#ci--quality-gates)
[![License](https://img.shields.io/badge/License-see%20LICENSE-blue)](#license)
[![Cite](https://img.shields.io/badge/Cite-CITATION.cff-informational)](#citation)

---

## Table of contents

- [Start here](#start-here)
- [What KFM is](#what-kfm-is)
- [Core principles](#core-principles)
- [Architecture overview](#architecture-overview)
- [End-to-end system flow](#end-to-end-system-flow)
- [Repository layout](#repository-layout)
- [Quickstart](#quickstart)
- [Working with data](#working-with-data)
- [Story Nodes and Focus Mode](#story-nodes-and-focus-mode)
- [APIs](#apis)
- [CI and quality gates](#ci-and-quality-gates)
- [Security and governance](#security-and-governance)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)
- [Maintainers and contact](#maintainers-and-contact)
- [Glossary](#glossary)

---

## Start here

- **Architecture & governance (canonical):** `docs/MASTER_GUIDE_v13.md` *(not confirmed in repo — keep path synced to reality)*
- **System architecture docs:** `docs/architecture/` *(if present)*
- **Documentation standards (governed):** `docs/standards/` + **KFM Markdown Guide**
- **Templates:** `docs/templates/` *(if present; includes Universal Doc, Story Node v3, API contract extensions)*
- **Local dev:** see [Quickstart](#quickstart)

> [!NOTE]
> Some paths/endpoints below reflect the **canonical KFM blueprint**. If this repository diverges, update the README and/or the Master Guide so there is **one source of truth**.

---

## What KFM is

KFM is designed as a **trustworthy, auditable geospatial + historical knowledge system**:

- **Pipeline-first:** raw sources are transformed deterministically into processed datasets.
- **Catalog-first:** every publishable dataset produces **STAC + DCAT + PROV** records before it becomes visible in the UI.
- **Governed delivery:** the UI and external clients access data **only through the API “trust membrane”** (never by querying databases directly).
- **Narratives as artifacts:** Story Nodes are versioned, machine-ingestible Markdown narratives with evidence linkages.
- **Focus Mode:** a read-only experience that presents Story Nodes with map/timeline context and only provenance-linked content.

### What KFM is not

- A loose collection of scripts and ad-hoc maps.
- A system where “AI answers” can bypass evidence or provenance.
- A UI that directly connects to PostGIS/Neo4j (this is explicitly forbidden).

---

## Core principles

### Provenance-first

Every user-facing output (layer, story, chart, AI answer) must be traceable to sources via catalogs and lineage logs.

### Deterministic truth path (fail-closed)

Data must flow through the canonical stages **with no shortcuts**:

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`
- plus catalog outputs:
  - `data/stac/` (STAC collections/items)
  - `data/catalog/dcat/` (DCAT JSON-LD)
  - `data/prov/` (W3C PROV lineage)

If required metadata or provenance is missing, the item is not considered publishable.

### Trust membrane

> [!IMPORTANT]
> **Frontend (React/MapLibre) and external clients never access databases directly.**  
> **Backend core logic never bypasses repository interfaces to talk directly to storage.**  
> All access routes through governed contracts (API + policy checks).

### Contract-first interfaces

APIs, schemas, and templates are first-class versioned artifacts. Breaking changes require explicit versioning and compatibility review.

### FAIR + CARE

KFM aims to be **Findable, Accessible, Interoperable, Reusable** while also honoring **Collective Benefit, Authority to Control, Responsibility, and Ethics**—especially for sensitive or sovereignty-relevant content.

> [!WARNING]
> If a dataset or narrative contains culturally sensitive information or precise locations that should not be public, **do not publish raw coordinates**. Use redaction/generalization and flag for governance review.

---

## Architecture overview

KFM follows a **Clean Architecture** layering model:

| Layer | Responsibility | Examples |
|---|---|---|
| **Domain** | Pure entities & core concepts, no DB/UI code | `LandParcel`, `HistoricalEvent`, `StoryNode` |
| **Use Case / Service** | Business workflows, policies, orchestration | ingestion, validation, timeline generation |
| **Integration / Interface** | Ports + adapters (interfaces for storage/APIs) | repository interfaces, API presenters |
| **Infrastructure** | Concrete tech implementations | PostGIS, Neo4j, FastAPI, React/MapLibre, CI/CD |

> [!TIP]
> Clean Architecture is enforced by **dependencies**: inner layers must not import outer layers. Prefer interfaces/ports defined inward, implemented outward.

---

## End-to-end system flow

```mermaid
flowchart LR
  subgraph Ingestion["📥 Ingestion & ETL"]
    raw["data/raw (immutable sources)"] --> work["data/work (intermediate)"]
    work --> processed["data/processed (final outputs)"]
    processed --> stac["data/stac (STAC collections/items)"]
    processed --> dcat["data/catalog/dcat (DCAT JSON-LD)"]
    processed --> prov["data/prov (W3C PROV lineage)"]
  end

  stac --> storage["Storage: PostGIS + Neo4j (+ optional search/vector index)"]
  dcat --> storage
  prov --> storage

  storage --> api["API Gateway: FastAPI (REST + optional GraphQL)"]
  api --> ui["UI: React (MapLibre · optional Cesium)"]
  ui --> story["Story Nodes + Focus Mode"]
```

---

## Repository layout

A canonical KFM monorepo commonly includes:

```text
.
├── api/                     # Backend (FastAPI; clean architecture packages)
├── web/                     # Frontend (React + MapLibre)
├── data/
│   ├── raw/                 # Immutable sources (organized by domain/topic)
│   ├── work/                # Intermediate ETL artifacts (optional)
│   ├── processed/           # Published, cleaned datasets
│   ├── stac/                # STAC records (collections/items)
│   ├── catalog/
│   │   └── dcat/            # DCAT dataset entries (JSON-LD)
│   └── prov/                # PROV lineage logs
├── docs/                    # Governed documentation + narratives + templates
├── policy/                  # Governance policies (e.g., OPA/Rego, AI/data rules)
├── deploy/                  # (Optional) Kubernetes/Helm/etc.
├── .github/                 # CI/CD workflows
├── docker-compose.yml       # Local dev stack (db + api + ui + graph)
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
└── CITATION.cff
```

> [!NOTE]
> If your repository uses different folder names (e.g., `frontend/` instead of `web/`), keep the **interfaces and invariants** the same—and document the divergence in the Master Guide.

---

## Quickstart

### Prerequisites

- Docker + Docker Compose (v2 recommended: `docker compose ...`)
- Git
- Optional (for running outside containers): Python + Node.js

### Run

```bash
# 1) clone (replace URL with the real repo)
git clone https://github.com/<ORG>/<REPO>.git
cd <REPO>

# 2) configure environment (if provided)
cp .env.example .env  # if present

# 3) start the full stack
docker compose up --build
# (older installs may require: docker-compose up --build)
```

### Verify (default dev conventions)

- FastAPI docs: `http://localhost:8000/docs`
- (Optional) FastAPI health: `http://localhost:8000/health`
- React UI: `http://localhost:3000`
- Neo4j browser (if enabled): `http://localhost:7474`

### Stop and reset (development)

```bash
# stop containers
docker compose down

# reset volumes too (destructive; for local dev only)
docker compose down -v
```

> [!WARNING]
> Default dev credentials (e.g., `postgres/postgres`) are for local development only. Use proper secrets management in staging/production.

---

## Working with data

### Adding a new dataset

Minimum checklist (fail-closed publishing):

- [ ] Place immutable sources under `data/raw/<domain>/` with a manifest (if required by the domain)
- [ ] Run deterministic ETL to produce `data/processed/<domain>/...`
- [ ] Generate boundary artifacts:
  - [ ] STAC collection/item records (`data/stac/...`)
  - [ ] DCAT dataset entry (`data/catalog/dcat/...`)
  - [ ] PROV lineage record (`data/prov/...`)
- [ ] Ensure required governance metadata exists (license, sensitivity, provenance refs)
- [ ] Run local validation (if provided) and open a PR

> [!IMPORTANT]
> Treat any analysis output (including AI-derived artifacts) as a **first-class dataset**: it must live in `data/processed/...` and have STAC/DCAT/PROV records before it can appear in the UI.

### Publishing rule of thumb

If you can’t answer **“where did this come from?”** with a chain of links from UI → API → catalog → provenance → raw source, it’s not publishable.

---

## Story Nodes and Focus Mode

Story Nodes are governed narrative artifacts designed to be rendered in the UI with map/timeline choreography.

A typical story includes:

- A **Markdown narrative** (text + evidence/citations)
- A **map/timeline binding script** (JSON/YAML) that binds narrative sections to map state/timeline behavior *(if used in your deployment)*

See (if present):

- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/stories/` *(or `docs/reports/<topic>/story_nodes/` depending on Master Guide)*

### Story Node minimum expectations

- Evidence-first: major claims should be supported by citations or dataset/catalog IDs.
- Sensitivity-aware: redact/generalize as required; flag for governance review.
- Render-friendly: use structured Markdown (tables, callouts, footnotes) so Focus Mode can render reliably.

---

## APIs

KFM typically exposes:

- REST endpoints for core data access and UI needs
- Optional GraphQL for flexible querying (deployment-dependent)

### Contract rules

- API schemas are versioned artifacts.
- Breaking changes require:
  - explicit version bump,
  - compatibility notes,
  - contract tests updated.

> [!TIP]
> Treat API responses as “public knowledge artifacts”: stable, documented, and provenance-friendly.

---

## CI and quality gates

KFM treats code, data, and documentation as governed artifacts.

Typical CI checks include:

- Backend tests (unit + integration)
- Frontend tests (where applicable)
- Markdown lint + structure validation + link checks
- Policy checks (e.g., OPA) for:
  - required metadata fields (license/sensitivity)
  - citation/provenance requirements for generated answers (where enforced)
  - access controls and publishing gates
- Secret scanning

### PR definition of done (recommended)

- [ ] Architectural boundaries maintained (no UI→DB, no core→DB direct calls)
- [ ] Data changes follow truth path and include catalogs + provenance
- [ ] Docs follow KFM Markdown standards and templates
- [ ] CI green (tests, lint, policy, link check)
- [ ] Governance review completed for sensitive content (if applicable)

---

## Security and governance

### Policy enforcement

KFM’s governance membrane can include policy enforcement at:

- **runtime** (API middleware / gateway checks)
- **CI** (policy tests / fail-closed publishing gates)

Policies may cover:

- authentication & authorization
- dataset sensitivity rules
- AI response requirements (e.g., “must include citations”)
- publishing gates for catalogs

### Sensitivity handling

If a dataset or narrative contains culturally sensitive information or precise locations that should not be public:

- do not publish raw coordinates
- publish generalized geometry (e.g., coarse bounding boxes) or redacted representations
- document the decision and route for governance review

---

## Contributing

See `CONTRIBUTING.md`.

At a minimum:

1. Make changes in a branch/fork.
2. Ensure data follows the truth path (raw → processed + catalogs + provenance).
3. Ensure docs follow KFM’s Markdown standards (tables, callouts, Mermaid, etc. where appropriate).
4. Open a PR; CI must pass; maintainers review for governance compliance.

> [!NOTE]
> If you add a new template, schema, or API contract, treat it as a governed artifact: version it, document it, and include compatibility guidance.

---

## Citation

KFM is designed to be citable. If present, use `CITATION.cff` for academic citations.

---

## License

See `LICENSE`.

> [!NOTE]
> Some KFM deployments use split licensing (e.g., code vs. data). Confirm the intended licensing model in this repo.

---

## Maintainers and contact

- Project governance: see `docs/governance/` *(if present)*
- Issues: use GitHub Issues

---

## Glossary

| Term | Meaning in KFM |
|---|---|
| **Truth path** | The governed lifecycle from `data/raw` → `data/processed` + catalogs + provenance |
| **Trust membrane** | The enforced boundary: clients use the API; backend core uses repository interfaces |
| **Catalog-first** | Catalog metadata (STAC/DCAT/PROV) is required before exposure in UI |
| **Story Node** | Governed narrative artifact rendered in Focus Mode with evidence linkages |
| **Focus Mode** | Read-only, provenance-linked presentation mode (story + map/timeline context) |

---