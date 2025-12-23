---
title: "KFM STAC Catalog Outputs — data/stac README"
path: "data/stac/README.md"
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

doc_uuid: "urn:kfm:doc:data:stac:readme:v1.0.0"
semantic_document_id: "kfm-data-stac-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:stac:readme:v1.0.0"
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

# KFM STAC Catalog Outputs

## 📘 Overview

### Purpose
- This README defines **what lives in `data/stac/`**, why it exists, and how downstream stages should interpret it.
- `data/stac/` is the canonical home for **STAC Collections and STAC Items** emitted by the KFM catalog stage.

### Scope

| In Scope | Out of Scope |
|---|---|
| Directory layout for STAC outputs | Full STAC field-by-field specification |
| What is expected to be published as Collections vs Items | Domain-specific mapping rules for each dataset |
| Validation expectations and governance notes | Implementing ETL / catalog build code (belongs under `src/pipelines/`) |
| How STAC outputs connect to DCAT + PROV + Graph + API | UI design details (belongs under `web/`) |

### Audience
- Primary: Catalog maintainers, data engineers producing STAC outputs.
- Secondary: Graph/ontology builders, API developers, Story Node authors.

### Definitions
- Glossary: `docs/glossary.md`
- Terms used in this doc: STAC, Collection, Item, Asset, DCAT, PROV, evidence artifact, provenance, redaction.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| STAC Collections | `data/stac/collections/` | Catalog stage | One JSON file per Collection |
| STAC Items | `data/stac/items/` | Catalog stage | One JSON file per Item |
| DCAT outputs | `data/catalog/dcat/` | Catalog stage | Dataset discovery records |
| PROV bundles | `data/prov/` | Catalog stage | Lineage bundles per run / dataset |
| STAC schemas | `schemas/stac/` | Schemas/CI | JSON Schema validation target |
| Master pipeline invariant | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Ordering is non-negotiable |

### Definition of done
- [ ] Front-matter complete and `path` matches file location
- [ ] Directory tree matches this README
- [ ] Outputs reference validation schemas under `schemas/` where applicable
- [ ] Governance and sensitivity handling is explicitly stated
- [ ] Downstream linkage expectations are documented (Graph/API/Story Nodes)

## 🗂️ Directory Layout

### This document
- `path`: `data/stac/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs per domain + catalog outputs |
| Catalog outputs | `data/stac/` | STAC Collections + Items (this folder) |
| DCAT catalog | `data/catalog/dcat/` | DCAT outputs (JSON-LD) |
| Provenance | `data/prov/` | PROV bundles (per run / per dataset) |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalog build + transforms |
| Schemas | `schemas/` | JSON schemas for STAC/DCAT/PROV + telemetry |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 data/
└── 📁 stac/
    ├── 📁 collections/
    │   ├── 📄 <collection-id>.json
    │   └── 📄 ...
    ├── 📁 items/
    │   ├── 📄 <item-id>.json
    │   └── 📄 ...
    └── 📄 README.md
~~~

## 🧭 Context

### Background
- The KFM pipeline treats **catalog + provenance outputs as evidence artifacts** that are consumed downstream (Graph, API, UI, Story Nodes). This folder is the STAC portion of that evidence bundle.
- The canonical system ordering is preserved end-to-end: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.

### Assumptions
- STAC outputs in `data/stac/` are produced from upstream domain processing (typically under `data/<domain>/processed/`) by a deterministic catalog-build process.
- The repository provides validation targets in `schemas/` for STAC/DCAT/PROV outputs.

### Constraints and invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracted data through APIs and does not read the graph directly.
- Sensitivity and sovereignty concerns must be handled through redaction and governance gates; do not publish precise sensitive locations unless policy explicitly allows.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the authoritative KFM STAC profile content beyond base STAC 1.0 | TBD | TBD |
| What are the stable ID conventions for Collections and Items across domains | TBD | TBD |
| Do we maintain any top-level STAC catalog index file in addition to `collections/` and `items/` | TBD | TBD |

### Future extensions
- Add/extend domain-specific STAC extensions via the governed STAC profile and matching JSON Schemas.
- Add CI lint rules for link integrity and orphan detection across STAC/DCAT/PROV.

## 🗺️ Diagrams

### System and dataflow diagram

~~~mermaid
flowchart LR
  A[ETL and transforms] --> B[Processed domain outputs]
  B --> C[Catalog build]
  C --> D[STAC Collections and Items]
  C --> E[DCAT datasets]
  C --> F[PROV bundles]

  D --> G[Neo4j Graph]
  E --> G
  F --> G

  G --> H[APIs]
  H --> I[UI]
  I --> J[Story Nodes]
  J --> K[Focus Mode]
~~~

### Optional sequence diagram

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Request narrative or entity context
  API->>Graph: Fetch subgraph + provenance refs
  Graph-->>API: Context bundle with evidence IDs
  API-->>UI: Response with citations and audit flags
~~~

## 📦 Data and Metadata

### Inputs

| Input | Path | Contract / schema | Notes |
|---|---|---|---|
| Domain processed outputs | `data/<domain>/processed/` | Domain-specific | Source material for catalog build |
| Domain mapping docs | `docs/data/` and or `data/<domain>/mappings/` | Governed docs | Optional mapping documentation that explains dataset → STAC/DCAT/PROV |
| STAC profile and schemas | `docs/standards/KFM_STAC_PROFILE.md` and `schemas/stac/` | KFM-STAC | Profile and schema constraints |

### Outputs

| Output | Path | Contract / schema | Notes |
|---|---|---|---|
| STAC Collections | `data/stac/collections/` | `schemas/stac/` | Discoverable groupings for Items |
| STAC Items | `data/stac/items/` | `schemas/stac/` | Evidence-level metadata with assets/links |
| Cross-catalog alignment | `data/catalog/dcat/` + `data/prov/` | `schemas/dcat/` + `schemas/prov/` | Required pairing with STAC outputs |

### Sensitivity and redaction
- If an Item contains sensitive geometry, culturally sensitive knowledge, or restricted site locations, apply redaction or generalization consistent with governance and sovereignty policy before publishing artifacts here.
- Any downstream UI exposure should occur via the API boundary with enforcement of classification rules.

### Quality signals
- Outputs validate against schemas where applicable.
- Catalog build is deterministic and repeatable.
- No orphan references between STAC, DCAT, PROV, Story Nodes, and Graph ingestion.

## 🌐 STAC, DCAT and PROV Alignment

### Required alignment rule
- Each new dataset or evidence product is expected to have:
  - STAC catalog entry
  - DCAT dataset description
  - PROV activity describing how it was produced

### Versioning and lineage
- Version relationships should be represented as explicit metadata links and mirrored in the graph so users can trace how data evolves over time.

## 🏗️ Architecture

### Components

| Layer / component | Responsibility | Owned by | Notes |
|---|---|---|---|
| Catalog outputs | Emit STAC/DCAT/PROV evidence artifacts | Data/Catalog maintainers | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Graph ingestion | Read catalog outputs and build graph | Graph maintainers | Uses STAC/DCAT/PROV as inputs |
| API boundary | Contracted access + redaction | Server maintainers | UI consumes via APIs only |
| UI | Map + narrative interface | Web maintainers | Uses API results and citations |
| Story Nodes | Evidence-led narratives | Curators | Must cite evidence IDs |

### Interfaces and contracts

| Interface | Canonical location | Schema / contract |
|---|---|---|
| STAC JSON | `data/stac/` | `schemas/stac/` |
| DCAT JSON-LD | `data/catalog/dcat/` | `schemas/dcat/` |
| PROV JSON-LD | `data/prov/` | `schemas/prov/` |
| API payloads | `src/server/` | OpenAPI / GraphQL |

### Extension points checklist
- [ ] New dataset added under `data/<domain>/...`
- [ ] STAC Collections and Items generated and validated
- [ ] DCAT dataset record created or updated
- [ ] PROV activity recorded
- [ ] Graph ingest updated if needed
- [ ] API endpoints expose new artifacts as needed
- [ ] UI layer and Story Nodes updated only via API contracts

## 🧠 Story Node and Focus Mode Integration

### How STAC artifacts surface downstream
- Story Nodes should reference evidence IDs that resolve to STAC/DCAT/PROV artifacts.
- Focus Mode narrative should only present provenance-linked content; any AI-derived narrative must include auditability and uncertainty metadata where required.

## ✅ Validation and CI

### Validation steps
- [ ] STAC JSON validates against `schemas/stac/` where applicable
- [ ] Link integrity checks pass
- [ ] No orphan references across catalogs
- [ ] Determinism checks pass for catalog build outputs

### Reproduction

~~~bash
# Placeholder: replace with repo-specific commands
# 1) Run catalog build for one domain
# 2) Validate STAC/DCAT/PROV outputs against schemas
# 3) Verify deterministic outputs across two runs
~~~

## 📡 Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Catalog validation pass/fail | CI | `docs/telemetry/` + `schemas/telemetry/` |
| Orphan reference count | CI | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE and Governance

### Review gates
- Changes that affect schema validation, redaction rules, or sensitive data handling require human review.
- Any expansion of catalog fields that could expose sensitive locations must be reviewed under sovereignty policy.

### CARE and sovereignty considerations
- Identify communities impacted and protection rules in domain documentation.
- Use generalization or redaction where required by sovereignty and ethics policy.

### AI usage constraints
- AI must not infer sensitive locations.
- AI outputs used in downstream narrative must remain provenance-linked and auditable.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for `data/stac/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
