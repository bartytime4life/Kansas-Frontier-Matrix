---
title: "🌦️ Kansas Frontier Matrix — Climatology Methods Dataset Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/climatology/methods/datasets/metadata/README.md"
version: "v10.2.2"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/analyses-climatology-methods-datasets-metadata-v3.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climatology Methods Dataset Metadata Registry**
`docs/analyses/climatology/methods/datasets/metadata/README.md`

**Purpose:**  
Maintain the **FAIR+CARE-compliant metadata registry** for all climatology methods datasets within the Kansas Frontier Matrix (KFM).  
This metadata repository provides **provenance, interoperability, and validation documentation** for raw, processed, and derived datasets used in the climatology analytical framework.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Methods_Metadata-orange)](../../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Active_Registry-brightgreen)](../../../../../../releases/)
</div>

---

## 📘 Overview

The **Climatology Methods Metadata Registry** aligns dataset documentation with **STAC 1.0**, **DCAT 3.0**, **ISO 19115**, and **FAIR+CARE v3** frameworks.  
It captures dataset lineage, validation results, sustainability telemetry, and governance review notes for each climatology dataset used in modeling and trend analyses.

Each metadata record is:
- **Machine-readable (JSON-LD / XML)**  
- **Ethically validated** through the FAIR+CARE Council  
- **Linked to the Governance Ledger** for permanent provenance tracking  

---

## 🗂️ Directory Layout

```plaintext
docs/analyses/climatology/methods/datasets/metadata/
├── README.md                                  # This document
├── stac_catalog.json                          # STAC 1.0-compliant metadata catalog
├── dcat_metadata.json                         # DCAT 3.0-compatible metadata record
├── faircare_validation.json                   # FAIR+CARE and ISO validation results
├── provenance_log.json                        # Data lineage, transformations, and checksum registry
└── iso19115_summary.xml                       # ISO 19115-3 crosswalk metadata summary
```

---

## 🧩 Metadata Standards Alignment

| Standard | Function | Description | Validation Source |
|-----------|-----------|-------------|--------------------|
| **STAC 1.0** | Spatiotemporal asset cataloging | Defines spatial/temporal extent and data links | `stac_catalog.json` |
| **DCAT 3.0** | Dataset discovery and interoperability | Defines datasets, distributions, and provenance | `dcat_metadata.json` |
| **ISO 19115-3** | Geospatial dataset lineage & CRS | XML schema crosswalk for datasets | `iso19115_summary.xml` |
| **FAIR+CARE v3** | Ethical and sustainability metadata | Includes telemetry, energy, carbon, and access controls | `faircare_validation.json` |

---

## 📑 STAC Catalog Example Entry

```json
{
  "stac_version": "1.0.0",
  "type": "Item",
  "id": "prism-climate-monthly-kansas",
  "collection": "prism-monthly",
  "properties": {
    "description": "PRISM monthly temperature and precipitation averages for Kansas (1895–2025).",
    "license": "CC-BY 4.0",
    "datetime": "2025-11-01T00:00:00Z",
    "keywords": ["temperature", "precipitation", "PRISM", "Kansas"],
    "providers": [{"name": "PRISM Climate Group", "roles": ["producer", "licensor"]}],
    "extent": {
      "spatial": {"bbox": [[-102.05, 36.99, -94.6, 40.0]]},
      "temporal": {"interval": [["1895-01-01", "2025-11-01"]]}
    }
  },
  "assets": {
    "data": {
      "href": "https://prism.oregonstate.edu/",
      "type": "application/x-netcdf",
      "roles": ["data"]
    }
  }
}
```

---

## 📄 DCAT Metadata Example (CMIP6 Projections)

```json
{
  "@context": "https://www.w3.org/ns/dcat3.jsonld",
  "@type": "dcat:Dataset",
  "dct:title": "CMIP6 Downscaled Climate Projections (Kansas SSP2–4.5)",
  "dct:identifier": "cmip6-ssp45-kansas",
  "dct:issued": "2025-11-09",
  "dct:license": "CC-BY 4.0",
  "dcat:keyword": ["CMIP6", "climate projections", "SSP", "temperature", "precipitation"],
  "dcat:temporalResolution": "monthly",
  "dcat:spatialResolutionInMeters": 25000,
  "dcat:distribution": [{
    "dcat:accessURL": "https://data.kfm.dev/cmip6/ssp45_kansas.nc",
    "dct:format": "NetCDF"
  }],
  "dcat:contactPoint": {
    "vcard:fn": "KFM Climate Analysis Group",
    "vcard:hasEmail": "contact@kfm.dev"
  }
}
```

---

## ⚙️ FAIR+CARE Validation Record Example

```json
{
  "validation_id": "climatology-methods-metadata-2025-11-09-0091",
  "validated_datasets": [
    "PRISM Monthly",
    "Daymet Daily",
    "CMIP6 SSP Projections",
    "NOAA GHCN-Daily"
  ],
  "metadata_integrity": {
    "stac_schema": "Pass",
    "dcat_schema": "Pass",
    "iso19115_crosswalk": "Pass"
  },
  "energy_joules": 9.2,
  "carbon_gCO2e": 0.0040,
  "validation_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T15:18:00Z"
}
```

---

## ⚖️ FAIR+CARE Governance Matrix

| Principle | Implementation | Verification Source |
|------------|----------------|--------------------|
| **Findable** | UUID-linked metadata registered in STAC/DCAT catalogs | `stac_catalog.json` |
| **Accessible** | Metadata available via FAIR+CARE API and repository | FAIR+CARE Ledger |
| **Interoperable** | JSON-LD and XML formats support cross-domain use | `telemetry_schema` |
| **Reusable** | Provenance and license information embedded | `manifest_ref` |
| **Responsibility** | Energy/carbon usage logged per metadata validation | `telemetry_ref` |
| **Ethics** | Privacy and sensitive information reviewed per FAIR+CARE | Council Ethics Audit |

---

## 🧾 Governance Ledger Record Example

```json
{
  "ledger_id": "climatology-methods-metadata-ledger-2025-11-09-0092",
  "component": "Climatology Methods Metadata Registry",
  "files": [
    "stac_catalog.json",
    "dcat_metadata.json",
    "iso19115_summary.xml"
  ],
  "energy_joules": 9.2,
  "carbon_gCO2e": 0.0040,
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T15:20:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.2.2 | 2025-11-09 | FAIR+CARE Council | Published climatology methods metadata registry with FAIR+CARE and ISO 19115 compliance. |
| v10.2.1 | 2025-11-09 | Metadata & Governance Group | Added DCAT/STAC examples and telemetry metrics. |
| v10.2.0 | 2025-11-09 | KFM Climate Team | Created metadata documentation aligned with hydrology standards and governance ledger. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Climatology Methods Datasets](../README.md) · [Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

