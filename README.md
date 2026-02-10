# 🗺️ Kansas Frontier Matrix (KFM)

> **Governed, evidence-first geospatial + historical knowledge system** for Kansas:  
> **data → pipeline → APIs → maps/stories → Focus Mode (auditable AI)**

![Governance](https://img.shields.io/badge/Governance-Governed-2b6cb0)
![Evidence-first](https://img.shields.io/badge/Principle-Evidence--First-2f855a)
![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%20%2B%20CARE-805ad5)
![Clean Architecture](https://img.shields.io/badge/Architecture-Clean%20Layers-4a5568)
![Trust membrane](https://img.shields.io/badge/Security-Trust%20Membrane-c05621)
![Policy](https://img.shields.io/badge/Policy-Fail--Closed%20Validation-1f2937)
![Status](https://img.shields.io/badge/Status-Governed%20Blueprint-6b7280)

---

> [!IMPORTANT]
> **Status note:** This README describes the **intended** KFM architecture and governance behaviors.  
> If any repo paths, ports, or service names differ, treat this as the **governed baseline** and update it to match the repository’s actual implementation (without inventing features).

---

## Table of contents

- [What KFM is](#what-kfm-is)
- [Core principles](#core-principles)
- [Scope and non-goals](#scope-and-non-goals)
- [Quickstart](#quickstart)
  - [Run with Docker Compose](#run-with-docker-compose)
  - [Build and run from source](#build-and-run-from-source)
  - [Configuration](#configuration)
- [Architecture at a glance](#architecture-at-a-glance)
- [Repo layout](#repo-layout)
- [Governed data pipeline](#governed-data-pipeline)
  - [Dataset identity and provenance](#dataset-identity-and-provenance)
  - [Minimum metadata requirements](#minimum-metadata-requirements)
- [Story Nodes and Focus Mode](#story-nodes-and-focus-mode)
- [Validation and CI gates](#validation-and-ci-gates)
- [Security](#security)
- [Contributing](#contributing)
- [Documentation](#documentation)
- [License](#license)
- [Support](#support)

---

## What KFM is

KFM is a **monorepo** that co-evolves **code, datasets, and governed narratives** in one versioned history—so the repository itself acts like a **traceable “data lake”** where lineage can be inspected via commits and metadata.

KFM is designed to support:

- **Interactive maps** (React + MapLibre) and time-aware exploration (timeline/layer controls).
- **A governed backend API** (FastAPI or equivalent) that mediates all data access and enforces policies.
- **Multiple governed stores** for different access patterns:
  - **PostgreSQL + PostGIS** for spatial-relational queries
  - **Neo4j** for knowledge-graph relationships
  - **Search + semantic retrieval** (OpenSearch/Elasticsearch and/or a vector index)
- **Story Nodes**: Markdown-driven interactive narratives with strict structure + citations.
- **Focus Mode**: a Q&A assistant that is **grounded in KFM’s own evidence** and returns **cited answers**.

> [!IMPORTANT]
> **KFM is “evidence-first.”** Any user-visible claim—map layer metadata, story narrative statements, and AI answers—should be traceable to data sources via **metadata and provenance** (e.g., DCAT/STAC/PROV + citations).

---

## Core principles

### ✅ Evidence-first by design
- Dataset dialogs and Focus Mode include an **Audit** view that surfaces provenance chains.
- Story Nodes require **citations for factual claims** and are validated in CI.
- Data cannot surface to UI/API unless it has:
  - a stable dataset ID,
  - a provenance chain,
  - a license/rights statement,
  - and passed validators.

### ✅ Clean architecture boundaries
KFM follows clean-layer separation to keep core rules stable while swapping infrastructure:

- **Domain**: pure entities/models (no DB/UI deps)
- **Use Case / Services**: workflows & business logic (depends only on interfaces)
- **Integration / Interfaces**: ports/contracts (repository interfaces, policy contracts)
- **Infrastructure**: PostGIS/Neo4j/search, FastAPI routers, React UI, CI/CD, containers

### ✅ Trust membrane
Frontend and external clients **never** access databases directly.  
All access flows through the governed API layer so that permissions, provenance, and policy checks stay centralized.

> [!CAUTION]
> **Rule:** “No direct DB access from UI” is not just style—it is a **governance boundary**. Any bypass breaks auditability.

---

## Scope and non-goals

**In scope**
- Governed ingestion, validation, lineage, and publishing of spatial/historical datasets.
- Story Nodes with citations, dataset references, and UI choreography.
- Focus Mode grounded Q&A with auditable citations and logs.

**Out of scope (by default)**
- Uncited narrative claims.
- “Open internet” answers inside Focus Mode (unless explicitly designed as a separate, clearly labeled mode).
- Exposing culturally restricted knowledge or precise sensitive locations without governance review.

---

## Quickstart

> [!NOTE]
> Docker Compose is the simplest local environment. If your repository uses different service names/ports, treat the values below as **defaults** and verify in your `docker-compose.yml` and `.env`.

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
| OpenSearch/Elasticsearch | `http://localhost:9200` |
| PostgreSQL/PostGIS | `localhost:5432` |

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

### Build and run from source

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

### Configuration

> [!IMPORTANT]
> Keep configuration in `.env` (local) and secret manager (CI/prod). **Never commit secrets.**

Suggested environment variables (examples; align to your implementation):

| Variable | Purpose | Example |
|---|---|---|
| `DATABASE_URL` | PostGIS connection | `postgresql://…` |
| `NEO4J_URL` | Neo4j bolt URI | `bolt://…` |
| `SEARCH_URL` | OpenSearch/ES base URL | `http://localhost:9200` |
| `KFM_POLICY_MODE` | policy enforcement mode | `enforced` / `warn` |
| `KFM_LOG_LEVEL` | log verbosity | `INFO` |
| `KFM_DATA_ROOT` | data root path | `./data` |

---

## Architecture at a glance

```mermaid
flowchart LR
  UI[React + MapLibre UI] -->|HTTP (governed)| API[Backend API (governed gateway)]

  subgraph Stores[Governed stores]
    PG[(PostgreSQL + PostGIS)]
    N4J[(Neo4j Knowledge Graph)]
    SRCH[(OpenSearch/Elasticsearch + Vector Index)]
    OBJ[(Files/Tiles/Object storage)]
  end

  API --> PG
  API --> N4J
  API --> SRCH
  API --> OBJ

  subgraph Gov[Governance controls]
    POL[Policy engine + rules]
    PROV[Provenance + lineage (PROV/DCAT/STAC)]
    AUD[Audit logs]
  end

  API --> POL
  API --> PROV
  API --> AUD
```

Key operational rule:
- **UI never talks to stores directly**; all queries go through the API boundary.

---

## Repo layout

> [!NOTE]
> The structure below is the **recommended** governed layout. If your repo differs, keep the same *concepts* and reflect actual paths.

```text
.
├── backend/                        # Backend app (clean architecture layers)
│   ├── domain/                     # Core entities/models (no DB/UI deps)
│   ├── services/                   # Use-cases / workflows / business logic
│   ├── interfaces/                 # Ports/contracts (repositories, policy interfaces)
│   ├── adapters/                   # Concrete integrations (DB/graph/search implementations)
│   └── api/                        # Routers/controllers (HTTP endpoints)
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
│   ├── templates/                  # Approved templates (Universal Doc, Story Node v3, API contract)
│   ├── governance/                 # ROOT_GOVERNANCE, ETHICS, SOVEREIGNTY, etc.
│   ├── stories/                    # Story Nodes
│   ├── api/                        # API docs, contract extensions
│   ├── ci/                         # Validation procedures, checklists
│   └── reference/                  # Curated external references
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

  META --> API[Backend API]
  PROV --> API
  API --> UI[UI + Focus Mode]
```

### Dataset identity and provenance
- Every dataset has a **stable identifier** used across catalog, graph, stories, and citations  
  (example: `kfm:hydrology:rivers_v1`).
- Every raw dataset includes a **manifest** capturing provenance context (source, acquisition date, checksum, license, etc.).
- Every processed dataset has PROV linking **inputs → transform activity → outputs**.

> [!IMPORTANT]
> **No dataset should appear in the UI/API without a provenance chain.**  
> If metadata is missing, the pipeline should **fail closed**.

### Minimum metadata requirements

A dataset is considered “publishable” (eligible for API/UI) only if all are true:

- [ ] **Stable dataset ID** exists and is referenced consistently
- [ ] **Raw immutability**: raw file(s) stored unchanged with checksums
- [ ] **License/rights** declared (dataset-level + file-level if needed)
- [ ] **PROV lineage** includes inputs, transforms, outputs
- [ ] **Catalog entry** exists (DCAT and/or STAC as appropriate)
- [ ] **Sensitivity review** passed (CARE / restricted locations / PII / culturally restricted info)
- [ ] **Schema validation** passed (geometries, CRS, attribute types, required fields)
- [ ] **Link checks** pass (story citations, dataset references, media links)

Example: minimal raw ingest manifest (illustrative)

```yaml
# data/raw/<domain>/<dataset_id>/manifest.yml
dataset_id: "kfm:example:dataset_v1"
title: "Example Dataset"
source:
  name: "Authoritative Source Name"
  url: "https://example.org/source"   # include only if allowed
  acquired_at: "2026-02-10"
license:
  spdx: "CC-BY-4.0"
checksums:
  - file: "input.zip"
    sha256: "<sha256>"
sensitivity:
  classification: "public"            # public | internal | restricted
  notes: "No PII; aggregated geometry."
```

> [!CAUTION]
> For culturally restricted or sensitive locations: **generalize/redact** by default and require governance approval before any precise geometry is published.

---

## Story Nodes and Focus Mode

### Story Nodes (governed narratives)
A Story Node is a curated narrative designed to *drive* the UI:

- Written in **Markdown** with required sections and citations.
- Paired with a structured “map choreography” configuration (front-matter or adjacent JSON/YAML)
  for steps (center/zoom/layers/time slice).
- Stored in the repo (commonly under `docs/stories/`).

Typical Story Node CI checks:
- Structure matches Story Node Template v3 (Overview, Steps, Conclusion, etc.).
- Citations present for substantive factual claims.
- Media references exist and include alt text.
- Dataset IDs referenced in the story exist in the catalog and have provenance chains.

### Focus Mode (auditable Q&A)
Focus Mode is a conversational assistant integrated into the KFM UI:

- **Grounded only in KFM’s knowledge base** (no open internet by default).
- Uses retrieval from catalog/graph/search to assemble context.
- Returns answers with **clickable citations** and logs interactions for audit.
- Can run a **local LLM** (e.g., via Ollama) for privacy and offline deployments.

> [!CAUTION]
> If a user requests sensitive location details or culturally restricted knowledge, the system must:
> 1) **generalize/redact**, and  
> 2) route the request for **governance review** (policy workflow).

---

## Validation and CI gates

KFM treats **code, data, and docs** as governed artifacts. CI should enforce:

| Gate | What it checks | Fail behavior |
|---|---|---|
| Markdown lint + link check | story/docs structure, working refs, alt text | **Fail closed** |
| Story Node schema validation | required headings/fields/citations | **Fail closed** |
| Dataset manifest validation | required fields, checksum format | **Fail closed** |
| PROV validation | lineage completeness, valid references | **Fail closed** |
| STAC/DCAT validation | required metadata + stable IDs | **Fail closed** |
| Data quality checks | CRS, geometry validity, required columns | **Fail closed** |
| Sensitivity checks | PII/restricted location flags, CARE notes | **Fail closed** |
| API contract tests | response shapes, error contracts | **Fail closed** |

<details>
<summary><strong>Suggested local “preflight” checklist</strong></summary>

- [ ] Run unit tests (backend)
- [ ] Run contract tests (backend ↔ UI expectations)
- [ ] Run doc/story validators
- [ ] Run dataset validators (manifest/STAC/DCAT/PROV)
- [ ] Run dependency vulnerability scan (baseline)
- [ ] Confirm no secrets in git diff

</details>

---

## Security

> [!IMPORTANT]
> KFM’s repo security should assume a modern DevSecOps baseline (branch protections + secret scanning + least-privilege CI).

Recommended practices:
- Protect `main` with required reviews + required status checks.
- Require signed commits for critical branches/tags.
- Enable secret scanning + push protection.
- Use dependency updates + code scanning.
- Harden CI:
  - `GITHUB_TOKEN` least privilege by default
  - pin third-party actions to SHAs
  - restrict secrets exposure
  - isolate deployments with environment protections

<details>
<summary><strong>Threat model quick note</strong></summary>

Common risks KFM should explicitly defend against:

- **Provenance bypass**: data appears in UI/API without lineage or license.
- **Trust membrane break**: UI or external client accesses DB directly.
- **Prompt/data injection**: malicious text in sources that influences Focus Mode output.
- **Sensitive location exposure**: precise coordinates leaked via narratives or Q&A.
- **Supply chain**: compromised dependencies/actions.

Mitigations: fail-closed gates, strict API boundary, allowlist retrieval sources, output redaction policies, signed/verified builds.

</details>

---

## Contributing

KFM treats **code, data, and docs** as first-class governed artifacts.

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
- [ ] STAC/DCAT metadata added/updated (as appropriate)
- [ ] PROV lineage record added/updated
- [ ] Validators pass (schema checks, link checks, policy checks)

#### Story Nodes / docs
- [ ] Uses the correct template (Story Node v3 / Universal Doc / API contract extension)
- [ ] All substantive claims have citations
- [ ] Links and images resolve; images include alt text
- [ ] Markdown lint passes; document renders cleanly

---

## Documentation

All official documentation should live under `docs/` and be organized by purpose:

- `docs/standards/` — protocols & standards
- `docs/templates/` — governed Markdown templates
- `docs/governance/` — higher-level policy docs
- `docs/stories/` — Story Nodes
- `docs/api/` — API docs + contract extensions
- `docs/ci/` — validation procedures and checklists
- `docs/reference/` — curated external references used by KFM

Documentation quality expectations:
- Use tables, task lists, callouts, Mermaid, and collapsible details appropriately.
- Pass markdown lint, structure/schema validation, link checks, and sensitivity/accessibility scans.

<details>
<summary><strong>Glossary (selected)</strong></summary>

- **Governed document**: Markdown that follows an approved template and passes governance + CI validation.
- **Provenance linkages**: explicit references to datasets/docs/commits that substantiate claims.
- **FAIR/CARE**: data governance principles (Findable/Accessible/Interoperable/Reusable + Collective Benefit/Authority to Control/Responsibility/Ethics).
- **Story Node**: narrative Markdown driving UI with evidence linking.
- **Focus Mode**: read-only UI mode presenting story content + related evidence, with grounded Q&A.

</details>

---

## License

KFM commonly separates licensing for:
- **Code** (often MIT)
- **Docs/Data** (often CC-BY)

> [!NOTE]
> Verify authoritative licenses in the repository root (e.g., `LICENSE`, `LICENSE-DATA`, `LICENSE-DOCS`) and follow any dataset-specific license terms recorded in manifests.

---

## Support

- Use the repo’s issue tracker for bugs, requests, and proposals.
- For sensitive data concerns (CARE / sovereignty / restricted locations), follow governance escalation procedures in `docs/governance/`.

---

<sub>Footnote: GitHub supports Mermaid diagrams and callout blocks like `> [!NOTE]` in GitHub-flavored Markdown on most surfaces (README, issues, PRs). If your rendering target differs, adapt accordingly.</sub>