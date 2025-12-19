---
title: "KFM — data/work/spatial README"
path: "data/work/spatial/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data:work:spatial:readme:v1.0.0"
semantic_document_id: "kfm-data-work-spatial-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:spatial:readme:v1.0.0"
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

# data/work/spatial

## 📘 Overview

### Purpose
This directory is the **spatial workbench** for KFM: a place to store **intermediate, in-progress, or QA-stage geospatial artifacts** produced during ETL and curation, *before* promotion into governed outputs (for example `data/processed/` and `data/stac/`).

It exists to keep the pipeline deterministic and tidy by separating:
- **Raw inputs** (`data/raw/` and/or source-domain raw folders)  
- **Work-in-progress transforms** (`data/work/spatial/` ← this folder)  
- **Governed outputs** (`data/processed/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`)

### Scope
| In Scope | Out of Scope |
|---|---|
| Intermediate vector/raster outputs used to reach a validated deliverable | Anything treated as a “source of truth” dataset |
| Geometry repair, reprojection, clipping, tiling experiments | Final STAC Items/Collections (those belong under `data/stac/`) |
| Pre-validation layers pending promotion | Public UI-serving assets (never serve directly from `data/work/`) |
| QA notes that explain spatial corrections | Long-term canonical datasets (use `data/processed/`) |

### Audience
- Primary: Data engineers, GIS analysts, pipeline maintainers
- Secondary: Historians/researchers who contribute spatial datasets and need to understand promotion rules

### Definitions
- Glossary link: `docs/glossary.md` (if present)
- “Work”: non-final outputs used to reach a governed artifact.
- “Promotion”: moving an artifact from `data/work/` into `data/processed/` with corresponding STAC/DCAT/PROV alignment as required by the pipeline.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Spatial workbench | `data/work/spatial/` | Data/ETL | Intermediate geospatial artifacts |
| Sibling work areas | `data/work/tables/` • `data/work/staging/` | Data/ETL | Tables + staging inputs that may feed spatial steps |
| Canonical pipeline reference | `docs/MASTER_GUIDE_v12.md` | Docs/Governance | Defines lifecycle + invariant ordering |

### Definition of done
- [ ] This README describes what belongs here and what does not
- [ ] The “promotion checklist” is present and consistent with the canonical pipeline ordering
- [ ] No claims imply the UI reads from `data/work/` directly
- [ ] Sensitivity and sovereignty guidance is stated without leaking sensitive locations

## 🗂️ Directory layout

### This document
- `path`: `data/work/spatial/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Work zone | `data/work/` | Intermediate assets across domains |
| Processed zone | `data/processed/` | Governed, stable, reusable outputs |
| STAC | `data/stac/` | STAC Items + Collections |
| DCAT | `data/catalog/dcat/` | DCAT dataset views |
| PROV | `data/prov/` | Lineage bundles and activity records |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 spatial/
        └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM’s pipeline relies on a strict staging flow so that work products do not accidentally become public-facing artifacts or bypass provenance requirements.

This folder provides a dedicated place to:
- iterate on spatial cleaning and transformations
- keep “scratch” artifacts out of governed catalogs
- make promotion into `data/processed/` and `data/stac/` an explicit, reviewable step

### Assumptions
- The canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Spatial work products can be regenerated; they are not assumed durable unless promoted.

### Constraints and invariants
- Frontend and downstream consumers must not read from `data/work/spatial/` directly.
- Promotion requires provenance alignment (STAC/DCAT/PROV) where applicable.
- Do not add hidden “policy” behavior here; governance rules live under `docs/governance/`.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we need a standardized subfolder convention under `data/work/spatial/` (by domain, by run, by activity)? | TBD | TBD |

### Future extensions
- Add a governed convention for subfolders such as `by_domain/`, `by_run/`, or `qa/` if standardized elsewhere in repo (not confirmed here).

## 🗺️ Diagrams

### System and dataflow
~~~mermaid
flowchart LR
  A[Raw spatial sources] --> B[ETL transforms in data/work/spatial]
  B --> C[Promote to data/processed]
  C --> D[STAC/DCAT/PROV catalogs]
  D --> E[Neo4j graph]
  E --> F[API layer]
  F --> G[UI]
  G --> H[Story Nodes]
  H --> I[Focus Mode]
~~~

## 📦 Data and metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Candidate spatial sources | vector/raster (varies) | `data/raw/` or domain sources | Basic integrity checks before transform |
| Lookup tables | CSV/Parquet/etc. | `data/work/tables/` | Schema + referential checks (as applicable) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Intermediate spatial artifacts | vector/raster (varies) | `data/work/spatial/` | Not a public contract |
| Promotion-ready outputs | vector/raster (varies) | `data/processed/` | Governed by domain docs + catalogs |
| Catalog entries | STAC/DCAT/PROV | `data/stac/` `data/catalog/dcat/` `data/prov/` | STAC/DCAT/PROV validation |

### Sensitivity and redaction
- Do not place precise sensitive locations or restricted geometries in public outputs.
- If a spatial artifact is sensitive, follow `docs/governance/SOVEREIGNTY.md` and related governance references before any promotion.

### Quality signals
- Geometry validity (no self-intersections where prohibited; valid polygons; no empty geometries)
- CRS is explicit and consistent across derived outputs
- Spatial bounds are plausible for Kansas-focused datasets (when applicable)
- Clear provenance notes exist prior to promotion

## 🌐 STAC, DCAT and PROV alignment

### STAC
- This folder is **not** a STAC location.
- When an artifact is ready for public discovery/use, create the appropriate STAC Collection/Item(s) under `data/stac/`.

### DCAT
- Datasets that become governed outputs should have DCAT mapping under `data/catalog/dcat/` (as applicable).

### PROV-O
- Promotion should be traceable:
  - `prov:wasDerivedFrom` should reference source IDs
  - `prov:wasGeneratedBy` should reference the transform activity/run ID

### Versioning
- If a promoted dataset replaces an earlier version, use predecessor/successor links in catalogs and mirror that lineage in the graph (where implemented).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL spatial work | Transform + QA spatial artifacts | Files in `data/work/spatial/` + run logs |
| Catalog build | Publish governed artifacts | STAC/DCAT/PROV outputs |
| Graph build | Integrate semantics | API-mediated graph access |
| API + UI | Serve content | Contracts only (no direct `data/work/` reads) |

### Interfaces and contracts
- There is **no public contract** for `data/work/spatial/`.
- Public-facing assets must be exposed via catalogs and API contracts.

## 🧠 Story Node and Focus Mode integration

### How this work surfaces in Focus Mode
- It should not surface directly.
- Only promoted artifacts with catalog/provenance references should be referenced by Story Nodes or Focus Mode narratives.

### Provenance-linked narrative rule
- Story Nodes must cite dataset/document IDs that resolve via catalogs/graph, not local work paths.

## 🧪 Validation and CI

### Validation steps
- [ ] Confirm work artifacts are not referenced by API/UI/story nodes
- [ ] If promoting: run STAC/DCAT/PROV validation for the new assets
- [ ] If promoting: ensure provenance references exist and resolve
- [ ] Ensure sensitive geometries are handled per governance docs

### Reproduction
~~~bash
# Placeholder: replace with repo-specific commands
# 1) run spatial validation checks
# 2) build/validate STAC/DCAT/PROV (if promoting)
# 3) run graph + API contract tests (if promotion affects downstream)
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE and governance

### Review gates
- Promotion of new public layers may require review per:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/ETHICS.md`
  - `docs/governance/SOVEREIGNTY.md`

### CARE and sovereignty considerations
- If spatial artifacts contain culturally sensitive or restricted information, apply required generalization/redaction and route through the appropriate review path.

### AI usage constraints
- This document allows “summarize/structure_extract/translate/keyword_index” and prohibits “generate_policy” and “infer_sensitive_locations”.

## 🕰️ Version history
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for spatial work directory | TBD |
