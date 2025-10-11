<div align="center">

# 🗂️ Kansas Frontier Matrix — Data Directory  
`/data/`

**Mission:** Organize, document, and preserve all **datasets, metadata, and provenance records**  
that power the Kansas Frontier Matrix (KFM) — integrating Kansas’s geography, climate, hydrology,  
land use, and history into a unified, reproducible open-data ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

## 📚 Overview

The `/data/` directory is the **core of the Kansas Frontier Matrix project**, housing all  
datasets, derivative layers, and metadata required to reconstruct, verify, and explore Kansas’s  
scientific and historical record through time and space.

All content here adheres to the **Master Coder Protocol (MCP)** for reproducibility  
and the **SpatioTemporal Asset Catalog (STAC 1.0)** specification for discoverability.

---

## 🗂️ Directory Structure

```bash
data/
├── raw/                    # Original source data (immutable snapshots)
├── processed/              # Cleaned, standardized, and derived datasets
│   ├── terrain/            # Elevation, hillshade, slope/aspect, DEM rasters
│   ├── hydrology/          # Rivers, watersheds, aquifers, floods
│   ├── landcover/          # Vegetation, NLCD, crop maps, change layers
│   ├── climate/            # Temperature, precipitation, drought indices
│   ├── hazards/            # Tornadoes, floods, wildfires, drought events
│   ├── tabular/            # Census, agriculture, economy, statistics
│   └── text/               # Newspapers, oral histories, treaties, OCR text
│
├── sources/                # JSON manifests describing raw data endpoints
├── stac/                   # STAC 1.0 catalog and items for spatial assets
└── checksums/              # Project-wide checksum manifests (data integrity)
````

> **Tip:** Each subdirectory includes a local `README.md` (MCP format) with schema notes, ETL steps, and STAC examples.

---

## 🧩 Data Model & Provenance Chain

| Stage            | Directory                      | Purpose                                                                     |
| :--------------- | :----------------------------- | :-------------------------------------------------------------------------- |
| **Source**       | `data/sources/`                | Defines origin, license, and retrieval method for each dataset.             |
| **Raw**          | `data/raw/`                    | Immutable snapshots of downloaded or ingested source data.                  |
| **Processed**    | `data/processed/`              | Cleaned, transformed, or derived datasets ready for analysis/visualization. |
| **Metadata**     | `data/processed/**/metadata/`  | STAC/schema metadata describing processed outputs (thumbnails, JSON, etc.). |
| **Checksums**    | `data/processed/**/checksums/` | SHA-256 hashes verifying data integrity and reproducibility.                |
| **STAC Catalog** | `data/stac/`                   | Global catalog of all spatiotemporal assets for indexing and discovery.     |

---

## 🧮 Standards & File Formats

| Category     | Primary Formats      | Standards                               |
| :----------- | :------------------- | :-------------------------------------- |
| Raster Data  | `.tif` (COG), `.vrt` | Cloud-Optimized GeoTIFF (COG), STAC 1.0 |
| Vector Data  | `.geojson`, `.shp`   | GeoJSON, OGC Simple Features            |
| Tabular Data | `.csv`, `.parquet`   | CSVW, Apache Parquet                    |
| Text Data    | `.jsonl`, `.txt`     | JSON Lines, UTF-8 Plain Text            |
| Metadata     | `.json`, `.yaml`     | STAC, JSON Schema, MCP Templates        |
| Checksums    | `.sha256`            | SHA-256 (FIPS 180-4)                    |

---

## ⚙️ Data Processing Workflow

1. **Ingest →** Fetch raw datasets via API, FTP, or local archives (`data/sources/`).
2. **Transform →** Standardize CRS, normalize attributes, and clean/format to open standards.
3. **Derive →** Generate new layers (e.g., hillshade, slope, hydrologic boundaries).
4. **Validate →** Run schema and checksum validation via CI/CD.
5. **Catalog →** Register each dataset in STAC (`data/stac/`).
6. **Visualize →** Produce thumbnails and previews for the web UI.

**Automation:** Fully reproducible via Make (e.g., `make terrain`, `make stac`, `make site`)
with continuous validation in GitHub Actions.

---

## 🧰 Example — STAC Metadata Reference

Each dataset is represented by a STAC Item describing its content, source, and spatial extent.

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018_2020",
  "properties": {
    "title": "Kansas LiDAR Digital Elevation Model (1 m, 2018–2020)",
    "datetime": "2020-01-01T00:00:00Z",
    "license": "Public Domain (USGS 3DEP)",
    "themes": ["terrain", "elevation"],
    "providers": [
      { "name": "USGS 3DEP", "roles": ["producer"] },
      { "name": "Kansas DASC", "roles": ["processor"] }
    ]
  },
  "assets": {
    "data": {
      "href": "../processed/terrain/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "../processed/terrain/metadata/thumbnails/ks_1m_dem_2018_2020.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

> **Note:** When Items live under `data/stac/`, asset `href` values are typically **relative**
> (e.g., `../processed/...`) for portability and cross-environment compatibility.

---

## 🧪 Make Targets (Data-Focused)

```bash
# Fetch sources declared in data/sources/*.json → data/raw/
make fetch

# Convert rasters → COG · vectors → GeoJSON (EPSG:4326) · build derivatives → data/processed/
make cogs vectors

# Build and validate STAC catalog → data/stac/
make stac

# Generate or verify SHA-256 sidecars under data/processed/**/checksums/
make checksums
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                          |
| :---------------------- | :---------------------------------------------------------------------- |
| **Documentation-first** | Each folder includes README + STAC examples and schema references.      |
| **Reproducibility**     | ETL logs + checksums + Make automation preserve data lineage.           |
| **Open Standards**      | GeoTIFF (COG), GeoJSON, Parquet, STAC, JSON Schema used consistently.   |
| **Provenance**          | Source, processing, and output metadata tracked end-to-end.             |
| **Auditability**        | CI validates schemas, checksums, and catalog integrity on every commit. |

---

## 📎 References & Standards

* [SpatioTemporal Asset Catalog (STAC) 1.0.0](https://stacspec.org)
* [Master Coder Protocol (MCP)](../docs/templates/)
* [Cloud-Optimized GeoTIFF (COG)](https://www.cogeo.org/)
* [GeoJSON (RFC 7946)](https://datatracker.ietf.org/doc/html/rfc7946)
* [Apache Parquet](https://parquet.apache.org/)
* [USGS 3DEP LiDAR Program](https://www.usgs.gov/3dep)
* [Kansas Data Access & Support Center (DASC)](https://www.kansasgis.org/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Building the Foundation of Time, Terrain, and Knowledge.”*
📍 [`/data/`](.) · Central hub for all datasets, metadata, and provenance assets.

</div>
