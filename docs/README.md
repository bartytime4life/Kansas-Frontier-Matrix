---
title: "Docs — Kansas Frontier Matrix Documentation Index"
path: "docs/README.md"
version: "v1.0.2"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:docs:readme:v1.0.2"
semantic_document_id: "kfm-docs-readme-v1.0.2"
event_source_id: "ledger:kfm:doc:docs:readme:v1.0.2"
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

# Docs — Kansas Frontier Matrix Documentation Index

## 📘 Overview

### Purpose

- Provide a single entry point for navigating `docs/` (the canonical governed documentation area).
- Point contributors to the correct templates/standards before adding or changing documentation.
- Keep documentation **architecture-synced** with the system pipeline:

  **ETL → STAC/DCAT/PROV → Graph (Neo4j) → API → UI (React/Map) → Story Nodes → Focus Mode**

- Make drift explicit: if a path is referenced but missing, mark it **not confirmed in repo** and propose the correct canonical home.

### Read-first order

> This order aligns to the repo’s “contract-first” intent: read pipeline invariants first, then the standards/templates that govern new docs.

1) `README.md` (repo root) — canonical roots + CI behavior contract *(not confirmed in repo: create if missing)*  
2) `docs/README.md` (this document) — docs navigation + template/placement guidance  
3) `docs/MASTER_GUIDE_v12.md` — canonical pipeline ordering, invariants, system inventory *(not confirmed in repo: a PDF source exists in project references; convert to governed Markdown if needed)*  
4) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — v13 target roots + readiness gates *(draft; PDF source exists; Markdown not confirmed in repo)*  
5) `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` — end-to-end architecture & vision *(draft; PDF source exists; Markdown not confirmed in repo)*  
6) `docs/standards/` — KFM-MDP + STAC/DCAT/PROV profiles + ontology protocol *(some files may be placeholders; not confirmed in repo)*  
7) `docs/templates/` — governed templates (Universal, Story Node, API Contract Extension)  
8) `data/README.md` — domain-pack layout + catalog/provenance outputs *(not confirmed in repo: create if missing)*  
9) `src/README.md` — subsystem layout: pipelines / graph / server *(not confirmed in repo: create if missing)*  
10) `schemas/README.md` — schema registry for validation gates *(not confirmed in repo: create if missing)*  
11) `.github/workflows/README.md` — CI gates and how validation maps to subsystem roots *(not confirmed in repo: create if missing)*

### Template selection quick reference

| You are writing… | Use this template | Canonical destination |
|---|---|---|
| Guides, standards, architecture docs, runbooks | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | `docs/**` |
| Story Nodes / Focus Mode narratives | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | `docs/reports/story_nodes/**` |
| API contract changes / new endpoints | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | `src/server/contracts/**` (schema) + `docs/api/**` (notes) |

### Scope

| In Scope | Out of Scope |
|---|---|
| Where documentation lives and how it is organized | Full implementation details of pipelines, services, or UI |
| Which templates to use (Universal / Story Node / API Contract) | Debugging runtime failures / operations runbooks (unless governed and placed under `docs/`) |
| Docs-to-data linkage expectations (STAC/DCAT/PROV identifiers, provenance references) | Replacing the Master Guide or templates |
| Explicit handling of “target layout” vs “legacy drift” | Making up missing policies or file paths |

### Audience

- Primary: contributors authoring/maintaining documentation in `docs/`
- Secondary: engineers and reviewers working in ETL, catalogs, graph, API, UI, and story layers

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or update this link if the glossary lives elsewhere)*

Common terms used across docs:

- STAC, DCAT, PROV-O
- Neo4j graph
- Story Nodes
- Focus Mode
- Contract tests (API/UI)
- Deterministic ETL (idempotent, replayable)

### Key artifacts

> If a referenced artifact is missing, treat it as **not confirmed in repo** and either add it at the canonical location or update links here.

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repo README | `README.md` | TBD | Entry point; canonical roots + CI behavior contract *(not confirmed in repo)* |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline source of truth *(PDF source exists in project refs; Markdown not confirmed in repo)* |
| Redesign blueprint (v13) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Target roots + CI gates *(draft; PDF source exists; Markdown not confirmed in repo)* |
| Full architecture & vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | TBD | End-to-end architecture *(draft; PDF source exists; Markdown not confirmed in repo)* |
| Next stages planning | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | TBD | Roadmap + sequencing *(draft; PDF source exists; Markdown not confirmed in repo)* |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default governed doc template *(DOCX source exists; Markdown not confirmed in repo)* |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Narrative + Focus Mode surfacing *(DOCX source exists; Markdown not confirmed in repo)* |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | REST/GraphQL contract changes *(DOCX source exists; Markdown not confirmed in repo)* |
| Standards (protocols + profiles) | `docs/standards/` | TBD | KFM-MDP + profiles (STAC/DCAT/PROV) + ontology protocol *(not confirmed in repo)* |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | TBD | Required governed-doc reference *(not confirmed in repo)* |
| Ethics policy | `docs/governance/ETHICS.md` | TBD | Required governed-doc reference *(not confirmed in repo)* |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | TBD | Required governed-doc reference *(not confirmed in repo)* |
| Data README | `data/README.md` | TBD | Domain pack layout + global catalogs *(not confirmed in repo)* |
| Source README | `src/README.md` | TBD | Subsystem layout: pipelines/graph/server *(not confirmed in repo)* |
| Schema registry | `schemas/README.md` | TBD | JSON schema registry + validation guidance *(not confirmed in repo)* |
| CI workflows index | `.github/workflows/README.md` | TBD | CI gates + validation mapping *(not confirmed in repo)* |

### Project reference library

These documents are part of the project’s working reference set. **They are not automatically assumed to be committed into the repo.** If you choose to vendor any of them into `docs/`, ensure licensing, size constraints, and governance review are completed.

#### Architecture, scope, planning, and expansion references

- *MASTER_GUIDE_v12.md* (PDF export) *(recommended governed home: `docs/MASTER_GUIDE_v12.md` — Markdown not confirmed in repo)*
- *Kansas Frontier Matrix — v13 Redesign Blueprint* (PDF) *(recommended governed home: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — not confirmed in repo)*
- *Comprehensive vision draft* (PDF) *(recommended governed home: `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` — not confirmed in repo)*
- *KFM Next Stages Planning* (PDF) *(recommended governed home: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` — not confirmed in repo)*
- *Kansas Frontier Matrix: System Structure and Scope* (PDF) *(recommended home: `docs/architecture/` — not confirmed in repo)*
- *Kansas Frontier Matrix (KFM) Implementation Guide* (PDF) *(recommended home: `docs/architecture/` — not confirmed in repo)*
- *Expanding the Kansas Frontier Matrix Knowledge Base* (PDF) *(recommended home: `docs/architecture/` or `docs/research/` — not confirmed in repo)*
- *Expanding the Kansas Frontier Matrix: External Data, Tools, and Frameworks* (PDF) *(recommended home: `docs/architecture/` or `docs/research/` — not confirmed in repo)*
- *Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design* (PDF) *(recommended home: `docs/architecture/` or `docs/design/` — not confirmed in repo)*

#### Documentation authoring and UI references

- *Comprehensive Guide to Markdown in Programming and Documentation* (PDF)
- *Universal Markdown templates* (DOCX) *(upstream source; prefer governed Markdown under `docs/templates/`)*
- *CSS Notes for Professionals* (PDF)
- *KFM-responsive-web-design-with-html5-and-css3* (PDF)
- *KFM-webgl-programming-guide-interactive-3d-graphics-programming-with-webgl* (PDF)
- *DesigningVirtualWorlds* (PDF)
- *KFM- Computer Graphics using JAVA 2D & 3D* (PDF)

#### Geospatial / modeling references

- *An Introduction to Spatial Data Analysis and Visualisation in R* (PDF)
- *KFM- python-geospatial-analysis-cookbook* (PDF)
- *Scientific Modeling and Simulation: A Comprehensive NASA-Grade Guide* (PDF)
- *KFM- Generalized Topology Optimization for Structural Design* (PDF)

#### AI / ML / statistics references

- *KFM- AI Foundations of Computational Agents (3rd Ed)* (PDF)
- *KFM- Artificial-neural-networks-an-introduction* (PDF)
- *KFM- deep-learning-in-python-prerequisites* (PDF)
- *KFM- Data Science & Machine Learning (Mathematical & Statistical Methods)* (PDF)
- *KFM- Understanding Statistics & Experimental Design* (PDF)
- *KFM- regression-analysis-with-python* (PDF)
- *KFM- Bayesian computational methods* (PDF)
- *KFM- Data Mining Concepts & applications* (PDF)

#### Graph and data engineering references

- *KFM- Spectral Geometry of Graphs* (PDF)
- *KFM- Scalable Data Management for Future Hardware* (PDF)
- *KFM- clean-architectures-in-python* (PDF)

#### Template + draft source documents (upstream)

- *TEMPLATE__KFM_UNIVERSAL_DOC* (DOCX)
- *TEMPLATE__STORY_NODE_V3* (DOCX)
- *TEMPLATE__API_CONTRACT_EXTENSION* (DOCX)
- *KFM data Refrences* (DOCX)
- *KFM data References 2* (DOCX)
- *KFM DATA Refrences 3* (DOCX)
- *README Information* (DOCX)

> If DOCX/PDF artifacts are being used as authoritative sources, prefer converting them into governed Markdown at canonical `docs/**` or `schemas/**` destinations and treating the DOCX/PDF as upstream references only (to avoid drift).

### Definition of done

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Links resolve (no broken internal references)
- [ ] Any “system rule” stated here is also reflected in governed artifacts (Master Guide / standards / blueprint), or is explicitly marked as *not confirmed in repo*
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated when relevant

## 🗂️ Directory Layout

### This document

- `path`: `docs/README.md`

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Architecture | `docs/architecture/` | System architecture, ADRs, diagrams, redesign blueprints |
| Standards | `docs/standards/` | Markdown protocol + profiles (STAC/DCAT/PROV) + ontology protocol |
| Templates | `docs/templates/` | Universal / Story Node / API Contract templates |
| Governance | `docs/governance/` | Governance, ethics, sovereignty controls |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts + assets |
| Domain docs | `docs/data/` | Domain documentation index (recommended canonical home) |
| Domain packs | `data/<domain>/` | Domain-local staging: `raw/`, `work/`, `processed/` *(v13 target)* |
| Global catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV outputs (global, machine-validated) |
| Graph import artifacts | `data/graph/csv/`, `data/graph/cypher/` | Neo4j import fixtures (if used) |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog generation |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations/constraints |
| API boundary | `src/server/` | Contracted API layer + redaction/generalization enforcement |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL schema snapshots + contract tests |
| UI | `web/` | React + map clients, layer registry |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/story/ui/telemetry as adopted) |
| Tests | `tests/` | Unit + integration + contract tests |
| Tools | `tools/` | CLI utilities, validators, wrappers (must not become canonical output homes) |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| CI | `.github/` | Workflows, CI gates |
| Releases | `releases/` | Versioned packaged artifacts |

> Legacy drift note: older documents may reference `src/api/` or governance paths under `docs/standards/**`. New work should prefer the canonical roots above and add explicit deprecation/migration notes when moving paths.

### Expected file tree for this sub-area (target)

~~~text
📁 docs/
├── 📄 README.md
├── 📄 MASTER_GUIDE_v12.md                           # (not confirmed) PDF source exists in project refs
├── 📄 glossary.md                                   # (not confirmed) add if missing
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md              # (not confirmed) PDF source exists
│   ├── 📄 KFM_VISION_FULL_ARCHITECTURE.md            # (not confirmed) PDF source exists
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md               # (not confirmed) PDF source exists
│   ├── 📁 diagrams/
│   └── 📁 adr/
├── 📁 standards/
│   ├── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md              # (not confirmed)
│   ├── 📄 KFM_REPO_STRUCTURE_STANDARD.md             # (not confirmed)
│   ├── 📄 KFM_STAC_PROFILE.md                        # (not confirmed / may be placeholder)
│   ├── 📄 KFM_DCAT_PROFILE.md                        # (not confirmed)
│   ├── 📄 KFM_PROV_PROFILE.md                        # (not confirmed / may be placeholder)
│   └── 📄 KFM_ONTology_PROTOCOL.md                   # (not confirmed)
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md             # (not confirmed) DOCX source exists
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md                 # (not confirmed) DOCX source exists
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md        # (not confirmed) DOCX source exists
├── 📁 governance/
│   ├── 📄 ROOT_GOVERNANCE.md                         # not confirmed in repo
│   ├── 📄 ETHICS.md                                  # not confirmed in repo
│   └── 📄 SOVEREIGNTY.md                              # not confirmed in repo
├── 📁 data/
│   └── 📄 <domain docs live here>                    # recommended canonical docs home for domains
├── 📁 pipelines/
│   └── 📄 <etl + catalog documentation lives here>
├── 📁 graph/
│   └── 📄 <ontology + entity/edge documentation lives here>
├── 📁 api/
│   └── 📄 <API docs + contract notes live here>      # code lives in src/server/
├── 📁 web/
│   └── 📄 <UI docs: map/layer registry/a11y/audit>
├── 📁 reports/
│   └── 📁 story_nodes/
│       ├── 📁 draft/                                 # optional; not confirmed in repo
│       ├── 📁 published/                             # optional; not confirmed in repo
│       └── 📁 assets/                                # optional; not confirmed in repo
├── 📁 telemetry/
│   └── 📄 <signals + instrumentation docs>
└── 📁 security/
    └── 📄 <redaction + threat model docs>
~~~

## 🧭 Context

### Background

KFM documentation is not just narrative: it defines and preserves the system’s contracts and invariants across ETL, catalogs, graph, API boundary, UI, and story layers.

At the system level, KFM is intended to be an evidence-first “living atlas” that integrates diverse Kansas historical/cultural/ecological data into a unified graph, and surfaces that evidence through interactive maps, timelines, and provenance-linked Story Nodes.

### Assumptions

- This README remains aligned to the **v12 Master Guide** as the current system anchor.
- v13 materials (blueprint/vision/next-stages) may exist as PDFs in the project reference set; if so, convert them into governed Markdown under `docs/architecture/` to avoid drift.
- If a referenced path/document is missing, treat it as **not confirmed in repo** and either:
  - add it under the correct canonical location, or
  - update this README to link to the correct existing location.

### Constraints / invariants (non-negotiable)

- Pipeline order is preserved:

  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

- The UI must consume graph/context through the **API boundary** (no direct Neo4j dependency).
- Focus Mode only consumes provenance-linked content (no uncited facts).
- No new public narrative without sources, no new data without provenance, and no new subsystem changes without docs + tests.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which `docs/**` subdirectories are present today vs target? | TBD | TBD |
| Where is the canonical glossary located (and is it complete)? | TBD | TBD |
| What is the canonical API schema format (OpenAPI, GraphQL, both)? | TBD | TBD |
| How should legacy staging patterns (`data/raw/<type>/...`) coexist with v13 domain packs (`data/<domain>/{raw,work,processed}/`)? | TBD | TBD |
| Are there legacy governance refs under `docs/standards/**` that need migration to `docs/governance/**`? | TBD | TBD |

### Future extensions

- Add an index README per major area (data, pipelines, graph, API, web/design, story nodes).
- Add a docs health-check script to validate internal links and required front matter.
- Add an ADR formalizing migration from legacy staging layouts to domain-pack layout (if both exist).

## 🗺️ Diagrams

### System / dataflow diagram (canonical roots)

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Neo4j Graph — src/graph (+ data/graph imports)"]
  C --> D["API boundary — src/server"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j via src/graph contracts)
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs (apply redaction rules)
  Graph-->>API: context bundle (entities + evidence refs)
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

## 📦 Data & Metadata

### Data lifecycle (v13 target)

- Domain-local staging (per domain pack):
  - `data/<domain>/raw/` → `data/<domain>/work/` → `data/<domain>/processed/`
- Global metadata outputs:
  - STAC: `data/stac/collections/` and `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`
  - Graph import: `data/graph/csv/` and `data/graph/cypher/`

### Legacy staging patterns (known drift)

Some older drafts and modules may still use patterns like:

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`
- `data/raw/<type>/` (e.g., `data/raw/terrain/`)

These are not inherently wrong, but they must be documented explicitly and mapped to the v13 target layout (prefer ADR + migration notes). If you add a new domain today, prefer the v13 domain-pack pattern.

### Domain expansion pattern

When adding a new domain:

1) Create the domain pack directories:
   - `data/<domain>/raw/`, `data/<domain>/work/`, `data/<domain>/processed/`

2) Ensure processed outputs can generate:
   - STAC Collection + Item(s)
   - DCAT dataset record(s)
   - PROV activity/bundle(s)
   - Graph import fixtures (if graph-ingested)

3) Create the docs home (recommended canonical):
   - `docs/data/<domain>/README.md`

4) If `data/<domain>/mappings/` is used, link it from `docs/data/<domain>/` to prevent drift.

### Example domain modules (from project drafts)

> These examples are drawn from project draft documents and may be **not confirmed in repo**.

- Air Quality (drafted module pattern):
  - `docs/data/air-quality/README.md`
  - `data/air-quality/governance/README.md`
- Land Treaties (drafted module pattern):
  - `docs/data/historical/land-treaties/README.md`
  - `data/historical/land-treaties/` *(verify whether this is domain-pack or legacy)*

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy

- Every dataset/evidence product must have:
  - STAC Collection + Item(s)
  - DCAT mapping (minimum title/description/license/keywords)
  - PROV bundle for the activity that generated it

### Versioning expectations

- New versions should link predecessor/successor relationships in catalogs.
- Graph should mirror version lineage where applicable.

### Where schemas live

- STAC validation: `schemas/stac/**`
- DCAT validation: `schemas/dcat/**`
- PROV validation: `schemas/prov/**`
- Story Node validation: `schemas/story_nodes/**` *(if adopted; not confirmed in repo)*
- UI registry validation: `schemas/ui/**` *(if adopted; not confirmed in repo)*

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| API boundary | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story Nodes | schema + citations + entity refs | no unsourced narrative |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Extension points checklist

- [ ] Data: new domain pack added under `data/<domain>/...`
- [ ] ETL: deterministic pipeline outputs land in canonical staging + catalogs
- [ ] STAC: new collection + item schema validation
- [ ] DCAT: dataset record created/validated
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] API: contract update + tests + redaction rules
- [ ] UI: layer registry entry + access rules + a11y notes
- [ ] Story Nodes: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

- Story Nodes must carry provenance annotations and connect to graph entities.
- Published Story Nodes should cite **graph entity IDs** and **STAC/DCAT/PROV evidence IDs**.
- Published Story Nodes must pass validation for front-matter, citations, entity references, and redaction compliance.

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Any predictive content must be opt-in and carry uncertainty/confidence metadata.

## 🧪 Validation & CI/CD

### CI behavior contract (design intent)

- **Validate if present**: if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid**: schema errors, missing links, or orphan references fail deterministically.
- **Skip if not applicable**: optional roots absent → skip without failing overall CI.

### Minimum checks

- [ ] Markdown protocol checks (governed docs)
- [ ] Schema validation (STAC/DCAT/PROV, Story Nodes, UI registries, telemetry)
- [ ] Graph integrity checks
- [ ] API contract tests (`src/server/contracts/**`)
- [ ] UI registry checks (layer registry schema)
- [ ] Link integrity checks for docs (if tooling exists)
- [ ] Security and sovereignty checks (as applicable)

### Local reproduction (placeholders)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.
# 1) validate schemas
# 2) validate provenance bundles
# 3) run unit/integration tests
# 4) run doc lint / link checks
~~~

### Telemetry signals (expected)

| Signal | Source | Where recorded |
|---|---|---|
| Telemetry schemas | `schemas/telemetry/` | `docs/telemetry/` + CI artifacts |
| Pipeline run lineage | `data/prov/` | `data/prov/**` + release manifests (if used) |

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### Sovereignty safety

- Document redaction/generalization rules for any restricted locations.
- Prefer API-boundary enforcement for redaction and downstream propagation into UI/story views.

### AI usage constraints

- Ensure the doc’s AI permissions/prohibitions match intended use.
- Do not infer or generate sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.2 | 2025-12-26 | Align docs index to v13 target roots (domain packs + global catalogs), add template-selection guidance, and expand project reference library to include all provided project files | TBD |
| v1.0.1 | 2025-12-24 | Align docs index with v12 guide + v13 blueprint; add canonical roots, CI gates, and project reference library | TBD |
| v1.0.0 | 2025-12-22 | Initial `docs/` README index | TBD |

---

Footer refs (do not remove):

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
