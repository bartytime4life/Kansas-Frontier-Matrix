---
title: "🗂️ Kansas Frontier Matrix — Artifact Inventory STAC Collections (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-stac-collections-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Collections"
intent: "artifact-inventory-stac-collections"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Artifact Inventory STAC Collections**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/README.md`

**Purpose:**  
Define the **STAC Collection layer** for artifact inventory datasets in the Kansas Frontier Matrix (KFM), enabling structured discovery, validation, FAIR+CARE compliance, and integration across KFM’s analytical, narrative, and visualization systems.

This directory provides **domain-level STAC Collections** grouping artifact datasets by material type (lithic, ceramic, metal), cultural phase, and provenance category.

All collections comply with **STAC 1.0**, **DCAT 3.0**, **PROV-O**, **KFM Archaeology Extensions**, and **CARE metadata standards**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

STAC Collections in this directory provide **high-level grouping metadata** for artifact inventories.  
Each collection acts as:

- A **semantic grouping node** for KFM’s STAC tree  
- A **source-of-truth for cultural + material categories**  
- A **FAIR+CARE governance checkpoint**  
- A **machine-readable metadata aggregator**  
- A **root reference** for artifact-specific STAC Items located in `../items/`

Collections support:

- Neo4j Knowledge Graph population  
- Story Node linking (material-culture narratives)  
- Focus Mode v2 contextual reasoning  
- Notebook-based analysis pipelines  
- MapLibre/Cesium visualization metadata inheritance  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/
├── README.md                           # This file
├── artifact-inventories.json           # Root collection for all artifact inventories
├── lithics.json                        # Lithic artifact collection
├── ceramics.json                       # Ceramic artifact collection
├── metals.json                         # Metal + protohistoric artifact collection
├── faunal.json                         # Public-domain faunal dataset collection
└── templates/                          # Collection template files and schemas
~~~

---

## 🧭 Required Structure for All STAC Collections

Every STAC Collection MUST include:

### ✔ Core Collection Fields

| Field | Description |
|---|---|
| `id` | Unique collection identifier |
| `type` | `"Collection"` |
| `stac_version` | `"1.0.0"` |
| `description` | Summary of dataset group |
| `license` | SPDX identifier |
| `extent.spatial` | Generalized BBOX |
| `extent.temporal` | OWL-Time start/end |
| `links` | Self, root, items |

### ✔ Collection-Level KFM Extensions (`kfm:*`)

| Field | Description |
|---|---|
| `kfm:material_class` | `"lithic"`, `"ceramic"`, `"metal"`, `"faunal"` |
| `kfm:domain` | `"archaeology:artifact-inventories"` |
| `kfm:review_cycle` | `"Biannual"` |
| `kfm:provenance_summary` | High-level lineage overview |

### ✔ CARE Metadata

| Field | Allowed Values |
|---|---|
| `care:sensitivity` | `general`, `generalized` |
| `care:review` | `"faircare"`, `"tribal"`, `"none-required"` |
| `care:notes` | Explanation of cultural treatment |

---

## 📚 Collection Descriptions

### **artifact-inventories.json** (Root Collection)
The master collection linking:

- All lithic datasets  
- All ceramic datasets  
- All metal/protohistoric datasets  
- All PD faunal datasets  

Spatial Extent: Entire Kansas region (generalized).  
Temporal Extent: Paleoindian → Historic.

---

### **lithics.json**
Includes all public-domain lithic artifact inventories.  
Metadata includes:

- Raw material types  
- Tool categories (projectile point, scraper, core, etc.)  
- Phase attribution  
- H3 generalized spatial coverage  

---

### **ceramics.json**
Includes:

- Ceramic sherd inventories  
- Motif categories (generalized for cultural safety)  
- Temporal phase distributions  
- Generalized site categories  

Requires **CARE-sensitive motif filtering**.

---

### **metals.json**
Includes:

- Protohistoric contact-era metal artifacts  
- European trade materials  
- Tool/weapon fragments (non-sensitive)  

Requires **tribal cultural review** for any metal artifacts associated with contact-era sites.

---

### **faunal.json**
Includes:

- Open-access zooarchaeological datasets  
- Pleistocene/Holocene PD faunal inventories  

Must exclude **sacred species** and any fauna associated with restricted archaeological contexts.

---

## 🧪 Validation Requirements

All STAC Collections MUST pass:

- STAC 1.0 Collection schema validation  
- KFM Archaeology STAC extension validation  
- CARE metadata validation  
- License verification  
- Temporal consistency checks  
- Spatial generalization (H3) verification  
- Cross-referencing with STAC Items in `../items/`

---

## 🧩 Example STAC Collection (Lithics)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "lithics",
  "description": "Public-domain lithic artifacts for prehistoric Kansas regions.",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": { "bbox": [[-102.1, 37.0, -94.6, 40.1]] },
    "temporal": { "interval": [["1200-01-01T00:00:00Z", "1500-01-01T00:00:00Z"]] }
  },
  "links": [],
  "kfm:material_class": "lithic",
  "kfm:domain": "archaeology:artifact-inventories",
  "kfm:review_cycle": "Biannual",
  "care:sensitivity": "general",
  "care:review": "faircare",
  "care:notes": "All lithic data generalized to H3 and culturally reviewed."
}
~~~

---

## 📊 Collection Index

| Collection File | Category | Status | Last Review |
|---|---|---|---|
| `artifact-inventories.json` | Root Collection | 🟢 Active | 2025-11 |
| `lithics.json` | Lithics | 🟢 Active | 2025-11 |
| `ceramics.json` | Ceramics | 🟢 Active | 2025-10 |
| `metals.json` | Metals | 🟡 Needs Review | 2025-09 |
| `faunal.json` | Faunal | 🟢 Active | 2025-11 |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created artifact STAC Collection catalog; added metadata rules, CARE requirements, and validation workflows |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial STAC Collection directory setup |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Artifact STAC Catalog](../README.md)

</div>