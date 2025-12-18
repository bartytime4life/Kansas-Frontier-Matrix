---
title: "Hydrology — Processed Data (README)"
path: "data/hydrology/processed/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
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

doc_uuid: "urn:kfm:doc:data:hydrology:processed:readme:v1.0.0"
semantic_document_id: "kfm-data-hydrology-processed-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:hydrology:processed:readme:v1.0.0"
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

# Hydrology — Processed Data (README)

## 📘 Overview

### Purpose
- This folder contains **processed / derived hydrology assets** that are ready for cataloging (STAC/DCAT/PROV) and downstream use (graph, APIs, UI).
- It defines the **minimum conventions** for what belongs here, how outputs are versioned, and what metadata/provenance must accompany each processed deliverable.

### Scope
| In Scope | Out of Scope |
|---|---|
| Derived hydrology layers (e.g., river/stream lines, floodplain polygons, reservoirs/waterbodies, watershed boundaries, time-series extracts) intended for reuse | Raw source downloads, ad-hoc scratch outputs, exploratory notebooks, pipeline code |
| Standardized file naming, versioning, metadata sidecars, and basic QA expectations | Publishing decisions for APIs/UI, ontology modeling, Story Node authoring |
| Provenance hooks (run IDs, inputs, transforms) | Long-form scientific reports, model calibration studies (place in `docs/` or `mcp/`) |

### Audience
- Primary: Data engineering + data curation (ETL and dataset lifecycle)
- Secondary: STAC/DCAT/PROV maintainers, graph builders, API/frontend implementers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Processed**: Derived, standardized, and validated outputs produced by governed transforms (safe to delete + regenerate from inputs).
  - **Dataset slug**: A stable, lowercase identifier for a dataset family (e.g., `rivers`, `floodplains`, `reservoirs`).
  - **Release/version**: An immutable output snapshot, typically date-tagged (recommended) or semver-tagged.
  - **Sidecar**: A metadata/provenance/QA file that travels with the data artifact.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Hydrology domain README | `data/hydrology/README.md` | Data domain steward | Parent overview for the hydrology domain (may be created separately). |
| Hydrology source registry | `data/sources/hydrology_sources.json` | Data curation | Referenced in design docs; presence/path not confirmed in repo. |
| Hydrology processed assets | `data/hydrology/processed/` | Data engineering | **This directory** (versioned, derived outputs). |
| STAC collections/items | `data/stac/hydrology/` | Catalog maintainer | Location may vary; keep STAC aligned with processed releases. |
| Pipeline implementation | `src/pipelines/hydrology/` | Data engineering | Location may vary; keep transforms reproducible and pinned. |
| Run logs / experiment lineage | `mcp/runs/` | Data engineering | Prefer logging run IDs and parameters here (or equivalent). |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Folder purpose + “what belongs here” is unambiguous
- [ ] File naming + versioning conventions are stated (with examples)
- [ ] STAC/DCAT/PROV alignment guidance is stated
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/hydrology/processed/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Hydrology domain root | `data/hydrology/` | Domain-level conventions + links (if used in repo layout). |
| Raw hydrology inputs | `data/hydrology/raw/` | Source downloads / ingested raw files (if used in repo layout). |
| Work/intermediate | `data/hydrology/work/` | Temporary or intermediate artifacts (often gitignored). |
| Processed hydrology outputs | `data/hydrology/processed/` | **Versioned derived outputs** (this folder). |
| Global processed (alternate layout) | `data/processed/hydrology/` | Some docs reference this location; keep a single source of truth. |
| STAC catalogs | `data/stac/` | STAC catalogs + collections + items. |
| Schemas | `schemas/` | JSON Schemas / profile constraints. |
| Pipelines | `src/pipelines/` | ETL + catalog builds + transforms. |
| MCP runs | `mcp/runs/` | Run manifests, experiment logs, outputs. |

### Expected file tree for this sub-area
~~~text
📁 data/hydrology/processed/
├── 📄 README.md
├── 📁 <dataset_slug>/
│   ├── 📁 vYYYYMMDD/                       # immutable release (recommended)
│   │   ├── 📦 <dataset_slug>__<variant>.<ext>
│   │   ├── 🧾 metadata.json                # human + machine metadata
│   │   ├── 🔗 provenance.json              # PROV pointers / run IDs / inputs
│   │   ├── 🔐 checksums.sha256             # integrity for all files in release
│   │   └── ✅ qa_report.json               # optional but encouraged
│   └── 🔖 latest -> vYYYYMMDD/             # optional convenience pointer
└── 📁 _scratch/                            # optional; should be gitignored
~~~

## 🧭 Context

### Background
- Hydrology layers are a foundational environmental context in KFM (e.g., waterways, floodplains, reservoirs). Processed outputs enable consistent reuse across mapping, analysis, and narrative products.

### Assumptions
- Every artifact in `data/hydrology/processed/` is **derivable** from tracked inputs and a pinned transform (no “mystery files”).
- Releases are **immutable**: once published under a release folder, do not edit in place—publish a new release folder instead.
- Processed assets are accompanied by enough metadata to support:
  - catalog registration (STAC/DCAT),
  - lineage (PROV),
  - downstream safety checks (redaction / sensitivity notes).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- “Processed” does **not** mean “unreviewed”: if an output is used by catalogs/UI, it must have basic QA + provenance.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize on GeoParquet for vectors and GeoTIFF for rasters, or allow mixed formats per dataset? | TBD | TBD |
| What is the canonical projection strategy (store-native vs web-native vs both)? | TBD | TBD |
| Where should “global layout” live if both `data/hydrology/processed/` and `data/processed/hydrology/` exist? | TBD | TBD |

### Future extensions
- Add scenario-based hydrology derivatives (e.g., modeled flood extents) with explicit scenario metadata (model name, calibration refs, parameters).
- Add time-series packaging conventions (e.g., partitioned parquet, per-station bundles) while keeping STAC/DCAT mappings stable.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Hydrology raw sources] --> B[Hydrology ETL / transforms]
  B --> C[data/hydrology/processed/ release assets]
  C --> D[STAC/DCAT/PROV catalogs]
  D --> E[Neo4j graph build]
  E --> F[APIs]
  F --> G[React/Map UI]
  G --> H[Story Nodes]
  H --> I[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Curator as Data Curator
  participant Pipeline as Pipeline
  participant Catalog as STAC/DCAT/PROV
  participant Graph as Graph Build
  Curator->>Pipeline: Register source + run transform
  Pipeline->>Pipeline: Generate processed release + sidecars
  Pipeline->>Catalog: Emit/Update STAC Items + DCAT/PROV
  Catalog->>Graph: Provide catalog refs for ingestion
  Graph-->>Curator: Ingest complete + provenance pointers stored
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Hydrology source datasets | Various (vector/raster/tabular) | `data/hydrology/raw/` (or source registry) | Source checksum + schema/field expectations (dataset-specific). |
| Transform parameters | YAML/JSON (recommended) | Pipeline config (location varies) | Config schema validation (if available). |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed hydrology vectors (example) | GeoPackage / GeoParquet | `data/hydrology/processed/<dataset_slug>/vYYYYMMDD/` | Dataset-specific schema (columns + geometry type). |
| Processed hydrology rasters (example) | GeoTIFF / COG | `data/hydrology/processed/<dataset_slug>/vYYYYMMDD/` | Raster metadata contract (CRS, resolution, nodata). |
| Sidecar metadata | JSON | `.../metadata.json` | Not yet confirmed in repo (recommend schema in `schemas/`). |
| Sidecar provenance | JSON | `.../provenance.json` | PROV mapping / run IDs (recommend schema in `schemas/`). |
| Checksums | sha256 text | `.../checksums.sha256` | Deterministic hashing of release contents. |

#### Naming conventions (recommended)
- Dataset directory: `data/hydrology/processed/<dataset_slug>/`
- Release directory: `vYYYYMMDD` (immutable snapshot date)  
  - If you must use semantic versioning, use `vMAJOR.MINOR.PATCH` and keep it immutable.
- Data filename pattern (suggested):
  - `<dataset_slug>__<variant>.<ext>`
  - Examples:
    - `rivers__centerlines.gpkg`
    - `floodplains__100yr.gpkg`
    - `reservoirs__polygons.parquet`

### Sensitivity & redaction
- Hydrology layers are often public, but **fine-grained infrastructure or private-site locations** can be sensitive (e.g., private wells, protected water infrastructure).
- If sensitive features exist:
  - omit them from public releases **or**
  - generalize geometry (snap/aggregate) and redact attributes that enable re-identification.

### Quality signals
- Geometry:
  - Valid geometry (no self-intersections for polygons, no empty geometries)
  - Consistent CRS declaration
  - No duplicate primary keys (where applicable)
- Attributes:
  - Required fields present, correct types
  - Controlled vocabulary fields normalized (if used)
- Temporal (if applicable):
  - Timestamp parsing stable, monotonic ordering for time series
  - Explicit time zone rules stated (if time-series data is included)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved:
  - One Collection per dataset family (recommended): `hydrology-<dataset_slug>`
- Items involved:
  - One Item per release (or per tiling/partition if needed)
- Extension(s):
  - Use extensions only when necessary; document any non-core fields in the dataset’s metadata sidecar.

### DCAT
- Dataset identifiers:
  - Keep DCAT dataset IDs aligned with STAC Collection IDs where practical.
- License mapping:
  - Must match upstream source license; do not assume CC licensing for derived data if upstream terms differ.
- Contact / publisher mapping:
  - Use the publisher/maintainer responsible for the curated derivative (and attribute upstream in provenance).

### PROV-O
- `prov:wasDerivedFrom`: Raw/source entities referenced by stable IDs (or source URLs if no internal IDs exist).
- `prov:wasGeneratedBy`: Pipeline activity/run identifier (store run_id + parameters hash).
- Activity / Agent identities:
  - Agent = pipeline or maintainer role (not an individual person unless governance allows).

### Versioning
- Releases are immutable; publish new releases instead of editing an existing one.
- Use STAC versioning links (e.g., `prev`/`next`) and graph predecessor/successor relationships as applicable.
- Avoid relying on `latest` pointers for reproducibility; treat them as convenience only.