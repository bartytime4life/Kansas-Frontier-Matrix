---
title: "🟫 Kansas Frontier Matrix — Soil & Air Ingestion Flow (SDA · SSURGO/STATSGO · OpenAQ v3 · CAMS NRT)"
path: "docs/events/environmental/soil-air-ingestion-overview.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Environmental Systems Working Group"
content_stability: "stable"

doc_kind: "Event / Pipeline Overview"
status: "Active"
intent: "soil-air-ingest-architecture"
semantic_document_id: "kfm-doc-environmental-soil-air-ingest-v11.2.6"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/soil-air-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/soil-air-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

header_profile: "standard"
footer_profile: "standard"
---

# 🟫 Soil & Air Ingestion Flow  
SDA (SSURGO/STATSGO) · OpenAQ v3 · CAMS NRT · Deterministic ETL → STAC/DCAT/PROV → Neo4j

KFM v11.2.6 performs deterministic ingestion of **soil** and **air-quality** observations across multiple public sources, with guardrails for reproducibility, chunk-safe ingestion, and cross-sensor harmonization.

> Pipeline fit: **Raw → Work → Processed → STAC/DCAT/PROV → Neo4j → API → Story Nodes → Focus Mode**

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 events/
    ├── 📁 environmental/
    │   ├── 📄 README.md
    │   └── 📄 soil-air-ingestion-overview.md    # 🟫 This file (soil & air ingestion overview)
    └── 📁 remote-sensing/
        ├── 📄 README.md
        └── 📄 stac-telemetry-overview.md        # 📡 STAC telemetry spec (freshness, energy, SLO)

src/
└── 📁 pipelines/
    └── 📁 environmental/
        ├── 📄 soil_ingest_sda.py                # SDA/SSURGO/STATSGO ingestion
        ├── 📄 air_ingest_openaq_cams.py         # OpenAQ v3 + CAMS NRT ingestion & enrichment
        └── 📄 soil_air_harmonize.py             # Soil + air joint harmonization

configs/
└── 📁 pipelines/
    └── 📁 environmental/
        ├── 📄 soil-sda-v11.yaml                 # SDA chunking + soil schema config
        ├── 📄 air-openaq-v3-v11.yaml            # OpenAQ v3 ingestion policy
        └── 📄 air-cams-nrt-v11.yaml             # CAMS NRT cadence + enrichment policy

data/
└── 📁 processed/
    └── 📁 environmental/
        ├── 📄 soil_layers.parquet               # Harmonized soil products
        └── 📄 air_quality_harmonized.parquet    # Harmonized air-quality products

mcp/
└── 📁 experiments/
    └── 📁 environmental/
        └── 📄 soil-air-ingestion-log.jsonl      # Deterministic logs + PROV references
~~~

Related governance and specs:

- `docs/data/air-quality/README.md` — air-quality sources & API governance  
- `docs/data/air-quality/unit-conversion/README.md` — ppb ↔ µg/m³ conversion guide  
- soil dataset governance (future: `docs/data/soil/README.md`)  

---

## 📘 Overview

KFM integrates two primary environmental channels:

1. **Soils (SDA / SSURGO / STATSGO)**  
   - SDA `post.rest` API  
   - deterministic chunking (≤ 100 k row & ≈ 32 MB return-size constraints)  
   - resolution-aware separation of **SSURGO** vs **STATSGO**  
   - graph modeling across **MapUnit → Component → Horizon**

2. **Air Quality (OpenAQ v3 + CAMS NRT)**  
   - bounding-box + time-window queries over Kansas AOIs  
   - harmonized **measurement schema** and unit-safe handling  
   - optional enrichment using atmospheric model fields from **CAMS NRT**

Outputs flow through the KFM pipeline and land as:

- STAC Collections/Items (`KFM-STAC v11`)  
- DCAT datasets (`KFM-DCAT v11`)  
- Neo4j graph nodes for soils and air-quality  
- Story Nodes / Focus Mode layers for environmental narratives

---

## 🟫 Soil: SDA Deterministic Ingestion

### Key API & Chunking Constraints

- SDA JSON responses capped at **100 000 rows** per query.  
- Effective payload limit ≈ **32 MB** per response.  
- Ingestion MUST use a deterministic **chunk plan**, such as:
  - `areasymbol` groupings  
  - `mukey` partitions  
  - spatial tiles (e.g., 1×1 degree or custom grid)  

Because **SSURGO** (high-resolution) and **STATSGO** (generalized) share SDA’s backing store, KFM must:

- explicitly request which resolution (e.g., SSURGO-only, STATSGO-only)  
- prevent accidental intermixing when building harmonized products  

### KFM Soil Graph Model (Draft)

| Node label       | Description                                           |
|------------------|-------------------------------------------------------|
| `SoilMapUnit`    | Mapunit boundary + metadata (SSURGO/STATSGO)         |
| `SoilComponent`  | Soil component and taxonomic properties              |
| `SoilHorizon`    | Horizon-level texture/chemical attributes            |
| `SoilSurveyArea` | Survey geography / area symbol                       |
| `SoilProperty`   | Extracted & normalized parameter/value records       |

Key relationships (directional, subject to KFM-OP review):

- `(:SoilSurveyArea)-[:HAS_MAPUNIT]->(:SoilMapUnit)`  
- `(:SoilMapUnit)-[:HAS_COMPONENT]->(:SoilComponent)`  
- `(:SoilComponent)-[:HAS_HORIZON]->(:SoilHorizon)`  
- `(:SoilHorizon)-[:HAS_PROPERTY]->(:SoilProperty)`  

STAC integration:

- soil survey area-level STAC Items:
  - geometry: survey area or tiled footprint  
  - properties:
    - `kfm:source_id = "sda"`  
    - `kfm:soil_resolution = "ssurgo" | "statsgo"`  
    - `kfm:chunk_plan_id` for deterministic re-runs  

---

## 🌬️ Air: OpenAQ v3 + CAMS NRT Integration

### OpenAQ v3 Highlights

- v1 and v2 retired in 2025 → **v3 only**.  
- KFM uses:
  - `bbox` queries over Kansas AOIs  
  - `date_from` / `date_to` with configured freshness windows  
  - `parameters[]` to restrict to relevant pollutants.  

OpenAQ responses are parsed into a harmonized schema:

- `AirObservation` — a measurement of `(parameter, value, unit)` at `(time, location)`  
- `SensorNode` — physical sensor or station metadata (network, operator, location)  
- `ParameterUnit` — unit & parameter metadata (with unit-conversion context)  
- `SourceNetwork` — upstream provider/network information  

Graph relationships:

- `(:SensorNode)-[:RECORDED]->(:AirObservation)`  
- `(:AirObservation)-[:OF_PARAMETER]->(:ParameterUnit)`  
- `(:SensorNode)-[:PART_OF_NETWORK]->(:SourceNetwork)`  

### CAMS NRT Enrichment

- CAMS NRT provides modeled fields such as:
  - PM₂.₅, O₃, NO₂  
  - speciation  
  - aerosol optical depth (AOD)  

Used when:

- ground sensors are sparse, or  
- interpolations are needed for Story Nodes / Focus Mode maps.  

**Provenance rule:** CAMS-sourced values must be stored as **separate assets/entities**, not mixed into raw in situ observations:

- separate STAC assets for model-derived fields  
- distinct graph nodes (e.g., `ModeledAirField`) with `DERIVED_FROM` links to model runs  
- clear `kfm:source_id = "cams-nrt"`  

This preserves **provenance purity** and prevents confusion between observational and modeled values.

---

## 🔄 ETL Summary (Deterministic)

### 🟫 Soil ETL Flow

1. **Chunk Plan Build**  
   - Precompute SDA chunk plan (areasymbol / mukey / spatial grid) and record:
     - configuration hash  
     - chunk IDs  
     - expected row counts per chunk (if available).

2. **Chunked SDA Queries**  
   - Execute SDA queries according to the chunk plan.  
   - Enforce:
     - ≤ 100 000 rows per response  
     - ≈ 32 MB payload limit.  

3. **Validation & Normalization**  
   - Apply table-integrity tests (e.g., Great Expectations) to each chunk.  
   - Normalize SDA relational schema into KFM soil schema (`SoilMapUnit`, `SoilComponent`, `SoilHorizon`, etc.).  

4. **STAC/DCAT Cataloging**  
   - Build STAC Collections (SSURGO, STATSGO) and Items per survey area / tile.  
   - Register DCAT datasets describing coverage, resolution, and license.  

5. **Graph Ingestion (Neo4j)**  
   - Upsert soil graph nodes and relationships.  
   - Ensure idempotent updates keyed by SDA identifiers and chunk IDs.  

6. **Telemetry & PROV**  
   - Emit energy/carbon telemetry for data pulls and processing.  
   - Write PROV bundles capturing:
     - chunk plan  
     - SDA queries  
     - normalization steps  

### 🌬️ Air ETL Flow

1. **OpenAQ v3 Fetches**  
   - Query OpenAQ v3 within Kansas AOIs and configured time windows.  
   - Deduplicate by `(sensor, parameter, timestamp)`.  

2. **Optional CAMS NRT Overlays**  
   - Retrieve CAMS NRT fields over matching spatiotemporal grids.  
   - Join onto observation grids as **separate modeled fields**, not overwriting observations.  

3. **Harmonization & Unit Handling**  
   - Normalize into harmonized air-quality schema.  
   - Defer ppb ↔ µg/m³ conversions to the unit-conversion pipeline, using:
     - `docs/data/air-quality/unit-conversion/README.md`.  

4. **STAC/DCAT Packaging**  
   - Create time-tiled STAC Items with:
     - observational and modeled assets clearly separated  
     - telemetry properties (freshness, energy, SLO state) per STAC telemetry spec.  
   - Register DCAT datasets with coverage and license metadata.  

5. **Graph Upserts**  
   - Upsert `SensorNode`, `AirObservation`, model fields, and region nodes.  
   - Maintain stable identifiers to ensure idempotent writes.  

6. **Telemetry & SLO Signals**  
   - Attach telemetry about:
     - query cost  
     - data volume  
     - compute and IO usage  
   - Push SLO-related signals into:
     - `soil-air-telemetry.json`  
     - STAC telemetry fields (`kfm:slo_state`, etc., where applicable).  

---

## 📖 Story Node & Focus Mode Integration

Soil and air layers feed into **Story Nodes** and **Focus Mode** to support cross-environment narratives.

### Soil Layers

Story Nodes may reference:

- **Land Capability** — from soil classifications and component properties  
- **Hydric Probability** — hydric soil flags and horizon properties  
- **Horizon Chemistry** — pH, nutrients, contaminants  
- **Texture Profiles** — vertical structure relevant to hydrology and root-zone behavior  

Spatial/temporal extents are linked to:

- `SoilSurveyArea` and `SoilMapUnit` nodes  
- STAC items representing particular survey tiles or products  

### Air Layers

Story Nodes may highlight:

- **Exposure Timelines** — pollutant concentrations over time for specific communities or regions  
- **AQ Episodes** — smoke events, dust storms, ozone spikes  
- **Sensor Reliability** — data gaps, calibration periods, or persistent outliers  
- **Region Health Index** — derived indicators combining multiple pollutants and model information  

### Cross-Environment Reasoning

Focus Mode can combine soil and air layers to explore:

- soil moisture / surface properties vs **PM₂.₅** episodes  
- wind patterns, land cover, soil texture vs **dust events**  
- joint exposure patterns in relation to **hydrology and land management**  

Story Nodes must clearly distinguish:

- **facts** — derived directly from catalogs and graph data  
- **interpretation** — Environmental Systems WG’s reading  
- **speculation** — hypotheses for future validation  

---

## 🧪 Validation & Provenance

Validation and provenance are mandatory for both soil and air pipelines:

- **STAC/DCAT Validation**
  - STAC Collections/Items validated against `KFM-STAC v11`.  
  - DCAT datasets validated against `KFM-DCAT v11`.  

- **PROV-O / OpenLineage**
  - PROV bundles describe:
    - raw API queries  
    - chunk plans and intermediate tables  
    - normalization transforms  
    - model-inference (CAMS) layers  
  - OpenLineage (or equivalent) connects pipeline runs across soil and air ingestion.  

- **Checksums**
  - per-chunk and per-bundle checksums computed and recorded in provenance.  

- **Telemetry**
  - ingestion-level telemetry written to `soil-air-telemetry.json`:
    - data volumes  
    - runtimes  
    - energy/carbon metrics  

---

## 🕰️ Version History

| Version  | Date       | Notes                                                        |
|----------|------------|--------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Initial aligned soil + air ingestion overview for KFM v11.2.6 |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **Environmental Systems Working Group**, with co-review by the FAIR+CARE Council and Governance Council  
- must be updated when soil or air ingestion architecture, source mix, or telemetry/provenance patterns materially change

Edits require approval from the Environmental Systems WG and FAIR+CARE Council and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and soil/air ETL and telemetry validation workflows.

<br/>

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🟫 **Kansas Frontier Matrix — Soil & Air Ingestion Flow v11.2.6**  
Deterministic SDA & AQ Ingestion · STAC/DCAT/PROV Aligned · FAIR+CARE Environmental Governance  

[📘 Docs Root](../../README.md) · [🌱 Environmental Events Index](./README.md) · [📊 Data Docs Index](../../data/README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>