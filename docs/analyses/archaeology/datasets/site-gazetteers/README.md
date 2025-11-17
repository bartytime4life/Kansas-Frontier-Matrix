---
title: "📍 Kansas Frontier Matrix — Site Gazetteer Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/site-gazetteers/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-site-gazetteers-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Category"
intent: "archaeology-site-gazetteers"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📍 **Kansas Frontier Matrix — Archaeological Site Gazetteers**  
`docs/analyses/archaeology/datasets/site-gazetteers/README.md`

**Purpose:**  
Define, index, and govern all **archaeological site gazetteer datasets** used in the Kansas Frontier Matrix (KFM).  
Site gazetteers provide **generalized**, FAIR+CARE–aligned references for:

- Prehistoric, protohistoric, and historic site locations  
- Cultural-phase place associations  
- Spatial units for analysis (H3 grids, generalized centroids)  
- Focus Mode v2 entity grounding  
- Story Node map anchors  
- Archaeological landscape reconstruction  

Only **generalized, open-license, non-restricted** site information is permitted.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

Site gazetteers in KFM include:

- Generalized archaeological site coordinates (H3 grid only)  
- Public-domain or academic registry sites  
- Tribal-approved generalized cultural locations  
- GNIS-linked features relevant to archaeological interpretation  
- Gazetteer-style entries describing cultural phases, site types, and confidence levels  

These datasets **do not** include:

- Precise coordinates of protected or sensitive sites  
- Burial locations  
- Ceremonial landscapes  
- Restricted tribal heritage data  
- Locational metadata obtained under confidentiality  

All spatial precision is reduced using **H3 level 5–7**, depending on sensitivity.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/site-gazetteers/
├── README.md                          # This file
├── gazetteers/                        # Cleaned, generalized site lists
├── stac/                              # STAC Items & Collections
├── metadata/                          # DCAT + CARE metadata
└── provenance/                        # PROV-O lineage logs
~~~

---

## 🧭 Gazetteer Dataset Categories

| Category | Description | Allowed | Notes |
|---|---|---|---|
| **Public-Domain Site Lists** | GNIS + PD archaeological site records | ✅ | Must be generalized |
| **Academic Gazetteers (PD)** | University research gazetteers (open-license) | ✅ | Requires citation |
| **Tribal-Reviewed Generalized Locations** | Sites approved for high-level public display | ⚠️ | Must follow tribal guidance |
| **Historic Sites** | Public historic register data | ✅ | Usually low sensitivity |
| **Cultural Phase Anchors** | Canonical sites tied to cultural periods | ⚠️ | Must be generalized; no coordinates |

Forbidden categories:

- Restricted site databases  
- Confidential site files  
- Raw survey points or high-precision coordinates  
- Sensitive ceremonial site information  

---

## 📦 Required Metadata (All Gazetteers)

### ✔ STAC 1.0 Item Requirements

| Field | Description |
|---|---|
| `id` | Gazetteer dataset ID |
| `bbox` | H3-generalized bounding box |
| `geometry` | Generalized polygons or centroids |
| `properties.kfm:site_type` | e.g., `"village"`, `"camp"`, `"resource"`, `"mound"` |
| `care:sensitivity` | `"generalized"`, `"restricted-generalized"` |
| `assets` | URLs to gazetteer files |
| `kfm:provenance` | Processing lineage reference |

### ✔ DCAT 3.0 Metadata

| Field | Example |
|---|---|
| `dct:title` | "Kansas Archaeological Gazetteer (Generalized)" |
| `dct:license` | `"CC-BY 4.0"` |
| `dcat:distribution` | Link to generalized site list |
| `dct:temporal` | Cultural/historic periods linked to sites |
| `dcat:keyword` | `["archaeology", "gazetteer", "site"]` |

### ✔ CARE Requirements

- Coordinates generalized to H3  
- Cultural roles documented  
- Tribal review if applicable  
- Culturally sensitive sites marked `"restricted"` even when generalized  
- Avoid colonial framing (“discovery”, “primitive”, etc.)

---

## 🧪 Data Preparation Requirements

All site gazetteers must:

- Use **standard schema fields**  
  - `site_id`, `name`, `culture_phase`, `site_type`, `location_h3`, `confidence_level`, `sources`
- Include **temporal data** (OWL-Time)
- Provide full **citation and provenance**
- Remove or generalize any sensitive descriptors
- Include shapefiles/GeoJSON only in generalized form
- Validate against:
  - CIDOC-CRM for cultural place entities  
  - STAC schema for spatial representation  
  - CARE schema for sensitivity handling  

Generalization rules:

- All sensitive coordinates → convert to H3(level 5–7)  
- Sites inside tribal boundaries require review  
- No raw point locations in any dataset  

---

## 🛰️ Integration Into KFM Systems

### **Knowledge Graph (Neo4j)**

Gazetteers generate:

Nodes:  
- `Site`  
- `CulturalPhase`  
- `PlaceName`  
- `LandscapeUnit`  

Relationships:  
- `LOCATED_AT` (via H3 region)  
- `BELONGS_TO`  
- `ASSOCIATED_WITH`  
- `MENTIONED_IN` (for documents)  

### **Story Nodes**
Gazetteers provide:

- Geographic anchors  
- Cultural timeline placement  
- High-level summaries for prehistoric/historic phases  

### **Focus Mode v2**
Gazetteers support:

- Entity grounding  
- Spatial filtering  
- Cultural context statements  
- CARE tone guarantees  

---

## 📊 Dataset Index

| Dataset | Category | Location | Status | Last Review | Notes |
|---|---|---|---|---|---|
| `gnis/archaeology-gnis-v1` | Public-Domain List | `gazetteers/` | 🟢 Active | 2025-11 | GNIS-linked features curated |
| `academic/open-kansas-sites-v1` | Academic PD | `gazetteers/` | 🟢 Active | 2025-10 | Cultural phases added |
| `tribal/generalized-list-v1` | Tribal-Reviewed | `gazetteers/` | 🟡 Needs Review | 2025-09 | Awaiting updated consent policy |
| `historic/registered-sites-v1` | Historic Sites | `gazetteers/` | 🟢 Active | 2025-11 | Public register compliant |

---

## 🧠 Example STAC Item (Generalized Archaeological Gazetteer)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "kfm-site-gazetteer-v1",
  "bbox": [-101.2, 37.4, -95.7, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[/* generalized */]]
  },
  "properties": {
    "kfm:site_type": "village",
    "kfm:culture_phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "kfm:provenance": "provenance/kfm-site-gazetteer-v1.json"
  },
  "assets": {
    "gazetteer": {
      "href": "https://example.com/gazetteers/kansas_generalized_sites_v1.csv",
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
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created site gazetteer dataset index; added CARE rules, STAC/DCAT requirements, and KFM integration |
| v10.0.0 | 2025-11-10 | Archaeology Dataset Team | Initial directory structure + definitions |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Datasets](../README.md)

</div>