---
title: "Kansas Frontier Matrix — Repository README"
path: "README.md"
version: "v1.0.1"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:readme:v1.0.1"
semantic_document_id: "kfm-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:readme:v1.0.1"
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

# Kansas Frontier Matrix (KFM)

A geospatial + historical knowledge system with governed data, catalogs, graph semantics, APIs, and a map/narrative UI.

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

## 📘 Overview

### Purpose

- Provide a single entry point for contributors and readers to understand:
  - what KFM is,
  - how the repository is organized,
  - where artifacts “live” across the pipeline,
  - and which governance/validation rules must not be broken.

### Scope

| In Scope | Out of Scope |
|---|---|
| Repository orientation + canonical pipeline + directory layout + contribution pointers | Full subsystem implementations, deployment specifics, and domain-specific dataset documentation (see domain READMEs + subsystem docs) |

### Audience

- Primary: maintainers and contributors (data, catalog, graph, API, UI, narrative).
- Secondary: reviewers (governance/ethics/sovereignty), historians/editors, and external collaborators.

### Definitions (link to glossary)

- Link: `docs/glossary.md` (if present)
- Terms used in this doc:
  - **Domain pack**: the minimal set that lets a domain participate in the pipeline (staging + mapping + tests + docs).
  - **Contract artifact**: machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
  - **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived products).
  - **Story Node**: a provenance-linked narrative artifact designed to render in the UI.
  - **Focus Mode**: an immersive UI view that consumes provenance-linked context only.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants + expected top-level layout |
| Standards index | `docs/standards/` | TBD | Governed standards, including KFM-MDP |
| Templates index | `docs/templates/` | TBD | Document + MCP templates |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default template for governed markdown docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Focus Mode narrative artifacts |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | REST/GraphQL contract changes |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] References point to canonical docs/templates (no dead paths)
- [ ] Directory layout matches the Master Guide’s expected top-levels
- [ ] Constraints/invariants are stated clearly (pipeline order, API boundary, provenance rules)
- [ ] Validation expectations are described (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `README.md` (must match front-matter)

### Repo top-levels (expected)

~~~text
.github/
data/
docs/
mcp/
schemas/
src/
tests/
tools/
web/
releases/
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Repo metadata + policy | `.github/` | security policy, workflows, issue templates |
| Data domains | `data/` | domain staging (`raw/`, `work/`, `processed/`) + (optional) domain docs |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC items/collections, DCAT datasets, PROV lineage bundles |
| Pipelines (code) | `src/pipelines/` | deterministic transforms; outputs written under `data/**` |
| Pipelines (docs) | `docs/pipelines/` | runbooks, domain pipeline notes (if used) |
| Graph (code) | `src/graph/` | ontology-governed ingest + migrations/constraints |
| Graph (imports) | `data/graph/` | import CSVs/scripts (and generated extracts for Neo4j) |
| API boundary | `src/server/` | contracted access layer (REST/GraphQL); redaction + provenance refs |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL schema snapshots + contract tests (if used) |
| Frontend | `web/` | map layers + Focus Mode UX; **no direct graph access** |
| Frontend docs | `docs/design/` | UI/UX design notes, a11y guidance (if used) |
| Schemas | `schemas/` | JSON Schemas for artifacts (catalogs, story nodes, UI registries, telemetry) |
| Story Nodes | `docs/reports/story_nodes/` | draft/published narratives + assets |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | observability + governance/security metrics (if used) |
| Security | `.github/SECURITY.md` + `docs/security/` | policy + technical standards (if used) |
| MCP / experiments | `mcp/` | experiment logs, run manifests, SOPs |
| Tests | `tests/` | unit + integration + contract tests |
| Tooling | `tools/` | scripts and utilities (repo lint, validators, etc.) |
| Releases | `releases/` | release manifests/SBOMs/telemetry snapshots (if used) |

### Expected file tree for this sub-area

~~~text
📁 Kansas-Frontier-Matrix/
├── 📄 README.md
├── 📁 .github/
├── 📁 data/
├── 📁 docs/
├── 📁 mcp/
├── 📁 schemas/
├── 📁 src/
├── 📁 tests/
├── 📁 tools/
├── 📁 web/
└── 📁 releases/
~~~

### Target data layout (reference)

~~~text
📁 data/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
├── 📁 prov/
├── 📁 graph/
│   ├── 📁 csv/
│   └── 📁 cypher/
├── 📁 reports/   # optional evidence products (if used)
└── 📁 <domain>/
    ├── 📁 raw/
    ├── 📁 work/
    ├── 📁 processed/
    ├── 📁 mappings/
    └── 📄 README.md
~~~

## 🧭 Context

### Background

KFM’s core design goal is an evidence-first, provenance-linked system where every downstream view (including narrative Focus Mode) remains traceable back to catalog + provenance artifacts.

### Assumptions

- The canonical pipeline ordering is preserved.
- Schema/contracts are treated as first-class artifacts.
- Pipelines are deterministic and reproducible.

### Constraints / invariants

- **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode** is preserved.
- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; all graph access is via `src/server/`.
- **Schemas/specs live in `schemas/` and API contracts live under `src/server/contracts/` (validated in CI).**
- **Derived datasets belong under `data/<domain>/processed/` (not under `src/`).**
- **Catalog outputs (STAC/DCAT/PROV) are evidence artifacts and must not be authored in `docs/`.**
- **Focus Mode only presents provenance-linked content (no uncited facts).**
- Predictive/AI-generated content (if any) is opt-in and must include uncertainty/confidence metadata.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which paths are currently implemented vs “target layout”? | TBD | TBD |
| Where is the canonical glossary located (and is it complete)? | TBD | TBD |
| Which CI validators exist today (Markdown protocol, schema lint, contract tests)? | TBD | TBD |
| Do we standardize domains as `air-quality` vs `air_quality` and resolve naming inconsistencies? | TBD | TBD |

### Future extensions

- New data domains with domain packs (staging + mapping + tests + docs).
- New evidence artifacts (analysis products) treated as catalog assets and linked into Focus Mode.
- New story node types (with schema validation and provenance requirements).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[API Layer]
  D --> E[Map UI — React · MapLibre · Cesium]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs (with redaction rules)
  Graph-->>API: context bundle + evidence references
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)

- `data/raw/` → `data/work/` → `data/processed/` → catalog outputs (`data/stac/`, `data/catalog/dcat/`, `data/prov/`) (+ `data/reports/` outputs as needed) → graph ingest exports (`data/graph/`)

### Domain expansion pattern (recommended)

- Add a new domain under: `data/<domain>/...`
- Add ETL/pipeline logic under: `src/pipelines/<domain>/...` (or shared utilities under `src/pipelines/common/`)
- Add domain docs under: `docs/<domain>/...` or `docs/data/<domain>/...` (choose one canonical home and link it)
- Add mapping notes under: `data/<domain>/mappings/` and/or `docs/data/<domain>/` (choose one canonical home and link it)

## 🌐 STAC, DCAT & PROV Alignment

### Policy for every dataset / evidence product

For each dataset or evidence product:

- STAC Collection + Item(s)
- DCAT mapping record (minimum title/description/license/keywords)
- PROV activity describing lineage (sources + run/activity identifiers)
- Version lineage links reflected in catalogs and (where applicable) the graph

### Versioning expectations

- New versions link predecessor/successor in catalogs.
- The graph mirrors version lineage (entities and evidence artifacts).

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Story Nodes are designed to be “machine-ingestible storytelling”:
  - provenance-linked,
  - connected to graph entities,
  - and reviewable/publishable artifacts.

### Provenance-linked narrative rule

- Every claim in Focus Mode contexts must trace to a dataset / record / asset identifier.
- Any predictive content must be opt-in and carry uncertainty/confidence metadata.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV, story nodes, UI registries, telemetry)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that typically require elevated review:

- Adding new sensitive layers (restricted locations, cultural knowledge, PII, etc.)
- Introducing or changing AI-generated narrative behavior visible to users
- Adding new external data sources
- Adding new public-facing endpoints

### CARE / sovereignty considerations

- Identify communities impacted and protection rules.
- Use generalization/redaction for restricted locations.
- Ensure sensitive assets (images/docs) follow review gates before publication.

### AI usage constraints

- Ensure the document’s AI permissions/prohibitions match intended use.
- Do not imply prohibited actions (e.g., inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial repository README (governed-doc format) | TBD |
| v1.0.1 | 2025-12-23 | Align README with Master Guide v12 directory map + v13 invariants | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
