---
title: "Kansas Frontier Matrix — Repository README"
path: "README.md"
version: "v1.0.2"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:readme:v1.0.2"
semantic_document_id: "kfm-readme-v1.0.2"
event_source_id: "ledger:kfm:doc:readme:v1.0.2"
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
2) `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` — near-term roadmap + vertical-slice checklist *(draft; not confirmed in repo)*  
3) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — canonical roots + v13 readiness gates *(draft; if adopted)*  
4) `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` — end‑to‑end architecture vision *(draft; not confirmed in repo)*  
5) `docs/README.md` — documentation index  
6) `data/README.md` — data lifecycle + domain layout  
7) `schemas/README.md` — schema registry + minimum contract set  
8) `src/README.md` — subsystem boundaries (pipelines/graph/server)  
9) `mcp/README.md` — experiments, run manifests, model cards, SOPs *(not confirmed in repo)*  
10) `.github/workflows/README.md` — CI gates + validation expectations

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
| Next Stages Blueprint (draft) | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | TBD | Roadmap + vertical-slice checklist (v12→v13) |
| v13 redesign blueprint (draft; if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Canonical roots + minimum contract set + readiness gates |
| Full architecture vision (draft) | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | TBD | End-to-end architecture context (long-term guidance) |
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
| Data | `data/README.md` | Data lifecycle + domain layout + catalog/prov locations |
| Schemas | `schemas/README.md` | Contract home for validations (catalogs/story/UI/telemetry) |
| Source | `src/README.md` | Subsystem boundaries (pipelines/graph/server) |
| CI | `.github/workflows/README.md` | Gatekeeping rules and expected checks |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published narratives for Focus Mode |
| MCP | `mcp/README.md` | Experiment logs, run manifests, model cards, SOPs *(if present)* |

### Common contribution patterns

| You are adding/changing… | Put it here | Also update / validate |
|---|---|---|
| A new dataset/domain (data staging) | **v12 baseline:** `data/raw/<domain>/`, `data/work/<domain>/`, `data/processed/<domain>/`  \n**v13 target (domain packs):** `data/<domain>/{raw,work,processed}/` | STAC/DCAT/PROV outputs + PROV activity; tests if present |
| Domain governance docs (sources, classification, QA) | `data/<domain>/governance/` *(or `docs/data/<domain>/...` — choose one canonical and link)* | Ensure classifications propagate into catalogs/UI |
| ETL or transforms | `src/pipelines/<domain>/` (or `src/pipelines/common/`) | Determinism (stable IDs) + run logs + provenance |
| Catalog schemas/profiles | `schemas/{stac,dcat,prov}/` | Schema validation + changelog/semver (if adopted) |
| Graph ingest/mappings | `src/graph/` and `data/graph/` | Ontology constraints + import fixtures |
| API endpoints/contracts | `src/server/` and `src/server/contracts/` | Contract tests + redaction rules at boundary |
| UI layers / registry entries | `web/` (and UI schemas in `schemas/ui/`) | UI registry schema validation + governance gates |
| Story Nodes | `docs/reports/story_nodes/` | Story Node schema validation + provenance-linked citations |
| Experiments / evaluation artifacts | `mcp/` | Keep outputs referenced (not duplicated); record run IDs + pointers to evidence |

## 🗂️ Directory Layout

### This document

- `path`: `README.md` (must match front‑matter)

### Canonical roots (top level)

| Area | Path | What lives here |
|---|---|---|
| Repo metadata + policy | `.github/` | workflows, issue templates, security policy, reproducibility kits (if adopted) |
| Standards + protocols | `docs/standards/` | repo standards, KFM‑MDP, profiles (STAC/DCAT/PROV), structure rules |
| Governance | `docs/governance/` | governance, ethics, sovereignty controls |
| Architecture | `docs/architecture/` | system architecture, ADRs, diagrams, redesign/roadmap blueprints |
| Documentation index | `docs/README.md` | canonical navigation for docs (if present) |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | observability + security/governance signals |
| Data domains + staging | `data/` | staging (`raw/`, `work/`, `processed/`) by domain *(v12 baseline)* OR domain packs under `data/<domain>/...` *(v13 target)* |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC, DCAT datasets, PROV lineage bundles |
| Graph | `src/graph/` + `data/graph/` + `docs/graph/` | ontology‑governed ingest + exports + graph docs |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | deterministic transforms; outputs written under `data/**` |
| API boundary | `src/server/` | contracted access layer (REST/GraphQL); redaction + provenance refs |
| Frontend | `web/` + `docs/web/` | map layers + Focus Mode UX; no direct graph access |
| Schemas | `schemas/` | JSON Schemas for catalogs, story nodes, UI registries, telemetry |
| Story Nodes | `docs/reports/story_nodes/` | draft/published narratives + assets |
| MCP / experiments | `mcp/` | experiment logs, run manifests, SOPs, model cards |
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

### Data layout patterns (baseline vs target)

#### Baseline staging layout (v12)

Use this layout if the repo stages data by lifecycle stage (with per-domain subfolders):

~~~text
📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
├── 📁 prov/
├── 📁 graph/
│   ├── 📁 csv/
│   └── 📁 cypher/
└── 📄 README.md
~~~

#### v13 target domain-pack layout (reference)

Use this layout if the repo stages data inside a domain pack (one domain owns its lifecycle folders):

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

> Choose **one** data layout pattern per domain (and document it in the domain README). Do not mix baseline and domain-pack staging for the same domain without an explicit migration note.

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
- Documentation and code must remain separated:
  - governed docs live under `docs/` (and other doc roots such as `data/<domain>/governance/` if adopted),
  - executable code lives under `src/` / `tools/` / `tests/` (no mixed “.py with YAML front‑matter” artifacts).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which paths are currently implemented vs “target layout”? | TBD | TBD |
| Which data layout is canonical per domain: v12 baseline staging vs v13 domain packs? | TBD | TBD |
| Are there legacy duplicate roots (e.g., `src/api/` vs `src/server/`, `src/map/` vs `web/`), and what is the migration/deprecation plan? | TBD | TBD |
| Where is the canonical glossary located (and is it complete)? | TBD | TBD |
| Which CI validators exist today (Markdown protocol, schema lint, contract tests, link checks)? | TBD | TBD |
| Where is the authoritative run manifest location: `data/prov/` vs `releases/<version>/`? | TBD | TBD |
| Is story content already aligned to `docs/reports/story_nodes/` (draft/published), or does a legacy path still exist? | TBD | TBD |
| Are domain naming conventions standardized (e.g., `air-quality` vs `air_quality`)? | TBD | TBD |

### Future extensions

- New data domains with domain packs (staging + mapping + tests + docs).
- New evidence artifacts treated as catalog assets and linked into Focus Mode.
- New Story Node types (with schema validation and provenance requirements).
- Composite CI actions / reproducibility kits (if adopted) to standardize validation and regression testing.

## 🗺️ Diagrams

### System / dataflow diagram (canonical roots)

~~~mermaid
flowchart LR
  R["Raw sources — data/raw or data/<domain>/raw"] --> A["ETL — src/pipelines"]
  A --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
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

Choose the lifecycle layout used for a given domain and keep it consistent:

- **v12 baseline:** `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`  
- **v13 target (domain packs):** `data/<domain>/raw/` → `data/<domain>/work/` → `data/<domain>/processed/`

Then:

- catalog outputs: `data/stac/`, `data/catalog/dcat/`, `data/prov/`
- graph ingest exports: `data/graph/`
- optional derived outputs (evidence products): `data/reports/` (treated as catalog assets)

### Domain expansion pattern (recommended)

- Add a domain README at: `data/<domain>/README.md` (and governance/runbooks as needed)
- Stage data using either:
  - `data/raw|work|processed/<domain>/` (v12 baseline), or
  - `data/<domain>/{raw,work,processed}/` (v13 target)
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

### Repo lint invariants (recommended CI gates)

- No YAML front‑matter in executable code files (split into docs + metadata).
- No duplicate canonical homes for the same subsystem without explicit deprecation markers.
- No “typo-paths” (e.g., `README.me`).
- No mixed doc/code artifacts (e.g., scripts under `docs/` that contain runnable code).

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
| v1.0.2 | 2025-12-24 | Added Next Stages + Full Vision references; reconciled v12 baseline vs v13 target data layout language; tightened doc/code separation and repo-lint invariants | TBD |

---

Footer refs (do not remove):
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Next stages blueprint: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Full architecture vision: `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`