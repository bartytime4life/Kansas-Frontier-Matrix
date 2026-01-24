---
title: "KFM — data/graph/csv/ (Neo4j Import CSVs)"
path: "data/graph/csv/README.md"
version: "v1.0.0"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:data:graph:csv:readme:v1.0.0"
semantic_document_id: "kfm-data-graph-csv-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:graph:csv:readme:v1.0.0"
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

# KFM — `data/graph/csv/` (Neo4j Import CSVs)

> **Purpose (required):** Define the folder-level contract for **graph import CSV artifacts** used to load/update the KFM Neo4j graph. This includes what belongs in this directory, minimum structural expectations (stable IDs, referential integrity), and how these artifacts must remain traceable to **STAC/DCAT/PROV** evidence and governance constraints.

## 📘 Overview

### What this directory is
`data/graph/csv/` is the canonical location for **generated, import-ready CSV tables** representing:
- **Node tables** (entities: Place, Person, Event, Document, Organization, Artifact, etc.)
- **Relationship tables** (edges between entities)

These CSVs are consumed by the **Graph stage** of the canonical pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

### What this directory is not
This directory must **not** contain:
- Graph build source code (belongs under `src/graph/` or repo-defined equivalent)
- Ontology definitions and schema contracts (belongs under governed ontology/graph docs + `schemas/`)
- API code/contract artifacts (belongs under `src/server/`)
- UI code or configuration (belongs under `web/`)
- “Hand-edited” CSVs that drift from deterministic pipeline outputs

### Audience
- Primary: graph maintainers producing Neo4j load artifacts
- Secondary: ETL/catalog maintainers validating evidence linkage; reviewers validating governance boundaries

### Definitions
- Glossary: `docs/glossary.md` (not confirmed in repo)
- Terms used here:
  - **import CSV**: a tabular export intended for a Neo4j loader (bulk import or scripted load)
  - **stable ID**: an identifier that does not change between deterministic rebuilds
  - **referential integrity**: every relationship endpoint ID exists as a node ID
  - **evidence linkage**: references from graph rows to STAC/DCAT/PROV identifiers (directly or via joinable keys)

### Definition of done
- [ ] `path` matches the file location (`data/graph/csv/README.md`)
- [ ] CSV artifacts are clearly categorized (nodes vs relationships) and are loader-compatible
- [ ] Stable IDs are enforced; no blank identifiers
- [ ] Referential integrity checks exist (CI or reproducible local checks)
- [ ] Sensitive or restricted content is not leaked (or is generalized/redacted per governance)
- [ ] Evidence/provenance linkage is present (direct columns or documented join strategy)

## 🗂️ Directory Layout

### This document
- `path`: `data/graph/csv/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Graph import root | `data/graph/` | Import artifacts (CSV + optional Cypher) |
| Graph import CSVs | `data/graph/csv/` | Loader-ready CSVs (this folder) |
| Post-import scripts | `data/graph/cypher/` | Optional Cypher scripts to run after import |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Evidence + lineage artifacts |
| Graph subsystem | `src/graph/` | Ontology bindings, graph build, migrations (code) |
| Pipelines | `src/pipelines/` | ETL + catalog build; may also orchestrate graph exports |
| API boundary | `src/server/` | Contracted access to graph + catalogs (UI never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Evidence-led narratives |

### Expected tree (examples)

~~~text
data/
└── 🕸️ graph/
    ├── 🧱 csv/
    │   ├── 📄 README.md                 # 📘 CSV conventions: required columns, ID formats, and import command examples
    │   ├── 🧱📄 <nodes-table>.csv        # Node table (one label/set): node ids + properties (stable headers)
    │   ├── 🔗📄 <relationships-table>.csv # Relationship table: start/end ids + type + relationship properties
    │   └── ➕ …                          # Additional node/rel tables (date-stamped snapshots recommended)
    └── 🧠 cypher/
        ├── 📄 README.md                 # 📘 Cypher conventions: when to use, safe/idempotent patterns, and verification queries
        └── ✅🧠📄 <post-import>.cypher    # Post-import script (constraints checks, derived fields, sanity queries)
~~~

Notes:
- CSV naming conventions are **repo-local**. If the graph loader expects a specific naming scheme, document it in `src/graph/` and keep this README aligned.
- If subfolders (e.g., `nodes/`, `rels/`) are adopted, reflect that in the tree above (not confirmed in repo).

## 🧭 Context

### Background
KFM treats catalogs and provenance artifacts as evidence products. Graph imports must therefore:
- remain consistent with the governed ontology and canonical pipeline ordering
- preserve traceability to catalog and provenance IDs
- avoid “mystery duplicates” by keeping one canonical output location (`data/graph/csv/`)

### Constraints and invariants
- **API boundary:** the UI must not read Neo4j directly; graph access is via contracted APIs.
- **Determinism:** graph export reruns with unchanged inputs must yield stable, diffable outputs.
- **Governance:** restricted locations / culturally sensitive knowledge must be generalized or redacted before publication/consumption.

### Common failure modes to prevent
- Unstable IDs (random UUIDs regenerated each run) → breaks lineage and downstream caching.
- Missing relationship endpoints → import failures or dangling edges.
- CSVs edited by hand → drift from source-of-truth pipeline behavior.
- Sensitive coordinates included without controls → governance breach.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL outputs<br/>data/<domain>/processed] --> B[Catalog evidence<br/>STAC/DCAT/PROV]
  B --> C[Graph build/export<br/>src/graph]
  C --> D[Import CSVs<br/>data/graph/csv]
  D --> E[Neo4j graph]
  E --> F[API boundary<br/>src/server]
  F --> G[UI<br/>web]
  G --> H[Story Nodes<br/>docs/reports/story_nodes]
  H --> I[Focus Mode<br/>provenance-linked]
~~~

## 📦 Data & Metadata

### Inputs (conceptual)
The CSVs in this directory are typically generated from:
- `data/<domain>/processed/` (normalized domain outputs)
- `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` (evidence + lineage)
- governed ontology mappings (typically under `src/graph/` + standards/docs)

### Outputs (what lives here)
- **Node CSVs:** one or more tables representing graph nodes
- **Relationship CSVs:** one or more tables representing graph relationships

Optional (repo-defined; not confirmed in repo):
- manifest files (listing produced CSVs, row counts, checksums)
- integrity reports (referential integrity counts, orphan counts)

### Minimum CSV format expectations (directory-level)
These are folder-level expectations. The **exact** header schema must match your loader and ontology mappings.

- Encoding: UTF-8 (avoid BOM where possible)
- Delimiter: comma (`,`), unless loader requires otherwise (document any deviation)
- Header row: required
- Line endings: consistent (LF preferred)
- No blank IDs: every row must have its required identifier fields populated

### Minimum structural expectations (independent of loader choice)
**Node tables** should have:
- a stable primary key column (commonly `id`)
- label/type representation (explicit columns or loader-provided mapping)
- optional evidence/provenance reference columns (recommended)

**Relationship tables** should have:
- stable endpoint identifiers:
  - `source_id` (or equivalent)
  - `target_id` (or equivalent)
- a relationship type (explicit column or loader mapping)
- optional evidence/provenance reference columns (recommended)

### Evidence linkage columns (recommended)
To keep graph content audit-ready, include (or provide a join strategy for) the following identifiers when applicable:
- `stac_item_id` and/or `stac_collection_id`
- `dcat_dataset_id`
- `prov_activity_id` (run/build activity)
- `source_doc_id` (document registry ID, if applicable)

If these columns are not embedded in the CSVs, document where the linkage is defined (e.g., mapping config under `src/graph/`).

## 🌐 STAC, DCAT & PROV Alignment

### Rule of record
Graph entities and relationships that originate from datasets must remain traceable back to:
- **STAC** (asset-level spatiotemporal metadata)
- **DCAT** (dataset-level discovery metadata)
- **PROV** (lineage: inputs → activities → outputs)

### Practical linkage strategy
At minimum, ensure one of the following is true:
1) The CSV row includes evidence/provenance IDs directly, **or**
2) The CSV row includes stable keys that can be joined to catalog/provenance artifacts deterministically.

## 🧱 Architecture

### Responsibilities by layer

| Layer | Responsibility | Reads from | Writes to |
|---|---|---|---|
| Catalog stage | Produce evidence artifacts | `data/<domain>/processed/` | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Graph stage | Build/refresh graph | catalogs + processed outputs | `data/graph/csv/` (+ Neo4j) |
| API boundary | Serve contracted data | Neo4j + catalogs | API responses (no direct UI→Neo4j) |
| UI | Render maps/narratives | APIs only | UI views |
| Story Nodes | Evidence-led narrative | APIs + evidence IDs | published narrative docs |

### Why `data/graph/csv/` exists (contract boundary)
This folder makes graph ingestion:
- reproducible (artifacts are explicit)
- reviewable (diffable exports)
- testable (CI can lint CSVs + referential integrity)
- governable (sensitivity checks can run before import/exposure)

## 🧠 Story Node & Focus Mode Integration

### How this directory affects Story Nodes
Story Nodes should never cite CSV files directly as primary evidence. Instead:
- CSVs feed Neo4j
- Story Nodes cite the **evidence artifacts** (STAC/DCAT/PROV IDs) that the graph nodes reference

### Focus Mode rule
Focus Mode must only present content that can be traced to provenance-linked evidence. If graph entities are created without evidence linkage, Focus Mode must treat them as non-displayable or “uncited” until remediated.

## 🧪 Validation & CI/CD

### Minimum checks (recommended)
- [ ] CSV parse check (delimiter/quoting/header)
- [ ] Required columns present for each CSV type (as defined by loader + ontology mapping)
- [ ] Stable IDs: no blank IDs; uniqueness where expected
- [ ] Referential integrity: every relationship endpoint ID exists in node tables
- [ ] Determinism: stable ordering and stable identifiers across identical rebuilds
- [ ] Governance scans: ensure restricted/sensitive locations are generalized/redacted
- [ ] Security scans: secret/PII scanning on artifacts (if artifacts are committed)

### Reproduction (placeholders)
~~~bash
# Placeholder only — replace with repo-specific commands:
# 1) Build graph export artifacts
# <command>

# 2) Run CSV validation + referential integrity checks
# <command>

# 3) (Optional) Load into a test Neo4j instance and run smoke tests
# <command>
~~~

## ⚖ FAIR+CARE & Governance

### Sensitivity and sovereignty safeguards
- Do not publish or expose protected locations or culturally sensitive knowledge in import CSVs unless policy explicitly allows.
- When restriction applies, generalize geometry and/or redact attributes before export, and ensure the API layer enforces access constraints.

### AI usage constraints
- AI must not infer sensitive locations from artifacts.
- Any AI-authored narrative content must be provenance-linked and audit-ready (downstream rule; included here for cross-layer clarity).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for `data/graph/csv/` import artifacts | TBD |

---

Footer refs:
- Graph import root: `data/graph/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
