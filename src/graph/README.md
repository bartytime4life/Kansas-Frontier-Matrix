---
title: "KFM — src/graph (README)"
path: "src/graph/README.md"
version: "v0.1.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:src:graph:readme:v0.1.0"
semantic_document_id: "kfm-src-graph-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:src:graph:readme:v0.1.0"
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

# src/graph

## 📘 Overview

### Purpose
`src/graph/` implements the **Graph stage** of the KFM pipeline: transforming cataloged assets into a governed Neo4j knowledge graph, aligned with the KFM ontology and provenance rules.

Canonical pipeline (do not break):
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

### Scope

| In Scope | Out of Scope |
|---|---|
| Graph ingestion from STAC/DCAT/PROV-derived artifacts | Raw ingestion/parsing of source files (ETL stage) |
| Ontology bindings (labels, relations), constraints, migrations | UI rendering and map layer UX |
| Provenance linkage in-graph (PROV Activity/Agent patterns) | Direct UI access to Neo4j (API boundary invariant) |
| Graph integrity tests + fixtures | API contract definitions (owned by API layer docs/code) |

### Audience
- Primary: graph engineers, backend engineers, data engineers
- Secondary: historians/editors validating entity linkage + provenance

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: STAC, DCAT, PROV-O, Neo4j, ontology, provenance, entity resolution

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Source of truth for ordering + subsystem boundaries |
| Graph docs | `docs/graph/` | Graph maintainers | Ontology + migration notes (not confirmed in repo) |
| Catalog inputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | DataOps | Graph ingests from catalog outputs |
| API boundary | `src/server/` + API docs | Backend | UI must not talk to Neo4j directly |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Graph stage responsibilities and boundaries stated
- [ ] Inputs/outputs described in terms of catalog + provenance contracts
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `src/graph/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts used as graph inputs |
| Graph | `src/graph/` | Graph ingest, ontology bindings, migrations, graph tests |
| Schemas | `schemas/` | STAC/DCAT/PROV + telemetry schemas (graph depends on validation) |
| APIs | `src/server/` | Contracted access layer (no UI → Neo4j direct access) |
| Frontend | `web/` | Map UI + Focus Mode UI |
| Tests | `tests/` | Integration tests and contract tests (graph integrity may live here) |

### Expected file tree for this sub-area
> This is a **conventional** layout for this directory; exact filenames may vary (not confirmed in repo).

~~~text
📁 src/graph/
├── 📄 README.md
├── 📁 ontology/
│   ├── 📄 README.md
│   └── 📄 <ontology-spec>.<yml|json|md>
├── 📁 ingest/
│   └── 📄 ingest_<source>_to_neo4j.py
├── 📁 migrations/
│   └── 📄 0001__<change>.cypher
├── 📁 queries/
│   └── 📄 <named_query>.cypher
└── 📁 tests/
    └── 📄 test_graph_<topic>.py
~~~

## 🧭 Context

### Background
KFM’s knowledge graph represents entities (e.g., places, people, events, documents, organizations, artifacts) and their relationships, and ingests cataloged metadata outputs (STAC/DCAT/PROV) into Neo4j rather than loading raw sources directly.

### Assumptions
- STAC, DCAT, and PROV artifacts are generated upstream and validated before graph ingest.
- The graph is served through the API layer; the UI consumes only API contracts (no direct graph access).
- Graph content is provenance-linked: every claim must trace back to a catalog/document identifier.

### Constraints / invariants
- Preserve the pipeline ordering: ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary:** UI never reads Neo4j directly; contracts live at the API layer.
- Provenance is first-class: graph nodes must link to source IDs and PROV activities/agents where applicable.
- Deterministic/idempotent runs: graph ingest should be replayable and not duplicate nodes.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the canonical ontology spec stored (repo path + format)? | TBD | TBD |
| What is the preferred graph migration mechanism (Cypher files, tool, or code-first)? | TBD | TBD |
| What node/edge ID stability rules are enforced (hashing/UUID/semantic IDs)? | TBD | TBD |

### Future extensions
- Add explicit “candidate sites” or “evidence artifacts” node types with provenance-first linkage.
- Add graph-to-API “context bundle” exports for Focus Mode, including citations + audit flags.

## 🗺️ Diagrams

### System / dataflow diagram (graph stage highlighted)

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph: src/graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram (API boundary)

~~~mermaid
sequenceDiagram
  participant UI as UI (React/Map)
  participant API as API Layer
  participant Graph as Neo4j Graph
  UI->>API: request focus bundle (entity_id)
  API->>Graph: query subgraph + provenance refs
  Graph-->>API: results + source IDs
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC Collections + Items | JSON | `data/stac/collections/` + `data/stac/items/` | STAC schema validation |
| DCAT dataset views | JSON-LD / Turtle | `data/catalog/dcat/` | DCAT profile validation |
| PROV lineage bundles | JSON-LD | `data/prov/` | PROV profile validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Neo4j graph state | DB | (runtime) | Graph constraints + integrity tests |
| Graph snapshots/exports (optional) | JSON/CSV | `data/processed/` or `mcp/runs/` | (define schema; not confirmed in repo) |
| Error/audit logs (optional) | JSON | `mcp/runs/` | telemetry schema (not confirmed in repo) |

### Sensitivity & redaction
- Content classification and sensitivity labels should be enforced end-to-end.
- If a node contains sensitive locations, apply generalization/redaction rules before serving to public clients.

### Quality signals
- Schema-valid inputs (STAC/DCAT/PROV).
- Stable IDs and deduplication checks (entity resolution rules).
- Relationship integrity checks (no dangling references; expected edge types only).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Graph nodes derived from STAC Items should retain:
  - STAC Item ID(s)
  - asset links / checksums (when applicable)
  - spatial/temporal extents (when applicable)

### DCAT
- Dataset-level groupings in DCAT may map to:
  - grouping nodes, tags, or annotations in the graph
  - publisher/license metadata for downstream UI display

### PROV-O
- Graph should represent provenance relationships using PROV patterns:
  - `prov:wasDerivedFrom` links from graph entities to source entity IDs
  - `prov:wasGeneratedBy` links from entities to Activities (ETL runs, transforms)
  - Activities link to Agents (scripts, contributors) with explicit IDs

### Versioning
- Graph lineage should mirror dataset versioning (predecessor/successor) when catalog artifacts publish versions.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Graph ingest | Build nodes/edges from catalogs | Input: STAC/DCAT/PROV JSON; Output: Neo4j |
| Ontology bindings | Define labels, edge types, property conventions | Docs + validation rules |
| Constraints/migrations | Enforce invariants + evolve schema | Cypher migrations + tests |
| Entity resolution | Link/merge duplicates with confidence + review hooks | Rule set + audit logs |
| Exports (optional) | Produce API-friendly bundles | JSON schema + contract tests |

### Interfaces / contracts
- Graph is queried only by the API layer. UI receives contracted payloads (no direct Neo4j access).
- Any Focus Mode payload must carry provenance references and sensitivity flags.

### Extension points checklist (for future work)
- [ ] Graph: add new labels/relations mapped + migration plan
- [ ] PROV: ensure activity + agent IDs recorded in-graph
- [ ] APIs: add/extend endpoints and contract tests (if graph changes require it)
- [ ] UI: render new entity types via API contracts only
- [ ] Telemetry: log ingest runs + validation outcomes with schema versioning

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode should operate on **provenance-linked context bundles** assembled from the graph and source catalogs.
- Every narrative claim must trace to dataset/record/asset IDs.

### Provenance-linked narrative rule
- No unsourced narrative: story nodes and Focus Mode outputs must include citations back to STAC/DCAT/PROV + document IDs.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (constraints + sample queries)
- [ ] API contract tests (if graph-facing payloads change)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction (placeholders)
~~~bash
# NOTE: Exact commands are repo-specific (not confirmed in repo)

# 1) Validate catalog artifacts (STAC/DCAT/PROV)
# <repo-command> validate-catalogs

# 2) Run graph ingest from catalogs
# <repo-command> graph-ingest --from data/stac --prov data/prov --dcat data/catalog/dcat

# 3) Run graph integrity tests
# <repo-command> test graph
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Ontology changes: requires human review (graph maintainer + historian/editor).
- Any change that affects sensitive locations or restricted datasets: requires governance review.

### CARE / sovereignty considerations
- Ensure restricted/sensitive spatial data is not exposed in public outputs.
- Follow `docs/governance/SOVEREIGNTY.md` rules when modeling culturally sensitive entities.

### AI usage constraints
- AI-generated inferences must be labeled as such and must not infer sensitive locations.
- Any model-driven merges/links should carry confidence and support human review.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-19 | Initial scaffolding for `src/graph` README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`