---
title: "📜 Kansas Frontier Matrix — Data Contracts & Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/contracts/README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-contracts-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Data Contracts & Schemas**
`docs/data/contracts/README.md`

**Purpose:**  
Define and standardize **data contracts, validation schemas, and provenance specifications** used across all ingestion and ETL pipelines of the **Kansas Frontier Matrix (KFM)**.  
These contracts guarantee interoperability, reproducibility, and **FAIR+CARE** ethical integrity across datasets and knowledge graph entities.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

**Data Contracts** serve as the foundation for **KFM’s ETL pipelines and knowledge graph ingestion**, providing explicit structure, validation, and ethical guarantees for every dataset.  
They are JSON Schema–compliant definitions that describe:
- Field names, data types, and validation rules  
- Provenance metadata and licensing  
- FAIR+CARE alignment and consent fields  
- Dataset versioning and linkage to STAC/DCAT catalogs  

Each data source integrated into KFM must conform to one of these contracts before being approved for ingestion.

---

## 🗂️ Directory Layout

```
docs/data/contracts/
├── README.md                      # This file
├── data-contract-v3.json           # Current KFM global data contract schema
├── metadata-schema.json            # Metadata structure for dataset-level fields
├── provenance-spec.json            # Provenance and consent data model
└── examples/
    ├── topo-map-contract-example.json
    ├── climate-data-contract-example.json
    └── focus-narrative-contract-example.json
```

---

## ⚙️ Contract Components

| Component | Description | Format |
|---|---|---|
| **Metadata Schema** | Defines dataset identity, title, license, spatial/temporal coverage. | JSON Schema |
| **Entity Contract** | Specifies entities, attributes, and relationships (Person, Place, Event). | JSON Schema / RDF |
| **Provenance Spec** | Captures dataset origin, author, consent, and lineage. | JSON-LD / PROV-O |
| **Ethical Use Fields** | FAIR+CARE extensions for consent and cultural control. | JSON Schema |
| **Validation Rules** | Data type, range, required/optional fields. | JSON Schema Draft 2020-12 |

---

## 🧩 Core Schema Fields (data-contract-v3.json)

| Field | Type | Description | Required |
|---|---|---|---|
| `id` | string | Unique dataset identifier (UUID or slug). | ✅ |
| `title` | string | Human-readable dataset name. | ✅ |
| `description` | string | Brief summary of dataset content. | ✅ |
| `license` | string | SPDX or Creative Commons identifier. | ✅ |
| `spatial` | object | Bounding box or region metadata (GeoJSON). | ✅ |
| `temporal` | object | Start/end ISO 8601 dates for dataset range. | ✅ |
| `schema_version` | string | Semantic version of applied data contract. | ✅ |
| `provenance` | object | Source, authorship, and consent metadata. | ✅ |
| `quality` | object | Data completeness, precision, and accuracy indicators. | — |
| `faircare` | object | FAIR+CARE ethical use metadata (below). | ✅ |

---

## ⚖️ FAIR+CARE Extensions (Embedded Fields)

| Field | Description | Example |
|---|---|---|
| `faircare.collective_benefit` | Describes intended community or societal benefit. | `"Supports open Kansas heritage research"` |
| `faircare.authority_to_control` | Specifies consent or ownership for Indigenous or personal data. | `"Controlled by Kaw Nation"` |
| `faircare.responsibility` | Declares stewardship and maintenance responsibilities. | `"FAIR+CARE Council"` |
| `faircare.ethics` | Notes cultural or contextual sensitivity. | `"Restricted images — cultural significance"` |

---

## 🔍 Provenance Specification (provenance-spec.json)

KFM follows **W3C PROV-O** and **PAV (Provenance, Authoring, Versioning)** standards.

| Field | Description | Example |
|---|---|---|
| `source_url` | Original data location or API endpoint. | `"https://www.ncei.noaa.gov/data/ghcn"` |
| `creator` | Dataset creator or institution. | `"NOAA NCEI"` |
| `contributor` | Secondary data handlers or KFM ingesters. | `"KFM ETL Team"` |
| `issued` | Publication date. | `"2025-04-02T00:00:00Z"` |
| `modified` | Last modified date. | `"2025-11-10T00:00:00Z"` |
| `license` | SPDX identifier for reuse. | `"CC-BY-4.0"` |
| `checksum` | SHA256 hash for verification. | `"6f9b23f..."` |
| `consent` | Declaration of ethical approval or cultural consent. | `"Approved under Kaw Nation data protocol"` |

---

## 🧾 Validation Workflows

| Workflow | Function | Output Artifact |
|---|---|---|
| `data-contract-validate.yml` | Validates dataset against JSON Schema. | `reports/data/schema-validation.json` |
| `data-provenance.yml` | Verifies lineage and consent fields. | `reports/data/provenance-summary.json` |
| `faircare-audit.yml` | Ensures ethical metadata fields are populated. | `reports/data/faircare-validation.json` |
| `data-quality.yml` | Measures completeness, accuracy, and consistency. | `reports/data/completeness.json` |

---

## 🧠 Example Contract — Climate Data

```json
{
  "id": "noaa_ks_climate_1880_2025",
  "title": "NOAA Kansas Historical Climate Observations",
  "license": "CC-BY-4.0",
  "description": "Daily temperature and precipitation data across Kansas (1880–2025).",
  "spatial": { "bbox": [-102.05, 37.0, -94.6, 40.0] },
  "temporal": { "start": "1880-01-01", "end": "2025-01-01" },
  "provenance": {
    "source_url": "https://www.ncei.noaa.gov/",
    "creator": "NOAA NCEI",
    "issued": "2025-01-05T00:00:00Z",
    "consent": "Public domain — U.S. Government data."
  },
  "faircare": {
    "collective_benefit": "Supports climate and agriculture resilience research.",
    "authority_to_control": "Open government dataset — unrestricted.",
    "responsibility": "Maintained by KFM ETL team.",
    "ethics": "No personal data or sensitive locations included."
  }
}
```

---

## 📊 Data Contract Versioning & Governance

| Version | Type | Effective Date | Governance Body |
|---|---|---|---|
| **v1.0** | Initial | 2023-01-10 | KFM Data Standards Team |
| **v2.0** | FAIR integration | 2024-03-25 | FAIR Council |
| **v3.0** | FAIR+CARE expansion + consent schema | 2025-07-01 | FAIR+CARE Council |

All new data contracts require **FAIR+CARE Council** and **Governance Committee** approval before deployment.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | Data Engineering & FAIR+CARE Council | Established complete data contract documentation, including schema, provenance, and validation workflows. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Data Index](../README.md) · [Provenance Spec →](provenance-spec.json)

</div>