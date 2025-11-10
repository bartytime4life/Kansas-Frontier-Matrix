---
title: "💧 Kansas Frontier Matrix — Hydrology TMP Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/work/tmp/hydrology/datasets/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/work-hydrology-tmp-datasets-v10.json"
governance_ref: "../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💧 Kansas Frontier Matrix — **Hydrology TMP Datasets**
`data/work/tmp/hydrology/datasets/README.md`

**Purpose:**  
Temporary **FAIR+CARE**-compliant repository for raw and normalized hydrological datasets prior to transformation and validation in the Kansas Frontier Matrix (KFM).  
This workspace enables controlled ETL staging of water-related datasets — **streamflow**, **aquifer levels**, **watershed boundaries**, and **precipitation indices** — with full provenance, **telemetry v2** sustainability metrics, and ethics traceability.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../docs/architecture/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Hydrology%20Datasets%20Certified-gold)](../../../../../docs/standards/faircare.md)
[![ISO 19115](https://img.shills.io/badge/ISO-19115%20Aligned-green)]()

</div>

---

## 📘 Overview

The **Hydrology TMP Datasets** directory houses short-lived raw and intermediate hydrological data used in active ETL and governance workflows.  
All entries are sourced from authoritative providers, normalized to KFM’s data contracts, registered in checksum manifests, and prepared for transformation and validation before promotion to staging.

**v10 Enhancements**

- Emission of **telemetry v2** per ingest batch (energy Wh, carbon gCO₂e, coverage %).  
- JSON-LD lineage anchors in `metadata.json` tying sources → TMP artifacts → ledger entries.  
- Strengthened pre-validation for CF and ISO crosswalks; continuous checksum reconciliation.

### Core Functions

- Ingest and stage hydrological data from trusted public sources (USGS, EPA, NIDIS, etc.).  
- Apply initial **schema normalization, CRS setup (EPSG 4326)**, and **FAIR+CARE** pre-audits.  
- Maintain **provenance and checksum** metadata for short-lived ETL activities.  
- Guarantee schema compliance and integrity prior to transformation and validation.

---

## 🗂️ Directory Layout

```plaintext
data/work/tmp/hydrology/datasets/
├── README.md                             # This file — overview of hydrology TMP datasets
│
├── groundwater_levels_tmp.csv            # Temporary groundwater measurement dataset (USGS)
├── streamflow_measurements_tmp.parquet   # Streamflow at gauging stations
├── aquifer_extent_tmp.geojson            # Aquifer boundaries (EPA / KGS)
├── watershed_boundaries_tmp.geojson      # Watershed polygons (HUC normalized)
└── metadata.json                         # Provenance, telemetry v2, and governance linkage
```

---

## ⚙️ Dataset Lifecycle Workflow

```mermaid
flowchart TD
    A["Raw Hydrology data raw hydrology"] --> B["Ingestion and Schema Normalization datasets"]
    B --> C["Checksum Verification and FAIR and CARE Pre Audit"]
    C --> D["Transformation and Reprojection transforms"]
    D --> E["Validation and Governance Registration validation"]
```

### Description

1. **Ingestion** — Load hydrological data from **USGS / EPA / NIDIS** into the TMP workspace.  
2. **Normalization** — Apply KFM field names, data types, and **EPSG 4326**; populate minimal ISO 19115 and FAIR+CARE metadata.  
3. **Audit** — Generate checksums and run **FAIR+CARE** pre-validation (licensing, accessibility, sensitivity).  
4. **Transformation** — Hand off to `data/work/tmp/hydrology/transforms/` for harmonization.  
5. **Governance** — Record lineage and hashes in `releases/v10.0.0/manifest.zip` and `data/reports/audit/data_provenance_ledger.json`.

---

## 🧩 Example Dataset Metadata Record

```json
{
  "id": "hydrology_tmp_datasets_v10.0.0",
  "source_files": [
    "data/raw/usgs/streamflow_measurements_2025.csv",
    "data/raw/epa/watershed_boundaries.geojson"
  ],
  "datasets_loaded": 4,
  "schema_compliance": 0.995,
  "checksum_verified": true,
  "fairstatus": "certified",
  "telemetry": { "energy_wh": 5.4, "carbon_gco2e": 6.1, "coverage_pct": 100 },
  "validator": "@kfm-hydro-data",
  "created": "2025-11-09T23:59:00Z",
  "governance_registered": true,
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## 🧠 FAIR+CARE Governance Matrix

| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | Indexed by source, dataset type, checksum, and cycle | `@kfm-data` |
| **Accessible** | Open CSV, Parquet, GeoJSON with license and access metadata | `@kfm-accessibility` |
| **Interoperable** | Normalized to STAC and DCAT, ISO 19115; CRS = EPSG 4326 | `@kfm-architecture` |
| **Reusable** | Provenance and checksum lineage enable reproducibility | `@kfm-design` |
| **Collective Benefit** | Supports sustainable hydrology and watershed planning | `@faircare-council` |
| **Authority to Control** | Council validates ingestion events and usage constraints | `@kfm-governance` |
| **Responsibility** | Hydrology maintainers perform schema and checksum vetting | `@kfm-security` |
| **Ethics** | Environmental and community sensitivity reviewed via FAIR+CARE | `@kfm-ethics` |

**Audit References:**  
`data/reports/audit/data_provenance_ledger.json` · `data/reports/fair/faircare.md`

---

## ⚙️ Key TMP Artifacts

| File | Description | Format |
|---|---|---|
| `groundwater_levels_tmp.csv` | Temporary groundwater observations | CSV |
| `streamflow_measurements_tmp.parquet` | Streamflow series for modeling | Parquet |
| `aquifer_extent_tmp.geojson` | Aquifer boundaries (intermediate) | GeoJSON |
| `watershed_boundaries_tmp.geojson` | HUC based watershed polygons | GeoJSON |
| `metadata.json` | Source, provenance, checksum, telemetry v2, and audit links | JSON |

**Automation:** `hydrology_tmp_dataset_sync_v2.yml`

---

## ⚖️ Retention & Provenance Policy

| Dataset Type | Retention Duration | Policy |
|---|---:|---|
| TMP Raw and Normalized | 7 Days | Auto purged after transform or validation |
| FAIR+CARE Audits | 180 Days | Retained for ethics certification |
| Metadata and Checksums | Permanent | Immutable under governance ledger |

---

## 🌱 Sustainability Metrics

| Metric | Value | Verified By |
|---|---:|---|
| Energy Use per TMP cycle | 5.4 Wh | `@kfm-sustainability` |
| Carbon Output | 6.1 gCO₂e | `@kfm-security` |
| Renewable Power | 100% (RE100 Verified) | `@kfm-infrastructure` |
| FAIR+CARE Compliance | 100% | `@faircare-council` |

**Telemetry:** `../../../../../releases/v10.0.0/focus-telemetry.json`

---

## 🧾 Citation

```text
Kansas Frontier Matrix (2025). Hydrology TMP Datasets (v10.0.0).
Temporary FAIR+CARE-compliant repository for hydrological ETL ingestion and normalization with checksum, JSON-LD lineage, and telemetry v2, aligned to MCP-DL v6.3 and ISO 19115.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-09 | `@kfm-hydro-data` | Upgraded to v10: telemetry v2, JSON-LD lineage anchors, reinforced CF and ISO pre-validation. |
| v9.7.0  | 2025-11-06 | `@kfm-hydro-data` | Telemetry schema added; governance and schema alignment refined. |
| v9.6.0  | 2025-11-03 | `@kfm-hydro-data` | Added checksum registry and FAIR+CARE audit integration for TMP datasets. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Hydrological Data × FAIR+CARE Ethics × Provenance Assurance*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Hydrology TMP](../README.md) · [Governance Charter](../../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>
