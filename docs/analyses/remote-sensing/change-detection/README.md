---
title: "🛰️ Kansas Frontier Matrix — Remote Sensing Change Detection Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/remote-sensing/change-detection/README.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/analyses-remote-sensing-change-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Remote Sensing Change Detection Overview**  
`docs/analyses/remote-sensing/change-detection/README.md`

**Purpose:**  
Document the workflows, datasets, and analytical methods used for detecting and visualizing land-surface and environmental change in Kansas using multi-temporal remote sensing imagery integrated with the KFM geospatial knowledge graph.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../standards/markdown_rules.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-gold)]()
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)]()
[![Scope: Analyses](https://img.shields.io/badge/Scope-Remote--Sensing-orange)]()

</div>

---

## 📚 Overview

The **Change Detection module** of the Kansas Frontier Matrix (KFM) applies AI-enhanced remote sensing analytics to identify, quantify, and visualize temporal landscape changes across Kansas. It integrates satellite imagery, aerial photography, and derived raster datasets (e.g., NDVI, surface water, soil moisture) to assess environmental evolution and human impact. This module bridges **historical cartography**, **modern earth observation**, and **graph-linked event analysis** within the KFM monorepo.

Core objectives:
- Detect multi-decadal land cover and hydrological changes using satellite archives (e.g., Landsat 5–9, Sentinel-2).  
- Align detected changes with historical and ecological datasets (treaties, droughts, floods, land deeds).  
- Automate pipeline reproducibility through FAIR+CARE-compliant metadata, STAC cataloging, and CIDOC CRM alignment.  
- Support AI-assisted “Focus Mode” to narrate environmental transitions for user-selected regions or events.

---

## 🛰️ Datasets and Sources

| Dataset | Description | Temporal Range | Format | Source / Access |
|----------|--------------|----------------|---------|-----------------|
| **Landsat Collection 2 (USGS)** | 30 m multispectral imagery for change detection analysis. | 1984–present | GeoTIFF / STAC | [USGS EROS](https://landsatlook.usgs.gov/) |
| **Sentinel-2 MSI (ESA Copernicus)** | 10–20 m imagery for vegetation, soil, and water indices. | 2015–present | SAFE / GeoTIFF / STAC | [Copernicus Open Hub](https://scihub.copernicus.eu/) |
| **Kansas NAIP Aerial Photos (USDA)** | High-resolution orthophotos for sub-meter change analysis. | 2003–present | GeoTIFF / COG | [USDA Geospatial Data Gateway](https://gdg.sc.egov.usda.gov/) |
| **Historic Aerials / Topographic Maps (USGS)** | Early 20th-century to late-century landscape records. | 1930–1990 | GeoTIFF / JPEG2000 | [USGS Historical Topo](https://www.usgs.gov/programs/national-geospatial-program/topographic-maps) |
| **NASA MODIS & VIIRS** | Coarse-scale NDVI and burn index time series for trend detection. | 2000–present | HDF / NetCDF | [NASA LP-DAAC](https://lpdaac.usgs.gov/) |

Each dataset is indexed via a **STAC v1.0** catalog under `data/stac/remote-sensing/change-detection/` and linked to corresponding **DCAT 3.0** metadata for semantic interoperability.

---

## ⚙️ Methodology

### 1. Preprocessing
- **Cloud Masking:** Implemented via Fmask / Sen2Cor; automated per-scene QA masks.  
- **Radiometric & Atmospheric Correction:** Converted to surface reflectance using USGS LaSRC or Sen2Cor.  
- **Co-registration & Resampling:** All imagery aligned to EPSG:4326 with 30 m grid standard.  
- **STAC Validation:** Each processed scene stored with complete provenance metadata (instrument, acquisition time, calibration parameters, checksum).

### 2. Change Detection Algorithms
- **Spectral Indices Differencing:** NDVI, NDBI, NDWI computed per year; Δ-index images indicate vegetation, built-up, or water change.  
- **Post-Classification Comparison:** Land cover maps classified by Random Forest or U-Net CNN models (trained on NLCD labels).  
- **Time Series Analysis:** Apply linear regression and break-detection (BFAST, CCDC) to NDVI/MODIS data for trend mapping.  
- **Anomaly Mapping:** Detect drought or flood anomalies via standardized indices (SPI, NDWI).  
- **Graph Linkage:** Detected changes stored as `(:Event:EnvironmentalChange)` nodes in Neo4j, linked to affected `(:Place)` and related human `(:Event)` nodes (e.g., `[:ASSOCIATED_WITH]->(:Treaty)`).

### 3. Validation & Visualization
- Compare against known reference datasets (e.g., Kansas GAP, NLCD).  
- Generate **COG hillshade composites** for web streaming.  
- Summaries exported to `docs/reports/remote-sensing/change-validation.md`.  
- Visualizations appear in the web UI as time-layered difference maps within the **Focus Mode environment**.

---

## 🌎 Integration with Focus Mode and Knowledge Graph

Detected change events are semantically encoded in the Neo4j knowledge graph:

```mermaid
graph TD
  RS[Remote Sensing Scene] -->|produces| EC[Environmental Change Event]
  EC -->|affects| PL[Place]
  EC -->|linked_to| HI[Historical Event]
  EC -->|recorded_in| DS[Dataset (STAC Item)]
  HI -->|stored_in| KG[(Knowledge Graph)]
```

Each Environmental Change Event carries:
- `date_start`, `date_end`, `index_type`, `magnitude`, and `confidence` fields.  
- Provenance fields referencing the STAC item, source sensor, and processing script.  
- CARE tags for data sensitivity (e.g., ecological monitoring sites).  

Focus Mode dynamically uses these graph links to summarize **“how this area changed”** when users explore specific counties or landmarks.

---

## 🧪 Reproducibility & FAIR+CARE Compliance

- **FAIR:** All raster outputs registered in STAC + DCAT with SPDX license and DOI.  
- **CARE:** Sensitive ecological or tribal land layers tagged and access-controlled.  
- **MCP Reproducibility:** ETL scripts stored under `src/pipelines/etl/remote-sensing/`; each run logged with environment YAML and SHA256 dataset checksums.  
- **Provenance Tracking:** Each change-event node includes `prov:wasGeneratedBy` metadata linking back to the ETL job, source imagery, and algorithm version.  

---

## 📊 Directory Layout

```
docs/analyses/remote-sensing/change-detection/
├── README.md                  # This file
├── methods/                   # Detailed algorithmic notebooks and workflow docs
├── results/                   # Generated figures, tables, and summaries
├── reports/                   # Validation & accuracy reports
└── governance.md              # Ethical and reproducibility governance notes
```

---

## 🧾 Version History

| Version | Date | Author | Description | Commit |
|----------|------|---------|--------------|---------|
| v10.2.2 | 2025-11-12 | KFM FAIR+CARE Council | Initial release aligned with KFM v10.2.2 architecture and remote sensing pipeline. | `<latest-commit-hash>` |
| v10.0.0 | 2025-10-05 | KFM Core Dev Team | Migrated to new monorepo structure, added Focus Mode integration. | `<hash>` |

---

<p align="center"><b>End of File — docs/analyses/remote-sensing/change-detection/README.md</b></p>