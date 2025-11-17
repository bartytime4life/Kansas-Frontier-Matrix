---
title: "🏺 Kansas Frontier Matrix — Artifact Inventories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-artifact-inventories-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Category"
intent: "archaeology-artifact-inventories"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Artifact Inventories**  
`docs/analyses/archaeology/datasets/artifact-inventories/README.md`

**Purpose:**  
Document, index, and govern the **public-domain archaeological artifact inventories** used in the Kansas Frontier Matrix (KFM), ensuring that all datasets are **FAIR+CARE aligned**, **ethically handled**, **culturally respectful**, and **compatible with KFM’s metadata, graph, and visualization pipelines**.

Artifact inventories support:

- Cultural landscape reconstruction  
- Chronological phase modeling  
- Material culture classification  
- AI-assisted pattern recognition  
- Story Node generation & Focus Mode v2 summaries  

Only **public-domain or openly licensed** artifact datasets are permitted.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

This directory contains artifact inventory datasets that have passed:

- **Scientific validation** (classification standards, methods transparency)  
- **Cultural validation** (CARE-compliant; excludes restricted materials)  
- **Metadata validation** (STAC, DCAT, CIDOC-CRM mapping)  
- **Spatial/temporal validation** (generalized coordinates, OWL-Time coverage)  

Prohibited datasets include:

- Human remains or funerary objects  
- Sacred or restricted ceremonial items  
- Unprovenanced artifacts  
- Culturally sensitive tribal belongings  
- Exact provenience data for protected sites  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/
├── README.md                           # This file
├── inventories/                        # Cleaned + validated artifact tables
├── stac/                               # STAC Items/Collections for artifact datasets
├── metadata/                           # DCAT + CARE metadata
└── provenance/                         # PROV-O lineage & processing logs
~~~

---

## 🧭 Artifact Inventory Categories

| Category | Description | Allowed | Notes |
|---|---|---|---|
| **Lithics** | Chipped stone, ground stone, debitage | ✅ | Public-domain lithic catalogs only |
| **Ceramics** | Sherds, vessel types, decorative motifs | ✅ | Typology data must not expose restricted tribal knowledge |
| **Faunal Remains (PD only)** | Open-source zooarchaeological datasets | ⚠️ | Must not include sacred species where restricted |
| **Metal Artifacts** | Trade metals, tools, hardware | ✅ | Provenance must be verifiable |
| **Protohistoric Items** | Contact-era artifacts | ⚠️ | Must undergo tribal review |
| **Misc. Material Culture** | Beads, ornaments, tools | ⚠️ | Only when confirmed public-domain / open-license |

Excluded categories: funerary goods, human remains, ritual objects, or anything requiring restricted access.

---

## 📦 Required Metadata (All Artifact Inventories)

Each inventory **MUST** have:

### ✔ STAC Item (Mandatory)
Fields:

| Field | Description |
|---|---|
| `id` | Dataset identifier |
| `assets.data.href` | Artifact dataset file |
| `properties.kfm:phase` | Cultural/temporal phase |
| `care:sensitivity` | Always `general` or `restricted-generalized` |
| `bbox` | H3-generalized site spatial extent |

### ✔ DCAT Dataset (Mandatory)

| Field | Description |
|---|---|
| `dct:title` | Name of artifact inventory |
| `dct:license` | License (PD or CC-BY required) |
| `dcat:distribution` | File download or repository reference |
| `dct:temporal` | Occupation or cultural phase dates |

### ✔ PROV-O Provenance

Every dataset must include:

- Original source (museum, academic archive, PD repository)  
- Processing steps  
- Classification methods  
- Version history  
- Analyst + review cycle  

---

## 🛡️ Cultural Safety (FAIR+CARE)

Artifact datasets must respect:

- **Authority to Control** — No tribal-restricted materials  
- **Responsible Use** — Avoid sensationalizing or decontextualizing cultural objects  
- **Ethics** — No objectification, exploitation, or colonial framing  
- **Collective Benefit** — Data serves educational, preservation, or research goals  

Sensitive coordinates MUST be generalized using **H3 levels 5–7**.

Any dataset flagged as **C4 (Ethics)** or **C2 (Authority to Control)** requires tribal council review before inclusion.

---

## 🧪 Data Preparation Requirements

Each inventory must:

- Be cleaned into standardized schema fields  
- Use controlled vocabularies for material, type, decoration, cultural phase  
- Reference classification authorities (e.g., Wedel, Lehmer, Strong)  
- Use **UUIDs** for artifact IDs  
- Provide **temporal bounding** (e.g., `1200–1450 CE`)  
- Remove any provenance that reveals restricted site locations  
- Include column-level documentation  

---

## 🛰️ Integration Into KFM (Pipelines & Graph)

Artifact datasets map into KFM through:

### **Knowledge Graph (Neo4j)**  
Nodes created:

- `Artifact`
- `ArtifactType`
- `Material`
- `Culture`
- `OccupationPhase`
- `Site` (generalized)

Relationships:

- `BELONGS_TO`  
- `FOUND_AT` (H3 region)  
- `ASSOCIATED_WITH`  
- `DATED_TO`  

### **Story Nodes & Focus Mode v2**

Artifact inventories feed:

- Cultural-phase Story Nodes  
- Material-culture timelines  
- Focus Mode explanations linking artifacts to settlement patterns  

All AI summaries require **tone and cultural review**.

### **Map Layers**

Artifact visualizations (generalized) include:

- H3 artifact-density grids  
- Material distributions  
- Temporal spread maps  

---

## 📊 Artifact Inventory Index

| Dataset | Category | Location | Status | Last Review | Notes |
|---|---|---|---|---|---|
| `lithics/flint-hills-lithics-v1` | Lithics | `inventories/` | 🟢 Active | 2025-11 | PD dataset |
| `ceramics/prairie-ceramics-v1` | Ceramics | `inventories/` | 🟢 Active | 2025-10 | Decoration categories validated |
| `faunal/fauna-kansas-v1` | Faunal | `inventories/` | 🟡 Needs Review | 2025-09 | Verify sacred species exclusions |
| `protohistoric/contact-era-v1` | Protohistoric | `inventories/` | 🔴 Hold | Pending tribal review |

---

## 🧠 Example STAC Item (Artifact Inventory)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "artifact-inventory-flint-hills-lithics-v1",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "properties": {
    "kfm:phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "datetime": null
  },
  "assets": {
    "data": {
      "href": "https://example.com/artifacts/flint_hills_lithics_v1.csv",
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
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created artifact inventories index; added CARE safeguards, metadata rules, and KFM graph/visualization integration details |
| v10.0.0 | 2025-11-10 | Archaeology Dataset Team | Initial structure outline |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Datasets](../README.md)

</div>