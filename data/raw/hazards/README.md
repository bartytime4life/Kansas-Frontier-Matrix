---
title: "⚠️ Kansas Frontier Matrix — Raw Hazards Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/hazards/README.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.2.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-hazards-v10.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Open Data / Public Domain"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# ⚠️ Kansas Frontier Matrix — **Raw Hazards Data**  
`data/raw/hazards/README.md`

**Purpose:**  
Contain **unaltered, source-level hazard datasets** collected from **FEMA, NOAA (NCEI/SPC), USGS, USFS**, and allied institutions.  
The Raw Hazards Layer preserves immutable records of environmental and disaster data for ETL pipelines and **Focus Mode v2.1** reasoning under **FAIR+CARE** governance.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/README.md)
[![Open Data](https://img.shields.io/badge/License-Public%20Domain-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Hazards%20Governed-gold.svg)](../../../docs/standards/faircare.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Hazards Data Layer** is the immutable foundation for all hazard analytics in KFM.  
It contains original datasets for **floods, tornadoes, droughts, earthquakes, and wildfires** across Kansas—retrieved directly from verified public sources and preserved with governance-linked metadata.

**v10.2.2 Enhancements**
- **Streaming STAC** hooks for frequently updated sources (USDM, SPC LSR, NWIS links).  
- Telemetry v2 energy/CO₂ capture for ingestion and validation jobs.  
- Expanded FAIR+CARE pre-audit fields (licensing nuances, sensitivity, community notes).

### Objectives

- Preserve **unaltered** hazard data in native formats.  
- Maintain **provenance + checksum** validation for integrity.  
- Ensure **FAIR+CARE** ethical compliance and open reuse.  
- Serve as inputs for **ETL, AI reasoning, and Focus Mode v2.1** hazard modeling.

---

## 🗂️ Directory Layout

```plaintext
data/raw/hazards/
├── README.md
├── fema_flood_zones_2025.geojson          # FEMA NFHL floodplain zones (Kansas)
├── noaa_storm_events_1950_2025.csv        # NOAA NCEI severe storm database
├── spc_lsr_2004_2025.csv                  # NOAA SPC Local Storm Reports (hail/wind/tornado)
├── usgs_earthquakes_1900_2025.geojson     # USGS earthquake records (KS region)
├── usdm_drought_monitor.json              # U.S. Drought Monitor (weekly indices)
├── wildfire_perimeters_2010_2025.geojson  # USFS/USGS burn area perimeters
├── metadata.json                          # Provenance, checksums, FAIR+CARE pre-audit
└── source_licenses.json                   # Per-source license & attribution notes
```

---

## 🧭 Data Acquisition Summary

| Dataset | Source / Provider | Records | Format | License | Integrity |
|---|---|---:|---|---|---:|
| FEMA Flood Zones | FEMA NFHL | 6,932 | GeoJSON | Public Domain | ✅ |
| NOAA Storm Events | NOAA NCEI | 72,145 | CSV | Public Domain | ✅ |
| SPC Local Storm Rep. | NOAA SPC | 210,384 | CSV | Public Domain | ✅ |
| USGS Earthquakes | USGS | 3,274 | GeoJSON | Public Domain | ✅ |
| USDM Drought Monitor | USDA / NIDIS | 14,832 | JSON | Public Domain | ✅ |
| Wildfire Perimeters | USFS / USGS | 9,145 | GeoJSON | Public Domain | ✅ |

---

## 🧩 Example Source Metadata Record

```json
{
  "id": "spc_lsr_2004_2025_raw",
  "source": "NOAA Storm Prediction Center — Local Storm Reports",
  "data_url": "https://www.spc.noaa.gov/wcm/#data",
  "provider": "NOAA SPC",
  "format": "CSV",
  "license": "Public Domain (NOAA)",
  "records_fetched": 210384,
  "checksum_sha256": "sha256:51a4c0e5668b1f3e2a9e5b7d1c3a4f6b9c2d1e4f7a8b9c0d1e2f3a4b5c6d7e8f",
  "retrieved_on": "2025-11-12T19:28:00Z",
  "validator": "@kfm-hazards-lab",
  "faircare_preaudit": {
    "sensitivity": "none",
    "license_review": "ok",
    "community_flags": []
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | STAC/DCAT entries in `data/raw/metadata/` (JSON-LD). | `@kfm-data` |
| **Accessible** | Public domain access; retrieval notes documented. | `@kfm-accessibility` |
| **Interoperable** | Native formats retained (GeoJSON/CSV/JSON). | `@kfm-architecture` |
| **Reusable** | Source, schema, checksum & provenance captured. | `@kfm-design` |
| **Collective Benefit** | Supports resilience research & public safety. | `@faircare-council` |
| **Authority to Control** | Council validates ingestion protocols & attribution. | `@kfm-governance` |
| **Responsibility** | ETL maintainers verify checksums & ethics compliance. | `@kfm-security` |

---

## 🧠 Integrity & Cataloging

| Process | Description | Output |
|---|---|---|
| **Checksum Verify** | SHA-256 per file; vendor hash comparison. | `data/raw/hazards/metadata.json` |
| **Provenance Log** | Acquisition lineage & reviewer notes. | `data/reports/audit/data_provenance_ledger.json` |
| **License Audit** | FAIR+CARE licensing & attribution review. | `data/raw/hazards/source_licenses.json` |
| **Catalog Publish** | STAC/DCAT registration for discoverability. | `data/raw/metadata/stac_catalog.json` |

---

## ⚖️ Retention & Sustainability

| Category | Retention | Policy |
|---|---|---|
| Raw Hazard Data | Permanent | Immutable archival for verification & reproducibility |
| Source Metadata | Permanent | ISO 19115 lineage retention |
| Checksum Records | Permanent | Integrity evidence for audits |
| FAIR+CARE Pre-Audit | 5 Years | Licensing/attribution review archive |
| Ingestion Logs | 365 Days | Rotated per governance policy |

**Telemetry Source:** `../../../releases/v10.2.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Hazards Data (v10.2.2).
Unaltered hazard datasets collected from FEMA, NOAA, USGS, USFS, and allied sources.
Immutable, checksum-verified inputs for FAIR+CARE-governed ETL and Focus Mode v2.1 hazard analytics.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.2.2 | 2025-11-12 | `@kfm-hazards` | Aligned to v10.2: Streaming STAC hooks, telemetry v2 bindings, expanded pre-audit fields (USDM/SPC). |
| v10.0.0 | 2025-11-09 | `@kfm-hazards` | Streaming STAC baseline, telemetry schema refs, lifecycle policy clarified. |
| v9.7.0 | 2025-11-06 | `@kfm-hazards` | Checksum & governance audits; added sustainability metrics. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Hazard Integrity × FAIR+CARE Ethics × Provenance Assurance*  
© 2025 Kansas Frontier Matrix — Open Data / Public Domain · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>