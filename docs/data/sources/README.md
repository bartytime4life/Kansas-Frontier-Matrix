---
title: "🌎 Kansas Frontier Matrix — Data Sources & Registries (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/sources/README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-sources-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌎 **Kansas Frontier Matrix — Data Sources & Registries**
`docs/data/sources/README.md`

**Purpose:**  
Catalog and describe all **approved datasets and APIs** integrated into the **Kansas Frontier Matrix (KFM)** platform.  
This registry provides authoritative references, provenance metadata, and governance status for environmental, historical, and cultural data sources under **FAIR+CARE** certification.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

KFM integrates data from **federal, state, tribal, academic, and open-source repositories** to reconstruct Kansas’s environmental and cultural history across time.  
This directory documents:
- All **active data sources** linked to the KFM data pipelines.  
- **Provenance**, **license**, and **format details** for each dataset.  
- **Governance status** (approved, restricted, pending).  
- **STAC/DCAT mappings** for automated catalog generation.

Every dataset listed here must meet:
1. **FAIR+CARE certification** requirements.  
2. **Schema conformance** to `data-contract-v3.json`.  
3. **Consent verification** for sensitive or Indigenous data.  

---

## 🗂️ Directory Layout

```
docs/data/sources/
├── README.md                         # This file
├── usgs_historic_topo.json            # USGS topographic maps metadata
├── noaa_stations.json                 # NOAA climate and weather data
├── ks_dem.json                        # Kansas elevation / DEM datasets
├── fema_disasters.json                # FEMA disaster declarations
├── blm_land_patents.json              # BLM General Land Office records
└── kgs_geology.json                   # Kansas Geological Survey open data
```

---

## 🌐 Primary Data Sources

| Dataset ID | Source Organization | Description | Format | License | Governance Status |
|---|---|---|---|---|---|
| `usgs_historic_topo` | U.S. Geological Survey | Historical topographic maps (1850–1990). | GeoTIFF / STAC | Public Domain | ✅ Approved |
| `noaa_stations` | NOAA NCEI | Daily climate records from Kansas stations. | CSV / API | Public Domain | ✅ Approved |
| `ks_dem` | Kansas DASC | 1m DEM elevation data and LiDAR archives. | GeoTIFF | CC-BY 4.0 | ✅ Approved |
| `fema_disasters` | FEMA | Federal disaster declarations (1953–Present). | JSON / API | Public Domain | ✅ Approved |
| `blm_land_patents` | Bureau of Land Management | Federal land patent records (1850–1900). | CSV / Shapefile | Public Domain | ⚙️ Pending FAIR+CARE Review |
| `kgs_geology` | Kansas Geological Survey | State geologic and aquifer datasets. | GeoJSON / NetCDF | CC-BY 4.0 | ✅ Approved |
| `tribal_boundaries` | Bureau of Indian Affairs | Historic tribal boundaries in Kansas. | Shapefile / GeoJSON | Restricted (Cultural Data) | ⚠️ Restricted |
| `khs_archives` | Kansas Historical Society | Historical manuscripts, maps, and records. | PDF / OCR Text | Mixed (Open + Restricted) | ⚙️ Pending Review |

---

## 🧩 Source Metadata Fields

Each `.json` file follows the **KFM Data Source Schema**, providing structured metadata for reproducibility and catalog generation.

| Field | Type | Description | Example |
|---|---|---|---|
| `id` | string | Unique source ID. | `"noaa_stations"` |
| `title` | string | Human-readable name. | `"NOAA Kansas Climate Data"` |
| `description` | string | Summary of dataset contents. | `"Daily climate observations from NOAA NCEI."` |
| `source_org` | string | Responsible agency or institution. | `"NOAA NCEI"` |
| `license` | string | SPDX or Creative Commons license. | `"CC-BY-4.0"` |
| `format` | string | File type or delivery method. | `"CSV"` |
| `spatial` | object | Geographic coverage (WGS84 bbox). | `[-102.05, 37.0, -94.6, 40.0]` |
| `temporal` | object | Date range for dataset coverage. | `{"start": "1880-01-01", "end": "2025-01-01"}` |
| `endpoint` | object | API or download endpoint. | `{"type": "http", "url": "https://data.noaa.gov/api"}` |
| `provenance` | object | Source URL, authorship, consent notes. | `{ "creator": "NOAA", "consent": "Public Domain" }` |
| `faircare` | object | CARE metadata for ethical governance. | `{ "authority_to_control": "Open", "ethics": "No sensitive data" }` |
| `status` | string | Governance status. | `"approved"` |

---

## ⚖️ FAIR+CARE Alignment

All datasets undergo **FAIR+CARE evaluation** during integration:

| Principle | Verification |
|---|---|
| **Findable** | Indexed through STAC/DCAT JSON catalogs with persistent identifiers. |
| **Accessible** | API endpoints and data download URLs documented with access notes. |
| **Interoperable** | Standardized schema, CRS (EPSG:4326), and open formats. |
| **Reusable** | Clear licensing, provenance, and temporal metadata included. |
| **Collective Benefit** | Datasets contribute to open education, climate research, and history. |
| **Authority to Control** | Cultural data restricted unless consent explicitly granted. |
| **Responsibility** | Data updates monitored through CI/CD workflows. |
| **Ethics** | Datasets screened for bias, misrepresentation, or colonial framing. |

---

## 🧾 Data Source Lifecycle

| Stage | Description | Responsible Entity |
|---|---|---|
| **Proposal** | New source submitted for inclusion. | Data Standards Committee |
| **Validation** | Schema and metadata verified via CI. | Data QA Team |
| **Ethical Review** | FAIR+CARE Council checks consent and cultural flags. | Ethics Board |
| **Approval** | Added to registry and STAC/DCAT catalog. | Governance Committee |
| **Monitoring** | Quarterly revalidation and metadata refresh. | Data Stewardship Lead |

All data sources are versioned and logged in `telemetry/dataset-stats.json`.

---

## 🧮 Example Data Source JSON

```json
{
  "id": "noaa_stations",
  "title": "NOAA Kansas Historical Climate Stations",
  "description": "Daily precipitation and temperature data for Kansas, 1880–present.",
  "license": "CC-BY-4.0",
  "format": "CSV",
  "source_org": "NOAA NCEI",
  "endpoint": {
    "type": "api",
    "url": "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
  },
  "spatial": {
    "bbox": [-102.05, 37.0, -94.6, 40.0],
    "crs": "EPSG:4326"
  },
  "temporal": {
    "start": "1880-01-01",
    "end": "2025-01-01"
  },
  "provenance": {
    "creator": "NOAA",
    "issued": "2025-01-05T00:00:00Z",
    "consent": "Public Domain (US Government Data)"
  },
  "faircare": {
    "collective_benefit": "Supports climate resilience and environmental modeling.",
    "authority_to_control": "Open",
    "responsibility": "FAIR+CARE Council verified",
    "ethics": "No personally identifiable or cultural data."
  },
  "status": "approved"
}
```

---

## 🧠 Data Provenance & Version Control

Each source JSON is linked to:
- **STAC Items:** Spatial-temporal metadata (`data/stac/`)  
- **Data Contracts:** Schema conformance (`data/contracts/data-contract-v3.json`)  
- **Telemetry Logs:** Validation history (`data/telemetry/dataset-stats.json`)  
- **Governance Minutes:** Approval record (`data/governance/review-council-minutes.md`)  

This traceability guarantees full dataset lineage and ethical accountability.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | Data Standards & FAIR+CARE Council | Established unified registry for data sources with governance metadata, schema validation, and FAIR+CARE compliance tracking. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Data Index](../README.md) · [Contracts →](../contracts/README.md)

</div>