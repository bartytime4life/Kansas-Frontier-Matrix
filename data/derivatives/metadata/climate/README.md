<div align="center">

# 🌡️ Kansas Frontier Matrix — Climate Derivative Metadata Summary  
`data/derivatives/metadata/climate/`

**Purpose:** Centralize and document all **climate derivative metadata** across the Kansas Frontier Matrix (KFM),  
ensuring provenance, version control, and machine-actionable linkage within the global derivative metadata ecosystem.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **metadata registries** for all **derived climate datasets** within  
`data/derivatives/climate/`. These JSON documents ensure **traceability**, **validation**,  
and **scientific reproducibility**, following **Master Coder Protocol (MCP)** and **STAC 1.0.0** standards.

Each metadata file records:
- Provenance of input datasets (`data/sources/...`)
- Processing lineage and ETL workflow details
- Version-controlled STAC schema validation status
- Temporal and spatial coverage
- Statistical uncertainty and bias correction metrics
- Dataset licensing and authorship metadata

All records follow the **KFM Derivative Metadata Schema v1.0**, located under `schema/`.

---

## 🧩 Directory Layout

```bash
data/derivatives/metadata/climate/
├── README.md                             # This file
├── mean_temperature_summary.json          # NOAA + PRISM mean temperature composites
├── precipitation_anomaly_summary.json     # Rainfall deviation metrics
├── drought_index_composite.json           # Combined SPI, PDSI, SPEI indices
├── evapotranspiration_trends.json         # ET and water-balance derived data
├── validation/                            # Validation reports and checksums
│   ├── checksums.sha256
│   └── stac-validation.log
└── schema/                                # JSON Schema for metadata validation
    └── climate_derivative_metadata.schema.json
````

---

## 🧮 Core Metadata Schema

| Field             | Type   | Description                                            |
| ----------------- | ------ | ------------------------------------------------------ |
| `id`              | string | Unique dataset identifier (STAC-compliant)             |
| `title`           | string | Human-readable dataset title                           |
| `description`     | string | Concise dataset summary and significance               |
| `provenance`      | object | Source references, ETL lineage, and responsible agents |
| `spatial_extent`  | object | Bounding box or named region (GeoJSON)                 |
| `temporal_extent` | object | Start and end ISO 8601 timestamps                      |
| `uncertainty`     | object | Statistical uncertainty and confidence metrics         |
| `stac_extensions` | array  | STAC extensions applied (e.g., processing, provenance) |
| `version`         | string | Dataset semantic version (x.y.z)                       |
| `created`         | string | ISO 8601 dataset creation timestamp                    |
| `last_updated`    | string | Last modification date                                 |

---

## 🧠 Example Metadata Record

```json
{
  "id": "kfm_climate_derivative_mean_temperature_v1",
  "title": "Mean Temperature Derivative (Kansas 1991–2020)",
  "description": "Derived from NOAA Climate Normals (1991–2020) and PRISM gridded temperature datasets.",
  "provenance": {
    "sources": [
      "data/sources/noaa_climate_normals_1991_2020.json",
      "data/sources/prism_temperature_monthly.json"
    ],
    "processing": "Aggregation and bias correction using KFM Climate ETL v1.2",
    "validation": "Checksum and STAC compliance verified on 2025-10-10"
  },
  "spatial_extent": {
    "bbox": [-102.05, 36.99, -94.59, 40.00],
    "crs": "EPSG:4326"
  },
  "temporal_extent": {
    "start": "1991-01-01",
    "end": "2020-12-31"
  },
  "uncertainty": {
    "mean_bias": 0.12,
    "rmse": 0.31,
    "confidence_interval": "95%"
  },
  "stac_extensions": [
    "https://stac-extensions.github.io/processing/v1.1.0/schema.json",
    "https://stac-extensions.github.io/provenance/v1.0.0/schema.json"
  ],
  "version": "1.0.0",
  "created": "2025-10-10",
  "last_updated": "2025-10-11"
}
```

---

## 🧭 Data Lineage

```mermaid
flowchart TD
  A["Source Datasets\n(NOAA Normals · PRISM · USGS)"] --> B["ETL & Harmonization\nPython · Makefile · Bias Correction"]
  B --> C["Derived Products\nMean Temp · Precipitation · Evapotranspiration"]
  C --> D["Metadata Registry\n(data/derivatives/metadata/climate)"]
  D --> E["STAC Catalog\n(data/stac/collections/climate_derivatives)"]


<!-- END OF MERMAID -->
```

---

## 🧪 Validation Workflow

Each metadata entry passes through standardized validation gates before merge or deployment.

| Check                        | Description                                                | Tool                                  |
| ---------------------------- | ---------------------------------------------------------- | ------------------------------------- |
| ✅ **JSON Schema**            | Validate against `climate_derivative_metadata.schema.json` | `jsonschema-cli`                      |
| ✅ **STAC Extension**         | Ensure valid STAC item structure                           | `stac-validator`                      |
| ✅ **Provenance Integrity**   | Verify referenced sources and checksum match               | `sha256sum`                           |
| ✅ **Semantic Version**       | Confirm `version` consistency with repo tag                | `bump2version`                        |
| ✅ **Continuous Integration** | Auto-validation on PR and build                            | `.github/workflows/stac-validate.yml` |

---

## 🧾 Versioning & Changelog

| Version | Date       | Author(s)                    | Description                                                        |
| ------- | ---------- | ---------------------------- | ------------------------------------------------------------------ |
| v1.1.0  | 2025-10-11 | KFM Climate Integration Team | Formatting upgrades, added frontmatter & enhanced schema reference |
| v1.0.0  | 2025-10-10 | Kansas Frontier Matrix Team  | Initial creation of climate derivative metadata registry           |

> All updates to metadata must increment the `version` field and append a corresponding changelog entry.

---

## 🧩 Related Documents

* [`data/derivatives/climate/README.md`](../../climate/README.md) — Core climate derivative datasets
* [`data/sources/climate/README.md`](../../../sources/climate/README.md) — Source dataset registry
* [`docs/standards/markdown_protocol.md`](../../../../../docs/standards/markdown_protocol.md) — Markdown & MCP documentation rules
* [`docs/templates/model_card.md`](../../../../../docs/templates/model_card.md) — Climate model documentation template
* [`docs/architecture/data_lineage.md`](../../../../../docs/architecture/data_lineage.md) — End-to-end lineage trace

---

## 🪶 License & Provenance

**License:** [CC-BY 4.0](../../../../../LICENSE)
**Provenance:** Generated and maintained under **Master Coder Protocol (MCP)** compliance, ensuring reproducibility, traceability, and transparency.
**Maintainers:** Kansas Frontier Matrix Climate & Data Integration Teams
**Last Updated:** 2025-10-11

---

```
