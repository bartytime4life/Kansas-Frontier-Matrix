<div align="center">

# 🗂️ Kansas Frontier Matrix — Data Format Standards  
`docs/standards/data-formats.md`

**Purpose:** Define approved and required **data, metadata, and file formats**  
used throughout the **Kansas Frontier Matrix (KFM)** system — ensuring all datasets,  
models, and derived products are reproducible, interoperable, and open-standard compliant.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 📚 Overview

All data managed within the Kansas Frontier Matrix follows **open, non-proprietary formats** that  
can be reproduced, validated, and accessed using free or open-source tools.  

This document defines:
- 📦 Approved **file formats** for each data domain (spatial, tabular, textual).  
- 🧾 Associated **metadata formats** and **validation rules**.  
- 🔐 Guidelines for **naming, encoding, and compression**.  
- 🧠 Integration requirements with **STAC 1.0.0** and **JSON Schema**.

> All formats listed here must align with **MCP Principles:**  
> Documentation-first · Reproducible · Open-standard · Provenance-tracked · Auditable.

---

## 🧩 Approved File Formats by Data Domain

| Domain | Data Type | Approved Formats | Description |
|:---------|:------------|:----------------|:--------------|
| **Terrain** | Raster (Elevation, Slope, Hillshade) | `.tif` (COG, GeoTIFF), `.png` (preview) | Primary elevation and surface raster datasets. |
| **Hydrology** | Vector (Rivers, Basins) | `.geojson`, `.gpkg` | Streams, flowlines, and watershed polygons. |
| **Landcover** | Raster (Classification, NDVI) | `.tif` (COG), `.png` | Landcover and vegetation index datasets. |
| **Climate** | Raster / NetCDF | `.tif`, `.nc`, `.csv` | Temperature, precipitation, drought indices. |
| **Hazards** | Vector / Raster | `.geojson`, `.tif`, `.csv` | Tornado, wildfire, flood, and drought datasets. |
| **Tabular** | Structured Data | `.csv`, `.parquet` | Census, economics, agriculture, and statistics. |
| **Text** | Unstructured Data | `.jsonl`, `.txt`, `.csv` | OCR, transcripts, and natural language corpora. |
| **Metadata** | Metadata & Catalogs | `.json` (STAC, JSON Schema) | Metadata for datasets and collections. |

---

## 🧾 Spatial Data Standards

### Raster Data (Terrain, Climate, Landcover)
| Property | Standard | Requirement |
|:-----------|:------------|:--------------|
| **Format** | GeoTIFF (Cloud-Optimized) | Must be tiled and internally compressed (`DEFLATE`). |
| **Projection** | EPSG:4326 (WGS84) | Default CRS unless domain-specific EPSG defined. |
| **Compression** | LZW or DEFLATE | Lossless only. |
| **Bit Depth** | 32-bit float | For continuous data (DEM, temperature). |
| **Tile Size** | 512x512 | For COG compatibility. |
| **Metadata** | Embedded + STAC JSON | Includes extent, CRS, checksum, and attribution. |

### Vector Data (Hydrology, Hazards)
| Property | Standard | Requirement |
|:-----------|:------------|:--------------|
| **Format** | GeoJSON (RFC 7946) | Default. |
| **Alternate** | GPKG (GeoPackage v1.3) | For multi-layer storage. |
| **Encoding** | UTF-8 | All attributes and geometry names. |
| **Projection** | EPSG:4326 | Consistent CRS across all vector data. |
| **Attributes** | Schema-aligned | Follow attribute conventions defined in domain metadata. |

---

## 🧮 Tabular Data Standards

| Attribute | Requirement | Notes |
|:------------|:---------------|:--------------|
| **Format** | `.csv` or `.parquet` | Use Parquet for large-scale data. |
| **Encoding** | UTF-8 | Required for all text-based files. |
| **Delimiter** | Comma (`,`) | No spaces or tabs. |
| **Header Row** | Mandatory | Contains attribute names. |
| **Missing Values** | `NULL` or empty string | No special placeholders. |
| **Units** | Must be specified in metadata | Use SI units where possible. |
| **Schema Validation** | Required | Validated using JSON Schema. |

Example CSV snippet:
```csv
year,county,population,median_income
2020,Douglas,118716,59000
2010,Douglas,110826,48500
````

---

## 🧠 Text Data Standards

| Property              | Standard                               | Requirement                            |
| :-------------------- | :------------------------------------- | :------------------------------------- |
| **Format**            | `.jsonl` (JSON Lines)                  | Each line = one document record.       |
| **Encoding**          | UTF-8                                  | Required.                              |
| **Fields**            | `id`, `source`, `text`, `date`, `tags` | Minimum set.                           |
| **Language Metadata** | ISO 639-1 code                         | e.g., `en`, `es`.                      |
| **Attribution**       | Required                               | Source or collection name in metadata. |

Example JSONL record:

```json
{"id": "ks_news_1898_001", "source": "Topeka Daily Capital", "date": "1898-07-14", "text": "Kansas River floodwaters rising rapidly."}
```

---

## 🧾 Metadata & Catalog Standards

| Metadata Type           | Format                 | Description                                 |
| :---------------------- | :--------------------- | :------------------------------------------ |
| **Dataset Metadata**    | STAC Item (JSON)       | Describes one dataset.                      |
| **Collection Metadata** | STAC Collection (JSON) | Groups related datasets by domain or theme. |
| **Checksum Record**     | SHA-256 text file      | Confirms integrity and reproducibility.     |
| **Schema Definition**   | JSON Schema            | Validates metadata structure.               |

**STAC Example:**
`data/stac/terrain/ks_1m_dem_2018_2020.json`

```json
{
  "stac_version": "1.0.0",
  "id": "ks_1m_dem_2018_2020",
  "type": "Feature",
  "properties": {
    "datetime": "2020-01-01T00:00:00Z",
    "license": "Public Domain",
    "description": "Kansas 1-meter DEM derived from USGS 3DEP LiDAR (2018–2020)"
  },
  "assets": {
    "data": {
      "href": "data/processed/terrain/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

---

## 🔐 Checksum & Integrity Files

| File Type    | Format    | Description                                                  |
| :----------- | :-------- | :----------------------------------------------------------- |
| **Checksum** | `.sha256` | Cryptographic signature verifying dataset integrity.         |
| **Manifest** | `.json`   | Collection of checksum entries for all datasets in a domain. |

Example `.sha256` file:

```text
4a2f7f3e94a1f12c7bde9b6d8120ee9876ab2b74d7c63c5c0a1a86b8a23de98a  ks_1m_dem_2018_2020.tif
```

---

## 🧩 Naming Conventions

| Element           | Format                                | Example                          |
| :---------------- | :------------------------------------ | :------------------------------- |
| **Dataset File**  | `<region>_<topic>_<year-range>.<ext>` | `ks_1m_dem_2018_2020.tif`        |
| **Metadata File** | `<dataset>.json`                      | `ks_1m_dem_2018_2020.json`       |
| **Checksum File** | `<dataset>.<ext>.sha256`              | `ks_1m_dem_2018_2020.tif.sha256` |
| **Thumbnail**     | `<dataset>.png`                       | `ks_1m_dem_2018_2020.png`        |
| **Logs**          | `<domain>_etl_debug.log`              | `terrain_etl_debug.log`          |

All filenames must:

* Be lowercase.
* Use underscores (`_`) instead of spaces.
* Exclude special characters or diacritics.

---

## 🧰 Compression & Packaging Standards

| Purpose                  | Recommended Format           | Tool                          |
| :----------------------- | :--------------------------- | :---------------------------- |
| **Archive Delivery**     | `.zip`                       | `zip`, `7zip`, or `tar`       |
| **Internal Compression** | DEFLATE / LZW                | Embedded in GeoTIFF or NetCDF |
| **Avoided Formats**      | `.rar`, `.7z` (non-standard) | —                             |

> All archives must maintain relative paths and preserve metadata folder structure.

---

## 🧾 Validation Requirements

| Validation Type            | Tool / Workflow                       | Applies To               |
| :------------------------- | :------------------------------------ | :----------------------- |
| **Checksum Verification**  | `make checksums`                      | All datasets             |
| **STAC Schema Validation** | `stac-validator`                      | Metadata (`.json`)       |
| **JSON Schema Validation** | `jsonschema`                          | Metadata & configuration |
| **Projection Validation**  | `gdalinfo`                            | Raster & vector datasets |
| **CI/CD Automation**       | `.github/workflows/stac-validate.yml` | Continuous verification  |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                      |
| :---------------------- | :------------------------------------------------------------------ |
| **Documentation-first** | Format standards documented for every domain before implementation. |
| **Reproducibility**     | Deterministic data formats ensure identical rebuilds.               |
| **Open Standards**      | All formats open, non-proprietary, and tool-agnostic.               |
| **Provenance**          | Every file links to source manifests, STAC items, and checksums.    |
| **Auditability**        | CI/CD workflows enforce validation and format compliance.           |

---

## 📎 Related Documentation

| Path                                     | Description                                           |
| :--------------------------------------- | :---------------------------------------------------- |
| `docs/standards/metadata-standards.md`   | Defines field-level metadata and schema conventions.  |
| `docs/architecture/data-architecture.md` | Describes data lifecycle and storage hierarchy.       |
| `docs/standards/naming-conventions.md`   | Establishes project-wide naming and versioning rules. |
| `.github/workflows/stac-validate.yml`    | CI/CD validation workflow enforcing standards.        |

---

## 📅 Version History

| Version | Date       | Author                   | Summary                                                       |
| :------ | :--------- | :----------------------- | :------------------------------------------------------------ |
| v1.0    | 2025-10-04 | KFM Data Governance Team | Initial documentation for approved data and metadata formats. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every File Open. Every Format Reproducible.”*
📍 [`docs/standards/data-formats.md`](.) · Official guide to data and metadata format standards under MCP compliance.

</div>
