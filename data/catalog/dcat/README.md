---
title: "KFM DCAT Catalog Output Directory"
path: "data/catalog/dcat/README.md"
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

doc_uuid: "urn:kfm:doc:data:catalog:dcat:readme:v1.0.0"
semantic_document_id: "kfm-data-catalog-dcat-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:catalog:dcat:readme:v1.0.0"
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

# KFM DCAT Catalog Output Directory

This directory is the canonical home for **DCAT dataset records** produced by the KFM **Catalog** stage.

Path: `data/catalog/dcat/`

KFM canonical ordering (non-negotiable):

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose

- Provide a single, predictable location for **DCAT dataset records** emitted by KFM catalog builds.
- Prevent drift and duplication by establishing folder-level rules: **what belongs here**, and **what does not**.
- Document how DCAT records link to **STAC** (`data/stac/`) and **PROV** (`data/prov/`) so downstream stages can resolve evidence and lineage.

### Scope

| In Scope | Out of Scope |
|---|---|
| Directory contract and naming/layout conventions for DCAT outputs | Full DCAT profile field-by-field specification (belongs in standards; see below) |
| Minimum expectations for dataset/distribution metadata at folder-level | ETL / catalog build implementation code (belongs under `src/pipelines/`) |
| Linkage expectations to STAC + PROV | API endpoint behavior and UI design details (belongs under `src/server/` and `web/`) |
| Validation expectations (schemas, link integrity, governance gates) | External publishing workflows (data portals, hosting) |

### Audience

- Primary: catalog maintainers, data engineering maintainers, API maintainers
- Secondary: governance reviewers, domain contributors, Story Node authors

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — if missing, add or link to the correct glossary path)*
- Terms used in this doc: DCAT, Dataset, Distribution, JSON-LD, RDF, STAC, PROV, stable identifier, lineage, access constraints

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering + invariants |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Canonical roots for catalog outputs |
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | Catalog maintainers | **not confirmed in repo** (add if missing) |
| DCAT validation schemas | `schemas/dcat/` | Schemas/CI | Expected machine validation target (**not confirmed in repo**) |
| STAC outputs | `data/stac/` | Catalog stage | Spatial asset catalogs (Collections + Items) |
| PROV outputs | `data/prov/` | ETL + catalog stage | Lineage bundles per run / per dataset |

### Definition of done

- [ ] Front-matter complete and `path` matches `data/catalog/dcat/README.md`
- [ ] Directory boundaries are explicit (no “mystery duplicates”)
- [ ] DCAT ↔ STAC/PROV linkage expectations are documented
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document

- `path`: `data/catalog/dcat/README.md` (must match front-matter)

### Expected file tree

~~~text
📁 data/
└── 📁 catalog/
    └── 📁 dcat/
        ├── 📄 README.md
        ├── 📄 dataset--<dataset_id>.jsonld
        ├── 📄 dataset--<dataset_id>.ttl              # optional (if repo adopts Turtle)
        └── 📄 catalog.<ext>                          # optional (if repo adopts an aggregate DCAT Catalog)
~~~

Notes:
- `dataset--<dataset_id>.<ext>` represents **one DCAT dataset record per logical dataset**.
- `catalog.<ext>` is optional and should only exist if the repo adopts a `dcat:Catalog` aggregate export.
- Exact naming + serialization rules must match the repo’s DCAT profile (if present).

### What belongs here

- **Generated catalog artifacts only**:
  - dataset records (`dcat:Dataset`)
  - optional aggregate catalog (`dcat:Catalog`)
  - optional alternate serializations for the same dataset record (only if explicitly adopted)

### What must not live here

- Raw source data (belongs in `data/<domain>/raw/`)
- Intermediate transforms (belongs in `data/<domain>/work/`)
- Processed/normalized data products (belongs in `data/<domain>/processed/`)
- STAC artifacts (belong in `data/stac/`)
- PROV bundles (belong in `data/prov/`)
- Graph import fixtures (belong in `data/graph/`)
- Pipeline or catalog builder code (belongs in `src/pipelines/`)
- UI assets/config (belongs in `web/`)

---

## 🔗 DCAT ↔ STAC ↔ PROV Alignment

KFM treats catalog + provenance artifacts as **evidence**. For each dataset:

1. **DCAT** describes the dataset at discovery/metadata level.
2. **STAC** describes spatiotemporal assets (when applicable).
3. **PROV** explains lineage for how artifacts were produced.

### Minimum linkage expectations

At a folder-contract level:

- A DCAT dataset record should include **stable identifiers** that can be referenced by:
  - Graph nodes (Neo4j)
  - API payloads
  - Story Nodes / Focus Mode evidence panels

- A DCAT dataset record should link (directly or indirectly) to:
  - relevant STAC Collection(s) / Item(s) for geospatial assets (if applicable)
  - at least one PROV activity/bundle identifier for lineage (required for publish-ready evidence)

### Recommended linkage table (repo-local convention)

This repo may adopt a mapping table convention (not required, but helpful) to ensure cross-catalog integrity:

| Field | Example | Where used |
|---|---|---|
| `dataset_id` | `air_quality_openaq_v3` | File naming, graph IDs, API refs |
| `stac_collection_id` | `air-quality-openaq-v3` | `data/stac/collections/` |
| `prov_activity_id` | `prov:activity:<run_id>` | `data/prov/` bundles |

If adopted, this table should be produced by CI or a catalog build report (not hand-edited).

---

## 📦 Data & Metadata Contract

### Inputs

| Input | Where from | Notes |
|---|---|---|
| Domain processed outputs | `data/<domain>/processed/` | Source material for catalog build |
| STAC outputs | `data/stac/**` | Optional but typical for geospatial datasets |
| PROV bundles | `data/prov/**` | Required for provenance-linked narrative |

### Outputs

| Output | Path | Notes |
|---|---|---|
| DCAT dataset record | `data/catalog/dcat/dataset--<dataset_id>.jsonld` | Required (preferred canonical serialization) |
| Optional Turtle | `data/catalog/dcat/dataset--<dataset_id>.ttl` | Only if the repo adopts Turtle |
| Optional aggregate catalog | `data/catalog/dcat/catalog.<ext>` | Only if the repo adopts an aggregate `dcat:Catalog` |

### Serialization policy

- **Preferred:** JSON-LD (machine-consumable + web-friendly)
- **Optional:** Turtle/RDF serializations, only if the repo adopts and validates them
- Do not introduce new serializations without schema/shape updates and CI validation.

---

## 🧪 Validation & CI/CD

### Minimum checks (DCAT-facing)

- [ ] DCAT records validate against `schemas/dcat/**` *(not confirmed in repo — add or align as needed)*
- [ ] Link integrity:
  - no broken internal `href` / repo-path references
  - any external distributions resolve only to approved domains/endpoints (if applicable)
- [ ] Orphan checks:
  - dataset IDs referenced by graph/API/UI/story resolve to a DCAT record
  - DCAT records referencing STAC/PROV resolve to existing artifacts (where required)
- [ ] Determinism:
  - rerunning catalog build with unchanged inputs produces diff-stable DCAT records (stable IDs, stable ordering)

### Reproduction

~~~bash
# Placeholders — replace with repo-specific commands
# 1) Run catalog build for one domain
# 2) Validate DCAT outputs against schemas
# 3) Run link/orphan integrity checks
~~~

---

## ⚖ FAIR+CARE & Governance

### Sensitivity and access constraints

- DCAT records must not leak:
  - restricted coordinates,
  - sensitive locations,
  - culturally protected knowledge.
- If a dataset is restricted, DCAT metadata must express access constraints and ensure distributions do not bypass policy.

### Review gates (minimum)

Changes require human review when they introduce or modify:

- new external datasets/sources (licensing + sovereignty implications)
- new sensitive layers or access classifications
- schema/profile changes that alter validation or metadata exposure

### AI usage constraints

- AI must not infer sensitive locations from DCAT metadata.
- Any AI-produced narrative downstream must remain provenance-linked and auditable (Focus Mode rule).

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for `data/catalog/dcat/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- STAC outputs: `data/stac/README.md`
- PROV outputs: `data/prov/README.md`