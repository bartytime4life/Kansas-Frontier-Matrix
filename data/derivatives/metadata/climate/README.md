<div align="center">

# 🌡️ Kansas Frontier Matrix — Climate Derivative Metadata Summary  
`data/derivatives/metadata/climate/`

**Purpose:** Aggregate and summarize all **climate derivative metadata** files across the Kansas Frontier Matrix (KFM),  
providing a domain-level registry for provenance, validation, and cross-linking within the global derivative metadata system.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/Container-Scan-informational)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory maintains **metadata summaries** for all **derived climate products** generated under  
`data/derivatives/climate/`, ensuring consistency, traceability, and MCP-aligned documentation.

Each metadata file describes:
- Source provenance (`data/sources/…`)
- Derived datasets and processing lineage
- Validation status (checksums, STAC schema compliance)
- Links to model parameters, inputs, and output artifacts
- Associated time ranges, spatial extents, and uncertainty metrics

All metadata conforms to **STAC 1.0.0 + KFM Derivative Metadata Schema v1.0**.

---

## 🧩 Directory Layout

```bash
data/derivatives/metadata/climate/
├── README.md                             # This file
├── mean_temperature_summary.json          # Derived NOAA + PRISM summaries
├── precipitation_anomaly_summary.json     # Rainfall deviation aggregates
├── drought_index_composite.json           # Combined SPI + PDSI + SPEI metrics
├── evapotranspiration_trends.json         # Modeled ET and water balance data
├── validation/                            # QA reports & checksum manifests
│   ├── checksums.sha256
│   └── stac-validation.log
└── schema/                                # JSON Schema for metadata validation
    └── climate_derivative_metadata.schema.json
````

---

## 🧮 Metadata Fields (Core Schema)

| Field             | Type   | Description                                                   |
| ----------------- | ------ | ------------------------------------------------------------- |
| `id`              | string | Unique identifier for the derived dataset                     |
| `title`           | string | Human-readable dataset name                                   |
| `description`     | string | Overview of derivation and relevance                          |
| `provenance`      | object | Source references, processing steps, and responsible entities |
| `spatial_extent`  | object | GeoJSON bbox or region name                                   |
| `temporal_extent` | object | Start/end dates                                               |
| `uncertainty`     | object | Model or aggregation uncertainty (σ, CI, etc.)                |
| `stac_extensions` | array  | References to applied STAC extensions                         |
| `version`         | string | Semantic version of the derivative metadata                   |
| `created`         | string | ISO 8601 creation timestamp                                   |
| `last_updated`    | string | ISO 8601 last update timestamp                                |

---

## 🧠 Example Metadata (Excerpt)

```json
{
  "id": "kfm_climate_derivative_mean_temperature_v1",
  "title": "Mean Temperature Derivative (Kansas 1991–2020)",
  "description": "Derived from NOAA Climate Normals (1991–2020) and PRISM gridded temperature data.",
  "provenance": {
    "sources": [
      "data/sources/noaa_climate_normals_1991_2020.json",
      "data/sources/prism_temperature_monthly.json"
    ],
    "processing": "Aggregation and bias correction via KFM Climate ETL v1.2",
    "validation": "STAC and checksum verified 2025-10-10"
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

## 🧭 Data Lineage (Mermaid Diagram)

```mermaid
flowchart TD
  A["Sources\n(NOAA Normals · PRISM · USGS)"] --> B["ETL + Harmonization\nPython · Makefile · Bias Correction"]
  B --> C["Derived Datasets\nMean Temp · Precip · ET Trends"]
  C --> D["Metadata Registry\n(data/derivatives/metadata/climate)"]
  D --> E["STAC Catalog\n(data/stac/collections/climate_derivatives)"]
<!-- END OF MERMAID -->
```

---

## 🧪 Validation Workflow

All metadata must pass the following gates before merging:

| Check                  | Description                                                 | Tool                                  |
| ---------------------- | ----------------------------------------------------------- | ------------------------------------- |
| ✅ JSON Schema          | Validate against `climate_derivative_metadata.schema.json`  | `jsonschema-cli`                      |
| ✅ STAC Extension       | Confirm valid STAC item fields                              | `stac-validator`                      |
| ✅ Provenance Integrity | Ensure all `provenance.sources[]` exist and match checksums | `sha256sum`                           |
| ✅ Semantic Version     | Validate `version` matches repo tag                         | `bump2version`                        |
| ✅ CI Status            | Auto-verified by GitHub Actions                             | `.github/workflows/stac-validate.yml` |

---

## 🧾 Versioning & Changelog

| Version | Date       | Author                      | Notes                                                    |
| ------- | ---------- | --------------------------- | -------------------------------------------------------- |
| v1.0.0  | 2025-10-11 | Kansas Frontier Matrix Team | Initial creation of climate derivative metadata registry |

All updates to metadata must increment `version` and append a changelog entry in this section.

---

## 🧩 Related Documents

* [`data/derivatives/climate/README.md`](../../climate/README.md) — Core derivative datasets
* [`data/sources/climate/README.md`](../../../sources/climate/README.md) — Source metadata inputs
* [`docs/standards/markdown_protocol.md`](../../../../../docs/standards/markdown_protocol.md) — Markdown & MCP documentation rules
* [`docs/templates/model_card.md`](../../../../../docs/templates/model_card.md) — Template for climate model documentation

---

## 🪶 License & Provenance

**License:** CC-BY 4.0 (data and metadata)
**Provenance:** Generated and maintained under Master Coder Protocol (MCP).
**Maintainers:** Kansas Frontier Matrix Data Integration & Climate Teams
**Last Updated:** 2025-10-11

---
