---
title: "Graph Ingest — README"
path: "src/graph/ingest/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:src:graph:ingest:readme:v1.0.0"
semantic_document_id: "kfm-src-graph-ingest-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:graph:ingest:readme:v1.0.0"
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

# Graph Ingest — README

## 📘 Overview

### Purpose
This README documents the contracts and contributor expectations for `src/graph/ingest/`, the subsystem responsible for ingesting **STAC/DCAT/PROV** catalog artifacts into the **Neo4j knowledge graph**, mapping records to the KFM ontology, and preserving provenance and governance metadata.

### Scope

| In Scope | Out of Scope |
|---|---|
| STAC/DCAT/PROV parsing for graph ingest | Raw source acquisition |
| Ontology mapping (labels/relations/properties) | Upstream ETL normalization/cleaning |
| Neo4j upsert/merge semantics | API contract definition (handled in `src/server/`) |
| Provenance linkage (Activity/Agent, derived-from) | Frontend rendering / map styling |
| Entity resolution + confidence scoring (if implemented here) | Story Node authoring / editorial |

### Audience
- Primary: Graph + pipeline engineers working on ingest, ontology bindings, and migrations.
- Secondary: API/UI contributors who need to understand graph shape, provenance references, and sensitivity handling.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: STAC, DCAT, PROV-O, Neo4j, ontology mapping, entity resolution, provenance.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Docs | Pipeline invariants + repo map |
| Architecture overview | `docs/architecture/` (PDFs) | Docs | Path may vary by repo; confirm location |
| STAC catalogs | `data/stac/` | Pipelines | Collections + items (validated) |
| DCAT catalogs | `data/catalog/dcat/` | Pipelines | RDF (Turtle/JSON-LD) records |
| PROV bundles | `data/prov/` | Pipelines | JSON-LD provenance |
| Graph contracts | `src/graph/` | Graph | Ontology bindings, migrations/constraints |
| API boundary | `src/server/` | API | Contracted access; UI does not query Neo4j directly |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Describes ingest purpose + contract boundaries (Graph vs API vs UI)
- [ ] Inputs/outputs + validation steps listed and repeatable
- [ ] Provenance + “no unsourced narrative” expectations are explicit
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Any entity resolution / merge behavior includes auditability guidance

## 🗂️ Directory Layout

### This document
- `path`: `src/graph/ingest/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Graph ingest | `src/graph/ingest/` | Catalog → graph ingestion logic |
| Graph core | `src/graph/` | Ontology bindings, migrations/constraints, graph build |
| Pipelines | `src/pipelines/` | ETL + catalog build + graph build orchestration |
| Data domains | `data/` | Raw/work/processed outputs (including STAC/DCAT/PROV) |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| MCP runs | `mcp/runs/` | Run logs, experiment artifacts, manifests |
| APIs | `src/server/` | REST/GraphQL contracted access layer |
| Frontend | `web/` | React + MapLibre UI, Focus Mode |

### Expected file tree for this sub-area
> NOTE: This is the **intended** organization. Align to what already exists in-repo.

~~~text
📁 src/
└── 📁 graph/
    └── 📁 ingest/
        ├── 📄 README.md
        ├── 📁 mappers/                # (recommended) STAC/DCAT/PROV → ontology objects
        ├── 📁 writers/                # (recommended) Neo4j upserts + batching
        ├── 📁 provenance/             # (recommended) PROV → Activity/Agent links
        ├── 📁 entity_resolution/      # (recommended) dedupe/merge w/ confidence + audit hooks
        └── 📁 cypher/                 # (recommended) constraints/migrations snippets
~~~

## 🧭 Context

### Background
KFM produces standard metadata catalogs (STAC, DCAT, PROV) during ETL/catalog stages and then ingests them into a Neo4j graph. The graph layer models core entities (e.g., Place, Person, Event, Document, Organization, Artifact) and relations (e.g., `located_in`, `happened_at`, `mentions`, `derives_from`). Provenance is first-class: ingested nodes should retain traceability back to source records and processing steps.

### Assumptions
- STAC/DCAT/PROV artifacts are generated upstream and have passed schema validation.
- Neo4j connectivity is available to the ingest runtime (connection details are repo-specific).
- Graph schema constraints and migrations exist (location is repo-specific).
- Ingest behavior is **deterministic and idempotent**: re-running on the same inputs should not create duplicates and should be reproducible.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No unsourced narrative: Focus Mode/story contexts must reference evidence/provenance IDs.
- Governance metadata (classification tags, sensitivity labels) must be preserved through ingest.
- If entity merges are automated, they must be logged and reviewable (human-in-the-loop for critical merges).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical ingest entrypoint (CLI/module) that drives this directory? | Graph | TBD |
| Where are Neo4j constraints/migrations defined and how are they applied in CI? | Graph | TBD |
| What are the configured entity-resolution thresholds (auto-merge vs review)? | Graph + Governance | TBD |
| Where are ingest run logs written (`mcp/runs/` vs telemetry docs), and what schema governs them? | Pipelines + Telemetry | TBD |

### Future extensions
- Incremental ingest (diff-based updates) with reproducible run manifests.
- Additional domain mappers (new STAC collections / DCAT datasets).
- More robust entity resolution features (temporal + spatial constraints; richer evidence capture).
- Automated graph integrity dashboards (constraints coverage; provenance completeness).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A["ETL + Normalization"] --> B["STAC/DCAT/PROV Catalogs"]
  B --> C["Graph Ingest"]
  C --> D["Neo4j Graph"]
  D --> E["APIs (REST/GraphQL)"]
  E --> F["React/Map UI"]
  F --> G["Story Nodes"]
  G --> H["Focus Mode"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC Collections + Items | `application/json` | `data/stac/` | STAC 1.0 + KFM-STAC profile |
| DCAT dataset catalog | RDF (Turtle/JSON-LD) | `data/catalog/dcat/` | DCAT 3 + KFM-DCAT profile |
| PROV bundles | JSON-LD | `data/prov/` | PROV-O + KFM-PROV profile |
| Entity-resolution config (optional) | YAML/JSON | `src/graph/ingest/` (repo-specific) | Schema (TBD) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Neo4j nodes + relationships | Graph DB | Neo4j | KFM ontology bindings + migrations |
| Provenance subgraph (Activity/Agent edges) | Graph DB | Neo4j | PROV profile mapping |
| Ingest run log / manifest | JSON | `mcp/runs/<run_id>/` | Telemetry schema (TBD) |
| Validation / audit report | MD/JSON | `mcp/runs/<run_id>/` (recommended) | Telemetry schema (TBD) |

### Sensitivity & redaction
- Preserve and propagate classification tags and sensitivity labels for all ingested entities and assets.
- Precise locations for protected sites (or similarly sensitive records) must be governed by classification/sensitivity metadata and downstream enforcement rules (typically at the API layer).

### Quality signals
- Completeness: required IDs, titles/names, time ranges, and provenance pointers present.
- Geometry validity (if geospatial): valid GeoJSON, sane bounds, coordinate reference consistency.
- Referential integrity: relationships point to existing nodes; no orphaned provenance.
- Deduplication health (if entity resolution enabled): number of candidate matches, merge confidence distributions, and human-review backlog.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: see `data/stac/collections/` (repo-specific inventory)
- Items involved: see `data/stac/items/` (repo-specific inventory)
- Extension(s): KFM-STAC + domain-specific extensions (confirm in schema registry)

### DCAT
- Dataset identifiers: map DCAT identifiers into stable graph keys (Dataset nodes and/or properties on relevant nodes).
- License mapping: carry forward license metadata for downstream display and reuse constraints.
- Contact / publisher mapping: map publishers/contacts into `Organization` nodes when appropriate.

### PROV-O
- `prov:wasDerivedFrom`: connect ingested entities/assets back to source records.
- `prov:wasGeneratedBy`: connect to `Activity` nodes representing ETL/ingest jobs.
- Activity / Agent identities: Agents can represent scripts, services, or persons; IDs must be stable and recorded for audit.

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.

## 🏗️ Architecture

### Component map (within `src/graph/ingest/`)
- Catalog readers/parsers: STAC JSON, DCAT RDF/JSON-LD, PROV JSON-LD.
- Ontology mapping: translate catalog records into graph nodes/edges (labels/relations/properties).
- Writers/upserters: Neo4j transactional writes, batching, idempotent upserts.
- Provenance writer: Activity/Agent modeling; derived-from edges.
- Entity resolution (optional): detect duplicates; propose/perform merges; record confidence + rationale.
- Validation: pre-flight schema checks + post-flight graph integrity checks.
- Run logging: record run inputs, versions, counts, and audit signals in run artifacts.

### Interfaces / contracts
- Input contracts: STAC 1.0 (KFM-STAC), DCAT 3 (KFM-DCAT), PROV-O (KFM-PROV).
- Graph contract: stable labels/relations + migration plan (no breaking changes without versioning).
- API boundary: UI must rely on API contracts, not direct Neo4j reads.
- Auditability: provenance + merge decisions must be queryable and traceable.

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests (if graph shape changes surface outward)
- [ ] UI: layer registry entry + access rules (if new data becomes visible)
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Entities that become focusable typically include: Place, Person, Event, Organization, Document, Artifact (as defined by the graph ontology).
- For every focus bundle, evidence must include:
  - pointers to STAC asset IDs and/or source Document nodes
  - DCAT dataset identifiers (where applicable)
  - PROV Activity/Agent references for “how it got here”

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls

~~~yaml
focus_layers:
  - "places"
  - "events"
  - "documents"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (constraints, uniqueness, referential integrity)
- [ ] Entity-resolution audit checks (if auto-merge is enabled)
- [ ] API contract tests (if ingest changes the surfaced graph shape)
- [ ] UI schema checks (layer registry) (if new data becomes visible)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate catalog artifacts (STAC/DCAT/PROV)
# <cmd>

# 2) run graph ingest (dry run / plan)
# <cmd>

# 3) apply constraints/migrations and ingest into Neo4j
# <cmd>

# 4) run graph integrity tests
# <cmd>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| ingest_run_id | Graph ingest | `mcp/runs/` (recommended) |
| nodes_written / relationships_written | Graph ingest | `mcp/runs/` (recommended) |
| entity_resolution_candidates / merges_applied | Entity resolution | `mcp/runs/` (recommended) |
| validation_failures | Validators | `mcp/runs/` + telemetry docs |

## ⚖ FAIR+CARE & Governance

### Review gates
- Ontology changes (labels/relations/properties) require Graph maintainer review.
- Any change that affects sensitive-location handling, classification propagation, or merge behavior requires governance review (as defined in governance docs).

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- Ensure classification tags and sensitivity labels are present and enforceable.
- Follow sovereignty/ethics policy documents for restricted or culturally sensitive content.

### AI usage constraints
- If AI is used to propose links/merges, ensure:
  - transparency: confidence + rationale are stored
  - auditability: machine vs human decisions are distinguishable
  - human-in-the-loop: critical merges are reviewable before acceptance
- Ensure this doc’s AI permissions/prohibitions match intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for `src/graph/ingest/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`