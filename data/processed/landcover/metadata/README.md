<div align="center">

# 🌾 Kansas-Frontier-Matrix — Processed Landcover Metadata (`data/processed/landcover/metadata/`)

**Mission:** Maintain **metadata documentation** for all processed landcover datasets —  
NLCD classifications, vegetation masks, and spectral composites — ensuring transparent lineage,  
licensing, and scientific reproducibility across Kansas Frontier Matrix landcover archives.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Metadata Schema](#metadata-schema)
- [STAC Integration](#stac-integration)
- [Validation & Provenance](#validation--provenance)
- [Adding or Updating Metadata](#adding-or-updating-metadata)
- [References](#references)

---

## 🌍 Overview

This directory contains **metadata JSON files** documenting every processed landcover dataset  
stored in `data/processed/landcover/`. Each file describes a dataset’s origin, processing steps,  
software, and spatial/temporal coverage, forming part of the project’s integrated STAC catalog  
and Master Coder Protocol (MCP) provenance network.

Metadata ensures Kansas’s landcover and vegetation data — from satellite composites to classification  
maps — are fully traceable and reusable across scientific and GIS workflows.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── landcover/
        └── metadata/
            ├── nlcd_2021_ks.json
            ├── vegetation_mask_ks.json
            ├── water_mask_ks.json
            ├── landsat_2021_ks.json
            ├── sentinel_2021_ks.json
            ├── template.json
            └── README.md
````

Each metadata JSON corresponds to one processed dataset and is linked to:

* its `.sha256` checksum in `data/processed/landcover/checksums/`, and
* its entry in the STAC catalog (`data/stac/items/landcover_*`).

---

## 🧩 Metadata Schema

All metadata follow the **hybrid MCP-STAC schema** for geospatial provenance,
which harmonizes open metadata standards (STAC, ISO 19115, schema.org)
with MCP’s documentation-first scientific workflow.

### Example Metadata Record

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "nlcd_2021_ks",
  "properties": {
    "title": "NLCD Landcover 2021 – Kansas",
    "datetime": "2021-01-01T00:00:00Z",
    "description": "National Land Cover Database 2021 classified raster clipped to Kansas boundaries. 30 m resolution.",
    "processing:software": "GDAL 3.8.0 + rasterio + NumPy",
    "mcp_provenance": "sha256:74bde6...",
    "derived_from": ["data/raw/nlcd_2021_us.tif"],
    "spatial_extent": [-102.05, 36.99, -94.59, 40.01],
    "temporal_extent": {"start": "2021-01-01", "end": "2021-12-31"},
    "license": "CC-BY 4.0",
    "keywords": ["landcover", "NLCD", "Kansas", "USGS", "classification"]
  },
  "assets": {
    "data": {
      "href": "../nlcd_2021_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

### Required Fields

| Field                 | Description                          | Example                                               |
| --------------------- | ------------------------------------ | ----------------------------------------------------- |
| `id`                  | Unique dataset identifier            | `"vegetation_mask_ks"`                                |
| `title`               | Dataset name                         | `"Vegetation Mask – Kansas"`                          |
| `description`         | Summary of contents                  | `"Binary raster of vegetation presence (NDVI > 0.3)"` |
| `datetime`            | Processing or dataset reference date | `"2021-07-01T00:00:00Z"`                              |
| `derived_from`        | Source dataset(s)                    | `["data/raw/landsat8_ks_2021.tif"]`                   |
| `processing:software` | Tools used to generate dataset       | `"GDAL 3.8.0 + Python"`                               |
| `mcp_provenance`      | SHA256 checksum reference            | `"sha256:6bfa0f..."`                                  |
| `spatial_extent`      | Bounding box [W, S, E, N]            | `[-102.05, 36.99, -94.59, 40.01]`                     |
| `temporal_extent`     | Dataset time period                  | `{"start": "2021-01-01", "end": "2021-12-31"}`        |
| `license`             | Usage license                        | `"CC-BY 4.0"`                                         |

Optional Fields:

* `keywords` (tags for indexing/search)
* `resolution` (spatial resolution in meters)
* `sensor` (e.g., `"Landsat 8"`, `"Sentinel-2 MSI"`)
* `classification:scheme` (e.g., `"NLCD 2021"`)
* `quality:metrics` (e.g., accuracy assessments or validation reports)

---

## 🌐 STAC Integration

Every metadata file feeds directly into the **SpatioTemporal Asset Catalog (STAC)** at
`data/stac/items/landcover_*`. These catalogs allow spatial and temporal queries by users or
automated workflows and integrate with the Frontier Matrix web map viewer.

**Integration Benefits:**

* Enables API-based access to metadata and assets
* Links datasets by time (e.g., NDVI 2021, NDVI 2022)
* Provides provenance traceability through `derived_from` fields
* Facilitates version control of landcover products

---

## 🔍 Validation & Provenance

All metadata undergo automated validation as part of CI/CD.

**Validation checks include:**

1. **JSON Schema Validation:** Confirms required keys and data types.
2. **Checksum Verification:** Confirms file integrity matches `mcp_provenance`.
3. **STAC Compliance:** Verifies that metadata aligns with STAC 1.0 JSON schema.
4. **Cross-linkage:** Ensures all `derived_from` and `href` paths exist.

Local validation can be performed with:

```bash
make validate-landcover
```

Results are logged to `validation_report.json` within this directory.

---

## 🧠 Adding or Updating Metadata

1. Copy `template.json` → rename it to match the dataset ID (e.g., `water_mask_ks.json`).
2. Fill in all required metadata fields, including processing software and license.
3. Generate or update the dataset’s checksum (`.sha256`) and include it in the metadata’s
   `mcp_provenance` field.
4. Validate locally:

   ```bash
   make validate-landcover
   ```
5. Commit the new or updated metadata, then open a Pull Request for review.
6. The CI pipeline will verify metadata validity, STAC linkage, and checksum accuracy.

---

## 📖 References

* **USGS National Land Cover Database (NLCD):** [https://www.mrlc.gov/data](https://www.mrlc.gov/data)
* **Landsat Science:** [https://landsat.gsfc.nasa.gov](https://landsat.gsfc.nasa.gov)
* **Sentinel-2 Documentation:** [https://scihub.copernicus.eu/](https://scihub.copernicus.eu/)
* **GDAL & rasterio Documentation:** [https://gdal.org](https://gdal.org) / [https://rasterio.readthedocs.io](https://rasterio.readthedocs.io)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)

---

<div align="center">

*“From tallgrass to tilled fields — these metadata preserve the story of Kansas land and its transformations.”*

</div>
```

