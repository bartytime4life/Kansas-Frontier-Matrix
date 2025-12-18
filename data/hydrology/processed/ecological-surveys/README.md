---
title: "Hydrology — Processed Ecological Surveys"
path: "data/hydrology/processed/ecological-surveys/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
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

doc_uuid: "urn:kfm:doc:data:hydrology:processed:ecological-surveys:readme:v1.0.0"
semantic_document_id: "kfm-data-hydrology-processed-ecological-surveys-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:hydrology:processed:ecological-surveys:readme:v1.0.0"
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

# Hydrology — Processed Ecological Surveys

## 📘 Overview

### Purpose
- Define what belongs in `data/hydrology/processed/ecological-surveys/` and how it should be organized.
- Establish minimum metadata, provenance, validation, and sensitivity requirements for **analysis-ready** ecological survey outputs in the Hydrology domain.

### Scope
| In Scope | Out of Scope |
|---|---|
| Standardized/normalized ecological survey outputs (tabular + geospatial) ready for downstream cataloging and graph ingestion. | Raw downloads and vendor-native formats (store in `data/hydrology/raw/ecological-surveys/`). |
| Derived indicators/indices computed from surveys (with reproducible provenance). | Scratch/intermediate artifacts (store in `data/hydrology/work/ecological-surveys/`). |
| QA reports, checksums, and provenance sidecars that support reproducibility and audit. | Story Nodes / narrative outputs (store under governed docs paths, not in `data/`). |
| Public-ready assets that respect redaction/generalization rules. | Any artifact that leaks restricted locations or sensitive fields. |

### Audience
- Primary: ETL/data contributors working on Hydrology ecological survey pipelines.
- Secondary: graph/API integrators, analysts, reviewers/auditors, Story Node authors (as downstream consumers).

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: ecological survey, sampling event, site/station, observation, transect/plot, indicator, QA, STAC Item/Collection, DCAT Dataset, PROV Activity/Entity/Agent.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/hydrology/processed/ecological-surveys/README.md` | TBD | Folder contract + conventions. |
| Processed survey tables | `data/hydrology/processed/ecological-surveys/tables/` | TBD | Normalized event/observation/indicator tables. |
| Processed survey geodata | `data/hydrology/processed/ecological-surveys/geodata/` | TBD | Sites, footprints, segments, etc. |
| QA + checksums | `data/hydrology/processed/ecological-surveys/qa/` | TBD | Validation outputs and integrity evidence. |
| Provenance sidecars | `data/hydrology/processed/ecological-surveys/provenance/` | TBD | PROV exports and run references. |
| STAC/DCAT catalogs | `data/stac/` | TBD | Catalog entries referencing assets in this folder. |
| Pipeline configs / code | `src/pipelines/` | TBD | Deterministic transforms that produce these artifacts. |
| Run logs / runs | `mcp/runs/` | TBD | Run IDs, parameterization, and reproducibility evidence. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Directory tree reflects intended contents and naming conventions for this folder

## 🗂️ Directory Layout

### This document
- `path`: `data/hydrology/processed/ecological-surveys/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Hydrology domain root | `data/hydrology/` | Domain-scoped raw/work/processed outputs and domain READMEs. |
| Raw ecological surveys | `data/hydrology/raw/ecological-surveys/` | Source downloads and unmodified extracts. |
| Work ecological surveys | `data/hydrology/work/ecological-surveys/` | Intermediate transforms, staging, temp joins. |
| Processed ecological surveys | `data/hydrology/processed/ecological-surveys/` | Analysis-ready outputs (this folder). |
| STAC catalogs | `data/stac/` | STAC Collections/Items referencing processed assets. |
| Schemas | `schemas/` | JSON schemas + validation contracts (dataset-specific if present). |
| Pipelines | `src/pipelines/` | ETL + catalog generation + transforms. |
| MCP runs | `mcp/runs/` | Run logs, experiment logs, reproducibility artifacts. |
| Governance | `docs/governance/` | Sensitivity, ethics, sovereignty policy references. |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 hydrology/
    └── 📁 processed/
        └── 📁 ecological-surveys/
            ├── 📄 README.md
            ├── 📁 tables/
            │   ├── 📄 <source_slug>__survey_events.parquet
            │   ├── 📄 <source_slug>__observations.parquet
            │   └── 📄 <source_slug>__indicators.parquet
            ├── 📁 geodata/
            │   ├── 📄 <source_slug>__sites.gpkg
            │   └── 📄 <source_slug>__survey_footprints.gpkg
            ├── 📁 rasters/
            │   └── 📄 <source_slug>__derived_index.tif
            ├── 📁 docs/
            │   ├── 📄 <source_slug>__data_dictionary.md
            │   └── 📄 <source_slug>__methods.md
            ├── 📁 qa/
            │   ├── 📄 <source_slug>__qa_report.md
            │   └── 📄 <source_slug>__checksums.sha256
            └── 📁 provenance/
                └── 📄 <source_slug>__prov.jsonld
~~~

## 🧭 Context

### Background
Ecological surveys (e.g., aquatic habitat assessments, riparian vegetation surveys, macroinvertebrate/fish sampling, or other biological monitoring) are frequently used as environmental evidence for hydrology-adjacent analyses. In KFM, these surveys become **processed evidence assets** that can be cataloged (STAC/DCAT/PROV), integrated into the knowledge graph, and consumed through APIs and UI layers with appropriate provenance and sensitivity controls.

### Assumptions
- Source programs use heterogeneous schemas; processed outputs in this folder normalize to consistent event/observation patterns.
- Every processed output is reproducible from raw inputs + pipeline configuration and is traceable via PROV run metadata.
- Spatial features may need generalization/redaction depending on sensitivity constraints.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What are the canonical output schemas for `survey_events`, `observations`, and `indicators` in Hydrology? | TBD | TBD |
| Which external ecological survey sources are prioritized and how are they versioned? | TBD | TBD |
| What redaction/generalization rules apply to threatened species presence or sensitive site locations? | TBD | TBD |

### Future extensions
- Extension point A: Add a formal schema package under `schemas/` for ecological survey outputs (tabular + geospatial).
- Extension point B: Expand graph modeling for observations/indicators with explicit provenance and uncertainty fields (where applicable).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  R[Raw ecological surveys] --> W[Work transforms]
  W --> P[Processed ecological surveys<br/>data/hydrology/processed/ecological-surveys]
  P --> C[STAC/DCAT/PROV catalogs]
  C --> G[Neo4j graph]
  G --> A[APIs]
  A --> U[React/Map UI]
  U --> S[Story Nodes]
  S --> F[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: request survey context (entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle (entities + prov links)
  API-->>UI: contracted payload (data + citations + audit flags)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw ecological survey data | CSV/XLSX/GeoPackage/etc. | `data/hydrology/raw/ecological-surveys/` | Checksums, schema expectations, row counts. |
| Spatial reference layers | Vector/Raster | Hydrology domain reference sources | CRS recorded; geometry validity; extent checks. |
| Taxonomy/parameter references | CSV/JSON | Project-managed or source-managed | Controlled vocabulary mapping coverage. |
| Methods/codebooks | PDF/MD | Source documentation | Linked in STAC/DCAT and stored under `docs/` if permitted. |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Normalized survey events | Parquet/CSV | `tables/<source_slug>__survey_events.*` | TBD (schema to be defined/linked). |
| Normalized observations | Parquet/CSV | `tables/<source_slug>__observations.*` | TBD (schema to be defined/linked). |
| Derived indicators | Parquet/CSV | `tables/<source_slug>__indicators.*` | TBD (schema to be defined/linked). |
| Survey sites/stations | GeoPackage/GeoParquet | `geodata/<source_slug>__sites.*` | TBD (geometry + attribute schema). |
| Survey footprints/segments | GeoPackage/GeoParquet | `geodata/<source_slug>__survey_footprints.*` | TBD. |
| QA reports + checksums | MD/TXT | `qa/` | Must be reproducible and tied to run IDs. |
| Provenance export | JSON-LD | `provenance/<source_slug>__prov.jsonld` | PROV-O aligned (KFM-PROV profile). |

### Sensitivity & redaction
- Identify any fields requiring generalization or omission for public outputs (e.g., precise coordinates for restricted sites, landowner/PII fields, or sensitive species presence).
- Apply sovereignty and ethics requirements in `docs/governance/SOVEREIGNTY.md` and `docs/governance/ETHICS.md` before publishing or surfacing via API/UI.

### Quality signals
- Completeness: required keys present (event IDs, site IDs, dates, methods).
- Referential integrity: observations reference valid events; events reference valid sites.
- Geometry validity: no invalid geometries; CRS explicitly recorded.
- Range checks: plausible coordinate ranges; temporal bounds; non-negative counts/measures.
- Consistency: stable units/parameter naming; taxonomy mapping coverage; duplicate detection.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `hydrology-ecological-surveys` (TBD canonical collection ID).
- Items involved: one Item per dataset release (or per partition, if adopted) with Assets pointing to files in this folder.
- Extension(s): use only the extensions required for the asset types (vector/raster/table/projection/etc.), aligned to `stac_profile` in front-matter.

### DCAT
- Dataset identifiers: align with STAC Collection IDs and use stable identifiers/URIs.
- License mapping: carry through the source license and any downstream restrictions.
- Contact / publisher mapping: record the responsible source org and KFM steward (where applicable).

### PROV-O
- `prov:wasDerivedFrom`: link processed entities to raw source artifacts + versions.
- `prov:wasGeneratedBy`: link processed entities to the pipeline run activity (run ID, parameters).
- Activity / Agent identities: identify the transform and the responsible agent (person/org/service) as permitted.

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships as applicable.

## 🧱 Architecture

- This folder is an **ETL output boundary**: outputs here should be ready for cataloging and graph ingestion without manual edits.
- Downstream integration expectations:
  - Catalogs (STAC/DCAT/PROV) reference these assets and provide discovery + provenance hooks.
  - Graph ingestion should model entities using KFM ontology patterns (Event/Place/Observation/Metric as appropriate) with explicit provenance links.
  - APIs/UI consume graph + catalog references, not raw files directly (except controlled download endpoints, if present).

## 🧪 Validation & CI/CD

Minimum checks before considering outputs “publishable”:
- [ ] Tabular schema validation (required columns/types; controlled vocab where applicable)
- [ ] Referential integrity checks (events ↔ observations ↔ sites)
- [ ] Geospatial validation (geometry validity, CRS recorded, extent sanity)
- [ ] Range/constraint checks (dates, numeric bounds, categorical domains)
- [ ] Checksums generated and stored under `qa/`
- [ ] STAC Items/Collections validate and correctly reference assets in this folder
- [ ] DCAT mapping includes minimum fields (title/description/license/keywords)
- [ ] PROV export references the generating run and source inputs
- [ ] Security/sovereignty review complete for any sensitive/restricted locations or fields

## ⚖ FAIR+CARE & Governance

- Governance references:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/ETHICS.md`
  - `docs/governance/SOVEREIGNTY.md`
- Governance review triggers for this folder commonly include:
  - New sensitive layers (e.g., precise locations for restricted ecological resources)
  - New external data sources with non-trivial licensing or use constraints
  - Any plan to expose processed outputs via public-facing APIs/UI
- CARE considerations:
  - If any subset of the data requires special handling, record the rule and the affected fields/geometry handling in this folder’s QA/provenance documentation (and in the catalog metadata).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial README scaffold for processed ecological surveys | TBD |
