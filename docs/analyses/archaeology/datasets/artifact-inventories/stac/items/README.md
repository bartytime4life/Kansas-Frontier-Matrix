---
title: "📄 Kansas Frontier Matrix — Artifact Inventory STAC Items (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/items/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-stac-items-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Items Index"
intent: "artifact-inventory-stac-items"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📄 **Kansas Frontier Matrix — Artifact Inventory STAC Items**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/items/README.md`

**Purpose:**  
Provide the **canonical index** of all **STAC Items** describing artifact inventory datasets in the Kansas Frontier Matrix (KFM).  
These STAC Items represent machine-readable metadata for cleaned, culturally reviewed inventories located under:

- `inventories/`  
- `metadata/`  
- `provenance/`  

All items comply with **STAC 1.0**, **DCAT 3.0**, **CIDOC-CRM**, **GeoSPARQL**, **PROV-O**, **KFM archaeology extensions**, and **FAIR+CARE sensitivity rules**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../../standards/faircare.md)  
[![License](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../../LICENSE)  
[![Status](https://img.shields.io/badge/Status-Active-success)](../../../../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

This directory contains **STAC Items**, each representing a single artifact inventory dataset.  
These files:

- Provide spatial, temporal, cultural, and provenance metadata  
- Enable machine discovery via STAC crawlers and KFM’s metadata engine  
- Govern dataset ingestion into Neo4j and AI/ETL pipelines  
- Enforce CARE sensitivity controls  
- Guarantee reproducibility and transparent lineage  

Every STAC Item **must** link to:

- Its dataset file in `inventories/`  
- Its metadata file in `metadata/`  
- Its provenance file in `provenance/`  
- Its parent STAC Collection in `../collections/`  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/items/
├── README.md                         # This file
├── flint-hills-lithics-v1.json       # Lithic artifact STAC Item
├── prairie-ceramics-v1.json          # Ceramic artifact STAC Item
├── contact-era-metals-v1.json        # Protohistoric metal artifacts (pending review)
├── fauna-open-v1.json                # Public-domain faunal dataset STAC Item
└── templates/                        # STAC Item templates for new datasets
~~~

---

## 🧭 Requirements for All STAC Items

Every STAC Item in this directory **must meet all** of the following specifications:

### ✔ STAC Core Fields

| Field | Requirement |
|---|---|
| `id` | Stable dataset identifier (matching file stem) |
| `stac_version` | `"1.0.0"` |
| `type` | `"Feature"` |
| `bbox` | Generalized bounding box (H3-derived) |
| `geometry` | `MultiPoint` or simplified polygon only |
| `properties.start_datetime` | Cultural-phase start date (if applicable) |
| `properties.end_datetime` | Cultural-phase end date |
| `assets.data.href` | Link to inventory CSV |
| `links.collection` | Must point to parent collection JSON |

### ✔ KFM Archaeology Extension (`kfm:*`)

| Field | Description |
|---|---|
| `kfm:phase` | Cultural-phase label |
| `kfm:datatype` | `"artifact-inventory"` |
| `kfm:source` | Data source institution |
| `kfm:provenance` | Path to PROV-O log |
| `kfm:material_class` | `"lithic"`, `"ceramic"`, `"metal"`, `"faunal"` |

### ✔ CARE Sensitivity Extension (`care:*`)

| Field | Allowed Values | Notes |
|---|---|---|
| `care:sensitivity` | `general`, `generalized` | Must match spatial generalization level |
| `care:review` | `"faircare"`, `"tribal"`, `"none-required"` | Metals often require tribal review |
| `care:notes` | Cultural / ethical notes | Required for ceramics, metals |
| `care:visibility_rules` | `"h3-only"`, `"no-exact-points"` | No precise provenience ever allowed |

### ✔ STAC Extensions Required

- **Projection (`proj`)**  
- **Versioning (`version`)**  
- **Checksum (`checksum`)**  
- **Scientific Metadata (`sci`)**  
- **KFM Archaeology Extension (`kfm`)**  
- **CARE Cultural Safety Extension (`care`)**

---

## 📄 Example STAC Item — Lithics

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "flint-hills-lithics-v1",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[/* generalized */]]
  },
  "properties": {
    "kfm:phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "kfm:provenance": "../../provenance/flint-hills-lithics-v1.json"
  },
  "assets": {
    "data": {
      "href": "../../inventories/flint-hills-lithics-v1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "../collections/lithics.json"
    }
  ]
}
~~~

---

## 📄 Example STAC Item — Ceramics

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "prairie-ceramics-v1",
  "bbox": [-101.9, 37.2, -95.9, 40.2],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[/* generalized */]]
  },
  "properties": {
    "kfm:phase": "Middle Ceramic",
    "care:sensitivity": "generalized",
    "care:notes": "Motif categories filtered for cultural safety.",
    "kfm:provenance": "../../provenance/prairie-ceramics-v1.json"
  },
  "assets": {
    "data": {
      "href": "../../inventories/prairie-ceramics-v1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "../collections/ceramics.json"
    }
  ]
}
~~~

---

## 🧪 Validation Requirements

All STAC Items in this directory must pass:

- STAC JSON schema validation  
- KFM archaeology STAC extension validation  
- CARE cultural sensitivity validation  
- Checksum verification  
- Matching crosswalk with:
  - Inventory file in `inventories/`  
  - Metadata file in `metadata/`  
  - Provenance file in `provenance/`  
  - Collection file in `../collections/`  

Validation workflows located in:

- `docs/analyses/archaeology/validation/`  
- `.github/workflows/artifact-stac-validate.yml`

---

## 📊 STAC Item Index

| STAC Item | Category | Sensitivity | Last Review | Status |
|---|---|---|---|---|
| `flint-hills-lithics-v1.json` | Lithics | generalized | 2025-11 | 🟢 Active |
| `prairie-ceramics-v1.json` | Ceramics | generalized | 2025-10 | 🟢 Active |
| `contact-era-metals-v1.json` | Metals | generalized | 2025-09 | 🟡 Needs Review |
| `fauna-open-v1.json` | Faunal | general | 2025-11 | 🟢 Active |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added full STAC Items index, examples, validation rules, and CARE extensions |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial STAC Item directory creation |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to STAC Catalog](../README.md)

</div>