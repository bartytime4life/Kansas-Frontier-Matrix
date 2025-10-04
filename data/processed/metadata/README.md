<div align="center">

# 🧾 Kansas-Frontier-Matrix — Processed Metadata (`data/processed/metadata/`)

**Mission:** Maintain **metadata records** describing all processed datasets — their lineage,  
license, temporal coverage, and schema — ensuring traceability and reproducibility throughout  
the Kansas Frontier Matrix data lifecycle.

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
- [Purpose & Scope](#purpose--scope)
- [Directory Layout](#directory-layout)
- [Metadata Standards](#metadata-standards)
- [STAC & MCP Integration](#stac--mcp-integration)
- [Validation & Provenance](#validation--provenance)
- [Adding or Updating Metadata](#adding-or-updating-metadata)
- [References](#references)

---

## 🧠 Overview

This directory contains the **metadata registry for all processed datasets** under  
`data/processed/`. It acts as the canonical record for dataset provenance,  
providing the “who, what, when, and how” for every intermediate product in  
the Kansas Frontier Matrix data pipeline.

Each JSON file describes:
- Source lineage (`derived_from`)  
- Software and parameters used for processing  
- Spatial and temporal coverage  
- Licensing, versioning, and author information  

All metadata here conforms to **STAC 1.0** and **Master Coder Protocol (MCP)**  
documentation rules to ensure consistency across layers and subdomains.

---

## 🎯 Purpose & Scope

This folder serves three main functions:
1. **Traceability:** Provide clear provenance for each processed dataset.  
2. **Validation:** Enable CI/CD automation to confirm schema compliance.  
3. **Integration:** Supply the [STAC catalog](../../stac/) and frontend UI with descriptive metadata.

Metadata in this directory connects *processed* datasets (intermediate, cleaned, or standardized)  
to their original raw inputs and derived downstream products.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── metadata/
        ├── schema/
        │   ├── processed_item.schema.json        # JSON schema for processed metadata
        │   ├── stac_item.schema.json             # STAC compliance reference
        │   └── validation_rules.json             # Additional MCP validation rules
        ├── terrain/
        │   ├── dem_1m_ks_filled.json
        │   ├── dem_30m_ned_ks.json
        ├── hydrology/
        │   ├── flow_dir_d8_1m_ks.json
        │   ├── watermask_ks.json
        ├── landcover/
        │   ├── nlcd_2021_ks.json
        │   ├── vegetation_mask_ks.json
        ├── climate/
        │   ├── precip_total_annual_1895_2024.json
        │   ├── drought_spi12_1895_2024.json
        ├── hazards/
        │   ├── tornado_tracks_1950_2024.json
        │   ├── fema_disasters_1953_2024.json
        ├── tabular/
        │   ├── tornado_counts_1950_2024.json
        │   ├── county_population_1850_2020.json
        ├── text/
        │   ├── newspapers_1854_1925_cleaned.json
        │   ├── ocr_cleaned_diaries_1850_1900.json
        ├── template.json                         # Metadata template for new datasets
        └── README.md
````

Each subfolder corresponds to a data domain (terrain, hydrology, etc.) and mirrors
the structure of `data/processed/` for easy navigation and consistency.

---

## 🧩 Metadata Standards

All metadata files conform to the **hybrid MCP-STAC schema**, ensuring both machine-readability
and scientific traceability.

### Required Fields

| Field                 | Description                          | Example                                                    |
| --------------------- | ------------------------------------ | ---------------------------------------------------------- |
| `id`                  | Unique dataset identifier            | `"dem_1m_ks_filled"`                                       |
| `stac_version`        | STAC schema version                  | `"1.0.0"`                                                  |
| `title`               | Human-readable dataset name          | `"Filled DEM (1m) – Kansas"`                               |
| `description`         | Summary of dataset contents          | `"Hydrologically conditioned DEM derived from LiDAR data"` |
| `datetime`            | Processing or dataset reference date | `"2020-01-01T00:00:00Z"`                                   |
| `derived_from`        | Raw source(s) or prior datasets      | `["data/raw/dem_1m_ks.tif"]`                               |
| `processing:software` | Tools or scripts used                | `"GDAL 3.8.0 + WhiteboxTools 2.2.0"`                       |
| `mcp_provenance`      | SHA256 checksum or version hash      | `"sha256:cf1e98..."`                                       |
| `license`             | Data license (default CC-BY 4.0)     | `"CC-BY 4.0"`                                              |
| `authors`             | Responsible parties                  | `["Frontier Matrix Core Team"]`                            |

### Optional Extensions

* `keywords` (array of thematic tags)
* `bbox` and `spatial_extent` (for geospatial datasets)
* `temporal_extent` (start/end ISO dates)
* `quality:metrics` (accuracy, completeness, etc.)

---

## 🌐 STAC & MCP Integration

Each processed metadata file is directly linked to:

* **STAC Catalog:** Populates entries in `data/stac/items/processed_*`
* **MCP Provenance Chain:** Enables automated lineage reconstruction via `mcp_provenance` fields

During CI/CD (`.github/workflows/stac-validate.yml`), each JSON is validated against:

1. `schema/processed_item.schema.json`
2. `schema/stac_item.schema.json`
3. MCP rules in `validation_rules.json`

This guarantees interoperability with geospatial APIs and metadata aggregators.

---

## 🔎 Validation & Provenance

Automated validation includes:

* **JSON Schema Validation:** Checks required fields and value types.
* **Checksum Verification:** Confirms all `mcp_provenance` hashes exist in corresponding checksum files.
* **STAC Compliance:** Verifies required STAC 1.0 fields (`id`, `type`, `stac_version`, `assets`, `properties`).
* **Temporal Consistency:** Confirms `datetime` and `temporal_extent` fields align with data content.

Run local validation with:

```bash
make validate-metadata
```

Results are saved as `validation_report.json` for review.

---

## 🧠 Adding or Updating Metadata

1. Copy `template.json` into the relevant subfolder (terrain, hydrology, etc.).
2. Fill in all mandatory fields: `id`, `title`, `description`, `derived_from`, `processing:software`.
3. Compute the dataset’s checksum and insert it into `mcp_provenance`.
4. Validate:

   ```bash
   make validate-metadata
   ```
5. Commit changes and submit a Pull Request including:

   * Updated metadata file
   * Associated dataset checksum
   * Description of processing updates

All contributions are automatically validated during CI/CD.

---

## 📖 References

* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **ISO 19115 Metadata Standard:** [https://www.iso.org/standard/53798.html](https://www.iso.org/standard/53798.html)
* **Schema.org Dataset Vocabulary:** [https://schema.org/Dataset](https://schema.org/Dataset)
* **JSON Schema Specification:** [https://json-schema.org](https://json-schema.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../docs/standards/)
* **Frontier Matrix STAC Catalog:** [`data/stac/`](../../stac/)

---

<div align="center">

*“Metadata is the foundation of reproducibility — every file tells its own origin story in the Kansas Frontier Matrix.”*

</div>
```

