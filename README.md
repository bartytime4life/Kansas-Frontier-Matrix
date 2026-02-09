# Kansas Frontier Matrix (KFM)

> **A provenance-first geospatial knowledge system for Kansas.**  
> KFM integrates maps, data, historical narratives, and AI-assisted analysis using a governed  
> **Raw → Processed → Catalog/Provenance → Databases → API → UI/AI** architecture, so every map, story, and answer is traceable to sources.

[![CI](https://img.shields.io/badge/CI-gated-success)](#ci--quality-gates)
[![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-6f42c1)](#fair--care--governance-operations)
[![Provenance](https://img.shields.io/badge/provenance-STAC%20%2B%20DCAT%20%2B%20PROV-0b7285)](#governed-artifacts-registry)
[![Accessibility](https://img.shields.io/badge/docs-accessibility-ALT%20%7C%20Headings%20%7C%20Tables-2ea44f)](#documentation-as-a-governed-artifact)
[![License](https://img.shields.io/badge/License-see%20LICENSE-blue)](#license)
[![Cite](https://img.shields.io/badge/Cite-CITATION.cff-informational)](#citation)

---

## Start here

### Canonical documentation (governed)
> [!IMPORTANT]
> These are **the first links** for onboarding and compliance. If paths differ in your repo, update either this README or the Master Guide so there is **one source of truth**.

- **Master guide (architecture + governance source of truth):** `docs/MASTER_GUIDE_v13.md`
- **Markdown rules (governed docs standard):** `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- **AI assistance rules (governed usage + disclosure):** `docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md`
- **PR checklist (CI expectations + gates):** `docs/ci/checklists/PR_CHECKLIST.md`
- **Reference library (reading + standards index):** `docs/reference/REFERENCE_LIBRARY.md`

### Quick navigation
- [What KFM is](#what-kfm-is)
- [Core principles](#core-principles)
- [Architecture overview](#architecture-overview)
- [Quickstart (Docker Compose)](#quickstart-docker-compose)
- [Local validation checklist](#local-validation-recommended-before-pr)
- [FAIR + CARE operations](#fair--care--governance-operations)
- [Governed artifacts registry](#governed-artifacts-registry)
- [CI & quality gates](#ci--quality-gates)
- [Troubleshooting](#troubleshooting)

---

## Documentation as a governed artifact

KFM documentation is treated as a **governed artifact** with explicit requirements:

- **FAIR + CARE expectations** (including culturally sensitive handling and review flags)
- **Accessibility checks**: descriptive alt text, valid heading hierarchy, proper table headers
- **Local workflow tips**: run `pre-commit`, preview Markdown, verify links before PR
- **Version history updates** for non-trivial changes

> [!NOTE]
> If you change meaning, policy, data contracts, or public narratives: treat the doc update as a governed change that must pass validation and review.

---

## What KFM is

KFM is designed as a **trustworthy, auditable geospatial + historical knowledge system**:

- **Pipeline-first:** raw sources are transformed deterministically into processed datasets.
- **Catalog-first:** every published dataset produces **STAC + DCAT + PROV** records before it becomes visible in the UI/AI.
- **Governed delivery:** the UI and external clients access data **only through the API trust membrane** (never by querying databases directly).
- **Narratives as artifacts:** Story Nodes are versioned, machine-ingestible Markdown narratives with evidence linkages.
- **Focus Mode:** a read-only experience that presents curated Story Nodes with map/timeline context and provenance-backed content only.

### What KFM is not
- Not a “direct DB query” app: clients do not bypass the API layer.
- Not a free-form wiki: documentation and narratives are governed artifacts with templates + validation gates.
- Not “best-effort provenance”: missing metadata/lineage **fails closed**.

---

## Core principles

### Provenance-first (“the map behind the map”)
Every user-facing output (layer, story, chart, AI answer) must be traceable to sources via catalogs and lineage logs.

### Deterministic truth path (fail-closed)
Data must flow through the canonical stages **with no shortcuts**:

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`
- plus boundary artifacts: `data/stac/`, `data/catalog/dcat/`, `data/prov/`

If required metadata or provenance is missing, the item is **not publishable**.

### Trust membrane (no bypasses)
> [!IMPORTANT]
> - **Frontend and external clients never access databases directly.**
> - **Backend core logic never bypasses repository interfaces to talk directly to storage.**
> - Every request/response passes governance checks at the API gateway (“trust gate”).

### Contract-first interfaces
APIs, schemas, and templates are first-class versioned artifacts. Breaking changes require explicit versioning and compatibility review.

### FAIR + CARE
KFM aims to be **Findable, Accessible, Interoperable, Reusable** while honoring **Collective Benefit, Authority to Control, Responsibility, Ethics**—especially for sensitive or sovereignty-relevant content.

---

## Architecture overview

KFM follows a **Clean Architecture** layering model:

| Layer | Responsibility | Examples |
|---|---|---|
| **Domain** | Pure entities & core concepts (no DB/UI deps) | `LandParcel`, `HistoricalEvent`, `StoryNode` |
| **Use Case / Service** | Workflows + policies + orchestration | ingestion, validation, timeline generation |
| **Integration / Interface** | Ports + adapters (contracts for storage/APIs) | repository interfaces, API presenters |
| **Infrastructure** | Concrete tech | PostGIS, Neo4j, FastAPI, React/MapLibre, CI/CD |

---

## End-to-end system flow

```mermaid
flowchart LR
  subgraph Ingestion["📥 Ingestion & ETL (deterministic)"]
    raw["data/raw (immutable sources)"] --> work["data/work (intermediate/sandbox)"]
    work --> processed["data/processed (publishable outputs)"]
    processed --> stac["data/stac (STAC collections/items)"]
    processed --> dcat["data/catalog/dcat (DCAT JSON-LD)"]
    processed --> prov["data/prov (W3C PROV lineage)"]
  end

  stac --> stores["Storage: PostGIS + Neo4j (+ optional search/vector index)"]
  dcat --> stores
  prov --> stores

  stores --> api["FastAPI API (REST + optional GraphQL)"]
  api --> ui["React UI (MapLibre · optional Cesium)"]
  ui --> focus["Focus Mode: Story Nodes + evidence views"]


⸻

Repository layout (expected)

.
├── api/                     # Backend (FastAPI; clean architecture packages)
├── web/                     # Frontend (React + MapLibre)
├── data/
│   ├── raw/                 # Immutable sources (organized by domain/topic)
│   ├── work/                # Intermediate ETL artifacts (non-authoritative)
│   ├── processed/           # Publishable, cleaned datasets
│   ├── stac/                # STAC records (collections/items)
│   ├── catalog/
│   │   └── dcat/            # DCAT dataset entries (JSON-LD)
│   └── prov/                # PROV lineage logs
├── docs/                    # Governed documentation + narratives
├── policy/                  # Policy engine rules (OPA/Rego or equivalent)
├── .github/                 # CI/CD workflows
├── docker-compose.yml       # Local dev stack (db + api + ui + graph)
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
└── CITATION.cff

[!TIP]
If your repo uses different folder names (e.g., frontend/ instead of web/), keep interfaces + invariants the same—and document the divergence in the Master Guide.

⸻

Quickstart (Docker Compose)

Prerequisites
	•	Docker + Docker Compose
	•	Git
	•	Optional (for running outside containers): Python + Node.js

Run

git clone https://github.com/<ORG>/<REPO>.git
cd <REPO>

# if present
cp .env.example .env

docker-compose up --build

Services & ports (dev conventions — verify docker-compose.yml)

[!NOTE]
These are typical conventions from KFM’s blueprint docs. Always confirm the actual values in docker-compose.yml.

Component	Typical service name	Typical port(s)	Notes
Postgres + PostGIS	db	5432	Spatial relational store
Neo4j	graph	7474 (HTTP), 7687 (Bolt)	Knowledge graph store
FastAPI	api	8000	REST (and optionally GraphQL)
React UI	web	3000	Dev server or served build
OPA (optional)	opa	8181	Policy decision point (if enabled)

Verify
	•	FastAPI docs: http://localhost:8000/docs
	•	Optional health: http://localhost:8000/health
	•	React UI: http://localhost:3000
	•	Neo4j browser (if enabled): http://localhost:7474

[!WARNING]
Default dev credentials are for local development only. Use proper secrets management in staging/production.

⸻

Governed artifacts registry

KFM treats datasets, catalogs, narratives, and contracts as governed artifacts.

Artifact type	Where it lives	“Publishable” gate
Dataset (raw)	data/raw/...	source manifest + license + sensitivity fields
Dataset (processed)	data/processed/...	deterministic build + validation + provenance
STAC	data/stac/...	schema-valid + links to processed assets
DCAT	data/catalog/dcat/...	schema-valid + license/sensitivity fields
PROV	data/prov/...	lineage resolves to inputs/outputs (no gaps)
Story Node (narrative)	docs/stories/... or docs/reports/.../story_nodes/...	template-valid + citations + review gates
API contract	api/ + OpenAPI	versioned + reviewed + compatibility assessed

[!IMPORTANT]
Treat any analysis output (including AI-derived artifacts) as a first-class dataset:
it must live in data/processed/... and have STAC/DCAT/PROV before it can ship to UI/AI.

⸻

Working with data (the truth path)

Adding a new dataset (minimum checklist)
	•	Place immutable sources under data/raw/<domain>/ (+ manifest if required)
	•	Run deterministic ETL to produce data/processed/<domain>/...
	•	Generate boundary artifacts:
	•	STAC collection/item records (data/stac/...)
	•	DCAT dataset entry (data/catalog/dcat/...)
	•	PROV lineage record (data/prov/...)
	•	Ensure license + sensitivity fields are present (fail-closed)
	•	Run local validation (see below) and open a PR

⸻

Story Nodes & Focus Mode

Story Nodes are governed narrative artifacts designed to be rendered in the UI with map/timeline choreography.

A typical story includes:
	•	A Markdown narrative (text + citations)
	•	A binding artifact (JSON/YAML) linking sections to map state & time controls

See:
	•	docs/templates/TEMPLATE__STORY_NODE_V3.md
	•	docs/stories/ or docs/reports/<topic>/story_nodes/ (per Master Guide)

⸻

Local validation (recommended before PR)

[!IMPORTANT]
Do this before committing or opening a PR.

1) Run pre-commit (if configured)

pre-commit run --all-files

2) Documentation checks
	•	Preview Markdown (GitHub / VS Code)
	•	Verify internal links and references (no broken anchors/files)
	•	Confirm accessibility:
	•	Images include meaningful alt text
	•	Heading levels are well-formed (no skipping)
	•	Tables use header rows and remain readable in raw form
	•	Update Version History for non-trivial changes (if the doc includes it)

[!NOTE]
CI is authoritative; local checks reduce turnaround time and review churn.

⸻

CI & quality gates

KFM treats code, data, and documentation as governed artifacts.

Typical CI checks include:
	•	Backend tests (unit + integration)
	•	Frontend tests (where applicable)
	•	Markdown lint + structure validation + link checks + accessibility checks
	•	Policy checks for:
	•	required metadata fields (license/sensitivity)
	•	publishing gates for catalogs
	•	access controls and protected content rules
	•	secret scanning

⸻

FAIR + CARE & governance operations

Operational checklist (what to do, not just values)

If a dataset or narrative may be sensitive (e.g., culturally restricted info, sacred/vulnerable sites, endangered species nesting locations, vulnerable infrastructure):
	•	Do not publish precise coordinates (reduce resolution, generalize, or redact)
	•	Mark sensitivity explicitly in metadata (dataset + doc)
	•	Route for governance review (council/maintainers) before publication
	•	Minimize harm: publish only what’s necessary for collective benefit
	•	Record the decision: include rationale and redaction strategy in the governed doc

[!WARNING]
“Interesting” is not a justification for publication.
If it increases risk to people, places, or culturally protected knowledge, fail closed and escalate for review.

AI assistance disclosure

If AI assistance is used to draft or transform governed docs/narratives:
	•	Follow docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md
	•	Disclose AI involvement per protocol (where required by template/policy)

⸻

Contributing

See CONTRIBUTING.md.

Minimum expectations:
	1.	Make changes in a branch/fork.
	2.	Ensure data follows the truth path (raw → processed + catalogs + provenance).
	3.	Ensure docs follow KFM Markdown standards (tables, callouts, Mermaid, footnotes, collapsible details).
	4.	Open a PR; CI must pass; maintainers review for governance compliance.

[!IMPORTANT]
KFM contributions are expected to follow the Master Coder Protocol (MCP):
linting/formatting, test expectations, documentation updates, and architectural boundary compliance are required.

⸻

Troubleshooting

Common issues
	•	Port conflicts (5432/7474/7687/8000/3000):
	•	Stop conflicting services or change Compose port mappings.
	•	First-run database initialization:
	•	If migrations/seeds fail, rebuild volumes (⚠️ local dev only):

docker-compose down -v
docker-compose up --build


	•	UI can’t load data:
	•	Confirm API is healthy (/health if present)
	•	Confirm UI is pointing at the right API base URL
	•	Confirm policy gates aren’t denying requests (OPA logs if enabled)
	•	CI passes but local fails (or vice versa):
	•	Ensure you’re using the repo’s pinned tool versions (pre-commit, node/python versions)
	•	Re-run pre-commit run --all-files

⸻

Citation

KFM is designed to be citable. If present, use CITATION.cff for academic citations.

⸻

License

See LICENSE.

[!NOTE]
Some KFM deployments use split licensing (e.g., code vs. data). Confirm the intended licensing model in this repo.

⸻

Maintainers & contact
	•	Governance: docs/governance/ (if present)
	•	Issues: GitHub Issues

⸻

Verification steps (make this README “repo-true,” not just “blueprint-true”)

Use this quick sanity pass to align the README to the actual repo, not just the conceptual blueprint:
	•	Confirm these paths exist and match names:
	•	docs/MASTER_GUIDE_v13.md
	•	docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md
	•	docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md
	•	docs/ci/checklists/PR_CHECKLIST.md
	•	docs/reference/REFERENCE_LIBRARY.md
	•	Open docker-compose.yml and verify:
	•	service names (db, graph, api, web, opa if present)
	•	port mappings
	•	whether the frontend is a dev server vs served build
	•	Confirm whether pre-commit is configured; if not, remove the command but keep the local validation concept.

**Source files referenced (project artifacts):**  [oai_citation:0‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)  [oai_citation:1‡Kansas Frontier Matrix (KFM) System Implementation Guide.pdf](sediment://file_00000000fca871f890bb5ef3aa2e9a93)  [oai_citation:2‡Kansas Frontier Matrix (KFM) System Implementation Blueprint & Capabilities Guide.pdf](sediment://file_00000000bb9071f596e5cb45d384df0b)