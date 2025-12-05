---
title: "🟫 KFM v11.2.4 — Automated Soil Data Ingestion Pipeline (gNATSGO · SSURGO Portal)"
path: "docs/pipelines/soil/gnatsgo-auto-ingest/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Soil Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active / Enforced"

doc_kind: "Pipeline"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "pipelines/soil"
  applies_to:
    - "soil"
    - "gnatsgo"
    - "ssurgo"
    - "statgso2"
    - "stac"
    - "dcat"
    - "graph"
    - "telemetry"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<sha256-of-previous>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/soil-ingest-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/soil-ingest-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:pipelines:soil:gnatsgo-auto-ingest:v11.2.4"
semantic_document_id: "kfm-pipeline-soil-gnatsgo-auto-ingest-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:soil:gnatsgo-auto-ingest:v11.2.4"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🟫 Automated Soil Data Ingestion Pipeline  
**gNATSGO + SSURGO Portal → Deterministic ETL → STAC/DCAT → KFM Knowledge Graph**  

`docs/pipelines/soil/gnatsgo-auto-ingest/README.md`

**Purpose:**  
Define the governed, deterministic, and provenance-complete ingestion pipeline for USDA NRCS soil datasets (gNATSGO, SSURGO Portal, STATSGO2, Raster Soil Surveys) into KFM — producing a canonical **Soil Layer** for archaeology, ecology, hydrology, geomorphology, and landscape-change analyses.

</div>

---

## 📘 Overview

This pipeline governs the **end-to-end ingestion** of national soils datasets into the Kansas Frontier Matrix (KFM). It:

- Ingests **gNATSGO**, **SSURGO Portal** (SQLite/GeoPackage), **STATSGO2**, and **Raster Soil Surveys**.  
- Ensures **deterministic behavior**, reproducible transformations, and version-aware upserts.  
- Emits **STAC Collections/Items** and **DCAT Datasets** suitable for catalog indexing.  
- Upserts into the **KFM knowledge graph** using soil ontology classes.  
- Captures full **telemetry and provenance** aligned with FAIR+CARE, ISO 19115, PROV-O, DCAT, and STAC 1.x.  

This document is the canonical reference for:

- How new soil releases are detected.  
- How schemas are validated and normalized.  
- How soil data is exposed in STAC/DCAT and Neo4j.  
- How telemetry and governance controls are applied.

---

## 🗂️ Directory Layout

```text
📂 docs/pipelines/soil/gnatsgo-auto-ingest/
├── 📄 README.md                       # 🟫 This pipeline specification
└── 🖼️ workflow-diagram.png            # (Optional) Visual diagram of ETL flow

📂 src/pipelines/soil/gnatsgo_auto/
├── 📄 dag.py                          # Pipeline DAG (Airflow/LangGraph)
├── 📂 nodes/                          # ETL nodes (download, normalize, export)
│   └── 📄 *.py
└── 📂 configs/                        # Config-driven, environment-specific settings
    ├── 📄 base.yaml
    ├── 📄 dev.yaml
    ├── 📄 stage.yaml
    └── 📄 prod.yaml

📂 data/raw/soil/gnatsgo/              # Immutable raw downloads (versioned)
📂 data/work/soil/gnatsgo/             # Intermediate/normalized work data
📂 data/processed/soil/gnatsgo/        # Production-ready tables/rasters
📂 data/stac/soil/gnatsgo/             # STAC Collections & Items for soil assets

📄 schemas/telemetry/soil-ingest-v1.json  # Telemetry schema for soil ingestion runs
```

Every directory listed above **must** have a README or schema describing its contents, and ETL code must treat `data/raw` as immutable.

---

## 🧭 Context

Within the KFM stack, this pipeline occupies the **soil data ingest** segment:

> NRCS Soil Releases → Immutable Staging → Deterministic ETL → STAC/DCAT → Neo4j Soil Ontology → Story Nodes & Focus Mode

It interacts with:

- **Upstream**  
  - USDA NRCS gNATSGO and SSURGO Portal distribution endpoints.  
  - STATSGO2 and Raster Soil Survey releases (where available).  

- **Downstream**  
  - STAC Collections/Items for soils (consumed by map/catalog frontends).  
  - DCAT dataset entries for soil collections and derived layers.  
  - Neo4j soil ontology graphs (`SoilMapUnit`, `SoilHorizon`, `SoilProperty`, etc.).  
  - Telemetry and energy/carbon accounting (via KFM energy standards).  

It must **coexist** with other pipelines (hydrology, climate, archaeology) without violating:

- Soil ontology constraints.  
- Geoprivacy rules (e.g., if future layers cross sensitive sites).  
- FAIR+CARE and provenance requirements.

---

## 🧱 Architecture

### 1. Pipeline flow

```mermaid
flowchart TD
    Monitor[NRCS Release Monitor] --> Stage[Immutable Download Staging]
    Stage --> Checksum[Checksum Verification<br/>+ PROV-O Lineage]
    Checksum --> SchemaVal[Schema Validation<br/>(Great Expectations)]
    SchemaVal --> ETL[Deterministic ETL<br/>(LangGraph DAG)]
    ETL --> Normalize[Raster/Vector Normalization]
    Normalize --> STAC[STAC Collection & Item Generation]
    STAC --> Graph[Neo4j Soil Ontology Upserts]
    Graph --> Telemetry[Telemetry → Energy · Storage · Cost · Drift]
```

This architecture must be implemented in a **config-driven** fashion, with environment-specific differences confined to config files and deployment descriptors.

### 2. Supported source data types

| Source              | Format          | Notes                                                                 |
|---------------------|-----------------|-----------------------------------------------------------------------|
| gNATSGO             | ESRI GDB        | Raster + 70+ tabular attributes. `MUKEY` primary key.                 |
| SSURGO Portal       | SQLite/GeoPackage | Preferred for openness & tooling neutrality.                          |
| STATSGO2            | Vector + tabular | Merged within gNATSGO composition; used for generalization.           |
| Raster Soil Surveys | Raster          | Region-specific, where available, for higher-resolution properties.   |

All source manifests must be registered under `data/sources/soil/...` with appropriate DCAT metadata.

### 3. Release monitoring & detection

The pipeline performs scheduled checks (daily or weekly, per environment overlay) using:

- Filename patterns (e.g., `gNATSGO_2025_12.gdb.zip`).  
- NRCS “official release” metadata (version tags, dates).  
- File-size drift thresholds.  
- SHA-256 changes relative to previous ingestions.

Detection events are logged (and optionally exported as PROV entities) in the form:

```json
{
  "event": "soil_release_detected",
  "source": "NRCS",
  "version_raw": "2025-12",
  "sha256": "<value>",
  "timestamp_ingest": "<UTC>"
}
```

These events feed:

- Release dashboards.  
- Provenance chains for soil datasets.  
- Conditional triggers for ETL reruns.

### 4. Schema & metadata validation

All sources must satisfy:

#### 4.1 Tabular validation

- Presence of `MUKEY` and other mandatory keys.  
- Relational integrity across component tables (no orphaned rows).  
- Null checks for required columns.  
- Field type consistency with USDA schema guidelines.

#### 4.2 Raster validation

- CRS compliance (e.g., EPSG:5070 or a documented soil CRS).  
- Resolution consistency (10 m or 30 m, depending on product).  
- Band statistics sanity checks (min/max, nodata handling, histograms).

#### 4.3 STAC/DCAT validation

- Required fields (id, title, license, datetime, assets).  
- Correct license (e.g., Public Domain where applicable).  
- PROV-O parent links to raw sources and ETL activities.

Validation jobs use **Great Expectations** and schema checks, with artifacts written under:

```text
data/quality/soil/gnatsgo/<version>/
```

### 5. Deterministic ETL

All ETL nodes are:

- **Deterministic**  
  - Fixed seeds for any random operations.  
  - Stable sort orders and grouping keys.  
  - No nondeterministic parallelism.

- **WAL-protected**  
  - State transitions logged to a write-ahead log for replay.  

- **Idempotent**  
  - Safe to replay on failure or in recovery scenarios.  

- **Config-driven**  
  - Environment config under:

```text
src/pipelines/soil/gnatsgo_auto/
    configs/
        base.yaml
        dev.yaml
        stage.yaml
        prod.yaml
```

Key ETL operations:

- Normalize tabular schema to KFM soil ontology expectations.  
- Convert ESRI GDB → Parquet/GeoParquet for performance and interoperability.  
- Consolidate soil property tables into analysis-ready structures.  
- Derive raster soil-property layers and summary statistics.  
- Build `MUKEY` → H3 mappings at governed resolutions.  
- Apply CARE-compliant location blurring or masking where required (e.g., in sensitive overlays).

### 6. Knowledge-graph ingestion

Each ingest produces:

- A **STAC Collection** for the dataset version.  
- **STAC Items** for raster and tabular layers.  
- **Neo4j upsert batches** using soil-ontology classes, such as:
  - `:SoilMapUnit`  
  - `:SoilHorizon`  
  - `:SoilProperty`  
  - `:RasterCell` linked to `MUKEY` and spatial cells.

Upserts must use:

- Idempotency keys (e.g., dataset-version + MUKEY).  
- Versioned relationships (e.g., `[:HAS_SOIL_PROPERTY {version: ...}]`).  
- Lineage references back to PROV-O metadata for each ETL activity and dataset.

---

## 📦 Data & Metadata

### 1. STAC & DCAT artifacts

For each ingestion run:

- **STAC Collection**  
  - Represents the soil dataset version (e.g., `gnatsgo-2025-12`).  
- **STAC Items**  
  - Separate Items for:
    - Raster layers (per property).  
    - Tabular exports (Parquet/GeoParquet).  

- **DCAT entries**  
  - Dataset-level descriptions for gNATSGO/SSURGO composite and derived products.  

All must include:

- License information (e.g., Public Domain / USDA).  
- Spatial & temporal coverage metadata.  
- Links to PROV bundles and upstream NRCS references.

### 2. Telemetry

Each run emits telemetry conforming to `soil-ingest-v1.json`, including:

- Energy (J → kWh → CO₂e) using the **Grid-Carbon Intensity** standard.  
- CPU/GPU wall time.  
- Disk I/O metrics and storage deltas.  
- Drift summary (# changed `MUKEY` entries, etc.).  
- Raster deltas (difference histograms per layer).  

Telemetry files are written to:

```text
releases/v11.2.4/soil-ingest-telemetry.json
```

Metric cardinality must be controlled via label allowlists (e.g., no per-MUKEY labels).

---

## 🌐 STAC, DCAT & PROV Alignment

This pipeline is designed from the outset to be catalog- and provenance-aligned:

- **STAC 1.x**
  - Collections and Items for soil data use:
    - `properties` for spatial/temporal coverage and product metadata.  
    - `assets` for rasters and tables.  
  - May include KFM-specific fields (e.g., `kfm:mu_density`, `kfm:soil_property`).  

- **DCAT**
  - Soil datasets appear as `dcat:Dataset` entries:
    - Linked to STAC Collections and Items via distributions.  
    - With `dct:license`, `dct:spatial`, `dct:temporal`, and `dct:provenance`.  

- **PROV-O**
  - ETL runs are `prov:Activity` entities:
    - `prov:used` → NRCS source files and previous versions.  
    - `prov:generated` → processed soil datasets and STAC/DCAT records.  
    - `prov:wasAssociatedWith` → pipeline service identities.  

The `provenance_ref` fields in datasets and telemetry should point to JSON-LD PROV bundles, enabling full trace-back from any soil product to its source release and transformations.

---

## 🧪 Validation & CI/CD

This pipeline must be enforced by CI/CD:

- **Schema & quality tests**
  - Run Great Expectations suites on:
    - Tabular `MUKEY` relationships.  
    - Required columns and type consistency.  
    - Raster CRS, resolution, and basic stats.  

- **Contract tests**
  - Verify that:
    - STAC and DCAT exports conform to schemas.  
    - Neo4j upserts respect ontology constraints and idempotency.  

- **Determinism tests**
  - Re-run ETL on a fixed input snapshot and compare outputs:
    - Checksum of processed tables/rasters.  
    - STAC/DCAT metadata equivalence.  

- **Telemetry tests**
  - Validate telemetry against `soil-ingest-v1.json`.  
  - Check that energy/CO₂e fields are computed and non-null.

CI workflows (e.g., `.github/workflows/kfm-ci-pipelines.yml`) must block merges if:

- Schema or quality tests fail.  
- STAC/DCAT/PROV schemas are violated.  
- Determinism checks fail beyond configured tolerances.

---

## ⚖ FAIR+CARE & Governance

This pipeline contributes to FAIR+CARE and governance objectives:

- **FAIR**
  - *Findable*: soil datasets are indexed via STAC/DCAT and the KFM graph.  
  - *Accessible*: consistent formats (Parquet/GeoParquet, COGs) and open schemas.  
  - *Interoperable*: alignment with USDA schemas, ISO 19115, STAC/DCAT, PROV-O.  
  - *Reusable*: full provenance, versioning, and quality metrics documented.  

- **CARE & sovereignty**
  - While soil data is generally low sensitivity, it underpins analyses in:
    - Archaeology.  
    - Indigenous land stewardship.  
    - Hydrology and environmental risk.  
  - Governance requirements:
    - Ensure any overlays with sensitive cultural data respect geoprivacy and geoethical standards.  
    - Use CARE-aware masking/generalization where soil interpretations might reveal sensitive contexts in combination with other layers.  

Review expectations:

- Soil Systems and FAIR+CARE Council jointly review pipeline changes.  
- Any major schema or ontology changes require governance approval and a migration plan.  
- Integration with Story Nodes and Focus Mode must respect geoethical and geoprivacy standards.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                |
|--------:|------------|-------------------|------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | Initial governed soil auto-ingest pipeline document. |

Future revisions must:

- Document changes to supported source types, schemas, or ontology mappings.  
- Update telemetry and PROV expectations as schemas evolve.  
- Link to any incident reports or major remapping events affecting soil data.

---

<div align="center">

🟫 **KFM v11.2.4 — Automated Soil Data Ingestion Pipeline (gNATSGO · SSURGO)**  
Deterministic ETL · Catalog-Ready Soil Layers · FAIR+CARE Governance  

[📘 Docs Root](../../..) · [⚙ Pipelines Index](../README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>