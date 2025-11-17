---
title: "🌄 Kansas Frontier Matrix — Cultural Landscape Metadata Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/metadata/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-metadata-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Metadata Standard"
intent: "cultural-landscape-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🌄 **Kansas Frontier Matrix — Cultural Landscape Metadata Standards**  
`docs/analyses/archaeology/datasets/cultural-landscapes/metadata/README.md`

**Purpose:**  
Define the **metadata specification** for all cultural landscape datasets within the Kansas Frontier Matrix (KFM).  
These standards apply to:

- Settlement regions  
- Interaction spheres  
- Resource procurement zones  
- Ancient trails & mobility routes  
- Territorial/cultural boundaries (generalized)  
- Environmental/cultural synthesis layers  

This ensures datasets remain compliant with **FAIR+CARE**, **STAC 1.0**, **DCAT 3.0**, **CIDOC-CRM**, **GeoSPARQL**, **PROV-O**, and **MCP-DL v6.3**.

</div>

---

# 📘 Overview

Cultural landscape metadata ensures:

- Ethical representation of cultural geographies  
- Protection of Indigenous sovereignty  
- Spatial generalization of sensitive areas  
- Temporal contextualization of cultural phases  
- Transparent provenance  
- Machine-readability for maps, graph, ETL, and Focus Mode v2  
- Alignment with archaeological terminology & controlled vocabularies  

This directory contains machine-readable metadata JSON files for each dataset under:

- `regions/`  
- `routes/`  
- `interaction-spheres/`  
- `resource-areas/`  
- `stac/`  
- `provenance/`

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/metadata/
├── README.md                          # This file
├── great-bend-aspect-v2.json          # DCAT + CARE + provenance-linked metadata
├── central-plains-exchange-v1.json    # Exchange sphere metadata
├── protohistoric-wichita-v1.json      # Sensitive dataset metadata
├── templates/                         # Metadata templates (STAC-aware)
└── schemas/                           # Validators for metadata files
~~~

---

# 📦 Required Metadata Components

Cultural landscape metadata files must include:

---

## ✔ DCAT 3.0 Fields

| Field | Description |
|---|---|---|
| `dct:title` | Dataset name |
| `dct:description` | Human-readable summary |
| `dct:license` | `"CC-BY-4.0"` or `"CC0"` |
| `dct:temporal` | OWL-Time interval |
| `dcat:keyword` | Tags: `"archaeology"`, `"cultural-landscape"`, `"region"`, etc. |
| `dcat:distribution` | Link to STAC Item or GeoJSON |

---

## ✔ KFM Archaeology Metadata

| Field | Description | Example |
|---|---|---|
| `kfm:culture_phase` | Cultural phase or multi-phase range | `"Late Prehistoric"` |
| `kfm:landscape_type` | Region, route, sphere, resource, etc. | `"interaction_sphere"` |
| `kfm:geometry_generalization` | Method used | `"H3-level-6"` |
| `kfm:source` | Data origin | `"Kansas Historical Society"` |
| `kfm:provenance` | PROV-O JSON reference | `"provenance/great-bend-v2.json"` |
| `kfm:schema_version` | Metadata schema version | `"1.0.0"` |

---

## ✔ CARE Cultural Safety Metadata

Cultural landscape datasets must contain:

| Field | Allowed Values | Purpose |
|---|---|---|
| `care:sensitivity` | `general`, `generalized`, `restricted-generalized` | Protects cultural landscapes |
| `care:review` | `faircare`, `tribal`, `none-required` | Indicates review authority |
| `care:notes` | Free text | Cultural safety explanation |
| `care:visibility_rules` | `h3-only`, `no-exact-points`, `polygon-generalized` | Controls public exposure |

**Rules:**

- `"restricted"` is never permitted in public KFM repos  
- `"restricted-generalized"` requires tribal approval  
- Territorial or sacred areas must use **H3-only** visibility  
- No exact boundaries without express tribal consent  

---

## ✔ Provenance Metadata (PROV-O Linked)

Metadata files must link to full provenance logs that describe:

- Data creation  
- GIS transformations  
- Cultural and ethical reviews  
- Generalization processes  
- Assumptions & uncertainties  

Field:

| Field | Description |
|---|---|
| `kfm:provenance` | Path to provenance JSON |

---

## ✔ STAC Alignment Requirements

Metadata must fully align with STAC Item fields:

| Metadata | STAC |
|---|---|
| `dct:title` | `id` or `description` |
| `kfm:culture_phase` | `properties.kfm:culture_phase` |
| `care:sensitivity` | `properties.care:sensitivity` |
| `kfm:provenance` | `properties.kfm:provenance` |
| `dcat:distribution` | `assets.data.href` |

---

# 🌍 Spatial Metadata Requirements

All cultural landscape metadata must include:

| Field | Requirement |
|---|---|
| CRS | EPSG:4326 unless otherwise justified |
| `bbox` | Generalized bounding box |
| Generalization Method | H3 or topological simplification |
| Geometry | No exact sacred/ceremonial polygons |

Generalization rules always apply to protect cultural sovereignty.

---

# 🕰️ Temporal Metadata Requirements

- Must specify earliest and latest likely dates  
- Use ISO 8601 or approximate dates (e.g., `"AD 1300–1600"`)  
- Use OWL-Time compatible structure in DCAT or STAC  
- Provide uncertainty notes where applicable  

---

# 🧪 Integration Into KFM Ecosystem

### **Knowledge Graph**
Nodes:
- `CulturalLandscape`
- `CulturalPhase`
- `Region`
- `ResourceArea`
- `InteractionSphere`

Edges:
- `LOCATED_IN`
- `ASSOCIATED_WITH`
- `OCCURRED_DURING`
- `GENERALIZED_FROM`
- `HAS_PROVENANCE`

### **Story Nodes**
Metadata drives:

- Culture narratives  
- Timeline synchronization  
- Region-based explanations  

### **Focus Mode v2**
Metadata feeds:

- Cultural context summaries  
- Ethics-aware interpretations  
- Provenance chips  

---

# 🧪 Validation Requirements

All metadata must pass:

- `metadata-core-schema.json`  
- `dcat-metadata-schema.json`  
- `care-metadata-schema.json`  
- `provenance-link-schema.json`  
- STAC crosswalk schema  

CI workflows:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  
- `.github/workflows/artifact-stac-validate.yml`  

Validation ensures:

- Cultural safety  
- Spatial generalization  
- Metadata completeness  
- Provenance traceability  
- Ethical compliance  

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Established cultural landscape metadata standards; added DCAT/STAC/CARE requirements |
| v10.0.0 | 2025-11-10 | Landscape Metadata Team | Initial metadata directory scaffold |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Cultural Landscapes](../README.md)

</div>