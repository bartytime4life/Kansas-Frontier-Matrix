---
title: "KFM — data/work Directory README"
path: "data/work/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data:work:readme:v1.0.0"
semantic_document_id: "kfm-data-work-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:readme:v1.0.0"
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

# KFM — data/work Directory README

## 📘 Overview

### Purpose
- Define the intended use and conventions for `data/work/` as the **non-canonical workspace** for intermediate artifacts produced during ETL, normalization, and validation.
- Ensure intermediate outputs are organized predictably so they can be promoted (when appropriate) into **canonical** locations (e.g., `data/processed/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`) without breaking the pipeline ordering.

### Scope
| In Scope | Out of Scope |
|---|---|
| Intermediate files produced during ingestion, parsing, validation, normalization, enrichment, and QA | Final/canonical datasets intended for long-term reference |
| Run logs, checksums, intermediate manifests, draft metadata | Public-facing catalogs (STAC/DCAT/PROV outputs belong in their canonical folders) |
| Temporary run scratch space | Application contracts, API schema design, UI behavior |

### Audience
- Primary: pipeline engineers, data contributors maintaining ETL runs
- Secondary: reviewers/auditors verifying provenance + quality gates

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Work area**: a transient workspace where intermediate pipeline artifacts may be created and iterated.
  - **Canonical outputs**: artifacts that are stable, versioned, and referenced by catalogs/graph/APIs.
  - **Run scope**: grouping of outputs produced by a single execution of a pipeline.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Work root | `data/work/` | DataOps | Non-canonical staging + intermediates |
| Staging | `data/work/staging/` | ETL | Downloaded/unpacked inputs in transit |
| Tables | `data/work/tables/` | ETL | Intermediate tabular extracts/joins |
| Spatial | `data/work/spatial/` | ETL | Intermediate geospatial transforms |
| Work-processed | `data/work/processed/` | ETL | Candidate processed outputs pending promotion |
| Metadata | `data/work/metadata/` | ETL | Draft/derived metadata, manifests, reports |
| Logs | `data/work/logs/` | ETL | Run logs, validation outputs, checksums |
| Temp | `data/work/tmp/` | ETL | Scratch space; safe-to-delete by convention |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory responsibilities are clearly stated (what belongs / what does not)
- [ ] Conventions avoid breaking the canonical pipeline ordering (ETL → catalogs → graph → APIs → UI → story → focus)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No secrets/credentials/PII are implied to be stored in `data/work/`

## 🗂️ Directory Layout

### This document
- `path`: `data/work/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data lifecycle root | `data/` | Raw/work/processed + catalogs |
| Raw sources | `data/raw/` | Source snapshots; minimally transformed |
| Canonical processed | `data/processed/` | Stable processed datasets (derived) |
| STAC catalogs | `data/stac/` | STAC collections/items + assets |
| DCAT catalogs | `data/catalog/dcat/` | Dataset-level catalog views |
| PROV bundles | `data/prov/` | Lineage/activity bundles |
| Pipelines | `src/pipelines/` | ETL + catalog build + transforms |
| Schemas | `schemas/` | Validation schemas (STAC/DCAT/PROV/telemetry/etc.) |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    ├── 📄 README.md
    ├── 📁 staging/
    │   └── 📄 README.md
    ├── 📁 tables/
    │   └── 📄 README.md
    ├── 📁 spatial/
    │   └── 📄 README.md
    ├── 📁 processed/
    │   └── 📄 README.md
    ├── 📁 metadata/
    │   └── 📄 README.md
    ├── 📁 logs/
    │   └── 📄 README.md
    └── 📁 tmp/
        └── 📄 README.md
~~~

## 🧭 Context

### Background
`data/work/` exists to support the **middle of the lifecycle** where data is being actively transformed, validated, and prepared for cataloging/graph ingestion. It is an operational convenience layer to keep intermediate artifacts separated from canonical outputs.

### Assumptions
- Intermediate artifacts may be created per “run” (recommended), but the exact run ID scheme is project-defined.
- Some files in `data/work/` may be regenerated frequently; consumers should avoid depending on them as stable inputs unless explicitly promoted/versioned elsewhere.

### Constraints / invariants
- The canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend clients must not depend on `data/work/` artifacts directly (API boundary remains the integration surface).
- `data/work/` must not be treated as an authoritative source of truth; authoritative datasets and catalogs must be promoted to their canonical locations.
- Never store secrets/credentials in `data/work/` (or anywhere in-repo).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Define a standard run identifier format (`run_id`) | TBD | TBD |
| Define retention/cleanup rules for `data/work/tmp/` and large intermediates | TBD | TBD |
| Decide which intermediate artifacts should be committed vs generated | TBD | TBD |

### Future extensions
- Extension point A: add a run manifest pattern (e.g., `data/work/metadata/<run_id>/manifest.json`)
- Extension point B: add standardized validation report outputs (row counts, geometry validity, schema checks)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A["data/raw (inputs)"] --> B["data/work (staging + transforms)"]
  B --> C["data/processed (canonical)"]
  C --> D["data/stac + data/catalog/dcat + data/prov (catalogs)"]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source snapshots | PDF/CSV/GeoPackage/etc. | `data/raw/` | Hash + basic type checks |
| Pipeline configs | YAML/JSON/etc. | `src/pipelines/` | Lint + schema (if defined) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Intermediate tables | CSV/Parquet/etc. | `data/work/tables/` | Schema checks (project-defined) |
| Intermediate spatial layers | GeoJSON/GeoPackage/etc. | `data/work/spatial/` | Geometry/CRS validity checks |
| Candidate processed outputs | dataset formats | `data/work/processed/` | Must be promotable to `data/processed/` |
| Draft metadata + manifests | JSON/YAML | `data/work/metadata/` | STAC/DCAT/PROV drafts validated before promotion |
| Logs + reports | text/JSON | `data/work/logs/` | No secrets; redaction rules apply |
| Scratch temp files | any | `data/work/tmp/` | Not relied upon |

### Sensitivity & redaction
- If any intermediate artifact contains sensitive fields (locations, names, or restricted content), it must be handled according to governance and sovereignty guidance and must not be promoted to public catalogs without appropriate generalization/redaction.

### Quality signals
- Recommended checks for intermediates:
  - Completeness (required columns present)
  - Range checks / type checks for numeric fields
  - Spatial validity (geometry validity + CRS present + bounding boxes)
  - Join cardinality checks where merges occur
  - Checksums and stable file naming for reproducibility

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- `data/work/` may contain **draft** STAC items/collections or extraction metadata, but **published** STAC outputs belong under `data/stac/`.

### DCAT
- `data/work/` may contain mapping drafts, but **published** DCAT records belong under `data/catalog/dcat/`.

### PROV-O
- `data/work/` may contain draft provenance reports, but **published** PROV bundles belong under `data/prov/`.
- When promoting any artifact out of `data/work/`, ensure it can be linked with:
  - `prov:wasDerivedFrom` (input source IDs)
  - `prov:wasGeneratedBy` (run/activity ID)
  - activity agent identity (human/system)

### Versioning
- Intermediate outputs in `data/work/` are not assumed stable.
- Promotion to canonical areas should introduce explicit versioning and lineage references (as applicable).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | ingest + normalize + validate | configs + run logs + intermediates |
| Work area | hold intermediate artifacts | filesystem conventions (this doc) |
| Catalog builders | generate STAC/DCAT/PROV | schema-validated JSON/LD outputs |
| Graph build | load canonical outputs into Neo4j | API-layer mediated access |
| APIs | serve contracted data | REST/GraphQL (contract tests) |
| UI | render map + narrative | API calls only |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Validation schemas | `schemas/` | Semver + changelog |
| Pipeline run logs (structured) | `data/work/logs/` | per-run scoping recommended |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | schema validated; linked lineage |

### Extension points checklist (for future work)
- [ ] Run-scoped output conventions (folders + manifests)
- [ ] Schema validation for intermediate tables/spatial layers
- [ ] Promotion checklist from `data/work/processed/` → `data/processed/`
- [ ] Automated cleanup rules for tmp artifacts
- [ ] Telemetry signals for run outcomes and validation status

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- `data/work/` artifacts should **not** be referenced directly by Story Nodes or Focus Mode.
- Only artifacts promoted to canonical, cataloged outputs (and linked into graph/API) should feed narrative experiences.

### Provenance-linked narrative rule
- Any narrative claim must trace to a dataset/record/asset ID in the canonical catalogs and/or graph.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Ensure no secrets/credentials exist in `data/work/`
- [ ] Intermediate table checks (types, required columns, row count sanity)
- [ ] Spatial validity checks (CRS present, geometry validity, bounding boxes)
- [ ] Draft STAC/DCAT/PROV artifacts validated before promotion
- [ ] Promotion checklist completed for any outputs moved to canonical directories

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands:
# 1) run ETL for a dataset/domain
# 2) validate intermediate outputs
# 3) promote approved outputs to canonical directories
# 4) generate catalogs + validate schemas
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| ETL run status | pipeline runtime | `data/work/logs/` |
| Validation report | validators | `data/work/logs/` or `data/work/metadata/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that affect promotion rules, sensitive data handling, or catalog publication should be reviewed (human review required).

### CARE / sovereignty considerations
- Avoid exposing sensitive locations or culturally sensitive information via intermediate artifacts.
- Ensure that any redaction/generalization rules are applied before content is moved into public-facing catalogs.

### AI usage constraints
- AI-assisted transformations must not infer sensitive locations or generate policy; keep AI usage aligned with repository governance documents.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `data/work/` README | TBD |
