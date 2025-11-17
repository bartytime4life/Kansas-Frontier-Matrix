---
title: "📑 Kansas Frontier Matrix — Artifact Inventory Metadata Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/metadata/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-inventory-metadata-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Metadata Standard"
intent: "artifact-inventory-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Artifact Inventory Metadata Standards**  
`docs/analyses/archaeology/datasets/artifact-inventories/metadata/README.md`

**Purpose:**  
Define the complete **metadata specification** for all artifact inventory datasets within the Kansas Frontier Matrix (KFM).  
Ensures full alignment with **FAIR+CARE**, **STAC 1.0**, **DCAT 3.0**, **CIDOC-CRM**, **GeoSPARQL**, **ISO 19115**, and **MCP-DL v6.3**.

Metadata in this directory supports:

- Neo4j graph ingestion  
- Story Node and Focus Mode v2 generation  
- Archaeological visualization (MapLibre + Cesium)  
- Predictive modeling and cultural-phase reconstructions  
- Artifact classification reproducibility and provenance traceability

Only **public-domain**, **open-license**, or **tribally approved** inventories may be represented here.

</div>

---

## 📘 Overview

Each metadata file in this directory provides machine-readable description, provenance, and cultural safety fields for:

- Lithic datasets  
- Ceramic datasets  
- Metal/protohistoric datasets  
- Faunal (PD-only) datasets  
- Any additional open-access artifact tables  

No sensitive, culturally restricted, or non-consented artifact information is allowed.

Metadata is stored as **JSON-LD, DCAT 3.0**, and **STAC 1.0** companion files.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/metadata/
├── README.md                                # This file
├── flint-hills-lithics-v1.json              # DCAT + STAC metadata
├── prairie-ceramics-v1.json                 # Cultural-phase ceramic metadata
├── contact-era-metals-v1.json               # Protohistoric metals metadata (pending review)
├── fauna-open-v1.json                       # Open PD faunal metadata
└── schemas/                                 # JSON schemas for metadata validation
~~~

---

## 📦 Required Metadata Components

Every metadata file MUST contain the following three layers:

---

### ✔ 1. **DCAT 3.0 Dataset Metadata**

| Field | Description | Example |
|---|---|---|  
| `dct:title` | Dataset title | `"Flint Hills Lithic Inventory v1"` |
| `dct:description` | Summary of dataset | `"Public-domain lithic dataset, generalized to H3"` |
| `dct:license` | SPDX code | `"CC-BY-4.0"` |
| `dct:creator` | Source institution | `"WSU Open Collections"` |
| `dct:temporal` | OWL-Time interval | `"1200–1400 CE"` |
| `dcat:distribution` | File location | `"inventories/flint-hills-lithics-v1.csv"` |
| `dcat:keyword` | Tags | `["lithic", "archaeology", "inventory"]` |

---

### ✔ 2. **STAC 1.0 Item Metadata**

Required fields:

| STAC Field | Description | Example |
|---|---|---|
| `id` | Unique dataset ID | `"flint-hills-lithics-v1"` |
| `stac_version` | `"1.0.0"` | Required |
| `bbox` | H3 generalized bounding box | `[-101.2, 37.5, -95.4, 40.1]` |
| `geometry` | Generalized point/multipoint | `MultiPoint` |
| `properties.datetime` | If known | `null` |
| `properties.kfm:phase` | Cultural-phase name | `"Late Prehistoric"` |
| `assets.data.href` | Inventory file | `"inventories/flint-hills-lithics-v1.csv"` |
| `proj:*` | CRS, transform | Included |
| `kfm:provenance` | Provenance file reference | `"provenance/flint-hills-lithics-v1.json"` |

---

### ✔ 3. **CARE Cultural Safety Metadata**

All artifact metadata MUST include:

| CARE Field | Description | Allowed Values |
|---|---|---|
| `care:sensitivity` | Sensitivity class | `general`, `generalized`, `restricted-generalized` |
| `care:notes` | Cultural context notes | Free text |
| `care:review` | Review authority | `"faircare"`, `"tribal"`, `"none-required"` |
| `care:visibility_rules` | Visibility constraints | `"h3-only"`, `"no-exact-points"` |

Forbidden:

- `"restricted"` artifacts  
- Precise provenience or excavation unit references  
- Human remains or funerary artifacts  
- Sacred or ceremonial items  

---

## 🧪 Validation Requirements

All metadata must pass:

- **STAC JSON schema validation**  
- **DCAT schema validation**  
- **KFM internal metadata linter**  
- **CARE sensitivity and narrative review**  
- **Checksum verification**  
- **Crosswalk alignment** with:  
  - Story Node schema  
  - Focus Mode context model  
  - Knowledge graph entity definitions  

Validation workflows defined in:

- `docs/analyses/archaeology/validation/`  
- `.github/workflows/artifact-metadata-validate.yml`

---

## 🛰️ Integration Into the KFM Ecosystem

Metadata files feed:

### **Neo4j Knowledge Graph**
- Entities: `Artifact`, `Material`, `CulturalPhase`, `GeneralizedSite`  
- Relationships inferred from metadata keys  

### **Story Nodes**
- Cultural-phase narratives  
- Material culture summaries  
- Phase timelines  

### **Focus Mode v2**
- Artifact interpretations  
- Bias-free summaries  
- Provenance chips  

### **Visualization**
- H3 artifact-density maps  
- Temporal distribution overlays  

---

## 📄 Example Metadata Snippet

~~~json
{
  "dct:title": "Flint Hills Lithic Inventory v1",
  "dct:description": "Generalized lithic artifact dataset, culturally reviewed.",
  "dct:license": "CC-BY-4.0",
  "dcat:distribution": "inventories/flint-hills-lithics-v1.csv",
  "dct:temporal": "1200–1400 CE",
  "dcat:keyword": ["lithic", "archaeology", "inventory"],

  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "flint-hills-lithics-v1",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "geometry": { "type": "MultiPoint", "coordinates": [] },
  "properties": {
    "kfm:phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "kfm:provenance": "provenance/flint-hills-lithics-v1.json"
  },
  "assets": {
    "data": {
      "href": "inventories/flint-hills-lithics-v1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created metadata standards for artifact inventories; added STAC/DCAT/CARE rules; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial structure and baseline metadata guidance |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Artifact Inventories](../README.md)

</div>