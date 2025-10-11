<div align="center">

# 🏔️ Kansas Frontier Matrix — Terrain Derivative Metadata  
`data/derivatives/terrain/metadata/`

**Purpose:** Define machine-readable metadata describing **terrain derivative layers**  
(DEMs, hillshades, slope maps, contours) created through the Kansas Frontier Matrix (KFM) ETL pipeline.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/Pre--Commit-enabled-success)](../../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Metadata Generation Flow](#metadata-generation-flow)
- [Directory Layout](#directory-layout)
- [Metadata JSON Example](#metadata-json-example)
- [JSON Schema (KFM Terrain Metadata)](#json-schema-kfm-terrain-metadata)
- [Best Practices](#best-practices)
- [Pipeline Usage](#pipeline-usage)
- [Validation & Reproducibility](#validation--reproducibility)
- [Relationships to Other Layers](#relationships-to-other-layers)
- [Changelog](#changelog)

---

## 🗺️ Overview

This directory contains **metadata JSON files** describing each processed terrain derivative product  
within the Kansas Frontier Matrix (KFM). These metadata files link derived raster and vector terrain layers  
to their **source datasets**, **checksum manifests**, and **STAC catalog items**, ensuring reproducibility,  
discoverability, and clear provenance.

Terrain derivatives include:
- **DEMs** (Digital Elevation Models)
- **Hillshade rasters**
- **Slope and aspect maps**
- **Contour line GeoJSONs**

Each metadata file conforms to KFM’s MCP-aligned schema and **STAC/DCAT** standards for interoperability.

---

## 🧭 Metadata Generation Flow

```mermaid
flowchart TD
  A["Terrain Sources\nUSGS 3DEP · LiDAR · DASC Archive"] --> B["ETL Pipeline\nProcess · Mosaic · Reproject"]
  B --> C["Terrain Derivatives\nDEM · Hillshade · Slope · Contours"]
  C --> D["Metadata JSONs\nvariables · CRS · temporal range · provenance"]
  D --> E["Checksums\nSHA-256 manifests"]
  D --> F["STAC Items\nassets · links · licenses"]
  F --> G["Knowledge Graph\nentities · provenance edges"]
  G --> H["Web UI\nMapLibre layers · timeline sync"]
````

<!-- END OF MERMAID -->

---

## 🗂️ Directory Layout

```bash
data/derivatives/terrain/metadata/
├── dem_1m_ks_lidar.json
├── hillshade_ks_1m.json
├── slope_map_ks.json
├── contour_ks_10m.json
└── README.md
```

> Each `.json` documents one terrain product: **lineage**, **CRS/bounds**, **temporal extent**, **checksum**, and **STAC link**.

---

## 🧾 Metadata JSON Example

```json
{
  "id": "dem_1m_ks_lidar",
  "title": "Kansas 1 m LiDAR Digital Elevation Model (USGS 3DEP)",
  "description": "High-resolution DEM of Kansas derived from USGS 3DEP LiDAR tiles; mosaicked and reprojected to WGS84.",
  "type": "raster",
  "format": "COG",
  "file": "../dem_1m_ks_cog.tif",
  "checksum": "../checksums/dem_1m_ks_cog.tif.sha256",
  "source": "../../../sources/usgs_3dep_dem.json",
  "stac_item": "../../../stac/items/dem_1m_ks_lidar.json",
  "spatial": {
    "crs": "EPSG:4326",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "temporal": {
    "start": "2018-01-01",
    "end": "2023-12-31"
  },
  "variables": [
    {
      "name": "elevation",
      "units": "m",
      "description": "Elevation above mean sea level (NAVD88)."
    }
  ],
  "license": "Public Domain (USGS)",
  "created": "2025-10-10",
  "last_updated": "2025-10-11",
  "mcp_stage": "derivatives",
  "derived_from": ["data/cogs/dem_1m_ks.tif"],
  "processing": {
    "software": "GDAL 3.8.0",
    "parameters": {
      "mosaic": true,
      "resampling": "bilinear"
    }
  }
}
```

> 💡 **Tip:** After any reprojection or re-tiling, update `spatial.crs`, `spatial.bbox`, and the **checksum** path.

---

## 📐 JSON Schema (KFM Terrain Metadata)

> Use this to validate each metadata file locally and in CI.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kfm.local/schemas/terrain_metadata.schema.json",
  "title": "KFM Terrain Derivative Metadata",
  "type": "object",
  "required": ["id","title","description","type","file","checksum","source","stac_item","spatial","license","created","mcp_stage"],
  "properties": {
    "id": {"type":"string", "pattern":"^[a-z0-9_\\-]+$"},
    "title": {"type":"string"},
    "description": {"type":"string"},
    "type": {"type":"string", "enum":["raster","vector"]},
    "format": {"type":"string"},
    "file": {"type":"string"},
    "checksum": {"type":"string"},
    "source": {"type":"string"},
    "stac_item": {"type":"string"},
    "derived_from": {"type":"array","items":{"type":"string"}},
    "spatial": {
      "type":"object",
      "required":["crs","bbox"],
      "properties":{
        "crs":{"type":"string", "pattern":"^EPSG:[0-9]+$"},
        "bbox":{
          "type":"array",
          "minItems":4,
          "maxItems":4,
          "items":{"type":"number"}
        }
      }
    },
    "temporal": {
      "type":"object",
      "properties":{
        "start":{"type":"string","format":"date"},
        "end":{"type":"string","format":"date"}
      }
    },
    "variables": {
      "type":"array",
      "items":{
        "type":"object",
        "required":["name"],
        "properties":{
          "name":{"type":"string"},
          "units":{"type":"string"},
          "description":{"type":"string"}
        }
      }
    },
    "processing": {
      "type":"object",
      "properties":{
        "software":{"type":"string"},
        "parameters":{"type":"object"}
      }
    },
    "license":{"type":"string"},
    "created":{"type":"string","format":"date"},
    "last_updated":{"type":"string","format":"date"},
    "mcp_stage":{"type":"string","enum":["sources","raw","processed","derivatives","stac"]}
  },
  "additionalProperties": false
}
```

---

## ✅ Best Practices

| Category              | Guideline                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------- |
| **Completeness**      | Every derivative file **must** ship with a matching `.json` metadata file.                |
| **Linkage**           | Always include `checksum`, `stac_item`, and `source` paths that resolve from this folder. |
| **Timestamps**        | Record both `created` and `last_updated` in ISO 8601.                                     |
| **Spatial Integrity** | Keep `crs` and `bbox` accurate after reprojections; update when bounds change.            |
| **Licensing**         | Reflect data source license (Public Domain, CC-BY, etc.) exactly.                         |
| **Naming**            | Prefer `terrain_<product>_<resolution>_<region>` for IDs/files.                           |
| **Minify for Prod**   | Store pretty JSON in Git; CI may emit minified copies alongside STAC items.               |

---

## 🧠 Pipeline Usage

* **ETL Step:** Each produced raster/vector triggers generation of a corresponding metadata JSON.
* **Graph Load:** These JSONs populate Neo4j nodes (e.g., `:TerrainLayer`) and provenance relationships.
* **STAC Reference:** `stac_item` points to `data/stac/items/*.json` for catalog discovery.
* **Web UI:** Layers are discoverable by `id` and styled via associated config (MapLibre).

---

## 🔁 Validation & Reproducibility

| Check             | Command / Mechanism                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------ |
| **JSON Schema**   | `make validate-terrain-metadata` (runs `ajv` or `python -m jsonschema` against the schema above) |
| **STAC Validate** | `make stac-validate` (CI also runs `.github/workflows/stac-validate.yml`)                        |
| **Checksums**     | `sha256sum -c ../checksums/<file>.sha256`                                                        |
| **Pre-Commit**    | JSON lint/format hooks ensure stable diffs and consistent formatting                             |
| **Containerized** | All validation/build steps runnable in the GDAL/ETL Docker image                                 |

> Minimal `Makefile` targets you can adopt:

```make
validate-terrain-metadata:
\tjsonschema -i data/derivatives/terrain/metadata/*.json schemas/terrain_metadata.schema.json

stac-validate:
\tstac-validator data/stac/items/*.json
```

---

## 🧩 Relationships to Other Layers

| Layer                           | Path                                  | Purpose                                   |
| ------------------------------- | ------------------------------------- | ----------------------------------------- |
| 🏔️ **Terrain Metadata (This)** | `data/derivatives/terrain/metadata/`  | Documents ETL-produced terrain layers     |
| 🧾 **Checksums**                | `data/derivatives/terrain/checksums/` | Ensures binary integrity of terrain files |
| 🗺️ **STAC Catalog**            | `data/stac/`                          | Registers geospatial & temporal metadata  |
| 🧠 **Knowledge Graph**          | `neo4j/` (external)                   | Links datasets with provenance & usage    |
| ⚙️ **ETL Pipeline**             | `Makefile`, `tools/terrain/`          | Processing, mosaicking, transformations   |

---

## 🗓 Changelog

| Version    | Date       | Notes                                                                                                       |
| ---------- | ---------- | ----------------------------------------------------------------------------------------------------------- |
| **v1.1.0** | 2025-10-11 | Added YAML frontmatter, JSON Schema, corrected relative links, and CI/make targets; hardened Mermaid block. |
| **v0.1.0** | 2025-10-10 | Initial creation of terrain metadata schema and examples.                                                   |

```
```
