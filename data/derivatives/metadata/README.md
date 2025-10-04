<div align="center">

# 🧾 Kansas-Frontier-Matrix — Derivative Metadata (`data/derivatives/metadata/`)

**Mission:** Store and validate all **metadata records** describing derivative datasets —  
ensuring provenance, lineage, licensing, and schema consistency for every processed layer in `data/derivatives/`.

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
- [References](#references)

---

## 🧠 Overview

This directory maintains **JSON metadata and schema definitions** describing every  
processed derivative dataset (e.g., terrain, hydrology, landcover, climate, hazards).  
It acts as the **source of truth** for dataset provenance, version, and lineage within  
the Kansas Frontier Matrix data ecosystem.

Each file documents **where a dataset came from**, **how it was derived**, and **who created it**.  
All metadata conforms to open standards (STAC 1.0, ISO 19115, schema.org) and integrates  
with the project’s [SpatioTemporal Asset Catalog (STAC)](../../stac/) for discovery and validation.

---

## 🎯 Purpose & Role

- Provide consistent **dataset-level metadata** for all products in `data/derivatives/`.  
- Track **source lineage** (`derived_from`) linking outputs to input datasets.  
- Maintain **processing details** (software, parameters, scripts used).  
- Record **temporal and spatial extents** for visualization and filtering.  
- Supply the foundation for **automated STAC generation and validation**.  

Metadata here feeds both:
- the **interactive catalog (data/stac/)**  
- and the **frontend web app** (timeline/map filters, legends, descriptions).  

---

## 🧱 Directory Layout

```bash
data/
└── derivatives/
    └── metadata/
        ├── schema/
        │   ├── derivative_item.schema.json     # JSON Schema for derivative metadata
        │   ├── stac_item.schema.json           # STAC 1.0 compliance reference
        │   └── validation_rules.json           # Custom MCP rules
        ├── terrain/
        │   ├── slope_1m_ks.json
        │   ├── hillshade_1m_ks.json
        ├── hydrology/
        │   ├── flow_direction_1m_ks.json
        │   └── flow_accumulation_1m_ks.json
        ├── landcover/
        │   ├── ndvi_2021_ks.json
        │   └── nlcd_1992_2021_change.json
        ├── climate/
        │   ├── temp_anomaly_1895_2024.json
        │   └── drought_index_spi12.json
        ├── hazards/
        │   ├── tornado_density_1950_2024.json
        │   └── flood_extent_1993_ks.json
        ├── template.json                       # Template for new derivative metadata
        └── README.md
````

---

## 🧩 Metadata Standards

Each metadata JSON follows the **MCP-compliant hybrid schema**, combining:

* **STAC Core fields:** `id`, `type`, `stac_version`, `assets`, `bbox`, `datetime`, `properties`
* **MCP Provenance fields:** `mcp_provenance`, `derived_from`, `processing:software`, `author`, `created_at`
* **Schema.org extensions:** for keywords, creators, and citations.

### Example

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ndvi_2021_ks",
  "properties": {
    "title": "Normalized Difference Vegetation Index (NDVI) – Kansas 2021",
    "datetime": "2021-07-01T00:00:00Z",
    "description": "Vegetation index derived from Landsat 8 imagery (B5–B4)/(B5+B4).",
    "processing:software": "GDAL 3.8.0 + NumPy",
    "mcp_provenance": "sha256:a23be8…",
    "derived_from": ["data/sources/landsat8_ks_2021.tif"],
    "license": "CC-BY 4.0",
    "keywords": ["NDVI", "vegetation", "Kansas", "remote sensing"]
  },
  "assets": {
    "data": {
      "href": "../../landcover/ndvi_2021_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

---

## 🌐 STAC Integration

Every metadata file is part of the Frontier Matrix’s broader **STAC Catalog**, linking
each derivative to its collection and enabling standardized spatial-temporal search.

Metadata from here feeds:

* `data/stac/items/` → per-layer catalog entries
* `data/stac/collections/` → thematic collections (terrain, hydrology, etc.)

A CI job (`.github/workflows/stac-validate.yml`) validates these JSONs against both
the **official STAC schema** and the **internal MCP schema** defined in `schema/`.

---

## 🧮 Validation & Provenance

All metadata undergoes **multi-layer validation**:

1. **JSON Schema validation:** ensures required fields and correct types.
2. **STAC compliance:** checks `stac_version`, asset roles, and required properties.
3. **Provenance verification:** cross-checks `derived_from` and `sha256` hashes.
4. **Temporal validation:** ensures dataset time ranges align with sources.

Validation runs automatically in CI/CD and can be triggered locally with:

```bash
make validate-metadata
```

The validation log is saved as `validation_report.json` in this directory.

---

## 🧠 Adding or Editing Metadata

1. Copy `template.json` into the appropriate subfolder (terrain, hydrology, etc.).
2. Fill in:

   * `title`, `description`, `datetime`, and `license`
   * `derived_from`: path(s) to original datasets
   * `processing:software` and `mcp_provenance` (hash)
3. Run schema validation locally:

   ```bash
   make validate-metadata
   ```
4. Commit the JSON file along with the related dataset and checksum.
5. Push changes — CI will validate automatically.

If metadata fails validation, errors are reported inline with line numbers and field names.

---

## 📖 References

* **STAC Specification 1.0.0:** [https://stacspec.org](https://stacspec.org)
* **ISO 19115 Metadata Standard:** [https://www.iso.org/standard/53798.html](https://www.iso.org/standard/53798.html)
* **Schema.org Dataset Vocabulary:** [https://schema.org/Dataset](https://schema.org/Dataset)
* **OGC GeoTIFF Standard:** [https://docs.opengeospatial.org/is/19-008r4/19-008r4.html](https://docs.opengeospatial.org/is/19-008r4/19-008r4.html)
* **Master Coder Protocol (MCP) Documentation:** [`docs/standards/`](../../../docs/standards/)
* **Kansas Frontier Matrix STAC Catalog:** [`data/stac/`](../../stac/)

---

<div align="center">

*“Metadata is the map of maps — preserving the who, what, when, and why behind Kansas’s digital frontier.”*

</div>
```

