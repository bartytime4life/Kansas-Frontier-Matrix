---
name: 🗃️ Data Request
about: Propose adding a new dataset to the Kansas Frontier Matrix repository.
title: "[DATA REQUEST] <Dataset Name or Theme>"
labels: ["data-request", "needs-review"]
assignees: []
---

## 🗃️ Dataset Overview

Provide key identifying details about the dataset.

| Field | Description |
|:------|:-------------|
| **Dataset Name** | (e.g., “USGS 3DEP LiDAR DEM”) |
| **Primary Source / Organization** | (e.g., USGS, NOAA, NASA, USDA, KHS, etc.) |
| **Data Type** | (e.g., Raster, Vector, Tabular, Text, NetCDF, Mixed) |
| **License** | (e.g., Public Domain, CC-BY 4.0, CC0, Restricted) |
| **Spatial Coverage** | (e.g., Statewide Kansas, Flint Hills, Kansas River Basin) |
| **Temporal Range** | (e.g., 1992–2021) |
| **Access URL / API Endpoint** | (Include direct link or REST endpoint) |
| **Citation / Reference** | (Provide canonical citation, DOI, or dataset identifier) |

---

## 🌐 Data Source Provenance

Describe **where** the data comes from and **how** it can be accessed.

- 🔗 **Official Source URL:**  
  (e.g., `https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer`)  

- 🔑 **Access Method:**  
  (e.g., Open REST API, FTP, HTTP download, Data Portal)

- 🧩 **Data Format(s):**  
  (e.g., GeoTIFF, Shapefile, GeoJSON, CSV, NetCDF, TXT)

- 🗺️ **Coordinate System / Projection:**  
  (e.g., EPSG:4326 WGS84, EPSG:3857 Web Mercator)

- 🧾 **Update Frequency:**  
  (e.g., Annual, Quarterly, Real-time, On-Demand)

---

## 🧩 Intended Integration

Explain **how** and **where** this dataset would fit into the Kansas Frontier Matrix ecosystem.

| Category | Integration Target | Purpose |
|:----------|:------------------|:----------|
| **Pipeline** | (e.g., `terrain_pipeline.py`, `climate_pipeline.py`) | (Processing workflow target) |
| **Data Domain** | (e.g., Terrain, Hydrology, Climate, Hazards, Tabular, Text) | (Classification by theme) |
| **STAC Linkage** | (Yes / No) | (Will a new STAC Item or Collection be created?) |
| **Visualization** | (e.g., Web Map Layer, Timeline Layer, 3D Model) | (Describe usage in web viewer) |

---

## 🧾 Metadata & Schema

Describe or attach sample metadata if available.

| Field | Description |
|:------|:-------------|
| **Attributes / Columns** | (e.g., elevation, slope, aspect, vegetation type, etc.) |
| **Units** | (e.g., meters, degrees Celsius, percent cover) |
| **Schema Source** | (If schema is published, link to it here.) |
| **Example File / Snippet** | (Optional JSON, CSV, or GeoJSON preview) |

---

## 🧮 Validation Requirements

Specify validation needs before integration.

- [ ] Check license and public access terms  
- [ ] Compute and verify SHA-256 checksum  
- [ ] Validate CRS and schema consistency  
- [ ] Generate sample thumbnail / preview  
- [ ] Create STAC metadata record  
- [ ] Confirm successful load via ETL pipeline  

---

## ⚙️ Implementation Plan (Optional)

| Step | Action | Owner | Dependencies |
|:------|:---------|:--------|:--------------|
| 1 | Review data license and provenance |  |  |
| 2 | Fetch and store under `data/raw/<domain>/` |  |  |
| 3 | Add manifest to `data/sources/<domain>/` |  |  |
| 4 | Update `data/checksums/<domain>/` |  |  |
| 5 | Integrate into processing pipeline |  |  |
| 6 | Add to STAC and web visualization layers |  |  |

---

## 🧠 MCP Compliance

| MCP Principle | Confirmation |
|:--------------|:---------------|
| **Documentation-first** | 🗹 Dataset fully described with provenance and structure. |
| **Reproducibility** | 🗹 Data can be fetched and verified deterministically. |
| **Open Standards** | 🗹 Uses open formats (GeoTIFF, CSV, GeoJSON, etc.). |
| **Provenance** | 🗹 Manifest and STAC links provided for traceability. |
| **Auditability** | 🗹 Validation and checksum steps defined for integration. |

---

## 🧩 Additional Notes

Include any extra context or references that will help reviewers evaluate this dataset proposal.  
Attach small sample files, screenshots, or links to metadata portals where possible.

---

**Kansas Frontier Matrix — “Every Dataset Documented. Every Source Proven.”**
```
