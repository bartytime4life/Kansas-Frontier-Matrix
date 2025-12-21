---
title: "KFM Graph Subsystem — src/graph"
path: "src/graph/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:src:graph:readme:v1.0.0"
semantic_document_id: "kfm-src-graph-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:graph:readme:v1.0.0"
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

# KFM Graph Subsystem — `src/graph/`

## 📘 Overview

### Purpose
- `src/graph/` contains **graph build and ingest logic** for the KFM knowledge graph (Neo4j), including ontology-governed mappings, constraints, and migrations.
- This area is responsible for keeping **graph semantics stable** while the underlying datasets and catalogs evolve.

KFM’s canonical pipeline ordering is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

### Scope

| In Scope | Out of Scope |
|---|---|
| Ontology-governed entity + relationship modeling | UI components / map layers (`web/`) |
| Graph ingest jobs (e.g., catalog → graph) | Direct UI-to-graph access (disallowed) |
| Neo4j constraints + indexes definitions | API contracts (live at the API boundary) |
| Schema migrations and backfills | Raw or derived datasets (belong under `data/**`) |
| Graph fixtures for tests / deterministic loads | Story Node authoring (lives under Story Node canonical roots) |

### Audience
- Primary: graph engineers, data engineers maintaining Neo4j ingest/migrations
- Secondary: API engineers writing graph-backed endpoints; governance reviewers for schema changes

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Ontology**: the controlled vocabulary of node labels + relationship types + required properties
  - **Migration**: a controlled, versioned schema/data change applied to the graph
  - **Constraint**: Neo4j constraint/index enforcing required properties or uniqueness
  - **Catalogs**: STAC/DCAT/PROV outputs used as inputs to graph ingest

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical ordering + subsystem homes) | `docs/MASTER_GUIDE_v12.md` | Governance | Canonical source of truth |
| Graph governed docs | `docs/graph/` | Graph owners | not confirmed in repo |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Catalog owners | Source inputs to graph ingest |
| Graph ingest code | `src/graph/` | Graph owners | This directory |
| Graph ingest fixtures / import data | `data/graph/` | Graph owners | Canonical per v13 blueprint; not confirmed in repo |
| API boundary | `src/server/` | API owners | Sole graph access path for UI clients |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Describes what belongs in `src/graph/` vs outside it
- [ ] Invariants captured (pipeline ordering + API boundary rules)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated


## 🗂️ Directory Layout

### This document
- `path`: `src/graph/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| ETL / pipelines | `src/pipelines/` | deterministic transforms; outputs land under `data/**` |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC items/collections, DCAT datasets, PROV bundles |
| Graph | `src/graph/` + `data/graph/` | ontology-governed ingest + import fixtures |
| API boundary | `src/server/` | OpenAPI/GraphQL contracts + graph query services |
| Frontend | `web/` | React + map client; **must not** query Neo4j directly |

### Expected file tree for this sub-area

> Note: aside from `README.md`, the subfolders below are **recommended** structure; exact presence is not confirmed in repo.

~~~text
📁 src/graph/
├── 📄 README.md
├── 📁 ingest/                   # recommended: STAC/DCAT/PROV → Neo4j loaders
├── 📁 ontology/                 # recommended: label/relationship mappings + constants
├── 📁 constraints/              # recommended: uniqueness + required-property constraints
├── 📁 migrations/               # recommended: ordered Cypher migrations/backfills
└── 📁 tests/                    # recommended: graph integrity tests + fixtures
~~~


## 🧭 Context

### Background
KFM uses a **Neo4j property graph** (nodes + labeled relationships) to represent people, places, events, documents, organizations, artifacts, and their provenance-linked connections. The graph is designed with ontology discipline, and can be modeled with semantic-web compatibility in mind even when stored as a property graph.

### Assumptions
- Graph ingest consumes the outputs of **STAC/DCAT/PROV** stages (catalogs and provenance bundles).
- Graph results are surfaced to users via the **API layer**, not direct database access.

### Constraints / invariants
- **Pipeline ordering is preserved:** ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.
- **No UI direct-to-graph reads:** the frontend must never query Neo4j directly; all access goes through the API boundary.
- **Stable labels/edges:** changes to node labels or relationship types require ontology updates and (when needed) migrations.
- **Data outputs are not code:** derived datasets and import fixtures belong under `data/**` (e.g., `data/graph/`), not under `src/`.
- **Provenance must remain linkable:** graph ingest should preserve references to dataset IDs / item IDs / run IDs so that downstream narrative remains auditable.
- **Sovereignty + sensitivity:** do not infer or publish sensitive locations; implement redaction/generalization at the API boundary when applicable.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical ontology spec stored (`docs/graph/...` vs `docs/standards/...`)? | Graph + governance | TBD |
| What is the standard migration format (naming, ordering, rollback policy)? | Graph owners | TBD |
| What graph integrity tests are required for “CI green”? | Contracts owners | TBD |

### Future extensions
- Linked-data export (RDF) for interoperability (if governance allows)
- Temporal modeling enhancements (time-aware relationships, validity ranges)
- Entity-resolution workflows that remain conservative + auditable


## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Neo4j Graph<br/>src/graph + data/graph]
  C --> D[API Boundary<br/>src/server]
  D --> E[UI<br/>web]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Sequence diagram (UI ↔ API ↔ Graph)
~~~mermaid
sequenceDiagram
  participant UI as Web UI (web/)
  participant API as API Boundary (src/server/)
  participant G as Neo4j Graph

  UI->>API: Request (entity, focus, search)
  API->>G: Query (with redaction rules + provenance)
  G-->>API: Subgraph + provenance refs
  API-->>UI: Contracted payload (no raw graph leakage)
~~~


## 📦 Data & Metadata

### Inputs to graph ingest
- **STAC**: item/collection metadata (spatiotemporal footprint, assets)
- **DCAT**: dataset-level records (grouping, discovery metadata)
- **PROV**: run-level lineage (activities/agents, generated outputs)

### Outputs / fixtures
- **Neo4j database** (deployed runtime instance)
- Optional **import fixtures** under `data/graph/` for deterministic loads/migrations (not confirmed in repo)


## 🧱 Graph modeling guide (high-level)

### Core entity labels (illustrative)
Common KFM entity labels include:
- `Place`, `Person`, `Event`, `Document`, `Organization`, `Artifact`

### Common relationship patterns (illustrative)
Examples of frequently used relationship semantics:
- `located_in` (Place → Place/Region)
- `happened_at` (Event → Place)
- `mentions` (Document → Person/Place/Event)
- `derives_from` (Entity → Source / Provenance link)

> This README does not replace the governed ontology. Treat labels/relationships as **ontology-controlled**; if you need a new type, follow the change process below.


## 🛠️ Change process

### Adding a new label or relationship type
1. Update the canonical ontology documentation (location: not confirmed in repo).
2. Add/adjust graph constraints (uniqueness, required properties).
3. Create a migration/backfill plan:
   - new relationship type introduction (safe)
   - label split/rename (may require version bump + compatibility plan)
4. Update ingest mapping (catalog fields → graph properties).
5. Add tests + fixtures proving:
   - idempotence (re-running ingest does not create duplicates)
   - constraints hold
   - provenance references remain attached
6. If API payloads change, update API contracts and contract tests at the API boundary.


## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (as applicable)
- [ ] Schema validation (STAC/DCAT/PROV) for any catalog inputs used by ingest
- [ ] Graph integrity checks (constraints + basic queries)
- [ ] API contract tests (if graph changes surface via endpoints)
- [ ] Security and sovereignty checks (if sensitive data could be exposed)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate catalogs (STAC/DCAT/PROV)
# 2) run graph unit/integration tests
# 3) run doc lint / markdown checks
~~~


## ⚖ FAIR+CARE & Governance

### Review gates
- Graph schema changes that affect public APIs or Story/Focus outputs should trigger governance review.
- Any data layer that could expose restricted or culturally sensitive locations requires explicit handling rules.

### CARE / sovereignty considerations
- If graph content could reveal restricted sites, prefer:
  - generalization, redaction, or omission in public outputs
  - documented rationale and reviewers

### AI usage constraints
- This document permits summarization/structuring/translation/keyword indexing.
- This document prohibits generating new policy or inferring sensitive locations (see front-matter).


## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `src/graph/` README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
