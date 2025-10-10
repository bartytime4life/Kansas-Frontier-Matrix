```yaml
---
name: 🗃️ Data Request
about: Propose adding or integrating a new dataset into the Kansas Frontier Matrix (KFM) repository.
title: "[DATA REQUEST] <Dataset Name or Theme>"
labels: ["data-request", "needs-review", "triage"]
assignees: []
version: "v2.1.0"
last_updated: "2025-10-10"
tags: ["data", "integration", "stac", "manifest", "provenance"]
governance:
  requires_license_check: true
  requires_checksum: true
  reviewers_required: 2
mcp:
  documentation_required: true
  provenance_required: true
  validation_required: true
---
```

<div align="center">

# 🗃️ Kansas Frontier Matrix — Data Request Template

### *“Every Dataset Documented. Every Source Proven. Every Integration Reproducible.”*

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 🧾 Dataset Overview

Provide identifying details about the dataset and its stewardship.

| Field                             | Description                                                      |
| :-------------------------------- | :--------------------------------------------------------------- |
| **Dataset Name**                  | (e.g., “USGS 3DEP LiDAR DEM”, “NOAA Drought Monitor 1990–2024”)  |
| **Primary Source / Organization** | (e.g., USGS, NOAA, NASA, USDA, KHS, FEMA, DASC)                  |
| **Data Type**                     | (Raster, Vector, Tabular, Text, NetCDF, Mixed)                   |
| **License**                       | (Public Domain, CC-BY 4.0, CC0, Restricted, Other)               |
| **Spatial Coverage**              | (Statewide Kansas, Flint Hills, Kansas River Basin, Multi-State) |
| **Temporal Range**                | (e.g., 1850–2025, Decadal averages)                              |
| **Access URL / API Endpoint**     | (Direct download, REST API, STAC catalog URL)                    |
| **Citation / DOI / Reference**    | (e.g., `10.5066/P9Z3D4AR` or dataset URL)                        |
| **Contact / Data Steward**        | (if applicable, organization or maintainer name/email)           |

---

## 🌐 Data Source Provenance

Describe **where** the data comes from, **how** it’s accessed, and **why** it’s reliable.

* 🔗 **Official Source URL:**
  (e.g., `https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer`)
* 🔑 **Access Method:**
  (REST API, FTP, HTTP, Open Data Portal, Bulk Download, etc.)
* 🧩 **Data Format(s):**
  (GeoTIFF, Shapefile, GeoJSON, CSV, NetCDF, Parquet)
* 🗺️ **Coordinate System / Projection:**
  (EPSG:4326 WGS84, EPSG:26914 NAD83 / Kansas South, etc.)
* 🧾 **Update Frequency:**
  (Annual, Quarterly, Real-Time, On-Demand)
* 🧮 **Quality Assurance:**
  (e.g., “Validated by NOAA QA/QC process”, “Verified through peer-reviewed publication”)

> **Note:** Include provenance statements or screenshots from official portals for traceability.

---

## 🧩 Intended Integration

Explain **how and where** this dataset fits within the KFM data architecture.

| Category                  | Integration Target                                               | Purpose                                        |
| :------------------------ | :--------------------------------------------------------------- | :--------------------------------------------- |
| **Pipeline**              | (e.g., `hydrology_pipeline.py`, `climate_etl.py`)                | (Processing integration target)                |
| **Data Domain**           | (Terrain, Hydrology, Hazards, Climate, Landcover, Text, Tabular) | (Domain classification)                        |
| **STAC Linkage**          | (Yes / No)                                                       | (Will generate a new STAC Item or Collection?) |
| **Visualization Layer**   | (Web Map, Timeline, Story Map, 3D Scene)                         | (Intended frontend use)                        |
| **Semantic Ontology Tag** | (CIDOC CRM, OWL-Time, PeriodO ID if applicable)                  | (Temporal or cultural linkage)                 |

---

## 🧠 Metadata & Schema

| Field                    | Description                                                    |
| :----------------------- | :------------------------------------------------------------- |
| **Attributes / Columns** | (e.g., elevation, slope, vegetation_type, drought_index, etc.) |
| **Units**                | (meters, °C, %, index, classification code)                    |
| **Schema Source / URL**  | (link to published schema, metadata XML/JSON)                  |
| **Encoding / CRS**       | (UTF-8 / GeoTIFF / EPSG:4326)                                  |
| **Example Snippet**      | Provide a small example (CSV, JSON, GeoJSON feature)           |
| **Metadata Standard**    | (ISO 19115, FGDC, DCAT, STAC 1.0.x)                            |

---

## 🧮 Validation Requirements

Checklist before dataset integration:

* [ ] ✅ Verify **license** & usage rights
* [ ] ✅ Confirm **accessibility** (API reachable, files downloadable)
* [ ] ✅ Compute **SHA-256 checksum** for downloaded assets
* [ ] ✅ Validate **CRS** (projection matches repo standard: EPSG:4326)
* [ ] ✅ Inspect **schema consistency** and attribute completeness
* [ ] ✅ Generate **thumbnail / preview** for documentation
* [ ] ✅ Create **STAC Item / Collection** under `data/stac/`
* [ ] ✅ Validate via `make stac-validate`
* [ ] ✅ Add entry to `data/sources/<domain>/<source>.json` manifest

> All validation steps must pass before PR approval or data merge.

---

## ⚙️ Implementation Plan *(Optional)*

| Step | Action                                    | Owner | Dependencies | Version |
| :--- | :---------------------------------------- | :---- | :----------- | :------ |
| 1    | Review data license & provenance          |       |              |         |
| 2    | Fetch & store under `data/raw/<domain>/`  |       |              |         |
| 3    | Add manifest to `data/sources/<domain>/`  |       |              |         |
| 4    | Compute and record checksums              |       |              |         |
| 5    | Integrate into pipeline (`make <domain>`) |       |              |         |
| 6    | Generate STAC item/collection + metadata  |       |              |         |
| 7    | Visualize in web/timeline layers          |       |              |         |

---

## 🧭 Versioning & Governance

| Scope                     | Current  | Proposed | Reason / Trigger    |
| :------------------------ | :------- | :------- | :------------------ |
| **Dataset (STAC)**        | `v1.0.0` | `v1.1.0` | new layer added     |
| **Domain Pipeline**       | `v2.1.0` | `v2.2.0` | ETL modified        |
| **Repo Release (SemVer)** | `v1.4.0` | `v1.5.0` | dataset integration |
| **Data Source Manifest**  | `v1.0.0` | `v1.0.1` | provenance update   |

> Dataset additions should result in a **minor version bump** (`vX.Y+1.Z`) in `CHANGELOG.md`.

---

## 🧠 MCP Compliance

| MCP Principle           | Confirmation                                                      |
| :---------------------- | :---------------------------------------------------------------- |
| **Documentation-first** | 🗹 Dataset fully described w/ provenance & metadata               |
| **Reproducibility**     | 🗹 Deterministic retrieval & checksum validation defined          |
| **Open Standards**      | 🗹 Data uses interoperable formats (COG, CSV, GeoJSON, NetCDF)    |
| **Provenance**          | 🗹 Manifest, STAC, and log lineage maintained                     |
| **Auditability**        | 🗹 CI validation steps reproducible and archived                  |
| **Versioning**          | 🗹 STAC `properties.version` & SemVer reflected in repo changelog |

---

## 🧩 Related Datasets

* Linked Sources: (e.g., `data/sources/hydro/usgs_nhd_flowlines.json`)
* Complementary Layers: (e.g., NLCD Landcover, NHD Waterbodies)
* Dependent Models: (e.g., Flood Risk, Soil Erosion, Vegetation Index)
* External References: (published studies, data portals, etc.)

---

## 🧰 Attachments

Attach or link small data samples, metadata files, or preview thumbnails.

| File           | Description        | Link / Path                                |
| :------------- | :----------------- | :----------------------------------------- |
| `example.json` | schema preview     | `/data/sources/climate/example.json`       |
| `preview.png`  | thumbnail for docs | `/docs/media/previews/climate_dataset.png` |

---

## 🧾 Maintainer Notes

* Ensure all STAC items pass CI (`make stac-validate`)
* Append dataset to `data/stac/catalog.json`
* Update README in target domain (`data/processed/<domain>/README.md`)
* Add dataset license to `/LICENSES/data/` if distinct
* Run `make checksums` before merge

---

## 🧩 Additional Notes

Include relevant **visual references**, **sample maps**, or **metadata screenshots** for curators.
Provide reasoning for priority (e.g., “critical for flood modeling module”).

---

<div align="center">

### 🧭 Kansas Frontier Matrix

**“Every Dataset Documented · Every Source Proven · Every Version Recorded.”**

</div>
