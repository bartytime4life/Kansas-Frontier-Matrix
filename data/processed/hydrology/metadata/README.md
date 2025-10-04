<div align="center">

# 💧 Kansas-Frontier-Matrix — Processed Hydrology Metadata (`data/processed/hydrology/metadata/`)

**Mission:** Maintain **metadata documentation** for all processed hydrology datasets —  
sink-filled DEMs, flow direction rasters, water masks, and accumulation grids —  
ensuring transparent provenance, validation, and reproducibility across the Kansas Frontier Matrix system.

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

## 🌊 Overview

This directory contains **structured metadata JSON files** describing every processed  
hydrology dataset in `data/processed/hydrology/`. These records provide the **traceable lineage**  
from source DEMs to hydrologically conditioned products used across the Kansas Frontier Matrix project.

Each metadata file conforms to **STAC 1.0** and the **Master Coder Protocol (MCP)** standards,  
allowing machine-readable documentation of processing steps, source provenance, and validation details.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── hydrology/
        └── metadata/
            ├── dem_filled_1m_ks.json
            ├── flow_dir_d8_1m_ks.json
            ├── flow_accum_base_1m_ks.json
            ├── watermask_ks.json
            ├── stream_seed_points.json
            ├── template.json
            └── README.md
````

Each metadata JSON corresponds to a dataset in the parent directory, providing descriptive,
temporal, spatial, and processing metadata.

---

## 🧩 Metadata Schema

Each JSON follows the MCP-STAC hybrid schema, supporting both **geospatial interoperability**
and **scientific traceability**.

### Example Metadata Record

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_dir_d8_1m_ks",
  "properties": {
    "title": "Flow Direction (D8) – Kansas LiDAR DEM",
    "datetime": "2020-01-01T00:00:00Z",
    "description": "Hydrologically conditioned D8 flow direction raster derived from 1 m LiDAR DEM for Kansas.",
    "processing:software": "WhiteboxTools 2.2.0 + GDAL 3.8.0",
    "mcp_provenance": "sha256:9fbe0b...",
    "derived_from": ["data/processed/hydrology/dem_filled_1m_ks.tif"],
    "spatial_extent": [-102.05, 36.99, -94.59, 40.01],
    "temporal_extent": { "start": "2018-01-01", "end": "2020-12-31" },
    "license": "CC-BY 4.0",
    "keywords": ["hydrology", "flow direction", "LiDAR", "Kansas"]
  },
  "assets": {
    "data": {
      "href": "../flow_dir_d8_1m_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  }
}
```

### Required Metadata Fields

| Field                 | Description                          | Example                                        |
| --------------------- | ------------------------------------ | ---------------------------------------------- |
| `id`                  | Unique dataset identifier            | `"dem_filled_1m_ks"`                           |
| `title`               | Dataset title                        | `"Filled DEM (1 m) – Kansas LiDAR"`            |
| `description`         | Short dataset summary                | `"Sink-filled DEM for hydrologic modeling"`    |
| `datetime`            | Processing or dataset reference date | `"2020-01-01T00:00:00Z"`                       |
| `derived_from`        | Source datasets                      | `["data/raw/dem_1m_ks.tif"]`                   |
| `processing:software` | Software and tools used              | `"WhiteboxTools 2.2.0 + GDAL 3.8.0"`           |
| `mcp_provenance`      | SHA256 checksum link                 | `"sha256:abcdef..."`                           |
| `license`             | Data license                         | `"CC-BY 4.0"`                                  |
| `spatial_extent`      | Bounding box [W, S, E, N]            | `[-102.05, 36.99, -94.59, 40.01]`              |
| `temporal_extent`     | Date range of dataset                | `{"start": "2018-01-01", "end": "2020-12-31"}` |

Optional fields:

* `keywords` (e.g., `"watershed"`, `"DEM"`, `"D8"`)
* `quality:metrics` (validation accuracy or completeness notes)
* `resolution` (cell size, e.g. 1.0 m)

---

## 🌐 STAC Integration

All metadata records are automatically synced with the **SpatioTemporal Asset Catalog (STAC)**
in `data/stac/items/hydro_*`. These catalogs enable:

* Spatial filtering (e.g., bounding box searches)
* Temporal querying by acquisition or processing year
* Programmatic access to hydrology data via STAC-compliant APIs
* Direct linkage to web map layers in the Kansas Frontier Matrix viewer

This metadata provides critical context for modelers, researchers, and developers using hydrologic products.

---

## 🔍 Validation & Provenance

All hydrology metadata undergoes multi-step validation:

1. **JSON Schema Validation:** Ensures compliance with `processed_item.schema.json`.
2. **Checksum Verification:** Confirms `mcp_provenance` values match corresponding `.sha256` hashes.
3. **STAC Compliance:** Validates all required fields (title, datetime, license, assets).
4. **Cross-Reference:** Confirms that each `derived_from` dataset exists in the repository.

Run validation locally:

```bash
make validate-hydro
```

All validation results are logged to `validation_report.json`.

---

## 🧠 Adding or Updating Metadata

1. Copy `template.json` → rename it to match dataset ID (e.g., `watermask_ks.json`).
2. Fill in all required MCP and STAC fields.
3. Add checksum hash (`mcp_provenance`) from the dataset’s `.sha256` file.
4. Validate:

   ```bash
   make validate-hydro
   ```
5. Commit metadata and open a Pull Request. CI/CD will run automated schema and checksum validation.

If dataset inputs change, update:

* `derived_from`
* `mcp_provenance`
* `datetime` and `temporal_extent`

---

## 📖 References

* **WhiteboxTools Documentation:** [https://www.whiteboxgeo.com/manual/](https://www.whiteboxgeo.com/manual/)
* **GDAL Utilities:** [https://gdal.org/](https://gdal.org/)
* **USGS 3DEP LiDAR Program:** [https://www.usgs.gov/3dep](https://www.usgs.gov/3dep)
* **Kansas DASC Hydrology Data:** [https://hub.kansasgis.org/](https://hub.kansasgis.org/)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)

---

<div align="center">

*“From groundwater to flowlines — these metadata preserve the lineage of every drop in Kansas’s digital watershed.”*

</div>
```

