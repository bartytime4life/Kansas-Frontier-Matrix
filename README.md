---
title: "Kansas Frontier Matrix — Repository README"
path: "README.md"
version: "v1.0.6"
last_updated: "2025-12-29"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:readme:v1.0.6"
semantic_document_id: "kfm-readme-v1.0.6"
event_source_id: "ledger:kfm:doc:readme:v1.0.6"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Kansas Frontier Matrix — Repository README

Kansas Frontier Matrix (KFM) is an open-source **geospatial + historical** knowledge system (a “living atlas” of Kansas) that ingests heterogeneous sources, publishes governed metadata catalogs (**STAC/DCAT/PROV**), builds a semantically structured **Neo4j graph**, and serves evidence through **contracted APIs** into a **map + narrative UI**. KFM is designed so that **every narrative claim can be traced to versioned evidence**, and every derived product has explicit lineage.

> **Non-negotiable discipline:** no new narrative without sources; no new data without provenance; no user-facing AI without explicit opt-in + uncertainty metadata; no UI access that bypasses contracted APIs.

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

**API boundary (non‑negotiable):** The UI never reads Neo4j directly; all access is via contracted APIs.

**Repo hygiene invariant:** KFM enforces “one canonical home per subsystem” and “one source of truth” for schemas/contracts/docs to reduce drift; avoid ad‑hoc folders outside canonical roots.

Quick navigation:
- `docs/MASTER_GUIDE_v12.md` (pipeline + invariants)
- `docs/templates/` (governed templates)
- `data/` (raw/work/processed + evidence catalogs)
- `src/` (pipelines + graph + API boundary)
- `web/` (UI; map + Focus Mode)

---

## 📘 Overview

### Purpose

- Provide a single entry point for contributors and readers to understand:
  - what KFM is,
  - the canonical pipeline ordering and non‑negotiables,
  - where artifacts live across the pipeline,
  - and which governance/validation constraints must not be broken.
- Preserve an evidence-first workflow where downstream views (including Focus Mode narrative) remain traceable back to catalogs and provenance.

### Scope

| In Scope | Out of Scope |
|---|---|
| Repository orientation; canonical pipeline; directory layout; contribution pointers; governance/validation invariants | Full subsystem implementations; deployment specifics; domain-specific dataset documentation (see domain READMEs + subsystem docs) |

### Audience

- Primary: maintainers and contributors (ETL, catalogs, graph/ontology, API, UI, narrative).
- Secondary: reviewers (governance/ethics/sovereignty), historians/editors, external collaborators.

### Definitions

- Glossary: `docs/glossary.md` (*not confirmed in repo* — add/repair link if glossary lives elsewhere)

Core terms used in this README:

- **Domain pack**: the minimal governed components that let a domain participate end-to-end (staging + transforms + catalogs + graph mappings + tests + docs).
- **Contract artifact**: machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
- **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived evidence products).
- **Story Node**: a governed narrative artifact that is machine‑ingestible and provenance‑linked.
- **Focus Mode**: a UI experience that consumes only provenance‑linked context bundles (no unsourced narrative).
- **Contract-first**: schemas + API contracts are first‑class artifacts; breaking changes require versioning + compatibility tests.
- **Deterministic pipeline**: idempotent, config-driven transforms with logged inputs/outputs and stable IDs.
- **Sensitivity propagation**: no derived output can be less restricted than any input in its lineage.

### Quick links (recommended reading order)

Treat any missing paths as *not confirmed in repo* and repair per repo hygiene:

1) `docs/MASTER_GUIDE_v12.md` (system + pipeline source of truth)  
2) `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`  
3) `docs/templates/TEMPLATE__STORY_NODE_V3.md`  
4) `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`  
5) Domain module READMEs under `docs/data/**` and/or `data/**` (when present)  
6) Architecture/roadmap docs under `docs/architecture/**` (when present)

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants + extension points |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Narrative + Focus Mode surfacing |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | REST/GraphQL contract changes |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Draft proposal; treat as “if adopted” (*not confirmed in repo*) |
| Next stages blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Architecture | Roadmap + gap closure plan (*not confirmed in repo*) |
| Full architecture vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture | End-to-end vision (*not confirmed in repo*) |
| Land Treaties module | `docs/data/historical/land-treaties/README.md` | Domain steward | Example domain module (governance-sensitive; *not confirmed in repo*) |
| Air Quality module | `docs/data/air-quality/README.md` | Domain steward | Example domain module (*not confirmed in repo*) |
| Soils (SDA) module | `data/soils/sda/README.md` | Domain steward | Example domain module (*not confirmed in repo*) |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |
| Repo structure standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | Docs | *not confirmed in repo* |

### Project reference library (optional; project PDFs)

These project files are **supporting references** (background, implementation notes, or design discussion). They should not be treated as authoritative over the Master Guide + templates unless incorporated into governed docs.

- System + scope + roadmap (KFM-specific)
  - `Kansas Frontier Matrix_ System Structure and Scope.pdf`
  - `Kansas Frontier Matrix (KFM) Implementation Guide.pdf`
  - `Kansas Frontier Matrix (KFM) System – Visual and Functional Overview.pdf`
  - `Expanding the Kansas Frontier Matrix Knowledge Base.pdf`
  - `Expanding the Kansas Frontier Matrix: External Data, Tools, and Frameworks.pdf`
  - `Elevating the Kansas Frontier Matrix: Gaps and Proposed Enhancements.pdf`
  - `KFM Reference Data.pdf`

- Templates (source exports / working docs)
  - `Universal Markdown templates.docx`
  - `TEMPLATE__KFM_UNIVERSAL_DOC.md.docx`
  - `TEMPLATE__STORY_NODE_V3.md.docx`
  - `TEMPLATE__API_CONTRACT_EXTENSION.md.docx`
  - `MASTER_GUIDE_v12.md.pdf`
  - `MASTER_GUIDE_v13.md.gdoc` (*not confirmed in repo / access varies*)

- Markdown & documentation practice
  - `Comprehensive Guide to Markdown in Programming and Documentation.pdf`
  - `The Comprehensive Markdown Guide.pdf`

- Geospatial + spatial analysis
  - `geoprocessing-with-python.pdf`
  - `KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf`
  - `An Introduction to Spatial Data Analysis and Visualisation in R - An Introduction to Spatial Data Analysis in R.pdf`
  - `graphical-data-analysis-with-r.pdf`

- Data science / stats / ML (for evidence artifacts and uncertainty)
  - `KFM- Understanding Statistics & Experimental Design.pdf`
  - `KFM-regression-analysis-with-python.pdf`
  - `KFM- Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf`
  - `KFM- Data Mining Concepts & applictions.pdf`
  - `KFM- Bayesian computational methods.pdf`
  - `KFM- Artificial-neural-networks-an-introduction.pdf`
  - `KFM- deep-learning-in-python-prerequisites.pdf`
  - `KFM- AI Foundations of Computational Agents 3rd Ed.pdf`

- Graph/geometry/optimization & simulation (advanced/optional)
  - `KFM- Spectral Geometry of Graphs.pdf`
  - `KFM- Generalized Topology Optimization for Structural Design.pdf`
  - `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
  - `KFM- Scalable Data Management for Future Hardware.pdf`

- UI / web / graphics
  - `CSS Notes for Professionals - CSSNotesForProfessionals.pdf`
  - `KFM-responsive-web-design-with-html5-and-css3.pdf`
  - `KFM-webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
  - `KFM- Computer Graphics using JAVA 2D & 3D.pdf`
  - `DesigningVirtualWorlds.pdf`

- Developer tooling / databases
  - `Git Notes for Professionals - GitNotesForProfessionals.pdf`
  - `Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf`
  - `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
  - `MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf`

### Contributing (high-level)

- **Docs:** use `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` for governed docs.
- **Story Nodes:** use `docs/templates/TEMPLATE__STORY_NODE_V3.md` and ensure every claim is source-linked.
- **API changes:** use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`; contract tests + redaction expectations are required.
- **Data domains:** add a vertical slice (raw → work → processed → STAC/DCAT/PROV → graph mapping → API → UI layer → at least one Story Node).

### Definition of done

- [ ] Front-matter complete + valid (`path: README.md`)
- [ ] H2 sections match the Universal template heading set (no extra H2 headings)
- [ ] Canonical pipeline + invariants stated clearly (pipeline order, API boundary, provenance rules)
- [ ] Canonical roots described; no new top-level “drift” encouraged
- [ ] Any repo path references are either verifiably present or explicitly marked *not confirmed in repo*
- [ ] Validation/CI expectations stated (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Footer refs preserved (governance + templates + architecture pointers)

---

## 🗂️ Directory Layout

### This document

- `path`: `README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Staged data + catalog outputs (STAC/DCAT/PROV) |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Templates | `docs/templates/` | Governed doc templates (universal/story/API) |
| Architecture | `docs/architecture/` | System designs, roadmaps, ADRs (if present) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators, utilities, QA scripts |
| CI | `.github/` | Workflows + policy gates |
| Releases | `releases/` | Versioned packaged artifacts (if used) |

Optional docs sub-roots (if adopted; keep one canonical home per concern):

- Standards: `docs/standards/`
- Security docs: `docs/security/` and/or `.github/SECURITY.md`
- Telemetry docs: `docs/telemetry/` with schemas under `schemas/telemetry/`
- Reference PDFs: `docs/library/` (*not confirmed in repo; recommended if project PDFs are committed*)

### Repo top-levels (expected)

~~~text
📁 .
├── 📄 README.md
├── 📁 .github/
│   ├── 📁 workflows/
│   └── 📄 SECURITY.md                         # if present
├── 📁 data/
│   ├── 📁 raw/
│   │   └── 📁 <domain>/
│   ├── 📁 work/
│   │   └── 📁 <domain>/
│   ├── 📁 processed/
│   │   └── 📁 <domain>/
│   ├── 📁 stac/
│   │   ├── 📁 collections/
│   │   └── 📁 items/
│   ├── 📁 catalog/
│   │   └── 📁 dcat/
│   └── 📁 prov/
├── 📁 docs/
│   ├── 📄 MASTER_GUIDE_v12.md
│   ├── 📁 templates/
│   │   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   │   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   │   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
│   ├── 📁 architecture/
│   │   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md
│   │   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md
│   │   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md
│   ├── 📁 data/
│   │   └── 📁 <domain>/
│   └── 📁 reports/
│       └── 📁 story_nodes/                    # pattern; draft/published split if defined
├── 📁 mcp/
│   ├── 📁 runs/
│   └── 📁 experiments/
├── 📁 schemas/
│   ├── 📁 stac/
│   ├── 📁 dcat/
│   ├── 📁 prov/
│   ├── 📁 story_nodes/
│   ├── 📁 ui/
│   └── 📁 telemetry/
├── 📁 src/
│   ├── 📁 pipelines/
│   ├── 📁 graph/
│   └── 📁 server/
├── 📁 web/
├── 📁 tests/
├── 📁 tools/
└── 📁 releases/
~~~

> Some directories may not exist yet. If a canonical root is missing, treat it as a gap and implement it per the Master Guide rather than introducing new top-level structure.

### Documentation map

- `docs/MASTER_GUIDE_v12.md` (system + pipeline source of truth)
- `docs/templates/` (document + MCP templates)
- `docs/architecture/` (designs/roadmaps; if present)
- `docs/reports/story_nodes/` (Story Nodes; draft/published split if defined)

---

## 🧭 Context

### Background

KFM’s design goal is an **evidence-first, provenance-linked** system where every downstream view (including narrative Focus Mode) remains traceable back to catalog and provenance artifacts.

As KFM scales to more domains and evidence products, it also hardens repository hygiene by enforcing **one canonical home per subsystem** and making **schemas/contracts** first-class artifacts.

### Assumptions

- Canonical pipeline ordering is preserved.
- Schemas/contracts are treated as first-class artifacts.
- Pipelines are deterministic, reproducible, and produce diffable outputs.

### Constraints and invariants

- **Pipeline ordering is non-negotiable:** **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- **API boundary is non-negotiable:** UI consumes contracted data via the API boundary only (no direct Neo4j dependency).
- **Evidence-first narrative:** no unsourced narrative in Story Nodes; Focus Mode is provenance-only.
- **Maintain one source of truth:** avoid duplicating schemas/contracts/docs across the repo; minimize redundancy to prevent drift.
- **One canonical home per subsystem:** do not introduce new top-level roots for convenience.
- **Contract-first versioning:** breaking changes require schema/contract version bumps and compatibility tests.
- **Sensitivity propagation:** no output can be less restricted than any input in its lineage.
- **No sensitive-location leakage:** for culturally sensitive materials, avoid publishing raw coordinates or re-identifying spatial precision; generalize/mask as required.
- **AI/predictive content constraints:** opt-in only, clearly labeled, includes uncertainty metadata, and must not infer or reveal sensitive locations.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which paths are currently implemented vs target layout? | TBD | TBD |
| Which staging model is canonical per domain: stage-first vs domain-pack? | TBD | TBD |
| Do legacy duplicate roots exist and what is the migration/deprecation plan? | TBD | TBD |
| Where is the canonical glossary located and is it complete? | TBD | TBD |
| Which CI validators exist today (Markdown protocol, schema lint, contract tests, link checks)? | TBD | TBD |
| Confirm Story Node publish workflow (`draft/` vs `published/`) and any legacy path. | TBD | TBD |
| Are domain naming conventions standardized (kebab-case vs snake_case)? | TBD | TBD |

### Future extensions

Use these “next-evolution extension points” to add capability without breaking contracts:

- **(A) Data:** new domain, new STAC extension profiles (if required)
- **(B) AI evidence:** analysis artifacts as STAC assets, linked into Focus Mode (with uncertainty metadata)
- **(C) Graph:** new entity types with explicit provenance + ontology mapping
- **(D) API:** new endpoints with contract tests + redaction rules
- **(E) UI:** new layer registry entries with provenance pointers + CARE gating

Readiness “vertical slice” expectation (recommended):

- one dataset → STAC/DCAT/PROV → graph ingest fixture → API endpoint → UI layer → one published Story Node

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  R["Raw sources — data/**"] --> A["ETL — src/pipelines/**"]
  A --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph (Neo4j)"]
  C --> D["API boundary — src/server (contracts + redaction)"]
  D --> E["UI — web/ (React + map + Focus Mode)"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked only"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j via src/graph)
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs (with redaction rules)
  Graph-->>API: context bundle + evidence references
  API-->>UI: contracted payload (citations + audit flags + sensitivity notices)
~~~

---

## 📦 Data & Metadata

### Inputs (staging model)

| Input | Typical content | Canonical location | Notes |
|---|---|---|---|
| Raw source snapshots | PDFs, CSVs, imagery, vectors, transcripts, etc. | `data/raw/<domain>/` | Immutable snapshots (prefer stable source IDs) |
| Intermediate transforms | Parsed text, normalized tables, reprojection outputs | `data/work/<domain>/` | Replaceable; should be reproducible |
| Processed outputs | Clean, join-ready datasets for publication | `data/processed/<domain>/` | Inputs to catalogs + graph ingest |
| Source manifests | source_id, provider, license, attribution | `data/sources/**` | Recommended (*not confirmed in repo*) |
| Run logs / manifests | inputs/outputs, code version, validation results | `mcp/runs/**` | Map to PROV Activities where possible |

### Outputs (boundary artifacts)

| Output | Format | Canonical location | Consumer(s) |
|---|---|---|---|
| STAC collections | JSON | `data/stac/collections/` | Catalog discovery, downstream linking |
| STAC items | JSON | `data/stac/items/` | Asset-level indexing + provenance pointers |
| DCAT datasets/distributions | JSON-LD | `data/catalog/dcat/` | Dataset discovery + federation |
| PROV bundles | JSON-LD / RDF | `data/prov/` | Lineage + auditability |
| Graph ingest fixtures/mappings | CSV/JSON/config | `src/graph/**` (+ `data/**` if used) | Neo4j graph build |
| API responses | JSON | `src/server/**` | UI + external consumers |
| UI layer registry | JSON (+ schema) | `web/**` + `schemas/ui/**` | Map layers + provenance links |
| Story Nodes | Markdown (+ schema) | `docs/reports/story_nodes/**` | Focus Mode narrative |

### Sensitivity and redaction

Public artifacts must not reveal restricted locations or culturally sensitive knowledge. Apply generalization/redaction at the earliest safe boundary:

- geometry generalization in catalog outputs when required,
- API-level redaction for sensitive fields and spatial precision,
- Story Node review gates before publication (especially for sensitive domains/assets).

### Quality signals

- STAC/DCAT/PROV validate against schemas in `schemas/**`.
- No orphan references: entity refs, evidence refs, and Story Node refs resolve.
- Deterministic runs and diffable outputs; stable IDs and versioned artifacts.
- Provenance is complete enough to answer: what changed, why, when, and by what process.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For each dataset/evidence product:

- STAC Collection + Item(s) exist and validate.
- Items reference assets and, where permitted, geometry; geometry may be generalized for public release.
- IDs are stable; versions are explicit.

### DCAT

- Each STAC Collection should map to a DCAT dataset record.
- Each publishable artifact/export bundle should map to a DCAT distribution record.
- DCAT records include license, description, keywords, and distribution access metadata.

### PROV-O

- PROV bundles describe lineage across raw → work → processed → catalog → graph ingest.
- Include:
  - `prov:Entity` for artifacts,
  - `prov:Activity` for pipeline runs and validation,
  - `prov:Agent` for tools and responsible parties.
- Prefer one PROV activity bundle per meaningful run under `data/prov/**`.

### Provenance requirements (minimum)

- `prov:wasDerivedFrom`: list source IDs
- `prov:wasGeneratedBy`: pipeline activity/run ID
- Confidence/uncertainty fields (if predictive content is included)

### Versioning

- IDs are stable; versions are explicit and machine-readable.
- Backward-incompatible changes require schema/contract version bumps.
- Catalogs and graph should link predecessor/successor versions where applicable.

---

## 🧱 Architecture

### Components

| Subsystem | Responsibility | Canonical home | Primary outputs |
|---|---|---|---|
| ETL / pipelines | Deterministic transforms | `src/pipelines/` | `data/work/**`, `data/processed/**`, run logs |
| Catalogs | Evidence metadata + discovery | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | STAC/DCAT/PROV bundles |
| Graph | Ontology-aligned knowledge graph | `src/graph/` | Neo4j-ready ingest + constraints |
| API boundary | Contracted access + redaction | `src/server/` | REST/GraphQL + audits |
| UI | Map + Focus Mode client | `web/` | Layer registry + narrative rendering |
| Story Nodes | Governed narratives | `docs/reports/story_nodes/` | Provenance-linked story artifacts |
| Focus Mode | Provenance-only deep dives | `web/` (UI) + `src/server/` (API) | Context bundles + citations |

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation notes | deterministic + replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated outputs |
| Graph | ontology + migrations + constraints | stable labels/edges (unless migrated) |
| APIs | OpenAPI/GraphQL schema + contract tests | backwards compatible or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story/Focus | provenance-linked context bundle | no hallucinated/unsourced claims |

### Canonical subsystem homes (one home per subsystem)

- Pipelines: `src/pipelines/`
- Catalog build/validation tooling: `tools/` and/or `src/pipelines/` (keep one canonical home)
- Graph build: `src/graph/`
- API boundary: `src/server/` (contracts under `src/server/contracts/**` if present)
- UI: `web/`

### Interfaces and contracts

- Governed docs: `docs/templates/**`
- JSON schemas: `schemas/**` (STAC, DCAT, PROV, story nodes, UI registries, telemetry)
- API contracts: `src/server/contracts/**` (or repo-defined equivalent; if different, *not confirmed in repo*)
- UI registries: schema-validated layer registries under `web/**` and `schemas/ui/**`

### Extension points checklist

For every new capability (dataset, domain, endpoint, UI layer, Story Node type):

- [ ] Add or update deterministic pipeline steps (`src/pipelines/**`)
- [ ] Produce/refresh STAC/DCAT/PROV evidence (`data/**`)
- [ ] Validate against schemas (`schemas/**`)
- [ ] Update graph mappings/fixtures (`src/graph/**`)
- [ ] Add/update API contracts + tests (`src/server/**`)
- [ ] Add/update UI registry entries (`web/**`)
- [ ] Add/update Story Node(s) with provenance-linked citations (`docs/reports/story_nodes/**`)
- [ ] Record telemetry signals + update schema if needed (`schemas/telemetry/**`)
- [ ] Add regression tests/validators and update release notes if applicable

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

Story Nodes must:

- carry provenance annotations and explicit citations to cataloged artifacts,
- connect to graph entities (Place/Person/Event/Document/etc.) via stable identifiers,
- separate **fact vs inference vs hypothesis** where applicable (especially for AI-generated text).

### Focus Mode rule (hard gate)

- Focus Mode only consumes **provenance-linked** content.
- Any predictive/suggestive content:
  - must be opt-in,
  - must carry uncertainty/confidence metadata,
  - must not infer or reveal sensitive locations.

### Focus Mode behavior expectations (UI + API)

- Map and timeline can narrow to the story’s scope.
- Only relevant layers should be enabled by default; unrelated layers are hidden/disabled.
- Citations must be rendered as first-class UI affordances (evidence is always one click away).
- Redaction/generalization must be visible via audit/disclosure affordances (never “silent”).

### Optional Focus Mode controls (Story Node-driven)

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Minimum CI gates

Recommended minimum checks:

- [ ] Markdown protocol validation (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers; “not confirmed in repo” used where appropriate)
- [ ] JSON schema validation:
  - STAC/DCAT/PROV
  - Story Node schemas (if present)
  - telemetry schemas (if present)
  - UI layer registry schemas (if present)
- [ ] Graph integrity tests (constraints, expected labels/edges)
- [ ] API contract tests (OpenAPI/GraphQL schema + resolver tests)
- [ ] UI layer registry schema checks
- [ ] Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Reproduction

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# 1) validate schemas (STAC/DCAT/PROV/story nodes/UI/telemetry)
# 2) run unit/integration tests
# 3) run doc lint / markdown protocol checks
# 4) run sovereignty/PII scans (where applicable)

# make validate-schemas
# make test
# make lint-docs
# make scan-governance
~~~

### Telemetry signals (recommended)

| Signal | Source | Where recorded |
|---|---|---|
| `classification_assigned` | pipeline + catalog | `docs/telemetry/` + `schemas/telemetry/` (*if present*) |
| `redaction_applied` | catalog + API | `docs/telemetry/` + `schemas/telemetry/` (*if present*) |
| `promotion_blocked` | CI governance gate | `docs/telemetry/` + `schemas/telemetry/` (*if present*) |
| `catalog_published` | catalog build | `docs/telemetry/` + `schemas/telemetry/` (*if present*) |
| `focus_mode_redaction_notice_shown` | UI audit affordance | `docs/telemetry/` + `schemas/telemetry/` (*if present*) |

### Release hardening (if `releases/` is used)

Recommended artifacts:

- SBOM (Software Bill of Materials)
- build provenance attestations (e.g., SLSA)
- signed manifests / versioned release bundles

---

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that typically require elevated review:

- Adding new sensitive layers (restricted locations, cultural knowledge, PII)
- Introducing/changing AI-generated narrative behavior visible to users
- Adding new external data sources (license/provenance review)
- Adding new public-facing endpoints
- Changing classification/sensitivity for any artifact
- Adding UI layers or interactions that could reveal sensitive locations by interaction/zoom

### CARE and sovereignty considerations

- Identify communities impacted and protection rules.
- Use generalization/redaction for restricted locations.
- Ensure sensitive assets (images/docs) follow review gates before publication.
- Redaction/generalization must be documented and enforced:
  - in datasets (`data/processed/**`),
  - in catalogs (STAC/DCAT),
  - in API responses (redaction policies),
  - and in UI rendering (CARE gating).

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not infer or generate sensitive locations.
- User-facing AI outputs must remain evidence-led, provenance-linked, and clearly labeled.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial repository README in governed-doc format | TBD |
| v1.0.1 | 2025-12-23 | Added repo navigation + clarified canonical roots/CI behavior | TBD |
| v1.0.2 | 2025-12-24 | Added architecture pointers; clarified data layout options; tightened doc/code separation | TBD |
| v1.0.3 | 2025-12-26 | Clarified staging vs domain-pack patterns; added provenance/run-pointer guidance | TBD |
| v1.0.4 | 2025-12-27 | Aligned sections and subheadings to Universal template; synced directory roots to Master Guide v12 inventory; normalized Data & Metadata and STAC/DCAT/PROV subsections | TBD |
| v1.0.5 | 2025-12-29 | Synced README language and file tree to Master Guide v12; consolidated Story Node/Focus Mode guidance under Architecture; tightened “one source of truth” + link-check expectations | TBD |
| v1.0.6 | 2025-12-29 | Added missing Universal-template H2 (`🧠 Story Node & Focus Mode Integration`); normalized directory layout + subsystem contracts; expanded project reference library | TBD |

---

Footer refs (do not remove):
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Next stages blueprint: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Full architecture vision: `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API Contract Extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`