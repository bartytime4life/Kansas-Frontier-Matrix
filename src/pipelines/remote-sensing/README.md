---
title: "🛰️ Kansas Frontier Matrix — Remote Sensing Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-remote-sensing-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Remote Sensing Pipelines**  
`src/pipelines/remote-sensing/README.md`

**Purpose:**  
Define the complete remote-sensing ETL architecture for KFM — ingestion, preprocessing, harmonization, analysis, STAC publication, provenance, CARE-aware masking, and Neo4j integration of satellite-derived geospatial products (optical, multispectral, SAR, DEM, climate composites, hazards, and ecological indicators).  

These pipelines convert **raw satellite products** into **FAIR+CARE-certified, STAC/DCAT-aligned, provenance-tracked geospatial assets** powering KFM’s map layers, climate/ecology analyses, and Focus Mode narratives.

<img alt="Remote Sensing" src="https://img.shields.io/badge/Remote_Sensing-ETL-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Integrated-orange"/>
<img alt="GDAL" src="https://img.shields.io/badge/GDAL-3.12-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

KFM remote-sensing pipelines incorporate:

- **Satellite providers**: LANDSAT, Sentinel-1/2, NAIP, MODIS, VIIRS  
- **Geospatial tools**: GDAL 3.12, rasterio, GeoParquet, xarray, dask  
- **Specialized processing**:  
  - Atmospheric correction  
  - Cloud/shadow masking  
  - Terrain correction for SAR  
  - Temporal compositing (monthly/seasonal)  
  - Change detection  
  - VI, NDVI, NDMI, NDWI, SAVI  
  - Hazard extraction (burn scars, flood extents, drought indicators)

Pipelines output:

- Processed COGs  
- GeoParquet vectors  
- STAC Items/Collections  
- Provenance lineages  
- AI-ready arrays for downstream models  
- MapLibre/Cesium tiles (when configured)

All outputs satisfy FAIR+CARE, provenance, and MCP-DL v6.3.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/
├── README.md                          # This file
│
├── ingest/                            # Fetch + stage provider assets
│   ├── landsat_ingest.py
│   ├── sentinel2_ingest.py
│   ├── sentinel1_ingest.py
│   ├── naip_ingest.py
│   └── modis_ingest.py
│
├── preprocessing/                     # Sensor-specific corrections
│   ├── cloud_mask.py
│   ├── atmospheric_correction.py
│   ├── sar_terrain_correction.py
│   ├── reprojection.py
│   └── harmonization.py
│
├── analytics/                         # Derivative products
│   ├── ndvi.py
│   ├── ndmi.py
│   ├── ndwi.py
│   ├── burn_scar.py
│   ├── flood_extent.py
│   └── change_detection.py
│
├── stac/                              # STAC integration tools
│   ├── build_item.py
│   ├── build_collection.py
│   ├── validate_item.py
│   └── publish.py
│
├── lineage/                           # PROV-O + checksum generation
│   ├── lineage_builder.py
│   ├── checksum_tools.py
│   └── provenance.jsonld
│
└── utils/                             # Shared helpers
    ├── read_write.py
    ├── geospatial.py
    ├── masking.py
    └── timestamps.py
~~~~~

---

## 🧩 Remote Sensing ETL Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Provider API / Bucket<br/>LANDSAT · Sentinel · MODIS · NAIP"] --> B["ingest/*"]
  B --> C["preprocessing/*<br/>Cloud Mask · AtmoCorr · TerrainCorr"]
  C --> D["analytics/*<br/>NDVI · NDMI · Change Detection"]
  D --> E["stac/build_item.py<br/>STAC Item Construction"]
  E --> F["stac/validate_item.py<br/>STAC Schema + GE Gate"]
  F -->|PASS| G["stac/publish.py<br/>COG/Parquet → Catalog"]
  F -->|FAIL| H["Quarantine<br/>Governance Review"]
  G --> I["lineage/*<br/>PROV-O · Checksums"]
  I --> J["Graph Hydration<br/>Scenes → Datasets → Themes"]
  G --> K["Focus Mode v2.4<br/>Narratives · Explanations"]
~~~~~

---

## 🌐 Supported Sensor Families

### 🛰️ Optical (Multispectral)
- **LANDSAT Collection 2 Level-2**
- **Sentinel-2 MSI**
- **NAIP aerial imagery**

Corrections & preprocessing:
- Cloud + shadow masks (FMask/S2Cloudless)  
- TOA → BOA reflectance  
- GSD normalization (10m/30m harmonization)

### 📡 SAR
- **Sentinel-1 GRD**
- Terrain correction  
- Speckle filtering  
- Backscatter normalization (σ° / γ°)  

### 🌏 Thermal / Environmental
- **MODIS**, **VIIRS**
- LST, thermal anomalies, drought composites

---

## ⚙️ Preprocessing Standards

All pipelines MUST:

- Reproject to **EPSG:4326**  
- Store COG output using:
  - `compress=DEFLATE`, `predictor=yes`, `tiled=true`, `overviews=auto`  
- Produce GeoParquet using:
  - `geometry: WGS84`  
  - `statistics=enabled`  
  - `dictionary-encoded strings`  

Cloud/shadow masking:
- CLOUD_MASK, SHADOW_MASK, QA_BAND required  
- No unmasked invalid data may pass validation

---

## 🔎 Analysis Modules (Derivatives)

### NDVI / NDMI / NDWI  
Computed using normalized formulas with sensor-appropriate coefficients.

### Change Detection  
Supports:
- Post-fire
- Flood extent  
- Drought monitoring  
- Agriculture health shifts  

### SAR Flood Extraction  
Combines:
- Backscatter calibration  
- Thresholding  
- Terrain correction  
- Hysteresis filters  

---

## 📦 STAC Publication Workflow

All processed assets MUST:

- Include EO, SAR, PROJ, and Raster STAC extensions as appropriate  
- Include STAC Item fields:
  - `proj:shape`, `proj:transform`  
  - `raster:bands`  
  - `eo:bands`  
  - `kfm:*` metadata (provenance, lineage, ingest version)  
- Be validated with:
  - JSON Schema  
  - Great Expectations checkpoint  
  - CARE governance validator  

---

## 🧬 Provenance & Lineage Requirements

All pipelines MUST:

- Generate `kfm:checksum` using sha256  
- Produce lineage JSON-LD following PROV-O:  
  - `prov:Entity` (input rasters)  
  - `prov:Activity` (ETL stages)  
  - `prov:wasGeneratedBy`  
  - `prov:used`  
- Reference upstream STAC Items when applicable  
- Link to versioning & governance ledgers

---

## ⚖️ FAIR+CARE Governance Requirements

### Masking Rules  
Remote sensing pipelines must enforce:

- No unmasked precise coordinates for **restricted** datasets  
- H3-based generalization where required  
- Raster masking for cultural/tribal sensitive areas  

### CARE Enforcement  
- CARE labels must propagate from input → derivative  
- Sovereignty conflicts must be logged  
- Governance escalations must halt publication

---

## 📡 Telemetry Integration

Remote-sensing telemetry MUST include:

- `rows_processed`, `raster_pixels_processed`  
- `processing_time_sec`  
- `energy_wh`, `co2_g`  
- `validation_passed`, `care_violations`  
- `publish_latency_ms`  
- Inputs & outputs checksums

Telemetry written to:

~~~~~text
../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Local Development

~~~~~bash
# Example: Sentinel-2 ingest + NDVI + STAC publish
python src/pipelines/remote-sensing/ingest/sentinel2_ingest.py --aoi data/geometry/kansas_aoi.geojson
python src/pipelines/remote-sensing/preprocessing/cloud_mask.py
python src/pipelines/remote-sensing/analytics/ndvi.py
python src/pipelines/remote-sensing/stac/build_item.py
python src/pipelines/remote-sensing/stac/publish.py
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Full remote-sensing pipeline architecture added with STAC, provenance, CARE, and telemetry integration. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Pipelines**  
High-Integrity Geospatial ETL × FAIR+CARE Governance × Scientific Reproducibility  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>
