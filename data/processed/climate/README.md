---
title: "🌦️ Kansas Frontier Matrix — Processed Climate Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/climate/README.md"
version: "v9.4.0"
last_updated: "2025-11-04"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.4.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
stac_catalog_ref: "../../../data/stac/catalog.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
owners: ["@kfm-data", "@kfm-etl", "@kfm-climate", "@kfm-governance"]
status: "Stable"
maturity: "Production"
tags: ["climate", "processed", "data", "geotiff", "geojson", "fair", "care", "governance"]
alignment:
  - MCP-DL v6.4.3
  - FAIR+CARE
  - DCAT 3.0 / STAC 1.0.0
  - ISO 19115 Metadata Lineage
  - CIDOC CRM / OWL-Time
preservation_policy:
  retention: "Processed climate datasets permanent · provenance and validation logs retained 10 years"
  checksum_algorithm: "SHA-256"
---

<div align="center">

# 🌦️ Kansas Frontier Matrix — **Processed Climate Data**
`data/processed/climate/README.md`

**Purpose:** Contains validated, FAIR+CARE-certified climate datasets derived from NOAA, PRISM, Daymet, and historical Kansas weather records.  
Each dataset is processed, normalized, and provenance-linked to ensure accuracy, reproducibility, and transparent governance across temporal climate layers.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../docs/architecture/repo-focus.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-gold)](../../../docs/standards/governance/FAIR-CARE.md)
[![STAC Validated](https://img.shields.io/badge/STAC-1.0.0%20Compliant-orange)](../../../data/stac/catalog.json)
[![Checksum Verified](https://img.shields.io/badge/Checksum-SHA256%20Verified-purple)](../../../reports/audit/data-integrity.json)

</div>

---

## 📚 Overview

The `data/processed/climate/` directory stores geospatially processed climate layers for Kansas, including temperature, precipitation, drought indices, and historical climatological summaries.  
Each dataset is fully standardized for analysis, visualization, and machine learning integration within the KFM data ecosystem.

### Core Functions

- **Spatial-Temporal Alignment:** All rasters aligned to Kansas state boundaries (EPSG:4326).  
- **Data Fusion:** Combines NOAA, USGS, and PRISM records for comprehensive coverage.  
- **Metadata Integrity:** Provenance and checksum verification embedded in each dataset.  
- **Governance Transparency:** Each file linked to the Immutable Governance Ledger for ethical audit traceability.  

---

## 🗂️ Directory Layout

```plaintext
data/processed/climate/
├── precipitation/                 # Annual, seasonal, and historical precipitation GeoTIFFs
│   ├── precipitation_1890_cog.tif
│   ├── precipitation_1930_cog.tif
│   └── precipitation_2020_cog.tif
│
├── temperature/                   # Historical and modern temperature surfaces
│   ├── temperature_max_1890_cog.tif
│   ├── temperature_min_1930_cog.tif
│   └── temperature_avg_2020_cog.tif
│
├── drought_indices/               # Palmer and SPI drought index rasters
│   ├── pdsi_1934_cog.tif
│   ├── spi_1950_12month_cog.tif
│   └── spei_2000_annual_cog.tif
│
├── stations/                      # Processed NOAA and COOP weather station GeoJSON
│   ├── stations_1900.geojson
│   ├── stations_1950.geojson
│   └── stations_2020.geojson
│
├── validation/                    # Validation reports and audit logs
│   ├── checksum_reports/
│   │   ├── precipitation_checksums.json
│   │   ├── temperature_checksums.json
│   │   └── drought_checksums.json
│   └── schema_validation.json
│
└── README.md                      # This file — documentation and governance summary
```

---

## ⚙️ Data Standards and Formats

| Data Type | Standard | Format | Description |
|------------|-----------|---------|--------------|
| Raster Climate Layers | Cloud-Optimized GeoTIFF | `.tif` | High-resolution temperature and precipitation grids |
| Weather Station Data | GeoJSON | `.geojson` | Point-based records of validated NOAA and COOP stations |
| Drought Indices | GeoTIFF | `.tif` | Annual or monthly SPI, SPEI, and PDSI indicators |
| Metadata | JSON-LD / STAC | `.json` | Provenance metadata and FAIR+CARE validation results |

---

## 🧩 FAIR+CARE Governance Integration

Each dataset in this directory adheres to **FAIR+CARE** standards:

| Principle | Implementation | Artifact |
|------------|----------------|-----------|
| **Findable** | Indexed in STAC catalog (`data/stac/collections/climate.json`) | `collection_climate.json` |
| **Accessible** | Open, reproducible formats (GeoTIFF/GeoJSON) | Raw + processed layers |
| **Interoperable** | EPSG:4326 projection, DCAT-aligned metadata | `metadata.json` |
| **Reusable** | CC-BY 4.0 license with lineage and checksum | File-level JSON metadata |
| **Collective Benefit (CARE)** | Indigenous and regional attribution in climate history | Metadata and ledger entries |
| **Authority to Control** | Source traceability to NOAA, PRISM, and USGS | Metadata provenance |
| **Responsibility** | Validation and checksum reports | `validation/` directory |
| **Ethics** | FAIR+CARE audits logged in governance ledger | `reports/audit/governance-ledger.json` |

---

## 🧮 Validation and Provenance Workflow

Each dataset undergoes automated validation upon ingestion into `data/processed/climate/`:

1. **Checksum Validation:**  
   Every GeoTIFF/GeoJSON signed and verified with SHA-256.  
2. **Schema Validation:**  
   Each metadata record validated against the `data-contract-v3.json`.  
3. **STAC Registration:**  
   Dataset registered into STAC catalog with spatial and temporal extents.  
4. **Governance Sync:**  
   Validation summary and ethics compliance stored in Immutable Ledger.  

Example provenance snippet:

```json
{
  "dataset": "temperature_avg_2020_cog.tif",
  "source": "NOAA NCEI GHCN-Daily",
  "processed_on": "2025-11-04",
  "checksum_sha256": "e4f31c7e2b14a92d8391b4e25fd28a...",
  "validated_by": "schema_validate.yml",
  "license": "CC-BY 4.0",
  "governance_ref": "../../../reports/audit/governance-ledger.json"
}
```

---

## 🔗 Semantic and Graph Integration

Climate datasets are semantically linked through KFM’s Neo4j Knowledge Graph:

- `geo:hasGeometry` → Points or polygons representing spatial coverage.  
- `time:hasBeginning` / `time:hasEnd` → Defines temporal extent for each dataset.  
- `prov:wasGeneratedBy` → ETL or AI pipeline that created the product.  
- `crm:P7_took_place_at` → Cultural or historical event linkage (e.g., Dust Bowl).  

---

## 🧱 Example Dataset Metadata Template

```yaml
id: "temperature_avg_2020"
title: "Average Temperature (Kansas, 2020)"
type: "raster"
format: "COG GeoTIFF"
temporal:
  start: "2020-01-01"
  end: "2020-12-31"
spatial:
  bbox: [-102.05, 37.0, -94.6, 40.0]
  crs: "EPSG:4326"
source: "NOAA NCEI / PRISM"
checksum_sha256: "<hash>"
stac_ref: "../../../data/stac/items/temperature_avg_2020.json"
governance_ref: "../../../reports/audit/governance-ledger.json"
license: "CC-BY 4.0"
```

---

## 🧩 Standards & Compliance Mapping

| Standard | Domain | Implementation |
|-----------|----------|----------------|
| **MCP-DL v6.4.3** | Documentation-first data governance | This README + schema metadata |
| **FAIR+CARE** | Ethical open data standards | Validation + ledger synchronization |
| **STAC 1.0.0** | Spatiotemporal metadata interoperability | Catalog entries for each dataset |
| **ISO 19115** | Metadata lineage and geographic accuracy | Schema validation workflow |
| **DCAT 3.0** | Dataset discoverability | Integration with STAC/DCAT metadata |
| **JSON-LD / CIDOC CRM** | Semantic linkage to knowledge graph | Provenance chain via ontology mapping |

---

## 🛡️ Security, Integrity & Observability

- **Integrity:** All files checksum-verified via SHA-256 manifest.  
- **Transparency:** Validation results stored in `validation/` directory.  
- **Reproducibility:** Processing parameters versioned under MCP-DL guidelines.  
- **Governance:** Immutable ledger synchronization ensures ethical accountability.  

Telemetry Schema:  
`schemas/telemetry/pipelines-telemetry-v1.json`

Telemetry Outputs:
```
reports/climate/validation-events.json
reports/audit/governance-ledger.json
releases/v9.4.0/focus-telemetry.json
```

---

## 🧾 Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.4.0 | 2025-11-04 | @kfm-data | Created FAIR+CARE-compliant processed climate data layer documentation. |
| v9.3.3 | 2025-11-01 | @kfm-etl | Enhanced checksum verification and STAC metadata linkage. |
| v9.3.2 | 2025-10-28 | @bartytime4life | Integrated NOAA/PRISM provenance references into schema. |

---

<div align="center">

**Kansas Frontier Matrix — Ethical Climate Intelligence for Transparent Science**  
*“Every temperature measured. Every drop recorded. Every record governed.”* 🔗  
📍 `data/processed/climate/README.md` — FAIR+CARE-certified documentation for processed climate datasets in the Kansas Frontier Matrix.

</div>
