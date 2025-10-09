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
| **Primary Source / Organization** | (e.g., USGS, NOAA, NASA, USDA, KHS) |
| **Data Type** | (e.g., Raster, Vector, Tabular, Text, NetCDF, Mixed) |
| **License** | (e.g., Public Domain, CC-BY 4.0, CC0, Restricted) |
| **Spatial Coverage** | (e.g., Statewide Kansas, Flint Hills, Kansas River Basin) |
| **Temporal Range** | (e.g., 1992–2021) |
| **Access URL / API Endpoint** | (Direct download or REST endpoint) |
| **Citation / Reference** | (Canonical citation, DOI, or dataset ID) |

---

## 🌐 Data Source Provenance
Describe **where** the data comes from and **how** it can be accessed.

- 🔗 **Official Source URL:**  
  (e.g., `https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer`)
- 🔑 **Access Method:**  
  (e.g., REST API, FTP, HTTP download, data portal)
- 🧩 **Data Format(s):**  
  (e.g., GeoTIFF, Shapefile, GeoJSON, CSV, NetCDF)
- 🗺️ **Coordinate System / Projection:**  
  (e.g., EPSG:4326 WGS84, EPSG:3857 Web Mercator)
- 🧾 **Update Frequency:**  
  (e.g., Annual, Quarterly, Real-time, On-Demand)

---

## 🧩 Intended Integration
Explain **how** and **where** this dataset fits into the KFM ecosystem.

| Category | Integration Target | Purpose |
|:----------|:------------------|:----------|
| **Pipeline** | (e.g., `terrain_pipeline.py`, `climate_pipeline.py`) | (Processing target) |
| **Data Domain** | (e.g., Terrain, Hydrology, Climate, Hazards, Tabular, Text) | (Domain classification) |
| **STAC Linkage** | (Yes / No) | (Will a new STAC Item or Collection be created?) |
| **Visualization** | (e.g., Web Map Layer, Timeline Layer, 3D Model) | (Intended web/UI use) |

---

## 🧾 Metadata & Schema
Provide or link metadata describing structure and attributes.

| Field | Description |
|:------|:-------------|
| **Attributes / Columns** | (e.g., elevation, slope, vegetation_type, etc.) |
| **Units** | (e.g., meters, degrees Celsius, percent cover) |
| **Schema Source** | (If published, provide schema link.) |
| **Example File / Snippet** | (Optional JSON, CSV, or GeoJSON sample.) |

---

## 🧮 Validation Requirements
Define checks before dataset integration.

- [ ] Verify license and public access terms  
- [ ] Compute and confirm SHA-256 checksum  
- [ ] Validate CRS and schema consistency  
- [ ] Generate thumbnail / preview image  
- [ ] Create STAC Item / Collection metadata  
- [ ] Confirm successful ETL load  

---

## ⚙️ Implementation Plan *(Optional)*
| Step | Action | Owner | Dependencies |
|:------|:---------|:--------|:--------------|
| 1 | Review data license and provenance |  |  |
| 2 | Fetch and store under `data/raw/<domain>/` |  |  |
| 3 | Add manifest to `data/sources/<domain>/` |  |  |
| 4 | Update `data/checksums/<domain>/` |  |  |
| 5 | Integrate into processing pipeline |  |  |
| 6 | Add to STAC catalog and web visualization layers |  |  |

---

## 🧠 MCP Compliance

| MCP Principle | Confirmation |
|:---------------|:--------------|
| **Documentation-first** | 🗹 Dataset described with provenance and structure |
| **Reproducibility** | 🗹 Data can be fetched and verified deterministically |
| **Open Standards** | 🗹 Open formats (GeoTIFF, CSV, GeoJSON, etc.) used |
| **Provenance** | 🗹 Manifest and STAC links ensure lineage traceability |
| **Auditability** | 🗹 Validation and checksum processes defined |

---

## 🧩 Additional Notes
Add any extra details, related datasets, or visual references for maintainers.  
Include small samples, thumbnails, or metadata screenshots if possible.

---

**Kansas Frontier Matrix — “Every Dataset Documented. Every Source Proven.”**
