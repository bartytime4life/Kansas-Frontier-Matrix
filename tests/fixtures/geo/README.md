<div align="center">

# 🌍 Kansas Frontier Matrix — **Geo Fixtures**  
`tests/fixtures/geo/`

**GeoJSON · Rasters · Spatial Micro-Samples**

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../../.github/workflows/tests.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Geo Fixtures (tests/fixtures/geo/)"
version: "v1.0.0"
last_updated: "2025-10-14"
owners: ["@kfm-data", "@kfm-gis"]
tags: ["geojson","raster","fixtures","gis","testing","stac","mcp"]
license: "MIT"
semantic_alignment:
  - GeoJSON RFC 7946
  - STAC 1.0
  - EPSG:4326 (WGS84)
  - MCP-DL v6.2 Reproducible Data Samples
---
````

---

## 🧭 Overview

The `tests/fixtures/geo/` directory contains **geospatial test samples** — minimal vector and raster datasets used to verify the **GIS**, **ETL**, and **STAC** processing pipelines in the **Kansas Frontier Matrix (KFM)** stack.

These samples are:

* 🌐 **Spatially accurate** (EPSG:4326 projection)
* 📏 **Tiny and deterministic** (for fast CI)
* 🧩 **Schema-valid** (GeoJSON / GeoTIFF)
* 🧾 **Provenance-tracked** (checksums, metadata, source citations)

> **Purpose:** to simulate real Kansas geography at small scale — validating reprojection, conversion, and schema logic across the toolchain.

---

## 🧱 Directory Structure

```text
tests/fixtures/geo/
├── ks_county_sample.geojson   # Simplified Kansas county boundaries
├── tiny_vector.geojson        # Two-feature GeoJSON for unit testing
├── dem_sample.tif             # 10×10 raster DEM (single band)
├── tiny_cog.tif               # Tiny Cloud-Optimized GeoTIFF sample
└── README.md                  # This documentation file
```

---

## 🧩 Description of Fixtures

| File                       | Type         | Description                                   | CRS       | Usage                                     |
| :------------------------- | :----------- | :-------------------------------------------- | :-------- | :---------------------------------------- |
| `ks_county_sample.geojson` | Vector       | Polygon boundaries for select Kansas counties | EPSG:4326 | Testing `convert_gis.py` and reprojection |
| `tiny_vector.geojson`      | Vector       | Two-feature micro sample (Larned, Ellsworth)  | EPSG:4326 | CI schema and feature parsing             |
| `dem_sample.tif`           | Raster       | 10×10 elevation raster                        | EPSG:4326 | COG conversion validation                 |
| `tiny_cog.tif`             | Raster (COG) | Pre-converted Cloud-Optimized GeoTIFF         | EPSG:4326 | Raster read and checksum tests            |

---

## 🧠 Fixture Metadata Example (`tiny_vector.geojson`)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "name": "Larned", "county": "Pawnee" },
      "geometry": {
        "type": "Point",
        "coordinates": [-99.1012, 38.1803]
      }
    },
    {
      "type": "Feature",
      "properties": { "name": "Ellsworth", "county": "Ellsworth" },
      "geometry": {
        "type": "Point",
        "coordinates": [-98.2289, 38.7312]
      }
    }
  ],
  "crs": {
    "type": "name",
    "properties": { "name": "EPSG:4326" }
  }
}
```

> Minimal yet complete — valid GeoJSON, UTF-8 encoded, schema-checked before each release.

---

## 🧪 Testing Integration

These geo fixtures are used by:

* `tools/convert_gis.py` → validates vector/raster conversions
* `tools/validate_stac.py` → ensures geometry metadata aligns with STAC Items
* `tools/tests/test_convert_gis.py` → unit tests for projection and field consistency
* `web/src/components/MapView` → optional test snapshots for rendering mock maps

Example test snippet:

```python
import json
from pathlib import Path
import pytest

def test_geojson_schema(fixtures_dir):
    geo = json.loads((fixtures_dir / "geo/tiny_vector.geojson").read_text())
    assert geo["type"] == "FeatureCollection"
    assert len(geo["features"]) == 2
```

---

## 🧮 Regeneration Process

| Step | Tool                                   | Purpose                                           |
| :--- | :------------------------------------- | :------------------------------------------------ |
| 1️⃣  | `tools/notebooks/gis_processing.ipynb` | Create / clip sample geometries                   |
| 2️⃣  | `GDAL` / `ogr2ogr`                     | Export to GeoJSON / GeoTIFF                       |
| 3️⃣  | `rio-cogeo`                            | Convert raster → COG                              |
| 4️⃣  | `pngquant` / `gdal_translate`          | Compress + verify integrity                       |
| 5️⃣  | `sha256sum`                            | Generate fixture checksum for provenance tracking |

All generated files are **validated**, **committed**, and **checksum-verified** under CI before merge.

---

## ♿ Accessibility & Standards

* CRS explicitly defined in metadata (`EPSG:4326`)
* Schema conforms to **GeoJSON RFC 7946**
* Filenames lowercase and descriptive (`tiny_vector.geojson`)
* UTF-8 encoding; no embedded binary data
* All rasters ≤ 10×10 pixels to maintain lightweight footprint
* Color scales for visual demos meet **WCAG 2.1 AA** contrast guidelines

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                                    |
| :--------------- | :------------------------------------------------------------- |
| **Inputs**       | Synthetic geometries and raster clips (USGS, NRCS public data) |
| **Outputs**      | Minimal GeoJSON and GeoTIFF fixtures for tests                 |
| **Dependencies** | GDAL, rasterio, geopandas                                      |
| **Integrity**    | SHA256 checksums verified during CI                            |
| **Traceability** | Linked to regeneration notebooks and commit hashes             |

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                      |
| :------------------ | :-------------------------------------------------- |
| Documentation-first | Each fixture described and versioned in this README |
| Reproducibility     | Generated via notebooks and logged with checksums   |
| Provenance          | Metadata JSON + embedded CRS and source             |
| Open Standards      | GeoJSON / GeoTIFF / EPSG:4326                       |
| Accessibility       | WCAG-compliant color scales for demo rasters        |
| Auditability        | CI validation and reproducibility logs published    |

---

<div align="center">

🗺️ **Small maps — big confidence.**
These geo fixtures are the foundation of reproducible spatial tests for Kansas Frontier Matrix.

</div>
```

