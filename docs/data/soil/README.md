---
title: "🌱 Kansas Frontier Matrix — Soil Data Integration Overview (SSURGO · SDA · gNATSGO)"
path: "docs/data/soil/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · Earth Systems Working Group"
content_stability: "stable"
status: "Active"

doc_kind: "Data Domain Overview"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-doc-data-soil-overview-v11.2.6"
doc_uuid: "urn:kfm:doc:data:soil:overview:v11.2.6"
event_source_id: "ledger:docs/data/soil/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/soil-telemetry.json"
telemetry_schema: "../../schemas/telemetry/soil-data-domain-v11.json"
governance_ref: "../standards/governance/DATA-GOVERNANCE.md"
---

# 🌱 Kansas Frontier Matrix — Soil Data Integration Overview  
**SSURGO · SDA Incremental API · gNATSGO Statewide Raster Refresh**  
`docs/data/soil/README.md` (v11.2.6)

## 📘 Overview

The soil domain integrates:

- **High-fidelity SSURGO** tabular and polygon survey data,  
- **SDA REST/POST SQL** incremental deltas, and  
- **Statewide gNATSGO** raster composites  

into the deterministic KFM pipeline:

> ETL → STAC/DCAT/PROV → Neo4j Graph Entities → API Layer → Web Clients → Story Nodes → Focus Mode

This document provides a **domain-level architecture overview** for soil data: how it enters KFM, how it is updated, how it is represented in catalogs and the knowledge graph, and how it is exposed to APIs, Story Nodes, and Focus Mode.

---

## 🗂️ Directory Layout

The soil domain documentation follows KFM’s emoji-style directory convention:

~~~text
📁 docs/
  📁 data/
    📁 soil/
      📄 README.md                 # This file – soil data domain overview
      📁 sda/
        📄 queries.md              # SDA SQL query patterns and examples
        📄 incremental-refresh.md  # Incremental refresh strategy and schedules
      📁 ssurgo/
        📄 schema.md               # SSURGO schema notes and table mappings
        📄 stac-collection.md      # STAC Collection definition for SSURGO
      📁 gnatsgo/
        📄 raster-layers.md        # gNATSGO layer descriptions and usage
        📄 stac-collection.md      # STAC Collection definition for gNATSGO rasters
~~~

Additional files under `docs/data/soil/` MUST be documented here as they are added, and kept consistent with the KFM-MDP v11.2.6 style.

---

## 🧭 Context — Core Soil Sources

Soil information in Kansas is anchored on three coordinated sources.

### SSURGO (Soil Survey Geographic Database)

Fine-resolution polygon and tabular soil survey datasets. KFM ingests SSURGO as **authoritative tabular truth**, preserving:

- `MUKEY` topology and spatial units  
- Map unit composition tables  
- Horizon tables and component-level properties  
- Additional survey metadata required for long-term comparability

### SDA (Soil Data Access) — Incremental SQL over REST

SDA provides **live, query-driven deltas** via the `sdmAPI/post.rest` service, using parameterized SQL to fetch only records changed since a given timestamp.

In KFM, SDA powers an **incremental refresh model**:

- Reduces bandwidth and ETL cost versus full reloads.  
- Enables near-real-time correction of soil attributes.  
- Feeds provenance-aware graph updates without full SSURGO re-ingest.

### gNATSGO — Statewide Soil Raster Composite

gNATSGO provides cloud-optimized raster (COG) layers built from SSURGO, STATSGO2, and raster soil survey products. In KFM, these rasters are used for:

- Modeling and spatial analysis (hydrology, erosion, productivity).  
- ML feature generation and scenario modeling.  
- Tiled visualization in Focus Mode and other map-based interfaces.

---

## 🧱 Architecture — Deterministic ETL & Graph Integration

### Input Sources

- **SSURGO**  
  - Tabular and vector datasets (local & cloud mirrors; versioned archive bundles).  

- **SDA**  
  - Real-time JSON deltas from `sdmAPI/post.rest`.  

- **gNATSGO**  
  - COG rasters and attribute tables (e.g., texture, depth, Ksat, hydrologic group).

### Soil ETL Steps

1. **Extract**

   - Pull SDA deltas per county or statewide MUKEY ranges (config-driven).  
   - Import SSURGO archive drops via versioned bundles.  
   - Ingest gNATSGO rasters and attributes (texture, depth, Ksat, hydrologic group, etc.).

2. **Transform**

   - Map hydrologic and pedologic properties to the KFM Soil Ontology (KFM-OP v11).  
   - Normalize depths, texture classes, and horizon definitions to stable KFM-wide conventions.  
   - Generate derived metrics for hydrology, agriculture, and climate pipelines (e.g. available water capacity, erosion indices).

3. **Load**

   - Publish STAC Items for soil tables and rasters (SSURGO, SDA deltas, gNATSGO layers).  
   - Populate Neo4j with soil-related entities and relationships (see Graph Model).  
   - Emit PROV-O bundles for each ETL run and derived dataset, including upstream dataset IDs, time windows, and config versions.

### Graph Model (Neo4j v11 Schema)

**Entities**

- `:SoilUnit` (MUKEY root)  
- `:SoilComponent`  
- `:SoilHorizon`  
- `:SoilProperty`  
- `:RasterLayer` (gNATSGO and related rasters)

**Relationships**

- `(:SoilUnit)-[:HAS_COMPONENT]->(:SoilComponent)`  
- `(:SoilComponent)-[:HAS_HORIZON]->(:SoilHorizon)`  
- `(:SoilHorizon)-[:HAS_PROPERTY]->(:SoilProperty)`  
- `(:RasterLayer)-[:DERIVED_FROM]->(:SoilUnit)` or underlying SSURGO/STATSGO entities  
- `(:RasterLayer)-[:COVERS_AREA]->(:Place)` for raster footprints  
- `(:SoilUnit)-[:UPDATED_BY]->(:SdaDelta)` (if modeled explicitly for SDA updates)

**Integration Rules**

- `MUKEY` is the canonical key for SSURGO-based entities.  
- SDA deltas may promote targeted graph updates (specific MUKEY ranges or tables) without full SSURGO refresh.  
- gNATSGO rasters are aligned by **spatial join plus MUKEY lookup** when available, with fallbacks to STATSGO-level units.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

**Collections (examples)**

- `soil-ssurgo-v11` — SSURGO tabular and polygon products.  
- `soil-sda-deltas-v11` — SDA change sets (by time window or region).  
- `soil-gnatsgo-v11` — gNATSGO raster composites and layers.

**Assets**

- JSON dumps of SSURGO tables (geoparquet/CSV).  
- Polygon shapefiles/GeoPackage/GeoParquet for map units.  
- gNATSGO COG rasters and attribute tables.

**Extensions**

- `checksum` — cryptographic hashes for all core assets.  
- `versions` — explicit dataset versioning and supersession metadata.  
- `provenance` / `processing` — links to ETL and SDA delta activities.

### DCAT

Dataset-level relationships:

- **SSURGO** — canonical tabular dataset representing survey truth.  
- **SDA** — update stream dataset with references back to SSURGO.  
- **gNATSGO** — derivative raster dataset with explicit lineage to SSURGO/STATSGO2.

DCAT records should describe:

- Spatial and temporal coverage (Kansas and relevant time extents).  
- Licensing, access constraints, and update cadence.  
- Links to STAC Collections and Items used in downstream processing.

### PROV-O

Each soil processing step emits PROV-O records:

- `prov:Entity` — ETL inputs (SSURGO archives, SDA deltas, gNATSGO rasters), intermediate tables, and final graph/raster outputs.  
- `prov:Activity` — extraction, transformation, and load runs (including SDA delta jobs).  
- `prov:Agent` — KFM ETL services, SDA service, USDA/NRCS as data providers.

Typical relations:

- `prov:wasGeneratedBy` — final soil tables/rasters generated by a given ETL run.  
- `prov:used` — SDA delta batches and SSURGO sources used in the run.  
- `prov:wasDerivedFrom` — gNATSGO products derived from SSURGO/STATSGO.  

---

## 📦 API Exposure (FastAPI / GraphQL)

### REST (Examples)

- `GET /soil/{mukey}`  
  - Retrieve soil unit and component details for a given MUKEY.  

- `GET /soil/horizon/{component_id}`  
  - Retrieve horizons and key properties for a soil component.  

- `GET /soil/raster/{layer}/{z}/{x}/{y}`  
  - Tile endpoint for gNATSGO and related raster layers.  

- `GET /soil/sda/changes?since={timestamp}`  
  - SDA delta API surface for pipeline/debug usage (governed).  

### GraphQL (Conceptual Example)

~~~graphql
query {
  soilUnit(mukey: "123456") {
    name
    components {
      name
      horizons {
        depthTop
        depthBottom
        texture
      }
    }
  }
}
~~~

API schemas live under `src/api/` and must remain aligned with the graph schema described above.

---

## 🧠 Story Node & Focus Mode Integration

Soil data powers a range of narrative and scenario-driven features in KFM.

### Story Nodes

Representative topics:

- **Settlement viability** and land-use histories linked to soil capability.  
- **Agricultural productivity timelines** across changing climate and management regimes.  
- **Pre-contact land-use reconstruction** grounded in soil and hydrological properties.  
- **Streambank and erosion risk narratives** for specific watersheds.  

Soil Story Nodes SHOULD:

- Reference specific soil datasets and gNATSGO layers via STAC/DCAT IDs.  
- Link to relevant graph entities (`SoilUnit`, `SoilComponent`, etc.).  
- Clearly separate data-backed facts from interpretive or speculative content.

### Focus Mode (v3)

Focus Mode may provide scenario sliders and overlays for:

- Soil moisture and storage capacity.  
- Texture influence on runoff and infiltration.  
- Carbon sequestration potential at different depths.  
- Aquifer recharge profiles and vulnerability.

All such scenarios MUST:

- Document which soil and climate datasets they use.  
- Record provenance for each scenario run.  
- Respect governance rules for sensitive interpretations (e.g., land valuation, risk scoring).

---

## ⚖ Governance, Provenance & Telemetry

### Governance

- All SDA queries are logged with:
  - SQL text (or an approved template identifier).  
  - Response hash and row counts.  
  - SDA service timestamp and status codes.  

- All gNATSGO rasters and derived products:
  - Include COG-level checksums and version tags.  
  - Are tied to STAC/DCAT datasets with clear derivation paths.

### Telemetry

Soil ETL and related pipelines emit telemetry captured in `soil-telemetry.json`, including:

- ETL runtime and success/failure status.  
- Energy/carbon cost per ETL job (via `energy_schema` and `carbon_schema` where applicable).  
- SDA request frequencies, error rates, and latency distributions.  
- Raster tiling throughput and cache hit rates for soil map services.

Telemetry is used for:

- Reliability and sustainability tracking.  
- Capacity planning and optimization of SDA query schedules.  
- Auditing and governance reporting.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                 |
|----------:|-----------:|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | Aligned soil domain overview with KFM-MDP v11.2.6; clarified ETL, STAC/DCAT/PROV, graph model, and API integration. |
| v11.2.5   | —          | Initial integration of gNATSGO rasters into soil domain architecture.  |
| v11.2.4   | —          | First unified soil domain architecture and SSURGO/SDA integration.     |

---

<div align="center">

🌱 **Kansas Frontier Matrix — Soil Data Integration Overview**  
Soil Surveys · SDA Deltas · gNATSGO Rasters  

[📘 Docs Root](../README.md) · [📂 Data Index](../README.md) · [⚖ Data Governance](../standards/governance/DATA-GOVERNANCE.md)

</div>