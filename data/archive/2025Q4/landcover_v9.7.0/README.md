---
title: "🌾 Kansas Frontier Matrix — Q4 2025 Landcover Dataset Archive (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/archive/2025Q4/landcover_v9.7.0/README.md"
version: "v9.7.0"
last_updated: "2025-11-06"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.7.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-landcover-archive-v4.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
---

<div align="center">

# 🌾 Kansas Frontier Matrix — **Q4 2025 Landcover Dataset Archive**
`data/archive/2025Q4/landcover_v9.7.0/README.md`

**Purpose:**  
Documents the **FAIR+CARE-certified landcover and vegetation datasets** archived for Q4 2025.  
These datasets support long-term land-use analysis, vegetation health monitoring, and sustainable land management in Kansas through open, ethically governed data.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../../docs/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](../../../../LICENSE)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Landcover%20Certified-gold.svg)](../../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-blue.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Q4 2025 Landcover Dataset Archive** integrates remote sensing and field-validated data on vegetation, crop cover, and soil classification from **NASA MODIS**, **USDA NLCD**, and **NOAA AVHRR** sources.  
This dataset represents a multi-temporal analysis of landcover trends for Kansas between **1980–2025**, optimized for **FAIR+CARE-compliant scientific reuse** and **Focus Mode visualization**.

All files are:
- **Checksum-verified (SHA-256)** with immutable ledger logging.  
- **FAIR+CARE-certified**, ensuring open, ethical stewardship.  
- **Interoperable** under STAC/DCAT catalogs and ISO 19115 metadata.  
- **Publicly licensed (CC-BY 4.0)** for sustainable reuse.

---

## 🗂️ Directory Layout

```plaintext
data/archive/2025Q4/landcover_v9.7.0/
├── README.md                           # This file — documentation for Q4 2025 Landcover dataset
│
├── landcover_ndvi_1980_2025.tif        # Normalized Difference Vegetation Index composite
├── landcover_classification.geojson    # Polygon dataset of landcover classification zones
├── landcover_statistics.parquet        # Tabular dataset of vegetation cover metrics
├── metadata.json                       # STAC/DCAT metadata (ISO 19115 compliant)
├── checksums.json                      # File-level SHA-256 verification records
└── validation_report.json              # FAIR+CARE and schema validation report
```

---

## ⚙️ Dataset Specifications

| Field | Description | Example |
|---|---|---|
| `feature_id` | Unique polygon or raster feature ID. | `KFM_LC_2025_00218` |
| `landcover_class` | Landcover type (forest, cropland, grassland, urban, barren, etc.). | `Cropland` |
| `ndvi_mean` | Mean NDVI (Normalized Difference Vegetation Index). | `0.72` |
| `soil_type` | USDA soil classification. | `Loam` |
| `percent_cover` | Percentage of area covered by vegetation type. | `68.4` |
| `year` | Observation year. | `2025` |
| `geometry` | GeoJSON geometry (Polygon/Multipolygon). | `{ "type": "Polygon", "coordinates": [...] }` |
| `fairstatus` | FAIR+CARE certification status. | `certified` |
| `checksum_sha256` | File hash for data integrity. | `sha256:f8c3e2a91f8d3a84b0f...` |

---

## 🧠 FAIR+CARE Governance Matrix

| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | Indexed through STAC and DCAT catalogs. | `@kfm-data` |
| **Accessible** | GeoTIFF, GeoJSON, and Parquet files openly available. | `@kfm-accessibility` |
| **Interoperable** | Schema adheres to ISO 19115 and FAIR+CARE Data Contract v3. | `@kfm-architecture` |
| **Reusable** | Includes lineage, licensing, and checksum metadata. | `@kfm-design` |
| **Collective Benefit** | Enables sustainable agriculture and conservation research. | `@faircare-council` |
| **Authority to Control** | FAIR+CARE Council validates and signs release certification. | `@kfm-governance` |
| **Responsibility** | Maintainers ensure schema validation and checksum verification. | `@kfm-security` |
| **Ethics** | Sensitive ecological data anonymized for public access. | `@kfm-ethics` |

Governance reference:  
`data/reports/audit/data_provenance_ledger.json`

---

## 🧩 Validation & Provenance Workflow

| Process | Tool / Workflow | Output |
|---|---|---|
| **Schema Validation** | `schema_validation.py` | `validation_report.json` |
| **Checksum Verification** | `checksum-verify.yml` | `checksums.json` |
| **FAIR+CARE Audit** | `faircare-validate.yml` | `data/reports/fair/faircare_summary.json` |
| **Governance Registration** | `governance-ledger.yml` | `data_provenance_ledger.json` |
| **Catalog Publication** | `stac-validate.yml` | `data/stac/catalog.json` |

---

## 📊 Example Provenance Record

```json
{
  "id": "landcover_v9.7.0",
  "records_total": 88935,
  "checksum_verified": true,
  "fairstatus": "certified",
  "schema_version": "v3.0.1",
  "governance_registered": true,
  "archived_by": "@kfm-data",
  "timestamp": "2025-11-06T19:51:00Z"
}
```

---

## 🌍 STAC & DCAT Integration

- **STAC Collection ID:** `landcover-kansas-v9.7.0`  
- **DCAT Dataset ID:** `kfm-landcover-2025q4`  
- **ISO Metadata File:** `data/archive/2025Q4/landcover_v9.7.0/metadata.json`  
- **JSON-LD Context:** `https://stacspec.org/v1.0.0/metadata.jsonld`

Catalog entry recorded in:  
`data/stac/landcover-kansas-v9.7.0.json`

---

## 🌱 Sustainability & Quality Metrics

| Metric | Value | Verified By |
|---|---|---|
| Checksum Accuracy | 100% | `@kfm-validation` |
| FAIR+CARE Compliance | ✅ Certified | `@faircare-council` |
| Schema Conformance | ≥ 99.8% | `@kfm-data` |
| Energy Efficiency | 10.2 Wh per validation run | `@kfm-sustainability` |
| Provenance Ledger Sync | ✅ Verified | `@kfm-governance` |

Telemetry reference:  
`../../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Landcover Dataset Archive (v9.7.0, Q4 2025).
FAIR+CARE-certified landcover datasets integrating MODIS, NLCD, and AVHRR records for Kansas.
Implements ISO 19115 metadata, STAC/DCAT interoperability, and ethical open-data governance for sustainable land management.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v9.7.0 | 2025-11-06 | `@kfm-data` | Created Q4 2025 landcover dataset README; added FAIR+CARE matrix, metadata, and checksum provenance. |
| v9.6.0 | 2025-11-03 | `@kfm-archive` | Added ISO metadata validation and DCAT indexing support. |
| v9.3.2 | 2025-10-28 | `@kfm-core` | Established base FAIR+CARE structure for landcover archives. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Landcover Transparency × FAIR+CARE Ethics × Provenance Preservation*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Q4 Archive](../README.md) · [Governance Charter](../../../../docs/standards/governance/DATA-GOVERNANCE.md) · [FAIR+CARE Reports](../../../../data/reports/fair/faircare_summary.json)

</div>

