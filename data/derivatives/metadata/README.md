<div align="center">

# 🧾 Kansas Frontier Matrix — Derivative Metadata  
`data/derivatives/metadata/`

**Mission:** Provide authoritative, reproducible **metadata records** for every derivative dataset —  
documenting provenance, lineage, licensing, and schema validation for the full KFM processing chain.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Purpose & Role](#purpose--role)
- [Directory Layout](#directory-layout)
- [Metadata Standards](#metadata-standards)
- [STAC Integration](#stac-integration)
- [Validation & Provenance](#validation--provenance)
- [Adding or Editing Metadata](#adding-or-editing-metadata)
- [Makefile & CI Hooks](#makefile--ci-hooks)
- [Examples](#examples)
- [References](#references)
- [Changelog](#changelog)

---

## 🧠 Overview

The **`data/derivatives/metadata/`** directory contains canonical JSON metadata for all processed derivative products  
(e.g., terrain, hydrology, landcover, climate, hazards).  
Each record is the **authoritative source of truth** for dataset lineage, versioning, licensing, and reproducibility  
under the **Master Coder Protocol (MCP)**.

All metadata conforms to:
- **STAC 1.0.0** (SpatioTemporal Asset Catalog)
- **ISO 19115** (Geospatial Metadata)
- **schema.org/Dataset**
- **MCP Provenance Extensions**

---

## 🎯 Purpose & Role

- Ensure each dataset in `data/derivatives/` has a reproducible metadata record.  
- Preserve **provenance**: track every dataset’s origin and derivation chain.  
- Encode **validation**, **licensing**, and **spatial/temporal context**.  
- Provide ready-to-ingest metadata for the **STAC catalog** and **MapLibre UI**.  
- Serve as the integration point between raw sources and derived public artifacts.

---

## 🧱 Directory Layout
```bash
data/
└── derivatives/
    └── metadata/
        ├── schema/
        │   ├── README.md                       # Schema documentation and validation rules
        │   ├── derivative_item.schema.json      # Core KFM metadata schema (STAC + MCP)
        │   ├── stac_item.schema.json            # Reference STAC 1.0 schema (mirrored/pinned)
        │   └── validation_rules.json            # MCP conditional logic and required field definitions
        ├── terrain/
        │   ├── README.md                        # Terrain derivative metadata registry
        │   ├── slope_1m_ks.json                 # 1m slope raster metadata
        │   ├── hillshade_1m_ks.json             # Hillshade derived from DEM
        │   └── validation/
        │       ├── README.md                    # Terrain metadata validation logs
        │       ├── checksums.sha256             # File integrity hashes
        │       └── stac-validation.log          # STAC + schema validation output
        ├── hydrology/
        │   ├── README.md                        # Hydrology derivative metadata registry
        │   ├── flow_direction_1m_ks.json        # Flow direction (TauDEM D8)
        │   ├── flow_accumulation_1m_ks.json     # Flow accumulation metadata
        │   └── validation/
        │       ├── README.md                    # Hydrology validation workflow + logs
        │       ├── checksums.sha256
        │       └── stac-validation.log
        ├── landcover/
        │   ├── README.md                        # Landcover derivative metadata registry
        │   ├── ndvi_2021_ks.json                # NDVI (Normalized Difference Vegetation Index)
        │   ├── nlcd_1992_2021_change.json       # NLCD landcover change detection
        │   └── validation/
        │       ├── README.md                    # Landcover metadata validation logs
        │       ├── checksums.sha256
        │       └── stac-validation.log
        ├── climate/
        │   ├── README.md                        # Climate derivative metadata registry
        │   ├── mean_temperature_summary.json     # NOAA + PRISM mean temperature composites
        │   ├── precipitation_anomaly_summary.json# Rainfall deviation metrics
        │   ├── drought_index_composite.json      # Combined SPI · PDSI · SPEI metrics
        │   ├── evapotranspiration_trends.json    # Modeled ET and water-balance data
        │   ├── validation/
        │   │   ├── README.md                    # Climate metadata validation logs
        │   │   ├── checksums.sha256
        │   │   └── stac-validation.log
        │   └── schema/
        │       ├── README.md                    # Climate metadata schema documentation
        │       └── climate_derivative_metadata.schema.json
        ├── hazards/
        │   ├── README.md                        # Hazards derivative metadata registry
        │   ├── tornado_density_1950_2024.json    # Tornado density (NOAA SPC)
        │   ├── flood_extent_1993_ks.json         # Flood extent polygons
        │   └── validation/
        │       ├── README.md                    # Hazards validation logs
        │       ├── checksums.sha256
        │       └── stac-validation.log
        ├── template.json                         # Template for new derivative metadata files
        └── README.md                             # This document (root metadata overview)

````

---

## 🧩 Metadata Standards

Each metadata JSON merges **MCP Provenance** with **STAC 1.0 Core**, extended for
machine reproducibility and knowledge-graph integration.

| Standard               | Key Fields                                                                                                         | Description                           |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------- | :------------------------------------ |
| **STAC Core**          | `id`, `type`, `stac_version`, `bbox`, `geometry`, `datetime`, `properties`, `assets`                               | Core item structure                   |
| **MCP Provenance**     | `mcp_provenance`, `derived_from`, `processing:software`, `processing:parameters`, `author`, `created_at`, `commit` | Document lineage & environment        |
| **Schema.org Dataset** | `keywords`, `citation`, `creator`, `isBasedOn`, `license`                                                          | Semantic enrichment for searchability |

> 🧮 Validation: `schema/derivative_item.schema.json` → **local check**,
> GitHub Actions `.github/workflows/stac-validate.yml` → **automated CI validation**.

---

## 🌐 STAC Integration

Every derivative metadata file contributes directly to the global **STAC catalog**:

* `data/stac/items/` → item-level JSON entries (each dataset)
* `data/stac/collections/` → thematic rollups (terrain, hydrology, climate, etc.)

Checksums from the derivative folders populate `checksum:sha256` in STAC asset definitions.
Automated workflows validate STAC compliance and maintain referential integrity.

---

## 🧮 Validation & Provenance

```mermaid
flowchart TD
    A["Raw Sources<br/>(data/sources/)"]
        --> B["ETL Processing<br/>(data/processed/)"]
    B --> C["Derived Products<br/>(data/derivatives/)"]
    C --> D["Derivative Metadata<br/>(data/derivatives/metadata/)"]
    D --> E["STAC Catalog<br/>(data/stac/items/ · collections/)"]
    E --> F["Continuous Validation<br/>Schema · STAC · Checksum"]
    F --> G["Web Application<br/>Timeline · Map · Entity Panels"]
```

---

## 🧠 Adding or Editing Metadata

1. **Copy template:**
   `cp template.json <domain>/<new_id>.json`
2. **Fill required fields:**
   `id`, `stac_version`, `title`, `description`, `license`,
   `processing:software`, `derived_from[]`.
3. **Add lineage:**
   Ensure `derived_from` paths reference valid upstream sources.
4. **Record environment:**
   Include `processing:parameters` and `container:image` if used.
5. **Validate:**
   `make validate-metadata`
6. **Commit + PR:**
   Include dataset + checksum; CI auto-runs STAC and schema validation.

---

## 🔧 Makefile & CI Hooks

```make
validate-metadata:
	jsonschema -i data/derivatives/metadata/**/*.json \
	           data/derivatives/metadata/schema/derivative_item.schema.json

stac-validate:
	stac-validator data/stac/items/**/*.json

check-checksums:
	python scripts/validate_checksums.py --root data/derivatives
```

**Recommended pre-commit hooks**

* `jsonlint` or `prettier --parser json`
* Schema validation of `data/derivatives/metadata/**/*.json`
* Require `checksum:sha256` for all assets

---

## 🧪 Example — Minimal Derivative Item

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ndvi_2021_ks",
  "properties": {
    "title": "NDVI — Kansas 2021",
    "description": "Normalized Difference Vegetation Index derived from Landsat 8.",
    "datetime": "2021-07-01T00:00:00Z",
    "processing:software": "GDAL 3.8.0 + NumPy",
    "processing:parameters": {"expression": "(B5 - B4)/(B5 + B4)"},
    "mcp_provenance": "sha256:a23be8...",
    "derived_from": ["data/sources/landsat8_ks_2021.tif"],
    "license": "CC-BY 4.0",
    "keywords": ["NDVI", "Kansas", "remote sensing"]
  },
  "assets": {
    "data": {
      "href": "../../landcover/ndvi_2021_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "checksum:sha256": "e3b0c44298fc1c149afbf4c8996fb924..."
    }
  }
}
```

---

## 📖 References

* [STAC 1.0 Specification](https://stacspec.org)
* [ISO 19115 — Geographic Metadata](https://www.iso.org/standard/53798.html)
* [Schema.org Dataset](https://schema.org/Dataset)
* [OGC GeoTIFF 1.1 Specification](https://docs.ogc.org/is/19-008r4/19-008r4.html)
* [Master Coder Protocol Docs](../../../docs/standards/)
* [KFM STAC Catalog](../../stac/)

---

## 🗓️ Changelog

| Version    | Date       | Author                | Notes                                                                                       |
| :--------- | :--------- | :-------------------- | :------------------------------------------------------------------------------------------ |
| **v1.3.0** | 2025-10-11 | Data Integration Team | Expanded Climate directory structure, improved Mermaid rendering, and standardized CI hooks |
| **v1.2.1** | 2025-10-11 | KFM Team              | Fixed fence balance and GitHub-safe rendering                                               |
| **v1.2.0** | 2025-10-10 | KFM Team              | Added Makefile hooks, clarified MCP fields                                                  |
| **v1.1.0** | 2025-10-08 | KFM Team              | Introduced hybrid MCP + STAC schema validation                                              |
| **v1.0.0** | 2025-10-01 | KFM Core              | Initial metadata registry foundation                                                        |

```

---
