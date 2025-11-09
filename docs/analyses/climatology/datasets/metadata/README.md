---
title: "🌦️ Kansas Frontier Matrix — Climatology Dataset Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/climatology/datasets/metadata/README.md"
version: "v10.2.2"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/analyses-climatology-datasets-metadata-v3.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climatology Dataset Metadata Registry**
`docs/analyses/climatology/datasets/metadata/README.md`

**Purpose:**  
Maintain the **metadata registry** for all climatology datasets (raw, processed, and derived) within the Kansas Frontier Matrix (KFM).  
This repository enforces standardized **STAC/DCAT 3.0**, **ISO 19115**, and **FAIR+CARE v3** documentation schemas to ensure transparency, interoperability, and sustainability compliance across all climate-related analyses.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Metadata-orange)](../../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Active_Registry-brightgreen)](../../../../../../releases/)
</div>

---

## 📘 Overview

The **Climatology Metadata Registry** ensures that every dataset integrated into the Kansas Frontier Matrix is **discoverable**, **traceable**, and **reusable** under FAIR+CARE and ISO-certified governance.  
Each metadata entry provides dataset provenance, licensing, spatial–temporal coverage, and telemetry linkage for sustainability tracking.  

All entries follow **machine-readable JSON-LD** format, registered under both **STAC (SpatioTemporal Asset Catalog)** and **DCAT (Data Catalog Vocabulary)** standards.

---

## 🗂️ Directory Layout

```plaintext
docs/analyses/climatology/datasets/metadata/
├── README.md                                  # This document
├── stac_catalog.json                          # STAC 1.0 collection of all climatology datasets
├── dcat_metadata.json                         # DCAT 3.0 equivalent metadata representation
├── faircare_validation.json                   # FAIR+CARE validation metrics and audit results
├── provenance_log.json                        # Dataset provenance and checksum registry
└── iso19115_summary.xml                       # ISO 19115-3 metadata crosswalk
```

---

## 🧩 Metadata Schema Alignment

| Standard | Function | Schema Reference |
|-----------|-----------|------------------|
| **STAC 1.0.0** | Geospatial dataset indexing and temporal cataloging | `metadata/stac_catalog.json` |
| **DCAT 3.0** | Dataset discovery and distribution metadata | `metadata/dcat_metadata.json` |
| **ISO 19115-3** | Geospatial metadata (spatial reference, lineage) | `metadata/iso19115_summary.xml` |
| **FAIR+CARE v3** | Ethical and sustainability metadata | `metadata/faircare_validation.json` |

---

## 📑 STAC Example — NOAA GHCN-Daily Entry

```json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "noaa-ghcn-daily",
  "title": "NOAA Global Historical Climatology Network - Daily (Kansas Subset)",
  "extent": {
    "spatial": {"bbox": [[-102.05, 36.99, -94.6, 40.0]]},
    "temporal": {"interval": [["1880-01-01T00:00:00Z", "2025-01-01T00:00:00Z"]]}
  },
  "license": "Public Domain",
  "keywords": ["climate", "precipitation", "temperature", "Kansas"],
  "providers": [
    {"name": "NOAA NCEI", "roles": ["producer", "licensor"]}
  ],
  "links": [
    {"rel": "self", "href": "stac_catalog.json"},
    {"rel": "alternate", "href": "dcat_metadata.json", "type": "application/json"}
  ]
}
```

---

## 📄 DCAT Example — CMIP6 Projections Dataset

```json
{
  "@context": "https://www.w3.org/ns/dcat3.jsonld",
  "@type": "dcat:Dataset",
  "dct:title": "CMIP6 Downscaled Climate Projections for Kansas",
  "dct:identifier": "cmip6-ssp-dataset-ks",
  "dct:issued": "2025-11-09",
  "dct:license": "CC-BY 4.0",
  "dcat:keyword": ["CMIP6", "projections", "temperature", "precipitation"],
  "dct:spatial": {
    "@type": "dct:Location",
    "locn:geometry": "{\"type\": \"Polygon\", \"coordinates\": [[[-102.05,36.99],[-94.6,36.99],[-94.6,40.0],[-102.05,40.0],[-102.05,36.99]]] }"
  },
  "dcat:distribution": [{
    "dcat:accessURL": "https://data.kfm.dev/cmip6_projections.nc",
    "dct:format": "NetCDF"
  }],
  "dcat:temporalResolution": "monthly",
  "dcat:startDate": "2015-01-01",
  "dcat:endDate": "2100-12-31"
}
```

---

## ⚙️ FAIR+CARE Validation Example

```json
{
  "validation_id": "climatology-metadata-2025-11-09-0032",
  "datasets_validated": [
    "NOAA GHCN-Daily",
    "PRISM Monthly",
    "NASA Daymet V4",
    "CMIP6 Projections"
  ],
  "metadata_checks": {
    "stac_schema": "Pass",
    "dcat_schema": "Pass",
    "iso_crosswalk": "Pass",
    "faircare_integrity": "Pass"
  },
  "energy_joules": 9.7,
  "carbon_gCO2e": 0.0041,
  "validation_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T14:20:00Z"
}
```

---

## ⚖️ FAIR+CARE & ISO Governance Matrix

| Principle | Implementation | Verification Source |
|------------|----------------|--------------------|
| **Findable** | STAC/DCAT catalog entries with UUIDs | `stac_catalog.json` |
| **Accessible** | Metadata publicly available via GitHub & API | FAIR+CARE Ledger |
| **Interoperable** | JSON-LD, XML, and RDF compatibility | `telemetry_schema` |
| **Reusable** | Provenance and validation logs attached | `provenance_log.json` |
| **Responsibility** | Telemetry metrics tracked per validation | `telemetry_ref` |
| **Ethics** | Metadata reviewed for privacy & indigenous considerations | FAIR+CARE Council Review |

---

## 🧾 Governance Ledger Record Example

```json
{
  "ledger_id": "climatology-metadata-ledger-2025-11-09-0033",
  "component": "Climatology Metadata Registry",
  "files": [
    "stac_catalog.json",
    "dcat_metadata.json",
    "iso19115_summary.xml"
  ],
  "energy_joules": 9.7,
  "carbon_gCO2e": 0.0041,
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T14:23:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.2.2 | 2025-11-09 | FAIR+CARE Council | Published full climatology metadata registry with STAC/DCAT/ISO/FAIR+CARE validation. |
| v10.2.1 | 2025-11-09 | KFM Metadata Group | Added JSON-LD crosswalk examples and governance ledger linkage. |
| v10.2.0 | 2025-11-09 | Climatology Analysis Team | Initial creation of metadata registry structure for climatology datasets. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Climatology Datasets](../README.md) · [Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

