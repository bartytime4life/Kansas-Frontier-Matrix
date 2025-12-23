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

A geospatial + historical knowledge system with **governed data**, **catalogs (STAC/DCAT/PROV)**, **graph semantics (Neo4j)**, **contracted APIs**, and a **map/narrative UI**.

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

## 🚦 Start here

Recommended reading order (paths are expected; if missing, treat as **not confirmed in repo** and update links):

1) `docs/MASTER_GUIDE_v12.md` — system + pipeline source of truth  
2) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — canonical roots + v13 readiness gates (draft; if adopted)  
3) `docs/README.md` — documentation index  
4) `data/README.md` — data lifecycle + domain layout  
5) `src/README.md` — subsystem boundaries (pipelines/graph/server)  
6) `schemas/README.md` — schema registry + minimum contract set  
7) `.github/workflows/README.md` — CI gates + validation expectations

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
| Repository orientation + canonical pipeline + directory layout + contribution pointers | Full subsystem implementations, deployment specifics, and domain‑specific dataset documentation (see domain READMEs + subsystem docs) |

### Audience

- Primary: maintainers and contributors (data, catalog, graph, API, UI, narrative).
- Secondary: reviewers (governance/ethics/sovereignty), historians/editors, external collaborators.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or repair link if the glossary lives elsewhere)*
- Terms used in this doc:
  - **Domain pack**: the minimal set that lets a domain participate in the pipeline (staging + mapping + tests + docs).
  - **Contract artifact**: machine‑validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
  - **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived products).
  - **Story Node**: a provenance‑linked narrative artifact designed to render in the UI.
  - **Focus Mode**: an immersive UI view that consumes provenance‑linked context only.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants + expected top‑level layout |
| v13 redesign blueprint (draft; if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical roots + minimum contract set + readiness gates |
| Docs index | `docs/README.md` | TBD | Where governed documentation is organized |
| Schema registry | `schemas/README.md` | TBD | Contract home for catalogs/story/UI/telemetry |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default template for governed Markdown docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Focus Mode narrative artifacts |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | REST/GraphQL contract changes |
| Security policy | `.github/SECURITY.md` | Maintainers | Private vulnerability reporting guidance |

### Definition of done (for this README)

- [ ] Front‑matter complete + valid (`path: README.md`)
- [ ] Canonical docs/templates referenced (no dead paths where possible)
- [ ] Canonical pipeline + invariants stated clearly (pipeline order, API boundary, provenance rules)
- [ ] Repository layout and canonical homes described (and marked if “target” vs “implemented”)
- [ ] Validation/CI expectations stated (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🧭 How to use this repository

### Repository navigation

| Area | What to open first | Why |
|---|---|---|
| Docs | `docs/README.md` | Canonical index for governed docs + templates/standards |
| Data | `data/README.md` | Domain staging + processed outputs + catalog/prov locations |
| Source | `src/README.md` | Subsystem boundaries (pipelines/graph/server) |
| Schemas | `schemas/README.md` | Contract home for validations (catalogs/story/UI/telemetry) |
| CI | `.github/workflows/README.md` | Gatekeeping rules and expected checks |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narratives for Focus Mode |

### Common contribution patterns

| You are adding/changing… | Put it here | Also update / validate |
|---|---|---|
| A new dataset/domain | `data/<domain>/{raw,work,processed}/` | STAC/DCAT/PROV outputs + PROV activity; tests if present |
| ETL or transforms | `src/pipelines/<domain>/` (or `src/pipelines/common/`) | Determinism (stable IDs) + run logs + provenance |
| Catalog schemas/profiles | `schemas/{stac,dcat,prov}/` | Schema validation + changelog/semver (if adopted) |
| Graph ingest/mappings | `src/graph/` and `data/graph/` | Ontology constraints + import fixtures |
| API endpoints/contracts | `src/server/` and `src/server/contracts/` | Contract tests + redaction rules at boundary |
| UI layers / registry entries | `web/` (and UI schemas in `schemas/ui/`) | UI registry schema validation + governance gates |
| Story Nodes | `docs/reports/story_nodes/` | Story Node schema validation + provenance-linked citations |

## 🗂️ Directory Layout

### This document

- `path`: `README.md` (must match front‑matter)

### Canonical roots (top level)

| Area | Path | What lives here |
|---|---|---|
| Repo metadata + policy | `.github/` | workflows, issue templates, security policy, reproducibility kits (if adopted) |
| Standards + protocols | `docs/standards/` | repo standards, KFM‑MDP, profiles (STAC/DCAT/PROV), structure rules |
| Governance | `docs/governance/` | governance, ethics, sovereignty controls |
| Architecture | `docs/architecture/` | system architecture, ADRs, diagrams, redesign blueprints |
| Documentation index | `docs/README.md` | canonical navigation for docs (if present) |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | observability + security/governance signals |
| Data domains | `data/` | domain staging (`raw/`, `work/`, `processed/`) + catalogs per pipeline |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC, DCAT datasets, PROV lineage bundles |
| Graph | `src/graph/` + `data/graph/` + `docs/graph/` | ontology‑governed ingest + exports + graph docs |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | deterministic transforms; outputs written under `data/**` |
| API boundary | `src/server/` | contracted access layer (REST/GraphQL); redaction + provenance refs |
| Frontend | `web/` + `docs/web/` | map layers + Focus Mode UX; no direct graph access |
| Schemas | `schemas/` | JSON Schemas for catalogs, story nodes, UI registries, telemetry |
| Story Nodes | `docs/reports/story_nodes/` | draft/published narratives + assets |
| MCP / experiments | `mcp/` | experiment logs, run manifests, SOPs |
| Tests | `tests/` | unit + integration + contract tests |
| Tooling | `tools/` | scripts and utilities (repo lint, validators, etc.) |
| Releases | `releases/` | release manifests/SBOMs/telemetry snapshots (if used) |

### Expected file tree (repo root)

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
├── 📁 reports/                  # optional: derived evidence products (as needed)
└── 📁 <domain>/
    ├── 📁 raw/
    ├── 📁 work/
    ├── 📁 processed/
    ├── 📁 mappings/             # optional: mapping notes (link from docs to avoid drift)
    └── 📄 README.md
~~~

## 🧭 Context

### Background

KFM’s core design goal is an **evidence‑first, provenance‑linked** system where every downstream view (including narrative Focus Mode) remains traceable back to catalog + provenance artifacts.

### Assumptions

- The canonical pipeline ordering is preserved.
- Schema/contracts are treated as first‑class artifacts.
- Pipelines are deterministic and reproducible.

### Constraints / invariants

- **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode** is preserved.
- **Frontend consumes contracts via APIs (no direct graph dependency).**
- **Focus Mode only presents provenance‑linked content (no uncited facts).**
- Predictive/AI‑generated content (if any) is opt‑in and must include uncertainty/confidence metadata.
- Canonical homes should not be duplicated without explicit deprecation/migration notes.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which paths are currently implemented vs “target layout”? | TBD | TBD |
| Where is the canonical glossary located (and is it complete)? | TBD | TBD |
| Which CI validators exist today (Markdown protocol, schema lint, contract tests)? | TBD | TBD |
| Where is the authoritative run manifest location: `data/prov/` vs `releases/<version>/`? | TBD | TBD |

### Future extensions

- New data domains with domain packs (staging + mapping + tests + docs).
- New evidence artifacts treated as catalog assets and linked into Focus Mode.
- New Story Node types (with schema validation and provenance requirements).
- Composite CI actions / reproducibility kits (if adopted) to standardize validation and regression testing.

## 🗺️ Diagrams

### System / dataflow diagram (canonical roots)

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph + data/graph"]
  C --> D["API boundary — src/server + contracts"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked"]
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
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)

- `data/<domain>/raw/` → `data/<domain>/work/` → `data/<domain>/processed/`
- Then: catalog outputs (`data/stac/`, `data/catalog/dcat/`, `data/prov/`)
- Then: graph ingest exports (`data/graph/`)
- Optional derived outputs (evidence products) may be written under `data/reports/` and treated as catalog assets.

### Domain expansion pattern (recommended)

- Add a new domain under: `data/<domain>/...`
- Add ETL/pipeline logic under: `src/pipelines/<domain>/...` (shared utilities under `src/pipelines/common/`)
- Add mapping docs under one canonical docs home (recommended): `docs/data/<domain>/...`
- If `data/<domain>/mappings/` is used, it MUST be linked from canonical docs to prevent drift.

## 🌐 STAC, DCAT & PROV Alignment

### Policy for every dataset / evidence product

For each dataset or evidence product:
- STAC Collection + Item(s)
- DCAT mapping record (minimum title/description/license/keywords)
- PROV activity describing lineage (sources + run/activity identifiers)
- Version lineage links reflected in catalogs and (where applicable) the graph

### Identifier linkage expectation

Graph nodes and APIs should reference:
- STAC Item IDs
- DCAT dataset ID
- PROV activity ID

This enables Focus Mode to resolve “what is this data?” into a traceable lineage bundle.

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | schemas + validators | machine‑validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance‑linked context bundle | no hallucinated sources |

### API boundary rule

- The UI does **not** connect to Neo4j directly.
- The API boundary mediates access and enforces provenance + redaction/generalization rules.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as evidence-first narrative

- Story Nodes should cite **graph entity IDs** and **STAC/DCAT/PROV evidence IDs**.
- Story Nodes may reference local assets (images/excerpts) with attribution, but the source‑of‑truth remains catalog + provenance artifacts.

### Focus Mode rule (non‑negotiable)

- Focus Mode must only consume **provenance‑linked** content.
- Any predictive/AI content must be clearly marked, opt‑in, and include uncertainty metadata.

## 🧪 Validation & CI/CD

### CI behavior contract

- **Validate if present**: if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid**: schema errors, missing links, or orphan references fail deterministically.
- **Skip if not applicable**: optional roots absent → skip without failing the overall pipeline.

### Minimum checks

- [ ] Markdown protocol checks (for governed docs)
- [ ] Schema validation (STAC/DCAT/PROV, story nodes, UI registries, telemetry)
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

# make validate-schemas
# make validate-lineage
# make test
# make lint-docs
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that typically require elevated review:
- Adding new sensitive layers (restricted locations, cultural knowledge, PII, etc.)
- Introducing/changing AI-generated narrative behavior visible to users
- Adding new external data sources
- Adding new public-facing endpoints

### CARE / sovereignty considerations

- Identify communities impacted and protection rules.
- Use generalization/redaction for restricted locations.
- Ensure sensitive assets (images/docs) follow review gates before publication.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not imply prohibited actions (e.g., inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial repository README (governed-doc format) | TBD |
| v1.0.1 | 2025-12-23 | Added repo navigation + clarified canonical roots/CI behavior; aligned wording with v13 contract-first guidance | TBD |

---

Footer refs (do not remove):
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
