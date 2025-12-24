---
title: "KFM Catalog Outputs — data/catalog README"
path: "data/catalog/README.md"
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

doc_uuid: "urn:kfm:doc:data:catalog:readme:v1.0.0"
semantic_document_id: "kfm-data-catalog-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:catalog:readme:v1.0.0"
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

# `data/catalog/` — KFM catalog outputs

> **Purpose (required):** Define what belongs in `data/catalog/`, how it is structured, and how catalog artifacts link to `data/stac/` and `data/prov/` for graph/API/UI/Story consumption.

## 📘 Overview

### What this folder is
`data/catalog/` is the canonical home for **dataset-level catalog artifacts** produced by the KFM **Catalog** stage. These artifacts make datasets discoverable and interoperable, and provide stable identifiers for downstream stages.

### What belongs here
- **DCAT outputs** (dataset discovery + distributions): `data/catalog/dcat/`
- (Future) additional catalog serializations (only when governed and validated)

### What does not belong here
- STAC artifacts (belong in `data/stac/`)
- Provenance bundles (belong in `data/prov/`)
- Domain data products (belong in `data/<domain>/{raw,work,processed}/`)
- Source code (belongs in `src/`)
- UI assets and configs (belongs in `web/`)
- Narrative Story Nodes (belongs in `docs/reports/story_nodes/`)

### Scope
| In Scope | Out of Scope |
|---|---|
| Directory contract + layout conventions for catalog artifacts | Full DCAT field specification (belongs under `docs/standards/`) |
| Directory-level linkage expectations to STAC + PROV | Implementing pipeline code (belongs under `src/pipelines/`) |
| Validation and governance expectations for published catalog artifacts | External publishing workflows outside the repo |

### Audience
- Primary: catalog maintainers, data engineering maintainers, API maintainers
- Secondary: governance reviewers, graph/ontology maintainers, Story Node authors

### Definition of done
- [ ] Front-matter complete and `path` matches file location
- [ ] Directory tree matches this README
- [ ] Clear boundaries: what belongs here vs elsewhere
- [ ] Linkage expectations to STAC + PROV are documented
- [ ] Validation & CI/CD steps are listed
- [ ] Governance + CARE/sovereignty considerations are explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/catalog/README.md` (must match front-matter)

### Expected tree

~~~text
📁 data/
└── 📁 catalog/
    ├── 📄 README.md
    └── 📁 dcat/
        ├── 📄 README.md
        ├── 📄 dataset--<dataset_id>.jsonld
        ├── 📄 dataset--<dataset_id>.ttl
        └── 📄 catalog.<ext>
~~~

Notes:
- `dcat/` is the canonical DCAT output directory.
- `catalog.<ext>` is optional (only if the repo adopts an aggregate `dcat:Catalog` artifact).
- Exact naming + serialization rules must align with the governed DCAT profile.

## 🧭 Context

### Why this exists
KFM treats **catalog artifacts** as machine-readable “evidence metadata” that downstream stages can rely on:
- Graph ingest can reference stable dataset IDs,
- APIs can expose dataset discovery consistently,
- UI/Story Nodes can cite dataset identifiers,
- Focus Mode can enforce provenance-linked narrative behavior.

### Architecture constraints and invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- UI must not access Neo4j directly; all access is through contracted APIs.
- Catalog artifacts should be produced deterministically (no hand-edited drift).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we maintain an aggregate `dcat:Catalog` file in addition to per-dataset records? | TBD | TBD |
| What is the canonical DCAT serialization in-repo (JSON-LD only vs JSON-LD + Turtle)? | TBD | TBD |
| What is the stable `dataset_id` naming convention across domains? | TBD | TBD |

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL & transforms] --> B[data/<domain>/processed]
  B --> C[Catalog build]
  C --> S[STAC<br/>data/stac]
  C --> D[DCAT<br/>data/catalog/dcat]
  C --> P[PROV<br/>data/prov]
  S --> G[Graph]
  D --> G
  P --> G
  G --> API[API boundary]
  API --> UI[UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Where from | Notes |
|---|---|---|
| Processed domain outputs | `data/<domain>/processed/` | Primary material for dataset metadata |
| STAC Collections/Items | `data/stac/**` | Referenced by DCAT distributions for geospatial assets |
| PROV bundles | `data/prov/**` | Referenced for lineage/auditability |

### Outputs
| Output | Location | Notes |
|---|---|---|
| DCAT dataset records | `data/catalog/dcat/` | Canonical dataset discovery artifacts |

### Sensitivity & redaction
- Catalog artifacts must not bypass sovereignty or governance policy.
- If a dataset is restricted, its catalog record must reflect access constraints and avoid linking to restricted distributions in a way that bypasses controls.

## 🌐 STAC, DCAT & PROV Alignment

### Minimum alignment rule
For each dataset/evidence product intended for downstream consumption:
- **STAC** (when spatial/temporal asset catalog is needed): `data/stac/`
- **DCAT** (dataset discovery + distributions): `data/catalog/dcat/`
- **PROV** (lineage + audit): `data/prov/`

### Linkage expectations
- DCAT records should link to:
  - STAC Collection and/or Item identifiers (when applicable), and/or
  - distributions pointing to controlled repo paths or controlled endpoints
- PROV bundles should include activity/entity/agent identifiers that can be referenced from catalog artifacts and mirrored into the graph.

## 🧱 Architecture

### Component responsibilities
| Component | Responsibility | Canonical location |
|---|---|---|
| ETL / pipelines | Deterministic transforms | `src/pipelines/` |
| Catalog artifacts | STAC/DCAT/PROV outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Graph | Ontology-governed ingest | `src/graph/` (+ `data/graph/` for import artifacts) |
| API boundary | Contracted access + redaction | `src/server/` |
| UI | Map + narrative | `web/` |
| Story Nodes | Evidence-led narratives | `docs/reports/story_nodes/` |

## 🧠 Story Node & Focus Mode Integration

- Story Nodes should cite **dataset identifiers** (DCAT) and **evidence identifiers** (STAC/DCAT/PROV).
- Focus Mode must only present provenance-linked content; any AI-derived narrative must be opt-in and uncertainty-tagged.

## 🧪 Validation & CI/CD

### Minimum checks
- [ ] Markdown protocol checks (KFM-MDP)
- [ ] DCAT artifacts validate against `schemas/dcat/**` (if present)
- [ ] Link integrity checks (distributions resolve; no broken internal refs)
- [ ] No secrets/PII in catalog artifacts
- [ ] Governance checks for restricted/sensitive datasets

### Reproduction

~~~bash
# Placeholder — replace with repo-specific commands
# 1) Run catalog build
# 2) Validate DCAT outputs
# 3) Verify link integrity
~~~

## ⚖ FAIR+CARE & Governance

### Review gates (directory-level)
- New external datasets and new public distributions require governance review.
- Any change that could expose sensitive locations or culturally sensitive knowledge must be reviewed under sovereignty policy.
- Any schema/profile changes require schema maintainer review.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial `data/catalog/` README | TBD |

---

Footer refs:
- Data root: `data/README.md`
- DCAT outputs: `data/catalog/dcat/README.md`
- STAC outputs: `data/stac/README.md`
- Provenance: `data/prov/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`