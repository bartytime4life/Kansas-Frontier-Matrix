---
title: "KFM Data Work — Processed (Intermediate Outputs)"
path: "data/work/processed/README.md"
version: "v1.0.0"
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

doc_uuid: "urn:kfm:doc:data:work:processed-readme:v1.0.0"
semantic_document_id: "kfm-data-work-processed-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:processed-readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# data/work/processed/

## 📘 Overview

### Purpose
This directory is the **“processed, but not yet published”** workspace inside `data/work/`. It holds **intermediate processed artifacts** produced by ETL/normalization steps (cleaned tables, normalized geometries, derived intermediate joins, etc.) that are **awaiting QA, curation, or promotion** to canonical outputs.

**Key principle:** contents here should be **reproducible** from sources + pipeline configs and may be **pruned/regenerated**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Intermediate processed outputs produced during ETL runs | Final, stable datasets meant to be consumed downstream |
| “Ready-for-validation” artifacts (e.g., cleaned/normalized exports) | Raw sources (those belong in `data/raw/` or source domain folders) |
| Temporary, reproducible working derivatives | Catalog outputs (STAC/DCAT/PROV) that belong under `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| QA byproducts (validation reports, simple summaries) | Secrets, credentials, private keys, tokens, or PII leakage |

### Audience
- Pipeline developers (ETL + transforms)
- Data curators performing QA/acceptance before publishing
- Reviewers validating provenance + sensitivity constraints

### Definitions (link to glossary)
- Glossary link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **Work area**: reproducible scratch/intermediate outputs
  - **Canonical processed**: stable datasets in `data/processed/` intended for downstream catalogs/graph
  - **Promotion**: moving/packaging a vetted artifact from work space into canonical processed + catalogs

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering | `docs/MASTER_GUIDE_v12.md` | KFM Maintainers | Canonical pipeline + invariants |
| Data lifecycle staging | `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` | KFM Maintainers | `data/work/processed/` is an internal sub-area of `data/work/` |
| Work sub-areas | `data/work/staging/` · `data/work/tables/` · `data/work/spatial/` | Pipeline Owners | Intermediate artifacts by type |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Clear distinction between **work outputs** and **canonical processed outputs**
- [ ] Explicit notes on provenance + reproducibility expectations
- [ ] Sensitivity and redaction expectations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/work/processed/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Work staging | `data/work/staging/` | Raw-ish extracts awaiting normalization |
| Work tables | `data/work/tables/` | Intermediate tabular artifacts (extractions, joins, reshapes) |
| Work spatial | `data/work/spatial/` | Intermediate spatial artifacts (vector/raster, reprojection, clipping) |
| Canonical processed | `data/processed/` | Stable processed datasets (publishable + referenceable) |
| STAC outputs | `data/stac/` | STAC Collections + Items for publishable assets |
| DCAT outputs | `data/catalog/dcat/` | Dataset-level catalog views |
| PROV outputs | `data/prov/` | Provenance bundles |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 processed/
        ├── 📁 <domain-or-project>/
        │   └── 📁 <run-or-batch>/
        │       ├── 📄 <intermediate-artifact>.<ext>
        │       └── 📄 <notes-or-qc>.<ext>
        └── 📄 README.md
~~~

> Folder naming conventions beyond “domain-or-project” and “run-or-batch” are **not confirmed in repo**; keep structures simple and reproducible.

## 🧭 Context

### Background
KFM’s canonical data lifecycle requires a clean separation between:
- **Working outputs** (reproducible, iterated, can be deleted), and
- **Published/stable outputs** (referenced by catalogs, graph, API contracts, and UI).

This directory exists to keep “almost-ready” artifacts **out of** `data/processed/` until they pass review.

### Assumptions
- ETL runs are deterministic and can be re-run to regenerate artifacts.
- Artifacts in `data/work/processed/` are **not** treated as stable references for catalogs or UI.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Downstream systems should prefer **`data/processed/` and catalogs** over `data/work/processed/`.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should `data/work/processed/` enforce a standardized run-id directory format? | TBD | TBD |
| Where should QC reports be stored when they become “official”? | TBD | TBD |

## 🗺️ Diagrams

### System / dataflow diagram (work processed context)
~~~mermaid
flowchart LR
  A[data/work/staging] --> B[data/work/processed]
  B --> C[data/processed]
  C --> D[data/stac · data/catalog/dcat · data/prov]
  D --> E[Neo4j Graph]
  E --> F[APIs]
  F --> G[React/Map UI]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Staged extracts | varies | `data/work/staging/` | basic type/shape checks |
| Intermediate tables | varies | `data/work/tables/` | schema/range/completeness checks |
| Intermediate spatial | varies | `data/work/spatial/` | CRS + geometry validity checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Intermediate processed artifacts | varies | `data/work/processed/...` | **not** treated as a public contract |

### Sensitivity & redaction
Artifacts in `data/work/processed/` may still be **unreviewed**. Do not assume anything here is safe for public export. If an artifact is intended to be published, apply required redaction/generalization rules **before** promoting it to `data/processed/` and generating catalog/graph outputs.

### Quality signals
- Prefer artifacts that include enough context to reproduce (source identifiers, transform notes, and run metadata).
- Validate basic integrity appropriate to data type (e.g., geometry validity, required columns present, no obviously broken encodings).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- **Do not** treat `data/work/processed/` as STAC output.
- Once an artifact is accepted into `data/processed/`, it can be packaged as STAC Item/Collection assets under `data/stac/`.

### DCAT
- DCAT dataset views should represent **published** datasets (post-promotion), not transient work outputs.

### PROV-O
- Provenance bundles should be emitted for published transformations (post-promotion) under `data/prov/`.
- For work outputs, capture enough run context to allow later PROV creation (at minimum: what source inputs, what transform, which run).

## 🧱 Architecture

### How this directory is used
- This directory is **not served directly** to end users.
- It is a controlled intermediate workspace supporting:
  - repeatable ETL processing,
  - QA/curation,
  - promotion into canonical processed datasets and catalogs.

### Interfaces / contracts
- None. Downstream contracts should only reference:
  - `data/processed/` (stable data),
  - `data/stac/` / `data/catalog/dcat/` / `data/prov/` (catalogs + provenance),
  - graph/API layers for consumption.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Confirm artifact is reproducible from defined sources + transforms
- [ ] Basic QA appropriate to artifact type (schema/geometry/time range checks)
- [ ] Sensitivity review where applicable
- [ ] Promotion plan defined (target location under `data/processed/` and intended catalog outputs)

### Reproduction
~~~bash
# Replace with repo-specific commands (not confirmed in repo).
# Goal: re-run the ETL steps that generate a target artifact in data/work/processed/
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- New external data sources
- Any content with potential sensitivity / sovereignty constraints
- Any artifact intended for publication into `data/processed/` + catalogs

### CARE / sovereignty considerations
- Treat unreviewed work outputs as potentially sensitive until verified.
- Apply required generalization/redaction rules before publication.

### AI usage constraints
- No speculative additions or inference of sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `data/work/processed/` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`