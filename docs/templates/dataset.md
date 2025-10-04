<div align="center">

# 🗃️ Kansas Frontier Matrix — Dataset Documentation Template  
`docs/templates/dataset.md`

**Purpose:** Provide a **structured, reproducible template** for documenting datasets  
in the Kansas Frontier Matrix (KFM) — ensuring that every dataset’s provenance, metadata,  
and processing history are transparent, versioned, and STAC-compliant.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 🧭 Dataset Metadata

| Field | Description |
|:------|:-------------|
| **Dataset ID** | Unique identifier (e.g., `DATASET-2025-001-TERRAIN-DEM`) |
| **Title** | Full descriptive dataset name |
| **Author(s) / Curator(s)** | Person(s) or team responsible |
| **Date Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Version** | v1.0, v1.1, etc. |
| **Domain** | Terrain / Hydrology / Climate / Landcover / Hazards / Tabular / Text |
| **Data Type** | Raster / Vector / Tabular / Text / Mixed |
| **License** | CC-BY 4.0 / MIT / Public Domain (as applicable) |
| **Source Manifests** | Path(s) in `data/sources/` |
| **Checksum Manifest** | Path(s) in `data/checksums/` |
| **STAC Metadata** | Path in `data/stac/` |

---

## 🧩 Abstract / Description

Provide a clear summary of what this dataset represents and how it fits into the KFM ecosystem.

> Example:  
> *This dataset contains a 1-meter resolution Digital Elevation Model (DEM) derived from USGS 3DEP LiDAR data for Kansas (2018–2020).  
> It serves as the foundational layer for hydrology, hazards, and landcover analysis.*

---

## 🌐 Data Provenance

Detail the origin, licensing, and acquisition process for this dataset.

| Source | Provider | Access Method | License | URL / API |
|:-----------|:------------|:----------------|:------------|:------------|
| **USGS 3DEP DEM** | USGS | REST API | Public Domain | [https://elevation.nationalmap.gov](https://elevation.nationalmap.gov) |
| **KS DASC LiDAR** | Kansas DASC | FTP | CC-BY 4.0 | [https://www.kansasgis.org/](https://www.kansasgis.org/) |

> All sources must correspond to an entry in `data/sources/<domain>/`.

---

## ⚙️ Data Processing Workflow

Summarize how this dataset was processed or transformed.

| Step | Description | Tool / Script | Output |
|:------|:-------------|:----------------|:----------|
| **1. Ingest** | Downloaded and archived raw data | `make fetch-raw` | `data/raw/terrain/` |
| **2. Reproject** | Converted to EPSG:4326 | `GDAL warp` | GeoTIFF |
| **3. Merge Tiles** | Mosaic 3DEP tiles | `gdal_merge.py` | `ks_1m_dem_2018_2020.tif` |
| **4. Derivatives** | Generated slope, aspect, hillshade | `terrain_pipeline.py` | `data/processed/terrain/` |
| **5. Metadata** | Generated STAC Items | `stac-generator.py` | `data/stac/terrain/ks_1m_dem_2018_2020.json` |

---

## 🧮 Data Specifications

| Attribute | Description | Value / Example |
|:-------------|:-------------|:----------------|
| **Spatial Resolution** | Ground sample distance | 1 m |
| **Projection (CRS)** | Coordinate Reference System | EPSG:4326 (WGS84) |
| **Spatial Extent (BBox)** | Geographic bounds | [-102.05, 36.99, -94.59, 40.00] |
| **Temporal Coverage** | Start / End dates | 2018–2020 |
| **File Format(s)** | Data file types | GeoTIFF (COG), PNG (thumbnail), JSON (metadata) |
| **File Size** | Total storage size | ~12 GB |
| **Number of Layers / Records** | Count | 1 raster layer |
| **Checksum** | SHA-256 | `4a2f7f3e94a1f12c...` |

---

## 🧾 Outputs & Products

| Output Type | File(s) | Description |
|:--------------|:-----------|:-------------|
| **Primary Dataset** | `data/processed/terrain/ks_1m_dem_2018_2020.tif` | Core processed raster output |
| **Derived Layers** | `hillshade`, `slope`, `aspect` | Visualization and terrain analysis derivatives |
| **Metadata** | `data/stac/terrain/ks_1m_dem_2018_2020.json` | STAC 1.0.0 metadata item |
| **Checksums** | `data/checksums/terrain/ks_1m_dem_2018_2020.tif.sha256` | Integrity verification file |
| **Thumbnail** | `data/processed/metadata/terrain/thumbnails/ks_1m_dem_2018_2020.png` | Preview image for web display |

---

## 🧠 Data Validation

Outline the validation procedures used to ensure dataset accuracy and integrity.

| Validation Step | Description | Method / Tool | Result |
|:------------------|:-------------|:----------------|:----------|
| **Checksum Validation** | Compare computed SHA-256 to manifest | `make checksums` | ✅ Passed |
| **STAC Validation** | Validate STAC JSON using schema | `stac-validator` | ✅ Passed |
| **Spatial QA/QC** | Verify projection and coverage alignment | `GDALinfo` | ✅ Passed |
| **CI/CD Verification** | Automated check via GitHub Actions | `.github/workflows/stac-validate.yml` | ✅ Passed |

> All validation logs must be stored in `data/work/logs/<domain>/<dataset>_validation.log`.

---

## 🧩 Relationships & Dependencies

| Relationship | Related Dataset | Type | Path |
|:---------------|:----------------|:--------|:-----------|
| **Derived From** | `usgs_3dep_dem` | Source | `data/sources/terrain/usgs_3dep_dem.json` |
| **Feeds** | `watersheds_huc12_2019` | Dependent | `data/processed/hydrology/watersheds_huc12_2019.geojson` |
| **Referenced In** | `ks_hillshade_2018_2020` | Derived | `data/processed/terrain/ks_hillshade_2018_2020.tif` |

---

## 🔐 Ethical, Legal & Licensing Notes

- Data is **open access** and licensed under **CC-BY 4.0**.  
- Attribution required for derivative works.  
- No personal or sensitive data present.  
- Usage must comply with **USGS and DASC data distribution policies**.  
- Derivative works must include **citation and acknowledgment** of original sources.

---

## 🧩 Integration with KFM Systems

| Component | Role | Integration |
|:------------|:------|:--------------|
| **Pipelines** | Generates processed datasets | `src/pipelines/terrain_pipeline.py` |
| **Metadata** | STAC linkage for catalog browsing | `data/stac/terrain/` |
| **CI/CD Validation** | Automatic schema and checksum validation | `.github/workflows/stac-validate.yml` |
| **Web Viewer** | Visualization via MapLibre layer | `web/config/layers.json` |
| **Knowledge Graph** | Links to entities and provenance graph | `docs/architecture/knowledge-graph.md` |

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
|:--------------|:----------------|
| **Documentation-first** | Dataset documented before publication. |
| **Reproducibility** | ETL process and checksums guarantee identical rebuilds. |
| **Open Standards** | Data and metadata adhere to STAC 1.0.0, GeoTIFF, and JSON Schema. |
| **Provenance** | All lineage recorded through manifest, STAC, and checksum. |
| **Auditability** | Validation logs and CI/CD checks ensure integrity. |

---

## 📎 Related Documentation

| File | Description |
|:------|:-------------|
| `docs/architecture/data-architecture.md` | Describes how datasets integrate into KFM architecture. |
| `docs/templates/experiment.md` | Template for experiments analyzing this dataset. |
| `docs/templates/sop.md` | SOPs governing processing and validation. |
| `data/ARCHITECTURE.md` | Technical description of dataset directory structure. |
| `.github/workflows/stac-validate.yml` | Workflow validating this dataset in CI/CD. |

---

## 📅 Version History

| Version | Date | Author | Summary |
|:---------|:------|:----------|:----------|
| v1.0 | 2025-10-04 | KFM Data Governance Team | Initial dataset template for MCP-compliant documentation. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Dataset Documented. Every Record Reproducible.”*  
📍 [`docs/templates/dataset.md`](.) · Template for standardized dataset documentation under MCP and STAC compliance.

</div>
