<div align="center">

# 🗂️ Kansas Frontier Matrix — **Data Directory**  
`/data/`

**Mission:** Organize, document, and preserve all **datasets, metadata, and provenance records**  
that power the Kansas Frontier Matrix (KFM) — integrating Kansas’s geography, climate, hydrology,  
land use, and history into a unified, reproducible open-data ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

```yaml
---
title: "KFM • Data Directory (/data/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-architecture"]
tags: ["data","etl","provenance","stac","cog","geojson","parquet","mcp"]
license: "CC-BY 4.0"
semantic_alignment:
  - STAC 1.0.0
  - GeoJSON (RFC 7946)
  - Cloud-Optimized GeoTIFF (COG)
  - CSVW / Apache Parquet
  - MCP-DL v6.2 (Reproducibility & Provenance)
---
```

---

## 📚 Overview

The `/data/` directory is the **core of KFM**, housing all datasets, derivative layers, and metadata needed to reconstruct, verify, and explore Kansas’s scientific and historical record across **time** and **space**.

All content complies with **MCP-DL v6.2** for reproducibility and **STAC 1.0** for discoverability.

> *“Data without provenance is folklore. Data with lineage is knowledge.”*

---

## 🗂️ Directory Structure

```bash
data/
├── raw/                       # Original source data (immutable snapshots)
├── processed/                 # Cleaned, standardized, and derived datasets
│   ├── terrain/               # Elevation, hillshade, slope/aspect, DEM rasters
│   ├── hydrology/             # Rivers, watersheds, aquifers, floods
│   ├── landcover/             # Vegetation, NLCD, crop maps, change layers
│   ├── climate/               # Temperature, precipitation, drought indices
│   ├── hazards/               # Tornadoes, floods, wildfires, drought events
│   ├── tabular/               # Census, agriculture, economy, statistics
│   └── text/                  # Newspapers, oral histories, treaties, OCR text
│
├── sources/                   # JSON manifests describing raw data endpoints
├── stac/                      # STAC 1.0 catalog and items for spatial assets
└── checksums/                 # Project-wide checksum manifests (data integrity)
```

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

| Category     | Primary Formats            | Standards / Notes                                 |
| :----------- | :------------------------- | :------------------------------------------------ |
| Raster Data  | `.tif` (COG), `.vrt`       | Cloud-Optimized GeoTIFF, internal overviews       |
| Vector Data  | `.geojson`, `.parquet`, `.shp` | GeoJSON (RFC 7946), OGC Simple Features, Parquet |
| Tabular Data | `.csv`, `.parquet`         | CSVW metadata, column types & units documented    |
| Text Data    | `.jsonl`, `.txt`           | JSON Lines UTF-8, page/line refs for OCR          |
| Metadata     | `.json`, `.yaml`           | STAC 1.0, JSON Schema, MCP templates              |
| Checksums    | `.sha256`                  | SHA-256 (FIPS 180-4), recorded per artifact       |

---

## ⚙️ Processing Workflow (ETL)

1. **Ingest →** Fetch raw datasets via API/FTP/archive (`data/sources/*.json`).
2. **Transform →** Standardize CRS (`EPSG:4326`), normalize fields, tidy schemas.
3. **Derive →** Generate products (hillshade, slope, hydrologic boundaries, joins).
4. **Validate →** Schema & checksum validation (CI: `stac-validate.yml`, `ci.yml`).
5. **Catalog →** Register each dataset in STAC (`data/stac/`) with relative `href`s.
6. **Visualize →** Produce thumbnails/previews for the web UI.

**Automation:** Reproducible via Make targets (`make fetch`, `make cogs`, `make vectors`, `make stac`, `make checksums`) and GitHub Actions.

---

## 🧰 Example — STAC Item (Processed Raster)

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

> **Note:** Assets use **relative `href`** (e.g., `../processed/...`) for portability across machines and CI runners.

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

## 🧱 Naming, Layout & Retention

| Policy Area        | Rule / Convention                                                                 |
| :----------------- | :--------------------------------------------------------------------------------- |
| **Filenames**      | lowercase, hyphens, no spaces: `domain_topic_year.ext`                            |
| **CRS**            | All vectors/rasters in `EPSG:4326` (unless explicitly documented otherwise).       |
| **Derivatives**    | Place next to source under `processed/<domain>/` with `metadata/` & `checksums/`. |
| **Retention**      | `raw/` is immutable; re-ingest rather than overwrite.                             |
| **Large Files**    | Prefer regeneration or track via Git LFS/DVC pointers (no binaries in Git).       |

---

## 🔐 Integrity & Provenance

| Artifact / Log              | Location                                 | Description                                              |
| :-------------------------- | :---------------------------------------- | :------------------------------------------------------- |
| **Checksums (SHA-256)**     | `data/processed/**/checksums/*.sha256`    | Per-file integrity sidecars (deterministic build output) |
| **Provenance Log**          | `logs/provenance.log`                     | `[timestamp user action target status commit]`           |
| **ETL Run Manifests**       | `data/processed/**/metadata/run-*.json`   | Parameters, versions, env hash                           |
| **STAC Validation Reports** | `data/stac/validation/*.json`             | CI validation summaries                                  |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                          |
| :---------------------- | :---------------------------------------------------------------------- |
| **Documentation-first** | Folder READMEs + STAC examples + schema links.                          |
| **Reproducibility**     | Make automation + checksums + pinned environments.                      |
| **Open Standards**      | COG, GeoJSON, Parquet, STAC, JSON Schema used consistently.             |
| **Provenance**          | End-to-end lineage via logs, manifests, and STAC metadata.              |
| **Auditability**        | CI validates schemas, checksums, and STAC integrity on every commit.    |

---

## 📎 References & Standards

* [SpatioTemporal Asset Catalog (STAC) 1.0.0](https://stacspec.org)
* [Cloud-Optimized GeoTIFF (COG)](https://www.cogeo.org/)
* [GeoJSON (RFC 7946)](https://datatracker.ietf.org/doc/html/rfc7946)
* [Apache Parquet](https://parquet.apache.org/)
* [MCP-DL v6.2 Templates](../docs/templates/)
* [USGS 3DEP LiDAR Program](https://www.usgs.gov/3dep)
* [Kansas Data Access & Support Center (DASC)](https://www.kansasgis.org/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Building the Foundation of Time, Terrain, and Knowledge.”*  
📍 [`/data/`](.) · Central hub for all datasets, metadata, and provenance assets.

</div>