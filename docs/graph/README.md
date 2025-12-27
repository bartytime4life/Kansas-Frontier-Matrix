---
title: "KFM Graph — README"
path: "docs/graph/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
status: "active"
doc_kind: "Reference"
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

doc_uuid: "urn:kfm:doc:graph:readme:v1.0.0"
semantic_document_id: "kfm-graph-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:graph:readme:v1.0.0"
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

# KFM Graph — README

This README documents the **governed conventions** for KFM’s **Graph subsystem** (Neo4j): ontology, migrations/constraints, ingest/import artifacts, and how the graph integrates with catalogs, APIs, Story Nodes, and Focus Mode.

## 📘 Overview

### Purpose

- Define the **Graph subsystem contract**: ontology + migrations + constraints, with **stable labels/edges**.
- Document how graph entities/relationships must remain **provenance-linked** to STAC/DCAT/PROV so Focus Mode can surface *only* evidence-backed context.
- Reinforce the **API boundary rule**: the UI must never query Neo4j directly; all graph access is mediated via contracted APIs.

### Scope

| In Scope | Out of Scope |
|---|---|
| Graph modeling conventions (labels, relationships, IDs, core properties) | Writing ETL transforms for raw sources (see `src/pipelines/`) |
| Ontology governance + schema evolution (migrations/constraints) | UI implementation details (see `web/`) |
| Catalog-to-graph linkage rules (STAC/DCAT/PROV → graph identifiers) | Defining new policies beyond governed docs |
| Graph import artifacts (`data/graph/**`) and how they’re produced | Operational deployment details for Neo4j (ops runbooks live elsewhere; not confirmed in repo) |

### Audience

- **Primary:** Contributors working on `src/graph/**`, ontology bindings, and graph integrity tests.
- **Secondary:** API maintainers (`src/server/**`), UI maintainers (`web/**`), and curators authoring Story Nodes.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — create if missing)*
- Terms used in this doc include: **property graph**, **ontology**, **label**, **relationship type**, **migration**, **constraint**, **entity resolution**, **provenance**, **evidence ID**, **Focus Mode**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline and invariants |
| Graph docs home | `docs/graph/` | Graph Maintainers | This README + ontology notes |
| Ontology definition | `docs/graph/ontology.md` | Graph Maintainers | Update when labels/edges change |
| Graph build + bindings | `src/graph/**` | Graph Eng | Generates/loads graph import artifacts |
| Graph import artifacts | `data/graph/csv/**` + `data/graph/cypher/**` | Graph Eng | CSV for bulk load; Cypher for constraints/migrations |
| Catalog outputs | `data/stac/**` + `data/catalog/dcat/**` + `data/prov/**` | Data Eng | Inputs to graph ingest and provenance |
| API boundary contracts | `src/server/contracts/**` | API Eng | Contract-first access to graph/context |
| Story Nodes | `docs/reports/story_nodes/**` | Curators | Must reference graph entity IDs + evidence IDs |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Canonical paths and invariants are stated (graph contract, API boundary, provenance-only Focus Mode)
- [ ] Directory layout + expected file tree present
- [ ] Validation steps listed (schema + graph integrity + contract tests)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `docs/graph/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Graph docs | `docs/graph/` | Ontology notes, migrations guidance, query examples |
| Graph build | `src/graph/` | Graph ingest/build logic + ontology bindings |
| Graph import | `data/graph/` | Import CSVs + Cypher migrations/constraints |
| STAC catalogs | `data/stac/` | Collections + Items used for discovery and traceability |
| DCAT catalogs | `data/catalog/dcat/` | Dataset-level catalog records |
| PROV bundles | `data/prov/` | Lineage bundles used by audits + Focus Mode |
| Schemas | `schemas/` | STAC/DCAT/PROV/Story Node/UI schemas |
| API boundary | `src/server/` | Contract-first access; redaction + query services |
| UI | `web/` | React/MapLibre UI (no direct Neo4j access) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative documents with citations + entity refs |
| Runs/experiments | `mcp/runs/` + `mcp/experiments/` | Pointers to PROV + evidence artifacts (avoid duplication) |

### Expected file tree for this sub-area

> Note: Some subfolders below are **recommended conventions** derived from project design docs. If they don’t exist yet, create them or adjust to match repo governance (avoid inventing new roots).

~~~text
📁 docs/
└── 📁 graph/
    ├── 📄 README.md                          # (this file)
    ├── 📄 ontology.md                         # graph ontology overview (create if missing)
    ├── 📁 migrations/                         # Cypher migrations/changelog (optional; not confirmed in repo)
    │   ├── 📄 README.md
    │   └── 📄 <YYYYMMDD>_<slug>.cypher
    ├── 📁 queries/                            # curated Cypher queries (optional; not confirmed in repo)
    │   ├── 📄 README.md
    │   └── 📄 <slug>.cypher
    ├── 📁 examples/                           # small example subgraphs (optional; not confirmed in repo)
    │   └── 📄 example_subgraph.md
    └── 📁 ops/                                # operational notes (optional; not confirmed in repo)
        └── 📄 README.md
~~~

## 🧭 Context

### Background

KFM uses a **Neo4j property graph** to connect entities, evidence, and provenance across domains so that:
- APIs can return a **context bundle** (entities + links + evidence references) for a given focus entity.
- Story Nodes can reference **graph entity IDs** and **evidence IDs** (STAC/DCAT/PROV) in a machine-checkable way.
- Focus Mode can enforce the rule: **provenance-linked only** (no unsourced narratives).

The graph is **ontology-driven**: label and relationship types are treated as a governed contract (changes require migrations and review). The graph is also designed to remain interoperable with semantic standards where applicable (e.g., PROV-O / GeoSPARQL alignment and optional RDF export).

### Assumptions

- Neo4j is the operational graph store for KFM (property graph).
- Graph ingest is driven by canonical artifacts produced earlier in the pipeline:
  - STAC (`data/stac/**`)
  - DCAT (`data/catalog/dcat/**`)
  - PROV (`data/prov/**`)
- Graph access from the UI is **always** mediated by APIs (no direct Neo4j connectivity from `web/`).
- Graph nodes store **references** back to catalog identifiers instead of duplicating large payloads.

### Constraints / invariants

- Canonical ordering is preserved:
  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- **Graph contract is canonical**: ontology + migrations + constraints must exist and remain consistent; labels/edges are stable.
- **No UI direct-to-graph reads**: the web client must never query Neo4j directly; API boundary enforces provenance + redaction.
- **Round-trip traceability**: when applicable, graph nodes include identifiers linking back to:
  - STAC Item IDs
  - DCAT dataset IDs
  - PROV activity IDs
- **No hallucinated sources**: any narrative surfaced in Focus Mode must resolve to real evidence references (datasets/documents), not fabricated citations.
- **Sensitive locations are protected**: restricted or culturally sensitive geometry/attributes must be generalized/redacted via governance rules before exposure.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical ID strategy for graph entities (URN/URI vs UUID)? | TBD | TBD |
| What is the authoritative list of labels/relationship types for the current ontology? | Graph Maintainers | TBD |
| Is RDF export (e.g., via Neo4j n10s) required or optional for v13 readiness? | TBD | TBD |
| Where should graph migration history be recorded (docs vs `data/graph/cypher/` vs both)? | TBD | TBD |

### Future extensions

- Add a governed “ontology changelog” that ties:
  - ontology version → migration files → CI graph integrity checks → API contract version bump.
- Add optional RDF export jobs and SHACL validation (if adopted; not confirmed in repo).
- Add stronger entity-resolution workflows (human review queues; confidence thresholds; audit logs).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph + data/graph"]
  C --> D["API boundary — src/server + contracts"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked"]
~~~

### Optional: sequence diagram (Focus Mode context query)

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

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC Collections/Items | JSON | `data/stac/**` | `schemas/stac/**` + KFM constraints |
| DCAT dataset records | JSON / JSON-LD | `data/catalog/dcat/**` | `schemas/dcat/**` (and/or shapes if used) |
| PROV bundles | JSON / JSON-LD | `data/prov/**` | `schemas/prov/**` |
| Domain processed outputs | mixed | `data/<domain>/processed/**` | domain-specific schemas + geometry validity |
| Ontology/migration artifacts | Markdown + Cypher | `docs/graph/**` + `data/graph/cypher/**` | review + graph integrity tests |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Graph import CSVs | CSV | `data/graph/csv/**` | ontology bindings + loader constraints |
| Graph migration/constraint scripts | Cypher | `data/graph/cypher/**` | stable labels/edges contract |
| Graph context bundles | API payloads | `src/server/**` | contract tests required |

### Sensitivity & redaction

- Restricted locations or culturally sensitive knowledge must be protected via:
  - geometry generalization where required,
  - API-level redaction rules,
  - Story Node review gates before publication.
- Avoid placing raw sensitive coordinates into graph properties that could be returned by APIs without governance gating.

### Quality signals

- Schema validation passes for STAC/DCAT/PROV artifacts.
- Deterministic runs and diffable outputs (idempotent pipelines).
- No orphan references:
  - graph entity refs resolve,
  - STAC/DCAT/PROV evidence refs resolve,
  - Story Node refs resolve.
- Graph integrity tests validate ontology bindings and constraint expectations.

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy (minimum)

For each dataset or evidence product:
- STAC Collection + Item(s)
- DCAT mapping record (minimum title/description/license/keywords)
- PROV activity describing lineage (sources + run/activity identifiers)
- Version lineage links reflected in catalogs and (where applicable) the graph

### Identifier linkage expectation

Graph nodes (and the APIs that serve them) should reference:
- STAC Item IDs
- DCAT dataset ID
- PROV activity ID

This enables Focus Mode to resolve “what is this?” into a traceable lineage bundle.

### Provenance modeling (graph-side)

- PROV artifacts can be represented as graph nodes (e.g., `Activity`, `Agent`) and linked to domain entities/artifacts.
- Keep the authoritative provenance payloads in `data/prov/**`; the graph should store identifiers/links and relationship structure.

### Interop note (optional)

- The graph may be exported or mapped to RDF where required for interoperability (e.g., PROV-O / GeoSPARQL alignment). Treat this as an extension point unless explicitly mandated by governance (not confirmed in repo).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Ontology (graph schema) | Defines allowed labels/edges/properties and their meaning | `docs/graph/ontology.md` |
| Migrations + constraints | Evolves schema safely; enforces uniqueness/shape rules | `data/graph/cypher/**` |
| Import artifact builder | Produces CSV/Cypher import artifacts from catalogs/prov | `src/graph/**` → `data/graph/**` |
| Entity resolution | Merges/links entities across datasets; carries confidence + review gates | graph pipelines + review workflow (not confirmed in repo) |
| Query services | Retrieve subgraphs/context bundles for APIs | `src/server/**` |
| Redaction enforcement | Prevents sensitive leakage; generalizes restricted geometry | API boundary + governance rules |

### Modeling guidelines (minimum safe rules)

- Use **stable identifiers** for entities (example URN style):
  - `urn:kfm:entity:Place:Fort_Leavenworth` *(example format; confirm canonical ID policy in ontology docs)*
- Use only ontology-approved labels and relationship types; do not invent new ones ad hoc.
  - Typical core labels referenced in design docs include: `Place`, `Person`, `Event`, `Document`, `Organization`, `Artifact` (authoritative list lives in `docs/graph/ontology.md`).
- When applicable, store **references** back to catalog/provenance IDs rather than duplicating large content:
  - `stac_item_id`, `dcat_dataset_id`, `prov_activity_id` (field names may vary; follow ontology bindings).
- AI- or heuristic-derived links must carry:
  - confidence/uncertainty metadata,
  - evidence pointers,
  - and must be reviewable (human-in-the-loop) before publication in public contexts.

### API boundary rule (non-negotiable)

- The UI does **not** connect to Neo4j directly.
- The API boundary mediates access and enforces provenance + redaction/generalization rules.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as evidence-first narrative

- Story Nodes should cite:
  - **graph entity IDs**, and
  - **STAC/DCAT/PROV evidence IDs**.
- Story Nodes must follow the Story Node template and validation rules (front-matter, citations, entity references, redaction compliance).

### Focus Mode rule

- Focus Mode only consumes **provenance-linked** content.
- Any predictive or AI-generated content must be:
  - opt-in,
  - labeled,
  - accompanied by uncertainty/confidence metadata,
  - and never presented as unmarked fact.

## 🧪 Validation & CI/CD

### Minimum CI gates (baseline)

- Markdown protocol validation
- Schema validation (STAC/DCAT/PROV)
- Graph integrity tests (no broken links; ontology bindings consistent)
- API contract tests (if graph-facing endpoints change)
- UI registry schema checks (if UI layers are affected)
- Security + sovereignty scanning gates (where applicable)

### Local reproduction (placeholder)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.
# Intent:
# 1) validate STAC/DCAT/PROV schemas
# 2) build graph import artifacts
# 3) run graph integrity tests
# 4) run API contract tests (if changed)
~~~

### Telemetry signals (optional)

| Signal | Source | Where recorded |
|---|---|---|
| Graph build run ID → PROV activity ID | pipeline run | `mcp/runs/**` (pointer) + `data/prov/**` |
| Orphan reference count | CI | telemetry schema (not confirmed in repo) |
| Redaction hits / suppressed fields | API logs | API observability (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Any change to:
  - ontology definitions (labels/edges),
  - sensitivity classification,
  - redaction/generalization behavior,
  - or public-facing graph-derived API outputs
  requires governance review per `docs/governance/ROOT_GOVERNANCE.md` *(process not confirmed in repo; treat as mandatory)*.

### CARE / sovereignty considerations

- Treat culturally sensitive knowledge and restricted locations as high-risk by default.
- Prefer coarse/aggregate public products and document decisions in:
  - catalog metadata (STAC/DCAT),
  - provenance bundles (PROV),
  - and Story Node review notes.

### AI usage constraints

- Allowed transformations: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy, inferring sensitive locations.
- Any AI-suggested graph links must remain reviewable and must not bypass evidence requirements.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial Graph subsystem README (ontology + provenance + API boundary conventions) | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API Contract Extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---
