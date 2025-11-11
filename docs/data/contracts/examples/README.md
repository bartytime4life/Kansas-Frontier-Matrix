---
title: "🧩 Kansas Frontier Matrix — Data Contract Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/contracts/examples/README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-contract-examples-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Data Contract Examples**
`docs/data/contracts/examples/README.md`

**Purpose:**  
Provide canonical **examples of dataset contracts** implemented across domains in the **Kansas Frontier Matrix (KFM)**, demonstrating proper schema usage, provenance linkage, and **FAIR+CARE-compliant** metadata for ingestion and governance workflows.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

These examples illustrate how real datasets conform to the **KFM Data Contract v3.0**.  
Each file below serves as a reproducible reference for defining **spatial, temporal, provenance, and ethical metadata** under the Master Coder Protocol (MCP v6.3).

All examples are:
- **JSON Schema–compliant**  
- **FAIR+CARE-audited**  
- **STAC/DCAT compatible**  
- Mapped to **Neo4j entity types** (Person, Place, Event, Dataset)

---

## 🗂️ Directory Layout

```
docs/data/contracts/examples/
├── README.md                              # This file
├── topo-map-contract-example.json          # Historical map ingestion example
├── climate-data-contract-example.json      # Climate & environmental records
└── focus-narrative-contract-example.json   # AI narrative content & consent
```

---

## 🧭 Example 1 — Topographic Map Contract

**File:** `topo-map-contract-example.json`

Represents integration of **USGS historical topographic maps**.

```json
{
  "id": "usgs_historic_topo_1894",
  "title": "USGS Historical Topographic Map (Ellsworth County, 1894)",
  "description": "Digitized 1894 USGS topographic survey of Ellsworth County, Kansas.",
  "license": "Public Domain",
  "schema_version": "v3.0.0",
  "spatial": {
    "bbox": [-99.5, 38.3, -98.8, 38.9],
    "crs": "EPSG:4326"
  },
  "temporal": {
    "start": "1894-01-01",
    "end": "1894-12-31"
  },
  "provenance": {
    "source_url": "https://www.usgs.gov/historical-topo",
    "creator": "U.S. Geological Survey",
    "issued": "1894-03-15",
    "consent": "Public domain (U.S. Government data)"
  },
  "faircare": {
    "collective_benefit": "Preserves environmental and cartographic heritage of Kansas.",
    "authority_to_control": "Open",
    "responsibility": "Data Engineering & FAIR+CARE Council",
    "ethics": "Culturally neutral archival content"
  }
}
```

---

## 🌦️ Example 2 — Climate Dataset Contract

**File:** `climate-data-contract-example.json`

Represents ingestion of **NOAA Kansas Historical Climate Data**.

```json
{
  "id": "noaa_ks_climate_1880_2025",
  "title": "NOAA Kansas Historical Climate Observations (1880–2025)",
  "description": "Aggregated temperature, precipitation, and drought indices for Kansas from 1880 to 2025.",
  "license": "CC-BY-4.0",
  "schema_version": "v3.0.0",
  "spatial": {
    "bbox": [-102.05, 37.0, -94.6, 40.0],
    "crs": "EPSG:4326"
  },
  "temporal": {
    "start": "1880-01-01",
    "end": "2025-01-01"
  },
  "provenance": {
    "source_url": "https://www.ncei.noaa.gov/",
    "creator": "NOAA NCEI",
    "issued": "2025-01-05T00:00:00Z",
    "modified": "2025-11-05T00:00:00Z",
    "consent": "Public Domain (U.S. Government data)"
  },
  "faircare": {
    "collective_benefit": "Supports environmental resilience research and historical climatology.",
    "authority_to_control": "Open",
    "responsibility": "NOAA / KFM Data Governance Team",
    "ethics": "No personal or sensitive data"
  }
}
```

---

## 🧠 Example 3 — Focus Narrative Contract

**File:** `focus-narrative-contract-example.json`

Defines **AI-generated narrative datasets** from Focus Mode v2 with ethical consent and provenance validation.

```json
{
  "id": "focus_narratives_2025Q2",
  "title": "Kansas Frontier Matrix — Focus Mode Narrative Outputs (Q2 2025)",
  "description": "AI-generated summaries and contextual narratives linking people, places, and events within the Kansas Frontier Matrix.",
  "license": "CC-BY-4.0",
  "schema_version": "v3.0.0",
  "temporal": {
    "start": "2025-04-01",
    "end": "2025-06-30"
  },
  "provenance": {
    "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
    "creator": "KFM AI Systems Team",
    "issued": "2025-06-15",
    "consent": "Generated from publicly available and consented archives",
    "checksum": "91b9a8b62f8..."
  },
  "faircare": {
    "collective_benefit": "Enhances accessibility of Kansas history through adaptive AI narratives.",
    "authority_to_control": "FAIR+CARE Ethics Board",
    "responsibility": "FAIR+CARE Council and AI Governance Team",
    "ethics": "Validated for neutral tone, inclusive language, and factual transparency."
  }
}
```

---

## ⚙️ Validation Workflow

| Workflow | Validation Task | Output |
|---|---|---|
| `data-contract-validate.yml` | Ensures schema conformance for all example contracts. | `reports/data/schema-validation.json` |
| `faircare-audit.yml` | Validates ethical fields within each example contract. | `reports/data/faircare-validation.json` |
| `data-provenance.yml` | Checks lineage fields and consent metadata. | `reports/data/provenance-summary.json` |
| `data-quality.yml` | Measures completeness and metadata density. | `reports/data/completeness.json` |

All examples are validated continuously via CI/CD and referenced in public governance documentation.

---

## ⚖️ FAIR+CARE Assurance

Each example contract has passed internal **FAIR+CARE Council audit**, confirming:
- ✅ Clear provenance and consent documentation  
- ✅ Schema conformance to `data-contract-v3.json`  
- ✅ Ethical usage of historical, environmental, or AI-generated data  
- ✅ Reproducibility and traceability under MCP standards  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | FAIR+CARE Data Governance Team | Added standard dataset contract examples for topographic, climate, and AI narrative datasets under v3.0 contract schema. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Data Contracts](../README.md) · [Provenance Spec →](../provenance-spec.json)

</div>