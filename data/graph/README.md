---
title: "KFM — data/graph/ (Graph Import Artifacts)"
path: "data/graph/README.md"
version: "v1.0.1"
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

doc_uuid: "urn:kfm:doc:data:graph:readme:v1.0.1"
semantic_document_id: "kfm-data-graph-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:data:graph:readme:v1.0.1"
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

# KFM data/graph import artifacts

## 📘 Overview

### Purpose

- Define what belongs in `data/graph/` and how it is used to load or update the KFM Neo4j knowledge graph while preserving the canonical pipeline ordering:

  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

- Keep the “data outputs are not code” boundary clear: this directory is for **generated import artifacts**, not source code, ontology definitions, or migrations.

### Scope

| In Scope | Out of Scope |
|---|---|
| Import-ready artifacts for graph ingest (CSV exports) | Graph build code and ontology bindings (canonical home: `src/graph/`) |
| Optional Cypher scripts applied after import (constraints, indexes, touch-ups) | API contracts and implementations (canonical home: `src/server/` — or repo-defined equivalent) |
| Deterministic, diffable, run-/release-ready exports | UI logic and direct-to-graph access patterns (`web/` must not query Neo4j directly) |
| Provenance and catalog references needed to support audits and Focus Mode evidence panels | Narrative Story Nodes (canonical home: `docs/reports/story_nodes/`) |

### Audience

- **Primary:** Graph + data engineers producing Neo4j load artifacts.
- **Secondary:** Reviewers validating provenance, governance, and redaction boundaries for graph loads.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — link may need repair)*
- Terms used in this doc: **graph ingest**, **bulk import**, **stable IDs**, **provenance**, **redaction**, **generalization**.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline + invariants |
| v13 redesign blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(not confirmed in repo — may be a PDF or different filename)* | Architecture maintainers | Canonical roots + readiness gates |
| Graph code + ontology bindings | `src/graph/` | Graph maintainers | Graph build + mapping logic |
| Graph import artifacts | `data/graph/` | Graph build | This directory (CSV + Cypher) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Catalog maintainers | Evidence + lineage artifacts referenced by graph |
| Schemas registry | `schemas/` | Contract owners | Validation targets (graph schemas not confirmed) |

### Definition of done

- [ ] Front-matter complete and `path` matches file location
- [ ] Directory responsibilities + placement rules documented
- [ ] Expected tree is explicit and CI-safe
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document

- `path`: `data/graph/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/<domain>/{raw,work,processed}/` | Source snapshots → transforms → normalized outputs |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts (STAC/DCAT) + lineage (PROV) |
| Graph import artifacts | `data/graph/` | Import-ready CSV + optional Cypher scripts (this folder) |
| Graph build + ontology bindings | `src/graph/` | Ontology-aligned ingest, mapping, migrations (code) |
| Pipelines | `src/pipelines/` | ETL + transforms producing processed outputs and catalogs |
| API boundary | `src/server/` | Contracted access + redaction/generalization enforcement |
| UI | `web/` | Map/narrative client (no direct Neo4j access) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts (provenance-linked) |

### Expected file tree

The v13 blueprint describes `data/graph/csv/` and `data/graph/cypher/` as the canonical output roots for graph import artifacts (if adopted).

~~~text
📁 data/
└── 📁 graph/
    ├── 📁 csv/                 # import-ready CSV exports (nodes/edges/etc.)
    ├── 📁 cypher/              # optional post-import scripts (constraints/indexes/patches)
    └── 📄 README.md            # (this file)
~~~

### Contents contract

#### `data/graph/csv/`

**What belongs here**

- Node and relationship tables exported as CSV for graph ingest.
- Exported tables must be:
  - **reproducible** (generated from upstream inputs),
  - **diffable** (stable ordering + stable IDs),
  - **minimally sufficient** (avoid duplicating large payloads already present in STAC/DCAT/PROV).

**What does not belong here**

- Raw datasets, intermediate transforms, or domain processed outputs (canonical homes: `data/<domain>/{raw,work,processed}/`).
- Hand-edited or one-off CSVs that are not reproducible.

#### `data/graph/cypher/`

**What belongs here**

- Cypher scripts required to finalize a load (constraints, indexes, post-load normalization), when the chosen ingest method requires them.

**What does not belong here**

- The authoritative ontology definitions, mapping logic, or migration code (canonical home: `src/graph/`).
- UI or API logic.

---

## 🧭 Context

### Background

KFM treats catalog and provenance outputs (STAC/DCAT/PROV) as evidence artifacts. The graph stage uses those artifacts plus processed datasets to build a queryable semantic layer for APIs and UI narrative.

### Assumptions

- The graph is built by a deterministic graph pipeline (code under `src/graph/`) that **writes** import artifacts into `data/graph/`.
- The specific Neo4j ingest mechanism is repo-defined (e.g., bulk import vs incremental merge) *(not confirmed in repo)*.
- Graph nodes should carry references back to evidence and lineage identifiers wherever applicable (STAC/DCAT/PROV IDs).

### Constraints and invariants

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- **API boundary is mandatory:** the UI must not query Neo4j directly; it consumes contracted API responses.
- Graph ingest must not “invent” facts: all graph content is derived from governed data + catalogs + provenance.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical ingest strategy (bulk import vs incremental merge)? | TBD | TBD |
| What is the canonical stable ID convention per label/domain? | TBD | TBD |
| Do we store per-run exports under `data/graph/<run_id>/...` or overwrite latest? | TBD | TBD |

---

## 🗺️ Diagrams

### Graph ingest in the canonical pipeline

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[Processed outputs<br/>data/<domain>/processed]
  B --> C[Catalog build]
  C --> D[STAC/DCAT/PROV<br/>data/stac + data/catalog/dcat + data/prov]
  D --> E[Graph build<br/>src/graph]
  E --> F[Import artifacts<br/>data/graph/csv + data/graph/cypher]
  E --> G[Neo4j Graph]
  G --> H[API boundary<br/>src/server]
  H --> I[UI<br/>web]
  I --> J[Story Nodes<br/>docs/reports/story_nodes]
  J --> K[Focus Mode<br/>provenance-linked only]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Typical location | Notes |
|---|---|---|
| Processed datasets | `data/<domain>/processed/` | Normalized, schema-stable outputs |
| Evidence catalogs | `data/stac/` + `data/catalog/dcat/` | Discoverability + dataset-level metadata |
| Lineage bundles | `data/prov/` | Run/product provenance and audit trail |
| Ontology + mappings | `src/graph/` | Label/relationship alignment and mapping rules |

### Outputs

| Output | Path | Notes |
|---|---|---|
| Import-ready node/edge exports | `data/graph/csv/` | CSVs intended for graph ingest |
| Post-import scripts | `data/graph/cypher/` | Optional; constraints/indexes/patches |
| Provenance links | `data/prov/` | Graph build should emit or link to a PROV activity bundle |
| Run manifests | `mcp/runs/` or `data/prov/` | Location is repo-defined *(not confirmed in repo)* |

### Recommended CSV conventions

These conventions are **recommended defaults**; align to the repo’s chosen Neo4j loader tooling.

- Use **stable primary keys** per node type (e.g., `id`) and keep them immutable across rebuilds.
- Store evidence linkage as identifiers, not embedded payloads:
  - `stac_item_id` (or equivalent)
  - `dcat_dataset_id` (or equivalent)
  - `prov_activity_id` (or equivalent)
- Ensure relationship CSVs reference existing node IDs (no dangling endpoints).

### Sensitivity and redaction

- Do not export restricted locations or sensitive attributes into public artifacts.
- If geometry is required, prefer:
  - generalized geometry,
  - bounding boxes,
  - or references to STAC assets that are access-controlled at the API boundary.
- Any redaction/generalization behavior must be documented in lineage (PROV) and enforced at the API boundary.

---

## 🌐 STAC, DCAT & PROV Alignment

### Traceability rule

Graph exports must preserve round-trip traceability:

- **Graph node/edge → evidence IDs (STAC/DCAT) → lineage (PROV) → upstream processed inputs**

This is required so that Story Nodes and Focus Mode can remain provenance-linked and auditable.

### No duplication rule

The graph should not duplicate large data products that already exist in:

- `data/<domain>/processed/` (tabular or geospatial datasets),
- STAC assets (COGs, Parquet, GeoJSON, etc.),
- PROV bundles (lineage metadata).

Instead, store identifiers and relationships; use APIs to resolve full payloads when needed.

---

## 🧱 Architecture

### Component responsibilities

| Layer | Responsibility | Canonical home |
|---|---|---|
| ETL | Ingest and normalize domain datasets | `src/pipelines/` → `data/<domain>/**` |
| Catalogs | Publish evidence artifacts + discovery metadata | `data/stac/` + `data/catalog/dcat/` + `data/prov/` |
| Graph build | Map evidence + processed data into graph form | `src/graph/` |
| Graph import artifacts | Import-ready exports for Neo4j loads | `data/graph/` |
| API boundary | Contracted access + redaction/generalization | `src/server/` |
| UI | Map + narrative exploration | `web/` |
| Story Nodes | Evidence-led narratives | `docs/reports/story_nodes/` |

### Interface boundaries

- UI never reads Neo4j directly; all graph access is via the API boundary.
- Graph build consumes only governed inputs (processed + catalogs + provenance) and emits governed outputs (import artifacts + lineage links).

---

## 🧠 Story Node & Focus Mode Integration

- Story Nodes cite **graph entity IDs** and **evidence IDs** (STAC/DCAT/PROV) rather than raw, uncited claims.
- Focus Mode must only surface provenance-linked content; any AI-derived content must be opt-in and carry uncertainty metadata (policy defined elsewhere).

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] CSV lint: delimiter/encoding, headers present, no empty IDs
- [ ] Referential integrity: every relationship endpoint exists in node exports
- [ ] Determinism: rebuild with unchanged inputs yields diff-stable outputs (ordering, IDs, file names)
- [ ] Evidence linkage: IDs referenced in graph exports resolve to STAC/DCAT/PROV artifacts
- [ ] Governance scans: no prohibited sensitive coordinates or restricted attributes in public artifacts

### Reproduction

~~~bash
# Placeholder only — replace with repo-accurate commands (not confirmed in repo).
# 1) Build catalogs: STAC/DCAT/PROV
# 2) Run graph export to produce data/graph/csv/*
# 3) (Optional) apply data/graph/cypher/* after load
# 4) Run validation checks (csv lint + referential integrity + evidence link checks)
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when:

- introducing a new domain into the graph (new labels/relationships/properties),
- changing redaction/generalization behavior for any graph-exported geometry,
- changing classification/sensitivity labels,
- publishing any dataset derived from restricted inputs.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing
- Prohibited: generating new policy, inferring sensitive locations

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial `data/graph/README.md` | TBD |
| v1.0.1 | 2025-12-24 | Align with v12/v13 invariants; clarify contracts and validation | TBD |

---

Footer refs (do not remove)

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(not confirmed in repo — may be a PDF or different filename)*
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`