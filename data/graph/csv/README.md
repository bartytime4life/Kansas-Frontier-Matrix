---
title: "KFM Graph Import CSVs — README"
path: "data/graph/csv/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:data:graph:csv-readme:v1.0.0"
semantic_document_id: "kfm-data-graph-csv-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:graph:csv-readme:v1.0.0"
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

# KFM Graph Import CSVs

## 📘 Overview

### Purpose

- This README defines what belongs in `data/graph/csv/` and how these artifacts fit into the KFM canonical pipeline.
- This directory is the canonical home for **Neo4j loader import CSVs** produced by the **Graph build** stage (import artifacts only; not UI-facing).

### Scope

| In Scope | Out of Scope |
|---|---|
| Folder purpose + expectations for CSV import artifacts | Neo4j deployment/runtime configuration |
| Relationship to catalog + provenance identifiers (STAC/DCAT/PROV) | API contract definitions (`src/server/contracts/**`) |
| Quality, determinism, and sensitivity expectations for import artifacts | Story Node authoring and publish workflow |

### Audience

- Primary: graph/ontology maintainers; pipeline engineers generating import artifacts.
- Secondary: debuggers and curators inspecting graph ingest inputs.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Graph import CSVs**: CSV files formatted for Neo4j bulk load or scripted ingestion.
  - **Neo4j loader**: the import tool/process that consumes CSVs and writes the Neo4j store.
  - **Evidence identifiers**: STAC Item/Collection IDs, DCAT dataset IDs, PROV activity IDs.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Graph import CSVs | `data/graph/csv/` | Graph build | This directory |
| Graph import Cypher | `data/graph/cypher/` | Graph build | Loader scripts / migrations / glue logic (if used) |
| Graph build code | `src/graph/` | Graph maintainers | Generates graph import artifacts |
| STAC catalogs | `data/stac/**` | Catalog stage | Evidence referenced by graph entities |
| DCAT records | `data/catalog/dcat/**` | Catalog stage | Dataset identifiers referenced by graph entities |
| PROV bundles | `data/prov/**` | Pipeline + catalog | Lineage referenced by graph entities and Focus Mode |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory purpose + boundaries clearly stated
- [ ] Expected file tree shown for this sub-area
- [ ] Validation steps listed and repeatable (even if placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `data/graph/csv/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/<domain>/{raw,work,processed}/` | Domain data lifecycle outputs |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | STAC/DCAT/PROV artifacts used as evidence + lineage |
| Graph build code | `src/graph/` | Graph build + ontology bindings |
| Graph import artifacts | `data/graph/` | Import-ready artifacts (CSV + Cypher) |
| API boundary | `src/server/` | Contracts and redaction enforced here |
| UI | `web/` | API consumers only (no direct Neo4j reads) |
| Story Nodes | `docs/reports/story_nodes/**` | Narrative artifacts linked to graph + evidence |

### Expected file tree for this sub-area

~~~text
📁 data/
└── 📁 graph/
    ├── 📁 csv/
    │   ├── 📄 README.md
    │   ├── 📄 <generated_node_csvs>.csv
    │   ├── 📄 <generated_relationship_csvs>.csv
    │   └── 📄 <optional_import_manifest>.json
    └── 📁 cypher/
        ├── 📄 <optional_loader_scripts>.cypher
        └── 📄 <optional_migrations>.cypher
~~~

## 🧭 Context

### Background

KFM preserves a non-negotiable system ordering:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.

`data/graph/csv/` exists to hold the **graph import CSV artifacts** that allow the graph build stage to materialize (or update) the Neo4j database in a repeatable way.

### Assumptions

- CSV import artifacts here are **build outputs** (generated), not hand-authored narratives.
- Graph entities should carry **references back to STAC/DCAT/PROV identifiers** to preserve evidence-first behavior.
- Any sensitivity controls required for restricted locations or culturally sensitive knowledge must be enforced consistently (see Governance section).

### Constraints / invariants

- The canonical pipeline ordering is preserved.
- UI consumers never read Neo4j directly; the API boundary is the only contract surface.
- Graph ingest should be derived from **processed** domain outputs plus catalog/provenance artifacts (STAC/DCAT/PROV), not from raw snapshots.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical CSV schema (required columns) for each label/relationship? | TBD | TBD |
| Where is the authoritative mapping from STAC/DCAT/PROV IDs into node/edge properties defined? | TBD | TBD |
| Should this directory store only build outputs, or also checked-in fixtures/samples for tests? | TBD | TBD |

### Future extensions

- Add `schemas/graph/csv/**` to validate import CSV structure (columns/types) in CI.
- Add a small, synthetic “vertical slice” dataset fixture for import regression tests.
- Add a manifest format (if adopted) that records: producing run ID, input artifact IDs, row counts, and checksums.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL outputs<br/>data/&lt;domain&gt;/processed] --> B[Catalog outputs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph build<br/>src/graph]
  C --> D[Import artifacts<br/>data/graph/csv]
  D --> E[Neo4j loader]
  E --> F[Neo4j Graph]
  F --> G[API boundary<br/>src/server]
  G --> H[UI<br/>web]
  H --> I[Story Nodes<br/>docs/reports/story_nodes]
  I --> J[Focus Mode<br/>provenance-linked only]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Build as GraphBuild
  participant CSV as data/graph/csv
  participant Loader as Neo4jLoader
  participant Graph as Neo4j
  Build->>CSV: write import CSVs (nodes + rels)
  Build->>CSV: write optional manifest (counts/checksums)
  Loader->>CSV: read import CSVs
  Loader->>Graph: load nodes/relationships (+ provenance refs)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Processed domain outputs | CSV/GeoJSON/etc. | `data/<domain>/processed/` | Domain schema/geo checks (domain-specific) |
| STAC catalogs | JSON (STAC) | `data/stac/**` | STAC schema validation |
| DCAT records | JSON-LD/RDF | `data/catalog/dcat/**` | DCAT profile validation |
| PROV bundles | JSON-LD | `data/prov/**` | PROV profile validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Graph import CSVs (nodes + rels) | CSV | `data/graph/csv/**` | CSV schema (TBD / not confirmed in repo) |
| Optional import manifest | JSON | `data/graph/csv/<manifest>.json` | Manifest schema (TBD / not confirmed in repo) |

### Sensitivity & redaction

- Import artifacts must not bypass governance constraints:
  - if restricted locations require generalization, those transformations must be applied consistently,
  - API-level redaction/generalization remains the contract boundary for UI delivery,
  - any sensitive assets/locations used to build the graph must be tracked and auditable via provenance.

### Quality signals

- Deterministic runs and diffable outputs (CSV changes should be explainable via provenance/run IDs).
- No orphan references:
  - evidence IDs referenced in import outputs must resolve to STAC/DCAT/PROV artifacts.
- Basic integrity checks:
  - stable identifiers for nodes/relationships,
  - relationship endpoints exist,
  - expected label/relationship sets are present for the build target.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: determined by the build target (see `data/stac/collections/**`).
- Items involved: determined by the build target (see `data/stac/items/**`).
- Extension(s): TBD (as needed by KFM STAC profile).

### DCAT

- Dataset identifiers: determined by the build target (see `data/catalog/dcat/**`).
- License mapping: tracked in DCAT records and/or STAC metadata.
- Contact / publisher mapping: tracked in DCAT records.

### PROV-O

- `prov:wasDerivedFrom`: graph entities/edges should reference upstream evidence artifacts.
- `prov:wasGeneratedBy`: graph build activities should be represented in provenance records where applicable.
- Activity / Agent identities: recorded by pipeline and/or graph build tooling (TBD).

### Versioning

- Use catalog versioning links and graph predecessor/successor relationships when versions change (TBD: concrete mechanism).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Domain pipeline configs + run logs |
| Catalogs | STAC/DCAT/PROV generation | JSON/JSON-LD artifacts + validators |
| Graph build | Produce import artifacts | CSV (+ optional Cypher) |
| Neo4j loader | Consume import artifacts | Bulk import / scripted import |
| Neo4j graph | Queryable knowledge base | Accessed only via API boundary |
| APIs | Serve contracts + enforce redaction | REST/GraphQL contracts |
| UI | Map + narrative | API calls only |
| Story Nodes | Curated narrative | Graph IDs + evidence IDs |
| Focus Mode | Provenance-linked context view | Provenance-aware bundles |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API contracts | `src/server/contracts/` | Contract tests required |
| Graph import CSV schema | `schemas/graph/csv/` | (TBD / not confirmed in repo) |

### Extension points checklist (for future work)

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Entities created via graph import become focusable only when they can present provenance-linked evidence.
- Focus Mode should be able to trace displayed facts back to STAC/DCAT/PROV identifiers represented in the graph.

### Provenance-linked narrative rule

- Every claim surfaced to users must trace to a dataset / record / asset ID.
- Graph ingest must preserve the evidence pointers required for Story Nodes and Focus Mode.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (node/edge referential integrity)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas
# (stac/dcat/prov)

# 2) run graph build to emit CSV import artifacts
# (graph build tooling emits into data/graph/csv/)

# 3) run loader/import step (local/dev)
# (neo4j loader consumes data/graph/csv/**)

# 4) run integrity checks
# (relationships resolve, evidence IDs present, etc.)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Graph build run ID | Graph build tooling | `data/prov/**` and/or `mcp/runs/**` (TBD) |
| Import artifact checksums | Build manifest | `data/graph/csv/<manifest>.json` (TBD) |
| Integrity check results | CI | CI logs (TBD) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that affect what gets imported into Neo4j, or how evidence/provenance is represented, require human review (TBD: role owners).
- Any changes involving sensitive locations or culturally sensitive knowledge require governance review per policy docs.

### CARE / sovereignty considerations

- Do not expose restricted locations or culturally sensitive knowledge in ways that violate sovereignty requirements.
- Ensure any generalization/redaction requirements are respected and auditable (e.g., via provenance).

### AI usage constraints

- Ensure doc’s AI permissions/prohibitions match intended use (see front-matter).
- Prohibited: generating new policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for graph import CSV directory | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
